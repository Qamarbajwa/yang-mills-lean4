/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.SpinorHermitianWickBridge
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.NormNum

/-!
# YM-171: Spinor-Hermitian Wick Bridge & `SL(2, ℂ)` Mass-Shell Certificate

Certifies:
1. Unconditional `2 × 2` spinor-matrix correspondence: Euclidean `det (eucQuatMat x) = ∑ x_μ²`,
   OS time reflection `-Qᴴ`, Hermitian Minkowski `minkHermMat` with `det = -minkowskiQuad x`,
   exact Wick identity `eucQuatMat (I * x₀) x₁ x₂ x₃ = I • minkHermMat x`, `SL(2, ℂ)` `2`-to-`1`
   double cover preserving Hermiticity/determinant/hyperbolic boosts `sl2Boost3 φ`, and strict
   future light-cone trace positivity `0 < (trace (sl2Act A (minkHermMat x))).re`.
2. Conditional spinor-mass-shell gap bridge from `ContractiveTransfer T Ω cert.r` (`YM150`) to
   boost-invariant forward spinor mass-shell hyperboloid `det (sl2Act A X) = m²` with `Δ² ≤ m²`.
-/

namespace YangMillsBlueprint.Certificates

open LorentzianMetricGroup Matrix SliceReflectionHilbert SpinorHermitianWickBridge
open WickSemigroupMassShell

/-- Certificate pairing contraction `0 < r < 1` with `SL(2, ℂ)` boost rapidity `φ`. -/
structure SpinorWickCert where
  r : ℝ
  φ : ℝ
  hr0 : 0 < r
  hr1 : r < 1

/-- Canonical spinor Wick witness (`r = 1 / 2` ⇒ Euclidean gap `log 2`, rapidity `φ = 1`). -/
noncomputable def canonicalSpinorWickCert : SpinorWickCert where
  r := 1 / 2
  φ := 1
  hr0 := by norm_num
  hr1 := by norm_num

instance : Nonempty SpinorWickCert :=
  ⟨canonicalSpinorWickCert⟩

/-- **UNCONDITIONAL:** Certifies the complexified `2 × 2` Euclidean/Minkowski Wick isomorphism,
`SL(2, ℂ)` double-cover invariance, hyperbolic boost group law, and future-cone positivity. -/
theorem spinor_hermitian_wick_double_cover_unconditional (cert : SpinorWickCert)
    (A : Matrix (Fin 2) (Fin 2) ℂ) (hA : A.det = 1) (x : Fin 4 → ℝ)
    (hx0 : 0 < x 0) (hfut : x 1 ^ 2 + x 2 ^ 2 + x 3 ^ 2 < x 0 ^ 2) :
    (eucQuatMat (x 0) (x 1) (x 2) (x 3)).det =
        ((x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 + x 3 ^ 2 : ℝ) : ℂ) ∧
      eucQuatMat (-((x 0 : ℝ) : ℂ)) (x 1) (x 2) (x 3) =
        -(eucQuatMat (x 0) (x 1) (x 2) (x 3))ᴴ ∧
      (minkHermMat x)ᴴ = minkHermMat x ∧
      (minkHermMat x).det = ((-minkowskiQuad x : ℝ) : ℂ) ∧
      eucQuatMat (Complex.I * ((x 0 : ℝ) : ℂ)) (x 1) (x 2) (x 3) =
        Complex.I • minkHermMat x ∧
      (sl2Act A (minkHermMat x))ᴴ = sl2Act A (minkHermMat x) ∧
      (sl2Act A (minkHermMat x)).det = (minkHermMat x).det ∧
      sl2Act (-A) (minkHermMat x) = sl2Act A (minkHermMat x) ∧
      (sl2Boost3 cert.φ).det = 1 ∧
      0 < (Matrix.trace (sl2Act A (minkHermMat x))).re := by
  refine ⟨?_, eucQuatMat_osReflect x, minkHermMat_conjTranspose x, minkHermMat_det x,
    wick_eucQuatMat_eq_I_smul_minkHermMat x, sl2Act_conjTranspose A (minkHermMat x)
      (minkHermMat_conjTranspose x), sl2Act_det A (minkHermMat x) hA,
    sl2Act_doubleCover A (minkHermMat x), sl2Boost3_det cert.φ,
    sl2Act_trace_re_pos_of_future_timelike A hA x hx0 hfut⟩
  rw [eucQuatMat_det_real]
  push_cast
  ring

