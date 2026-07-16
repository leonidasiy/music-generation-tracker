# Dual-Representation Pilot

A feasibility spike for paired symbolic/audio measurement. It creates a small ABA MIDI piece, renders it with two deterministic synthesizer timbres, makes a controlled structural corruption, and compares symbolic and audio estimates.

The pilot is deliberately small. It tests plumbing and failure modes, not the validity of CRVP or any publication claim.

## Run

```bash
cd /Users/lirenzhang/.hermes/profiles/researcher/projects/music-generation-research/pilots/dual_representation
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python pilot.py --output outputs
.venv/bin/python -m unittest -v test_pilot.py
```

## Expected artifacts

- `outputs/base.mid`
- `outputs/base_sine.wav`
- `outputs/base_harmonic.wav`
- `outputs/corrupt.mid`
- `outputs/corrupt_sine.wav`
- `outputs/results.json`

## Verdict: PENDING

The verdict is written after real execution.
