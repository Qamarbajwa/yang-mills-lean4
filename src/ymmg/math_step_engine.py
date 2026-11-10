"""MATH-GOV v0.5: fail-closed structural mathematics step/obligation engine.

No cryptographic authority, mathematical checker, Lean daemon, or AI agent is created here.
All declared verification/acceptance status in user-supplied JSON is untrusted.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from collections import defaultdict, deque
from pathlib import Path

SCHEMA = 'MATH-GOV-STEP-ENGINE-0.5'
STEP_STATES = {'PROPOSED','NEEDS_JUSTIFICATION','EXECUTED','FORMAL_CANDIDATE','INVALIDATED','REFUTED','SUPERSEDED'}
TASK_STATES = {'PLANNED','IN_PROGRESS','EXECUTED','PAUSED','FAILED','INVALIDATED'}
EDGE_TYPES = {'AND','OR','OPTIONAL','REFUTES','ANALOGY'}
OBJECT_TYPES = {'STEP','TASK','CLAIM','DIAGRAM','PUBLICATION','SOURCE','FORMAL_TARGET','RESEARCH_PATH'}
STRONG_CLAIMS = {'FORMALLY_VERIFIED','THEOREM_PROVED','INDEPENDENTLY_ACCEPTED'}


def digest(data: str | bytes) -> str:
    if isinstance(data, str): data = data.encode('utf-8')
    return hashlib.sha256(data).hexdigest()


def canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(',', ':'))


def _required_string(value, label, errors):
    if not isinstance(value, str) or not value.strip():
        errors.append(f'{label}: must be a non-empty string')
        return False
    return True


def index_graph(case):
    """Build typed graph with complete, explicit inventories, never inferred omissions."""
    errors=[]
    if not isinstance(case, dict): return {}, [], ['ROOT: expected object']
    if case.get('schema') != SCHEMA: errors.append('ROOT: unsupported schema')
    orig=case.get('original')
    if not isinstance(orig, dict): errors.append('ORIGINAL: missing original question record')
    else:
        if _required_string(orig.get('text'), 'ORIGINAL.text', errors):
            if orig.get('digest') != digest(orig['text']): errors.append('ORIGINAL: digest mismatch')
    tgt=case.get('formal_target')
    if not isinstance(tgt,dict): errors.append('TARGET: missing formalization')
    else:
        if _required_string(tgt.get('statement'), 'TARGET.statement', errors):
            if tgt.get('digest') != digest(tgt['statement']): errors.append('TARGET: digest mismatch')
        if tgt.get('approved') is not True:
            errors.append('TARGET: formalization not recorded as approved (host authorization is still required)')
    nodes=case.get('nodes')
    if not isinstance(nodes,list): return {}, [], errors+['GRAPH: nodes not an array']
    idx={}
    for i,node in enumerate(nodes):
        if not isinstance(node,dict): errors.append(f'NODE[{i}]: expected object'); continue
        node_id=node.get('id')
        if not _required_string(node_id,f'NODE[{i}].id', errors): continue
        if node_id in idx: errors.append(f'GRAPH: duplicate node {node_id}'); continue
        if node.get('kind') not in OBJECT_TYPES: errors.append(f'{node_id}: invalid kind')
        idx[node_id]=node
    required_edges=case.get('required_edges')
    if not isinstance(required_edges,list): errors.append('GRAPH: missing independent required edge inventory')
    edges=case.get('edges')
    if not isinstance(edges,list): return idx, [], errors+['GRAPH: edges not an array']
    normalized=[]
    for i,edge in enumerate(edges):
        if not isinstance(edge,dict): errors.append(f'EDGE[{i}]: expected object'); continue
        a,b,t=edge.get('source'),edge.get('target'),edge.get('kind')
        if a not in idx or b not in idx: errors.append(f'EDGE[{i}]: unknown source or target'); continue
        if a==b: errors.append(f'EDGE[{i}]: self-edge'); continue
        if t not in EDGE_TYPES: errors.append(f'EDGE[{i}]: unknown type'); continue
        if t=='OR' and not _required_string(edge.get('group'), f'EDGE[{i}].group', errors): continue
        normalized.append((a,b,t,edge.get('group')))
    if isinstance(required_edges,list):
        if not all(isinstance(e,dict) for e in required_edges): errors.append('GRAPH: malformed required edge')
        else:
            required_set={(e.get('source'),e.get('target'),e.get('kind'),e.get('group')) for e in required_edges}
            for e in sorted(required_set-set(normalized),key=str): errors.append(f'GRAPH: required edge missing {e}')
            for e in sorted(set(normalized)-required_set,key=str): errors.append(f'GRAPH: unauthorized new edge {e}')
    # All dependencies, including speculative links, are acyclic to prevent circular explanations.
    successors=defaultdict(list); indeg={k:0 for k in idx}
    for a,b,t,g in normalized:
        successors[a].append(b); indeg[b]+=1
    queue=deque(k for k in idx if not indeg[k]); scanned=0
    while queue:
        x=queue.popleft(); scanned+=1
        for nxt in successors[x]:
            indeg[nxt]-=1
            if indeg[nxt]==0: queue.append(nxt)
    if scanned != len(idx): errors.append('GRAPH: dependency or conceptual-link cycle')
    required=case.get('required_inventory')
    if not isinstance(required,list) or not required or not all(isinstance(x,str) for x in required):
        errors.append('INVENTORY: missing authoritative required-ID array')
    else:
        if len(required)!=len(set(required)): errors.append('INVENTORY: duplicate required IDs')
        for missing in sorted(set(required)-set(idx)): errors.append(f'INVENTORY: missing {missing}')
        for extra in sorted(set(idx)-set(required)): errors.append(f'INVENTORY: unregistered node {extra}')
    for src,dst,typ,grp in normalized:
        if typ in ('AND','OR') and idx[src].get('kind')=='TASK' and idx[dst].get('kind')=='TASK':
            sb,db=idx[src].get('branch'),idx[dst].get('branch')
            if sb not in ('ROOT',db) and db != 'INTEGRATION':
                errors.append(f'{dst}: unauthorized cross-branch dependency from {src}')
    for ident,node in idx.items():
        typ=node.get('kind')
        if typ=='STEP':
            if node.get('state') not in STEP_STATES:
                errors.append(f'{ident}: invalid or self-asserted formal verification state')
            for prop in ('goal','justification','task_id'):
                _required_string(node.get(prop),f'{ident}.{prop}', errors)
            if isinstance(node.get('goal'),str) and node.get('goal_digest')!=digest(node['goal']):
                errors.append(f'{ident}: goal digest mismatch')
            if not isinstance(node.get('obligations'),list) or not all(isinstance(x,str) and x for x in node['obligations']):
                errors.append(f'{ident}: invalid proof obligations')
            if not isinstance(node.get('discharged'),list) or not all(isinstance(x,str) for x in node['discharged']):
                errors.append(f'{ident}: invalid discharged obligations')
            if node.get('task_id') not in idx or idx.get(node.get('task_id'),{}).get('kind')!='TASK':
                errors.append(f'{ident}: missing owning TASK')
            if node.get('state')=='FORMAL_CANDIDATE' and not isinstance(node.get('lean'),dict):
                errors.append(f'{ident}: missing Lean candidate')
            if isinstance(node.get('lean'),dict):
                lc=node['lean']
                for field in ('theorem','formal_statement','source_digest'):
                    _required_string(lc.get(field), f'{ident}.lean.{field}',errors)
                if isinstance(lc.get('formal_statement'),str) and lc.get('statement_digest') != digest(lc['formal_statement']):
                    errors.append(f'{ident}: Lean formal statement digest mismatch')
            for p in (node.get('premises') if isinstance(node.get('premises'),list) else []):
                if p not in idx: errors.append(f'{ident}: missing premise {p}')
                elif (p,ident,'AND',None) not in normalized:
                    errors.append(f'{ident}: premise {p} absent from dependency graph')
            if not isinstance(node.get('premises'), list): errors.append(f'{ident}: premises not array')
        elif typ=='TASK':
            if node.get('state') not in TASK_STATES:
                errors.append(f'{ident}: untrusted task acceptance state not permitted')
            for sid in node.get('step_ids',[]):
                if sid not in idx or idx[sid].get('kind')!='STEP':
                    errors.append(f'{ident}: missing associated STEP {sid}')
                elif idx[sid].get('task_id')!=ident:
                    errors.append(f'{ident}: step {sid} ownership mismatch')
            if not isinstance(node.get('step_ids'),list): errors.append(f'{ident}: step_ids not array')
            if node.get('purpose') not in ('PROOF','RESEARCH'):
                errors.append(f'{ident}: task purpose must be PROOF or RESEARCH')
            if node.get('purpose')=='PROOF' and not node.get('step_ids'):
                errors.append(f'{ident}: proof task has no mathematical steps')
            if not isinstance(node.get('branch'),str) or not node['branch']: errors.append(f'{ident}: missing branch')
        elif typ=='CLAIM':
            if node.get('reported_strength') in STRONG_CLAIMS:
                errors.append(f'{ident}: strong proof/acceptance claim cannot be self-declared')
            if not isinstance(node.get('evidence_refs'),list) or not node['evidence_refs']:
                errors.append(f'{ident}: no evidence references')
            else:
                for r in node['evidence_refs']:
                    if r not in idx: errors.append(f'{ident}: unknown evidence {r}')
                    elif (r,ident,'AND',None) not in normalized:
                        errors.append(f'{ident}: evidence {r} not linked in graph')
        elif typ=='SOURCE':
            if _required_string(node.get('content'),f'{ident}.content',errors):
                if node.get('content_digest')!=digest(node['content']): errors.append(f'{ident}: content digest mismatch')
    # Steps cannot be completed on open obligations; an executed step is not formally verified.
    for ident,node in idx.items():
        if node.get('kind')=='STEP':
            obs=node.get('obligations',[]); discharged=node.get('discharged',[])
            if isinstance(obs,list) and isinstance(discharged,list):
                if len(set(obs))!=len(obs) or len(set(discharged))!=len(discharged):
                    errors.append(f'{ident}: duplicate proof obligations')
                if not set(discharged).issubset(set(obs)):
                    errors.append(f'{ident}: discharged goal not in declared obligations')
                if node.get('state')=='FORMAL_CANDIDATE' and set(obs)!=set(discharged):
                    errors.append(f'{ident}: formal candidate has open obligations')
    return idx,normalized,sorted(set(errors))


def audit(case, trusted_original_digest=None, trusted_formal_digest=None, trusted_contract_digest=None):
    try:
        idx,edges,errors=index_graph(case)
        if not isinstance(trusted_original_digest,str) or not re.fullmatch(r'[0-9a-f]{64}',trusted_original_digest):
            errors.append('TRUST: missing independently anchored original-question digest')
        elif isinstance(case.get('original'),dict) and case['original'].get('digest') != trusted_original_digest:
            errors.append('TRUST: original question differs from owner-anchored digest')
        if not isinstance(trusted_formal_digest,str) or not re.fullmatch(r'[0-9a-f]{64}',trusted_formal_digest):
            errors.append('TRUST: missing independently anchored formal target digest')
        elif isinstance(case.get('formal_target'),dict) and case['formal_target'].get('digest') != trusted_formal_digest:
            errors.append('TRUST: formal target differs from approved digest')
        contract={'required_inventory':case.get('required_inventory'), 'required_edges':case.get('required_edges')} if isinstance(case,dict) else None
        if not isinstance(trusted_contract_digest,str) or not re.fullmatch(r'[0-9a-f]{64}',trusted_contract_digest):
            errors.append('TRUST: missing independent inventory/edge contract digest')
        elif digest(canonical(contract)) != trusted_contract_digest:
            errors.append('TRUST: independently anchored graph contract differs')
        states=defaultdict(int)
        for node in idx.values(): states[f"{node.get('kind','?')}:{node.get('state','UNREVIEWED')}"]+=1
        return {'verdict':'BLOCKED' if errors else 'STRUCTURAL_PREFLIGHT_PASS_ONLY',
                'errors':sorted(set(errors)), 'counts':dict(sorted(states.items())),
                'formal_proof_verified':False,'release_authorized':False,
                'verification_limit':'No real Lean run or authenticated reviewer/acceptor identity in structural audit'}
    except (TypeError,ValueError,AttributeError,KeyError) as e:
        return {'verdict':'BLOCKED','errors':[f'MALFORMED_INPUT: {type(e).__name__}: {e}'],
                'formal_proof_verified':False,'release_authorized':False}


def _impact_impl(before, after, trusted_before_digest=None):
    """Source-derived change tracking; never accepts worker-supplied changed_ids."""
    if trusted_before_digest is None:
        return {'verdict':'BLOCKED','errors':['missing externally anchored baseline snapshot digest']}
    if digest(canonical(before))!=trusted_before_digest:
        return {'verdict':'BLOCKED','errors':['baseline snapshot digest mismatch']}
    b,be,berr=index_graph(before); a,ae,aerr=index_graph(after)
    if berr or aerr: return {'verdict':'BLOCKED','errors':sorted(set(berr+aerr))}
    changed=set()
    root_modified=any(canonical(before.get(k))!=canonical(after.get(k)) for k in ('original','formal_target','schema'))
    if root_modified: changed.update(b.keys()|a.keys())
    for key in b.keys()|a.keys():
        if canonical(b.get(key))!=canonical(a.get(key)): changed.add(key)
    edge_before=set(be); edge_after=set(ae)
    for src,dst,kind,group in (edge_before ^ edge_after):
        changed.add(src); changed.add(dst)
    rev=defaultdict(set)
    for src,dst,kind,group in edge_before | edge_after: rev[src].add(dst)
    all_impacted=set(changed); queue=deque(sorted(changed))
    while queue:
        x=queue.popleft()
        for nxt in sorted(rev[x]):
            if nxt not in all_impacted:
                all_impacted.add(nxt); queue.append(nxt)
    # Invalidated items are conservative including optional/analogy links; cannot silently reuse any derived claim.
    return {'verdict':'IMPACT_REPORT_NOT_APPLIED','changed':sorted(changed),
            'must_revalidate':sorted(all_impacted),'release_authorized':False,
            'new_state_revision_required':bool(changed),
            'note':'Must be atomically applied by a trusted host; not an authorization or mutation.'}


def impact(before, after, trusted_before_digest=None):
    try:
        return _impact_impl(before,after,trusted_before_digest)
    except (KeyError,ValueError,TypeError,AttributeError) as exc:
        return {'verdict':'BLOCKED','errors':[f'MALFORMED_DIFF_INPUT: {type(exc).__name__}: {exc}'],'release_authorized':False}


def task_readiness(case, task_id, trusted_completed_task_ids=()):
    """Trusted task acceptance IDs MUST originate from host, never case JSON.
    Even when ready, worker dispatch requires authenticated source retrieval and policy gate.
    """
    idx,edges,errors=index_graph(case)
    if errors: return {'dispatch':'BLOCKED','errors':errors}
    task=idx.get(task_id)
    if not task or task['kind']!='TASK': return {'dispatch':'BLOCKED','errors':['unknown task']}
    accepted=set(trusted_completed_task_ids)
    if not accepted.issubset(idx.keys()): return {'dispatch':'BLOCKED','errors':['unknown accepted task']}
    deps_all={a for a,b,t,g in edges if b==task_id and t=='AND' and idx[a]['kind']=='TASK'}
    groups=defaultdict(set)
    for a,b,t,g in edges:
        if b==task_id and t=='OR' and idx[a]['kind']=='TASK': groups[g].add(a)
    missing=sorted(deps_all-accepted)
    failed_groups=[group for group,choices in groups.items() if not choices.intersection(accepted)]
    if missing or failed_groups: return {'dispatch':'BLOCKED_DEPENDENCIES','missing':missing,'unsatisfied_or_groups':sorted(failed_groups)}
    if task['state'] not in ('PLANNED','PAUSED'):
        return {'dispatch':'BLOCKED','errors':['task state not schedulable']}
    return {'dispatch':'STRUCTURALLY_READY_HOST_GRANT_REQUIRED','task_id':task_id,
            'original_digest':case['original']['digest'],
            'formal_target_digest':case['formal_target']['digest'],
            'branch':task['branch'],'step_goals':[
                {'step_id':sid,'goal':idx[sid]['goal'],'goal_digest':idx[sid]['goal_digest'],
                 'premises':idx[sid].get('premises',[]),'obligations':idx[sid]['obligations']}
                for sid in task.get('step_ids',[])],
            'required': ['Trusted-host source fetch and exact digest validation','Branch access enforcement',
                'A source-complete prompt/result archive','Capability assessment and context recall test']}


def progress(case):
    """Never promote task/execution completion to theorem percent complete."""
    idx,_,errors=index_graph(case)
    if errors: return {'verdict':'BLOCKED','errors':errors}
    tasks=[n for n in idx.values() if n['kind']=='TASK']
    steps=[n for n in idx.values() if n['kind']=='STEP']
    return {'verdict':'DESCRIPTIVE_UNVERIFIED','tasks_total':len(tasks),
            'tasks_execution_finished':sum(t['state']=='EXECUTED' for t in tasks),
            'steps_with_open_obligations':sum(set(s['obligations'])!=set(s['discharged']) for s in steps),
            'theorem_progress_percent':'UNKNOWN', 'proof_verified':False,
            'note':'Task and obligation counts are descriptive; no verified theorem progress percentage inferred.'}


def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='command',required=True)
    v=sub.add_parser('audit'); v.add_argument('case'); v.add_argument('--original-digest'); v.add_argument('--formal-digest');v.add_argument('--contract-digest')
    c=sub.add_parser('capsule'); c.add_argument('case'); c.add_argument('task')
    d=sub.add_parser('diff'); d.add_argument('before'); d.add_argument('after'); d.add_argument('--baseline-digest')
    pr=sub.add_parser('progress'); pr.add_argument('case')
    args=p.parse_args()
    try:
        data=json.loads(Path(args.case if args.command!='diff' else args.before).read_text(encoding='utf-8'))
        if args.command=='audit': output=audit(data,args.original_digest,args.formal_digest,args.contract_digest)
        elif args.command=='capsule': output=task_readiness(data,args.task)
        elif args.command=='diff': output=impact(data,json.loads(Path(args.after).read_text(encoding='utf-8')),args.baseline_digest)
        else: output=progress(data)
    except (OSError,ValueError,TypeError) as e: output={'verdict':'BLOCKED','errors':[f'INPUT_ERROR: {e}']}
    print(json.dumps(output,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__': main()
