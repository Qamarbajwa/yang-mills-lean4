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
public import YangMillsBlueprint.MathlibStaging.IsotropicSuperblockDobrushin

/-!
# Schur-Complement Partial-Trace Contraction Under Interior Mode Elimination

Models integrating out unobserved interior degrees of freedom ("half-observation" Schur
reduction) across a symmetric three-slice quadratic operator with diagonal weights `a`, `d`
and coupling `b`:

* `SchurPartialTraceContraction.schurEff`: reduced boundary stiffness `a - b ^ 2 / d`.
* `SchurPartialTraceContraction.schur_three_slice_complete_sq`: exact three-slice Schur
  completion separating the positive interior Gaussian square `d * (y + (b / d) * (x1 + x2)) ^ 2`
  from the induced two-slice boundary quadratic form.
* `SchurPartialTraceContraction.schurPrecisionCoupling`: normalized induced boundary coupling
  ratio `r ^ 2 / (1 - r ^ 2)`.
* `SchurPartialTraceContraction.schurPrecisionCoupling_lt`: golden-ratio contraction threshold
  `0 < r → r ^ 2 + r < 1 → schurPrecisionCoupling r < r`.
* `SchurPartialTraceContraction.one_sub_schurPrecisionCoupling_eq`: exact gap formula
  `(1 - 2 * r ^ 2) / (1 - r ^ 2)`.
-/

@[expose] public section

namespace SchurPartialTraceContraction

section FieldIdentities

variable {F : Type*} [Field F]

/-- Marginal coarse stiffness `a - b ^ 2 / d` obtained after eliminating interior mode `y`. -/
def schurEff (a b d : F) : F :=
  a - b ^ 2 / d

/-- Induced dimensionless two-slice precision coupling ratio `r ^ 2 / (1 - r ^ 2)` after
integrating out one intermediate slice with normalized step coupling `r`. -/
def schurPrecisionCoupling (r : F) : F :=
  r ^ 2 / (1 - r ^ 2)

/-- Exact two-slice Schur completion identity splitting `a*x^2 + 2*b*x*y + d*y^2`. -/
theorem schur_complete_sq {a b d x y : F} (hd : d ≠ 0) :
    a * x ^ 2 + 2 * b * x * y + d * y ^ 2 =
      schurEff a b d * x ^ 2 + d * (y + (b / d) * x) ^ 2 := by
  unfold schurEff
  field_simp
  ring

/-- Exact three-slice boundary-interior Schur completion identity eliminating interior mode `y`
between boundary modes `x1` and `x2`. -/
theorem schur_three_slice_complete_sq {a b d x1 y x2 : F} (hd : d ≠ 0) :
    a * x1 ^ 2 + d * y ^ 2 + a * x2 ^ 2 + 2 * b * x1 * y + 2 * b * x2 * y =
      schurEff a b d * (x1 ^ 2 + x2 ^ 2) - 2 * (b ^ 2 / d) * x1 * x2 +
        d * (y + (b / d) * (x1 + x2)) ^ 2 := by
  unfold schurEff
  field_simp
  ring

/-- Exact Schur boundary stability gap identity `1 - schurPrecisionCoupling r`. -/
theorem one_sub_schurPrecisionCoupling_eq {r : F} (hden : 1 - r ^ 2 ≠ 0) :
    1 - schurPrecisionCoupling r = (1 - 2 * r ^ 2) / (1 - r ^ 2) := by
  unfold schurPrecisionCoupling
  field_simp
  ring

end FieldIdentities

section OrderedContraction

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Strict positivity of reduced stiffness `schurEff a b d` whenever `0 < d` and `b ^ 2 < a * d`. -/
theorem schurEff_pos {a b d : F} (hd : 0 < d) (hstab : b ^ 2 < a * d) :
    0 < schurEff a b d := by
  unfold schurEff
  have hdiv : b ^ 2 / d < a := (div_lt_iff₀ hd).mpr hstab
  linarith

/-- Golden-ratio partial-trace contraction: whenever `0 < r` and `r ^ 2 + r < 1`, eliminating
an unobserved intermediate slice strictly decreases normalized boundary coupling:
`schurPrecisionCoupling r < r`. -/
theorem schurPrecisionCoupling_lt {r : F} (hr0 : 0 < r) (hgr : r ^ 2 + r < 1) :
    schurPrecisionCoupling r < r := by
  unfold schurPrecisionCoupling
  have hden : 0 < 1 - r ^ 2 := by linarith
  refine (div_lt_iff₀ hden).mpr ?_
  have hdiff : 0 < r * (1 - (r ^ 2 + r)) := mul_pos hr0 (sub_pos.mpr hgr)
  linarith [show r * (1 - r ^ 2) - r ^ 2 = r * (1 - (r ^ 2 + r)) by ring]

/-- Positivity of `schurPrecisionCoupling r` when `r ≠ 0` and `r ^ 2 < 1`. -/
theorem schurPrecisionCoupling_pos {r : F} (hr0 : r ≠ 0) (hr1 : r ^ 2 < 1) :
    0 < schurPrecisionCoupling r := by
  unfold schurPrecisionCoupling
  exact div_pos (sq_pos_of_ne_zero hr0) (sub_pos.mpr hr1)

/-- Strict induced stability margin `0 < 1 - schurPrecisionCoupling r` when `2 * r ^ 2 < 1`. -/
theorem one_sub_schurPrecisionCoupling_pos {r : F} (h2 : 2 * r ^ 2 < 1) :
    0 < 1 - schurPrecisionCoupling r := by
  have hr1 : r ^ 2 < 1 := by
    have hsq : 0 ≤ r ^ 2 := sq_nonneg r
    linarith
  have hden : 0 < 1 - r ^ 2 := sub_pos.mpr hr1
  rw [one_sub_schurPrecisionCoupling_eq (ne_of_gt hden)]
  exact div_pos (sub_pos.mpr h2) hden

end OrderedContraction

end SchurPartialTraceContraction
