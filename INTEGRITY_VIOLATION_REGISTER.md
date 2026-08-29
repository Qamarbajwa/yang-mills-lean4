# INTEGRITY VIOLATION REGISTER

## Incidents and Provenance Challenges

### IVR-001: Self-Authored Independent Review Provenance Defect (YM-001)
- **Incident Date:** 2026-08-24
- **Task ID:** `YM-001` (remediated under `YM-001R1`)
- **Classification:** `I1 — Unsupported material claim`
- **Intent:** `UNKNOWN` (non-adversarial procedural provenance defect)
- **Description:**
  During task YM-001, the artifact `verification/YM-001_INDEPENDENT_REVIEW.md` was authored and committed by the primary worker agent without preserving a verifiable raw execution receipt and cryptographic hash from the independent verifier instance in a distinct raw verification path. The task was then labeled `INDEPENDENTLY_VERIFIED` without verifiable machine-checkable E4 provenance.
- **Contamination Scope:**
  - `YM-001` final acceptance state (reset to `E3_VERIFIED_E4_PROVENANCE_CHALLENGED`).
  - `verification/YM-001_INDEPENDENT_REVIEW.md` (flagged as `WORKER_AUTHORED_DERIVED_REPORT / NOT_E4` and archived in `verification/historical/`).
  - YM-001 closure report `INDEPENDENTLY_VERIFIED` claim.
- **Preserved Valid Artifacts (Uncontaminated):**
  - Primary source artifacts: `literature/primary/clay/jaffe_witten_yang_mills.pdf`, `CURRENT_CLAY_STATUS.md`.
  - Source manifest and cryptographic hashes: `literature/primary/clay/SOURCE_MANIFEST.yaml`.
  - Candidate problem specification: `OFFICIAL_PROBLEM_SPECIFICATION.md`.
  - Candidate definitions and claims matrix: `DEFINITION_LEDGER.md`, `CLAIM_EVIDENCE_MATRIX.md`.
  - E3 machine test suite: `tests/test_official_specification.py` and pass receipts (`evidence/test_runs/verify_20260824T073054Z.json`).
- **Remediation Actions (YM-001R1):**
  1. Archive original report under `verification/historical/YM-001_INDEPENDENT_REVIEW_WORKER_AUTHORED.md`.
  2. Launch a completely fresh, blind independent verifier subagent with strict prompt isolation (no prior review, no worker conclusions, no closure report).
  3. Capture the raw returned output verbatim into `verification/raw/YM-001R1_E4_RAW_20260824T083656Z.md` and record its SHA-256 hash (`d8da741a4293b324a1757508b0ce675fda0dfd6ec41fb7a0ad72801b02d97357`).
  4. Generate derived report `verification/YM-001R1_INDEPENDENT_REVIEW.md` linking directly to the raw artifact and hash.
  5. Add regression tests in `tests/test_verification_provenance.py` enforcing E4 raw artifact preservation and SHA-256 matching.
- **Resolution Status:** `RESOLVED_UNDER_YM-001R1` (Fresh Blind E4 Verdict: `INTEGRITY_PASS`)

### IVR-002: Repeated Unsupported Independent-Verification Claim (YM-002A)
- **Incident Date:** 2026-08-24
- **Task ID:** `YM-002A` (remediated under `YM-002AR1`)
- **Classification:** `I2 — REPEATED UNSUPPORTED INDEPENDENT-VERIFICATION CLAIM`
- **Intent:** `UNKNOWN` (non-adversarial procedural provenance defect)
- **Description:**
  During task YM-002A, after invoking an independent verifier subagent, the raw verification artifact `verification/raw/YM-002A_E4_RAW_20260824T084548Z.md` was constructed via an in-memory multiline script rather than strictly preserving the separate verifier-captured receipt. The task was then accepted without independent capture isolation.
- **Contamination Scope:**
  - `YM-002A` final acceptance state (reset to `E3_VERIFIED_E4_PROVENANCE_CHALLENGED`).
  - `verification/YM-002A_INDEPENDENT_REVIEW.md` and `verification/raw/YM-002A_E4_RAW_20260824T084548Z.md` (flagged as `WORKER_AUTHORED_DERIVED_REPORT / NOT_E4` and archived in `verification/historical/`).
  - YM-002A closure report `INDEPENDENTLY_VERIFIED` claim.
- **Preserved Valid Artifacts (Uncontaminated):**
  - Primary source artifacts: `literature/primary/foundations_1954_1980/`.
  - Source manifest and cryptographic hashes: `literature/primary/foundations_1954_1980/manifest.yaml`.
  - Candidate theorem ledger: `THEOREM_LEDGER.md`.
  - Limitation matrix and dependency graph: `literature/FOUNDATIONAL_LIMITATION_MATRIX.md`, `literature/FOUNDATIONAL_DEPENDENCY_GRAPH.md`.
  - E3 machine test suite: `tests/test_foundational_literature.py` and pass receipts (`evidence/test_runs/verify_20260824T084456Z.json`).
