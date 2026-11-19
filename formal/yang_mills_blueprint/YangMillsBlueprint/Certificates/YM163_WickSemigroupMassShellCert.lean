/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.WickSemigroupMassShell
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# YM-163: Wick Rotation Semigroup & Lorentzian Mass-Shell Certificate

Certifies:
1. Unconditional complex half-plane Wick semigroup identities (`‖wickAmplitude 0 tM E‖ = 1`,
   `‖wickAmplitude tE tM E(p)‖ ≤ exp(-tE * Δ)`) and boost-invariant mass-shell hyperboloid
   `Δ² ≤ -(p'ᵀ η p') = m²` with `p' 0 > 0`.
2. Conditional synthesis linking `YM160` (`wilsonCrossingRPForm` / `OSHilbert`) + `YM150`
   (`ContractiveTransfer T Ω cert.r` giving Euclidean gap `Δ = log(1/r) > 0`) to the
   Lorentzian mass-shell hyperboloid floor `Δ² ≤ -minkowskiQuad (B₁(φ) *ᵥ p)` (`p' 0 > 0`).
-/

namespace YangMillsBlueprint.Certificates

open LatticeHaarGibbs LatticeReflectionPositivity LorentzianMetricGroup Matrix
open MeasureTheory SliceReflectionHilbert WickSemigroupMassShell

/-- Certificate pairing a strict transfer contraction `0 < r < 1` with a Lorentz boost rapidity. -/
structure WickMassShellCert where
  r : ℝ
  φ : ℝ
  hr0 : 0 < r
  hr1 : r < 1

/-- Canonical witness (`r = 1 / 2` ⇒ Euclidean gap `log 2 > 0`, unit rapidity `φ = 1`). -/
noncomputable def canonicalWickMassShellCert : WickMassShellCert where
  r := 1 / 2
  φ := 1
  hr0 := by norm_num
  hr1 := by norm_num

instance : Nonempty WickMassShellCert :=
  ⟨canonicalWickMassShellCert⟩

/-- **UNCONDITIONAL:** For any `cert : WickMassShellCert` with Euclidean gap scale
`Δ = Real.log (1 / cert.r) > 0`, any rest mass `m ≥ Δ`, `tE ≥ 0`, real `tM`, and 3-momentum
`(p₁, p₂, p₃)`, the complex Wick amplitude satisfies unitary modulus `1` on the Lorentzian axis
and exponential gap contraction `≤ exp (-tE * Δ)` in Euclidean time, while the boosted
4-momentum stays strictly on the forward mass-shell hyperboloid above `Δ²`. -/
theorem wick_semigroup_mass_shell_unconditional (cert : WickMassShellCert)
    {tE m : ℝ} (htE : 0 ≤ tE) (hm : Real.log (1 / cert.r) ≤ m) (tM p1 p2 p3 : ℝ) :
    0 < Real.log (1 / cert.r) ∧
      ‖wickAmplitude tE tM (massShellEnergy m p1 p2 p3)‖ ≤
        Real.exp (-(tE * Real.log (1 / cert.r))) ∧
      ‖wickAmplitude 0 tM (massShellEnergy m p1 p2 p3)‖ = 1 ∧
      -minkowskiQuad (lorentzBoost1 cert.φ *ᵥ massShellFourMom m p1 p2 p3) = m ^ 2 ∧
      Real.log (1 / cert.r) ^ 2 ≤
        -minkowskiQuad (lorentzBoost1 cert.φ *ᵥ massShellFourMom m p1 p2 p3) ∧
      0 < (lorentzBoost1 cert.φ *ᵥ massShellFourMom m p1 p2 p3) 0 := by
  have hΔpos : 0 < Real.log (1 / cert.r) :=
    Real.log_pos (one_lt_one_div cert.hr0 cert.hr1)
  have hΔ0 : 0 ≤ Real.log (1 / cert.r) := le_of_lt hΔpos
  have hmpos : 0 < m := lt_of_lt_of_le hΔpos hm
  have hwick := wickAmplitude_euclidean_gap_bound htE hm tM p1 p2 p3
  have hunit := wickAmplitude_lorentzian_unitary tM (massShellEnergy m p1 p2 p3)
  have hshell := massShell_boost_invariant_gap hmpos hΔ0 hm p1 p2 p3 cert.φ
  exact ⟨hΔpos, hwick, hunit, hshell.1, hshell.2.1, hshell.2.2⟩

/-- **CONDITIONAL:** On the completed OS Hilbert space `OSHilbert B` of a finite-box Wilson
reflection-positive form `B` (`YM160`), assuming continuum transfer contraction
`ContractiveTransfer T Ω cert.r` (`YM150`, open Clay RG/OS continuum frontier) induces spectral
gap `Δ = log (1 / cert.r) > 0` for excitations `m ≥ Δ`, every state orthogonal to `Ω` decays at
rate `≥ Δ` under `(T ^ n)` while Wick continuation lands on the forward Lorentzian mass-shell
hyperboloid above `Δ²` with unitary real-time evolution `‖wickAmplitude 0 tM‖ = 1`. -/
theorem wick_mass_shell_gap_conditional
    {V : Type*} [AddCommGroup V] [Module ℝ V] (B : ReflectionPositiveForm V)
    (T : OSHilbert B →ₗ[ℝ] OSHilbert B) (Ω : OSHilbert B) (cert : WickMassShellCert)
    (hT : ContractiveTransfer T Ω cert.r) (u v : OSHilbert B) (hv : inner ℝ Ω v = 0)
    (n : ℕ) {tE m : ℝ} (htE : 0 ≤ tE) (hm : Real.log (1 / cert.r) ≤ m) (tM p1 p2 p3 : ℝ) :
    SpectralMassGapBridge.HasOrthogonalCoercivity (LinearMap.id - T) Ω (1 - cert.r) ∧
      |inner ℝ u ((T ^ n) v)| ≤
        Real.exp (-(Real.log (1 / cert.r) * (n : ℝ))) * (‖u‖ * ‖v‖) ∧
      ‖wickAmplitude tE tM (massShellEnergy m p1 p2 p3)‖ ≤
        Real.exp (-(tE * Real.log (1 / cert.r))) ∧
      ‖wickAmplitude 0 tM (massShellEnergy m p1 p2 p3)‖ = 1 ∧
      Real.log (1 / cert.r) ^ 2 ≤
        -minkowskiQuad (lorentzBoost1 cert.φ *ᵥ massShellFourMom m p1 p2 p3) ∧
      0 < (lorentzBoost1 cert.φ *ᵥ massShellFourMom m p1 p2 p3) 0 := by
  have hcoerc := transfer_to_coercivity hT
  have hdec := (transfer_correlator_exp_decay hT u hv n).1
  have hshell := wick_semigroup_mass_shell_unconditional cert htE hm tM p1 p2 p3
  exact ⟨hcoerc, hdec, hshell.2.1, hshell.2.2.1, hshell.2.2.2.2.1, hshell.2.2.2.2.2⟩

end YangMillsBlueprint.Certificates
