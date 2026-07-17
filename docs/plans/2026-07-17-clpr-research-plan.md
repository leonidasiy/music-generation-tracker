# CLPR Research and Implementation Plan

> **For Hermes:** Execute this plan task-by-task with test-first implementation, explicit evidence gates, and documentation/frontend synchronization after every meaningful increment.

**Goal:** Establish and validate Counterfactual Localized Plan Responsiveness (CLPR) as a diagnostic benchmark for whether long-form music generators perform a requested local change while preserving protected musical regions.

**Architecture:** The project proceeds from mechanical feasibility to oracle calibration, generator benchmarking, human validation, robustness testing, and publication. Generated outputs, prompts, settings, hashes, detector outputs, and judgments remain separate artifacts connected through immutable run manifests. CLPR remains a diagnostic vector—target effect, directional accuracy, off-target leakage, boundary spillover, and optional plan-relation evidence—not a universal scalar until human evidence supports aggregation.

**Tech Stack:** Python 3.11+, JSON/JSON Schema, NumPy/SciPy/librosa or equivalent verified audio tools, ACE-Step 1.5, Udio manual mode, BabySlakh/Slakh2100, Git/GitHub Pages, unit tests, deterministic file hashing, and later a browser-based human-listening interface.

---

## Fixed Research Decisions

- **Paper 1 flagship:** M09 / CLPR.
- **Stage 0 status:** mechanical feasibility only; it cannot establish human validity, metric superiority, broad generalization, or a universal aggregate.
- **Initial domain:** instrumental electronic / beat-driven pop.
- **Form:** time-anchored A–B–A′.
- **Duration:** 60-second minimum; 75–120 seconds preferred when interfaces permit.
- **Initial interventions:** B-section lead-register change and B-section closed-hi-hat rhythmic-activity change, evaluated separately.
- **Open core:** ACE-Step 1.5, subject to local runtime and determinism verification.
- **Commercial anchor:** Udio manual mode, subject to subscription, version, settings, terms, and seed verification.
- **Oracle calibration:** BabySlakh first; Slakh2100 when additional coverage is needed.
- **Stem policy:** post-separated stems are estimates, not native source ground truth; instrument-presence compliance is non-core.
- **Budget ceiling:** $90 provisional allocation within a hard $100 ceiling: $10 Udio, up to $50 cloud contingency, up to $30 listener reserve.

## Reserved Paper 1 Claim

> Minimal localized changes to long-form music instructions produce measurable target-section responses and collateral-change patterns that CLPR distinguishes from same-prompt stochastic variability; these diagnostics explain human judgments of localized instruction compliance better than global text–audio alignment or target-only segment similarity.

Every stage below states which portion of this claim it may support. No earlier stage inherits a stronger conclusion from a later intended analysis.

---

# Stage 0 — Mechanical Feasibility and Protocol Freeze

## Objective

Determine whether the proposed generators, prompts, metadata pipeline, oracle edits, and null-variability design can be executed reproducibly enough to justify a larger pilot.

## Stage 0A — Governance, Files, and Immutable Metadata

**Artifacts:**

- Create: `pilots/clpr_stage0/README.md`
- Create: `pilots/clpr_stage0/config/prompt_pairs.json`
- Create: `pilots/clpr_stage0/config/run_manifest.schema.json`
- Create: `pilots/clpr_stage0/src/clpr_stage0.py`
- Create: `pilots/clpr_stage0/tests/test_clpr_stage0.py`
- Create: `pilots/clpr_stage0/runs/.gitkeep`
- Modify: `pilots/clpr_stage0/.gitignore`

**Required manifest fields:**

- Run and pair identifiers
- Generator, access type, displayed version, source revision, and generation date
- Interface and subscription tier
- Full submitted prompt, target-clause identifier, and condition
- Duration request and observed duration
- Seed and whether it is exposed, fixed, or unavailable
- All generation settings and prompt-rewriting state
- Hardware and software environment
- Output path, SHA-256 hash, sample rate, channels, and file size
- Target, strict-preservation, adaptation-halo, and out-of-scope intervals
- Failure flags and free-text notes
- Cost in USD and cumulative Stage 0 cost

**Verification:**

1. Tests reject missing required fields.
2. Tests reject a prompt pair that changes more than the declared target clause.
3. Tests reject overlapping or unordered timing regions.
4. Tests verify SHA-256 calculation against a known fixture.
5. `python -m unittest discover -s pilots/clpr_stage0/tests -v` passes.

