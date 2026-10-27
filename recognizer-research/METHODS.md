# Recognizer Research — methods and evidence boundaries

This is the separate execution lane requested on 24 October 2026, not a replacement for the generation tracker or its existing Execution Log. The machine-readable status.json drives the new page.

## Current method amendment — 27 October 2026

The dated foundation sections below describe historical scopes, not the current corpus or a claim that only DSP has run. The current checkpoint is an exploratory frozen-pretrained rhythm pilot, with no production integration.

- **Score:** percentage of intended recordings whose relative BPM deviation is strictly above 8%. Severe deviations above 50%, missing outputs, and combined unacceptable-or-missing incidence are separate. Each offending recording counts once; mean magnitude is secondary. Missing estimates never shrink the denominator. Other analysis tasks need their own tolerances.
- **Current execution:** 151 inspected recordings, one fixed Beat This! `single_final0` checkpoint, original mixtures, and direct versus licensed librosa DP decoding of identical frozen activations. Both use a prespecified event-to-BPM readout; no reference-guided octave correction, sample removal or per-record winner selection.
- **Observed result:** direct has 11 above-tolerance estimates and 2 missing, combined 13/151 = 8.61%, versus previous preprocessing 59/151 = 39.07%. DP has 16/151 = 10.60%, with no missing. This is an exploratory numerical gain, not independently established broad performance.
- **Exposure:** 100 exact publisher-training cases, 21 exact publisher-validation cases, 18 related-comp solos and 12 unresolved cases. Publisher validation may inform model/checkpoint selection and shares performer/session families; it is not untouched confirmation. The 21-case direct rate of 1/21 = 4.76% is a separate diagnostic, not a replacement denominator.
- **Limits:** guitar solos remain 6/18 = 33.33% failures; all three new direct regressions are solos. Ungated DP returns about 300 BPM on silence and non-rhythmic controls. Numerical/API control completion is not musical correctness or safety qualification.
- **Protocol revisions:** author eight-fold weight downloads stalled before model inference. A public mirror supplied the exact author-checksummed single-split checkpoint; blocked plans and partial attempts were retained. CASM installation was deferred because its own decoder licence was unclear. The actual comparison is not CASM or a reproduction of its paper.
- **Verification:** 16 tests, eight API controls, a synthetic CPU/MPS parity check, 151 activation-cache identities, 302 event readouts, 152 summary and 152 paired cells; independent runtime and exploratory-reporting reviews. No new human beat/tactus annotations, full-corpus CPU reproduction or broad-genre confirmation.
- **Next priority:** independent genre/audio-type-diverse confirmation with source/artist/composition/performance overlap checks and an advance resource/rights proposal. A frozen released model baseline now precedes further fine-tuning or novel architecture investment.

## Why this lane exists
An eight-area source audit and native Dereck review selected beat/pulse reliability, then chord discrimination, then instrument-presence/admission validation. This is a task-dependent research-investment judgment, not a comparison of incompatible accuracy percentages. The 36-step prospective protocol remains a plan, not 36 completed experiments.

## Historical foundation increment — 24 October 2026
- Preserve the original application and its datasets. Execute only exact copied rhythm functions and matching shared features. Do not claim full-app integration verification.
- Four local regression recordings are selected from manifest IDs without using outcomes: the lexicographically first original GuitarSet comp and solo, and first GMD validation and test recordings. They are NOT an independent performance sample.
- Six explicitly synthetic numerical controls cover silence, DC, a sustained tone, and 60/120/180-BPM pulse trains. Known click placement is not a perceptually adjudicated musical beat reference.
- A separate implementation agent owns task-separated metrics/tests; a reference agent owns blinded instructions and source rights/overlap; a diagnosis agent owns reanalysis of historical predictions. Native Codex sessions are requested as gpt-6.1-sol with medium reasoning; they cannot spawn further agents.
- Keep exact global BPM, accepted-level diagnostic, beat timing, downbeat timing, literal meter and availability separate. Maximum-cardinality one-to-one timing matching is a transparent prototype, not a claim of mir_eval parity or continuity validation.
- New source annotation requires prediction-blinded independent musical judgment; no agent output is presented as human annotation.

## Scientific connection
CLPR remains the existing flagship and CRVP its representation/renderer validation work package. Task-specific recognizer qualification can expose false compliance or leakage conclusions, but chord/meter reliability does not validate register or note-density measurement. A known symbolic edit is not automatically an audible musical effect.

## Publication gate
A reused-data exploratory numerical gain is now recorded, but independently confirmed broad recognizer performance and an empirical paper are not established. A methods paper requires independently referenced source-disjoint evaluation, a differentiated contribution, uncertainty, confound controls and reproducibility. Synthetic controls, saved-output reaggregation and code-review approval are not substitutes.

## Primary background
- [Beat this! Accurate beat tracking without DBN postprocessing (2024)](https://arxiv.org/abs/2407.21658) — academic source; beat/downbeat evidence does not by itself establish global BPM/meter utility.
- [GuitarSet](https://guitarset.weebly.com/) — dataset source; current local cases are inspected development material.
- [Groove MIDI Dataset](https://magenta.tensorflow.org/datasets/groove) — dataset source; electronic-kit recordings and metadata have domain/split limits.

The private source audit and agent transcripts remain local. Only curated status, aggregate findings and safe artifact identities are published here. Milestone checkpoints are deployed, not streamed continuously.

## Training/architecture amendment — 24 October 2026

The owner now explicitly authorizes fine-tuning, retraining and promising architecture changes in the research workspace. This supersedes the initial no-training phase boundary, not the historical results. No training has run yet. Existing inspected datasets may support honestly labeled exploratory development training after rights/label/group checks; they cannot become untouched confirmation. Unknown beat/meter labels must not be invented from session BPM or treated as negatives. Resource and independent evaluation gates remain. Paid compute and production modifications are separate decisions.

The comparison ladder is unchanged/simple rules → small trained head or adapter → limited backbone fine-tuning → a mechanism-motivated architecture extension. Each tier must be falsifiable against simpler and complexity-matched controls.

### Close prior art, not our new finding
[Explore This! Beat and Downbeat Tracking From a Learned Tatum Grid (Kihlborg, Holzapfel, Schlüter; ISMIR 2026)](https://arxiv.org/pdf/2610.14817) already models a learned tatum grid, candidate tempo/phase distributions and joint metrical states. The [official program entry](https://ismir2026program.ismir.net/poster_320.html) and [released source](https://github.com/CPJKU/explore_this) confirm the identity and scope. Paper/code are not independent replications of musical performance. Its reported limitations are hypotheses for diagnosis, not established local gains. The original reproduction commit named in the upstream README is `18906da44d2247b19829e0cf9a098bed6d42316f`; its modules live under `beat_this/model/`, unlike the current README's renamed path. Only small code/license files were retrieved; no weights or upstream model execution.

Thus a joint grid/meter architecture alone does not establish novelty. Candidate extensions, training and scientific claims remain separately gated.
