# PROJECT_INTENT.md — TEMPLATE v2.10.1

> Direction layer, file 1 of 3. Owner-authored. This is the authority for WHY.
> The orchestrator reads it at binding and treats it as authority level 4
> (accepted project decisions) in the kernel §0 hierarchy.
> Keep it under one page. If a section is genuinely unknown, write UNKNOWN —
> the orchestrator must not invent it.

## What this product is

<2–4 sentences. What it does, in plain words.>

## Who it is for

<Primary user. One sentence. If there are two very different users, name both.>

## What DONE looks like (current horizon)

<The concrete state at which this phase/version is finished.
Observable, not aspirational. e.g. "A user can X, Y, Z end-to-end without me intervening.">

## Non-goals (explicit)

- <thing the AI must NOT build or optimize for right now>
- <feature deliberately postponed>
- <quality bar deliberately NOT targeted yet, e.g. "no i18n", "no mobile">

## Quality priorities (ordered)

<Rank what wins when trade-offs appear, e.g.:>
1. correctness
2. speed of iteration
3. performance
4. polish

## Hard constraints

- <platform, stack, budget, licensing, privacy, offline, language — whatever is fixed>

## Success signal

<How you (the owner) will judge whether this is working — one line.>

---
intent_version: 1
last_updated: <yyyy-mm-dd>
updated_by: OWNER
# Orchestrator rule: this file is OWNER-authored. The orchestrator may propose
# edits as a diff for approval but never modifies it unilaterally (protected path).
