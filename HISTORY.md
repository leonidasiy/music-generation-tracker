# Work History

## 2026-07-14 — Session Start
- Project initiated by Leonidas
- Created project directory structure
- Set up documentation files: TODO.md, HISTORY.md, INFO.md, REFERENCES.md
- Began Phase 1: Initial Research on music generation and orchestration models
- Searched arXiv for frontier papers (2023–2026)
- Compiled 14 papers with verified citation counts

## 2026-07-14 — Phase 1 Complete
- Compiled 14 high-quality papers (all 10+ citations, ~5,300+ total)
- Papers cover: raw audio generation, symbolic generation, multi-track, style transfer, surveys
- Top papers: Jukebox (1,373 cit.), MusicLM (1,235 cit.), MusicGen (1,199 cit.)
- Ran validation subagent — found 3 metadata issues
- Fixed: MuPT arXiv ID (2404.06393), JEN-1 arXiv ID (2310.19180), Paper 14 author/venue correction

## 2026-07-14 — Frontend Tracker Built
- Designed and built self-contained HTML progress tracker (397 lines, 32KB)
- 5 tabs: Recent Research, My Progress, TODO, References, Info
- Search/filter, category dropdown, responsive design
- Embedded all 14 papers with structured metadata

## 2026-07-14 — Deployed
- Authenticated gh CLI via GitHub PAT (leonidasiy)
- Created repo: github.com/leonidasiy/music-generation-tracker
- Deployed to GitHub Pages: https://leonidasiy.github.io/music-generation-tracker/
- Frontend validation subagent ran: **APPROVED** with 3 minor notes
- Fixed citation total (5,300+ from 5,600+)

## 2026-07-14 — Light Mode + Final Delivery
- Converted color scheme from dark to light mode
- All badge and tag backgrounds updated for light theme
- Pushed and verified live deployment
- Documentation complete: TODO.md, HISTORY.md, INFO.md, REFERENCES.md

## 2026-07-16 — Refined Research Agenda
- Evaluated the feasibility of combining long-form coherent structure with music instruction tuning
- Narrowed the shared problem to section-level compositional plan adherence
- Defined a diagnostic metric suite, controlled counterfactual violations, falsifiable hypotheses, and go/no-go gates
- Added a dedicated Research Plan tab to the website with linked primary sources
- Validated HTML structure, JavaScript interaction, responsive layout, and all eight prior-work links
- Deployed the update to GitHub Pages and verified the live Research Plan tab

## 2026-07-16 — Metric Lab Initial Exploration
- Surveyed music structure analysis, motif discovery, expectation, tension, controllability, psychometrics, causal evaluation, and dynamical-systems methods
- Consulted cross-domain work from film, narrative, poetry, dance, visual composition, architecture, and interactive narrative
- Opened `METRICS.md` as a living registry with ten candidate diagnostics, novelty threats, feasibility, failure cases, and falsification tests
- Added fifteen foundational and cross-domain sources to `REFERENCES.md`
- Added an evolving Metric Lab tab to the website with implementation priorities and open decisions
- Applied an independent review: normalized epistemic status labels, tightened cross-domain mappings, added direct film/poetry/game sources, and improved tab/search accessibility
- Deployed the Metric Lab to GitHub Pages; verified 10 cards, 9 cross-domain links, correct tab/ARIA state, seven hidden inactive panels, and zero browser-console errors

## 2026-07-16 — Dual-Representation Exploration
- Leonidas chose to keep symbolic and native-audio representations open during exploration
- Surveyed symbolic reliability, audio/transcription failure modes, and psychometric methods for comparing imperfect measurement methods
- Added candidate M11, Cross-Representation Validity Profile, with CRVC, RSAA, and MISD diagnostics
- Added eighteen systematic investigation questions and seven cross-representation sources
- Firecrawl search credits were exhausted; continued through the arXiv API and direct primary-source extraction instead

## 2026-07-16 — Reliability Gate and Strategic Narrowing
- Benchmarked DDGS on five known academic targets over two runs each; primary sources appeared in 9/10 top-five sets, while repeated exact-URL overlap was low (mean Jaccard 0.180)
- Benchmarked local extraction on eight public HTML/PDF/repository sources; all eight produced usable content, and the private-network case was blocked before fetch
- Preserved raw ordered search results, labels, extraction routes, and arithmetic in `WEB_RESEARCH_QA_RAW.json`; documented limitations and operating rules in `WEB_RESEARCH_QA.md`
- Audited the dual-representation pilot, fixed a tautological preservation assertion, reran four passing tests, and confirmed byte-identical output regeneration
- Reclassified the current pilot as a deterministic feasibility spike rather than evidence of cross-renderer or construct validity
- Verified newer competing work including SongEval, CMI-RewardBench, SegTune, MAD/MusicPrefs, transcription-robustness studies, and method-comparison foundations
- Narrowed Paper 1 around M09 localized instruction responsiveness; HPGA/PCCM are optional structural evidence channels and CRVP is validation infrastructure
- Operationalized TES, DA, OTL, BS, and applicable PRD with held-out same-prompt null scales, explicit protected regions, and piece/intervention-level uncertainty
- Passed independent re-review after correcting source wording, metric ambiguity, causal scope, renderer terminology, and QA auditability
- Updated the Metric Lab and Research Plan website sections to reflect the reliability gate and revised research strategy

