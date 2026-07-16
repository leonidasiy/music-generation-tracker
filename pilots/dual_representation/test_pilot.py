import tempfile
import unittest
from pathlib import Path

import numpy as np

from pilot import (
    build_piece,
    render_audio,
    symbolic_features,
    audio_features,
    cosine_similarity,
    run_pilot,
)


class DualRepresentationPilotTests(unittest.TestCase):
    def test_render_change_preserves_symbolic_source(self):
        midi = build_piece(corrupt=False)
        before = symbolic_features(midi)
        a = render_audio(midi, timbre="sine", sample_rate=8000)
        b = render_audio(midi, timbre="harmonic", sample_rate=8000)
        self.assertEqual(a.shape, b.shape)
        self.assertFalse(np.allclose(a, b))
        self.assertEqual(before, symbolic_features(midi))

    def test_structural_corruption_changes_symbolic_profile(self):
        base = symbolic_features(build_piece(corrupt=False))
        corrupt = symbolic_features(build_piece(corrupt=True))
        self.assertLess(cosine_similarity(base["section_b_pcp"], corrupt["section_b_pcp"]), 0.8)
        self.assertEqual(base["note_count"], corrupt["note_count"])

    def test_audio_features_are_finite(self):
        midi = build_piece(corrupt=False)
        audio = render_audio(midi, timbre="sine", sample_rate=8000)
        features = audio_features(audio, sample_rate=8000, duration=midi.get_end_time())
        self.assertTrue(np.isfinite(features["onset_rate_hz"]))
        self.assertEqual(len(features["global_chroma"]), 12)

    def test_end_to_end_writes_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run_pilot(Path(tmp), sample_rate=8000)
            self.assertTrue((Path(tmp) / "results.json").exists())
            self.assertIn("render_stability", result)
            self.assertIn("corruption_sensitivity", result)


if __name__ == "__main__":
    unittest.main()
