/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.AbstractPolymerCluster
public import YangMillsBlueprint.MathlibStaging.BlockPolymerOscillation

/-!
# Multiscale `K`-Uniform Bałaban UV Flow, Counterterm Necessity & Collar Lifting

Formalizes the multiscale step-count uniformity of Stage 1 Bałaban UV renormalization across an
arbitrarily long UV trajectory `k = 0, ..., K` (`K(β₀) ~ O(β₀) → ∞` as lattice spacing `a → 0`):

* `invCoupling_backward_ge`: linear backward growth `β_* + δ_b * (K - k) ≤ β k`.
* `multiscale_irrelevant_sum_le`: subtracted `O(g_k^4) = O(1 / β_k²)` irrelevant operator errors
  telescope unconditionally below the `K`-independent cap `C_irr / (δ_b * β_*)`.
* `multiscale_large_field_sum_le`: cumulative large-field polymer weights `exp(-κ * β_k)` converge
  uniformly in `K` below a geometric ceiling.
* `harmonic_marginal_sum_ge_log` & `harmonic_marginal_sum_unbounded`: unsubtracted `O(g_k^2) =
  O(1 / β_k)` marginal/Faddeev-Popov terms diverge logarithmically as `K → ∞`, proving formally why
  running counterterm absorption is necessary to obtain a continuum-uniform Stage-1 measure.
-/

@[expose] public section

namespace MultiscaleBalabanFlow

open AbstractPolymerCluster BlockPolymerOscillation LatticeHaarGibbs MeasureTheory

section MultiscaleSummability

/-- Backward linear coupling lower bound `β_* + δ_b * (K - k) ≤ β k` along any decreasing
UV inverse-coupling flow with per-step drop `δ_b ≤ β k - β (k + 1)`. -/
theorem invCoupling_backward_ge (β : ℕ → ℝ) (K : ℕ) (βstar δ_b : ℝ)
    (hK : βstar ≤ β K) (hstep : ∀ k : ℕ, k < K → δ_b ≤ β k - β (k + 1)) :
    ∀ k : ℕ, k ≤ K → βstar + δ_b * ((K - k : ℕ) : ℝ) ≤ β k := by
  have hind : ∀ d k : ℕ, k + d = K → βstar + δ_b * (d : ℝ) ≤ β k := by
    intro d
    induction d with
    | zero =>
        intro k hk
        simp only [add_zero] at hk
        subst hk
        simpa using hK
    | succ d ih =>
        intro k hk
        have hklt : k < K := by omega
        have hih := ih (k + 1) (by omega)
        have hst := hstep k hklt
        push_cast
        linarith
  intro k hk
  exact hind (K - k) k (Nat.add_sub_of_le hk)

private theorem telescoping_inv_sq_sum_le_diff {c δ : ℝ} (hc : 0 < c) (hδ : 0 < δ) (K : ℕ) :
    (∑ m ∈ Finset.range K, 1 / (c + δ * ((m + 1 : ℕ) : ℝ)) ^ 2) ≤
      1 / (δ * c) - 1 / (δ * (c + δ * (K : ℝ))) := by
  induction K with
  | zero => simp
  | succ K ih =>
      rw [Finset.sum_range_succ]
      let u0 := c + δ * (K : ℝ)
      let u1 := c + δ * ((K + 1 : ℕ) : ℝ)
      have hu0 : 0 < u0 := by
        dsimp [u0]
        positivity
      have hu1 : 0 < u1 := by
        dsimp [u1]
        positivity
      have huDiff : u1 = u0 + δ := by
        dsimp [u0, u1]
        push_cast
        ring
      have hlt : u0 < u1 := by linarith
      have hterm : 1 / u1 ^ 2 ≤ 1 / (δ * u0) - 1 / (δ * u1) := by
        have hdiffEq : 1 / (δ * u0) - 1 / (δ * u1) = 1 / (u0 * u1) := by
          rw [huDiff]
          field_simp [ne_of_gt hδ, ne_of_gt hu0, ne_of_gt (show 0 < u0 + δ by linarith)]
          ring
        rw [hdiffEq]
        refine one_div_le_one_div_of_le (mul_pos hu0 hu1) ?_
        have hle : u0 * u1 ≤ u1 * u1 := mul_le_mul_of_nonneg_right hlt.le hu1.le
        simpa [sq] using hle
      dsimp [u0, u1] at hterm
      push_cast at ih hterm ⊢
      linarith

