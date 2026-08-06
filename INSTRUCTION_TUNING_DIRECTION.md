# Instruction-Following Music Generation: Feasibility and Unified Research Direction

**Assessment date:** 2026-08-06  
**Epistemic status:** Literature-based feasibility and research-design assessment; no new model training or benchmark experiment has yet been performed.

## Executive Summary

Yes: instruction fine-tuning can make a symbolic music model respond to requests involving key, bar count, chord progression, repetition, form, and instrumentation, and existing systems already demonstrate parts of this capability.[1][2][3][5] [Peer-reviewed papers / academic preprints, 2023–2025] [HIGH]

However, present systems do **not** establish reliable exact compliance with compound requests: Text2MIDI reports only 33.6% exact-key accuracy in its current repository evaluation, its chord-matching listening score is 2.50/7, and MuseCoco explicitly warns that it cannot guarantee 100% control and works best with predefined attributes.[13][14] [Official research repositories, accessed 2026-08-06] [HIGH]

The strongest research program is therefore not “fine-tune a waveform generator and hope.” It is a **verified neuro-symbolic pipeline**: natural language → canonical musical plan → constrained symbolic generation → deterministic validation → rendering → audio-grounded interpretation, with the existing CLPR framework measuring whether requested changes occur in the correct region without unnecessary collateral change. [SYNTHESIS; proposed architecture, not an established fact]

## Systematic Research Questions

1. What exact output behavior would count as following a compound musical instruction?
2. Can a model reliably parse key, mode, meter, bar count, harmonic rhythm, Roman numerals, repetition count, form, instrumentation, and voicing as separate constraints?
3. Should natural language condition a generator directly, or first compile into a typed intermediate musical plan?
4. Which representation—ABC, MIDI/REMI, MusicXML, chord chart, or audio tokens—best preserves exact harmonic and structural constraints?
5. Can supervised instruction tuning alone guarantee exact bar count and chord order?
6. When should finite-state or grammar-constrained decoding replace learned compliance?
7. How should ambiguous prompts be detected rather than silently guessed?
8. Can synthetic instructions generated from symbolic scores provide enough diversity without teaching template artifacts?
9. Which real symbolic datasets contain usable key, chord, bar, section, and arrangement information?
10. How should Roman-numeral progressions be transposed and validated across keys and modes?
11. Can a model create musically varied melody, rhythm, voicing, and orchestration while preserving an exact harmonic skeleton?
12. Does parameter-efficient adaptation preserve the base model’s musicality better than full fine-tuning?
13. How much compute is required for parser tuning, symbolic generation tuning, and direct audio tuning?
14. Do current text-to-MIDI or ABC systems actually obey compound theory-rich prompts?
15. Can automatic symbolic checks predict musicians’ instruction-compliance judgments?
16. How should exact compliance, musicality, production quality, originality, and preference be reported separately?
17. Can CLPR detect target response, off-target leakage, and boundary spillover for symbolic as well as audio outputs?
18. Can a generated piece later be interpreted for mood, imagery, and narrative in an audio-grounded, counterfactually tested way?

## Concrete Interpretation of the Example

Given the default assumption of one chord per bar in G major, the request describes eight bars:

```text
Bars:       1     2     3     4      5     6     7     8
Roman:      I     V     IV    vii°   I     V     IV    vii°
Chord root: G     D     C     F♯     G     D     C     F♯
Quality:    major major major diminished, repeated once
```

This is only one valid realization. The prompt does not specify meter, tempo, inversion, voicing, register, instrumentation, chord duration, melodic content, or whether “repeat twice” means two total occurrences or two additional repetitions. A reliable system should either apply a documented default policy or return a clarification request; silently choosing defaults makes exact-compliance evaluation ill-posed. [MUSIC-THEORY INTERPRETATION / task analysis] [HIGH for the stated assumption; LOW for unstated user intent]

## Key Findings

### 1. The central idea is technically feasible, especially in symbolic music

ChatMusician continually pretrains and fine-tunes LLaMA-2 on ABC notation as a second textual language and reports strict-format generation conditioned on text, **absolute chord symbols**, melodies, motifs, and automatically derived form labels.[1] [Peer-reviewed ACL Findings paper, 2024] [HIGH]

MuseCoco decomposes text-to-symbolic-music generation into text-to-attribute understanding and attribute-to-music generation; its fixed control inventory includes bar range, time signature, key-related categories, tempo, pitch range, emotion, and instrumentation, but not arbitrary per-bar chord progressions or Roman numerals.[2][14] [Academic preprint + official research repository, 2023] [HIGH]

