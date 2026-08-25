# ROADMAP.md — TEMPLATE v2.10.1

> Direction layer, file 3 of 3. Co-authored: owner sets goals, orchestrator
> decomposes them into governed increments and maintains this file as part of
> UPDATE CANONICAL STATE. This is the authority for WHAT'S NEXT.
>
> Kernel §21 rule: `SELECT NEXT VALID INCREMENT` = the top READY item below.
> Empty or ambiguous roadmap → owner escalation (kernel §18), never invention.

## How to read this file

- Increments are ordered. Top READY item is next.
- Each increment maps 1:1 to a future task execution envelope:
  `objective` → envelope objective, `done_when` → acceptance_criteria.
- Status: `READY | BLOCKED(<by>) | IN_PROGRESS(<envelope id>) | DONE(<envelope id>) | DROPPED(<why>)`
- The orchestrator updates status; it adds/reorders/splits increments only as
  a proposal for owner approval, except splitting one READY item into smaller
  increments with the same combined scope, which is autonomous.

## Current goal (owner-set)

<One sentence: the goal this batch of increments serves. Must trace to PROJECT_INTENT.>

## Increments

### INC-001 — <short name>
- objective: <exact, testable objective — what, not how>
- done_when:
  - <observable criterion>
  - <observable criterion>
- expected_risk: T1 | T2 | T3 | T4
- depends_on: NONE | INC-xxx
- status: READY

### INC-002 — <short name>
- objective: <...>
- done_when:
  - <...>
- expected_risk: <...>
- depends_on: <...>
- status: READY

<!-- Add more. Keep increments small: one bounded contract each.
     If an increment needs >1 envelope, it should have been split. -->

## Parked / later

<Ideas deliberately not in the current batch. Prevents scope creep and
prevents fresh sessions from "helpfully" starting these.>

- <parked item>

## Completed (rolling log)

| Increment | Envelope | Accepted on | Notes |
|---|---|---|---|
| | | | |

---
roadmap_version: 1
last_updated: <yyyy-mm-dd>
