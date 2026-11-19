/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.NonCriticalSlabContraction
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# YM-166: Stage 2B Non-Critical Slab Contraction Certificate

Certifies:
1. Unconditional exclusion of algebraic power-law decay from any fixed uniform contraction
   factor `r < 1` (`powerLaw_fails_uniform_contraction_unconditional`), paired with finite
   exponential slab contraction (`slabTailSum cert.α cert.r cert.k < 1`).
2. Conditional Stage-2B super-block contraction (`stage2b_noncritical_slab_dobrushin_conditional`)
   wiring `SliceReflectionHilbert.ContractiveTransfer T Ω cert.r` and bounded spatial leakage
   into `IsotropicSuperblockDobrushin` coupling contraction `< 1`.
-/

namespace YangMillsBlueprint.Certificates

open CoarseSliceDecoherence IsotropicSuperblockDobrushin NonCriticalSlabContraction
open SliceReflectionHilbert

/-- Certificate bundling exponential transfer ratio `0 < r < 1`, isotropic leakage ratio `α ≥ 0`,
and super-block thickness `k ≥ 1`. -/
structure NonCriticalSlabCert where
  r : ℝ
  α : ℝ
  k : ℕ
  hr0 : 0 < r
  hr1 : r < 1
  hα0 : 0 ≤ α
  hk1 : 1 ≤ k
  hgap : (2 + α) * r ^ k < 1

/-- Canonical witness (`r = 1/2`, `α = 1/2`, `k = 2` ⇒ `slabTailSum = 1/2 < 1`). -/
noncomputable def canonicalNonCriticalSlabCert : NonCriticalSlabCert where
  r := 1 / 2
  α := 1 / 2
  k := 2
  hr0 := by norm_num
  hr1 := by norm_num
  hα0 := by norm_num
  hk1 := by norm_num
  hgap := by norm_num

instance : Nonempty NonCriticalSlabCert :=
  ⟨canonicalNonCriticalSlabCert⟩

/-- **UNCONDITIONAL:** Every algebraic power-law critical correlator violates `cert.r < 1` at
sufficiently large separation `T`, whereas every exponential transfer contraction `0 < r < 1`
strictly satisfies `slabTailSum cert.α cert.r cert.k < 1` at thickness `cert.k` and evaluates to
`1 / 2` on `canonicalNonCriticalSlabCert`. -/
theorem powerLaw_fails_uniform_contraction_unconditional (cert : NonCriticalSlabCert) :
    (∃ T : ℕ, ∀ t : ℕ, T ≤ t → cert.r < powerLawRatio cert.k t) ∧
      slabTailSum cert.α cert.r cert.k < 1 ∧
      slabTailSum canonicalNonCriticalSlabCert.α canonicalNonCriticalSlabCert.r
        canonicalNonCriticalSlabCert.k = 1 / 2 := by
  refine ⟨powerLaw_fails_uniform_contraction cert.k cert.hr1,
    slabTailSum_lt_one_of_gap cert.hα0 (le_of_lt cert.hr0) cert.hgap, ?_⟩
  dsimp [canonicalNonCriticalSlabCert, slabTailSum]
  norm_num

/-- **CONDITIONAL:** Once Stage-2B establishes exponential transfer contraction
`ContractiveTransfer T Ω cert.r` on `OSHilbert B` together with bounded spatial block leakage
`chiOut ≤ cert.α * chiIn` (`0 < chiIn`), coarse isotropic super-block susceptibility stays
strictly contractive (`< 1`) while `id - T` preserves orthogonal coercivity gap `1 - cert.r`. -/
theorem stage2b_noncritical_slab_dobrushin_conditional {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : ReflectionPositiveForm V) (T : OSHilbert B →ₗ[ℝ] OSHilbert B) (Ω : OSHilbert B)
    (cert : NonCriticalSlabCert) (hT : ContractiveTransfer T Ω cert.r)
    {chiIn chiOut : ℝ} (hin : 0 < chiIn) (hleak : chiOut ≤ cert.α * chiIn) :
    SpectralMassGapBridge.HasOrthogonalCoercivity (LinearMap.id - T) Ω (1 - cert.r) ∧
      coarseSliceCoupling (superblockM0 chiIn chiOut) cert.r cert.k < 1 ∧
      slabTailSum cert.α cert.r cert.k < 1 := by
  have hcoerc := transfer_to_coercivity hT
  have hrk0 : 0 ≤ cert.r ^ cert.k := pow_nonneg (le_of_lt cert.hr0) cert.k
  have hle1 : (1 + cert.α) * cert.r ^ cert.k ≤ 1 - cert.r ^ cert.k := by
    linarith [cert.hgap]
  have hsuper := superblock_coupling_le_margin hin hleak (le_of_lt cert.hr0) hle1
  have hlt1 : coarseSliceCoupling (superblockM0 chiIn chiOut) cert.r cert.k < 1 := by
    have hpowlt : cert.r ^ cert.k < 1 := by
      have : (2 + cert.α) * cert.r ^ cert.k < 1 := cert.hgap
      nlinarith [cert.hα0]
    have : 0 < cert.r ^ cert.k := pow_pos cert.hr0 cert.k
    linarith
  exact ⟨hcoerc, hlt1, slabTailSum_lt_one_of_gap cert.hα0 (le_of_lt cert.hr0) cert.hgap⟩

end YangMillsBlueprint.Certificates
