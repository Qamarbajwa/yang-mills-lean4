/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.PerturbedCocycleSchurBasin
import YangMillsBlueprint.MathlibStaging.MeasureBathtubFiberFloor
import YangMillsBlueprint.MathlibStaging.MultiscaleBalabanFlow
import Mathlib.Tactic.NormNum

/-!
# YM-175: Perturbed Cocycle Saturation & Iterated Schur Contraction Basin Certificate

Certifies:
1. Unconditional Stage-2A sharp dynamical dichotomies
   (`stage2a_cocycle_and_schur_thresholds_unconditional`):
   - Perturbed Bianchi cocycle finite hitting time vs. breakdown above `η > c / 4`.
   - Non-Markovian Schur all-level contraction basin vs. finite-step escape beyond
     `5 τ_e + 4 τ_o > 1`.
2. Conditional Stage-2A full crossover bridge (`stage2a_full_crossover_basin_conditional`) chaining
   Stage 1 (`YM173`) → Bathtub Haar fiber variance floor (`YM174`) → Perturbed cocycle saturation →
   All-level Schur contraction (`YM175`) → OS Hilbert exponential decay (`YM150`).
-/

namespace YangMillsBlueprint.Certificates

open AbstractPolymerCluster BlockPolymerOscillation LatticeHaarGibbs MeasureBathtubFiberFloor
open MeasureTheory MultiscaleBalabanFlow PerturbedCocycleSchurBasin SliceReflectionHilbert

/-- Certificate bundling Stage-2A cocycle defect and non-Markovian Schur basin parameters. -/
structure Stage2ABasinCert where
  c : ℝ
  η : ℝ
  δ₀ : ℝ
  δstar : ℝ
  τ_e : ℝ
  τ_o : ℝ
  haarFloor : ℝ
  hc0 : 0 < c
  hδ0 : 0 < δ₀
  hδle : δ₀ ≤ δstar
  hstar1 : δstar < 1
  hγ : 0 < c * min (δ₀ * (1 - δ₀)) (δstar * (1 - δstar)) - η
  hτe0 : 0 ≤ τ_e
  hτo0 : 0 ≤ τ_o
  hbasin : 5 * τ_e + 4 * τ_o < 1
  hfloor : 0 < haarFloor

/-- Canonical Stage-2A witness: `c = 1/2`, `η = 1/32 < 1/8`, `τ_e = τ_o = 1/16`
(`5 τ_e + 4 τ_o = 9/16 < 1`, `ρmid = 15/32 < 1`). -/
noncomputable def canonicalStage2ABasinCert : Stage2ABasinCert where
  c := 1 / 2
  η := 1 / 32
  δ₀ := 1 / 8
  δstar := 1 / 2
  τ_e := 1 / 16
  τ_o := 1 / 16
  haarFloor := 1
  hc0 := by norm_num
  hδ0 := by norm_num
  hδle := by norm_num
  hstar1 := by norm_num
  hγ := by norm_num
  hτe0 := by norm_num
  hτo0 := by norm_num
  hbasin := by norm_num
  hfloor := by norm_num

instance : Nonempty Stage2ABasinCert :=
  ⟨canonicalStage2ABasinCert⟩

