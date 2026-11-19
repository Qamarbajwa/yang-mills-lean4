/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.TreeFrameGaugeInvariance
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# YM-154: Hierarchical Tree-Frame Gauge Invariance Certificate

Certifies that assigning local spanning-tree frames on any finite lattice `(V, E)` over a
compact topological group `G`:
1. Flattens every spanning-tree link identically to `1` without losing Haar invariance.
2. Preserves `partitionIntegral` and `weightedExpectation` on `productHaarProb E G`.
3. Lifts bounded effective action oscillation in any assigned frame slice directly to a
   uniform Boltzmann expectation lower bound via `LatticeHaarGibbs`.
-/

namespace YangMillsBlueprint.Certificates

open LatticeHaarGibbs TreeFrameGaugeInvariance MeasureTheory

/-- Real certificate bundling tree-frame effective action bounds and Haar floor. -/
structure TreeFrameGaugeCert where
  vMin : ℝ
  vMax : ℝ
  haarFloor : ℝ
  hle : vMin ≤ vMax
  hfloor : 0 < haarFloor

/-- Canonical witness (`vMin = 0`, `vMax = log 3`, `haarFloor = 3` ⇒ floor `1`). -/
noncomputable def canonicalTreeFrameGaugeCert : TreeFrameGaugeCert where
  vMin := 0
  vMax := Real.log 3
  haarFloor := 3
  hle := Real.log_nonneg (by norm_num)
  hfloor := by norm_num

instance : Nonempty TreeFrameGaugeCert :=
  ⟨canonicalTreeFrameGaugeCert⟩

/-- Exact canonical tree-frame expectation floor `Real.exp (-(log 3 - 0)) * 3 = 1`. -/
theorem canonical_tree_frame_floor_eq :
    Real.exp (-(canonicalTreeFrameGaugeCert.vMax - canonicalTreeFrameGaugeCert.vMin)) *
      canonicalTreeFrameGaugeCert.haarFloor = 1 := by
  dsimp [canonicalTreeFrameGaugeCert]
  rw [sub_zero, Real.exp_neg, Real.exp_log (by norm_num)]
  norm_num

/-- **UNCONDITIONAL:** Any fixed frame assignment `g : V → G` flattens tree edges `e` where
`g (dst e) = g (src e) * U e` to `1` and preserves `productHaarProb E G` integrals and Gibbs
expectations identically on any compact topological group `G`. -/
theorem tree_frame_gauge_expectation_unconditional {V E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (src dst : E → V) (g : V → G)
    (U : E → G) (e : E) (htree : g (dst e) = g (src e) * U e)
    (S f : (E → G) → ℝ) :
    gaugeTransform src dst g U e = 1 ∧
      weightedExpectation (productHaarProb E G)
          (fun W => S (gaugeTransform src dst g W))
          (fun W => f (gaugeTransform src dst g W)) =
        weightedExpectation (productHaarProb E G) S f :=
  ⟨gaugeTransform_eq_one_of_tree_frame src dst g U e htree,
    weightedExpectation_gaugeTransform src dst g S f⟩

/-- **CONDITIONAL:** If pulling `(S, f)` back into an assigned frame slice `gaugeTransform src dst g`
gives bounded action oscillation `[cert.vMin, cert.vMax]` and a Haar floor
`cert.haarFloor ≤ ∫ W, f (gaugeTransform src dst g W) ∂(productHaarProb E G)`, then the original
un-gauged Gibbs expectation satisfies the identical strict lower bound
`Real.exp (-(cert.vMax - cert.vMin)) * cert.haarFloor ≤ weightedExpectation (productHaarProb E G) S f`. -/
theorem tree_frame_oscillation_floor_conditional {V E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (cert : TreeFrameGaugeCert)
    (src dst : E → V) (g : V → G) (S f : (E → G) → ℝ)
    (hint : Integrable (expWeight S) (productHaarProb E G))
    (hf : Integrable f (productHaarProb E G))
    (hfw : Integrable (fun W => f W * expWeight S W) (productHaarProb E G))
    (hf0 : ∀ W, 0 ≤ f (gaugeTransform src dst g W))
    (hmin : ∀ W, cert.vMin ≤ S (gaugeTransform src dst g W))
    (hmax : ∀ W, S (gaugeTransform src dst g W) ≤ cert.vMax)
    (hhaar :
      cert.haarFloor ≤ ∫ W, f (gaugeTransform src dst g W) ∂(productHaarProb E G)) :
    0 < Real.exp (-(cert.vMax - cert.vMin)) * cert.haarFloor ∧
      Real.exp (-(cert.vMax - cert.vMin)) * cert.haarFloor ≤
        weightedExpectation (productHaarProb E G) S f := by
  let Sg : (E → G) → ℝ := fun W => S (gaugeTransform src dst g W)
  let fg : (E → G) → ℝ := fun W => f (gaugeTransform src dst g W)
  have hintG : Integrable (expWeight Sg) (productHaarProb E G) :=
    (integrable_gaugeTransform_iff src dst g (expWeight S)).mpr hint
  have hfG : Integrable fg (productHaarProb E G) :=
    (integrable_gaugeTransform_iff src dst g f).mpr hf
  have hfwG : Integrable (fun W => fg W * expWeight Sg W) (productHaarProb E G) :=
    (integrable_gaugeTransform_iff src dst g (fun W => f W * expWeight S W)).mpr hfw
  have hpos : 0 < Real.exp (-(cert.vMax - cert.vMin)) * cert.haarFloor :=
    mul_pos (Real.exp_pos _) cert.hfloor
  have hmul :
      Real.exp (-(cert.vMax - cert.vMin)) * cert.haarFloor ≤
        Real.exp (-(cert.vMax - cert.vMin)) * ∫ W, fg W ∂(productHaarProb E G) :=
    mul_le_mul_of_nonneg_left hhaar (le_of_lt (Real.exp_pos _))
  have hexp := productHaar_expectation_ge_exp_neg_osc hintG hfG hfwG hf0 hmin hmax
  rw [weightedExpectation_gaugeTransform src dst g S f] at hexp
  exact ⟨hpos, le_trans hmul hexp⟩

end YangMillsBlueprint.Certificates