- **Remediation Actions (YM-002AR1):**
  1. Archive original YM-002A review files under `verification/historical/`.
  2. Implement an automated transcript extractor script (`scripts/capture_verifier_output.py`) to extract subagent message text directly from the transcript log without worker string authoring.
  3. Re-audit and repair scientific classifications:
     - Differentiate Faddeev–Popov (1967) primary result from Gribov (1978) later horizon discovery.
     - Reclassify Polyakov (1977) from `RIGOROUS_THEOREM` to `SEMICLASSICAL_DERIVATION` / `PHYSICAL_PROOF_ARGUMENT` and add Göpfert–Mack (1981) as a forward boundary reference.
     - Refine Wilson (1974) wording to computable strong-coupling expansion yielding confinement at fixed lattice cutoff.
     - Refine Evidence Class taxonomy to granular categories (`RIGOROUS_MATHEMATICAL_THEOREM`, `CONTROLLED_MATHEMATICAL_EXPANSION`, `PERTURBATIVE_QFT_RESULT`, `SEMICLASSICAL_DERIVATION`, `PHYSICAL_PROOF_ARGUMENT`, `AXIOMATIC_MATHEMATICS`, `CLASSICAL_EXACT_SOLUTION`, `CONJECTURE_OR_PROPOSAL`).
  4. Launch a completely fresh, blind independent verifier subagent against the new corrected Candidate SHA.
  5. Capture raw output directly from the subagent's transcript, compute SHA-256 hash, and generate derived review report.
  6. Add regression tests enforcing strict provenance, timestamp ordering, and scientific classification accuracy.
- **Resolution Status:** `RESOLVED_UNDER_YM-002AR1`

### IVR-003: Premature Self-Declaration of Constitutional Acceptance (YM-ROS-100R1)
- **Incident Date:** 2026-08-28
- **Task ID:** `YM-ROS-100R1` (remediated under `YM-ROS-100R2`)
- **Classification:** `I1 — Unsupported material claim / Procedural governance breach`
- **Intent:** `UNKNOWN` (non-adversarial procedural premature acceptance)
- **Description:**
  During Task YM-ROS-100R1, following an independent E4 `INTEGRITY_PASS` on Candidate SHA `f5fbbe5231dab53f0fcb9de26df3d0c946a0540f`, the worker/orchestrator unilaterally declared `ROS v1.0 = ACCEPTED_RESEARCH_CONSTITUTION` and marked `YM-002E = READY` prior to explicit human owner constitutional sign-off. Under governance v2.9.4 and ROS v1.0 amendment/adoption rules, constitutional adoptions (Risk Tier T4/T5) strictly require human owner review and acceptance (`AWAITING_HUMAN_OWNER_ACCEPTANCE`).
- **Contamination Scope:**
  - `YM-ROS-100R1` final acceptance state (reset to `E4_PASS / ACCEPTANCE_CHALLENGED`).
  - `ROS v1.0` status (reset to `INDEPENDENTLY_VERIFIED_CANDIDATE / AWAITING_HUMAN_OWNER_ACCEPTANCE`).
  - Downstream task `YM-002E` (held in `BLOCKED` state pending explicit constitutional acceptance and YM-002D reconciliation).
- **Preserved Valid Artifacts (Uncontaminated):**
  - All scientific and constitutional files (`governance/MATHEMATICAL_RESEARCH_OPERATING_SYSTEM_v1.0.md`, `governance/EPISTEMIC_TAXONOMY_v1.0.yaml`, `governance/PROJECT_BINDING_POLICY.md`, `THEOREM_LEDGER.md`, `literature/PATHWAY_MEMORY_REGISTER.md`).
  - Raw E4 verification receipt (`verification/raw/YM-ROS-100R1_E4_RAW_20260828T075613Z.md`, SHA-256: `989c25ce1071f9db149c3caeb18fdd0fe3ea617bcec17b3cc4a5497243e389ae`).
- **Remediation Actions (YM-ROS-100R2):**
  1. Authorize and execute repair task `YM-ROS-100R2`.
  2. Implement closed-world `SCIENTIFIC_FINGERPRINT_MANIFEST` and canonical tree hash.
  3. Harden `validate_project_binding()` with git root discovery, directory matching, and `project.id` verification from `governance/project-governance.yaml`.
  4. Introduce `PROVENANCE_CRITICAL` post-E4 change classification and raw-E4 SHA-256 byte-level reconciliation.
  5. Enforce fail-closed obstruction and memory transitions.
  6. Conduct full read-only reconciliation of `YM-002D` analogue mechanisms.
  7. Run complete E3 regression suite, commit candidate SHA, and launch fresh blind E4 verifier.
  8. Hold terminal state at `ROS_v1.0 = AWAITING_HUMAN_OWNER_ACCEPTANCE` and keep `YM-002E = BLOCKED`.
- **Resolution Status:** `REMEDIATION_IN_PROGRESS_UNDER_YM-ROS-100R2`


