/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
# YM-178: Exact Spectral `Real.log` Taylor Sandwich & Small-Field Gribov Clearance

Formalizes the two provable finite-dimensional analytic bridges from `UNIFORM_CONTINUUM_RG_PLAN.md`:
1. `small_field_gribov_clearance_unconditional`: Deterministic `2^4`-fiber Gribov-horizon
   clearance on the small-field domain `‖F‖ ≤ M · λ_0 / C` (`0 ≤ M < 1`), proving
   `(1 / λ_0) · ‖W_para‖_op ≤ M < 1` and `0 < 1 - M ≤ 1 + λ` for all `λ ∈ [-M, M]`.
2. `real_log_fourth_order_sandwich_unconditional`: Exact calculus proof (via `HasDerivAt`
   and `monotoneOn` / `antitoneOn`) that for every `0 ≤ M < 1` and `λ ∈ [-M, M]`,
   `λ - λ^2/2 + λ^3/3 - λ^4 / (4 * (1 - M)) ≤ Real.log (1 + λ) ≤ λ - λ^2/2 + λ^3/3`.
3. `trace_log_schur_sandwich_unconditional`: Summing over eigenvalues `λ : Fin n → ℝ`
   in `[-M, M]` with `∑ i, λ i = 0` (`Tr(K_para) = 0`) yields the exact two-sided `Real.log`
   Schur determinant sandwich in terms of `∑ (λ i)^2`, `∑ (λ i)^3`, `∑ (λ i)^4`.
-/

namespace YangMillsBlueprint.Certificates

structure SpectralGribovCert where
  lam0 : ℝ
  cComm : ℝ
  mOp : ℝ
  hLam0 : 0 < lam0
  hCComm : 0 < cComm
  hM0 : 0 ≤ mOp
  hM1 : mOp < 1

noncomputable def canonicalSpectralGribovCert : SpectralGribovCert where
  lam0 := 4
  cComm := 2
  mOp := 4346 / 10000
  hLam0 := by norm_num
  hCComm := by norm_num
  hM0 := by norm_num
  hM1 := by norm_num

instance : Nonempty SpectralGribovCert :=
  ⟨canonicalSpectralGribovCert⟩

/-- **UNCONDITIONAL:** Deterministic `2^4`-fiber small-field Gribov-horizon clearance.
If `λ_min(H_diam) ≥ λ_0 > 0`, `‖W_para‖_op ≤ C · ‖F‖`, and `0 ≤ ‖F‖ ≤ M · λ_0 / C`
with `0 ≤ M < 1`, then `(1 / λ_0) · ‖W_para‖_op ≤ M < 1` and `0 < 1 - M ≤ 1 + λ`
for every eigenvalue `λ ∈ [-M, M]`. -/
theorem small_field_gribov_clearance_unconditional
    (lam0 c_comm normF normW M : ℝ)
    (hLam0 : 0 < lam0) (hC : 0 < c_comm) (_hM0 : 0 ≤ M) (hM1 : M < 1)
    (hW : normW ≤ c_comm * normF) (hSmall : normF ≤ M * lam0 / c_comm) :
    (1 / lam0) * normW ≤ M ∧
      0 < 1 - M ∧
      ∀ lam : ℝ, -M ≤ lam → lam ≤ M → 1 - M ≤ 1 + lam := by
  have hWle : normW ≤ M * lam0 := by
    have hMul : c_comm * normF ≤ c_comm * (M * lam0 / c_comm) :=
      mul_le_mul_of_nonneg_left hSmall (le_of_lt hC)
    have hEq : c_comm * (M * lam0 / c_comm) = M * lam0 := by
      have hcne : c_comm ≠ 0 := ne_of_gt hC
      field_simp [hcne]
    linarith
  have hKop : (1 / lam0) * normW ≤ M := by
    have hInvPos : 0 ≤ 1 / lam0 := div_nonneg zero_le_one (le_of_lt hLam0)
    have hMul := mul_le_mul_of_nonneg_left hWle hInvPos
    have hEq : (1 / lam0) * (M * lam0) = M := by
      have hlne : lam0 ≠ 0 := ne_of_gt hLam0
      field_simp [hlne]
    linarith
  refine ⟨hKop, by linarith, ?_⟩
  intro lam hlo _hhi
  linarith

