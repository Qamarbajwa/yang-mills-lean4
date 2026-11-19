/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.BigOperators.Fin
public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Algebra.Order.Field.Basic
public import Mathlib.Data.Matrix.Basic
public import Mathlib.LinearAlgebra.Matrix.Trace
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.AdjointBianchiNorm
public import YangMillsBlueprint.MathlibStaging.LatticeHaarGibbs

/-!
# Four-Link Wilson Plaquette Action and Unconditional Single-Link Gibbs Bounds

Proves gauge invariance of the 4-link plaquette trace under orthogonal gauge transformations,
derives exact Frobenius trace bounds `-(n : F) ≤ M.trace ≤ n` (`0 ≤ plaquetteCost M ≤ 2`),
establishes uniform `m`-staple action oscillation bounds `0 ≤ stapleAction β staples U ≤ 2*m*β`,
and lifts them unconditionally via `LatticeHaarGibbs` to single-link Haar Gibbs density caps
(`≤ exp (2 * m * β)`) and expectation floors (`≥ exp (-(2 * m * β)) * ∫ f ∂μ_Haar`).

## Main results

* `WilsonPlaquetteAction.orth_mul_orth`: product of orthogonal matrices is orthogonal.
* `WilsonPlaquetteAction.plaquette_trace_gauge_invariant`: exact 4-link trace invariance.
* `WilsonPlaquetteAction.orth_trace_bounds`: `-(n : F) ≤ M.trace ≤ (n : F)`.
* `WilsonPlaquetteAction.plaquetteCost_mem_Icc`: normalized plaquette cost in `[0, 2]`.
* `WilsonPlaquetteAction.stapleAction_mem_Icc`: `m`-staple action in `[0, 2 * m * β]`.
* `WilsonPlaquetteAction.singleLink_conditional_density_cap`: unconditional density cap.
* `WilsonPlaquetteAction.singleLink_conditional_variance_floor`: unconditional variance floor.
-/

@[expose] public section

namespace WilsonPlaquetteAction

open Matrix MeasureTheory

section PlaquetteInvariance

/-- Ordered product of four link matrices around an elementary lattice plaquette. -/
def plaquetteHolonomy {n : ℕ} {R : Type*} [CommRing R]
    (U1 U2 U3 U4 : Matrix (Fin n) (Fin n) R) : Matrix (Fin n) (Fin n) R :=
  U1 * U2 * U3 * U4

/-- Orthogonal matrices (`A * Aᵀ = 1`) are closed under matrix multiplication. -/
theorem orth_mul_orth {n : ℕ} {R : Type*} [CommRing R]
    {A B : Matrix (Fin n) (Fin n) R} (hA : A * Aᵀ = 1) (hB : B * Bᵀ = 1) :
    (A * B) * (A * B)ᵀ = 1 := by
  rw [Matrix.transpose_mul, Matrix.mul_assoc]
  have h1 : A * (B * (Bᵀ * Aᵀ)) = A * ((B * Bᵀ) * Aᵀ) := by
    simp only [Matrix.mul_assoc]
  rw [h1, hB, Matrix.one_mul, hA]

