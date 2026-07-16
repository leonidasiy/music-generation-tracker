# Candidate Metric Registry

> Initial exploration opened: 2026-07-16  
> Scope: long-form compositional plan adherence and music instruction following  
> Status labels: **Candidate** = proposed but unvalidated; **Adaptation** = established method transferred to this task; **Speculative** = promising construct with major measurement risk.

> **Current strategy:** M09 / CLPR is the Paper 1 flagship; M01 / HPGA and M04 / PCCM are optional intervention-specific evidence channels; M11 / CRVP is validation infrastructure. The next work item is a minimal prompt-pair pilot with same-prompt null baselines.

## Representation decision — 2026-07-16

**Keep symbolic and native-audio paths open during exploration.** Neither representation will be treated as ground truth. Symbolic and audio estimates are modeled as different, imperfect measurement methods; paired rendered-MIDI experiments will isolate representation effects from transcription and performance effects.

## Rules for this registry

1. New ideas are added as soon as they emerge; they are not presented as validated metrics.
2. Each metric must name its target construct, inputs, baselines, novelty threat, failure cases, and falsification test.
3. Adherence, coherence, musicality, production quality, and preference remain separate.
4. Automatic, oracle/symbolic, and human-conditioned results must be reported separately.
5. Candidate metrics are promoted only after controlled perturbation and held-out-human validation.

## Initial candidate set

