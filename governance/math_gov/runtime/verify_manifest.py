"""Recompute exact file hashes in candidate distribution.

Verifies byte integrity only, not author identity, mathematical truth, live tool
executions or permission. Needs independently trusted manifest signature to gain authenticity.
"""
import hashlib, json, sys
from pathlib import Path

def sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    return h.hexdigest()

def verify(root):
    manifest=json.loads((root/'SHA256_MANIFEST.json').read_text())
    expected=manifest['files']
    actual={str(p.relative_to(root)).replace('\\', '/'):sha(p) for p in root.rglob('*') if p.is_file() and p != root/'SHA256_MANIFEST.json' and '__pycache__' not in p.parts and p.suffix!='.pyc'}
    missing=sorted(set(expected)-set(actual));extra=sorted(set(actual)-set(expected));changed=sorted(p for p in set(expected)&set(actual) if expected[p]!=actual[p])
    return {'verdict':'BYTE_INTEGRITY_PASS_UNAUTHENTICATED' if not (missing or extra or changed) else 'BYTE_INTEGRITY_FAILED',
            'missing':missing,'extra':extra,'changed':changed,'entries':len(expected),
            'note':'Integrity of this supplied manifest is NOT an authenticated publisher signature.'}

if __name__=='__main__':
    root=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).resolve().parents[1])
    ans=verify(root);print(json.dumps(ans,indent=2));sys.exit(0 if ans['verdict']=='BYTE_INTEGRITY_PASS_UNAUTHENTICATED' else 2)
