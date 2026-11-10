#!/usr/bin/env python3
"""Non-authoritative, read-only governance STRUCTURAL preview.

This tool never runs Gemini, never runs Lean, never grants or executes mutation,
never signs receipts, and always returns release_authorized=False.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from collections import defaultdict, deque

HEX64 = re.compile(r'^[0-9a-f]{64}$')
TASK_STATES = {'PLANNED','PAUSED','READY','LEASED','EXECUTING','EXECUTED','SUBMITTED',
               'REVIEW_PENDING','ACCEPTED_TASK','REJECTED','BLOCKED','STALE'}
DONE_EXECUTION = {'EXECUTED','SUBMITTED','REVIEW_PENDING','ACCEPTED_TASK'}
VALID_STEPS = {'PROPOSED','OPEN_OBLIGATIONS','NOT_FORMALLY_VERIFIED','FORMAL_CANDIDATE',
              'LOCAL_LEAN_CHECKED','INDEPENDENT_REPLAYED','SEMANTIC_AUDITED',
              'ACCEPTED_STEP','STALE','REJECTED'}
ALLOWED_AUTH = ["governance/GOVERNANCE.md", "governance/PROJECT_DIRECTION.md", "governance/PROJECT_STATE.yaml"]

class Invalid(ValueError): pass

def unique_pairs(pairs):
    out = {}
    for k,v in pairs:
        if k in out: raise Invalid('duplicate JSON key: '+str(k))
        out[k]=v
    return out

def read_json(filename):
    return json.loads(Path(filename).read_text(encoding='utf-8'),object_pairs_hook=unique_pairs)

def hash_json(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,
                        separators=(',',':')).encode('utf-8')).hexdigest()

def _must(o, kind, name):
    if not isinstance(o,kind): raise Invalid(f'{name} must be {kind.__name__}')
    return o

def _str(o,name):
    if not isinstance(o,str) or not o.strip(): raise Invalid(f'{name} required string')
    return o

def _refs(items, path):
    _must(items,list,path)
    for i,ref in enumerate(items): _str(ref,f'{path}[{i}]')
    return items

def validate_state(state):
    _must(state,dict,'state')
    errors=[]
    if state.get('schema')!='MATH-GOV-PROJECT-STATE-0.6': errors.append('state schema mismatch')
    if state.get('authority_files') != ALLOWED_AUTH: errors.append('exact three authority files required')
    if state.get('release_authorized') is not False: errors.append('state claims release without trusted host')
    if state.get('status') != 'UNBOUND_NO_LIVE_AUTHORITY':
        errors.append('local preview cannot verify any bound or live state; requires external host')
    if state.get('revision')!=0: errors.append('template revision changed; cannot treat as authentic')
    proj=state.get('project')
    if not isinstance(proj,dict): errors.append('missing project binding record')
    elif any(proj.get(k) for k in ('id','owner_grant_ref','original_digest','formal_target_digest')):
        errors.append('project binding claims require authenticated external host')
    host=state.get('external_host')
    if not isinstance(host,dict) or host.get('authenticated') is not False:
        errors.append('external host must remain unverified in prototype')
    gates=state.get('hard_gates')
    if not isinstance(gates,dict) or any(gates.get(f'G{i}')!='UNVERIFIED' for i in range(13)):
        errors.append('gate claims require actual independent host evidence')
    return {'verdict':'NO_GO_UNBOUND' if not errors else 'BLOCKED_TAMPER_OR_LIVE_CLAIM',
            'errors':errors,'release_authorized':False,
            'note':'Read-only status preview. No live governance authority is established.'}

def validate_plan(data):
    _must(data,dict,'plan')
    errors=[]
    if data.get('schema')!='MATH-GOV-PLAN-0.6': errors.append('invalid plan schema')
    if data.get('project_status')!='ILLUSTRATIVE_ONLY':
        errors.append('this runner accepts only illustrative, not real or approved project state')
    for field in ('original_question_digest','formal_target_digest','snapshot_digest'):
        if not isinstance(data.get(field),str) or not HEX64.fullmatch(data[field]):
            errors.append(f'{field} must have 64 lowercase hex characters')
    branches=data.get('branches')
    tasks=data.get('tasks')
    steps=data.get('steps')
    if not isinstance(branches,list) or not isinstance(tasks,list) or not isinstance(steps,list):
        raise Invalid('branches/tasks/steps must be arrays')
    branch_map={};task_map={};step_map={}
    for br in branches:
        if not isinstance(br,dict):raise Invalid('branch must be object')
        bid=_str(br.get('id'),'branch.id')
        if bid in branch_map:errors.append(f'duplicate branch {bid}')
        branch_map[bid]=br
        if br.get('visibility')!='ISOLATED':errors.append(f'branch {bid} cannot assert unreviewed cross-branch visibility')
    for st in steps:
        if not isinstance(st,dict):raise Invalid('step must be object')
        sid=_str(st.get('id'),'step.id')
        if sid in step_map:errors.append(f'duplicate step {sid}')
        step_map[sid]=st
        if st.get('status') not in VALID_STEPS:errors.append(f'step {sid} invalid status')
        if st.get('status') in ('LOCAL_LEAN_CHECKED','INDEPENDENT_REPLAYED','SEMANTIC_AUDITED','ACCEPTED_STEP'):
            errors.append(f'step {sid} strong verification state not authenticated in preview')
        if st.get('open_obligations') is not None and (type(st['open_obligations'])!=int or st['open_obligations']<0):
            errors.append(f'step {sid} invalid open_obligations')
    deps=defaultdict(set)
    all_step_owners=defaultdict(set)
    for task in tasks:
        if not isinstance(task,dict):raise Invalid('task must be object')
        tid=_str(task.get('id'),'task.id')
        if tid in task_map:errors.append(f'duplicate task {tid}')
        task_map[tid]=task
        if task.get('branch') not in branch_map: errors.append(f'task {tid} unknown branch')
        if task.get('state') not in TASK_STATES: errors.append(f'task {tid} invalid state')
        if task.get('state')=='ACCEPTED_TASK': errors.append(f'task {tid} unsupported accepted state in preview')
        for field in ('deps_all','deps_any','proof_steps'):
            if not isinstance(task.get(field),list):raise Invalid(f'{tid}.{field} must be array')
        for p in task['deps_all']:
            _str(p,f'{tid}.deps_all');deps[tid].add(p)
        for group in task['deps_any']:
            if not isinstance(group,list) or len(group)==0: raise Invalid(f'{tid}.deps_any groups must be nonempty arrays')
            for p in group:_str(p,f'{tid}.deps_any');deps[tid].add(p)
        for p in task['proof_steps']:
            _str(p,f'{tid}.proof_steps')
            if p not in step_map:errors.append(f'{tid} missing step {p}')
            all_step_owners[p].add(tid)
    for st in step_map:
        if st not in all_step_owners: errors.append(f'orphan step {st} has no task owner')
    for tid,parents in deps.items():
        for p in parents:
            if p not in task_map: errors.append(f'{tid} missing dependency {p}')
            if p==tid: errors.append(f'{tid} self dependency')
    indeg={k:0 for k in task_map};children=defaultdict(set)
    for child,parents in deps.items():
        for p in parents:
            if p in task_map and p!=child:
                if child not in children[p]:
                    indeg[child]+=1;children[p].add(child)
    queue=deque(k for k in sorted(indeg) if indeg[k]==0)
    visited=0
    while queue:
        k=queue.popleft();visited+=1
        for child in sorted(children[k]):
            indeg[child]-=1
            if indeg[child]==0:queue.append(child)
    if visited!=len(indeg):errors.append('cycle in task dependencies')
    if data.get('host_attestations') or data.get('verified_task_receipts') or data.get('lean_receipts'):
        errors.append('preview cannot authenticate receipts; must be empty')
    return errors,task_map,step_map,branch_map

def plan(data):
    errors,tasks,steps,branches=validate_plan(data)
    if errors:return {'verdict':'BLOCKED','errors':sorted(set(errors)),'release_authorized':False}
    status=[]
    for tid,task in sorted(tasks.items()):
        missing=sorted(set(task['deps_all']))
        unsatisfied_any=[[str(x) for x in group] for group in task['deps_any']]
        # No independently verified task receipts can be established by this preview.
        if task['state'] not in ('PLANNED','PAUSED'):
            outcome='ALREADY_EXECUTED_OR_NOT_SCHEDULABLE'
        elif missing or unsatisfied_any:
            outcome='DEPENDENCIES_NOT_AUTHENTICATED'
        else:outcome='STRUCTURALLY_READY_REQUIRES_HOST_GRANT_AND_CAPSULE'
        status.append({'task_id':tid,'branch_id':task['branch'],'task_state':task['state'],
                       'dispatch_preview':outcome,'unverified_and_prereqs':missing,
                       'unverified_or_groups':unsatisfied_any})
    return {'verdict':'STRUCTURAL_PLAN_PREVIEW_ONLY','tasks':status,
            'verified_task_ids':[],'release_authorized':False,
            'limitations':'No user-approved project binding, live model, trusted provenance or authenticated dependencies'}

def capsule(data,task_id):
    errors,tasks,steps,branches=validate_plan(data)
    if errors:return {'verdict':'BLOCKED','errors':sorted(set(errors)),'release_authorized':False}
    if task_id not in tasks:return {'verdict':'BLOCKED','errors':['unknown task_id'],'release_authorized':False}
    t=tasks[task_id]
    return {'verdict':'INCOMPLETE_CONTEXT_CAPSULE_NOT_DISPATCHABLE',
            'task_id':task_id,'branch_id':t['branch'],
            'original_subject_ref':data.get('original_question_ref'),
            'original_subject_digest':data.get('original_question_digest'),
            'formal_target_ref':data.get('formal_target_ref'),
            'formal_target_digest':data.get('formal_target_digest'),
            'snapshot_digest':data.get('snapshot_digest'),
            'deps_all':t['deps_all'],'deps_any':t['deps_any'],
            'step_records':[steps[s] for s in t['proof_steps']],
            'missing':['authenticated exact original text','approved target full text',
                       'relevant definitions and source bytes','verified premise receipts',
                       'failed/negative attempt archive','verified task-appropriate model capability',
                       'host-enforced actor and tool grant','signed step context read receipt',
                       'trusted lease and budget','context recall test'],
            'no_unauthorized_cross_branch_data':True,
            'release_authorized':False}

def report(data):
    errors,tasks,steps,branches=validate_plan(data)
    if errors:return {'verdict':'BLOCKED','errors':sorted(set(errors)),'release_authorized':False}
    executed=sum(t['state'] in DONE_EXECUTION for t in tasks.values())
    submitted=sum(t['state']=='SUBMITTED' for t in tasks.values())
    open_count=sum(int(s['open_obligations'] or 0) for s in steps.values())
    # Never invent proof acceptance. Empty evidence does not imply all remaining work is zero.
    claims=data.get('claims')
    positives=data.get('positive_findings');negatives=data.get('negative_findings')
    if not all(isinstance(x,list) for x in [claims,positives,negatives]):
        return {'verdict':'BLOCKED','errors':['claims/findings must be arrays'],'release_authorized':False}
    if claims:
        return {'verdict':'BLOCKED','errors':['cannot verify user-supplied strong claim register in prototype; review required'],'release_authorized':False}
    return {'verdict':'NON_AUTHORITATIVE_PROGRESS_REPORT',
            'tasks_total':len(tasks),'tasks_executed_or_submitted':executed,
            'tasks_submitted_pending_review':submitted,'tasks_independently_accepted':0,
            'steps_with_recorded_open_obligations':sum((s['open_obligations'] or 0)>0 for s in steps.values()),
            'open_obligations_in_demo':open_count,
            'formal_proofs_verified':0,'theorem_progress':'UNKNOWN',
            'original_question_authenticated':False,'independent_reviews_authenticated':0,
            'report_completeness':'NOT_ATTESTED',
            'note':'Illustrative fixture counts, not actual project progress; missing knowledge is UNKNOWN.',
            'release_authorized':False}

def safe_main():
    parser=argparse.ArgumentParser()
    sub=parser.add_subparsers(dest='mode',required=True)
    for mode in ('audit','plan','capsule','report'):
        p=sub.add_parser(mode);p.add_argument('data')
        if mode=='capsule':p.add_argument('task_id')
    args=parser.parse_args()
    try:
        data=read_json(args.data)
        result={'audit':lambda:validate_state(data),
                'plan':lambda:plan(data),'capsule':lambda:capsule(data,args.task_id),
                'report':lambda:report(data)}[args.mode]()
    except (Invalid,OSError,ValueError,TypeError,KeyError,UnicodeError,RecursionError) as e:
        result={'verdict':'BLOCKED_MALFORMED_OR_INACCESSIBLE','errors':[f'{type(e).__name__}: {e}'],
                'release_authorized':False}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result['verdict'] in ('STRUCTURAL_PLAN_PREVIEW_ONLY','INCOMPLETE_CONTEXT_CAPSULE_NOT_DISPATCHABLE','NON_AUTHORITATIVE_PROGRESS_REPORT','NO_GO_UNBOUND') else 2

if __name__=='__main__':sys.exit(safe_main())
