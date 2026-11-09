"""Deterministic compact-progress checks; no network or model inference."""
import hashlib
import json
import re
import unittest
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'recognizer-research'

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        for field in ['href', 'src']:
            if field in attrs: self.links.append(attrs[field])

class CompactProgressTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.status=json.loads((SITE/'status.json').read_text())
        cls.overview=json.loads((SITE/'overview.json').read_text())
    def test_source_bytes_bound(self):
        self.assertEqual(hashlib.sha256((SITE/'status.json').read_bytes()).hexdigest(),self.overview['source_checkpoint']['sha256'])
    def test_current_checkpoint(self):
        for field in ['checkpoint','updated_at']:
            self.assertEqual(self.status[field],self.overview['source_checkpoint'][field])
    def test_all_original_records_counted(self):
        for kind in ['milestones','findings','activity']:
            self.assertEqual(len(self.status[kind]),self.overview['source_checkpoint']['counts'][kind])
            self.assertEqual(len(self.status[kind]),self.overview['overall']['archive_counts'][kind])
    def test_exact_disjoint_category_cover(self):
        mapped=[m for c in self.overview['categories'] for m in c['milestone_ids']]
        self.assertEqual(Counter(mapped),Counter(m['id'] for m in self.status['milestones']))
        self.assertTrue(all(v==1 for v in Counter(mapped).values()))
    def test_four_application_areas(self):
        self.assertEqual({r['id'] for r in self.overview['cards']},{'rhythm-tempo','chords-harmony','instrument-presence','lead-accompaniment'})
        self.assertEqual(len(self.overview['cards']),4)
    def test_budgeted_card_prose(self):
        for row in self.overview['cards']:
            for field,cap in [('title',8),('result',65),('limit',50),('next',45)]:
                self.assertLessEqual(len(row[field].split()),cap,(row['id'],field))
            self.assertLessEqual(len(row['evidence']),3)
    def test_known_endpoints_still_distinct(self):
        rows={r['id']:r for r in self.overview['cards']}
        lead=json.dumps(rows['lead-accompaniment']); chord=json.dumps(rows['chords-harmony']); presence=json.dumps(rows['instrument-presence'])
        self.assertIn('5/6',lead);self.assertIn('voice-component value unproven',lead);self.assertIn('No reliability gain',lead)
        historical=json.dumps(next(x for x in self.status['milestones'] if x['id']=='moe-learned-router-20261105'))
        self.assertIn('hard12',historical);self.assertIn('match the strongest expert',historical)
        posthoc=json.loads((SITE/'lead-vocal-confirmation-aggregate.json').read_text())['posthoc_diagnostic']
        self.assertEqual(posthoc['hits'],5);self.assertEqual(posthoc['relation_to_frozen_candidate'],'tie')
        self.assertIn('no inference',posthoc['status']);self.assertIn('unproven',posthoc['implication'])
        self.assertIn('3/7',chord);self.assertIn('below-30%',chord);self.assertIn('ordinary default',chord)
        self.assertIn('55/292',presence);self.assertIn('22 invalid',presence);self.assertIn('149 missing',presence)
    def test_lead_confirmation_is_aggregate_only_and_qualifies_posthoc_result(self):
        path=SITE/'lead-vocal-confirmation-aggregate.json'
        raw=path.read_text(); parsed=json.loads(raw)
        for case_id in ['B01','B02','B03','B04','B05','B06','B07','B08']:
            self.assertNotIn(case_id,raw)
        for key in ['cases','audit','emitted','source_path','source_sha256','artist','recording','track']:
            self.assertNotIn(key,parsed)
        self.assertEqual(parsed['primary']['candidate']['hits'],5)
        self.assertEqual(parsed['paired_comparisons']['candidate_vs_role_cap2']['rescues'],1)
        diagnostic=parsed['posthoc_diagnostic']
        self.assertEqual(diagnostic['hits'],5)
        self.assertIn('post-hoc',diagnostic['status'])
        self.assertIn('not a new model test',diagnostic['implication'])
        self.assertEqual(parsed['interpretation']['application_adoption'],'not_authorized_or_claimed')
        self.assertEqual(parsed['interpretation']['independent_broad_validation'],'not_established')
    def test_local_evidence_allowlist(self):
        allowed=set(self.overview['link_allowlist'])
        for row in self.overview['cards']:
            for link in row['evidence']:
                self.assertIn(link['href'],allowed); self.assertTrue((SITE/link['href']).is_file())
                self.assertFalse(urlparse(link['href']).scheme)
    def test_html_ids_and_links(self):
        for name in ['index.html','archive.html']:
            parser=Links();parser.feed((SITE/name).read_text())
            self.assertEqual(len(parser.ids),len(set(parser.ids)))
            for href in parser.links:
                target=urlparse(href)
                if target.scheme:continue
                if target.path:self.assertTrue((SITE/target.path).exists(),(name,href))
                if target.fragment and not target.path:
                    self.assertTrue(target.fragment in parser.ids or target.fragment in {r['id'] for r in self.overview['cards']},(name,href))
    def test_no_raw_feed_on_default(self):
        text=(SITE/'index.html').read_text()
        self.assertNotIn('id="milestones"',text);self.assertNotIn('id="activity"',text);self.assertNotIn('id="findings"',text)
        self.assertIn('archive.html',text);self.assertIn('color-scheme" content="light',text)
    def test_no_html_injection_rendering(self):
        for name in ['app.js','archive.js','checkpoint.js']:
            text=(SITE/name).read_text();self.assertNotIn('innerHTML',text);self.assertNotIn('insertAdjacentHTML',text)
    def test_aggregate_prose_no_private_literals(self):
        text=(SITE/'overview.json').read_text()
        for _ in range(3): text=unquote(text)
        for pattern in [r'/Users/[^\s"<>]+',r'/home/[^\s"<>]+',r'file://',r'(?i)bearer\s+[A-Za-z0-9._-]{16,}',r'gh[pousr]_[A-Za-z0-9]{20,}']:
            self.assertIsNone(re.search(pattern,text),pattern)
        self.assertNotIn('Verified artifact identities',text)
    def test_maintained_docs_links(self):
        for name in ['PROGRESS.md','METHODS.md','MAINTENANCE.md']:
            text=(SITE/name).read_text()
            for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
                if not urlparse(href).scheme:self.assertTrue((SITE/urlparse(href).path).exists(),(name,href))
    def test_history_files_preserved(self):
        for name in ['PROGRESS-HISTORY.md','METHODS-HISTORY.md']:
            self.assertTrue((SITE/name).is_file())

if __name__=='__main__':unittest.main()
