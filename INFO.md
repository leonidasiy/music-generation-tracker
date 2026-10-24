# Noteworthy Information

## Research Domains Covered
1. **Music Generation** — Text-to-music, symbolic music generation, raw audio generation
2. **Music Orchestration** — Automatic arrangement, instrumentation selection, multi-track generation
3. **Model Architectures** — Diffusion models, transformers, autoregressive, GANs, language models for music

## Key Conference Venues
- ISMIR (International Society for Music Information Retrieval)
- ICASSP (IEEE International Conference on Acoustics, Speech and Signal Processing)
- NeurIPS (Neural Information Processing Systems)
- ICML (International Conference on Machine Learning)
- ICLR (International Conference on Learning Representations)
- ACM MM (Multimedia)

## Major Industry Models (frontier)
- **ACE-Step 1.5** — Open long-form generator with duration, seed, metadata, repaint, and local execution controls; primary Stage 0 candidate
- **MusicGen** (Meta, 2023) — Transformer-based text-to-music, released open-source
- **Suno** — Proprietary, high-quality song generation from lyrics
- **Suno Studio 2.0** — Premier-only chat-driven production environment with chat-generated audio/MIDI, audio↔MIDI workflows, project arrangement, custom effects, automation, built-in synthesis, and stem separation; bounded commercial qualification-audit candidate as of 2026-08-22
- **Veena Studio** — Browser-based agentic MIDI/audio DAW added as a dated interactive-MIDI development pilot after a 2026-09-06 user-operated test; demonstrated exact repaired chord creation and zero-leakage local editing, but compound harmonic compliance, functional chord realization, required downstream adaptation, and self-verification were inconsistent
- **Udio** — Proprietary, high-fidelity music generation
- **Stable Audio** (Stability AI) — Diffusion-based audio generation
- **Jukebox** (OpenAI, 2020) — VQ-VAE + transformer for raw audio
- **MusicLM** (Google, 2023) — Hierarchical text-to-music
- **Riffusion** — Stable Diffusion fine-tuned on spectrograms

## Key Research Directions (2024–2026)
- Controllable music generation (genre, tempo, key, structure)
- Long-form coherent music (full songs vs short clips)
- Multi-track / stem-based generation
- Music understanding + generation joint models
- Efficiency improvements (latency, memory, real-time generation)
- Evaluation metrics beyond FAD (Fréchet Audio Distance)

## Metric Exploration Principles — 2026-07-16
- Treat the benchmark as a diagnostic scorecard, not a universal scalar.
- Separate generator error, analysis/recognizer error, and instruction ambiguity.
- Evaluate recurrence by requested role and transformation, not repetition quantity alone.
- Use counterfactual prompt pairs to test localized responsiveness rather than incidental compliance.
- Borrow relations—not superficial metaphors—from other arts: film pacing, narrative setup/payoff, poetic enjambment, choreographic transformation, and architectural local/global intelligibility.
- Validate every candidate with controlled corruptions, held-out generators, human construct ratings, and simple confound baselines.

## Competitive scan and narrowed paper core — 2026-07-16
- Global long-form aesthetics and structural-clarity evaluation is now occupied by SongEval and the ICASSP song-aesthetics challenge.
- Broad multimodal music instruction scoring is directly addressed by CMI-RewardBench.
- Segment-level prompt alignment is addressed by SegTune and adjacent temporally controlled generation work.
- The clearest remaining gap is **localized counterfactual responsiveness**: minimally change one section instruction, require the intended local effect, and penalize collateral change elsewhere.
- Paper 1 should be framed as one benchmark for **localized instruction responsiveness**, not eleven allegedly novel metrics. Paired-effect or counterfactual language is conditional on defensible seed coupling.
- HPGA and PCCM are interpretable structural evidence inside the flagship CLPR test.
- CRVP is a validation protocol for representation/renderer dependence, not a novel psychometric theory.
- Compliance, musicality, production quality, and preference must remain distinct outcomes.