/-- Exact gauge invariance of the 4-link plaquette trace under orthogonal vertex gauge
transformations `U_ij ↦ g_i * U_ij * g_jᵀ` (`gᵀ * g = 1`). -/
theorem plaquette_trace_gauge_invariant {n : ℕ} {R : Type*} [CommRing R]
    (g1 g2 g3 g4 U1 U2 U3 U4 : Matrix (Fin n) (Fin n) R)
    (hg1 : g1ᵀ * g1 = 1) (hg2 : g2ᵀ * g2 = 1)
    (hg3 : g3ᵀ * g3 = 1) (hg4 : g4ᵀ * g4 = 1) :
    (plaquetteHolonomy (g1 * U1 * g2ᵀ) (g2 * U2 * g3ᵀ)
      (g3 * U3 * g4ᵀ) (g4 * U4 * g1ᵀ)).trace =
      (plaquetteHolonomy U1 U2 U3 U4).trace := by
  have h12 : (g1 * U1 * g2ᵀ) * (g2 * U2 * g3ᵀ) = g1 * U1 * U2 * g3ᵀ := by
    calc (g1 * U1 * g2ᵀ) * (g2 * U2 * g3ᵀ)
        = g1 * U1 * (g2ᵀ * g2) * U2 * g3ᵀ := by simp only [Matrix.mul_assoc]
      _ = g1 * U1 * U2 * g3ᵀ := by rw [hg2, Matrix.mul_one]
  have h123 : (g1 * U1 * U2 * g3ᵀ) * (g3 * U3 * g4ᵀ) = g1 * U1 * U2 * U3 * g4ᵀ := by
    calc (g1 * U1 * U2 * g3ᵀ) * (g3 * U3 * g4ᵀ)
        = g1 * U1 * U2 * (g3ᵀ * g3) * U3 * g4ᵀ := by simp only [Matrix.mul_assoc]
      _ = g1 * U1 * U2 * U3 * g4ᵀ := by rw [hg3, Matrix.mul_one]
  have h1234 :
      (g1 * U1 * U2 * U3 * g4ᵀ) * (g4 * U4 * g1ᵀ) =
        (g1 * (U1 * U2 * U3 * U4)) * g1ᵀ := by
    calc (g1 * U1 * U2 * U3 * g4ᵀ) * (g4 * U4 * g1ᵀ)
        = g1 * U1 * U2 * U3 * (g4ᵀ * g4) * U4 * g1ᵀ := by simp only [Matrix.mul_assoc]
      _ = g1 * U1 * U2 * U3 * U4 * g1ᵀ := by rw [hg4, Matrix.mul_one]
      _ = (g1 * (U1 * U2 * U3 * U4)) * g1ᵀ := by simp only [Matrix.mul_assoc]
  unfold plaquetteHolonomy
  rw [h12, h123, h1234, Matrix.trace_mul_comm]
  have hc : g1ᵀ * (g1 * (U1 * U2 * U3 * U4)) = (g1ᵀ * g1) * (U1 * U2 * U3 * U4) := by
    simp only [Matrix.mul_assoc]
  rw [hc, hg1, Matrix.one_mul]

/-- Frobenius identity `frobSq (M - 1) = 2 * (n - M.trace)` for orthogonal `M`. -/
theorem frobSq_sub_one_eq_of_orth {n : ℕ} {R : Type*} [CommRing R]
    {M : Matrix (Fin n) (Fin n) R} (hM : M * Mᵀ = 1) :
    AdjointBianchiNorm.frobSq (M - 1) = 2 * ((n : R) - M.trace) := by
  unfold AdjointBianchiNorm.frobSq
  rw [Matrix.transpose_sub, Matrix.transpose_one, Matrix.sub_mul, Matrix.mul_sub, Matrix.mul_sub]
  simp only [Matrix.mul_one, Matrix.one_mul, hM, Matrix.trace_sub, Matrix.trace_transpose]
  rw [Matrix.trace_one, Fintype.card_fin]
  ring

/-- Frobenius identity `frobSq (M + 1) = 2 * (n + M.trace)` for orthogonal `M`. -/
theorem frobSq_add_one_eq_of_orth {n : ℕ} {R : Type*} [CommRing R]
    {M : Matrix (Fin n) (Fin n) R} (hM : M * Mᵀ = 1) :
    AdjointBianchiNorm.frobSq (M + 1) = 2 * ((n : R) + M.trace) := by
  unfold AdjointBianchiNorm.frobSq
  rw [Matrix.transpose_add, Matrix.transpose_one, Matrix.add_mul, Matrix.mul_add, Matrix.mul_add]
  simp only [Matrix.mul_one, Matrix.one_mul, hM, Matrix.trace_add, Matrix.trace_transpose]
  rw [Matrix.trace_one, Fintype.card_fin]
  ring

end PlaquetteInvariance

