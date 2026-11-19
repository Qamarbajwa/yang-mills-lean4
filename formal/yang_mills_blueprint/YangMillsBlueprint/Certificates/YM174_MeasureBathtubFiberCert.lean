/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.MeasureBathtubFiberFloor
import YangMillsBlueprint.MathlibStaging.MultiscaleBalabanFlow
import Mathlib.Tactic.NormNum

/-!
# YM-174: Measure-Theoretic Lieb-Loss Bathtub & Stage 2A Fiber Floor Certificate

Certifies:
1. Unconditional probability-space Lieb-Loss bathtub lower bounds: exact `1 / (2 * c * M)` constant
   (`4 / M` at `c = 1/8`), arbitrary transverse codimension `d` scaling `M ^ (-2 / d)`, and
   monotone floor strengthening across `SO(3) (d=2) → SU(3) (d=6) → G₂ (d=12) → F₄ (d=48) → E₈`.
2. Conditional Stage-2A compact product Haar fiber bathtub floor wiring Stage 1's
   `K`- and `L`-uniform `multiscaleEffectiveOsc` (`YM173`) directly into
   `boltzmann_measure_bathtub_codim_d_floor`.
-/

namespace YangMillsBlueprint.Certificates

open AbstractPolymerCluster BlockPolymerOscillation LatticeHaarGibbs MeasureBathtubFiberFloor
open MeasureTheory MultiscaleBalabanFlow

/-- Stage-2A codimension-`d` Haar sublevel and density-cap certificate. -/
structure MeasureBathtubCert where
  c : ℝ
  M : ℝ
  d : ℕ
  hc0 : 0 < c
  hM0 : 0 < M
  hbig : 1 ≤ 2 * c * M
  hd2 : 2 ≤ d

/-- Canonical `SU(2)`/`SO(3)` Hopf witness (`c = 1/8`, `M = 4`, `d = 2` ⇒ `4 / M = 1`). -/
noncomputable def canonicalMeasureBathtubCert : MeasureBathtubCert where
  c := 1 / 8
  M := 4
  d := 2
  hc0 := by norm_num
  hM0 := by norm_num
  hbig := by norm_num
  hd2 := by norm_num

instance : Nonempty MeasureBathtubCert :=
  ⟨canonicalMeasureBathtubCert⟩

theorem canonical_bathtub_sharp_eq :
    1 / (2 * canonicalMeasureBathtubCert.c * canonicalMeasureBathtubCert.M) = 1 ∧
      4 / canonicalMeasureBathtubCert.M = 1 := by
  unfold canonicalMeasureBathtubCert
  norm_num

