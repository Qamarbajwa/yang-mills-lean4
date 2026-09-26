import fs from 'fs';
import os from 'os';
import path from 'path';
import crypto from 'crypto';
import { fileURLToPath, pathToFileURL } from 'url';

export const SUPPORTED = Object.freeze({
  manifestSchema: 'UGM-PACKAGE-MANIFEST-1',
  package: 'UNIVERSAL_GOVERNANCE_MINIMAL',
  version: '4.0.6-r3',
  activeAuthorities: [
    'governance/GOVERNANCE.md',
    'governance/PROJECT_DIRECTION.md',
    'governance/PROJECT_STATE.yaml'
  ],
  payloads: [
    'ADOPTION_PROMPT.md',
    'EVIDENCE_AND_MIGRATION.md',
    'README.md',
    'governance/GOVERNANCE.md',
    'governance/PROJECT_DIRECTION.md',
    'governance/PROJECT_STATE.yaml',
    'tools/test-verify-package.mjs',
    'tools/verify-package.mjs'
  ]
});

export function sha256File(p) {
  return crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
}

// Strict dependency-free JSON parser: the source state template is intentionally
// JSON-compatible YAML 1.2. Duplicate object keys are rejected.
export function parseStrictJson(text, label='input') {
  let i = 0;
  const err = msg => { throw new Error(`${label}: ${msg} at byte ${i}`); };
  const ws = () => { while (i < text.length && /\s/.test(text[i])) i++; };
  const parseString = () => {
    if (text[i] !== '"') err('expected string');
    const start = i++;
    let escaped = false;
    while (i < text.length) {
      const c = text[i++];
      if (escaped) { escaped = false; continue; }
      if (c === '\\') { escaped = true; continue; }
      if (c === '"') {
        const raw = text.slice(start, i);
        try { return JSON.parse(raw); } catch { err('invalid string escape'); }
      }
      if (c.charCodeAt(0) < 0x20) err('control character in string');
    }
    err('unterminated string');
  };
  const parseNumber = () => {
    const m = text.slice(i).match(/^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/);
    if (!m) err('invalid number');
    i += m[0].length;
    const n = Number(m[0]);
    if (!Number.isFinite(n)) err('non-finite number');
    return n;
  };
  const parseValue = () => {
    ws();
    if (i >= text.length) err('unexpected end');
    if (text[i] === '"') return parseString();
    if (text[i] === '{') return parseObject();
    if (text[i] === '[') return parseArray();
    if (text.startsWith('true', i)) { i += 4; return true; }
    if (text.startsWith('false', i)) { i += 5; return false; }
    if (text.startsWith('null', i)) { i += 4; return null; }
    if (text[i] === '-' || /\d/.test(text[i])) return parseNumber();
    err('unexpected token');
  };
  const parseObject = () => {
    const obj = {};
    const keys = new Set();
    i++; ws();
    if (text[i] === '}') { i++; return obj; }
    while (true) {
      ws();
      const key = parseString();
      if (keys.has(key)) err(`duplicate key ${JSON.stringify(key)}`);
      keys.add(key);
      ws(); if (text[i++] !== ':') err('expected colon');
      obj[key] = parseValue();
      ws();
      if (text[i] === '}') { i++; return obj; }
      if (text[i++] !== ',') err('expected comma');
    }
  };
  const parseArray = () => {
    const arr = [];
    i++; ws();
    if (text[i] === ']') { i++; return arr; }
    while (true) {
      arr.push(parseValue()); ws();
      if (text[i] === ']') { i++; return arr; }
      if (text[i++] !== ',') err('expected comma');
    }
  };
  const value = parseValue(); ws();
  if (i !== text.length) err('trailing content');
  return value;
}

function requireObject(v, name, failures) {
  if (!v || typeof v !== 'object' || Array.isArray(v)) failures.push(`${name}:object-required`);
}
function isStringOrNull(v) { return v === null || typeof v === 'string'; }
function nonEmptyString(v) { return typeof v === 'string' && v.trim().length > 0; }
function validSha(v) { return v === null || /^[0-9a-f]{64}$/.test(v); }
function exactSha(v) { return typeof v === 'string' && /^[0-9a-f]{64}$/.test(v); }

