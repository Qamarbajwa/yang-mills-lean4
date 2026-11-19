/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.BlockPolymerOscillation
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

/-!
# YM-155: Block Polymer Tail Oscillation and Haar Gibbs Certificate

Certifies the volume-independent effective oscillation bound
`effectiveBlockOsc B_int C θ = B_int + 2 * C * θ / (1 - θ)` and lifts finite-box
polymer-bounded block actions into `LatticeHaarGibbs` density caps and expectation floors.
-/

namespace YangMillsBlueprint.Certificates

open LatticeHaarGibbs BlockPolymerOscillation MeasureTheory

/-- Real certificate bundling interior chord capacity `B_int`, polymer prefactor `C`, decay
ratio `0 ≤ θ < 1`, and Haar floor `haarFloor > 0`. -/
structure BlockPolymerOscCert where
  B_int : ℝ
  C : ℝ
  θ : ℝ
  haarFloor : ℝ
  hB0 : 0 ≤ B_int
  hC0 : 0 ≤ C
  hθ0 : 0 ≤ θ
  hθ1 : θ < 1
  hfloor : 0 < haarFloor

/-- Canonical calibrated witness (`B_int = 1`, `C = 1`, `θ = 1 / 3`, `haarFloor = 1`). -/
noncomputable def canonicalBlockPolymerOscCert : BlockPolymerOscCert where
  B_int := 1
  C := 1
  θ := 1 / 3
  haarFloor := 1
  hB0 := by norm_num
  hC0 := by norm_num
  hθ0 := by norm_num
  hθ1 := by norm_num
  hfloor := by norm_num

instance : Nonempty BlockPolymerOscCert :=
  ⟨canonicalBlockPolymerOscCert⟩

/-- Exact canonical polymer effective oscillation `1 + 2 * (1 * (1/3) / (1 - 1/3)) = 2`. -/
theorem canonical_polymer_osc_eq :
    effectiveBlockOsc canonicalBlockPolymerOscCert.B_int canonicalBlockPolymerOscCert.C
      canonicalBlockPolymerOscCert.θ = 2 := by
  dsimp [canonicalBlockPolymerOscCert, effectiveBlockOsc, polymerTailBound]
  norm_num

/-- **CONDITIONAL:** Once Stage 1 (`E-UV-RG`) establishes a uniform decomposition
`S = S_int + S_ext` with `0 ≤ S_int ≤ cert.B_int` and boundary polymer tail
`|S_ext| ≤ polymerTailBound cert.C cert.θ` (`0 ≤ cert.θ < 1`), every finite box `(E → G)`
inherits a volume-independent Boltzmann density cap `exp (effectiveBlockOsc)` and strictly
positive weighted expectation floor `exp (-effectiveBlockOsc) * cert.haarFloor`. -/
theorem block_polymer_oscillation_gibbs_conditional {E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (cert : BlockPolymerOscCert)
    (S S_int S_ext f : (E → G) → ℝ)
    (hint : Integrable (expWeight S) (productHaarProb E G))
    (hf : Integrable f (productHaarProb E G))
    (hfw : Integrable (fun U => f U * expWeight S U) (productHaarProb E G))
    (hf0 : ∀ U, 0 ≤ f U)
    (hdecomp : ∀ U, S U = S_int U + S_ext U)
    (hintLo : ∀ U, 0 ≤ S_int U) (hintHi : ∀ U, S_int U ≤ cert.B_int)
    (hext : ∀ U, |S_ext U| ≤ polymerTailBound cert.C cert.θ)
    (hhaar : cert.haarFloor ≤ ∫ U, f U ∂(productHaarProb E G)) :
    0 < Real.exp (-effectiveBlockOsc cert.B_int cert.C cert.θ) * cert.haarFloor ∧
      Real.exp (-effectiveBlockOsc cert.B_int cert.C cert.θ) * cert.haarFloor ≤
        weightedExpectation (productHaarProb E G) S f ∧
      ∀ U, expWeight S U / partitionIntegral (productHaarProb E G) S ≤
        Real.exp (effectiveBlockOsc cert.B_int cert.C cert.θ) := by
  have hpos :
      0 < Real.exp (-effectiveBlockOsc cert.B_int cert.C cert.θ) * cert.haarFloor :=
    mul_pos (Real.exp_pos _) cert.hfloor
  have hmul :
      Real.exp (-effectiveBlockOsc cert.B_int cert.C cert.θ) * cert.haarFloor ≤
        Real.exp (-effectiveBlockOsc cert.B_int cert.C cert.θ) *
          (∫ U, f U ∂(productHaarProb E G)) :=
    mul_le_mul_of_nonneg_left hhaar (le_of_lt (Real.exp_pos _))
  have hexp := productHaar_polymer_expectation_floor S S_int S_ext f cert.B_int cert.C cert.θ
    hint hf hfw hf0 hdecomp hintLo hintHi hext
  have hcap := productHaar_polymer_density_cap S S_int S_ext cert.B_int cert.C cert.θ
    hint hdecomp hintLo hintHi hext
  exact ⟨hpos, le_trans hmul hexp, hcap⟩

end YangMillsBlueprint.Certificates
