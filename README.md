# YangMillsBlueprint (`yang-mills-lean4`, `YM101`–`YM140`, v1.3.0)

Standalone Lean 4 / Mathlib4 package providing 39 Mathlib-ready foundational modules (`YangMillsBlueprint/MathlibStaging/`) and 40 audited certificate modules (`YM101`–`YM140`, `YangMillsBlueprint/Certificates/`) verified cleanly against `[propext, Classical.choice, Quot.sound]` (`2925` Lake jobs, `294` audited theorems, `38` nonempty certificate structures) with zero `sorry`, zero `admit`, zero custom axioms, and zero `native_decide`.

**Epistemic Status:** `clay_problem: OPEN_AND_UNSOLVED` | `goal_complete: false`  
**Micro-Papers & Companion Archive:** https://github.com/Qamarbajwa/yang-mills-lean4-papers

## Reproduce Locally

```bash
lake exe cache get
lake build
lake env lean YangMillsBlueprint/VerifyNoTraps.lean
```
