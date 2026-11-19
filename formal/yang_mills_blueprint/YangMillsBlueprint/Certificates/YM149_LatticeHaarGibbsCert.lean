/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.LatticeHaarGibbs
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

/-!
# YM-149: Finite-Box Compact Group Haar Product Gibbs Measure Certificate

Bridges algebraic bounded-oscillation estimates (`YM-144`) to genuine finite-box
`MeasureTheory.Measure` Haar product spaces `productHaarProb E G` over any compact
topological group `G` and finite edge index `E`, certifying:
- Normalization `0 < partitionIntegral (productHaarProb E G) S`.
- Pointwise Radon-Nikodym density cap `Real.exp (vMax - vMin)`.
- Weighted expectation lower bound from a Haar-expectation floor (`YM-143` / `YM-144`).
-/

namespace YangMillsBlueprint.Certificates

open LatticeHaarGibbs MeasureTheory

/-- Real certificate bundling action oscillation bounds and a Haar observable floor. -/
structure LatticeHaarGibbsCert where
  vMin : ℝ
  vMax : ℝ
  haarFloor : ℝ
  hosc : vMin ≤ vMax
  hfloor : 0 < haarFloor

/-- Canonical witness (`vMin = 0`, `vMax = log 2`, `haarFloor = 4` ⇒ weighted floor `2`). -/
noncomputable def canonicalLatticeHaarGibbsCert : LatticeHaarGibbsCert where
  vMin := 0
  vMax := Real.log 2
  haarFloor := 4
  hosc := Real.log_nonneg (by norm_num)
  hfloor := by norm_num

instance : Nonempty LatticeHaarGibbsCert :=
  ⟨canonicalLatticeHaarGibbsCert⟩

/-- Exact canonical density cap `Real.exp (log 2 - 0) = 2`. -/
theorem canonical_haar_osc_density_cap_eq :
    Real.exp (canonicalLatticeHaarGibbsCert.vMax - canonicalLatticeHaarGibbsCert.vMin) = 2 := by
  dsimp [canonicalLatticeHaarGibbsCert]
  rw [sub_zero, Real.exp_log (by norm_num)]

/-- Exact canonical weighted expectation lower bound `Real.exp (-(log 2 - 0)) * 4 = 2`. -/
theorem canonical_haar_exp_floor_eq :
    Real.exp (-(canonicalLatticeHaarGibbsCert.vMax - canonicalLatticeHaarGibbsCert.vMin)) *
      canonicalLatticeHaarGibbsCert.haarFloor = 2 := by
  dsimp [canonicalLatticeHaarGibbsCert]
  rw [sub_zero, Real.exp_neg, Real.exp_log (by norm_num)]
  norm_num

/-- **CONDITIONAL:** On any finite lattice index `E` and compact topological group `G`, an
integrable bounded-oscillation action `vMin <= S <= vMax` together with a Haar integral floor
`haarFloor <= ∫ f d(productHaarProb E G)` forces strictly positive Boltzmann expectation and
the bounded Radon-Nikodym density cap `Real.exp (vMax - vMin)`. -/
theorem lattice_haar_gibbs_variance_floor_conditional
    {E G : Type*} [Fintype E] [Group G] [TopologicalSpace G] [CompactSpace G]
    [IsTopologicalGroup G] [MeasurableSpace G] [BorelSpace G]
    (cert : LatticeHaarGibbsCert) (S f : (E → G) → ℝ)
    (hint : Integrable (expWeight S) (productHaarProb E G))
    (hf : Integrable f (productHaarProb E G))
    (hfw : Integrable (fun U => f U * expWeight S U) (productHaarProb E G))
    (hf0 : ∀ U, 0 ≤ f U) (hmin : ∀ U, cert.vMin ≤ S U) (hmax : ∀ U, S U ≤ cert.vMax)
    (hhaar : cert.haarFloor ≤ ∫ U, f U ∂(productHaarProb E G)) :
    0 < Real.exp (-(cert.vMax - cert.vMin)) * cert.haarFloor ∧
      Real.exp (-(cert.vMax - cert.vMin)) * cert.haarFloor ≤
        weightedExpectation (productHaarProb E G) S f ∧
      ∀ U, expWeight S U / partitionIntegral (productHaarProb E G) S ≤
        Real.exp (cert.vMax - cert.vMin) := by
  have hpos : 0 < Real.exp (-(cert.vMax - cert.vMin)) * cert.haarFloor :=
    mul_pos (Real.exp_pos _) cert.hfloor
  have hmul :
      Real.exp (-(cert.vMax - cert.vMin)) * cert.haarFloor ≤
        Real.exp (-(cert.vMax - cert.vMin)) * ∫ U, f U ∂(productHaarProb E G) :=
    mul_le_mul_of_nonneg_left hhaar (le_of_lt (Real.exp_pos _))
  have hexp := productHaar_expectation_ge_exp_neg_osc hint hf hfw hf0 hmin hmax
  exact ⟨hpos, le_trans hmul hexp, productHaar_density_le_exp_osc hint hmin hmax⟩

end YangMillsBlueprint.Certificates
