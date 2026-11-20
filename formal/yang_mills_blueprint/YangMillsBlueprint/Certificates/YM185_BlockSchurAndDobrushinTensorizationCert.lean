/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import Mathlib.Basic.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp

/-!
# YM-185: Volume-Uniform Dobrushin Slice Tensorization & Block-Schur Innovation

Formalizes three unconditional structural theorems extending `YM183`–`YM184`:
1. `dobrushin_slice_tensorization_contraction_unconditional`: For any spatial volume
   `N + 1` (`Fin (N + 1)`), if a non-negative time-slice correlation vector `v : ℕ → Fin (N + 1) → ℝ`
   satisfies `v (t + 1) i ≤ Γ₀ * v t i + ∑ j : Fin (N + 1), c i j * v t j` with
   `0 ≤ Γ₀`, `0 ≤ c i j`, `∑ j, c i j ≤ γ_spatial`, and `M_t = sup_i v t i`, then
   `∀ t i, v t i ≤ (Γ₀ + γ_spatial) ^ t * M_0` uniformly in spatial volume `N + 1`.
2. `schur_complement_positivity_and_cholesky_step_unconditional`: For any `a > 0`, `d > 0`,
   and `b^2 < a * d`, the Schur complement `s = d - b^2 / a` satisfies `0 < s`, `s ≤ d`,
   `a * s = a * d - b^2 > 0`, and `-b^2 / a < 0` whenever `b ≠ 0`.
3. `volume_uniform_exponential_clustering_unconditional`: Exact identity
   `Γ_unif ^ t = Real.exp (-(-Real.log Γ_unif / ℓ_IR) * ((t : ℝ) * ℓ_IR))` for all
   `0 < Γ_unif < 1`, `ℓ_IR > 0`, and `t : ℕ`.
-/

namespace YangMillsBlueprint.Certificates

structure DobrushinTensorCert where
  gamma0 : ℝ
  gammaSpatial : ℝ
  ellIR : ℝ
  hG0 : 0 ≤ gamma0
  hGsp : 0 ≤ gammaSpatial
  hSum : gamma0 + gammaSpatial < 1
  hEll : 0 < ellIR

noncomputable def canonicalDobrushinTensorCert : DobrushinTensorCert where
  gamma0 := 3020 / 10000
  gammaSpatial := 328 / 10000
  ellIR := 1
  hG0 := by norm_num
  hGsp := by norm_num
  hSum := by norm_num
  hEll := by norm_num

instance : Nonempty DobrushinTensorCert :=
  ⟨canonicalDobrushinTensorCert⟩

