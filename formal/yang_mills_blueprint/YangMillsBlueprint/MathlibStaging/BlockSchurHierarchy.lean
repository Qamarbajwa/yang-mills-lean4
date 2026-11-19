/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.Order.Field.Basic
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.SchurPartialTraceContraction

/-!
# Multi-Level Block-Matrix Schur Divide-and-Conquer Hierarchy

Formalizes how partitioning an arbitrarily large banded block chain `(d, c)` into alternating
even/odd sub-blocks and eliminating all even blocks via Schur complement induces exact
renormalization maps:

* `blockDiagNext d c := d - 2 * c ^ 2 / d`
* `blockCouplingNext d c := c ^ 2 / d`
* `blockRatioNext ρ := ρ ^ 2 / (2 - ρ ^ 2)`

## Main results

* `BlockSchurHierarchy.schur_chain_margin_eq`: exact margin amplification identity
  `blockDiagNext d c - 2 * blockCouplingNext d c = (d - 2 * c) * ((d + 2 * c) / d)`.
* `BlockSchurHierarchy.blockRatio_renorm_eq`: exact normalized ratio `ρ ^ 2 / (2 - ρ ^ 2)`.
* `BlockSchurHierarchy.blockRatioNext_lt_sq`: quadratic acceleration `blockRatioNext ρ < ρ ^ 2`
  across the entire open interval `0 < ρ < 1`.
* `BlockSchurHierarchy.blockChain_margin_monotone`: unconditional spectral gap growth
  `d - 2 * c ≤ blockDiagNext d c - 2 * blockCouplingNext d c`.
-/

@[expose] public section

namespace BlockSchurHierarchy

section FieldAlgebra

variable {F : Type*} [Field F]

/-- Schur-reduced diagonal stiffness per remaining block in a two-neighbor chain. -/
def blockDiagNext (d c : F) : F :=
  d - 2 * c ^ 2 / d

/-- Schur-induced nearest-neighbor coupling weight after eliminating intermediate blocks. -/
def blockCouplingNext (d c : F) : F :=
  c ^ 2 / d

/-- Normalized coupling ratio renormalization `ρ ↦ ρ ^ 2 / (2 - ρ ^ 2)`. -/
def blockRatioNext (ρ : F) : F :=
  ρ ^ 2 / (2 - ρ ^ 2)

/-- Iterated `k`-level recursive Schur ratio reduction across `2^k` coarse blocks. -/
def iteratedBlockRatio (ρ₀ : F) : ℕ → F
  | 0 => ρ₀
  | k + 1 => blockRatioNext (iteratedBlockRatio ρ₀ k)

/-- Exact two-neighbor even-block Schur completion identity:
eliminating intermediate variable `y` between neighbors `xL` and `xR` removes one
`c^2 / d` diagonal contribution from each neighbor and induces cross-coupling
`-2 * (c^2 / d) * xL * xR`. -/
theorem even_block_chain_complete_sq {d c xL y xR : F} (hd : d ≠ 0) :
    (c ^ 2 / d) * (xL ^ 2 + xR ^ 2) + d * y ^ 2 +
      2 * c * xL * y + 2 * c * xR * y =
      d * (y + (c / d) * (xL + xR)) ^ 2 - 2 * (c ^ 2 / d) * xL * xR := by
  field_simp
  ring

/-- Exact Gershgorin / spectral gap margin identity under even-block Schur elimination:
`(d - 2 * c^2 / d) - 2 * (c^2 / d) = (d - 2 * c) * ((d + 2 * c) / d)`. -/
theorem schur_chain_margin_eq {d c : F} (hd : d ≠ 0) :
    blockDiagNext d c - 2 * blockCouplingNext d c =
      (d - 2 * c) * ((d + 2 * c) / d) := by
  unfold blockDiagNext blockCouplingNext
  field_simp
  ring

end FieldAlgebra

section OrderedContraction

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Exact ratio renormalization identity when `2 * c = ρ * d`:
`2 * blockCouplingNext d c / blockDiagNext d c = blockRatioNext ρ`. -/
theorem blockRatio_renorm_eq {d c ρ : F}
    (hd : d ≠ 0) (hc : 2 * c = ρ * d) (hden : 2 - ρ ^ 2 ≠ 0) :
    2 * blockCouplingNext d c / blockDiagNext d c = blockRatioNext ρ := by
  unfold blockCouplingNext blockDiagNext blockRatioNext
  have h2 : (2 : F) ≠ 0 := ne_of_gt two_pos
  have hc_eq : c = ρ * d / 2 := by
    rw [← hc]
    field_simp
  rw [hc_eq]
  have hden2 : d - 2 * (ρ * d / 2) ^ 2 / d ≠ 0 := by
    have hEq : d - 2 * (ρ * d / 2) ^ 2 / d = d * (2 - ρ ^ 2) / 2 := by
      field_simp
    rw [hEq]
    exact div_ne_zero (mul_ne_zero hd hden) h2
  field_simp

