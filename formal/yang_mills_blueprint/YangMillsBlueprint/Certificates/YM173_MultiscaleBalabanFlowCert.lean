/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.MultiscaleBalabanFlow
import Mathlib.Tactic.NormNum

/-!
# YM-173: Multiscale `K`-Uniform Bałaban UV Flow Certificate

Certifies:
1. Unconditional dichotomy along any decreasing inverse-coupling RG trajectory `β 0, ..., β K`:
   subtracted `O(1 / β_k²)` irrelevant errors and cumulative large-field polymer weights remain
   uniformly bounded independently of `K`, while unsubtracted `O(1 / β_k)` marginal terms grow
   logarithmically without bound (`harmonic_marginal_sum_unbounded`).
2. Conditional Stage-1 compact product Haar Gibbs lifting combining `K`-uniform irrelevant +
   large-field accumulations with `L`-uniform Kotecký-Preiss collar decoupling (`YM172`).
-/

namespace YangMillsBlueprint.Certificates

open AbstractPolymerCluster BlockPolymerOscillation LatticeHaarGibbs MeasureTheory
open MultiscaleBalabanFlow

/-- Certificate bundling Stage-1 UV flow parameters across arbitrary step count `K`. -/
structure MultiscaleBalabanCert where
  B_core : ℝ
  C_irr : ℝ
  C_lf : ℝ
  βstar : ℝ
  δ_b : ℝ
  κ : ℝ
  collarCap : ℝ
  haarFloor : ℝ
  hB0 : 0 ≤ B_core
  hCirr : 0 ≤ C_irr
  hClf : 0 ≤ C_lf
  hβ0 : 0 < βstar
  hδ0 : 0 < δ_b
  hκ : 0 < κ
  hcol : 0 ≤ collarCap
  hfloor : 0 < haarFloor

/-- Canonical Stage-1 witness (`βstar = 2`, `δ_b = 1 / 2`, `κ = 1`, `collarCap = 1 / 2`). -/
noncomputable def canonicalMultiscaleBalabanCert : MultiscaleBalabanCert where
  B_core := 1
  C_irr := 1
  C_lf := 1
  βstar := 2
  δ_b := 1 / 2
  κ := 1
  collarCap := 1 / 2
  haarFloor := 1
  hB0 := by norm_num
  hCirr := by norm_num
  hClf := by norm_num
  hβ0 := by norm_num
  hδ0 := by norm_num
  hκ := by norm_num
  hcol := by norm_num
  hfloor := by norm_num

instance : Nonempty MultiscaleBalabanCert :=
  ⟨canonicalMultiscaleBalabanCert⟩

/-- **UNCONDITIONAL:** For any multiscale UV flow `β : ℕ → ℝ` ending at `β K ≥ cert.βstar` with
step drops `≥ cert.δ_b`, cumulative `O(1 / β_k²)` irrelevant sums and `exp (-κ * β_k)` large-field
sums stay uniformly bounded for ALL `K`, whereas unsubtracted `O(1 / β_k)` harmonic sums grow
logarithmically above every finite bound `M`. -/
theorem multiscale_balaban_summability_vs_harmonic_unconditional (cert : MultiscaleBalabanCert)
    (β : ℕ → ℝ) (K : ℕ) (hK : cert.βstar ≤ β K)
    (hstep : ∀ k : ℕ, k < K → cert.δ_b ≤ β k - β (k + 1)) (M : ℝ) :
    (∑ k ∈ Finset.range K, cert.C_irr / (β k) ^ 2) ≤ cert.C_irr / (cert.δ_b * cert.βstar) ∧
      (∑ k ∈ Finset.range K, cert.C_lf * Real.exp (-(cert.κ * β k))) ≤
        cert.C_lf * Real.exp (-(cert.κ * cert.βstar)) *
          polymerTailBound 1 (Real.exp (-(cert.κ * cert.δ_b))) ∧
      ∃ K_div : ℕ, M < ∑ m ∈ Finset.range K_div,
        1 / (cert.βstar + cert.δ_b * ((m + 1 : ℕ) : ℝ)) :=
  ⟨multiscale_irrelevant_sum_le β K cert.hβ0 cert.hδ0 cert.hCirr hK hstep,
    multiscale_large_field_sum_le β K cert.hδ0 cert.hκ cert.hClf hK hstep,
    harmonic_marginal_sum_unbounded cert.hβ0 cert.hδ0 M⟩