private lemma log_upper_deriv (x : ℝ) (hx : -1 < x) :
    HasDerivAt (fun t : ℝ => t - t ^ 2 / 2 + t ^ 3 / 3 - Real.log (1 + t))
      (x ^ 3 / (1 + x)) x := by
  have h1x : 1 + x ≠ 0 := by linarith
  have ht2 : HasDerivAt (fun t : ℝ => t ^ 2 / 2) x x := by
    simpa using (hasDerivAt_pow 2 x).div_const 2
  have ht3 : HasDerivAt (fun t : ℝ => t ^ 3 / 3) (x ^ 2) x := by
    simpa using (hasDerivAt_pow 3 x).div_const 3
  have hPoly : HasDerivAt (fun t : ℝ => t - t ^ 2 / 2 + t ^ 3 / 3) (1 - x + x ^ 2) x :=
    ((hasDerivAt_id x).sub ht2).add ht3
  have hLog : HasDerivAt (fun t : ℝ => Real.log (1 + t)) (1 / (1 + x)) x :=
    ((hasDerivAt_id x).const_add 1).log h1x
  convert hPoly.sub hLog using 1
  field_simp [h1x]
  ring

private lemma log_lower_deriv (M x : ℝ) (hM1 : M < 1) (hx : -M ≤ x) :
    HasDerivAt
      (fun t : ℝ => Real.log (1 + t) - (t - t ^ 2 / 2 + t ^ 3 / 3 - t ^ 4 / (4 * (1 - M))))
      (x ^ 3 * (x + M) / ((1 - M) * (1 + x))) x := by
  have h1x : 1 + x ≠ 0 := by linarith
  have h1mM : 1 - M ≠ 0 := by linarith
  have hLog : HasDerivAt (fun t : ℝ => Real.log (1 + t)) (1 / (1 + x)) x :=
    ((hasDerivAt_id x).const_add 1).log h1x
  have ht2 : HasDerivAt (fun t : ℝ => t ^ 2 / 2) x x := by
    simpa using (hasDerivAt_pow 2 x).div_const 2
  have ht3 : HasDerivAt (fun t : ℝ => t ^ 3 / 3) (x ^ 2) x := by
    simpa using (hasDerivAt_pow 3 x).div_const 3
  have ht4 : HasDerivAt (fun t : ℝ => t ^ 4 / (4 * (1 - M))) (x ^ 3 / (1 - M)) x := by
    convert (hasDerivAt_pow 4 x).div_const (4 * (1 - M)) using 1
    field_simp [h1mM]
    ring
  have hPoly :
      HasDerivAt (fun t : ℝ => t - t ^ 2 / 2 + t ^ 3 / 3 - t ^ 4 / (4 * (1 - M)))
        (1 - x + x ^ 2 - x ^ 3 / (1 - M)) x :=
    (((hasDerivAt_id x).sub ht2).add ht3).sub ht4
  convert hLog.sub hPoly using 1
  field_simp [h1x, h1mM]
  ring