Text2MIDI uses a frozen FLAN-T5 encoder and an autoregressive REMI+ MIDI decoder; its captions may contain chords, keys, tempo, time signature, instruments, style, and mood.[3][13] [AAAI paper + official MIT-licensed repository, 2025] [HIGH]

SymPAC encodes genre, section, tempo, absolute major/minor chords, and tracks in symbolic prompt bars and uses a finite-state machine to restrict generation to grammatically and user-valid token subsets; it is not a natural-language instruction-tuned system.[5] [ISMIR paper, 2024] [HIGH]

**Finding:** instruction tuning is not speculative in the broad sense. The unsolved part is **reliable compositional constraint satisfaction under compound, natural-language requests**. [SYNTHESIS] [HIGH]

### 2. Exact compliance is still weak

The current Text2MIDI repository reports 33.6% Correct Key and 35.6% Correct Key with relative-minor duplicates; its listening-test means are 3.64/7 for key matching and 2.50/7 for chord matching.[13] [Official research repository, accessed 2026-08-06] [HIGH]

MuseCoco’s official instructions say that control accuracy is difficult to guarantee at 100%, recommend only supported attribute values, and suggest filtering generated samples using an attribute evaluator.[14] [Official research repository, accessed 2026-08-06] [HIGH]

ChatMusician’s own MusicTheoryBench results show that symbolic music reasoning remained close to a 25% random baseline: the paper reports 26.3 for ChatMusician, 27.1 for ChatMusician-Base, and 25.6 for GPT-4 in its zero-shot reasoning subset.[1] [Peer-reviewed ACL Findings paper, 2024] [HIGH]

ABC-Eval later evaluated seven LLMs across 1,086 samples and ten symbolic understanding/instruction-following subtasks, reporting notable limitations.[12] [Academic preprint, 2025] [MEDIUM; one benchmark paper]

**Finding:** a fluent output or valid MIDI file is not evidence that all requested constraints were obeyed. This claim requires additional verification for every model and instruction family. [SYNTHESIS] [HIGH]

### 3. A compiler-like intermediate representation is preferable to direct free-form control

MuseCoco’s two-stage text→attributes→music design makes the inferred controls inspectable, while SymPAC demonstrates that finite-state constraints can enforce known grammar and user inputs during decoding.[2][5] [Academic papers, 2023–2024] [HIGH]

MusicAgent uses an LLM to decompose a request into subtasks and invoke specialized music tools rather than requiring one model to perform every operation internally.[11] [Peer-reviewed EMNLP system-demonstration paper, 2023] [HIGH]

**Recommended intermediate plan:**

```json
{
  "key": {"tonic": "G", "mode": "major"},
  "meter": "4/4",
  "bars": 8,
  "harmonic_rhythm": "1 chord/bar",
  "progression_roman": ["I", "V", "IV", "vii°", "I", "V", "IV", "vii°"],
  "progression_absolute": ["G", "D", "C", "F#dim", "G", "D", "C", "F#dim"],
  "repeat": {"unit_bars": 4, "total_occurrences": 2},
  "defaults_applied": ["4/4", "one chord per bar"]
}
```

The parser can be instruction-tuned, but bar arithmetic, Roman-numeral realization, schema validation, and output acceptance should be deterministic. The generator should supply melody, rhythm, voicing, texture, and orchestration inside the validated plan rather than being trusted to remember exact hard constraints. [SYNTHESIS; proposed design] [HIGH]

### 4. Instruction-tuning data can be created, but data provenance and shortcut learning are serious risks

ChatMusician created handcrafted symbolic generation tasks and used 1.1 million music-score samples in its reported fine-tuning stage; its full pretraining used 16 A800 80GB GPUs.[1] [Peer-reviewed ACL Findings paper, 2024] [HIGH]

Text2MIDI pretrains on pseudo-captions generated from extractable MIDI attributes and then fine-tunes on the 168,401-item MidiCaps caption dataset; the reported model has 159 million trainable parameters and was trained on six L40S 48GB GPUs.[3] [AAAI paper, 2025] [HIGH]

MetaScore contains 963,000 scores with metadata and uses LLM-generated captions, but the authors explicitly flag copyright concerns and restrict non-public-domain material to research access.[4] [ISMIR paper, 2025] [HIGH]

