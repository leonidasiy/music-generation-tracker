# Instrument-presence detection: PaSST matched comparison

## Executive summary
PaSST-assisted instrument presence reduced observed-reference failure recordings from 19/47 (40.43%) to 14/47 (29.79%). Misses 12→7; false positives 8→8; severe 1→1; missing0. Eight recordings rescued, three regressed. 49 intended ten-second recordings,29 artist groups,47 scorable/99 sparse observed nonvoice pairs. PublisherTEST was used for checkpoint selection; this is bounded development evidence, not independent final confirmation or full-inventory accuracy. Application not modified; full-song aggregation remains untested. Wider historical regression is mixed: 100/320→97/320 failures, FN64→32 but FP55→79; keep the candidate experimental, not default.

## Key findings
- Actual matched inference completed on all49 recordings plus4 synthetic controls for each arm (106 receipts), with zero failures. Both arms bind original and decoded-wave identities; baselineMPS and headCPUfloat32 are explicit. [matched baseline/head summaries;31Oct2026;Executed technical evidence;HIGH scoped]
- The prespecified zero-observed-error recording-failure gate passes numerically. This is not a complete audible-instrument inventory accuracy claim. [matched-results.json and independent verifier;31Oct2026;Executed reference-proxy comparison;HIGH scoped counts]
- Candidate threshold/weights/classes/music gate were fixed before outcomes. No fitting, fine-tuning or threshold sweep occurred. The rejected calibrator remains rejected; its new-cohort output is diagnostic only. [MATCHED-FREEZE.json;31Oct2026;Executed provenance;HIGH scoped]
- All4 synthetic null controls gain no final instrument names; digital silence preserves the baseline bypass despite nonzero raw PaSST scores. [matched-results.json;31Oct2026;Executed controls;HIGH scoped]
- Independent stdlib reconstruction verifies all4 arms, final projection, sparse masks, class/category counts and paired results. It does not independently re-decode audio or regenerate family headings. [outcome-verifier/verdict.json and parent rerun;31Oct2026;Independent technical review;HIGH scoped]
- No actual application files were edited. Integration and complete-report smoke are separate from this clip-level result. [application preservation receipt;31Oct2026;Technical evidence;scope constrained]

## Comparative scoring
Primary: fraction of intended reference-scorable recordings with >=1 observed-class disagreement. Severe means >=2 disagreements; missing is separate. All19 nonvoice classes remain in accounting. Unknown/tie/duplicate observations are excluded, not converted to negatives.

- **baseline**: failures19/47 (40.43%); severe1, missing0; TP31, FP8, FN12, TN48; observed-pair precision79.49%, recall72.09%.
- **passt_hybrid**: failures14/47 (29.79%); severe1, missing0; TP36, FP8, FN7, TN48; observed-pair precision81.82%, recall83.72%.
- **rejected_calibrator_diagnostic**: failures17/47 (36.17%); severe0, missing0; TP36, FP10, FN7, TN46; observed-pair precision78.26%, recall83.72%.
- **passt_native05_diagnostic**: failures15/47 (31.91%); severe3, missing0; TP26, FP1, FN17, TN55; observed-pair precision96.30%, recall60.47%.

The native0.50 head is a coarse-class diagnostic, not a fine-name replacement. It has fewer FP but more FN and severe recordings; therefore PaSST-alone is not interchangeable with the tested hybrid.

Paired changes: 8 rescued/3 regressed; net5 fewer observed-failure recordings. Artist-macro candidate-minus-baseline failure fraction -0.074713. Descriptive5000artist-cluster95% interval: [-25.00,2.44] percentage points. It crosses zero; not statistically secure population evidence.

## Class-specific results
Counts are sparse and do not establish all-class superiority. Format: positive/negative support; baseline TP/FP/FN/TN → hybrid TP/FP/FN/TN.

- accordion: support0/4; 0/2/0/2 → 0/0/0/4
- banjo: support1/4; 0/2/1/2 → 0/1/1/3
- bass: support1/2; 1/1/0/1 → 1/1/0/1
- cello: support1/2; 1/0/0/2 → 1/0/0/2
- clarinet: support1/3; 0/0/1/3 → 1/0/0/3
- cymbals: support4/0; 2/0/2/0 → 2/0/2/0
- drums: support1/2; 1/0/0/2 → 1/0/0/2
- flute: support3/5; 2/0/1/5 → 2/1/1/4
- guitar: support2/1; 1/0/1/1 → 1/0/1/1
- mallet_percussion: support1/6; 1/0/0/6 → 1/0/0/6
- mandolin: support3/4; 3/0/0/4 → 2/0/1/4
- organ: support1/2; 0/0/1/2 → 0/0/1/2
- piano: support8/0; 8/0/0/0 → 8/0/0/0
- saxophone: support3/5; 3/1/0/4 → 3/1/0/4
- synthesizer: support3/0; 1/0/2/0 → 3/0/0/0
- trombone: support3/3; 3/0/0/3 → 3/0/0/3
- trumpet: support2/3; 2/1/0/2 → 2/1/0/2
- ukulele: support4/4; 1/0/3/4 → 4/2/0/2
- violin: support1/6; 1/1/0/5 → 1/1/0/5

