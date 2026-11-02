import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { fileURLToPath, pathToFileURL } from 'url';

export const SUPPORTED = Object.freeze({
  manifestSchema: 'UGM-PACKAGE-MANIFEST-1',
  package: 'UNIVERSAL_GOVERNANCE_MINIMAL',
  version: '4.1.0-r3',
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
    'tools/verify-package.mjs',
    'tools/autonomy-engine.mjs',
    'tools/test-autonomy-engine.mjs',
    'AUTONOMY_RUNTIME.md'
  ],
  adoptionModes: ['NEW_PROJECT', 'MID_PROJECT_UNGOVERNED', 'MIGRATION_GOVERNED'],
  productArchetypes: [
    'WEB_APP', 'MOBILE_IOS', 'DESKTOP_CAD_BIM', 'CLI_TOOL', 'API_SERVICE',
    'DISTRIBUTED_SYSTEM', 'EMBEDDED_EDGE', 'DATA_ML_PIPELINE',
    'AUTONOMOUS_AGENT_SWARM', 'LIBRARY_SDK'
  ],
  paradigms: [
    'FUNCTIONAL', 'OOP', 'PROCEDURAL', 'DECLARATIVE_UI', 'REACTIVE_STREAM',
    'EVENT_DRIVEN', 'ACTOR_MODEL', 'DATA_ORIENTED', 'RELATIONAL_LOGIC'
  ],
  specStatuses: ['UNVERIFIED', 'BLOCKED_MISSING_SPEC', 'SPEC_VERIFIED'],
  diagramStatuses: ['UNVERIFIED', 'DIAGRAM_PENDING', 'DIAGRAM_LOCKED', 'DIAGRAM_DRIFT'],
  autonomyPhases: ['IDLE','DISCOVER','SPECIFY','STANDARDS','DIAGRAM','IMPLEMENT','TEST','REVIEW','ACCEPT','RECORD','EVOLVE','BLOCKED','RECONCILE'],
  autonomyModes: ['DISABLED','BOUNDED']
});

export function sha256File(p) {
  return crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
}

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
    const obj = Object.create(null); // JSON object keys, including __proto__, never mutate the prototype
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
  const m = v.match(/^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})/);
  if (!m || Number(m[2]) < 1 || Number(m[2]) > 12 || Number(m[3]) < 1 || Number(m[3]) > new Date(Date.UTC(Number(m[1]), Number(m[2]), 0)).getUTCDate()) return false;
  if (Number(m[4]) > 23 || Number(m[5]) > 59 || Number(m[6]) > 59) return false;
  const off = v.match(/([+-])(\d{2}):(\d{2})$/);
  if (off && (Number(off[2]) > 23 || Number(off[3]) > 59)) return false;
  return true;
}
function validRefArray(v) { return Array.isArray(v) && v.every(nonEmptyString); }
function nonemptyRefArray(v) { return validRefArray(v) && v.length > 0 && new Set(v).size === v.length; }

