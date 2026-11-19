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
public import YangMillsBlueprint.MathlibStaging.PerturbedBlockSchur
public import YangMillsBlueprint.MathlibStaging.SliceReflectionHilbert

/-!
# Perturbed Cocycle Saturation & Iterated Non-Markovian Block Schur Basin

Formalizes the sharp Stage-2A discrete dynamical thresholds governing `E-CROSSOVER`:

* **Part A — Perturbed Bianchi Cocycle Dynamics (`c_corr`, `η`):**
  `perturbedCocycleStep c η δ := δ + c * δ * (1 - δ) - η`.
  Proves geometric decay `1 - δ_k ≤ (1 - δ₀) (1 - c δ₀)^k` at `η = 0`, finite-step saturation
  `δstar ≤ δ K` whenever the defect remains below `c * min (δ₀(1-δ₀)) (δstar(1-δstar))`, and
  sharp breakdown below `0` whenever `η > c / 4`.
* **Part B — Iterated Non-Markovian Block Schur Contraction (`5 τ_e + 4 τ_o < 1`):**
  `schurIterMap τ_e τ_o ρ := τ_e + τ_o + ρ ^ 2 / (1 - τ_e)` (matching `PerturbedBlockSchur`).
  Proves all-level invariance inside `[0, ρstar]`, explicit fixed point `0 ≤ ρfix < (1 - τ_e)/2`
  and geometric contraction `|ρ_n - ρfix| ≤ q^n |ρ₀ - ρfix|` (`q < 1`) throughout the sharp basin
  `5 τ_e + 4 τ_o < 1`, plus unconditional finite-step escape past `1` whenever `5 τ_e + 4 τ_o > 1`.
-/

@[expose] public section

namespace PerturbedCocycleSchurBasin

open Filter PerturbedBlockSchur SliceReflectionHilbert Topology

section PerturbedCocycle

/-- One dyadic step of the Bianchi cocycle with additive cross-correlation defect `-η`. -/
def perturbedCocycleStep (c η δ : ℝ) : ℝ :=
  δ + c * δ * (1 - δ) - η

/-- Exact unperturbed complement factorization `1 - δ' = (1 - δ) * (1 - c * δ)`. -/
theorem one_sub_unperturbedCocycleStep (c δ : ℝ) :
    1 - perturbedCocycleStep c 0 δ = (1 - δ) * (1 - c * δ) := by
  unfold perturbedCocycleStep
  ring

/-- Monotone floor and geometric saturation rate for unperturbed (`η = 0`) cocycle trajectories. -/
theorem cocycle_unperturbed_decay_le {c δ₀ : ℝ} {δ : ℕ → ℝ}
    (hδ0 : 0 < δ₀) (hδ1 : δ₀ ≤ 1) (hc0 : 0 < c) (hc1 : c ≤ 1)
    (hinit : δ₀ ≤ δ 0) (hle1 : ∀ k, δ k ≤ 1)
    (hstep : ∀ k, perturbedCocycleStep c 0 (δ k) ≤ δ (k + 1)) :
    ∀ k : ℕ, δ₀ ≤ δ k ∧ 1 - δ k ≤ (1 - δ₀) * (1 - c * δ₀) ^ k := by
  intro k
  induction k with
  | zero =>
      refine ⟨hinit, ?_⟩
      simp only [pow_zero, mul_one]
      linarith
  | succ k ih =>
      rcases ih with ⟨ihLo, ihGap⟩
      have h1k : 0 ≤ 1 - δ k := sub_nonneg.mpr (hle1 k)
      have hposDelta : 0 < δ k := lt_of_lt_of_le hδ0 ihLo
      have hstepK := hstep k
      have hgrow : 0 ≤ c * δ k * (1 - δ k) := by positivity
      have hloNext : δ₀ ≤ δ (k + 1) := by
        unfold perturbedCocycleStep at hstepK
        linarith
      have h1cδ : 0 ≤ 1 - c * δ₀ := by
        have hmul : c * δ₀ ≤ 1 * 1 := mul_le_mul hc1 hδ1 hδ0.le (by norm_num)
        linarith
      have hck : 1 - c * δ k ≤ 1 - c * δ₀ := by
        have := mul_le_mul_of_nonneg_left ihLo hc0.le
        linarith
      have hcomp : 1 - δ (k + 1) ≤ (1 - δ k) * (1 - c * δ k) := by
        rw [← one_sub_unperturbedCocycleStep]
        linarith
      have hstepGap : (1 - δ k) * (1 - c * δ k) ≤ (1 - δ₀) * (1 - c * δ₀) ^ (k + 1) := by
        calc (1 - δ k) * (1 - c * δ k)
            ≤ (1 - δ k) * (1 - c * δ₀) := mul_le_mul_of_nonneg_left hck h1k
          _ ≤ ((1 - δ₀) * (1 - c * δ₀) ^ k) * (1 - c * δ₀) :=
              mul_le_mul_of_nonneg_right ihGap h1cδ
          _ = (1 - δ₀) * (1 - c * δ₀) ^ (k + 1) := by rw [pow_succ]; ring
      exact ⟨hloNext, le_trans hcomp hstepGap⟩

