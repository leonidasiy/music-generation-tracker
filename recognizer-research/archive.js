'use strict';
const el = id => document.getElementById(id);
let allEntries = [];
function node(tag, text, cls) {
  const result = document.createElement(tag);
  if (text !== undefined) result.textContent = String(text);
  if (cls) result.className = cls;
  return result;
}
function entry(title, fields, kind, index) {
  const article = node('article', undefined, 'entry'); article.dataset.kind = kind;
  article.id = kind + '-' + index;
  article.dataset.search = (kind + ' ' + title + ' ' + fields.map(pair => String(pair[1] ?? '')).join(' ')).toLocaleLowerCase();
  const details = document.createElement('details'); const summary = node('summary', title); details.append(summary);
  const body = node('div', undefined, 'detail');
  for (const [label, value] of fields) {
    if (value === undefined || value === null || value === '') continue;
    const paragraph = node('p'); paragraph.append(node('strong', label + ': '), document.createTextNode(String(value))); body.append(paragraph);
  }
  details.append(body); article.append(details); return article;
}
function filter() {
  const query = el('search').value.trim().toLocaleLowerCase();
  for (const item of allEntries) item.hidden = Boolean(query) && !item.dataset.search.includes(query);
  for (const group of el('milestone-groups').children) group.hidden = ![...group.querySelectorAll('.entry')].some(row => !row.hidden);
  const visible = allEntries.filter(item => !item.hidden).length;
  el('message').textContent = (document.body.dataset.state === 'error' ? 'Previously loaded records are stale. ' : '') + visible + ' of ' + allEntries.length + ' records shown. ' + (visible ? 'Open a record for its full historical detail.' : 'No matches; clear or change the search.');
}
function render(status, overview) {
  const idCategory = new Map();
  for (const category of overview.categories) for (const id of category.milestone_ids) idCategory.set(id, category.id);
  el('checkpoint').textContent = status.checkpoint;
  for (const [field, key] of [['milestone-count', 'milestones'], ['finding-count', 'findings'], ['activity-count', 'activity']]) el(field).textContent = '(' + status[key].length + ')';
  const groups = el('milestone-groups'); groups.replaceChildren();
  for (const category of overview.categories) {
    const items = status.milestones.filter(item => idCategory.get(item.id) === category.id);
    const section = node('section', undefined, 'group'); section.id = 'group-' + category.id;
    const heading = node('h3', category.title + ' · ' + items.length); heading.id = section.id + '-heading'; section.setAttribute('aria-labelledby', heading.id); section.append(heading);
    for (const item of items) section.append(entry(item.title, [['ID', item.id], ['Status', item.status], ['Evidence type', item.evidence_type], ['Detail', item.detail]], 'milestone', item.id));
    groups.append(section);
  }
  el('finding-list').replaceChildren(...status.findings.map((item, index) => entry(item.title, [['Finding', item.detail], ['Evidence type', item.evidence_type], ['Confidence', item.confidence], ['Source', item.source]], 'finding', index)));
  el('activity-list').replaceChildren(...status.activity.map((item, index) => entry(item.title, [['Time', item.time], ['Action', item.action], ['Result', item.result], ['Status', item.status]], 'activity', index)));
  allEntries = [...document.querySelectorAll('.entry')]; filter();
}
async function load() {
  const button = el('refresh'); button.disabled = true; document.body.dataset.state = 'loading';
  el('message').className = ''; el('message').textContent = 'Loading complete categorized checkpoint…';
  const controller = new AbortController(); const timer = setTimeout(() => controller.abort(), 15000);
  try {
    const {status, overview} = await RecognizerCheckpoint.fetchPair(controller.signal); render(status, overview);
    document.body.dataset.state = 'ready';
  } catch (error) {
    el('message').className = 'error'; el('message').textContent = 'Could not verify the archive or category coverage. Any previously displayed records are stale; retry or open status.json.';
    document.body.dataset.state = 'error';
  } finally { clearTimeout(timer); button.disabled = false; }
}
el('search').addEventListener('input', filter);
el('refresh').addEventListener('click', load);
load();
