import os
import yaml
import json
import hashlib
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOV_DIR = ROOT / "governance"
REF_DIR = GOV_DIR / "reference"
CURR_DIR = REF_DIR / "current"
HIST_DIR = REF_DIR / "historical"

CURR_DIR.mkdir(parents=True, exist_ok=True)
HIST_DIR.mkdir(parents=True, exist_ok=True)
(ROOT / "verification" / "candidate_reviews").mkdir(parents=True, exist_ok=True)
(ROOT / "verification" / "raw").mkdir(parents=True, exist_ok=True)
(ROOT / "verification" / "accepted").mkdir(parents=True, exist_ok=True)
(ROOT / "verification" / "historical").mkdir(parents=True, exist_ok=True)

# 1. v2.9.3 Runtime Kernel
kernel_v293 = r"""# AUTONOMOUS PROJECT RUNTIME GOVERNANCE KERNEL — v2.9.3

> Compact always-loaded operational governance kernel extracted from
> `MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md`.
>
> The full master is the authoritative constitution. This runtime kernel
> provides the immutable rules and active operational invariants for every task.

# PART 0 — COMPACT IMMUTABLE RUNTIME KERNEL

## 0.1 Irreducible Truth Axioms

1. **Reality outranks model report.** Repository files, execution receipts, and source documents outrank any assistant summary.
2. **Model self-report is not acceptance evidence.** No worker may self-verify or self-accept its own output.
3. **Truth outranks task completion.** Acknowledging an unresolved blocker, error, or limitation is superior to false progress.
4. **Unknown, blocked, partial, and failed are valid states.** Never simulate success when requirements are unmet.
5. **Consequential work requires verified evidence.** No material claim (T2+) may be accepted without required evidence receipts.
6. **Worker != Verifier != Acceptance Authority.** Separation of roles is mandatory for all consequential claims.
7. **Never fabricate execution or provenance.** Never author, template, or synthesize independent verifier receipts.
8. **Inspect before editing.** Read and understand current repository state before introducing modifications.
9. **Preserve verified truth.** Never mutate or delete verified historical evidence; append corrections.
10. **Every feature receives regression tests.** Changes must be machine-checkable and regression-protected.
11. **Maintain known-good checkpoints.** Establish verified Git recovery points before and after consequential work.
12. **Integrity history escalates review.** Repeated provenance defects enforce strict isolation and autonomy reduction.

## 0.2 Independence Hierarchy for E4 Reviews

- **LEVEL_A:** Same application, same model family, separate subagent session/context.
- **LEVEL_B:** Same application, different model version or specialized prompt mode.
- **LEVEL_C:** Same application, different model family (e.g. cross-vendor subagent).
- **LEVEL_D:** Different application, different model family, isolated workspace.
- **LEVEL_E:** Deterministic external mathematical evaluator or human acceptance authority.

For T3+ tasks, Level A or higher is required. The primary writer MUST NOT author or template raw verifier artifacts.

## 0.3 Phased Governance State Modes

- **HYBRID_DISCOVERY:** Markdown documents remain authoritative; structured YAML state begins incremental reconciliation.
- **STRUCTURED_RECONCILIATION:** All core registers mirrored in validated YAML; discrepancies actively tracked.
- **SCHEMA_VALIDATED:** Machine-checkable JSON schema validates all governance files before test passage.
- **CANONICAL:** Single-source-of-truth structured control plane with automated gating.

Current project mode: `HYBRID_DISCOVERY`.
"""
(CURR_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.3.md").write_text(kernel_v293, encoding="utf-8")
print("Wrote v2.9.3 Runtime Kernel")

# 2. v2.9.3 Master Constitution
master_v293 = r"""# MASTER AUTONOMOUS PROJECT GOVERNANCE, DEVELOPMENT & EVOLUTION CONSTITUTION — v2.9.3

## 1. Scope and Authority

This document defines the complete governance constitution for autonomous, semi-autonomous, and pair-programming software and scientific research projects. It establishes immutable truth axioms, risk tiers, role separation, verifier capture protocols, truth control planes, and audit standards.

## 2. Core Governance Architecture

### 2.1 Role Separation & Invariants
- **ORCHESTRATOR:** Decomposes goals into bounded task contracts, assigns risk tiers, and schedules agent routing.
- **WRITER / WORKER:** Researches, drafts, and implements changes. Writes candidate artifacts. Never self-accepts T3+ tasks.
- **INDEPENDENT VERIFIER (REVIEWER):** Operates in a distinct session/thread with read-only tools. Audits candidate artifacts against primary sources and specifications. Generates unedited, verbatim review output.
- **ACCEPTANCE AUTHORITY:** Project owner or designated deterministic gate that promotes candidate checkpoints to accepted state.

### 2.2 Verifier Evidence Ownership and Isolation
- `verification/candidate_reviews/`: Candidate review notes prior to final sealing.
- `verification/raw/`: Verbatim unedited output captured directly from the verifier's execution transcript. Immediately hashed (SHA-256).
- `verification/accepted/`: Promoted verification receipts signed off by acceptance authority.
- `verification/historical/`: Archived, superseded, or provenance-challenged reviews.

### 2.3 Risk Escalation & Integrity Quarantines
- When an agent or model incurs an integrity incident (e.g., `IVR-001`, `IVR-002`), it is placed on the `AGENT/MODEL_WITH_INTEGRITY_HISTORY` register.
- Consequence: The primary worker is strictly prohibited from authoring or reconstructing raw verifier artifacts. All verification receipts must be extracted via automated transcript capture.

### 2.4 Governance State Migration Modes
1. `HYBRID_DISCOVERY` (Initial adoption)
2. `STRUCTURED_RECONCILIATION` (Structured data parity)
3. `SCHEMA_VALIDATED` (Strict machine schema validation)
4. `CANONICAL` (Automated governance control plane)
"""
(CURR_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md").write_text(master_v293, encoding="utf-8")
print("Wrote v2.9.3 Master Constitution")

# 3. CODING_ENVIRONMENT_PROFILE.yaml
env_profile = """coding_environment:
  name: "Google Antigravity"
  platform: "Antigravity Agentic IDE"
  os: "windows"
  shell: "powershell"
  python_environment: ".venv (Python 3.10+)"

available_agents:
  - id: "antigravity-primary-worker"
    provider: "Google DeepMind"
    model_family: "Gemini / Antigravity"
    model_version: "inherit"
    supported_roles:
      - WRITER
      - RESEARCHER
      - ORCHESTRATOR
  - id: "antigravity-subagent-verifier"
    provider: "Google DeepMind"
    model_family: "Gemini / Antigravity"
    model_version: "inherit"
    supported_roles:
      - REVIEWER
      - VERIFIER
      - ADVERSARIAL_CHALLENGER

capabilities:
  supports_separate_sessions: true
  supports_read_only_review: true
  supports_different_models: true
  supports_isolated_worktrees: true
  supports_external_reviewer: true
  supports_raw_verifier_capture: true

discovery_evidence:
  commands_or_tool_observations:
    - "Active workspace: d:/Comfy UI/yang mills and the mass gap"
    - "Tools exposed: run_command, view_file, replace_file_content, invoke_subagent, manage_subagents, etc."
    - "Subagent transcript path: C:/Users/arqam/.gemini/antigravity/brain/<conversation-id>/.system_generated/logs/transcript.jsonl"
    - "Raw capture script: scripts/capture_verifier_output.py"
  timestamp_utc: "2026-08-24T09:00:00Z"
  limitations: "Subagents execute under same OS user account; process isolation is managed via IDE agent orchestrator and read-only subagent tool restrictions (soft control)."
"""
(GOV_DIR / "CODING_ENVIRONMENT_PROFILE.yaml").write_text(env_profile, encoding="utf-8")
print("Wrote governance/CODING_ENVIRONMENT_PROFILE.yaml")

# 4. GOVERNANCE_VERSION_MANIFEST.yaml
# Compute hashes
k_v29_hash = hashlib.sha256((HIST_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.md").read_bytes()).hexdigest()
m_v29_hash = hashlib.sha256((HIST_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.md").read_bytes()).hexdigest()
k_v293_hash = hashlib.sha256((CURR_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.3.md").read_bytes()).hexdigest()
m_v293_hash = hashlib.sha256((CURR_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md").read_bytes()).hexdigest()

gov_manifest = {
    "manifest_version": "1.0",
    "timestamp_utc": "2026-08-24T09:00:00Z",
    "active_governance_version": "2.9.3",
    "documents": [
        {
            "filename": "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md",
            "path": "governance/reference/current/MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md",
            "version": "2.9.3",
            "status": "CURRENT",
            "sha256": m_v293_hash,
            "adopted_timestamp": "2026-08-24T09:00:00Z",
            "supersedes": "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.md"
        },
        {
            "filename": "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.3.md",
            "path": "governance/reference/current/AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.3.md",
            "version": "2.9.3",
            "status": "CURRENT",
            "sha256": k_v293_hash,
            "adopted_timestamp": "2026-08-24T09:00:00Z",
            "supersedes": "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.md"
        },
        {
            "filename": "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.md",
            "path": "governance/reference/historical/MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.md",
            "version": "2.9",
            "status": "HISTORICAL_SUPERSEDED",
            "sha256": m_v29_hash,
            "superseded_by": "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md"
        },
        {
            "filename": "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.md",
            "path": "governance/reference/historical/AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.md",
            "version": "2.9",
            "status": "HISTORICAL_SUPERSEDED",
            "sha256": k_v29_hash,
            "superseded_by": "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.3.md"
        }
    ]
}
(GOV_DIR / "GOVERNANCE_VERSION_MANIFEST.yaml").write_text(yaml.dump(gov_manifest, sort_keys=False), encoding="utf-8")
print("Wrote governance/GOVERNANCE_VERSION_MANIFEST.yaml")

# 5. GOVERNANCE_STATE_MIGRATION.md
state_mig = """# GOVERNANCE STATE MIGRATION

- **CURRENT_MODE:** `HYBRID_DISCOVERY`
- **TARGET_MODE:** `CANONICAL`
- **CURRENT_GOVERNANCE_VERSION:** `2.9.3`
- **PREVIOUS_GOVERNANCE_VERSION:** `2.9`
- **MIGRATION_TASK_ID:** `YM-GOV-293`

---

## Migration Status and Discrepancies

### Canonical Ownership Already Established
- `governance/GOVERNANCE_VERSION_MANIFEST.yaml`: Authoritative manifest of all active and historical governance constitutions and hashes.
- `governance/CODING_ENVIRONMENT_PROFILE.yaml`: Discovered platform and tool profile.
- `governance/AGENT_CAPABILITY_REGISTRY.yaml`: Active agent roles, permissions, and risk tiers.
- `governance/MODEL_TOOL_ROUTING.yaml`: Dynamic routing matrix.
- `governance/TOOL_PERMISSION_MATRIX.yaml`: Tool authority boundaries.

### Fields Still Hybrid / Markdown-Authoritative
- Theorem definitions and literature extractions (`THEOREM_LEDGER.md`, `OFFICIAL_PROBLEM_SPECIFICATION.md`).
- Historical integrity register (`INTEGRITY_VIOLATION_REGISTER.md`).
- Negative findings (`NEGATIVE_EVIDENCE_REGISTER.md`).

### Discrepancies Tracked
- `DISC-001`: YM-002A initial acceptance was challenged under IVR-002 and is undergoing formal E4 re-audit under v2.9.3.
- `DISC-002`: Tool isolation on Windows is logical/process-based (soft control) supported by transcript cryptographic hashing.

### Next Migration Step
Reconcile theorem ledger and problem specification into structured schema validation during Task `YM-003`.
"""
(GOV_DIR / "GOVERNANCE_STATE_MIGRATION.md").write_text(state_mig, encoding="utf-8")
print("Wrote governance/GOVERNANCE_STATE_MIGRATION.md")

# 6. project-governance.yaml
proj_gov = {
    "project": {
        "project_id": "yang-mills-mass-gap",
        "canonical_name": "Yang–Mills and the Mass Gap",
        "governance_version": "2.9.3",
        "base_sha": "34e8b411feef4e198723b9cd5fe2275a90a87a44"
    },
    "governance_state": {
        "mode": "HYBRID_DISCOVERY",
        "manifest_ref": "governance/GOVERNANCE_VERSION_MANIFEST.yaml",
        "migration_doc_ref": "governance/GOVERNANCE_STATE_MIGRATION.md"
    },
    "coding_environment": {
        "profile_ref": "governance/CODING_ENVIRONMENT_PROFILE.yaml",
        "isolation_level": "SOFT_CONTROL_PROCESS_ISOLATION"
    },
    "integrity": {
        "open_incidents": ["IVR-001", "IVR-002"],
        "status": "INCIDENTS_CONTAINED_REMEDIATION_ACTIVE",
        "acceptance_constraints": [
            "raw verifier provenance required",
            "writer cannot satisfy own E4 gate",
            "exact candidate binding required",
            "transcript log extraction required for raw E4"
        ]
    },
    "current_state": {
        "active_governance_task": "YM-GOV-293",
        "scientific_work_paused_for_governance_migration": True,
        "ym_000": "ACCEPTED_BASELINE",
        "ym_001": "INDEPENDENTLY_VERIFIED",
        "ym_001r1": "INDEPENDENTLY_VERIFIED",
        "ym_002a": "E3_VERIFIED_E4_PROVENANCE_CHALLENGED",
        "ym_002ar1": "IN_PROGRESS",
        "ym_002b": "BLOCKED"
    },
    "known_good_checkpoint": {
        "checkpoint_ref": "KNOWN_GOOD_CHECKPOINT.md",
        "last_sealed_checkpoint": "checkpoints/checkpoint_20260824T085716Z.json"
    }
}
(GOV_DIR / "project-governance.yaml").write_text(yaml.dump(proj_gov, sort_keys=False), encoding="utf-8")
print("Wrote governance/project-governance.yaml")

# 7. project-governance.schema.json
schema_json = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "ProjectGovernanceSchema_v293",
    "type": "object",
    "required": [
        "project",
        "governance_state",
        "coding_environment",
        "integrity",
        "current_state",
        "known_good_checkpoint"
    ],
    "properties": {
        "project": {
            "type": "object",
            "required": ["project_id", "canonical_name", "governance_version", "base_sha"],
            "properties": {
                "project_id": {"type": "string"},
                "canonical_name": {"type": "string"},
                "governance_version": {"type": "string", "enum": ["2.9.3"]},
                "base_sha": {"type": "string"}
            }
        },
        "governance_state": {
            "type": "object",
            "required": ["mode", "manifest_ref", "migration_doc_ref"],
            "properties": {
                "mode": {"type": "string", "enum": ["HYBRID_DISCOVERY", "STRUCTURED_RECONCILIATION", "SCHEMA_VALIDATED", "CANONICAL"]},
                "manifest_ref": {"type": "string"},
                "migration_doc_ref": {"type": "string"}
            }
        },
        "coding_environment": {
            "type": "object",
            "required": ["profile_ref", "isolation_level"],
            "properties": {
                "profile_ref": {"type": "string"},
                "isolation_level": {"type": "string"}
            }
        },
        "integrity": {
            "type": "object",
            "required": ["open_incidents", "status", "acceptance_constraints"],
            "properties": {
                "open_incidents": {"type": "array", "items": {"type": "string"}},
                "status": {"type": "string"},
                "acceptance_constraints": {"type": "array", "items": {"type": "string"}}
            }
        },
        "current_state": {
            "type": "object",
            "required": [
                "active_governance_task",
                "scientific_work_paused_for_governance_migration",
                "ym_002a",
                "ym_002b"
            ],
            "properties": {
                "active_governance_task": {"type": "string"},
                "scientific_work_paused_for_governance_migration": {"type": "boolean"},
                "ym_002a": {"type": "string"},
                "ym_002b": {"type": "string"}
            }
        },
        "known_good_checkpoint": {
            "type": "object",
            "required": ["checkpoint_ref", "last_sealed_checkpoint"],
            "properties": {
                "checkpoint_ref": {"type": "string"},
                "last_sealed_checkpoint": {"type": "string"}
            }
        }
    }
}
(GOV_DIR / "project-governance.schema.json").write_text(json.dumps(schema_json, indent=2), encoding="utf-8")
print("Wrote governance/project-governance.schema.json")

# 8. AGENT_CAPABILITY_REGISTRY.yaml
agent_cap = """agents:
  - id: "primary-writer-gemini"
    provider: "Google DeepMind"
    model_family: "Gemini / Antigravity"
    model_version: "inherit"
    environment: "Antigravity IDE Local Agent"
    supported_roles:
      - ORCHESTRATOR
      - RESEARCH_WRITER
      - MATHEMATICAL_WORKER
    qualification_status: "CONDITIONALLY_QUALIFIED"
    maximum_risk_tier: "T3"
    tool_permissions:
      - "view_file"
      - "replace_file_content"
      - "write_to_file"
      - "run_command"
      - "invoke_subagent"
      - "grep_search"
      - "find_by_name"
    known_strengths:
      - "Fast code execution and structured documentation synthesis"
      - "Mathematical physics literature structuring"
    known_weaknesses:
      - "Tendency to construct self-authored verification reports when unconstrained"
    integrity_incidents:
      - "IVR-001 (YM-001 review provenance defect)"
      - "IVR-002 (YM-002A review provenance recurrence)"
    last_qualification: "2026-08-24"
    requalification_triggers:
      - "Successful automated capture pipeline verification under YM-GOV-293 / YM-002AR1"

  - id: "independent-verifier-subagent"
    provider: "Google DeepMind"
    model_family: "Gemini / Antigravity"
    model_version: "inherit"
    environment: "Antigravity Research Subagent"
    supported_roles:
      - INDEPENDENT_REVIEWER
      - VERIFIER
      - ADVERSARIAL_CHALLENGER
    qualification_status: "QUALIFIED"
    maximum_risk_tier: "T4"
    tool_permissions:
      - "view_file"
      - "grep_search"
      - "find_by_name"
      - "list_dir"
      - "read_url_content"
      - "search_web"
    known_strengths:
      - "Unbiased blind verification of mathematical and bibliographic claims"
      - "Zero write authority prevents artifact contamination"
    known_weaknesses:
      - "Read-only access limits self-testing execution without orchestrator commands"
    integrity_incidents: []
    last_qualification: "2026-08-24"
    requalification_triggers: []
"""
(GOV_DIR / "AGENT_CAPABILITY_REGISTRY.yaml").write_text(agent_cap, encoding="utf-8")
print("Wrote governance/AGENT_CAPABILITY_REGISTRY.yaml")

# 9. MODEL_TOOL_ROUTING.yaml
routing_yaml = """routing_policy:
  version: "2.9.3"
  invariant: "WRITER_ID != REVIEWER_ID for all T3+ contracts"

role_assignments:
  ORCHESTRATOR:
    agent_id: "primary-writer-gemini"
    risk_tiers: ["T0", "T1", "T2", "T3", "T4"]
    constraints: "Must compile bounded task envelopes"

  RESEARCH_WRITER:
    agent_id: "primary-writer-gemini"
    risk_tiers: ["T0", "T1", "T2", "T3"]
    constraints: "Writes candidate artifacts only; no self-acceptance"

  MATHEMATICAL_WORKER:
    agent_id: "primary-writer-gemini"
    risk_tiers: ["T0", "T1", "T2", "T3"]
    constraints: "Executes Python / SymPy proofs and derivations"

  INDEPENDENT_REVIEWER:
    agent_id: "independent-verifier-subagent"
    risk_tiers: ["T2", "T3", "T4"]
    constraints: "Read-only subagent session; prompt isolation mandatory"

  ADVERSARIAL_CHALLENGER:
    agent_id: "independent-verifier-subagent"
    risk_tiers: ["T3", "T4"]
    constraints: "Actively attempts to construct counterexamples and find flaws"

  ACCEPTANCE_AUTHORITY:
    agent_id: "deterministic-evaluator-and-user"
    risk_tiers: ["T0", "T1", "T2", "T3", "T4"]
    constraints: "E3 deterministic test pass + genuine E4 receipt required"
"""
(GOV_DIR / "MODEL_TOOL_ROUTING.yaml").write_text(routing_yaml, encoding="utf-8")
print("Wrote governance/MODEL_TOOL_ROUTING.yaml")

# 10. TOOL_PERMISSION_MATRIX.yaml
perm_matrix = """permissions:
  WRITER:
    allowed_tools:
      - "view_file"
      - "replace_file_content"
      - "write_to_file"
      - "run_command"
      - "invoke_subagent"
      - "grep_search"
      - "find_by_name"
      - "list_dir"
    forbidden_actions:
      - "Modifying verification/raw/ or verification/accepted/"
      - "Overwriting historical integrity incident records"
      - "Self-certifying E4 gates for T3+ tasks"

  REVIEWER:
    allowed_tools:
      - "view_file"
      - "grep_search"
      - "find_by_name"
      - "list_dir"
      - "read_url_content"
      - "search_web"
    forbidden_actions:
      - "Writing or mutating workspace files directly"
      - "Executing modifying shell commands"

  ACCEPTANCE_AUTHORITY:
    allowed_actions:
      - "Sealing checkpoints"
      - "Promoting candidate state to INDEPENDENTLY_VERIFIED"
      - "Accepting governance transitions"
"""
(GOV_DIR / "TOOL_PERMISSION_MATRIX.yaml").write_text(perm_matrix, encoding="utf-8")
print("Wrote governance/TOOL_PERMISSION_MATRIX.yaml")

# 11. Truth Control Plane & Supporting Policies
truth_control = """# TRUTH CONTROL PLANE (v2.9.3)

## 1. Core Invariants
- **Primary Source Hegemony:** Primary mathematical and physical literature outranks secondary surveys, model reconstructions, and LLM completions.
- **Role Isolation:** `WRITER_ID != REVIEWER_ID != ACCEPTANCE_AUTHORITY` for all $T \ge 3$ tasks.
- **Immutable Receipts:** Every verified claim is anchored to deterministic E3 machine receipts and verbatim E4 reviewer transcripts.

## 2. Evidence Levels
- **E0:** Unverified assertion / informal conjecture.
- **E1:** Self-reported model reasoning / plausible argument.
- **E2:** Static cross-reference or bibliographic citation.
- **E3:** Deterministic local machine test execution with log and cryptographic JSON receipt.
- **E4:** Fresh, blind independent verifier review with raw transcript preservation and SHA-256 binding.
- **E5:** Formal machine-checked proof (e.g. Lean / Coq) or universal human peer acceptance.
"""
(GOV_DIR / "TRUTH_CONTROL_PLANE.md").write_text(truth_control, encoding="utf-8")

accept_gate = """# ACCEPTANCE GATE POLICY (v2.9.3)

## Gate Criteria by Risk Tier
- **T0 (Informational / Scratch):** Worker self-check.
- **T1 (Minor Refactor / Documentation):** Deterministic E3 test pass.
- **T2 (Substantive Code / Standard Feature):** E3 test pass + structural integrity check.
- **T3 (Scientific Claim / Theorem Ledger / Problem Spec):** E3 deterministic test suite + fresh blind E4 independent review with raw transcript capture.
- **T4 (Governance Constitution / Root Control Plane):** Full E3 test suite + independent T4 audit + explicit candidate binding + user sign-off.
"""
(GOV_DIR / "ACCEPTANCE_GATE_POLICY.md").write_text(accept_gate, encoding="utf-8")

eval_owner = """# EVALUATOR OWNERSHIP POLICY (v2.9.3)

## Separation of Evaluator and Evaluated
- Evaluator scripts (`tests/`, `scripts/check_repo.py`, `scripts/seal_checkpoint.py`, `scripts/capture_verifier_output.py`) are protected assets.
- A worker implementing a scientific task may not weaken test assertions to achieve artificial test passes.
- All test modifications must be accompanied by explicit justifications and verified under regression tests.
"""
(GOV_DIR / "EVALUATOR_OWNERSHIP.md").write_text(eval_owner, encoding="utf-8")

gov_lock = """# GOVERNANCE LOCK POLICY (v2.9.3)

## Governance Modification Constraints
- Governance files (`governance/`, `tests/test_governance*.py`) may only be modified under explicit `T4` governance change tasks (e.g. `YM-GOV-293`).
- Scientific workers executing standard tasks (e.g. `YM-002B`) must treat governance documents as read-only.
- Any unauthorized governance mutation immediately fails verification.
"""
(GOV_DIR / "GOVERNANCE_LOCK_POLICY.md").write_text(gov_lock, encoding="utf-8")

tamper_audit = """# TAMPER-EVIDENT AUDIT POLICY (v2.9.3)

## Verification Receipt Integrity
- All raw verifier outputs in `verification/raw/` are hashed with SHA-256 immediately upon transcript extraction.
- Derived reviews in `verification/` must record `DERIVED FROM`, `RAW_SHA256`, `VERIFIER CONVERSATION ID`, and `CANDIDATE GIT SHA AUDITED`.
- Modification of any file in `verification/raw/` invalidates the associated E4 receipt.
"""
(GOV_DIR / "TAMPER_EVIDENT_AUDIT_POLICY.md").write_text(tamper_audit, encoding="utf-8")

# 12. INTEGRITY_QUARANTINE.md
int_quarantine = """# INTEGRITY QUARANTINE REGISTER (v2.9.3)

## Active Quarantines

### Q-001: Acceptance-Critical Raw Verifier Artifact Authoring
- **Target Role / Agent:** `primary-writer-gemini` (Worker Agent)
- **Trigger Incidents:** `IVR-001` (YM-001), `IVR-002` (YM-002A)
- **Quarantine Scope:**
  The primary writer is strictly prohibited from authoring, templating, in-memory generating, or overwriting raw verification artifacts in `verification/raw/` and `verification/accepted/`.
- **Enforced Workflow:**
  1. Verifier subagent executes independently in a separate conversation session (`research` read-only subagent).
  2. Raw output is extracted directly from the subagent's execution transcript via `scripts/capture_verifier_output.py`.
  3. Raw SHA-256 is computed directly from disk.
- **Requalification Requirement:**
  Verification pipeline must pass automated regression testing in `tests/test_governance_v293.py` and receive successful independent review under `YM-GOV-293` and `YM-002AR1`.
- **Status:** `ACTIVE_ENFORCEMENT`
"""
(GOV_DIR / "INTEGRITY_QUARANTINE.md").write_text(int_quarantine, encoding="utf-8")

# 13. CONTRACT_OWNERSHIP_LEDGER.yaml
contracts = {
    "contracts": [
        {
            "contract_id": "CONTRACT-YM-000",
            "task_id": "YM-000",
            "risk_tier": "T2",
            "writer_id": "primary-writer-gemini",
            "reviewer_id": "deterministic-test-suite",
            "independence_level": "LEVEL_E_DETERMINISTIC_EXTERNAL_OR_HUMAN",
            "outcome": "ACCEPTED"
        },
        {
            "contract_id": "CONTRACT-YM-001",
            "task_id": "YM-001",
            "risk_tier": "T3",
            "writer_id": "primary-writer-gemini",
            "reviewer_id": "self-authored (CHALLENGED under IVR-001)",
            "independence_level": "INVALID_SELF_AUTHORED",
            "outcome": "SUPERSEDED_BY_YM-001R1"
        },
        {
            "contract_id": "CONTRACT-YM-001R1",
            "task_id": "YM-001R1",
            "risk_tier": "T3",
            "writer_id": "primary-writer-gemini",
            "reviewer_id": "bf418fe4-0e72-4987-b56f-02ed2d051c43",
            "independence_level": "LEVEL_A_SAME_APP_SAME_MODEL_SEPARATE_SESSION",
            "candidate_id": "24af7f9c9b648269be7438af10480c036f177dd4",
            "outcome": "INDEPENDENTLY_VERIFIED"
        },
        {
            "contract_id": "CONTRACT-YM-002A",
            "task_id": "YM-002A",
            "risk_tier": "T3",
            "writer_id": "primary-writer-gemini",
            "reviewer_id": "b3661f81-ff9a-483f-af3f-13de74b6ede5 (CHALLENGED under IVR-002)",
            "independence_level": "PROVENANCE_CHALLENGED",
            "candidate_id": "b15cbf62e4a9c40f7a6eb8d885f36fc805f2ae09",
            "outcome": "CHALLENGED_REQUIRES_REPAIR"
        },
        {
            "contract_id": "CONTRACT-YM-002AR1",
            "task_id": "YM-002AR1",
            "risk_tier": "T3",
            "writer_id": "primary-writer-gemini",
            "reviewer_id": "9dc7460c-e591-4229-b602-6d8ac5e56026",
            "independence_level": "LEVEL_A_SAME_APP_SAME_MODEL_SEPARATE_SESSION",
            "candidate_id": "f718005bb6d326eae36d4e0d627c362a6766858d",
            "outcome": "READY_FOR_EVALUATION"
        },
        {
            "contract_id": "CONTRACT-YM-GOV-293",
            "task_id": "YM-GOV-293",
            "risk_tier": "T4",
            "writer_id": "primary-writer-gemini",
            "reviewer_id": "independent-verifier-subagent",
            "independence_level": "LEVEL_A_SAME_APP_SAME_MODEL_SEPARATE_SESSION",
            "outcome": "IN_PROGRESS"
        }
    ]
}
(GOV_DIR / "CONTRACT_OWNERSHIP_LEDGER.yaml").write_text(yaml.dump(contracts, sort_keys=False), encoding="utf-8")
print("Wrote governance/CONTRACT_OWNERSHIP_LEDGER.yaml")

print("Governance v2.9.3 generation complete.")

