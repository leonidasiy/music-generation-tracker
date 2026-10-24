import json
from pathlib import Path
import tempfile
import unittest
from publish_recognizer_status import validate_status, publish_status

class PublicStatusTests(unittest.TestCase):
    def sample(self):
        return {'schema_version':1,'checkpoint':'test-checkpoint','updated_at':'2026-10-24T00:00:00Z','title':'Recognizer Research','phase':'Test','summary':'No gain claimed','publication_ready':False,'milestones':[],'findings':[],'blockers':[],'next_steps':[],'agents':[],'activity':[],'artifacts':[],'limits':[],'sources':[]}
    def test_valid_projection_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/'src.json';dest=Path(d)/'status.json'
            src.write_text(json.dumps(self.sample()))
            publish_status(src,dest)
            self.assertEqual(json.loads(dest.read_text()),self.sample())
    def test_private_paths_keys_and_encoded_forms_fail(self):
        for s in ['/Users/private/source','file:///home/name/data','~/.hermes/profiles/name','%252FUsers%252Fname%252Ffile','https://127.0.0.1:8100','[HOME]/.hermes/profiles/private','token=abcdefghijk']:
            for in_key in (True,False):
                d=self.sample();d['activity']=[{s:'safe'} if in_key else {'summary':s}]
                with self.assertRaises(ValueError,msg=s):validate_status(d)
    def test_artifact_hash_and_size_are_required(self):
        d=self.sample();d['artifacts']=[{'name':'local/result.json','bytes':3,'sha256':'bad'}]
        with self.assertRaises(ValueError):validate_status(d)
    def test_nan_and_wrong_schema_fail(self):
        for key,value in [('summary',float('nan')),('schema_version',2),('publication_ready','false')]:
            d=self.sample();d[key]=value
            with self.assertRaises(ValueError):validate_status(d)
    def test_parent_traversal_artifact_fails(self):
        d=self.sample();d['artifacts']=[{'name':'../private','bytes':1,'sha256':'a'*64}]
        with self.assertRaises(ValueError):validate_status(d)
    def test_publication_change_fails_closed(self):
        d=self.sample();d['publication_ready']=True
        with self.assertRaises(ValueError):validate_status(d)

if __name__=='__main__':unittest.main()
