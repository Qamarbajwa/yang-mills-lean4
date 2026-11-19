/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.BigOperators.Group.Finset.Basic
public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Analysis.SpecificLimits.Basic
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.LatticeHaarGibbs
public import YangMillsBlueprint.MathlibStaging.PolydiskMajorant

/-!
# L-Uniform Block Polymer Tail Envelope and Haar Gibbs Lifting

Formalizes the finite-range / exponentially decaying polymer tail envelope needed when
hierarchical block actions split into a bounded interior part `S_int ∈ [0, B_int]` plus
boundary polymer tails `∑_{r ≥ 1} C * θ ^ r` (`0 ≤ θ < 1`). Proves volume-independent finite
prefix truncation bounds `≤ C * θ / (1 - θ)`, the combined oscillation interval bound
`osc_eff ≤ B_int + 2 * C * θ / (1 - θ)`, and lifts both into `LatticeHaarGibbs` density caps
and expectation floors on compact product Haar spaces `(E → G)`.

## Main results

* `BlockPolymerOscillation.polymerTailBound`: summed polymer envelope `C * θ / (1 - θ)`.
* `BlockPolymerOscillation.effectiveBlockOsc`: combined effective block oscillation.
* `BlockPolymerOscillation.finset_geom_tail_le_polymerTailBound`: prefix sum bound for any `N`.
* `BlockPolymerOscillation.block_action_mem_Icc_of_polymer_tail`: interval enclosure of `S`.
* `BlockPolymerOscillation.productHaar_polymer_density_cap`: Radon-Nikodym density cap.
* `BlockPolymerOscillation.productHaar_polymer_expectation_floor`: weighted expectation floor.
-/

@[expose] public section

namespace BlockPolymerOscillation

open MeasureTheory LatticeHaarGibbs

/-- Summed infinite boundary polymer tail bound `C * θ / (1 - θ)` for `θ < 1`. -/
noncomputable def polymerTailBound (C θ : ℝ) : ℝ :=
  C * θ / (1 - θ)

/-- Effective block oscillation width `B_int + 2 * C * θ / (1 - θ)`. -/
noncomputable def effectiveBlockOsc (B_int C θ : ℝ) : ℝ :=
  B_int + 2 * polymerTailBound C θ

/-- Non-negativity of `polymerTailBound C θ` under `0 ≤ C` and `0 ≤ θ < 1`. -/
theorem polymerTailBound_nonneg {C θ : ℝ} (hC : 0 ≤ C) (hθ0 : 0 ≤ θ) (hθ1 : θ < 1) :
    0 ≤ polymerTailBound C θ := by
  unfold polymerTailBound
  have h1θ : 0 < 1 - θ := sub_pos.mpr hθ1
  positivity

/-- Non-negativity of `effectiveBlockOsc B_int C θ`. -/
theorem effectiveBlockOsc_nonneg {B_int C θ : ℝ} (hB : 0 ≤ B_int) (hC : 0 ≤ C)
    (hθ0 : 0 ≤ θ) (hθ1 : θ < 1) :
    0 ≤ effectiveBlockOsc B_int C θ := by
  unfold effectiveBlockOsc
  have ht := polymerTailBound_nonneg hC hθ0 hθ1
  linarith

/-- Any finite range `N` boundary polymer sum `∑_{k < N} C * θ ^ (k + 1)` is uniformly
bounded independently of `N` by `polymerTailBound C θ = C * θ / (1 - θ)`. -/
theorem finset_geom_tail_le_polymerTailBound {C θ : ℝ}
    (hC : 0 ≤ C) (hθ0 : 0 ≤ θ) (hθ1 : θ < 1) (N : ℕ) :
    (∑ k ∈ Finset.range N, C * θ ^ (k + 1)) ≤ polymerTailBound C θ := by
  rw [← Finset.mul_sum]
  have hs : Summable (fun k : ℕ => θ ^ (k + 1)) :=
    PolydiskMajorant.summable_geometric_tail hθ0 hθ1
  have hnonneg : ∀ k : ℕ, 0 ≤ θ ^ (k + 1) := fun k => pow_nonneg hθ0 _
  have hle := hs.sum_le_tsum (Finset.range N) fun k _ => hnonneg k
  rw [PolydiskMajorant.tsum_geometric_tail_eq hθ0 hθ1] at hle
  unfold polymerTailBound
  have hmul := mul_le_mul_of_nonneg_left hle hC
  rwa [← mul_div_assoc] at hmul

