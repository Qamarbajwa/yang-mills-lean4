# YM-002E — CLAIMED-SOLUTION ADVERSARIAL AUDIT LEDGER

- **TASK_ID:** `YM-002E`
- **STATUS:** `RELEASED_IN_PROGRESS`
- **RELEASE_AUTHORITY:** Human project owner acceptance recorded in `governance/HUMAN_OWNER_ACCEPTANCE_ROS_v1.0_20260830.md`.
- **SCOPE:** Adversarial screening of quarantined claims against the official Yang–Mills existence and mass-gap obligations.
- **NON-NEGOTIABLE RULE:** No claim is promoted to a solution without an identifiable primary artifact, complete scope, and evidence addressing the continuum, infinite-volume, universal-group, axiomatic-QFT, nontriviality, and positive-gap obligations.

## Initial audit basis

The local queue contains three quarantined claim classes in `literature/CLAIM_QUARANTINE_REGISTER.md`. The official Clay status page still states that no proof of the mass-gap property is known; this ledger therefore treats each external claim as unaccepted until its exact source and proof obligations are independently checked.

## Claim findings

### CLAIM-2024-001 — Sky Yang, 2024

- **Local claim:** 4D continuum mass-gap proof via effective action / spectral analysis.
- **Primary-artifact identity:** `MISSING` — no DOI, URL, version, content hash, or local full text is bound in the quarantine register.
- **Adversarial result:** `NOT_ACCEPTED_PROVENANCE_INSUFFICIENT`.
- **Required follow-up:** Supply the exact primary artifact and test its construction against the official axioms, universal compact-simple-group quantifier, pure-Yang–Mills field content, nontriviality, continuum/infinite-volume limits, and uniform positive spectral gap.

### CLAIM-2025-001 — Various preprints

- **Local claim:** Mass gap from truncated Schwinger–Dyson equations / ghost-gluon vertex ansatz.
- **Primary-artifact identity:** `MISSING` — the register names no specific authors, title, identifier, version, or hash.
- **Adversarial result:** `NOT_ACCEPTED_PROVENANCE_INSUFFICIENT`.
- **Known failure condition:** A truncation or ansatz is not a proof without controlled nonperturbative error bounds and a demonstrated bridge to the exact 4D pure-Yang–Mills theory.
- **Required follow-up:** Bind each claimed preprint separately and audit truncation closure, gauge consistency, continuum control, and spectral positivity.

### CLAIM-2026-001 — Various preprints

- **Local claim:** Continuum limit from finite-lattice approximations.
- **Primary-artifact identity:** `MISSING` — the register names no specific authors, title, identifier, version, or hash.
- **Adversarial result:** `NOT_ACCEPTED_PROVENANCE_INSUFFICIENT`.
- **Known failure condition:** The local verified lattice records explicitly distinguish fixed-cutoff or strong-coupling lattice results from the required weak-coupling continuum limit and uniform infinite-volume spectral gap.
- **Required follow-up:** Bind each claimed preprint separately and audit both joint limits `a → 0`, `V → ∞`, and uniform lower spectral bounds for the target theory.

## Intake conclusion

- `CLAIM-2024-001`: remains quarantined.
- `CLAIM-2025-001`: remains quarantined.
- `CLAIM-2026-001`: remains quarantined.
- `NO_UNSUPPORTED_SOLUTION_CLAIM_ACCEPTED`: `TRUE`.
- `YM-002E`: remains `IN_PROGRESS`; closing requires claim-specific primary artifacts, adversarial findings, and the task’s independent review/evidence gate.

External context: [Clay Mathematics Institute — Yang–Mills & the Mass Gap](https://www.claymath.org/millennium/yang-mills-the-maths-gap/).

## Source-resolution addendum

The 2026-08-30 source-resolution and adversarial triage pass is recorded in `verification/YM-002E_SOURCE_RESOLUTION_20260830.md`. It resolved several relevant primary-paper leads but did not establish exact identity for any of the three internal queue rows. The leads remain non-bound and quarantined; no claim was promoted.

- `CLAIM-2024-001`: source identity unresolved.
- `CLAIM-2025-001`: queue identity unresolved; DSE/gluon-propagator lead triaged as insufficient for the Clay target.
- `CLAIM-2026-001`: queue identity unresolved; conditional single-group continuum lead triaged as insufficient for the Clay target.
- Separate `SU(3)` proof lead: recorded as unassigned and quarantined, not silently attached to a queue row.

## Byte-level source binding

The three artifact leads named for the next audit phase now have local source records and SHA-256 bindings in `evidence/primary/YM-002E/`:

- Ferreira et al., arXiv `2508.20568v1`: `7c78d18c6e6222d114a05c3852b3814f45e15261fc97d336dcd0f9df46db5c30`.
- Kirk, Zenodo `18824739` v1.0: `13b9fc8cb7109f8f55cca7b285417458bd9a2b99faccf11bc483f25d26fcd3e1`; Zenodo MD5 reconciled.
- Jacobsen, arXiv `2506.00284v1` source: `f97569b3bd122de923d6d7a642ec24bccb319f8e215fa1f6f4781a241efcf51`.

This binding does not rewrite the legacy `CLAIM-2024-001 — Sky Yang` entry, whose exact artifact remains unresolved.

## Claim-level audit result

The E3 claim-level audit is recorded in `verification/YM-002E_CLAIM_LEVEL_AUDIT_20260830.md`. Ferreira is classified as a related mechanism result rather than a solution claim; Kirk is conditional on unproved `WC1–WC3` and limited to `SU(2)`; Jacobsen v1 is quarantined because proof completeness and source traceability remain unverified and the artifact is limited to `SU(3)`, with v2 withdrawal recorded only as provenance. The legacy Sky Yang row remains unresolved. No claim was promoted.
