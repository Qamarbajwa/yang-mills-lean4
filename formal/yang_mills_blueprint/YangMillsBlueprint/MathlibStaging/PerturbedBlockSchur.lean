/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Algebra.Order.Field.Basic
public import Mathlib.Data.Matrix.Mul
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.BlockSchurHierarchy

/-!
# Tail-Perturbed Block Schur Contraction and Matrix Gershgorin Coercivity

Extends `BlockSchurHierarchy` (`YM147`) to non-Markovian block operators perturbed by even-sector
and odd-sector polymer tails `τ_e, τ_o ≥ 0`:

* `PerturbedBlockSchur.gershgorin_row_lower_bound` and
  `PerturbedBlockSchur.diag_dominant_mulVec_injective`: unconditional matrix `ℓ^∞` Gershgorin
  coercivity and injectivity for any strictly diagonally dominant square matrix.
* `PerturbedBlockSchur.perturbedMarginNext` and `PerturbedBlockSchur.perturbedRatioBound`:
  coarse margin `(1 - τ_e - τ_o) - ρ ^ 2 / (1 - τ_e)` and effective coupling bound
  `τ_e + τ_o + ρ ^ 2 / (1 - τ_e)` after eliminating the even block `(I - K_ee)⁻¹`.
* `PerturbedBlockSchur.recoilRatio`: 1D block-chain Schur ratio with diagonal recoil and polymer
  tails, recovering `BlockSchurHierarchy.blockRatioNext ρ` unconditionally at `τ_e = τ_o = 0`.
-/

@[expose] public section

namespace PerturbedBlockSchur

open BlockSchurHierarchy Matrix

section GershgorinCoercivity