## Local web-stack reliability gate — 2026-07-16
- DDGS found a correct primary source in 9 of 10 repeated known-item query runs, but exact result-set overlap was low (mean URL Jaccard 0.180).
- Direct/local extraction succeeded on all eight tested public sources and blocked the private-network test.
- Search snippets are discovery aids, not evidence; citation counts require dedicated scholarly sources.
- Metadata-only landing pages must be followed to PDFs for substantive claims.
- Long extracted documents may be summarized by the tool layer; quotations require checking the primary PDF.

## Current project status — 2026-09-06
- **Completed:** initial 14-paper collection, metadata review, light-mode tracker, GitHub Pages deployment, refined research agenda, Metric Lab, web-research reliability gate, deterministic dual-representation pilot audit, producer review, Stage 0 generator/dataset scan, detailed Stage 0–6 plan, frozen Stage 0 prompts, and tested manifest utilities.
- **Paper 1 focus:** test whether a minimal temporal-instruction change causes the requested local musical effect while preserving preregistered non-target regions.
- **Primary outputs:** TES and DA for target response; OTL and BS for collateral effects; PRD only when an intervention changes a structural relation.
- **Current evidence limit:** the existing deterministic pilot establishes mechanical feasibility and reproducibility only; it does not establish human validity, cross-renderer invariance, or population-level robustness.
- **Stage 0 status:** local 10-second fixed-seed mechanics passed: two seed-42 runs were byte-identical and seed 43 produced a distinct valid artifact. The third run breached the disk/swap safety gate, so 60/90-second execution is deferred to a 48/80 GB institutional or cloud GPU.
- **Initial musical scope:** instrumental electronic / beat-driven pop in a time-anchored A–B–A′ form; minimum duration 60 seconds, with 75–120 seconds preferred where supported.
- **Initial interventions:** manipulate B-section register and rhythmic activity separately while holding all other prompt clauses fixed.
- **Revised commercial panel:** ACE-Step 1.5 remains the reproducible open audio core. Suno Studio 2.0 enters a bounded interactive-system qualification audit because it exposes chat-to-MIDI, localized project editing, audio↔MIDI, effects, and automation. Udio remains the provisional raw-audio commercial candidate until a matched access/export/repeatability/construct-equivalence gate resolves the claim-bearing commercial slot; only one commercial access period will be purchased initially.
- **ACE-Step source audit:** official revision `6d467e4b5081ccb0abf1ec1bf4fdf9051a2d34b0` is pinned locally. The current environment resolves 124 packages, and the model repository reports 9.39 GiB before dependency/cache overhead.
- **Current blocker:** the model and environment are installed, but local long-form generation is unsafe under the observed swap pressure. Resume the 60/90-second gate only on a suitable GPU host.
- **Oracle calibration:** use BabySlakh/Slakh2100 for exact MIDI/stem counterfactuals before interpreting generated outputs.
- **Budget:** up to $30 Suno + up to $45 cloud contingency + up to $20 listener reserve = $95 provisional total, leaving $5 below the $100 ceiling. No purchase has been made.
- **Active next increment:** build the stateful instruction/action schema, verify Suno checkout/terms/export/version behavior, run the six-task bounded Suno audit from imported oracle projects, apply a matched Suno–Udio qualification gate without quality ranking, secure a suitable GPU host for ACE-Step, create oracle edits, and estimate repeated-instruction/same-prompt null variability.
- **Veena pilot:** two archived MIDI exports and a standard-library parser establish a mechanical single-session result: Query 1 final exactness was 32/32 notes after repair; Query 2 harmonic-position compliance was 23/32 (71.875%); Query 3 obeyed the maximum-one-non-chord-event rule in 3/8 bars; Query 5 changed only Track 1 note events in bars 6–7 with zero protected-event changes, but omitted `Ab` from `Bb7(#11)` and left an incompatible bass bar unchanged.
- **Method refinement:** retain CLPR and symbolic-first validation; add agent-claim calibration, verification/repair trajectories, required-adaptation omission, and function-defining chord-degree checks. Split locality into strictly protected, adaptation-allowed-but-unnecessary, adaptation-required, and unconstrained state.
- **Panel refinement:** Veena is a free dated development pilot, not a validated winner or reproducible core. Suno remains the bounded paid interactive audit; ACE-Step remains the open audio core; Udio remains provisional for raw-audio construct comparison.