/-- **UNCONDITIONAL:** Both sharp Stage-2A dynamical phase thresholds hold unconditionally for any
witness `cert` and adversarial comparator `(η_bad > c/4, 5 τ_e' + 4 τ_o' > 1)`: inside the basin,
the cocycle hits `δstar` in finitely many steps and all Schur iterates contract geometrically to
`ρfix < (1 - τ_e)/2 < 1`; beyond either threshold, escape occurs in finite steps. -/
theorem stage2a_cocycle_and_schur_thresholds_unconditional (cert : Stage2ABasinCert)
    (δ_good : ℕ → ℝ) (hinit : cert.δ₀ ≤ δ_good 0) (hlb : ∀ k, cert.δ₀ ≤ δ_good k)
    (hstepG : ∀ k, δ_good k ≤ cert.δstar →
      perturbedCocycleStep cert.c cert.η (δ_good k) ≤ δ_good (k + 1))
    (η_bad : ℝ) (hηbad : cert.c / 4 < η_bad) (δ_bad : ℕ → ℝ)
    (hstepB : ∀ k, δ_bad (k + 1) ≤ perturbedCocycleStep cert.c η_bad (δ_bad k))
    (τ_e' τ_o' ρ_bad : ℝ) (hτe1' : τ_e' < 1) (hesc : 1 < 5 * τ_e' + 4 * τ_o') :
    (∃ K : ℕ, cert.δstar ≤ δ_good K) ∧
      (∃ K_bad : ℕ, δ_bad K_bad < 0) ∧
      (∃ ρfix < (1 - cert.τ_e) / 2, 0 ≤ ρfix ∧
        schurIterMap cert.τ_e cert.τ_o ρfix = ρfix ∧
        (((1 - cert.τ_e) / 2 + ρfix) / (1 - cert.τ_e)) < 1 ∧
        ∀ ρ : ℝ, 0 ≤ ρ → ρ ≤ (1 - cert.τ_e) / 2 → ∀ n : ℕ,
          (schurIterMap cert.τ_e cert.τ_o)^[n] ρ ≤ (1 - cert.τ_e) / 2 ∧
          |(schurIterMap cert.τ_e cert.τ_o)^[n] ρ - ρfix| ≤
            (((1 - cert.τ_e) / 2 + ρfix) / (1 - cert.τ_e)) ^ n * |ρ - ρfix|) ∧
      (∃ n_esc : ℕ, 1 < (schurIterMap τ_e' τ_o')^[n_esc] ρ_bad) := by
  have hHit := exists_perturbed_cocycle_hitting_time cert.hc0 cert.hδle cert.hγ hinit hlb hstepG
  have hBrk := (perturbed_cocycle_breakdown_above_quarter cert.hc0 hηbad hstepB).2
  have hSchur := schurIterMap_strict_basin_of_five_four cert.hτe0 cert.hτo0 cert.hbasin
  rcases hSchur with ⟨_, _, _, hfix0, hfixLt, hfpt, hq, hiter⟩
  have hEsc := (schurIterMap_diverges_above_five_four hτe1' hesc ρ_bad).2
  refine ⟨hHit, hBrk, ⟨_, hfixLt, hfix0, hfpt, hq, ?_⟩, hEsc⟩
  intro ρ hρ0 hρmid n
  exact ⟨(hiter ρ hρ0 hρmid n).2.1, (hiter ρ hρ0 hρmid n).2.2⟩

/-- **CONDITIONAL:** End-to-end Stage-1 + Stage-2A crossover bridge: Stage 1's `K`- and `L`-uniform
oscillation (`YM173`) yields a strict measure-theoretic bathtub fiber floor (`YM174`); initializing
the Bianchi cocycle above `0` drives it past `δstar` in finitely many steps inside `η < c/4`; and
inside the non-Markovian Schur basin `5 τ_e + 4 τ_o < 1`, every OS transfer operator obeying the
coarse Schur contraction `(schurIterMap cert.τ_e cert.τ_o)^[n] ρ₀` exhibits strictly positive
exponential clustering `0 < Real.log (1 / ρmid)`. -/
theorem stage2a_full_crossover_basin_conditional {Ω H : Type*} [MeasurableSpace Ω]
    {ν : Measure Ω} [IsProbabilityMeasure ν] [NormedAddCommGroup H] [InnerProductSpace ℝ H]
    (cert : Stage2ABasinCert) (c_bt : ℝ) (d_bt : ℕ) (hcbt : 0 < c_bt) (hdbt : 0 < d_bt)
    {S f : Ω → ℝ} {vMin vMax : ℝ}
    (hA : MeasurableSet
      {y : Ω | f y < (1 / (2 * c_bt * Real.exp (vMax - vMin))) ^ ((2 : ℝ) / (d_bt : ℝ))})
    (hint : Integrable (expWeight S) ν) (hf : Integrable f ν)
    (hfw : Integrable (fun y => f y * expWeight S y) ν)
    (hf0 : ∀ y, 0 ≤ f y) (hmin : ∀ y, vMin ≤ S y) (hmax : ∀ y, S y ≤ vMax)
    (hvol : ν.real
      {y : Ω | f y < (1 / (2 * c_bt * Real.exp (vMax - vMin))) ^ ((2 : ℝ) / (d_bt : ℝ))} ≤
      c_bt * ((1 / (2 * c_bt * Real.exp (vMax - vMin))) ^ ((2 : ℝ) / (d_bt : ℝ))) ^
        ((d_bt : ℝ) / 2))
    (δ : ℕ → ℝ) (hinit : cert.δ₀ ≤ δ 0) (hlb : ∀ k, cert.δ₀ ≤ δ k)
    (hstep : ∀ k, δ k ≤ cert.δstar →
      perturbedCocycleStep cert.c cert.η (δ k) ≤ δ (k + 1))
    {T : H →ₗ[ℝ] H} {Ω_vac : H} (ρ₀ : ℝ) (n : ℕ)
    (hρ0 : 0 ≤ ρ₀) (hρmid : ρ₀ ≤ (1 - cert.τ_e) / 2)
    (hTvac : ‖Ω_vac‖ = 1) (hTfix : T Ω_vac = Ω_vac)
    (hTsymm : ∀ u v : H, inner ℝ u (T v) = inner ℝ (T u) v)
    (hTcon : ∀ ψ : H, inner ℝ Ω_vac ψ = 0 →
      ‖T ψ‖ ≤ ((schurIterMap cert.τ_e cert.τ_o)^[n] ρ₀) * ‖ψ‖)
    (u v : H) (hv : inner ℝ Ω_vac v = 0) (m : ℕ) :
    0 < (1 / 2 : ℝ) * (1 / (2 * c_bt * Real.exp (vMax - vMin))) ^ ((2 : ℝ) / (d_bt : ℝ)) ∧
      (1 / 2 : ℝ) * (1 / (2 * c_bt * Real.exp (vMax - vMin))) ^ ((2 : ℝ) / (d_bt : ℝ)) ≤
        weightedExpectation ν S f ∧
      (∃ K : ℕ, cert.δstar ≤ δ K) ∧
      (|inner ℝ u ((T ^ m) v)| ≤
          Real.exp (-(Real.log (1 / ((1 - cert.τ_e) / 2)) * (m : ℝ))) * (‖u‖ * ‖v‖) ∧
        0 < Real.log (1 / ((1 - cert.τ_e) / 2))) := by
  have hbase : 0 < 1 / (2 * c_bt * Real.exp (vMax - vMin)) := by positivity
  have hflPos :
      0 < (1 / 2 : ℝ) * (1 / (2 * c_bt * Real.exp (vMax - vMin))) ^ ((2 : ℝ) / (d_bt : ℝ)) :=
    mul_pos (by norm_num) (Real.rpow_pos_of_pos hbase _)
  have hbt := boltzmann_measure_bathtub_codim_d_floor hcbt hdbt hA hint hf hfw hf0 hmin hmax hvol
  have hHit := exists_perturbed_cocycle_hitting_time cert.hc0 cert.hδle cert.hγ hinit hlb hstep
  have hSchur := schurIterMap_strict_basin_of_five_four cert.hτe0 cert.hτo0 cert.hbasin
  rcases hSchur with ⟨hmid0, hmid1, _, _, _, _, _, hiter⟩
  have hnLe : (schurIterMap cert.τ_e cert.τ_o)^[n] ρ₀ ≤ (1 - cert.τ_e) / 2 :=
    (hiter ρ₀ hρ0 hρmid n).2.1
  have hCT : ContractiveTransfer T Ω_vac ((1 - cert.τ_e) / 2) :=
    { r_pos := hmid0
      r_lt_one := hmid1
      norm_vac := hTvac
      fixes_vac := hTfix
      symm := hTsymm
      contractive := fun ψ hψ => by
        have h1 := hTcon ψ hψ
        have h2 := mul_le_mul_of_nonneg_right hnLe (norm_nonneg ψ)
        exact le_trans h1 h2 }
  exact ⟨hflPos, hbt, hHit, transfer_correlator_exp_decay hCT u hv m⟩

end YangMillsBlueprint.Certificates