## 2026-07-16 — Progress and Documentation Synchronization
- Replaced stale frontend progress states that still described the built, reviewed, and deployed tracker as pending
- Aligned the frontend TODO with the repository TODO and made the next experimental increment explicit
- Rebuilt the core `REFERENCES.md` registry deterministically from the 14-paper frontend dataset; current registry totals are 3,721 approximate citations and 14/14 open-source or open-artifact entries
- Added a concise current-status snapshot to INFO.md and the current flagship strategy to METRICS.md
- Synchronized all project documentation around M09 / CLPR as Paper 1, optional HPGA/PCCM evidence, CRVP validation infrastructure, and the prompt-pair pilot as the active next step

## 2026-07-16 — Codex Producer-Practitioner Validation
- Created and invoked Dereck as a native Codex custom subagent with a professional music-production, arrangement, sound-design, vocal-production, and audio-engineering role
- Dereck independently read the complete M01–M11 registry and completed successfully without modifying project files
- Retained M09 / CLPR as the Paper 1 flagship and M11 / CRVP as validation infrastructure
- Marked M01–M04 for revision and deferred M05–M08 and M10 from the Paper 1 core
- Added three CLPR locality classes: strict-preservation, adaptation-allowed, and unconstrained regions
- Elevated production-proxy gaming, stochastic pairing, alignment uncertainty, and annotation-scope expansion as practical risks
- Required separate reporting for instruction compliance, musicality, production quality, preference, and perceived artifacts
- Recorded the epistemic limit: Dereck's conclusions are practitioner judgments and experiment-design guidance, not empirical metric validation

## 2026-07-16 — Iterative Dereck Revision Loop Complete
- Applied first-round revisions to M01–M04 covering multi-label form roles, boundary uncertainty, motif salience, formal-versus-production boundary evidence, and channel-selective contrast/cohesion
- A fresh Dereck pass marked M02, M06, M07, and M09 for further revision
- Added non-aggregated instrumental/vocal motif channels and loudness-matched proxy controls to M02
- Split musical-event pacing from production-intensity pacing and bounded M06 by preregistered style, meter, and section role
- Split harmonic tension, arrangement/performance intensity, and production intensity in M07 and removed unsupported style-general aggregation
- Added explicit stochastic-coupling criteria, prompt/oracle/inferred alignment classes, alignment-sensitivity intervals, and proxy-only compliance tests to M09
- Ran a second fresh native Codex Dereck review over all current definitions
- Final verdict: M01–M04, M06–M07, M09, and M11 KEEP; M05, M08, and M10 DEFER; no REJECT; `REVISE_COUNT: 0`
- Preserved the evidence limit: professional coherence is not empirical metric validation

## 2026-07-17 — CLPR Stage 0 Resource and Evidence Decision
- Clarified the boundary between the Stage 0 feasibility pilot and the claim-bearing Paper 1 experiment
- Reserved Paper 1's empirical claim for evidence that CLPR separates localized response and collateral change from stochastic variability and improves agreement with human localized-compliance judgments over simpler baselines
- Reviewed current academic practice and adopted a mixed-panel policy: reproducible open generators form the core, while commercial systems serve as dated external-validity snapshots
- Selected ACE-Step 1.5 as the primary open candidate and Udio as the first commercial anchor, both conditional on runtime, version, terms, and seed-coupling audits
- Fixed the initial production scope to instrumental electronic / beat-driven pop, time-anchored A–B–A′, at least 60 seconds with 75–120 seconds preferred
- Restricted the first minimal prompt contrasts to separate B-section register and rhythmic-activity interventions
- Selected BabySlakh/Slakh2100 for exact MIDI/stem oracle edits and kept instrument-presence compliance outside the universal scorecard unless native tracks are available
- Established a provisional $90 allocation: $10 Udio, up to $50 cloud contingency, and up to $30 listener micro-study reserve
- Synchronized TODO, INFO, METRICS, REFERENCES, HISTORY, and the frontend around these decisions