/-- Any unperturbed cocycle trajectory exceeds every threshold `δstar < 1` for large `k`. -/
theorem exists_unperturbed_cocycle_saturation {c δ₀ δstar : ℝ} {δ : ℕ → ℝ}
    (hδ0 : 0 < δ₀) (hδ1 : δ₀ ≤ 1) (hc0 : 0 < c) (hc1 : c ≤ 1) (hstar : δstar < 1)
    (hinit : δ₀ ≤ δ 0) (hle1 : ∀ k, δ k ≤ 1)
    (hstep : ∀ k, perturbedCocycleStep c 0 (δ k) ≤ δ (k + 1)) :
    ∃ K : ℕ, ∀ k : ℕ, K ≤ k → δstar ≤ δ k := by
  have h1c0 : 0 ≤ 1 - c * δ₀ := by
    have hmul : c * δ₀ ≤ 1 * 1 := mul_le_mul hc1 hδ1 hδ0.le (by norm_num)
    linarith
  have h1c1 : 1 - c * δ₀ < 1 := by
    have hpos : 0 < c * δ₀ := mul_pos hc0 hδ0
    linarith
  have htend : Tendsto (fun k : ℕ => (1 - δ₀) * (1 - c * δ₀) ^ k) atTop (𝓝 0) := by
    have hpow := tendsto_pow_atTop_nhds_zero_of_lt_one h1c0 h1c1
    simpa using tendsto_const_nhds.mul hpow
  have hgapPos : 0 < 1 - δstar := sub_pos.mpr hstar
  have hev := htend.eventually (gt_mem_nhds hgapPos)
  rw [eventually_atTop] at hev
  obtain ⟨K, hK⟩ := hev
  refine ⟨K, fun k hk => ?_⟩
  have hdec := (cocycle_unperturbed_decay_le hδ0 hδ1 hc0 hc1 hinit hle1 hstep k).2
  have hlt := hK k hk
  linarith

