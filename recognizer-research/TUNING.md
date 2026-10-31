# Threshold tuning and root-focused chords —31October2026

## Executive summary
Threshold/blend tuning reduced development instrumentation failures 88/292→73/292 (25.00%), but mixed diagnostic transfer prevents a task-wide below30% claim. Soft chord readout improves roots, whereas learned transition history and a newly fitted small quality head do not solve chord-quality errors. Actual application remains unchanged; research findings, not deployment approval.

## Key findings — executed counts, high confidence in computation; generalization unconfirmed
1. Instrumentation: head threshold0.30, head weight0.75 chosen on original295development recordings only; all5artist-grouped outer folds selected the same pair. Cross-fitted failures88/292→73/292, severe15→11, FP48→44, FN57→42, missing0. Fixed hybrid had84/292failures,FP69,FN29; tuning trades some recall for fewerfalsepositives.
2. Inspected diagnostics, never used to rank parameters: old34cohort28scorable baseline12/fixed13/tuned10; new49cohort47scorable baseline19/fixed14/tuned15 (31.91%). Tuned transfer is not uniformly better. Publisher training/checkpoint-selection exposure remains.
3. Display cutoff stays inclusive0.20; explicit monotone decision-score remapping shifts the head threshold, then blends with baseline. This is not probability calibration. Only11existing singleton names change after Music≥0.50; coarse/world/Vocal identities and current-global section ownership remain unchanged.
4. Chords: all60recordings×6oldvariants replayed, zero original-score mismatches. The original triad score already ignored bass equality; genuine inversion acceptance is not a new model gain. There is a separate bass-insertion/omission representation effect, so strict bass-stripped metrics must be labeled separately and retain explicit omissions. Root-only discards quality errors, not merely inversions.
5. Newly extracted soft acoustic logits on all60clips exactly reproduce the original baseline. Baseline root-only duration error24.67%→19.98% for a fixed soft readout; recordings exceeding30%rooterror20/60→16/60(26.67%). At historical40%within-recording tolerance14/60→11/60. Root+triad failures30/60→29/60 at40%tolerance; durationerror45.95%→44.89%. The40%tolerance is provisional historical sensitivity, not a newly validated utility threshold.
6. Same-emission duration/history comparison: duration-only29/60triadfailures, rootdurationerror20.00%; learned history29/60,rooterror20.26%. Thus first-order harmonic history did not beat the simpler control. Five saved outer-fold transition models plus30auxiliary inner-fold fits; no test reference history fed into decoding. Fifteenstyle/progressionprefixes are blocked as proxies, not certified independent compositions; all data are inspected guitar development.
7. Actual supervised training:65convexquality-head fits, five saved outer-fold models;13learned coefficients each plus training-only normalization. Root+triad failures remain29/60 and durationerror45.16%, worse than simple softreadout44.89%; at30%within-recording tolerance qualityfailures36/60 versussoft34/60. Consonancebackbone not retrained; trained head rejected for adoption.

## Structural ceiling — diagnostic, not achieved performance
With only24major/minorchords plusN, even a perfect-timing reference-informed oracle has at least22/60failures at40%within-recording error tolerance under originaltriads. Under the separately bass-contribution-stripped policy the floor is20/60. Both exceed a strict<30%recording-failure target: retaining that vocabulary while training a larger network cannot clear the quality endpoint on these references. This is a representation/vocabulary ceiling, not an achieved recognizer score or independent annotation consensus.

## Contradictions and limits
- Development tuning improves overall incidence but worsens the new49diagnostic versusfixedhybrid; thresholds are not selected from those diagnostic results.
- Root-only can satisfy a development target while chord quality still fails. Quality errors have not been silently forgiven.
- More history and actual training did not outperform the simpler readout. This rejects these specific interventions, not all sequence models or fine-tuning.
- References are sparse or annotation-construction-dependent; all chord clips are solo-guitar comping. No whole-song, broad genre/audio-type or untouched confirmation result.
- Unknown references remain unknown. N, X, missing and ambiguous intervals remain distinct; abstention is not discarded as easy time.
- Chord severe>80% panels are explicitly exploratory sensitivity only, not an accepted severe-error tier.