section OrthogonalTraceBounds

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Sharp trace bounds `-(n : F) ≤ M.trace ≤ n` for any orthogonal matrix `M * Mᵀ = 1`. -/
theorem orth_trace_bounds {n : ℕ} {M : Matrix (Fin n) (Fin n) F} (hM : M * Mᵀ = 1) :
    -(n : F) ≤ M.trace ∧ M.trace ≤ (n : F) := by
  have hsub : 0 ≤ 2 * ((n : F) - M.trace) := by
    rw [← frobSq_sub_one_eq_of_orth hM]
    exact AdjointBianchiNorm.frobSq_nonneg (M - 1)
  have hadd : 0 ≤ 2 * ((n : F) + M.trace) := by
    rw [← frobSq_add_one_eq_of_orth hM]
    exact AdjointBianchiNorm.frobSq_nonneg (M + 1)
  exact ⟨by linarith, by linarith⟩

/-- Normalized Wilson plaquette cost `1 - Tr(M) / n`. -/
def plaquetteCost {n : ℕ} (M : Matrix (Fin n) (Fin n) F) : F :=
  1 - M.trace / (n : F)

/-- Boundedness of the Wilson plaquette cost inside `[0, 2]` for orthogonal `M` (`n > 0`). -/
theorem plaquetteCost_mem_Icc {n : ℕ} (hn : 0 < n) {M : Matrix (Fin n) (Fin n) F}
    (hM : M * Mᵀ = 1) :
    0 ≤ plaquetteCost M ∧ plaquetteCost M ≤ 2 := by
  have hnF : (0 : F) < (n : F) := Nat.cast_pos.mpr hn
  rcases orth_trace_bounds hM with ⟨hlo, hhi⟩
  have hdivLo : -1 ≤ M.trace / (n : F) := by
    rw [le_div_iff₀ hnF]
    linarith
  have hdivHi : M.trace / (n : F) ≤ 1 := by
    rw [div_le_iff₀ hnF]
    linarith
  unfold plaquetteCost
  exact ⟨by linarith, by linarith⟩

/-- Single-link conditional Wilson staple action `β * ∑ j, (1 - Tr(U * staple j) / n)`. -/
def stapleAction {m n : ℕ} (β : F) (staples : Fin m → Matrix (Fin n) (Fin n) F)
    (U : Matrix (Fin n) (Fin n) F) : F :=
  β * ∑ j : Fin m, plaquetteCost (U * staples j)

/-- Exact uniform oscillation interval `[0, 2 * m * β]` for the single-link Wilson staple
action over any orthogonal family of staples, independently of spatial box volume `L`. -/
theorem stapleAction_mem_Icc {m n : ℕ} (hn : 0 < n) {β : F} (hβ : 0 ≤ β)
    {staples : Fin m → Matrix (Fin n) (Fin n) F}
    (hS : ∀ j : Fin m, staples j * (staples j)ᵀ = 1)
    {U : Matrix (Fin n) (Fin n) F} (hU : U * Uᵀ = 1) :
    0 ≤ stapleAction β staples U ∧ stapleAction β staples U ≤ 2 * (m : F) * β := by
  have hterm : ∀ j : Fin m, 0 ≤ plaquetteCost (U * staples j) ∧
      plaquetteCost (U * staples j) ≤ 2 := fun j =>
    plaquetteCost_mem_Icc hn (orth_mul_orth hU (hS j))
  have hsum0 : 0 ≤ ∑ j : Fin m, plaquetteCost (U * staples j) :=
    Finset.sum_nonneg fun j _ => (hterm j).1
  have hsum2 : ∑ j : Fin m, plaquetteCost (U * staples j) ≤ 2 * (m : F) := by
    calc ∑ j : Fin m, plaquetteCost (U * staples j)
        ≤ ∑ _j : Fin m, (2 : F) := Finset.sum_le_sum fun j _ => (hterm j).2
      _ = 2 * (m : F) := by
          simp [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul, mul_comm]
  unfold stapleAction
  refine ⟨mul_nonneg hβ hsum0, ?_⟩
  have hmul : β * ∑ j : Fin m, plaquetteCost (U * staples j) ≤ β * (2 * (m : F)) :=
    mul_le_mul_of_nonneg_left hsum2 hβ
  have hrw : β * (2 * (m : F)) = 2 * (m : F) * β := by ring
  linarith

end OrthogonalTraceBounds

section SingleLinkConditionalGibbs

