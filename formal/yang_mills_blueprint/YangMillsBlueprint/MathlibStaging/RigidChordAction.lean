/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.Order.Field.Basic
public import Mathlib.Data.Matrix.Basic
public import Mathlib.LinearAlgebra.Matrix.Trace
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.AdjointBianchiNorm
public import YangMillsBlueprint.MathlibStaging.WilsonPlaquetteAction

/-!
# Rigid Frobenius Chord Geometry and Orthogonal Action Bounds

Formalizes the geometric identification of the Wilson plaquette cost with the normalized
squared Frobenius chord distance from the assigned identity frame `1`:
`plaquetteCost M = frobSq (M - 1) / (2 * n)` (`0` at `1`, `2` at antipodal `-1`), proves
conjugate frame invariance `frobSq (g * M * gᵀ - 1) = frobSq (M - 1)`, and establishes
rigid product chord bounds `frobSq (A * B - 1) ≤ 2 * frobSq (A - 1) + 2 * frobSq (B - 1)`
supporting coarse-graining of multi-link Wilson loops.

## Main results

* `RigidChordAction.orth_left_mul_orth`: left-orthogonal closure `(A * B)ᵀ * (A * B) = 1`.
* `RigidChordAction.frobSq_conj_sub_one`: rigid frame conjugation invariance of chord distance.
* `RigidChordAction.frobSq_mul_sub_one_le`: rigid product chord triangle-squared bound.
* `RigidChordAction.frobSq_plaquette_le_four_sum`: 4-link plaquette chord bound by link chords.
* `RigidChordAction.plaquetteCost_eq_frobSq_div`: exact equivalence with Frobenius chord distance.
* `RigidChordAction.plaquetteCost_neg_one_eq_two`: antipodal reflection `-1` hits maximum `2`.
-/

@[expose] public section

namespace RigidChordAction

open Matrix AdjointBianchiNorm WilsonPlaquetteAction

section RingIdentities

/-- Left-orthogonal matrices (`Aᵀ * A = 1`) are closed under matrix multiplication. -/
theorem orth_left_mul_orth {n : ℕ} {R : Type*} [CommRing R]
    {A B : Matrix (Fin n) (Fin n) R} (hA : Aᵀ * A = 1) (hB : Bᵀ * B = 1) :
    (A * B)ᵀ * (A * B) = 1 := by
  rw [Matrix.transpose_mul, Matrix.mul_assoc]
  have h1 : Aᵀ * (A * B) = (Aᵀ * A) * B := by rw [Matrix.mul_assoc]
  rw [h1, hA, Matrix.one_mul, hB]

/-- Negative identity matrix `-1` is orthogonal (`(-1) * (-1)ᵀ = 1`). -/
theorem neg_one_orth {n : ℕ} {R : Type*} [CommRing R] :
    (-1 : Matrix (Fin n) (Fin n) R) * (-1 : Matrix (Fin n) (Fin n) R)ᵀ = 1 := by
  rw [Matrix.transpose_neg, Matrix.transpose_one, neg_mul_neg, Matrix.one_mul]

/-- Frobenius parallelogram identity for square matrices over any commutative ring. -/
theorem frobSq_add_frobSq_sub {n : ℕ} {R : Type*} [CommRing R]
    (X Y : Matrix (Fin n) (Fin n) R) :
    frobSq (X + Y) + frobSq (X - Y) = 2 * frobSq X + 2 * frobSq Y := by
  unfold frobSq
  rw [Matrix.transpose_add, Matrix.transpose_sub]
  simp only [Matrix.add_mul, Matrix.mul_add, Matrix.sub_mul, Matrix.mul_sub,
    Matrix.trace_add, Matrix.trace_sub]
  ring

