/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Analysis.SpecificLimits.Basic
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.IsotropicSuperblockDobrushin
public import YangMillsBlueprint.MathlibStaging.SliceReflectionHilbert

/-!
# Stage 2B Non-Critical Exponential Slab Contraction vs. Power-Law Failure

Addresses Referee Gap 3 (`Stage 2B`):

* `NonCriticalSlabContraction.powerLaw_fails_uniform_contraction`: rigorously proves that an
  algebraic (massless critical) correlation ratio `((t + 1) / (t + 2)) ^ k` tends to `1` as
  `t → ∞`, hence violates every fixed contraction threshold `r < 1` at large separation `t`.
* `NonCriticalSlabContraction.exists_slab_thickness_contraction`: proves that under an exponential
  transfer gap `0 < r < 1` (`ContractiveTransfer`) with bounded super-block leakage `α ≥ 0`,
  there exists a finite slab thickness `k ≥ 1` making both `(2 + α) * r ^ k < 1` and the
  `YM145`/`YM147` Schur slab coupling ratio `slabTailSum α r k < 1`.
-/

@[expose] public section

namespace NonCriticalSlabContraction

open Filter IsotropicSuperblockDobrushin SliceReflectionHilbert Topology

/-- Algebraic power-law separation ratio `((t + 1) / (t + 2)) ^ k` of a critical phase. -/
noncomputable def powerLawRatio (k t : ℕ) : ℝ :=
  (((t : ℝ) + 1) / ((t : ℝ) + 2)) ^ k

/-- Non-Markovian Schur-rescaled slab tail coupling `(1 + α) * r ^ k / (1 - r ^ k)`. -/
noncomputable def slabTailSum (α r : ℝ) (k : ℕ) : ℝ :=
  (1 + α) * r ^ k / (1 - r ^ k)

/-- Every fixed-width power-law correlation ratio converges to `1` as `t → ∞`. -/
theorem tendsto_powerLawRatio_one (k : ℕ) :
    Tendsto (powerLawRatio k) atTop (𝓝 1) := by
  have hdiv : Tendsto (fun t : ℕ => (1 : ℝ) / ((t : ℝ) + 2)) atTop (𝓝 0) := by
    simpa [Nat.cast_add, Nat.cast_ofNat] using
      (tendsto_add_atTop_iff_nat 2).2 (tendsto_one_div_atTop_nhds_zero_nat (𝕜 := ℝ))
  have hbase : Tendsto (fun t : ℕ => ((t : ℝ) + 1) / ((t : ℝ) + 2)) atTop (𝓝 1) := by
    have heq : (fun t : ℕ => ((t : ℝ) + 1) / ((t : ℝ) + 2)) =
        fun t : ℕ => 1 - (1 : ℝ) / ((t : ℝ) + 2) := by
      funext t
      have hne : (t : ℝ) + 2 ≠ 0 := by positivity
      field_simp
      ring
    rw [heq]
    simpa using tendsto_const_nhds.sub hdiv
  unfold powerLawRatio
  simpa using hbase.pow k

/-- **UNCONDITIONAL REFUTATION:** An algebraic power-law critical phase violates any fixed strict
contraction factor `r < 1` at sufficiently large block thickness/separation `t ≥ T`. -/
theorem powerLaw_fails_uniform_contraction (k : ℕ) {r : ℝ} (hr : r < 1) :
    ∃ T : ℕ, ∀ t : ℕ, T ≤ t → r < powerLawRatio k t := by
  have hev := (tendsto_powerLawRatio_one k).eventually (lt_mem_nhds hr)
  rw [eventually_atTop] at hev
  exact hev

/-- If `(2 + α) * r ^ k < 1` with `0 ≤ α` and `0 ≤ r`, then the slab Schur tail ratio
`(1 + α) * r ^ k / (1 - r ^ k)` is strictly less than `1`. -/
theorem slabTailSum_lt_one_of_gap {α r : ℝ} (hα : 0 ≤ α) (hr0 : 0 ≤ r)
    {k : ℕ} (hk : (2 + α) * r ^ k < 1) :
    slabTailSum α r k < 1 := by
  unfold slabTailSum
  have hrk_lt : r ^ k < 1 := by
    have hrk0 : 0 ≤ r ^ k := pow_nonneg hr0 k
    nlinarith
  have hden : 0 < 1 - r ^ k := sub_pos.mpr hrk_lt
  rw [div_lt_one hden]
  linarith

/-- Finite slab thickness theorem: for any `α ≥ 0` and exponential transfer contraction `0 < r < 1`,
there exists finite `k ≥ 1` with `(2 + α) * r ^ k < 1` and `slabTailSum α r k < 1`. -/
theorem exists_slab_thickness_contraction {α r : ℝ} (hα : 0 ≤ α) (hr0 : 0 < r) (hr1 : r < 1) :
    ∃ k : ℕ, 1 ≤ k ∧ (2 + α) * r ^ k < 1 ∧ slabTailSum α r k < 1 := by
  have h2α : 0 < 2 + α := by linarith
  have htarget : 0 < (1 : ℝ) / (2 + α) := div_pos zero_lt_one h2α
  have hev : ∀ᶠ k in atTop, r ^ k < 1 / (2 + α) :=
    (tendsto_pow_atTop_nhds_zero_of_lt_one (le_of_lt hr0) hr1).eventually (gt_mem_nhds htarget)
  rw [eventually_atTop] at hev
  obtain ⟨K, hK⟩ := hev
  let k := max K 1
  have hk_ge_K : K ≤ k := le_max_left K 1
  have hk_ge_1 : 1 ≤ k := le_max_right K 1
  have hpow : r ^ k < 1 / (2 + α) := hK k hk_ge_K
  have hmul : (2 + α) * r ^ k < 1 := by
    have h := mul_lt_mul_of_pos_left hpow h2α
    rwa [mul_one_div_cancel (ne_of_gt h2α)] at h
  exact ⟨k, hk_ge_1, hmul, slabTailSum_lt_one_of_gap hα (le_of_lt hr0) hmul⟩

end NonCriticalSlabContraction
