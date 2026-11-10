"""Integrates local frozen-step audit and real Lean execution (when installed).
Never grants production proof acceptance or external semantic review.
"""
import argparse
import json
from pathlib import Path
try:
    from src.ymmg.math_step_engine import audit, digest, index_graph
    from src.ymmg.lean_step_runner import check_step
except ImportError:
    try:
        from .math_step_engine import audit, digest, index_graph
        from .lean_step_runner import check_step
    except (ImportError, ValueError):
        from math_step_engine import audit, digest, index_graph
        from lean_step_runner import check_step


def blocked(reason, detail=None):
    r={'verdict':'BLOCKED','reason':reason,'proof_verified':False,'release_authorized':False}
    if detail is not None:r['detail']=detail
    return r


def check_formal_step(case, step_id, project_root, relative_source,
                      trusted_original_digest, trusted_target_digest,
                      trusted_step_goal_digest, trusted_source_digest, trusted_contract_digest, timeout=120):
    pre=audit(case,trusted_original_digest,trusted_target_digest,trusted_contract_digest)
    if pre['verdict']!='STRUCTURAL_PREFLIGHT_PASS_ONLY':
        return blocked('STRUCTURAL_OR_SOURCE_ANCHOR_FAILURE',pre['errors'])
    idx,_,_=index_graph(case)
    step=idx.get(step_id)
    if step is None or step['kind']!='STEP': return blocked('UNKNOWN_STEP')
    if step['state'] in ('INVALIDATED','REFUTED','SUPERSEDED'):
        return blocked('STEP_NOT_ACTIVE')
    if step.get('goal_digest')!=trusted_step_goal_digest:
        return blocked('STEP_GOAL_ANCHOR_MISMATCH')
    lean=step.get('lean')
    if not isinstance(lean,dict): return blocked('STEP_NOT_FORMALIZED')
    if lean.get('source_digest')!=trusted_source_digest:
        return blocked('STEP_LEAN_SOURCE_ANCHOR_MISMATCH')
    if lean.get('statement_digest')!=step['goal_digest'] or lean.get('formal_statement')!=step['goal']:
        return blocked('FORMALIZATION_REQUIRES_SEPARATE_SEMANTIC_MAPPING_AUDIT')
    result=check_step(project_root,relative_source,lean['theorem'],lean['formal_statement'],trusted_source_digest,timeout)
    if not result.get('lean_kernel_check_passed'):
        return blocked('LEAN_CHECK_FAILED_OR_NOT_AVAILABLE',result)
    return {'verdict':'LOCAL_LEAN_STEP_PASS_SEMANTIC_AND_INDEPENDENT_REVIEW_PENDING',
            'step_id':step_id,'subject_digest':trusted_original_digest,
            'target_digest':trusted_target_digest,'step_goal_digest':trusted_step_goal_digest,
            'tool_receipt':result,'proof_verified':False,'release_authorized':False,
            'open_acceptance_gates':['independent replay in isolated environment',
                                     'meaning audit of original question vs formal theorem',
                                     'full proof-obligation inventory reconciliation',
                                     'trusted source and actor authorization',
                                     'owner/acceptor confirmation']}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('case');p.add_argument('step');p.add_argument('lean_project');p.add_argument('lean_source')
    p.add_argument('--original-digest',required=True);p.add_argument('--formal-digest',required=True)
    p.add_argument('--step-goal-digest',required=True);p.add_argument('--source-digest',required=True);p.add_argument('--contract-digest',required=True)
    a=p.parse_args()
    try:
        case=json.loads(Path(a.case).read_text(encoding='utf-8'))
        result=check_formal_step(case,a.step,a.lean_project,a.lean_source,a.original_digest,a.formal_digest,a.step_goal_digest,a.source_digest,a.contract_digest)
    except (OSError,ValueError,TypeError) as e:
        result=blocked('INPUT_ERROR',str(e))
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__': main()