/-- **CONDITIONAL:** Once Stage-1 analytic renormalization discharges counterterms up to scale
`K` (`S = S_core + S_irr + S_lf + S_collar`) along `β` with `|S_irr|` bounded by the subtracted
`O(1 / β_k²)` sum, `|S_lf|` bounded by the cumulative large-field weight sum, and `|S_collar|`
bounded by `YM172`'s `L`-uniform collar decoupling theorem, the effective blocked measure obeys a
`K`-uniform and `L`-uniform Boltzmann density cap and positive expectation floor. -/
theorem balaban_multiscale_stage1_bridge_conditional {E G P : Type*} [Fintype E]
    [DecidableEq P] [Group G] [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (cert : MultiscaleBalabanCert)
    (incomp : P → P → Prop) (hrefl : ∀ u, incomp u u)
    (hsym : ∀ u v, incomp u v → incomp v u) (U S₁ S₂ B : Finset P)
    (z a : P → ℝ) (ha : ∀ x ∈ U, 0 ≤ a x)
    (hrHalf : ∀ x ∈ U, |z x| * Real.exp (a x) ≤ 1 / 2)
    (hkp : ∀ x ∈ U, (∑ y ∈ nbhd incomp U x, |z y| * Real.exp (a y)) ≤ a x / 2)
    (h12 : Disjoint S₁ S₂) (h1B : Disjoint S₁ B) (h2B : Disjoint S₂ B)
    (hcompat : ∀ u ∈ S₁, ∀ v ∈ S₂, ¬ incomp u v) (hsub : S₁ ∪ S₂ ∪ B ⊆ U)
    (hcollarSum : (∑ y ∈ B, kpLogWeight z a y) ≤ cert.collarCap)
    (β : ℕ → ℝ) (K : ℕ) (hK : cert.βstar ≤ β K)
    (hstep : ∀ k : ℕ, k < K → cert.δ_b ≤ β k - β (k + 1))
    (S S_core S_irr S_lf S_collar f : (E → G) → ℝ)
    (hint : Integrable (expWeight S) (productHaarProb E G))
    (hf : Integrable f (productHaarProb E G))
    (hfw : Integrable (fun W => f W * expWeight S W) (productHaarProb E G))
    (hf0 : ∀ W, 0 ≤ f W)
    (hdecomp : ∀ W, S W = S_core W + S_irr W + S_lf W + S_collar W)
    (hcoreLo : ∀ W, 0 ≤ S_core W) (hcoreHi : ∀ W, S_core W ≤ cert.B_core)
    (hirr : ∀ W, |S_irr W| ≤ ∑ k ∈ Finset.range K, cert.C_irr / (β k) ^ 2)
    (hlf : ∀ W, |S_lf W| ≤ ∑ k ∈ Finset.range K, cert.C_lf * Real.exp (-(cert.κ * β k)))
    (hcol : ∀ W, |S_collar W| ≤
      |Real.log (polymerZ incomp z (S₁ ∪ S₂ ∪ B)) -
        (Real.log (polymerZ incomp z S₁) + Real.log (polymerZ incomp z S₂))|)
    (hhaar : cert.haarFloor ≤ ∫ W, f W ∂(productHaarProb E G)) :
    0 < Real.exp (-(multiscaleEffectiveOsc cert.B_core cert.C_irr cert.C_lf
        cert.βstar cert.δ_b cert.κ cert.collarCap)) * cert.haarFloor ∧
      Real.exp (-(multiscaleEffectiveOsc cert.B_core cert.C_irr cert.C_lf
          cert.βstar cert.δ_b cert.κ cert.collarCap)) * cert.haarFloor ≤
        weightedExpectation (productHaarProb E G) S f ∧
      ∀ W, expWeight S W / partitionIntegral (productHaarProb E G) S ≤
        Real.exp (multiscaleEffectiveOsc cert.B_core cert.C_irr cert.C_lf
          cert.βstar cert.δ_b cert.κ cert.collarCap) := by
  obtain ⟨hr, hdkp⟩ := kotecky_preiss_half_condition_implies_dkp incomp hrHalf hkp
  have hdec := polymerZ_collar_decoupling_le hrefl hsym ha hr hdkp h12 h1B h2B hcompat hsub
  have hirrSum := multiscale_irrelevant_sum_le β K cert.hβ0 cert.hδ0 cert.hCirr hK hstep
  have hlfSum := multiscale_large_field_sum_le β K cert.hδ0 cert.hκ cert.hClf hK hstep
  let irrCap := cert.C_irr / (cert.δ_b * cert.βstar)
  let lfCap := cert.C_lf * Real.exp (-(cert.κ * cert.βstar)) *
    polymerTailBound 1 (Real.exp (-(cert.κ * cert.δ_b)))
  have hmin : ∀ W, -(irrCap + lfCap + cert.collarCap) ≤ S W := by
    intro W
    have hi := (abs_le.mp (le_trans (hirr W) hirrSum)).1
    have hl := (abs_le.mp (le_trans (hlf W) hlfSum)).1
    have hc := (abs_le.mp (le_trans (hcol W) (le_trans hdec hcollarSum))).1
    linarith [hdecomp W, hcoreLo W]
  have hmax : ∀ W, S W ≤ cert.B_core + irrCap + lfCap + cert.collarCap := by
    intro W
    have hi := (abs_le.mp (le_trans (hirr W) hirrSum)).2
    have hl := (abs_le.mp (le_trans (hlf W) hlfSum)).2
    have hc := (abs_le.mp (le_trans (hcol W) (le_trans hdec hcollarSum))).2
    linarith [hdecomp W, hcoreHi W]
  have hoscEq :
      (cert.B_core + irrCap + lfCap + cert.collarCap) - (-(irrCap + lfCap + cert.collarCap)) =
        multiscaleEffectiveOsc cert.B_core cert.C_irr cert.C_lf
          cert.βstar cert.δ_b cert.κ cert.collarCap := by
    unfold multiscaleEffectiveOsc
    dsimp [irrCap, lfCap]
    ring
  have hpos :
      0 < Real.exp (-(multiscaleEffectiveOsc cert.B_core cert.C_irr cert.C_lf
          cert.βstar cert.δ_b cert.κ cert.collarCap)) * cert.haarFloor :=
    mul_pos (Real.exp_pos _) cert.hfloor
  have hexp := productHaar_expectation_ge_exp_neg_osc hint hf hfw hf0 hmin hmax
  have hcap := productHaar_density_le_exp_osc hint hmin hmax
  rw [hoscEq] at hexp hcap
  have hmul :
      Real.exp (-(multiscaleEffectiveOsc cert.B_core cert.C_irr cert.C_lf
          cert.βstar cert.δ_b cert.κ cert.collarCap)) * cert.haarFloor ≤
        Real.exp (-(multiscaleEffectiveOsc cert.B_core cert.C_irr cert.C_lf
            cert.βstar cert.δ_b cert.κ cert.collarCap)) *
          (∫ W, f W ∂(productHaarProb E G)) :=
    mul_le_mul_of_nonneg_left hhaar (le_of_lt (Real.exp_pos _))
  exact ⟨hpos, le_trans hmul hexp, hcap⟩

end YangMillsBlueprint.Certificates
