'use strict';
const el = id => document.getElementById(id);
function textNode(tag, text, cls) {
  const node = document.createElement(tag);
  if (text !== undefined) node.textContent = String(text);
  if (cls) node.className = cls;
  return node;
}
function render(data) {
  el('checkpoint').textContent = data.source_checkpoint.checkpoint;
  el('summary').textContent = data.overall.summary;
  el('limits').replaceChildren(...data.overall.limitations.map(value => textNode('li', value)));
  const cards = data.cards.map(item => {
    const article = textNode('article', undefined, 'card'); article.id = item.id;
    article.setAttribute('aria-labelledby', item.id + '-heading');
    const title = textNode('h3', item.title); title.id = item.id + '-heading';
    article.append(textNode('span', 'Current result', 'badge'), title, textNode('p', item.result), textNode('p', item.limit, 'meta'));
    const gate = textNode('p'); gate.append(textNode('strong', 'Next gate: '), document.createTextNode(item.next)); article.append(gate);
    const links = textNode('div', undefined, 'links');
    for (const link of item.evidence) {
      const anchor = textNode('a', link.label); anchor.href = link.href; links.append(anchor);
    }
    article.append(links); return article;
  });
  el('cards').replaceChildren(...cards);
  const counts = data.source_checkpoint.counts;
  el('archive-link').textContent = 'Full archive: ' + counts.milestones + ' milestones · ' + counts.findings + ' findings · ' + counts.activity + ' activity records';
  el('content').hidden = false;
}
async function load() {
  const button = el('refresh'); button.disabled = true;
  el('loadStatus').textContent = 'Checking current area summaries…'; el('loadStatus').className = '';
  document.body.dataset.state = 'loading';
  const controller = new AbortController(); const timer = setTimeout(() => controller.abort(), 15000);
  try {
    const {overview} = await RecognizerCheckpoint.fetchPair(controller.signal); render(overview);
    el('loadStatus').textContent = 'Current area summaries loaded. Details remain in the archive.';
    document.body.dataset.state = 'ready';
  } catch (error) {
    el('loadStatus').textContent = 'Could not verify the current overview. Any previously displayed summaries are stale; retry or open the archive/source checkpoint.';
    el('loadStatus').className = 'error'; document.body.dataset.state = 'error';
  } finally { clearTimeout(timer); button.disabled = false; }
}
el('refresh').addEventListener('click', load);
load();
