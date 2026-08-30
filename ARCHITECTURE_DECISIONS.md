# ARCHITECTURE DECISIONS — YANG-MILLS AND THE MASS GAP

## Architecture snapshot

| Area | Observed current state | Evidence | Confidence |
|---|---|---|---|
| Runtime/stack | Python package under `src/ymmg`; YAML/JSON/Markdown research records | `src/ymmg/`, `pyproject.toml` | HIGH |
| Data/storage | Git-tracked repository artifacts; evidence and raw transcripts stored locally | `evidence/`, `verification/`, `EVIDENCE_LEDGER.md` | HIGH |
| Auth/identity | Project binding, typed authority, candidate-bound evidence, human-owner acceptance | `src/ymmg/ros.py`, `governance/` | HIGH |
| External integrations | No configured Git remote or production provider integration observed | `git remote -v` | HIGH |
| Deployment | No production/customer deployment; internal research repository only | `GOVERNANCE_STATE.yaml`, project intent | HIGH |
| Test/CI | Local pytest suite; 152 tests collected and passing; no external CI configured | `tests/`, pytest run | HIGH |
| Other | Scientific fingerprint contains 17 canonical scientific files and fails closed on unknown research artifacts | `governance/SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml` | HIGH |

## Decision log

### ADR-300-001 — Preserve ROS as the mathematical epistemic constitution

- State: DECIDED_TECHNICAL
- Date: 2026-08-30
- Problem: Universal governance must not replace project-specific mathematical truth rules.
- Intent/requirement trace: `PROJECT_INTENT.md`; migration request precedence record.
- Options considered: replace ROS; run both without precedence; explicitly layer v3 execution governance above ROS.
- Technical evidence: accepted ROS v1.0 records and YM-ROS-100R3/YM-002DR1 E4 packet.
- Risk tier: T4
- Affected contracts/capabilities: all research task envelopes and evidence gates.
- Decision: v3 governs execution/authority/evidence semantics; ROS governs mathematical identity, assumptions, epistemic maturity, provenance, and analogue barriers.
- Why: Prevents authority and evidence semantics from silently relaxing mathematical constraints.
- Invariants: `GOVERNANCE_MIGRATION != SCIENTIFIC_PROGRESS`; `EXACT_RESULT != COMPLETE_SOLUTION_OF_THEORY`.
- Consequences/trade-offs: Two governance layers require explicit precedence and contradiction logging.
- Verification required: migration conformance and independent review.
- Rollback/migration path: preserve v3 artifacts as a bounded migration commit; revert only through a governed migration, without rewriting history.
- Owner-reserved boundary affected? NO

### ADR-300-002 — Local deterministic verification remains the technical evidence baseline

- State: OBSERVED
- Date: 2026-08-30
- Problem: Establish actual current project behavior before migration claims.
- Intent/requirement trace: CORE-TEST-INTEGRITY and CORE-EVIDENCE.
- Options considered: external CI dependency; local pytest baseline; both.
- Technical evidence: 152 collected and passing tests; no remote/CI observed.
- Risk tier: T3
- Affected contracts/capabilities: migration and YM-002E.
- Decision: use local pytest as E3 baseline and require independent review for T3/T4 closure.
- Why: Matches observed environment without overstating missing external CI.
- Consequences/trade-offs: No external CI independence is claimed.
- Verification required: rerun full suite after migration.
- Rollback/migration path: preserve receipts and revert only through bounded Git history.
- Owner-reserved boundary affected? NO