/-- Strict `K`-independent telescoping upper bound for subtracted `O(g_k^4)` sums. -/
theorem telescoping_inv_sq_sum_lt {c δ : ℝ} (hc : 0 < c) (hδ : 0 < δ) (K : ℕ) :
    (∑ m ∈ Finset.range K, 1 / (c + δ * ((m + 1 : ℕ) : ℝ)) ^ 2) < 1 / (δ * c) := by
  have hle := telescoping_inv_sq_sum_le_diff hc hδ K
  have hrem : 0 < 1 / (δ * (c + δ * (K : ℝ))) := by positivity
  linarith

/-- Uniform `K`-independent cap on subtracted `O(1 / β_k²)` irrelevant-operator accumulations. -/
theorem multiscale_irrelevant_sum_le (β : ℕ → ℝ) (K : ℕ) {βstar δ_b C_irr : ℝ}
    (hβ0 : 0 < βstar) (hδ0 : 0 < δ_b) (hC : 0 ≤ C_irr)
    (hK : βstar ≤ β K) (hstep : ∀ k : ℕ, k < K → δ_b ≤ β k - β (k + 1)) :
    (∑ k ∈ Finset.range K, C_irr / (β k) ^ 2) ≤ C_irr / (δ_b * βstar) := by
  rw [← Finset.sum_range_reflect (fun k => C_irr / (β k) ^ 2) K]
  have hterm : ∀ m ∈ Finset.range K,
      C_irr / (β (K - 1 - m)) ^ 2 ≤
        C_irr * (1 / (βstar + δ_b * ((m + 1 : ℕ) : ℝ)) ^ 2) := by
    intro m hm
    rw [Finset.mem_range] at hm
    have hkLe : K - 1 - m ≤ K := by omega
    have hdiff : K - (K - 1 - m) = m + 1 := by omega
    have hlb := invCoupling_backward_ge β K βstar δ_b hK hstep (K - 1 - m) hkLe
    rw [hdiff] at hlb
    have hposL : 0 < βstar + δ_b * ((m + 1 : ℕ) : ℝ) := by positivity
    have hsq : (βstar + δ_b * ((m + 1 : ℕ) : ℝ)) ^ 2 ≤ (β (K - 1 - m)) ^ 2 :=
      pow_le_pow_left₀ hposL.le hlb 2
    have hdiv := div_le_div_of_nonneg_left hC (sq_pos_of_pos hposL) hsq
    rwa [mul_one_div]
  have hsum1 := Finset.sum_le_sum hterm
  rw [← Finset.mul_sum] at hsum1
  have htel := (telescoping_inv_sq_sum_lt hβ0 hδ0 K).le
  have hmul := mul_le_mul_of_nonneg_left htel hC
  have heq : C_irr * (1 / (δ_b * βstar)) = C_irr / (δ_b * βstar) := by ring
  linarith

