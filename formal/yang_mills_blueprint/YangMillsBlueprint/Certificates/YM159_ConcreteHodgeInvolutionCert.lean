/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.ConcreteHodgeInvolution
import Mathlib.Tactic.NormNum

/-!
# YM-159: Concrete 4D (`6 = 3 + 3`) and 8D (`70 = 35 + 35`) Hodge Involution Certificate

Unconditionally certifies genuine concrete `SelfDualWaveProjection.SymmInvolution` operators:
- `hodge4D` on `EuclideanSpace ℝ (Fin 6)` with `+1`/`-1` subspaces of exact `Module.finrank = 3`
  summing to `Nat.choose 4 2 = 6`,
- `hodge8D` on `EuclideanSpace ℝ (Fin 70)` (`∧⁴ S₈⁺`) with `+1`/`-1` subspaces of exact
  `Module.finrank = 35` summing to `Nat.choose 8 4 = 70`,
- Unconditional pointwise Bogomol'nyi splits and bounds in `4D`, `8D`, and arbitrary balanced
  half-dimension `cert.halfDim + cert.halfDim`.
-/

namespace YangMillsBlueprint.Certificates

open ConcreteHodgeInvolution SelfDualWaveProjection

/-- Positive half-dimension certificate for balanced `+1`/`-1` Hodge splits. -/
structure ConcreteHodgeCert where
  halfDim : ℕ
  hpos : 0 < halfDim

/-- Canonical 8D `∧⁴ S₈⁺` spinor four-form certificate (`70 = 35 + 35`). -/
def canonicalHodge8DCert : ConcreteHodgeCert where
  halfDim := 35
  hpos := by norm_num

instance : Nonempty ConcreteHodgeCert :=
  ⟨canonicalHodge8DCert⟩

/-- **UNCONDITIONAL:** Concrete 4D curvature (`Fin 6`, `3 + 3 = C(4, 2)`) and 8D spinor four-form
(`Fin 70`, `35 + 35 = C(8, 4)`) Hodge involutions together with exact balanced `finrank` splits
for any `ConcreteHodgeCert`. -/
theorem hodge4D_and_8D_unconditional (cert : ConcreteHodgeCert) :
    SymmInvolution hodge4D ∧
      SymmInvolution hodge8D ∧
      Module.finrank ℝ (LinearMap.range (sdEmbed 3)) +
        Module.finrank ℝ (LinearMap.range (asdEmbed 3)) = Nat.choose 4 2 ∧
      Module.finrank ℝ (LinearMap.range (sdEmbed 35)) +
        Module.finrank ℝ (LinearMap.range (asdEmbed 35)) = Nat.choose 8 4 ∧
      Module.finrank ℝ (LinearMap.range (sdEmbed cert.halfDim)) +
        Module.finrank ℝ (LinearMap.range (asdEmbed cert.halfDim)) =
          cert.halfDim + cert.halfDim := by
  refine ⟨symmInvolution_hodge4D, symmInvolution_hodge8D,
    finrank_hodge4D_split.2.2, finrank_hodge8D_split.2.2, ?_⟩
  rw [finrank_range_sdEmbed, finrank_range_asdEmbed]

/-- **UNCONDITIONAL:** Pointwise Bogomol'nyi splitting and topological action inequality
`|⟪x, J x⟫| ≤ ‖x‖²` for `hodge4D`, `hodge8D`, and `halfSwap cert.halfDim`. -/
theorem hodge4D_8D_energy_bogomolnyi_unconditional (cert : ConcreteHodgeCert)
    (F : EuclideanSpace ℝ (Fin 6)) (ω : EuclideanSpace ℝ (Fin 70))
    (x : EuclideanSpace ℝ (Fin (cert.halfDim + cert.halfDim))) :
    (‖F‖ ^ 2 = ‖projPlus hodge4D F‖ ^ 2 + ‖projMinus hodge4D F‖ ^ 2 ∧
      |inner ℝ F (hodge4D F)| ≤ ‖F‖ ^ 2) ∧
    (‖ω‖ ^ 2 = ‖projPlus hodge8D ω‖ ^ 2 + ‖projMinus hodge8D ω‖ ^ 2 ∧
      |inner ℝ ω (hodge8D ω)| ≤ ‖ω‖ ^ 2) ∧
    (‖x‖ ^ 2 =
        ‖projPlus (halfSwap cert.halfDim) x‖ ^ 2 + ‖projMinus (halfSwap cert.halfDim) x‖ ^ 2 ∧
      |inner ℝ x (halfSwap cert.halfDim x)| ≤ ‖x‖ ^ 2) := by
  refine ⟨hodge4D_bogomolnyi F, hodge8D_bogomolnyi ω, ?_⟩
  have hsym := symmInvolution_halfSwap cert.halfDim
  exact ⟨norm_sq_eq_projPlus_add_projMinus hsym x, abs_inner_invol_le_norm_sq hsym x⟩

end YangMillsBlueprint.Certificates
