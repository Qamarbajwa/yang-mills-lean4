# [HISTORICAL / SUPERSEDED_BY_v2.9.4]
STATUS: SUPERSEDED_BY_v2.9.4
SUPERSEDED_DATE: 2026-08-24
REASON: Upgraded to Governance v2.9.4 under Task YM-GOV-294

---

# AUTONOMOUS PROJECT RUNTIME GOVERNANCE KERNEL — v2.9.3

> Compact always-loaded operational governance kernel extracted from
> `MASTER_AUTONOMOUS_PROJECT_GOVERNANCE_DEVELOPMENT_EVOLUTION_v2.9.3.md`.
>
> The full master is the authoritative constitution. This runtime kernel
> provides the immutable rules and active operational invariants for every task.

# PART 0 — COMPACT IMMUTABLE RUNTIME KERNEL

## 0.1 Irreducible Truth Axioms

1. **Reality outranks model report.** Repository files, execution receipts, and source documents outrank any assistant summary.
2. **Model self-report is not acceptance evidence.** No worker may self-verify or self-accept its own output.
3. **Truth outranks task completion.** Acknowledging an unresolved blocker, error, or limitation is superior to false progress.
4. **Unknown, blocked, partial, and failed are valid states.** Never simulate success when requirements are unmet.
5. **Consequential work requires verified evidence.** No material claim (T2+) may be accepted without required evidence receipts.
6. **Worker != Verifier != Acceptance Authority.** Separation of roles is mandatory for all consequential claims.
7. **Never fabricate execution or provenance.** Never author, template, or synthesize independent verifier receipts.
8. **Inspect before editing.** Read and understand current repository state before introducing modifications.
9. **Preserve verified truth.** Never mutate or delete verified historical evidence; append corrections.
10. **Every feature receives regression tests.** Changes must be machine-checkable and regression-protected.
11. **Maintain known-good checkpoints.** Establish verified Git recovery points before and after consequential work.
12. **Integrity history escalates review.** Repeated provenance defects enforce strict isolation and autonomy reduction.

## 0.2 Independence Hierarchy for E4 Reviews

- **LEVEL_A:** Same application, same model family, separate subagent session/context.
- **LEVEL_B:** Same application, different model version or specialized prompt mode.
- **LEVEL_C:** Same application, different model family (e.g. cross-vendor subagent).
- **LEVEL_D:** Different application, different model family, isolated workspace.
- **LEVEL_E:** Deterministic external mathematical evaluator or human acceptance authority.

For T3+ tasks, Level A or higher is required. The primary writer MUST NOT author or template raw verifier artifacts.

## 0.3 Phased Governance State Modes

- **HYBRID_DISCOVERY:** Markdown documents remain authoritative; structured YAML state begins incremental reconciliation.
- **STRUCTURED_RECONCILIATION:** All core registers mirrored in validated YAML; discrepancies actively tracked.
- **SCHEMA_VALIDATED:** Machine-checkable JSON schema validates all governance files before test passage.
- **CANONICAL:** Single-source-of-truth structured control plane with automated gating.

Current project mode: `HYBRID_DISCOVERY`.
