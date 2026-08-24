# TAMPER-EVIDENT AUDIT POLICY (v2.9.3)

## Verification Receipt Integrity
- All raw verifier outputs in `verification/raw/` are hashed with SHA-256 immediately upon transcript extraction.
- Derived reviews in `verification/` must record `DERIVED FROM`, `RAW_SHA256`, `VERIFIER CONVERSATION ID`, and `CANDIDATE GIT SHA AUDITED`.
- Modification of any file in `verification/raw/` invalidates the associated E4 receipt.