const RFC3339 = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$/;
function validInstant(v) {
  if (!nonEmptyString(v) || !RFC3339.test(v)) return false;
  const n = Date.parse(v);
  if (!Number.isFinite(n)) return false;
  // Reject dates JS normalizes (e.g. 2026-02-31) and invalid offsets.
  const m = v.match(/^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})/);
  if (!m || Number(m[2]) < 1 || Number(m[2]) > 12 || Number(m[3]) < 1 || Number(m[3]) > new Date(Date.UTC(Number(m[1]), Number(m[2]), 0)).getUTCDate()) return false;
  if (Number(m[4]) > 23 || Number(m[5]) > 59 || Number(m[6]) > 59) return false;
  const off = v.match(/([+-])(\d{2}):(\d{2})$/);
  if (off && (Number(off[2]) > 23 || Number(off[3]) > 59)) return false;
  return true;
}
function validRefArray(v) { return Array.isArray(v) && v.every(nonEmptyString); }
function nonemptyRefArray(v) { return validRefArray(v) && v.length > 0 && new Set(v).size === v.length; }

// SHAPE_AND_CONSISTENCY_ONLY. Neither a local machine clock nor a caller-supplied
// state object proves a live grant, non-revocation, identity, evidence or permission.
export function validateReleaseState(state, {now = new Date().toISOString()} = {}) {
  const f=[];
  // A supplied bad clock is an invalid validation input, never a reason to skip expiry.
  if (!validInstant(now)) f.push('state:invalid-now');
  requireObject(state, 'state', f);
  if (f.length) return f;
  if (!Number.isInteger(state.revision) || state.revision < 0) f.push('state:revision');
  if (!validRefArray(state.lifecycle_review_refs)) f.push('state:lifecycle-review-refs');
  if (!state.hard_gates || typeof state.hard_gates !== 'object' || Array.isArray(state.hard_gates)) f.push('state:hard-gates-object-required');
  if (!Array.isArray(state.blockers)) f.push('state:blockers-array-required');
  if (!['UNBOUND','STAGED','ACTIVE','INACTIVE'].includes(state.activation)) f.push('state:activation');
  requireObject(state.candidate_identity, 'candidate_identity', f);
  requireObject(state.release, 'release', f);
  if (f.length) return f;
  const ci=state.candidate_identity, rel=state.release;
  if (!isStringOrNull(ci.subject_ref)) f.push('candidate_identity:subject_ref');
  if (!validSha(ci.subject_digest)) f.push('candidate_identity:subject_digest');
  if (!validRefArray(ci.subject_scope)) f.push('candidate_identity:subject_scope');
  if (!(ci.frozen_at_state_revision===null || (Number.isInteger(ci.frozen_at_state_revision) && ci.frozen_at_state_revision>=0 && ci.frozen_at_state_revision<=state.revision))) f.push('candidate_identity:frozen_at_state_revision');
  requireObject(rel.eligibility,'release.eligibility',f);
  requireObject(rel.deployment_authorization,'release.deployment_authorization',f);
  if (!Array.isArray(rel.deployment_observations)) f.push('release.deployment_observations:array-required');
  if (f.length) return f;
  for (const [idx,obs] of rel.deployment_observations.entries()) {
    if (!obs || typeof obs!=='object' || Array.isArray(obs) || !nonEmptyString(obs.candidate_ref) || !nonEmptyString(obs.environment_ref) || !validInstant(obs.observed_at)) f.push(`release.deployment_observations:${idx}:invalid`);
  }
  const e=rel.eligibility;
  if (!['NO-GO','RELEASE_ELIGIBLE'].includes(e.status)) f.push('release.eligibility:status');
  for (const k of ['candidate_ref','environment_ref','scope_ref','decision_ref','decided_at','valid_until','freshness_ref','reason']) if (!isStringOrNull(e[k])) f.push(`release.eligibility:${k}`);
  if (!validRefArray(e.evidence_refs)) f.push('release.eligibility:evidence_refs');
  if (e.status==='NO-GO') {
    if (e.candidate_ref!==null || e.environment_ref!==null || e.scope_ref!==null) f.push('release.eligibility:no-go-has-current-grant-subject');
  } else if (e.status==='RELEASE_ELIGIBLE') {
    // Structural fail-closed checks. The authoritative, project-bound readiness
    // adapter below must ALSO verify whether the declared set is complete.
    if (!state.hard_gates || typeof state.hard_gates !== 'object' || Array.isArray(state.hard_gates) || Object.keys(state.hard_gates).length === 0) f.push('release.eligibility:hard-gates-required');
    else for (const [name,gate] of Object.entries(state.hard_gates)) {
      if (!gate || typeof gate!=='object' || Array.isArray(gate) || !['PASS','NOT_APPLICABLE'].includes(gate.status)) f.push(`release.eligibility:hard-gate-${name}-not-verified`);
      else if (gate.status==='PASS' && (!nonemptyRefArray(gate.evidence_refs) || gate.subject_digest!==ci.subject_digest)) f.push(`release.eligibility:hard-gate-${name}-evidence-or-candidate`);
      else if (gate.status==='NOT_APPLICABLE' && !nonEmptyString(gate.reason)) f.push(`release.eligibility:hard-gate-${name}-inapplicability-unjustified`);
    }
    if (!Array.isArray(state.blockers) || state.blockers.length !== 0) f.push('release.eligibility:unresolved-blockers');
    if (!nonEmptyString(ci.subject_ref) || !/^[0-9a-f]{64}$/.test(ci.subject_digest||'') || !nonemptyRefArray(ci.subject_scope) || ci.frozen_at_state_revision===null) f.push('release.eligibility:frozen-candidate-digest-scope-required');
    if (!nonEmptyString(e.candidate_ref) || e.candidate_ref!==ci.subject_ref) f.push('release.eligibility:candidate-mismatch');
    if (!nonEmptyString(e.environment_ref) || !nonEmptyString(e.scope_ref) || !ci.subject_scope?.includes(e.scope_ref)) f.push('release.eligibility:environment-scope-required');
    if (!nonemptyRefArray(e.evidence_refs)) f.push('release.eligibility:evidence-required');
    if (!nonEmptyString(e.decision_ref) || !validInstant(e.decided_at)) f.push('release.eligibility:decision-required');
    if (!nonEmptyString(e.valid_until) && !nonEmptyString(e.freshness_ref)) f.push('release.eligibility:freshness-required');
    if (e.valid_until!==null && (!validInstant(e.valid_until) || (validInstant(now) && Date.parse(e.valid_until)<=Date.parse(now)))) f.push('release.eligibility:expired-or-invalid');
    if (validInstant(e.decided_at) && validInstant(now) && Date.parse(e.decided_at)>Date.parse(now)) f.push('release.eligibility:future-decision');
    if (validInstant(e.decided_at) && validInstant(e.valid_until) && Date.parse(e.valid_until)<=Date.parse(e.decided_at)) f.push('release.eligibility:date-order');
  }
  const a=rel.deployment_authorization;
  if (!['NONE','AUTHORIZED','REVOKED','EXPIRED','CONSUMED'].includes(a.status)) f.push('deployment_authorization:status');
  // Only ACTIVE project authority can assert a current release or live grant.
  // STAGED is prepared but not activated; INACTIVE is no longer active; UNBOUND has no bound authority.
  if (state.activation!=='ACTIVE') {
    if (e.status==='RELEASE_ELIGIBLE') f.push('activation:current-release-requires-ACTIVE');
    if (a.status==='AUTHORIZED') f.push('activation:current-authorization-requires-ACTIVE');
  }
  for (const k of ['grant_ref','candidate_ref','environment_ref','scope_ref','action','granted_at','valid_until','freshness_ref','revoked_at']) if (!isStringOrNull(a[k])) f.push(`deployment_authorization:${k}`);
  if (a.status==='NONE') {
    for (const k of ['grant_ref','candidate_ref','environment_ref','scope_ref','action','granted_at','valid_until','freshness_ref','revoked_at']) if (a[k]!==null) f.push(`deployment_authorization:none-has-${k}`);
  } else if (a.status==='AUTHORIZED') {
    if (e.status!=='RELEASE_ELIGIBLE') f.push('deployment_authorization:requires-current-eligibility');
    if (!nonEmptyString(a.grant_ref) || !nonEmptyString(a.action) || !validInstant(a.granted_at)) f.push('deployment_authorization:grant-action-time-required');
    if (!nonEmptyString(a.candidate_ref) || !nonEmptyString(a.environment_ref) || !nonEmptyString(a.scope_ref) || a.candidate_ref!==e.candidate_ref || a.environment_ref!==e.environment_ref || a.scope_ref!==e.scope_ref) f.push('deployment_authorization:candidate-environment-scope-drift');
    if (!nonEmptyString(a.valid_until) && !nonEmptyString(a.freshness_ref)) f.push('deployment_authorization:freshness-required');
    if (a.valid_until!==null && (!validInstant(a.valid_until) || (validInstant(now) && Date.parse(a.valid_until)<=Date.parse(now)))) f.push('deployment_authorization:expired-or-invalid');
    if (validInstant(a.granted_at) && validInstant(now) && Date.parse(a.granted_at)>Date.parse(now)) f.push('deployment_authorization:future-grant');
    if (validInstant(a.granted_at) && validInstant(a.valid_until) && Date.parse(a.valid_until)<=Date.parse(a.granted_at)) f.push('deployment_authorization:date-order');
    if (a.revoked_at!==null) f.push('deployment_authorization:authorized-but-revoked');
  }
  return [...new Set(f)];
}

