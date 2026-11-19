/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.Archimedean.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Algebra.Order.Field.Basic

/-!
# YM-177: Two-Step Inductive RG Remainder Contraction & Basin Entry Certificate

Formalizes the discrete two-variable inductive renormalization-group contraction lemma
bridging 1-step `2^4`-fiber paramagnetic Schur dominance (`YM176`) to multi-step
blocking trajectories `(β_k, ε_k)`:
  `β_{k+1} = β_k - c_para · δ_k + r_k`,
  `ε_{k+1} ≤ θ_Schur · ε_k + C_fluct · β_k^{-2}`.

Unconditional theorems:
1. `remainder_trap_invariant_unconditional`: Whenever `0 ≤ θ < 1`, `C_fluct ≥ 0`,
   `β_basin > 0`, `ε_k ≤ ε_max := C_fluct / (β_basin^2 * (1 - θ))`, and `β_k ≥ β_basin`,
   the next remainder satisfies `ε_{k+1} ≤ ε_max`.
2. `strict_coupling_descent_step_unconditional`: Under positive paramagnetic drift
   `c_para · δ_min - M_rem · ε_max = η_net > 0`, every blocking step in the UV band
   `β_k ≥ β_basin` strictly decreases the effective coupling by at least `η_net`.
3. `inductive_rg_basin_entry_unconditional`: Any trajectory starting at arbitrarily large
   UV coupling `β_0` with `ε_0 ≤ ε_max` enters the strong-contraction crossover basin
   `β_{k*} < β_basin` in `k* = O(β_0)` steps (`(k* : ℝ) * η_net ≤ β_0 - β_basin + η_net`)
   while maintaining `ε_k ≤ ε_max` uniformly for all `k ≤ k*`.
-/

namespace YangMillsBlueprint.Certificates

structure TwoStepInductiveRGCert where
  thetaSchur : ℝ
  cFluct : ℝ
  betaBasin : ℝ
  cPara : ℝ
  deltaMin : ℝ
  mRem : ℝ
  hTheta0 : 0 ≤ thetaSchur
  hTheta1 : thetaSchur < 1
  hFluct : 0 ≤ cFluct
  hBasin : 0 < betaBasin
  hCPara : 0 < cPara
  hDelta : 0 < deltaMin
  hMRem : 0 ≤ mRem

noncomputable def canonicalTwoStepInductiveRGCert : TwoStepInductiveRGCert where
  thetaSchur := 1 / 2
  cFluct := 1 / 10
  betaBasin := 23 / 10
  cPara := 301 / 1000
  deltaMin := 1 / 2
  mRem := 1
  hTheta0 := by norm_num
  hTheta1 := by norm_num
  hFluct := by norm_num
  hBasin := by norm_num
  hCPara := by norm_num
  hDelta := by norm_num
  hMRem := by norm_num

instance : Nonempty TwoStepInductiveRGCert :=
  ⟨canonicalTwoStepInductiveRGCert⟩

