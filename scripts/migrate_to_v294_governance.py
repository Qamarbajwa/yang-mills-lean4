import yaml
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOV_DIR = ROOT / "governance"
REF_DIR = GOV_DIR / "reference"
CURR_DIR = REF_DIR / "current"
HIST_DIR = REF_DIR / "historical"

CURR_DIR.mkdir(parents=True, exist_ok=True)
HIST_DIR.mkdir(parents=True, exist_ok=True)

# 1. Archive v2.9.3 to historical/
header_v293 = """# [HISTORICAL / SUPERSEDED_BY_v2.9.4]
STATUS: SUPERSEDED_BY_v2.9.4
SUPERSEDED_DATE: 2026-08-24
REASON: Upgraded to Governance v2.9.4 under Task YM-GOV-294

---

"""

for f in CURR_DIR.glob("*.md"):
    content = f.read_text(encoding="utf-8")
    (HIST_DIR / f.name).write_text(header_v293 + content, encoding="utf-8")
    f.unlink()
print("Archived v2.9.3 to governance/reference/historical/")

# 2. Write v2.9.4 Runtime Kernel
kernel_v294 = r"""# AUTONOMOUS PROJECT RUNTIME GOVERNANCE KERNEL — v2.9.4

> Compact always-loaded operational governance kernel extracted from
> `MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md`.
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
7. **Acceptance Authority is a Role, not a Brand.** No model, provider, or application (e.g. Codex, OpenAI, Gemini, Claude, DeepSeek) holds universal or inherent acceptance authority.
8. **Environment-Local Role Mapping.** Acceptance authority is determined by the active coding environment's local parent/orchestrator or designated local acceptance mechanism. Cross-application review is optional fallback.
9. **Never fabricate execution or provenance.** Never author, template, or synthesize independent verifier receipts.
10. **Inspect before editing.** Read and understand current repository state before introducing modifications.
11. **Preserve verified truth.** Never mutate or delete verified historical evidence; append corrections.
12. **Every feature receives regression tests.** Changes must be machine-checkable and regression-protected.
13. **Maintain known-good checkpoints.** Establish verified Git recovery points before and after consequential work.
14. **Integrity history escalates review.** Repeated provenance defects enforce strict isolation and autonomy reduction.

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
(CURR_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.4.md").write_text(kernel_v294, encoding="utf-8")
print("Wrote v2.9.4 Runtime Kernel")

# 3. Write v2.9.4 Master Constitution
master_v294 = r"""# MASTER AUTONOMOUS PROJECT GOVERNANCE, DEVELOPMENT & EVOLUTION CONSTITUTION — v2.9.4

## 1. Scope and Authority

This document defines the complete governance constitution for autonomous, semi-autonomous, and pair-programming software and scientific research projects. It establishes immutable truth axioms, risk tiers, role separation, environment-local role mapping, verifier capture protocols, truth control planes, and audit standards.

## 2. Core Governance Architecture

### 2.1 Role-Based Acceptance Authority Invariant
- **`ACCEPTANCE_AUTHORITY` is a functional role**, not a model, not a provider, and not a permanent application.
- Universal provider or model authority is explicitly prohibited:
  - `CODEX != UNIVERSAL_ACCEPTANCE_AUTHORITY`
  - `OPENAI != UNIVERSAL_PARENT`
  - `GEMINI != UNIVERSAL_ACCEPTANCE_AUTHORITY`
  - `CLAUDE != UNIVERSAL_ACCEPTANCE_AUTHORITY`
  - `DEEPSEEK != UNIVERSAL_ACCEPTANCE_AUTHORITY`
- The acceptance authority for any task contract is mapped dynamically from the **active coding environment**:
  - **Antigravity:** Gemini Writer -> Separate Gemini Reviewer (Level A) -> Deterministic Tests (E3) -> Antigravity Parent Orchestrator / Designated Local Acceptance Gate.
  - **Claude Code:** Claude Writer -> Separate Claude Reviewer -> Deterministic Tests (E3) -> Claude Code Parent Orchestrator.
  - **OpenCode:** OpenCode Writer -> Distinct OpenCode Reviewer -> Deterministic Tests (E3) -> OpenCode Parent Orchestrator.