## Stage 0B — Prompt and Timing Freeze

### Canonical 60-second timing

- A: 0–20 s
- B: 20–40 s
- A′: 40–60 s
- Strict A: 0–18 s
- First adaptation halo: 18–22 s
- B target core: 22–38 s
- Second adaptation halo: 38–42 s
- Strict A′: 42–60 s

### Canonical 90-second timing

- A: 0–30 s
- B: 30–60 s
- A′: 60–90 s
- Strict A: 0–28 s
- First adaptation halo: 28–32 s
- B target core: 32–58 s
- Second adaptation halo: 58–62 s
- Strict A′: 62–90 s

### Register pair

Hold the complete prompt invariant except:

- R0: `During the B section only, play the synth-lead hook in the same middle register used in A`
- R1: `During the B section only, play the synth-lead hook exactly one octave above the register used in A`

Preserve lead rhythm, note durations, pitch-class sequence, phrase count, patch, harmony, bass, drums, density, dynamics, and mix.

### Rhythmic-activity pair

Hold the complete prompt invariant except:

- H0: `During the B section only, the closed hi-hat plays steady eighth notes`
- H1: `During the B section only, the closed hi-hat plays steady sixteenth notes`

Preserve tempo, kick, snare, bass, lead, harmony, hat sound, accent topology, panning, section loudness, density, and mix.

**Verification:**

- A deterministic validator confirms exactly one declared clause changes.
- Producer review confirms that the target wording does not imply excitement, climax, brightness, loudness, patch, density, or global tempo changes.
- Prompt text and timing regions are versioned before generation.

## Stage 0C — ACE-Step 1.5 Access and Runtime Spike

**External source location:** `~/.cache/clpr-stage0/ACE-Step-1.5`

**Do not commit:** model weights, dependency caches, generated audio, or external repository contents.

**Steps:**

1. Record available disk, hardware, OS, `uv`, Python, and source revision.
2. Clone the official repository at a pinned commit.
3. Read the current macOS/MLX installation and inference documentation.
4. Estimate source, dependency, and model storage before downloading weights.
5. Install the minimal supported macOS environment only after the storage gate passes.
6. Generate one short instrumental smoke-test output with a fixed seed.
7. Repeat identical settings and seed twice.
8. Hash and compare outputs; if bytes differ, compare duration, waveform, and feature-level differences.
9. Run one 60-second A–B–A′ prompt only after the short smoke test succeeds.
10. Record runtime, peak memory if observable, output duration, warnings, and failures.

**Go condition:** ACE-Step produces analyzable audio on the available machine without exhausting storage or memory, and fixed-seed behavior is either deterministic or quantitatively characterizable.

**Fallback:** If local execution is unsafe or impractical, price a pinned cloud-GPU run within the $50 contingency. Do not spend without explicit approval.

## Stage 0D — Udio Interface and Commercial Snapshot

**Prerequisites requiring Leonidas:**

- Approval of the current subscription charge if a free tier is insufficient
- Login performed by Leonidas or a user-provided access route; never record credentials
- Decision on native Udio duration versus a preregistered supported-duration analysis window

**Steps:**

1. Record pricing, tier, terms, model/version label, manual mode, instrumental mode, duration options, prompt expansion, seed, prompt strength, quality, and clip-start controls.
2. Disable prompt expansion or rewriting.
3. Generate an identical-prompt, identical-settings, identical-seed repeat.
4. Archive prompts, displayed settings, raw outputs, hashes, date, and cost.
5. Generate one clause-minimal pair only after the repeatability check.
6. Do not call Udio pairs counterfactual until coupling diagnostics pass.

**Go condition:** The service exposes enough settings and stable output retrieval to create a dated, auditable external-validity snapshot.

## Stage 0E — BabySlakh Oracle Calibration

**Steps:**

1. Download only the minimal BabySlakh subset needed for prototyping.
2. Select pieces with active lead/piano and percussion content through the target interval.
3. Produce exact oracle edits for:
   - one-octave register shift in B
   - eighth-to-sixteenth closed-hat activity in B where a suitable track exists
   - unchanged control render
   - one-bar transition-tail case
   - boundary displacement case
   - loudness-only proxy
   - brightness-only proxy
   - density-only proxy
4. Preserve stems and MIDI for ground truth.
5. Verify that target detectors respond in the correct interval.
6. Verify that leakage diagnostics stay near the control level outside the edit.
7. Verify that proxy-only edits do not masquerade as target compliance.

