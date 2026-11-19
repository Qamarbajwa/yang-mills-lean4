/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.WilsonPlaquetteAction
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

/-!
# YM-152: Four-Dimensional Single-Link Wilson Action Unconditional Gibbs Certificate

Specializes `WilsonPlaquetteAction` to `d = 4` (`m = 2 * (4 - 1) = 6` staples per link),
proving:
- `wilson_4d_single_link_unconditional`: strictly unconditional density cap `≤ Real.exp (12 * β)`
  and Gibbs expectation lower bound `≥ Real.exp (-(12 * β)) * ∫ f dμ_Haar` on any compact group
  `G` with orthogonal matrix representation, independently of lattice box size `L`.
- `wilson_crossover_continuum_gap_conditional`: isolates the open RG continuum requirement that
  renormalized crossover couplings remain uniformly bounded (`β_eff ≤ βMax`) as bare `a → 0`.
-/

namespace YangMillsBlueprint.Certificates

open WilsonPlaquetteAction LatticeHaarGibbs MeasureTheory Matrix

/-- Real certificate bundling bare/effective coupling upper bound `βMax` and Haar floor. -/
structure WilsonSingleLinkCert where
  β : ℝ
  βMax : ℝ
  haarFloor : ℝ
  hβ0 : 0 ≤ β
  hβle : β ≤ βMax
  hfloor : 0 < haarFloor

/-- Canonical witness at unit-oscillation crossover threshold `12 * β = 1`, `haarFloor = 4`. -/
noncomputable def canonicalWilsonSingleLinkCert : WilsonSingleLinkCert where
  β := 1 / 12
  βMax := 1 / 12
  haarFloor := 4
  hβ0 := by norm_num
  hβle := by norm_num
  hfloor := by norm_num

instance : Nonempty WilsonSingleLinkCert :=
  ⟨canonicalWilsonSingleLinkCert⟩

/-- Exact 4D 6-staple oscillation constant `2 * 6 * β = 12 * β`. -/
theorem canonical_4d_staple_osc_eq (β : ℝ) :
    2 * ((6 : ℕ) : ℝ) * β = 12 * β := by
  norm_num

/-- **UNCONDITIONAL:** On any compact topological group `G` equipped with an orthogonal
representation `rep : G → Matrix (Fin n) (Fin n) ℝ` (`n > 0`) and any `6` surrounding 4D
plaquette staples at coupling `β ≥ 0`, the single-link Boltzmann Radon-Nikodym density is
uniformly bounded by `exp (12 * β)` and any non-negative observable obeys the lower bound
`exp (-(12 * β)) * ∫ f dμ_Haar ≤ weightedExpectation` independently of lattice volume `L`. -/
theorem wilson_4d_single_link_unconditional
    {G : Type*} [Group G] [TopologicalSpace G] [CompactSpace G]
    [IsTopologicalGroup G] [MeasurableSpace G] [BorelSpace G]
    {n : ℕ} (hn : 0 < n) {β : ℝ} (hβ : 0 ≤ β)
    (rep : G → Matrix (Fin n) (Fin n) ℝ) (hrep : ∀ g : G, rep g * (rep g)ᵀ = 1)
    (staples : Fin 6 → Matrix (Fin n) (Fin n) ℝ)
    (hS : ∀ j : Fin 6, staples j * (staples j)ᵀ = 1)
    (f : G → ℝ)
    (hint : Integrable
      (expWeight (fun x => stapleAction β staples (rep x))) (compactHaarProb G))
    (hf : Integrable f (compactHaarProb G))
    (hfw : Integrable
      (fun x => f x * expWeight (fun y => stapleAction β staples (rep y)) x)
      (compactHaarProb G))
    (hf0 : ∀ x : G, 0 ≤ f x) :
    (∀ g : G,
      expWeight (fun x => stapleAction β staples (rep x)) g /
        partitionIntegral (compactHaarProb G) (fun x => stapleAction β staples (rep x)) ≤
        Real.exp (12 * β)) ∧
      Real.exp (-(12 * β)) * (∫ x, f x ∂(compactHaarProb G)) ≤
        weightedExpectation (compactHaarProb G) (fun x => stapleAction β staples (rep x)) f := by
  have hcap := fun g =>
    singleLink_conditional_density_cap hn hβ rep hrep staples hS hint g
  have hfloor :=
    singleLink_conditional_variance_floor hn hβ rep hrep staples hS f hint hf hfw hf0
  rw [canonical_4d_staple_osc_eq β] at hcap hfloor
  exact ⟨hcap, hfloor⟩

/-- **CONDITIONAL:** Once Stage 1 / Stage 2A RG blocking establishes a uniform crossover effective
coupling bound `β ≤ cert.βMax` and a strictly positive Haar variance floor `cert.haarFloor ≤ ∫ f`,
the weighted 4D single-link variance stays strictly above `exp (-(12 * βMax)) * haarFloor`. -/
theorem wilson_crossover_continuum_gap_conditional
    {G : Type*} [Group G] [TopologicalSpace G] [CompactSpace G]
    [IsTopologicalGroup G] [MeasurableSpace G] [BorelSpace G]
    {n : ℕ} (hn : 0 < n) (cert : WilsonSingleLinkCert)
    (rep : G → Matrix (Fin n) (Fin n) ℝ) (hrep : ∀ g : G, rep g * (rep g)ᵀ = 1)
    (staples : Fin 6 → Matrix (Fin n) (Fin n) ℝ)
    (hS : ∀ j : Fin 6, staples j * (staples j)ᵀ = 1)
    (f : G → ℝ)
    (hint : Integrable
      (expWeight (fun x => stapleAction cert.β staples (rep x))) (compactHaarProb G))
    (hf : Integrable f (compactHaarProb G))
    (hfw : Integrable
      (fun x => f x * expWeight (fun y => stapleAction cert.β staples (rep y)) x)
      (compactHaarProb G))
    (hf0 : ∀ x : G, 0 ≤ f x)
    (hhaar : cert.haarFloor ≤ ∫ x, f x ∂(compactHaarProb G)) :
    0 < Real.exp (-(12 * cert.βMax)) * cert.haarFloor ∧
      Real.exp (-(12 * cert.βMax)) * cert.haarFloor ≤
        weightedExpectation (compactHaarProb G)
          (fun x => stapleAction cert.β staples (rep x)) f := by
  have hpos : 0 < Real.exp (-(12 * cert.βMax)) * cert.haarFloor :=
    mul_pos (Real.exp_pos _) cert.hfloor
  have hexpLe : Real.exp (-(12 * cert.βMax)) ≤ Real.exp (-(12 * cert.β)) := by
    apply Real.exp_le_exp.mpr
    linarith [cert.hβle]
  have hmul1 :
      Real.exp (-(12 * cert.βMax)) * cert.haarFloor ≤
        Real.exp (-(12 * cert.β)) * cert.haarFloor :=
    mul_le_mul_of_nonneg_right hexpLe (le_of_lt cert.hfloor)
  have hmul2 :
      Real.exp (-(12 * cert.β)) * cert.haarFloor ≤
        Real.exp (-(12 * cert.β)) * (∫ x, f x ∂(compactHaarProb G)) :=
    mul_le_mul_of_nonneg_left hhaar (le_of_lt (Real.exp_pos _))
  have hraw :=
    (wilson_4d_single_link_unconditional hn cert.hβ0 rep hrep staples hS f hint hf hfw hf0).2
  exact ⟨hpos, le_trans hmul1 (le_trans hmul2 hraw)⟩

end YangMillsBlueprint.Certificates