// BOUND READINESS: no local state record or source-template PASS proves real
// dependencies, reviewer identity, evidence, required gate inventory or absence
// of remote blockers. The supplied runtime is a PROJECT-BOUND TRUST ANCHOR.
export async function validateBoundReleaseReadiness(state, runtime) {
  const failures=validateReleaseState(state,{now:runtime?.trustedNow});
  if (!runtime || !validInstant(runtime.trustedNow)) failures.push('readiness:trusted-clock-required');
  if (!runtime || typeof runtime.verifyAuthoritativeReadiness!=='function') failures.push('readiness:trusted-adapter-required');
  if (state?.release?.eligibility?.status!=='RELEASE_ELIGIBLE') failures.push('readiness:not-release-eligible');
  if (failures.length) return [...new Set(failures)];
  try {
    const receipt=await runtime.verifyAuthoritativeReadiness({
      state_revision:state.revision,
      candidate_ref:state.candidate_identity.subject_ref,
      subject_digest:state.candidate_identity.subject_digest,
      environment_ref:state.release.eligibility.environment_ref,
      scope_ref:state.release.eligibility.scope_ref,
      evidence_refs:state.release.eligibility.evidence_refs,
      gate_names:Object.keys(state.hard_gates),
      decision_ref:state.release.eligibility.decision_ref,
      now:runtime.trustedNow
    });
    if (!receipt || receipt.ready!==true || receipt.state_revision!==state.revision ||
      receipt.candidate_ref!==state.candidate_identity.subject_ref ||
      receipt.subject_digest!==state.candidate_identity.subject_digest ||
      receipt.environment_ref!==state.release.eligibility.environment_ref ||
      receipt.scope_ref!==state.release.eligibility.scope_ref ||
      receipt.hard_gates_verified!==true || receipt.blockers_clear!==true ||
      receipt.dependencies_verified!==true || receipt.required_review_verified!==true ||
      receipt.evidence_verified!==true || !nonEmptyString(receipt.receipt_ref))
      failures.push('readiness:authoritative-readiness-not-confirmed');
  } catch { failures.push('readiness:authoritative-readiness-failed'); }
  return [...new Set(failures)];
}