private theorem quad_min_le_on_interval {δ₀ δstar u : ℝ}
    (hlo : δ₀ ≤ u) (hhi : u ≤ δstar) :
    min (δ₀ * (1 - δ₀)) (δstar * (1 - δstar)) ≤ u * (1 - u) := by
  by_cases heq : δ₀ = δstar
  · have hu : u = δ₀ := le_antisymm (heq ▸ hhi) hlo
    rw [hu, heq]
    exact min_le_right _ _
  · have hlt : δ₀ < δstar := lt_of_le_of_ne (le_trans hlo hhi) heq
    have hdiff : 0 < δstar - δ₀ := sub_pos.mpr hlt
    have hu1 : 0 ≤ u - δ₀ := sub_nonneg.mpr hlo
    have hu2 : 0 ≤ δstar - u := sub_nonneg.mpr hhi
    let m := min (δ₀ * (1 - δ₀)) (δstar * (1 - δstar))
    have hm1 : m ≤ δ₀ * (1 - δ₀) := min_le_left _ _
    have hm2 : m ≤ δstar * (1 - δstar) := min_le_right _ _
    have hid :
        (δstar - δ₀) * (u * (1 - u)) -
            ((δstar - u) * (δ₀ * (1 - δ₀)) + (u - δ₀) * (δstar * (1 - δstar))) =
          (δstar - δ₀) * (u - δ₀) * (δstar - u) := by
      ring
    have hrem : 0 ≤ (δstar - δ₀) * (u - δ₀) * (δstar - u) := by positivity
    have hlin : (δstar - u) * m + (u - δ₀) * m = (δstar - δ₀) * m := by ring
    have hmul :
        (δstar - δ₀) * m ≤
          (δstar - u) * (δ₀ * (1 - δ₀)) + (u - δ₀) * (δstar * (1 - δstar)) := by
      have ha : (δstar - u) * m ≤ (δstar - u) * (δ₀ * (1 - δ₀)) :=
        mul_le_mul_of_nonneg_left hm1 hu2
      have hb : (u - δ₀) * m ≤ (u - δ₀) * (δstar * (1 - δstar)) :=
        mul_le_mul_of_nonneg_left hm2 hu1
      linarith
    nlinarith

/-- Finite hitting-time bound for perturbed cocycle trajectories with bounded cross-correlation
defect `η < c * min (δ₀ * (1 - δ₀)) (δstar * (1 - δstar))`. -/
theorem exists_perturbed_cocycle_hitting_time {c η δ₀ δstar : ℝ} {δ : ℕ → ℝ}
    (hc : 0 < c) (_hδle : δ₀ ≤ δstar)
    (hγ : 0 < c * min (δ₀ * (1 - δ₀)) (δstar * (1 - δstar)) - η)
    (hinit : δ₀ ≤ δ 0) (hlb : ∀ k, δ₀ ≤ δ k)
    (hstep : ∀ k, δ k ≤ δstar → perturbedCocycleStep c η (δ k) ≤ δ (k + 1)) :
    ∃ K : ℕ, δstar ≤ δ K := by
  let γ : ℝ := c * min (δ₀ * (1 - δ₀)) (δstar * (1 - δstar)) - η
  by_contra hnot
  push Not at hnot
  have hind : ∀ k : ℕ, δ₀ + (k : ℝ) * γ ≤ δ k := by
    intro k
    induction k with
    | zero => simpa using hinit
    | succ k ih =>
        have hklt : δ k < δstar := hnot k
        have hq := quad_min_le_on_interval (hlb k) hklt.le
        have hcq : c * min (δ₀ * (1 - δ₀)) (δstar * (1 - δstar)) ≤ c * (δ k * (1 - δ k)) :=
          mul_le_mul_of_nonneg_left hq hc.le
        have hst := hstep k hklt.le
        have hup : δ k + γ ≤ δ (k + 1) := by
          unfold perturbedCocycleStep at hst
          dsimp [γ] at *
          linarith
        push_cast
        linarith
  obtain ⟨K, hK⟩ := exists_nat_gt ((δstar - δ₀) / γ)
  have hKmul : δstar - δ₀ < (K : ℝ) * γ := by
    have h := (div_lt_iff₀ hγ).mp hK
    linarith
  have hhit := hind K
  linarith [hnot K]

/-- **SHARP BREAKDOWN THRESHOLD (`η > c / 4`):** No cocycle step can remain above `δ - (η - c/4)`
when the adversarial cross-correlation defect exceeds `c / 4`, forcing escape below `0`. -/
theorem perturbed_cocycle_step_le_of_above_quarter {c η : ℝ} (hc : 0 < c) (δ : ℝ) :
    perturbedCocycleStep c η δ ≤ δ - (η - c / 4) := by
  have hsq : 0 ≤ c * (δ - 1 / 2) ^ 2 := mul_nonneg hc.le (sq_nonneg _)
  have hid :
      (δ - (η - c / 4)) - perturbedCocycleStep c η δ = c * (δ - 1 / 2) ^ 2 := by
    unfold perturbedCocycleStep
    ring
  linarith