variable {F : Type*} [CommRing F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Sum of absolute off-diagonal entries in row `i` of a square matrix `A`. -/
def offDiagAbsSum {n : ℕ} (A : Matrix (Fin n) (Fin n) F) (i : Fin n) : F :=
  ∑ j ∈ Finset.univ.erase i, |A i j|

/-- Row `i` Gershgorin diagonal dominance margin `|A i i| - ∑_{j ≠ i} |A i j|`. -/
def rowGershgorinMargin {n : ℕ} (A : Matrix (Fin n) (Fin n) F) (i : Fin n) : F :=
  |A i i| - offDiagAbsSum A i

/-- If row `i` maximizes `|v j|` across coordinates, then `rowGershgorinMargin A i * |v i| ≤
|(A *ᵥ v) i|`. This holds over any linearly ordered commutative ring with zero division. -/
theorem gershgorin_row_lower_bound {n : ℕ} (A : Matrix (Fin n) (Fin n) F) (v : Fin n → F)
    {i : Fin n} (hmax : ∀ j : Fin n, |v j| ≤ |v i|) :
    rowGershgorinMargin A i * |v i| ≤ |(A *ᵥ v) i| := by
  have hrow : A i i * v i = (A *ᵥ v) i - ∑ j ∈ Finset.univ.erase i, A i j * v j := by
    have hsplit := Finset.add_sum_erase Finset.univ (fun j : Fin n => A i j * v j)
      (Finset.mem_univ i)
    have hmul : (A *ᵥ v) i = ∑ j : Fin n, A i j * v j := rfl
    linarith
  have htri : |A i i * v i| ≤ |(A *ᵥ v) i| + |∑ j ∈ Finset.univ.erase i, A i j * v j| := by
    rw [hrow, sub_eq_add_neg]
    calc
      |(A *ᵥ v) i + -(∑ j ∈ Finset.univ.erase i, A i j * v j)|
          ≤ |(A *ᵥ v) i| + |-(∑ j ∈ Finset.univ.erase i, A i j * v j)| := abs_add_le _ _
      _ = |(A *ᵥ v) i| + |∑ j ∈ Finset.univ.erase i, A i j * v j| := by rw [abs_neg]
  have hsumAbs :
      |∑ j ∈ Finset.univ.erase i, A i j * v j| ≤ offDiagAbsSum A i * |v i| := by
    calc
      |∑ j ∈ Finset.univ.erase i, A i j * v j|
          ≤ ∑ j ∈ Finset.univ.erase i, |A i j * v j| := Finset.abs_sum_le_sum_abs _ _
      _ = ∑ j ∈ Finset.univ.erase i, |A i j| * |v j| := by
            refine Finset.sum_congr rfl ?_
            intro j _
            exact abs_mul (A i j) (v j)
      _ ≤ ∑ j ∈ Finset.univ.erase i, |A i j| * |v i| := by
            refine Finset.sum_le_sum ?_
            intro j _
            exact mul_le_mul_of_nonneg_left (hmax j) (abs_nonneg (A i j))
      _ = offDiagAbsSum A i * |v i| := by
            rw [← Finset.sum_mul]
            rfl
  have hdiag : |A i i * v i| = |A i i| * |v i| := abs_mul (A i i) (v i)
  unfold rowGershgorinMargin
  linarith

/-- Uniform `ℓ^∞` Gershgorin lower bound: if every row margin of `A` is at least `δ ≥ 0`, then
for any vector `v` and index `k` there exists a coordinate `i` with `δ * |v k| ≤ |(A *ᵥ v) i|`. -/
theorem diag_dominant_linfty_lower_bound {n : ℕ} (A : Matrix (Fin n) (Fin n) F) {δ : F}
    (hδ0 : 0 ≤ δ) (hδ : ∀ i : Fin n, δ ≤ rowGershgorinMargin A i) (v : Fin n → F) (k : Fin n) :
    ∃ i : Fin n, δ * |v k| ≤ |(A *ᵥ v) i| := by
  have hne : (Finset.univ : Finset (Fin n)).Nonempty := ⟨k, Finset.mem_univ k⟩
  obtain ⟨i, _, hmax⟩ := Finset.exists_max_image Finset.univ (fun j : Fin n => |v j|) hne
  refine ⟨i, ?_⟩
  have h1 : δ * |v k| ≤ δ * |v i| :=
    mul_le_mul_of_nonneg_left (hmax k (Finset.mem_univ k)) hδ0
  have h2 : δ * |v i| ≤ rowGershgorinMargin A i * |v i| :=
    mul_le_mul_of_nonneg_right (hδ i) (abs_nonneg (v i))
  have h3 : rowGershgorinMargin A i * |v i| ≤ |(A *ᵥ v) i| :=
    gershgorin_row_lower_bound A v (fun j => hmax j (Finset.mem_univ j))
  exact le_trans h1 (le_trans h2 h3)

/-- Unconditional strict diagonal dominance injectivity: if `0 < rowGershgorinMargin A i` for
every row `i`, then `A.mulVec` is injective. -/
theorem diag_dominant_mulVec_injective {n : ℕ} (A : Matrix (Fin n) (Fin n) F)
    (hdom : ∀ i : Fin n, 0 < rowGershgorinMargin A i) :
    Function.Injective A.mulVec := by
  intro v₁ v₂ hv
  have hdiff : A *ᵥ (v₁ - v₂) = 0 := by
    rw [Matrix.mulVec_sub, hv, sub_self]
  ext k
  have hne : (Finset.univ : Finset (Fin n)).Nonempty := ⟨k, Finset.mem_univ k⟩
  obtain ⟨i, _, hmax⟩ := Finset.exists_max_image Finset.univ (fun j : Fin n => |(v₁ - v₂) j|) hne
  have hbound : rowGershgorinMargin A i * |(v₁ - v₂) i| ≤ |(A *ᵥ (v₁ - v₂)) i| :=
    gershgorin_row_lower_bound A (v₁ - v₂) (fun j => hmax j (Finset.mem_univ j))
  have hzero : (A *ᵥ (v₁ - v₂)) i = 0 := by
    rw [hdiff]
    rfl
  rw [hzero, abs_zero] at hbound
  have hle0 : |(v₁ - v₂) i| ≤ 0 := by
    by_contra hlt
    have hgt : 0 < |(v₁ - v₂) i| := lt_of_not_ge hlt
    exact absurd (mul_pos (hdom i) hgt) (not_lt_of_ge hbound)
  have hk0 : |(v₁ - v₂) k| ≤ 0 := le_trans (hmax k (Finset.mem_univ k)) hle0
  have hsub0 : (v₁ - v₂) k = 0 := abs_nonpos_iff.mp hk0
  exact sub_eq_zero.mp hsub0

end GershgorinCoercivity

section PerturbedSchurDefinitions

variable {F : Type*} [Field F]

/-- Coarse-grained odd-sector Gershgorin margin after eliminating `(I - K_ee)⁻¹`:
`1 - τ_e - τ_o - ρ ^ 2 / (1 - τ_e)`. -/
def perturbedMarginNext (ρ τ_e τ_o : F) : F :=
  (1 - τ_e - τ_o) - ρ ^ 2 / (1 - τ_e)

/-- Coarse-grained effective off-diagonal coupling bound after even-block elimination:
`τ_e + τ_o + ρ ^ 2 / (1 - τ_e)`. -/
def perturbedRatioBound (ρ τ_e τ_o : F) : F :=
  τ_e + τ_o + ρ ^ 2 / (1 - τ_e)

/-- 1D block-chain Schur coupling ratio with diagonal recoil and non-Markovian polymer tails:
`((ρ ^ 2 / (2 * (1 - τ_e))) + τ_o) / (1 - ρ ^ 2 / (2 * (1 - τ_e)))`. -/
def recoilRatio (ρ τ_e τ_o : F) : F :=
  (ρ ^ 2 / (2 * (1 - τ_e)) + τ_o) / (1 - ρ ^ 2 / (2 * (1 - τ_e)))

/-- Complement relation between coarse margin and coarse coupling ratio. -/
theorem perturbedMarginNext_eq (ρ τ_e τ_o : F) :
    perturbedMarginNext ρ τ_e τ_o = 1 - perturbedRatioBound ρ τ_e τ_o := by
  unfold perturbedMarginNext perturbedRatioBound
  ring

/-- Difference between total pre-Schur coupling `ρ + τ_e` and the coarse Schur bound
`perturbedRatioBound ρ τ_e τ_o`. -/
theorem perturbedRatioBound_sub_tot {ρ τ_e τ_o : F} (hτ : 1 - τ_e ≠ 0) :
    (ρ + τ_e) - perturbedRatioBound ρ τ_e τ_o =
      ρ * (1 - τ_e - ρ) / (1 - τ_e) - τ_o := by
  unfold perturbedRatioBound
  field_simp
  ring

/-- Exact recoil ratio identity cleared of inner fractions. -/
theorem recoilRatio_eq {ρ τ_e τ_o : F} (h2 : (2 : F) ≠ 0) (hτ : 1 - τ_e ≠ 0) :
    recoilRatio ρ τ_e τ_o =
      (ρ ^ 2 + 2 * τ_o * (1 - τ_e)) / (2 * (1 - τ_e) - ρ ^ 2) := by
  unfold recoilRatio
  field_simp

/-- Unconditional specialization: setting both polymer tails `τ_e = τ_o = 0` recovers
`YM147` (`BlockSchurHierarchy.blockRatioNext ρ = ρ ^ 2 / (2 - ρ ^ 2)`). -/
theorem recoilRatio_recovers_ym147 {ρ : F} (h2 : (2 : F) ≠ 0) :
    recoilRatio ρ 0 0 = blockRatioNext ρ := by
  unfold recoilRatio blockRatioNext
  field_simp
  ring

/-- Symmetric specialization `τ_o = 0`: the coarse margin factorizes multiplicatively just as
in `BlockSchurHierarchy.schur_chain_margin_eq`. -/
theorem perturbedMarginNext_factor_zero {ρ τ_e : F} (hτ : 1 - τ_e ≠ 0) :
    perturbedMarginNext ρ τ_e 0 = (1 - τ_e - ρ) * ((1 - τ_e + ρ) / (1 - τ_e)) := by
  unfold perturbedMarginNext
  field_simp
  ring

end PerturbedSchurDefinitions

section PerturbedSchurContraction

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Under pre-Schur contraction `0 < ρ`, `ρ + τ_e < 1`, and bounded odd-sector tail excess
`τ_o < ρ * (1 - τ_e - ρ) / (1 - τ_e)`, the coarse coupling bound is strictly below `ρ + τ_e`. -/
theorem perturbedRatioBound_lt_tot {ρ τ_e τ_o : F} (hρ0 : 0 < ρ)
    (hr : ρ + τ_e < 1) (hτo : τ_o < ρ * (1 - τ_e - ρ) / (1 - τ_e)) :
    perturbedRatioBound ρ τ_e τ_o < ρ + τ_e := by
  have h1τ : 0 < 1 - τ_e := by linarith
  have h1τ0 : 1 - τ_e ≠ 0 := ne_of_gt h1τ
  have hsub := perturbedRatioBound_sub_tot (ρ := ρ) (τ_e := τ_e) (τ_o := τ_o) h1τ0
  have hpos : 0 < (ρ + τ_e) - perturbedRatioBound ρ τ_e τ_o := by
    rw [hsub]
    exact sub_pos.mpr hτo
  exact sub_pos.mp hpos

/-- Dual margin amplification theorem: under the same hypotheses, the coarse Gershgorin margin
strictly exceeds the pre-Schur margin `1 - (ρ + τ_e)`. -/
theorem perturbedMarginNext_gt_margin {ρ τ_e τ_o : F} (hρ0 : 0 < ρ)
    (hr : ρ + τ_e < 1) (hτo : τ_o < ρ * (1 - τ_e - ρ) / (1 - τ_e)) :
    1 - (ρ + τ_e) < perturbedMarginNext ρ τ_e τ_o := by
  rw [perturbedMarginNext_eq]
  have hlt := perturbedRatioBound_lt_tot hρ0 hr hτo
  linarith

/-- 1D recoil contraction bound: whenever `0 ≤ ρ`, `0 ≤ τ_e`, `τ_e < 1`, `τ_o ≤ τ_e`, and
`ρ + τ_e ≤ 1`, the recoil ratio does not exceed the total pre-Schur coupling `ρ + τ_e`. -/
theorem recoilRatio_le_self {ρ τ_e τ_o : F} (hρ0 : 0 ≤ ρ) (hτe0 : 0 ≤ τ_e) (hτe1 : τ_e < 1)
    (hτole : τ_o ≤ τ_e) (hr : ρ + τ_e ≤ 1) :
    recoilRatio ρ τ_e τ_o ≤ ρ + τ_e := by
  have h2 : (2 : F) ≠ 0 := ne_of_gt two_pos
  have h1τ : 0 < 1 - τ_e := by linarith
  have h1τ0 : 1 - τ_e ≠ 0 := ne_of_gt h1τ
  rw [recoilRatio_eq h2 h1τ0]
  have hρ1 : ρ ≤ 1 - τ_e := by linarith
  have hρsq : ρ ^ 2 ≤ (1 - τ_e) ^ 2 := by
    have hnonneg : 0 ≤ (1 - τ_e) + ρ := by linarith
    nlinarith [sq_nonneg ρ]
  have h1τle1 : (1 - τ_e) ^ 2 ≤ 1 - τ_e := by
    nlinarith
  have hden_pos : 0 < 2 * (1 - τ_e) - ρ ^ 2 := by linarith
  rw [div_le_iff₀ hden_pos]
  have hrem1 : 0 ≤ ρ * (2 + ρ) * (1 - ρ - τ_e) := by
    have ha : 0 ≤ ρ * (2 + ρ) := by positivity
    have hb : 0 ≤ 1 - ρ - τ_e := by linarith
    exact mul_nonneg ha hb
  have hrem2 : 0 ≤ 2 * (τ_e - τ_o) * (1 - τ_e) := by
    have ha : 0 ≤ 2 * (τ_e - τ_o) := by linarith
    exact mul_nonneg ha (le_of_lt h1τ)
  have hid :
      (ρ + τ_e) * (2 * (1 - τ_e) - ρ ^ 2) - (ρ ^ 2 + 2 * τ_o * (1 - τ_e)) =
        ρ * (2 + ρ) * (1 - ρ - τ_e) + 2 * (τ_e - τ_o) * (1 - τ_e) := by
    ring
  linarith

/-- Symmetric `τ_o = 0` specialization of `recoilRatio`: stays at or below `ρ` whenever
`0 ≤ ρ`, `0 ≤ τ_e < 1`, and `ρ + τ_e ≤ 1`. -/
theorem recoilRatio_zero_le_rho {ρ τ_e : F} (hρ0 : 0 ≤ ρ) (hτe0 : 0 ≤ τ_e) (hτe1 : τ_e < 1)
    (hr : ρ + τ_e ≤ 1) :
    recoilRatio ρ τ_e 0 ≤ ρ := by
  have h2 : (2 : F) ≠ 0 := ne_of_gt two_pos
  have h1τ : 0 < 1 - τ_e := by linarith
  have h1τ0 : 1 - τ_e ≠ 0 := ne_of_gt h1τ
  rw [recoilRatio_eq h2 h1τ0]
  have hρle1τ : ρ ≤ 1 - τ_e := by linarith
  have hρle1 : ρ ≤ 1 := by linarith
  have hρsq : ρ ^ 2 ≤ (1 - τ_e) ^ 2 := by
    have hnonneg : 0 ≤ (1 - τ_e) + ρ := by linarith
    nlinarith [sq_nonneg ρ]
  have h1τle1 : (1 - τ_e) ^ 2 ≤ 1 - τ_e := by nlinarith
  have hden_pos : 0 < 2 * (1 - τ_e) - ρ ^ 2 := by linarith
  rw [div_le_iff₀ hden_pos]
  have hrem : 0 ≤ ρ * (2 * (1 - τ_e - ρ) + ρ * (1 - ρ)) := by
    have ha : 0 ≤ 1 - τ_e - ρ := by linarith
    have hb : 0 ≤ 1 - ρ := by linarith
    have hc : 0 ≤ 2 * (1 - τ_e - ρ) + ρ * (1 - ρ) := by
      exact add_nonneg (mul_nonneg (by positivity) ha) (mul_nonneg hρ0 hb)
    exact mul_nonneg hρ0 hc
  have hid :
      ρ * (2 * (1 - τ_e) - ρ ^ 2) - (ρ ^ 2 + 2 * 0 * (1 - τ_e)) =
        ρ * (2 * (1 - τ_e - ρ) + ρ * (1 - ρ)) := by
    ring
  linarith

end PerturbedSchurContraction

end PerturbedBlockSchur
