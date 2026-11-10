# Truthful reporting, intuition and cross-project link rules

## Claim evidence map
For every reportable claim: (a) exact mathematical statement, domain and quantifiers; (b) claim status; (c) minimum sufficient evidence; (d) counterevidence or explicit lack of search; (e) freshness and affected dependencies; (f) verification authority; (g) limitations; (h) reproducibility method.

- `VERIFIED_FORMAL`: specific frozen formal theorem checked under reported axioms, but semantic audit may remain pending.
- `SEMANTICALLY_AUDITED`: statement-mapping review exists; not necessarily independent acceptance.
- `INDEPENDENTLY_ACCEPTED`: exact reviewed proof package approved by distinct qualified acceptor.
- `CONJECTURAL`: plausible but unproved; report precisely.
- `REFUTED`: counterexample or proof of negation sufficient for specified claim; preserve scope.
- `UNKNOWN`: not examined, unsupported or inaccessible—never map to zero or true.

Bidirectional check is mandatory: (1) no narrative claim stronger than evidence and (2) no relevant, supported outcome quietly absent from report. Absence from a summary may be a format choice; absence from full claim inventory is a governance finding.

## Interpretation lifecycle
`USER_RAW_UTTERANCE` (unaltered) -> `TENTATIVE_INTERPRETATIONS[]` (could be multiple) -> `OWNER_APPROVED_MEANING` OR `UNRESOLVED/REJECTED`. Mathematical links may be useful without agreeing a formal interpretation; preserve why a mapping was not selected.

## Link taxonomy
`DEDUCED_IMPLICATION` (proof required), `DEPENDENCY` (technical prerequisite), `SPECIAL_CASE` (scope map), `EQUIVALENCE` (two-way proof), `ANALOGY` (heuristic only), `POSSIBLE_RELEVANCE` (hypothesis), `CONTRADICTION` (with evidence), `REJECTED_LINK` (reason and boundaries), `UNASSESSED` (not checked). No implied inference from analogical similarity or mere shared vocabulary.
