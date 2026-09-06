#!/usr/bin/env python3
"""Deterministically audit the 2026-09-06 Veena MIDI pilot."""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import struct
from pathlib import Path

NOTE_NAMES = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")


def read_vlq(data: bytes, index: int) -> tuple[int, int]:
    value = 0
    while True:
        byte = data[index]
        index += 1
        value = (value << 7) | (byte & 0x7F)
        if byte < 0x80:
            return value, index


def note_name(number: int) -> str:
    return f"{NOTE_NAMES[number % 12]}{number // 12 - 1}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_midi(path: Path) -> dict:
    data = path.read_bytes()
    if data[:4] != b"MThd":
        raise ValueError(f"Not a Standard MIDI File: {path}")
    header_length = struct.unpack(">I", data[4:8])[0]
    midi_format, track_count, division = struct.unpack(">HHH", data[8:14])
    if division & 0x8000:
        raise ValueError("SMPTE time division is unsupported")
    if header_length < 6 or 8 + header_length > len(data):
        raise ValueError("Invalid MIDI header length")
    header_extra = data[14 : 8 + header_length]
    position = 8 + header_length
    tracks = []

    for track_index in range(track_count):
        if data[position : position + 4] != b"MTrk":
            raise ValueError(f"Missing MTrk header at track {track_index}")
        position += 4
        track_length = struct.unpack(">I", data[position : position + 4])[0]
        position += 4
        track_data = data[position : position + track_length]
        position += track_length

        index = 0
        tick = 0
        running_status = None
        active: dict[tuple[int, int], list[tuple[int, int]]] = {}
        notes = []
        programs = []
        metadata = []
        raw_events = []
        track_name = ""
        event_index = 0
        end_of_track_tick = None

        while index < len(track_data):
            delta, index = read_vlq(track_data, index)
            tick += delta
            status = track_data[index]
            if status < 0x80:
                if running_status is None:
                    raise ValueError("Running status without previous status")
                status = running_status
            else:
                index += 1
                if status < 0xF0:
                    running_status = status

            if status == 0xFF:
                meta_type = track_data[index]
                index += 1
                length, index = read_vlq(track_data, index)
                payload = track_data[index : index + length]
                if len(payload) != length:
                    raise ValueError(f"Truncated meta event in track {track_index}")
                index += length
                raw_events.append({
                    "event_index": event_index,
                    "tick": tick,
                    "type": "meta",
                    "meta_type": meta_type,
                    "payload_hex": payload.hex(),
                })
                if meta_type == 0x03:
                    track_name = payload.decode("utf-8", "replace")
                if meta_type == 0x51 and len(payload) == 3:
                    microseconds = int.from_bytes(payload, "big")
                    metadata.append({"tick": tick, "type": "tempo_bpm", "value": 60_000_000 / microseconds})
                elif meta_type == 0x58 and len(payload) >= 2:
                    metadata.append({"tick": tick, "type": "time_signature", "value": [payload[0], 2 ** payload[1]]})
                elif meta_type == 0x59 and len(payload) >= 2:
                    metadata.append({"tick": tick, "type": "key_signature", "value": [int.from_bytes(payload[:1], "big", signed=True), payload[1]]})
                if meta_type == 0x2F:
                    if payload:
                        raise ValueError(
                            f"Track {track_index} has malformed end-of-track payload"
                        )
                    end_of_track_tick = tick
                    if index != len(track_data):
                        raise ValueError(
                            f"Track {track_index} contains {len(track_data) - index} byte(s) after end-of-track"
                        )
                    break
            elif status in (0xF0, 0xF7):
                length, index = read_vlq(track_data, index)
                payload = track_data[index : index + length]
                if len(payload) != length:
                    raise ValueError(f"Truncated SysEx event in track {track_index}")
                index += length
                raw_events.append({
                    "event_index": event_index,
                    "tick": tick,
                    "type": "sysex",
                    "status": status,
                    "payload_hex": payload.hex(),
                })
            else:
                event_type = status & 0xF0
                channel = status & 0x0F
                if event_type in (0xC0, 0xD0):
                    first = track_data[index]
                    index += 1
                    raw_event = {
                        "event_index": event_index,
                        "tick": tick,
                        "type": "program_change" if event_type == 0xC0 else "channel_pressure",
                        "status": status,
                        "channel": channel,
                        "data": [first],
                    }
                    raw_events.append(raw_event)
                    if event_type == 0xC0:
                        programs.append({"tick": tick, "channel": channel, "program": first})
                else:
                    first, second = track_data[index], track_data[index + 1]
                    index += 2
                    if event_type == 0x90 and second > 0:
                        active.setdefault((channel, first), []).append((tick, second, status, event_index))
                    elif event_type == 0x80 or (event_type == 0x90 and second == 0):
                        queue = active.get((channel, first), [])
                        if queue:
                            start, velocity, on_status, on_index = queue.pop(0)
                            notes.append(
                                {
                                    "start_tick": start,
                                    "duration_tick": tick - start,
                                    "pitch": first,
                                    "pitch_name": note_name(first),
                                    "velocity": velocity,
                                    "channel": channel,
                                    "start_quarters": start / division,
                                    "duration_quarters": (tick - start) / division,
                                    "bar_4_4": int((start / division) // 4) + 1,
                                    "beat_4_4": (start / division) % 4 + 1,
                                }
                            )
                            raw_events.append({
                                "event_index": on_index,
                                "release_event_index": event_index,
                                "tick": start,
                                "release_tick": tick,
                                "type": "note_on_note_off",
                                "on_status": on_status,
                                "off_status": status,
                                "channel": channel,
                                "pitch": first,
                                "on_velocity": velocity,
                                "off_velocity": second,
                            })
                        else:
                            raw_events.append({
                                "event_index": event_index,
                                "tick": tick,
                                "type": "note_off",
                                "status": status,
                                "channel": channel,
                                "data": [first, second],
                            })
                    else:
                        event_names = {
                            0xA0: "polyphonic_key_pressure",
                            0xB0: "control_change",
                            0xE0: "pitch_bend",
                        }
                        raw_events.append({
                            "event_index": event_index,
                            "tick": tick,
                            "type": event_names.get(event_type, f"channel_0x{event_type:02x}"),
                            "status": status,
                            "channel": channel,
                            "data": [first, second],
                        })
            event_index += 1

        if end_of_track_tick is None:
            raise ValueError(f"Track {track_index} is missing end-of-track event")

        for (channel, pitch), pending in active.items():
            for start, velocity, status, on_index in pending:
                raw_events.append({
                    "event_index": on_index,
                    "tick": start,
                    "type": "note_on",
                    "status": status,
                    "channel": channel,
                    "data": [pitch, velocity],
                })

        notes.sort(key=lambda note: (note["start_tick"], note["pitch"], note["duration_tick"], note["velocity"]))
        tracks.append(
            {
                "index": track_index,
                "name": track_name,
                "notes": notes,
                "program_changes": programs,
                "metadata": metadata,
                "chunk_length": track_length,
                "end_of_track_tick": end_of_track_tick,
                "raw_events": sorted(raw_events, key=lambda event: event["event_index"]),
            }
        )

    if position != len(data):
        raise ValueError(
            f"MIDI track count mismatch: header declares {track_count} track(s), "
            f"but {len(data) - position} trailing byte(s) remain"
        )

    return {
        "path": path.name,
        "sha256": sha256(path),
        "size_bytes": len(data),
        "format": midi_format,
        "ticks_per_quarter": division,
        "track_count": track_count,
        "header_length": header_length,
        "header_extra_hex": header_extra.hex(),
        "tracks": tracks,
    }


def canonical(value):
    """Return a stable hashable form without discarding decoded MIDI fields."""
    if isinstance(value, dict):
        return tuple((key, canonical(item)) for key, item in sorted(value.items()))
    if isinstance(value, list):
        return tuple(canonical(item) for item in value)
    return value


def uncanonical(value):
    if isinstance(value, tuple) and all(isinstance(item, tuple) and len(item) == 2 and isinstance(item[0], str) for item in value):
        return {key: uncanonical(item) for key, item in value}
    if isinstance(value, tuple):
        return [uncanonical(item) for item in value]
    return value


def is_target_event(
    track_index: int,
    event: dict,
    ticks_per_quarter: int,
    end_of_track_tick: int | None = None,
) -> bool:
    if track_index != 1 or event["type"] not in {"note_on_note_off", "note_on", "note_off"}:
        return False
    target_start = 5 * 4 * ticks_per_quarter
    target_end = 7 * 4 * ticks_per_quarter
    if not target_start <= event["tick"] < target_end:
        return False
    # A paired note belongs to the target only when it does not sustain into
    # protected bar 8. A release exactly on the bar-8 boundary closes bar 7.
    if event["type"] == "note_on_note_off":
        return event["release_tick"] <= target_end
    # An unmatched note-on can remain sounding until the track ends, so it is
    # target-safe only when a well-formed EOT closes the track by the boundary.
    if event["type"] == "note_on":
        return end_of_track_tick is not None and end_of_track_tick <= target_end
    return True


def compare(before: dict, after: dict) -> dict:
    track_diffs = []
    protected_changes = 0
    target_changes = 0
    target_removed = 0
    target_added = 0
    header_before = {
        key: before[key] for key in ("format", "ticks_per_quarter", "track_count", "header_length", "header_extra_hex")
    }
    header_after = {
        key: after[key] for key in ("format", "ticks_per_quarter", "track_count", "header_length", "header_extra_hex")
    }
    header_differences = []
    for key in header_before:
        if header_before[key] != header_after[key]:
            header_differences.append({"field": key, "before": header_before[key], "after": header_after[key]})
            protected_changes += 1

    track_count = max(len(before["tracks"]), len(after["tracks"]))
    for track_index in range(track_count):
        before_track = before["tracks"][track_index] if track_index < len(before["tracks"]) else None
        after_track = after["tracks"][track_index] if track_index < len(after["tracks"]) else None
        old_events = before_track["raw_events"] if before_track else []
        new_events = after_track["raw_events"] if after_track else []
        old = collections.Counter(canonical(event) for event in old_events)
        new = collections.Counter(canonical(event) for event in new_events)
        removed = list((old - new).elements())
        added = list((new - old).elements())
        differences = []
        chunk_length_difference = None
        if before_track and after_track and before_track["chunk_length"] != after_track["chunk_length"]:
            chunk_length_difference = {
                "before": before_track["chunk_length"],
                "after": after_track["chunk_length"],
            }
            protected_changes += 1
        for kind, events in (("removed", removed), ("added", added)):
            for encoded in events:
                event = uncanonical(encoded)
                tpq = before["ticks_per_quarter"] if kind == "removed" else after["ticks_per_quarter"]
                source_track = before_track if kind == "removed" else after_track
                quarter = event["tick"] / tpq
                record = {"kind": kind, "bar_4_4": int(quarter // 4) + 1, "beat_4_4": quarter % 4 + 1, "event": event}
                differences.append(record)
                if is_target_event(
                    track_index,
                    event,
                    tpq,
                    source_track.get("end_of_track_tick") if source_track else None,
                ):
                    target_changes += 1
                    if kind == "removed":
                        target_removed += 1
                    else:
                        target_added += 1
                else:
                    protected_changes += 1
        track_diffs.append(
            {
                "track_index": track_index,
                "name": (before_track or after_track)["name"],
                "before_note_count": len(before_track["notes"]) if before_track else 0,
                "after_note_count": len(after_track["notes"]) if after_track else 0,
                "unchanged_event_count": sum((old & new).values()),
                "differences": sorted(differences, key=lambda item: (item["bar_4_4"], item["beat_4_4"], item["kind"])),
                "chunk_length_difference": chunk_length_difference,
                "program_changes_preserved": bool(before_track and after_track and before_track["program_changes"] == after_track["program_changes"]),
            }
        )
    return {
        "protected_event_changes": protected_changes,
        "target_note_event_multiset_differences": target_changes,
        "target_note_events_removed": target_removed,
        "target_note_events_added": target_added,
        "zero_protected_region_leakage": protected_changes == 0,
        "header_differences": header_differences,
        "tracks": track_diffs,
    }


def evaluate_baseline(midi: dict) -> dict:
    tracks = midi["tracks"]
    chord_track = tracks[1]["notes"]
    bass_track = tracks[2]["notes"]
    melody_track = tracks[3]["notes"]

    expected_chords = {
        1: ["A2", "E3", "C4", "B4"],
        2: ["A2", "F3", "C4", "E4"],
        3: ["D3", "F3", "C4", "E4"],
        4: ["E3", "G#3", "D4", "F4"],
        5: ["A2", "E3", "C4", "B4"],
        6: ["D3", "F3", "C4", "E4"],
        7: ["E3", "G#3", "D4", "F4"],
        8: ["A2", "E3", "C4", "E4"],
    }
    actual_chords = collections.defaultdict(list)
    for note in chord_track:
        actual_chords[note["bar_4_4"]].append(note["pitch_name"])
    chord_exact = sum(collections.Counter(actual_chords[bar]) == collections.Counter(expected) for bar, expected in expected_chords.items())

    # Score against the documented chord symbols, not only the exported voicings.
    # Dm9 includes A; E7(b9) includes B even though those degrees were unvoiced.
    chord_pitch_classes = {
        1: {9, 0, 4, 11}, 2: {5, 9, 0, 4}, 3: {2, 5, 9, 0, 4}, 4: {4, 8, 11, 2, 5},
        5: {9, 0, 4, 11}, 6: {2, 5, 9, 0, 4}, 7: {4, 8, 11, 2, 5}, 8: {9, 0, 4},
    }
    roots = {1: 9, 2: 5, 3: 2, 4: 4, 5: 9, 6: 2, 7: 4, 8: 9}
    bass_by_bar = collections.defaultdict(list)
    for note in bass_track:
        bass_by_bar[note["bar_4_4"]].append(note)
    root_ok = []
    inner_ok = []
    beat4_ok = []
    for bar in range(1, 9):
        notes = sorted(bass_by_bar[bar], key=lambda note: note["start_tick"])
        root_ok.append(notes[0]["pitch"] % 12 == roots[bar])
        inner_ok.extend(note["pitch"] % 12 in chord_pitch_classes[bar] for note in notes[1:3])
        if bar < 8:
            target = roots[bar + 1]
            pitch_class = notes[3]["pitch"] % 12
            distance = min((pitch_class - target) % 12, (target - pitch_class) % 12)
            next_notes = sorted(bass_by_bar[bar + 1], key=lambda note: note["start_tick"])
            actual_next_downbeat_is_root = bool(
                next_notes
                and next_notes[0]["beat_4_4"] == 1
                and next_notes[0]["pitch"] % 12 == target
            )
            beat4_ok.append(
                pitch_class in chord_pitch_classes[bar]
                or (distance == 1 and actual_next_downbeat_is_root)
            )
        else:
            beat4_ok.append(notes[3]["pitch"] % 12 in chord_pitch_classes[bar])

    melody_by_bar = collections.defaultdict(list)
    for note in melody_track:
        melody_by_bar[note["bar_4_4"]].append(note)
    non_chord_counts = {
        bar: sum(note["pitch"] % 12 not in chord_pitch_classes[bar] for note in melody_by_bar[bar])
        for bar in range(1, 9)
    }

    return {
        "query_1": {
            "exact_chord_bars": chord_exact,
            "total_bars": 8,
            "exact_note_count": len(chord_track),
            "all_notes_start_on_bar_downbeat": all(note["beat_4_4"] == 1 for note in chord_track),
            "all_notes_last_four_quarters": all(note["duration_quarters"] == 4 for note in chord_track),
        },
        "query_2": {
            "correct_beat_1_roots": sum(root_ok),
            "beat_1_root_opportunities": len(root_ok),
            "correct_beat_2_3_chord_tones": sum(inner_ok),
            "beat_2_3_opportunities": len(inner_ok),
            "valid_beat_4_tones_or_approaches": sum(beat4_ok),
            "beat_4_opportunities": len(beat4_ok),
            "combined_harmonic_positions_correct": sum(root_ok) + sum(inner_ok) + sum(beat4_ok),
            "combined_harmonic_positions_total": 32,
            "combined_harmonic_compliance": (sum(root_ok) + sum(inner_ok) + sum(beat4_ok)) / 32,
            "all_quarter_notes": all(note["duration_quarters"] == 1 for note in bass_track),
            "all_in_requested_range": all(33 <= note["pitch"] <= 52 for note in bass_track),
        },
        "query_3": {
            "note_count": len(melody_track),
            "all_in_requested_range": all(71 <= note["pitch"] <= 81 for note in melody_track),
            "non_chord_events_by_bar": non_chord_counts,
            "bars_meeting_max_one_non_chord_event": sum(value <= 1 for value in non_chord_counts.values()),
            "bars_total": 8,
            "ends_g_sharp_to_a": [note["pitch_name"] for note in melody_track[-2:]] == ["G#5", "A5"],
        },
    }


def evaluate_intervention(after: dict) -> dict:
    chord_by_bar = collections.defaultdict(list)
    bass_by_bar = collections.defaultdict(list)
    melody_by_bar = collections.defaultdict(list)
    for note in after["tracks"][1]["notes"]:
        chord_by_bar[note["bar_4_4"]].append(note["pitch_name"])
    for note in after["tracks"][2]["notes"]:
        bass_by_bar[note["bar_4_4"]].append(note["pitch_name"])
    for note in after["tracks"][3]["notes"]:
        melody_by_bar[note["bar_4_4"]].append(note["pitch_name"])
    bar6_classes = {name.rstrip("-0123456789") for name in chord_by_bar[6]}
    bar7_classes = {name.rstrip("-0123456789") for name in chord_by_bar[7]}
    return {
        "bar_6_chord_notes": chord_by_bar[6],
        "bar_6_is_complete_b_half_diminished_7": bar6_classes == {"B", "D", "F", "A"},
        "bar_7_chord_notes": chord_by_bar[7],
        "bar_7_required_b_flat_7_sharp_11_degrees": ["A#", "D", "G#", "E"],
        "bar_7_has_root": "A#" in bar7_classes,
        "bar_7_has_major_third": "D" in bar7_classes,
        "bar_7_has_minor_seventh": "G#" in bar7_classes,
        "bar_7_has_sharp_11": "E" in bar7_classes,
        "bar_7_functionally_complete": {"A#", "D", "G#", "E"}.issubset(bar7_classes),
        "bar_7_bass_notes_unchanged_and_conflicting": bass_by_bar[7],
        "bar_7_melody_notes_preserved": melody_by_bar[7],
    }


def analyze(before_path: Path, after_path: Path) -> dict:
    """Return the complete deterministic audit for two Veena MIDI exports."""
    before = parse_midi(before_path)
    after = parse_midi(after_path)
    return {
        "schema_version": 1,
        "pilot_date": "2026-09-06",
        "status": "mechanical_single-session_pilot_not_formal_validation",
        "before": before,
        "after": after,
        "baseline_evaluation": evaluate_baseline(before),
        "query_5_intervention": evaluate_intervention(after),
        "comparison": compare(before, after),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--before", type=Path, default=Path("baseline.mid"))
    parser.add_argument("--after", type=Path, default=Path("after_query_5.mid"))
    parser.add_argument("--output", type=Path, default=Path("results.json"))
    args = parser.parse_args()

    results = analyze(args.before, args.after)
    before = results["before"]
    after = results["after"]
    args.output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "before_sha256": before["sha256"],
        "after_sha256": after["sha256"],
        "baseline_evaluation": results["baseline_evaluation"],
        "query_5_intervention": results["query_5_intervention"],
        "comparison": {
            "protected_event_changes": results["comparison"]["protected_event_changes"],
            "target_note_event_multiset_differences": results["comparison"]["target_note_event_multiset_differences"],
            "target_note_events_removed": results["comparison"]["target_note_events_removed"],
            "target_note_events_added": results["comparison"]["target_note_events_added"],
            "zero_protected_region_leakage": results["comparison"]["zero_protected_region_leakage"],
        },
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