## Stage 0 evidence and publication boundary — 2026-07-17
- Current academic practice supports mixed open/commercial panels when a benchmark seeks real-world or frontier relevance, but commercial systems are not methodologically preferred by default. Reproducible open models should remain the benchmark core.
- The proposed Paper 1 claim is that CLPR distinguishes requested target-section response and collateral-change patterns from same-prompt stochastic variability, and that these diagnostics explain human localized-compliance judgments better than global alignment or target-only similarity baselines.
- Stage 0 can establish access, repeatability, null scales, alignment behavior, detector behavior, costs, and failure rates. It cannot establish human validity, broad generalization, metric superiority, or a universal CLPR aggregate.
- A fixed seed is not sufficient by itself to justify counterfactual language. Equal-seed prompt variants must demonstrate useful stochastic coupling against same-prompt, permuted-seed, and independent-sample diagnostics.
- Commercial outputs are dated product snapshots: record the service, displayed model/version, tier, date, interface, prompt-expansion state, all settings, seeds, raw files, and hashes.
- Post-hoc source separation is not native-stem ground truth. Instrument-presence compliance remains an experimental lane and stays outside the common aggregate unless every compared system exposes genuinely native tracks.

## Producer-practitioner validation — 2026-07-16
- A native Codex custom subagent named **Dereck** reviewed the full M01–M11 registry from production, arrangement, synthesis, vocal-production, and audio-engineering perspectives.
- Dereck retained M09 / CLPR as the Paper 1 flagship and M11 / CRVP as validation infrastructure; M01–M04 require revision, while M05–M08 and M10 should remain outside the Paper 1 core.
- CLPR locality now distinguishes **strict-preservation**, **adaptation-allowed**, and **unconstrained** regions so musically necessary pickups, transitions, tails, automation, voice-leading, and downstream consequences are not mislabeled as leakage.
- Production proxies are a principal threat: loudness, brightness, density, stereo width, patch novelty, vocal intensity, and transition effects can imitate form, contrast, pacing, tension, or boundary evidence.
- Human evaluation must report instruction compliance, musicality, production quality, preference, and perceived artifacts separately.
- This is practitioner review, not empirical metric validation.

### Final iterative verdict
- Dereck reviewed the revised registry again after M01–M04 and then M02/M06/M07/M09 were amended.
- Final result: **M01–M04, M06–M07, M09, and M11 KEEP; M05, M08, and M10 DEFER; no REJECT; `REVISE_COUNT: 0`.**
- “KEEP” means professionally coherent at the stated scope, not empirically validated.
- Completed safeguards include separate applicable channels, explicit N/A handling, vocal/production separation, loudness-matched proxy controls, style and meter bounds, no unsupported aggregate, verified seed-coupling criteria, and alignment-sensitivity analysis.

## Instruction-following symbolic generation direction — 2026-08-06
- **Feasibility verdict:** instruction fine-tuning for exact key, bar, chord, repetition, form, and orchestration requests is technically plausible, but current symbolic systems do not establish reliable compound-constraint compliance.
- **Preferred architecture:** natural-language instruction → typed musical-plan compiler → constrained symbolic generator → deterministic validator → renderer → CLPR/CRVP analysis → audio-grounded plural interpretation.
- **Why symbolic first:** MIDI/ABC/event representations expose key, bar boundaries, chords, repetition, and form to exact tests; direct audio models currently offer weaker verification and the reviewed instruction-tuned audio systems focus mainly on editing.
- **Immediate research contribution:** build an instruction compiler and exact-compliance benchmark before training a new generator; compare prompting, tool augmentation, supervised parser tuning, constrained decoding, rejection, and repair.
- **CLPR connection:** use one-field counterfactuals such as changing one chord, key, bar count, repetition count, or orchestration clause; score requested response and collateral change in exact target/protected regions.
- **CRVP connection:** validate symbolically first, render through multiple synthesizers, and quantify which conclusions survive audio-side estimation and renderer changes.
- **Interpretation connection:** after compliance is established, test whether controlled musical changes alter audio-grounded mood, imagery, tension, or narrative responses without treating any interpretation as objective essence.
- **Detailed archive:** `INSTRUCTION_TUNING_DIRECTION.md` contains the 18-question investigation, literature review, contradictions, research gaps, proposed work packages, and linked sources.
- **Independent audit refinement:** no reviewed open system jointly demonstrates free-form exact tonic/key, bar count, Roman-numeral sequence, explicit repetition, and form. The defensible novelty is the combined instruction-plan → CLPR → CRVP → plural-interpretation validation chain.
- **Audio comparison:** Mustango and JASCO strengthen the hybrid recommendation because their precise chord/beat control is predicted or explicitly supplied as time-aligned structure rather than inferred reliably from prose alone.

