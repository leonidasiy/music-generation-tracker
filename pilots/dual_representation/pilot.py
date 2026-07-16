#!/usr/bin/env python3
"""Small paired symbolic/audio feasibility spike.

This is not an implementation of CRVP. It creates controlled data needed to
see whether a later cross-representation validation design is mechanically
possible and where representation-specific artifacts enter.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable

import numpy as np
import pretty_midi
from scipy.io import wavfile
from scipy.signal import find_peaks


def _add_note(inst: pretty_midi.Instrument, pitch: int, start: float, duration: float, velocity: int = 90) -> None:
    inst.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))


def build_piece(corrupt: bool = False) -> pretty_midi.PrettyMIDI:
    """Construct a deterministic 12-bar ABA piece at 120 BPM.

    The corruption changes only B-section pitch content. Duration, note count,
    rhythm, and A sections remain fixed, giving a controlled content edit.
    """
    midi = pretty_midi.PrettyMIDI(initial_tempo=120.0)
    melody = pretty_midi.Instrument(program=0, name="melody")
    bass = pretty_midi.Instrument(program=32, name="bass")
    bar_seconds = 2.0
    quarter = 0.5
    a_pattern = [60, 64, 67, 64]
    b_pattern = [65, 69, 72, 69]
    corrupt_pattern = [61, 63, 66, 70]

    for bar in range(12):
        section_pos = bar % 8
        if bar < 4 or bar >= 8:
            pattern = a_pattern
            root = 48
        else:
            pattern = corrupt_pattern if corrupt else b_pattern
            root = 53 if not corrupt else 49
        start_bar = bar * bar_seconds
        for beat, pitch in enumerate(pattern):
            _add_note(melody, pitch, start_bar + beat * quarter, quarter * 0.82, 96)
            _add_note(bass, root, start_bar + beat * quarter, quarter * 0.9, 62)

    midi.instruments.extend([melody, bass])
    return midi


def _pcp_from_notes(notes: Iterable[pretty_midi.Note]) -> np.ndarray:
    pcp = np.zeros(12, dtype=float)
    for note in notes:
        pcp[note.pitch % 12] += max(note.end - note.start, 0.0) * note.velocity
    total = pcp.sum()
    return pcp / total if total else pcp


def symbolic_features(midi: pretty_midi.PrettyMIDI) -> Dict[str, object]:
    notes = [n for inst in midi.instruments for n in inst.notes]
    duration = midi.get_end_time()
    b_notes = [n for n in notes if 8.0 <= n.start < 16.0]
    return {
        "duration_seconds": float(duration),
        "note_count": len(notes),
        "note_rate_hz": len(notes) / duration,
        "global_pcp": _pcp_from_notes(notes).tolist(),
        "section_b_pcp": _pcp_from_notes(b_notes).tolist(),
    }


def render_audio(midi: pretty_midi.PrettyMIDI, timbre: str = "sine", sample_rate: int = 16000) -> np.ndarray:
    """Render parsed MIDI notes with deterministic sine or harmonic timbre."""
    if timbre not in {"sine", "harmonic"}:
        raise ValueError("timbre must be 'sine' or 'harmonic'")
    duration = midi.get_end_time() + 0.25
    audio = np.zeros(int(np.ceil(duration * sample_rate)), dtype=np.float64)
    partials = [(1, 1.0)] if timbre == "sine" else [(1, 1.0), (2, 0.32), (3, 0.15), (4, 0.08)]

    for inst in midi.instruments:
        gain = 0.34 if inst.name == "melody" else 0.20
        for note in inst.notes:
            start = int(round(note.start * sample_rate))
            end = int(round(note.end * sample_rate))
            n = max(end - start, 1)
            t = np.arange(n) / sample_rate
            freq = 440.0 * 2.0 ** ((note.pitch - 69) / 12.0)
            tone = np.zeros(n, dtype=float)
            for harmonic, amp in partials:
                tone += amp * np.sin(2 * np.pi * freq * harmonic * t)
            attack = max(1, min(int(0.015 * sample_rate), n // 4))
            release = max(1, min(int(0.04 * sample_rate), n // 3))
            env = np.ones(n)
            env[:attack] = np.linspace(0, 1, attack, endpoint=False)
            env[-release:] *= np.linspace(1, 0, release)
            audio[start:end] += gain * (note.velocity / 127.0) * tone * env

    peak = np.max(np.abs(audio))
    if peak:
        audio = 0.92 * audio / peak
    return audio.astype(np.float32)


def _chroma_from_audio(audio: np.ndarray, sample_rate: int, start: float = 0.0, end: float | None = None) -> np.ndarray:
    lo = int(start * sample_rate)
    hi = len(audio) if end is None else min(len(audio), int(end * sample_rate))
    x = np.asarray(audio[lo:hi], dtype=float)
    frame = 2048
    hop = 512
    if len(x) < frame:
        x = np.pad(x, (0, frame - len(x)))
    chroma = np.zeros(12, dtype=float)
    window = np.hanning(frame)
    freqs = np.fft.rfftfreq(frame, 1.0 / sample_rate)
    valid = (freqs >= 40.0) & (freqs <= min(5000.0, sample_rate / 2.0))
    midi_bins = np.rint(69 + 12 * np.log2(np.maximum(freqs[valid], 1e-9) / 440.0)).astype(int)
    pcs = np.mod(midi_bins, 12)
    for pos in range(0, max(len(x) - frame + 1, 1), hop):
        chunk = x[pos : pos + frame]
        if len(chunk) < frame:
            chunk = np.pad(chunk, (0, frame - len(chunk)))
        mag = np.abs(np.fft.rfft(chunk * window))[valid]
        for pc in range(12):
            chroma[pc] += mag[pcs == pc].sum()
    total = chroma.sum()
    return chroma / total if total else chroma


def audio_features(audio: np.ndarray, sample_rate: int, duration: float) -> Dict[str, object]:
    frame = 512
    hop = 128
    x = np.asarray(audio, dtype=float)
    energies = []
    for pos in range(0, max(len(x) - frame + 1, 1), hop):
        chunk = x[pos : pos + frame]
        if len(chunk) < frame:
            chunk = np.pad(chunk, (0, frame - len(chunk)))
        energies.append(float(np.sqrt(np.mean(chunk * chunk))))
    energies = np.asarray(energies)
    novelty = np.maximum(np.diff(energies, prepend=energies[0]), 0.0)
    threshold = float(np.median(novelty) + 2.5 * np.std(novelty))
    peaks, _ = find_peaks(novelty, height=threshold, distance=max(1, int(0.18 * sample_rate / hop)))
    return {
        "duration_seconds": float(duration),
        "onset_rate_hz": float(len(peaks) / duration),
        "global_chroma": _chroma_from_audio(x, sample_rate).tolist(),
        "section_b_chroma": _chroma_from_audio(x, sample_rate, 8.0, 16.0).tolist(),
    }


def cosine_similarity(a: Iterable[float], b: Iterable[float]) -> float:
    x = np.asarray(list(a), dtype=float)
    y = np.asarray(list(b), dtype=float)
    denom = np.linalg.norm(x) * np.linalg.norm(y)
    return float(np.dot(x, y) / denom) if denom else 0.0


def _write_wav(path: Path, audio: np.ndarray, sample_rate: int) -> None:
    wavfile.write(path, sample_rate, np.int16(np.clip(audio, -1, 1) * 32767))


def run_pilot(output: Path, sample_rate: int = 16000) -> Dict[str, object]:
    output.mkdir(parents=True, exist_ok=True)
    base = build_piece(corrupt=False)
    corrupt = build_piece(corrupt=True)
    base.write(str(output / "base.mid"))
    corrupt.write(str(output / "corrupt.mid"))

    rendered = {
        "base_sine": render_audio(base, "sine", sample_rate),
        "base_harmonic": render_audio(base, "harmonic", sample_rate),
        "corrupt_sine": render_audio(corrupt, "sine", sample_rate),
    }
    for name, audio in rendered.items():
        _write_wav(output / f"{name}.wav", audio, sample_rate)

    sym_base = symbolic_features(base)
    sym_corrupt = symbolic_features(corrupt)
    aud = {
        name: audio_features(signal, sample_rate, base.get_end_time() if name.startswith("base") else corrupt.get_end_time())
        for name, signal in rendered.items()
    }
    result = {
        "status": "feasibility_spike_not_metric_validation",
        "sample_rate": sample_rate,
        "symbolic": {"base": sym_base, "corrupt": sym_corrupt},
        "audio": aud,
        "render_stability": {
            "global_chroma_cosine": cosine_similarity(aud["base_sine"]["global_chroma"], aud["base_harmonic"]["global_chroma"]),
            "onset_rate_absolute_difference": abs(aud["base_sine"]["onset_rate_hz"] - aud["base_harmonic"]["onset_rate_hz"]),
        },
        "corruption_sensitivity": {
            "symbolic_b_section_distance": 1.0 - cosine_similarity(sym_base["section_b_pcp"], sym_corrupt["section_b_pcp"]),
            "audio_b_section_distance": 1.0 - cosine_similarity(aud["base_sine"]["section_b_chroma"], aud["corrupt_sine"]["section_b_chroma"]),
        },
        "symbolic_audio_agreement": {
            "base_global_cosine": cosine_similarity(sym_base["global_pcp"], aud["base_sine"]["global_chroma"]),
            "corrupt_global_cosine": cosine_similarity(sym_corrupt["global_pcp"], aud["corrupt_sine"]["global_chroma"]),
        },
    }
    (output / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("outputs"))
    parser.add_argument("--sample-rate", type=int, default=16000)
    args = parser.parse_args()
    result = run_pilot(args.output, args.sample_rate)
    print(json.dumps({
        "render_stability": result["render_stability"],
        "corruption_sensitivity": result["corruption_sensitivity"],
        "symbolic_audio_agreement": result["symbolic_audio_agreement"],
    }, indent=2))


if __name__ == "__main__":
    main()
