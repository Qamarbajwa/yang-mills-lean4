"""Durable exact-byte prompt/result ledger, with detectability of local edits.

This is NOT cryptographic authentication. A full ledger can be rewritten unless its
head digest is independently anchored in a trusted separate system.
"""
import argparse
import base64
import binascii
import hashlib
import json
import sqlite3
from datetime import datetime,timezone
from pathlib import Path


def h(s: bytes): return hashlib.sha256(s).hexdigest()

def encode_bytes(b: bytes):
    return {'base64':base64.b64encode(b).decode('ascii'),'sha256':h(b),'byte_length':len(b)}

def verify_bytes(o):
    if not isinstance(o,dict): raise ValueError('missing bytes record')
    raw=base64.b64decode(o['base64'],validate=True)
    if h(raw)!=o['sha256'] or len(raw)!=o['byte_length']:
        raise ValueError('byte payload integrity mismatch')
    return raw

def init(conn):
    conn.execute('CREATE TABLE IF NOT EXISTS events (seq INTEGER PRIMARY KEY, prev TEXT NOT NULL, event TEXT NOT NULL, hash TEXT NOT NULL)')
    conn.commit()

def append(conn,kind,actor,subject_id,prompt: bytes,result: bytes,metadata=None):
    if not all(isinstance(x,str) and x.strip() for x in (kind,actor,subject_id)):
        raise ValueError('missing event category, actor or subject')
    metadata = metadata if metadata is not None else {}
    if not isinstance(metadata,dict): raise ValueError('metadata must be object')
    event={'kind':kind,'actor':actor,'subject_id':subject_id,
           'recorded_at_utc_unattested':datetime.now(timezone.utc).isoformat(),
           'prompt':encode_bytes(prompt),'result':encode_bytes(result),'metadata':metadata}
    payload=json.dumps(event,sort_keys=True,ensure_ascii=False,separators=(',',':'))
    conn.execute('BEGIN IMMEDIATE')
    last=conn.execute('SELECT seq,hash FROM events ORDER BY seq DESC LIMIT 1').fetchone()
    seq=1 if last is None else last[0]+1
    prev='0'*64 if last is None else last[1]
    item_hash=h((prev+'\n'+str(seq)+'\n'+payload).encode('utf-8'))
    conn.execute('INSERT INTO events(seq,prev,event,hash) VALUES(?,?,?,?)',(seq,prev,payload,item_hash))
    conn.commit()
    return {'seq':seq,'event_hash':item_hash,'anchor_required':'Save this head digest with a separate trusted host'}

def verify(conn,externally_anchored_head=None,expected_count=None):
    rows=conn.execute('SELECT seq,prev,event,hash FROM events ORDER BY seq').fetchall()
    prev='0'*64
    for expected_seq,(seq,linked,data,recorded) in enumerate(rows,1):
        if seq!=expected_seq or linked!=prev:
            return {'verdict':'TAMPER_OR_GAP_DETECTED','at':expected_seq}
        try:
            obj=json.loads(data)
            verify_bytes(obj['prompt']);verify_bytes(obj['result'])
        except (ValueError,KeyError,TypeError,binascii.Error) as e:
            return {'verdict':'TAMPER_OR_INVALID_EVENT','at':expected_seq,'error':str(e)}
        if h((prev+'\n'+str(seq)+'\n'+data).encode('utf-8'))!=recorded:
            return {'verdict':'TAMPER_DETECTED','at':expected_seq}
        prev=recorded
    if externally_anchored_head is not None and prev!=externally_anchored_head:
        return {'verdict':'EXTERNAL_ANCHOR_MISMATCH','head':prev,'count':len(rows)}
    if expected_count is not None and expected_count!=len(rows):
        return {'verdict':'EVENT_COUNT_MISMATCH','count':len(rows)}
    return {'verdict':'LOCAL_CHAIN_VALID_UNAUTHENTICATED' if externally_anchored_head is None else 'CHAIN_MATCHES_SUPPLIED_EXTERNAL_ANCHOR',
            'count':len(rows),'head':prev}

def main():
    p=argparse.ArgumentParser();p.add_argument('database');sub=p.add_subparsers(dest='action',required=True)
    a=sub.add_parser('append');a.add_argument('kind');a.add_argument('actor');a.add_argument('subject');a.add_argument('prompt_file');a.add_argument('result_file')
    v=sub.add_parser('verify');v.add_argument('--head');v.add_argument('--count',type=int)
    args=p.parse_args()
    conn=sqlite3.connect(args.database)
    init(conn)
    if args.action=='append':
        ans=append(conn,args.kind,args.actor,args.subject,Path(args.prompt_file).read_bytes(),Path(args.result_file).read_bytes())
    else: ans=verify(conn,args.head,args.count)
    print(json.dumps(ans,indent=2))

if __name__=='__main__': main()
