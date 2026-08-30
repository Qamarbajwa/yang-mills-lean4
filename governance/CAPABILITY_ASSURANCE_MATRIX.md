# CAPABILITY ASSURANCE MATRIX — v3.0.0 MIGRATION

| Capability | Contract/evidence | Environment | Required strength | Independence | Gate | State |
|---|---|---|---|---|---|---|
| Project binding | `src/ymmg/ros.py`; project profile/governance identity | INTEGRATED_LOCAL | E3 | IND0 | Correct project and candidate bound | PASS |
| Typed authority | `GOVERNANCE_STATE.yaml`; owner-action reclassification | STATIC | E3 | IND0 | Domains not collapsed into generic approval | PASS_PENDING_REVIEW |
| Candidate-bound evidence | scientific hash, Git SHA, E4 raw receipt | INTEGRATED_LOCAL | E4 | IND1 | Stale candidate fails closed | PASS |
| Historical preservation | v2.9.4/ROS records, receipts, incidents, negative evidence | STATIC | E2 | IND0 | No historical overwrite | PASS |
| YM-002E claim quarantine | `verification/YM-002E_CLAIMED_SOLUTION_ADVERSARIAL_AUDIT.md` | STATIC | E3 | IND0 | No unsupported claim promotion | PASS_INITIAL |
| Migration conformance | `tests/test_governance_v300_conformance.py` and migration receipt | INTEGRATED_LOCAL | E3 | IND1 | Required v3 conformance checks pass | PENDING_INDEPENDENT_REVIEW |