// Deliberately does NOT return [] as a live-effect authorization. Legacy callers
// cannot turn a preflight shape/receipt check into permission to deploy.
export async function validateLiveDeploymentAuthorization() {
  return ['live:preflight-only-use-atomic-effect-boundary'];
}

// PROJECT-BOUND EFFECT BOUNDARY: invokes a trusted adapter which must re-read
// actual immutable artifact bytes/digest INSIDE the atomic effect, check the
// authoritative grant (time/revocation/scope/action), consume one-shot grants,
// apply the effect idempotently and durably record the execution receipt.
// This generic package cannot independently establish adapter trust or atomicity.
export async function executeAuthorizedDeployment(state, request, runtime) {
  const failures=await validateBoundReleaseReadiness(state,runtime);
  if (!request || !nonEmptyString(request.candidate_ref) ||
    !nonEmptyString(request.environment_ref) || !nonEmptyString(request.scope_ref) ||
    !nonEmptyString(request.action) || !exactSha(request.artifact_digest)) failures.push('effect:exact-request-and-artifact-digest-required');
  const grant=state?.release?.deployment_authorization;
  if (!grant || grant.status!=='AUTHORIZED') failures.push('effect:no-current-grant');
  if (!runtime || typeof runtime.authorizeAndExecute!=='function') failures.push('effect:trusted-atomic-effect-adapter-required');
  if (!failures.length) {
    for (const k of ['candidate_ref','environment_ref','scope_ref','action'])
      if (request[k]!==grant[k]) failures.push(`effect:${k}-mismatch`);
    if (request.artifact_digest!==state.candidate_identity.subject_digest) failures.push('effect:artifact-candidate-digest-mismatch');
  }
  if (failures.length) return {ok:false, failures:[...new Set(failures)], receipt:null};
  try {
    const receipt=await runtime.authorizeAndExecute({grant_ref:grant.grant_ref,request,
      frozen_subject_digest:state.candidate_identity.subject_digest,
      state_revision:state.revision,now:runtime.trustedNow});
    if (!receipt || receipt.applied!==true || receipt.grant_consumed!==true ||
      receipt.durable!==true || receipt.exact_artifact_verified_at_effect!==true ||
      !nonEmptyString(receipt.operation_ref) || !nonEmptyString(receipt.receipt_ref) ||
      receipt.grant_ref!==grant.grant_ref ||
      receipt.artifact_digest!==request.artifact_digest ||
      receipt.candidate_ref!==request.candidate_ref ||
      receipt.environment_ref!==request.environment_ref ||
      receipt.scope_ref!==request.scope_ref || receipt.action!==request.action)
      return {ok:false,failures:['effect:atomic-execution-not-confirmed'],receipt:null};
    return {ok:true,failures:[],receipt};
  } catch {return {ok:false,failures:['effect:trusted-atomic-execution-failed-or-uncertain-reconcile-before-retry'],receipt:null};}
}

