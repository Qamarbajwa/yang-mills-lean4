/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.Certificates.YM189_S3GibbsCocycleLowerBoundCert

/-!
# YM-190: Small-Field Gribov Clearance & Balaban Polymer Tree Majorant Contraction

Attacks Phase I Obligations 1 & 3 of Hypothesis 4.1:
1. `gribov_clearance_from_plaquette_envelope_unconditional`:
   On the small-field Wilson plaquette ball `ε_plaq ≤ ε_*`, if
   `‖K_para‖_op ≤ c_para * ε_plaq` (`c_para > 0`) and `c_para * ε_* ≤ θ_max < 3/4`,
   then `‖K_para‖_op ≤ θ_max < 3/4 < 1` (clearing the Gribov horizon).
2. `balaban_polymer_tree_majorant_contraction_unconditional`:
   If the multi-loop polymer remainder `R_poly^(k)` is majorized by the
   Kotecky-Preiss / Balaban geometric tree sum `C_tree * w_step^2 / (1 - w_step)`
   (`0 ≤ w_step < 1`, `0 ≤ C_tree`) and this majorant is bounded by
   `(1/2) * (|F_para^(k)| - ΔF_diam^(k))` with `|F_para^(k)| - ΔF_diam^(k) ≥ 2 * η_min > 0`,
   then `YM187` Lemma `YM2` fires and guarantees `η_net^(k) ≥ η_min > 0`.

Epistemic honesty: Proving uniformly as `(a → 0, L → ∞)` that the true 4D Wilson
Gibbs measure concentrates on `ε_plaq ≤ ε_*` and obeys `w_step < 1` across the
entire crossover regime remains part of open Hypothesis 4.1.
-/

namespace YangMillsBlueprint.Certificates

structure GribovPolymerTreeCert where
  cPara : ℝ
  epsStar : ℝ
  thetaMax : ℝ
  wStep : ℝ
  cTree : ℝ
  hCPara : 0 < cPara
  hEpsStar : 0 ≤ epsStar
  hEnv : cPara * epsStar ≤ thetaMax
  hThetaLt : thetaMax < 3 / 4
  hW0 : 0 ≤ wStep
  hW1 : wStep < 1
  hCTree : 0 ≤ cTree

noncomputable def canonicalGribovPolymerTreeCert : GribovPolymerTreeCert where
  cPara := 1
  epsStar := 4346 / 10000
  thetaMax := 4346 / 10000
  wStep := 1 / 5
  cTree := 1 / 2
  hCPara := by norm_num
  hEpsStar := by norm_num
  hEnv := by norm_num
  hThetaLt := by norm_num
  hW0 := by norm_num
  hW1 := by norm_num
  hCTree := by norm_num

instance : Nonempty GribovPolymerTreeCert :=
  ⟨canonicalGribovPolymerTreeCert⟩

/-- **UNCONDITIONAL (Small-Field Gribov Clearance from Plaquette Envelope):**
    If `‖K_para‖_op ≤ c_para * ε_plaq` (`c_para > 0`), `ε_plaq ≤ ε_*`, and
    `c_para * ε_* ≤ θ_max < 3/4`, then `‖K_para‖_op ≤ θ_max < 3/4`. -/
theorem gribov_clearance_from_plaquette_envelope_unconditional
    (normK c_para eps_plaq eps_star theta_max : ℝ)
    (hCPara : 0 < c_para) (hPlaq : eps_plaq ≤ eps_star)
    (hBound : normK ≤ c_para * eps_plaq)
    (hCap : c_para * eps_star ≤ theta_max) (hThetaLt : theta_max < 3 / 4) :
    normK ≤ theta_max ∧ theta_max < 3 / 4 ∧ normK < 1 := by
  have hMono : c_para * eps_plaq ≤ c_para * eps_star :=
    mul_le_mul_of_nonneg_left hPlaq (le_of_lt hCPara)
  have h1 : normK ≤ theta_max := le_trans hBound (le_trans hMono hCap)
  refine ⟨h1, hThetaLt, by linarith⟩

/-- **UNCONDITIONAL (Balaban Polymer Tree Majorant Contraction):**
    If `R_poly^(k) ≤ C_tree * (w_step^2 / (1 - w_step))` (`0 ≤ w_step < 1`)
    and `C_tree * (w_step^2 / (1 - w_step)) ≤ (1/2) * (|F_para^(k)| - ΔF_diam^(k))`
    with `|F_para^(k)| - ΔF_diam^(k) ≥ 2 * η_min > 0`, then `η_net^(k) ≥ η_min > 0`. -/
theorem balaban_polymer_tree_majorant_contraction_unconditional
    (absFPara deltaFDiam rPoly : ℕ → ℝ) (c_tree w_step etaMin : ℝ)
    (hW0 : 0 ≤ w_step) (hW1 : w_step < 1) (hCTree : 0 ≤ c_tree) (hEtaMin : 0 < etaMin)
    (hMaj : ∀ k : ℕ, rPoly k ≤ c_tree * (w_step ^ 2 / (1 - w_step)))
    (hTreeHalf : ∀ k : ℕ,
      c_tree * (w_step ^ 2 / (1 - w_step)) ≤ (1 / 2 : ℝ) * (absFPara k - deltaFDiam k))
    (hDiff : ∀ k : ℕ, 2 * etaMin ≤ absFPara k - deltaFDiam k) :
    ∀ k : ℕ,
      0 ≤ c_tree * (w_step ^ 2 / (1 - w_step)) ∧
      etaMin ≤ absFPara k - deltaFDiam k - rPoly k ∧
      0 < absFPara k - deltaFDiam k - rPoly k := by
  have hDenPos : 0 < 1 - w_step := by linarith
  have hFracNonneg : 0 ≤ c_tree * (w_step ^ 2 / (1 - w_step)) :=
    mul_nonneg hCTree (div_nonneg (sq_nonneg w_step) (le_of_lt hDenPos))
  have hPolyHalf : ∀ k : ℕ, rPoly k ≤ (1 / 2 : ℝ) * (absFPara k - deltaFDiam k) :=
    fun k => le_trans (hMaj k) (hTreeHalf k)
  have hYM2 := ym_YM2_balaban_polymer_tree_geometric_convergence
    absFPara deltaFDiam rPoly etaMin hEtaMin hPolyHalf hDiff
  intro k
  exact ⟨hFracNonneg, (hYM2 k).1, (hYM2 k).2⟩

end YangMillsBlueprint.Certificates
