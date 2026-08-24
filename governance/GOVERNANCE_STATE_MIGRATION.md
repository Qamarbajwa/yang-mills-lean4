# GOVERNANCE STATE MIGRATION

- **CURRENT_MODE:** `HYBRID_DISCOVERY`
- **TARGET_MODE:** `CANONICAL`
- **CURRENT_GOVERNANCE_VERSION:** `2.9.3`
- **PREVIOUS_GOVERNANCE_VERSION:** `2.9`
- **MIGRATION_TASK_ID:** `YM-GOV-293`

---

## Migration Status and Discrepancies

### Canonical Ownership Already Established
- `governance/GOVERNANCE_VERSION_MANIFEST.yaml`: Authoritative manifest of all active and historical governance constitutions and hashes.
- `governance/CODING_ENVIRONMENT_PROFILE.yaml`: Discovered platform and tool profile.
- `governance/AGENT_CAPABILITY_REGISTRY.yaml`: Active agent roles, permissions, and risk tiers.
- `governance/MODEL_TOOL_ROUTING.yaml`: Dynamic routing matrix.
- `governance/TOOL_PERMISSION_MATRIX.yaml`: Tool authority boundaries.

### Fields Still Hybrid / Markdown-Authoritative
- Theorem definitions and literature extractions (`THEOREM_LEDGER.md`, `OFFICIAL_PROBLEM_SPECIFICATION.md`).
- Historical integrity register (`INTEGRITY_VIOLATION_REGISTER.md`).
- Negative findings (`NEGATIVE_EVIDENCE_REGISTER.md`).

### Discrepancies Tracked
- `DISC-001`: YM-002A initial acceptance was challenged under IVR-002 and is undergoing formal E4 re-audit under v2.9.3.
- `DISC-002`: Tool isolation on Windows is logical/process-based (soft control) supported by transcript cryptographic hashing.

### Next Migration Step
Reconcile theorem ledger and problem specification into structured schema validation during Task `YM-003`.
