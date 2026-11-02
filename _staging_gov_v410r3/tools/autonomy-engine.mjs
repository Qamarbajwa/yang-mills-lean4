/**
 * Universal, dependency-free autonomous development policy and dispatch interface.
 * No subprocess, provider, disk-write, network, secret or deployment capabilities.
 * The project-specific host MUST implement and authenticate all runtime adapters.
 */
import fs from 'fs';
import {fileURLToPath} from 'url';
import path from 'path';
import {parseStrictJson, validateReleaseState, validatePreCodeAuthorization, validateRoleCombination} from './verify-package.mjs';

export const PHASE_ORDER = Object.freeze([
  'DISCOVER','SPECIFY','STANDARDS','DIAGRAM','IMPLEMENT','TEST',
  'REVIEW','ACCEPT','RECORD','EVOLVE'
]);
const STOP = new Set(['IDLE','BLOCKED','RECONCILE']);
const RESERVED = new Set(['DEPLOY','MERGE_PROTECTED','PUBLISH_GOVERNANCE','SPEND','CHANGE_BUSINESS_POLICY','ACCESS_SECRETS','DELETE_USER_DATA']);
const ACTOR_ROLE = Object.freeze({
  DISCOVER:'worker_id', SPECIFY:'worker_id', STANDARDS:'worker_id',
  DIAGRAM:'worker_id', IMPLEMENT:'worker_id', TEST:'worker_id',
  REVIEW:'reviewer_id', ACCEPT:'acceptor_id', RECORD:'acceptor_id',
  EVOLVE:'worker_id'
});
const NEXT = Object.freeze(Object.fromEntries(PHASE_ORDER.map((p,i)=>[p,PHASE_ORDER[i+1]??'IDLE'])));
const string = x=>typeof x==='string'&&x.trim().length>0;
const unique = a=>new Set(a).size===a.length;
const denial = (reason,extra={})=>({ok:false, action:'HALT', reason, ...extra});

function matchScope(blocker, scope) {
  if (!blocker || typeof blocker!=='object' || Array.isArray(blocker)) return true;
  if (blocker.status==='RESOLVED') return false;
  const ref=blocker.subject_scope??blocker.scope_ref;
  // A structured project adapter must implement hierarchical/overlap matching.
  return !string(ref)||ref===scope;
}
export function eligibleObjectives(state) {
  const items=Array.isArray(state?.objectives)?state.objectives:[];
  const done=new Set(items.filter(x=>x&&x.status==='ACCEPTED_BOUNDED').map(x=>x.id));
  return items.filter(o=>o&&string(o.id)&&string(o.subject_scope)&&
    ['QUEUED','READY'].includes(o.status)&&Array.isArray(o.dependencies)&&
    o.dependencies.every(d=>done.has(d))&&
    !RESERVED.has(o.action)&&o.action!=='RELEASE_CONTROL'&&
    !(state.blockers??[]).some(b=>matchScope(b,o.subject_scope)))
    .sort((a,b)=>(Number.isFinite(b.priority)?b.priority:0)-(Number.isFinite(a.priority)?a.priority:0)||a.id.localeCompare(b.id));
}

