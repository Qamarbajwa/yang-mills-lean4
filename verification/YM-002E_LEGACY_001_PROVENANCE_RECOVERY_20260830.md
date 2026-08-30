# YM-002E-LEGACY-001 — Provenance Recovery for CLAIM-2024-001

- Date: `2026-08-30`
- Task: `YM-002E-LEGACY-001`
- Parent YM-002E candidate: `176606c358137ebc8a80e4129abc16c6c4b2b206`
- Scope: bounded repository-history and historical-ledger recovery; no broad web search and no silent source substitution.

## Search performed

The following were searched across all reachable Git revisions and the current repository:

- `CLAIM-2024-001`
- `Sky Yang`
- `Sky Cao`
- `Sky Yang Cao`
- `2024`
- `mass gap`
- `claimed proof`
- `solution`
- URLs, DOI/arXiv identifiers, title fragments, quotes, imported-source notes, and source-resolution notes associated with the legacy row.

Commands included `git log --all -S...`, `git log --all -G...`, revision-wide `git grep`, full-history path inspection, and direct inspection of the introducing commit and its parent.

## Recovered provenance

- `CLAIM-2024-001` first appears in commit `d9fc71a4867f5a695d5b50401bdd9cb569477148` (`2026-08-25`, subject `YM-002CR1: candidate modern literature scope, taxonomy, and completeness repair`).
- The quarantined register is newly added in that commit; its parent `a97f0dfb2f4c8a1026d3664219537ad9890376c1` has no `literature/CLAIM_QUARANTINE_REGISTER.md`.
- The originating row contains only the legacy author string `Sky Yang`, year `2024`, a generic claim summary, a generic proposed mechanism, a quarantine reason, and task assignment. It contains no URL, title, author detail, date beyond the year, DOI, arXiv identifier, quote, imported source, or content hash.
- Later revisions preserve the row but add no primary-source identity. No Git revision contains `Sky Cao` or `Sky Yang Cao`.
- Therefore the repository contains no recoverable provenance that uniquely identifies a claim artifact.

## Identity hypothesis boundary

The continuation checkpoint supplied an external candidate hypothesis `Sky Yang Cao / Sky Cao`. That hypothesis is recorded as a lead only; it is not present in repository provenance and is not bound to any artifact. `AUTHOR_IDENTITY_CANDIDATE` therefore remains `HIGH_BUT_NOT_PROVEN_FROM_LEGACY_RECORD`, not an identity resolution.

## Final bounded disposition

```text
CLAIM-2024-001
AUTHOR_STRING_LEGACY: Sky Yang
AUTHOR_IDENTITY_CANDIDATE: Sky Yang Cao / Sky Cao
AUTHOR_IDENTITY_CONFIDENCE: HIGH_BUT_NOT_PROVEN_FROM_LEGACY_RECORD
PRIMARY_ARTIFACT: UNRESOLVED
CLAIMED_CLAY_SOLUTION_ARTIFACT: NOT_IDENTIFIED_AFTER_BOUNDED_REPOSITORY_PROVENANCE_RECOVERY
STATE: UNRESOLVED_ORPHANED_LEGACY_CLAIM
CLAIM_ACCEPTANCE: NOT_ACCEPTED_PROVENANCE_INSUFFICIENT
```

The original quarantine row is not deleted or rewritten. No Sky Cao artifact is silently assigned to it. This disposition satisfies the bounded provenance-recovery branch of `YM-002E` and permits final claim-obligation synthesis, subject to candidate-bound E3 and independent E4 closeout.
