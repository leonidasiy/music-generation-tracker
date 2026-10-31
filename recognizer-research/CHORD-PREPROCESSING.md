# Chord harmonic-emphasis frontend: executed smoke, not an accuracy result

## Executive summary
One previously exposed guitar recording passed an actual original-versus-fixed-HPSS waveform inference smoke, with four real model forwards and independent saved-output verification. The mandatory original arm exactly reproduced its decoded waveform, five saved acoustic arrays and native events. No reference accuracy was measured, so this is neither an achieved improvement nor a rejection of preprocessing. [A13 frozen execution and independent reconstruction, 31 Oct 2026; Internal experiment/review; HIGH scoped confidence]

## Key findings
- Fixed intervention: half original waveform plus half HPSS harmonic reconstruction, at22050Hz, STFT2048/hop512,31×31 HPSS kernels, power2 and margins1. No new model, fitting, paid service, adapter normalization or production change. The existing model's own chunk normalization remains unchanged. [Frozen protocol/source, 31 Oct 2026; Internal implementation; HIGH scoped confidence]
- One outcome-independent first entry of the existing60-case roster;22.32439909297052seconds, not a cropped or outcome-chosen case. This is inspected development material, not confirmation. [Frozen roster and original cache, 31 Oct 2026; Internal evidence; HIGH scoped confidence]
- Four actual model forwards: two padded20-second chunks per arm. Each yields242 valid clipped frames on exactly the same clock; full padded raw outputs are retained privately for audit. [Actual hooks and independent reconstruction, 31 Oct 2026; Internal execution/review; HIGH scoped confidence]
- Baseline waveform hash, starts/ends/root/pitch/bass arrays and native events match exactly. Fifteen DSP controls and nine supervisor controls pass; actual tiny-child deadline/pressure termination was tested. [Controls and parity receipts, 31 Oct 2026; Internal verification; HIGH scoped confidence]
- The processed arm changes30 raw root-argmax frames and native events9→7. Neither count establishes better or worse accuracy or segmentation; no reference scores were computed. [Saved predictions/reconstruction, 31 Oct 2026; Internal diagnostic; HIGH scoped confidence]

## Contradictions and limits
Source-separation remix papers do not establish that this simple HPSS blend benefits this model. The [2025 APSIPA paper](https://www.apsipa.org/proceedings/2025/papers/APSIPA2025_P307.pdf) reports a small duration/frame-level net gain using neural stems and a selected remix setting, while a [negative author implementation](https://ko28.github.io/chord-transcription) reports worse average results under a different model/training setup. These are not matched replications; no transfer effect to this HPSS recipe is established. [Authors' reports, 2025/undated; Academic paper/author project; MEDIUM, requires additional verification for transfer]

A [related learned-remix chapter](https://link.springer.com/chapter/10.1007/978-3-032-30573-2_24) was published online10 July2026 with a2027 citation year. Accessible metadata do not provide a usable numerical denominator or demonstrate this untrained fixed blend; related authors are not independent confirmation. [Publisher metadata/abstract, 2026; Academic publisher; MEDIUM, requires additional verification]

## Research gaps and next test
Freeze a broader matched roster and the existing root-only/strict-triad/expanded-full-pitch scoring policies before new outcome comparison. Preserve recording-failure incidence as headline, severe/missing separately and all regressions/category supports; do not replace it with an attractive duration-only aggregate. One exposed guitar recording cannot validate genre/audio-type robustness or broad below30% error. Do not change production on this smoke. [Protocol and evidence limits, 31 Oct 2026; Internal design; HIGH scoped confidence]

[Current comparison](CAMPAIGN.md) · [Curated aggregates](autonomous-summary.json)