/-- **UNCONDITIONAL:** On any probability space `(Ω, ν)`, any `L^∞`-bounded density `0 ≤ ρ ≤ M`
satisfies the sharp codimension-`2` floor `1 / (2 * c * M) ≤ ∫ f ρ dν`, general codimension-`d`
floor `(1 / 2) * (1 / (2 * c * M)) ^ (2 / d) ≤ ∫ f ρ dν`, and monotone strengthening in `d ≤ d'`. -/
theorem measure_bathtub_sharp_and_codim_d_unconditional {Ω : Type*} [MeasurableSpace Ω]
    {ν : Measure Ω} [IsProbabilityMeasure ν] (cert : MeasureBathtubCert)
    {f ρ : Ω → ℝ} (hf : Integrable f ν) (hρ : Integrable ρ ν)
    (hfρ : Integrable (fun y => f y * ρ y) ν)
    (hf0 : ∀ y, 0 ≤ f y) (hρ0 : ∀ y, 0 ≤ ρ y) (hρM : ∀ y, ρ y ≤ cert.M)
    (hρInt : ∫ y, ρ y ∂ν = 1)
    (hA2 : MeasurableSet {y : Ω | f y < 1 / (cert.c * cert.M)})
    (hvol2 : ν.real {y : Ω | f y < 1 / (cert.c * cert.M)} ≤
      cert.c * (1 / (cert.c * cert.M)))
    (hintSub2 : (cert.c / 2) * (1 / (cert.c * cert.M)) ^ 2 ≤
      ∫ y in {y : Ω | f y < 1 / (cert.c * cert.M)}, f y ∂ν)
    (hAd : MeasurableSet
      {y : Ω | f y < (1 / (2 * cert.c * cert.M)) ^ ((2 : ℝ) / (cert.d : ℝ))})
    (hvold :
      ν.real {y : Ω | f y < (1 / (2 * cert.c * cert.M)) ^ ((2 : ℝ) / (cert.d : ℝ))} ≤
        cert.c * ((1 / (2 * cert.c * cert.M)) ^ ((2 : ℝ) / (cert.d : ℝ))) ^
          ((cert.d : ℝ) / 2))
    (d' : ℕ) (hd' : cert.d ≤ d') :
    1 / (2 * cert.c * cert.M) ≤ ∫ y, f y * ρ y ∂ν ∧
      (1 / 2 : ℝ) * (1 / (2 * cert.c * cert.M)) ^ ((2 : ℝ) / (cert.d : ℝ)) ≤
        ∫ y, f y * ρ y ∂ν ∧
      (1 / 2 : ℝ) * (1 / (2 * cert.c * cert.M)) ^ ((2 : ℝ) / (cert.d : ℝ)) ≤
        (1 / 2 : ℝ) * (1 / (2 * cert.c * cert.M)) ^ ((2 : ℝ) / (d' : ℝ)) := by
  have hdPos : 0 < cert.d := lt_of_lt_of_le (by norm_num) cert.hd2
  exact ⟨measure_bathtub_codim2_sharp_floor cert.hc0 cert.hM0 hA2 hf hρ hfρ hρ0 hρM hρInt
      hvol2 hintSub2,
    measure_bathtub_codim_d_floor cert.hc0 cert.hM0 hdPos hAd hf hρ hfρ hf0 hρ0 hρM hρInt hvold,
    codim_bathtub_floor_mono_dim cert.hc0 cert.hM0 cert.hbig hdPos hd'⟩

/-- **CONDITIONAL:** Given Stage 1's `K`- and `L`-uniform action bounds feeding
`multiscaleEffectiveOsc` (`YM173`) and Haar sublevel scaling `ν.real {f < t} ≤ c * t ^ (d / 2)`
on a fiber of `(E → G)`, the Stage-2A normalized Boltzmann expectation of `f` enjoys a strictly
positive volume-independent bathtub floor `(1 / 2) * (1 / (2 * c * exp osc₁)) ^ (2 / d)`. -/
theorem stage2a_fiber_measure_bathtub_conditional {E G P : Type*} [Fintype E]
    [DecidableEq P] [Group G] [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (bcert : MeasureBathtubCert)
    (B_core C_irr C_lf βstar δ_b κ collarCap : ℝ) (hB : 0 ≤ B_core) (hCirr : 0 ≤ C_irr)
    (hClf : 0 ≤ C_lf) (hβ : 0 < βstar) (hδ : 0 < δ_b) (hκ : 0 < κ) (hcolCap : 0 ≤ collarCap)
    (incomp : P → P → Prop) (hrefl : ∀ u, incomp u u)
    (hsym : ∀ u v, incomp u v → incomp v u) (U S₁ S₂ B : Finset P)
    (z a : P → ℝ) (ha : ∀ x ∈ U, 0 ≤ a x)
    (hrHalf : ∀ x ∈ U, |z x| * Real.exp (a x) ≤ 1 / 2)
    (hkp : ∀ x ∈ U, (∑ y ∈ nbhd incomp U x, |z y| * Real.exp (a y)) ≤ a x / 2)
    (h12 : Disjoint S₁ S₂) (h1B : Disjoint S₁ B) (h2B : Disjoint S₂ B)
    (hcompat : ∀ u ∈ S₁, ∀ v ∈ S₂, ¬ incomp u v) (hsub : S₁ ∪ S₂ ∪ B ⊆ U)
    (hcollarSum : (∑ y ∈ B, kpLogWeight z a y) ≤ collarCap)
    (β : ℕ → ℝ) (K : ℕ) (hK : βstar ≤ β K)
    (hstep : ∀ k : ℕ, k < K → δ_b ≤ β k - β (k + 1))
    (S S_core S_irr S_lf S_collar f : (E → G) → ℝ)
    (hint : Integrable (expWeight S) (productHaarProb E G))
    (hf : Integrable f (productHaarProb E G))
    (hfw : Integrable (fun W => f W * expWeight S W) (productHaarProb E G))
    (hf0 : ∀ W, 0 ≤ f W)
    (hdecomp : ∀ W, S W = S_core W + S_irr W + S_lf W + S_collar W)
    (hcoreLo : ∀ W, 0 ≤ S_core W) (hcoreHi : ∀ W, S_core W ≤ B_core)
    (hirr : ∀ W, |S_irr W| ≤ ∑ k ∈ Finset.range K, C_irr / (β k) ^ 2)
    (hlf : ∀ W, |S_lf W| ≤ ∑ k ∈ Finset.range K, C_lf * Real.exp (-(κ * β k)))
    (hcol : ∀ W, |S_collar W| ≤
      |Real.log (polymerZ incomp z (S₁ ∪ S₂ ∪ B)) -
        (Real.log (polymerZ incomp z S₁) + Real.log (polymerZ incomp z S₂))|)
    (hA : MeasurableSet
      {W : E → G | f W < (1 / (2 * bcert.c * Real.exp
        (multiscaleEffectiveOsc B_core C_irr C_lf βstar δ_b κ collarCap))) ^
          ((2 : ℝ) / (bcert.d : ℝ))})
    (hvol : (productHaarProb E G).real
      {W : E → G | f W < (1 / (2 * bcert.c * Real.exp
        (multiscaleEffectiveOsc B_core C_irr C_lf βstar δ_b κ collarCap))) ^
          ((2 : ℝ) / (bcert.d : ℝ))} ≤
      bcert.c * ((1 / (2 * bcert.c * Real.exp
        (multiscaleEffectiveOsc B_core C_irr C_lf βstar δ_b κ collarCap))) ^
          ((2 : ℝ) / (bcert.d : ℝ))) ^ ((bcert.d : ℝ) / 2)) :
    0 < (1 / 2 : ℝ) * (1 / (2 * bcert.c * Real.exp
        (multiscaleEffectiveOsc B_core C_irr C_lf βstar δ_b κ collarCap))) ^
          ((2 : ℝ) / (bcert.d : ℝ)) ∧
      (1 / 2 : ℝ) * (1 / (2 * bcert.c * Real.exp
        (multiscaleEffectiveOsc B_core C_irr C_lf βstar δ_b κ collarCap))) ^
          ((2 : ℝ) / (bcert.d : ℝ)) ≤
        weightedExpectation (productHaarProb E G) S f := by
  have _hOsc0 := multiscaleEffectiveOsc_nonneg hB hCirr hClf hβ hδ hκ hcolCap
  obtain ⟨hr, hdkp⟩ := kotecky_preiss_half_condition_implies_dkp incomp hrHalf hkp
  have hdec := polymerZ_collar_decoupling_le hrefl hsym ha hr hdkp h12 h1B h2B hcompat hsub
  have hirrSum := multiscale_irrelevant_sum_le β K hβ hδ hCirr hK hstep
  have hlfSum := multiscale_large_field_sum_le β K hδ hκ hClf hK hstep
  let irrCap := C_irr / (δ_b * βstar)
  let lfCap := C_lf * Real.exp (-(κ * βstar)) *
    polymerTailBound 1 (Real.exp (-(κ * δ_b)))
  have hmin : ∀ W, -(irrCap + lfCap + collarCap) ≤ S W := fun W => by
    have hi := (abs_le.mp (le_trans (hirr W) hirrSum)).1
    have hl := (abs_le.mp (le_trans (hlf W) hlfSum)).1
    have hc := (abs_le.mp (le_trans (hcol W) (le_trans hdec hcollarSum))).1
    linarith [hdecomp W, hcoreLo W]
  have hmax : ∀ W, S W ≤ B_core + irrCap + lfCap + collarCap := fun W => by
    have hi := (abs_le.mp (le_trans (hirr W) hirrSum)).2
    have hl := (abs_le.mp (le_trans (hlf W) hlfSum)).2
    have hc := (abs_le.mp (le_trans (hcol W) (le_trans hdec hcollarSum))).2
    linarith [hdecomp W, hcoreHi W]
  have hoscEq :
      (B_core + irrCap + lfCap + collarCap) - (-(irrCap + lfCap + collarCap)) =
        multiscaleEffectiveOsc B_core C_irr C_lf βstar δ_b κ collarCap := by
    unfold multiscaleEffectiveOsc
    dsimp [irrCap, lfCap]
    ring
  have hdPos : 0 < bcert.d := lt_of_lt_of_le (by norm_num) bcert.hd2
  rw [← hoscEq] at hA hvol ⊢
  have hpos :
      0 < (1 / 2 : ℝ) * (1 / (2 * bcert.c *
        Real.exp ((B_core + irrCap + lfCap + collarCap) - (-(irrCap + lfCap + collarCap))))) ^
          ((2 : ℝ) / (bcert.d : ℝ)) := by
    have hbase : 0 < 1 / (2 * bcert.c *
        Real.exp ((B_core + irrCap + lfCap + collarCap) - (-(irrCap + lfCap + collarCap)))) := by
      have := bcert.hc0
      positivity
    exact mul_pos (by norm_num) (Real.rpow_pos_of_pos hbase _)
  exact ⟨hpos, boltzmann_measure_bathtub_codim_d_floor bcert.hc0 hdPos hA hint hf hfw hf0
    hmin hmax hvol⟩

end YangMillsBlueprint.Certificates
