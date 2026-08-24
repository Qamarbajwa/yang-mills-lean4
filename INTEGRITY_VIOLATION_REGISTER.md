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