CHORDONOMICON contains more than 666,000 user-generated chord progressions with structure, genre, and release metadata, making it a possible harmonic-language resource; its scraped provenance requires a separate licensing audit before training or redistribution.[8] [Academic preprint, 2024] [MEDIUM; dataset paper and unresolved downstream licensing]

**Recommended data mixture:**

1. Deterministically generated instruction↔plan pairs for exact theory and compositional constraints.
2. Real symbolic excerpts paired with plans extracted by trusted symbolic tools.
3. Paraphrase augmentation with a language model, followed by deterministic semantic equivalence checks.
4. Negative and contrastive examples differing in exactly one field.
5. Ambiguous or impossible prompts requiring clarification or explicit error output.
6. Real composer-like variation examples so the model does not learn sterile block-chord templates.

[SYNTHESIS; proposed dataset] [HIGH for methodological rationale, UNVERIFIED for eventual performance]

### 5. Direct audio instruction tuning exists, but current demonstrations concern editing more than exact theory-rich generation

Instruct-MusicGen adds audio- and text-fusion modules to pretrained MusicGen, trains roughly 8% additional parameters for 5,000 steps, and supports instructions such as adding, removing, or separating stems.[6][15] [ISMIR paper + official Apache-2.0 repository, 2025] [HIGH]

InstructME is a latent-diffusion editing system that adds a chord-progression matrix and a chunk transformer; its demonstrations center on instrument editing, remixing, and multi-round editing.[7] [Academic preprint, 2023] [MEDIUM; author-reported evaluation]

These papers demonstrate that parameter-efficient instruction adaptation of audio models is possible, but neither establishes exact compliance with a request such as eight bars in a named key with a repeated Roman-numeral progression. This claim requires additional verification. [SYNTHESIS] [HIGH]

**Decision:** start symbolically, render to audio afterward, and treat direct audio fine-tuning as a later comparison—not the first implementation. [RECOMMENDATION] [HIGH]

### 6. This direction fits the existing CLPR benchmark unusually well

The current CLPR project already asks whether a minimal localized instruction change causes the requested target effect while preserving protected regions, reporting Target Effect Size, Directional Accuracy, Off-Target Leakage, and Boundary Spillover. [Project record: `METRICS.md`, 2026-07-17] [Internal Research Record] [HIGH]

The new symbolic instruction task supplies exact, machine-checkable interventions:

- change `V` to `vi` in bar 2 only;
- transpose G major to A major while preserving Roman functions;
- change one chord per bar to two chords per bar;
- repeat the four-bar unit twice versus vary the second occurrence;
- change only the final `vii°` to `V7`;
- orchestrate the second repetition for strings without altering the harmonic plan.

These can be evaluated with exact symbolic oracles before audio rendering. The same pairs can then be rendered through multiple soundfonts or synthesizers to test CRVP-style representation robustness and analyzed in native audio with CLPR. [SYNTHESIS with project methods] [HIGH]

### 7. It also connects to the separate music-interpretation POC

The interpretation POC proposes waveform→music encoder→temporal adapter→language model, with answers separated into audible observation, interpretation, evidence, alternative reading, and confidence. [Project record: `music-interpretation-poc/INFO.md` and `RESEARCH.md`, 2026-07-18] [Internal Research Record] [HIGH]

MusiLingo separately demonstrates instruction-tuned music understanding and dialogue from audio, but it is not a music generator and therefore supports only the interpretation side of the loop.[10] [Peer-reviewed NAACL Findings paper, 2024] [HIGH]

A unified generate→verify→interpret loop would test whether controlled compositional changes produce predictable perceptual and interpretive consequences:

```text
natural-language instruction
        ↓
canonical symbolic plan
        ↓
constrained symbolic generator
        ↓
exact symbolic validator ── reject/repair if invalid
        ↓
renderer(s) → audio
        ↓
CLPR + CRVP compliance analysis
        ↓
audio-grounded interpretation model
        ↓
listener study: compliance, musicality, mood/imagery, preference
```

For example, after holding tempo, instrumentation, voicing, and production constant, one could compare interpretations of `I–V–IV–vii°` against a minimally altered cadence. Any mood or narrative difference would remain a listener/model-response association, not proof that a chord progression has one objective meaning. [SYNTHESIS; proposed experiment] [HIGH for design logic, LOW for predicted perceptual effect]

## Independent Audit Refinements