### M01 — Hierarchical Plan-Graph Alignment (HPGA)
- **Status:** Candidate; high implementation priority
- **Construct:** Ordered, nested section-form adherence
- **Core idea:** Convert the instruction into a typed hierarchy containing boundaries, section identities, recurrence/contrast edges, and duration ranges. Align an inferred music hierarchy using L-measure, boundary agreement, relation accuracy, and penalized duration warping.
- **Inputs:** Parsed plan; audio/MIDI; beat/bar tracking; multiscale section embeddings; optional human segmentation.
- **Baselines:** Boundary F-score, L-measure, section-label edit distance, uniform segmentation.
- **Novelty threat:** Individual components are established; novelty depends on the typed prompt-derived plan graph and relation diagnostics.
- **Falsification:** Preserve all sections while permuting order, deleting a reprise, or breaking hierarchy. HPGA must decline monotonically and beat bag-of-label baselines on human plan-adherence judgments.
- **Feasibility:** High for symbolic; medium for audio.
- **Established components:** [L-measure](https://pmc.ncbi.nlm.nih.gov/articles/PMC5541043/) and [Foote novelty segmentation](https://ccrma.stanford.edu/workshops/mir2009/references/Foote_00.pdf).

### M02 — Role-Conditioned Motif Recurrence and Transformation (RMRT)
- **Status:** Candidate; high novelty potential
- **Cross-domain inspiration:** Choreographic theme-and-variation, rondo, canon, accumulation, and retrograde
- **Construct:** Requested motif introduction, development, absence, and return without trivial looping
- **Core idea:** Detect motif families and transformation types by section. Reward the requested recurrence role and moderate transformation; penalize leakage into forbidden sections, exact copying when variation was requested, and identity loss.
- **Inputs:** Motif example or first occurrence; section-role schedule; melody/polyphonic representation; transformation-aware matcher.
- **Baselines:** Exact n-grams, DTW, MIREX motif occurrence scores, self-similarity stripe energy.
- **Novelty threat:** Motif discovery is established; contribution must be the dramatic-role schedule and two-sided copy-versus-drift diagnosis.
- **Falsification:** Compare exact copies, valid transformations, and unrelated replacements using human “same idea, varied” judgments.
- **Feasibility:** High for monophonic symbolic; medium-low for polyphonic audio.
- **Transferred source:** [Laban/choreographic transformation vocabulary](https://www.danceedlab.com/wp-content/uploads/2021/05/LMA-Series-Horizontal.pdf). The proposed music metric retains typed recurrence and transformation, not movement semantics.

### M03 — Perceptual Boundary-Evidence Calibration (PBEC)
- **Status:** Candidate; medium implementation priority
- **Cross-domain inspiration:** Film cuts and cognitive event segmentation
- **Construct:** Whether requested boundaries are perceptually signaled and unrequested boundaries avoided
- **Core idea:** Fuse feature-specific novelty curves for harmony, timbre, register, dynamics, density, rhythm, and instrumentation into a calibrated boundary probability. Compare it with a soft target density around planned boundaries.
- **Inputs:** Planned boundaries; feature novelty curves; listener-click calibration subset.
- **Baselines:** Foote novelty, boundary F-score, single-feature novelty.
- **Novelty threat:** Novelty functions and boundary detectors are established; the fused, instruction-conditioned, listener-calibrated posterior is proposed.
- **Falsification:** Listener boundary clicks must distinguish true planned boundaries from surface accents and recording artifacts.
- **Feasibility:** Medium-high.
- **Established component:** [Foote novelty segmentation](https://ccrma.stanford.edu/workshops/mir2009/references/Foote_00.pdf). **Validation precedent:** [hierarchical annotation disagreement](https://pmc.ncbi.nlm.nih.gov/articles/PMC5541043/).

### M04 — Planned Contrast–Cohesion Margin (PCCM)
- **Status:** Candidate; high implementation priority
- **Construct:** Same/varied sections remain related, contrast sections remain distinct, and sections remain internally coherent
- **Core idea:** Use typed relation edges over section embeddings. Compute margins between requested recurrence pairs and requested contrast pairs, channel by channel, after correcting for ordinary temporal proximity.
- **Inputs:** Section boundaries; relation graph; melody, harmony, rhythm, timbre, and instrumentation embeddings.
- **Baselines:** Binary SSM-template correlation, silhouette score, pairwise clustering F-score.
- **Novelty threat:** Close to metric learning and SSM loss; typed relations and feature decomposition must add measurable value.
- **Falsification:** Swap relation labels and independently perturb melody, rhythm, or instrumentation. The corresponding channel—not all channels—should fail.
- **Feasibility:** High.
- **Established component:** self-similarity and relation comparison; [hierarchical structure evaluation](https://pmc.ncbi.nlm.nih.gov/articles/PMC5541043/) is a validation baseline, not evidence for the proposed typed margin.

### M05 — Boundary Bridging and Enjambment Index (BBEI)
- **Status:** Adaptation; unvalidated for music instruction evaluation
- **Cross-domain inspiration:** Continuity editing, poetic enjambment, and narrative entity persistence
- **Construct:** Requested transition type: seamless, hard cut, bridged discontinuity, overlap, interruption, or unresolved continuation
- **Core idea:** Separate surface discontinuity from bridging continuity. A large orchestration change with a continuing melody should differ from an unrelated hard cut.
- **Inputs:** Cross-boundary feature distance; motif/voice persistence; common tones; rhythmic continuation; overlap; phrase-resolution evidence.
- **Baselines:** Boundary novelty magnitude and adjacent-window embedding distance.
- **Novelty threat:** “Musical enjambment” is useless unless the two perceptual dimensions are independently validated.
- **Falsification:** Listeners must independently rate abruptness and continuity for matched transition pairs.
- **Feasibility:** Medium-high for basic features; medium for phrase dependency.
- **Transferred sources:** [film continuity/discontinuity editing](https://pmc.ncbi.nlm.nih.gov/articles/PMC9684412/), [narrative entity persistence](https://aclanthology.org/J08-1001.pdf), and [automatic enjambment detection](https://dh2017.adho.org/abstracts/485/485.pdf). The retained invariant is formal boundary plus continuing dependency; the analogy fails if listeners do not perceive abruptness and continuity separately.

### M06 — Pacing Envelope Concordance (PEC)
- **Status:** Adaptation; unvalidated for music instruction evaluation
- **Cross-domain inspiration:** Film cutting-rate and shot-duration curves
- **Construct:** Requested acceleration, deceleration, build, interruption, and climax timing
- **Core idea:** Build a multichannel pacing trajectory from onset density, harmonic-change rate, timbral-change rate, boundary density, loudness motion, and texture change. Compare against the target envelope with rank correlation, constrained DTW, and peak-location error.
- **Inputs:** Beat-synchronous features; prompt-derived target envelope; style-conditioned normalization corpus.
- **Baselines:** Tempo-only, loudness-only, onset-density-only curves.
- **Novelty threat:** Most ingredients are established; value depends on multidimensional instruction-conditioned validation.
- **Falsification:** Manipulate tempo, density, harmony rate, and timbral activity independently; human pacing judgments must support multiple channels.
- **Feasibility:** High.
- **Transferred source:** [Cinemetrics discussion of shot-length and cutting-rate analysis](https://cinemetrics.uchicago.edu/article/616e7ecc-7915-4768-b84d-7dec79aa77c2). The 2022 [movie-editing experiment](https://pmc.ncbi.nlm.nih.gov/articles/PMC9684412/) supports cut-type effects on perceived duration, not the full pacing-envelope proposal.

### M07 — Tension-Arc Adherence and Resolution Debt (TAARD)
- **Status:** Candidate; medium risk
- **Construct:** Requested buildup, climax, relaxation, and resolution
- **Core idea:** Estimate multidimensional tension from harmony, loudness, density, register, roughness, tempo, and expectation. Score ordinal arc constraints, climax location, and **resolution debt**, provisionally defined as residual tension above a style- and opening-calibrated endpoint target plus renewed upward tension motion inside the requested resolution interval.
- **Inputs:** Plan constraints; audio/MIDI features; tonal or tonal-free tension model; listener tension curves for calibration.
- **Baselines:** Loudness, density, tonal strain, target-curve DTW.
- **Novelty threat:** Tension estimation is established; novelty depends on natural-language arc constraints, channel attribution, and resolution debt.
- **Falsification:** Metric must not mistake louder audio for greater harmonic tension and must generalize beyond one tonal style.
- **Feasibility:** High for tonal symbolic; medium for audio; low outside calibrated idioms.
- **Established component and validation precedent:** [continuous listener tension trajectories and feature-specific time windows](https://pmc.ncbi.nlm.nih.gov/articles/PMC3874841/). Resolution debt is proposed, not established.

### M08 — Expectation-Regime Schedule Divergence (ERSD)
- **Status:** Candidate; mathematically promising, representation-sensitive
- **Construct:** Whether sections establish requested regimes of stability, uncertainty, surprise, development, and return
- **Core idea:** Track predictive entropy and realized surprisal at multiple scales using a style model plus within-piece memory. Compare each section’s joint distribution with a **target role distribution**, initially an empirically estimated distribution from human pieces and listener-labeled sections playing the same role. A return should become more predictable when within-piece memory is enabled.
- **Inputs:** Symbolic events or reliable transcription; style-matched expectation model; section roles.
- **Baselines:** Mean surprisal, perplexity, entropy alone, generic versus style-matched models.
- **Novelty threat:** Entropy and surprisal are established; novelty is the role schedule and long-term-versus-within-piece memory return test.
- **Falsification:** Must distinguish random errors from intentional surprise and exact looping from memory-supported thematic return.
- **Feasibility:** High for melody; medium-low for full audio.
- **Established component:** [IDyOM, entropy, surprisal, and long-/short-term memory](https://onlinelibrary.wiley.com/doi/10.1111/j.1756-8765.2012.01214.x). The section-role schedule is proposed.

### M09 — Counterfactual Localized Plan Responsiveness (CLPR)
- **Status:** Candidate; strongest model-level control diagnostic
- **Cross-domain inspiration:** Meaningful agency in interactive narrative
- **Construct:** Whether changing one instruction causes the requested local change without needless collateral changes
- **Core idea:** Generate minimal prompt contrasts with matched seeds. Report target effect, direction accuracy, off-target leakage, boundary spillover, and uncertainty across seeds.
- **Inputs:** Repeatable generator access; minimal prompt pairs; section alignment; relevant feature detectors or human pairwise labels.
- **Baselines:** Same-prompt repeated generations, prompt shuffle, control-token ablation, independent-seed variance.
- **Novelty threat:** Causal contrasts are standard in ML; novelty is localized long-form music plan evaluation.
- **Falsification:** Opposing instructions must produce opposing local effects while unrelated sections remain more stable than target sections.
- **Feasibility:** High with seed control; medium without it; impossible from isolated outputs.
- **Transferred source:** [objective interactive-narrative metrics](https://access.archive-ouverte.unige.ch/access/metadata/d6a5eec8-adfb-4d4f-b399-031ac0cbd3b9/download), where option count is distinguished from consequential agency. The music analogue is clause-specific consequence with preservation of unrelated state. **Causal foundation:** [Rubin](https://doi.apa.org/doi/10.1037/h0037350).

### M10 — Setup–Payoff Connectivity (SPC)
- **Status:** Speculative; research-only
- **Cross-domain inspiration:** Causal narrative networks
- **Construct:** Long-range setup, return, resolution, and structural consequence
- **Core idea:** Build a directed graph from introduced motifs, unresolved harmonies, timbres, or processes to later transformations/resolutions. A provisional setup/payoff edge requires transformation or resolution evidence exceeding similarity and temporal-distance nulls. Measure requested setup/payoff coverage, payoff delay, unresolved setup rate, and event centrality.
- **Inputs:** Motif/harmony/process annotations; human causal-relatedness subset; permutation nulls.
- **Baselines:** Similarity-only and temporal-distance-only edges.
- **Novelty threat:** “Causality” may be an unjustified metaphor. Treat edges as perceived dependency until counterfactual listener evidence exists.
- **Falsification:** Use matched edits that preserve the payoff and surrounding production while removing or replacing only the alleged setup. If perceived relatedness, comprehensibility, or payoff satisfaction does not decline beyond edit-artifact controls, the edge is merely similarity.
- **Feasibility:** Medium-low.
- **Transferred source:** [causal-event networks in narrative](https://pmc.ncbi.nlm.nih.gov/articles/PMC11305923/). “Causal” remains a perceptual dependency hypothesis in music.

### M11 — Cross-Representation Validity Profile (CRVP)
- **Status:** Validation work package; not a headline metric. Use paired representation/renderer perturbations, agreement analyses, and held-out-pipeline sensitivity checks. Fit MTMM only if indicator count, identification, and simulation-based power are adequate.
- **Cross-domain inspiration:** Psychometric multi-trait multi-method analysis, measurement invariance, and method-comparison studies without a gold standard
- **Construct:** Whether a proposed musical trait is measured robustly across symbolic and audio representations—or whether conclusions are dominated by representation-specific artifacts
- **Core idea:** Model multiple traits jointly, with at least three indicators per trait and method, on paired symbolic/rendered-audio pieces. Pre-specify an identifiable MTMM model, its constraints, matched cross-method anchors, and simulation-based sample-size requirements. Report common-factor, method, and residual variance separately; add absolute/rank agreement and bootstrap uncertainty.
- **Inputs:** Paired MIDI/MusicXML and multiple audio renders; optional aligned human performances; multiple traits; at least three indicators per trait/method; explicitly matched or anchored cross-method indicators; bootstrap resamples; controlled confound perturbations; human construct judgments for external validity.
- **Diagnostic outputs:** **CRVC**, provisionally the model-estimated share of variance associated with a cross-method common factor—not yet the target trait until externally validated; **RSAA**, bias- and bootstrap-adjusted cross-method rank agreement; **MISD**, median standardized divergence between linked method-specific latent scores, reported only when the required scale-linking or scalar/alignment invariance assumptions hold.
- **Baselines:** Pearson/Spearman correlation, raw mean absolute difference, ICC for consistency and absolute agreement, Bland–Altman limits, symbolic-only and audio-only rankings.
- **Novelty threat:** MTMM, invariance testing, ICC, generalizability theory, and Bland–Altman analysis are established. The publishable contribution would be their preregistered adaptation to music-generation metric validation, paired rendering design, and evidence that naïve comparisons reach different conclusions.
- **Falsification:** Perturbations that preserve a trait across rendering changes should remain stable; production-only perturbations should change audio-only traits but not symbolic-content traits. Shared-confound interventions must show whether common variance is actually the intended construct. The metric fails if tempo masquerading as rhythmic complexity.
- **Feasibility:** Medium-low until identification and power simulations are complete. Statistical methods are available, but credible factor modeling needs multiple jointly modeled traits, anchored indicators, adequate sample size, held-out renderers, and human validation.
- **Measurement warning:** High cross-method agreement is not proof of construct validity; both methods can share the same confound.
- **Foundations:** [Campbell & Fiske’s MTMM framework](https://doi.org/10.1037/h0046016), [measurement-invariance practice](https://pmc.ncbi.nlm.nih.gov/articles/PMC5145197/), [why invariance is insufficient by itself](https://pmc.ncbi.nlm.nih.gov/articles/PMC11562939/), and [audio–sheet correspondence without transcription-as-truth](https://arxiv.org/abs/1707.09887).

## Competitive update — 2026-07-16

The newest benchmark scan changes the paper strategy:

- **M09 CLPR is promoted to the flagship contribution.** SongEval, MusicEval, MAD/MusicPrefs, AIME, and CMI-RewardBench already cover global aesthetics, preference, broad alignment, or multimodal instruction scoring. SegTune and related systems add segment-level alignment, but observational segment similarity does not establish that a changed instruction caused the requested local change.
- **M01 HPGA and M04 PCCM become optional, preregistered structural evidence channels alongside CLPR**, not independent headline metrics. Report them only for interventions that alter a section boundary, identity, order, duration, recurrence, variation, or contrast relation; they are not required components of a universal CLPR aggregate.
- **M11 CRVP becomes validation infrastructure**, not a claim that cross-representation psychometrics is novel. MTMM, generalizability theory, invariance, ICC, and Bland–Altman analysis are established. The substantive contribution would be showing which music-plan traits survive representation and renderer changes.
- **M02, M03, M06, and M07 remain optional subtests.** Motif transformation, boundaries, pacing, and tension all have substantial prior work; including all of them in Paper 1 would weaken coherence and inflate annotation cost.
- **M05, M08, and M10 are deferred.** They remain useful exploratory hypotheses but are not required to establish the core localized instruction-responsiveness claim; hierarchical evidence is optional and intervention-specific.

### M09 operational profile

For intervention `i`, piece `j`, repeated generation `s`, minimally different prompts `p0` and `p1`, target interval `T`, and predeclared protected regions, report five outputs:

1. **Target Effect Size (TES).** For a preregistered scalar feature `f_i` and requested direction `d_i ∈ {-1,+1}`, define `ΔT_ijs = f_i(y1_ijs,T_ij) - f_i(y0_ijs,T_ij)`. Standardize the signed contrast `d_i ΔT_ijs` using a null scale estimated from held-out same-prompt replicate differences within preregistered generator × genre × section-type strata. For vector features, preregister the scalar projection or distance and its direction. Pieces and intervention types—not seeds—are the principal independent units.
2. **Directional Accuracy (DA).** Average the signed target contrast across repeated generations for each piece × intervention unit, then report the fraction whose direction is positive. Also report a noise-exceedance version using a threshold fixed from held-out same-prompt null contrasts. Resample pieces and interventions for uncertainty.
3. **Off-Target Leakage (OTL).** Preregister distal or semantically protected region–feature cells. Excluding a boundary halo, compute absolute intervention changes divided by cell-specific held-out same-prompt null scales, then combine with fixed weights. Report same-feature leakage and cross-feature collateral change separately.
4. **Boundary Spillover (BS).** Report a distance-indexed curve of absolute standardized change in non-overlapping rings immediately outside the target boundary. A preregistered halo AUC or decay length is secondary. The halo is excluded from OTL, so BS measures near-boundary decay while OTL measures distal or semantically protected change.
5. **Plan Relation Delta (PRD).** Use only when one plan edge or structural constraint changes. For evidence function `q(y;e,r)` and intervention from relation `r0` to `r1`, report the contrast-in-contrasts `[q(y1;e,r1)-q(y1;e,r0)] - [q(y0;e,r1)-q(y0;e,r0)]`, standardized against same-prompt null contrasts. Report unaffected-edge change separately as structural leakage; otherwise mark PRD not applicable.

With defensibly matched seeds, TES estimates a paired controlled-generator intervention effect. Without seed coupling, estimate a repeated-sample average intervention effect and do not call individual output pairs counterfactuals. TES/DA characterize target response; OTL/BS characterize distinct distal and near-boundary collateral effects; PRD is an optional structural explanation. These outputs are dependent and are not five separate discoveries. No aggregate is primary until human judgments establish a defensible weighting; report compliance separately from quality and preference.

### Systematic questions for the narrowed paper

1. Which instruction types admit a minimal intervention whose intended acoustic or symbolic effect is independently measurable?
2. Can generator randomness be matched strongly enough for counterfactual comparisons, or must same-prompt variance define a weaker baseline?
3. Which target intervals are known from the prompt, and which require uncertain alignment after generation?
4. How should TES be standardized when feature variance differs by genre, section type, and generator?
5. Do TES, DA, OTL, BS, and applicable PRD conclusions remain stable when using alternative audio embeddings, beat trackers, or transcribers?
6. Can HPGA and PCCM localize the failure better than segment CLAP/MuLan similarity?
7. Do global metrics remain unchanged when a musically important instruction is moved to the wrong section?
8. Can a model game the metric through abrupt boundaries, exaggerated instrumentation, or excessive repetition?
9. Which controlled corruptions isolate section order, relation, timing, instrumentation, and dynamics without creating obvious edit artifacts?
10. How many independent compositions, prompt pairs, seeds, renderers, and listeners are needed for stable effect estimates?
11. Do musicians and general listeners agree on instruction compliance even when they disagree on preference?
12. Are compliance judgments separable from production quality, loudness, familiarity, and memorability?
13. Which findings generalize to an unseen generator, prompt template, renderer, genre, and duration range?
14. Does audio–symbolic disagreement reflect representation error, transcription error, renderer effects, or genuine construct ambiguity?
15. Can track-level bootstrap and multi-pipeline sensitivity envelopes preserve calibrated uncertainty without pretending detector activations are probabilities?
16. What open models can actually generate long enough outputs and expose repeatable randomness at tolerable compute cost?
17. What annotation design gives sufficient reliability without making full-song expert listening financially prohibitive?
18. Would reviewers see the contribution as one localized instruction-responsiveness benchmark with optional hierarchical channels, or as a loose bundle of established MIR measurements?

## Revised implementation order

1. CLPR counterfactual prompt-pair pilot with same-prompt variance baselines
2. HPGA + PCCM as localized structural evidence channels
3. Paired symbolic/audio/renderer perturbation benchmark for CRVP-style validation
4. Human compliance study separated from preference and quality
5. PBEC or RMRT only if they explain residual human judgments
6. PEC/TAARD only after the core benchmark is stable
7. BBEI, ERSD, and SPC deferred from Paper 1

## Systematic questions for the dual-representation stage

1. Which target constructs have operational definitions that remain meaningful in both symbolic and audio domains?
2. Which constructs are inherently representation-specific and should never be forced into a cross-domain score?
3. What three or more indicators can measure each shared trait in each representation?
4. Which symbolic features survive rendering, and which expressive audio features have no symbolic counterpart?
5. How much do renderer, soundfont, tempo, dynamics, and room simulation alter audio-side rankings?
6. How much do transcription, source separation, beat tracking, and segmentation errors alter downstream metric values?
7. Can paired rendered MIDI separate representation error from transcription error and human-performance variation?
8. Which human-performance datasets can test whether findings survive beyond synthetic rendering?
9. Do the same factor structures emerge for symbolic and audio indicators?
10. If metric or scalar invariance fails, which comparisons remain defensible?
11. Are ranking conclusions stable under bootstrap resampling and held-out renderers?
12. Do genre, instrumentation, polyphony, duration, or production quality moderate representation disagreement?
13. Can automatic confidence estimates be propagated into uncertainty intervals for final metric outputs?
14. Does a metric correlate with human judgments after controlling for tempo, loudness, density, and production quality?
15. Can controlled perturbations independently target musical content and surface production?
16. Which conclusions change when using oracle symbolic annotations, automatic audio estimates, and human annotations?
17. What sample size is required for reliable latent-variable and invariance tests?
18. Should cross-representation robustness be a publication contribution, a validation gate, or both?

## Open design questions

1. **Answered:** keep symbolic and audio representations open during exploration; use paired tracks for calibration rather than selecting a winner now.
2. Which genres and formal vocabularies define the first scope?
3. What minimum duration qualifies as long-form for the core benchmark?
4. Will source stems or multitracks be available for instrument-entry ground truth?
5. Can tested generators expose deterministic or approximately matched seeds?
6. Is the primary publication target ISMIR, an ML evaluation venue, or a thesis/workshop?
7. What listener population is realistically available: musicians, arrangers, general listeners, or all three?

## Core sources

- McFee et al. (2017), hierarchical L-measure: https://pmc.ncbi.nlm.nih.gov/articles/PMC5541043/
- Foote (2000), audio novelty segmentation: https://ccrma.stanford.edu/workshops/mir2009/references/Foote_00.pdf
- Pearce & Wiggins (2012), information dynamics and musical expectation: https://onlinelibrary.wiley.com/doi/10.1111/j.1756-8765.2012.01214.x
- Farbood & Upham (2013), listener tension trajectories: https://pmc.ncbi.nlm.nih.gov/articles/PMC3874841/
- SymPAC (2024), prompted and constrained symbolic generation: https://arxiv.org/abs/2409.03055
- Movie editing and time perception (2022): https://pmc.ncbi.nlm.nih.gov/articles/PMC9684412/
- Barzilay & Lapata (2008), entity-grid coherence: https://aclanthology.org/J08-1001.pdf
- Chen & Bornstein (2024), causal narrative structure: https://pmc.ncbi.nlm.nih.gov/articles/PMC11305923/
- McManus et al. (2011), empirical limits of visual balance: https://pmc.ncbi.nlm.nih.gov/articles/PMC3485801/
- Yamu et al. (2021), space syntax and intelligibility: https://www.mdpi.com/2071-1050/13/6/3394
- Dance Education Laboratory, Laban movement analysis: https://www.danceedlab.com/wp-content/uploads/2021/05/LMA-Series-Horizontal.pdf
- Peyré et al. (2016), Gromov–Wasserstein comparison: https://proceedings.mlr.press/v48/peyre16.pdf
- Eckmann et al. (1987), recurrence plots: https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B92%5D.pdf
- Brier (1950), probabilistic forecast verification: https://journals.ametsoc.org/view/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.xml
- Rubin (1974), causal effects: https://doi.apa.org/doi/10.1037/h0037350
- Dorfer et al. (2017), audio–sheet correspondence: https://arxiv.org/abs/1707.09887
- Putnick & Bornstein (2016), measurement invariance conventions: https://pmc.ncbi.nlm.nih.gov/articles/PMC5145197/
- Protzko et al. (2024), invariance is not sufficient for valid comparison: https://pmc.ncbi.nlm.nih.gov/articles/PMC11562939/
- Ycart et al. (2024), musically informed transcription evaluation: https://arxiv.org/abs/2406.08454
- PIAST multimodal audio/symbolic/text dataset (2024): https://arxiv.org/abs/2411.02551
- Unified score/symbolic/audio translation (2025): https://arxiv.org/abs/2505.12863

## Competitive and robustness sources — added 2026-07-16

- SongEval, full-length song aesthetics and structure clarity: https://arxiv.org/abs/2505.10793
- CMI-RewardBench, compositional multimodal instruction reward evaluation: https://arxiv.org/abs/2603.00610
- SegTune, segment-level song control and alignment metrics: https://arxiv.org/abs/2510.18416
- MAD / MusicPrefs, human-aligned distributional music evaluation: https://arxiv.org/abs/2503.16669
- AIME human preference benchmark: https://arxiv.org/abs/2506.19085
- Ycart et al., perceptual validity of piano-transcription metrics: https://transactions.ismir.net/articles/10.5334/tismir.57
- Hu et al., musically informed piano-transcription evaluation: https://arxiv.org/abs/2406.08454
- Marták et al., sound and music biases in transcription models: https://link.springer.com/article/10.1186/s13636-025-00428-z
- Mauch & Ewert, Audio Degradation Toolbox robustness benchmark: https://sebewert.github.io/publications_pdf/2013_MauchEwert_AudioDegradationToolbox_ISMIR.pdf
- Davies & Böck, evaluation measures for beat tracking: https://archives.ismir.net/ismir2014/paper/000238.pdf
- McLeod & Steedman, MV2H and disjoint symbolic penalties: https://arxiv.org/abs/1906.00566
- Eid et al., MTMM models for structurally different and interchangeable methods: https://doi.org/10.1037/a0013219
- Nussbeck et al., sample-size requirements for ordinal MTMM models: https://pubmed.ncbi.nlm.nih.gov/16709286/
- Bland & Altman, why correlation is not method agreement: https://pubmed.ncbi.nlm.nih.gov/2868172/