/** A pure decision. This never grants permission or writes a file. */
export function planAutonomousCycle(state, {now = new Date().toISOString()} = {}) {
  if (!state?.autonomy || state.autonomy.enabled!==true || state.autonomy.mode!=='BOUNDED') return denial('AUTONOMY_INACTIVE');
  if (state.activation!=='ACTIVE') return denial('PROJECT_NOT_ACTIVE');
  const shape=validateReleaseState(state,{now});
  // A state may be structurally valid but still lack trusted project evidence.
  if (shape.length) return denial('STATE_INVALID',{failures:shape});
  if (state.autonomy.retry_count>=state.autonomy.max_retries && state.autonomy.retry_count>0) return denial('RETRY_BUDGET_EXHAUSTED');
  const roles=state.coordination?.active_role_assignment??{};
  const roleIssues=validateRoleCombination({risk:'R3',changeClass:'GOVERNANCE',mode:'THREE_ROLE',
    workerId:roles.worker_id,reviewerId:roles.reviewer_id,acceptorId:roles.acceptor_id,
    routerId:roles.router_id,watchdogId:roles.watchdog_id,reviewerIndependence:roles.reviewer_independence});
  if (roleIssues.length) return denial('ROLES_UNVERIFIED',{failures:roleIssues});
  if (STOP.has(state.autonomy.phase)&&state.autonomy.phase!=='IDLE') return denial('MANUAL_RECONCILIATION_REQUIRED',{phase:state.autonomy.phase});
  if (state.autonomy.phase==='IDLE') {
    const next=eligibleObjectives(state)[0];
    if (!next) return {ok:true,action:'IDLE',reason:'NO_ELIGIBLE_OBJECTIVES'};
    return {ok:true,action:'SELECT_OBJECTIVE',objective_ref:next.id,subject_scope:next.subject_scope,
      phase:'DISCOVER',reason:'DEPENDENCIES_SATISFIED',requires_trusted_scheduler:true};
  }
  const a=state.autonomy, scope=a.subject_scope, phase=a.phase;
  if (!PHASE_ORDER.includes(phase)||!string(scope)||!string(a.objective_ref)) return denial('INVALID_AUTONOMY_PHASE');
  if (!state.candidate_identity?.subject_scope?.includes(scope)) return denial('SCOPE_NOT_FROZEN');
  if ((state.blockers??[]).some(b=>matchScope(b,scope))) return denial('APPLICABLE_BLOCKER');
  const obj=(state.objectives??[]).find(o=>o?.id===a.objective_ref&&o.subject_scope===scope);
  if (!obj || !['QUEUED','READY','IN_PROGRESS','ACCEPTED_BOUNDED'].includes(obj.status)) return denial('OBJECTIVE_NOT_CURRENT');
  const accepted=new Set((state.objectives??[]).filter(x=>x?.status==='ACCEPTED_BOUNDED').map(x=>x.id));
  if (!Array.isArray(obj.dependencies)||obj.dependencies.some(d=>!accepted.has(d))) return denial('OBJECTIVE_DEPENDENCY_DRIFT');
  if (RESERVED.has(obj.action)||obj.action==='RELEASE_CONTROL'||(obj.reserved_actions??[]).some(x=>RESERVED.has(x))) return denial('RESERVED_OWNER_DECISION');
  if (state.specification_gate?.status==='BLOCKED_MISSING_SPEC') {
    const prompts=state.specification_gate?.missing_specification_prompts??[];
    if(state.specification_gate.missing_kind==='TECHNICAL' && a.retry_count<a.max_retries) {
      return {ok:true,action:'EXECUTE_PHASE',phase:'STANDARDS',technical_repair:true,
        objective_ref:a.objective_ref,subject_scope:scope,actor_role:'worker_id',
        actor_id:roles.worker_id,expected_revision:state.revision,
        subject_digest:state.candidate_identity.subject_digest,
        budget_ref:a.budget_ref,requires_trusted_scheduler:true,
        missing_specification_prompts:prompts};
    }
    return denial(state.specification_gate.missing_kind==='TECHNICAL'?'TECHNICAL_RESEARCH_BUDGET_EXHAUSTED':'OWNER_CLARIFICATION_REQUIRED',
      {missing_specification_prompts:prompts});
  }
  if (['IMPLEMENT','TEST','REVIEW','ACCEPT','RECORD','EVOLVE'].includes(phase) &&
      (state.specification_gate?.status!=='SPEC_VERIFIED'||state.specification_gate?.diagram_first_status!=='DIAGRAM_LOCKED'||
       state.specification_gate?.subject_scope_ref!==scope||state.specification_gate?.diagram_lock_subject_digest!==state.candidate_identity?.subject_digest))
    return denial('SPEC_OR_DIAGRAM_NOT_LOCKED');
  if (phase==='ACCEPT' && (!string(a.review_receipt_ref)||a.review_subject_digest!==state.candidate_identity?.subject_digest))
    return denial('REVIEW_NOT_BOUND_TO_CANDIDATE');
  return {ok:true,action:'EXECUTE_PHASE',phase,objective_ref:a.objective_ref,subject_scope:scope,
    actor_role:ACTOR_ROLE[phase],actor_id:roles[ACTOR_ROLE[phase]],
    expected_revision:state.revision,subject_digest:state.candidate_identity.subject_digest,
    budget_ref:a.budget_ref,requires_trusted_scheduler:true};
}

