# ARCHITECTURE_DECISIONS.md — TEMPLATE v2.10.1

> Direction layer, file 2 of 3. Co-authored: filled by the orchestrator during
> binding, approved by the owner. This is the authority for SHAPE.
> Fresh sessions read this instead of relitigating settled choices.
> Changing a DECIDED entry is a T3 governed change, not a session preference.

## Stack (decided)

| Layer | Choice | Status |
|---|---|---|
| Language(s) | <e.g. Rust> | DECIDED |
| Framework(s) | <e.g. Tauri v2, wgpu> | DECIDED |
| Storage | <...> | DECIDED / OPEN |
| Build/CI | <...> | DECIDED / OPEN |

## Module map (decided boundaries)

<Short list of top-level modules/components and their single responsibility.
One line each. This is the map workers use before editing anything.>

- `<module>` — <responsibility> — stability: EXPERIMENTAL | STABLE | PROTECTED

## Key contracts (settled interfaces/semantics)

<Interfaces, data shapes, invariants that many modules depend on.
Changing any of these = shared semantic change = at least T3.>

- <contract 1>
- <contract 2>

## Decision log (append-only)

| # | Date | Decision | Why | Alternatives rejected |
|---|---|---|---|---|
| 1 | <date> | <what was decided> | <one line> | <one line> |

## Open questions (not yet decided)

<Things intentionally undecided. The orchestrator must not silently decide
these; deciding one = a decision-log entry + owner approval.>

- <open question 1>

---
architecture_version: 1
last_updated: <yyyy-mm-dd>
# Orchestrator rule: append to the decision log, never rewrite history.
# DECIDED entries are re-openable only via a governed T3 exception with owner approval.
