/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.PerturbedBlockSchur
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# YM-158: Tail-Perturbed Block Schur Contraction & Gershgorin Invertibility Certificate

Certifies the Probe IV-2 non-Markovian block-Schur renormalization bounds:
- Matrix `ℓ^∞` Gershgorin odd/even block injectivity (`diag_dominant_mulVec_injective`),
- Calibrated non-Markovian witness `ρ = 3/5`, `τ_e = 3/10`, `τ_o = 0` with pre-Schur radius
  `r_tot = 9/10 < 1` contracting strictly to `perturbedRatioBound = 57/70 < 9/10` (`margin = 13/70`)
  and 1D recoil ratio `recoilRatio = 9/26`,
- Exact recovery of `YM147` (`BlockSchurHierarchy.blockRatioNext`) at `τ_e = τ_o = 0`.
-/

namespace YangMillsBlueprint.Certificates

open BlockSchurHierarchy PerturbedBlockSchur

/-- Real certificate bundling nearest-block coupling `ρ` and polymer tails `τ_e, τ_o`. -/
structure PerturbedBlockSchurCert where
  ρ : ℝ
  τ_e : ℝ
  τ_o : ℝ
  hρ0 : 0 < ρ
  hτe0 : 0 ≤ τ_e
  hτo0 : 0 ≤ τ_o
  hrtot : ρ + τ_e < 1
  hτo_le : τ_o ≤ τ_e
  hτo_contr : τ_o < ρ * (1 - τ_e - ρ) / (1 - τ_e)

/-- Probe IV-2 calibrated witness (`ρ = 3/5`, `τ_e = 3/10`, `τ_o = 0`, `r_tot = 9/10`). -/
noncomputable def canonicalPerturbedBlockSchurCert : PerturbedBlockSchurCert where
  ρ := 3 / 5
  τ_e := 3 / 10
  τ_o := 0
  hρ0 := by norm_num
  hτe0 := by norm_num
  hτo0 := by norm_num
  hrtot := by norm_num
  hτo_le := by norm_num
  hτo_contr := by norm_num

instance : Nonempty PerturbedBlockSchurCert :=
  ⟨canonicalPerturbedBlockSchurCert⟩

/-- **UNCONDITIONAL:** Exact rational evaluation of the canonical Probe IV-2 witness:
`r_tot = 9/10`, `perturbedRatioBound = 57/70 < 9/10`, `perturbedMarginNext = 13/70`, and
`recoilRatio = 9/26`. -/
theorem canonical_perturbed_schur_eval :
    canonicalPerturbedBlockSchurCert.ρ + canonicalPerturbedBlockSchurCert.τ_e = 9 / 10 ∧
      perturbedRatioBound canonicalPerturbedBlockSchurCert.ρ canonicalPerturbedBlockSchurCert.τ_e
        canonicalPerturbedBlockSchurCert.τ_o = 57 / 70 ∧
      perturbedMarginNext canonicalPerturbedBlockSchurCert.ρ canonicalPerturbedBlockSchurCert.τ_e
        canonicalPerturbedBlockSchurCert.τ_o = 13 / 70 ∧
      recoilRatio canonicalPerturbedBlockSchurCert.ρ canonicalPerturbedBlockSchurCert.τ_e
        canonicalPerturbedBlockSchurCert.τ_o = 9 / 26 ∧
      perturbedRatioBound canonicalPerturbedBlockSchurCert.ρ canonicalPerturbedBlockSchurCert.τ_e
        canonicalPerturbedBlockSchurCert.τ_o <
        canonicalPerturbedBlockSchurCert.ρ + canonicalPerturbedBlockSchurCert.τ_e := by
  dsimp [canonicalPerturbedBlockSchurCert, perturbedRatioBound, perturbedMarginNext, recoilRatio]
  norm_num

/-- **CONDITIONAL:** Assuming Stage 2 multi-scale polymer bounds yield strictly diagonally
dominant even blocks `M_ee` (`0 < rowGershgorinMargin M_ee i`) and tail parameters satisfying
`PerturbedBlockSchurCert`, even-block multiplication is injective, the coarse Schur margin strictly
grows past `1 - (ρ + τ_e)`, the effective coupling contracts strictly below `ρ + τ_e`, and the
1D recoil ratio stays bounded by `ρ + τ_e` while recovering `YM147` at `τ_e = τ_o = 0`. -/
theorem perturbed_schur_tail_contraction_conditional {n : ℕ}
    (cert : PerturbedBlockSchurCert) (M_ee : Matrix (Fin n) (Fin n) ℝ)
    (hdom : ∀ i : Fin n, 0 < rowGershgorinMargin M_ee i) :
    Function.Injective M_ee.mulVec ∧
      1 - (cert.ρ + cert.τ_e) < perturbedMarginNext cert.ρ cert.τ_e cert.τ_o ∧
      perturbedRatioBound cert.ρ cert.τ_e cert.τ_o < cert.ρ + cert.τ_e ∧
      recoilRatio cert.ρ cert.τ_e cert.τ_o ≤ cert.ρ + cert.τ_e ∧
      recoilRatio cert.ρ 0 0 = blockRatioNext cert.ρ := by
  have hinj : Function.Injective M_ee.mulVec := diag_dominant_mulVec_injective M_ee hdom
  have hmargin :
      1 - (cert.ρ + cert.τ_e) < perturbedMarginNext cert.ρ cert.τ_e cert.τ_o :=
    perturbedMarginNext_gt_margin cert.hρ0 cert.hrtot cert.hτo_contr
  have hratio : perturbedRatioBound cert.ρ cert.τ_e cert.τ_o < cert.ρ + cert.τ_e :=
    perturbedRatioBound_lt_tot cert.hρ0 cert.hrtot cert.hτo_contr
  have hτe1 : cert.τ_e < 1 := by linarith [cert.hρ0, cert.hrtot]
  have hrecoil : recoilRatio cert.ρ cert.τ_e cert.τ_o ≤ cert.ρ + cert.τ_e :=
    recoilRatio_le_self (le_of_lt cert.hρ0) cert.hτe0 hτe1 cert.hτo_le (le_of_lt cert.hrtot)
  have hym147 : recoilRatio cert.ρ 0 0 = blockRatioNext cert.ρ :=
    recoilRatio_recovers_ym147 (by norm_num)
  exact ⟨hinj, hmargin, hratio, hrecoil, hym147⟩

end YangMillsBlueprint.Certificates