const requiredMethods=['authenticateActors','attestControlPlanes','acquireScopeLease','authorizeMandate','executeStep','verifyReceipt','commitStateCAS','releaseScopeLease'];
/** Runs ONE bounded step, not a background loop, and never mutates local source itself. */
export async function executeAutonomousCycle(state, host) {
  const plan=planAutonomousCycle(state, {now:host?.trustedNow??new Date().toISOString()});
  if(!plan.ok||plan.action==='IDLE') return {...plan,executed:false};
  if(!host||requiredMethods.some(k=>typeof host[k]!=='function')||!string(host.trustedNow))
    return denial('TRUSTED_PROJECT_HOST_REQUIRED',{executed:false});
  if(plan.action==='SELECT_OBJECTIVE') {
    // Only a trusted serialized state writer can start a new scoped objective.
    try {
      const control=await host.attestControlPlanes(state,plan);
      const roles=state.coordination.active_role_assignment;
      if(control?.authenticated!==true||control?.router_id!==roles.router_id||control?.watchdog_id!==roles.watchdog_id||
        control?.router_no_mutation!==true||control?.watchdog_no_acceptance!==true||control?.isolation_verified!==true)
        return denial('CONTROL_PLANE_ISOLATION_NOT_ATTESTED');
      const identity=await host.authenticateActors(state,plan);
      if(identity?.authenticated!==true||identity?.state_revision!==state.revision) return denial('UNAUTHENTICATED_ACTORS');
      const before=state.revision;
      // A new scope cannot inherit an unrelated locked specification/diagram receipt.
      // Existing verified evidence remains append-only; only the active scope gate is reset.
      const oldGate=state.specification_gate;
      const newScope=oldGate.subject_scope_ref!==plan.subject_scope;
      const proposedGate=newScope?{
        ...oldGate,status:'UNVERIFIED',diagram_first_status:'DIAGRAM_PENDING',
        subject_scope_ref:plan.subject_scope,diagram_lock_subject_digest:null,
        dimension_refs:Object.fromEntries(Object.keys(oldGate.dimension_refs).map(k=>[k,null])),
        relative_search_refs:[],diagram_refs:[],diagram_approval_ref:null,
        missing_specification_prompts:[],missing_kind:null
      }:oldGate;
      const proposed={...state,revision:before+1,
        current_objective:plan.objective_ref,
        specification_gate:proposedGate,
        objectives:state.objectives.map(x=>x.id===plan.objective_ref?{...x,status:'IN_PROGRESS'}:x),
        autonomy:{...state.autonomy,phase:'DISCOVER',objective_ref:plan.objective_ref,subject_scope:plan.subject_scope,retry_count:0,last_reconciled_revision:before}};
      const committed=await host.commitStateCAS({expected_revision:before,proposed_state:proposed,reason:'SELECT_OBJECTIVE'});
      return committed?.committed===true&&committed?.new_revision===before+1 ? {ok:true,executed:true,phase:'DISCOVER',objective_ref:plan.objective_ref} : denial('STALE_OR_UNCOMMITTED_STATE');
    }catch {return denial('HOST_SELECTION_ERROR');}
  }
  const assignment=state.coordination.active_role_assignment;
  let lease;
  try {
    const control=await host.attestControlPlanes(state,plan);
    if(control?.authenticated!==true||control?.router_id!==assignment.router_id||
      control?.watchdog_id!==assignment.watchdog_id||control?.router_no_mutation!==true||
      control?.watchdog_no_acceptance!==true||control?.isolation_verified!==true)
      return denial('CONTROL_PLANE_ISOLATION_NOT_ATTESTED');
    const identity=await host.authenticateActors(state,plan);
    if(identity?.authenticated!==true||identity?.state_revision!==state.revision ||
        !Array.isArray(identity.actor_ids)||!unique(identity.actor_ids)||
        ![assignment.worker_id,assignment.reviewer_id,assignment.acceptor_id,assignment.router_id,assignment.watchdog_id].every(x=>identity.actor_ids.includes(x)))
      return denial('UNAUTHENTICATED_ROLE_SEPARATION');
    lease=await host.acquireScopeLease({scope:plan.subject_scope,objective_ref:plan.objective_ref,expected_revision:state.revision,
      budget_ref:plan.budget_ref});
    if(!lease||!string(lease.lease_ref)||lease.scope!==plan.subject_scope||lease.state_revision!==state.revision||lease.exclusive!==true)
      return denial('TRUSTED_SCOPE_LEASE_REQUIRED');
    const permission=await host.authorizeMandate({...plan,lease_ref:lease.lease_ref});
    if(permission?.authorized!==true||permission?.state_revision!==state.revision||permission?.subject_scope!==plan.subject_scope||permission?.budget_ref!==plan.budget_ref||permission?.limits_enforced!==true||permission?.tools_within_allowlist!==true||permission?.external_effects_disabled!==true)
      return denial('UNAUTHORIZED_MANDATE');
    // For ALL code-writing work, pass the existing independent pre-code guard.
    if(plan.phase==='IMPLEMENT') {
      const pre=await validatePreCodeAuthorization(state,{subject_scope:plan.subject_scope,worker_id:plan.actor_id},host);
      if(!pre.ok) return denial('PRECODE_DENIED',{failures:pre.failures});
    }
    const receipt=await host.executeStep({...plan,lease_ref:lease.lease_ref,
      reviewer_read_only:plan.phase==='REVIEW',
      forbidden_actions:[...RESERVED]});
    if(!receipt||receipt.outcome!=='PASS'||receipt.phase!==plan.phase||receipt.objective_ref!==plan.objective_ref||
       receipt.subject_scope!==plan.subject_scope||receipt.state_revision!==state.revision||
       receipt.subject_digest!==state.candidate_identity.subject_digest||
       receipt.actor_id!==plan.actor_id||!string(receipt.receipt_id)||!string(receipt.evidence_ref))
       return denial('MISMATCHED_OR_FAILED_PHASE_RECEIPT');
    if(plan.phase==='REVIEW' && (receipt.read_only!==true||receipt.reviewer_independence!=='IND2'&&receipt.reviewer_independence!=='IND3'))
      return denial('REVIEW_INDEPENDENCE_OR_READ_ONLY_UNPROVEN');
    if(plan.phase==='ACCEPT' && (receipt.review_receipt_ref!==state.autonomy.review_receipt_ref||receipt.verification_ok!==true))
      return denial('ACCEPTOR_DID_NOT_VERIFY_REVIEW_AND_TESTS');
    const proof=await host.verifyReceipt({receipt,plan,identity,lease});
    if(proof?.authentic!==true||proof?.candidate_bound!==true||proof?.actor_authorized!==true)
      return denial('RECEIPT_NOT_INDEPENDENTLY_AUTHENTICATED');
    const next=plan.technical_repair?'SPECIFY':NEXT[plan.phase];
    const proposed={...state,revision:state.revision+1,
      current_objective:next==='IDLE'?null:state.current_objective,
      evidence_refs:[...new Set([...(state.evidence_refs??[]),receipt.evidence_ref])],
      objectives:plan.phase==='ACCEPT'?state.objectives.map(o=>o.id===plan.objective_ref?{...o,status:'ACCEPTED_BOUNDED',acceptance_ref:receipt.receipt_id}:o):state.objectives,
      autonomy:{...state.autonomy,
      phase:next,last_receipt_ref:receipt.receipt_id,retry_count:plan.technical_repair?state.autonomy.retry_count+1:0,
      lease_ref:null,
      ...(plan.phase==='REVIEW'?{review_receipt_ref:receipt.receipt_id,review_subject_digest:receipt.subject_digest}:{}),
      ...(next==='IDLE'?{objective_ref:null,subject_scope:null,review_receipt_ref:null,review_subject_digest:null}:{})}};
    // Commit goes through real CAS; a returned receipt is not authority on its own.
    const committed=await host.commitStateCAS({expected_revision:state.revision,proposed_state:proposed,
      receipt,reason:'ADVANCE_AUTONOMOUS_PHASE'});
    if(committed?.committed!==true||committed?.new_revision!==state.revision+1) return denial('STALE_OR_UNCOMMITTED_STATE');
    return {ok:true,executed:true,completed_phase:plan.phase,next_phase:next,
      receipt_ref:receipt.receipt_id,revision:state.revision+1};
  }catch {return denial('TRUSTED_HOST_OR_STEP_ERROR');}
  finally { if(lease?.lease_ref) {try {await host.releaseScopeLease({lease_ref:lease.lease_ref,scope:plan.subject_scope});} catch {/* host incident monitor owns lock recovery */}} }
}

// A safe inspection CLI. A project host must use the exported execute function.
if(process.argv[1] && path.resolve(process.argv[1])===fileURLToPath(import.meta.url)) {
  const args=process.argv.slice(2);
  if(args[0]!=='--plan') {console.error('USAGE node tools/autonomy-engine.mjs --plan [path-to-PROJECT_STATE.yaml]'); process.exitCode=2;}
  else {
    try {
      const statePath=args[1]?path.resolve(args[1]):path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../governance/PROJECT_STATE.yaml');
      const state=parseStrictJson(fs.readFileSync(statePath,'utf8'),'PROJECT_STATE.yaml');
      const plan=planAutonomousCycle(state);
      console.log(JSON.stringify(plan,null,2));
      if(!plan.ok&&plan.reason!=='AUTONOMY_INACTIVE') process.exitCode=1;
    }catch(e) {console.error('AUTONOMY_PLAN_ERROR',e.message);process.exitCode=1;}
  }
}
