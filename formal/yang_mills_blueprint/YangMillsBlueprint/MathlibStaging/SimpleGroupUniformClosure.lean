/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.Order.Field.Basic
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.BlockSchurHierarchy
public import YangMillsBlueprint.MathlibStaging.CenterlessWeylAlcoveGap
public import YangMillsBlueprint.MathlibStaging.CoarseSliceDecoherence
public import YangMillsBlueprint.MathlibStaging.IsotropicSuperblockDobrushin

/-!
# Uniform Transverse-Codimension and Block-Hierarchy Closure

Unifies coercive lower bounds parameterized strictly by the transverse codimension
`transverseCodim dimG rankG = dimG - rankG >= 2` and bounded density cap `M > 0`, together
with isotropic block susceptibility contraction and recursive Schur chain dominance, without
depending on finite cyclic center structure.

## Main results

* `SimpleGroupUniformClosure.transverseCodim_ge_two`: codimension lower bound `2 <= dimG - rankG`.
* `SimpleGroupUniformClosure.codimNormalizedFloor_ge_base`: uniform floor `4 / M <= floor`.
* `SimpleGroupUniformClosure.codimNormalizedFloor_pos`: strict positivity `0 < floor`.
* `SimpleGroupUniformClosure.uniform_superblock_ratio_lt_one`: super-block contraction `< 1`.
* `SimpleGroupUniformClosure.uniform_block_schur_gap_pos`: combined gap & Schur ratio invariants.
-/

@[expose] public section

namespace SimpleGroupUniformClosure

section NatCodim

/-- Transverse root-space codimension `dimG - rankG`. -/
def transverseCodim (dimG rankG : ℕ) : ℕ :=
  dimG - rankG

/-- Whenever `rankG + 2 <= dimG`, the transverse codimension is at least `2`. -/
theorem transverseCodim_ge_two {dimG rankG : ℕ} (h : rankG + 2 ≤ dimG) :
    2 ≤ transverseCodim dimG rankG := by
  unfold transverseCodim
  omega

end NatCodim

section OrderedClosure

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Codimension-scaled inverse-density floor `2 * codim / densityCap`. -/
def codimNormalizedFloor (codim : ℕ) (densityCap : F) : F :=
  (2 * (codim : F)) / densityCap

/-- For any `codim >= 2` and positive density cap `M > 0`, the floor dominates `4 / M`. -/
theorem codimNormalizedFloor_ge_base {codim : ℕ} {M : F}
    (hc : 2 ≤ codim) (hM : 0 < M) :
    4 / M ≤ codimNormalizedFloor codim M := by
  unfold codimNormalizedFloor
  have hcast : (2 : F) ≤ (codim : F) := by
    simpa using (Nat.cast_le (α := F)).mpr hc
  have hnum : (4 : F) ≤ 2 * (codim : F) := by linarith
  rw [div_eq_mul_inv, div_eq_mul_inv]
  exact mul_le_mul_of_nonneg_right hnum (inv_nonneg.mpr (le_of_lt hM))

/-- Strict positivity of `codimNormalizedFloor` for `codim >= 2` and `0 < M`. -/
theorem codimNormalizedFloor_pos {codim : ℕ} {M : F}
    (hc : 2 ≤ codim) (hM : 0 < M) :
    0 < codimNormalizedFloor codim M := by
  have h4 : (0 : F) < 4 := by positivity
  exact lt_of_lt_of_le (div_pos h4 hM) (codimNormalizedFloor_ge_base hc hM)

/-- Dimensionless coarse slice coupling strictly below `1` under bounded block leakage. -/
theorem uniform_superblock_ratio_lt_one {chiIn chiOut α r η : F} {k : ℕ}
    (hin : 0 < chiIn) (hleak : chiOut ≤ α * chiIn)
    (hr0 : 0 ≤ r) (hη0 : 0 < η)
    (hdecay : (1 + α) * r ^ k ≤ 1 - η) :
    CoarseSliceDecoherence.coarseSliceCoupling
      (IsotropicSuperblockDobrushin.superblockM0 chiIn chiOut) r k < 1 := by
  have hle :=
    IsotropicSuperblockDobrushin.superblock_coupling_le_margin hin hleak hr0 hdecay
  linarith

/-- Combined positivity of the Cartan-plus-codimension floor, Schur diagonal-dominance margin,
and iterated Schur coupling ratio bound strictly below `1`. -/
theorem uniform_block_schur_gap_pos {codim : ℕ} {M qCartan d c ρ0 : F}
    (hc : 2 ≤ codim) (hM : 0 < M) (hq : 0 ≤ qCartan)
    (hd : 0 < d) (hc0 : 0 ≤ c) (hgap : 2 * c < d) (hρ : ρ0 = 2 * c / d) (k : ℕ) :
    0 < qCartan + codimNormalizedFloor codim M ∧
      0 < BlockSchurHierarchy.blockDiagNext d c -
        2 * BlockSchurHierarchy.blockCouplingNext d c ∧
      BlockSchurHierarchy.iteratedBlockRatio ρ0 k < 1 := by
  have hfloor : 0 < codimNormalizedFloor codim M := codimNormalizedFloor_pos hc hM
  have hgapPos : 0 < qCartan + codimNormalizedFloor codim M :=
    CenterlessWeylAlcoveGap.weylAlcoveCoerciveGap_pos hq hfloor le_rfl
  have hmargin : 0 < d - 2 * c := sub_pos.mpr hgap
  have hmono := BlockSchurHierarchy.blockChain_margin_monotone hd hc0 (le_of_lt hgap)
  have hρ0_nonneg : 0 ≤ ρ0 := by
    rw [hρ]
    exact div_nonneg (by linarith) (le_of_lt hd)
  have hρ0_lt1 : ρ0 < 1 := by
    rw [hρ, div_lt_one hd]
    exact hgap
  have hratio := (BlockSchurHierarchy.iteratedBlockRatio_mem_Ico hρ0_nonneg hρ0_lt1 k).2
  exact ⟨hgapPos, lt_of_lt_of_le hmargin hmono, hratio⟩

end OrderedClosure

end SimpleGroupUniformClosure
