import fs from 'fs';
import os from 'os';
import path from 'path';
import crypto from 'crypto';
import { fileURLToPath } from 'url';
import { verifyPackage, parseStrictJson, validateReleaseState, validateSourceTemplate, validateRoleCombination, validatePreCodeAuthorization, validateLiveDeploymentAuthorization, validateBoundReleaseReadiness, executeAuthorizedDeployment, sha256File } from './verify-package.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const source = path.resolve(here, '..');
let pass=0, fail=0;
const report=[];
const assert = (name, cond, detail='') => { if (cond) {pass++; report.push(`PASS ${name}`);} else {fail++; report.push(`FAIL ${name} ${detail}`);} };
const clone = name => { const d=fs.mkdtempSync(path.join(os.tmpdir(),`ugm-${name}-`)); fs.cpSync(source,d,{recursive:true}); return d; };
const manifestPath = d => path.join(d,'PACKAGE_MANIFEST.json');
const readManifest = d => JSON.parse(fs.readFileSync(manifestPath(d),'utf8'));
const writeManifest = (d,m) => fs.writeFileSync(manifestPath(d), JSON.stringify(m,null,2)+'\n');
const rehash = (d, rel) => { const m=readManifest(d); m.files[rel]=sha256File(path.join(d,...rel.split('/'))); writeManifest(d,m); };
const mutateState = (d, fn) => { const p=path.join(d,'governance/PROJECT_STATE.yaml'); const o=JSON.parse(fs.readFileSync(p,'utf8')); fn(o); fs.writeFileSync(p,JSON.stringify(o,null,2)+'\n'); rehash(d,'governance/PROJECT_STATE.yaml'); };
const mutateReadme = (d, text) => { const p=path.join(d,'README.md'); fs.appendFileSync(p,`\n${text}\n`); rehash(d,'README.md'); };

assert('pristine-package', verifyPackage(source).ok, verifyPackage(source).failures.join(','));
{
 const d=clone('lifecycle-reviews-populated'); mutateState(d,o=>{o.lifecycle_review_refs=['invented-evidence'];});
 assert('unbound-lifecycle-must-have-no-observations', !verifyPackage(d).ok);
}
{
 const d=clone('lifecycle-reviews-invalid'); mutateState(d,o=>{o.lifecycle_review_refs='not-an-array';});
 assert('invalid-lifecycle-review-references-rejected', !verifyPackage(d).ok);
}