Three independent research audits converged on a stricter conclusion: **no verified open system jointly follows a free-form request containing exact tonic/key, exact bar count, Roman-numeral sequence, explicit repetition relation, and musical form**. ChatMusician supplies the closest language-to-ABC instruction precedent, while SymPAC supplies the closest hard-control mechanism; combining them with a Roman-numeral/form-aligned dataset is a proposed extension, not a demonstrated system.[1][5] [Peer-reviewed papers + independent source audit, 2024] [HIGH]

The terms used by adjacent papers must remain separated:

- “natural-language controllable” may mean classification into a closed attribute ontology, as in MuseCoco—not open-ended compositional instruction following.[2][14] [Academic paper + official repository, 2023] [HIGH]
- “chord-conditioned” generally means absolute chord labels rather than key-relative Roman-numeral functions.[1][5][21] [Academic papers, 2022–2024] [HIGH]
- “long-form” or bar-aware encoding does not establish exact requested bar count; MuPT and NotaGen are important symbolic foundation models but are not general natural-language instruction-following systems.[9][22] [Academic papers, 2024–2025] [HIGH]
- Repeat signs or learned recurrence do not establish compliance with an explicit relation such as “repeat this four-bar unit exactly twice.” This claim requires additional verification.[1] [Peer-reviewed paper, 2024] [HIGH]

### Stronger direct-audio comparison

Mustango is the closest reviewed text-to-audio precedent for chord-rich prompts, but it internally predicts beat and timestamped chord controls before diffusion, generates ten-second audio, and therefore supports language as a front end to structured control rather than proof of implicit waveform-level musical reasoning.[16] [Academic preprint, 2023] [HIGH]

JASCO combines global text with frame-aligned chord, melody, drum, or audio controls; its evidence supports using an explicit verified chord timeline for rendering, while also showing that strong local guidance can conflict with text-based instrumentation and require multi-source guidance balancing.[17] [Academic paper, 2024] [HIGH]

Coco-Mulla explicitly argues that text has limited power for direct pitch/chord/drum control, while Music ControlNet obtains precise local audio control from explicit time-varying trajectories rather than prose.[18][19] [Academic papers, 2023–2024] [HIGH]

**Refined system role:** symbolic planning is responsible for harmony, meter, repetition, and exact form; a conditioned audio model is responsible for arrangement, timbre, realism, and production. The rendered waveform must be re-analyzed against the retained symbolic plan, but the symbolic and audio measurements should remain separate under CRVP. [SYNTHESIS] [HIGH]

### Refined novelty claim

Text-conditioned symbolic generation, temporally local music control, audio-language grounding, and plural affect modeling all have prior work. The strongest defensible novelty is therefore the **combined intervention estimand and validation chain**: exact instruction plan → localized target/leakage/boundary diagnostics → cross-representation validation → distributional audio-grounded interpretation. [SYNTHESIS FROM INDEPENDENT AUDIT] [HIGH]

### Dataset refinement

MusicPile-SFT is the closest open instruction-schema source, while When-in-Rome and DCML corpora provide functional harmonic analyses that could be transformed into Roman-numeral-aligned instruction examples; these are analysis corpora, not ready-made instruction datasets, and score-level licenses and alignment must be audited before reuse.[1][20] [Research dataset/repository sources, 2024 and accessed 2026-08-06] [MEDIUM]

## Proposed Unified Research Program

### Work Package A — Instruction compiler and benchmark (best immediate project)

**Goal:** Parse free-form compositional requests into a typed plan and validate semantic equivalence.

**Inputs:** templated and paraphrased instructions covering key, mode, bars, meter, tempo, harmonic rhythm, Roman numerals, absolute chords, repetition, form, instrumentation, register, and local edits.

**Outputs:** canonical JSON plus clarification/error decisions.

**Baselines:** rules only; general-purpose LLM prompting; LLM plus deterministic tools; compact supervised parser; parser with constrained JSON decoding.

**Metrics:** field exact match, progression edit distance, transposition equivalence, bar-count validity, contradiction detection, clarification precision/recall, and adversarial paraphrase robustness.

**Undergraduate feasibility:** high. Most of the claim-bearing work is data design, deterministic validation, and small-model adaptation rather than foundation-model pretraining. [RECOMMENDATION] [HIGH]

### Work Package B — Constrained symbolic generation

**Goal:** Generate musically varied MIDI/ABC while obeying the accepted plan.

**Preferred baselines:** Text2MIDI, MuseCoco, ChatMusician, MuPT where checkpoint access permits, and a SymPAC-style constrained decoder.[1][2][3][5][9] [Academic systems, 2023–2025] [HIGH]