/-- **UNCONDITIONAL:** Uniform polymer remainder trap invariance in the UV-to-crossover band
`β_k ≥ β_basin > 0`. If `0 ≤ θ < 1`, `C_fluct ≥ 0`, and `ε_k ≤ C_fluct / (β_basin^2 * (1 - θ))`,
then `ε_{k+1} ≤ θ * ε_k + C_fluct / β_k^2 ≤ C_fluct / (β_basin^2 * (1 - θ))`. -/
theorem remainder_trap_invariant_unconditional
    (theta c_fluct beta_basin beta_k eps_k eps_next : ℝ)
    (hTheta0 : 0 ≤ theta) (hTheta1 : theta < 1) (hFluct : 0 ≤ c_fluct)
    (hBasin : 0 < beta_basin) (hBeta : beta_basin ≤ beta_k)
    (hEps : eps_k ≤ c_fluct / (beta_basin ^ 2 * (1 - theta)))
    (hStep : eps_next ≤ theta * eps_k + c_fluct / beta_k ^ 2) :
    eps_next ≤ c_fluct / (beta_basin ^ 2 * (1 - theta)) := by
  have h1mT : 0 < 1 - theta := by linarith
  have hBasin2 : 0 < beta_basin ^ 2 := sq_pos_of_pos hBasin
  have hBk2 : beta_basin ^ 2 ≤ beta_k ^ 2 :=
    sq_le_sq' (by linarith) hBeta
  have hInv : c_fluct / beta_k ^ 2 ≤ c_fluct / beta_basin ^ 2 :=
    div_le_div_of_nonneg_left hFluct hBasin2 hBk2
  have hMul : theta * eps_k ≤ theta * (c_fluct / (beta_basin ^ 2 * (1 - theta))) :=
    mul_le_mul_of_nonneg_left hEps hTheta0
  have hId :
      theta * (c_fluct / (beta_basin ^ 2 * (1 - theta))) + c_fluct / beta_basin ^ 2 =
        c_fluct / (beta_basin ^ 2 * (1 - theta)) := by
    have hBasin2ne : beta_basin ^ 2 ≠ 0 := ne_of_gt hBasin2
    have h1mTne : 1 - theta ≠ 0 := ne_of_gt h1mT
    field_simp [hBasin2ne, h1mTne]
    ring
  linarith

/-- **UNCONDITIONAL:** Strict coupling descent per RG step whenever the paramagnetic cocycle
drift `c_para · δ_k` dominates the bounded polymer remainder perturbation `|r_k| ≤ M_rem · ε_max`. -/
theorem strict_coupling_descent_step_unconditional
    (beta_k delta_k r_k c_para delta_min m_rem eps_max : ℝ)
    (hCPara : 0 < c_para) (hDelta : delta_min ≤ delta_k)
    (hRem : r_k ≤ m_rem * eps_max) :
    beta_k - c_para * delta_k + r_k ≤ beta_k - (c_para * delta_min - m_rem * eps_max) := by
  have hMul : c_para * delta_min ≤ c_para * delta_k :=
    mul_le_mul_of_nonneg_left hDelta (le_of_lt hCPara)
  linarith

