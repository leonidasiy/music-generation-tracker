# Noteworthy Information

## Research Domains Covered
1. **Music Generation** — Text-to-music, symbolic music generation, raw audio generation
2. **Music Orchestration** — Automatic arrangement, instrumentation selection, multi-track generation
3. **Model Architectures** — Diffusion models, transformers, autoregressive, GANs, language models for music

## Key Conference Venues
- ISMIR (International Society for Music Information Retrieval)
- ICASSP (IEEE International Conference on Acoustics, Speech and Signal Processing)
- NeurIPS (Neural Information Processing Systems)
- ICML (International Conference on Machine Learning)
- ICLR (International Conference on Learning Representations)
- ACM MM (Multimedia)

## Major Industry Models (frontier)
- **MusicGen** (Meta, 2023) — Transformer-based text-to-music, released open-source
- **Suno** — Proprietary, high-quality song generation from lyrics
- **Udio** — Proprietary, high-fidelity music generation
- **Stable Audio** (Stability AI) — Diffusion-based audio generation
- **Jukebox** (OpenAI, 2020) — VQ-VAE + transformer for raw audio
- **MusicLM** (Google, 2023) — Hierarchical text-to-music
- **Riffusion** — Stable Diffusion fine-tuned on spectrograms

## Key Research Directions (2024–2026)
- Controllable music generation (genre, tempo, key, structure)
- Long-form coherent music (full songs vs short clips)
- Multi-track / stem-based generation
- Music understanding + generation joint models
- Efficiency improvements (latency, memory, real-time generation)
- Evaluation metrics beyond FAD (Fréchet Audio Distance)

## Metric Exploration Principles — 2026-07-16
- Treat the benchmark as a diagnostic scorecard, not a universal scalar.
- Separate generator error, analysis/recognizer error, and instruction ambiguity.
- Evaluate recurrence by requested role and transformation, not repetition quantity alone.
- Use counterfactual prompt pairs to test localized responsiveness rather than incidental compliance.
- Borrow relations—not superficial metaphors—from other arts: film pacing, narrative setup/payoff, poetic enjambment, choreographic transformation, and architectural local/global intelligibility.
- Validate every candidate with controlled corruptions, held-out generators, human construct ratings, and simple confound baselines.