export function validateReleaseState(state, {now = new Date().toISOString()} = {}) {
  const f = [];
  if (!validInstant(now)) f.push('state:invalid-now');
  requireObject(state, 'state', f);
  if (f.length) return f;
  if (!Number.isInteger(state.revision) || state.revision < 0) f.push('state:revision');
  if (!validRefArray(state.lifecycle_review_refs)) f.push('state:lifecycle-review-refs');

  // Autonomy is disabled in source templates. Runtime execution needs an ACTIVE
  // bound project, a trusted host and its own authenticated admission gates.
  const auto = state.autonomy;
  requireObject(auto, 'autonomy', f);
  if (auto && typeof auto === 'object' && !Array.isArray(auto)) {
    for (const key of ['enabled','mode','phase','objective_ref','subject_scope','lease_ref','budget_ref','last_receipt_ref','last_failure_ref','retry_count','max_retries','last_reconciled_revision','review_receipt_ref','review_subject_digest']) {
      if (!Object.hasOwn(auto,key)) f.push(`autonomy:missing-${key}`);
    }
    if (typeof auto.enabled !== 'boolean' || !SUPPORTED.autonomyModes.includes(auto.mode) || !SUPPORTED.autonomyPhases.includes(auto.phase)) f.push('autonomy:invalid-mode-phase-or-enable');
    for (const k of ['objective_ref','subject_scope','lease_ref','budget_ref','last_receipt_ref','last_failure_ref','review_receipt_ref']) if (!isStringOrNull(auto[k])) f.push(`autonomy:${k}:invalid`);
    if (!validSha(auto.review_subject_digest)) f.push('autonomy:invalid-review-digest');
    if (!Number.isInteger(auto.retry_count) || auto.retry_count<0 || !Number.isInteger(auto.max_retries) || auto.max_retries<0 || auto.retry_count>auto.max_retries) f.push('autonomy:invalid-retry-bounds');
    if (!(auto.last_reconciled_revision===null || (Number.isInteger(auto.last_reconciled_revision) && auto.last_reconciled_revision>=0 && auto.last_reconciled_revision<=state.revision))) f.push('autonomy:invalid-last-reconciled-revision');
    if (auto.enabled && (auto.mode!=='BOUNDED' || state.activation!=='ACTIVE' || !nonEmptyString(auto.budget_ref))) f.push('autonomy:bound-execution-prerequisites');
    if (!auto.enabled && auto.mode!=='DISABLED') f.push('autonomy:disabled-mode-required');
    if (auto.enabled && auto.phase!=='IDLE' && (!nonEmptyString(auto.objective_ref) || !nonEmptyString(auto.subject_scope))) f.push('autonomy:active-phase-scope-and-objective-required');
    if (auto.enabled && auto.phase!=='IDLE' && !state.candidate_identity?.subject_scope?.includes(auto.subject_scope)) f.push('autonomy:phase-scope-not-frozen');
    // No post-diagram phase may inherit a different objective's spec/diagram lock.
    if (auto.enabled && ['IMPLEMENT','TEST','REVIEW','ACCEPT','RECORD','EVOLVE'].includes(auto.phase)) {
      if (state.specification_gate?.subject_scope_ref !== auto.subject_scope || state.specification_gate?.diagram_lock_subject_digest !== state.candidate_identity?.subject_digest) f.push('autonomy:post-diagram-phase-scope-or-digest-mismatch');
    }
  }

  if (!Array.isArray(state.required_hard_gates) || !state.required_hard_gates.every(nonEmptyString)) f.push('state:required-hard-gates-array-required');
  if (!state.hard_gates || typeof state.hard_gates !== 'object' || Array.isArray(state.hard_gates)) f.push('state:hard-gates-object-required');
  if (!Array.isArray(state.blockers)) f.push('state:blockers-array-required');
  if (!['UNBOUND','STAGED','ACTIVE','INACTIVE'].includes(state.activation)) f.push('state:activation');
  if (state.schema_version !== SUPPORTED.version) f.push('state:schema-version-mismatch');

  requireObject(state.project, 'project', f);
  requireObject(state.coordination, 'coordination', f);
  requireObject(state.specification_gate, 'specification_gate', f);
  requireObject(state.candidate_identity, 'candidate_identity', f);
  requireObject(state.release, 'release', f);
  if (f.length) return f;

  // Project archetype, adoption_mode, and active_paradigms validation
  const prj = state.project;
  if (prj.adoption_mode !== null && !SUPPORTED.adoptionModes.includes(prj.adoption_mode)) f.push('project:invalid-adoption-mode');
  if (prj.product_archetype !== null && !SUPPORTED.productArchetypes.includes(prj.product_archetype)) f.push('project:invalid-product-archetype');
  if (!Array.isArray(prj.active_paradigms) || !prj.active_paradigms.every(p => SUPPORTED.paradigms.includes(p)) || (Array.isArray(prj.active_paradigms) && new Set(prj.active_paradigms).size !== prj.active_paradigms.length)) f.push('project:invalid-active-paradigms');
  if (state.activation === 'ACTIVE' && (!SUPPORTED.adoptionModes.includes(prj.adoption_mode) || !SUPPORTED.productArchetypes.includes(prj.product_archetype) || !Array.isArray(prj.active_paradigms) || !prj.active_paradigms.length)) f.push('project:active-project-requires-archetype-mode-paradigm');
  if (state.activation === 'ACTIVE' && (!nonEmptyString(prj.id) || !nonEmptyString(prj.root))) f.push('project:active-project-identity-root-required');
  if (state.activation === 'ACTIVE' && (state.governance_binding?.active_version !== SUPPORTED.version || !nonEmptyString(state.governance_binding?.project_binding_ref))) f.push('governance_binding:active-project-authority-binding-required');

  // Specification Gate & Diagram-First validation
  const sg = state.specification_gate;
  requireObject(sg.dimension_refs, 'specification_gate.dimension_refs', f);
  if (!validRefArray(sg.diagram_refs)) f.push('specification_gate:invalid-diagram-refs');
  if (!isStringOrNull(sg.diagram_approval_ref)) f.push('specification_gate:invalid-diagram-approval');
  if (!validSha(sg.diagram_lock_subject_digest)) f.push('specification_gate:invalid-diagram-lock-digest');
  if (!isStringOrNull(sg.subject_scope_ref)) f.push('specification_gate:invalid-locked-subject-scope');
  const specDimensions = ['intent_actors','data_interfaces','paradigm_boundaries','diagrams','relative_standards','acceptance_negative'];
  if (sg.dimension_refs && typeof sg.dimension_refs === 'object' && !Array.isArray(sg.dimension_refs)) {
    if (JSON.stringify(Object.keys(sg.dimension_refs).sort()) !== JSON.stringify([...specDimensions].sort())) f.push('specification_gate:wrong-dimension-keys');
    for (const k of specDimensions) if (!isStringOrNull(sg.dimension_refs[k])) f.push(`specification_gate:dimension-${k}-invalid`);
  }
  if (sg.status === 'SPEC_VERIFIED') {
    for (const k of specDimensions) if (!nonEmptyString(sg.dimension_refs?.[k])) f.push(`specification_gate:missing-dimension-${k}`);
    if (!nonemptyRefArray(sg.relative_search_refs)) f.push('specification_gate:standards-search-required');
    if (sg.diagram_first_status !== 'DIAGRAM_LOCKED') f.push('specification_gate:requires-locked-diagrams');
    if (!nonemptyRefArray(sg.diagram_refs) || !nonEmptyString(sg.diagram_approval_ref) || !exactSha(sg.diagram_lock_subject_digest)) f.push('specification_gate:approved-diagram-lock-required');
    if (!nonEmptyString(sg.subject_scope_ref) || !state.candidate_identity?.subject_scope?.includes(sg.subject_scope_ref)) f.push('specification_gate:approved-scope-binding-required');
  }
  // The Super-Agent control actors must be distinct from the three technical roles on bound task assignments.
  const assignment = state.coordination?.active_role_assignment;
  if (assignment && typeof assignment === 'object' && !Array.isArray(assignment)) {
    for (const k of ['worker_id','reviewer_id','acceptor_id','router_id','watchdog_id']) if (!isStringOrNull(assignment[k])) f.push(`coordination:role-${k}-invalid`);
    const used = ['worker_id','reviewer_id','acceptor_id','router_id','watchdog_id'].map(k=>assignment[k]).filter(nonEmptyString);
    if (new Set(used).size !== used.length) f.push('coordination:roles-must-be-distinct');
    if (assignment.reviewer_independence !== null && !['IND2','IND3'].includes(assignment.reviewer_independence)) f.push('coordination:reviewer-independence-insufficient');
    if (state.activation === 'ACTIVE' && (state.current_objective !== null || state.autonomy?.enabled === true || state.release?.eligibility?.status === 'RELEASE_ELIGIBLE')) {
      if (used.length !== 5 || !['IND2','IND3'].includes(assignment.reviewer_independence)) f.push('coordination:complete-strict-five-actor-binding-required');
    }
  }
  
  if (sg.missing_kind!==null&&!['TECHNICAL','OWNER_INTENT','MIXED'].includes(sg.missing_kind)) f.push('specification_gate:invalid-missing-kind');
  if (sg.status==='BLOCKED_MISSING_SPEC' && !['TECHNICAL','OWNER_INTENT','MIXED'].includes(sg.missing_kind)) f.push('specification_gate:missing-kind-classification-required');
  if (sg.status==='SPEC_VERIFIED' && sg.missing_kind!==null) f.push('specification_gate:verified-cannot-have-unresolved-missing-kind');
  if (!SUPPORTED.specStatuses.includes(sg.status)) f.push('specification_gate:invalid-status');
  if (!validRefArray(sg.missing_specification_prompts)) f.push('specification_gate:invalid-missing-prompts');
  if (!SUPPORTED.diagramStatuses.includes(sg.diagram_first_status)) f.push('specification_gate:invalid-diagram-status');
  if (!validRefArray(sg.relative_search_refs)) f.push('specification_gate:invalid-relative-search-refs');
  if (sg.status === 'BLOCKED_MISSING_SPEC' && Array.isArray(sg.missing_specification_prompts) && sg.missing_specification_prompts.length === 0) {
    f.push('specification_gate:blocked-requires-missing-specification-prompts');
  }
  if (sg.status === 'SPEC_VERIFIED' && Array.isArray(sg.missing_specification_prompts) && sg.missing_specification_prompts.length > 0) {
    f.push('specification_gate:verified-cannot-have-missing-prompts');
  }

  const ci = state.candidate_identity, rel = state.release;
  if (!isStringOrNull(ci.subject_ref)) f.push('candidate_identity:subject_ref');
  if (!validSha(ci.subject_digest)) f.push('candidate_identity:subject_digest');
  if (!validRefArray(ci.subject_scope)) f.push('candidate_identity:subject_scope');
  if (!(ci.frozen_at_state_revision === null || (Number.isInteger(ci.frozen_at_state_revision) && ci.frozen_at_state_revision >= 0 && ci.frozen_at_state_revision <= state.revision))) f.push('candidate_identity:frozen_at_state_revision');
  requireObject(rel.eligibility, 'release.eligibility', f);
  requireObject(rel.deployment_authorization, 'release.deployment_authorization', f);
  if (!Array.isArray(rel.deployment_observations)) f.push('release.deployment_observations:array-required');
  if (f.length) return f;

  for (const [idx, obs] of rel.deployment_observations.entries()) {
    if (!obs || typeof obs !== 'object' || Array.isArray(obs) || !nonEmptyString(obs.candidate_ref) || !nonEmptyString(obs.environment_ref) || !validInstant(obs.observed_at)) f.push(`release.deployment_observations:${idx}:invalid`);
  }

  const e = rel.eligibility;
  if (!['NO-GO','RELEASE_ELIGIBLE'].includes(e.status)) f.push('release.eligibility:status');
  for (const k of ['candidate_ref','environment_ref','scope_ref','decision_ref','decided_at','valid_until','freshness_ref','reason']) if (!isStringOrNull(e[k])) f.push(`release.eligibility:${k}`);
  if (!validRefArray(e.evidence_refs)) f.push('release.eligibility:evidence_refs');

  if (e.status === 'NO-GO') {
    if (e.candidate_ref !== null || e.environment_ref !== null || e.scope_ref !== null) f.push('release.eligibility:no-go-has-current-grant-subject');
    // F3 repair: validate historical timestamps on NO-GO if non-null
    if (e.decided_at !== null && (!validInstant(e.decided_at) || (validInstant(now) && Date.parse(e.decided_at) > Date.parse(now)))) f.push('release.eligibility:no-go-invalid-or-future-decided_at');
    if (e.valid_until !== null && !validInstant(e.valid_until)) f.push('release.eligibility:no-go-invalid-valid_until');
    if (e.valid_until !== null && e.decided_at === null) f.push('release.eligibility:no-go-valid-until-requires-decided-at');
    if (e.decided_at !== null && e.valid_until !== null && validInstant(e.decided_at) && validInstant(e.valid_until) && Date.parse(e.valid_until) <= Date.parse(e.decided_at)) f.push('release.eligibility:no-go-date-order');
  } else if (e.status === 'RELEASE_ELIGIBLE') {
    // Specification & Diagram-First gates required for RELEASE_ELIGIBLE
    if (sg.status !== 'SPEC_VERIFIED') f.push('release.eligibility:specification-gate-not-verified');
    if (sg.diagram_first_status !== 'DIAGRAM_LOCKED') f.push('release.eligibility:diagram-first-gate-not-locked');
    if (sg.diagram_lock_subject_digest !== ci.subject_digest) f.push('release.eligibility:diagram-lock-subject-digest-mismatch');
    if (sg.subject_scope_ref !== e.scope_ref) f.push('release.eligibility:approved-diagram-scope-mismatch');
    if (!nonEmptyString(sg.diagram_approval_ref) || !nonemptyRefArray(sg.diagram_refs)) f.push('release.eligibility:missing-approved-diagram-references');
    if (!Array.isArray(sg.missing_specification_prompts) || sg.missing_specification_prompts.length > 0) f.push('release.eligibility:unresolved-missing-specification-prompts');

    // F1 repair: require non-empty required_hard_gates inventory and check every required gate
    if (!nonemptyRefArray(state.required_hard_gates)) f.push('release.eligibility:required-hard-gates-inventory-empty');
    if (!state.hard_gates || typeof state.hard_gates !== 'object' || Array.isArray(state.hard_gates) || Object.keys(state.hard_gates).length === 0) f.push('release.eligibility:hard-gates-required');
    else {
      for (const reqGate of (Array.isArray(state.required_hard_gates) ? state.required_hard_gates : [])) {
        if (!Object.hasOwn(state.hard_gates, reqGate)) f.push(`release.eligibility:missing-required-hard-gate:${reqGate}`);
      }
      for (const [name, gate] of Object.entries(state.hard_gates)) {
        if (!gate || typeof gate !== 'object' || Array.isArray(gate) || !['PASS','NOT_APPLICABLE'].includes(gate.status)) f.push(`release.eligibility:hard-gate-${name}-not-verified`);
        else if (gate.status === 'PASS' && (!nonemptyRefArray(gate.evidence_refs) || gate.subject_digest !== ci.subject_digest)) f.push(`release.eligibility:hard-gate-${name}-evidence-or-candidate`);
        else if (gate.status === 'NOT_APPLICABLE' && !nonEmptyString(gate.reason)) f.push(`release.eligibility:hard-gate-${name}-inapplicability-unjustified`);
      }
    }
    if (!Array.isArray(state.blockers) || state.blockers.length !== 0) f.push('release.eligibility:unresolved-blockers');
    if (!nonEmptyString(ci.subject_ref) || !/^[0-9a-f]{64}$/.test(ci.subject_digest || '') || !nonemptyRefArray(ci.subject_scope) || ci.frozen_at_state_revision === null) f.push('release.eligibility:frozen-candidate-digest-scope-required');
    if (!nonEmptyString(e.candidate_ref) || e.candidate_ref !== ci.subject_ref) f.push('release.eligibility:candidate-mismatch');
    if (!nonEmptyString(e.environment_ref) || !nonEmptyString(e.scope_ref) || !ci.subject_scope?.includes(e.scope_ref)) f.push('release.eligibility:environment-scope-required');
    if (!nonemptyRefArray(e.evidence_refs)) f.push('release.eligibility:evidence-required');
    if (!nonEmptyString(e.decision_ref) || !validInstant(e.decided_at)) f.push('release.eligibility:decision-required');
    if (!nonEmptyString(e.valid_until) && !nonEmptyString(e.freshness_ref)) f.push('release.eligibility:freshness-required');
    if (e.valid_until !== null && (!validInstant(e.valid_until) || (validInstant(now) && Date.parse(e.valid_until) <= Date.parse(now)))) f.push('release.eligibility:expired-or-invalid');
    if (validInstant(e.decided_at) && validInstant(now) && Date.parse(e.decided_at) > Date.parse(now)) f.push('release.eligibility:future-decision');
    if (validInstant(e.decided_at) && validInstant(e.valid_until) && Date.parse(e.valid_until) <= Date.parse(e.decided_at)) f.push('release.eligibility:date-order');
  }

  const a = rel.deployment_authorization;
  if (!['NONE','AUTHORIZED','REVOKED','EXPIRED','CONSUMED'].includes(a.status)) f.push('deployment_authorization:status');
  if (state.activation !== 'ACTIVE') {
    if (e.status === 'RELEASE_ELIGIBLE') f.push('activation:current-release-requires-ACTIVE');
    if (a.status === 'AUTHORIZED') f.push('activation:current-authorization-requires-ACTIVE');
  }
  for (const k of ['grant_ref','candidate_ref','environment_ref','scope_ref','action','granted_at','valid_until','freshness_ref','revoked_at']) if (!isStringOrNull(a[k])) f.push(`deployment_authorization:${k}`);
  if (a.status === 'NONE') {
    for (const k of ['grant_ref','candidate_ref','environment_ref','scope_ref','action','granted_at','valid_until','freshness_ref','revoked_at']) if (a[k] !== null) f.push(`deployment_authorization:none-has-${k}`);
  } else if (a.status === 'AUTHORIZED') {
    if (e.status !== 'RELEASE_ELIGIBLE') f.push('deployment_authorization:requires-current-eligibility');
    if (!nonEmptyString(a.grant_ref) || !nonEmptyString(a.action) || !validInstant(a.granted_at)) f.push('deployment_authorization:grant-action-time-required');
    if (!nonEmptyString(a.candidate_ref) || !nonEmptyString(a.environment_ref) || !nonEmptyString(a.scope_ref) || a.candidate_ref !== e.candidate_ref || a.environment_ref !== e.environment_ref || a.scope_ref !== e.scope_ref) f.push('deployment_authorization:candidate-environment-scope-drift');
    if (!nonEmptyString(a.valid_until) && !nonEmptyString(a.freshness_ref)) f.push('deployment_authorization:freshness-required');
    if (a.valid_until !== null && (!validInstant(a.valid_until) || (validInstant(now) && Date.parse(a.valid_until) <= Date.parse(now)))) f.push('deployment_authorization:expired-or-invalid');
    if (validInstant(a.granted_at) && validInstant(now) && Date.parse(a.granted_at) > Date.parse(now)) f.push('deployment_authorization:future-grant');
    if (validInstant(a.granted_at) && validInstant(a.valid_until) && Date.parse(a.valid_until) <= Date.parse(a.granted_at)) f.push('deployment_authorization:date-order');
    if (a.revoked_at !== null) f.push('deployment_authorization:authorized-but-revoked');
  }
  return [...new Set(f)];
}

