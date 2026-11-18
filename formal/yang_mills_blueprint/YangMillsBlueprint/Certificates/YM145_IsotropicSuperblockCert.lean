/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.IsotropicSuperblockDobrushin
import YangMillsBlueprint.Certificates.YM138_SliceTensorGapCert
import Mathlib.Data.Rat.Init
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# YM-145: Isotropic Spatial-Temporal Super-Block Contraction Certificate (`Stage 2B`)

Instantiates `IsotropicSuperblockDobrushin` over `ℚ` matching the `L=12`, `β=2.5`, `b_s=4`
Phase A-2 scaling regime (`chiIn = 8`, `chiOut = 12` ⇒ `superblockM0 = 5 / 2 = 2.5`), proving:
- Unblocked `chiTotal = 20` collapses to bounded `M₀ = 5 / 2 ≤ 1 + 3 / 2` under isotropic
  spatial blocking.
- At `k = 3` coarse temporal blocks (`r = 1 / 2`), `coarseSliceCoupling (5 / 2) (1 / 2) 3 = 5 / 16`
  leaves strict Schur spectral-gap margin `η = 11 / 16 > 2 / 3 > 0`.
- Conditional uniform spectral gap theorem `superblock_uniform_gap_conditional`.
-/

namespace YangMillsBlueprint.Certificates

open CoarseSliceDecoherence IsotropicSuperblockDobrushin SliceMarkovTensorization

/-- Rational certificate bundling isotropic spatial-temporal super-block contraction data. -/
structure IsotropicSuperblockCert where
  chiIn : ℚ
  chiOut : ℚ
  α : ℚ
  r : ℚ
  η : ℚ
  k : ℕ
  hin : 0 < chiIn
  hout : 0 ≤ chiOut
  hleak : chiOut ≤ α * chiIn
  hr0 : 0 ≤ r
  hη : 0 < η
  hcap : (1 + α) * r ^ k ≤ 1 - η

/-- Canonical Phase A-2 calibrated certificate (`chiIn = 8, chiOut = 12, α = 3/2, r = 1/2, k = 3`). -/
def canonicalIsotropicSuperblockCert : IsotropicSuperblockCert where
  chiIn := 8
  chiOut := 12
  α := 3 / 2
  r := 1 / 2
  η := 11 / 16
  k := 3
  hin := by norm_num
  hout := by norm_num
  hleak := by norm_num
  hr0 := by norm_num
  hη := by norm_num
  hcap := by norm_num

instance : Nonempty IsotropicSuperblockCert :=
  ⟨canonicalIsotropicSuperblockCert⟩

/-- Exact canonical dimensionless susceptibility `superblockM0 8 12 = 5 / 2`. -/
theorem canonical_superblock_m0_eq :
    superblockM0 canonicalIsotropicSuperblockCert.chiIn
      canonicalIsotropicSuperblockCert.chiOut = 5 / 2 := by
  dsimp [canonicalIsotropicSuperblockCert, superblockM0]
  norm_num

/-- Exact `k = 3` coarse super-block coupling `5 / 16 ≤ 5 / 16 = 1 - 11 / 16`. -/
theorem canonical_superblock_coupling_eval :
    coarseSliceCoupling
      (superblockM0 canonicalIsotropicSuperblockCert.chiIn
        canonicalIsotropicSuperblockCert.chiOut)
      canonicalIsotropicSuperblockCert.r canonicalIsotropicSuperblockCert.k = 5 / 16 := by
  dsimp [canonicalIsotropicSuperblockCert, coarseSliceCoupling, superblockM0]
  norm_num

/-- Strict contraction margin `5 / 16 < 1 / 3` at `k = 3`. -/
theorem canonical_superblock_coupling_lt_third :
    coarseSliceCoupling
      (superblockM0 canonicalIsotropicSuperblockCert.chiIn
        canonicalIsotropicSuperblockCert.chiOut)
      canonicalIsotropicSuperblockCert.r canonicalIsotropicSuperblockCert.k < 1 / 3 := by
  rw [canonical_superblock_coupling_eval]
  norm_num

/-- **CONDITIONAL:** Once Stage 2B proves uniform spatial block leakage `chiOut ≤ α * chiIn`
and transfer decay `r^k` satisfying `(1 + α) * r^k ≤ 1 - η` independently of cutoff `a → 0`
and volume `L → ∞`, the resulting `ℓ²` slice quadratic contraction `(1 - ρ_E^2) ≥ η * (2 - η) > 0`
holds uniformly across arbitrary spatial block counts `n : ℕ`. -/
theorem superblock_uniform_gap_conditional (c : IsotropicSuperblockCert)
    (n : ℕ) (x : Fin n → ℚ) (ρ_E : ℚ)
    (hρ0 : 0 ≤ ρ_E)
    (hρ_eq : ρ_E = coarseSliceCoupling (superblockM0 c.chiIn c.chiOut) c.r c.k) :
    c.η * (2 - c.η) ≤ 1 - ρ_E ^ 2 ∧
      (c.η * (2 - c.η)) * (∑ i : Fin n, x i ^ 2) ≤
        (1 - ρ_E ^ 2) * (∑ i : Fin n, x i ^ 2) := by
  have hle : ρ_E ≤ 1 - c.η := by
    rw [hρ_eq]
    exact superblock_coupling_le_margin c.hin c.hleak c.hr0 c.hcap
  have h0_le : 0 ≤ 1 - c.η := le_trans hρ0 hle
  have hsq : ρ_E ^ 2 ≤ (1 - c.η) ^ 2 :=
    sq_le_sq' (by linarith [c.hη, h0_le]) hle
  have hgap : c.η * (2 - c.η) ≤ 1 - ρ_E ^ 2 := by nlinarith
  have hsum : 0 ≤ ∑ i : Fin n, x i ^ 2 :=
    Finset.sum_nonneg fun i _ => sq_nonneg (x i)
  exact ⟨hgap, mul_le_mul_of_nonneg_right hgap hsum⟩

end YangMillsBlueprint.Certificates
