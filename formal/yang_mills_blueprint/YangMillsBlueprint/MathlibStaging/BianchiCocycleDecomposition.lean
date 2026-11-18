/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.Order.Field.Basic
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.BianchiDyadicAccumulation
public import YangMillsBlueprint.MathlibStaging.StokesAdjointDispersion

/-!
# Orthogonal Adjoint Cocycle Composition Decomposition

Decomposes the commutator norm squared of a product of two orthogonal matrices `V * W`
into the individual losses plus an explicit cross-correlation remainder term:

* `BianchiCocycleDecomposition.adjDelta`: transport residual `adjAction U X - X`.
* `BianchiCocycleDecomposition.adjDelta_mul`: linear cocycle rule for `V * W`.
* `BianchiCocycleDecomposition.frobSq_matrixComm_mul_eq`: exact norm-squared expansion.
* `BianchiCocycleDecomposition.normalizedLoss`: normalized loss `‖[U, X]‖² / (2 ‖X‖²)`.
* `BianchiCocycleDecomposition.cocycleLoss_split_eq`: exact dyadic + remainder split.
* `BianchiCocycleDecomposition.dyadic_step_ge_of_remainder_bound`: monotonic lower bound.
-/

@[expose] public section

namespace BianchiCocycleDecomposition

open AdjointBianchiNorm BianchiDyadicAccumulation Matrix StokesAdjointDispersion

/-- Transport residual `adjAction U X - X`. -/
def adjDelta {n : ℕ} {R : Type*} [CommRing R] (U X : Matrix (Fin n) (Fin n) R) :
    Matrix (Fin n) (Fin n) R :=
  adjAction U X - X

/-- Orthogonal `adjAction` composes multiplicatively under `V * W`. -/
theorem adjAction_mul {n : ℕ} {R : Type*} [CommRing R]
    (V W X : Matrix (Fin n) (Fin n) R) :
    adjAction (V * W) X = adjAction V (adjAction W X) := by
  unfold adjAction
  rw [Matrix.transpose_mul]
  simp only [Matrix.mul_assoc]

/-- Left distribution of `adjAction V` over subtraction. -/
theorem adjAction_sub {n : ℕ} {R : Type*} [CommRing R]
    (V A B : Matrix (Fin n) (Fin n) R) :
    adjAction V (A - B) = adjAction V A - adjAction V B := by
  unfold adjAction
  rw [Matrix.mul_sub, Matrix.sub_mul]

/-- Exact cocycle composition law for `adjDelta (V * W) X`. -/
theorem adjDelta_mul {n : ℕ} {R : Type*} [CommRing R]
    (V W X : Matrix (Fin n) (Fin n) R) :
    adjDelta (V * W) X = adjAction V (adjDelta W X) + adjDelta V X := by
  unfold adjDelta
  rw [adjAction_mul, adjAction_sub]
  abel

/-- Product of two right-orthogonal matrices stays right-orthogonal. -/
theorem mul_orth_right {n : ℕ} {R : Type*} [CommRing R]
    {V W : Matrix (Fin n) (Fin n) R} (hV : V * Vᵀ = 1) (hW : W * Wᵀ = 1) :
    (V * W) * (V * W)ᵀ = 1 := by
  rw [Matrix.transpose_mul, Matrix.mul_assoc, ← Matrix.mul_assoc W Wᵀ Vᵀ,
    hW, Matrix.one_mul, hV]

/-- Product of two left-orthogonal matrices stays left-orthogonal. -/
theorem mul_orth_left {n : ℕ} {R : Type*} [CommRing R]
    {V W : Matrix (Fin n) (Fin n) R} (hV : Vᵀ * V = 1) (hW : Wᵀ * W = 1) :
    (V * W)ᵀ * (V * W) = 1 := by
  rw [Matrix.transpose_mul, Matrix.mul_assoc, ← Matrix.mul_assoc Vᵀ V W,
    hV, Matrix.one_mul, hW]