/-- **UNCONDITIONAL:** Exact 4th-order `Real.log` Taylor sandwich on `[-M, M]` for `0 ≤ M < 1`:
`λ - λ^2/2 + λ^3/3 - λ^4 / (4 * (1 - M)) ≤ Real.log (1 + λ) ≤ λ - λ^2/2 + λ^3/3`. -/
theorem real_log_fourth_order_sandwich_unconditional
    (M lam : ℝ) (_hM0 : 0 ≤ M) (hM1 : M < 1) (hLo : -M ≤ lam) (hHi : lam ≤ M) :
    lam - lam ^ 2 / 2 + lam ^ 3 / 3 - lam ^ 4 / (4 * (1 - M)) ≤ Real.log (1 + lam) ∧
      Real.log (1 + lam) ≤ lam - lam ^ 2 / 2 + lam ^ 3 / 3 := by
  let g : ℝ → ℝ := fun t => t - t ^ 2 / 2 + t ^ 3 / 3 - Real.log (1 + t)
  have hg0 : g 0 = 0 := by simp [g]
  have hg_nonneg : 0 ≤ g lam := by
    rcases le_total 0 lam with h0 | h0
    · have hMono : MonotoneOn g (Set.Icc 0 lam) := by
        apply monotoneOn_of_deriv_nonneg (convex_Icc 0 lam)
        · intro x hx
          exact (log_upper_deriv x (by linarith [hx.1])).continuousAt.continuousWithinAt
        · intro x hx
          have hx' := interior_subset hx
          exact (log_upper_deriv x (by linarith [hx'.1])).differentiableAt.differentiableWithinAt
        · intro x hx
          have hx' := interior_subset hx
          have hx0 : 0 ≤ x := hx'.1
          have h1x : 0 < 1 + x := by linarith
          rw [(log_upper_deriv x (by linarith [hx'.1])).deriv]
          exact div_nonneg (pow_nonneg hx0 3) (le_of_lt h1x)
      have hle := hMono ⟨le_rfl, h0⟩ ⟨h0, le_rfl⟩ h0
      linarith [hg0]
    · have hAnti : AntitoneOn g (Set.Icc lam 0) := by
        apply antitoneOn_of_deriv_nonpos (convex_Icc lam 0)
        · intro x hx
          exact (log_upper_deriv x (by linarith [hx.1])).continuousAt.continuousWithinAt
        · intro x hx
          have hx' := interior_subset hx
          exact (log_upper_deriv x (by linarith [hx'.1])).differentiableAt.differentiableWithinAt
        · intro x hx
          have hx' := interior_subset hx
          have hx0 : x ≤ 0 := hx'.2
          have h1x : 0 < 1 + x := by linarith [hx'.1, hLo, hM1]
          have hx3 : x ^ 3 ≤ 0 := by nlinarith [sq_nonneg x]
          rw [(log_upper_deriv x (by linarith [hx'.1])).deriv]
          exact div_nonpos_of_nonpos_of_nonneg hx3 (le_of_lt h1x)
      have hle := hAnti ⟨le_rfl, h0⟩ ⟨h0, le_rfl⟩ h0
      linarith [hg0]
  let h : ℝ → ℝ := fun t => Real.log (1 + t) - (t - t ^ 2 / 2 + t ^ 3 / 3 - t ^ 4 / (4 * (1 - M)))
  have hh0 : h 0 = 0 := by simp [h]
  have hh_nonneg : 0 ≤ h lam := by
    rcases le_total 0 lam with h0 | h0
    · have hMono : MonotoneOn h (Set.Icc 0 lam) := by
        apply monotoneOn_of_deriv_nonneg (convex_Icc 0 lam)
        · intro x hx
          exact (log_lower_deriv M x hM1 (by linarith [hx.1])).continuousAt.continuousWithinAt
        · intro x hx
          have hx' := interior_subset hx
          exact (log_lower_deriv M x hM1 (by linarith [hx'.1])).differentiableAt.differentiableWithinAt
        · intro x hx
          have hx' := interior_subset hx
          have hx0 : 0 ≤ x := hx'.1
          have hxM : 0 ≤ x + M := by linarith
          have hden : 0 < (1 - M) * (1 + x) := mul_pos (by linarith) (by linarith [hx'.1])
          rw [(log_lower_deriv M x hM1 (by linarith [hx'.1])).deriv]
          exact div_nonneg (mul_nonneg (pow_nonneg hx0 3) hxM) (le_of_lt hden)
      have hle := hMono ⟨le_rfl, h0⟩ ⟨h0, le_rfl⟩ h0
      linarith [hh0]
    · have hAnti : AntitoneOn h (Set.Icc lam 0) := by
        apply antitoneOn_of_deriv_nonpos (convex_Icc lam 0)
        · intro x hx
          exact (log_lower_deriv M x hM1 (by linarith [hx.1])).continuousAt.continuousWithinAt
        · intro x hx
          have hx' := interior_subset hx
          exact (log_lower_deriv M x hM1 (by linarith [hx'.1])).differentiableAt.differentiableWithinAt
        · intro x hx
          have hx' := interior_subset hx
          have hx0 : x ≤ 0 := hx'.2
          have hx3 : x ^ 3 ≤ 0 := by nlinarith [sq_nonneg x]
          have hxM : 0 ≤ x + M := by linarith [hx'.1]
          have hden : 0 < (1 - M) * (1 + x) := mul_pos (by linarith) (by linarith [hx'.1])
          rw [(log_lower_deriv M x hM1 (by linarith [hx'.1])).deriv]
          exact div_nonpos_of_nonpos_of_nonneg (mul_nonpos_of_nonpos_of_nonneg hx3 hxM) (le_of_lt hden)
      have hle := hAnti ⟨le_rfl, h0⟩ ⟨h0, le_rfl⟩ h0
      linarith [hh0]
  exact ⟨by dsimp [h] at hh_nonneg; linarith, by dsimp [g] at hg_nonneg; linarith⟩

/-- **UNCONDITIONAL:** Exact `Real.log` Schur determinant sandwich summed over eigenvalues
`λ : Fin n → ℝ` inside `[-M, M]` with `∑ i, λ i = 0` (`Tr(K_para) = 0`). -/
theorem trace_log_schur_sandwich_unconditional
    {n : ℕ} (M : ℝ) (lam : Fin n → ℝ)
    (hM0 : 0 ≤ M) (hM1 : M < 1)
    (hBound : ∀ i : Fin n, -M ≤ lam i ∧ lam i ≤ M)
    (hTr0 : (∑ i : Fin n, lam i) = 0) :
    -(1 / 4 : ℝ) * (∑ i : Fin n, lam i ^ 2) + (1 / 6 : ℝ) * (∑ i : Fin n, lam i ^ 3) -
        (1 / (8 * (1 - M))) * (∑ i : Fin n, lam i ^ 4) ≤
      (1 / 2 : ℝ) * (∑ i : Fin n, Real.log (1 + lam i)) ∧
      (1 / 2 : ℝ) * (∑ i : Fin n, Real.log (1 + lam i)) ≤
        -(1 / 4 : ℝ) * (∑ i : Fin n, lam i ^ 2) + (1 / 6 : ℝ) * (∑ i : Fin n, lam i ^ 3) := by
  have hPoint : ∀ i : Fin n,
      lam i - lam i ^ 2 / 2 + lam i ^ 3 / 3 - lam i ^ 4 / (4 * (1 - M)) ≤ Real.log (1 + lam i) ∧
        Real.log (1 + lam i) ≤ lam i - lam i ^ 2 / 2 + lam i ^ 3 / 3 :=
    fun i => real_log_fourth_order_sandwich_unconditional M (lam i) hM0 hM1 (hBound i).1 (hBound i).2
  have hSumLo :
      (∑ i : Fin n, (lam i - lam i ^ 2 / 2 + lam i ^ 3 / 3 - lam i ^ 4 / (4 * (1 - M)))) ≤
        ∑ i : Fin n, Real.log (1 + lam i) :=
    Finset.sum_le_sum (fun i _ => (hPoint i).1)
  have hSumHi :
      (∑ i : Fin n, Real.log (1 + lam i)) ≤
        ∑ i : Fin n, (lam i - lam i ^ 2 / 2 + lam i ^ 3 / 3) :=
    Finset.sum_le_sum (fun i _ => (hPoint i).2)
  have hRewriteHi :
      (∑ i : Fin n, (lam i - lam i ^ 2 / 2 + lam i ^ 3 / 3)) =
        -(1 / 2 : ℝ) * (∑ i : Fin n, lam i ^ 2) + (1 / 3 : ℝ) * (∑ i : Fin n, lam i ^ 3) := by
    simp only [div_eq_mul_inv, Finset.sum_add_distrib, Finset.sum_sub_distrib,
      ← Finset.sum_mul, hTr0]
    ring
  have hRewriteLo :
      (∑ i : Fin n, (lam i - lam i ^ 2 / 2 + lam i ^ 3 / 3 - lam i ^ 4 / (4 * (1 - M)))) =
        -(1 / 2 : ℝ) * (∑ i : Fin n, lam i ^ 2) + (1 / 3 : ℝ) * (∑ i : Fin n, lam i ^ 3) -
          (1 / (4 * (1 - M))) * (∑ i : Fin n, lam i ^ 4) := by
    simp only [div_eq_mul_inv, Finset.sum_add_distrib, Finset.sum_sub_distrib,
      ← Finset.sum_mul, hTr0]
    ring
  have hHalfLo :
      (1 / 2 : ℝ) * (-(1 / 2 : ℝ) * (∑ i : Fin n, lam i ^ 2) +
          (1 / 3 : ℝ) * (∑ i : Fin n, lam i ^ 3) -
          (1 / (4 * (1 - M))) * (∑ i : Fin n, lam i ^ 4)) =
        -(1 / 4 : ℝ) * (∑ i : Fin n, lam i ^ 2) + (1 / 6 : ℝ) * (∑ i : Fin n, lam i ^ 3) -
          (1 / (8 * (1 - M))) * (∑ i : Fin n, lam i ^ 4) := by
    have h1mM : 1 - M ≠ 0 := by linarith
    field_simp [h1mM]
    ring
  constructor
  · linarith [hSumLo, hRewriteLo, hHalfLo]
  · linarith [hSumHi, hRewriteHi]

end YangMillsBlueprint.Certificates