export async function validateBoundReleaseReadiness(state, runtime) {
  const failures = validateReleaseState(state, {now: runtime?.trustedNow});
  if (!runtime || !validInstant(runtime.trustedNow)) failures.push('readiness:trusted-clock-required');
  if (!runtime || typeof runtime.verifyAuthoritativeReadiness !== 'function') failures.push('readiness:trusted-adapter-required');
  if (state?.release?.eligibility?.status !== 'RELEASE_ELIGIBLE') failures.push('readiness:not-release-eligible');
  if (failures.length) return [...new Set(failures)];
  try {
    const receipt = await runtime.verifyAuthoritativeReadiness({
      state_revision: state.revision,
      candidate_ref: state.candidate_identity.subject_ref,
      subject_digest: state.candidate_identity.subject_digest,
      environment_ref: state.release.eligibility.environment_ref,
      scope_ref: state.release.eligibility.scope_ref,
      evidence_refs: state.release.eligibility.evidence_refs,
      required_hard_gates: state.required_hard_gates,
      gate_names: Object.keys(state.hard_gates),
      specification_status: state.specification_gate.status,
      diagram_first_status: state.specification_gate.diagram_first_status,
      decision_ref: state.release.eligibility.decision_ref,
      now: runtime.trustedNow
    });
    if (!receipt || receipt.ready !== true || receipt.state_revision !== state.revision ||
      receipt.candidate_ref !== state.candidate_identity.subject_ref ||
      receipt.subject_digest !== state.candidate_identity.subject_digest ||
      receipt.environment_ref !== state.release.eligibility.environment_ref ||
      receipt.scope_ref !== state.release.eligibility.scope_ref ||
      receipt.hard_gates_verified !== true || receipt.blockers_clear !== true ||
      receipt.dependencies_verified !== true || receipt.required_review_verified !== true ||
      receipt.evidence_verified !== true || !nonEmptyString(receipt.receipt_ref))
      failures.push('readiness:authoritative-readiness-not-confirmed');
  } catch { failures.push('readiness:authoritative-readiness-failed'); }
  return [...new Set(failures)];
}

