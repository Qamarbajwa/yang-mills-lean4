/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.AbstractPolymerCluster
import Mathlib.Tactic.NormNum

/-!
# YM-172: Abstract Finite Polymer Cluster Convergence & Collar Decoupling Certificate

Certifies:
1. Unconditional abstract finite polymer cluster bounds (`0 < polymerZ S`, pinned ratio
   `≤ exp (a x)`, deletion bound, and `L`-uniform collar decoupling independent of exterior `S₂`)
   from the classical Kotecký-Preiss `1/2` criterion (`kotecky_preiss_half_condition_implies_dkp`).
2. Conditional Stage-1 compact product Haar Gibbs lifting combining interior capacity `B_int` with
   volume-independent polymer collar decoupling error bounded by `∑_{y ∈ B} kpLogWeight z a y`.
-/

namespace YangMillsBlueprint.Certificates

open AbstractPolymerCluster BalabanPolymerCollar BlockPolymerOscillation LatticeHaarGibbs
open MeasureTheory

/-- Stage-1 abstract polymer activity and logarithmic weight envelope certificate. -/
structure AbstractPolymerCert where
  a0 : ℝ
  zCap : ℝ
  haarFloor : ℝ
  ha0 : 0 < a0
  hz0 : 0 ≤ zCap
  hkpHalf : zCap * Real.exp a0 ≤ 1 / 2
  hfloor : 0 < haarFloor

/-- Canonical calibrated Kotecký-Preiss witness (`a0 = log 2`, `zCap = 1/4` ⇒ `1/4 * 2 = 1/2`). -/
noncomputable def canonicalAbstractPolymerCert : AbstractPolymerCert where
  a0 := Real.log 2
  zCap := 1 / 4
  haarFloor := 1
  ha0 := Real.log_pos (by norm_num)
  hz0 := by norm_num
  hkpHalf := by
    rw [Real.exp_log (by norm_num)]
    norm_num
  hfloor := by norm_num

instance : Nonempty AbstractPolymerCert :=
  ⟨canonicalAbstractPolymerCert⟩

/-- **UNCONDITIONAL:** Any finite polymer family `(U, incomp, z, a)` obeying the classical
Kotecký-Preiss `1/2` criterion satisfies Dobrushin-Kotecký-Preiss, strict positivity `0 < Z(S)`,
uniform pinned ratio `≤ exp (a x)`, single-deletion stability, and `L`-uniform collar decoupling
for arbitrary compatible disjoint exterior regions `S₂`. -/
theorem abstract_polymer_kp_collar_decoupling_unconditional {P : Type*} [DecidableEq P]
    (incomp : P → P → Prop) (hrefl : ∀ u, incomp u u)
    (hsym : ∀ u v, incomp u v → incomp v u) {U : Finset P} {z a : P → ℝ}
    (ha : ∀ x ∈ U, 0 ≤ a x) (hrHalf : ∀ x ∈ U, |z x| * Real.exp (a x) ≤ 1 / 2)
    (hkp : ∀ x ∈ U, (∑ y ∈ nbhd incomp U x, |z y| * Real.exp (a y)) ≤ a x / 2)
    {S₁ S₂ B : Finset P} (h12 : Disjoint S₁ S₂) (h1B : Disjoint S₁ B) (h2B : Disjoint S₂ B)
    (hcompat : ∀ u ∈ S₁, ∀ v ∈ S₂, ¬ incomp u v) (hsub : S₁ ∪ S₂ ∪ B ⊆ U) (x : P)
    (hxU : x ∈ U) :
    0 < polymerZ incomp z (S₁ ∪ S₂ ∪ B) ∧
      polymerZ incomp z (withoutNbhd incomp (S₁ ∪ S₂ ∪ B) x) /
          polymerZ incomp z (S₁ ∪ S₂ ∪ B) ≤ Real.exp (a x) ∧
      |Real.log (polymerZ incomp z (S₁ ∪ S₂ ∪ B)) -
          (Real.log (polymerZ incomp z S₁) + Real.log (polymerZ incomp z S₂))| ≤
        ∑ y ∈ B, kpLogWeight z a y := by
  obtain ⟨hr, hdkp⟩ := kotecky_preiss_half_condition_implies_dkp incomp hrHalf hkp
  have hb := dobrushin_kp_cluster_bounds hrefl hsym ha hr hdkp hsub
  have hdec := polymerZ_collar_decoupling_le hrefl hsym ha hr hdkp h12 h1B h2B hcompat hsub
  exact ⟨hb.1, hb.2.2 x hxU, hdec⟩

