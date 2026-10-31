<!-- autonomous-improvement-20261031 -->
## Current autonomous improvement milestone —31October2026

Temporal chord smoothing leaves guitar failures at 26/60 while reducing events from 1,437 to 850. Four external classical whole songs were scored with predictions sealed before reference access. Instrument window study: baseline: 88/292, global_fixed: 73/292, mean: 86/292, max: 96/292, top2: 93/292, persistence: 82/292. Original application unchanged; broad sub-30% confirmation remains open.

See [current detailed comparison](CAMPAIGN.md) and [curated aggregates](autonomous-summary.json). Internal scientificreviews pass; exactpublic security/browser/deployment gates are separately recorded. The masked 768D follow-up has now completed training and independent verification: learned arms give88/86/89 failed recordings versus global73/292, and all five grouped outer folds retain global. All learned arms are rejected; no new backbone inference or production adoption.
<!-- end autonomous-improvement-20261031 -->

<!-- extended-decoding-20261031 -->
## Current richer-decoding increment —31October2026

Class-aware instrument tuning: 74/292 failures versus 73/292 for the simpler global setting; reject adoption. Fixed 181-label root-first chords improve expanded full-pitch error from 59.09% to 51.42%, but strict quality still fails 26/60 clips. Root error of 19.94% matches the prior raw-root control. The new quality head, tested with 27 corpus fits, fails 27/60 and is rejected. Original application unchanged; no broad sub-30% confirmation.

27corpus multinomialfits/32total optimizercalls/28model files; no acoustic-backbone retraining. An additive extension-aware full-pitch rescore preserves historical encoding/scores; main quality denominator1832.6404seconds. Cache-backed integration9tests/180projections is not full-app testing. Sixsourcefamilies inspected; two prospective recent full songs total14,651,020bytes,NCaudio/reference reuse unresolved; no new audio/model acquired. See [latest detailed report](EXTENDED.md) and [curated aggregates](extended-decoding-summary.json). Overall target and production adoption remain open.
<!-- end extended-decoding-20261031 -->

<!-- passt-current-20261031 -->
# PaSST matched instrumentation comparison —31October2026

PaSST-assisted instrument presence reduced observed-reference failure recordings from 19/47 (40.43%) to 14/47 (29.79%). Misses 12→7; false positives 8→8; severe 1→1; missing0. Eight recordings rescued, three regressed. 49 intended ten-second recordings,29 artist groups,47 scorable/99 sparse observed nonvoice pairs. PublisherTEST was used for checkpoint selection; this is bounded development evidence, not independent final confirmation or full-inventory accuracy. Application not modified; full-song aggregation remains untested. Wider historical regression is mixed: 100/320→97/320 failures, FN64→32 but FP55→79; keep the candidate experimental, not default.

- Primary failure means at least one disagreement on an observed reference class; unknown/unannotated classes are never negatives. Two reference-unscorable recordings remain in inference accounting.
- PaSST publisher TEST served validation/checkpoint selection. New local artist groups do not imply independence from model selection, compositions or pretrained exposure.
- The descriptive artist-cluster95% interval for candidate-minus-baseline failure incidence spans -25.00 to +2.44 percentage points; it includes no difference. No population-level improvement is established.
- Only eleven existing one-to-one singleton names are rescored; eight coarse/multimember classes and Vocal/world vocabulary are unchanged. No new instrument rows are invented.
- These results concern ten-second clips. The prepared local integration must fall back on longer inputs; a first-window score must not be assigned to an entire song. Full-track pooling and section audibility remain separate experiments.
- Genres and marked/not-marked instrumental are overlapping track metadata, not verified excerpt vocal/solo/live/studio conditions. Broad independent final audio-condition coverage remains open.
- Source licence and conditional author weight permission do not establish commercial/hosted/redistribution clearance. No paid annotation/data/compute service was used; existing assistant billing and electricity are excluded.
- The native PaSST0.50 coarse-head diagnostic is not the hybrid or a deployable fine-instrument mapping. Sigmoid scores are not calibrated presence probabilities.

Read [instrument results](INSTRUMENTS.md) and [aggregate machine-readable results](instrument-presence-summary.json).
<!-- end passt-current-20261031 -->

---

# Presence tracing: decision and next evidence

## Historical presence-trace checkpoint — 31 October 2026 (superseded by the opening PaSST comparison)

**Scope:** saved-output/source tracing and pure replay, not new model inference or a musical-accuracy experiment. Tempo remains implemented; this increment does not change instrument or chord models.