/-- **UNCONDITIONAL (Volume-Uniform Dobrushin Slice Tensorization):**
For any spatial block count `N + 1`, if `v (t + 1) i ≤ Γ₀ * v t i + ∑ j, c i j * v t j`
with `0 ≤ Γ₀`, `0 ≤ c i j`, `∑ j, c i j ≤ γ_spatial`, and `∀ i, 0 ≤ v 0 i ∧ v 0 i ≤ M₀`,
then `v t i ≤ (Γ₀ + γ_spatial) ^ t * M₀` uniformly in `N` for all `t : ℕ` and `i`. -/
theorem dobrushin_slice_tensorization_contraction_unconditional
    (N : ℕ) (v : ℕ → Fin (N + 1) → ℝ) (c : Fin (N + 1) → Fin (N + 1) → ℝ)
    (gamma0 gamma_spatial M0 : ℝ)
    (hG0 : 0 ≤ gamma0) (hGsp : 0 ≤ gamma_spatial) (hM0 : 0 ≤ M0)
    (hc_nonneg : ∀ i j, 0 ≤ c i j)
    (hc_row : ∀ i, (∑ j : Fin (N + 1), c i j) ≤ gamma_spatial)
    (hv0 : ∀ i, 0 ≤ v 0 i ∧ v 0 i ≤ M0)
    (hv_step : ∀ t i, v (t + 1) i ≤ gamma0 * v t i + ∑ j : Fin (N + 1), c i j * v t j)
    (_hv_nonneg : ∀ t i, 0 ≤ v t i) :
    ∀ t : ℕ, ∀ i : Fin (N + 1), v t i ≤ (gamma0 + gamma_spatial) ^ t * M0 := by
  intro t
  induction t with
  | zero =>
    intro i
    simpa using (hv0 i).2
  | succ m ih =>
    intro i
    have hPowNonneg : 0 ≤ (gamma0 + gamma_spatial) ^ m * M0 :=
      mul_nonneg (pow_nonneg (by linarith) m) hM0
    have hDiag : gamma0 * v m i ≤ gamma0 * ((gamma0 + gamma_spatial) ^ m * M0) :=
      mul_le_mul_of_nonneg_left (ih i) hG0
    have hSum :
        (∑ j : Fin (N + 1), c i j * v m j) ≤
          (∑ j : Fin (N + 1), c i j) * ((gamma0 + gamma_spatial) ^ m * M0) := by
      rw [Finset.sum_mul]
      refine Finset.sum_le_sum (fun j _ => ?_)
      exact mul_le_mul_of_nonneg_left (ih j) (hc_nonneg i j)
    have hRow :
        (∑ j : Fin (N + 1), c i j) * ((gamma0 + gamma_spatial) ^ m * M0) ≤
          gamma_spatial * ((gamma0 + gamma_spatial) ^ m * M0) :=
      mul_le_mul_of_nonneg_right (hc_row i) hPowNonneg
    have hStep := hv_step m i
    have hPow :
        (gamma0 + gamma_spatial) ^ (m + 1) * M0 =
          gamma0 * ((gamma0 + gamma_spatial) ^ m * M0) +
            gamma_spatial * ((gamma0 + gamma_spatial) ^ m * M0) := by
      rw [pow_succ']
      ring
    linarith

/-- **UNCONDITIONAL (Block-Schur Positivity & Cholesky Innovation Step):**
For `a > 0`, `d > 0`, and `b^2 < a * d`, the Schur complement `s = d - b^2 / a`
obeys `0 < s ≤ d`, `a * s = a * d - b^2 > 0`, and `b ≠ 0 → -b^2 / a < 0`. -/
theorem schur_complement_positivity_and_cholesky_step_unconditional
    (a b d : ℝ) (ha : 0 < a) (_hd : 0 < d) (hdet : b ^ 2 < a * d) :
    let s := d - b ^ 2 / a
    0 < s ∧ s ≤ d ∧ a * s = a * d - b ^ 2 ∧ (b ≠ 0 → -(b ^ 2 / a) < 0) := by
  dsimp only
  have hane : a ≠ 0 := ne_of_gt ha
  have hmul : a * (d - b ^ 2 / a) = a * d - b ^ 2 := by
    field_simp [hane]
  have has_pos : 0 < a * (d - b ^ 2 / a) := by linarith
  have hs_pos : 0 < d - b ^ 2 / a := by
    by_contra hle
    push Not at hle
    have : a * (d - b ^ 2 / a) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos (le_of_lt ha) hle
    linarith
  have hsq_nonneg : 0 ≤ b ^ 2 / a := div_nonneg (sq_nonneg b) (le_of_lt ha)
  refine ⟨hs_pos, by linarith, hmul, ?_⟩
  intro hb
  have hb2 : 0 < b ^ 2 := sq_pos_of_ne_zero hb
  have hdiv : 0 < b ^ 2 / a := div_pos hb2 ha
  linarith

/-- **UNCONDITIONAL (Volume-Uniform Exponential Clustering Identity):**
For `0 < Γ_unif < 1` and `ℓ_IR > 0`, the `t`-step transfer decay `Γ_unif ^ t` equals
`Real.exp (-m_phys * ((t : ℝ) * ℓ_IR))` with `m_phys = -Real.log Γ_unif / ℓ_IR > 0`. -/
theorem volume_uniform_exponential_clustering_unconditional
    (gamma_unif ell_IR : ℝ) (t : ℕ)
    (hg0 : 0 < gamma_unif) (hg1 : gamma_unif < 1) (hell : 0 < ell_IR) :
    let m_phys := -Real.log gamma_unif / ell_IR
    0 < m_phys ∧
      gamma_unif ^ t = Real.exp (-m_phys * ((t : ℝ) * ell_IR)) := by
  dsimp only
  have hlog : Real.log gamma_unif < 0 := Real.log_neg hg0 hg1
  have hm_pos : 0 < -Real.log gamma_unif / ell_IR := div_pos (by linarith) hell
  have hell_ne : ell_IR ≠ 0 := ne_of_gt hell
  have hexp_eq :
      -(-Real.log gamma_unif / ell_IR) * ((t : ℝ) * ell_IR) =
        (t : ℝ) * Real.log gamma_unif := by
    field_simp [hell_ne]
  refine ⟨hm_pos, ?_⟩
  rw [hexp_eq, Real.exp_nat_mul, Real.exp_log hg0]

end YangMillsBlueprint.Certificates
