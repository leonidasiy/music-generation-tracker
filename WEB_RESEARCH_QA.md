# Local Web Research Stack — Reliability Gate

> Tested: 2026-07-16 20:04 HKT
> Stack: DDGS search; direct HTTP + Trafilatura extraction; Jina Reader fallback

## Executive result

The stack is **fit for research discovery and primary-source extraction with verification safeguards**, but it is not an archival search index and should not be treated as one. Exact-paper discovery had high observed yield in this five-target known-item benchmark; result-set stability was weak. Public-URL extraction succeeded for all eight tested public cases, but most source classes had only one example, HTML landing pages may expose only metadata, and long documents may be summarized by the Hermes tool layer.

Raw ordered URLs, labels, per-query Jaccard values, extraction routes, lengths, and observations are stored in [`WEB_RESEARCH_QA_RAW.json`](WEB_RESEARCH_QA_RAW.json). Jaccard is `|run1 URLs ∩ run2 URLs| / |run1 URLs ∪ run2 URLs|`.

## Search benchmark

Five known academic targets were queried twice with five results per query:

1. Dorfer et al., arXiv:1707.09887
2. Hu et al., arXiv:2406.08454
3. McFee et al., hierarchical structure / L-measure
4. MusicGen, arXiv:2306.05284
5. PIAST, arXiv:2411.02551

### Observed

- A primary paper, publisher, or repository page appeared in the top five in **9/10 query-runs**.
- A primary paper, publisher, or repository page appeared at rank one in **9/10 query-runs**.
- Mean exact-URL Jaccard overlap between repeated result sets was **0.180**.
- The least stable case was arXiv:1707.09887: one run returned arXiv/ar5iv; the other returned author profiles and a citing thesis. The descriptions still referred to the correct paper, but no primary paper page appeared in that second top-five set.

### Judgment

- **Known-item lookup with title or identifier:** high observed utility in this five-target test; out-of-sample reliability was not estimated.
- **Broad discovery:** useful but non-exhaustive.
- **Rank stability / reproducible systematic review search:** low.
- **Citation counts from snippets:** unacceptable as a sole source.

DDGS should generate candidate URLs, not constitute the evidentiary record.

## Extraction benchmark

Tested eight public sources and one blocked private target. Most public source classes had one example; PDFs had two:

- arXiv abstract HTML
- PMC full article HTML
- ACL Anthology landing page
- PMLR article page
- GitHub repository page
- Hermes Docusaurus documentation
- arXiv PDF
- Stanford-hosted conference PDF
- localhost/private URL safety case

### Observed

- Public extraction success: **8/8**.
- Private/internal URL blocking: **1/1**, correctly rejected before connection.
- Titles and expected topical terms were present for all eight public cases.
- PDF fallback produced detailed, topically faithful text for both tested PDFs.
- Important limitation: the ACL Anthology HTML page yielded bibliographic metadata and a PDF link, not the paper body. Research requiring claims from the paper must extract the linked PDF.
- Long pages and papers can be summarized/truncated by the Hermes `web_extract` presentation layer. A fluent summary is not a verbatim quotation and cannot support exact-wording claims without checking the PDF or raw page.

### Judgment

- **Metadata and abstract extraction:** 8/8 observed public-case success; broader reliability is unestimated.
- **Topical full-paper understanding:** successful on the two tested PDFs, but broader reliability is unestimated.
- **Verbatim quotation / page-level fidelity:** not established by this benchmark; check the primary PDF.
- **Completeness across arbitrary sites:** not estimated. JavaScript-heavy, login-gated, anti-bot, and metadata-only pages still require browser or PDF fallback.

## Operating protocol for this project

1. Search with exact titles, arXiv IDs, DOIs, or author names whenever possible.
2. Treat DDGS rankings and snippets as discovery evidence only.
3. Prefer primary academic pages: arXiv, publisher proceedings, PMC, ACL Anthology, PMLR, DOI landing pages, and official repositories.
4. For claims beyond the abstract, extract the PDF or full article—not merely a landing page.
5. Verify key factual claims against at least two independent sources or one primary paper plus its official code/data repository.
6. Do not infer citation counts from DDGS snippets. Use OpenAlex, Semantic Scholar, Crossref, or publisher metadata and record the retrieval date.
7. Preserve URLs and source type in `REFERENCES.md`; label summaries separately from quotations.
8. Re-run broad searches with query variants because low result-set overlap can hide papers.
9. For systematic-review-like coverage, supplement DDGS with arXiv API, OpenAlex, venue proceedings, backward references, and forward citations.
10. If extraction returns suspiciously short content, follow the PDF link or use browser extraction.

## Bottom line

**GO**, with safeguards. The new stack removes the Firecrawl quota bottleneck and is adequate for the current exploratory research. It does not remove the ordinary burden of source criticism; software rarely performs that miracle, despite marketing departments’ repeated attempts.
