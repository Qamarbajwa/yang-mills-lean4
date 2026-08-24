# EVIDENCE LEDGER

| ID | Claim supported | Evidence level | Artifact | Exact version/SHA | Reproducibility | Status |
|---|---|---|---|---|---|---|
| EVD-000-01 | YM-000 Repository bootstrap and environment verification | E3 | `evidence/test_runs/verify_20260824T070007Z.json` | `a0d7eaa79c96af3dc8d00fa59f2c7857c6e83c1107b1b6f7c15c5c6940c457ea` | REPRODUCIBLE_LOCALLY (`RUN_VERIFY.ps1`) | ACCEPTED |
| EVD-001-01 | YM-001 Primary source preservation and integrity | E3 | `literature/primary/clay/jaffe_witten_yang_mills.pdf` | `3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09` | MACHINE_CHECKED (`SOURCE_MANIFEST.yaml`) | ACCEPTED |
| EVD-001-02 | YM-001 Machine specification invariant tests | E3 | `evidence/test_runs/verify_20260824T073054Z.json` | `c0df18c651a9e50d109946a0de605825a889ff20a7e5c8f248ee7e6691840855` | REPRODUCIBLE_LOCALLY (`pytest tests/`) | ACCEPTED |
| EVD-001R1-01 | YM-001R1 Fresh Blind E4 Independent Audit (Verifier `bf418fe4-0e72-4987-b56f-02ed2d051c43`) | E4 | `verification/raw/YM-001R1_E4_RAW_20260824T083656Z.md` | `d8da741a4293b324a1757508b0ce675fda0dfd6ec41fb7a0ad72801b02d97357` (Candidate SHA: `24af7f9c9b648269be7438af10480c036f177dd4`) | INDEPENDENT_SUBAGENT_TRANSCRIPT | ACCEPTED |
| EVD-001R1-02 | YM-001R1 Derived E4 Independent Review Report | E4_DERIVED | `verification/YM-001R1_INDEPENDENT_REVIEW.md` | Derived from raw `d8da741a4293b324a1757508b0ce675fda0dfd6ec41fb7a0ad72801b02d97357` | TRACEABLE_TO_RAW_E4 | ACCEPTED |