## Suno Studio 2.0 research impact — 2026-08-22
- **Decision:** KEEP CLPR as Paper 1. Suno's release increases the ecological relevance of localized instruction responsiveness but publishes no exact compound-compliance, leakage, spillover, or repeatability benchmark.
- **Architecture refinement:** expand the static typed musical plan into a stateful production-action schema with project preconditions, actions, protected state, and post-action diffs. Initial actions: create/edit MIDI, arrange clips, audio→MIDI, MIDI→audio, create/revise plugins, set parameters, write automation, split stems, and export.
- **Capability boundary:** official documentation supports chat-generated MIDI clips, audio-to-MIDI transcription, MIDI-to-audio generation, conversational plugin creation/revision, and manual parameter automation. It does not establish reliable exact constraints or a universal direct "voice to any instrument" operation.
- **New empirical lane:** add audio↔MIDI round-trip validation to CRVP using labeled monophonic, sung-root, instrumental, and controlled polyphonic inputs, followed by multi-instrument rendering.
- **Secondary lane:** plugin and automation instruction compliance is valuable but deferred from the Paper 1 core until score/MIDI CLPR is stable.
- **Commercial-system policy:** run one bounded Suno Studio qualification period after price/terms/export/version checks; do not replace Udio or subscribe to both before the matched construct-equivalence gate resolves.
- **Budget refinement:** provisional ceiling becomes $95: up to $30 Suno access, up to $45 cloud inference, up to $20 listener pilot, and $5 uncommitted. Verify live checkout before spending.
- **Detailed archive:** `SUNO_STUDIO_2_IMPACT.md` contains the 18-question review, claim corrections, contradictions, gaps, audit protocol, and citations.


## Separate recognizer research lane — 2026-10-24

Recognizer Research is a separate curated milestone page under recognizer-research/, not a replacement for this generation project or its existing Execution Log. Task-specific rhythm/beat qualification starts the analyzer work; CLPR remains flagship and CRVP remains validation infrastructure. The first checkpoint is deployed and live-verified; the separate page publishes reviewed milestone checkpoints. New analyzer work does not validate register/activity constructs or reopen unsafe long-form local generation.


## Trained recognizer research scope — 2026-10-24

Fine-tuning/retraining and promising new architectures are now permitted for research copies; no training has run. The separate Recognizer Research page reports this lane without changing the flagship or existing generator budget. Explore This! is newly verified close 2026 prior art, so joint grid/meter modeling alone is not claimed novel.


## Architecture design closure — 2026-10-24

Architecture-design closure: the independent reviewer first requested six bounded corrections. All were applied and a fresh gpt-6.1-sol medium read-only review approved the current design. Corrections restore inherited 512 MiB new-files / 30 GiB free-disk limits pending a separate measured preflight; prohibit automatic cache deletion; separate numerical 0.05 s scorer plumbing from unfrozen musical tolerance; correct capability attribution and superseded restrictions; and match hard routing and all downstream gradient-detachment controls. Approval is design coherence only, not training feasibility, musical benefit or novelty. No training has run.
