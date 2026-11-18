# YangMillsBlueprint (`yang-mills-lean4`, `YM101`–`YM141`)

Standalone Lean 4 / Mathlib4 package providing 40 Mathlib-ready foundational modules (`YangMillsBlueprint/MathlibStaging/`) and 41 audited certificate modules (`YM101`–`YM141`, `YangMillsBlueprint/Certificates/`) verified cleanly against `[propext, Classical.choice, Quot.sound]` with zero `sorry`, zero `admit`, zero custom axioms, and zero `native_decide`.

**Scope:** Unconditional Lean 4 formalizations (`YM101`–`YM141`) of finite-volume lattice Yang–Mills cluster expansions, Lie-algebraic rigidity, and conditional continuum reduction hypotheses.  
**Micro-Papers & Companion Archive:** https://github.com/Qamarbajwa/yang-mills-lean4-papers

## Reproduce Locally

```bash
lake exe cache get
lake build
lake env lean YangMillsBlueprint/VerifyNoTraps.lean
```
