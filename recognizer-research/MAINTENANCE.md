# Recognizer Research — frontend maintenance contract

## Information architecture
- Default page: exactly four bounded area cards—rhythm/tempo, chords/harmony, instrument presence, lead/accompaniment. Each has a short current result, evidence/scope limit, next gate and direct evidence links.
- Keep the overview under900 visible words, excluding browser chrome. No append-only milestone, finding, activity, agent or hash inventory on the main page. Replace the relevant area summary after major changes.
- `status.json` retains detailed aggregate evidence/history. `overview.json` declares the matching source checkpoint/counts and maps every milestone ID to exactly one area or shared-evaluation category. Cross-endpoint experiments have a declared primary location; summaries may discuss each endpoint without duplicating milestones.
- `archive.html`/`archive.js` expose all categorized milestones and all findings/activity with accessible disclosure/search. Never silently truncate original history. Preserve stable evidence/document links and dated historical scope.

## Source-of-truth boundaries
Current research policy/state/tasks live in the associated researcher-profile project, not in old public activity. Update them and the area overview at major decisions. Keep round-specific permissions/budgets out of reusable skills and do not treat historical audit-only statements as global bans or unchecked TODOs as new authorization. Policy cleanup never resumes blocked experiments or resets admission counters.

Current lead-role evidence is a negative frozen learned-router result, not 'MoE never tested' or 'all MoE exhausted'. Private chord and local tempo implementation status differs from unchanged lead/presence components. Do not write blanket whole-app unchanged/no-gain claims that erase these distinctions.

## Validation and publication
1. Parse schemas and compute exact category coverage/counts; bound overview text/card count and reject source drift. Verify every explicit evidence/asset/anchor link resolves locally.
2. Scan full candidate keys/values for private paths, credentials, source identities and per-record arrays; use explicit aggregate allowlists. Keep original evidence/snapshot bytes unchanged and archive old docs before consolidation.
3. Test normal load, refresh, reload, failed-fetch/schema-mismatch recovery, keyboard navigation/search/disclosure, desktop/mobile whole-page overflow and console/runtime errors. Inspect screenshots; light mode and semantic labels are required.
4. Independently review exact candidate bytes/claims. A changed artifact invalidates its affected approval; retain failed/stale receipts and obtain successor review. Approval is scoped, not musical validation.
5. Run diff/source tests and commit only named reviewed site files. Wait for the exact-commit deployment, fetch changed live artifacts byte-for-byte and repeat visible desktop/mobile checks. Do not call push success a completed deployment.

Preserve underlying research evidence and `__pycache__`; no app edits, model/audio acquisition, training, installs or paid operations are authorized by frontend maintenance. Routine site milestones are not unsolicited musical-gain alerts; direct requested maintenance gets one consolidated completion report.