theorem perturbed_cocycle_breakdown_above_quarter {c η : ℝ} {δ : ℕ → ℝ}
    (hc : 0 < c) (hη : c / 4 < η)
    (hstep : ∀ k, δ (k + 1) ≤ perturbedCocycleStep c η (δ k)) :
    (∀ k : ℕ, δ k ≤ δ 0 - (k : ℝ) * (η - c / 4)) ∧ ∃ K : ℕ, δ K < 0 := by
  have hdec : ∀ k : ℕ, δ k ≤ δ 0 - (k : ℝ) * (η - c / 4) := by
    intro k
    induction k with
    | zero => simp
    | succ k ih =>
        have h1 := hstep k
        have h2 := perturbed_cocycle_step_le_of_above_quarter (η := η) hc (δ k)
        push_cast
        linarith
  have hpos : 0 < η - c / 4 := sub_pos.mpr hη
  obtain ⟨K, hK⟩ := exists_nat_gt (δ 0 / (η - c / 4))
  have hKmul : δ 0 < (K : ℝ) * (η - c / 4) := (div_lt_iff₀ hpos).mp hK
  exact ⟨hdec, K, by linarith [hdec K]⟩

end PerturbedCocycle

section IteratedSchurBasin

/-- Discrete Schur recursion `ρ ↦ τ_e + τ_o + ρ^2 / (1 - τ_e)` from `YM158`. -/
noncomputable def schurIterMap (τ_e τ_o ρ : ℝ) : ℝ :=
  τ_e + τ_o + ρ ^ 2 / (1 - τ_e)

private theorem schurIterMap_sub_eq {τ_e τ_o x y : ℝ} (hden : 1 - τ_e ≠ 0) :
    schurIterMap τ_e τ_o x - schurIterMap τ_e τ_o y =
      ((x + y) / (1 - τ_e)) * (x - y) := by
  unfold schurIterMap
  field_simp [hden]
  ring

theorem schurIterMap_eq_perturbedRatioBound (τ_e τ_o ρ : ℝ) :
    schurIterMap τ_e τ_o ρ = perturbedRatioBound ρ τ_e τ_o :=
  rfl

theorem schurIterMap_nonneg {τ_e τ_o : ℝ} (hτe0 : 0 ≤ τ_e) (hτe1 : τ_e < 1)
    (hτo0 : 0 ≤ τ_o) (ρ : ℝ) :
    0 ≤ schurIterMap τ_e τ_o ρ := by
  unfold schurIterMap
  have hden : 0 < 1 - τ_e := sub_pos.mpr hτe1
  positivity

theorem schurIterMap_mono {τ_e τ_o ρ₁ ρ₂ : ℝ} (hτe1 : τ_e < 1) (h0 : 0 ≤ ρ₁) (hle : ρ₁ ≤ ρ₂) :
    schurIterMap τ_e τ_o ρ₁ ≤ schurIterMap τ_e τ_o ρ₂ := by
  unfold schurIterMap
  have hden : 0 < 1 - τ_e := sub_pos.mpr hτe1
  have hsq : ρ₁ ^ 2 ≤ ρ₂ ^ 2 := pow_le_pow_left₀ h0 hle 2
  linarith [div_le_div_of_nonneg_right hsq hden.le]

