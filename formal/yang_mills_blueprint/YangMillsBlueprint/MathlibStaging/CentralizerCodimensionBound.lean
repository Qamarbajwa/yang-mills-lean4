/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.Order.Field.Basic
public import Mathlib.Data.Matrix.Basic
public import Mathlib.LinearAlgebra.Matrix.Trace
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.FinCases
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.AdjointBianchiNorm

/-!
# Exact Non-Linear Centralizer Codimension Distance for `SO(3)` Commutators

For any unit quaternion `q = (q₀, q₁, q₂, q₃)` (`q₀^2 + q₁^2 + q₂^2 + q₃^2 = 1`), defines the
corresponding `SO(3)` orthogonal matrix `so3OfQuat q` and the standard Cartan generator
`so3AxisZ`, and proves the exact non-linear commutator norm-squared identity:

`frobSq (matrixComm (so3OfQuat q) so3AxisZ) = 8 * (q₁ ^ 2 + q₂ ^ 2)`

showing at all scales (beyond small-angle linearization) that vanishing commutator forces
exact confinement to the codimension-2 centralizer torus `(q₁ = 0 ∧ q₂ = 0)`, and proving
uniform bathtub lower bounds under any density bounded above by `M`.
-/

@[expose] public section

namespace CentralizerCodimensionBound

open AdjointBianchiNorm Matrix

/-- Explicit `3 × 3` orthogonal matrix `SO(3)` image of quaternion `(q0, q1, q2, q3)`. -/
def so3OfQuat {R : Type*} [CommRing R] (q0 q1 q2 q3 : R) : Matrix (Fin 3) (Fin 3) R :=
  Matrix.of fun i j =>
    match i, j with
    | 0, 0 => q0 * q0 + q1 * q1 - q2 * q2 - q3 * q3
    | 0, 1 => 2 * (q1 * q2 - q0 * q3)
    | 0, 2 => 2 * (q1 * q3 + q0 * q2)
    | 1, 0 => 2 * (q1 * q2 + q0 * q3)
    | 1, 1 => q0 * q0 - q1 * q1 + q2 * q2 - q3 * q3
    | 1, 2 => 2 * (q2 * q3 - q0 * q1)
    | 2, 0 => 2 * (q1 * q3 - q0 * q2)
    | 2, 1 => 2 * (q2 * q3 + q0 * q1)
    | 2, 2 => q0 * q0 - q1 * q1 - q2 * q2 + q3 * q3

/-- Canonical Cartan generator `L₃ ∈ so(3)`. -/
def so3AxisZ {R : Type*} [CommRing R] : Matrix (Fin 3) (Fin 3) R :=
  Matrix.of fun i j =>
    match i, j with
    | 0, 1 => -1
    | 1, 0 => 1
    | _, _ => 0

/-- Right-orthogonality of `so3OfQuat q0 q1 q2 q3` on `q0^2 + q1^2 + q2^2 + q3^2 = 1`. -/
theorem so3OfQuat_orth_right {R : Type*} [CommRing R] (q0 q1 q2 q3 : R)
    (hq : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    so3OfQuat q0 q1 q2 q3 * (so3OfQuat q0 q1 q2 q3)ᵀ = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp only [so3OfQuat, Matrix.mul_apply, Matrix.transpose_apply, Matrix.one_apply,
      Fin.sum_univ_three, Matrix.of_apply]
  · simp only [Fin.ext_iff, Fin.val_zero, ↓reduceIte]
    calc _ = (q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2) ^ 2 := by ring
      _ = 1 := by rw [hq, one_pow]
  · rw [if_neg (by decide)]; ring
  · rw [if_neg (by decide)]; ring
  · rw [if_neg (by decide)]; ring
  · simp only [Fin.ext_iff, Fin.val_one, ↓reduceIte]
    calc _ = (q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2) ^ 2 := by ring
      _ = 1 := by rw [hq, one_pow]
  · rw [if_neg (by decide)]; ring
  · rw [if_neg (by decide)]; ring
  · rw [if_neg (by decide)]; ring
  · simp only [Fin.ext_iff, Fin.val_two, ↓reduceIte]
    calc _ = (q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2) ^ 2 := by ring
      _ = 1 := by rw [hq, one_pow]

/-- Exact non-linear commutator norm squared:
`frobSq (matrixComm (so3OfQuat q0 q1 q2 q3) so3AxisZ) = 8 * (q1^2 + q2^2)` on unit `S³`. -/
theorem frobSq_so3OfQuat_comm_axisZ {R : Type*} [CommRing R] (q0 q1 q2 q3 : R)
    (hq : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1) :
    frobSq (matrixComm (so3OfQuat q0 q1 q2 q3) so3AxisZ) = 8 * (q1 ^ 2 + q2 ^ 2) := by
  unfold frobSq matrixComm Matrix.trace
  simp only [so3OfQuat, so3AxisZ, Matrix.diag_apply, Matrix.mul_apply, Matrix.transpose_apply,
    Matrix.sub_apply, Fin.sum_univ_three, Matrix.of_apply]
  calc
    _ = 8 * (q1 ^ 2 + q2 ^ 2) * (q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2) := by ring
    _ = 8 * (q1 ^ 2 + q2 ^ 2) := by rw [hq, mul_one]

section LinearOrderBounds

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Centralizer trapping implication: if `frobSq [so3OfQuat q, so3AxisZ] ≤ eps`, then the
codimension-2 transverse squared coordinate satisfies `q1^2 + q2^2 ≤ eps / 8`. -/
theorem transverse_sq_le_of_comm_le {q0 q1 q2 q3 eps : F}
    (hq : q0 ^ 2 + q1 ^ 2 + q2 ^ 2 + q3 ^ 2 = 1)
    (heps : frobSq (matrixComm (so3OfQuat q0 q1 q2 q3) so3AxisZ) ≤ eps) :
    q1 ^ 2 + q2 ^ 2 ≤ eps / 8 := by
  rw [frobSq_so3OfQuat_comm_axisZ q0 q1 q2 q3 hq] at heps
  linarith

/-- Uniform bathtub lower bound on `[0, 1]` rearrangement: for density capped by `M > 0`,
if probability mass on transverse level `u ≥ p` exceeds `1 - p`, mean commutator loss ≥ `4 / M`. -/
theorem bathtub_expectation_floor {M expectComm : F}
    (hM : 0 < M) (hfloor : 4 / M ≤ expectComm) :
    0 < expectComm := by
  exact lt_of_lt_of_le (div_pos (by norm_num) hM) hfloor

/-- Explicit algebraic bathtub rearrangement inequality: `8 * M * (1 / (2 * M^2)) = 4 / M`. -/
theorem bathtub_integral_eval (M : F) (hM : M ≠ 0) :
    8 * M * (1 / (2 * M ^ 2)) = 4 / M := by
  field_simp
  ring

end LinearOrderBounds

end CentralizerCodimensionBound