/-- Squared Frobenius chord distance from identity is invariant under rigid frame conjugation. -/
theorem frobSq_conj_sub_one {n : ℕ} {R : Type*} [CommRing R]
    {g M : Matrix (Fin n) (Fin n) R} (hg1 : g * gᵀ = 1) (hg2 : gᵀ * g = 1) :
    frobSq (g * M * gᵀ - 1) = frobSq (M - 1) := by
  have hfact : g * M * gᵀ - 1 = g * (M - 1) * gᵀ := by
    calc g * M * gᵀ - 1
        = g * M * gᵀ - g * 1 * gᵀ := by rw [Matrix.mul_one, hg1]
      _ = g * (M - 1) * gᵀ := by rw [Matrix.mul_sub, Matrix.sub_mul]
  rw [hfact, frobSq_mul_right_orth _ gᵀ (by simpa [Matrix.transpose_transpose] using hg2)]
  exact frobSq_mul_left_orth g (M - 1) hg2

/-- Telescoping group-difference identity `A * B - 1 = A * (B - 1) + (A - 1)`. -/
theorem mul_sub_one_eq {n : ℕ} {R : Type*} [CommRing R]
    (A B : Matrix (Fin n) (Fin n) R) :
    A * B - 1 = A * (B - 1) + (A - 1) := by
  rw [Matrix.mul_sub, Matrix.mul_one, sub_add_sub_cancel]

end RingIdentities

section OrderedChordBounds

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Frobenius sum-squared bound `frobSq (X + Y) ≤ 2 * frobSq X + 2 * frobSq Y`. -/
theorem frobSq_add_le_two_mul {n : ℕ} (X Y : Matrix (Fin n) (Fin n) F) :
    frobSq (X + Y) ≤ 2 * frobSq X + 2 * frobSq Y := by
  have hpar := frobSq_add_frobSq_sub X Y
  have h0 : 0 ≤ frobSq (X - Y) := frobSq_nonneg (X - Y)
  linarith

/-- Rigid product chord inequality: `frobSq (A * B - 1) ≤ 2 * frobSq (A - 1) + 2 * frobSq (B - 1)`
whenever `A` preserves Euclidean inner products (`Aᵀ * A = 1`). -/
theorem frobSq_mul_sub_one_le {n : ℕ} {A B : Matrix (Fin n) (Fin n) F}
    (hA : Aᵀ * A = 1) :
    frobSq (A * B - 1) ≤ 2 * frobSq (A - 1) + 2 * frobSq (B - 1) := by
  rw [mul_sub_one_eq]
  calc frobSq (A * (B - 1) + (A - 1))
      ≤ 2 * frobSq (A * (B - 1)) + 2 * frobSq (A - 1) := frobSq_add_le_two_mul _ _
    _ = 2 * frobSq (B - 1) + 2 * frobSq (A - 1) := by rw [frobSq_mul_left_orth A (B - 1) hA]
    _ = 2 * frobSq (A - 1) + 2 * frobSq (B - 1) := by ring

/-- Balanced 4-link plaquette chord bound in terms of individual link chord distances:
`frobSq (U1 * U2 * U3 * U4 - 1) ≤ 4 * ∑_i frobSq (Ui - 1)`. -/
theorem frobSq_plaquette_le_four_sum {n : ℕ}
    (U1 U2 U3 U4 : Matrix (Fin n) (Fin n) F)
    (hU1 : U1ᵀ * U1 = 1) (hU2 : U2ᵀ * U2 = 1) (hU3 : U3ᵀ * U3 = 1) :
    frobSq (plaquetteHolonomy U1 U2 U3 U4 - 1) ≤
      4 * (frobSq (U1 - 1) + frobSq (U2 - 1) + frobSq (U3 - 1) + frobSq (U4 - 1)) := by
  have hsplit : plaquetteHolonomy U1 U2 U3 U4 = (U1 * U2) * (U3 * U4) := by
    unfold plaquetteHolonomy
    simp only [Matrix.mul_assoc]
  have h12 : (U1 * U2)ᵀ * (U1 * U2) = 1 := orth_left_mul_orth hU1 hU2
  have houter :
      frobSq ((U1 * U2) * (U3 * U4) - 1) ≤
        2 * frobSq (U1 * U2 - 1) + 2 * frobSq (U3 * U4 - 1) :=
    frobSq_mul_sub_one_le h12
  have hleft : frobSq (U1 * U2 - 1) ≤ 2 * frobSq (U1 - 1) + 2 * frobSq (U2 - 1) :=
    frobSq_mul_sub_one_le hU1
  have hright : frobSq (U3 * U4 - 1) ≤ 2 * frobSq (U3 - 1) + 2 * frobSq (U4 - 1) :=
    frobSq_mul_sub_one_le hU3
  rw [hsplit]
  linarith