**Ablations:** direct caption conditioning; explicit plan tokens; SFT; LoRA; constrained decoding; post-generation rejection; deterministic repair; retrieval-augmented examples.

**Primary compliance metrics:** exact key, exact bar count, chord root/quality/function accuracy by bar, repetition identity/variation profile, parse success, and constraint-satisfaction rate.

**Separate outcomes:** musicality, originality, voice-leading, orchestration quality, and listener preference.

### Work Package C — Localized responsiveness and cross-representation validation

**Goal:** Extend CLPR from coarse audio instructions to exact symbolic compositional interventions.

**Design:** create one-field prompt pairs, hold the random draw or repeated-sample protocol fixed, validate exact symbolic differences, render with multiple synthesizers, and compare symbolic versus audio conclusions.

**Primary outputs:** TES and Directional Accuracy for requested changes; Off-Target Leakage for protected bars/features; Boundary Spillover for transitions; representation/renderer sensitivity as CRVP infrastructure. [Project record: `METRICS.md`, 2026-07-17] [Internal Research Record] [HIGH]

### Work Package D — Grounded interpretation of controlled changes

**Goal:** Determine whether the generated and verified musical changes yield distinguishable, audio-grounded differences in mood, imagery, tension, or narrative descriptions.

**Validity gates:** wrong-audio substitution, silence, temporal shuffle, cited-segment deletion, stem ablation, paraphrase controls, and listener-disagreement modeling. [Project record: `music-interpretation-poc/RESEARCH.md`, 2026-07-18] [Internal Research Record] [HIGH]

**Claim boundary:** report conditional listener/model associations and audio dependence; do not claim objective essence, authorial intent, or machine feeling.

## Contradictions Found

1. **“Text-to-MIDI supports keys and chords” versus weak exact control.** Text2MIDI states that captions may include chords and keys, yet its repository reports 33.6% exact-key accuracy and a 2.50/7 chord-matching listening score.[3][13] [Peer-reviewed paper + official repository] [CONFLICTING — capability exists, reliability is weak]
2. **“Natural-language control” versus supported-vocabulary dependence.** MuseCoco presents a natural-language interface, but its repository recommends predefined attribute values and warns that unsupported values degrade control.[2][14] [Academic paper + official repository] [CONFLICTING — interface is open-form, control ontology is largely closed]
3. **“LLMs can reason about music” versus benchmark performance near chance.** ChatMusician improves symbolic specialization but reports reasoning accuracy near the 25% random baseline, while ABC-Eval also reports substantial limitations.[1][12] [Peer-reviewed paper + academic preprint] [HIGH CONFIDENCE that reasoning remains unsolved]
4. **End-to-end elegance versus verifiability.** Text2MIDI criticizes two-stage inference as slower, while MuseCoco and SymPAC provide more inspectable or enforceable control paths.[2][3][5] [Academic papers] [CONFLICTING DESIGN PRIORITIES — no universal winner]
5. **Large synthetic captions enable scale versus introduce bias.** MetaScore and Text2MIDI gain data volume through LLM/pseudo captions, but such captions are derived from available metadata and therefore cannot teach constraints absent from that metadata.[3][4] [Academic papers] [MEDIUM; mechanism is clear, downstream bias magnitude unmeasured]

## Research Gaps

- No verified benchmark found for compound prompts jointly testing exact key, bar count, harmonic rhythm, Roman-numeral sequence, repetition semantics, and local structural edits. Evidence is insufficient to claim none exists; the search may have missed unpublished or poorly indexed work.
- No current paper reviewed here establishes near-perfect exact compliance on theory-rich symbolic requests across paraphrases and unseen keys.
- The best representation for balancing exact constraints, expressive performance, and multitrack orchestration remains unsettled.
- The amount of real rather than synthetic instruction data needed for generalization is unknown.
- The effect of constrained decoding on musicality and diversity requires experiment.
- Licensing and provenance remain unresolved for scraped symbolic/chord corpora and trained derivatives.[4][8] [Academic dataset papers] [MEDIUM]
- The causal effect of specific harmonic changes on mood or imagery is not established by the generation literature and requires controlled listener research.

## Recommendations Based on High-Confidence Findings

