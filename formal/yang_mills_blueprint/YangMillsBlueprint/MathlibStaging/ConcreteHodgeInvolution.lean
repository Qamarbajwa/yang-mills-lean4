/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Analysis.InnerProductSpace.PiL2
public import Mathlib.LinearAlgebra.Dimension.Finrank
public import Mathlib.Tactic.NormNum
public import YangMillsBlueprint.MathlibStaging.SelfDualWaveProjection

/-!
# Concrete Hodge Dual Involutions in 4D (`6 = 3 + 3`) and 8D (`70 = 35 + 35`)

Constructs explicit symmetric involutions `halfSwap m` on `EuclideanSpace ℝ (Fin (m + m))`
together with injective `+1` (self-dual) and `-1` (anti-self-dual) embeddings `sdEmbed m` and
`asdEmbed m` of rank `m`.

Specializing unconditionally to `m = 3` (`Fin 6`, `Nat.choose 4 2 = 3 + 3`) and `m = 35`
(`Fin 70`, `Nat.choose 8 4 = 35 + 35`) realizes the 4D Yang-Mills curvature and 8D `∧⁴ S₈⁺`
splittings as genuine concrete `SelfDualWaveProjection.SymmInvolution` operators with exact
subspace `Module.finrank` counts and pointwise Bogomol'nyi inequalities.
-/

@[expose] public section

namespace ConcreteHodgeInvolution

open SelfDualWaveProjection

/-- Half-swap permutation on `Fin (m + m)` exchanging lower block `[0, m)` with upper block
`[m, 2m)`. -/
def swapIdx (m : ℕ) (i : Fin (m + m)) : Fin (m + m) :=
  if h : (i : ℕ) < m then ⟨(i : ℕ) + m, by omega⟩ else ⟨(i : ℕ) - m, by omega⟩

/-- Half-swap index map is an involution. -/
theorem swapIdx_invol (m : ℕ) (i : Fin (m + m)) : swapIdx m (swapIdx m i) = i := by
  by_cases h : (i : ℕ) < m
  · have hnot : ¬ ((i : ℕ) + m < m) := by omega
    apply Fin.ext
    simp [swapIdx, h, hnot]
  · have hlt : (i : ℕ) - m < m := by omega
    apply Fin.ext
    simp [swapIdx, h, hlt]
    omega

/-- Equivalence permutation wrapper for `swapIdx m`. -/
def swapEquiv (m : ℕ) : Equiv.Perm (Fin (m + m)) where
  toFun := swapIdx m
  invFun := swapIdx m
  left_inv := swapIdx_invol m
  right_inv := swapIdx_invol m

/-- Explicit linear Hodge-type half-swap operator on `EuclideanSpace ℝ (Fin (m + m))`. -/
def halfSwap (m : ℕ) :
    EuclideanSpace ℝ (Fin (m + m)) →ₗ[ℝ] EuclideanSpace ℝ (Fin (m + m)) where
  toFun x := WithLp.toLp 2 fun i => x (swapIdx m i)
  map_add' x y := by
    ext i
    simp
  map_smul' c x := by
    ext i
    simp

@[simp]
theorem halfSwap_apply (m : ℕ) (x : EuclideanSpace ℝ (Fin (m + m))) (i : Fin (m + m)) :
    halfSwap m x i = x (swapIdx m i) := rfl

/-- `halfSwap m` is a genuine symmetric involution (`SymmInvolution`) on `EuclideanSpace`. -/
theorem symmInvolution_halfSwap (m : ℕ) : SymmInvolution (halfSwap m) where
  invol x := by
    ext i
    simp [swapIdx_invol]
  symm x y := by
    simp only [EuclideanSpace.inner_eq_star_dotProduct, dotProduct, star_trivial]
    refine Fintype.sum_equiv (swapEquiv m)
      (fun i => y i * x (swapIdx m i)) (fun i => y (swapIdx m i) * x i) ?_
    intro i
    show y i * x (swapIdx m i) = y (swapIdx m (swapIdx m i)) * x (swapIdx m i)
    rw [swapIdx_invol]