{
 const d=clone('empty-manifest'); const m=readManifest(d); m.version='wrong-version'; m.files={}; m.active_authorities=[]; writeManifest(d,m);
 assert('wrong-version-empty-manifest-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('bad-digest'); const m=readManifest(d); m.files['README.md']='xyz'; writeManifest(d,m);
 assert('invalid-digest-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('missing-payload'); fs.unlinkSync(path.join(d,'README.md'));
 assert('missing-payload-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('unexpected-nested'); fs.mkdirSync(path.join(d,'governance/nested')); fs.writeFileSync(path.join(d,'governance/nested/extra.md'),'x');
 assert('unexpected-nested-file-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('unexpected-empty-governance-directory');fs.mkdirSync(path.join(d,'governance/nested'));
 assert('unexpected-empty-governance-directory-rejected',!verifyPackage(d).ok);
}
{
 const d=clone('traversal'); const m=readManifest(d); const dig=m.files['README.md']; delete m.files['README.md']; m.files['../README.md']=dig; writeManifest(d,m);
 assert('manifest-traversal-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('absolute'); const m=readManifest(d); const dig=m.files['README.md']; delete m.files['README.md']; m.files['C:/temp/README.md']=dig; writeManifest(d,m);
 assert('manifest-absolute-path-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('malformed-state'); const p=path.join(d,'governance/PROJECT_STATE.yaml'); fs.writeFileSync(p,'{ "schema_version": '); rehash(d,'governance/PROJECT_STATE.yaml');
 assert('malformed-state-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('duplicate-state'); const p=path.join(d,'governance/PROJECT_STATE.yaml'); let t=fs.readFileSync(p,'utf8'); t=t.replace('"revision": 0,','"revision": 0,\n  "revision": 1,'); fs.writeFileSync(p,t); rehash(d,'governance/PROJECT_STATE.yaml');
 assert('duplicate-key-state-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('comment-camouflage'); const p=path.join(d,'governance/PROJECT_STATE.yaml'); fs.appendFileSync(p,'// activation: UNBOUND state: NO-GO'); rehash(d,'governance/PROJECT_STATE.yaml');
 assert('comments-cannot-satisfy-state', !verifyPackage(d).ok);
}
{
 const d=clone('activated-source'); mutateState(d,o=>{o.activation='ACTIVE'; o.project.id='x'; o.project.root='relative/project';});
 assert('activated-source-template-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('wrong-type'); mutateState(d,o=>{o.revision='zero';});
 assert('wrong-state-type-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('windows-backslash'); mutateReadme(d,'Local residue C:\\Users\\Example\\project\\file.txt');
 assert('windows-single-backslash-neutrality-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('windows-forward'); mutateReadme(d,'Local residue C:/Users/Example/project/file.txt');
 assert('windows-forward-slash-neutrality-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('posix-home'); mutateReadme(d,'Local residue /home/example/project/file.txt');
 assert('posix-home-neutrality-rejected', !verifyPackage(d).ok);
}
{
 const d=clone('relative-positive'); mutateReadme(d,'Valid relative reference docs/project/file.md');
 const r=verifyPackage(d); assert('relative-path-positive-case', r.ok, r.failures.join(','));
}

// Generic release consistency: historical observation may survive present NO-GO.
{
 const s=JSON.parse(fs.readFileSync(path.join(source,'governance/PROJECT_STATE.yaml'),'utf8'));
 s.release.deployment_observations.push({candidate_ref:'old', environment_ref:'prod', observed_at:'2026-01-01T00:00:00Z'});
 assert('historical-observation-does-not-grant-current-permission', validateReleaseState(s).length===0, validateReleaseState(s).join(','));
}
{
 const s=JSON.parse(fs.readFileSync(path.join(source,'governance/PROJECT_STATE.yaml'),'utf8'));
 s.activation='ACTIVE'; s.candidate_identity.subject_ref='candidate-A'; s.release.eligibility={...s.release.eligibility,status:'RELEASE_ELIGIBLE',candidate_ref:'candidate-A',environment_ref:'staging',scope_ref:'scope-1',evidence_refs:['e1'],decision_ref:'d1',decided_at:'2026-01-01T00:00:00Z',freshness_ref:'fresh-1',reason:null};
 s.release.deployment_authorization={...s.release.deployment_authorization,status:'AUTHORIZED',grant_ref:'g1',candidate_ref:'candidate-B',environment_ref:'staging',scope_ref:'scope-1',action:'deploy',granted_at:'2026-01-01T00:01:00Z',freshness_ref:'fresh-2'};
 assert('partially-bound-invalid-deployment-rejected', validateReleaseState(s).length>0);
}
{
 const s=JSON.parse(fs.readFileSync(path.join(source,'governance/PROJECT_STATE.yaml'),'utf8'));
 s.activation='ACTIVE'; s.candidate_identity.subject_ref='candidate-A'; s.release.eligibility={...s.release.eligibility,status:'RELEASE_ELIGIBLE',candidate_ref:'candidate-A',environment_ref:'staging',scope_ref:'scope-1',evidence_refs:[],decision_ref:null,decided_at:null,freshness_ref:null,reason:null};
 assert('contradictory-release-eligibility-rejected', validateReleaseState(s).length>0);
}

// Role matrix.
assert('R3-writer-self-accept-rejected', validateRoleCombination({risk:'R3',changeClass:'PRODUCT',mode:'THREE_ROLE',writerId:'A',reviewerId:'B',acceptorId:'A',reviewerIndependence:'IND2'}).length>0);
assert('governance-distinct-roles-pass', validateRoleCombination({risk:'R1',changeClass:'GOVERNANCE',mode:'THREE_ROLE',writerId:'A',reviewerId:'B',acceptorId:'C',reviewerIndependence:'IND2',routerId:'D',watchdogId:'E'}).length===0);
assert('IND1-cannot-satisfy-R3', validateRoleCombination({risk:'R3',changeClass:'PRODUCT',mode:'THREE_ROLE',writerId:'A',reviewerId:'B',acceptorId:'C',reviewerIndependence:'IND1'}).length>0);
assert('v410-R2-combined-reviewer-acceptor-now-denied-in-strict-profile', validateRoleCombination({risk:'R2',changeClass:'PRODUCT',mode:'REVIEW_ACCEPT',writerId:'A',reviewerId:'B',acceptorId:'B',reviewerIndependence:'IND2',combinedReviewerAcceptorAllowed:true}).length>0);
assert('v410-R1-self-path-denied-even-with-legacy-policy', validateRoleCombination({risk:'R1',changeClass:'PRODUCT',mode:'SELF_CHECKED',writerId:'A',projectAllowsLowRiskR1Self:true,reversibleLowBlast:true,touchesConsequentialBoundary:false}).length>0);
assert('R1-low-risk-self-path-rejected-without-policy', validateRoleCombination({risk:'R1',changeClass:'PRODUCT',mode:'SELF_CHECKED',writerId:'A',projectAllowsLowRiskR1Self:false,reversibleLowBlast:true}).length>0);
assert('R1-self-path-cannot-evade-consequential-boundary', validateRoleCombination({risk:'R1',changeClass:'PRODUCT',mode:'SELF_CHECKED',writerId:'A',projectAllowsLowRiskR1Self:true,reversibleLowBlast:true,touchesConsequentialBoundary:true}).length>0);


// Adversarial repairs: these cases previously returned [] (false PASS).
const sourceState = () => parseStrictJson(fs.readFileSync(path.join(source,'governance/PROJECT_STATE.yaml'),'utf8'));
const bound = () => {
  const s=sourceState();s.activation='ACTIVE';s.revision=3;
  s.project.id='test-project';s.project.root='bound-repository';s.project.adoption_mode='NEW_PROJECT';s.project.product_archetype='WEB_APP';s.project.active_paradigms=['FUNCTIONAL'];
  s.governance_binding.active_version='4.1.0-r3';s.governance_binding.project_binding_ref='reviewed-project-binding';
  s.coordination.active_role_assignment={worker_id:'worker-a',reviewer_id:'reviewer-b',acceptor_id:'acceptor-c',reviewer_independence:'IND2',router_id:'router-d',watchdog_id:'watchdog-e'};
  s.candidate_identity={subject_ref:'candidate-A',subject_digest:'a'.repeat(64),subject_scope:['scope-1'],frozen_at_state_revision:2};
  s.specification_gate={status:'SPEC_VERIFIED',missing_specification_prompts:[],diagram_first_status:'DIAGRAM_LOCKED',relative_search_refs:['standards-ref-1'],dimension_refs:{intent_actors:'intent-ref',data_interfaces:'data-ref',paradigm_boundaries:'paradigm-ref',diagrams:'diagrams-ref',relative_standards:'standard-ref',acceptance_negative:'acceptance-ref'},diagram_refs:['diagram-1'],diagram_approval_ref:'reviewer-approved-diagram-1',diagram_lock_subject_digest:'a'.repeat(64),subject_scope_ref:'scope-1',missing_kind:null};
  s.required_hard_gates=['quality_security'];
  s.hard_gates={quality_security:{status:'PASS',evidence_refs:['gate-evidence-1'],subject_digest:'a'.repeat(64)}};
  s.release.eligibility={...s.release.eligibility,status:'RELEASE_ELIGIBLE',candidate_ref:'candidate-A',environment_ref:'staging',scope_ref:'scope-1',evidence_refs:['evidence-1'],decision_ref:'decision-1',decided_at:'2026-01-01T00:00:00Z',valid_until:'2030-01-01T00:00:00Z',freshness_ref:null,reason:null};
  s.release.deployment_authorization={...s.release.deployment_authorization,status:'AUTHORIZED',grant_ref:'grant-1',candidate_ref:'candidate-A',environment_ref:'staging',scope_ref:'scope-1',action:'deploy',granted_at:'2026-01-02T00:00:00Z',valid_until:'2030-01-01T00:00:00Z',freshness_ref:null,revoked_at:null};
  return s;
};
const at={now:'2026-09-24T00:00:00Z'};
assert('valid-bound-release-shape-pass',validateReleaseState(bound(),at).length===0,validateReleaseState(bound(),at).join(','));
{
 const s=bound();s.release.deployment_authorization.candidate_ref='foreign-candidate';
 assert('v410-bound-deployment-candidate-drift-explicitly-rejected',validateReleaseState(s,at).some(x=>x.includes('drift')));
}
{
 const s=bound();s.candidate_identity.subject_digest=null;s.candidate_identity.subject_scope=[];
 assert('release-missing-frozen-digest-and-scope-rejected',validateReleaseState(s,at).length>0);
}
{
 const s=bound();s.release.deployment_authorization.valid_until='2020-01-02T00:00:00Z';
 assert('expired-deployment-grant-rejected',validateReleaseState(s,at).some(x=>x.includes('expired')));
}
{
 const s=bound();s.release.deployment_authorization.granted_at='2026-02-31T00:00:00Z';
 assert('invalid-calendar-date-rejected',validateReleaseState(s,at).length>0);
}
{
 const s=bound();s.release.eligibility.scope_ref='missing-scope';
 assert('release-scope-not-in-frozen-subject-rejected',validateReleaseState(s,at).length>0);
}
{
 const s=sourceState();delete s.hard_gates;
 assert('source-missing-hard-gates-rejected',validateSourceTemplate(s).length>0);
}
{
 const s=sourceState();s.release.deployment_observations=[{candidate_ref:'old',environment_ref:'prod',observed_at:'2026-01-01T00:00:00Z'}];
 assert('source-invented-deployment-observation-rejected',validateSourceTemplate(s).length>0);
}
{
 const s=sourceState();s.release.eligibility.decision_ref='invented';
 assert('source-NO-GO-invented-decision-rejected',validateSourceTemplate(s).length>0);
}
{
 const s=sourceState();s.negative_history_refs=['invented'];
 assert('source-fake-negative-history-rejected',validateSourceTemplate(s).length>0);
}
assert('R2-three-role-missing-acceptor-rejected',validateRoleCombination({risk:'R2',changeClass:'PRODUCT',mode:'THREE_ROLE',writerId:'A',reviewerId:'B',reviewerIndependence:'IND2'}).length>0);
assert('R1-three-role-IND0-rejected',validateRoleCombination({risk:'R1',changeClass:'PRODUCT',mode:'THREE_ROLE',writerId:'A',reviewerId:'B',acceptorId:'C',reviewerIndependence:'IND0'}).length>0);
assert('R0-review-accept-missing-reviewer-rejected',validateRoleCombination({risk:'R0',changeClass:'PRODUCT',mode:'REVIEW_ACCEPT',writerId:'A',acceptorId:'B',reviewerIndependence:'IND1',combinedReviewerAcceptorAllowed:true}).length>0);
assert('v410-R0-combined-reviewer-acceptor-denied-even-with-policy', validateRoleCombination({risk:'R0',changeClass:'PRODUCT',mode:'REVIEW_ACCEPT',writerId:'A',reviewerId:'B',acceptorId:'B',reviewerIndependence:'IND1',combinedReviewerAcceptorAllowed:true}).length>0);
assert('v410-R0-self-check-denied-in-strict-profile', validateRoleCombination({risk:'R0',changeClass:'PRODUCT',mode:'SELF_CHECKED',writerId:'A'}).length>0);
assert('governance-self-path-rejected',validateRoleCombination({risk:'R0',changeClass:'GOVERNANCE',mode:'SELF_CHECKED',writerId:'A'}).length>0);
{
 const req={candidate_ref:'candidate-A',environment_ref:'staging',scope_ref:'scope-1',action:'deploy',artifact_digest:'a'.repeat(64)};
 const s=bound();
 const noRuntime=await executeAuthorizedDeployment(s,req,null);
 assert('effect-unbound-runtime-denied',!noRuntime.ok);
 const readinessReceipt={ready:true,state_revision:s.revision,candidate_ref:req.candidate_ref,subject_digest:req.artifact_digest,environment_ref:req.environment_ref,scope_ref:req.scope_ref,hard_gates_verified:true,blockers_clear:true,dependencies_verified:true,required_review_verified:true,evidence_verified:true,receipt_ref:'synthetic-readiness-1'};
 const validRuntime={trustedNow:'2026-09-24T00:00:00Z',verifyAuthoritativeReadiness:async()=>readinessReceipt};
 const noChecker=await executeAuthorizedDeployment(s,req,validRuntime);
 assert('effect-without-atomic-adapter-denied',!noChecker.ok);
 const wrong=await executeAuthorizedDeployment(s,{...req,environment_ref:'production'}, {...validRuntime,authorizeAndExecute:async()=>({applied:true})});
 assert('effect-cross-environment-denied',!wrong.ok);
 const stale=await executeAuthorizedDeployment(s,req,{...validRuntime,authorizeAndExecute:async()=>({applied:true,grant_consumed:false})});
 assert('effect-not-consumed-denied',!stale.ok);
 assert('legacy-preflight-never-authorizes-effect',(await validateLiveDeploymentAuthorization(s,req,validRuntime)).length>0);
 const receipt={applied:true,grant_consumed:true,durable:true,exact_artifact_verified_at_effect:true,operation_ref:'synthetic-op-1',receipt_ref:'synthetic-execution-1',grant_ref:'grant-1',state_revision:s.revision,frozen_subject_digest:s.candidate_identity.subject_digest,...req};
 const synthetic=await executeAuthorizedDeployment(s,req,{...validRuntime,authorizeAndExecute:async()=>receipt});
 assert('synthetic-atomic-adapter-receipt-shape-pass',synthetic.ok,synthetic.failures.join(','));
}


// r2 regressions: deliberately recompute manifests to exercise semantics, not hashes.
for (const [name,mutate] of [
  ['source-nested-eligibility-admin-override',s=>{s.release.eligibility.admin_override=true;}],
  ['source-nested-deployment-authorized',s=>{s.release.deployment_authorization.authorized=true;}],
  ['source-extra-project',s=>{s.project.extra_project='AnotherProject';}],
  ['source-extra-release',s=>{s.release.emergency_authorization=true;}],
  ['source-extra-candidate',s=>{s.candidate_identity.override_digest=true;}],
  ['source-extra-overhead',s=>{s.overhead.security_exception=true;}],
  ['source-extra-views',s=>{s.views.release_override=true;}],
  ['source-extra-governance-binding',s=>{s.governance_binding.alternate_active_version='x';}],
  ['source-missing-nested-key',s=>{delete s.release.eligibility.reason;}]
]) {
  const d=clone(name); mutateState(d,mutate); const r=verifyPackage(d);
  assert(`${name}-rehash-rejected`,!r.ok,r.failures.join(','));
}
for (const status of ['UNBOUND','STAGED','INACTIVE']) {
  const s=bound(); s.activation=status;
  assert(`${status}-release-ineligible`,validateReleaseState(s,at).some(x=>x==='activation:current-release-requires-ACTIVE'));
  assert(`${status}-grant-not-authorized`,validateReleaseState(s,at).some(x=>x==='activation:current-authorization-requires-ACTIVE'));
}
{
 const s=bound();s.activation='STAGED';s.release.eligibility={...sourceState().release.eligibility};s.release.deployment_authorization={...sourceState().release.deployment_authorization};
 assert('staged-NO-GO-NONE-pass',validateReleaseState(s,at).length===0,validateReleaseState(s,at).join(','));
}
{
 const s=bound();s.activation='INACTIVE';s.release.eligibility={...sourceState().release.eligibility};s.release.deployment_authorization={...sourceState().release.deployment_authorization,status:'CONSUMED'};
 assert('inactive-NO-GO-historical-consumed-pass',validateReleaseState(s,at).length===0,validateReleaseState(s,at).join(','));
}
assert('missing-class-rejected',validateRoleCombination({risk:'R1',mode:'SELF_CHECKED',writerId:'A',projectAllowsLowRiskR1Self:true,reversibleLowBlast:true}).includes('roles:unknown-change-class'));
for (const name of ['GOVERNANCE_MISSPELLED','VALIDATR','APPROVAL_CONTRO','RELEASE_CONTRO','',null,'UNKNOWN']) {
 const result=validateRoleCombination({risk:'R1',changeClass:name,mode:'SELF_CHECKED',writerId:'A',projectAllowsLowRiskR1Self:true,reversibleLowBlast:true});
 assert(`unknown-class-${JSON.stringify(name)}-rejected`,result.includes('roles:unknown-change-class'),result.join(','));
}
for (const name of ['GOVERNANCE','VALIDATOR','APPROVAL_CONTROL','RELEASE_CONTROL']) {
 assert(`${name}-not-R1-self`,validateRoleCombination({risk:'R1',changeClass:name,mode:'SELF_CHECKED',writerId:'A',projectAllowsLowRiskR1Self:true,reversibleLowBlast:true}).length>0);
 assert(`${name}-valid-three-role`,validateRoleCombination({risk:'R1',changeClass:name,mode:'THREE_ROLE',writerId:'A',reviewerId:'B',acceptorId:'C',reviewerIndependence:'IND2',routerId:'D',watchdogId:'E'}).length===0);
}
for (const now of ['NOT_A_DATE','2026-02-31T00:00:00Z',null,'']) {
 const error=validateReleaseState(sourceState(),{now});
 assert(`invalid-now-${JSON.stringify(now)}-rejected`,error.includes('state:invalid-now'),error.join(','));
}
assert('explicit-valid-clock-NO-GO-pass',validateReleaseState(sourceState(),at).length===0);
for (const [name,raw] of [['null','null'],['array','[]'],['string','"manifest"'],['number','42']]) {
 const d=clone('manifest-'+name);fs.writeFileSync(manifestPath(d),raw);
 let r; try {r=verifyPackage(d);} catch(e) {r={ok:true,failures:['THREW '+e.message]};}
 assert(`manifest-${name}-clean-rejection`,!r.ok && r.failures.includes('manifest:object-required'),r.failures.join(','));
}
{
 const d=path.join(os.tmpdir(),`ugm-missing-root-${Date.now()}-should-not-exist`);
 const r=verifyPackage(d); assert('missing-root-clean-rejection',!r.ok && r.failures.includes('package-root:directory-required'));
}

// r3 adversarial regression: structural versus true bound-readiness versus effect.
for (const [name,mut] of [
 ['missing-hard-gates',s=>{delete s.hard_gates;}],
 ['empty-hard-gates',s=>{s.hard_gates={};}],
 ['failed-gate',s=>{s.hard_gates.quality_security.status='FAIL';}],
 ['unknown-gate',s=>{s.hard_gates.quality_security.status='UNKNOWN';}],
 ['gate-wrong-digest',s=>{s.hard_gates.quality_security.subject_digest='b'.repeat(64);}],
 ['gate-missing-evidence',s=>{s.hard_gates.quality_security.evidence_refs=[];}],
 ['unresolved-blocker',s=>{s.blockers.push('unresolved');}],
 ['future-decision',s=>{s.release.eligibility.decided_at='2027-01-01T00:00:00Z';}],
 ['future-grant',s=>{s.release.deployment_authorization.granted_at='2027-01-01T00:00:00Z';}]
]) {const s=bound();mut(s);const r=validateReleaseState(s,at);assert(`r3-${name}-rejected`,r.length>0,r.join(','));}
{
 const s=bound();s.hard_gates.quality_security={status:'NOT_APPLICABLE',reason:'Bound policy declares this gate inapplicable'};
 assert('r3-documented-inapplicable-gate-structural-pass',validateReleaseState(s,at).length===0,validateReleaseState(s,at).join(','));
}
{
 const s=bound();const now='2026-09-24T00:00:00Z';
 const noAdapter=await validateBoundReleaseReadiness(s,{trustedNow:now});
 assert('r3-bound-readiness-no-adapter-denied',noAdapter.includes('readiness:trusted-adapter-required'));
 const falseAdapter=await validateBoundReleaseReadiness(s,{trustedNow:now,verifyAuthoritativeReadiness:async()=>({ready:true})});
 assert('r3-readiness-false-receipt-denied',falseAdapter.includes('readiness:authoritative-readiness-not-confirmed'));
 const goodReceipt={ready:true,state_revision:s.revision,candidate_ref:'candidate-A',subject_digest:'a'.repeat(64),environment_ref:'staging',scope_ref:'scope-1',hard_gates_verified:true,blockers_clear:true,dependencies_verified:true,required_review_verified:true,evidence_verified:true,receipt_ref:'synthetic'};
 const adapter={trustedNow:now,verifyAuthoritativeReadiness:async()=>goodReceipt};
 assert('r3-synthetic-readiness-shape-pass',(await validateBoundReleaseReadiness(s,adapter)).length===0);
 const req={candidate_ref:'candidate-A',environment_ref:'staging',scope_ref:'scope-1',action:'deploy',artifact_digest:'a'.repeat(64)};
 for (const [name,mut] of [
  ['missing-artifact',r=>{delete r.artifact_digest;}],
  ['wrong-artifact',r=>{r.artifact_digest='b'.repeat(64);}],
  ['wrong-action',r=>{r.action='erase';}]
 ]) {const r={...req};mut(r);const result=await executeAuthorizedDeployment(s,r,{...adapter,authorizeAndExecute:async()=>{throw Error('must never be invoked')}});assert(`r3-${name}-denied`,!result.ok && !result.failures.some(f=>f.includes('failed-or-uncertain')),result.failures.join(','));}
 const noReady=await executeAuthorizedDeployment(s,req,{trustedNow:now,authorizeAndExecute:async()=>({applied:true})});
 assert('r3-effect-without-readiness-denied',!noReady.ok);
 const unconsumed=await executeAuthorizedDeployment(s,req,{...adapter,authorizeAndExecute:async()=>({applied:true,grant_consumed:false})});
 assert('r3-effect-without-consumption-denied',!unconsumed.ok);
 const notAtEffect=await executeAuthorizedDeployment(s,req,{...adapter,authorizeAndExecute:async()=>({applied:true,grant_consumed:true,durable:true,exact_artifact_verified_at_effect:false})});
 assert('r3-effect-no-effect-boundary-digest-denied',!notAtEffect.ok);
 const receipt={applied:true,grant_consumed:true,durable:true,exact_artifact_verified_at_effect:true,operation_ref:'synthetic-operation',receipt_ref:'synthetic-execution',grant_ref:'grant-1',state_revision:s.revision,frozen_subject_digest:s.candidate_identity.subject_digest,...req};
 const yes=await executeAuthorizedDeployment(s,req,{...adapter,authorizeAndExecute:async()=>receipt});
 assert('r3-synthetic-execution-receipt-shape-pass',yes.ok && yes.receipt===receipt,yes.failures.join(','));
 const thrown=await executeAuthorizedDeployment(s,req,{...adapter,authorizeAndExecute:async()=>{throw Error('uncertain')}});
 assert('r3-uncertain-effect-denies-and-requires-reconcile',!thrown.ok && thrown.failures.some(f=>f.includes('uncertain-reconcile')));
}

// v4.1.0-r3 source and runtime gate regressions (candidate-only synthetic verification).
for (const [name,mutate] of [
  ['missing-specification-gate',s=>{delete s.specification_gate;}],
  ['missing-required-hard-gates',s=>{delete s.required_hard_gates;}],
  ['source-spec-verified-falsification',s=>{s.specification_gate.status='SPEC_VERIFIED';}],
  ['source-diagram-locked-falsification',s=>{s.specification_gate.diagram_first_status='DIAGRAM_LOCKED';}],
  ['source-invented-required-gate',s=>{s.required_hard_gates=['imaginary-gate'];}],
  ['source-invented-reviewer',s=>{s.coordination.active_role_assignment.reviewer_id='reviewer';}],
  ['source-invented-archetype',s=>{s.project.product_archetype='WEB_APP';}]
]) {
  const s=sourceState();mutate(s);
  assert(`v410-${name}-source-rejected`,validateSourceTemplate(s).length>0);
}
{
  const s=sourceState();s.specification_gate={...s.specification_gate,status:'BLOCKED_MISSING_SPEC',diagram_first_status:'DIAGRAM_PENDING',relative_search_refs:[],missing_specification_prompts:['missing-intent'],missing_kind:'OWNER_INTENT'};
  assert('v410-blocked-missing-spec-is-valid-no-go',validateReleaseState(s,at).length===0,validateReleaseState(s,at).join(','));
}
for (const [name,mutate] of [
  ['unverified-spec',s=>{s.specification_gate.status='UNVERIFIED';}],
  ['blocked-spec',s=>{s.specification_gate.status='BLOCKED_MISSING_SPEC';s.specification_gate.missing_specification_prompts=['owner intent unresolved'];s.specification_gate.missing_kind='OWNER_INTENT';}],
  ['diagram-pending',s=>{s.specification_gate.diagram_first_status='DIAGRAM_PENDING';}],
  ['diagram-drift',s=>{s.specification_gate.diagram_first_status='DIAGRAM_DRIFT';}],
  ['unresolved-spec-prompts',s=>{s.specification_gate.missing_specification_prompts=['missing-acceptance-condition'];}],
  ['empty-required-inventory',s=>{s.required_hard_gates=[];}],
  ['missing-required-inventory',s=>{delete s.required_hard_gates;}],
  ['hard-gate-name-mismatch',s=>{s.required_hard_gates=['quality_security','privacy_gate'];}],
  ['duplicate-required-gate-names',s=>{s.required_hard_gates=['quality_security','quality_security'];}],
  ['required-gate-not-applicable-no-reason',s=>{s.hard_gates.quality_security={status:'NOT_APPLICABLE'};}],
  ['invalid-archetype',s=>{s.project.product_archetype='ALIEN';}],
  ['invalid-paradigm',s=>{s.project.active_paradigms=['INVALID'];}],
  ['missing-active-binding',s=>{s.governance_binding.active_version=null;}],
  ['wrong-active-binding-version',s=>{s.governance_binding.active_version='4.0.4';}],
  ['missing-project-binding-ref',s=>{s.governance_binding.project_binding_ref=null;}],
  ['missing-active-project-identity',s=>{s.project.id=null;}],
  ['missing-active-root',s=>{s.project.root=null;}],
  ['stale-state-schema-version',s=>{s.schema_version='4.0.6-r3';}]
]) {
 const s=bound();mutate(s);
 const errors=validateReleaseState(s,at);
 assert(`v410-${name}-release-rejected`,errors.length>0,errors.join(','));
}
{
 const s=bound();s.required_hard_gates=['quality_security','privacy_gate'];
 s.hard_gates.privacy_gate={status:'PASS',subject_digest:s.candidate_identity.subject_digest,evidence_refs:['privacy-evidence']};
 assert('v410-complete-required-inventory-structural-pass',validateReleaseState(s,at).length===0,validateReleaseState(s,at).join(','));
}
for (const [name,mut] of [
  ['invalid-blocked-prompts-type',s=>{s.specification_gate.status='BLOCKED_MISSING_SPEC';s.specification_gate.missing_specification_prompts=null;}],
  ['invalid-required-gates-type',s=>{s.required_hard_gates={not:'iterable'};}]
]) {
 const s=bound();mut(s);
 let errors=[];let threw=false;
 try { errors=validateReleaseState(s,at); } catch(e) {threw=true;errors=[e.message];}
 assert(`v410-${name}-fail-closed-not-throw`,!threw&&errors.length>0,errors.join(','));
}
{
 const s=bound(); const request={candidate_ref:'candidate-A',environment_ref:'staging',scope_ref:'scope-1',action:'deploy',artifact_digest:'a'.repeat(64)};
 const readiness={ready:true,state_revision:s.revision,candidate_ref:request.candidate_ref,subject_digest:request.artifact_digest,environment_ref:request.environment_ref,scope_ref:request.scope_ref,hard_gates_verified:true,blockers_clear:true,dependencies_verified:true,required_review_verified:true,evidence_verified:true,receipt_ref:'synthetic-ready'};
 const runtime={trustedNow:at.now,verifyAuthoritativeReadiness:async()=>readiness};
 const baseReceipt={applied:true,grant_consumed:true,durable:true,exact_artifact_verified_at_effect:true,operation_ref:'synthetic-operation',receipt_ref:'synthetic-effect',grant_ref:'grant-1',...request,state_revision:s.revision,frozen_subject_digest:s.candidate_identity.subject_digest};
 for (const [name,mutate] of [
  ['effect-missing-state-revision',r=>{delete r.state_revision;}],
  ['effect-stale-state-revision',r=>{r.state_revision=s.revision-1;}],
  ['effect-missing-frozen-subject',r=>{delete r.frozen_subject_digest;}],
  ['effect-wrong-frozen-subject',r=>{r.frozen_subject_digest='b'.repeat(64);}],
  ['effect-replayed-grant',r=>{r.grant_consumed=false;}]
 ]) {
   const receipt={...baseReceipt};mutate(receipt);
   const result=await executeAuthorizedDeployment(s,request,{...runtime,authorizeAndExecute:async()=>receipt});
   assert(`v410-${name}-denied`,!result.ok && result.failures.includes('effect:atomic-execution-not-confirmed'),result.failures.join(','));
 }
 const good=await executeAuthorizedDeployment(s,request,{...runtime,authorizeAndExecute:async()=>({...baseReceipt})});
 assert('v410-exact-state-revision-and-subject-echo-pass-synthetic-only',good.ok,good.failures.join(','));
}


// F3: historical NO-GO timestamps are checked for shape and impossible chronology.
for (const [name,mutate] of [
 ['no-go-invalid-decided-at',s=>{s.release.eligibility.decided_at='not-a-date';}],
 ['no-go-future-decided-at',s=>{s.release.eligibility.decided_at='2029-01-01T00:00:00Z';}],
 ['no-go-invalid-valid-until',s=>{s.release.eligibility.valid_until='not-a-date';}],
 ['no-go-invalid-date-order',s=>{s.release.eligibility.decided_at='2026-01-02T00:00:00Z';s.release.eligibility.valid_until='2026-01-01T00:00:00Z';}],
 ['no-go-valid-until-without-decision',s=>{s.release.eligibility.valid_until='2026-02-01T00:00:00Z';}]
]) {
 const s=sourceState();mutate(s);
 const failures=validateReleaseState(s,at);
 assert(`v410-${name}-denied`,failures.length>0,failures.join(','));
}
{
 const s=sourceState();s.release.eligibility.decided_at='2026-01-01T00:00:00Z';s.release.eligibility.valid_until='2026-02-01T00:00:00Z';
 assert('v410-no-go-well-formed-history-does-not-grant-release',validateReleaseState(s,at).length===0 && s.release.eligibility.status==='NO-GO');
}

// v4.1.0-r3-r1 strict three-agent controls and mandatory Router/Watchdog identity uniqueness.
for (const risk of ['R0','R1','R2','R3']) {
  const proper={risk,changeClass:'PRODUCT',mode:'THREE_ROLE',workerId:'worker-a',reviewerId:'reviewer-b',acceptorId:'acceptor-c',reviewerIndependence:'IND2',routerId:'router-d',watchdogId:'watchdog-e'};
  assert(`strict-${risk}-five-actor-assignment-valid`,validateRoleCombination(proper).length===0);
  assert(`strict-${risk}-self-check-denied`,validateRoleCombination({...proper,mode:'SELF_CHECKED'}).length>0);
  assert(`strict-${risk}-combined-roles-denied`,validateRoleCombination({...proper,acceptorId:'reviewer-b'}).length>0);
}
for (const [name,changes] of [
  ['router-matches-worker',{routerId:'worker-a'}],
  ['watchdog-matches-acceptor',{watchdogId:'acceptor-c'}],
  ['router-matches-watchdog',{routerId:'watchdog-e'}],
  ['low-independence',{reviewerIndependence:'IND1'}],
  ['missing-reviewer',{reviewerId:null}],
  ['missing-router',{routerId:undefined}],
  ['missing-watchdog',{watchdogId:undefined}],
]) {
  const base={risk:'R1',changeClass:'PRODUCT',mode:'THREE_ROLE',workerId:'worker-a',reviewerId:'reviewer-b',acceptorId:'acceptor-c',reviewerIndependence:'IND2',routerId:'router-d',watchdogId:'watchdog-e'};
  assert(`superagent-${name}-rejected`,validateRoleCombination({...base,...changes}).length>0);
}
for (const [name,mut] of [
  ['missing-intent-dimension',s=>{s.specification_gate.dimension_refs.intent_actors=null;}],
  ['missing-acceptance-dimension',s=>{s.specification_gate.dimension_refs.acceptance_negative=null;}],
  ['missing-standard-search',s=>{s.specification_gate.relative_search_refs=[];}],
  ['missing-diagram-approval',s=>{s.specification_gate.diagram_approval_ref=null;}],
  ['missing-approved-scope',s=>{s.specification_gate.subject_scope_ref=null;}],
  ['approved-scope-outside-candidate',s=>{s.specification_gate.subject_scope_ref='unknown';}],
  ['missing-locked-diagram-refs',s=>{s.specification_gate.diagram_refs=[];}],
  ['incorrect-diagram-lock',s=>{s.specification_gate.diagram_lock_subject_digest='b'.repeat(64);}],
  ['approved-scope-release-mismatch',s=>{s.candidate_identity.subject_scope.push('scope-2');s.release.eligibility.scope_ref='scope-2';s.release.deployment_authorization.scope_ref='scope-2';}],
  ['role-collision',s=>{s.coordination.active_role_assignment.router_id='worker-a';s.coordination.active_role_assignment.worker_id='worker-a';}],
  ['missing-watchdog-for-release',s=>{s.coordination.active_role_assignment.watchdog_id=null;}],
  ['missing-reviewer-for-release',s=>{s.coordination.active_role_assignment.reviewer_id=null;}],
]) {
  const s=bound();mut(s);
  assert(`spec-deep-${name}-denied`,validateReleaseState(s,at).length>0);
}
// Harden strict JSON parser against JavaScript's magic inherited __proto__ setter.
{
  const parsed=parseStrictJson('{"__proto__":{"admin":true},"ordinary":2}');
  assert('strict-json-proto-magic-key-remains-own-data',Object.hasOwn(parsed,'__proto__') && parsed['__proto__'].admin===true && !Object.hasOwn(Object.prototype,'admin'));
  assert('strict-json-proto-magic-key-cannot-inject-authorization',parsed.admin === undefined && parsed.ordinary===2);
}
// True scope-specific pre-code authorization needs an actual trusted adapter; stubs only test contract.
{
  const s=bound();
  s.coordination.active_role_assignment={worker_id:'worker-a',reviewer_id:'reviewer-b',acceptor_id:'acceptor-c',reviewer_independence:'IND2',router_id:'router-d',watchdog_id:'watchdog-e'};
  const task={subject_scope:'scope-1',worker_id:'worker-a'};
  const rt={trustedNow:at.now};
  const failure=await validatePreCodeAuthorization(s,task,rt);
  assert('precode-no-trusted-adapter-blocks',!failure.ok&&failure.failures.includes('precode:trusted-authorizer-required'));
  const approval={authorized:true,state_revision:s.revision,subject_digest:s.candidate_identity.subject_digest,subject_scope:task.subject_scope,worker_id:task.worker_id,diagram_approval_ref:s.specification_gate.diagram_approval_ref,receipt_ref:'synthetic-precode'};
  const ok=await validatePreCodeAuthorization(s,task,{...rt,verifyPreCodeAuthorization:async()=>approval});
  assert('precode-synthetic-valid-receipt-structural-only',ok.ok,ok.failures.join(','));
  for (const [name,mut] of [
    ['stale-revision',r=>r.state_revision--],
    ['stale-digest',r=>r.subject_digest='b'.repeat(64)],
    ['wrong-scope',r=>r.subject_scope='foreign'],
    ['wrong-worker',r=>r.worker_id='intruder'],
    ['missing-approval-ref',r=>delete r.diagram_approval_ref],
    ['missing-receipt',r=>delete r.receipt_ref],
  ]) {
    const v={...approval}; mut(v);
    const result=await validatePreCodeAuthorization(s,task,{...rt,verifyPreCodeAuthorization:async()=>v});
    assert(`precode-${name}-refused`,!result.ok);
  }
  const revoked=await validatePreCodeAuthorization({...s,activation:'STAGED'},task,{...rt,verifyPreCodeAuthorization:async()=>approval});
  assert('precode-nonactive-refused',!revoked.ok);
  const badScope=await validatePreCodeAuthorization(s,{...task,subject_scope:'other'}, {...rt,verifyPreCodeAuthorization:async()=>approval});
  assert('precode-outside-scope-refused',!badScope.ok);
  const development={...s,release:{...s.release,eligibility:sourceState().release.eligibility,deployment_authorization:sourceState().release.deployment_authorization}};
  const blockedGlobal=await validatePreCodeAuthorization({...development,blockers:['DIAGRAM_DRIFT']},task,{...rt,verifyPreCodeAuthorization:async()=>approval});
  assert('precode-unscoped-diagram-drift-blocker-denied',!blockedGlobal.ok && blockedGlobal.failures.includes('precode:unresolved-applicable-blockers'));
  const blockedScoped=await validatePreCodeAuthorization({...development,blockers:[{class:'DIAGRAM_DRIFT',subject_scope:'scope-1',status:'OPEN'}]},task,{...rt,verifyPreCodeAuthorization:async()=>approval});
  assert('precode-in-scope-diagram-drift-blocker-denied',!blockedScoped.ok);
  const resolvedScoped=await validatePreCodeAuthorization({...development,blockers:[{class:'DIAGRAM_DRIFT',subject_scope:'scope-1',status:'RESOLVED'}]},task,{...rt,verifyPreCodeAuthorization:async()=>approval});
  assert('precode-explicit-resolved-blocker-not-spuriously-blocking',resolvedScoped.ok);
  const otherScope=await validatePreCodeAuthorization({...development,blockers:[{class:'TECHNICAL',subject_scope:'scope-2',status:'OPEN'}]},task,{...rt,verifyPreCodeAuthorization:async()=>approval});
  assert('precode-disjoint-scoped-blocker-not-global',otherScope.ok);
  const broadened=structuredClone(s);broadened.candidate_identity.subject_scope.push('scope-2');
  const crossScope=await validatePreCodeAuthorization(broadened,{...task,subject_scope:'scope-2'}, {...rt,verifyPreCodeAuthorization:async(args)=>({...approval,subject_scope:args.subject_scope})});
  assert('precode-approval-of-one-scope-cannot-authorize-another',!crossScope.ok && crossScope.failures.includes('precode:approved-diagram-scope-mismatch'));
}
for (const [name,mut] of [
 ['router-unbound',s=>s.coordination.active_role_assignment.router_id='unexpected'],
 ['watchdog-unbound',s=>s.coordination.active_role_assignment.watchdog_id='unexpected'],
 ['dimension-unbound',s=>s.specification_gate.dimension_refs.diagrams='invented'],
 ['diagram-approval-unbound',s=>s.specification_gate.diagram_approval_ref='invented'],
 ['diagram-ref-unbound',s=>s.specification_gate.diagram_refs.push('invented')],
 ['diagram-digest-unbound',s=>s.specification_gate.diagram_lock_subject_digest='a'.repeat(64)],
 ['diagram-scope-unbound',s=>s.specification_gate.subject_scope_ref='scope-1'],
]) {
  const s=sourceState();mut(s);
  assert(`source-${name}-rejected`,validateSourceTemplate(s).length>0);
}

// Independent validator-level tests for the r3 role and post-diagram scope guards.
{
 const s=sourceState();s.activation='ACTIVE';s.revision=4;
 s.project={...s.project,id:'bound',root:'relative-root',adoption_mode:'NEW_PROJECT',product_archetype:'API_SERVICE',active_paradigms:['FUNCTIONAL']};
 s.governance_binding={...s.governance_binding,active_version:'4.1.0-r3',project_binding_ref:'binding'};
 s.autonomy={...s.autonomy,enabled:true,mode:'BOUNDED',budget_ref:'finite-budget'};
 const failures=validateReleaseState(s,{now:'2026-11-02T12:00:00Z'});
 assert('r3-enabled-autonomy-requires-complete-five-actor-assignment',failures.includes('coordination:complete-strict-five-actor-binding-required'),failures.join(','));
}
{
 const s=bound();s.release.eligibility={...s.release.eligibility,status:'NO-GO',candidate_ref:null,environment_ref:null,scope_ref:null};
 s.release.deployment_authorization={...s.release.deployment_authorization,status:'NONE',grant_ref:null,candidate_ref:null,environment_ref:null,scope_ref:null,action:null,granted_at:null,valid_until:null,freshness_ref:null,revoked_at:null};
 s.autonomy={...s.autonomy,enabled:true,mode:'BOUNDED',phase:'REVIEW',objective_ref:'objective-B',subject_scope:'scope-2',budget_ref:'finite-budget'};
 s.candidate_identity.subject_scope.push('scope-2');
 const failures=validateReleaseState(s,{now:'2026-11-02T12:00:00Z'});
 assert('r3-review-cannot-use-cross-scope-diagram-approval',failures.includes('autonomy:post-diagram-phase-scope-or-digest-mismatch'),failures.join(','));
}

console.log(report.join('\n'));
console.log(`SUMMARY pass=${pass} fail=${fail}`);
if (fail) process.exit(1);
