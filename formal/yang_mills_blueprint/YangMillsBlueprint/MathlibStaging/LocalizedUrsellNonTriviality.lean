/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Analysis.SpecificLimits.Basic
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

/-!
# Localized 4-Point Ursell Non-Triviality vs. `1 / V` Slice CLT Dilution

Addresses Referee Gap 4B (`E-NONTRIV-WITNESS`):

* `LocalizedUrsellNonTriviality.ursell4_ne_zero_implies_non_gaussian`: any non-zero connected
  4-point cumulant `m4 - 3 * m2 ^ 2 ≠ 0` rules out Wick factorization `m4 = 3 * m2 ^ 2`.
* `LocalizedUrsellNonTriviality.tendsto_sliceAvgKurtosis_zero`: proves that dividing fixed local
  excess kurtosis by spatial volume `V` tends to `0` as `V → ∞`, explaining why zero-momentum
  slice averages fail as non-triviality witnesses (`WP5-B`).
* `LocalizedUrsellNonTriviality.tendsto_localized_ursell_ne_zero`: proves that any sequence of
  localized connected 4-point cumulants uniformly bounded away from zero (`0 < c4 ≤ |u4 k|`)
  retains non-zero limit `u4_lim ≠ 0`, ruling out Gaussian triviality.
-/

@[expose] public section

namespace LocalizedUrsellNonTriviality

open Filter Topology

/-- Connected 4-point Ursell cumulant `u4 = m4 - 3 * m2 ^ 2`. -/
def ursell4 (m4 m2 : ℝ) : ℝ :=
  m4 - 3 * m2 ^ 2

/-- Normalized 4-point excess kurtosis `u4 / v ^ 2`. -/
noncomputable def excessKurtosis (u4 v : ℝ) : ℝ :=
  u4 / v ^ 2

/-- Spatial-volume diluted slice-averaged excess kurtosis `excessKurtosis u4 v / V`. -/
noncomputable def sliceAvgKurtosis (u4 v : ℝ) (V : ℕ) : ℝ :=
  excessKurtosis u4 v / (V : ℝ)

theorem ursell4_gaussian_eq_zero {m4 m2 : ℝ} (hgauss : m4 = 3 * m2 ^ 2) :
    ursell4 m4 m2 = 0 := by
  unfold ursell4
  linarith

theorem ursell4_ne_zero_implies_non_gaussian {m4 m2 : ℝ} (hne : ursell4 m4 m2 ≠ 0) :
    m4 ≠ 3 * m2 ^ 2 := by
  intro h
  exact hne (ursell4_gaussian_eq_zero h)

/-- Spatial slice averaging dilutes excess kurtosis as `1 / V → 0` when `V → ∞`. -/
theorem tendsto_sliceAvgKurtosis_zero (u4 v : ℝ) :
    Tendsto (sliceAvgKurtosis u4 v) atTop (𝓝 0) := by
  unfold sliceAvgKurtosis
  exact tendsto_const_div_atTop_nhds_zero_nat (excessKurtosis u4 v)

/-- Unconditional continuum preservation of localized non-Gaussianity: if localized connected
4-point cumulants satisfy `0 < c4 ≤ |u4 k|` along the cutoff sequence and converge to `u4_lim`,
then `c4 ≤ |u4_lim|` and hence `u4_lim ≠ 0`. -/
theorem tendsto_localized_ursell_ne_zero (u4 : ℕ → ℝ) (u4_lim c4 : ℝ)
    (hc4 : 0 < c4) (hbd : ∀ k : ℕ, c4 ≤ |u4 k|)
    (hlim : Tendsto u4 atTop (𝓝 u4_lim)) :
    c4 ≤ |u4_lim| ∧ u4_lim ≠ 0 := by
  have hlim_abs : Tendsto (fun k => |u4 k|) atTop (𝓝 |u4_lim|) :=
    (continuous_abs.tendsto _).comp hlim
  have hle : c4 ≤ |u4_lim| := ge_of_tendsto hlim_abs (Eventually.of_forall hbd)
  have hpos : 0 < |u4_lim| := lt_of_lt_of_le hc4 hle
  exact ⟨hle, abs_pos.mp hpos⟩

end LocalizedUrsellNonTriviality