/-- Unconditional quadratic acceleration `blockRatioNext ρ < ρ ^ 2` for all `0 < ρ < 1`. -/
theorem blockRatioNext_lt_sq {ρ : F} (h0 : 0 < ρ) (h1 : ρ < 1) :
    blockRatioNext ρ < ρ ^ 2 := by
  unfold blockRatioNext
  have hsq : ρ ^ 2 < 1 := by
    have hmul : ρ * ρ < 1 * 1 := mul_lt_mul h1 (le_of_lt h1) h0 zero_le_one
    linarith [show ρ ^ 2 = ρ * ρ by ring]
  have hden1 : 1 < 2 - ρ ^ 2 := by linarith
  have hden0 : 0 < 2 - ρ ^ 2 := by linarith
  refine (div_lt_iff₀ hden0).mpr ?_
  have hr2 : 0 < ρ ^ 2 := sq_pos_of_ne_zero (ne_of_gt h0)
  nlinarith

/-- Linear contraction `blockRatioNext ρ < ρ` across the entire open unit interval `0 < ρ < 1`. -/
theorem blockRatioNext_lt_self {ρ : F} (h0 : 0 < ρ) (h1 : ρ < 1) :
    blockRatioNext ρ < ρ := by
  have hsq : ρ ^ 2 < ρ := by
    have hmul : ρ * ρ < ρ * 1 := mul_lt_mul_of_pos_left h1 h0
    linarith [show ρ ^ 2 = ρ * ρ by ring]
  exact lt_trans (blockRatioNext_lt_sq h0 h1) hsq

/-- Invariance of `[0, 1)` under recursive Schur ratio iteration. -/
theorem iteratedBlockRatio_mem_Ico {ρ₀ : F} (h0 : 0 ≤ ρ₀) (h1 : ρ₀ < 1) (k : ℕ) :
    0 ≤ iteratedBlockRatio ρ₀ k ∧ iteratedBlockRatio ρ₀ k < 1 := by
  induction k with
  | zero => exact ⟨h0, h1⟩
  | succ k ih =>
      rcases ih with ⟨ih0, ih1⟩
      change 0 ≤ blockRatioNext (iteratedBlockRatio ρ₀ k) ∧
        blockRatioNext (iteratedBlockRatio ρ₀ k) < 1
      rcases lt_or_eq_of_le ih0 with hpos | heq
      · have hlt := blockRatioNext_lt_self hpos ih1
        unfold blockRatioNext
        have hsq : (iteratedBlockRatio ρ₀ k) ^ 2 < 1 := by
          have hmul : iteratedBlockRatio ρ₀ k * iteratedBlockRatio ρ₀ k < 1 * 1 :=
            mul_lt_mul ih1 (le_of_lt ih1) hpos zero_le_one
          linarith [show iteratedBlockRatio ρ₀ k ^ 2 =
            iteratedBlockRatio ρ₀ k * iteratedBlockRatio ρ₀ k by ring]
        exact ⟨div_nonneg (sq_nonneg _) (by linarith), lt_trans hlt ih1⟩
      · rw [← heq]
        unfold blockRatioNext
        simp [zero_lt_one]

/-- Unconditional spectral gap monotonicity under recursive even-block Schur elimination:
whenever `0 ≤ c` and `2 * c ≤ d` with `0 < d`, the Gershgorin diagonal-dominance margin never
decreases (`d - 2 * c ≤ blockDiagNext d c - 2 * blockCouplingNext d c`). -/
theorem blockChain_margin_monotone {d c : F}
    (hd : 0 < d) (hc0 : 0 ≤ c) (hgap : 2 * c ≤ d) :
    d - 2 * c ≤ blockDiagNext d c - 2 * blockCouplingNext d c := by
  rw [schur_chain_margin_eq (ne_of_gt hd)]
  have hfac : 1 ≤ (d + 2 * c) / d := by
    rw [le_div_iff₀ hd]
    linarith
  have hmargin : 0 ≤ d - 2 * c := sub_nonneg.mpr hgap
  calc d - 2 * c = (d - 2 * c) * 1 := by ring
    _ ≤ (d - 2 * c) * ((d + 2 * c) / d) := mul_le_mul_of_nonneg_left hfac hmargin

end OrderedContraction

end BlockSchurHierarchy