/-- Explicit injective embedding of `EuclideanSpace ℝ (Fin m)` onto the `+1` (self-dual)
eigenspace of `halfSwap m`. -/
def sdEmbed (m : ℕ) :
    EuclideanSpace ℝ (Fin m) →ₗ[ℝ] EuclideanSpace ℝ (Fin (m + m)) where
  toFun u := WithLp.toLp 2 fun i =>
    if h : (i : ℕ) < m then u ⟨(i : ℕ), h⟩ else u ⟨(i : ℕ) - m, by omega⟩
  map_add' u v := by
    ext i
    by_cases h : (i : ℕ) < m <;> simp [h]
  map_smul' c u := by
    ext i
    by_cases h : (i : ℕ) < m <;> simp [h]

/-- Explicit injective embedding of `EuclideanSpace ℝ (Fin m)` onto the `-1` (anti-self-dual)
eigenspace of `halfSwap m`. -/
def asdEmbed (m : ℕ) :
    EuclideanSpace ℝ (Fin m) →ₗ[ℝ] EuclideanSpace ℝ (Fin (m + m)) where
  toFun u := WithLp.toLp 2 fun i =>
    if h : (i : ℕ) < m then u ⟨(i : ℕ), h⟩ else -u ⟨(i : ℕ) - m, by omega⟩
  map_add' u v := by
    ext i
    by_cases h : (i : ℕ) < m
    · simp [h]
    · simp [h]
      ring
  map_smul' c u := by
    ext i
    by_cases h : (i : ℕ) < m <;> simp [h]

/-- `sdEmbed m u` lies strictly in the `+1` eigenspace of `halfSwap m`. -/
theorem halfSwap_sdEmbed (m : ℕ) (u : EuclideanSpace ℝ (Fin m)) :
    halfSwap m (sdEmbed m u) = sdEmbed m u := by
  ext i
  by_cases h : (i : ℕ) < m
  · have hnot : ¬ ((i : ℕ) + m < m) := by omega
    simp [halfSwap, sdEmbed, swapIdx, h, hnot]
  · have hlt : (i : ℕ) - m < m := by omega
    simp [halfSwap, sdEmbed, swapIdx, h, hlt]

/-- `asdEmbed m u` lies strictly in the `-1` eigenspace of `halfSwap m`. -/
theorem halfSwap_asdEmbed (m : ℕ) (u : EuclideanSpace ℝ (Fin m)) :
    halfSwap m (asdEmbed m u) = -asdEmbed m u := by
  ext i
  by_cases h : (i : ℕ) < m
  · have hnot : ¬ ((i : ℕ) + m < m) := by omega
    simp [halfSwap, asdEmbed, swapIdx, h, hnot]
  · have hlt : (i : ℕ) - m < m := by omega
    simp [halfSwap, asdEmbed, swapIdx, h, hlt]

/-- `sdEmbed m` is injective. -/
theorem sdEmbed_injective (m : ℕ) : Function.Injective (sdEmbed m) := by
  intro u v huv
  ext k
  have hk := congrArg (fun x : EuclideanSpace ℝ (Fin (m + m)) => x ⟨k.val, by omega⟩) huv
  simpa [sdEmbed, k.isLt] using hk

/-- `asdEmbed m` is injective. -/
theorem asdEmbed_injective (m : ℕ) : Function.Injective (asdEmbed m) := by
  intro u v huv
  ext k
  have hk := congrArg (fun x : EuclideanSpace ℝ (Fin (m + m)) => x ⟨k.val, by omega⟩) huv
  simpa [asdEmbed, k.isLt] using hk

/-- Exact subspace dimension of the concrete self-dual half: `finrank = m`. -/
theorem finrank_range_sdEmbed (m : ℕ) :
    Module.finrank ℝ (LinearMap.range (sdEmbed m)) = m := by
  rw [LinearMap.finrank_range_of_inj (sdEmbed_injective m), finrank_euclideanSpace_fin]

/-- Exact subspace dimension of the concrete anti-self-dual half: `finrank = m`. -/
theorem finrank_range_asdEmbed (m : ℕ) :
    Module.finrank ℝ (LinearMap.range (asdEmbed m)) = m := by
  rw [LinearMap.finrank_range_of_inj (asdEmbed_injective m), finrank_euclideanSpace_fin]

