/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Analysis.Complex.Trigonometric
public import Mathlib.Data.Matrix.Basic
public import Mathlib.Data.Matrix.Mul
public import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
public import Mathlib.Tactic.FinCases
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring

/-!
# Minkowski Metric Involution and Lorentz Group `O(1,3)` Matrix Algebra

Formalizes the 4D Lorentzian metric tensor `minkowskiEta = diag(-1, 1, 1, 1)` as an asymmetric
symmetric involution (`ηᵀ = η`, `η * η = 1`, `det η = -1`), defines the Lorentz group condition
`IsLorentzMatrix Λ ↔ Λᵀ * η * Λ = η`, and proves unconditionally:

* Discrete reflection subgroup (`1`, `-1`, `η`, `-η`) and product/inverse closure
  `lorentzInv Λ * Λ = 1`.
* Exact Minkowski bilinear form and quadratic form invariance under all `Λ ∈ O(1,3)`.
* Spatial rotation embedding `spatialRotMatrix R` (`R ∈ O(3)`) into `O(1,3)`.
* Hyperbolic boosts `lorentzBoost1 φ` (`cosh φ`, `sinh φ`): rapidity additivity
  `lorentzBoost1 φ₁ * lorentzBoost1 φ₂ = lorentzBoost1 (φ₁ + φ₂)`, `IsLorentzMatrix`,
  `det (lorentzBoost1 φ) = 1`, and forward light-cone preservation `lorentzBoost1_future_pos`.
-/

@[expose] public section

namespace LorentzianMetricGroup

open Matrix

section MinkowskiMetric

/-- 4D Minkowski metric matrix `η = diag(-1, 1, 1, 1)`. -/
def minkowskiEta : Matrix (Fin 4) (Fin 4) ℝ :=
  Matrix.diagonal ![(-1 : ℝ), 1, 1, 1]

/-- Minkowski metric matrix is symmetric (`ηᵀ = η`). -/
theorem minkowskiEta_transpose : minkowskiEtaᵀ = minkowskiEta := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [minkowskiEta]

/-- Minkowski metric matrix is an involution (`η * η = 1`). -/
theorem minkowskiEta_mul_self : minkowskiEta * minkowskiEta = 1 := by
  unfold minkowskiEta
  rw [Matrix.diagonal_mul_diagonal]
  ext i j
  fin_cases i <;> fin_cases j <;> simp

/-- Minkowski metric matrix has determinant `-1`. -/
theorem minkowskiEta_det : minkowskiEta.det = -1 := by
  unfold minkowskiEta
  rw [Matrix.det_diagonal, Fin.prod_univ_four]
  norm_num

/-- Minkowski indefinite inner product `xᵀ η y`. -/
def minkowskiInner (x y : Fin 4 → ℝ) : ℝ :=
  dotProduct x (minkowskiEta *ᵥ y)

/-- Minkowski quadratic form `xᵀ η x = -x₀² + x₁² + x₂² + x₃²`. -/
def minkowskiQuad (x : Fin 4 → ℝ) : ℝ :=
  minkowskiInner x x

theorem minkowskiInner_eq (x y : Fin 4 → ℝ) :
    minkowskiInner x y = -(x 0 * y 0) + x 1 * y 1 + x 2 * y 2 + x 3 * y 3 := by
  unfold minkowskiInner minkowskiEta
  simp only [dotProduct, Matrix.mulVec_diagonal, Fin.sum_univ_four]
  norm_num

theorem minkowskiQuad_eq (x : Fin 4 → ℝ) :
    minkowskiQuad x = -(x 0 ^ 2) + x 1 ^ 2 + x 2 ^ 2 + x 3 ^ 2 := by
  unfold minkowskiQuad
  rw [minkowskiInner_eq]
  ring

end MinkowskiMetric

section LorentzGroup

/-- A `4 × 4` real matrix belongs to `O(1,3)` iff `Λᵀ * η * Λ = η`. -/
def IsLorentzMatrix (Λ : Matrix (Fin 4) (Fin 4) ℝ) : Prop :=
  Λᵀ * minkowskiEta * Λ = minkowskiEta

