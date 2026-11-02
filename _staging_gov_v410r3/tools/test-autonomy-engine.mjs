import fs from 'fs';
import path from 'path';
import {fileURLToPath} from 'url';
import {validateReleaseState,validateSourceTemplate} from './verify-package.mjs';
import {planAutonomousCycle,eligibleObjectives,executeAutonomousCycle} from './autonomy-engine.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const origin=JSON.parse(fs.readFileSync(path.join(root,'governance/PROJECT_STATE.yaml'),'utf8'));
const copy=o=>structuredClone(o);
const tests=[];
const test=(name,p)=>tests.push({name,fn:p});
const now='2026-11-02T12:00:00Z';
const digest='a'.repeat(64);
function bound(phase='IDLE') {
 const s=copy(origin);s.activation='ACTIVE';s.revision=4;
 s.project={...s.project,id:'sample',root:'sample-root',adoption_mode:'NEW_PROJECT',product_archetype:'API_SERVICE',active_paradigms:['FUNCTIONAL']};
 s.governance_binding={...s.governance_binding,active_version:'4.1.0-r3',project_binding_ref:'binding-1'};
 s.coordination.active_role_assignment={worker_id:'worker-1',reviewer_id:'reviewer-2',acceptor_id:'acceptor-3',router_id:'router-4',watchdog_id:'watchdog-5',reviewer_independence:'IND2'};
 s.candidate_identity={subject_ref:'source-frozen',subject_digest:digest,subject_scope:['module-A','module-B'],frozen_at_state_revision:3};
 s.objectives=[{id:'A',subject_scope:'module-A',status:'QUEUED',priority:10,dependencies:[]},{id:'B',subject_scope:'module-B',status:'QUEUED',priority:1,dependencies:['A']}];
 s.autonomy={...s.autonomy,enabled:true,mode:'BOUNDED',phase,objective_ref:phase==='IDLE'?null:'A',subject_scope:phase==='IDLE'?null:'module-A',budget_ref:'budget-signed',max_retries:3};
 s.specification_gate={...s.specification_gate,status:'SPEC_VERIFIED',diagram_first_status:'DIAGRAM_LOCKED',relative_search_refs:['relative-search'],dimension_refs:{intent_actors:'a',data_interfaces:'b',paradigm_boundaries:'c',diagrams:'d',relative_standards:'e',acceptance_negative:'f'},diagram_refs:['diagram'],diagram_approval_ref:'independent-diagram-receipt',diagram_lock_subject_digest:digest,subject_scope_ref:'module-A',missing_kind:null};
 return s;
}
function host(s,{mutateReceipt=()=>{},mutateHost=()=>{}}={}) {
 const roles=s.coordination.active_role_assignment;
 let committed=null, released=0;
 const h={trustedNow:now,
  attestControlPlanes:async()=>({authenticated:true,router_id:roles.router_id,watchdog_id:roles.watchdog_id,router_no_mutation:true,watchdog_no_acceptance:true,isolation_verified:true}),
  authenticateActors:async()=>({authenticated:true,state_revision:s.revision,actor_ids:[roles.worker_id,roles.reviewer_id,roles.acceptor_id,roles.router_id,roles.watchdog_id]}),
  acquireScopeLease:async p=>({lease_ref:'exclusive-1',scope:p.scope,state_revision:p.expected_revision,exclusive:true}),
  authorizeMandate:async p=>({authorized:true,state_revision:p.expected_revision,subject_scope:p.subject_scope,budget_ref:p.budget_ref,limits_enforced:true,tools_within_allowlist:true,external_effects_disabled:true}),
  verifyPreCodeAuthorization:async p=>({authorized:true,state_revision:p.state_revision,subject_digest:p.subject_digest,subject_scope:p.subject_scope,worker_id:p.worker_id,diagram_approval_ref:p.diagram_approval_ref,receipt_ref:'pre-code-verified'}),
  executeStep:async p=>{const receipt={outcome:'PASS',phase:p.phase,objective_ref:p.objective_ref,subject_scope:p.subject_scope,state_revision:p.expected_revision,subject_digest:p.subject_digest,actor_id:p.actor_id,receipt_id:'phase-evidence-1',evidence_ref:'immutable-evidence-1',read_only:true,reviewer_independence:'IND2',verification_ok:true,review_receipt_ref:s.autonomy.review_receipt_ref};mutateReceipt(receipt);return receipt;},
  verifyReceipt:async()=>({authentic:true,candidate_bound:true,actor_authorized:true}),
  commitStateCAS:async q=>{committed=q;return {committed:true,new_revision:q.expected_revision+1};},
  releaseScopeLease:async()=>{released++;}
 };mutateHost(h);
 return Object.assign(h,{getCommitted:()=>committed,getReleased:()=>released});
}
const assert=(cond,extra='')=>{if(!cond)throw Error(extra||'assertion failed');};
const status=(s,expect)=>{const p=planAutonomousCycle(s,{now});assert(p.reason===expect,JSON.stringify(p));};
test('source template dormant and strict',()=>assert(validateSourceTemplate(origin).length===0,validateSourceTemplate(origin).join(',')));
test('source plan dormant',()=>status(origin,'AUTONOMY_INACTIVE'));
test('autonomy source rejects pre-enabled',()=>{const s=copy(origin);s.autonomy.enabled=true;assert(validateSourceTemplate(s).length>0);});
test('active autonomy requires bound budget',()=>{const s=bound();s.autonomy.budget_ref=null;assert(validateReleaseState(s,{now}).some(x=>x.includes('autonomy:bound')));});
test('active phase requires scoped objective',()=>{const s=bound('IMPLEMENT');s.autonomy.objective_ref=null;assert(validateReleaseState(s,{now}).some(x=>x.includes('autonomy:active-phase')));});
test('eligible queue dependency order',()=>{const s=bound();assert(eligibleObjectives(s).map(x=>x.id).join(',')==='A');});
test('no missing dependency accepted',()=>{const s=bound();s.objectives[0].dependencies=['missing'];assert(eligibleObjectives(s).length===0);});
test('select objective when idle',()=>{const p=planAutonomousCycle(bound(),{now});assert(p.action==='SELECT_OBJECTIVE'&&p.objective_ref==='A');});
test('block global blocker',()=>{const s=bound('IMPLEMENT');s.blockers=[{status:'OPEN',scope_ref:null}];status(s,'APPLICABLE_BLOCKER');});
test('block scoped diagram drift',()=>{const s=bound('IMPLEMENT');s.blockers=[{status:'OPEN',scope_ref:'module-A',class:'DIAGRAM_DRIFT'}];status(s,'APPLICABLE_BLOCKER');});
test('disjoint blocker does not block',()=>{const s=bound('IMPLEMENT');s.blockers=[{status:'OPEN',scope_ref:'module-B'}];assert(planAutonomousCycle(s,{now}).action==='EXECUTE_PHASE');});
test('owner reserved actions stop',()=>{const s=bound('IMPLEMENT');s.objectives[0].reserved_actions=['DEPLOY'];status(s,'RESERVED_OWNER_DECISION');});
test('spec missing CRP',()=>{const s=bound('IMPLEMENT');s.specification_gate.status='BLOCKED_MISSING_SPEC';s.specification_gate.missing_specification_prompts=['intent-question'];s.specification_gate.missing_kind='OWNER_INTENT';status(s,'OWNER_CLARIFICATION_REQUIRED');});
test('code requires locked diagrams',()=>{const s=bound('IMPLEMENT');s.specification_gate.diagram_first_status='DIAGRAM_PENDING';assert(['STATE_INVALID','SPEC_OR_DIAGRAM_NOT_LOCKED'].includes(planAutonomousCycle(s,{now}).reason));});
test('phase acceptance needs review',()=>status(bound('ACCEPT'),'REVIEW_NOT_BOUND_TO_CANDIDATE'));
test('review of different digest denied',()=>{const s=bound('ACCEPT');s.autonomy.review_receipt_ref='review-1';s.autonomy.review_subject_digest='b'.repeat(64);status(s,'REVIEW_NOT_BOUND_TO_CANDIDATE');});
test('valid acceptance plan',()=>{const s=bound('ACCEPT');s.autonomy.review_receipt_ref='review-1';s.autonomy.review_subject_digest=digest;assert(planAutonomousCycle(s,{now}).action==='EXECUTE_PHASE');});
test('reject missing host adapter',async()=>{const s=bound('TEST');assert((await executeAutonomousCycle(s,null)).reason==='TRUSTED_PROJECT_HOST_REQUIRED');});
test('selection commits only through CAS',async()=>{const s=bound(),h=host(s);const r=await executeAutonomousCycle(s,h);assert(r.ok&&r.phase==='DISCOVER'&&h.getCommitted().proposed_state.revision===5);});
test('selection denied on stale CAS',async()=>{const s=bound(),h=host(s,{mutateHost:h=>{h.commitStateCAS=async()=>({committed:false});}});const r=await executeAutonomousCycle(s,h);assert(!r.ok&&r.reason==='STALE_OR_UNCOMMITTED_STATE');});
test('test phase advances and releases lease',async()=>{const s=bound('TEST'),h=host(s);const r=await executeAutonomousCycle(s,h);assert(r.ok&&r.next_phase==='REVIEW'&&h.getReleased()===1&&h.getCommitted().proposed_state.autonomy.phase==='REVIEW',JSON.stringify(r));});
test('wrong actor receipt denied',async()=>{const s=bound('TEST'),h=host(s,{mutateReceipt:r=>r.actor_id='spoof'});const r=await executeAutonomousCycle(s,h);assert(r.reason==='MISMATCHED_OR_FAILED_PHASE_RECEIPT'&&!h.getCommitted()&&h.getReleased()===1);});
test('wrong candidate receipt denied',async()=>{const s=bound('TEST'),h=host(s,{mutateReceipt:r=>r.subject_digest='b'.repeat(64)});assert((await executeAutonomousCycle(s,h)).reason==='MISMATCHED_OR_FAILED_PHASE_RECEIPT');});
test('stale receipt denied',async()=>{const s=bound('TEST'),h=host(s,{mutateReceipt:r=>r.state_revision=1});assert((await executeAutonomousCycle(s,h)).reason==='MISMATCHED_OR_FAILED_PHASE_RECEIPT');});
test('missing exclusive lease denies action',async()=>{const s=bound('TEST'),h=host(s,{mutateHost:h=>{h.acquireScopeLease=async()=>({lease_ref:'nonexclusive',scope:'module-A',state_revision:4,exclusive:false});}});assert((await executeAutonomousCycle(s,h)).reason==='TRUSTED_SCOPE_LEASE_REQUIRED');});
test('unverified actors denied',async()=>{const s=bound('TEST'),h=host(s,{mutateHost:h=>{h.authenticateActors=async()=>({authenticated:false,state_revision:4});}});assert((await executeAutonomousCycle(s,h)).reason==='UNAUTHENTICATED_ROLE_SEPARATION');});
test('unauthorized mandate denied',async()=>{const s=bound('TEST'),h=host(s,{mutateHost:h=>{h.authorizeMandate=async()=>({authorized:false});}});assert((await executeAutonomousCycle(s,h)).reason==='UNAUTHORIZED_MANDATE');});
test('untrusted receipt denied',async()=>{const s=bound('TEST'),h=host(s,{mutateHost:h=>{h.verifyReceipt=async()=>({authentic:false});}});assert((await executeAutonomousCycle(s,h)).reason==='RECEIPT_NOT_INDEPENDENTLY_AUTHENTICATED');});
test('review read-only receipt required',async()=>{const s=bound('REVIEW'),h=host(s,{mutateReceipt:r=>r.read_only=false});assert((await executeAutonomousCycle(s,h)).reason==='REVIEW_INDEPENDENCE_OR_READ_ONLY_UNPROVEN');});
test('review receipt recorded in state only after CAS',async()=>{const s=bound('REVIEW'),h=host(s);const r=await executeAutonomousCycle(s,h);assert(r.ok&&h.getCommitted().proposed_state.autonomy.review_receipt_ref==='phase-evidence-1');});
test('acceptor cannot skip matching prior review',async()=>{const s=bound('ACCEPT');s.autonomy.review_receipt_ref='original-review';s.autonomy.review_subject_digest=digest;const h=host(s,{mutateReceipt:r=>r.review_receipt_ref='different-review'});assert((await executeAutonomousCycle(s,h)).reason==='ACCEPTOR_DID_NOT_VERIFY_REVIEW_AND_TESTS');});
test('implement requires authenticated pre-code gate',async()=>{const s=bound('IMPLEMENT'),h=host(s,{mutateHost:h=>{h.verifyPreCodeAuthorization=async()=>({authorized:false});}});assert((await executeAutonomousCycle(s,h)).reason==='PRECODE_DENIED');});
test('implement with bound pre-code receipt',async()=>{const s=bound('IMPLEMENT'),h=host(s);const r=await executeAutonomousCycle(s,h);assert(r.ok&&r.next_phase==='TEST',JSON.stringify(r));});
test('host exception stops rather than passes',async()=>{const s=bound('TEST'),h=host(s,{mutateHost:h=>{h.executeStep=async()=>{throw Error('crashed');};}});assert((await executeAutonomousCycle(s,h)).reason==='TRUSTED_HOST_OR_STEP_ERROR');});
test('no release from phase acceptance',async()=>{const s=bound('ACCEPT');s.autonomy.review_receipt_ref='review-a';s.autonomy.review_subject_digest=digest;const h=host(s);const r=await executeAutonomousCycle(s,h);assert(r.ok&&s.release.eligibility.status==='NO-GO'&&h.getCommitted().proposed_state.release.eligibility.status==='NO-GO');});
test('reserved action objective never selected',()=>{const s=bound();s.objectives[0].action='MERGE_PROTECTED';assert(eligibleObjectives(s).length===0);});
test('objective dependency drift stops later phase',()=>{const s=bound('TEST');s.objectives[0].dependencies=['unknown'];status(s,'OBJECTIVE_DEPENDENCY_DRIFT');});
test('end-to-end-bounded-cycle-and-dependent-next-objective',async()=>{
  let s=bound();let good=true;
  for (let i=0;i<11;i++) {
    const h=host(s);
    const result=await executeAutonomousCycle(s,h);
    if (!result.ok || !h.getCommitted()) {good=false;break;}
    s=h.getCommitted().proposed_state;
  }
  assert(good&&s.objectives[0].status==='ACCEPTED_BOUNDED'&&s.autonomy.phase==='IDLE'&&s.release.eligibility.status==='NO-GO'&&eligibleObjectives(s).map(x=>x.id).join(',')==='B');
});