export function validateSourceTemplate(state) {
  const f=validateReleaseState(state);
  if (!state || typeof state!=='object' || Array.isArray(state)) return ['source-state:object-required'];
  const requiredTop=['schema_version','revision','activation','project','governance_binding','coordination','candidate_identity','current_objective','objectives','capabilities','external_systems','hard_gates','evidence_refs','negative_history_refs','regression_protection_refs','operational_diagnostics_refs','blockers','known_risks','reserved_actions','release','last_verified_checkpoint','overhead','views','lifecycle_review_refs'];
  if (JSON.stringify(Object.keys(state).sort())!==JSON.stringify([...requiredTop].sort())) f.push('source-state:required-top-fields');
  // The DISTRIBUTION source is an exact UNBOUND contract. Project-bound extensions
  // belong in reviewed delegated sources, not in implicit source-template authority.
  const exactKeys=(obj, keys, name) => {
    if (!obj || typeof obj!=='object' || Array.isArray(obj)) {f.push(`source-state:${name}:object-required`);return;}
    for (const key of Object.keys(obj)) if (!keys.includes(key)) f.push(`source-state:${name}:unexpected:${key}`);
    for (const key of keys) if (!Object.hasOwn(obj,key)) f.push(`source-state:${name}:missing:${key}`);
  };
  const strictGroups={
    project:['id','root','head','dirty'],
    governance_binding:['active_version','proposed_version','source_manifest_ref','project_binding_ref','evidence_companion_ref','migration_receipt_ref'],
    coordination:['state_writer','serialization_method','last_expected_revision','last_updated_at','active_contract','execution_envelope_ref','last_handoff_ref'],
    candidate_identity:['subject_ref','subject_digest','subject_scope','frozen_at_state_revision'],
    release:['eligibility','deployment_authorization','deployment_observations'],
    eligibility:['status','candidate_ref','environment_ref','scope_ref','evidence_refs','decision_ref','decided_at','valid_until','freshness_ref','reason'],
    deployment_authorization:['status','grant_ref','candidate_ref','environment_ref','scope_ref','action','granted_at','valid_until','freshness_ref','revoked_at'],
    overhead:['measurement','last_sampled_at','notes'],
    views:['last_validated_revision','evidence_refs']
  };
  for (const [group,keys] of Object.entries(strictGroups)) {
    const obj=group==='eligibility'?state.release?.eligibility:group==='deployment_authorization'?state.release?.deployment_authorization:state[group];
    exactKeys(obj,keys,group);
  }
  if (state.schema_version!==SUPPORTED.version) f.push('source-state:schema-version');
  if (state.revision!==0 || state.activation!=='UNBOUND') f.push('source-state:revision-activation');
  const nulls={
    project:['id','root','head','dirty'],
    governance_binding:['active_version','source_manifest_ref','project_binding_ref','evidence_companion_ref','migration_receipt_ref'],
    coordination:['state_writer','serialization_method','last_expected_revision','last_updated_at','active_contract','execution_envelope_ref','last_handoff_ref'],
    candidate_identity:['subject_ref','subject_digest','frozen_at_state_revision'],
    releaseEligibility:['candidate_ref','environment_ref','scope_ref','decision_ref','decided_at','valid_until','freshness_ref'],
    deploymentAuthorization:['grant_ref','candidate_ref','environment_ref','scope_ref','action','granted_at','valid_until','freshness_ref','revoked_at'],
    overhead:['last_sampled_at'], views:['last_validated_revision']
  };
  const objects={project:state.project,governance_binding:state.governance_binding,coordination:state.coordination,candidate_identity:state.candidate_identity,releaseEligibility:state.release?.eligibility,deploymentAuthorization:state.release?.deployment_authorization,overhead:state.overhead,views:state.views};
  for (const [group, keys] of Object.entries(nulls)) {
    const o=objects[group];
    if (!o || typeof o!=='object' || Array.isArray(o)) {f.push(`source-state:${group}:object-required`);continue;}
    for (const k of keys) if (!Object.hasOwn(o,k) || o[k]!==null) f.push(`source-state:${group}.${k}:must-be-null`);
  }
  if (state.governance_binding?.proposed_version!==SUPPORTED.version) f.push('source-state:proposed-version');
  if (state.current_objective!==null || state.last_verified_checkpoint!==null) f.push('source-state:current-work-not-unbound');
  const emptyArrays=['objectives','evidence_refs','negative_history_refs','regression_protection_refs','operational_diagnostics_refs','blockers','known_risks','reserved_actions','lifecycle_review_refs'];
  for (const k of emptyArrays) if (!Array.isArray(state[k]) || state[k].length!==0) f.push(`source-state:${k}:must-be-empty-array`);
  for (const k of ['capabilities','external_systems','hard_gates']) if (!state[k] || typeof state[k]!=='object' || Array.isArray(state[k]) || Object.keys(state[k]).length!==0) f.push(`source-state:${k}:must-be-empty-object`);
  if (!Array.isArray(state.candidate_identity?.subject_scope) || state.candidate_identity.subject_scope.length!==0) f.push('source-state:subject-scope');
  const e=state.release?.eligibility,a=state.release?.deployment_authorization;
  if (!e || e.status!=='NO-GO' || e.reason!=='PROJECT_NOT_BOUND_OR_VERIFIED' || !Array.isArray(e.evidence_refs) || e.evidence_refs.length!==0) f.push('source-state:eligibility-not-default');
  if (!a || a.status!=='NONE') f.push('source-state:deployment-not-default');
  if (!Array.isArray(state.release?.deployment_observations) || state.release.deployment_observations.length!==0) f.push('source-state:deployment-observations-not-empty');
  if (!state.overhead || state.overhead.measurement!=='UNKNOWN' || !Array.isArray(state.overhead.notes) || state.overhead.notes.length!==0) f.push('source-state:overhead-not-default');
  if (!state.views || !Array.isArray(state.views.evidence_refs) || state.views.evidence_refs.length!==0) f.push('source-state:views-not-default');
  return [...new Set(f)];
}

