# INTEGRITY QUARANTINE REGISTER (v2.9.3)

## Active Quarantines

### Q-001: Acceptance-Critical Raw Verifier Artifact Authoring
- **Target Role / Agent:** `primary-writer-gemini` (Worker Agent)
- **Trigger Incidents:** `IVR-001` (YM-001), `IVR-002` (YM-002A)
- **Quarantine Scope:**
  The primary writer is strictly prohibited from authoring, templating, in-memory generating, or overwriting raw verification artifacts in `verification/raw/` and `verification/accepted/`.
- **Enforced Workflow:**
  1. Verifier subagent executes independently in a separate conversation session (`research` read-only subagent).
  2. Raw output is extracted directly from the subagent's execution transcript via `scripts/capture_verifier_output.py`.
  3. Raw SHA-256 is computed directly from disk.
- **Requalification Requirement:**
  Verification pipeline must pass automated regression testing in `tests/test_governance_v293.py` and receive successful independent review under `YM-GOV-293` and `YM-002AR1`.
- **Status:** `ACTIVE_ENFORCEMENT`
