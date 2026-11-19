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
public import Mathlib.LinearAlgebra.Matrix.Trace
public import Mathlib.Tactic.FinCases
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.LorentzianMetricGroup
public import YangMillsBlueprint.MathlibStaging.WickSemigroupMassShell

/-!
# Complexified `2 × 2` Spinor-Hermitian Wick Bridge and `SL(2, ℂ)` Double Cover

Formalizes the Pauli `2 × 2` matrix spinor representation of 4D Euclidean and Minkowski geometry:

* `eucQuatMat x₀ x₁ x₂ x₃`: `2 × 2` complex matrix representation of Euclidean 4-vectors with
  `det = x₀² + x₁² + x₂² + x₃²` and OS reflection law `eucQuatMat (-x₀) x₁ x₂ x₃ = -(Q)ᴴ`.
* `minkHermMat x`: Hermitian `2 × 2` Minkowski matrix representation (`Xᴴ = X`) with
  `det (minkHermMat x) = -minkowskiQuad x = x₀² - x₁² - x₂² - x₃²`.
* `wick_eucQuatMat_eq_I_smul_minkHermMat`: exact Wick bridge `Q(i x₀, x⃗) = i • minkHermMat x`.
* `sl2Act A X = A * X * Aᴴ`: `2`-to-`1` `SL(2, ℂ)` double cover preserving Hermiticity, `det`,
  hyperbolic boosts `sl2Boost3 φ`, and strict forward light-cone trace positivity.
-/

@[expose] public section

namespace SpinorHermitianWickBridge

open LorentzianMetricGroup Matrix SliceReflectionHilbert WickSemigroupMassShell

section SpinorMatrices

