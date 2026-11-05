'use strict';
// Shared, dependency-free source/overview contract. No outcome is inferred here.
(function (root) {
  const AREA_IDS = ['rhythm-tempo', 'chords-harmony', 'instrument-presence', 'lead-accompaniment'];
  const CATEGORY_IDS = [...AREA_IDS, 'shared-evaluation'];
  const LINKS = new Set(['lead-vocal-specialist.json','lead-passt-cap2.json','lead-cap2-promise.json','lead-role-readout-diagnosis.json',"lead-inclusive-hit.json",'moe-learned-router.json','btc-private-seven.json','btc-app-six.json','lead-role-pilot.json','private-chord-adoption.json','full64-complete.json','panns-matched.json','instrument-presence-summary.json','progress-numbers.json','METHODS.md','PRACTICAL-SOLUTIONS.md','FOLLOWUP.md','CAMPAIGN.md','EXTENDED.md','TUNING.md']);
  const requireThat = (value, message) => { if (!value) throw new Error(message); };
  const isText = value => typeof value === 'string' && value.trim().length > 0;
  const wordCount = value => String(value).trim().split(/\s+/).length;
  function validate(status, overview) {
    requireThat(status?.schema_version === 1 && overview?.schema_version === 1, 'Unsupported checkpoint schema');
    const source = overview.source_checkpoint;
    requireThat(source?.file === 'status.json' && source.checkpoint === status.checkpoint && source.updated_at === status.updated_at, 'Overview is stale: source checkpoint changed');
    requireThat(/^[a-f0-9]{64}$/.test(source.sha256), 'Missing source-byte binding');
    for (const field of ['milestones', 'findings', 'activity']) {
      requireThat(Array.isArray(status[field]) && source.counts?.[field] === status[field].length && overview.overall?.archive_counts?.[field] === status[field].length, 'Checkpoint count drift: ' + field);
    }
    requireThat(Array.isArray(overview.categories) && overview.categories.length === CATEGORY_IDS.length, 'Category count mismatch');
    const categories = new Set(); const mapped = new Set();
    for (const category of overview.categories) {
      requireThat(CATEGORY_IDS.includes(category.id) && !categories.has(category.id) && isText(category.title) && Array.isArray(category.milestone_ids), 'Invalid or duplicate category');
      categories.add(category.id);
      for (const id of category.milestone_ids) {
        requireThat(isText(id) && !mapped.has(id), 'Duplicate milestone mapping'); mapped.add(id);
      }
    }
    const sourceIDs = status.milestones.map(row => row.id);
    requireThat(new Set(sourceIDs).size === sourceIDs.length && mapped.size === sourceIDs.length && sourceIDs.every(id => mapped.has(id)), 'Milestone category coverage mismatch');
    requireThat(Array.isArray(overview.cards) && overview.cards.length === AREA_IDS.length, 'Overview must contain four area cards');
    const cards = new Set();
    for (const card of overview.cards) {
      requireThat(AREA_IDS.includes(card.id) && !cards.has(card.id), 'Invalid or duplicate area card'); cards.add(card.id);
      for (const [field, cap] of [['title', 8], ['result', 65], ['limit', 50], ['next', 45]]) {
        requireThat(isText(card[field]) && wordCount(card[field]) <= cap, 'Area text exceeds budget or is missing: ' + field);
      }
      requireThat(Array.isArray(card.evidence) && card.evidence.length > 0 && card.evidence.length <= 3, 'Evidence-link budget mismatch');
      for (const link of card.evidence) requireThat(LINKS.has(link.href) && isText(link.label), 'Disallowed evidence link');
    }
    requireThat(isText(overview.overall.summary) && wordCount(overview.overall.summary) <= 60 && Array.isArray(overview.overall.limitations) && overview.overall.limitations.length <= 3, 'Overall summary budget mismatch');
    requireThat(overview.overall.limitations.every(x => isText(x) && wordCount(x) <= 45), 'Invalid limitation');
    return {status, overview};
  }
  async function fetchPair(signal) {
    const stamp = Date.now();
    const responses = await Promise.all(['status.json', 'overview.json'].map(file => fetch(file + '?refresh=' + stamp, {cache:'no-store', signal})));
    for (const response of responses) requireThat(response.ok, 'Checkpoint HTTP ' + response.status);
    const [sourceText, overviewText] = await Promise.all(responses.map(response => response.text()));
    const status = JSON.parse(sourceText); const overview = JSON.parse(overviewText);
    validate(status, overview);
    const digest = await root.crypto.subtle.digest('SHA-256', new TextEncoder().encode(sourceText));
    const actual = Array.from(new Uint8Array(digest), x => x.toString(16).padStart(2, '0')).join('');
    requireThat(actual === overview.source_checkpoint.sha256, 'Overview is stale: source bytes changed');
    return {status, overview};
  }
  root.RecognizerCheckpoint = Object.freeze({validate, fetchPair});
  if (typeof module !== 'undefined' && module.exports) module.exports = root.RecognizerCheckpoint;
})(globalThis);