/-- **UNCONDITIONAL:** Finite-time crossover basin entry (`k* = O(β_0)`) with uniform polymer
remainder bound along the entire RG trajectory. -/
theorem inductive_rg_basin_entry_unconditional
    (beta eps : ℕ → ℝ) (theta c_fluct beta_basin eta_net : ℝ)
    (hTheta0 : 0 ≤ theta) (hTheta1 : theta < 1) (hFluct : 0 ≤ c_fluct)
    (hBasin : 0 < beta_basin) (hEta : 0 < eta_net)
    (hEps0 : eps 0 ≤ c_fluct / (beta_basin ^ 2 * (1 - theta)))
    (hStep : ∀ k : ℕ, beta_basin ≤ beta k →
      eps (k + 1) ≤ theta * eps k + c_fluct / (beta k) ^ 2 ∧
      beta (k + 1) ≤ beta k - eta_net) :
    ∃ k_star : ℕ,
      beta k_star < beta_basin ∧
      (k_star : ℝ) * eta_net ≤ max (beta 0 - beta_basin) 0 + eta_net ∧
      ∀ k : ℕ, k ≤ k_star → eps k ≤ c_fluct / (beta_basin ^ 2 * (1 - theta)) := by
  classical
  let eps_max : ℝ := c_fluct / (beta_basin ^ 2 * (1 - theta))
  have hPrefix : ∀ n : ℕ,
      (∀ j : ℕ, j < n → beta_basin ≤ beta j) →
      eps n ≤ eps_max ∧ beta n ≤ beta 0 - (n : ℝ) * eta_net := by
    intro n
    induction n with
    | zero =>
      intro _
      refine ⟨hEps0, ?_⟩
      simp
    | succ m ih =>
      intro hAll
      have hPrev := ih (fun j hj => hAll j (Nat.lt_succ_of_lt hj))
      have hmBasin : beta_basin ≤ beta m := hAll m (Nat.lt_succ_self m)
      obtain ⟨hEpsStep, hBetaStep⟩ := hStep m hmBasin
      have hEpsNext : eps (m + 1) ≤ eps_max :=
        remainder_trap_invariant_unconditional theta c_fluct beta_basin (beta m) (eps m)
          (eps (m + 1)) hTheta0 hTheta1 hFluct hBasin hmBasin hPrev.1 hEpsStep
      have hBetaNext : beta (m + 1) ≤ beta 0 - ((m + 1 : ℕ) : ℝ) * eta_net := by
        have hCast : ((m + 1 : ℕ) : ℝ) * eta_net = (m : ℝ) * eta_net + eta_net := by
          push_cast
          ring
        linarith [hPrev.2, hBetaStep, hCast]
      exact ⟨hEpsNext, hBetaNext⟩
  obtain ⟨K, hK⟩ := exists_nat_gt ((max (beta 0 - beta_basin) 0) / eta_net)
  have hKmul : max (beta 0 - beta_basin) 0 < (K : ℝ) * eta_net :=
    (div_lt_iff₀ hEta).1 hK
  have hExists : ∃ k : ℕ, beta k < beta_basin := by
    by_contra hNo
    push Not at hNo
    have hKbound := (hPrefix K (fun j _ => hNo j)).2
    have hNoK : beta_basin ≤ beta K := hNo K
    have hMax : beta 0 - beta_basin ≤ max (beta 0 - beta_basin) 0 := le_max_left _ _
    linarith
  let k_star : ℕ := Nat.find hExists
  have hkHit : beta k_star < beta_basin := Nat.find_spec hExists
  have hkMin : ∀ j : ℕ, j < k_star → beta_basin ≤ beta j := by
    intro j hj
    exact le_of_not_gt (Nat.find_min hExists hj)
  have hkStep : k_star ≤ K := by
    by_contra hGt
    have hLt : K < k_star := Nat.lt_of_not_le hGt
    have hKbound := (hPrefix K (fun j hj => hkMin j (lt_trans hj hLt))).2
    have hNoK : beta_basin ≤ beta K := hkMin K hLt
    have hMax : beta 0 - beta_basin ≤ max (beta 0 - beta_basin) 0 := le_max_left _ _
    linarith
  have hkTime : (k_star : ℝ) * eta_net ≤ max (beta 0 - beta_basin) 0 + eta_net := by
    rcases Nat.eq_zero_or_pos k_star with hk0 | hkPos
    · rw [hk0]
      simp only [Nat.cast_zero, zero_mul]
      linarith [le_max_right (beta 0 - beta_basin) 0]
    · have hmLt : k_star - 1 < k_star := Nat.sub_lt hkPos Nat.zero_lt_one
      have hmBound := (hPrefix (k_star - 1) (fun j hj => hkMin j (lt_trans hj hmLt))).2
      have hmBasin : beta_basin ≤ beta (k_star - 1) := hkMin (k_star - 1) hmLt
      have hMax : beta 0 - beta_basin ≤ max (beta 0 - beta_basin) 0 := le_max_left _ _
      have hmCast : (k_star : ℝ) = ((k_star - 1 : ℕ) : ℝ) + 1 := by
        rw [← Nat.cast_add_one, Nat.sub_add_cancel hkPos]
      have hMul : (k_star : ℝ) * eta_net = ((k_star - 1 : ℕ) : ℝ) * eta_net + eta_net := by
        rw [hmCast]
        ring
      linarith
  refine ⟨k_star, hkHit, hkTime, ?_⟩
  intro k hkLe
  exact (hPrefix k (fun j hj => hkMin j (lt_of_lt_of_le hj hkLe))).1

end YangMillsBlueprint.Certificates