/-- All iterates of `schurIterMap` stay inside any trapping interval `[0, ρstar]`. -/
theorem schurIterMap_iter_basin_invariant {τ_e τ_o ρstar ρ : ℝ}
    (hτe0 : 0 ≤ τ_e) (hτe1 : τ_e < 1) (hτo0 : 0 ≤ τ_o)
    (htrap : schurIterMap τ_e τ_o ρstar ≤ ρstar) (hρ0 : 0 ≤ ρ) (hρstar : ρ ≤ ρstar) :
    ∀ n : ℕ, 0 ≤ (schurIterMap τ_e τ_o)^[n] ρ ∧ (schurIterMap τ_e τ_o)^[n] ρ ≤ ρstar := by
  intro n
  induction n with
  | zero => exact ⟨hρ0, hρstar⟩
  | succ n ih =>
      rcases ih with ⟨ih0, ihStar⟩
      rw [Function.iterate_succ_apply']
      exact ⟨schurIterMap_nonneg hτe0 hτe1 hτo0 _,
        le_trans (schurIterMap_mono hτe1 ih0 ihStar) htrap⟩

/-- Geometric fixed-point contraction on `[0, ρstar]` with factor
`q = (ρstar + ρfix) / (1 - τ_e)`. -/
theorem schurIterMap_iter_contraction {τ_e τ_o ρstar ρfix ρ : ℝ}
    (hτe0 : 0 ≤ τ_e) (hτe1 : τ_e < 1) (hτo0 : 0 ≤ τ_o)
    (htrap : schurIterMap τ_e τ_o ρstar ≤ ρstar)
    (hfix0 : 0 ≤ ρfix) (hfpt : schurIterMap τ_e τ_o ρfix = ρfix)
    (hρ0 : 0 ≤ ρ) (hρstar : ρ ≤ ρstar) :
    ∀ n : ℕ,
      |(schurIterMap τ_e τ_o)^[n] ρ - ρfix| ≤
        ((ρstar + ρfix) / (1 - τ_e)) ^ n * |ρ - ρfix| := by
  have hden : 0 < 1 - τ_e := sub_pos.mpr hτe1
  have hinv := schurIterMap_iter_basin_invariant hτe0 hτe1 hτo0 htrap hρ0 hρstar
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
      rw [Function.iterate_succ_apply']
      rcases hinv n with ⟨hn0, hnStar⟩
      have hdiff :
          schurIterMap τ_e τ_o ((schurIterMap τ_e τ_o)^[n] ρ) - ρfix =
            (((schurIterMap τ_e τ_o)^[n] ρ + ρfix) / (1 - τ_e)) *
              ((schurIterMap τ_e τ_o)^[n] ρ - ρfix) := by
        have hsub := schurIterMap_sub_eq (τ_e := τ_e) (τ_o := τ_o)
          (x := (schurIterMap τ_e τ_o)^[n] ρ) (y := ρfix) (ne_of_gt hden)
        rwa [hfpt] at hsub
      have hnonneg : 0 ≤ ((schurIterMap τ_e τ_o)^[n] ρ + ρfix) / (1 - τ_e) := by
        have := add_nonneg hn0 hfix0
        exact div_nonneg this hden.le
      have hq :
          ((schurIterMap τ_e τ_o)^[n] ρ + ρfix) / (1 - τ_e) ≤
            (ρstar + ρfix) / (1 - τ_e) :=
        div_le_div_of_nonneg_right (add_le_add hnStar le_rfl) hden.le
      calc
        |schurIterMap τ_e τ_o ((schurIterMap τ_e τ_o)^[n] ρ) - ρfix|
            = |((schurIterMap τ_e τ_o)^[n] ρ + ρfix) / (1 - τ_e)| *
                |(schurIterMap τ_e τ_o)^[n] ρ - ρfix| := by
              rw [hdiff, abs_mul]
        _ = (((schurIterMap τ_e τ_o)^[n] ρ + ρfix) / (1 - τ_e)) *
              |(schurIterMap τ_e τ_o)^[n] ρ - ρfix| := by
              rw [abs_of_nonneg hnonneg]
        _ ≤ ((ρstar + ρfix) / (1 - τ_e)) *
              (((ρstar + ρfix) / (1 - τ_e)) ^ n * |ρ - ρfix|) :=
              mul_le_mul hq ih (abs_nonneg _) (le_trans hnonneg hq)
        _ = ((ρstar + ρfix) / (1 - τ_e)) ^ (n + 1) * |ρ - ρfix| := by
              rw [pow_succ]; ring

/-- **EXACT SCHUR CONTRACTION THRESHOLD (`5 * τ_e + 4 * τ_o < 1`):**
Inside the critical boundary `5 τ_e + 4 τ_o < 1`, midpoint `ρmid := (1 - τ_e) / 2` is strictly
trapped (`schurIterMap τ_e τ_o ρmid < ρmid < 1`), there exists an explicit fixed point
`0 ≤ ρfix < ρmid`, and every trajectory starting in `[0, ρmid]` contracts geometrically to `ρfix`
with contraction factor `q := (ρmid + ρfix) / (1 - τ_e) < 1`. -/
theorem schurIterMap_strict_basin_of_five_four {τ_e τ_o : ℝ}
    (hτe0 : 0 ≤ τ_e) (hτo0 : 0 ≤ τ_o) (hbasin : 5 * τ_e + 4 * τ_o < 1) :
    let ρmid : ℝ := (1 - τ_e) / 2
    let disc : ℝ := (1 - τ_e) * (1 - 5 * τ_e - 4 * τ_o)
    let ρfix : ℝ := ((1 - τ_e) - Real.sqrt disc) / 2
    let q : ℝ := (ρmid + ρfix) / (1 - τ_e)
    0 < ρmid ∧ ρmid < 1 ∧ schurIterMap τ_e τ_o ρmid < ρmid ∧
      0 ≤ ρfix ∧ ρfix < ρmid ∧ schurIterMap τ_e τ_o ρfix = ρfix ∧ q < 1 ∧
      ∀ ρ : ℝ, 0 ≤ ρ → ρ ≤ ρmid → ∀ n : ℕ,
        0 ≤ (schurIterMap τ_e τ_o)^[n] ρ ∧ (schurIterMap τ_e τ_o)^[n] ρ ≤ ρmid ∧
          |(schurIterMap τ_e τ_o)^[n] ρ - ρfix| ≤ q ^ n * |ρ - ρfix| := by
  have hτe1 : τ_e < 1 := by linarith
  have hden : 0 < 1 - τ_e := sub_pos.mpr hτe1
  let ρmid : ℝ := (1 - τ_e) / 2
  let disc : ℝ := (1 - τ_e) * (1 - 5 * τ_e - 4 * τ_o)
  let ρfix : ℝ := ((1 - τ_e) - Real.sqrt disc) / 2
  let q : ℝ := (ρmid + ρfix) / (1 - τ_e)
  have h15 : 0 < 1 - 5 * τ_e - 4 * τ_o := by linarith
  have hdiscPos : 0 < disc := mul_pos hden h15
  have hsqrtPos : 0 < Real.sqrt disc := Real.sqrt_pos.mpr hdiscPos
  have hdiscLe : disc ≤ (1 - τ_e) ^ 2 := by
    dsimp [disc]
    have hrem : (1 - τ_e) ^ 2 - (1 - τ_e) * (1 - 5 * τ_e - 4 * τ_o) =
        4 * (1 - τ_e) * (τ_e + τ_o) := by ring
    have hpos : 0 ≤ 4 * (1 - τ_e) * (τ_e + τ_o) := by positivity
    linarith
  have hsqrtLe : Real.sqrt disc ≤ 1 - τ_e := by
    have := Real.sqrt_le_sqrt hdiscLe
    rwa [Real.sqrt_sq hden.le] at this
  have hmid0 : 0 < ρmid := by dsimp [ρmid]; linarith
  have hmid1 : ρmid < 1 := by dsimp [ρmid]; linarith
  have htrap : schurIterMap τ_e τ_o ρmid < ρmid := by
    dsimp [ρmid, schurIterMap]
    have hid :
        ((1 - τ_e) / 2) - (τ_e + τ_o + ((1 - τ_e) / 2) ^ 2 / (1 - τ_e)) =
          (1 - 5 * τ_e - 4 * τ_o) / 4 := by
      field_simp [ne_of_gt hden]
      ring
    linarith
  have hfix0 : 0 ≤ ρfix := by dsimp [ρfix]; linarith
  have hfixLt : ρfix < ρmid := by dsimp [ρfix, ρmid]; linarith
  have hfpt : schurIterMap τ_e τ_o ρfix = ρfix := by
    unfold schurIterMap
    dsimp [ρfix]
    have hsq : Real.sqrt disc ^ 2 = disc := Real.sq_sqrt hdiscPos.le
    field_simp [ne_of_gt hden]
    nlinarith [hsq]
  have hq : q < 1 := by
    dsimp [q]
    rw [div_lt_one hden]
    have h2mid : ρmid + ρmid = 1 - τ_e := by
      dsimp [ρmid]
      ring
    linarith
  refine ⟨hmid0, hmid1, htrap, hfix0, hfixLt, hfpt, hq, fun ρ hρ0 hρmid n => ?_⟩
  have hinv := schurIterMap_iter_basin_invariant hτe0 hτe1 hτo0 htrap.le hρ0 hρmid n
  have hcon := schurIterMap_iter_contraction hτe0 hτe1 hτo0 htrap.le hfix0 hfpt hρ0 hρmid n
  exact ⟨hinv.1, hinv.2, hcon⟩

/-- **SHARP ESCAPE THRESHOLD (`5 * τ_e + 4 * τ_o > 1`):** Beyond `5 * τ_e + 4 * τ_o = 1`,
every Schur step advances by at least `ε := (5 * τ_e + 4 * τ_o - 1) / 4 > 0`, forcing every
starting coupling `ρ` to exceed `1` in finitely many iterations. -/
theorem schurIterMap_diverges_above_five_four {τ_e τ_o : ℝ}
    (hτe1 : τ_e < 1) (hesc : 1 < 5 * τ_e + 4 * τ_o) (ρ : ℝ) :
    let ε : ℝ := (5 * τ_e + 4 * τ_o - 1) / 4
    (∀ n : ℕ, ρ + (n : ℝ) * ε ≤ (schurIterMap τ_e τ_o)^[n] ρ) ∧
      ∃ n : ℕ, 1 < (schurIterMap τ_e τ_o)^[n] ρ := by
  have hden : 0 < 1 - τ_e := sub_pos.mpr hτe1
  let ε : ℝ := (5 * τ_e + 4 * τ_o - 1) / 4
  have hε : 0 < ε := by dsimp [ε]; linarith
  have hstep : ∀ x : ℝ, x + ε ≤ schurIterMap τ_e τ_o x := fun x => by
    have hid :
        schurIterMap τ_e τ_o x - (x + ε) = (x - (1 - τ_e) / 2) ^ 2 / (1 - τ_e) := by
      unfold schurIterMap
      dsimp [ε]
      field_simp [ne_of_gt hden]
      ring
    have hnn : 0 ≤ (x - (1 - τ_e) / 2) ^ 2 / (1 - τ_e) := by positivity
    linarith
  have hind : ∀ n : ℕ, ρ + (n : ℝ) * ε ≤ (schurIterMap τ_e τ_o)^[n] ρ := by
    intro n
    induction n with
    | zero => simp
    | succ n ih =>
        rw [Function.iterate_succ_apply']
        have hnxt := hstep ((schurIterMap τ_e τ_o)^[n] ρ)
        push_cast
        linarith
  obtain ⟨N, hN⟩ := exists_nat_gt ((1 - ρ) / ε)
  have hNmul : 1 - ρ < (N : ℝ) * ε := (div_lt_iff₀ hε).mp hN
  exact ⟨hind, N, by linarith [hind N]⟩

end IteratedSchurBasin

end PerturbedCocycleSchurBasin
