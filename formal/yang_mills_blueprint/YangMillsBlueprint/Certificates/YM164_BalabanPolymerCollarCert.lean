/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.BalabanPolymerCollar
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

/-!
# YM-164: Stage 1 Balaban Polymer Collar & Faddeev-Popov Certificate

Certifies:
1. Unconditional Kotecky-Preiss cluster-expansion geometric convergence `∑ q^(n+1) ≤ a`,
   monotone exponential collar suppression `kpCollarTail q d`, small-field Faddeev-Popov matrix
   injectivity `Function.Injective (1 - E).mulVec`, and log-determinant bound `fpLogDetCap`.
2. Conditional Stage-1 compact product Haar lifting combining bounded interior action `B_int`,
   Faddeev-Popov Jacobian fluctuation `2 * fpLogDetCap`, and boundary tail `C * θ / (1 - θ)`.
-/

namespace YangMillsBlueprint.Certificates

open BalabanPolymerCollar BlockPolymerOscillation LatticeHaarGibbs MeasureTheory

/-- Stage-1 Balaban small-field Jacobian and Kotecky-Preiss polymer collar certificate. -/
structure BalabanCollarCert where
  ε : ℝ
  q : ℝ
  a : ℝ
  B_int : ℝ
  C : ℝ
  θ : ℝ
  m : ℕ
  haarFloor : ℝ
  hε0 : 0 ≤ ε
  hε1 : ε < 1
  hq0 : 0 ≤ q
  hq1 : q < 1
  hkp : q / (1 - q) ≤ a
  hB0 : 0 ≤ B_int
  hC0 : 0 ≤ C
  hθ0 : 0 ≤ θ
  hθ1 : θ < 1
  hfloor : 0 < haarFloor

/-- Canonical Stage-1 witness (`ε = 1/4`, `q = 1/5`, `a = 1/4`, `θ = 1/3`, `B_int = 1`). -/
noncomputable def canonicalBalabanCollarCert : BalabanCollarCert where
  ε := 1 / 4
  q := 1 / 5
  a := 1 / 4
  B_int := 1
  C := 1
  θ := 1 / 3
  m := 1
  haarFloor := 1
  hε0 := by norm_num
  hε1 := by norm_num
  hq0 := by norm_num
  hq1 := by norm_num
  hkp := by norm_num
  hB0 := by norm_num
  hC0 := by norm_num
  hθ0 := by norm_num
  hθ1 := by norm_num
  hfloor := by norm_num

instance : Nonempty BalabanCollarCert :=
  ⟨canonicalBalabanCollarCert⟩

/-- **UNCONDITIONAL:** For any `cert : BalabanCollarCert`, small-field Faddeev-Popov perturbation
`E` with row `ℓ^1` norm `≤ cert.ε < 1`, eigenvalues `ev i ∈ [1 - cert.ε, 1 + cert.ε]`, and
Kotecky-Preiss collar distances `d₁ ≤ d₂`, `(1 - E).mulVec` is injective, the Faddeev-Popov
log-determinant is capped by `fpLogDetCap cert.m cert.ε`, and Kotecky-Preiss sums obey `≤ a`. -/
theorem balaban_fp_jacobian_and_kp_unconditional (cert : BalabanCollarCert)
    (E : Matrix (Fin cert.m) (Fin cert.m) ℝ)
    (hE : ∀ i : Fin cert.m, (∑ j : Fin cert.m, |E i j|) ≤ cert.ε)
    (ev : Fin cert.m → ℝ) (hev : ∀ i : Fin cert.m, 1 - cert.ε ≤ ev i ∧ ev i ≤ 1 + cert.ε)
    (N : ℕ) {d₁ d₂ : ℕ} (hd : d₁ ≤ d₂) :
    Function.Injective (1 - E).mulVec ∧
      |Real.log (∏ i : Fin cert.m, ev i)| ≤ fpLogDetCap cert.m cert.ε ∧
      (∑ n ∈ Finset.range N, cert.q ^ (n + 1)) ≤ cert.a ∧
      kpCollarTail cert.q d₂ ≤ kpCollarTail cert.q d₁ := by
  exact ⟨(fp_matrix_injective E cert.hε1 hE).2,
    fp_abs_log_prod_le ev cert.hε0 cert.hε1 hev,
    kp_geometric_sum_le cert.hq0 cert.hq1 cert.hkp N,
    kpCollarTail_anti cert.hq0 (le_of_lt cert.hq1) hd⟩

