import fs from 'fs';
import os from 'os';
import path from 'path';
import crypto from 'crypto';
import { fileURLToPath } from 'url';
import { verifyPackage, parseStrictJson, validateReleaseState, validateSourceTemplate, validateRoleCombination, validateLiveDeploymentAuthorization, validateBoundReleaseReadiness, executeAuthorizedDeployment, sha256File } from './verify-package.mjs';

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
 assert('deployment-candidate-drift-rejected', validateReleaseState(s).some(x=>x.includes('drift')));
}
{
 const s=JSON.parse(fs.readFileSync(path.join(source,'governance/PROJECT_STATE.yaml'),'utf8'));
 s.activation='ACTIVE'; s.candidate_identity.subject_ref='candidate-A'; s.release.eligibility={...s.release.eligibility,status:'RELEASE_ELIGIBLE',candidate_ref:'candidate-A',environment_ref:'staging',scope_ref:'scope-1',evidence_refs:[],decision_ref:null,decided_at:null,freshness_ref:null,reason:null};
 assert('contradictory-release-eligibility-rejected', validateReleaseState(s).length>0);
}

// Role matrix.
assert('R3-writer-self-accept-rejected', validateRoleCombination({risk:'R3',changeClass:'PRODUCT',mode:'THREE_ROLE',writerId:'A',reviewerId:'B',acceptorId:'A',reviewerIndependence:'IND2'}).length>0);
assert('governance-distinct-roles-pass', validateRoleCombination({risk:'R1',changeClass:'GOVERNANCE',mode:'THREE_ROLE',writerId:'A',reviewerId:'B',acceptorId:'C',reviewerIndependence:'IND2'}).length===0);
assert('IND1-cannot-satisfy-R3', validateRoleCombination({risk:'R3',changeClass:'PRODUCT',mode:'THREE_ROLE',writerId:'A',reviewerId:'B',acceptorId:'C',reviewerIndependence:'IND1'}).length>0);
assert('R2-combined-reviewer-acceptor-allowed-when-bound', validateRoleCombination({risk:'R2',changeClass:'PRODUCT',mode:'REVIEW_ACCEPT',writerId:'A',reviewerId:'B',acceptorId:'B',reviewerIndependence:'IND2',combinedReviewerAcceptorAllowed:true}).length===0);
assert('R1-low-risk-self-path-pass-when-bound', validateRoleCombination({risk:'R1',changeClass:'PRODUCT',mode:'SELF_CHECKED',writerId:'A',projectAllowsLowRiskR1Self:true,reversibleLowBlast:true,touchesConsequentialBoundary:false}).length===0);
assert('R1-low-risk-self-path-rejected-without-policy', validateRoleCombination({risk:'R1',changeClass:'PRODUCT',mode:'SELF_CHECKED',writerId:'A',projectAllowsLowRiskR1Self:false,reversibleLowBlast:true}).length>0);
assert('R1-self-path-cannot-evade-consequential-boundary', validateRoleCombination({risk:'R1',changeClass:'PRODUCT',mode:'SELF_CHECKED',writerId:'A',projectAllowsLowRiskR1Self:true,reversibleLowBlast:true,touchesConsequentialBoundary:true}).length>0);


// Adversarial repairs: these cases previously returned [] (false PASS).
const sourceState = () => parseStrictJson(fs.readFileSync(path.join(source,'governance/PROJECT_STATE.yaml'),'utf8'));
const bound = () => {
  const s=sourceState();s.activation='ACTIVE';s.revision=3;
  s.candidate_identity={subject_ref:'candidate-A',subject_digest:'a'.repeat(64),subject_scope:['scope-1'],frozen_at_state_revision:2};
  s.hard_gates={quality_security:{status:'PASS',evidence_refs:['gate-evidence-1'],subject_digest:'a'.repeat(64)}};
  s.release.eligibility={...s.release.eligibility,status:'RELEASE_ELIGIBLE',candidate_ref:'candidate-A',environment_ref:'staging',scope_ref:'scope-1',evidence_refs:['evidence-1'],decision_ref:'decision-1',decided_at:'2026-01-01T00:00:00Z',valid_until:'2030-01-01T00:00:00Z',freshness_ref:null,reason:null};
  s.release.deployment_authorization={...s.release.deployment_authorization,status:'AUTHORIZED',grant_ref:'grant-1',candidate_ref:'candidate-A',environment_ref:'staging',scope_ref:'scope-1',action:'deploy',granted_at:'2026-01-02T00:00:00Z',valid_until:'2030-01-01T00:00:00Z',freshness_ref:null,revoked_at:null};
  return s;
};
const at={now:'2026-09-24T00:00:00Z'};
assert('valid-bound-release-shape-pass',validateReleaseState(bound(),at).length===0,validateReleaseState(bound(),at).join(','));
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
assert('R0-review-accept-valid-bound-pass',validateRoleCombination({risk:'R0',changeClass:'PRODUCT',mode:'REVIEW_ACCEPT',writerId:'A',reviewerId:'B',acceptorId:'B',reviewerIndependence:'IND1',combinedReviewerAcceptorAllowed:true}).length===0);
assert('R0-self-check-remains-light',validateRoleCombination({risk:'R0',changeClass:'PRODUCT',mode:'SELF_CHECKED',writerId:'A'}).length===0);
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
 const receipt={applied:true,grant_consumed:true,durable:true,exact_artifact_verified_at_effect:true,operation_ref:'synthetic-op-1',receipt_ref:'synthetic-execution-1',grant_ref:'grant-1',...req};
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
 assert(`${name}-valid-three-role`,validateRoleCombination({risk:'R1',changeClass:name,mode:'THREE_ROLE',writerId:'A',reviewerId:'B',acceptorId:'C',reviewerIndependence:'IND2'}).length===0);
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
 const receipt={applied:true,grant_consumed:true,durable:true,exact_artifact_verified_at_effect:true,operation_ref:'synthetic-operation',receipt_ref:'synthetic-execution',grant_ref:'grant-1',...req};
 const yes=await executeAuthorizedDeployment(s,req,{...adapter,authorizeAndExecute:async()=>receipt});
 assert('r3-synthetic-execution-receipt-shape-pass',yes.ok && yes.receipt===receipt,yes.failures.join(','));
 const thrown=await executeAuthorizedDeployment(s,req,{...adapter,authorizeAndExecute:async()=>{throw Error('uncertain')}});
 assert('r3-uncertain-effect-denies-and-requires-reconcile',!thrown.ok && thrown.failures.some(f=>f.includes('uncertain-reconcile')));
}
console.log(report.join('\n'));
console.log(`SUMMARY pass=${pass} fail=${fail}`);
if (fail) process.exit(1);
