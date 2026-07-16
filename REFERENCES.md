# References — Music Generation & Orchestration Research

> Last updated: 2026-07-14  
> **14 frontier papers** with summaries, all with 10+ citations.

---

## Paper 1: Jukebox — A Generative Model for Music
- **Authors:** Prafulla Dhariwal, Heewoo Jun, Christine Payne, Jong Wook Kim, Alec Radford, Ilya Sutskever (OpenAI)
- **Year:** 2020 | **Venue:** arXiv / OpenAI Research
- **arXiv:** [2005.00341](https://arxiv.org/abs/2005.00341)
- **Citations:** ~1,373 [HIGH CONFIDENCE — multiple sources confirm]
- **Code:** [github.com/openai/jukebox](https://github.com/openai/jukebox)

**Key Findings:** Introduced the first model to generate raw-audio music with singing. Uses a multi-scale VQ-VAE to compress raw audio into discrete codes, then models those codes with autoregressive Transformers. Can condition on artist, genre, and unaligned lyrics. Generates coherent songs lasting multiple minutes. Pioneered raw-audio generation at scale, laying the foundation for all subsequent high-fidelity music generation work.

**Architecture:** Multi-scale VQ-VAE + Hierarchical Autoregressive Transformers  
**Modality:** Raw audio (44.1kHz)  
**Open-source:** ✅ Yes (code + weights)

---

## Paper 2: MusicLM — Generating Music From Text
- **Authors:** Andrea Agostinelli, Timo I. Denk, Zalán Borsos, Jesse Engel, Mauro Verzetti et al. (Google Research)
- **Year:** 2023 | **Venue:** arXiv
- **arXiv:** [2301.11325](https://arxiv.org/abs/2301.11325)
- **Citations:** ~1,235 [HIGH CONFIDENCE]
- **Dataset:** [MusicCaps](https://kaggle.com/datasets/googleai/musiccaps) (5.5k music-text pairs)

**Key Findings:** Pioneered high-fidelity text-to-music generation. Casts conditional music generation as hierarchical sequence-to-sequence modeling. Generates 24kHz audio coherent over several minutes. Supports both text and melody conditioning (whistled/hummed input → styled output). Released MusicCaps, the first large-scale expert-annotated music-text dataset. Set the benchmark for text-aligned music generation quality.

**Architecture:** Hierarchical Seq2Seq (SoundStream + w2v-BERT + MuLan)  
**Modality:** Audio (24kHz)  
**Open-source:** ❌ No (model not released; dataset only)

---

## Paper 3: MusicGen — Simple and Controllable Music Generation
- **Authors:** Jade Copet, Felix Kreuk, Itai Gat, Tal Remez, David Kant, Gabriel Synnaeve, Yossi Adi, Alexandre Défossez (Meta)
- **Year:** 2023 | **Venue:** NeurIPS 2023
- **arXiv:** [2306.05284](https://arxiv.org/abs/2306.05284)
- **Citations:** ~1,199 [HIGH CONFIDENCE]
- **Code:** [github.com/facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft)

**Key Findings:** Simplified music generation to a single-stage transformer LM operating over compressed discrete tokens. Eliminated cascaded/hierarchical models used in prior work. Supports dual conditioning on text + melody. Achieved state-of-the-art on text-to-music benchmarks. Ablation studies validated each component's contribution. Fully open-source release drove widespread adoption and follow-up research.

**Architecture:** Single-stage Transformer LM + EnCodec tokenizer + token interleaving  
**Modality:** Audio (32kHz, mono + stereo)  
**Open-source:** ✅ Yes (code + pretrained models)

---

## Paper 4: Noise2Music — Text-Conditioned Music Generation with Diffusion Models
- **Authors:** Qingqing Huang, Daniel S. Park, Tao Wang, Timo I. Denk et al. (Google Research)
- **Year:** 2023 | **Venue:** arXiv
- **arXiv:** [2302.03917](https://arxiv.org/abs/2302.03917)
- **Citations:** ~333 [MEDIUM CONFIDENCE — web search aggregation]

**Key Findings:** Introduced a series of diffusion models trained to generate high-quality 30-second music clips from text prompts. Uses a two-model cascade: a generator model produces intermediate representations conditioned on text, and a cascader model generates high-fidelity audio. Demonstrated that diffusion models can match or exceed autoregressive approaches for music generation.

**Architecture:** Diffusion cascade (Generator + Cascader)  
**Modality:** Audio (30-second clips)  
**Open-source:** ❌ No

---

## Paper 5: Symbolic Music Generation with Diffusion Models
- **Authors:** Gautam Mittal, Jesse Engel, Curtis Hawthorne, Ian Simon (Google Brain / Magenta)
- **Year:** 2021 | **Venue:** ISMIR 2021
- **arXiv:** [2103.16091](https://arxiv.org/abs/2103.16091)
- **Citations:** ~318 [MEDIUM CONFIDENCE]

**Key Findings:** First successful application of diffusion models to symbolic (MIDI/piano roll) music generation. Adapted continuous diffusion to discrete sequential data. Demonstrated that diffusion models produce more musically coherent outputs than autoregressive baselines for symbolic music. Influential bridge between image diffusion techniques and music generation.

**Architecture:** Denoising Diffusion Probabilistic Model (DDPM) adapted for sequences  
**Modality:** Symbolic (piano rolls)  
**Open-source:** ✅ Yes (part of Magenta)

---

## Paper 6: Fast Timing-Conditioned Latent Audio Diffusion (Stable Audio)
- **Authors:** Zach Evans, CJ Carr, Josiah Taylor, Scott H. Hawley, Jordi Pons (Stability AI)
- **Year:** 2024 | **Venue:** arXiv / ICML 2024
- **arXiv:** [2402.04825](https://arxiv.org/abs/2402.04825)
- **Citations:** ~283 [MEDIUM CONFIDENCE]

**Key Findings:** Efficient generation of long-form, variable-length stereo music and sounds at 44.1kHz from text prompts. Introduced timing conditioning for controlling output duration. Achieved significant computational efficiency gains over prior approaches through latent diffusion. Formed the foundation for Stability AI's Stable Audio product. Demonstrated commercial viability of diffusion-based music generation.

**Architecture:** Latent Diffusion + Timing Conditioning  
**Modality:** Stereo audio (44.1kHz, variable length)  
**Open-source:** Partially (Stable Audio Open released)

---

## Paper 7: Theme Transformer — Symbolic Music Generation with Theme-Conditioned Transformer
- **Authors:** Yi-Jen Shih, Shih-Lun Wu, Frank Zalkow, Meinard Müller, Yi-Hsuan Yang
- **Year:** 2022 | **Venue:** IEEE/ACM TASLP
- **arXiv:** [2111.04093](https://arxiv.org/abs/2111.04093)
- **Citations:** ~166 [MEDIUM CONFIDENCE]

**Key Findings:** Proposed theme-based conditioning for symbolic music generation, where a given musical theme (melody phrase) guides the generation of the full piece. Unlike standard prompt-based conditioning, the theme transformer explicitly models thematic repetition and variation — a core aspect of musical composition. Achieved superior coherence and thematic consistency over prompt-based baselines.

**Architecture:** Theme-conditioned Transformer  
**Modality:** Symbolic (MIDI)  
**Open-source:** ✅ Yes

---

## Paper 8: Long-Form Music Generation with Latent Diffusion
- **Authors:** Zach Evans, Julian D. Parker, CJ Carr, Zack Zukowski, Josiah Taylor, Jordi Pons (Stability AI)
- **Year:** 2024 | **Venue:** ISMIR 2024
- **arXiv:** [2404.10301](https://arxiv.org/abs/2404.10301)
- **Citations:** ~136 [HIGH CONFIDENCE]

**Key Findings:** First model to generate full-length music tracks (up to 4min 45s) with coherent musical structure from text prompts. Uses a diffusion-transformer operating on highly downsampled continuous latent representations (21.5Hz rate). Achieved state-of-the-art on audio quality and prompt alignment metrics. Subjective tests confirmed coherent structure across the full track. Critical milestone for long-form music generation.

**Architecture:** Diffusion-Transformer with highly compressed latent space  
**Modality:** Audio (up to 4m45s)  
**Open-source:** ❌ No

---

## Paper 9: Symbolic Music Generation with Transformer-GANs
- **Authors:** Aashiq Muhamed, Liang Li, Xingjian Shi, Suri Yaddanapudi, Wayne Chi et al.
- **Year:** 2021 | **Venue:** AAAI 2021
- **Citations:** ~111 [MEDIUM CONFIDENCE]

**Key Findings:** Combined Transformers and GANs for symbolic music generation. Transformer generates a sequence, GAN discriminator evaluates musical quality. The hybrid approach improved output quality over pure autoregressive Transformers. Demonstrated that adversarial training benefits symbolic music generation where traditional teacher-forcing leads to exposure bias.

**Architecture:** Transformer generator + GAN discriminator  
**Modality:** Symbolic (MIDI)  
**Open-source:** ✅ Yes

---

## Paper 10: Foundation Models for Music — A Survey
- **Authors:** Yinghao Ma, Anders Øland, Anton Ragni et al. (42 authors)
- **Year:** 2024 | **Venue:** arXiv (under review)
- **arXiv:** [2408.14340](https://arxiv.org/abs/2408.14340)
- **Citations:** ~76 [MEDIUM CONFIDENCE]

**Key Findings:** Comprehensive survey of foundation models in music covering representation learning, generative learning, and multimodal learning. Key insight: many music representations remain underexplored in foundation model development. Highlights underrepresented topics: instruction tuning, in-context learning for music, scaling laws, emergent abilities, long-sequence modeling. Dedicated section on music agents. Emphasizes ethical considerations including interpretability, transparency, and copyright. Essential roadmap for music AI research.

**Architecture:** N/A (Survey)  
**Modality:** Comprehensive (audio + symbolic + multimodal)  
**Open-source:** ✅ Yes (CC BY-NC-SA 4.0)

---

## Paper 11: MuPT — Generative Symbolic Music Pretrained Transformer
- **Authors:** Xingwei Qu, Yizhi Li, Ruibin Yuan, Ge Zhang et al. (28 authors)
- **Year:** 2024 | **Venue:** ICLR 2025
- **arXiv:** [2404.06393](https://arxiv.org/abs/2404.06393)
- **Citations:** ~38 [MEDIUM CONFIDENCE]

**Key Findings:** Applied LLM pretraining techniques (next-token prediction at scale) to symbolic music. Trained a decoder-only transformer on a large corpus of ABC notation music. Demonstrated that scaling model size and data improves symbolic music generation, mirroring trends in natural language. Showed emergent capabilities in musical structure understanding at larger scales.

**Architecture:** Decoder-only Transformer (LLM-style) for ABC notation  
**Modality:** Symbolic (ABC notation)  
**Open-source:** ✅ Yes

---

## Paper 12: JEN-1 Composer — Unified Multi-Track Music Generation
- **Authors:** Yao Yao, Peike Li, Boyu Chen, Alex Wang (Futureverse)
- **Year:** 2023 | **Venue:** AAAI 2025
- **arXiv:** [2310.19180](https://arxiv.org/abs/2310.19180)
- **Citations:** ~28 [MEDIUM CONFIDENCE]

**Key Findings:** Unified framework for multi-track music generation. Models marginal, conditional, and joint distributions for multi-track generation in a single model. Generates coherent multi-stem compositions (different instruments in separate tracks). Addresses the crucial gap between single-mix generation and real music production workflows. Represents the frontier of multi-track orchestration models.

**Architecture:** Unified diffusion framework for multi-track generation  
**Modality:** Multi-track audio  
**Open-source:** ❌ No

---

## Paper 13: Combining Audio Control and Style Transfer Using Latent Diffusion
- **Authors:** Nils Demerlé, Philippe Esling, Guillaume Doras, David Genova (IRCAM)
- **Year:** 2024 | **Venue:** ISMIR 2024
- **arXiv:** [2408.00196](https://arxiv.org/abs/2408.00196)
- **Citations:** ~27 [LOW CONFIDENCE — recent paper]

**Key Findings:** Unified explicit control and style transfer in a single latent diffusion model. Separates local information (pitch, timing) from global information (timbre, genre, mood). Enables fine-grained control: specify the notes/pitches while independently controlling genre/style. Important for practical music production where both structure and style matter.

**Architecture:** Latent Diffusion with disentangled local/global conditioning  
**Modality:** Audio  
**Open-source:** ✅ Yes

---

## Paper 14: Musical Timbre Style Transfer with Diffusion Model
- **Authors:** Hong Huang, Junfeng Man, Luyao Li, Rongke Zeng (Hunan University of Technology)
- **Year:** 2024 | **Venue:** PeerJ Computer Science (vol. 10, e2194)
- **DOI:** [10.7717/peerj-cs.2194](https://doi.org/10.7717/peerj-cs.2194)
- **Citations:** ~20 [MEDIUM CONFIDENCE]

**Key Findings:** Focused on the specific problem of timbre transfer — changing the instrument sound (e.g., piano → violin) while preserving musical content. Used spectrogram-based diffusion models for multi-to-multi timbre transfer. Achieved high-quality instrument conversion without degrading musical structure. Niche but important problem for orchestration: automatic instrument assignment and arrangement.

**Architecture:** Spectrogram-based Diffusion Model  
**Modality:** Audio (spectrograms)  
**Open-source:** ✅ Yes

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total papers | 14 |
| Date range | 2020–2025 |
| Total citations (estimated) | ~5,600+ |
| Open-source papers | 9 of 14 (64%) |
| Audio generation papers | 9 |
| Symbolic generation papers | 4 |
| Multi-track / orchestration | 3 |
| Survey papers | 1 |

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