const indRank = {IND0:0, IND1:1, IND2:2, IND3:3};
export function validateRoleCombination(cfg) {
  const f=[];
  if (!cfg || typeof cfg!=='object') return ['roles:config-object-required'];
  const {risk,changeClass,mode,writerId,reviewerId=null,acceptorId=null,reviewerIndependence='IND0',projectAllowsLowRiskR1Self=false,reversibleLowBlast=false,combinedReviewerAcceptorAllowed=false,touchesConsequentialBoundary=false}=cfg;
  const classes=['PRODUCT','GOVERNANCE','VALIDATOR','APPROVAL_CONTROL','RELEASE_CONTROL'];
  if (!classes.includes(changeClass)) f.push('roles:unknown-change-class');
  // A caller-provided class and ID are claims, not an authenticated classifier/identity.
  const special=classes.slice(1).includes(changeClass);
  if (!['R0','R1','R2','R3'].includes(risk)) f.push('roles:risk');
  if (!nonEmptyString(writerId)) f.push('roles:writer');
  if (!Object.hasOwn(indRank,reviewerIndependence)) f.push('roles:independence');
  const rank=indRank[reviewerIndependence]??-1;
  if (special || risk==='R3') {
    if (mode!=='THREE_ROLE') f.push('roles:three-role-required');
  } else if (risk==='R2' && !['REVIEW_ACCEPT','THREE_ROLE'].includes(mode)) f.push('roles:R2-review-required');
  else if (['R0','R1'].includes(risk) && !['SELF_CHECKED','REVIEW_ACCEPT','THREE_ROLE'].includes(mode)) f.push('roles:mode');
  if (mode==='SELF_CHECKED') {
    if (reviewerId!==null || acceptorId!==null) f.push('roles:self-has-extraneous-review-identities');
    if (special || risk==='R2' || risk==='R3') f.push('roles:independent-review-required');
    if (risk==='R1' && (!projectAllowsLowRiskR1Self || !reversibleLowBlast || touchesConsequentialBoundary)) f.push('roles:R1-self-path-not-authorized');
  } else if (mode==='REVIEW_ACCEPT') {
    if (!nonEmptyString(reviewerId) || writerId===reviewerId) f.push('roles:independent-reviewer-required');
    if (!nonEmptyString(acceptorId) || acceptorId!==reviewerId || !combinedReviewerAcceptorAllowed) f.push('roles:combined-role-not-authorized');
    if (rank<(risk==='R2'?2:1)) f.push('roles:review-independence-too-low');
    if (special || risk==='R3') f.push('roles:three-role-required');
  } else if (mode==='THREE_ROLE') {
    if (!nonEmptyString(reviewerId) || !nonEmptyString(acceptorId) || writerId===reviewerId || writerId===acceptorId || reviewerId===acceptorId) f.push('roles:distinct-three-role-required');
    if (rank<(special || risk==='R3' || risk==='R2'?2:1)) f.push('roles:review-independence-too-low');
  }
  return [...new Set(f)];
}