**Go condition:** At least one preregistered detector plus producer listening recovers each known target direction while rejecting key production proxies.

## Stage 0F — Same-Prompt Nulls and Coupling Diagnostics

**Minimal executable design:**

- Start with 2 intervention families.
- Start with at least 2 base plans per family; increase only after inspecting typed failure modes, not significance.
- For each generator and base plan, collect unchanged-prompt replicates under:
  - identical fixed seed, when supported
  - different seeds
  - permuted seed pairings
- Collect changed-prompt pairs under identical candidate seeds and independent seeds.
- Treat pieces and interventions—not individual seeds—as the conceptual independent units.

**Diagnostics:**

- Exact-output repeatability
- Within-seed same-prompt distance
- Between-seed same-prompt distance
- Same-seed cross-prompt target and protected-region distances
- Permuted-seed cross-prompt distances
- Independent-sample average response
- Boundary-alignment sensitivity
- Typed failures: target omission, timing failure, form failure, collateral rewrite, proxy response, artifact, truncation, service failure

**Provisional gate:** Paired-seed language is retained only if same-seed matching reduces protected-region variability relative to permuted and independent pairing while preserving sensitivity to the target clause. Otherwise Stage 1 uses repeated independent-sample estimands.

## Stage 0 Deliverables

- Reproducible source and environment record
- Frozen prompt-pair registry
- Validated run-manifest schema
- ACE-Step runtime verdict
- Udio interface verdict or documented access blocker
- BabySlakh oracle-calibration report
- Same-prompt/null and seed-coupling report
- Exact cost ledger
- `README.md` verdict: `VALIDATED`, `PARTIAL`, or `INVALIDATED`

## Stage 0 Claims Allowed

- Mechanical execution succeeded or failed under documented constraints.
- Fixed-seed behavior is deterministic, approximately coupled, or unsuitable.
- Oracle edits are or are not recovered by the current measurement pipeline.
- Target effects are or are not distinguishable from observed same-prompt variability in this small feasibility sample.

No human-validity, cross-generator ranking, population estimate, or causal-generalization claim is allowed.

---

# Stage 1 — Calibrated Multi-Plan Pilot

## Objective

Turn the Stage 0 spike into a stable, preregisterable pilot and determine whether CLPR has enough signal to justify claim-bearing data collection.

## Tasks

1. Freeze generator versions and either paired-seed or independent-sample estimands.
2. Expand to 6–10 base plans per intervention family, contingent on Stage 0 failure diversity.
3. Add controlled prompt paraphrases only as a robustness block, not as additional independent discoveries.
4. Freeze register and rhythmic-activity detectors against held-out oracle edits.
5. Define prompt-anchored and plausible-alignment analyses before scoring generated pairs.
6. Report TES, DA, OTL, BS, and alignment sensitivity separately.
7. Keep PRD not applicable unless a structural-relation intervention is added.
8. Conduct blinded producer checks for form, target response, preservation, artifacts, and technical quality.
9. Estimate costs and failure rates for Stage 2.
10. Draft the preregistration and statistical-analysis plan.

## Gate to Stage 2

Proceed only if target effects exceed practical null variability on more than isolated cherry-picked examples, protected-region measurements are interpretable, oracle tests remain valid, and typed failures can be handled without post-hoc metric changes.

---

# Stage 2 — Claim-Bearing Benchmark Data Collection

## Objective

Collect the frozen benchmark needed to test the responsiveness and locality portions of the Paper 1 claim.

## Tasks

1. Select 3–4 generator families or explicitly narrow the claim to the tested two-system panel.
2. Pin open model commits/checkpoints and snapshot every commercial model/version.
3. Preregister prompt families, interventions, regions, null strata, exclusions, and analysis code.
4. Hold out prompt templates and at least one generator where feasible.
5. Generate unchanged-prompt nulls before inspecting changed-prompt effects.
6. Run all frozen prompt pairs and retain every output, including failures.
7. Hash and archive immutable raw audio and manifests.
8. Run frozen feature extraction and alignment-sensitivity analyses.
9. Report generator-specific and pooled estimates without treating seeds as independent subjects.
10. Preserve compliance, quality, artifacts, and preference as separate outcomes.

## Gate to Stage 3

Proceed to human validation only after data integrity, exclusions, manifests, and frozen automatic scores pass independent audit.

---

# Stage 3 — Human Construct Validation and Metric Meta-Evaluation

## Objective

Test whether CLPR diagnostics measure perceived localized compliance rather than detector artifacts or production quality.