test('technical missing spec autonomously dispatches standards only',()=>{const s=bound('SPECIFY');s.specification_gate.status='BLOCKED_MISSING_SPEC';s.specification_gate.missing_kind='TECHNICAL';s.specification_gate.missing_specification_prompts=['RFC selection unknown'];const p=planAutonomousCycle(s,{now});assert(p.action==='EXECUTE_PHASE'&&p.phase==='STANDARDS'&&p.technical_repair===true);});
test('technical missing spec does not allow code write',async()=>{const s=bound('IMPLEMENT');s.specification_gate.status='BLOCKED_MISSING_SPEC';s.specification_gate.missing_kind='TECHNICAL';s.specification_gate.missing_specification_prompts=['protocol unknown'];const h=host(s);const r=await executeAutonomousCycle(s,h);assert(r.ok&&r.completed_phase==='STANDARDS'&&h.getCommitted().proposed_state.autonomy.phase==='SPECIFY'&&h.getCommitted().proposed_state.specification_gate.status==='BLOCKED_MISSING_SPEC');});
test('technical research bounded retries',()=>{const s=bound('SPECIFY');s.specification_gate.status='BLOCKED_MISSING_SPEC';s.specification_gate.missing_kind='TECHNICAL';s.specification_gate.missing_specification_prompts=['protocol unknown'];s.autonomy.retry_count=3;status(s,'RETRY_BUDGET_EXHAUSTED');});
test('mixed intent cannot auto-research around owner',()=>{const s=bound('SPECIFY');s.specification_gate.status='BLOCKED_MISSING_SPEC';s.specification_gate.missing_kind='MIXED';s.specification_gate.missing_specification_prompts=['owner business policy'];status(s,'OWNER_CLARIFICATION_REQUIRED');});

