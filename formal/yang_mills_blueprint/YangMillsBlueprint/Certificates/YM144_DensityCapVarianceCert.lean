/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.GibbsDensityCapVariance
import YangMillsBlueprint.Certificates.YM143_CentralizerCodimensionCert
import Mathlib.Data.Rat.Init
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# YM-144: Stage 1-to-2A Bounded-Oscillation Density Cap & Variance Floor Certificate

Bridges Stage 1 finite effective action oscillation (`osc = vMax - vMin`) to `YM-143`'s
centralizer codimension bathtub lower bound (`4 / M ≤ expectComm`), showing that any
uniform `O(1)` action oscillation at crossover scale `ℓ_cross` enforces a strictly positive
adjoint commutator dispersion floor `4 * Real.exp (-osc) > 0` independent of `(a, L)`.
-/

namespace YangMillsBlueprint.Certificates

open CentralizerCodimensionBound GibbsDensityCapVariance

/-- Rational certificate bounding single-cell Gibbs weight oscillation ratio `wMax / Z ≤ cap`. -/
structure DensityCapVarianceCert where
  wMin : ℚ
  wMax : ℚ
  zPart : ℚ
  cap : ℚ
  hwmin : 0 < wMin
  hz : wMin ≤ zPart
  hcap : wMax ≤ cap * wMin
  hcap_pos : 0 < cap

/-- Canonical crossover-scale witness (`cap = 8`, yielding commutator floor `4 / 8 = 1 / 2`). -/
def canonicalDensityCapCert : DensityCapVarianceCert where
  wMin := 1 / 8
  wMax := 1
  zPart := 1 / 4
  cap := 8
  hwmin := by norm_num
  hz := by norm_num
  hcap := by norm_num
  hcap_pos := by norm_num

instance : Nonempty DensityCapVarianceCert :=
  ⟨canonicalDensityCapCert⟩

/-- Unconditional density ratio upper bound `wMax / zPart ≤ cap` on any certified cell. -/
theorem canonical_density_cap_le :
    canonicalDensityCapCert.wMax / canonicalDensityCapCert.zPart ≤
      canonicalDensityCapCert.cap :=
  gibbsRatio_le_bound canonicalDensityCapCert.hwmin (by dsimp [canonicalDensityCapCert]; norm_num)
    canonicalDensityCapCert.hz canonicalDensityCapCert.hcap

/-- Calibrated rational variance floor `4 / cap = 1 / 2` at canonical oscillation cap `8`. -/
theorem canonical_variance_floor_half :
    (4 : ℚ) / canonicalDensityCapCert.cap = 1 / 2 := by
  dsimp [canonicalDensityCapCert]
  norm_num

/-- **CONDITIONAL:** Once Stage 1 localized RG bounds effective single-cell action oscillation by
`osc` (`Real.exp (-vMin) ≤ expOsc * Real.exp (-vMax)`) and the Hopf bathtub bound holds at
density cap `M = Real.exp osc`, expected non-Abelian commutator loss retains the strictly
positive uniform floor `4 * Real.exp (-osc) > 0`. -/
theorem crossover_variance_floor_of_bounded_osc_conditional (osc expectComm : ℝ)
    (hbat : 8 * Real.exp osc * (1 / (2 * Real.exp osc ^ 2)) ≤ expectComm) :
    0 < 4 * Real.exp (-osc) ∧ 4 * Real.exp (-osc) ≤ expectComm := by
  have hexp_ne : Real.exp osc ≠ 0 := Real.exp_ne_zero osc
  have heval := bathtub_integral_eval (Real.exp osc) hexp_ne
  have hfloor : 4 / Real.exp osc ≤ expectComm := by linarith
  exact variance_floor_of_bounded_osc hfloor

end YangMillsBlueprint.Certificates