/-- Exact commutator norm-squared expansion for composed orthogonal transporters `V * W`. -/
theorem frobSq_matrixComm_mul_eq {n : ℕ} {R : Type*} [CommRing R]
    (V W X : Matrix (Fin n) (Fin n) R)
    (hV1 : V * Vᵀ = 1) (hV2 : Vᵀ * V = 1)
    (hW1 : W * Wᵀ = 1) (hW2 : Wᵀ * W = 1) :
    frobSq (matrixComm (V * W) X) =
      frobSq (matrixComm V X) + frobSq (matrixComm W X) +
        2 * frobInner (adjAction V (adjDelta W X)) (adjDelta V X) := by
  have hVW1 := mul_orth_right hV1 hW1
  have hVW2 := mul_orth_left hV2 hW2
  rw [← frobSq_adjAction_sub_eq (V * W) X hVW1 hVW2]
  change frobSq (adjDelta (V * W) X) = _
  rw [adjDelta_mul, frobSq_add_eq, frobSq_adjAction V (adjDelta W X) hV2]
  have hW : frobSq (adjDelta W X) = frobSq (matrixComm W X) :=
    frobSq_adjAction_sub_eq W X hW1 hW2
  have hV : frobSq (adjDelta V X) = frobSq (matrixComm V X) :=
    frobSq_adjAction_sub_eq V X hV1 hV2
  rw [hW, hV]
  ring

section NormalizedLoss

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Normalized adjoint commutator loss `frobSq [U, X] / (2 * frobSq X)`. -/
def normalizedLoss {n : ℕ} (U X : Matrix (Fin n) (Fin n) F) : F :=
  frobSq (matrixComm U X) / (2 * frobSq X)

/-- Cross-correlation remainder separating `normalizedLoss (V * W) X` from the
independent dyadic composition formula `δV + δW - δV * δW`. -/
def cocycleRemainder {n : ℕ} (V W X : Matrix (Fin n) (Fin n) F) : F :=
  frobInner (adjAction V (adjDelta W X)) (adjDelta V X) / frobSq X +
    normalizedLoss V X * normalizedLoss W X

/-- Exact dyadic + remainder split for `normalizedLoss (V * W) X`. -/
theorem cocycleLoss_split_eq {n : ℕ} (V W X : Matrix (Fin n) (Fin n) F)
    (hV1 : V * Vᵀ = 1) (hV2 : Vᵀ * V = 1)
    (hW1 : W * Wᵀ = 1) (hW2 : Wᵀ * W = 1)
    (hX : frobSq X ≠ 0) :
    normalizedLoss (V * W) X =
      (normalizedLoss V X + normalizedLoss W X -
        normalizedLoss V X * normalizedLoss W X) + cocycleRemainder V W X := by
  unfold cocycleRemainder
  unfold normalizedLoss
  rw [frobSq_matrixComm_mul_eq V W X hV1 hV2 hW1 hW2]
  have h2 : (2 : F) ≠ 0 := two_ne_zero
  field_simp
  ring

/-- Dyadic monotone lower bound: whenever `d ≤ dV, dW ≤ 1` and the cocycle remainder
satisfies `-(1 - c) * (2 * d - d^2) ≤ eps`, the composed loss retains at least
`c * dyadicLossStep d`. -/
theorem dyadic_step_ge_of_remainder_bound {c d dV dW dVW eps : F}
    (hsplit : dVW = (dV + dW - dV * dW) + eps)
    (hdV0 : d ≤ dV) (hdW0 : d ≤ dW) (hdV1 : dV ≤ 1) (hdW1 : dW ≤ 1)
    (hrem : -(1 - c) * dyadicLossStep d ≤ eps) :
    c * dyadicLossStep d ≤ dVW := by
  have h1 : 0 ≤ 1 - dV := sub_nonneg.mpr hdV1
  have h2 : 0 ≤ 1 - dW := sub_nonneg.mpr hdW1
  have h3 : 1 - dV ≤ 1 - d := sub_le_sub_left hdV0 1
  have h4 : 1 - dW ≤ 1 - d := sub_le_sub_left hdW0 1
  have hsub : (1 - dV) * (1 - dW) ≤ (1 - d) * (1 - d) :=
    mul_le_mul h3 h4 h2 (le_trans h1 h3)
  have hcomb : dyadicLossStep d ≤ dV + dW - dV * dW := by
    unfold dyadicLossStep
    linarith
  have htot : dyadicLossStep d + eps ≤ dVW := by linarith
  have hc : c * dyadicLossStep d = dyadicLossStep d + -(1 - c) * dyadicLossStep d := by
    ring
  linarith

end NormalizedLoss

end BianchiCocycleDecomposition
