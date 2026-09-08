# Project direction — Yang–Mills Mass Gap

Governance version: 4.0.3. This file defines intended scope, not live progress.

## Intent and boundaries

- **Project ID:** YANG_MILLS_MASS_GAP
- **Purpose:** Produce reliable, novel, explainable, reproducible, cumulative mathematical understanding of the Yang–Mills existence and mass gap problem (Clay Millennium Problem #4)
- **Desired outcomes:**
  1. Rigorous source-reconciled specification of the official problem requirements
  2. Complete theorem/literature ledger covering all known approaches (1954–2026)
  3. Structural dependency graph identifying the minimal load-bearing open bridges
  4. Reconstruction of the rigorous RG (Bałaban) and lattice gap programs
  5. Identification of the precise non-meeting estimates between UV and IR control
  6. (Long-term) Contribution to resolving the Clay problem
- **Target users:** Human owner (sole researcher); no external users
- **Non-goals:**
  - Product deployment, UI, external API, or user-facing application
  - Claiming proof without rigorous independent verification
  - Speculative bridges or ungrounded mechanisms
  - Software beyond research governance tooling
- **Unacceptable outcomes:**
  - Silently promoting unproved results to PROVED
  - Confusing lattice gap with continuum gap
  - Confusing confinement with mass gap
  - Memory loss of established negative results or obstructions
  - Self-acceptance of scientific results
- **Supported release scope:** Internal research repository only; no release, no deployment
- **Owner/business/legal/exposure boundaries:** No external exposure; no spend; no credentials; Clay Institute IP requirements respected

## Delegated source map

| Path/ID | Narrow Role | Owner | Version | Conflict Rule |
|---|---|---|---|---|
| `governance/MATHEMATICAL_RESEARCH_OPERATING_SYSTEM_v1.0.md` | Mathematical epistemic constitution (10+1 laws, 7 layers) | Human owner | v1.0.0 | ROS strengthens governance; neither silently overrides the other |
| `governance/EPISTEMIC_TAXONOMY_v1.0.yaml` | Status vocabulary for epistemic states | ROS v1.0 | v1.0 | Canonical |
| `THEOREM_LEDGER.md` | Verified theorem register with provenance | ROS v1.0 | Living | Append-only; corrections via supersession |
| `OFFICIAL_PROBLEM_SPECIFICATION.md` | Clay problem requirements | ROS v1.0 | Sealed | Immutable after YM-001 closeout |
| `DEFINITION_LEDGER.md` | Mathematical definition register | ROS v1.0 | Living | Append-only |
| `CLAIM_EVIDENCE_MATRIX.md` | Claim-evidence traceability | ROS v1.0 | Living | Append-only |
| `governance/CONTRACT_OWNERSHIP_LEDGER.yaml` | Contract registry | Primary worker | Living | Append-only |
| `governance/envelopes/YM-*.yaml` | Task execution envelopes | Primary worker | Per-task | Sealed after closeout |
| `governance/SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml` | Scientific fingerprint paths | ROS v1.0 | Living | Append when artifacts added |
| `src/ymmg/ros.py` | Closed-world fingerprint validator | Primary worker | Living | Must match classification |
| `literature/*` | Scientific artifacts and literature | Primary worker | Living | Generated from source data |
| `tests/test_*.py` | Deterministic test suite | Primary worker | Living | Must pass before acceptance |
| `verification/*` | E4 raw receipts and reviews | Verifier subagents | Per-task | Append-only |
| `governance/EVIDENCE_MAPPING_v403.yaml` | Active evidence and risk tier mapping (v4.0.3) | ROS v1.0 | v4.0.3 | Canonical |
| `governance/EVIDENCE_MAPPING_v3.0.0.yaml` | Historical evidence mapping | Historical | v3.0.0 | Preserved, not active |
| `governance/MIGRATION_RECEIPT_YM-GOV-300.md` | Historical migration receipt | Historical | Sealed | Preserved, not active |
| `governance/HUMAN_OWNER_ACCEPTANCE_ROS_v1.0_20260830.md` | ROS v1.0 acceptance record | Historical | Sealed | Preserved, not active |
| `governance/HUMAN_OWNER_ACCEPTANCE_YM-GOV-403_20260908.md` | v4.0.3 migration acceptance record | Historical | Sealed | Preserved |
| `governance/HUMAN_OWNER_ACCEPTANCE_YM-003_20260908.md` | YM-003 acceptance record | Historical | Sealed | Preserved |
| `governance/HUMAN_OWNER_ACCEPTANCE_YM-XNS-001_20260908.md` | YM-XNS-001 acceptance record | Historical | Sealed | Preserved |
| All `governance/*_v2.10.1*` files | Legacy templates | Historical | v2.10.1 | Inactive; preserved for hash integrity |

## Capability contracts and actors

### CAP-001: Mathematical Problem Specification
- **Actors:** Primary worker (writer), verifier subagent (reviewer), human owner (acceptor)
- **Journey:** Extract official requirements from primary source → construct specification → independent audit → acceptance
- **Entry surface:** NONE_BY_DESIGN (research artifact, not UI)
- **Acceptance evidence:** E4 independent audit against primary source
- **Status:** COMPLETE (YM-001, YM-001R1)

### CAP-002: Theorem/Literature Ledger
- **Actors:** Primary worker (writer), verifier subagent (reviewer), human owner (acceptor)
- **Journey:** Extract theorems from primary literature → classify by era → independent audit → acceptance
- **Entry surface:** NONE_BY_DESIGN
- **Acceptance evidence:** E4 independent audit per sub-era
- **Status:** COMPLETE for YM-002A through YM-002F; YM-002 parent CLOSED

### CAP-003: Missing-Bridge Graph
- **Actors:** Primary worker (writer), verifier subagent (reviewer), human owner (acceptor)
- **Journey:** Construct proof-dependency DAG from verified ledger → validate acyclicity → critical cut-set analysis → independent audit
- **Entry surface:** NONE_BY_DESIGN
- **Acceptance evidence:** E4 independent audit of 19-edge graph structure
- **Status:** ACCEPTED / CLOSED (YM-003 accepted by human owner 2026-09-08)

### CAP-004: RG Program Reconstruction
- **Actors:** Primary worker (writer), verifier subagent (reviewer), human owner (acceptor)
- **Journey:** Reconstruct Bałaban multi-scale RG program → verify theorem statements → isolate finite-volume stopping point and boundary terms → independent audit
- **Entry surface:** NONE_BY_DESIGN
- **Acceptance evidence:** E4 independent audit
- **Status:** ACCEPTED / CLOSED (Accepted by human owner 2026-09-08/2026-09-09)

### CAP-005: Lattice Gap Program Reconstruction
- **Actors:** Primary worker (writer), verifier subagent (reviewer), human owner (acceptor)
- **Journey:** Reconstruct Wilson strong-coupling expansion, cluster expansions, transfer matrix, infinite volume, modern theorems → canonical IR boundary record → independent audit
- **Entry surface:** NONE_BY_DESIGN
- **Acceptance evidence:** E4 independent audit
- **Status:** IN_PROGRESS (YM-005 unblocked by YM-004 acceptance)

### CAP-006: Non-Meeting Estimate Identification
- **Status:** BLOCKED (gated on YM-004, YM-005)

### CAP-007: Lean Formalization Pipeline (Non-Blocking Parallel)
- **Actors:** Primary worker (writer), verifier subagent (reviewer), human owner (acceptor)
- **Journey:** Scope formalization of Clay problem statement and Osterwalder–Schrader reconstruction chain in Lean 4
- **Entry surface:** NONE_BY_DESIGN
- **Status:** READY / IN_PARALLEL (YM-LEAN-001)

## Architecture and integrations

### Research Pipeline Architecture
Seven-layer epistemic pipeline (ROS v1.0):

```
Identity → Knowledge → Discovery → Falsification → Verification → Understanding → Evolution
```

Each layer has explicit entry/exit criteria defined in `governance/MATHEMATICAL_RESEARCH_OPERATING_SYSTEM_v1.0.md`.

### Data Flow
```
Primary Sources (literature/primary/) → Theorem Extraction → THEOREM_LEDGER.md
→ Bridge Graph (src/ymmg/bridge_graph.py) → literature/BRIDGE_EDGE_REGISTER.md
→ Critical Cut-Set Analysis → literature/CRITICAL_CUT_SET_REPORT.md
→ Minimal Estimate Register → literature/MINIMAL_SUFFICIENT_ESTIMATE_REGISTER.md
```

### Operational Requirements
- No external services or autonomous agents beyond fresh blind verifier subagents
- Python 3.10+ with pytest for deterministic test suite
- Git for version control (local only, no remote)

## Shared presentation

NONE_BY_DESIGN — This is a mathematical research repository with no user interface.

## Roadmap and decisions

### Bounded objectives (task graph)

| Objective | Dependencies | Capability | Status |
|---|---|---|---|
| YM-001: Problem specification | YM-000 | CAP-001 | INDEPENDENTLY_VERIFIED |
| YM-002A–F: Literature ledger | YM-001R1 | CAP-002 | CLOSED |
| YM-003: Missing-bridge graph | YM-002F | CAP-003 | ACCEPTED / CLOSED |
| YM-XNS-001: Navier–Stokes transfer audit | YM-003 | Cross-Problem | ACCEPTED / CLOSED |
| YM-GOV-403: Governance v4.0.3 migration | YM-003 (parallel) | Governance | ACCEPTED / CLOSED |
| YM-004: RG program reconstruction | YM-003 | CAP-004 | **ACCEPTED / CLOSED** |
| YM-LEAN-001: Lean formalization scoping | YM-003 | CAP-007 | **READY / IN_PARALLEL** |
| YM-005: Lattice gap reconstruction | YM-004 | CAP-005 | **IN_PROGRESS** |
| YM-006: Non-meeting estimate | YM-004, YM-005 | CAP-006 | BLOCKED |

### Key decisions
- ROS v1.0 adopted as constitutional overlay (2026-08-30, human owner accepted)
- Universal Governance v3.0.0 adopted (2026-08-30, independently verified)
- v4.0.3 migration authorized, audited, and accepted (2026-09-08)
- YM-003 accepted as authoritative missing-bridge decomposition (2026-09-08)
- Navier–Stokes breakthrough transfer audit completed and accepted (2026-09-08)
- YM-004 activated with "Euler-first" precursor emphasis on Bałaban finite-volume stopping point

## Completion

- **Milestone boundaries:** Each YM-task is independently closeable
- **Parity criteria:** N/A (no frontend/backend split)
- **Zero unresolved release-critical defects:** Required per task
- **Release eligibility:** NOT_APPLICABLE — internal research repository

## Update rule

Update this file only for intent, architecture, contract, reference, or roadmap changes. Routine PASS/FAIL updates go to `PROJECT_STATE.yaml`. Historical decisions preserved by reference.
