# CLPR Stage 0 — Mechanical Feasibility Spike

## Verdict: IN PROGRESS

Stage 0 tests whether the CLPR protocol can be executed and audited. It does **not** establish human validity, metric superiority, broad generator generalization, or causal counterfactual behavior.

## Fixed scope

- Instrumental electronic / beat-driven pop
- 120 BPM, 4/4
- Time-anchored A–B–A′
- 60-second minimum; 90-second preferred pilot template
- Separate B-section register and closed-hi-hat activity interventions
- ACE-Step 1.5 open core
- Udio commercial snapshot after access and payment approval
- BabySlakh/Slakh2100 oracle calibration

## Directory map

- `config/prompt_pairs.json` — frozen clause-minimal prompt registry and timing maps
- `config/run_manifest.schema.json` — immutable run-record schema
- `src/clpr_stage0.py` — deterministic validation and hashing utilities
- `tests/test_clpr_stage0.py` — test-first protocol checks
- `runs/` — ignored raw manifests and generated outputs; only curated non-audio summaries may be committed

## Current execution evidence — 2026-07-17

- Host: Apple M5 MacBook Air, 24 GB unified memory
- Available project-volume storage before ACE-Step installation: approximately 23 GiB
- ACE-Step 1.5 Hugging Face repository storage reported by the API: 10,079,024,720 bytes, approximately 9.39 GiB, before dependency and cache overhead
- `uv 0.6.14` is available
- Prompt registry frozen for 60- and 90-second variants
- Seven Stage 0 protocol tests pass
- ACE-Step source and environment installed under `/Users/lirenzhang/.cache/clpr-stage0/ACE-Step-1.5/` (approximately 11 GB)
- Two 10-second seed-42 runs produced byte-identical FLAC files with SHA-256 `df405f00c845e3d745d2e584603b2b3127c08d58d94b11cb48ed25c0dfae7f09`
- One 10-second seed-43 run produced a distinct FLAC with SHA-256 `c2933382abd0dd77610f1d24b21ae0ebbf5e4920ecfc57815469bade2d2a41f5`, confirming that the pinned configuration is not seed-insensitive
- The successful local path used MLX, batch size one, eight ODE steps, direct prompting, and no planning-LM initialization
- No paid subscription or commercial credential has been used

## Active local resource gate

The model and environment are installed, and the host had approximately 24 GiB free before the seed-43 diagnostic. That single 10-second generation increased reported swap usage from approximately 2.2 GiB to 14.2 GiB and reduced free disk to 12 GiB. Stopping ACE-Step restored free disk to 21 GiB. An earlier inference session had temporarily reduced free space to roughly 328 MiB.

The 15 GiB stop threshold was therefore triggered. Do not attempt the 60/90-second gate locally under the current storage and memory headroom; resume long-form testing on a 48/80 GB institutional or cloud GPU. No files will be deleted or moved without separate explicit permission.

## Test commands

```bash
PYTHONPATH=pilots/clpr_stage0/src \
  python3 -m unittest discover -s pilots/clpr_stage0/tests -v

PYTHONPATH=pilots/clpr_stage0/src \
  python3 -m clpr_stage0 registry pilots/clpr_stage0/config/prompt_pairs.json
```

## Stage 0 completion criteria

- ACE-Step runtime and fixed-seed behavior characterized, or a precise infeasibility verdict recorded
- Udio interface/version/terms and seed behavior characterized, or access blocker recorded
- BabySlakh oracle edits recover the target direction and reject proxy-only edits
- Same-prompt null and seed-coupling diagnostics completed
- Cost ledger remains at or below $100
- Final verdict changed to `VALIDATED`, `PARTIAL`, or `INVALIDATED`
