# MASTER AUTONOMOUS PROJECT GOVERNANCE, DEVELOPMENT & EVOLUTION CONSTITUTION — v2.9.4

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
