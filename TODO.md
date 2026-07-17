# Music Generation & Orchestration Research — TODO

> Project initiated: 2026-07-14

## Phase 1: Initial Research
- [x] Search arXiv for music generation papers (2023–2026)
- [x] Search arXiv for music orchestration / arrangement papers
- [x] Search web for frontier music generation models (MusicGen, Suno, Udio, etc.)
- [x] Compile 10+ papers with 10+ citations each
- [x] Write short summaries for each core paper

## Phase 2: Deep Dive
- [ ] Extract full paper contents via arXiv API / PDF
- [ ] Write detailed summaries with key findings
- [ ] Catalog technical approaches (diffusion, transformer, autoregressive, etc.)
- [ ] Document evaluation metrics used
- [ ] Note open-source model availability

## Phase 3: Frontend Tracker
- [x] Design UI layout with tabs
- [x] Code self-contained HTML page
- [x] Embed the core paper registry and current research agenda
- [x] Add interactive features (search, filtering, keyboard-accessible tabs)

## Phase 4: Deployment
- [x] Set up GitHub Pages repository
- [x] Deploy frontend
- [x] Verify live URL accessibility

## Phase 5: Finalization
- [x] Validate the initial hosted tracker
- [x] Deliver the hosted URL

## Current Status — 2026-07-17
- [x] Narrow Paper 1 to localized instruction responsiveness (M09 / CLPR)
- [x] Reclassify HPGA/PCCM as optional evidence channels and CRVP as validation infrastructure
- [x] Audit the deterministic dual-representation feasibility pilot (4/4 tests passing)
- [x] Validate the DDGS + local extraction research stack and document its limits
- [x] Synchronize the frontend, TODO, HISTORY, INFO, REFERENCES, and METRICS status
- [x] Run native Codex producer-practitioner review with Dereck and retain CLPR as flagship
- [x] Add strict-preservation, adaptation-allowed, and unconstrained locality classes to CLPR
- [x] Decide that Stage 0 is a feasibility pilot rather than the claim-bearing Paper 1 experiment
- [x] Review academic practice for open versus commercial generator evaluation
- [x] Select ACE-Step 1.5 as the primary open candidate and Udio as the commercial anchor
- [x] Identify BabySlakh/Slakh2100 as the first oracle-calibration corpus
- [x] Set a provisional total budget ceiling of $90 within the approved sub-$100 limit
- [ ] Complete full-text deep dives for the remaining core papers

## Refined Research Agenda — 2026-07-16
- [x] Review feasibility of combining long-form structure and music instruction tuning
- [x] Identify section-level compositional plan adherence as the unifying problem
- [x] Define proposed metric suite, controlled violations, hypotheses, and go/no-go gates
- [x] Add the refined plan to the website as a dedicated Research Plan tab
- [x] Run browser and content validation on the updated site
- [x] Deploy and verify the updated GitHub Pages site

## Metric Exploration — Initial Stage
- [x] Survey music-generation, MIR, cognition, and human-evaluation metrics
- [x] Survey temporal evaluation methods from film, narrative, dance, and visual art
- [x] Survey information-theoretic, graph, and dynamical-systems measures of form
- [x] Maintain a candidate metric registry with novelty and feasibility status
- [x] Add an evolving Metric Lab section to the website
- [x] Validate the initial Metric Lab website increment locally and on GitHub Pages
- [x] Record open questions that require Leonidas's clarification

## Dual-Representation Exploration
- [x] Record the decision to keep symbolic and native-audio paths open
- [x] Investigate symbolic, audio, and cross-representation measurement risks
- [x] Add Cross-Representation Validity Profile (CRVP) as candidate M11
- [x] Define 18 systematic questions for paired symbolic/audio evaluation
- [x] Update the Metric Lab with the decision and M11
- [x] Build a small rendered-MIDI pilot and compare symbolic/audio estimates

## Reliability Gate and Continued Exploration — 2026-07-16
- [x] Benchmark DDGS search coverage and repeatability on known academic targets
- [x] Benchmark local extraction fidelity across HTML, repositories, and papers
- [x] Document limitations and source-verification rules for the local research stack
- [x] Audit and interpret the dual-representation pilot outputs
- [x] Investigate representation-robust metric design and transcription-error propagation
- [x] Validate new findings with independent reviewers
- [x] Update METRICS.md, INFO.md, REFERENCES.md, HISTORY.md, and the Metric Lab website

## Next Experimental Increment
- [x] Freeze exact prompt wording for separate B-section register and rhythmic-activity interventions in instrumental electronic / beat-driven pop
- [x] Write the detailed Stage 0–6 research and implementation plan
- [x] Create the Stage 0 prompt registry, run-manifest schema, deterministic validators, and seven passing tests
- [x] Identify candidate generators with repeatable randomness and sufficient duration: ACE-Step 1.5 plus Udio
- [x] Pin ACE-Step source revision `6d467e4b5081ccb0abf1ec1bf4fdf9051a2d34b0` and complete the no-download dependency audit
- [ ] Resolve the ACE-Step storage location: the 9.39 GiB model plus 124 packages is unsafe to install by default on a volume with approximately 23 GiB free
- [ ] Run an ACE-Step 1.5 installation and fixed-seed smoke test on the M5 / 24 GB Mac
- [ ] Decide whether Udio must use native 60/90-second outputs or a preregistered supported-duration analysis window
- [ ] Provision one month of Udio Standard and record the exact model/version, manual-mode settings, seed behavior, and terms
- [ ] Build BabySlakh oracle edits for target effect, leakage, boundary spillover, and production-proxy controls
- [ ] Build same-prompt replicate baselines for TES/DA/OTL/BS
- [ ] Implement a small CLPR prompt-pair pilot before adding more candidate metrics
- [ ] Expand the representation benchmark across multiple renderers and controlled degradations
- [ ] Design separate human judgments for compliance, musicality, production quality, and preference
- [ ] Add oracle DAW perturbations for production-proxy gaming, justified adaptation, and alignment uncertainty

## Stage 0 Resource Plan — 2026-07-17
- [x] Open core: ACE-Step 1.5, subject to local runtime and determinism verification
- [x] Commercial external-validity anchor: Udio Standard at $10 for one month
- [x] Cloud-compute contingency: up to $50 only if local execution is inadequate
- [x] Listener micro-study reserve: up to $30 after mechanical feasibility passes
- [x] Total provisional allocation: $90; $10 remains below the $100 ceiling
- [x] Keep instrument-presence evaluation outside the universal scorecard unless native stems are available
- [ ] Audit output redistribution rights before publishing commercial generations

## Iterative Dereck Metric Review — 2026-07-16
- [x] Apply Dereck's first-round professional revisions to M01–M04
- [x] Run a fresh native Codex Dereck review over all M01–M11 definitions
- [x] Revise every metric still marked REVISE and resubmit
- [x] Reach a final Dereck verdict with no metric marked REVISE
- [x] Synchronize METRICS, INFO, HISTORY, TODO, and the live Metric Lab after the final decision
