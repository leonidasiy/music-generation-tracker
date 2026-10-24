'use strict';
const element = id => document.getElementById(id);
function node(tag, text, className) {
  const result = document.createElement(tag);
  if (text !== undefined) result.textContent = String(text);
  if (className) result.className = className;
  return result;
}
function list(id, rows, format = x => x) {
  element(id).replaceChildren(...rows.map(row => node('li', format(row))));
}
function render(data) {
  if (data.schema_version !== 1 || typeof data.checkpoint !== 'string' ||
      typeof data.publication_ready !== 'boolean' || !Array.isArray(data.milestones) ||
      !Array.isArray(data.findings) || !Array.isArray(data.activity)) throw new Error('Unsupported checkpoint schema');
  element('phase').textContent = data.phase;
  element('summary').textContent = data.summary;
  element('updated').textContent = 'Checkpoint updated: ' + data.updated_at;
  element('checkpoint').textContent = data.checkpoint;
  element('publication').textContent = data.publication_ready ? 'Evidence gate passed; submission still requires explicit approval.' : 'Not ready for an empirical submission.';
  const allowed = new Set(['complete','running','pending','blocked']);
  element('milestones').replaceChildren(...data.milestones.map(item => {
    const card = node('article', undefined, 'card');
    const state = allowed.has(item.status) ? item.status : 'pending';
    card.append(node('span',state,'badge '+state),node('h3',item.title),node('p',item.evidence_type,'meta'),node('p',item.detail));
    return card;
  }));
  element('findings').replaceChildren(...(data.findings.length ? data.findings.map(item => {
    const card = node('article',undefined,'card');
    card.append(node('h3',item.title),node('p',item.detail),node('p',item.evidence_type+' · Confidence: '+item.confidence,'meta'));
    if (item.source) card.append(node('p','Source: '+item.source,'meta'));
    return card;
  }) : [node('p','No new performance finding has cleared the execution-review gate.','muted')]));
  list('blockers',data.blockers); list('next',data.next_steps); list('limits',data.limits);
  list('agents',data.agents,item => item.responsibility+' — '+item.model+', '+item.reasoning+' reasoning');
  element('activity').replaceChildren(...data.activity.map(item => {
    const row = node('li');
    row.append(node('h3',item.title),node('p',item.time,'meta'),node('p',item.action),node('p',item.result));
    return row;
  }));
  element('content').hidden = false;
}
async function loadCheckpoint() {
  const button = element('refresh'); button.disabled = true;
  element('loadStatus').className = ''; element('loadStatus').textContent = 'Checking latest deployed checkpoint…';
  const controller = new AbortController(); const timeout = setTimeout(() => controller.abort(),15000);
  try {
    const response = await fetch('status.json?t='+Date.now(),{cache:'no-store',signal:controller.signal});
    if (!response.ok) throw new Error('HTTP '+response.status);
    const data = await response.json(); render(data);
    element('loadStatus').textContent = 'Deployed checkpoint loaded. This is not a live process stream.';
    document.body.dataset.state = 'ready';
  } catch (error) {
    element('loadStatus').className = 'error';
    element('loadStatus').textContent = 'Could not refresh the checkpoint. Previously displayed data, if any, is stale. Try again or open the status JSON.';
    document.body.dataset.state = 'error';
  } finally { clearTimeout(timeout); button.disabled = false; }
}
element('refresh').addEventListener('click',loadCheckpoint);
loadCheckpoint();
