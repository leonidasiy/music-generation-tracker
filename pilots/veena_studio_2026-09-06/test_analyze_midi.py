import copy
import hashlib
import json
import struct
import tempfile
import unittest
from pathlib import Path

from analyze_midi import analyze, compare, evaluate_baseline, parse_midi


HERE = Path(__file__).resolve().parent
BEFORE = HERE / "baseline.mid"
AFTER = HERE / "after_query_5.mid"


def vlq(value):
    encoded = [value & 0x7F]
    value >>= 7
    while value:
        encoded.append(0x80 | (value & 0x7F))
        value >>= 7
    return bytes(reversed(encoded))


def midi_bytes(tracks, midi_format=1, tpq=480, declared_track_count=None, header_extra=b""):
    count = len(tracks) if declared_track_count is None else declared_track_count
    header_payload = struct.pack(">HHH", midi_format, count, tpq) + header_extra
    chunks = [b"MThd" + struct.pack(">I", len(header_payload)) + header_payload]
    for events in tracks:
        payload = b"".join(vlq(delta) + event for delta, event in events)
        chunks.append(b"MTrk" + struct.pack(">I", len(payload)) + payload)
    return b"".join(chunks)


def parse_bytes(data):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "fixture.mid"
        path.write_bytes(data)
        return parse_midi(path)


BASE_EVENTS = [
    (0, b"\xff\x51\x03\x07\xa1\x20"),
    (0, b"\xb0\x07\x64"),
    (0, b"\xd0\x20"),
    (0, b"\xe0\x00\x40"),
    (0, b"\xf0\x02\x01\x02"),
    (0, b"\xff\x2f\x00"),
]


class VeenaMidiAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = analyze(BEFORE, AFTER)

    def test_archived_midi_hashes(self):
        self.assertEqual(
            hashlib.sha256(BEFORE.read_bytes()).hexdigest(),
            "fbeda0e6c2adc6437863cff528197569dd98a408fd5e31f8cebdd34f5d2f1c21",
        )
        self.assertEqual(
            hashlib.sha256(AFTER.read_bytes()).hexdigest(),
            "b9807056666aebd37f0d2613654528010688391662dc0d5455307507f6ae6f78",
        )

    def test_baseline_query_metrics(self):
        q1 = self.result["baseline_evaluation"]["query_1"]
        q2 = self.result["baseline_evaluation"]["query_2"]
        q3 = self.result["baseline_evaluation"]["query_3"]
        self.assertEqual(q1["exact_note_count"], 32)
        self.assertEqual(q1["exact_chord_bars"], 8)
        self.assertEqual(q2["correct_beat_2_3_chord_tones"], 12)
        self.assertEqual(q2["valid_beat_4_tones_or_approaches"], 5)
        self.assertEqual(q2["combined_harmonic_positions_correct"], 23)
        self.assertEqual(q2["combined_harmonic_positions_total"], 32)
        self.assertEqual(q2["combined_harmonic_compliance"], 0.71875)
        self.assertEqual(q3["bars_meeting_max_one_non_chord_event"], 3)
        self.assertEqual(q3["bars_total"], 8)
        self.assertTrue(q3["ends_g_sharp_to_a"])

    def test_query_5_target_and_protection(self):
        q5 = self.result["query_5_intervention"]
        comparison = self.result["comparison"]
        self.assertTrue(q5["bar_6_is_complete_b_half_diminished_7"])
        self.assertFalse(q5["bar_7_has_minor_seventh"])
        self.assertFalse(q5["bar_7_functionally_complete"])
        self.assertEqual(comparison["protected_event_changes"], 0)
        self.assertEqual(comparison["target_note_event_multiset_differences"], 14)
        self.assertEqual(comparison["target_note_events_removed"], 7)
        self.assertEqual(comparison["target_note_events_added"], 7)
        self.assertTrue(comparison["zero_protected_region_leakage"])

    def test_full_chord_symbols_include_unvoiced_d_m9_a_and_e7_flat9_b(self):
        q2 = self.result["baseline_evaluation"]["query_2"]
        self.assertEqual(q2["correct_beat_2_3_chord_tones"], 12)
        self.assertEqual(q2["valid_beat_4_tones_or_approaches"], 5)

    def test_semitone_approach_requires_actual_next_downbeat_root(self):
        baseline = copy.deepcopy(self.result["before"])
        q2 = evaluate_baseline(baseline)["query_2"]
        self.assertEqual(q2["valid_beat_4_tones_or_approaches"], 5)
        bar_3_downbeat = next(
            note for note in baseline["tracks"][2]["notes"]
            if note["bar_4_4"] == 3 and note["beat_4_4"] == 1
        )
        bar_3_downbeat["pitch"] += 2
        changed = evaluate_baseline(baseline)["query_2"]
        self.assertEqual(changed["valid_beat_4_tones_or_approaches"], 4)

    def test_header_format_tpq_and_track_count_changes_are_protected(self):
        base = parse_bytes(midi_bytes([BASE_EVENTS]))
        variants = [
            parse_bytes(midi_bytes([BASE_EVENTS], midi_format=0)),
            parse_bytes(midi_bytes([BASE_EVENTS], tpq=960)),
            parse_bytes(midi_bytes([BASE_EVENTS, [(0, b"\xff\x2f\x00")]])),
        ]
        for variant in variants:
            with self.subTest(variant=(variant["format"], variant["ticks_per_quarter"], variant["track_count"])):
                self.assertGreater(compare(base, variant)["protected_event_changes"], 0)

    def test_extra_tracks_are_compared_and_not_zip_truncated(self):
        base = parse_bytes(midi_bytes([BASE_EVENTS]))
        extra = parse_bytes(midi_bytes([BASE_EVENTS, [(0, b"\xff\x03\x01X"), (0, b"\xff\x2f\x00")]]))
        result = compare(base, extra)
        self.assertGreater(result["protected_event_changes"], 0)
        self.assertEqual(len(result["tracks"]), 2)

    def test_declared_track_count_mismatch_is_rejected(self):
        data = midi_bytes([BASE_EVENTS, [(0, b"\xff\x2f\x00")]], declared_track_count=1)
        with self.assertRaisesRegex(ValueError, "track count"):
            parse_bytes(data)

    def test_meta_controller_pressure_pitch_bend_and_sysex_changes_are_protected(self):
        base = parse_bytes(midi_bytes([BASE_EVENTS]))
        mutations = {
            "tempo/meta": (0, b"\xff\x51\x03\x07\xa1\x21"),
            "controller": (0, b"\xb0\x07\x63"),
            "channel pressure": (0, b"\xd0\x21"),
            "pitch bend": (0, b"\xe0\x01\x40"),
            "SysEx": (0, b"\xf0\x02\x01\x03"),
        }
        for name, replacement in mutations.items():
            events = list(BASE_EVENTS)
            index = {"tempo/meta": 0, "controller": 1, "channel pressure": 2, "pitch bend": 3, "SysEx": 4}[name]
            events[index] = replacement
            with self.subTest(event=name):
                changed = parse_bytes(midi_bytes([events]))
                self.assertGreater(compare(base, changed)["protected_event_changes"], 0)

    def test_track_chunk_length_change_is_protected(self):
        base = parse_bytes(midi_bytes([BASE_EVENTS]))
        changed = copy.deepcopy(base)
        changed["tracks"][0]["chunk_length"] += 1
        result = compare(base, changed)
        self.assertGreater(result["protected_event_changes"], 0)
        self.assertIsNotNone(result["tracks"][0]["chunk_length_difference"])

    def test_bytes_after_end_of_track_are_rejected(self):
        events = list(BASE_EVENTS) + [(0, b"\xb0\x07\x64")]
        with self.assertRaisesRegex(ValueError, "after end-of-track"):
            parse_bytes(midi_bytes([events]))

    def test_missing_end_of_track_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "missing end-of-track"):
            parse_bytes(midi_bytes([BASE_EVENTS[:-1]]))

    def test_unmatched_target_note_on_uses_end_of_track_boundary(self):
        target_start = 5 * 4 * 480
        target_end = 7 * 4 * 480
        before_events = [
            (target_start, b"\x90\x3c\x50"),
            (target_end - target_start + 1, b"\xff\x2f\x00"),
        ]
        after_events = [
            (target_start, b"\x90\x3d\x50"),
            (target_end - target_start + 1, b"\xff\x2f\x00"),
        ]
        before = parse_bytes(midi_bytes([[BASE_EVENTS[-1]], before_events]))
        after = parse_bytes(midi_bytes([[BASE_EVENTS[-1]], after_events]))
        self.assertEqual(before["tracks"][1]["end_of_track_tick"], target_end + 1)
        result = compare(before, after)
        self.assertEqual(result["target_note_event_multiset_differences"], 0)
        self.assertEqual(result["protected_event_changes"], 2)

    def test_paired_target_note_ending_exactly_at_boundary_is_eligible(self):
        target_start = 5 * 4 * 480
        target_end = 7 * 4 * 480
        before_events = [
            (target_start, b"\x90\x3c\x50"),
            (target_end - target_start, b"\x80\x3c\x00"),
            (0, b"\xff\x2f\x00"),
        ]
        after_events = [
            (target_start, b"\x90\x3d\x50"),
            (target_end - target_start, b"\x80\x3d\x00"),
            (0, b"\xff\x2f\x00"),
        ]
        before = parse_bytes(midi_bytes([[BASE_EVENTS[-1]], before_events]))
        after = parse_bytes(midi_bytes([[BASE_EVENTS[-1]], after_events]))
        result = compare(before, after)
        self.assertEqual(result["target_note_event_multiset_differences"], 2)
        self.assertEqual(result["protected_event_changes"], 0)

    def test_target_note_sustaining_past_bar_7_is_protected(self):
        target_tick = 5 * 4 * 480
        base = {
            "format": 1, "ticks_per_quarter": 480, "track_count": 2,
            "header_length": 6, "header_extra_hex": "",
            "tracks": [
                {"name": "", "notes": [], "program_changes": [], "chunk_length": 0, "raw_events": []},
                {"name": "Chords", "notes": [], "program_changes": [], "chunk_length": 1,
                 "raw_events": [{"event_index": 0, "release_event_index": 1,
                                 "tick": target_tick, "release_tick": 8 * 4 * 480,
                                 "type": "note_on_note_off", "on_status": 144,
                                 "off_status": 128, "channel": 0, "pitch": 60,
                                 "on_velocity": 80, "off_velocity": 0}]},
            ],
        }
        changed = copy.deepcopy(base)
        changed["tracks"][1]["raw_events"][0]["pitch"] = 61
        result = compare(base, changed)
        self.assertEqual(result["target_note_event_multiset_differences"], 0)
        self.assertEqual(result["protected_event_changes"], 2)

    def test_real_files_have_only_fourteen_target_raw_note_event_differences(self):
        comparison = compare(parse_midi(BEFORE), parse_midi(AFTER))
        self.assertEqual(comparison["target_note_event_multiset_differences"], 14)
        self.assertEqual(comparison["target_note_events_removed"], 7)
        self.assertEqual(comparison["target_note_events_added"], 7)
        self.assertEqual(comparison["protected_event_changes"], 0)

    def test_checked_in_results_are_reproducible(self):
        checked_in = json.loads((HERE / "results.json").read_text(encoding="utf-8"))
        self.assertEqual(json.loads(json.dumps(self.result)), checked_in)
        with tempfile.TemporaryDirectory() as tmp:
            rendered = Path(tmp) / "results.json"
            rendered.write_text(
                json.dumps(self.result, indent=2, sort_keys=False) + "\n",
                encoding="utf-8",
            )
            self.assertEqual(rendered.read_bytes(), (HERE / "results.json").read_bytes())


if __name__ == "__main__":
    unittest.main()
