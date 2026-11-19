/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.LorentzianMetricGroup
import Mathlib.Tactic.NormNum

/-!
# YM-161: Minkowski Metric Involution & `O(1,3)` Lorentz Boost Certificate

Unconditionally certifies the core Minkowski matrix geometry linking the identity `1`,
antipodal inversion `-1`, and Lorentzian signature `minkowskiEta = diag(-1, 1, 1, 1)`:
- `minkowskiEta` symmetry, involution (`η * η = 1`), and determinant `-1`,
- Exact `O(1,3)` inverse `lorentzInv Λ * Λ = 1` and quadratic form invariance,
- Hyperbolic boost group `lorentzBoost1 φ` (`cosh`, `sinh`) with rapidity additivity,
  determinant `+1`, and forward light-cone energy positivity `E * cosh φ + p₁ * sinh φ > 0`.
-/

namespace YangMillsBlueprint.Certificates

open LorentzianMetricGroup Matrix

/-- Real certificate bundling boost rapidity `φ` and strict positive rest mass `m > 0`. -/
structure LorentzianMetricCert where
  φ : ℝ
  m : ℝ
  hm : 0 < m

/-- Canonical unit-rapidity, unit-mass witness (`φ = 1`, `m = 1`). -/
noncomputable def canonicalLorentzianMetricCert : LorentzianMetricCert where
  φ := 1
  m := 1
  hm := by norm_num

instance : Nonempty LorentzianMetricCert :=
  ⟨canonicalLorentzianMetricCert⟩

/-- **UNCONDITIONAL:** Certifies `minkowskiEta` involution and determinant `-1`, group/inverse
closure for `O(1,3)`, `lorentzBoost1 cert.φ ∈ SO⁺(1,3)` with `det = 1`, quadratic invariance of
`(cert.m, p₁, 0, 0)` on the mass-shell hyperboloid, and forward-cone positivity whenever
`|p₁| ≤ cert.m`. -/
theorem lorentzian_metric_and_boost_group_unconditional (cert : LorentzianMetricCert)
    (Λ₁ Λ₂ : Matrix (Fin 4) (Fin 4) ℝ)
    (h₁ : IsLorentzMatrix Λ₁) (h₂ : IsLorentzMatrix Λ₂)
    (x : Fin 4 → ℝ) {p1 : ℝ} (hcausal : |p1| ≤ cert.m) :
    minkowskiEtaᵀ = minkowskiEta ∧
      minkowskiEta * minkowskiEta = 1 ∧
      minkowskiEta.det = -1 ∧
      IsLorentzMatrix (Λ₁ * Λ₂) ∧
      lorentzInv Λ₁ * Λ₁ = 1 ∧
      minkowskiQuad (Λ₁ *ᵥ x) = minkowskiQuad x ∧
      IsLorentzMatrix (lorentzBoost1 cert.φ) ∧
      (lorentzBoost1 cert.φ).det = 1 ∧
      0 < cert.m * Real.cosh cert.φ + p1 * Real.sinh cert.φ := by
  exact ⟨minkowskiEta_transpose, minkowskiEta_mul_self, minkowskiEta_det,
    isLorentzMatrix_mul h₁ h₂, lorentzInv_mul_self h₁, isLorentzMatrix_preserves_quad h₁ x,
    isLorentzMatrix_lorentzBoost1 cert.φ, lorentzBoost1_det cert.φ,
    lorentzBoost1_future_pos cert.hm hcausal cert.φ⟩

end YangMillsBlueprint.Certificates