/-- Decomposition `S x = S_int x + S_ext x` with `0 ≤ S_int x ≤ B_int` and
`|S_ext x| ≤ polymerTailBound C θ` encloses `S` inside an interval of width
`effectiveBlockOsc B_int C θ`. -/
theorem block_action_mem_Icc_of_polymer_tail {Ω : Type*} (S S_int S_ext : Ω → ℝ)
    (B_int C θ : ℝ) (hdecomp : ∀ x, S x = S_int x + S_ext x)
    (hintLo : ∀ x, 0 ≤ S_int x) (hintHi : ∀ x, S_int x ≤ B_int)
    (hext : ∀ x, |S_ext x| ≤ polymerTailBound C θ) :
    (∀ x, -polymerTailBound C θ ≤ S x) ∧
      (∀ x, S x ≤ B_int + polymerTailBound C θ) ∧
      (B_int + polymerTailBound C θ) - (-polymerTailBound C θ) =
        effectiveBlockOsc B_int C θ := by
  refine ⟨fun x => ?_, fun x => ?_, ?_⟩
  · rcases abs_le.mp (hext x) with ⟨hlo, _⟩
    have := hintLo x
    linarith [hdecomp x]
  · rcases abs_le.mp (hext x) with ⟨_, hhi⟩
    have := hintHi x
    linarith [hdecomp x]
  · unfold effectiveBlockOsc
    ring

/-- **UNCONDITIONAL (`L`-uniform density cap):** Given an interior action bound `B_int` and
polymer tail envelope `|S_ext| ≤ polymerTailBound C θ`, the product-Haar Boltzmann density is
bounded uniformly by `Real.exp (effectiveBlockOsc B_int C θ)`. -/
theorem productHaar_polymer_density_cap {E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (S S_int S_ext : (E → G) → ℝ)
    (B_int C θ : ℝ)
    (hint : Integrable (expWeight S) (productHaarProb E G))
    (hdecomp : ∀ U, S U = S_int U + S_ext U)
    (hintLo : ∀ U, 0 ≤ S_int U) (hintHi : ∀ U, S_int U ≤ B_int)
    (hext : ∀ U, |S_ext U| ≤ polymerTailBound C θ) (U : E → G) :
    expWeight S U / partitionIntegral (productHaarProb E G) S ≤
      Real.exp (effectiveBlockOsc B_int C θ) := by
  rcases block_action_mem_Icc_of_polymer_tail S S_int S_ext B_int C θ hdecomp hintLo hintHi
      hext with ⟨hmin, hmax, hosc⟩
  have hcap := productHaar_density_le_exp_osc hint hmin hmax U
  rwa [hosc] at hcap

/-- **UNCONDITIONAL (`L`-uniform expectation floor):** Lifting `effectiveBlockOsc` into
`LatticeHaarGibbs` yields the uniform Boltzmann expectation lower bound
`Real.exp (-effectiveBlockOsc B_int C θ) * ∫ f dμ_Haar ≤ weightedExpectation`. -/
theorem productHaar_polymer_expectation_floor {E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (S S_int S_ext f : (E → G) → ℝ)
    (B_int C θ : ℝ)
    (hint : Integrable (expWeight S) (productHaarProb E G))
    (hf : Integrable f (productHaarProb E G))
    (hfw : Integrable (fun U => f U * expWeight S U) (productHaarProb E G))
    (hf0 : ∀ U, 0 ≤ f U)
    (hdecomp : ∀ U, S U = S_int U + S_ext U)
    (hintLo : ∀ U, 0 ≤ S_int U) (hintHi : ∀ U, S_int U ≤ B_int)
    (hext : ∀ U, |S_ext U| ≤ polymerTailBound C θ) :
    Real.exp (-effectiveBlockOsc B_int C θ) * (∫ U, f U ∂(productHaarProb E G)) ≤
      weightedExpectation (productHaarProb E G) S f := by
  rcases block_action_mem_Icc_of_polymer_tail S S_int S_ext B_int C θ hdecomp hintLo hintHi
      hext with ⟨hmin, hmax, hosc⟩
  have hexp := productHaar_expectation_ge_exp_neg_osc hint hf hfw hf0 hmin hmax
  rwa [hosc] at hexp

end BlockPolymerOscillation