/-- **CONDITIONAL:** Once Stage-1 polymer expansion splits finite-box effective action as
`S U = S_int U + log Z_ext(S₁ ∪ S₂ ∪ B)` with `S_int ∈ [0, B_int]` and Kotecký-Preiss collar
coupling bounded independently of exterior `S₂` by `∑_{y ∈ B} kpLogWeight z a y ≤ collarCap`,
every compact Haar box `(E → G)` inherits a uniform density cap and strict expectation floor. -/
theorem stage1_polymer_gas_gibbs_decoupling_conditional {E G P : Type*} [Fintype E]
    [DecidableEq P] [Group G] [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (cert : AbstractPolymerCert)
    (incomp : P → P → Prop) (hrefl : ∀ u, incomp u u)
    (hsym : ∀ u v, incomp u v → incomp v u) (U S₁ S₂ B : Finset P)
    (z a : P → ℝ) (ha : ∀ x ∈ U, 0 ≤ a x)
    (hrHalf : ∀ x ∈ U, |z x| * Real.exp (a x) ≤ 1 / 2)
    (hkp : ∀ x ∈ U, (∑ y ∈ nbhd incomp U x, |z y| * Real.exp (a y)) ≤ a x / 2)
    (h12 : Disjoint S₁ S₂) (h1B : Disjoint S₁ B) (h2B : Disjoint S₂ B)
    (hcompat : ∀ u ∈ S₁, ∀ v ∈ S₂, ¬ incomp u v) (hsub : S₁ ∪ S₂ ∪ B ⊆ U)
    (B_int collarCap : ℝ)
    (S S_int S_ext f : (E → G) → ℝ)
    (hint : Integrable (expWeight S) (productHaarProb E G))
    (hf : Integrable f (productHaarProb E G))
    (hfw : Integrable (fun W => f W * expWeight S W) (productHaarProb E G))
    (hf0 : ∀ W, 0 ≤ f W)
    (hdecomp : ∀ W, S W = S_int W + S_ext W)
    (hintLo : ∀ W, 0 ≤ S_int W) (hintHi : ∀ W, S_int W ≤ B_int)
    (hcollarSum : (∑ y ∈ B, kpLogWeight z a y) ≤ collarCap)
    (hextBd : ∀ W,
      |S_ext W| ≤
        |Real.log (polymerZ incomp z (S₁ ∪ S₂ ∪ B)) -
          (Real.log (polymerZ incomp z S₁) + Real.log (polymerZ incomp z S₂))|)
    (hhaar : cert.haarFloor ≤ ∫ W, f W ∂(productHaarProb E G)) :
    0 < Real.exp (-(B_int + 2 * collarCap)) * cert.haarFloor ∧
      Real.exp (-(B_int + 2 * collarCap)) * cert.haarFloor ≤
        weightedExpectation (productHaarProb E G) S f ∧
      ∀ W, expWeight S W / partitionIntegral (productHaarProb E G) S ≤
        Real.exp (B_int + 2 * collarCap) := by
  obtain ⟨hr, hdkp⟩ := kotecky_preiss_half_condition_implies_dkp incomp hrHalf hkp
  have hdec := polymerZ_collar_decoupling_le hrefl hsym ha hr hdkp h12 h1B h2B hcompat hsub
  have hextCollar : ∀ W, |S_ext W| ≤ collarCap := fun W =>
    le_trans (hextBd W) (le_trans hdec hcollarSum)
  have hmin : ∀ W, -collarCap ≤ S W := fun W => by
    have := (abs_le.mp (hextCollar W)).1
    linarith [hdecomp W, hintLo W]
  have hmax : ∀ W, S W ≤ B_int + collarCap := fun W => by
    have := (abs_le.mp (hextCollar W)).2
    linarith [hdecomp W, hintHi W]
  have hoscEq : (B_int + collarCap) - (-collarCap) = B_int + 2 * collarCap := by ring
  have hpos : 0 < Real.exp (-(B_int + 2 * collarCap)) * cert.haarFloor :=
    mul_pos (Real.exp_pos _) cert.hfloor
  have hexp := productHaar_expectation_ge_exp_neg_osc hint hf hfw hf0 hmin hmax
  have hcap := productHaar_density_le_exp_osc hint hmin hmax
  rw [hoscEq] at hexp hcap
  have hmul :
      Real.exp (-(B_int + 2 * collarCap)) * cert.haarFloor ≤
        Real.exp (-(B_int + 2 * collarCap)) * (∫ W, f W ∂(productHaarProb E G)) :=
    mul_le_mul_of_nonneg_left hhaar (le_of_lt (Real.exp_pos _))
  exact ⟨hpos, le_trans hmul hexp, hcap⟩

end YangMillsBlueprint.Certificates