test('control plane isolation denial',async()=>{const s=bound('TEST');const h=host(s,{mutateHost:h=>{h.attestControlPlanes=async()=>({authenticated:true,router_id:'router-4',watchdog_id:'watchdog-5',router_no_mutation:false,watchdog_no_acceptance:true,isolation_verified:true});}});assert((await executeAutonomousCycle(s,h)).reason==='CONTROL_PLANE_ISOLATION_NOT_ATTESTED');});
test('unbounded budget denial',async()=>{const s=bound('TEST');const h=host(s,{mutateHost:h=>{h.authorizeMandate=async p=>({authorized:true,state_revision:p.expected_revision,subject_scope:p.subject_scope,budget_ref:p.budget_ref,limits_enforced:false,tools_within_allowlist:true,external_effects_disabled:true});}});assert((await executeAutonomousCycle(s,h)).reason==='UNAUTHORIZED_MANDATE');});
test('external effects from development mandate denied',async()=>{const s=bound('TEST');const h=host(s,{mutateHost:h=>{h.authorizeMandate=async p=>({authorized:true,state_revision:p.expected_revision,subject_scope:p.subject_scope,budget_ref:p.budget_ref,limits_enforced:true,tools_within_allowlist:true,external_effects_disabled:false});}});assert((await executeAutonomousCycle(s,h)).reason==='UNAUTHORIZED_MANDATE');});
// r3 adversarial repairs (F1-F3): active actors, cross-scope locks, and second-task selection.
test('F1-active-autonomy-with-null-roles-rejected-by-release-state',()=>{
  const s=bound('IMPLEMENT');s.current_objective=null;
  s.coordination.active_role_assignment={worker_id:null,reviewer_id:null,acceptor_id:null,
    reviewer_independence:null,router_id:null,watchdog_id:null};
  assert(validateReleaseState(s,{now}).includes('coordination:complete-strict-five-actor-binding-required'));
});
test('F2-plan-rejects-post-diagram-phase-when-spec-scope-mismatches-autonomy-scope',()=>{
  const s=bound('IMPLEMENT');s.autonomy.objective_ref='B';s.autonomy.subject_scope='module-B';
  s.objectives[0].status='ACCEPTED_BOUNDED';s.objectives[1].status='IN_PROGRESS';
  const p=planAutonomousCycle(s,{now});
  assert(!p.ok&&['STATE_INVALID','SPEC_OR_DIAGRAM_NOT_LOCKED'].includes(p.reason),JSON.stringify(p));
});
test('F3-execute-rejects-review-phase-when-spec-scope-mismatches-autonomy-scope',async()=>{
  const s=bound('REVIEW');s.autonomy.objective_ref='B';s.autonomy.subject_scope='module-B';
  s.objectives[0].status='ACCEPTED_BOUNDED';s.objectives[1].status='IN_PROGRESS';
  const h=host(s);const r=await executeAutonomousCycle(s,h);
  assert(!r.ok&&!h.getCommitted()&&!r.executed,JSON.stringify(r));
});
test('F2-selection-resets-stale-diagram-lock-on-next-objective',async()=>{
  const s=bound('IDLE');s.objectives[0].status='ACCEPTED_BOUNDED';
  const h=host(s);const r=await executeAutonomousCycle(s,h);const candidate=h.getCommitted()?.proposed_state;
  assert(r.ok&&r.objective_ref==='B'&&candidate.current_objective==='B');
  assert(candidate.specification_gate.status==='UNVERIFIED'&&
    candidate.specification_gate.diagram_first_status==='DIAGRAM_PENDING'&&
    candidate.specification_gate.subject_scope_ref==='module-B'&&
    candidate.specification_gate.diagram_lock_subject_digest===null);
  assert(candidate.release.eligibility.status==='NO-GO'&&
    validateReleaseState(candidate,{now}).length===0,JSON.stringify(validateReleaseState(candidate,{now})));
});
test('F1-current-objective-is-cleared-only-when-cycle-finishes',async()=>{
  const s=bound('EVOLVE');s.current_objective='A';
  const h=host(s);const r=await executeAutonomousCycle(s,h);
  assert(r.ok&&h.getCommitted().proposed_state.current_objective===null&&
    h.getCommitted().proposed_state.autonomy.phase==='IDLE');
});
test('F2-diagram-lock-digest-mismatch-rejected-in-test-phase',()=>{
  const s=bound('TEST');s.specification_gate.diagram_lock_subject_digest='b'.repeat(64);
  const p=planAutonomousCycle(s,{now});
  assert(!p.ok&&['STATE_INVALID','SPEC_OR_DIAGRAM_NOT_LOCKED'].includes(p.reason));
});

let pass=0,fail=0;
for(const t of tests){try{await t.fn();pass++;console.log('PASS',t.name);}catch(e){fail++;console.error('FAIL',t.name,e.message);}}
console.log(`AUTONOMY_SUMMARY pass=${pass} fail=${fail}`);
if(fail)process.exitCode=1;
