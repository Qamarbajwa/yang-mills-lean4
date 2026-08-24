# ACCEPTANCE GATE POLICY (v2.9.4)

## 1. Acceptance Authority Invariant
- `ACCEPTANCE_AUTHORITY` is a **functional role**, not a model, provider, or company.
- Universal provider or model authority (e.g. Codex, OpenAI, Gemini, Claude, DeepSeek) is prohibited.
- Technical acceptance is **environment-local**:
  - `Antigravity`: Gemini Writer -> Separate Gemini Reviewer -> E3 Deterministic Tests -> Antigravity Local Acceptance Gate.
  - `Claude Code`: Claude Writer -> Separate Claude Reviewer -> E3 Deterministic Tests -> Claude Code Local Acceptance Gate.
  - `OpenCode`: OpenCode Writer -> Distinct OpenCode Reviewer -> E3 Deterministic Tests -> OpenCode Local Acceptance Gate.

## 2. Gate Sequence for Consequential Contracts (T3+)
```
CANDIDATE
    -> EVIDENCE_ATTACHED
    -> MACHINE_CHECKED (E3)
    -> INDEPENDENT_REVIEW (E4)
    -> INTEGRITY_CHECKED
    -> ENVIRONMENT_LOCAL_ACCEPTANCE
    -> ACCEPTED
```

## 3. Distinction Between Technical Acceptance and Release Authority
- Environment-local technical acceptance = `BOUNDED TECHNICAL CONTRACT ACCEPTED`.
- It does NOT constitute `RELEASE_READY` or `PRODUCTION_AUTHORIZED`.
- T4/T5 governance or deployment changes retain distinct `HUMAN_AUTHORITY` authorization.

## 4. Stale Evidence Invalidation
- If any material candidate artifact changes after review, `OLD EVIDENCE = STALE`.
- Full E3 machine verification and E4 independent review must be rerun against the exact final candidate.

## 5. Execution Identity Separation vs Role Name Inequality
- `ROLE_NAME DIFFERENCE != EXECUTION IDENTITY SEPARATION`.
- For T3+ contracts, the writer execution identity (`writer.execution_id`) and reviewer execution identity (`reviewer.execution_id`) must be distinct.
- A single agent cannot satisfy independent technical acceptance merely by renaming its role from `primary-writer` to `local-orchestrator` within the same execution session (`writer.execution_id == acceptance_authority.execution_id`).
- Independent technical acceptance must bind to a distinct subagent session, deterministic CI evaluator, or the Human Project Owner.