export async function validateLiveDeploymentAuthorization() {
  return ['live:preflight-only-use-atomic-effect-boundary'];
}

export async function executeAuthorizedDeployment(state, request, runtime) {
  const failures = await validateBoundReleaseReadiness(state, runtime);
  if (!request || !nonEmptyString(request.candidate_ref) ||
    !nonEmptyString(request.environment_ref) || !nonEmptyString(request.scope_ref) ||
    !nonEmptyString(request.action) || !exactSha(request.artifact_digest)) failures.push('effect:exact-request-and-artifact-digest-required');
  const grant = state?.release?.deployment_authorization;
  if (!grant || grant.status !== 'AUTHORIZED') failures.push('effect:no-current-grant');
  if (!runtime || typeof runtime.authorizeAndExecute !== 'function') failures.push('effect:trusted-atomic-effect-adapter-required');
  if (!failures.length) {
    for (const k of ['candidate_ref','environment_ref','scope_ref','action'])
      if (request[k] !== grant[k]) failures.push(`effect:${k}-mismatch`);
    if (request.artifact_digest !== state.candidate_identity.subject_digest) failures.push('effect:artifact-candidate-digest-mismatch');
  }
  if (failures.length) return {ok: false, failures: [...new Set(failures)], receipt: null};
  try {
    const receipt = await runtime.authorizeAndExecute({
      grant_ref: grant.grant_ref,
      request,
      frozen_subject_digest: state.candidate_identity.subject_digest,
      state_revision: state.revision,
      now: runtime.trustedNow
    });
    // F2 repair: enforce receipt.state_revision and receipt.frozen_subject_digest echo
    if (!receipt || receipt.applied !== true || receipt.grant_consumed !== true ||
      receipt.durable !== true || receipt.exact_artifact_verified_at_effect !== true ||
      receipt.state_revision !== state.revision ||
      receipt.frozen_subject_digest !== state.candidate_identity.subject_digest ||
      !nonEmptyString(receipt.operation_ref) || !nonEmptyString(receipt.receipt_ref) ||
      receipt.grant_ref !== grant.grant_ref ||
      receipt.artifact_digest !== request.artifact_digest ||
      receipt.candidate_ref !== request.candidate_ref ||
      receipt.environment_ref !== request.environment_ref ||
      receipt.scope_ref !== request.scope_ref || receipt.action !== request.action)
      return {ok: false, failures: ['effect:atomic-execution-not-confirmed'], receipt: null};
    return {ok: true, failures: [], receipt};
  } catch {
    return {ok: false, failures: ['effect:trusted-atomic-execution-failed-or-uncertain-reconcile-before-retry'], receipt: null};
  }
}

