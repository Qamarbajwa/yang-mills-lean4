# TASK GRAPH

| Task | Objective | Prerequisites | Risk | Required evidence | State |
|---|---|---|---|---|---|
| YM-000 | Bootstrap and verify local repository | none | T2 | E3 local reproducible tests | DONE |
| YM-001 | Reconstruct official problem specification | YM-000 | T3 | primary-source citations + independent consistency check | INDEPENDENTLY_VERIFIED |
| YM-001R1 | Repair independent-review E4 provenance | YM-001 | T3 | fresh blind E4 audit + raw receipt preservation | INDEPENDENTLY_VERIFIED |
| YM-GOV-293 | Governance migration v2.9 -> v2.9.3 | none | T4 | E3 deterministic test suite + fresh blind E4 review | SUPERSEDED_BY_YM-GOV-294 |
| YM-GOV-294 | Governance migration to v2.9.4 (Role-based environment-local acceptance) | none | T4 | E3 deterministic test suite + fresh blind E4 review | ACCEPTED_AFTER_ACCEPTANCE_REPAIR |
| YM-GOV-294R1 | Acceptance-authority identity reconciliation | YM-GOV-294 | T4 | E3 identity regression + blind independent review | INDEPENDENTLY_VERIFIED |
| YM-GOV-300 | Universal Governance v3.0.0 migration | YM-ROS-100R3, ROS v1.0 acceptance | T4 | E3 conformance + fresh blind independent review | ACCEPTED / ACTIVE |
| YM-002 | Build theorem/literature ledger | YM-001R1 | T2 | primary literature + theorem-level extraction | IN_PROGRESS |
| YM-002A | Foundational Yang–Mills advancement ledger (1954–1980) | YM-001R1 | T3 | primary literature + fresh blind E4 audit | INDEPENDENTLY_VERIFIED_AFTER_REPAIR |
| YM-002AR1 | E4 provenance + foundational semantic repair | YM-002A, YM-GOV-294R1 | T3 | fresh blind E4 audit + raw receipt capture | INDEPENDENTLY_VERIFIED |
| YM-002B | Constructive / RG foundations ledger (1980–2000) | YM-002AR1 | T3 | primary literature + fresh blind E4 audit | INDEPENDENTLY_VERIFIED |
| YM-002BR1 | Constructive pathway-memory semantic + closeout reconciliation | YM-002B | T3 | fresh blind E4 audit + epistemic taxonomy | INDEPENDENTLY_VERIFIED |
| YM-002C | Modern rigorous advances (2000–2026) | YM-002BR1 | T3 | primary literature + fresh blind E4 audit | E3_VERIFIED_E4_CHALLENGED_SUPERSEDED |
| YM-002CR1 | Modern literature scope, taxonomy & completeness repair | YM-002C | T3 | fresh blind E4 audit + epistemic taxonomy | E3_VERIFIED_E4_CHALLENGED_SUPERSEDED |
| YM-002CR2A | Modern-source locator and theorem-wording erratum | YM-002CR2 | T2 | fresh blind E4 audit + bounded erratum verification | INDEPENDENTLY_VERIFIED |
| YM-002D | Solved, modified, and analogous theories ledger | YM-002CR2A | T3 | primary literature + theorem extraction | CLOSED |
| YM-ROS-100R1 | ROS v1.0 constitutional semantic and acceptance hardening | YM-002D | T4 | E3 deterministic test suite + fresh blind E4 audit | E4_PASS_ACCEPTANCE_CHALLENGED |
| YM-ROS-100R2 | ROS v1.0 constitutional & epistemic hardening repair | YM-ROS-100R1 | T4 | E3 deterministic test suite + fresh blind E4 audit | INDEPENDENTLY_VERIFIED |
| YM-ROS-100R3 | ROS v1.0 discovery-based closed-world fingerprint enforcement | YM-ROS-100R2 | T4 | E3 discovery regressions + fresh blind delta-E4 audit | ACCEPTED / ACTIVE |
| YM-002DR1 | Analogue semantic classification errata and reconciliation | YM-002D | T3 | ten-row semantic regression + fresh blind delta-E4 audit | CLOSED |
| YM-002E | Claimed-solution adversarial audit ledger | YM-002DR1, YM-ROS-100R3 | T3 | primary claims + refutation evidence | INDEPENDENTLY_VERIFIED / CLOSED |
| YM-002F | Cross-era theorem and dependency synthesis | YM-002E | T3 | structural graph synthesis + E4 review | INDEPENDENTLY_VERIFIED / CLOSED |
| YM-003 | Construct missing-bridge graph | YM-002F | T3 | independent semantic review | ACCEPTED / CLOSED |
| YM-GOV-403 | Universal Governance v4.0.3 migration | YM-GOV-300, ROS v1.0 | T4 | 14 transition tests + fresh blind E4 + owner cutover | ACCEPTED / ACTIVE |
| YM-XNS-001 | Navier–Stokes breakthrough transfer audit | YM-003 | T3 | cross-problem transfer audit + independent review | ACCEPTED / CLOSED |
| YM-004 | Reconstruct rigorous RG/Bałaban program | YM-003 | T3 | theorem reproduction + finite-volume stopping point | ACCEPTED / CLOSED |
| YM-LEAN-001 | Lean 4 formalization scoping for Clay spec and OS reconstruction | YM-003 | T2 | formalization design + non-blocking scoping | COMPLETED / SCOPED |
| YM-005 | Reconstruct rigorous lattice gap program | YM-004 | T3 | theorem reproduction + independent review | SCIENTIFICALLY_ACCEPTED (WITH_REGULATED_SCOPE, YM-005-R1) |
| YM-006 | Identify the precise non-meeting estimate | YM-004, YM-005 | T3 | explicit dependency proof + adversarial review | SCIENTIFIC_REVIEW_HOLD |
| YM-007 | Evaluation of novel theoretical mechanisms | YM-006 | T3 | non-perturbative mechanism evaluation + E4 review | SCIENTIFIC_REVIEW_HOLD |
| YM-008 | Synthesis and formulation of hybrid attack strategy | YM-007 | T3 | hybrid attack specification + adversarial falsification | SCIENTIFIC_REVIEW_HOLD |
| YM-009 | Execution of hybrid attack strategy and quantitative closure | YM-008 | T3 | non-perturbative gluing + independent review | SCIENTIFIC_REVIEW_HOLD / NOT_ESTABLISHED |
| YM-010 | Global research monograph, axiomatic verification, and Clay synthesis | YM-009 | T3 | program monograph + global bridge closure + E4 review | SCIENTIFIC_REVIEW_HOLD / NOT_ESTABLISHED |
| YM-GOV-011 | Emergency scientific integrity audit | YM-005 through YM-010 | T4 | independent adversarial audit + proof-level verification | COMPLETED / AUDIT_ACCEPTED |
| YM-GOV-012 | Scientific recovery and proof-dependency repair | YM-GOV-011 | T3 | 19-edge graph reconciliation + YM-011 formulation | COMPLETED |
| YM-GOV-014 | Autonomous scientific repair & acceptance authority correction | YM-GOV-012 | T4 | ROS state machine repair + YM-005-R1 + E4 review | COMPLETED / AUDIT_ACCEPTED |
| YM-011-PRE | Fixed-lattice gradient-flow loop perturbation precursor | YM-004 | T3 | differential loop flow estimate + independent review | SCIENTIFICALLY_ACCEPTED (YM-011-PRE-R1) |
| YM-011-OBS-MAP | Two-lattice observable-transfer construction | YM-004, YM-011-PRE | T3 | midpoint-exponential blocking map + independent review | SCIENTIFICALLY_ACCEPTED |
| YM-011-PLAQUETTE-EXP | Finite-lattice Gibbs expectation bound for plaquette defect | YM-004, YM-011-PRE, YM-011-OBS-MAP | T3 | expectation reduction + group range + independent review | SCIENTIFICALLY_ACCEPTED (YM-011-PLAQUETTE-EXP-R2) |
| YM-GOV-ADOPT-0406R3 | Evaluate and bind Universal Governance v4.0.6-r3 controls | YM-011-PLAQUETTE-EXP | T4 | 18 adoption tests + 12-gate readiness rule + E4 review | CLOSED / ACCEPTED |
| YM-011-TREE-GAUGE | Maximal spanning-tree gauge fixing & co-tree plaquette map | YM-GOV-ADOPT-0406R3, YM-011-PLAQUETTE-EXP | T3 | tree gauge + toron moduli separation + R1 provenance reconciliation | SCIENTIFICALLY_ACCEPTED (YM-011-TREE-GAUGE-R1) |
| YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB | Periodic toron quartic zero modes & Brascamp–Lieb covariance analysis | YM-011-TREE-GAUGE | T3 | quartic commutator integral + Brascamp–Lieb / non-Gaussian bounds | SCIENTIFICALLY_ACCEPTED (P1=PROVED, P2=OPEN, P3=OPEN) |
| YM-011-DYADIC-FREE-ENERGY-UNIFORMITY | Non-asymptotic volume uniformity of periodic dyadic free-energy increment | YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB | T3 | volume-uniform bound on (1/|P_+|) ln(Z(beta/2)/Z(beta)) or Peierls/RG block localization | SCIENTIFICALLY_ACCEPTED (P1=PROVED, P2=PROVED_AT_WEAK_COUPLING, P3=OPEN) |
| YM-011 | First load-bearing bridge lemma | YM-004, YM-011-PRE, YM-011-OBS-MAP, YM-011-PLAQUETTE-EXP, YM-011-TREE-GAUGE, YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB, YM-011-DYADIC-FREE-ENERGY-UNIFORMITY | T3 | UV scale-transfer lemma proof + counterexample testing | PROPOSED / READY_FOR_AUTHORIZATION |