/-- Exact additive dimension balance: `finrank (range sdEmbed m) + finrank (range asdEmbed m) =
finrank (EuclideanSpace ℝ (Fin (m + m)))`. -/
theorem finrank_sd_add_asd (m : ℕ) :
    Module.finrank ℝ (LinearMap.range (sdEmbed m)) +
      Module.finrank ℝ (LinearMap.range (asdEmbed m)) =
      Module.finrank ℝ (EuclideanSpace ℝ (Fin (m + m))) := by
  rw [finrank_range_sdEmbed, finrank_range_asdEmbed, finrank_euclideanSpace_fin]

/-- Concrete 4D Yang-Mills curvature Hodge involution on `EuclideanSpace ℝ (Fin 6)` (`6 = 3+3`). -/
abbrev hodge4D : EuclideanSpace ℝ (Fin 6) →ₗ[ℝ] EuclideanSpace ℝ (Fin 6) :=
  halfSwap 3

/-- Concrete 8D spinor four-form Hodge involution on `EuclideanSpace ℝ (Fin 70)` (`70 = 35+35`). -/
abbrev hodge8D : EuclideanSpace ℝ (Fin 70) →ₗ[ℝ] EuclideanSpace ℝ (Fin 70) :=
  halfSwap 35

/-- `hodge4D` is an unconditional symmetric involution on `EuclideanSpace ℝ (Fin 6)`. -/
theorem symmInvolution_hodge4D : SymmInvolution hodge4D :=
  symmInvolution_halfSwap 3

/-- `hodge8D` is an unconditional symmetric involution on `EuclideanSpace ℝ (Fin 70)`. -/
theorem symmInvolution_hodge8D : SymmInvolution hodge8D :=
  symmInvolution_halfSwap 35

/-- Unconditional 4D `Fin 6` Hodge split `3 + 3 = Nat.choose 4 2`. -/
theorem finrank_hodge4D_split :
    Module.finrank ℝ (LinearMap.range (sdEmbed 3)) = 3 ∧
      Module.finrank ℝ (LinearMap.range (asdEmbed 3)) = 3 ∧
      Module.finrank ℝ (LinearMap.range (sdEmbed 3)) +
        Module.finrank ℝ (LinearMap.range (asdEmbed 3)) = Nat.choose 4 2 := by
  rw [finrank_range_sdEmbed, finrank_range_asdEmbed, fourD_curvature_choose_split]
  exact ⟨rfl, rfl, rfl⟩

/-- Unconditional 8D `Fin 70` spinor four-form Hodge split `35 + 35 = Nat.choose 8 4`. -/
theorem finrank_hodge8D_split :
    Module.finrank ℝ (LinearMap.range (sdEmbed 35)) = 35 ∧
      Module.finrank ℝ (LinearMap.range (asdEmbed 35)) = 35 ∧
      Module.finrank ℝ (LinearMap.range (sdEmbed 35)) +
        Module.finrank ℝ (LinearMap.range (asdEmbed 35)) = Nat.choose 8 4 := by
  rw [finrank_range_sdEmbed, finrank_range_asdEmbed, eightD_spinor_fourform_choose_split]
  exact ⟨rfl, rfl, rfl⟩

/-- Unconditional 4D Bogomol'nyi splitting and bound on `EuclideanSpace ℝ (Fin 6)`. -/
theorem hodge4D_bogomolnyi (F : EuclideanSpace ℝ (Fin 6)) :
    ‖F‖ ^ 2 = ‖projPlus hodge4D F‖ ^ 2 + ‖projMinus hodge4D F‖ ^ 2 ∧
      |inner ℝ F (hodge4D F)| ≤ ‖F‖ ^ 2 :=
  ⟨norm_sq_eq_projPlus_add_projMinus symmInvolution_hodge4D F,
    abs_inner_invol_le_norm_sq symmInvolution_hodge4D F⟩

/-- Unconditional 8D Bogomol'nyi splitting and bound on `EuclideanSpace ℝ (Fin 70)`. -/
theorem hodge8D_bogomolnyi (ω : EuclideanSpace ℝ (Fin 70)) :
    ‖ω‖ ^ 2 = ‖projPlus hodge8D ω‖ ^ 2 + ‖projMinus hodge8D ω‖ ^ 2 ∧
      |inner ℝ ω (hodge8D ω)| ≤ ‖ω‖ ^ 2 :=
  ⟨norm_sq_eq_projPlus_add_projMinus symmInvolution_hodge8D ω,
    abs_inner_invol_le_norm_sq symmInvolution_hodge8D ω⟩

end ConcreteHodgeInvolution
