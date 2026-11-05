'use strict';
// Synthetic contract mutations, not musical measurements.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const {webcrypto} = require('node:crypto');
const site = path.resolve(__dirname, '../recognizer-research');
const statusText = fs.readFileSync(path.join(site,'status.json'),'utf8');
const overviewText = fs.readFileSync(path.join(site,'overview.json'),'utf8');
const status = JSON.parse(statusText), overview = JSON.parse(overviewText);
const code = fs.readFileSync(path.join(site,'checkpoint.js'),'utf8');
let checks=0;
function context(fetch) {
  const ctx = {crypto:webcrypto,TextEncoder,Uint8Array,fetch,module:{exports:{}}};
  vm.runInNewContext(code,ctx); return ctx.module.exports;
}
const contract=context();contract.validate(status,overview);checks++;
const copy=value=>JSON.parse(JSON.stringify(value));
function rejects(mutate) {const s=copy(status),o=copy(overview);mutate(s,o);assert.throws(()=>contract.validate(s,o));checks++;}
rejects((s,o)=>o.source_checkpoint.checkpoint='synthetic-stale');
rejects((s,o)=>o.source_checkpoint.updated_at='synthetic-old');
rejects((s,o)=>o.source_checkpoint.sha256='invalid');
rejects((s,o)=>o.source_checkpoint.counts.milestones--);
rejects((s,o)=>o.overall.archive_counts.activity--);
rejects((s,o)=>o.categories[0].milestone_ids.pop());
rejects((s,o)=>o.categories[0].milestone_ids.push(o.categories[1].milestone_ids[0]));
rejects((s,o)=>o.categories[0].milestone_ids[0]='synthetic-unknown');
rejects((s,o)=>o.categories[0].id='synthetic-category');
rejects((s,o)=>o.cards.pop());
rejects((s,o)=>o.cards[0].id=o.cards[1].id);
rejects((s,o)=>o.cards[0].result='word '.repeat(66));
rejects((s,o)=>o.cards[0].limit='');
rejects((s,o)=>o.cards[0].evidence[0].href='javascript:alert(1)');
rejects((s,o)=>o.cards[0].evidence[0].href='../../unexpected');
rejects((s,o)=>s.milestones.push(s.milestones[0]));
rejects((s,o)=>s.schema_version=99);
async function run() {
  let mode='valid';
  const fetch=async url=>({ok:mode!=='http',status:mode==='http'?503:200,text:async()=>url.startsWith('status.json')?(mode==='bytes'?statusText+' ':statusText):(mode==='parse'?'{':overviewText)});
  const c=context(fetch);await c.fetchPair();checks++;
  for (const fault of ['http','parse','bytes']) {mode=fault;await assert.rejects(c.fetchPair());checks++;}
  console.log(JSON.stringify({status:'PASS',contract_checks:checks,scope:'Synthetic schema/drift/link/fetch guards only; not model reliability gains'}));
}
run().catch(error=>{console.error(error);process.exitCode=1;});