## Genre and audio-type metadata strata
These categories overlap and must not be summed. They are track metadata, not listening verification. Format: baseline → hybrid failed/scorable recordings.

- broad_genre/classical_chamber: 2/7 → 2/7; intended7.
- broad_genre/electronic_ambient_dance: 5/17 → 4/17; intended17.
- broad_genre/folk_country: 4/8 → 3/8; intended8.
- broad_genre/jazz_blues: 2/3 → 2/3; intended3.
- broad_genre/other_genre: 1/3 → 1/3; intended3.
- broad_genre/rock_punk_metal: 2/4 → 1/4; intended6.
- broad_genre/unknown_genre: 5/8 → 3/8; intended8.
- metadata_instrumental/marked: 3/4 → 3/4; intended4.
- metadata_instrumental/not_marked: 16/43 → 11/43; intended45.

## Contradictions found
- Overall net gain coexists with three regressed recordings and higher false-positive support for some singleton classes. Aggregate FP staying8 does not mean the same errors persisted.
- PaSST alone at0.50 is conservative (one FP) but misses17 observed positives, versus7 in the hybrid. Better precision alone is not the primary objective.
- The local-new-artist split is still publisher validation/checkpoint-selection exposed; local novelty is not model-independent confirmation.
- The previous calibrator selection gain did not survive its own34-case fresh-artist test (12/28→13/28). Its diagnostic17/47 result here does not retroactively overturn that rejection.

## Research gaps and limits
- Primary failure means at least one disagreement on an observed reference class; unknown/unannotated classes are never negatives. Two reference-unscorable recordings remain in inference accounting.
- PaSST publisher TEST served validation/checkpoint selection. New local artist groups do not imply independence from model selection, compositions or pretrained exposure.
- The descriptive artist-cluster95% interval for candidate-minus-baseline failure incidence spans -25.00 to +2.44 percentage points; it includes no difference. No population-level improvement is established.
- Only eleven existing one-to-one singleton names are rescored; eight coarse/multimember classes and Vocal/world vocabulary are unchanged. No new instrument rows are invented.
- These results concern ten-second clips. The prepared local integration must fall back on longer inputs; a first-window score must not be assigned to an entire song. Full-track pooling and section audibility remain separate experiments.
- Genres and marked/not-marked instrumental are overlapping track metadata, not verified excerpt vocal/solo/live/studio conditions. Broad independent final audio-condition coverage remains open.
- Source licence and conditional author weight permission do not establish commercial/hosted/redistribution clearance. No paid annotation/data/compute service was used; existing assistant billing and electricity are excluded.
- The native PaSST0.50 coarse-head diagnostic is not the hybrid or a deployable fine-instrument mapping. Sigmoid scores are not calibrated presence probabilities.

## Implementation and recommendation
Retain the tested PaSST hybrid as a promising bounded candidate. Preserve unchanged application reporting semantics, including sections as a subset of the CURRENT displayed global list. Do not install or claim full-song improvement from a ten-second benchmark. The next substantive step is a separately frozen full-track window/aggregation study and independent diverse references; chord work remains a distinct event-sequence experiment. Current application is unchanged pending explicit integration scope and the remaining release gates.

## Reproduction
- `MATCHED-FREEZE.json` pins206 executable/data/asset inputs before fresh outcomes.
- `matched_run.py --stage baseline`, then `--stage head`; `matched_eval.py` scores the frozen comparison.
- `outcome-verifier/verify.py` independently reconstructs the saved outcomes;17 parent scorer/adapter tests passed.
- Corrected isolated integration:10tests pass, including49-cache parity and current-global section subset. Both baseline and candidate source copies pass227application tests with9skips each. A real paired full-report smoke uses the actual PaSST head, matches frozen displayed globals exactly and preserves section/current-global subset; changed section/lead/articulation inputs are not claimed more accurate.
- Original49OGGs, attribution, acquisition hashes, weights, failed RED logs and per-case inference receipts are retained privately.

## Additional historical regression and integration status
Actual329/329historical head inference completed;320reference-scorable recordings/740observedpairs. Baseline100/320→hybrid97/320 failures; severe17→12; FN64→32 but FP55→79; missing0;36rescued/33regressed. Previously used old34-case subset worsens12/28→13/28. These are development/training-exposed cases, not independent confirmation. Parent reran the waveform/source/score verifier successfully using the application interpreter.
The isolated integration is exercised, not adopted. The first draft wrongly retained baseline-global section membership; parent caught the owner-contract violation, a failing regression test was retained, and the corrected patch preserves CURRENT-global section intersection. Both source copies pass the actual application suite and real paired full-report smoke. Given the wider FP regressions, weak uncertainty and ten-second scope, keep the method experimental rather than enable it by default.

## Primary external sources
- Official released task checkpoint: https://github.com/kkoutini/PaSST/releases/tag/v0.0.5 [Author research release;2022; inspected31Oct2026].
- Task training/validation interface: https://github.com/kkoutini/PaSST/blob/d7049e78e84ba38173ffd779479d1c9ec7d1c116/ex_openmic.py [Author research code; pinned release].
- OpenMIC publisher: https://zenodo.org/records/1432913 [Research dataset;2018].
- Conditional checkpoint licence clarification: https://github.com/kkoutini/PaSST/issues/51 [Author issue response;single evidence lineage;commercial rights unresolved].
