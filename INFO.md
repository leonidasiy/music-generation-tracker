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

## Current project status — 2026-07-17
- **Completed:** initial 14-paper collection, metadata review, light-mode tracker, GitHub Pages deployment, refined research agenda, Metric Lab, web-research reliability gate, deterministic dual-representation pilot audit, producer review, Stage 0 generator/dataset scan, detailed Stage 0–6 plan, frozen Stage 0 prompts, and tested manifest utilities.
- **Paper 1 focus:** test whether a minimal temporal-instruction change causes the requested local musical effect while preserving preregistered non-target regions.
- **Primary outputs:** TES and DA for target response; OTL and BS for collateral effects; PRD only when an intervention changes a structural relation.
- **Current evidence limit:** the existing deterministic pilot establishes mechanical feasibility and reproducibility only; it does not establish human validity, cross-renderer invariance, or population-level robustness.
- **Stage 0 status:** local 10-second fixed-seed mechanics passed: two seed-42 runs were byte-identical and seed 43 produced a distinct valid artifact. The third run breached the disk/swap safety gate, so 60/90-second execution is deferred to a 48/80 GB institutional or cloud GPU.
- **Initial musical scope:** instrumental electronic / beat-driven pop in a time-anchored A–B–A′ form; minimum duration 60 seconds, with 75–120 seconds preferred where supported.
- **Initial interventions:** manipulate B-section register and rhythmic activity separately while holding all other prompt clauses fixed.
- **Candidate panel:** ACE-Step 1.5 as the reproducible open core and Udio as one commercial external-validity anchor; selection remains conditional on runtime, version, and seed-coupling audits.
- **ACE-Step source audit:** official revision `6d467e4b5081ccb0abf1ec1bf4fdf9051a2d34b0` is pinned locally. The current environment resolves 124 packages, and the model repository reports 9.39 GiB before dependency/cache overhead.
- **Current blocker:** the model and environment are installed, but local long-form generation is unsafe under the observed swap pressure. Resume the 60/90-second gate only on a suitable GPU host.
- **Oracle calibration:** use BabySlakh/Slakh2100 for exact MIDI/stem counterfactuals before interpreting generated outputs.
- **Budget:** $10 Udio + up to $50 cloud contingency + up to $30 listener reserve = $90 provisional total, leaving $10 below the $100 ceiling.
- **Active next increment:** secure a suitable GPU host, run the 60-second duplicate gate, audit Udio's current interface and terms, create oracle edits, estimate same-prompt null variability, and run the small CLPR prompt-pair pilot.

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