/-- Euclidean quaternionic `2 × 2` complex matrix representation `x₀ I + i (x⃗ · σ⃗)`. -/
def eucQuatMat (x0 x1 x2 x3 : ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![x0 + Complex.I * x3, x2 + Complex.I * x1;
     -x2 + Complex.I * x1, x0 - Complex.I * x3]

/-- Minkowski Hermitian `2 × 2` spinor representation `x₀ I + x⃗ · σ⃗`. -/
def minkHermMat (x : Fin 4 → ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![((x 0 + x 3 : ℝ) : ℂ), ((x 1 : ℝ) : ℂ) - Complex.I * ((x 2 : ℝ) : ℂ);
     ((x 1 : ℝ) : ℂ) + Complex.I * ((x 2 : ℝ) : ℂ), ((x 0 - x 3 : ℝ) : ℂ)]

/-- Spinor group `SL(2, ℂ)` congruent action `A * X * Aᴴ` on Hermitian `2 × 2` matrices. -/
def sl2Act (A X : Matrix (Fin 2) (Fin 2) ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  A * X * Aᴴ

/-- Hyperbolic boost `diag(exp(φ/2), exp(-φ/2)) ∈ SL(2, ℂ)` along spatial axis 3. -/
noncomputable def sl2Boost3 (φ : ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  Matrix.diagonal ![((Real.exp (φ / 2) : ℝ) : ℂ), ((Real.exp (-(φ / 2)) : ℝ) : ℂ)]

/-- Euclidean determinant identity `det (eucQuatMat x₀ x₁ x₂ x₃) = x₀² + x₁² + x₂² + x₃²`. -/
theorem eucQuatMat_det_real (x0 x1 x2 x3 : ℂ) :
    (eucQuatMat x0 x1 x2 x3).det = x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2 := by
  unfold eucQuatMat
  rw [Matrix.det_fin_two]
  simp only [Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_fin_one]
  ring_nf
  simp only [Complex.I_sq]
  ring

/-- OS time reflection on real Euclidean `4`-vectors equals `-Qᴴ`. -/
theorem eucQuatMat_osReflect (x : Fin 4 → ℝ) :
    eucQuatMat (-((x 0 : ℝ) : ℂ)) (x 1) (x 2) (x 3) =
      -(eucQuatMat (x 0) (x 1) (x 2) (x 3))ᴴ := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [eucQuatMat, Matrix.conjTranspose_apply, Complex.ext_iff]

/-- Every `minkHermMat x` is identically Hermitian (`Xᴴ = X`). -/
theorem minkHermMat_conjTranspose (x : Fin 4 → ℝ) :
    (minkHermMat x)ᴴ = minkHermMat x := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [minkHermMat, Matrix.conjTranspose_apply, Complex.ext_iff]

/-- Lorentzian determinant identity `det (minkHermMat x) = -minkowskiQuad x`. -/
theorem minkHermMat_det (x : Fin 4 → ℝ) :
    (minkHermMat x).det = ((-minkowskiQuad x : ℝ) : ℂ) := by
  unfold minkHermMat
  rw [Matrix.det_fin_two, minkowskiQuad_eq]
  simp only [Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_fin_one]
  push_cast
  ring_nf
  simp only [Complex.I_sq]
  ring

/-- Exact Wick-rotation bridge: `eucQuatMat (i x₀, x₁, x₂, x₃) = i • minkHermMat x`. -/
theorem wick_eucQuatMat_eq_I_smul_minkHermMat (x : Fin 4 → ℝ) :
    eucQuatMat (Complex.I * ((x 0 : ℝ) : ℂ)) (x 1) (x 2) (x 3) =
      Complex.I • minkHermMat x := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [eucQuatMat, minkHermMat] <;>
    ring_nf <;>
    simp only [Complex.I_sq] <;>
    ring

theorem sl2Act_conjTranspose (A X : Matrix (Fin 2) (Fin 2) ℂ) (hX : Xᴴ = X) :
    (sl2Act A X)ᴴ = sl2Act A X := by
  unfold sl2Act
  rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
    hX, Matrix.mul_assoc]

theorem sl2Act_det (A X : Matrix (Fin 2) (Fin 2) ℂ) (hA : A.det = 1) :
    (sl2Act A X).det = X.det := by
  unfold sl2Act
  rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_conjTranspose, hA, star_one, one_mul, mul_one]

theorem sl2Act_doubleCover (A X : Matrix (Fin 2) (Fin 2) ℂ) :
    sl2Act (-A) X = sl2Act A X := by
  unfold sl2Act
  simp

theorem sl2Boost3_det (φ : ℝ) : (sl2Boost3 φ).det = 1 := by
  unfold sl2Boost3
  rw [Matrix.det_diagonal, Fin.prod_univ_two]
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_fin_one]
  rw [← Complex.ofReal_mul, ← Real.exp_add]
  simp

theorem sl2Boost3_add (φ₁ φ₂ : ℝ) :
    sl2Boost3 φ₁ * sl2Boost3 φ₂ = sl2Boost3 (φ₁ + φ₂) := by
  unfold sl2Boost3
  rw [Matrix.diagonal_mul_diagonal]
  congr 1
  ext i
  fin_cases i
  · dsimp
    rw [← Complex.ofReal_mul, ← Real.exp_add]
    congr 2
    ring
  · dsimp
    rw [← Complex.ofReal_mul, ← Real.exp_add]
    congr 2
    ring

/-- Action of `sl2Boost3 φ ∈ SL(2, ℂ)` induces the exact `(cosh φ, sinh φ)` boost in `SO⁺(1,3)`. -/
theorem sl2Act_boost3_eq (φ : ℝ) (x : Fin 4 → ℝ) :
    sl2Act (sl2Boost3 φ) (minkHermMat x) =
      minkHermMat ![x 0 * Real.cosh φ + x 3 * Real.sinh φ,
        x 1, x 2, x 0 * Real.sinh φ + x 3 * Real.cosh φ] := by
  have hexpPosSq :
      ((Real.exp (φ / 2) : ℝ) : ℂ) ^ 2 = ((Real.exp φ : ℝ) : ℂ) := by
    rw [sq, ← Complex.ofReal_mul, ← Real.exp_add]
    ring_nf
  have hexpNegSq :
      ((Real.exp (-(φ / 2)) : ℝ) : ℂ) ^ 2 = ((Real.exp (-φ) : ℝ) : ℂ) := by
    rw [sq, ← Complex.ofReal_mul, ← Real.exp_add]
    ring_nf
  have hexpMix :
      ((Real.exp (φ / 2) : ℝ) : ℂ) * ((Real.exp (-(φ / 2)) : ℝ) : ℂ) = 1 := by
    rw [← Complex.ofReal_mul, ← Real.exp_add]
    simp
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [-Complex.ofReal_exp, sl2Act, sl2Boost3, minkHermMat, Matrix.mul_apply, Fin.sum_univ_two,
      Real.cosh_eq, Real.sinh_eq]
  · linear_combination (((x 0 : ℝ) : ℂ) + ((x 3 : ℝ) : ℂ)) * hexpPosSq
  · linear_combination (((x 1 : ℝ) : ℂ) - Complex.I * ((x 2 : ℝ) : ℂ)) * hexpMix
  · linear_combination (((x 1 : ℝ) : ℂ) + Complex.I * ((x 2 : ℝ) : ℂ)) * hexpMix
  · linear_combination (((x 0 : ℝ) : ℂ) - ((x 3 : ℝ) : ℂ)) * hexpNegSq

end SpinorMatrices

section FutureConePositivity

private theorem rowTraceRe_formula (u v : ℂ) (x : Fin 4 → ℝ) :
    ((u * ((x 0 + x 3 : ℝ) : ℂ) + v * (((x 1 : ℝ) : ℂ) + Complex.I * ((x 2 : ℝ) : ℂ))) *
        star u +
      (u * (((x 1 : ℝ) : ℂ) - Complex.I * ((x 2 : ℝ) : ℂ)) + v * ((x 0 - x 3 : ℝ) : ℂ)) *
        star v).re =
      (u.re ^ 2 + u.im ^ 2 + v.re ^ 2 + v.im ^ 2) * x 0 +
        (2 * (u.re * v.re + u.im * v.im)) * x 1 +
        (2 * (u.im * v.re - u.re * v.im)) * x 2 +
        (u.re ^ 2 + u.im ^ 2 - v.re ^ 2 - v.im ^ 2) * x 3 := by
  simp [Complex.add_re, Complex.mul_re]
  ring

private theorem rowQuad_nonneg {ur ui vr vi x0 x1 x2 x3 : ℝ} (hx0 : 0 < x0)
    (hfut : x1 ^ 2 + x2 ^ 2 + x3 ^ 2 < x0 ^ 2) :
    let w := ur ^ 2 + ui ^ 2 + vr ^ 2 + vi ^ 2
    let n1 := 2 * (ur * vr + ui * vi)
    let n2 := 2 * (ui * vr - ur * vi)
    let n3 := ur ^ 2 + ui ^ 2 - vr ^ 2 - vi ^ 2
    0 ≤ w * x0 + n1 * x1 + n2 * x2 + n3 * x3 ∧
      (0 < w → 0 < w * x0 + n1 * x1 + n2 * x2 + n3 * x3) := by
  intro w n1 n2 n3
  have hnorm : n1 ^ 2 + n2 ^ 2 + n3 ^ 2 = w ^ 2 := by
    dsimp [w, n1, n2, n3]
    ring
  have hlagrange :
      (n1 * x1 + n2 * x2 + n3 * x3) ^ 2 ≤
        (n1 ^ 2 + n2 ^ 2 + n3 ^ 2) * (x1 ^ 2 + x2 ^ 2 + x3 ^ 2) := by
    have hdiff :
        (n1 ^ 2 + n2 ^ 2 + n3 ^ 2) * (x1 ^ 2 + x2 ^ 2 + x3 ^ 2) -
          (n1 * x1 + n2 * x2 + n3 * x3) ^ 2 =
          (n1 * x2 - n2 * x1) ^ 2 + (n1 * x3 - n3 * x1) ^ 2 + (n2 * x3 - n3 * x2) ^ 2 := by
      ring
    linarith [sq_nonneg (n1 * x2 - n2 * x1), sq_nonneg (n1 * x3 - n3 * x1),
      sq_nonneg (n2 * x3 - n3 * x2)]
  have hstrict :
      ∀ hw : 0 < w, 0 < w * x0 + n1 * x1 + n2 * x2 + n3 * x3 := by
    intro hw
    have hlt1 : (n1 ^ 2 + n2 ^ 2 + n3 ^ 2) * (x1 ^ 2 + x2 ^ 2 + x3 ^ 2) < (w * x0) ^ 2 := by
      rw [hnorm]
      have hm := mul_lt_mul_of_pos_left hfut (sq_pos_of_pos hw)
      have hsq : w ^ 2 * x0 ^ 2 = (w * x0) ^ 2 := by ring
      exact hsq ▸ hm
    have hlt2 : (n1 * x1 + n2 * x2 + n3 * x3) ^ 2 < (w * x0) ^ 2 :=
      lt_of_le_of_lt hlagrange hlt1
    have habs : |n1 * x1 + n2 * x2 + n3 * x3| < w * x0 := by
      have h := sq_lt_sq.mp hlt2
      rwa [abs_of_pos (mul_pos hw hx0)] at h
    linarith [(abs_lt.mp habs).1]
  by_cases hw : 0 < w
  · exact ⟨le_of_lt (hstrict hw), fun _ => hstrict hw⟩
  · have hwle : w ≤ 0 := not_lt.mp hw
    have hur : ur = 0 := sq_eq_zero_iff.mp (by
      dsimp [w] at hwle
      linarith [sq_nonneg ur, sq_nonneg ui, sq_nonneg vr, sq_nonneg vi])
    have hui : ui = 0 := sq_eq_zero_iff.mp (by
      dsimp [w] at hwle
      linarith [sq_nonneg ur, sq_nonneg ui, sq_nonneg vr, sq_nonneg vi])
    have hvr : vr = 0 := sq_eq_zero_iff.mp (by
      dsimp [w] at hwle
      linarith [sq_nonneg ur, sq_nonneg ui, sq_nonneg vr, sq_nonneg vi])
    have hvi : vi = 0 := sq_eq_zero_iff.mp (by
      dsimp [w] at hwle
      linarith [sq_nonneg ur, sq_nonneg ui, sq_nonneg vr, sq_nonneg vi])
    have hzero : w * x0 + n1 * x1 + n2 * x2 + n3 * x3 = 0 := by
      dsimp [w, n1, n2, n3]
      simp [hur, hui, hvr, hvi]
    exact ⟨by linarith, fun hpos => absurd hpos hw⟩

/-- Every `A ∈ SL(2, ℂ)` preserves strict future timelike orientation (`Re Tr(A X Aᴴ) > 0`). -/
theorem sl2Act_trace_re_pos_of_future_timelike (A : Matrix (Fin 2) (Fin 2) ℂ)
    (hA : A.det = 1) (x : Fin 4 → ℝ) (hx0 : 0 < x 0)
    (hfut : x 1 ^ 2 + x 2 ^ 2 + x 3 ^ 2 < x 0 ^ 2) :
    0 < (Matrix.trace (sl2Act A (minkHermMat x))).re := by
  have htr :
      (Matrix.trace (sl2Act A (minkHermMat x))).re =
        ((A 0 0 * ((x 0 + x 3 : ℝ) : ℂ) +
              A 0 1 * (((x 1 : ℝ) : ℂ) + Complex.I * ((x 2 : ℝ) : ℂ))) * star (A 0 0) +
            (A 0 0 * (((x 1 : ℝ) : ℂ) - Complex.I * ((x 2 : ℝ) : ℂ)) +
              A 0 1 * ((x 0 - x 3 : ℝ) : ℂ)) * star (A 0 1)).re +
          ((A 1 0 * ((x 0 + x 3 : ℝ) : ℂ) +
              A 1 1 * (((x 1 : ℝ) : ℂ) + Complex.I * ((x 2 : ℝ) : ℂ))) * star (A 1 0) +
            (A 1 0 * (((x 1 : ℝ) : ℂ) - Complex.I * ((x 2 : ℝ) : ℂ)) +
              A 1 1 * ((x 0 - x 3 : ℝ) : ℂ)) * star (A 1 1)).re := by
    unfold sl2Act minkHermMat
    rw [Matrix.trace_fin_two]
    simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_two, Matrix.of_apply,
      Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_fin_one, Complex.add_re]
  rw [htr, rowTraceRe_formula, rowTraceRe_formula]
  have h0 := rowQuad_nonneg (ur := (A 0 0).re) (ui := (A 0 0).im)
    (vr := (A 0 1).re) (vi := (A 0 1).im) hx0 hfut
  have h1 := rowQuad_nonneg (ur := (A 1 0).re) (ui := (A 1 0).im)
    (vr := (A 1 1).re) (vi := (A 1 1).im) hx0 hfut
  by_cases hw0 : 0 < (A 0 0).re ^ 2 + (A 0 0).im ^ 2 + (A 0 1).re ^ 2 + (A 0 1).im ^ 2
  · linarith [h0.2 hw0, h1.1]
  · by_cases hw1 : 0 < (A 1 0).re ^ 2 + (A 1 0).im ^ 2 + (A 1 1).re ^ 2 + (A 1 1).im ^ 2
    · linarith [h0.1, h1.2 hw1]
    · have hw0le := not_lt.mp hw0
      have ha00re : (A 0 0).re = 0 := sq_eq_zero_iff.mp (by
        linarith [sq_nonneg (A 0 0).re, sq_nonneg (A 0 0).im,
          sq_nonneg (A 0 1).re, sq_nonneg (A 0 1).im])
      have ha00im : (A 0 0).im = 0 := sq_eq_zero_iff.mp (by
        linarith [sq_nonneg (A 0 0).re, sq_nonneg (A 0 0).im,
          sq_nonneg (A 0 1).re, sq_nonneg (A 0 1).im])
      have ha01re : (A 0 1).re = 0 := sq_eq_zero_iff.mp (by
        linarith [sq_nonneg (A 0 0).re, sq_nonneg (A 0 0).im,
          sq_nonneg (A 0 1).re, sq_nonneg (A 0 1).im])
      have ha01im : (A 0 1).im = 0 := sq_eq_zero_iff.mp (by
        linarith [sq_nonneg (A 0 0).re, sq_nonneg (A 0 0).im,
          sq_nonneg (A 0 1).re, sq_nonneg (A 0 1).im])
      have ha00 : A 0 0 = 0 := Complex.ext ha00re ha00im
      have ha01 : A 0 1 = 0 := Complex.ext ha01re ha01im
      rw [Matrix.det_fin_two, ha00, ha01] at hA
      norm_num at hA

end FutureConePositivity

end SpinorHermitianWickBridge
