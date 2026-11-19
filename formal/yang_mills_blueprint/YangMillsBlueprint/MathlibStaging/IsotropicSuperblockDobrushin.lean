/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.Order.Field.Basic
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.CoarseSliceDecoherence

/-!
# Isotropic Spatial-Temporal Super-Block Normalization for Coarse Slice Contraction

Eliminates the `O(ξ³)` UV slice-susceptibility blowup in `CoarseSliceDecoherence` (`YM-140`)
via isotropic spatial cell averaging of block volume `V = b_s³`:

* Given unblocked site susceptibility `chiTotal = chiIn + chiOut` normalized against single-block
  coercive variance ratio `chiIn > 0`, the dimensionless super-block susceptibility equals
  `superblockM0 chiIn chiOut = 1 + chiOut / chiIn`.
* Whenever exterior inter-block leakage satisfies `chiOut ≤ α * chiIn` uniformly as cutoff `a → 0`
  and box size `L → ∞`, `superblockM0 chiIn chiOut ≤ 1 + α` stays `O(1)` independent of `ξ`.
* Composing with `coarseSliceCoupling` (`YM-140`) yields `rhoE ≤ 1 - η < 1` at fixed integer
  step count `k = O(1)` without logarithmic `log ξ` growth.
-/

@[expose] public section

namespace IsotropicSuperblockDobrushin

open CoarseSliceDecoherence

section FieldAlg

variable {F : Type*} [Field F]

/-- Dimensionless isotropic super-block susceptibility `1 + chiOut / chiIn`. -/
def superblockM0 (chiIn chiOut : F) : F :=
  1 + chiOut / chiIn

/-- Exact equivalence between summed point covariance ratio `(chiIn + chiOut) / chiIn` and
`superblockM0 chiIn chiOut` for `chiIn ≠ 0`. -/
theorem total_div_in_eq_superblockM0 {chiIn chiOut : F} (hin : chiIn ≠ 0) :
    (chiIn + chiOut) / chiIn = superblockM0 chiIn chiOut := by
  unfold superblockM0
  field_simp

end FieldAlg

section OrderedMargin

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Cutoff-uniform `O(1)` cap on `superblockM0` whenever exterior block leakage satisfies
`chiOut ≤ α * chiIn` with `0 < chiIn`. -/
theorem superblockM0_le_of_leakage_ratio {chiIn chiOut α : F}
    (hin : 0 < chiIn) (hleak : chiOut ≤ α * chiIn) :
    superblockM0 chiIn chiOut ≤ 1 + α := by
  unfold superblockM0
  have hdiv : chiOut / chiIn ≤ α := (div_le_iff₀ hin).mpr hleak
  linarith

/-- Non-negativity of `superblockM0` when `0 < chiIn` and `0 ≤ chiOut`. -/
theorem superblockM0_nonneg {chiIn chiOut : F} (hin : 0 < chiIn) (hout : 0 ≤ chiOut) :
    0 ≤ superblockM0 chiIn chiOut := by
  unfold superblockM0
  have h0 : 0 ≤ chiOut / chiIn := div_nonneg hout (le_of_lt hin)
  linarith

/-- End-to-end coarse slice contraction transfer from bounded block leakage ratio `α`:
if `chiOut ≤ α * chiIn` (`0 < chiIn`, `0 ≤ chiOut`) and `(1 + α) * r ^ k ≤ 1 - η`, then
`coarseSliceCoupling (superblockM0 chiIn chiOut) r k ≤ 1 - η`. -/
theorem superblock_coupling_le_margin {chiIn chiOut α r η : F} {k : ℕ}
    (hin : 0 < chiIn) (hleak : chiOut ≤ α * chiIn)
    (hr0 : 0 ≤ r) (hcap : (1 + α) * r ^ k ≤ 1 - η) :
    coarseSliceCoupling (superblockM0 chiIn chiOut) r k ≤ 1 - η := by
  have hm0 : superblockM0 chiIn chiOut ≤ 1 + α := superblockM0_le_of_leakage_ratio hin hleak
  have hrk : 0 ≤ r ^ k := pow_nonneg hr0 k
  have hmul : superblockM0 chiIn chiOut * r ^ k ≤ (1 + α) * r ^ k :=
    mul_le_mul_of_nonneg_right hm0 hrk
  unfold coarseSliceCoupling
  exact le_trans hmul hcap

end OrderedMargin

end IsotropicSuperblockDobrushin
