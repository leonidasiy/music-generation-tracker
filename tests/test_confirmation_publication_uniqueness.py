"""Public evidence allowlists must be unique and free of transient prep state."""
import json
import re
import unittest
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / 'recognizer-research'

class ConfirmationPublicationTests(unittest.TestCase):
    def test_overview_allowlist_unique(self):
        data = json.loads((SITE / 'overview.json').read_text())
        self.assertEqual(len(data['link_allowlist']), len(set(data['link_allowlist'])))

    def test_javascript_allowlist_unique(self):
        source = (SITE / 'checkpoint.js').read_text()
        values = re.search(r'const LINKS = new Set\(\[(.*?)\]\)', source).group(1)
        names = re.findall(r'[\'\"]([^\'\"]+)[\'\"]', values)
        self.assertEqual(len(names), len(set(names)))

    def test_lead_card_has_no_obsolete_prepublication_state(self):
        data = json.loads((SITE / 'overview.json').read_text())
        card = next(c for c in data['cards'] if c['id'] == 'lead-accompaniment')
        text = json.dumps(card).casefold()
        for obsolete in ['publication pending review', 'parent public review', 'deployment remain pending']:
            self.assertNotIn(obsolete, text)

if __name__ == '__main__':
    unittest.main()