/-- Canonical Lorentz inverse candidate `η * Λᵀ * η`. -/
def lorentzInv (Λ : Matrix (Fin 4) (Fin 4) ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  minkowskiEta * Λᵀ * minkowskiEta

theorem isLorentzMatrix_one : IsLorentzMatrix 1 := by
  unfold IsLorentzMatrix
  simp

theorem isLorentzMatrix_neg_one : IsLorentzMatrix (-1) := by
  unfold IsLorentzMatrix
  simp

theorem isLorentzMatrix_eta : IsLorentzMatrix minkowskiEta := by
  unfold IsLorentzMatrix
  rw [minkowskiEta_transpose, Matrix.mul_assoc, minkowskiEta_mul_self, Matrix.mul_one]

theorem isLorentzMatrix_neg_eta : IsLorentzMatrix (-minkowskiEta) := by
  unfold IsLorentzMatrix
  rw [Matrix.transpose_neg, minkowskiEta_transpose, Matrix.neg_mul, neg_mul_neg,
    Matrix.mul_assoc, minkowskiEta_mul_self, Matrix.mul_one]

theorem isLorentzMatrix_mul {Λ₁ Λ₂ : Matrix (Fin 4) (Fin 4) ℝ}
    (h₁ : IsLorentzMatrix Λ₁) (h₂ : IsLorentzMatrix Λ₂) :
    IsLorentzMatrix (Λ₁ * Λ₂) := by
  unfold IsLorentzMatrix at h₁ h₂ ⊢
  rw [Matrix.transpose_mul]
  calc
    Λ₂ᵀ * Λ₁ᵀ * minkowskiEta * (Λ₁ * Λ₂)
        = Λ₂ᵀ * (Λ₁ᵀ * minkowskiEta * Λ₁) * Λ₂ := by simp only [Matrix.mul_assoc]
    _ = Λ₂ᵀ * minkowskiEta * Λ₂ := by rw [h₁]
    _ = minkowskiEta := h₂

theorem lorentzInv_mul_self {Λ : Matrix (Fin 4) (Fin 4) ℝ} (hΛ : IsLorentzMatrix Λ) :
    lorentzInv Λ * Λ = 1 := by
  unfold lorentzInv
  calc
    (minkowskiEta * Λᵀ * minkowskiEta) * Λ
        = minkowskiEta * (Λᵀ * minkowskiEta * Λ) := by simp only [Matrix.mul_assoc]
    _ = minkowskiEta * minkowskiEta := by rw [hΛ]
    _ = 1 := minkowskiEta_mul_self

/-- Exact bilinear invariance `(Λ *ᵥ x)ᵀ η (Λ *ᵥ y) = xᵀ η y` for all `Λ ∈ O(1,3)`. -/
theorem isLorentzMatrix_preserves_inner {Λ : Matrix (Fin 4) (Fin 4) ℝ} (hΛ : IsLorentzMatrix Λ)
    (x y : Fin 4 → ℝ) :
    minkowskiInner (Λ *ᵥ x) (Λ *ᵥ y) = minkowskiInner x y := by
  unfold minkowskiInner
  calc
    dotProduct (Λ *ᵥ x) (minkowskiEta *ᵥ (Λ *ᵥ y))
        = dotProduct (x ᵥ* Λᵀ) (minkowskiEta *ᵥ (Λ *ᵥ y)) := by
          rw [Matrix.vecMul_transpose]
    _ = dotProduct x (Λᵀ *ᵥ (minkowskiEta *ᵥ (Λ *ᵥ y))) := by
          rw [← Matrix.dotProduct_mulVec]
    _ = dotProduct x ((Λᵀ * minkowskiEta * Λ) *ᵥ y) := by
          simp only [Matrix.mulVec_mulVec, Matrix.mul_assoc]
    _ = dotProduct x (minkowskiEta *ᵥ y) := by rw [hΛ]

/-- Exact quadratic-form invariance `minkowskiQuad (Λ *ᵥ x) = minkowskiQuad x`. -/
theorem isLorentzMatrix_preserves_quad {Λ : Matrix (Fin 4) (Fin 4) ℝ} (hΛ : IsLorentzMatrix Λ)
    (x : Fin 4 → ℝ) :
    minkowskiQuad (Λ *ᵥ x) = minkowskiQuad x :=
  isLorentzMatrix_preserves_inner hΛ x x

/-- Block-diagonal spatial embedding of any `3 × 3` matrix into `4 × 4` spacetime matrices. -/
def spatialRotMatrix (R : Matrix (Fin 3) (Fin 3) ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![1, 0, 0, 0;
     0, R 0 0, R 0 1, R 0 2;
     0, R 1 0, R 1 1, R 1 2;
     0, R 2 0, R 2 1, R 2 2]

/-- Every `O(3)` spatial orthogonal matrix `Rᵀ * R = 1` embeds into `O(1,3)`. -/
theorem isLorentzMatrix_spatialRot {R : Matrix (Fin 3) (Fin 3) ℝ} (hR : Rᵀ * R = 1) :
    IsLorentzMatrix (spatialRotMatrix R) := by
  have hRij : ∀ a b : Fin 3,
      R 0 a * R 0 b + R 1 a * R 1 b + R 2 a * R 2 b = if a = b then 1 else 0 := by
    intro a b
    have hmul := congr_fun (congr_fun hR a) b
    simp only [Matrix.mul_apply, Matrix.transpose_apply, Matrix.one_apply, Fin.sum_univ_three]
      at hmul
    exact hmul
  unfold IsLorentzMatrix
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [spatialRotMatrix, minkowskiEta, Matrix.mul_apply, Fin.sum_univ_four]
  · simpa using hRij 0 0
  · simpa using hRij 0 1
  · simpa using hRij 0 2
  · simpa using hRij 1 0
  · simpa using hRij 1 1
  · simpa using hRij 1 2
  · simpa using hRij 2 0
  · simpa using hRij 2 1
  · simpa using hRij 2 2

end LorentzGroup

section HyperbolicBoosts

/-- Pure hyperbolic Lorentz boost along axis 1 with rapidity `φ`. -/
noncomputable def lorentzBoost1 (φ : ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![Real.cosh φ, Real.sinh φ, 0, 0;
     Real.sinh φ, Real.cosh φ, 0, 0;
     0, 0, 1, 0;
     0, 0, 0, 1]

theorem lorentzBoost1_transpose (φ : ℝ) : (lorentzBoost1 φ)ᵀ = lorentzBoost1 φ := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [lorentzBoost1]

theorem lorentzBoost1_zero : lorentzBoost1 0 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [lorentzBoost1]

/-- Exact hyperbolic rapidity addition law `B₁(φ₁) * B₁(φ₂) = B₁(φ₁ + φ₂)`. -/
theorem lorentzBoost1_add (φ₁ φ₂ : ℝ) :
    lorentzBoost1 φ₁ * lorentzBoost1 φ₂ = lorentzBoost1 (φ₁ + φ₂) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [lorentzBoost1, Matrix.mul_apply, Fin.sum_univ_four, Real.cosh_add, Real.sinh_add] <;>
    ring

/-- Every hyperbolic boost `lorentzBoost1 φ` belongs to `O(1,3)`. -/
theorem isLorentzMatrix_lorentzBoost1 (φ : ℝ) : IsLorentzMatrix (lorentzBoost1 φ) := by
  have hcs : Real.cosh φ * Real.cosh φ - Real.sinh φ * Real.sinh φ = 1 := by
    simpa [sq] using Real.cosh_sq_sub_sinh_sq φ
  unfold IsLorentzMatrix
  rw [lorentzBoost1_transpose]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [lorentzBoost1, minkowskiEta, Matrix.mul_apply, Matrix.vecMul_diagonal,
      Fin.sum_univ_four]
  · linarith
  · ring
  · ring
  · linarith

/-- Every hyperbolic boost `lorentzBoost1 φ` has determinant `+1` (proper `SO⁺(1,3)`). -/
theorem lorentzBoost1_det (φ : ℝ) : (lorentzBoost1 φ).det = 1 := by
  have hcs : Real.cosh φ * Real.cosh φ - Real.sinh φ * Real.sinh φ = 1 := by
    simpa [sq] using Real.cosh_sq_sub_sinh_sq φ
  rw [Matrix.det_succ_row_zero, Fin.sum_univ_four]
  simp only [lorentzBoost1, Matrix.det_fin_three, Matrix.submatrix_apply, Fin.succAbove,
    Fin.lt_def]
  norm_num
  linarith

/-- Strict hyperbola gap `|sinh φ| < cosh φ` for all real rapidities `φ`. -/
theorem abs_sinh_lt_cosh (φ : ℝ) : |Real.sinh φ| < Real.cosh φ := by
  have hsq : Real.sinh φ ^ 2 < Real.cosh φ ^ 2 := by
    linarith [Real.cosh_sq_sub_sinh_sq φ]
  have hlt : |Real.sinh φ| < |Real.cosh φ| := sq_lt_sq.mp hsq
  rwa [abs_of_pos (Real.cosh_pos φ)] at hlt

/-- Forward light-cone preservation: any strictly future-directed causal vector
(`0 < E`, `|p₁| ≤ E`) keeps positive energy under any boost `lorentzBoost1 φ`. -/
theorem lorentzBoost1_future_pos {E p1 : ℝ} (hE : 0 < E) (hcausal : |p1| ≤ E) (φ : ℝ) :
    0 < E * Real.cosh φ + p1 * Real.sinh φ := by
  have h1 : |p1 * Real.sinh φ| = |p1| * |Real.sinh φ| := abs_mul p1 (Real.sinh φ)
  have h2 : |p1| * |Real.sinh φ| ≤ E * |Real.sinh φ| :=
    mul_le_mul_of_nonneg_right hcausal (abs_nonneg (Real.sinh φ))
  have h3 : E * |Real.sinh φ| < E * Real.cosh φ :=
    mul_lt_mul_of_pos_left (abs_sinh_lt_cosh φ) hE
  have hlt : |p1 * Real.sinh φ| < E * Real.cosh φ := lt_of_le_of_lt (h1 ▸ h2) h3
  linarith [neg_le_abs (p1 * Real.sinh φ)]

end HyperbolicBoosts

end LorentzianMetricGroup
