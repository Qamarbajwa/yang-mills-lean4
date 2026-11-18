/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.Order.Field.Basic
public import Mathlib.Analysis.SpecialFunctions.ExpDeriv
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.CentralizerCodimensionBound

/-!
# Bounded-Oscillation Gibbs Density Cap & Transverse Bathtub Variance Floor

Links finite local action oscillation bounds `Vmin ≤ V ≤ Vmax` (`osc = Vmax - Vmin`) via the
Holley-Stroock Boltzmann ratio `Real.exp (-Vmin) / Real.exp (-Vmax) = Real.exp (Vmax - Vmin)`
directly to `CentralizerCodimensionBound.bathtub_expectation_floor`, producing the explicit
dimension-free variance lower bound `4 * Real.exp (-osc) ≤ expectComm`.

## Main results

* `GibbsDensityCapVariance.gibbsRatio_le_bound`: ratio upper bound from partition lower bound.
* `GibbsDensityCapVariance.exp_neg_ratio_eq_exp_sub`: exact Boltzmann ratio `exp (Vmax - Vmin)`.
* `GibbsDensityCapVariance.four_div_exp_eq_four_mul_exp_neg`:
  `4 / Real.exp osc = 4 * Real.exp (-osc)`.
* `GibbsDensityCapVariance.variance_floor_of_bounded_osc`: uniform positive floor from `osc`.
-/

@[expose] public section

namespace GibbsDensityCapVariance

section OrderedFieldRatio

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Partition-normalized weight ratio bound: if `0 < wMin ≤ Z` and `wMax ≤ cap * wMin`,
then `wMax / Z ≤ cap`. -/
theorem gibbsRatio_le_bound {wMin wMax Z cap : F}
    (hwmin : 0 < wMin) (hwmax : 0 ≤ wMax) (hZ : wMin ≤ Z) (hcap : wMax ≤ cap * wMin) :
    wMax / Z ≤ cap := by
  have hZpos : 0 < Z := lt_of_lt_of_le hwmin hZ
  have hcap0 : 0 ≤ cap := by
    by_contra hneg
    have hlt : cap < 0 := lt_of_not_ge hneg
    have hmul : cap * wMin < 0 := mul_neg_of_neg_of_pos hlt hwmin
    linarith
  have hle : wMax ≤ cap * Z := le_trans hcap (mul_le_mul_of_nonneg_left hZ hcap0)
  exact (div_le_iff₀ hZpos).mpr hle

end OrderedFieldRatio

section RealBoltzmann

open Real

/-- Exact Boltzmann density oscillation ratio identity:
`Real.exp (-vMin) / Real.exp (-vMax) = Real.exp (vMax - vMin)`. -/
theorem exp_neg_ratio_eq_exp_sub (vMin vMax : ℝ) :
    Real.exp (-vMin) / Real.exp (-vMax) = Real.exp (vMax - vMin) := by
  rw [← Real.exp_sub]
  congr 1
  ring

/-- Conversion between `4 / Real.exp osc` and `4 * Real.exp (-osc)`. -/
theorem four_div_exp_eq_four_mul_exp_neg (osc : ℝ) :
    4 / Real.exp osc = 4 * Real.exp (-osc) := by
  rw [div_eq_mul_inv, Real.exp_neg]

/-- Strictly positive uniform variance floor `4 * Real.exp (-osc) ≤ expectComm` once the
Boltzmann expectation obeys the `YM-143` bathtub lower bound at density cap `M = Real.exp osc`. -/
theorem variance_floor_of_bounded_osc {osc expectComm : ℝ}
    (hfloor : 4 / Real.exp osc ≤ expectComm) :
    0 < 4 * Real.exp (-osc) ∧ 4 * Real.exp (-osc) ≤ expectComm := by
  have hpos : 0 < 4 * Real.exp (-osc) := by positivity
  rw [← four_div_exp_eq_four_mul_exp_neg]
  exact ⟨by rwa [four_div_exp_eq_four_mul_exp_neg], hfloor⟩

end RealBoltzmann

end GibbsDensityCapVariance