## Listener Tasks

Collect separate judgments for:

- requested B-section change
- A/A′ preservation
- non-target B-feature preservation
- transition acceptability
- audible artifacts
- musical coherence
- production quality
- preference

## Design Requirements

1. Blind model and condition identity.
2. Loudness-match where the construct permits.
3. Randomize order and sides.
4. Include attention and anchor trials.
5. Include oracle edits, wrong-section edits, proxy-only edits, and unchanged controls.
6. Estimate inter-rater reliability by construct.
7. Compare CLPR outputs against global CLAP-like alignment and target-only segment similarity.
8. Test incremental association with human compliance after controlling for quality and artifacts.
9. Do not optimize metric weights and evaluate them on the same listener sample.
10. Release a de-identified judgment dataset where consent and licenses permit.

## Gate to Stage 4

Proceed only if listeners can distinguish the target constructs reliably enough and CLPR contributes beyond simpler baselines without merely tracking loudness, brightness, density, or production quality.

---

# Stage 4 — Robustness, Generalization, and Representation Validation

## Objective

Determine where CLPR conclusions survive model, prompt, alignment, detector, representation, and musical-domain changes.

## Work Packages

- **Generator generalization:** held-out models and version drift.
- **Prompt robustness:** held-out templates and constrained paraphrases.
- **Alignment robustness:** prompt anchors versus adjudicated plausible boundaries.
- **Detector robustness:** alternative pitch, onset, beat, and source-analysis pipelines.
- **Representation robustness:** aligned MIDI, rendered audio, natural multitracks, and automatic transcription.
- **Production robustness:** loudness, brightness, width, saturation, reverb, density, and mastering perturbations.
- **Genre expansion:** only after the electronic/beat-driven scope is stable.
- **Duration expansion:** multi-minute stress tests after 60–120 second validity.

## Outputs

- Generator/version sensitivity profile
- Alignment-sensitivity intervals
- Detector and renderer dependence
- Scope conditions and explicit failure domains
- CRVP-style validation where indicator count and sample size justify it

---

# Stage 5 — Paper 1 Freeze, Release, and Reproduction

## Objective

Produce a reproducible benchmark paper whose claims do not exceed the validated evidence.

## Tasks

1. Freeze benchmark version, manifests, schemas, prompts, code, and tests.
2. Archive open-model revisions and commercial snapshot metadata.
3. Publish generated audio only where redistribution terms permit.
4. Otherwise publish prompts, manifests, hashes, settings, and derived annotations.
5. Release automatic metrics and human-evaluation code.
6. Write a model card/dataset card with exclusions, licenses, ethical risks, and known failure modes.
7. Run an independent reproduction from a clean environment.
8. Report negative and null results.
9. Separate preregistered analyses from exploratory analyses.
10. Update the live tracker and all project documents to the final evidence state.

---

# Stage 6 — Follow-Up Research, Conditional on Paper 1

Possible follow-ups are explicitly downstream:

- Prompt-only intervention optimization
- Best-of-N selection and reranking
- Constraint-specific regeneration or repainting
- Native multitrack/source-preservation benchmark
- Additional instruction families: dynamics, density, instrument entry/exit, recurrence, and structural relations
- Lightweight adapters or LoRA only if prompt-only methods plateau
- Longer-form and genre-general CLPR studies

These must not be allowed to expand Stage 0 or delay the first valid benchmark.

---

# Documentation and Synchronization Rule

After every meaningful increment:

1. Update `TODO.md` immediately.
2. Append objective execution evidence to `HISTORY.md`.
3. Update stable decisions and caveats in `INFO.md`.
4. Update operational definitions in `METRICS.md` only when the protocol changes.
5. Add verified sources to `REFERENCES.md`.
6. Synchronize the corresponding frontend status and next actions in `index.html`.
7. Run unit tests, HTML structure checks, title parity, `git diff --check`, browser inspection, and JavaScript-console checks.
8. Commit, push, and verify the GitHub Pages deployment.

# Immediate Execution Order

1. Create the Stage 0 scaffold and tests.
2. Freeze the two exact prompt pairs and timing maps.
3. Pin and inspect ACE-Step source without downloading weights.
4. Resolve the local-storage gate before model/dependency download.
5. Run the ACE-Step short fixed-seed smoke test.
6. Obtain Udio access/payment only when the commercial lane is ready.
7. Download BabySlakh and create oracle edits.
8. Run same-prompt/null and coupling diagnostics.
9. Issue the Stage 0 verdict.