## Next steps and recommendation
Keep tuned instrumentation and soft-root readout as research candidates; no default switch based on inspected diagnostics. Establish broader licensed independent development/confirmation sources and whole-song aggregation. For chord quality, evaluate an explicit richer vocabulary/omission policy before expensive backbone retraining; for owner-priority roots, confirm the simple readout on varied audio before adding architecture complexity. Resolve whether quality errors themselves are acceptable rather than assuming inversion permission also waives quality. No paid annotations/services.

## Evidence
- [Machine-readable curated results](tuning-root-summary.json)
- [Previous PaSST comparison](INSTRUMENTS.md)
- Fresh primary-source feasibility check: [2017negative](https://arxiv.org/abs/1702.00178), [2018duration/language](https://arxiv.org/pdf/1808.05335), [2026eventmodel](https://arxiv.org/pdf/2604.24386), [Consonance](https://github.com/andreamust/consonance-ACE), [GuitarSetpublisher](https://zenodo.org/records/3371780). Author reports/releases are not local comparative proof; availableweights/licensing require exactartifact checks. ChordFormer README checkpoint claims were not verified by the fresh tree/API check, so no installation/superiority claim.

## Stronger content-family transfer and reviewer corrections
Publisher documentation plus actual instructed chord content verifies THREE cross-genre templates (21/21/18clips), not15independentharmonicgrammars. The prior fivefold15prefix analysis is retained only as arrangement-blocked sensitivity. A separately frozen leave-one-content-family-out comparison (3outer/2innerfolds) holds every style/performer/key/tempo of a template together. These are leakage-control groups, not certified independent compositions or fresh test data.

The additional comparison completed27supervisedqualityfits,3savedheads,zero single-class no-fit fallbacks; across both studies92actualfits and8savedheads. All60clips/5arms complete,zero fullymissing. Newqualityhead durationerror45.37% (historicaltriads), again worse than simple44.89%; no rescue of thequalitytarget. Transition work totals8savedoutermodels plus42auxiliaryinnerfitcalls (50countfits), not50savedmodels.

Each row below: original triad durationerror / strictly bass-stripped triad durationerror; failurecounts at historical40%within-recording tolerance, out of60. Strictstripping removes bass contribution but preserves explicitly omitted tones; it is a separately named policy, not a rewrite of historicalscores.
- baseline: 45.95% / 43.21%; failures30/60 / 27/60.
- soft_no_history: 44.89% / 42.11%; failures29/60 / 27/60.
- duration_selected: 44.69% / 41.92%; failures29/60 / 27/60.
- history_selected: 44.87% / 42.10%; failures29/60 / 27/60.
- trained_quality_head: 45.37% / 42.59%; failures29/60 / 27/60.

Training-label caveat: quality fitting used the historical bass-augmented triad bitmap, not strictly bass-stripped targets;26annotation spans totaling56.496104seconds differ. Inference uses no bass feature, but that is not proof of fully inversion-invariant supervision. The root softmax is frozen; joint root/quality argmax can still change the decoded root. Unsupported dim/aug/sus/omission patterns cannot be represented by a forcedmajor/minor/Nhead.

Known-coverage caveat: new25state arms replace X with forcedmajor/minor/Npredictions; baseline X=134.209160seconds. This is an explicit output-policy change in research, not neutral plumbing or an adopted public API. Every eligible reference interval remains in evaluation; allarms retain the tiny uncovered annotation tail. Auxiliary innerpredictions were not retained, so independent audit reconstructs outerpredictions and models and checks innerselection from savedcandidate summaries, not a claimed independent rerun of every innerprediction.