1. **Proceed, but frame the first contribution as instruction compilation plus verified symbolic compliance—not a new audio foundation model.**
2. **Use a hybrid system:** instruction-tuned parser + explicit plan schema + music-theory tools + constrained symbolic decoder + deterministic validator.
3. **Build the benchmark before training.** Include valid, ambiguous, contradictory, and impossible prompts; create clause-minimal counterfactual pairs.
4. **Start with chord-plan generation and accompaniment, not full songs.** Eight- to sixteen-bar MIDI examples make exact validation cheap and interpretable.
5. **Compare SFT with non-learning baselines.** Rules, tool-augmented prompting, constrained decoding, rejection sampling, and repair may outperform fine-tuning on hard constraints.
6. **Reuse CLPR immediately.** Symbolic interventions provide exact target/protected regions and resolve several alignment problems that complicate raw-audio experiments.
7. **Render only after symbolic validation.** Then use multiple renderers to test whether audio-side conclusions survive representation changes.
8. **Connect interpretation last.** Only analyze mood/imagery after compliance is established, and retain plural interpretations and audio-ablation gates.
9. **Do not claim “understanding” from syntactic compliance.** Separate language parsing, music-theory validity, compositional quality, audio realization, and human interpretation.
10. **Do not reproduce the full ChatMusician or Text2MIDI training recipes as an undergraduate first step.** Their reported multi-GPU training scales are unnecessary for a parser/adapter/benchmark contribution.[1][3] [Academic papers] [HIGH]

## Practical First Experiment

Create a deterministic benchmark with 500–2,000 synthetic base plans and multiple human-style paraphrases per plan. Keep a held-out split by progression family, key, and wording template. [PROPOSED SCALE; SPECULATION]

Begin with five instruction families:

1. key + exact Roman progression;
2. bar count + repetition count;
3. harmonic-rhythm change;
4. one-bar chord substitution;
5. transposition while preserving Roman function.

Evaluate four systems:

1. general LLM prompted to emit the plan schema;
2. general LLM plus deterministic music-theory tools;
3. compact instruction-tuned parser;
4. parser plus constrained symbolic generation.

The go/no-go result is simple: if deterministic tool augmentation already solves parsing but existing generators fail compliance, focus the paper on constrained generation and CLPR; if parsing itself fails on paraphrases and ambiguity, focus on the compiler benchmark. Either outcome is publishable only if the benchmark is independently validated and the test split defeats template memorization. [RESEARCH DESIGN] [MEDIUM]

## Sources

[1] ChatMusician: Understanding and Generating Music Intrinsically with LLM — https://aclanthology.org/2024.findings-acl.373/  
[2] MuseCoco: Generating Symbolic Music from Text — https://arxiv.org/abs/2306.00110  
[3] Text2MIDI: Generating Symbolic Music from Captions — https://arxiv.org/abs/2412.16526  
[4] Generating Symbolic Music from Natural Language Prompts using an LLM-Enhanced Dataset — https://arxiv.org/abs/2410.02084  
[5] SymPAC: Scalable Symbolic Music Generation With Prompts And Constraints — https://arxiv.org/abs/2409.03055  
[6] Instruct-MusicGen: Unlocking Text-to-Music Editing via Instruction Tuning — https://arxiv.org/abs/2405.18386  
[7] InstructME: An Instruction Guided Music Edit and Remix Framework — https://arxiv.org/abs/2308.14360  
[8] CHORDONOMICON — https://arxiv.org/abs/2410.22046  
[9] MuPT: A Generative Symbolic Music Pretrained Transformer — https://arxiv.org/abs/2404.06393  
[10] MusiLingo — https://aclanthology.org/2024.findings-naacl.231/  
[11] MusicAgent — https://aclanthology.org/2023.emnlp-demo.21/  
[12] ABC-Eval — https://arxiv.org/abs/2509.23350  
[13] Text2MIDI official repository — https://github.com/AMAAI-Lab/Text2midi  
[14] MuseCoco official repository — https://github.com/microsoft/muzic/tree/main/musecoco  
[15] Instruct-MusicGen official repository — https://github.com/ldzhangyx/instruct-MusicGen
[16] Mustango — https://arxiv.org/abs/2311.08355
[17] JASCO — https://arxiv.org/abs/2406.10970
[18] Coco-Mulla — https://arxiv.org/abs/2310.17162
[19] Music ControlNet — https://arxiv.org/abs/2311.07069
[20] When-in-Rome harmonic analysis corpus — https://github.com/MarkGotham/When-in-Rome
[21] FIGARO — https://arxiv.org/abs/2201.10936
[22] NotaGen — https://arxiv.org/abs/2502.18008