export function validateSourceTemplate(state) {
  const f = validateReleaseState(state);
  if (!state || typeof state !== 'object' || Array.isArray(state)) return ['source-state:object-required'];
  const requiredTop = [
    'schema_version','revision','activation','project','governance_binding',
    'coordination','specification_gate','candidate_identity','current_objective',
    'objectives','capabilities','external_systems','required_hard_gates','hard_gates',
    'evidence_refs','negative_history_refs','regression_protection_refs',
    'operational_diagnostics_refs','blockers','known_risks','reserved_actions','autonomy',
    'release','last_verified_checkpoint','overhead','views','lifecycle_review_refs'
  ];
  if (JSON.stringify(Object.keys(state).sort()) !== JSON.stringify([...requiredTop].sort())) f.push('source-state:required-top-fields');

  const exactKeys = (obj, keys, name) => {
    if (!obj || typeof obj !== 'object' || Array.isArray(obj)) { f.push(`source-state:${name}:object-required`); return; }
    for (const key of Object.keys(obj)) if (!keys.includes(key)) f.push(`source-state:${name}:unexpected:${key}`);
    for (const key of keys) if (!Object.hasOwn(obj, key)) f.push(`source-state:${name}:missing:${key}`);
  };
  const strictGroups = {
    project: ['id','root','head','dirty','adoption_mode','product_archetype','active_paradigms'],
    governance_binding: ['active_version','proposed_version','source_manifest_ref','project_binding_ref','evidence_companion_ref','migration_receipt_ref','standards_registry_ref','diagram_registry_ref','ui_philosophy_ref'],
    coordination: ['state_writer','serialization_method','last_expected_revision','last_updated_at','active_contract','execution_envelope_ref','last_handoff_ref','active_role_assignment'],
    active_role_assignment: ['worker_id','reviewer_id','acceptor_id','reviewer_independence','router_id','watchdog_id'],
    specification_gate: ['status','missing_specification_prompts','diagram_first_status','relative_search_refs','dimension_refs','diagram_refs','diagram_approval_ref','diagram_lock_subject_digest','subject_scope_ref','missing_kind'],
    dimension_refs: ['intent_actors','data_interfaces','paradigm_boundaries','diagrams','relative_standards','acceptance_negative'],
    candidate_identity: ['subject_ref','subject_digest','subject_scope','frozen_at_state_revision'],
    release: ['eligibility','deployment_authorization','deployment_observations'],
    eligibility: ['status','candidate_ref','environment_ref','scope_ref','evidence_refs','decision_ref','decided_at','valid_until','freshness_ref','reason'],
    deployment_authorization: ['status','grant_ref','candidate_ref','environment_ref','scope_ref','action','granted_at','valid_until','freshness_ref','revoked_at'],
    overhead: ['measurement','last_sampled_at','notes'],
    views: ['last_validated_revision','evidence_refs'],
    autonomy: ['enabled','mode','phase','objective_ref','subject_scope','lease_ref','budget_ref','last_receipt_ref','last_failure_ref','retry_count','max_retries','last_reconciled_revision','review_receipt_ref','review_subject_digest']
  };
  for (const [group, keys] of Object.entries(strictGroups)) {
    const obj = group === 'eligibility' ? state.release?.eligibility
      : group === 'deployment_authorization' ? state.release?.deployment_authorization
      : group === 'active_role_assignment' ? state.coordination?.active_role_assignment
      : group === 'dimension_refs' ? state.specification_gate?.dimension_refs
      : state[group];
    exactKeys(obj, keys, group);
  }
  if (state.schema_version !== SUPPORTED.version) f.push('source-state:schema-version');
  if (state.revision !== 0 || state.activation !== 'UNBOUND') f.push('source-state:revision-activation');
  const nulls = {
    project: ['id','root','head','dirty','adoption_mode','product_archetype'],
    governance_binding: ['active_version','source_manifest_ref','project_binding_ref','evidence_companion_ref','migration_receipt_ref','standards_registry_ref','diagram_registry_ref','ui_philosophy_ref'],
    coordination: ['state_writer','serialization_method','last_expected_revision','last_updated_at','active_contract','execution_envelope_ref','last_handoff_ref'],
    active_role_assignment: ['worker_id','reviewer_id','acceptor_id','reviewer_independence','router_id','watchdog_id'],
    candidate_identity: ['subject_ref','subject_digest','frozen_at_state_revision'],
    dimension_refs: ['intent_actors','data_interfaces','paradigm_boundaries','diagrams','relative_standards','acceptance_negative'],
    spec_gate: ['diagram_approval_ref','diagram_lock_subject_digest','subject_scope_ref','missing_kind'],
    releaseEligibility: ['candidate_ref','environment_ref','scope_ref','decision_ref','decided_at','valid_until','freshness_ref'],
    deploymentAuthorization: ['grant_ref','candidate_ref','environment_ref','scope_ref','action','granted_at','valid_until','freshness_ref','revoked_at'],
    overhead: ['last_sampled_at'],
    views: ['last_validated_revision']
  };
  const objects = {
    project: state.project,
    governance_binding: state.governance_binding,
    coordination: state.coordination,
    active_role_assignment: state.coordination?.active_role_assignment,
    dimension_refs: state.specification_gate?.dimension_refs,
    spec_gate: state.specification_gate,
    candidate_identity: state.candidate_identity,
    releaseEligibility: state.release?.eligibility,
    deploymentAuthorization: state.release?.deployment_authorization,
    overhead: state.overhead,
    views: state.views
  };
  for (const [group, keys] of Object.entries(nulls)) {
    const o = objects[group];
    if (!o || typeof o !== 'object' || Array.isArray(o)) { f.push(`source-state:${group}:object-required`); continue; }
    for (const k of keys) if (!Object.hasOwn(o, k) || o[k] !== null) f.push(`source-state:${group}.${k}:must-be-null`);
  }
  if (!Array.isArray(state.project?.active_paradigms) || state.project.active_paradigms.length !== 0) f.push('source-state:project.active_paradigms:must-be-empty-array');
  if (!Array.isArray(state.specification_gate?.diagram_refs) || state.specification_gate.diagram_refs.length !== 0) f.push('source-state:diagram_refs:must-be-empty-array');
  if (state.specification_gate?.status !== 'UNVERIFIED' || state.specification_gate?.diagram_first_status !== 'UNVERIFIED') f.push('source-state:specification_gate:not-unverified');
  if (!Array.isArray(state.specification_gate?.missing_specification_prompts) || state.specification_gate.missing_specification_prompts.length !== 0) f.push('source-state:specification_gate.missing_specification_prompts:must-be-empty-array');
  if (!Array.isArray(state.specification_gate?.relative_search_refs) || state.specification_gate.relative_search_refs.length !== 0) f.push('source-state:specification_gate.relative_search_refs:must-be-empty-array');
  if (state.governance_binding?.proposed_version !== SUPPORTED.version) f.push('source-state:proposed-version');
  const au = state.autonomy;
  if (!au || au.enabled !== false || au.mode !== 'DISABLED' || au.phase !== 'IDLE' || au.retry_count !== 0 || au.max_retries !== 0 || au.last_reconciled_revision !== null || ['objective_ref','subject_scope','lease_ref','budget_ref','last_receipt_ref','last_failure_ref','review_receipt_ref','review_subject_digest'].some(k=>au[k]!==null)) f.push('source-state:autonomy-must-be-unbound');
  if (state.current_objective !== null || state.last_verified_checkpoint !== null) f.push('source-state:current-work-not-unbound');
  const emptyArrays = ['objectives','required_hard_gates','evidence_refs','negative_history_refs','regression_protection_refs','operational_diagnostics_refs','blockers','known_risks','reserved_actions','lifecycle_review_refs'];
  for (const k of emptyArrays) if (!Array.isArray(state[k]) || state[k].length !== 0) f.push(`source-state:${k}:must-be-empty-array`);
  for (const k of ['capabilities','external_systems','hard_gates']) if (!state[k] || typeof state[k] !== 'object' || Array.isArray(state[k]) || Object.keys(state[k]).length !== 0) f.push(`source-state:${k}:must-be-empty-object`);
  if (!Array.isArray(state.candidate_identity?.subject_scope) || state.candidate_identity.subject_scope.length !== 0) f.push('source-state:subject-scope');
  const e = state.release?.eligibility, a = state.release?.deployment_authorization;
  if (!e || e.status !== 'NO-GO' || e.reason !== 'PROJECT_NOT_BOUND_OR_VERIFIED' || !Array.isArray(e.evidence_refs) || e.evidence_refs.length !== 0) f.push('source-state:eligibility-not-default');
  if (!a || a.status !== 'NONE') f.push('source-state:deployment-not-default');
  if (!Array.isArray(state.release?.deployment_observations) || state.release.deployment_observations.length !== 0) f.push('source-state:deployment-observations-not-empty');
  if (!state.overhead || state.overhead.measurement !== 'UNKNOWN' || !Array.isArray(state.overhead.notes) || state.overhead.notes.length !== 0) f.push('source-state:overhead-not-default');
  if (!state.views || !Array.isArray(state.views.evidence_refs) || state.views.evidence_refs.length !== 0) f.push('source-state:views-not-default');
  return [...new Set(f)];
}

