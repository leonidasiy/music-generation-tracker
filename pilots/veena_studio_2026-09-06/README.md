# Veena Studio Pilot — 2026-09-06

This directory contains the machine-auditable artifacts for the user-operated Veena Studio MIDI instruction and localized-edit pilot.

## Files

- `baseline.mid` — export after Queries 1–4 and before localized reharmonization.
- `after_query_5.mid` — export after localized reharmonization.
- `analyze_midi.py` — standard-library MIDI parser, compliance evaluator, and event-diff tool.
- `test_analyze_midi.py` — seventeen regression tests for source hashes, corrected chord classes/approach resolution, complete protected-event coverage, well-formed end-of-track handling, unmatched and boundary-ending notes, locality, and byte-identical reproduction.
- `results.json` — generated decoded event inventory and deterministic results.
- [`../../VEENA_STUDIO_PILOT.md`](../../VEENA_STUDIO_PILOT.md) — prompts, preserved responses, results, evidence limits, and methodology implications.

## Reproduce

```bash
python3 pilots/veena_studio_2026-09-06/analyze_midi.py \
  --before pilots/veena_studio_2026-09-06/baseline.mid \
  --after pilots/veena_studio_2026-09-06/after_query_5.mid \
  --output pilots/veena_studio_2026-09-06/results.json

PYTHONPATH=pilots/veena_studio_2026-09-06 \
  python3 -m unittest pilots/veena_studio_2026-09-06/test_analyze_midi.py -v
```

## Scope

Mechanical single-session pilot only. No repeated identical-state trials, stable model identifier, seed control, human evaluation, or broad product claim is available.