/-- Unconditional single-link conditional Boltzmann density cap `≤ Real.exp (2 * m * β)`
relative to `compactHaarProb G`, independent of external staples and lattice volume. -/
theorem singleLink_conditional_density_cap {G : Type*} [Group G] [TopologicalSpace G]
    [CompactSpace G] [IsTopologicalGroup G] [MeasurableSpace G] [BorelSpace G]
    {m n : ℕ} (hn : 0 < n) {β : ℝ} (hβ : 0 ≤ β)
    (rep : G → Matrix (Fin n) (Fin n) ℝ) (hrep : ∀ g : G, rep g * (rep g)ᵀ = 1)
    (staples : Fin m → Matrix (Fin n) (Fin n) ℝ)
    (hS : ∀ j : Fin m, staples j * (staples j)ᵀ = 1)
    (hint : Integrable
      (LatticeHaarGibbs.expWeight (fun g => stapleAction β staples (rep g)))
      (LatticeHaarGibbs.compactHaarProb G))
    (g : G) :
    LatticeHaarGibbs.expWeight (fun x => stapleAction β staples (rep x)) g /
        LatticeHaarGibbs.partitionIntegral (LatticeHaarGibbs.compactHaarProb G)
          (fun x => stapleAction β staples (rep x)) ≤
      Real.exp (2 * (m : ℝ) * β) := by
  have hmin : ∀ x : G, (0 : ℝ) ≤ stapleAction β staples (rep x) := fun x =>
    (stapleAction_mem_Icc hn hβ hS (hrep x)).1
  have hmax : ∀ x : G, stapleAction β staples (rep x) ≤ 2 * (m : ℝ) * β := fun x =>
    (stapleAction_mem_Icc hn hβ hS (hrep x)).2
  have hcap := LatticeHaarGibbs.boltzmannDensity_le_exp_osc hint hmin hmax g
  rwa [sub_zero] at hcap

/-- Unconditional single-link conditional Boltzmann expectation lower bound
`Real.exp (-(2 * m * β)) * ∫ f dμ_Haar ≤ weightedExpectation` for non-negative `f`. -/
theorem singleLink_conditional_variance_floor {G : Type*} [Group G] [TopologicalSpace G]
    [CompactSpace G] [IsTopologicalGroup G] [MeasurableSpace G] [BorelSpace G]
    {m n : ℕ} (hn : 0 < n) {β : ℝ} (hβ : 0 ≤ β)
    (rep : G → Matrix (Fin n) (Fin n) ℝ) (hrep : ∀ g : G, rep g * (rep g)ᵀ = 1)
    (staples : Fin m → Matrix (Fin n) (Fin n) ℝ)
    (hS : ∀ j : Fin m, staples j * (staples j)ᵀ = 1)
    (f : G → ℝ)
    (hint : Integrable
      (LatticeHaarGibbs.expWeight (fun x => stapleAction β staples (rep x)))
      (LatticeHaarGibbs.compactHaarProb G))
    (hf : Integrable f (LatticeHaarGibbs.compactHaarProb G))
    (hfw : Integrable
      (fun x => f x * LatticeHaarGibbs.expWeight (fun y => stapleAction β staples (rep y)) x)
      (LatticeHaarGibbs.compactHaarProb G))
    (hf0 : ∀ x : G, 0 ≤ f x) :
    Real.exp (-(2 * (m : ℝ) * β)) * (∫ x, f x ∂(LatticeHaarGibbs.compactHaarProb G)) ≤
      LatticeHaarGibbs.weightedExpectation (LatticeHaarGibbs.compactHaarProb G)
        (fun x => stapleAction β staples (rep x)) f := by
  have hmin : ∀ x : G, (0 : ℝ) ≤ stapleAction β staples (rep x) := fun x =>
    (stapleAction_mem_Icc hn hβ hS (hrep x)).1
  have hmax : ∀ x : G, stapleAction β staples (rep x) ≤ 2 * (m : ℝ) * β := fun x =>
    (stapleAction_mem_Icc hn hβ hS (hrep x)).2
  have hexp := LatticeHaarGibbs.weightedExpectation_ge_exp_neg_osc_mul_integral
    hint hf hfw hf0 hmin hmax
  rwa [sub_zero] at hexp

end SingleLinkConditionalGibbs

end WilsonPlaquetteAction