- Cross-application review and acceptance is **OPTIONAL / FALLBACK**, not default.

### 2.2 Role Separation & Invariants
- **ORCHESTRATOR:** Decomposes goals into bounded task contracts, assigns risk tiers, and schedules agent routing.
- **WRITER / WORKER:** Researches, drafts, and implements changes. Writes candidate artifacts. Never self-accepts T3+ tasks (`WRITER_ID != ACCEPTANCE_AUTHORITY_ID`).
- **INDEPENDENT VERIFIER (REVIEWER):** Operates in a distinct session/thread with read-only tools (`WRITER_ID != REVIEWER_ID`). Audits candidate artifacts against primary sources. Generates unedited, verbatim review output.
- **ACCEPTANCE AUTHORITY:** Environment-local authority that records technical contract acceptance upon satisfaction of E3 deterministic tests and genuine E4 review.
- **HUMAN / RELEASE AUTHORITY:** Distinct from technical acceptance; required for production deployment or fundamental constitutional changes where specified.

### 2.3 Verifier Evidence Ownership and Isolation
- `verification/candidate_reviews/`: Candidate review notes prior to final sealing.
- `verification/raw/`: Verbatim unedited output captured directly from the verifier's execution transcript. Immediately hashed (SHA-256).
- `verification/accepted/`: Promoted verification receipts signed off by acceptance authority.
- `verification/historical/`: Archived, superseded, or provenance-challenged reviews.

### 2.4 Risk Escalation & Integrity Quarantines
- When an agent or model incurs an integrity incident (e.g., `IVR-001`, `IVR-002`), it is placed on the `AGENT/MODEL_WITH_INTEGRITY_HISTORY` register.
- Consequence: The primary worker is strictly prohibited from authoring or reconstructing raw verifier artifacts. All verification receipts must be extracted via automated transcript capture.

### 2.5 Governance State Migration Modes
1. `HYBRID_DISCOVERY` (Initial adoption)
2. `STRUCTURED_RECONCILIATION` (Structured data parity)
3. `SCHEMA_VALIDATED` (Strict machine schema validation)
4. `CANONICAL` (Automated governance control plane)
"""
(CURR_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md").write_text(master_v294, encoding="utf-8")
print("Wrote v2.9.4 Master Constitution")

# 4. Update CODING_ENVIRONMENT_PROFILE.yaml
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

acceptance_capabilities:
  local_parent_orchestrator: true
  distinct_reviewer: true
  automated_acceptance_gate: true
  human_approval_available: true

discovery_evidence:
  evidence:
    - "Active workspace: d:/Comfy UI/yang mills and the mass gap"
    - "Tools exposed: run_command, view_file, replace_file_content, invoke_subagent, manage_subagents, etc."
    - "Subagent transcript path: C:/Users/arqam/.gemini/antigravity/brain/<conversation-id>/.system_generated/logs/transcript.jsonl"
    - "Raw capture script: scripts/capture_verifier_output.py"
    - "Acceptance authority: Environment-local Antigravity Orchestrator + Deterministic Test Suite"
  timestamp_utc: "2026-08-24T09:15:00Z"
  limitations: "Subagents execute under same OS user account; process isolation is managed via IDE agent orchestrator and read-only subagent tool restrictions (soft control)."
"""
(GOV_DIR / "CODING_ENVIRONMENT_PROFILE.yaml").write_text(env_profile, encoding="utf-8")
print("Wrote governance/CODING_ENVIRONMENT_PROFILE.yaml")

