# Candidate Metric Registry

> Initial exploration opened: 2026-07-16  
> Scope: long-form compositional plan adherence and music instruction following  
> Status labels: **Candidate** = proposed but unvalidated; **Adaptation** = established method transferred to this task; **Speculative** = promising construct with major measurement risk.

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

## Initial implementation order

1. HPGA
2. PCCM
3. CLPR
4. PBEC
5. RMRT on symbolic melody
6. PEC
7. TAARD on tonal symbolic music
8. ERSD on melody/chord representations
9. BBEI after a transition-listening pilot
10. SPC only after human construct validation

## Open design questions

1. Should the first benchmark use symbolic music, rendered symbolic music, native generated audio, or parallel tracks?
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
