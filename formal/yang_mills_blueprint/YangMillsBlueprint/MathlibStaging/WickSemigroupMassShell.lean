/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Analysis.Complex.Trigonometric
public import Mathlib.Analysis.Real.Sqrt
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.LatticeReflectionPositivity
public import YangMillsBlueprint.MathlibStaging.LorentzianMetricGroup
public import YangMillsBlueprint.MathlibStaging.SliceReflectionHilbert

/-!
# Complex Wick Semigroup Contraction and Lorentzian Mass-Shell Spectral Gap

Formalizes the algebraic and analytic Wick rotation bridge `t_E + i t_M` between Euclidean
exponential clustering (`t_E ≥ 0`) and unitary Lorentzian time evolution (`t_M ∈ ℝ`) on the
positive-energy mass shell `E(p) = √(m² + ‖p‖²)`:

* `wickAmplitude tE tM E = Complex.exp (-(tE : ℂ) * E - Complex.I * tM * E)`: satisfies exact
  multiplicative semigroup law `wickAmplitude_add`, modulus `Real.exp (-(tE * E))`, Euclidean
  gap decay `≤ Real.exp (-(tE * Δ))` for `Δ ≤ m`, and unitary modulus `1` at `tE = 0`.
* `massShellFourMom m p₁ p₂ p₃`: sits unconditionally on the hyperboloid `-minkowskiQuad p = m²`.
* `massShell_boost_invariant_gap`: every boost `lorentzBoost1 φ` preserves the invariant
  `-minkowskiQuad p = m² ≥ Δ²` and keeps boosted energy strictly positive `p' 0 > 0`.
-/

@[expose] public section

namespace WickSemigroupMassShell

open LorentzianMetricGroup Matrix

section MassShellKinematics

/-- Relativistic mass-shell energy `E(m, p) = √(m² + p₁² + p₂² + p₃²)`. -/
noncomputable def massShellEnergy (m p1 p2 p3 : ℝ) : ℝ :=
  Real.sqrt (m ^ 2 + p1 ^ 2 + p2 ^ 2 + p3 ^ 2)

/-- On-shell 4-momentum vector `(E(m, p), p₁, p₂, p₃) : Fin 4 → ℝ`. -/
noncomputable def massShellFourMom (m p1 p2 p3 : ℝ) : Fin 4 → ℝ :=
  ![massShellEnergy m p1 p2 p3, p1, p2, p3]

theorem massShellEnergy_nonneg (m p1 p2 p3 : ℝ) :
    0 ≤ massShellEnergy m p1 p2 p3 :=
  Real.sqrt_nonneg _

theorem massShellEnergy_pos {m : ℝ} (hm : 0 < m) (p1 p2 p3 : ℝ) :
    0 < massShellEnergy m p1 p2 p3 := by
  unfold massShellEnergy
  apply Real.sqrt_pos.mpr
  have h1 : 0 < m ^ 2 := sq_pos_of_pos hm
  have h2 : 0 ≤ p1 ^ 2 + p2 ^ 2 + p3 ^ 2 := by positivity
  linarith

theorem massShellEnergy_ge (m p1 p2 p3 : ℝ) :
    m ≤ massShellEnergy m p1 p2 p3 := by
  unfold massShellEnergy
  exact Real.le_sqrt_of_sq_le (by linarith [sq_nonneg p1, sq_nonneg p2, sq_nonneg p3])

theorem abs_p1_le_massShellEnergy (m p1 p2 p3 : ℝ) :
    |p1| ≤ massShellEnergy m p1 p2 p3 := by
  rw [← Real.sqrt_sq_eq_abs p1]
  unfold massShellEnergy
  exact Real.sqrt_le_sqrt (by linarith [sq_nonneg m, sq_nonneg p2, sq_nonneg p3])

/-- Exact on-shell Minkowski invariant `- (pᵀ η p) = m²`. -/
theorem massShellFourMom_quad (m p1 p2 p3 : ℝ) :
    minkowskiQuad (massShellFourMom m p1 p2 p3) = -(m ^ 2) := by
  unfold massShellFourMom
  rw [minkowskiQuad_eq]
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
  have hsq : massShellEnergy m p1 p2 p3 ^ 2 = m ^ 2 + p1 ^ 2 + p2 ^ 2 + p3 ^ 2 := by
    unfold massShellEnergy
    exact Real.sq_sqrt (by positivity)
  linarith