const indRank = {IND0:0, IND1:1, IND2:2, IND3:3};
export function validateRoleCombination(cfg) {
  const failures = [];
  if (!cfg || typeof cfg !== 'object' || Array.isArray(cfg)) return ['roles:config-object-required'];
  const {risk,changeClass,mode,workerId,writerId,reviewerId,acceptorId,reviewerIndependence,routerId,watchdogId} = cfg;
  if (!['R0','R1','R2','R3'].includes(risk)) failures.push('roles:risk');
  if (!['PRODUCT','GOVERNANCE','VALIDATOR','APPROVAL_CONTROL','RELEASE_CONTROL'].includes(changeClass)) failures.push('roles:unknown-change-class');
  if (mode !== 'THREE_ROLE') failures.push('roles:strict-three-role-required');
  const worker = workerId ?? writerId;
  if (![worker,reviewerId,acceptorId].every(nonEmptyString) || new Set([worker,reviewerId,acceptorId]).size !== 3) failures.push('roles:distinct-three-role-required');
  if (!(reviewerIndependence in indRank) || indRank[reviewerIndependence]<2) failures.push('roles:review-independence-too-low');
  if (!nonEmptyString(routerId)) failures.push('roles:router-id-required');
  if (!nonEmptyString(watchdogId)) failures.push('roles:watchdog-id-required');
  const identities = [worker,reviewerId,acceptorId,routerId,watchdogId].filter(nonEmptyString);
  if (new Set(identities).size !== identities.length) failures.push('roles:control-plane-identity-collision');
  return [...new Set(failures)];
}