# 5. Update GOVERNANCE_VERSION_MANIFEST.yaml
k_v29_hash = hashlib.sha256((HIST_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.md").read_bytes()).hexdigest()
m_v29_hash = hashlib.sha256((HIST_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.md").read_bytes()).hexdigest()
k_v293_hash = hashlib.sha256((HIST_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.3.md").read_bytes()).hexdigest()
m_v293_hash = hashlib.sha256((HIST_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md").read_bytes()).hexdigest()
k_v294_hash = hashlib.sha256((CURR_DIR / "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.4.md").read_bytes()).hexdigest()
m_v294_hash = hashlib.sha256((CURR_DIR / "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md").read_bytes()).hexdigest()

gov_manifest = {
    "manifest_version": "1.1",
    "timestamp_utc": "2026-08-24T09:15:00Z",
    "active_governance_version": "2.9.4",
    "documents": [
        {
            "filename": "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md",
            "path": "governance/reference/current/MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md",
            "version": "2.9.4",
            "status": "CURRENT",
            "sha256": m_v294_hash,
            "adopted_timestamp": "2026-08-24T09:15:00Z",
            "supersedes": "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md"
        },
        {
            "filename": "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.4.md",
            "path": "governance/reference/current/AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.4.md",
            "version": "2.9.4",
            "status": "CURRENT",
            "sha256": k_v294_hash,
            "adopted_timestamp": "2026-08-24T09:15:00Z",
            "supersedes": "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.3.md"
        },
        {
            "filename": "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md",
            "path": "governance/reference/historical/MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md",
            "version": "2.9.3",
            "status": "HISTORICAL_SUPERSEDED",
            "sha256": m_v293_hash,
            "superseded_by": "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md"
        },
        {
            "filename": "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.3.md",
            "path": "governance/reference/historical/AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.3.md",
            "version": "2.9.3",
            "status": "HISTORICAL_SUPERSEDED",
            "sha256": k_v293_hash,
            "superseded_by": "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.4.md"
        },
        {
            "filename": "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.md",
            "path": "governance/reference/historical/MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.md",
            "version": "2.9",
            "status": "HISTORICAL_SUPERSEDED",
            "sha256": m_v29_hash,
            "superseded_by": "MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.4.md"
        },
        {
            "filename": "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.md",
            "path": "governance/reference/historical/AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.md",
            "version": "2.9",
            "status": "HISTORICAL_SUPERSEDED",
            "sha256": k_v29_hash,
            "superseded_by": "AUTONOMOUS_PROJECT_RUNTIME_GOVERNANCE_KERNEL_v2.9.4.md"
        }
    ]
}
(GOV_DIR / "GOVERNANCE_VERSION_MANIFEST.yaml").write_text(yaml.dump(gov_manifest, sort_keys=False), encoding="utf-8")
print("Wrote governance/GOVERNANCE_VERSION_MANIFEST.yaml")

# 6. Update GOVERNANCE_STATE_MIGRATION.md
state_mig = """# GOVERNANCE STATE MIGRATION

- **CURRENT_MODE:** `HYBRID_DISCOVERY`
- **TARGET_MODE:** `CANONICAL`
- **CURRENT_GOVERNANCE_VERSION:** `2.9.4`
- **PREVIOUS_GOVERNANCE_VERSIONS:** `2.9`, `2.9.3`
- **MIGRATION_TASK_ID:** `YM-GOV-294`

---

## Migration Status and Discrepancies

### Canonical Ownership Already Established
- `governance/GOVERNANCE_VERSION_MANIFEST.yaml`: Authoritative manifest of active (v2.9.4) and historical (v2.9, v2.9.3) governance documents and cryptographic hashes.
- `governance/CODING_ENVIRONMENT_PROFILE.yaml`: Discovered platform, tools, and acceptance capabilities.
- `governance/AGENT_CAPABILITY_REGISTRY.yaml`: Active agent roles, permissions, and risk tiers.
- `governance/MODEL_TOOL_ROUTING.yaml`: Dynamic routing matrix enforcing environment-local acceptance authority.
- `governance/TOOL_PERMISSION_MATRIX.yaml`: Tool authority boundaries.

### Fields Still Hybrid / Markdown-Authoritative
- Theorem definitions and literature extractions (`THEOREM_LEDGER.md`, `OFFICIAL_PROBLEM_SPECIFICATION.md`).
- Historical integrity register (`INTEGRITY_VIOLATION_REGISTER.md`).
- Negative findings (`NEGATIVE_EVIDENCE_REGISTER.md`).

### Discrepancies Tracked
- `DISC-001`: YM-002A initial acceptance was challenged under IVR-002 and is undergoing formal E4 re-audit under v2.9.4 (`YM-002AR1`).
- `DISC-002`: Tool isolation on Windows is logical/process-based (soft control) supported by transcript cryptographic hashing.

### Next Migration Step
Reconcile theorem ledger and problem specification into structured schema validation during Task `YM-003`.
"""
(GOV_DIR / "GOVERNANCE_STATE_MIGRATION.md").write_text(state_mig, encoding="utf-8")
print("Wrote governance/GOVERNANCE_STATE_MIGRATION.md")

# 7. Update project-governance.yaml
proj_gov = {
    "project": {
        "id": "YM-MASS-GAP",
        "project_id": "YM-MASS-GAP",
        "name": "Yang-Mills and the Mass Gap",
        "canonical_name": "Yang–Mills and the Mass Gap",
        "governance_version": "2.9.4",
        "base_sha": "0550d6138f9f61ac877baf340971517cbb3c2e95"
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
    "acceptance": {
        "authority_model": "ENVIRONMENT_LOCAL",
        "universal_codex_authority": False,
        "universal_provider_authority": False,
        "mapping_ref": "governance/CODING_ENVIRONMENT_PROFILE.yaml"
    },
    "integrity": {
        "open_incidents": ["IVR-001", "IVR-002"],
        "status": "INCIDENTS_CONTAINED_REMEDIATION_ACTIVE",
        "acceptance_constraints": [
            "raw verifier provenance required",
            "writer cannot satisfy own E4 gate",
            "exact candidate binding required",
            "transcript log extraction required for raw E4",
            "acceptance authority is role not permanent provider"
        ]
    },
    "current_state": {
        "active_governance_task": "YM-GOV-294",
        "scientific_work_paused_for_governance_migration": True,
        "proof_status": "NO_CANDIDATE_PROOF",
        "original_verified_lemmas": 0,
        "ym_000": "ACCEPTED_BASELINE",
        "ym_001": "INDEPENDENTLY_VERIFIED",
        "ym_001r1": "INDEPENDENTLY_VERIFIED",
        "ym_002a": "E3_VERIFIED_E4_PROVENANCE_CHALLENGED",
        "ym_002ar1": "BLOCKED",
        "ym_002b": "BLOCKED"
    },
    "known_good_checkpoint": {
        "checkpoint_ref": "KNOWN_GOOD_CHECKPOINT.md",
        "last_sealed_checkpoint": "checkpoints/checkpoint_20260824T091056Z.json"
    }
}
(GOV_DIR / "project-governance.yaml").write_text(yaml.dump(proj_gov, sort_keys=False), encoding="utf-8")
print("Wrote governance/project-governance.yaml")

# 8. Update project-governance.schema.json
schema_json = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "ProjectGovernanceSchema_v294",
    "type": "object",
    "required": [
        "project",
        "governance_state",
        "coding_environment",
        "acceptance",
        "integrity",
        "current_state",
        "known_good_checkpoint"
    ],
    "properties": {
        "project": {
            "type": "object",
            "required": ["id", "project_id", "canonical_name", "governance_version", "base_sha"],
            "properties": {
                "id": {"type": "string"},
                "project_id": {"type": "string"},
                "name": {"type": "string"},
                "canonical_name": {"type": "string"},
                "governance_version": {"type": "string", "enum": ["2.9.4"]},
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
        "acceptance": {
            "type": "object",
            "required": ["authority_model", "universal_codex_authority", "universal_provider_authority", "mapping_ref"],
            "properties": {
                "authority_model": {"type": "string", "enum": ["ENVIRONMENT_LOCAL", "EXTERNAL_AUTHORITY"]},
                "universal_codex_authority": {"type": "boolean", "enum": [False]},
                "universal_provider_authority": {"type": "boolean", "enum": [False]},
                "mapping_ref": {"type": "string"}
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
                "proof_status",
                "original_verified_lemmas",
                "ym_002a",
                "ym_002ar1",
                "ym_002b"
            ],
            "properties": {
                "active_governance_task": {"type": "string"},
                "scientific_work_paused_for_governance_migration": {"type": "boolean"},
                "proof_status": {"type": "string"},
                "original_verified_lemmas": {"type": "integer"},
                "ym_002a": {"type": "string"},
                "ym_002ar1": {"type": "string"},
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

# 9. Update AGENT_CAPABILITY_REGISTRY.yaml
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
      - "Successful automated capture pipeline verification under YM-GOV-294 / YM-002AR1"

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
      - "Unbiased blind verification of mathematical, bibliographic, and governance claims"
      - "Zero write authority prevents artifact contamination"
    known_weaknesses:
      - "Read-only access limits self-testing execution without orchestrator commands"
    integrity_incidents: []
    last_qualification: "2026-08-24"
    requalification_triggers: []
"""
(GOV_DIR / "AGENT_CAPABILITY_REGISTRY.yaml").write_text(agent_cap, encoding="utf-8")
print("Wrote governance/AGENT_CAPABILITY_REGISTRY.yaml")

# 10. Update MODEL_TOOL_ROUTING.yaml
routing_yaml = """routing_policy:
  version: "2.9.4"
  invariants:
    - "WRITER_ID != REVIEWER_ID for all T3+ contracts"
    - "WRITER_ID != ACCEPTANCE_AUTHORITY_ID for all consequential contracts"
    - "NO_PERMANENT_MODEL_ACCEPTANCE_AUTHORITY (Acceptance Authority is a functional role)"
    - "Acceptance routing is environment-local by default; cross-application is optional fallback"

role_assignments:
  ORCHESTRATOR:
    agent_id: "primary-writer-gemini"
    environment: "Antigravity"
    risk_tiers: ["T0", "T1", "T2", "T3", "T4"]
    constraints: "Must compile bounded task envelopes"

  RESEARCH_WRITER:
    agent_id: "primary-writer-gemini"
    environment: "Antigravity"
    risk_tiers: ["T0", "T1", "T2", "T3"]
    constraints: "Writes candidate artifacts only; no self-acceptance"

  MATHEMATICAL_WORKER:
    agent_id: "primary-writer-gemini"
    environment: "Antigravity"
    risk_tiers: ["T0", "T1", "T2", "T3"]
    constraints: "Executes Python / SymPy proofs and derivations"

  INDEPENDENT_REVIEWER:
    agent_id: "independent-verifier-subagent"
    environment: "Antigravity"
    risk_tiers: ["T2", "T3", "T4"]
    constraints: "Read-only subagent session; prompt isolation mandatory"

  ADVERSARIAL_CHALLENGER:
    agent_id: "independent-verifier-subagent"
    environment: "Antigravity"
    risk_tiers: ["T3", "T4"]
    constraints: "Actively attempts to construct counterexamples and find flaws"

  ACCEPTANCE_AUTHORITY:
    agent_id: "antigravity-local-acceptance-orchestrator"
    environment: "Antigravity"
    authority_type: "ENVIRONMENT_LOCAL"
    risk_tiers: ["T0", "T1", "T2", "T3", "T4"]
    constraints: "E3 deterministic test pass + genuine E4 receipt required. No universal provider authority."

  HUMAN_AUTHORITY:
    agent_id: "project-owner-human"
    environment: "User"
    risk_tiers: ["T4", "T5"]
    constraints: "Mandatory for production release or fundamental constitution overhaul"
"""
(GOV_DIR / "MODEL_TOOL_ROUTING.yaml").write_text(routing_yaml, encoding="utf-8")
print("Wrote governance/MODEL_TOOL_ROUTING.yaml")

# 11. Update TOOL_PERMISSION_MATRIX.yaml
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
      - "Recording environment-local technical acceptance"

  HUMAN_AUTHORITY:
    allowed_actions:
      - "Authorizing major governance constitution migrations (T4/T5)"
      - "Production deployment authorization"
"""
(GOV_DIR / "TOOL_PERMISSION_MATRIX.yaml").write_text(perm_matrix, encoding="utf-8")
print("Wrote governance/TOOL_PERMISSION_MATRIX.yaml")

# 12. Update ACCEPTANCE_GATE_POLICY.md
accept_gate = """# ACCEPTANCE GATE POLICY (v2.9.4)

## 1. Acceptance Authority Invariant
- `ACCEPTANCE_AUTHORITY` is a **functional role**, not a model, provider, or company.
- Universal provider or model authority (e.g. Codex, OpenAI, Gemini, Claude, DeepSeek) is prohibited.
- Technical acceptance is **environment-local**:
  - `Antigravity`: Gemini Writer -> Separate Gemini Reviewer -> E3 Deterministic Tests -> Antigravity Local Acceptance Gate.
  - `Claude Code`: Claude Writer -> Separate Claude Reviewer -> E3 Deterministic Tests -> Claude Code Local Acceptance Gate.
  - `OpenCode`: OpenCode Writer -> Distinct OpenCode Reviewer -> E3 Deterministic Tests -> OpenCode Local Acceptance Gate.

## 2. Gate Sequence for Consequential Contracts (T3+)
```
CANDIDATE
    -> EVIDENCE_ATTACHED
    -> MACHINE_CHECKED (E3)
    -> INDEPENDENT_REVIEW (E4)
    -> INTEGRITY_CHECKED
    -> ENVIRONMENT_LOCAL_ACCEPTANCE
    -> ACCEPTED
```

## 3. Distinction Between Technical Acceptance and Release Authority
- Environment-local technical acceptance = `BOUNDED TECHNICAL CONTRACT ACCEPTED`.
- It does NOT constitute `RELEASE_READY` or `PRODUCTION_AUTHORIZED`.
- T4/T5 governance or deployment changes retain distinct `HUMAN_AUTHORITY` authorization.
"""
(GOV_DIR / "ACCEPTANCE_GATE_POLICY.md").write_text(accept_gate, encoding="utf-8")
print("Wrote governance/ACCEPTANCE_GATE_POLICY.md")

# 13. Update CONTRACT_OWNERSHIP_LEDGER.yaml
contracts = {
    "contracts": [
        {
            "contract_id": "CONTRACT-YM-000",
            "task_id": "YM-000",
            "risk_tier": "T2",
            "writer": {
                "environment": "Antigravity",
                "agent_id": "primary-writer-gemini",
                "model": "Gemini / Antigravity"
            },
            "reviewer": {
                "environment": "Antigravity",
                "agent_id": "deterministic-test-suite",
                "model": "pytest",
                "independence_level": "LEVEL_E_DETERMINISTIC_EXTERNAL_OR_HUMAN"
            },
            "acceptance_authority": {
                "environment": "Antigravity",
                "authority_id": "antigravity-local-acceptance-orchestrator",
                "authority_type": "ENVIRONMENT_LOCAL"
            },
            "outcome": "ACCEPTED"
        },
        {
            "contract_id": "CONTRACT-YM-001",
            "task_id": "YM-001",
            "risk_tier": "T3",
            "writer": {
                "environment": "Antigravity",
                "agent_id": "primary-writer-gemini",
                "model": "Gemini / Antigravity"
            },
            "reviewer": {
                "environment": "Antigravity",
                "agent_id": "self-authored (CHALLENGED under IVR-001)",
                "model": "Gemini / Antigravity",
                "independence_level": "INVALID_SELF_AUTHORED"
            },
            "outcome": "SUPERSEDED_BY_YM-001R1"
        },
        {
            "contract_id": "CONTRACT-YM-001R1",
            "task_id": "YM-001R1",
            "risk_tier": "T3",
            "writer": {
                "environment": "Antigravity",
                "agent_id": "primary-writer-gemini",
                "model": "Gemini / Antigravity"
            },
            "reviewer": {
                "environment": "Antigravity",
                "agent_id": "bf418fe4-0e72-4987-b56f-02ed2d051c43",
                "model": "Gemini / Antigravity",
                "independence_level": "LEVEL_A_SAME_APP_SAME_MODEL_SEPARATE_SESSION"
            },
            "acceptance_authority": {
                "environment": "Antigravity",
                "authority_id": "antigravity-local-acceptance-orchestrator",
                "authority_type": "ENVIRONMENT_LOCAL"
            },
            "candidate_id": "24af7f9c9b648269be7438af10480c036f177dd4",
            "outcome": "INDEPENDENTLY_VERIFIED"
        },
        {
            "contract_id": "CONTRACT-YM-002A",
            "task_id": "YM-002A",
            "risk_tier": "T3",
            "writer": {
                "environment": "Antigravity",
                "agent_id": "primary-writer-gemini",
                "model": "Gemini / Antigravity"
            },
            "reviewer": {
                "environment": "Antigravity",
                "agent_id": "b3661f81-ff9a-483f-af3f-13de74b6ede5 (CHALLENGED under IVR-002)",
                "model": "Gemini / Antigravity",
                "independence_level": "PROVENANCE_CHALLENGED"
            },
            "candidate_id": "b15cbf62e4a9c40f7a6eb8d885f36fc805f2ae09",
            "outcome": "CHALLENGED_REQUIRES_REPAIR"
        },
        {
            "contract_id": "CONTRACT-YM-002AR1",
            "task_id": "YM-002AR1",
            "risk_tier": "T3",
            "writer": {
                "environment": "Antigravity",
                "agent_id": "primary-writer-gemini",
                "model": "Gemini / Antigravity"
            },
            "reviewer": {
                "environment": "Antigravity",
                "agent_id": "9dc7460c-e591-4229-b602-6d8ac5e56026",
                "model": "Gemini / Antigravity",
                "independence_level": "LEVEL_A_SAME_APP_SAME_MODEL_SEPARATE_SESSION"
            },
            "acceptance_authority": {
                "environment": "Antigravity",
                "authority_id": "antigravity-local-acceptance-orchestrator",
                "authority_type": "ENVIRONMENT_LOCAL"
            },
            "candidate_id": "f718005bb6d326eae36d4e0d627c362a6766858d",
            "outcome": "BLOCKED"
        },
        {
            "contract_id": "CONTRACT-YM-GOV-293",
            "task_id": "YM-GOV-293",
            "risk_tier": "T4",
            "writer": {
                "environment": "Antigravity",
                "agent_id": "primary-writer-gemini",
                "model": "Gemini / Antigravity"
            },
            "reviewer": {
                "environment": "Antigravity",
                "agent_id": "ce14fe80-a7fe-46bc-91e0-cf249b52b3e2",
                "model": "Gemini / Antigravity",
                "independence_level": "LEVEL_A_SAME_APP_SAME_MODEL_SEPARATE_SESSION"
            },
            "acceptance_authority": {
                "environment": "Antigravity",
                "authority_id": "antigravity-local-acceptance-orchestrator",
                "authority_type": "ENVIRONMENT_LOCAL"
            },
            "candidate_id": "690faecc3d643f1dada3f5f6ecb5937461609af3",
            "outcome": "SUPERSEDED_BY_YM-GOV-294"
        },
        {
            "contract_id": "CONTRACT-YM-GOV-294",
            "task_id": "YM-GOV-294",
            "risk_tier": "T4",
            "writer": {
                "environment": "Antigravity",
                "agent_id": "primary-writer-gemini",
                "model": "Gemini / Antigravity"
            },
            "reviewer": {
                "environment": "Antigravity",
                "agent_id": "independent-verifier-subagent",
                "model": "Gemini / Antigravity",
                "independence_level": "LEVEL_A_SAME_APP_SAME_MODEL_SEPARATE_SESSION"
            },
            "acceptance_authority": {
                "environment": "Antigravity",
                "authority_id": "antigravity-local-acceptance-orchestrator",
                "authority_type": "ENVIRONMENT_LOCAL"
            },
            "outcome": "IN_PROGRESS"
        }
    ]
}
(GOV_DIR / "CONTRACT_OWNERSHIP_LEDGER.yaml").write_text(yaml.dump(contracts, sort_keys=False), encoding="utf-8")
print("Wrote governance/CONTRACT_OWNERSHIP_LEDGER.yaml")

print("Migration to v2.9.4 complete.")

