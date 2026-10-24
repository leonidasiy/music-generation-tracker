"""Fail-closed deterministic projection of a curated recognizer research registry.

Never takes raw logs/transcripts as input. Private paths and credential-like values
are rejected, including encoded forms and dictionary keys, rather than redacted.
"""
import argparse
from datetime import datetime
import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import unquote

FIELDS = {'schema_version','checkpoint','updated_at','title','phase','summary','publication_ready','milestones','findings','blockers','next_steps','agents','activity','artifacts','limits','sources'}
PRIVATE = re.compile(r'(?i)(?:/Users(?:/|\\)|/home(?:/|\\)|~[/\\]|\.hermes(?:/|\\)|file://|localhost|127\.0\.0\.1|\[HOME\]|\[PROFILE\]|\b(?:token|api[_-]?key|password|secret|authorization)\s*[:=]|\bBearer\s+[a-z0-9])')

def validate_status(data):
    if not isinstance(data,dict) or set(data)!=FIELDS:
        raise ValueError('Unexpected registry fields')
    if type(data['schema_version']) is not int or data['schema_version']!=1:
        raise ValueError('Unsupported registry version')
    if data['publication_ready'] is not False:
        raise ValueError('Publication gate has not passed; manual reviewed schema migration required')
    for field in ('checkpoint','updated_at','title','phase','summary'):
        if not isinstance(data[field],str) or not data[field]:raise ValueError('Missing '+field)
    datetime.fromisoformat(data['updated_at'].replace('Z','+00:00'))
    for field in ('milestones','findings','blockers','next_steps','agents','activity','artifacts','limits','sources'):
        if not isinstance(data[field],list):raise ValueError('Expected list '+field)
    for row in data['milestones']:
        if set(row)!={'id','title','status','evidence_type','detail'} or row['status'] not in ('complete','running','blocked','pending'):
            raise ValueError('Invalid milestone')
    for artifact in data['artifacts']:
        if set(artifact)!={'name','bytes','sha256'}:raise ValueError('Invalid artifact record')
        name=artifact['name']
        if not isinstance(name,str) or not name or PurePosixPath(name).is_absolute() or '..' in PurePosixPath(name).parts or '\\' in name:
            raise ValueError('Unsafe artifact identity')
        if type(artifact['bytes']) is not int or artifact['bytes']<0 or not re.fullmatch('[a-f0-9]{64}',str(artifact['sha256'])):
            raise ValueError('Invalid artifact size/hash')
    encoded=json.dumps(data,ensure_ascii=False,sort_keys=True,allow_nan=False)
    if len(encoded.encode())>1048576:raise ValueError('Public registry exceeds 1 MiB')
    # JSON serialization includes every key and value; decode repeated URL escaping.
    decoded=encoded
    for _ in range(6):
        if PRIVATE.search(decoded):raise ValueError('Private path, local URL or credential-like text in registry')
        next_value=unquote(decoded)
        if next_value==decoded:break
        decoded=next_value
    if PRIVATE.search(decoded):raise ValueError('Encoded private material')
    return data

def publish_status(source,destination):
    data=validate_status(json.loads(Path(source).read_text()))
    destination=Path(destination)
    destination.parent.mkdir(parents=True,exist_ok=True)
    output=json.dumps(data,indent=2,ensure_ascii=False,allow_nan=False)+'\n'
    destination.write_text(output)
    return data

def main():
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('destination');a=p.parse_args()
    publish_status(a.source,a.destination)
    print('Validated and projected curated public status')

if __name__=='__main__':main()
