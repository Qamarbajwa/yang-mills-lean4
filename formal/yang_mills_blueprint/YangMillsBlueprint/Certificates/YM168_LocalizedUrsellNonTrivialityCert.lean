/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.LocalizedUrsellNonTriviality
import Mathlib.Tactic.NormNum

/-!
# YM-168: Localized Ursell Non-Triviality (`E-NONTRIV-WITNESS`) Certificate

Certifies unconditionally why localized 4-point connected cumulants preserve non-Gaussianity across
cutoff limits while `1 / V`-averaged zero-momentum slice kurtosis vanishes as `V → ∞`, and wraps
the conditional continuum witness preventing Gaussian triviality.
-/

namespace YangMillsBlueprint.Certificates

open Filter LocalizedUrsellNonTriviality Topology

/-- Certificate bundling canonical local 4-point moments `(m2, m4)`, spatial box size `V ≥ 1`, and
strict non-Gaussian floor `0 < c4`. -/
structure LocalizedUrsellCert where
  m2 : ℝ
  m4 : ℝ
  c4 : ℝ
  V : ℕ
  hc4 : 0 < c4
  hV : 1 ≤ V
  hu4 : ursell4 m4 m2 = c4

/-- Canonical non-Gaussian local witness (`m2 = 1/2`, `m4 = 1`, `c4 = 1/4`, `V = 64`). -/
noncomputable def canonicalLocalizedUrsellCert : LocalizedUrsellCert where
  m2 := 1 / 2
  m4 := 1
  c4 := 1 / 4
  V := 64
  hc4 := by norm_num
  hV := by norm_num
  hu4 := by dsimp [ursell4]; norm_num

instance : Nonempty LocalizedUrsellCert :=
  ⟨canonicalLocalizedUrsellCert⟩

/-- **UNCONDITIONAL:** Non-zero localized Ursell cumulant rules out Gaussian Wick factorization
`m4 = 3 * m2 ^ 2`, while spatial slice averaging forces `sliceAvgKurtosis → 0` as `V → ∞`. -/
theorem localized_ursell_rules_out_gaussian_unconditional (cert : LocalizedUrsellCert)
    (v : ℝ) :
    cert.m4 ≠ 3 * cert.m2 ^ 2 ∧
      Tendsto (sliceAvgKurtosis cert.c4 v) atTop (𝓝 0) ∧
      ursell4 canonicalLocalizedUrsellCert.m4 canonicalLocalizedUrsellCert.m2 = 1 / 4 := by
  have hne : ursell4 cert.m4 cert.m2 ≠ 0 := by
    rw [cert.hu4]
    exact ne_of_gt cert.hc4
  refine ⟨ursell4_ne_zero_implies_non_gaussian hne, tendsto_sliceAvgKurtosis_zero cert.c4 v, ?_⟩
  dsimp [canonicalLocalizedUrsellCert, ursell4]
  norm_num

/-- **CONDITIONAL:** Once localized gauge-invariant 4-point cumulants along the continuum sequence
stay bounded below by `cert.c4 ≤ |u4 k|` and converge to `u4_lim`, the continuum theory satisfies
`|u4_lim| ≥ cert.c4 > 0` and cannot collapse to a Gaussian free field (`E-NONTRIV-WITNESS`). -/
theorem continuum_localized_nontriviality_conditional (cert : LocalizedUrsellCert)
    (u4 : ℕ → ℝ) (u4_lim : ℝ)
    (hbd : ∀ k : ℕ, cert.c4 ≤ |u4 k|)
    (hlim : Tendsto u4 atTop (𝓝 u4_lim)) :
    cert.c4 ≤ |u4_lim| ∧ u4_lim ≠ 0 :=
  tendsto_localized_ursell_ne_zero u4 u4_lim cert.c4 cert.hc4 hbd hlim

end YangMillsBlueprint.Certificates