**Reporting-contract guardrail:** the current analyzer applies the global inclusive 0.20 display cutoff, removes generic taxonomy rows, and permits a section name only when it is also in that global list and meets its own cutoff. A local score above cutoff does not override the global membership rule. Removing the rule or unioning section names into the global list would change the report contract, not merely repair a typo. [Current source and quality policy, checked 31 Oct 2026; Internal primary source evidence; HIGH for literal implementation, not musical accuracy.]

**Known limits:** above-cutoff similarity is not proof of audibility; a candidate admitted by a counterfactual gate is not automatically a corrected musical error. Missing prefilter section evidence must remain unknown, not be reconstructed from displayed rows alone.

**No-fee reference route:** existing human annotations are acceptable leads when exact-source rights, task fit, partial-label masks and study/checkpoint overlap are established. No paid annotation, paid data service or similar purchase will be pursued. Existing inspected recordings remain development/regression evidence.

**Frontier check:** a 2026 instrument-grounding preprint evaluates temporal localization by concatenating three OpenMIC excerpts, not by manually labeling natural song sections. MIREX 2026 reports different public/hidden rankings for a submitted adapted-encoder system; its hidden labels are activation-derived and not manually verified. These are reasons to test local failure stages and external validity, not grounds to assume a newer model will win. [Academic preprint and benchmark organizer report, retrieved 31 Oct 2026; MEDIUM, single-source reported results; additional verification required.]
- [Instrument-grounding preprint](https://arxiv.org/html/2606.31338)
- [MIREX instrument-recognition results](https://music-ir.org/mirex/wiki/2026:Audio_Instrument_Recognition_Results)

**Resource policy:** justified research storage is authorized; demonstrably disposable temporary/superseded artifacts may be cleaned up while required data, checkpoints and audit evidence are retained. Alert only when free disk falls below 15 GB. Earlier dated 30 GiB pauses remain historical records, not the current operational stop rule.

## Executed findings and closure

- **Replay scope:** 505 historical fusion returns, 505 separate current-function comparisons, 66 current saved-score reconstructions, 269 global/family report projections and 326 section projections. There are 190 distinct saved IDs, not 269 independent recordings. Fifteen contract controls and 15 invented-coverage probes are distinct synthetic scopes. [Executed replay and parent reproduction, 31 Oct 2026; Internal deterministic evidence; HIGH for retained counts/behavior only.]
- **Exact gate example:** the 6.3–10.0 s Vocal row scores 0.215 while global Vocal is 0.190; local global-membership exclusion is intentional. No local human interval label is supplied by the score. Twenty-five independent contract assertions pass and were rerun by the parent. [Saved scorer returns, source and historical adverse-case tests, 31 Oct 2026; Internal primary evidence; HIGH for contract, local musical correctness unverified.]
- **Different upstream loss:** all 15 saved Bassoon cases have zero CLAP-only coverage. Inventing coverage 1.0 admits 15 rows, but only 11 pass display cutoff. This is not a deployed method, accuracy result or justified prompt/threshold change. [Executed counterfactual replay, 31 Oct 2026; HIGH for tested mechanism only.]
- **Do not inflate internal changes:** zero public generic rows despite 5,355 internal generic row instances; 169 nongeneric blocked local row instances across 35 overlapping saved IDs are not 169 verified misses. Prefilter evidence absent from other reports stays unknown. [Retained-row accounting, 31 Oct 2026; Internal evidence; HIGH within inspected archive.]
- **Separate downstream policy:** articulation uses pre-display candidates, while role scoring follows final display eligibility. Current scoring code uses transformed AudioSet maxima despite a stale max/mean docstring; this audit establishes no averaging-dilution cause for global/local score differences. [Source/scalar controls and independent review, 31 Oct 2026; HIGH for literal/tested behavior, causal audio explanation unresolved.]

**Decision:** keep production bytes unchanged. Removing the global intersection, unioning local names into global, or realigning articulation is a separate semantic proposal needing evidence and authorization, not an automatic bug fix.

## Next evidence, not an unearned model promotion
1. Preserve the unchanged baseline and report standard.
2. Use a bounded diagnostic intake with exact source identities, known positive/negative masks, explicit unknowns and raw→mapping→coverage→fusion→display stage traces.
3. Separate whole-recording presence, natural section-local audibility, exact identity, family identity and melody-role targets.
4. Before candidate outcomes, freeze task-specific above-tolerance recording incidence, severe/missing handling and category support. Broad genre/audio-type-independent confirmation remains a separate gate.
5. Admit only no-fee rights-evidenced references; estimate any substantial acquisition/inference/training before starting. No large archive downloads by default.

## Earlier chord-readiness work
The previous source-clearance milestone reviewed 16 exact metadata candidates and built human-response validation; no new recording was admitted and no human chord labels were collected. That preparation remains available but does not authorize paid recruitment. The detailed previous-methods chronology is retained in METHODS.md.