/-- **CONDITIONAL:** Assuming `ContractiveTransfer T Ω cert.r` on `OSHilbert B` gives Euclidean gap
`Δ = log (1 / cert.r) > 0`, any on-shell 4-momentum `massShellFourMom m p₁ p₂ p₃` (`m ≥ Δ`) lifted
to `sl2Act A (minkHermMat p)` keeps determinant `m²` (`Δ² ≤ m²`) and positive forward trace under
every `A ∈ SL(2, ℂ)`. -/
theorem spinor_mass_shell_os_gap_conditional {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : ReflectionPositiveForm V) (T : OSHilbert B →ₗ[ℝ] OSHilbert B) (Ω : OSHilbert B)
    (cert : SpinorWickCert) (hT : ContractiveTransfer T Ω cert.r)
    (A : Matrix (Fin 2) (Fin 2) ℂ) (hA : A.det = 1)
    {m : ℝ} (hm : Real.log (1 / cert.r) ≤ m) (p1 p2 p3 : ℝ) :
    0 < Real.log (1 / cert.r) ∧
      SpectralMassGapBridge.HasOrthogonalCoercivity (LinearMap.id - T) Ω (1 - cert.r) ∧
      Real.log (1 / cert.r) ^ 2 ≤ m ^ 2 ∧
      (sl2Act A (minkHermMat (massShellFourMom m p1 p2 p3))).det = ((m ^ 2 : ℝ) : ℂ) ∧
      0 < (Matrix.trace (sl2Act A (minkHermMat (massShellFourMom m p1 p2 p3)))).re := by
  have hΔpos : 0 < Real.log (1 / cert.r) :=
    Real.log_pos (one_lt_one_div cert.hr0 cert.hr1)
  have hΔ0 : 0 ≤ Real.log (1 / cert.r) := le_of_lt hΔpos
  have hmpos : 0 < m := lt_of_lt_of_le hΔpos hm
  have hm2 : Real.log (1 / cert.r) ^ 2 ≤ m ^ 2 :=
    pow_le_pow_left₀ hΔ0 hm 2
  have hp0 : 0 < massShellFourMom m p1 p2 p3 0 :=
    massShellEnergy_pos hmpos p1 p2 p3
  have hfut :
      massShellFourMom m p1 p2 p3 1 ^ 2 + massShellFourMom m p1 p2 p3 2 ^ 2 +
          massShellFourMom m p1 p2 p3 3 ^ 2 <
        massShellFourMom m p1 p2 p3 0 ^ 2 := by
    unfold massShellFourMom massShellEnergy
    have hnonneg : 0 ≤ m ^ 2 + p1 ^ 2 + p2 ^ 2 + p3 ^ 2 := by positivity
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val]
    rw [Real.sq_sqrt hnonneg]
    have hm2pos : 0 < m ^ 2 := sq_pos_of_pos hmpos
    linarith
  have hquad := massShellFourMom_quad m p1 p2 p3
  have hdet :
      (sl2Act A (minkHermMat (massShellFourMom m p1 p2 p3))).det = ((m ^ 2 : ℝ) : ℂ) := by
    rw [sl2Act_det A _ hA, minkHermMat_det, hquad]
    simp
  have htr := sl2Act_trace_re_pos_of_future_timelike A hA (massShellFourMom m p1 p2 p3) hp0 hfut
  exact ⟨hΔpos, transfer_to_coercivity hT, hm2, hdet, htr⟩

end YangMillsBlueprint.Certificates
