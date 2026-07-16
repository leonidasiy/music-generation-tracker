# Dual-Representation Pilot Audit

> Audit date: 2026-07-16
> Status: deterministic feasibility spike; not metric validation

## What was executed

- Four unit tests passed.
- The pilot was rerun into a clean temporary output directory.
- The regenerated `results.json` was byte-for-byte identical to the stored result.

## What the numbers actually show

- **Within-renderer synthesized-timbre perturbation:** global chroma cosine between sine and harmonic renders was `0.99576`; detected onset-rate difference was `0.0`. The JSON key `render_stability` is an implementation label, not evidence of cross-renderer stability.
- **Controlled B-section pitch corruption:** symbolic section distance was `1.0`; audio-chroma section distance was `0.74824`.
- **Global symbolic/audio agreement:** cosine was `0.90699` for the base piece and `0.91125` for the corrupted piece.
- **Onset-rate interpretation:** symbolic note rate is about `4.01 notes/s` because melody and bass notes are counted separately; the audio detector reports about `1.96 onset events/s`, close to the two simultaneous beat events per second. These are not competing estimates of the same quantity.

## Valid inference

The pipeline can generate paired MIDI/audio, alter one symbolic region while holding rhythm and duration fixed, change the timbre mode within one deterministic renderer, and compute deterministic representation-specific measurements. Audio chroma is sensitive to the intended pitch corruption while remaining fairly stable under this one renderer’s sine-to-additive-harmonic timbre change.

## Invalid inference

The pilot does **not** validate CRVP, HPGA, PCCM, or any latent trait. It cannot establish renderer invariance, generalize beyond a synthetic ABA piano/bass pattern, estimate population agreement, or show human construct validity.

Specific reasons:

1. The B-section corruption uses nearly disjoint pitch-class content, making the symbolic distance of `1.0` deliberately easy.
2. Only two elementary synthesizer timbres are compared; neither resembles the variation among soundfonts, instruments, rooms, mastering chains, or human performances.
3. Global chroma suppresses order and hierarchy. A high global cosine can coexist with incorrect section order.
4. The same source generates both representations, so shared agreement may reflect a shared construction rather than an externally validated musical trait.
5. No transcription, beat-tracking, segmentation, source-separation, or human-annotation error is present.
6. Four unit tests verify mechanics, not scientific validity.

## Recommended next pilot

Use a factorial controlled benchmark rather than fitting a latent model prematurely:

- 12–30 short pieces with explicit two- or three-section plans.
- At least three renderers/soundfonts per piece.
- Independent perturbations: section reorder/delete, motif replacement, pitch-content corruption, timing jitter, half/double beat grid, dynamics flattening, noise/reverb, and transcription note deletion/insertion.
- Metrics: oracle symbolic result, each audio pipeline result, audio–symbolic discrepancy, renderer variance, perturbation response curve, and model-ranking stability.
- Resample whole pieces, not frames.
- Defer MTMM/CFA until simulation shows identification and adequate independent-composition sample size.

## Decision

**Pilot mechanics: PASS. Scientific validation: NOT YET ATTEMPTED.**