/-- **CONDITIONAL:** Once Stage-1 Bałaban blocking produces an interior action split
`S = (S_int + J_fp) + S_ext` with `|J_fp U| ≤ fpLogDetCap cert.m cert.ε` and collar tail
`|S_ext U| ≤ polymerTailBound cert.C cert.θ`, every compact product Haar box `(E → G)` obeys the
uniform density cap `exp (balabanEffectiveOsc ...)` and expectation floor
`exp (-balabanEffectiveOsc ...) * cert.haarFloor`. -/
theorem balaban_stage1_collar_gibbs_conditional {E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (cert : BalabanCollarCert)
    (S S_int J_fp S_ext f : (E → G) → ℝ)
    (hint : Integrable (expWeight S) (productHaarProb E G))
    (hf : Integrable f (productHaarProb E G))
    (hfw : Integrable (fun U => f U * expWeight S U) (productHaarProb E G))
    (hf0 : ∀ U, 0 ≤ f U)
    (hdecomp : ∀ U, S U = (S_int U + fpLogDetCap cert.m cert.ε + J_fp U) + S_ext U)
    (hintLo : ∀ U, 0 ≤ S_int U) (hintHi : ∀ U, S_int U ≤ cert.B_int)
    (hfp : ∀ U, |J_fp U| ≤ fpLogDetCap cert.m cert.ε)
    (hext : ∀ U, |S_ext U| ≤ polymerTailBound cert.C cert.θ)
    (hhaar : cert.haarFloor ≤ ∫ U, f U ∂(productHaarProb E G)) :
    0 < Real.exp (-balabanEffectiveOsc cert.B_int cert.m cert.ε cert.C cert.θ) *
        cert.haarFloor ∧
      Real.exp (-balabanEffectiveOsc cert.B_int cert.m cert.ε cert.C cert.θ) *
        cert.haarFloor ≤ weightedExpectation (productHaarProb E G) S f ∧
      ∀ U, expWeight S U / partitionIntegral (productHaarProb E G) S ≤
        Real.exp (balabanEffectiveOsc cert.B_int cert.m cert.ε cert.C cert.θ) := by
  let S_inner : (E → G) → ℝ := fun U => S_int U + fpLogDetCap cert.m cert.ε + J_fp U
  have hinnerLo : ∀ U, 0 ≤ S_inner U := by
    intro U
    rcases abs_le.mp (hfp U) with ⟨hlo, _⟩
    dsimp [S_inner]
    linarith [hintLo U]
  have hinnerHi : ∀ U, S_inner U ≤ cert.B_int + 2 * fpLogDetCap cert.m cert.ε := by
    intro U
    rcases abs_le.mp (hfp U) with ⟨_, hhi⟩
    dsimp [S_inner]
    linarith [hintHi U]
  have hoscEq :
      effectiveBlockOsc (cert.B_int + 2 * fpLogDetCap cert.m cert.ε) cert.C cert.θ =
        balabanEffectiveOsc cert.B_int cert.m cert.ε cert.C cert.θ := by
    unfold effectiveBlockOsc balabanEffectiveOsc
    ring
  have hcap := productHaar_polymer_density_cap S S_inner S_ext
    (cert.B_int + 2 * fpLogDetCap cert.m cert.ε) cert.C cert.θ
    hint hdecomp hinnerLo hinnerHi hext
  have hexp := productHaar_polymer_expectation_floor S S_inner S_ext f
    (cert.B_int + 2 * fpLogDetCap cert.m cert.ε) cert.C cert.θ
    hint hf hfw hf0 hdecomp hinnerLo hinnerHi hext
  rw [hoscEq] at hcap hexp
  have hpos :
      0 < Real.exp (-balabanEffectiveOsc cert.B_int cert.m cert.ε cert.C cert.θ) *
        cert.haarFloor :=
    mul_pos (Real.exp_pos _) cert.hfloor
  have hmul :
      Real.exp (-balabanEffectiveOsc cert.B_int cert.m cert.ε cert.C cert.θ) * cert.haarFloor ≤
        Real.exp (-balabanEffectiveOsc cert.B_int cert.m cert.ε cert.C cert.θ) *
          (∫ U, f U ∂(productHaarProb E G)) :=
    mul_le_mul_of_nonneg_left hhaar (le_of_lt (Real.exp_pos _))
  exact ⟨hpos, le_trans hmul hexp, fun U => hcap U⟩

end YangMillsBlueprint.Certificates