/-- Boost invariance of the Lorentzian mass-shell gap `-p'ᵀ η p' = m² ≥ Δ²` and strict
future-cone positivity `p' 0 > 0` for all boosts `lorentzBoost1 φ`. -/
theorem massShell_boost_invariant_gap {m Δ : ℝ} (hm : 0 < m) (hΔ0 : 0 ≤ Δ) (hΔm : Δ ≤ m)
    (p1 p2 p3 φ : ℝ) :
    -minkowskiQuad (lorentzBoost1 φ *ᵥ massShellFourMom m p1 p2 p3) = m ^ 2 ∧
      Δ ^ 2 ≤ -minkowskiQuad (lorentzBoost1 φ *ᵥ massShellFourMom m p1 p2 p3) ∧
      0 < (lorentzBoost1 φ *ᵥ massShellFourMom m p1 p2 p3) 0 := by
  have hpres :
      minkowskiQuad (lorentzBoost1 φ *ᵥ massShellFourMom m p1 p2 p3) =
        minkowskiQuad (massShellFourMom m p1 p2 p3) :=
    isLorentzMatrix_preserves_quad (isLorentzMatrix_lorentzBoost1 φ) _
  have hm2 : -minkowskiQuad (lorentzBoost1 φ *ᵥ massShellFourMom m p1 p2 p3) = m ^ 2 := by
    rw [hpres, massShellFourMom_quad]
    ring
  have hgap : Δ ^ 2 ≤ -minkowskiQuad (lorentzBoost1 φ *ᵥ massShellFourMom m p1 p2 p3) := by
    rw [hm2]
    nlinarith
  have hpos0 : 0 < (lorentzBoost1 φ *ᵥ massShellFourMom m p1 p2 p3) 0 := by
    have hE0 : 0 < massShellEnergy m p1 p2 p3 := massShellEnergy_pos hm p1 p2 p3
    have hcausal : |p1| ≤ massShellEnergy m p1 p2 p3 := abs_p1_le_massShellEnergy m p1 p2 p3
    have hfut := lorentzBoost1_future_pos hE0 hcausal φ
    have hcomp :
        (lorentzBoost1 φ *ᵥ massShellFourMom m p1 p2 p3) 0 =
          massShellEnergy m p1 p2 p3 * Real.cosh φ + p1 * Real.sinh φ := by
      simp only [Matrix.mulVec, dotProduct, lorentzBoost1, massShellFourMom, Fin.sum_univ_four]
      norm_num
      ring
    rwa [hcomp]
  exact ⟨hm2, hgap, hpos0⟩

end MassShellKinematics

section WickSemigroup

/-- Complex half-plane Wick amplitude `exp (-(tE + i tM) * E)`. -/
noncomputable def wickAmplitude (tE tM E : ℝ) : ℂ :=
  Complex.exp (-(tE : ℂ) * (E : ℂ) - Complex.I * (tM : ℂ) * (E : ℂ))

/-- Exact modulus of the complex Wick semigroup `‖exp(-(tE + i tM) E)‖ = exp(-tE * E)`. -/
theorem wickAmplitude_norm (tE tM E : ℝ) :
    ‖wickAmplitude tE tM E‖ = Real.exp (-(tE * E)) := by
  unfold wickAmplitude
  rw [Complex.norm_exp]
  congr 1
  simp [Complex.sub_re, Complex.mul_re]

/-- On the Lorentzian boundary (`tE = 0`), time evolution is strictly unitary (`‖·‖ = 1`). -/
theorem wickAmplitude_lorentzian_unitary (tM E : ℝ) :
    ‖wickAmplitude 0 tM E‖ = 1 := by
  rw [wickAmplitude_norm, zero_mul, neg_zero, Real.exp_zero]

/-- Multiplicative semigroup/group composition law in the `(tE, tM)` upper half-plane. -/
theorem wickAmplitude_add (tE₁ tE₂ tM₁ tM₂ E : ℝ) :
    wickAmplitude (tE₁ + tE₂) (tM₁ + tM₂) E =
      wickAmplitude tE₁ tM₁ E * wickAmplitude tE₂ tM₂ E := by
  unfold wickAmplitude
  rw [← Complex.exp_add]
  congr 1
  push_cast
  ring

/-- Euclidean decay envelope along the mass shell: for `tE ≥ 0` and `0 ≤ Δ ≤ m`,
`‖wickAmplitude tE tM (massShellEnergy m p)‖ ≤ Real.exp (-(tE * Δ))`. -/
theorem wickAmplitude_euclidean_gap_bound {tE Δ m : ℝ} (htE : 0 ≤ tE)
    (hΔm : Δ ≤ m) (tM p1 p2 p3 : ℝ) :
    ‖wickAmplitude tE tM (massShellEnergy m p1 p2 p3)‖ ≤ Real.exp (-(tE * Δ)) := by
  rw [wickAmplitude_norm]
  apply Real.exp_le_exp.mpr
  have hge : Δ ≤ massShellEnergy m p1 p2 p3 :=
    le_trans hΔm (massShellEnergy_ge m p1 p2 p3)
  linarith [mul_le_mul_of_nonneg_left hge htE]

end WickSemigroup

end WickSemigroupMassShell
