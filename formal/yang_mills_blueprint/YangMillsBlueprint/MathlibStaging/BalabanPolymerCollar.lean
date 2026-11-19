/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.BlockPolymerOscillation
public import YangMillsBlueprint.MathlibStaging.PerturbedBlockSchur

/-!
# Stage 1 Balaban Small-Field Polymer Collar and Faddeev-Popov Jacobian Bounds

Formalizes the constructive UV renormalization cluster-expansion and Faddeev-Popov bounds
supporting `Stage 1 (E-UV-RG)` up to the crossover scale `ℓ_cross(β)`:

* `BalabanPolymerCollar.kp_geometric_sum_le`: Kotecky-Preiss cluster convergence bound
  `∑ n < N, q ^ (n + 1) ≤ a` from `q / (1 - q) ≤ a`.
* `BalabanPolymerCollar.kpCollarTail_anti`: exponential boundary-collar decay in distance `d`.
* `BalabanPolymerCollar.fp_matrix_injective`: unconditional small-field Faddeev-Popov
  invertibility (`Function.Injective (1 - E).mulVec`) whenever `‖E‖_∞ ≤ ε < 1`.
* `BalabanPolymerCollar.fp_abs_log_prod_le`: Faddeev-Popov log-determinant oscillation bound
  `|Real.log (∏ i, λ i)| ≤ (m : ℝ) * (-Real.log (1 - ε))`.
-/

@[expose] public section

namespace BalabanPolymerCollar

open BlockPolymerOscillation Matrix PerturbedBlockSchur

section KoteckyPreissCollar

/-- Kotecky-Preiss single-polymer weighted activity `z * K * exp a`. -/
noncomputable def kpActivity (z K a : ℝ) : ℝ :=
  z * K * Real.exp a

/-- Exponential boundary-collar remainder envelope at lattice block distance `d`:
`q ^ d / (1 - q)`. -/
noncomputable def kpCollarTail (q : ℝ) (d : ℕ) : ℝ :=
  q ^ d / (1 - q)

/-- Uniform small-field Faddeev-Popov log-determinant cap `(m : ℝ) * (-Real.log (1 - ε))`. -/
noncomputable def fpLogDetCap (m : ℕ) (ε : ℝ) : ℝ :=
  (m : ℝ) * (-Real.log (1 - ε))

/-- Effective Stage-1 blocked oscillation combining interior capacity, symmetric Faddeev-Popov
Jacobian log-det fluctuation, and boundary Kotecky-Preiss polymer tail. -/
noncomputable def balabanEffectiveOsc (B_int : ℝ) (m : ℕ) (ε C θ : ℝ) : ℝ :=
  B_int + 2 * fpLogDetCap m ε + 2 * polymerTailBound C θ

theorem kp_geometric_sum_le {q a : ℝ} (hq0 : 0 ≤ q) (hq1 : q < 1)
    (hkp : q / (1 - q) ≤ a) (N : ℕ) :
    (∑ n ∈ Finset.range N, q ^ (n + 1)) ≤ a := by
  have h1 := finset_geom_tail_le_polymerTailBound (C := (1 : ℝ)) (θ := q)
    (by norm_num) hq0 hq1 N
  have h1' : (∑ n ∈ Finset.range N, q ^ (n + 1)) ≤ q / (1 - q) := by
    simpa [polymerTailBound] using h1
  exact le_trans h1' hkp

theorem kpCollarTail_anti {q : ℝ} (hq0 : 0 ≤ q) (hq1 : q ≤ 1) {d₁ d₂ : ℕ} (hd : d₁ ≤ d₂) :
    kpCollarTail q d₂ ≤ kpCollarTail q d₁ := by
  unfold kpCollarTail
  rcases eq_or_lt_of_le hq1 with rfl | hlt
  · simp
  · have hpos : 0 < 1 - q := sub_pos.mpr hlt
    have hpow : q ^ d₂ ≤ q ^ d₁ := pow_le_pow_of_le_one hq0 hq1 hd
    exact div_le_div_of_nonneg_right hpow (le_of_lt hpos)

