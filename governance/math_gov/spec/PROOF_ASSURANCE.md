# Lean proof assurance and semantic fidelity

## Separate five different facts
1. A worker wrote a formal Lean proof candidate. This proves NOTHING until checked.
2. A local `lake build` reports success. It checks compiling included files but does not by itself prove that the *intended human statement* was formalized, nor that unapproved axioms were absent.
3. A host-controlled Lean kernel check of frozen sources was successful under explicit permitted axioms. This supports only the exact formal proposition in that environment.
4. `lake comparator` compares independent trusted challenge to submitted proof for named theorem(s); this strengthens statement-mismatch detection but the challenge itself still requires a qualified semantic audit.
5. Mathematical acceptance requires independent reviewer+acceptor, proof obligation closure, assumptions, exact scope, meaning, and reproducibility. Publication adds novelty and venue requirements.

## Exact checklist per theorem and lemma
- Independent theorem statement with approved math meaning/domain/quantifiers/assumptions/axioms.
- Version-frozen `lean-toolchain`, `lake-manifest.json`, import graph and source/tree digest.
- Confirm the target file is built and proof target name is exact; no shadowed namespace, vacuity or self-defined theorem names masquerading as intended result.
- Run isolated `lake build`, `#print axioms TargetName` and parse/report all transitive axiom dependencies. `sorryAx` is fatal for accepted theorem; nonstandard axioms must be explicitly allowed and justified.
- Lean 4.35+ supports `lake check --paranoid`; verify installed exact CLI version and sandbox needs, plus trusted `lake comparator --config=...` with independent challenge and frozen configuration. These are planned host-side gates, not executed by this package.
- Preserve exact command invocation, environment, exit code, stdout/stderr, source and target hashes, verifier identity and toolchain provenance. No fabricated logs.
- Review the meaning of definitions and any possible vacuous true hypotheses or hidden contradictory assumptions.
- Every changed formal dependency invalidates prior proof certificates until full re-run on exact new tree.

## Illustrative small proof (NOT a claimed executed theorem)
```
example (x : Nat) : x = x := by
  rfl
```
A semantic audit should confirm the intended proposition actually corresponds to the English question; the demonstration above says nothing about any research-level theorem.

## Relevant official docs
- https://lean-lang.org/doc/reference/latest/Axioms/
- https://lean-lang.org/doc/reference/latest/releases/v4.35.0/
- https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/
