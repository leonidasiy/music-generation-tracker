# References — Music Generation & Orchestration Research

> Last updated: 2026-07-17
> **14 core tracker papers** synchronized with `index.html`, plus metric-design, competitive-benchmark, robustness, psychometric, and cross-domain sources. Citation counts are approximate snapshots and should not be treated as live bibliometrics.

---

## Core Paper 1: CLAP: Contrastive Language-Audio Pretraining
- **Authors:** Benjamin Elizalde, Soham Deshmukh, Mahmoud Al Ismail, Huaming Wang
- **Organization:** LAION / Microsoft
- **Year:** 2022 | **Venue:** ICASSP 2023
- **arXiv:** [2206.04769](https://arxiv.org/abs/2206.04769)
- **Citations:** ~1,220 [HIGH CONFIDENCE]
- **Relevance:** Active

**Key Findings:** Learns joint audio-text representations via contrastive learning. Trained on 4.6M audio-text pairs. Enables zero-shot audio classification and cross-modal retrieval. Foundation for music-text alignment — directly powers prompt engineering and cross-modal analysis research directions. Widely adopted as embedding backbone for music generation evaluation.

**Architecture:** Dual-encoder contrastive (audio + text)
**Modality:** Audio + Text embeddings
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** cross-modal, prompt-engineering

---

## Core Paper 2: MusicGen: Simple and Controllable Music Generation
- **Authors:** Jade Copet, Felix Kreuk, Itai Gat, Tal Remez, David Kant, Gabriel Synnaeve et al.
- **Organization:** Meta
- **Year:** 2023 | **Venue:** NeurIPS 2023
- **arXiv:** [2306.05284](https://arxiv.org/abs/2306.05284)
- **Citations:** ~1,199 [HIGH CONFIDENCE]
- **Relevance:** Active

**Key Findings:** Single-stage transformer LM over compressed discrete tokens. Dual conditioning on text + melody. SOTA on text-to-music benchmarks. Fully open-source via Audiocraft. Ideal starting point for controllability experiments — add conditioning dimensions and measure effect.

**Architecture:** Single-stage Transformer LM + EnCodec tokenizer
**Modality:** Audio (32kHz, mono + stereo)
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** controllability

---

## Core Paper 3: MusicLDM: Enhancing Novelty in Text-to-Music Generation Using Beat-Synchronous Mixup
- **Authors:** Ke Chen, Yusong Wu, Haohe Liu, Marianna Nezhurina, Taylor Berg-Kirkpatrick, Shlomo Dubnov
- **Organization:** UC San Diego / Qualcomm
- **Year:** 2023 | **Venue:** ICASSP 2024
- **arXiv:** [2308.01546](https://arxiv.org/abs/2308.01546)
- **Citations:** ~204 [MEDIUM CONFIDENCE]
- **Relevance:** Active

**Key Findings:** First to adapt Stable Diffusion + AudioLDM to music domain as open-source baseline. Introduces beat-synchronous mixup for training data augmentation, increasing output diversity. Reproducible, well-documented codebase. Excellent starting point for undergrads wanting a trainable text-to-music diffusion model.

**Architecture:** Latent Diffusion (adapted from Stable Diffusion/AudioLDM)
**Modality:** Audio (mel-spectrograms)
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** controllability, efficient-generation

---

## Core Paper 4: MAGNeT: Masked Audio Generation using a Single Non-Autoregressive Transformer
- **Authors:** Alon Ziv, Itai Gat, Gael Le Lan, Tal Remez, Felix Kreuk et al.
- **Organization:** Meta
- **Year:** 2024 | **Venue:** ICLR 2024
- **arXiv:** [2401.04577](https://arxiv.org/abs/2401.04577)
- **Citations:** ~82 [MEDIUM CONFIDENCE]
- **Relevance:** Active

**Key Findings:** Non-autoregressive masked generative modeling for audio. Generates high-quality music in fewer steps via parallel token prediction. Part of Meta's Audiocraft. Complements MusicGen — useful for efficiency experiments and comparing AR vs. non-AR approaches.

**Architecture:** Masked Non-Autoregressive Transformer
**Modality:** Audio (32kHz)
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** efficient-generation

---

## Core Paper 5: LP-MusicCaps: LLM-Based Pseudo Music Captioning
- **Authors:** SeungHeon Doh, Keunwoo Choi, Jongpil Lee, Juhan Nam
- **Organization:** KAIST / Gaudio Lab
- **Year:** 2023 | **Venue:** ISMIR 2023
- **arXiv:** [2307.16372](https://arxiv.org/abs/2307.16372)
- **Citations:** ~176 [MEDIUM CONFIDENCE]
- **Relevance:** Active

**Key Findings:** Uses LLMs to generate ~2.2M music captions from 0.5M audio clips. Addresses the critical bottleneck of labeled music data. Enables large-scale training for text-to-music and music understanding. Directly relevant for dataset creation, prompt engineering analysis, and training captioning models.

**Architecture:** LLM-based pseudo-captioning pipeline
**Modality:** Text (music captions)
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** dataset-creation, prompt-engineering

---

## Core Paper 6: Symbolic Music Generation with Diffusion Models
- **Authors:** Gautam Mittal, Jesse Engel, Curtis Hawthorne, Ian Simon
- **Organization:** Google Brain / Magenta
- **Year:** 2021 | **Venue:** ISMIR 2021
- **arXiv:** [2103.16091](https://arxiv.org/abs/2103.16091)
- **Citations:** ~318 [MEDIUM CONFIDENCE]
- **Relevance:** Foundational

**Key Findings:** First successful application of diffusion models to symbolic (MIDI/piano roll) music. Adapted continuous diffusion to discrete sequential data. Critical bridge paper between image diffusion and music. Foundational for understanding how diffusion applies to musical sequences.

**Architecture:** DDPM adapted for sequences
**Modality:** Symbolic (piano rolls)
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** symbolic-finetuning

---

## Core Paper 7: FIGARO: Generating Symbolic Music with Fine-Grained Artistic Control
- **Authors:** Dimitri von Rütte, Luca Biggio, Yannic Kilcher, Thomas Hofmann
- **Organization:** ETH Zürich
- **Year:** 2022 | **Venue:** ICLR 2023
- **arXiv:** [2201.10936](https://arxiv.org/abs/2201.10936)
- **Citations:** ~75 [MEDIUM CONFIDENCE]
- **Relevance:** Active

**Key Findings:** Transformer-based model for controllable symbolic music generation. Uses learned expert descriptors for fine-grained control (genre, instrumentation, mood). Achieves SOTA in multi-track symbolic generation with style transfer. Open-source code available. Directly relevant for controllability experiments on symbolic music.

**Architecture:** Transformer with learned expert descriptors
**Modality:** Symbolic (multi-track MIDI)
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** controllability, symbolic-finetuning

---

## Core Paper 8: Theme Transformer: Symbolic Music Generation with Theme-Conditioned Transformer
- **Authors:** Yi-Jen Shih, Shih-Lun Wu, Frank Zalkow, Meinard Müller, Yi-Hsuan Yang
- **Organization:** Academia
- **Year:** 2022 | **Venue:** IEEE/ACM TASLP
- **arXiv:** [2111.04093](https://arxiv.org/abs/2111.04093)
- **Citations:** ~166 [MEDIUM CONFIDENCE]
- **Relevance:** Niche

**Key Findings:** Theme-based conditioning: a given melody phrase guides full-piece generation. Explicitly models thematic repetition and variation. Achieved superior coherence over prompt-based baselines. Relevant for controllability — demonstrates how explicit musical structure conditioning improves output.

**Architecture:** Theme-conditioned Transformer
**Modality:** Symbolic (MIDI)
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** controllability

---

## Core Paper 9: Benchmarking Music Generation Models and Metrics via Human Preference Studies
- **Authors:** Florian Grötschla, Luca A. Lanzendörfer, et al.
- **Organization:** ETH Zürich
- **Year:** 2025 | **Venue:** NeurIPS 2025 / ICASSP 2025
- **arXiv:** [2506.19085](https://arxiv.org/abs/2506.19085)
- **Citations:** ~27 [MEDIUM CONFIDENCE]
- **Relevance:** Active

**Key Findings:** Generated 6k songs from 12 SOTA models; 15k pairwise comparisons with 2.5k participants. Found that existing automated metrics (FAD, CLAP score) correlate poorly with human preference. Established that specialized music evaluators outperform general audio metrics. Direct blueprint for evaluation benchmark design.

**Architecture:** Human preference study + metric correlation analysis
**Modality:** Evaluation benchmark
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** evaluation-metrics

---

## Core Paper 10: Foundation Models for Music: A Survey
- **Authors:** Yinghao Ma, Anders Øland, Anton Ragni et al. (42 authors)
- **Organization:** Multi-institution
- **Year:** 2024 | **Venue:** arXiv (under review)
- **arXiv:** [2408.14340](https://arxiv.org/abs/2408.14340)
- **Citations:** ~76 [MEDIUM CONFIDENCE]
- **Relevance:** Active

**Key Findings:** Comprehensive survey of foundation models in music. Key insight: instruction tuning and evaluation remain underexplored. Highlights scaling laws, music agents, ethical considerations. Essential roadmap for identifying research gaps.

**Architecture:** N/A (Survey)
**Modality:** Comprehensive (audio + symbolic + multimodal)
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** evaluation-metrics, controllability

---

## Core Paper 11: The Song Describer Dataset: A Corpus of Audio Captions for Music-and-Language Evaluation
- **Authors:** Ilaria Manco, Benno Weck, SeungHeon Doh, Minz Won, et al.
- **Organization:** Multi-institution
- **Year:** 2023 | **Venue:** ISMIR 2023 / NeurIPS 2023 Datasets
- **arXiv:** [2311.10057](https://arxiv.org/abs/2311.10057)
- **Citations:** ~93 [MEDIUM CONFIDENCE]
- **Relevance:** Active

**Key Findings:** Crowdsourced corpus of ~1.1k high-quality captions for 706 permissively licensed recordings. Designed for evaluating music-and-language models. Gold-standard benchmark for text-to-music alignment and music captioning. Directly usable for cross-modal analysis and prompt engineering studies.

**Architecture:** N/A (Dataset)
**Modality:** Audio captions
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** cross-modal, dataset-creation, prompt-engineering

---

## Core Paper 12: MuPT: Generative Symbolic Music Pretrained Transformer
- **Authors:** Xingwei Qu, Yizhi Li, Ruibin Yuan, Ge Zhang et al. (28 authors)
- **Organization:** Multi-institution
- **Year:** 2024 | **Venue:** ICLR 2025
- **arXiv:** [2404.06393](https://arxiv.org/abs/2404.06393)
- **Citations:** ~38 [MEDIUM CONFIDENCE]
- **Relevance:** Active

**Key Findings:** Applied LLM pretraining techniques to symbolic music (ABC notation). Scaling model size improves generation quality, mirroring NLP. Emergent structure understanding at scale. Open-source — suitable for fine-tuning on niche genres/composers as an undergrad project.

**Architecture:** Decoder-only Transformer (LLM-style)
**Modality:** Symbolic (ABC notation)
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** symbolic-finetuning

---

## Core Paper 13: Combining Audio Control and Style Transfer Using Latent Diffusion
- **Authors:** Nils Demerlé, Philippe Esling, Guillaume Doras, David Genova
- **Organization:** IRCAM
- **Year:** 2024 | **Venue:** ISMIR 2024
- **arXiv:** [2408.00196](https://arxiv.org/abs/2408.00196)
- **Citations:** ~27 [LOW CONFIDENCE]
- **Relevance:** Niche

**Key Findings:** Unified explicit control and style transfer in one latent diffusion model. Disentangles local (pitch, timing) from global (timbre, genre, mood). Open-source code available. Ideal base for style transfer ablation studies: test what breaks when disentanglement components are removed.

**Architecture:** Latent Diffusion, disentangled local/global cond.
**Modality:** Audio
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** style-transfer, controllability

---

## Core Paper 14: Musical Timbre Style Transfer with Diffusion Model
- **Authors:** Hong Huang, Junfeng Man, Luyao Li, Rongke Zeng
- **Organization:** Hunan University of Technology
- **Year:** 2024 | **Venue:** PeerJ Computer Science (vol. 10, e2194)
- **DOI:** [10.7717/peerj-cs.2194](https://doi.org/10.7717/peerj-cs.2194)
- **Citations:** ~20 [MEDIUM CONFIDENCE]
- **Relevance:** Niche

**Key Findings:** Spectrogram-based diffusion for instrument timbre transfer (e.g., piano→violin). Preserves musical content while changing instrument identity. Important for orchestration and automatic arrangement. Niche but well-defined — suitable for focused undergrad exploration of timbre-space manipulation.

**Architecture:** Spectrogram-based Diffusion Model
**Modality:** Audio (spectrograms)
**Open-source / open artifact:** ✅ Yes
**Tracked directions:** style-transfer

---

## Core Registry Summary

- **Core papers:** 14
- **Date range:** 2021–2025
- **Approximate citation snapshot:** 3,721 (~3,700+)
- **Open-source or open-artifact entries:** 14 of 14
- **Categories:** 6 audio, 4 symbolic, 4 benchmark/dataset/survey

---

## Metric Exploration Sources — Added 2026-07-16

### Music structure, cognition, and control
- [McFee et al. — Evaluating Hierarchical Structure in Music Annotations](https://pmc.ncbi.nlm.nih.gov/articles/PMC5541043/) — L-measure and multi-annotator hierarchy disagreement. [Academic Study]
- [Foote — Automatic Audio Segmentation Using a Measure of Audio Novelty](https://ccrma.stanford.edu/workshops/mir2009/references/Foote_00.pdf) — self-similarity and novelty-based boundaries. [Academic Study]
- [Pearce & Wiggins — Auditory Expectation: The Information Dynamics of Music Perception and Cognition](https://onlinelibrary.wiley.com/doi/10.1111/j.1756-8765.2012.01214.x) — entropy, surprisal, and IDyOM. [Academic Study]
- [Farbood & Upham — Listener Judgments of Musical Tension](https://pmc.ncbi.nlm.nih.gov/articles/PMC3874841/) — continuous tension ratings and feature-specific time windows. [Academic Study]
- [SymPAC](https://arxiv.org/abs/2409.03055) — prompted and finite-state constrained symbolic generation. [Academic Study]

### Cross-art-domain inspirations
- [Kovarski et al. — Movie Editing Influences Spectators’ Time Perception](https://pmc.ncbi.nlm.nih.gov/articles/PMC9684412/) — continuity/discontinuity editing and perceived pacing. [Academic Study]
- [Barzilay & Lapata — Modeling Local Coherence: An Entity-Based Approach](https://aclanthology.org/J08-1001.pdf) — persistence patterns across narrative units. [Academic Study]
- [Chen & Bornstein — The Causal Structure and Computational Value of Narratives](https://pmc.ncbi.nlm.nih.gov/articles/PMC11305923/) — setup/payoff and causal-event networks. [Academic Review]
- [McManus et al. — Arnheim’s Gestalt Theory of Visual Balance](https://pmc.ncbi.nlm.nih.gov/articles/PMC3485801/) — contradictory evidence against simplistic visual balance metrics. [Academic Study]
- [Yamu et al. — Space Syntax](https://www.mdpi.com/2071-1050/13/6/3394) — local/global integration and structural intelligibility. [Academic Review]
- [Laban Movement Analysis chart](https://www.danceedlab.com/wp-content/uploads/2021/05/LMA-Series-Horizontal.pdf) — choreographic transformation and recurrence vocabulary. [Educational/Practice Source]
- [Ruiz Fabo et al. — Automatic Enjambment Detection](https://dh2017.adho.org/abstracts/485/485.pdf) — formal boundaries crossed by continuing syntactic dependencies. [Academic Study]
- [Salt — The Metrics in Cinemetrics](https://cinemetrics.uchicago.edu/article/616e7ecc-7915-4768-b84d-7dec79aa77c2) — shot-length and cutting-rate analysis with warnings about spurious trends. [Academic/Practice Analysis]
- [Szilas & Ilea — Objective Metrics for Interactive Narrative](https://access.archive-ouverte.unige.ch/access/metadata/d6a5eec8-adfb-4d4f-b399-031ac0cbd3b9/download) — choice variability and consequences rather than option count alone. [Academic Study]

### Mathematical and measurement foundations
- [Peyré, Cuturi & Solomon — Gromov–Wasserstein Averaging](https://proceedings.mlr.press/v48/peyre16.pdf) — relational graph comparison. [Academic Study]
- [Eckmann, Kamphorst & Ruelle — Recurrence Plots](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B92%5D.pdf) — dynamical recurrence analysis. [Academic Study]
- [Brier — Verification of Forecasts Expressed in Terms of Probability](https://journals.ametsoc.org/view/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.xml) — proper probabilistic scoring. [Academic Study]
- [Rubin — Estimating Causal Effects](https://doi.apa.org/doi/10.1037/h0037350) — counterfactual treatment-effect framework. [Academic Study]

### Cross-representation and psychometric validation
- [Campbell & Fiske — Multitrait-Multimethod Matrix](https://doi.org/10.1037/h0046016) — separates target-trait agreement from measurement-method effects. [Academic Study]
- [Putnick & Bornstein — Measurement Invariance Conventions](https://pmc.ncbi.nlm.nih.gov/articles/PMC5145197/) — configural, metric, and scalar invariance practice. [Academic Review]
- [Protzko et al. — Measurement Invariance Is Not Sufficient](https://pmc.ncbi.nlm.nih.gov/articles/PMC11562939/) — statistical invariance does not establish construct validity. [Academic Study]
- [Dorfer et al. — Learning Audio–Sheet Music Correspondences](https://arxiv.org/abs/1707.09887) — paired cross-modal learning without requiring transcription as truth. [Academic Study]
- [Ycart et al. — Musically Informed Evaluation of Piano Transcription](https://arxiv.org/abs/2406.08454) — limits of frame/note metrics for articulation, dynamics, and rhythmic precision. [Academic Study]
- [PIAST](https://arxiv.org/abs/2411.02551) — aligned piano audio, symbolic music, and expert text labels. [Academic Dataset]
- [Unified Cross-modal Translation of Score Images, Symbolic Music, and Performance Audio](https://arxiv.org/abs/2505.12863) — multimodal translation evidence. [Academic Study]

### Competitive benchmarks and robustness studies — added 2026-07-16
- [SongEval](https://arxiv.org/abs/2505.10793) — 2,399 full-length songs totaling more than 140 hours, with aesthetic ratings from 16 professional annotators, including overall coherence and clarity of song structure. [Academic Preprint] [HIGH CONFIDENCE: primary paper verified]
- [CMI-RewardBench](https://arxiv.org/abs/2603.00610) — evaluates reward models across musicality, text–music alignment, and compositional instruction alignment for music conditioned on text descriptions, lyrics, and audio prompts. [Academic Preprint] [HIGH CONFIDENCE: primary abstract verified]
- [SegTune](https://arxiv.org/abs/2510.18416) — segment-level prompts and proposed segment-alignment/vocal-consistency evaluation for structured song generation. [Academic Preprint] [HIGH CONFIDENCE: primary abstract verified]
- [MAD / MusicPrefs](https://arxiv.org/abs/2503.16669) — reports MAD rank correlation 0.84 versus FAD 0.49 on synthetic meta-evaluations and 0.62 versus 0.14 against MusicPrefs. [Academic Preprint] [HIGH CONFIDENCE: primary abstract verified]
- [AIME](https://arxiv.org/abs/2506.19085) — human preference and metric benchmark; limited for long-form structure because evaluation uses short excerpts. [Academic Preprint] [MEDIUM CONFIDENCE: primary paper exists; detailed design needs continued checking]
- [Investigating the Perceptual Validity of AMT Metrics](https://transactions.ismir.net/articles/10.5334/tismir.57) — shows standard transcription metrics do not uniformly reflect perceptual consequences. [Peer-reviewed Academic Study] [HIGH CONFIDENCE]
- [Towards Musically Informed Evaluation of Piano Transcription Models](https://arxiv.org/abs/2406.08454) — decomposes timing, articulation, harmony, and dynamics under recordings and controlled degradation. [Academic Preprint] [HIGH CONFIDENCE: PDF extracted]
- [Sound and Music Biases in Deep Music Transcription Models](https://link.springer.com/article/10.1186/s13636-025-00428-z) — reports note-level F1 drops of roughly 20 points from sound shift and 14 from genre shift. [Peer-reviewed Academic Study] [HIGH CONFIDENCE: publisher article verified]
- [Audio Degradation Toolbox](https://sebewert.github.io/publications_pdf/2013_MauchEwert_AudioDegradationToolbox_ISMIR.pdf) — controlled degradation chains and evidence that method rankings can depend on degradation. [Peer-reviewed Academic Study] [HIGH CONFIDENCE]
- [Evaluating Beat-Tracking Evaluation Measures](https://archives.ismir.net/ismir2014/paper/000238.pdf) — shows metric tolerances and allowed metrical alternatives materially alter apparent performance and human agreement. [Peer-reviewed Academic Study] [HIGH CONFIDENCE]
- [MV2H](https://arxiv.org/abs/1906.00566) — evaluates pitch, voice, meter, value, and harmony with disjoint penalties to avoid cascading one error into several penalties. [Academic Study] [HIGH CONFIDENCE]
- [Eid et al. on MTMM model choice](https://doi.org/10.1037/a0013219) — distinguishes structurally different from interchangeable methods; relevant because symbolic/audio are not exchangeable while renderers may be. [Peer-reviewed Methods Study] [HIGH CONFIDENCE]
- [Nussbeck et al. on ordinal MTMM sample size](https://pubmed.ncbi.nlm.nih.gov/16709286/) — simulation-conditional evidence that confirmatory MTMM generally needs hundreds of independent observations, not a tiny paired pilot. [Peer-reviewed Simulation Study] [HIGH CONFIDENCE]
- [Bland & Altman](https://pubmed.ncbi.nlm.nih.gov/2868172/) — correlation measures association, not agreement between methods. [Peer-reviewed Methods Study] [HIGH CONFIDENCE]

### Stage 0 generator, commercial-practice, and oracle sources — added 2026-07-17
- [ACE-Step 1.5 official repository](https://github.com/ace-step/ACE-Step-1.5) — documents 10-second to 10-minute duration, local execution, instrumental generation, metadata controls, repainting, and Apple Silicon support. [Official Open-Source Repository] [HIGH CONFIDENCE for documented capabilities; independent quality claims unverified]
- [ACE-Step 1.5 tutorial](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/Tutorial.md) — documents fixed-seed comparisons, task modes, interval repainting, and hardware guidance. [Official Technical Documentation] [HIGH CONFIDENCE]
- [Udio pricing](https://www.udio.com/pricing) — documents the current $10 monthly Standard tier, 2,400 monthly credits, and 130-second generation option. [Corporate Product Documentation] [HIGH CONFIDENCE as a dated pricing snapshot]
- [Udio two-minute model and controls](https://www.udio.com/blog/two-minute-model-new-controls) — documents explicit random seeds, manual-mode reproducibility controls, prompt strength, and clip start-time. [Corporate Product Documentation] [HIGH CONFIDENCE as a dated interface snapshot]
- [Udio model updates](https://help.udio.com/en/articles/10756068-model-updates) — states that matching prompt, settings, and seed currently reproduce outputs while warning that future product changes may break this behavior. [Corporate Product Documentation] [HIGH CONFIDENCE as a dated behavior claim]
- [Music Arena](https://arxiv.org/abs/2507.20900) — combines open-weight and API-based systems, reports access type and capabilities, and motivates renewable evaluation under model turnover. [Academic Preprint] [HIGH CONFIDENCE: primary paper verified]
- [ACE-Step](https://arxiv.org/abs/2506.00045) — compares an open model with proprietary and open full-song systems, illustrating mixed-panel academic practice. [Academic Preprint] [HIGH CONFIDENCE: primary paper verified]
- [DiffRhythm 2 official repository](https://github.com/ASLP-lab/DiffRhythm2) — released full-song and instrumental generation code and weights under Apache 2.0; fixed-seed support remains to be audited. [Official Open-Source Repository] [MEDIUM CONFIDENCE for CLPR suitability]
- [YuE official repository](https://github.com/multimodal-art-projection/YuE) — open full-song lyrics-to-song model with substantial long-form hardware requirements; deferred from Stage 0. [Official Open-Source Repository] [HIGH CONFIDENCE for documented requirements]
- [Slakh2100](https://zenodo.org/records/4599666) — 2,100 synthesized multitracks, aligned MIDI, 145 hours, and detailed source metadata; selected for oracle calibration rather than generator responsiveness. [Academic Dataset Archive] [HIGH CONFIDENCE]
- [MedleyDB](https://steinhardt.nyu.edu/marl/research/resources/medleydb) — natural multitracks and instrument/source metadata for later timbral-realism validation. [Academic Dataset] [HIGH CONFIDENCE]
- [MoisesDB](https://github.com/moises-ai/moises-db) — professionally recorded sources with a fine-grained stem taxonomy; suitable for later natural-audio calibration. [Academic Dataset Repository] [HIGH CONFIDENCE]
- [MSG-LD](https://github.com/karchkha/MSG-LD) — native four-track generation and arrangement/inpainting for bass, drums, guitar, and piano; retained as a separate source-level experimental lane. [Academic Open-Source Repository] [HIGH CONFIDENCE]