theorem kpCollarTail_nonneg {q : ℝ} (hq0 : 0 ≤ q) (hq1 : q < 1) (d : ℕ) :
    0 ≤ kpCollarTail q d := by
  unfold kpCollarTail
  have hpos : 0 < 1 - q := sub_pos.mpr hq1
  exact div_nonneg (pow_nonneg hq0 d) (le_of_lt hpos)

end KoteckyPreissCollar

section FaddeevPopovBounds

/-- Unconditional small-field Faddeev-Popov row-dominance and injectivity for `1 - E`
whenever every row `ℓ^1` norm of the perturbation `E` is at most `ε < 1`. -/
theorem fp_matrix_injective {m : ℕ} (E : Matrix (Fin m) (Fin m) ℝ) {ε : ℝ}
    (hε : ε < 1) (hE : ∀ i : Fin m, (∑ j : Fin m, |E i j|) ≤ ε) :
    (∀ i : Fin m, 1 - ε ≤ rowGershgorinMargin (1 - E) i) ∧
      Function.Injective (1 - E).mulVec := by
  have hmargin : ∀ i : Fin m, 1 - ε ≤ rowGershgorinMargin (1 - E) i := by
    intro i
    have hoff : offDiagAbsSum (1 - E) i = ∑ j ∈ Finset.univ.erase i, |E i j| := by
      unfold offDiagAbsSum
      refine Finset.sum_congr rfl ?_
      intro j hj
      have hne : j ≠ i := Finset.ne_of_mem_erase hj
      simp [Matrix.sub_apply, Matrix.one_apply_ne' hne]
    have hsplit : |E i i| + ∑ j ∈ Finset.univ.erase i, |E i j| = ∑ j : Fin m, |E i j| :=
      Finset.add_sum_erase Finset.univ (fun j => |E i j|) (Finset.mem_univ i)
    have hdiag : 1 - |E i i| ≤ |(1 - E) i i| := by
      rw [Matrix.sub_apply, Matrix.one_apply_eq]
      have htri : |(1 : ℝ)| ≤ |1 - E i i| + |E i i| := by
        simpa [sub_add_cancel] using abs_add_le (1 - E i i) (E i i)
      simp only [abs_one] at htri
      linarith
    unfold rowGershgorinMargin
    rw [hoff]
    linarith [hE i]
  have hdom : ∀ i : Fin m, 0 < rowGershgorinMargin (1 - E) i := by
    intro i
    have h1ε : 0 < 1 - ε := sub_pos.mpr hε
    exact lt_of_lt_of_le h1ε (hmargin i)
  exact ⟨hmargin, diag_dominant_mulVec_injective (1 - E) hdom⟩

/-- Elementary log envelope `log (1 + ε) ≤ -log (1 - ε)` on `[0, 1)`. -/
theorem log_one_add_le_neg_log_one_sub {ε : ℝ} (hε0 : 0 ≤ ε) (hε1 : ε < 1) :
    Real.log (1 + ε) ≤ -Real.log (1 - ε) := by
  have h1m : 0 < 1 - ε := sub_pos.mpr hε1
  have h1p : 0 < 1 + ε := by linarith
  have hinv : 1 + ε ≤ (1 - ε)⁻¹ := by
    rw [← one_div, le_div_iff₀ h1m]
    have hsq : 1 - ε ^ 2 ≤ 1 := by linarith [sq_nonneg ε]
    have hmul : (1 + ε) * (1 - ε) = 1 - ε ^ 2 := by ring
    linarith
  calc
    Real.log (1 + ε) ≤ Real.log ((1 - ε)⁻¹) := Real.log_le_log h1p hinv
    _ = -Real.log (1 - ε) := Real.log_inv (1 - ε)

private theorem finset_prod_le_prod_nonneg {m : ℕ} (u v : Fin m → ℝ)
    (hu : ∀ i : Fin m, 0 ≤ u i) (huv : ∀ i : Fin m, u i ≤ v i) :
    (∏ i : Fin m, u i) ≤ ∏ i : Fin m, v i := by
  classical
  have hind : ∀ s : Finset (Fin m),
      0 ≤ (∏ i ∈ s, u i) ∧ (∏ i ∈ s, u i) ≤ ∏ i ∈ s, v i := by
    intro s
    induction s using Finset.induction with
    | empty => simp
    | @insert a s ha ih =>
        rw [Finset.prod_insert ha, Finset.prod_insert ha]
        exact ⟨mul_nonneg (hu a) ih.1,
          mul_le_mul (huv a) ih.2 ih.1 (le_trans (hu a) (huv a))⟩
  exact (hind Finset.univ).2

/-- Determinant product enclosure for positive small-field eigenvalues `1 - ε ≤ ev i ≤ 1 + ε`. -/
theorem fp_prod_det_bounds {m : ℕ} (ev : Fin m → ℝ) {ε : ℝ}
    (hε1 : ε < 1) (hev : ∀ i : Fin m, 1 - ε ≤ ev i ∧ ev i ≤ 1 + ε) :
    (1 - ε) ^ m ≤ (∏ i : Fin m, ev i) ∧ (∏ i : Fin m, ev i) ≤ (1 + ε) ^ m := by
  have hlo0 : ∀ i : Fin m, 0 ≤ 1 - ε := fun _ => sub_nonneg.mpr (le_of_lt hε1)
  have hlo : (∏ _i : Fin m, (1 - ε)) ≤ ∏ i : Fin m, ev i :=
    finset_prod_le_prod_nonneg (fun _ => 1 - ε) ev hlo0 fun i => (hev i).1
  have hhi0 : ∀ i : Fin m, 0 ≤ ev i := fun i => le_trans (hlo0 i) (hev i).1
  have hhi : (∏ i : Fin m, ev i) ≤ ∏ _i : Fin m, (1 + ε) :=
    finset_prod_le_prod_nonneg ev (fun _ => 1 + ε) hhi0 fun i => (hev i).2
  simp only [Finset.prod_const, Finset.card_fin] at hlo hhi
  exact ⟨hlo, hhi⟩

/-- Uniform Stage-1 Faddeev-Popov log-determinant bound
`|Real.log (∏ i, ev i)| ≤ (m : ℝ) * (-Real.log (1 - ε))`. -/
theorem fp_abs_log_prod_le {m : ℕ} (ev : Fin m → ℝ) {ε : ℝ}
    (hε0 : 0 ≤ ε) (hε1 : ε < 1) (hev : ∀ i : Fin m, 1 - ε ≤ ev i ∧ ev i ≤ 1 + ε) :
    |Real.log (∏ i : Fin m, ev i)| ≤ fpLogDetCap m ε := by
  have h1m : 0 < 1 - ε := sub_pos.mpr hε1
  have hpowLo : 0 < (1 - ε) ^ m := pow_pos h1m m
  obtain ⟨hlo, hhi⟩ := fp_prod_det_bounds ev hε1 hev
  have hprodPos : 0 < ∏ i : Fin m, ev i := lt_of_lt_of_le hpowLo hlo
  have hlogLo : (m : ℝ) * Real.log (1 - ε) ≤ Real.log (∏ i : Fin m, ev i) := by
    calc
      (m : ℝ) * Real.log (1 - ε) = Real.log ((1 - ε) ^ m) := (Real.log_pow (1 - ε) m).symm
      _ ≤ Real.log (∏ i : Fin m, ev i) := Real.log_le_log hpowLo hlo
  have hlogHi : Real.log (∏ i : Fin m, ev i) ≤ (m : ℝ) * (-Real.log (1 - ε)) := by
    have hlogU : Real.log (∏ i : Fin m, ev i) ≤ (m : ℝ) * Real.log (1 + ε) := by
      calc
        Real.log (∏ i : Fin m, ev i) ≤ Real.log ((1 + ε) ^ m) := Real.log_le_log hprodPos hhi
        _ = (m : ℝ) * Real.log (1 + ε) := Real.log_pow (1 + ε) m
    have hcmp : (m : ℝ) * Real.log (1 + ε) ≤ (m : ℝ) * (-Real.log (1 - ε)) :=
      mul_le_mul_of_nonneg_left (log_one_add_le_neg_log_one_sub hε0 hε1) (Nat.cast_nonneg m)
    exact le_trans hlogU hcmp
  unfold fpLogDetCap
  exact abs_le.mpr ⟨by linarith, hlogHi⟩

end FaddeevPopovBounds

end BalabanPolymerCollar
