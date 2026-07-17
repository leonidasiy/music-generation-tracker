import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from clpr_stage0 import (
    ManifestError,
    PromptRegistryError,
    render_prompt_pair,
    sha256_file,
    validate_manifest,
    validate_prompt_registry,
    validate_regions,
)


class PromptRegistryTests(unittest.TestCase):
    def valid_registry(self):
        return {
            "schema_version": "0.1.0",
            "scope": "instrumental electronic / beat-driven pop",
            "durations": {
                "60": {
                    "duration_sec": 60,
                    "regions": [
                        {"name": "strict_a", "class": "strict_preservation", "start_sec": 0, "end_sec": 18},
                        {"name": "halo_ab", "class": "adaptation_allowed", "start_sec": 18, "end_sec": 22},
                        {"name": "target_b", "class": "target", "start_sec": 22, "end_sec": 38},
                        {"name": "halo_ba", "class": "adaptation_allowed", "start_sec": 38, "end_sec": 42},
                        {"name": "strict_aprime", "class": "strict_preservation", "start_sec": 42, "end_sec": 60},
                    ],
                }
            },
            "pairs": [
                {
                    "id": "register_b",
                    "template": "Create an exactly {DURATION}-second track; {TARGET_CLAUSE}; no vocals.",
                    "clauses": {
                        "control": "During B only, keep the lead in A's register",
                        "intervention": "During B only, move the lead exactly one octave above A",
                    },
                    "changed_field": "target_clause",
                }
            ],
        }

    def test_valid_registry_renders_clause_minimal_pair(self):
        registry = self.valid_registry()
        validate_prompt_registry(registry)
        control, intervention = render_prompt_pair(registry["pairs"][0], duration_sec=60)
        self.assertIn(registry["pairs"][0]["clauses"]["control"], control)
        self.assertIn(registry["pairs"][0]["clauses"]["intervention"], intervention)
        self.assertEqual(
            control.replace(registry["pairs"][0]["clauses"]["control"], "<TARGET>"),
            intervention.replace(registry["pairs"][0]["clauses"]["intervention"], "<TARGET>"),
        )

    def test_registry_rejects_multiple_target_placeholders(self):
        registry = self.valid_registry()
        registry["pairs"][0]["template"] += " {TARGET_CLAUSE}"
        with self.assertRaises(PromptRegistryError):
            validate_prompt_registry(registry)

    def test_regions_reject_overlap(self):
        regions = self.valid_registry()["durations"]["60"]["regions"]
        regions[2]["start_sec"] = 21
        with self.assertRaises(PromptRegistryError):
            validate_regions(regions, duration_sec=60)


class ManifestTests(unittest.TestCase):
    def valid_manifest(self):
        return {
            "schema_version": "0.1.0",
            "run_id": "ace-register-b-seed-42-control-r1",
            "pair_id": "register_b",
            "condition": "control",
            "generator": {
                "name": "ACE-Step 1.5",
                "access_type": "local_open",
                "version": "test-revision",
                "interface": "python",
            },
            "generation": {
                "submitted_prompt": "prompt",
                "duration_requested_sec": 60,
                "seed": 42,
                "seed_status": "fixed",
                "settings": {},
                "prompt_rewriting": False,
            },
            "environment": {"hardware": "Apple M5", "software": {}},
            "output": {
                "path": "runs/example.wav",
                "sha256": "0" * 64,
                "duration_observed_sec": 60.0,
                "sample_rate_hz": 44100,
                "channels": 2,
                "size_bytes": 1,
            },
            "regions": [
                {"name": "target_b", "class": "target", "start_sec": 22, "end_sec": 38}
            ],
            "failures": [],
            "cost_usd": 0.0,
            "cumulative_stage0_cost_usd": 0.0,
            "created_at": "2026-07-17T00:00:00Z",
        }

    def test_manifest_accepts_complete_record(self):
        validate_manifest(self.valid_manifest())

    def test_manifest_rejects_missing_generator_version(self):
        manifest = self.valid_manifest()
        del manifest["generator"]["version"]
        with self.assertRaises(ManifestError):
            validate_manifest(manifest)

    def test_manifest_rejects_invalid_condition(self):
        manifest = self.valid_manifest()
        manifest["condition"] = "high"
        with self.assertRaises(ManifestError):
            validate_manifest(manifest)


class HashTests(unittest.TestCase):
    def test_sha256_file_matches_hashlib(self):
        payload = b"clpr-stage0-fixture\n"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.bin"
            path.write_bytes(payload)
            self.assertEqual(sha256_file(path), hashlib.sha256(payload).hexdigest())


if __name__ == "__main__":
    unittest.main()