/-- Uniform `K`-independent cap on cumulative large-field polymer weights `C_lf * exp(-κ * β_k)`. -/
theorem multiscale_large_field_sum_le (β : ℕ → ℝ) (K : ℕ) {βstar δ_b κ C_lf : ℝ}
    (hδ0 : 0 < δ_b) (hκ : 0 < κ) (hC : 0 ≤ C_lf)
    (hK : βstar ≤ β K) (hstep : ∀ k : ℕ, k < K → δ_b ≤ β k - β (k + 1)) :
    (∑ k ∈ Finset.range K, C_lf * Real.exp (-(κ * β k))) ≤
      C_lf * Real.exp (-(κ * βstar)) *
        polymerTailBound 1 (Real.exp (-(κ * δ_b))) := by
  rw [← Finset.sum_range_reflect (fun k => C_lf * Real.exp (-(κ * β k))) K]
  have hterm : ∀ m ∈ Finset.range K,
      C_lf * Real.exp (-(κ * β (K - 1 - m))) ≤
        (C_lf * Real.exp (-(κ * βstar))) * (1 * (Real.exp (-(κ * δ_b))) ^ (m + 1)) := by
    intro m hm
    rw [Finset.mem_range] at hm
    have hkLe : K - 1 - m ≤ K := by omega
    have hdiff : K - (K - 1 - m) = m + 1 := by omega
    have hlb := invCoupling_backward_ge β K βstar δ_b hK hstep (K - 1 - m) hkLe
    rw [hdiff] at hlb
    have hexp :
        Real.exp (-(κ * β (K - 1 - m))) ≤
          Real.exp (-(κ * (βstar + δ_b * ((m + 1 : ℕ) : ℝ)))) := by
      apply Real.exp_le_exp.mpr
      nlinarith
    have hsplit :
        Real.exp (-(κ * (βstar + δ_b * ((m + 1 : ℕ) : ℝ)))) =
          Real.exp (-(κ * βstar)) * (Real.exp (-(κ * δ_b))) ^ (m + 1) := by
      have harg :
          -(κ * (βstar + δ_b * ((m + 1 : ℕ) : ℝ))) =
            -(κ * βstar) + ((m + 1 : ℕ) : ℝ) * (-(κ * δ_b)) := by ring
      rw [harg, Real.exp_add, ← Real.exp_nat_mul]
    rw [hsplit] at hexp
    have hmul := mul_le_mul_of_nonneg_left hexp hC
    linarith
  have hsum1 :
      (∑ m ∈ Finset.range K, C_lf * Real.exp (-(κ * β (K - 1 - m)))) ≤
        (C_lf * Real.exp (-(κ * βstar))) *
          ∑ m ∈ Finset.range K, 1 * (Real.exp (-(κ * δ_b))) ^ (m + 1) := by
    rw [Finset.mul_sum]
    exact Finset.sum_le_sum hterm
  have hθ0 : 0 ≤ Real.exp (-(κ * δ_b)) := (Real.exp_pos _).le
  have hθ1 : Real.exp (-(κ * δ_b)) < 1 := Real.exp_lt_one_iff.mpr (by nlinarith)
  have hgeom := finset_geom_tail_le_polymerTailBound (C := (1 : ℝ)) (θ := Real.exp (-(κ * δ_b)))
    (by norm_num) hθ0 hθ1 K
  have hpre0 : 0 ≤ C_lf * Real.exp (-(κ * βstar)) := mul_nonneg hC (Real.exp_pos _).le
  exact le_trans hsum1 (mul_le_mul_of_nonneg_left hgeom hpre0)

/-- Logarithmic lower bound on unsubtracted `O(g_k^2) = O(1 / β_k)` harmonic sums. -/
theorem harmonic_marginal_sum_ge_log {c δ : ℝ} (hc : 0 < c) (hδ : 0 < δ) (K : ℕ) :
    Real.log ((c + δ * ((K + 1 : ℕ) : ℝ)) / (c + δ)) / δ ≤
      ∑ m ∈ Finset.range K, 1 / (c + δ * ((m + 1 : ℕ) : ℝ)) := by
  have hind : ∀ N : ℕ,
      Real.log ((c + δ * ((N + 1 : ℕ) : ℝ)) / (c + δ)) ≤
        δ * ∑ m ∈ Finset.range N, 1 / (c + δ * ((m + 1 : ℕ) : ℝ)) := by
    intro N
    induction N with
    | zero =>
        simp only [zero_add, Nat.cast_one, mul_one, div_self (by linarith : c + δ ≠ 0),
          Real.log_one, Finset.range_zero, Finset.sum_empty, mul_zero, le_refl]
    | succ N ih =>
        rw [Finset.sum_range_succ, mul_add]
        let uN := c + δ * ((N + 1 : ℕ) : ℝ)
        let uNext := c + δ * ((N + 1 + 1 : ℕ) : ℝ)
        have huN : 0 < uN := by
          dsimp [uN]
          positivity
        have huNext : 0 < uNext := by
          dsimp [uNext]
          positivity
        have hstep :
            Real.log (uNext / uN) ≤ δ * (1 / uN) := by
          have hdiv : uNext / uN = 1 + δ / uN := by
            dsimp [uN, uNext]
            push_cast
            field_simp [ne_of_gt huN]
            ring
          rw [hdiv]
          have hpos : 0 < 1 + δ / uN := by positivity
          have hlog := Real.log_le_sub_one_of_pos hpos
          have heq : 1 + δ / uN - 1 = δ * (1 / uN) := by ring
          linarith
        have hlogAdd :
            Real.log (uNext / (c + δ)) =
              Real.log (uN / (c + δ)) + Real.log (uNext / uN) := by
          have hcd : 0 < c + δ := by linarith
          have hprod : uNext / (c + δ) = (uN / (c + δ)) * (uNext / uN) := by
            field_simp [ne_of_gt hcd, ne_of_gt huN]
          rw [hprod, Real.log_mul (div_pos huN hcd).ne' (div_pos huNext huN).ne']
        dsimp [uN, uNext] at ih hstep hlogAdd ⊢
        linarith
  exact (div_le_iff₀ hδ).mpr (by rw [mul_comm _ δ]; exact hind K)