end OrderedChordBounds

section FieldConjugation

variable {F : Type*} [Field F]

/-- Normalized Wilson plaquette cost is invariant under orthogonal conjugation
`g * M * gᵀ`. -/
theorem plaquetteCost_conj_invariant {n : ℕ} (g M : Matrix (Fin n) (Fin n) F)
    (hg : gᵀ * g = 1) :
    plaquetteCost (g * M * gᵀ) = plaquetteCost M := by
  have htr : (g * M * gᵀ).trace = M.trace := by
    rw [Matrix.trace_mul_comm]
    have h1 : gᵀ * (g * M) = (gᵀ * g) * M := by rw [Matrix.mul_assoc]
    rw [h1, hg, Matrix.one_mul]
  unfold plaquetteCost
  rw [htr]

end FieldConjugation

section CharZeroFieldCost

variable {F : Type*} [Field F] [CharZero F]

/-- Exact equivalence between normalized Wilson plaquette cost and normalized squared Frobenius
chord distance from the identity matrix `1` for any orthogonal `M` (`n > 0`). -/
theorem plaquetteCost_eq_frobSq_div {n : ℕ} (hn : 0 < n)
    {M : Matrix (Fin n) (Fin n) F} (hM : M * Mᵀ = 1) :
    plaquetteCost M = frobSq (M - 1) / (2 * (n : F)) := by
  have hnNe : (n : F) ≠ 0 := Nat.cast_ne_zero.mpr (ne_of_gt hn)
  have h2n : (2 : F) * (n : F) ≠ 0 := mul_ne_zero two_ne_zero hnNe
  rw [frobSq_sub_one_eq_of_orth hM]
  unfold plaquetteCost
  rw [eq_div_iff h2n]
  calc (1 - M.trace / (n : F)) * (2 * (n : F))
      = 2 * ((n : F) - (M.trace / (n : F)) * (n : F)) := by ring
    _ = 2 * ((n : F) - M.trace) := by rw [div_mul_cancel₀ _ hnNe]

/-- At the assigned identity frame `1`, the Wilson plaquette cost vanishes identically. -/
theorem plaquetteCost_one_eq_zero {n : ℕ} (hn : 0 < n) :
    plaquetteCost (1 : Matrix (Fin n) (Fin n) F) = 0 := by
  have hnNe : (n : F) ≠ 0 := Nat.cast_ne_zero.mpr (ne_of_gt hn)
  unfold plaquetteCost
  rw [Matrix.trace_one, Fintype.card_fin, div_self hnNe, sub_self]

/-- At the antipodal negative identity `-1`, the Wilson plaquette cost attains its sharp
maximum `2`. -/
theorem plaquetteCost_neg_one_eq_two {n : ℕ} (hn : 0 < n) :
    plaquetteCost (-1 : Matrix (Fin n) (Fin n) F) = 2 := by
  have hnNe : (n : F) ≠ 0 := Nat.cast_ne_zero.mpr (ne_of_gt hn)
  unfold plaquetteCost
  rw [Matrix.trace_neg, Matrix.trace_one, Fintype.card_fin, neg_div, div_self hnNe,
    sub_neg_eq_add, one_add_one_eq_two]

end CharZeroFieldCost

end RigidChordAction