function safeManifestRel(rel) {
  if (!nonEmptyString(rel) || rel.includes('\0') || rel.includes('\\')) return false;
  if (path.posix.isAbsolute(rel) || path.win32.isAbsolute(rel)) return false;
  const norm = path.posix.normalize(rel);
  if (norm !== rel || norm === '..' || norm.startsWith('../') || rel.split('/').some(x => !x || x === '.' || x === '..')) return false;
  return true;
}

function listDistributionFiles(root, failures) {
  const out = [];
  const walk = dir => {
    for (const ent of fs.readdirSync(dir, {withFileTypes:true})) {
      const abs = path.join(dir, ent.name);
      const rel = path.relative(root, abs).split(path.sep).join('/');
      const lst = fs.lstatSync(abs);
      if (lst.isSymbolicLink()) { failures.push(`symlink:${rel}`); continue; }
      if (lst.isDirectory()) {
        if (!['governance','tools'].includes(rel)) failures.push(`inventory:unexpected-directory:${rel}`);
        walk(abs);
      }
      else if (lst.isFile()) out.push(rel);
      else failures.push(`unsupported-file-type:${rel}`);
    }
  };
  walk(root);
  return out.sort();
}

const neutralityPatterns = [
  {name:'windows-absolute', rx:/\b[A-Za-z]:[\\/][^\r\n<>"|]+/},
  {name:'posix-home', rx:/(?:^|[\s`'"(])\/(?:Users|home|mnt)\/[^\s`'"<>]+/m},
  {name:'localhost-port', rx:/(?:localhost|127\.0\.0\.1):\d{2,5}/i}
];

export function verifyPackage(root) {
  const failures = [];
  if (typeof root!=='string' || !fs.existsSync(root) || !fs.statSync(root).isDirectory()) return {ok:false,failures:['package-root:directory-required']};
  const manifestPath = path.join(root, 'PACKAGE_MANIFEST.json');
  if (!fs.existsSync(manifestPath)) return {ok:false, failures:['manifest:missing']};
  let manifest;
  try { manifest = parseStrictJson(fs.readFileSync(manifestPath,'utf8'), 'PACKAGE_MANIFEST.json'); }
  catch (e) { return {ok:false, failures:[`manifest:parse:${e.message}`]}; }

  if (!manifest || typeof manifest!=='object' || Array.isArray(manifest)) return {ok:false,failures:['manifest:object-required']};
  const topKeys = Object.keys(manifest).sort();
  const expectedTop = ['active_authorities','files','manifest_schema','package','version'].sort();
  if (JSON.stringify(topKeys) !== JSON.stringify(expectedTop)) failures.push('manifest:top-level-schema');
  if (manifest.manifest_schema !== SUPPORTED.manifestSchema) failures.push('manifest:schema');
  if (manifest.package !== SUPPORTED.package) failures.push('manifest:package');
  if (manifest.version !== SUPPORTED.version) failures.push('manifest:version');
  if (!Array.isArray(manifest.active_authorities) || JSON.stringify(manifest.active_authorities) !== JSON.stringify(SUPPORTED.activeAuthorities)) failures.push('manifest:active-authorities');
  if (!manifest.files || typeof manifest.files !== 'object' || Array.isArray(manifest.files)) failures.push('manifest:files-object');

  const declared = manifest.files && typeof manifest.files === 'object' && !Array.isArray(manifest.files) ? Object.keys(manifest.files).sort() : [];
  const expectedPayloads = [...SUPPORTED.payloads].sort();
  if (JSON.stringify(declared) !== JSON.stringify(expectedPayloads)) failures.push('manifest:required-payload-set');
  for (const rel of declared) {
    if (!safeManifestRel(rel)) { failures.push(`manifest:unsafe-path:${rel}`); continue; }
    const digest = manifest.files[rel];
    if (typeof digest !== 'string' || !/^[0-9a-f]{64}$/.test(digest)) failures.push(`manifest:invalid-digest:${rel}`);
  }

  const actual = listDistributionFiles(root, failures).filter(x => x !== 'PACKAGE_MANIFEST.json');
  if (JSON.stringify(actual) !== JSON.stringify(expectedPayloads)) {
    for (const x of expectedPayloads) if (!actual.includes(x)) failures.push(`inventory:missing:${x}`);
    for (const x of actual) if (!expectedPayloads.includes(x)) failures.push(`inventory:unexpected:${x}`);
  }

  const rootReal = fs.realpathSync(root);
  for (const rel of expectedPayloads) {
    if (!safeManifestRel(rel)) continue;
    const abs = path.resolve(root, ...rel.split('/'));
    if (!fs.existsSync(abs)) continue;
    const lst = fs.lstatSync(abs);
    if (lst.isSymbolicLink()) { failures.push(`payload:symlink:${rel}`); continue; }
    const real = fs.realpathSync(abs);
    if (!(real === rootReal || real.startsWith(rootReal + path.sep))) failures.push(`payload:escape:${rel}`);
    if (manifest.files && /^[0-9a-f]{64}$/.test(manifest.files[rel] || '') && sha256File(abs) !== manifest.files[rel]) failures.push(`hash:${rel}`);
  }

  const statePath = path.join(root, 'governance/PROJECT_STATE.yaml');
  let state;
  try { state = parseStrictJson(fs.readFileSync(statePath,'utf8'), 'PROJECT_STATE.yaml'); }
  catch (e) { failures.push(`source-state:parse:${e.message}`); }
  if (state) failures.push(...validateSourceTemplate(state));

  const govDir = path.join(root, 'governance');
  if (fs.existsSync(govDir)) {
    const active = fs.readdirSync(govDir).filter(x => fs.lstatSync(path.join(govDir,x)).isFile()).sort();
    const names = SUPPORTED.activeAuthorities.map(x => path.posix.basename(x)).sort();
    if (JSON.stringify(active) !== JSON.stringify(names)) failures.push(`active-authorities:${active.join(',')}`);
  }

  for (const rel of expectedPayloads.filter(x => /\.(md|yaml|yml|json|mjs)$/.test(x) && x !== 'tools/test-verify-package.mjs')) {
    const abs = path.join(root, ...rel.split('/'));
    if (!fs.existsSync(abs)) continue;
    const txt = fs.readFileSync(abs,'utf8');
    for (const {name,rx} of neutralityPatterns) if (rx.test(txt)) failures.push(`neutrality-limited:${name}:${rel}`);
  }

  return {ok: failures.length===0, failures:[...new Set(failures)]};
}

function main() {
  const here = path.dirname(fileURLToPath(import.meta.url));
  const root = path.resolve(here, '..');
  const args = process.argv.slice(2);
  if (args[0] === '--validate-state') {
    const p = path.resolve(args[1] || '');
    try {
      const state = parseStrictJson(fs.readFileSync(p,'utf8'), p);
      const failures = validateReleaseState(state);
      if (failures.length) { console.error('STATE_CONTRACT_FAIL'); failures.forEach(x=>console.error(x)); process.exit(1); }
      console.log('STATE_SHAPE_AND_CONSISTENCY_PASS live_authorization=NOT_PROVEN');
      return;
    } catch (e) { console.error('STATE_CONTRACT_FAIL'); console.error(e.message); process.exit(1); }
  }
  const result = verifyPackage(root);
  if (!result.ok) {
    console.error('PACKAGE_VERIFY_FAIL');
    result.failures.forEach(x=>console.error(x));
    process.exit(1);
  }
  console.log(`PACKAGE_VERIFY_PASS package=${SUPPORTED.package} version=${SUPPORTED.version} files=${SUPPORTED.payloads.length} active_authorities=3`);
  console.log('SOURCE_TEMPLATE_SEMANTICS_PASS strict_json_compatible_yaml=true duplicate_keys_rejected=true');
  console.log('NEUTRALITY_SCAN_PASS_LIMITED manual_semantic_review_still_required=true');
  console.log('PUBLISHER_AUTHENTICITY=NOT_PROVEN');
  console.log('PROJECT_CONFORMANCE=NOT_PROVEN');
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) main();