/-- Unsubtracted `O(g_k^2)` marginal/FP sums grow without bound as `K → ∞`. -/
theorem harmonic_marginal_sum_unbounded {c δ : ℝ} (hc : 0 < c) (hδ : 0 < δ) (M : ℝ) :
    ∃ K : ℕ, M < ∑ m ∈ Finset.range K, 1 / (c + δ * ((m + 1 : ℕ) : ℝ)) := by
  have hcd : 0 < c + δ := by linarith
  let target := (c + δ) * Real.exp (max (δ * M) 0 + 1)
  obtain ⟨K, hK⟩ := exists_nat_gt (target / δ)
  refine ⟨K, ?_⟩
  have h1 : target < δ * (K : ℝ) := (div_lt_iff₀' hδ).mp hK
  have h2 : target < c + δ * ((K + 1 : ℕ) : ℝ) := by
    push_cast
    linarith
  have hdiv : Real.exp (max (δ * M) 0 + 1) < (c + δ * ((K + 1 : ℕ) : ℝ)) / (c + δ) := by
    rw [lt_div_iff₀ hcd]
    simpa [target, mul_comm] using h2
  have hlog : max (δ * M) 0 + 1 < Real.log ((c + δ * ((K + 1 : ℕ) : ℝ)) / (c + δ)) := by
    have := Real.log_lt_log (Real.exp_pos _) hdiv
    simpa [Real.log_exp] using this
  have hMlt : δ * M < Real.log ((c + δ * ((K + 1 : ℕ) : ℝ)) / (c + δ)) := by
    have : δ * M ≤ max (δ * M) 0 := le_max_left _ _
    linarith
  have hdivM : M < Real.log ((c + δ * ((K + 1 : ℕ) : ℝ)) / (c + δ)) / δ :=
    (lt_div_iff₀' hδ).mpr hMlt
  exact lt_of_lt_of_le hdivM (harmonic_marginal_sum_ge_log hc hδ K)

end MultiscaleSummability

section MultiscaleEffectiveEnvelope

/-- Uniform Stage-1 accumulated effective action oscillation independent of both RG depth `K`
and exterior volume `L`. -/
noncomputable def multiscaleEffectiveOsc
    (B_core C_irr C_lf βstar δ_b κ collarCap : ℝ) : ℝ :=
  B_core + 2 * (C_irr / (δ_b * βstar)) +
    2 * (C_lf * Real.exp (-(κ * βstar)) * polymerTailBound 1 (Real.exp (-(κ * δ_b)))) +
    2 * collarCap

theorem multiscaleEffectiveOsc_nonneg {B_core C_irr C_lf βstar δ_b κ collarCap : ℝ}
    (hB : 0 ≤ B_core) (hCirr : 0 ≤ C_irr) (hClf : 0 ≤ C_lf)
    (hβ : 0 < βstar) (hδ : 0 < δ_b) (hκ : 0 < κ) (hcol : 0 ≤ collarCap) :
    0 ≤ multiscaleEffectiveOsc B_core C_irr C_lf βstar δ_b κ collarCap := by
  unfold multiscaleEffectiveOsc
  have hθ0 : 0 ≤ Real.exp (-(κ * δ_b)) := (Real.exp_pos _).le
  have hθ1 : Real.exp (-(κ * δ_b)) < 1 := Real.exp_lt_one_iff.mpr (by nlinarith)
  have htail := polymerTailBound_nonneg (C := (1 : ℝ)) (θ := Real.exp (-(κ * δ_b)))
    (by norm_num) hθ0 hθ1
  have h1 : 0 ≤ C_irr / (δ_b * βstar) := by positivity
  have h2 : 0 ≤ C_lf * Real.exp (-(κ * βstar)) *
      polymerTailBound 1 (Real.exp (-(κ * δ_b))) :=
    mul_nonneg (mul_nonneg hClf (Real.exp_pos _).le) htail
  linarith

end MultiscaleEffectiveEnvelope

end MultiscaleBalabanFlow
