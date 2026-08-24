# [HISTORICAL / SUPERSEDED_BY_v2.9.4]
STATUS: SUPERSEDED_BY_v2.9.4
SUPERSEDED_DATE: 2026-08-24
REASON: Upgraded to Governance v2.9.4 under Task YM-GOV-294

---

# MASTER AUTONOMOUS PROJECT GOVERNANCE, DEVELOPMENT & EVOLUTION CONSTITUTION — v2.9.3

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
