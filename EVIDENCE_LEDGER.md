# EVIDENCE LEDGER

| ID | Claim supported | Evidence level | Artifact | Exact version/SHA | Reproducibility | Status |
|---|---|---|---|---|---|---|
| EVD-000-01 | YM-000 Repository bootstrap and environment verification | E3 | `evidence/test_runs/verify_20260824T070007Z.json` | `a0d7eaa79c96af3dc8d00fa59f2c7857c6e83c1107b1b6f7c15c5c6940c457ea` | REPRODUCIBLE_LOCALLY (`RUN_VERIFY.ps1`) | ACCEPTED |
| EVD-001-01 | YM-001 Primary source preservation and integrity | E3 | `literature/primary/clay/jaffe_witten_yang_mills.pdf` | `3558403ca14c11e382f73a09e548222708540bfdf478cf96aa11c52d43e23e09` | MACHINE_CHECKED (`SOURCE_MANIFEST.yaml`) | ACCEPTED |
| EVD-001-02 | YM-001 Machine specification invariant tests | E3 | `evidence/test_runs/verify_20260824T073054Z.json` | `c0df18c651a9e50d109946a0de605825a889ff20a7e5c8f248ee7e6691840855` | REPRODUCIBLE_LOCALLY (`pytest tests/`) | ACCEPTED |
| EVD-001R1-01 | YM-001R1 Fresh Blind E4 Independent Audit (Verifier `bf418fe4-0e72-4987-b56f-02ed2d051c43`) | E4 | `verification/raw/YM-001R1_E4_RAW_20260824T083656Z.md` | `d8da741a4293b324a1757508b0ce675fda0dfd6ec41fb7a0ad72801b02d97357` (Candidate SHA: `24af7f9c9b648269be7438af10480c036f177dd4`) | INDEPENDENT_SUBAGENT_TRANSCRIPT | ACCEPTED |
| EVD-001R1-02 | YM-001R1 Derived E4 Independent Review Report | E4_DERIVED | `verification/YM-001R1_INDEPENDENT_REVIEW.md` | Derived from raw `d8da741a4293b324a1757508b0ce675fda0dfd6ec41fb7a0ad72801b02d97357` | TRACEABLE_TO_RAW_E4 | ACCEPTED |
| EVD-002A-01 | YM-002A Primary source manifest and records (13 papers, 1954–1980) | E3 | `literature/primary/foundations_1954_1980/manifest.yaml` | `manifest.yaml` verified against local files | MACHINE_CHECKED (`manifest.yaml`) | ACCEPTED |
| EVD-002A-02 | YM-002A Foundational machine invariant test suite (17 tests) | E3 | `tests/test_foundational_literature.py` | Pass receipt `evidence/test_runs/verify_20260824T084456Z.json` | REPRODUCIBLE_LOCALLY (`pytest tests/`) | ACCEPTED |
| EVD-002A-03 | YM-002A Fresh Blind E4 Independent Audit (Verifier `b3661f81-ff9a-483f-af3f-13de74b6ede5`) | E4 | `verification/raw/YM-002A_E4_RAW_20260824T084548Z.md` | `0bcaf5cdb43d936f56c15c6d7c5014bb665bfd677f71fda30584919f3585a133` | PROVENANCE_CHALLENGED (IVR-002) | PROVENANCE_CHALLENGED_HISTORICAL |
| EVD-002A-04 | YM-002A Derived E4 Independent Review Report | E4_DERIVED | `verification/YM-002A_INDEPENDENT_REVIEW.md` | Derived from raw `0bcaf5cdb43d936f56c15c6d7c5014bb665bfd677f71fda30584919f3585a133` | PROVENANCE_CHALLENGED (IVR-002) | PROVENANCE_CHALLENGED_HISTORICAL |
| EVD-002AR1-01 | YM-002AR1 Primary source manifest and boundary records (15 papers) | E3 | `literature/primary/foundations_1954_1980/manifest.yaml` | `manifest.yaml` v1.1 verified against local files | MACHINE_CHECKED (`manifest.yaml`) | ACCEPTED |
| EVD-002AR1-02 | YM-002AR1 Machine test suite with semantic regressions (20 foundational tests) | E3 | `tests/test_foundational_literature.py` | Pass receipt `evidence/test_runs/verify_20260824T085502Z.json` | REPRODUCIBLE_LOCALLY (`pytest tests/`) | ACCEPTED |
| EVD-002AR1-03 | YM-002AR1 Fresh Blind E4 Independent Audit (Verifier `9dc7460c-e591-4229-b602-6d8ac5e56026`) | E4 | `verification/raw/YM-002AR1_E4_RAW_20260824T085619Z.md` | `04da3555f8a8dcb6d61f24bdc3abc9578d9407afaa47360fc804d957def6566d` (Candidate SHA: `f718005bb6d326eae36d4e0d627c362a6766858d`) | TRANSCRIPT_LOG_CAPTURED | ACCEPTED |
| EVD-002AR1-04 | YM-002AR1 Derived E4 Independent Review Report | E4_DERIVED | `verification/YM-002AR1_INDEPENDENT_REVIEW.md` | Derived from raw `04da3555f8a8dcb6d61f24bdc3abc9578d9407afaa47360fc804d957def6566d` | TRACEABLE_TO_RAW_E4 | ACCEPTED |



