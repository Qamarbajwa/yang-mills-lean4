/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.RigidChordAction
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

/-!
# YM-153: Rigid Frobenius Chord Action Certificate

Certifies the exact geometric correspondence between Wilson plaquette cost and normalized
Frobenius chord distance from the identity frame `1` (`0` at `1`, `2` at antipodal `-1`),
orthogonal conjugation invariance, and rigid 4-link plaquette chord bounds from link chords.
-/

namespace YangMillsBlueprint.Certificates

open Matrix AdjointBianchiNorm WilsonPlaquetteAction RigidChordAction

/-- Real certificate bundling matrix representation size `n > 0` and uniform per-link squared
Frobenius chord cap `linkChordCap`. -/
structure RigidChordCert where
  n : ℕ
  hn : 0 < n
  linkChordCap : ℝ
  hcap : 0 ≤ linkChordCap

/-- Canonical `n = 3` (adjoint `SO(3)` scale) small-field witness `linkChordCap = 1 / 4`. -/
noncomputable def canonicalRigidChordCert : RigidChordCert where
  n := 3
  hn := by norm_num
  linkChordCap := 1 / 4
  hcap := by norm_num

instance : Nonempty RigidChordCert :=
  ⟨canonicalRigidChordCert⟩

/-- **UNCONDITIONAL:** Canonical evaluation confirming zero plaquette cost at `1` and sharp
maximum `2` at antipodal `-1` for `n = 3`. -/
theorem canonical_identity_and_antipodal_cost :
    plaquetteCost (1 : Matrix (Fin canonicalRigidChordCert.n) (Fin canonicalRigidChordCert.n) ℝ) = 0 ∧
      plaquetteCost (-1 : Matrix (Fin canonicalRigidChordCert.n) (Fin canonicalRigidChordCert.n) ℝ) = 2 :=
  ⟨plaquetteCost_one_eq_zero canonicalRigidChordCert.hn,
    plaquetteCost_neg_one_eq_two canonicalRigidChordCert.hn⟩

/-- **UNCONDITIONAL:** For any 4 orthogonal links around a plaquette (`n > 0`), the normalized
Wilson plaquette cost is bounded above by `(2 / n) * ∑_{i=1}^4 frobSq (Ui - 1)`. -/
theorem rigid_plaquette_cost_le_two_div_n_mul_link_chords {n : ℕ} (hn : 0 < n)
    {U1 U2 U3 U4 : Matrix (Fin n) (Fin n) ℝ}
    (hU1l : U1ᵀ * U1 = 1) (hU2l : U2ᵀ * U2 = 1) (hU3l : U3ᵀ * U3 = 1)
    (hU1r : U1 * U1ᵀ = 1) (hU2r : U2 * U2ᵀ = 1) (hU3r : U3 * U3ᵀ = 1) (hU4r : U4 * U4ᵀ = 1) :
    plaquetteCost (plaquetteHolonomy U1 U2 U3 U4) ≤
      (2 / (n : ℝ)) *
        (frobSq (U1 - 1) + frobSq (U2 - 1) + frobSq (U3 - 1) + frobSq (U4 - 1)) := by
  have hporth :
      plaquetteHolonomy U1 U2 U3 U4 * (plaquetteHolonomy U1 U2 U3 U4)ᵀ = 1 := by
    unfold plaquetteHolonomy
    exact orth_mul_orth (orth_mul_orth (orth_mul_orth hU1r hU2r) hU3r) hU4r
  rw [plaquetteCost_eq_frobSq_div hn hporth]
  have hchord := frobSq_plaquette_le_four_sum U1 U2 U3 U4 hU1l hU2l hU3l
  have hnPos : (0 : ℝ) < (n : ℝ) := Nat.cast_pos.mpr hn
  have h2nPos : 0 < 2 * (n : ℝ) := by positivity
  rw [div_le_iff₀ h2nPos]
  calc frobSq (plaquetteHolonomy U1 U2 U3 U4 - 1)
      ≤ 4 * (frobSq (U1 - 1) + frobSq (U2 - 1) + frobSq (U3 - 1) + frobSq (U4 - 1)) := hchord
    _ = (2 / (n : ℝ)) *
          (frobSq (U1 - 1) + frobSq (U2 - 1) + frobSq (U3 - 1) + frobSq (U4 - 1)) *
          (2 * (n : ℝ)) := by
        field_simp [ne_of_gt hnPos]
        ring

/-- **CONDITIONAL:** In any rigid gauge-fixed region where each link satisfies the per-link chord
cap `frobSq (Ui - 1) ≤ cert.linkChordCap`, every 4-link plaquette cost is uniformly capped by
`8 * cert.linkChordCap / cert.n`. -/
theorem rigid_small_field_plaquette_cap_conditional (cert : RigidChordCert)
    {U1 U2 U3 U4 : Matrix (Fin cert.n) (Fin cert.n) ℝ}
    (hU1l : U1ᵀ * U1 = 1) (hU2l : U2ᵀ * U2 = 1) (hU3l : U3ᵀ * U3 = 1)
    (hU1r : U1 * U1ᵀ = 1) (hU2r : U2 * U2ᵀ = 1) (hU3r : U3 * U3ᵀ = 1) (hU4r : U4 * U4ᵀ = 1)
    (hc1 : frobSq (U1 - 1) ≤ cert.linkChordCap)
    (hc2 : frobSq (U2 - 1) ≤ cert.linkChordCap)
    (hc3 : frobSq (U3 - 1) ≤ cert.linkChordCap)
    (hc4 : frobSq (U4 - 1) ≤ cert.linkChordCap) :
    0 ≤ plaquetteCost (plaquetteHolonomy U1 U2 U3 U4) ∧
      plaquetteCost (plaquetteHolonomy U1 U2 U3 U4) ≤
        8 * cert.linkChordCap / (cert.n : ℝ) := by
  have hporth :
      plaquetteHolonomy U1 U2 U3 U4 * (plaquetteHolonomy U1 U2 U3 U4)ᵀ = 1 := by
    unfold plaquetteHolonomy
    exact orth_mul_orth (orth_mul_orth (orth_mul_orth hU1r hU2r) hU3r) hU4r
  have h0 := (plaquetteCost_mem_Icc cert.hn hporth).1
  have hbound :=
    rigid_plaquette_cost_le_two_div_n_mul_link_chords cert.hn hU1l hU2l hU3l hU1r hU2r hU3r hU4r
  have hnPos : (0 : ℝ) < (cert.n : ℝ) := Nat.cast_pos.mpr cert.hn
  have h2divNonneg : 0 ≤ 2 / (cert.n : ℝ) := by positivity
  have hsum :
      frobSq (U1 - 1) + frobSq (U2 - 1) + frobSq (U3 - 1) + frobSq (U4 - 1) ≤
        4 * cert.linkChordCap := by
    linarith
  have hmul :
      (2 / (cert.n : ℝ)) *
          (frobSq (U1 - 1) + frobSq (U2 - 1) + frobSq (U3 - 1) + frobSq (U4 - 1)) ≤
        (2 / (cert.n : ℝ)) * (4 * cert.linkChordCap) :=
    mul_le_mul_of_nonneg_left hsum h2divNonneg
  have hrw : (2 / (cert.n : ℝ)) * (4 * cert.linkChordCap) =
      8 * cert.linkChordCap / (cert.n : ℝ) := by
    ring
  exact ⟨h0, le_trans hbound (hmul.trans_eq hrw)⟩

end YangMillsBlueprint.Certificates