// A missing/unscoped blocker applies globally. Scoped unresolved blockers apply only to
// that exact subject scope; hierarchical/overlapping scopes need stronger project adapters.
// These are rejection rules, not proof that external/project blockers were inventoried.
function blocksScope(blocker, subjectScope) {
  if (typeof blocker !== 'object' || blocker === null || Array.isArray(blocker)) return true;
  if (blocker.status === 'RESOLVED') return false;
  const scope = blocker.subject_scope ?? blocker.scope_ref;
  return !nonEmptyString(scope) || scope === subjectScope;
}

// Mandatory entrypoint for a project's actual filesystem-write guard. A synthetic adapter
// can only test shape/flow; its receipt is NOT proof of authenticated reviewers or actual isolation.
export async function validatePreCodeAuthorization(state, task, runtime) {
  const errors = validateReleaseState(state, {now:runtime?.trustedNow});
  if (state?.activation !== 'ACTIVE') errors.push('precode:active-project-binding-required');
  if (state?.specification_gate?.status !== 'SPEC_VERIFIED' || state?.specification_gate?.diagram_first_status !== 'DIAGRAM_LOCKED') errors.push('precode:spec-and-diagrams-must-be-locked');
  if (state?.specification_gate?.diagram_lock_subject_digest !== state?.candidate_identity?.subject_digest) errors.push('precode:stale-diagram-lock');
  if (!nonEmptyString(task?.subject_scope) || !state?.candidate_identity?.subject_scope?.includes(task.subject_scope)) errors.push('precode:scope-not-bound');
  if (state?.specification_gate?.subject_scope_ref !== task?.subject_scope) errors.push('precode:approved-diagram-scope-mismatch');
  if (!Array.isArray(state?.blockers) || state.blockers.some(b=>blocksScope(b,task?.subject_scope))) errors.push('precode:unresolved-applicable-blockers');
  if (!nonEmptyString(task?.worker_id) || state?.coordination?.active_role_assignment?.worker_id !== task.worker_id) errors.push('precode:worker-identity-not-bound');
  const roles = state?.coordination?.active_role_assignment;
  if (!roles || ![roles.worker_id,roles.reviewer_id,roles.acceptor_id,roles.router_id,roles.watchdog_id].every(nonEmptyString) ||
      new Set([roles.worker_id,roles.reviewer_id,roles.acceptor_id,roles.router_id,roles.watchdog_id]).size !== 5 ||
      !['IND2','IND3'].includes(roles.reviewer_independence)) errors.push('precode:isolated-actor-binding-required');
  if (!runtime || !validInstant(runtime.trustedNow) || typeof runtime.verifyPreCodeAuthorization!=='function') errors.push('precode:trusted-authorizer-required');
  if (errors.length) return {ok:false,failures:[...new Set(errors)]};
  try {
    const result = await runtime.verifyPreCodeAuthorization({
      state_revision: state.revision, subject_digest:state.candidate_identity.subject_digest,
      subject_scope:task.subject_scope, worker_id:task.worker_id,
      diagram_approval_ref:state.specification_gate.diagram_approval_ref,
      diagram_refs:state.specification_gate.diagram_refs,
      dimension_refs:state.specification_gate.dimension_refs,
      standards_refs:state.specification_gate.relative_search_refs
    });
    if (!result || result.authorized!==true || result.state_revision!==state.revision ||
        result.subject_digest!==state.candidate_identity.subject_digest ||
        result.subject_scope!==task.subject_scope || result.worker_id!==task.worker_id ||
        result.diagram_approval_ref!==state.specification_gate.diagram_approval_ref ||
        !nonEmptyString(result.receipt_ref)) return {ok:false,failures:['precode:trusted-authorization-receipt-not-confirmed']};
    return {ok:true,failures:[],receipt:result};
  } catch { return {ok:false,failures:['precode:trusted-authorizer-error']}; }
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
    for (const ent of fs.readdirSync(dir, {withFileTypes: true})) {
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
  {name: 'windows-absolute', rx: /\b[A-Za-z]:[\\/][^\r\n<>"|]+/},
  {name: 'posix-home', rx: /(?:^|[\s`'"(])\/(?:Users|home|mnt)\/[^\s`'"<>]+/m},
  {name: 'localhost-port', rx: /(?:localhost|127\.0\.0\.1):\d{2,5}/i}
];

export function verifyPackage(root) {
  const failures = [];
  if (typeof root !== 'string' || !fs.existsSync(root) || !fs.statSync(root).isDirectory()) return {ok: false, failures: ['package-root:directory-required']};
  const manifestPath = path.join(root, 'PACKAGE_MANIFEST.json');
  if (!fs.existsSync(manifestPath)) return {ok: false, failures: ['manifest:missing']};
  let manifest;
  try { manifest = parseStrictJson(fs.readFileSync(manifestPath, 'utf8'), 'PACKAGE_MANIFEST.json'); }
  catch (e) { return {ok: false, failures: [`manifest:parse:${e.message}`]}; }

  if (!manifest || typeof manifest !== 'object' || Array.isArray(manifest)) return {ok: false, failures: ['manifest:object-required']};
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
  try { state = parseStrictJson(fs.readFileSync(statePath, 'utf8'), 'PROJECT_STATE.yaml'); }
  catch (e) { failures.push(`source-state:parse:${e.message}`); }
  if (state) failures.push(...validateSourceTemplate(state));

  const govDir = path.join(root, 'governance');
  if (fs.existsSync(govDir)) {
    const active = fs.readdirSync(govDir).filter(x => fs.lstatSync(path.join(govDir, x)).isFile()).sort();
    const names = SUPPORTED.activeAuthorities.map(x => path.posix.basename(x)).sort();
    if (JSON.stringify(active) !== JSON.stringify(names)) failures.push(`active-authorities:${active.join(',')}`);
  }

  for (const rel of expectedPayloads.filter(x => /\.(md|yaml|yml|json|mjs)$/.test(x) && !['tools/test-verify-package.mjs','tools/test-autonomy-engine.mjs'].includes(x))) {
    const abs = path.join(root, ...rel.split('/'));
    if (!fs.existsSync(abs)) continue;
    const txt = fs.readFileSync(abs, 'utf8');
    for (const {name, rx} of neutralityPatterns) if (rx.test(txt)) failures.push(`neutrality-limited:${name}:${rel}`);
  }

  return {ok: failures.length === 0, failures: [...new Set(failures)]};
}

function main() {
  const here = path.dirname(fileURLToPath(import.meta.url));
  const root = path.resolve(here, '..');
  const args = process.argv.slice(2);
  if (args[0] === '--validate-state') {
    const p = path.resolve(args[1] || '');
    try {
      const state = parseStrictJson(fs.readFileSync(p, 'utf8'), p);
      const failures = validateReleaseState(state);
      if (failures.length) { console.error('STATE_CONTRACT_FAIL'); failures.forEach(x => console.error(x)); process.exit(1); }
      console.log('STATE_SHAPE_AND_CONSISTENCY_PASS live_authorization=NOT_PROVEN');
      return;
    } catch (e) { console.error('STATE_CONTRACT_FAIL'); console.error(e.message); process.exit(1); }
  }
  const result = verifyPackage(root);
  if (!result.ok) {
    console.error('PACKAGE_VERIFY_FAIL');
    result.failures.forEach(x => console.error(x));
    process.exit(1);
  }
  console.log(`PACKAGE_VERIFY_PASS package=${SUPPORTED.package} version=${SUPPORTED.version} files=${SUPPORTED.payloads.length} active_authorities=3`);
  console.log('SOURCE_TEMPLATE_SEMANTICS_PASS strict_json_compatible_yaml=true duplicate_keys_rejected=true');
  console.log('NEUTRALITY_SCAN_PASS_LIMITED manual_semantic_review_still_required=true');
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) main();

