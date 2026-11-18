/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.BianchiCocycleDecomposition
import YangMillsBlueprint.Certificates.YM136_GeneralGroupBianchiCert
import Mathlib.Data.Rat.Init
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# YM-142: Non-Abelian Adjoint Cocycle Decomposition Certificate (`WP2-C` / `Phase B1`)

Instantiates `BianchiCocycleDecomposition` over `ℚ` on coherent `SO(3)` 3-4-5 Pythagorean
rotations `so3RotZ345` (`cos θ = 3/5, sin θ = 4/5`) acting on `so3GenX`:
- Unconditional single-step loss: `normalizedLoss so3RotZ345 so3GenX = 2 / 5`.
- Composed double-step loss: `normalizedLoss (so3RotZ345 * so3RotZ345) so3GenX = 32 / 25`.
- Strictly positive cocycle remainder `cocycleRemainder = +16 / 25 > 0`, giving super-dyadic
  amplification ratio `2 > 1` (`dyadicLossStep (2 / 5) = 16 / 25`).
- Conditional dyadic step persistence `cocycle_dyadic_lower_bound_conditional`.
-/

namespace YangMillsBlueprint.Certificates

open AdjointBianchiNorm BianchiCocycleDecomposition BianchiDyadicAccumulation
open Matrix StokesAdjointDispersion

/-- Orthogonal `SO(3)` rotation around the 3-axis with `(cos, sin) = (3/5, 4/5)`. -/
def so3RotZ345 : Matrix (Fin 3) (Fin 3) ℚ :=
  !![3 / 5, -4 / 5, 0; 4 / 5, 3 / 5, 0; 0, 0, 1]

/-- Right-orthogonality of `so3RotZ345`. -/
theorem so3RotZ345_orth1 : so3RotZ345 * so3RotZ345ᵀ = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [so3RotZ345, Matrix.mul_apply, Fin.sum_univ_three] <;> norm_num

/-- Left-orthogonality of `so3RotZ345`. -/
theorem so3RotZ345_orth2 : so3RotZ345ᵀ * so3RotZ345 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [so3RotZ345, Matrix.mul_apply, Fin.sum_univ_three] <;> norm_num

/-- Certificate bundling coherent `SO(3)` orthogonal cocycle composition bounds. -/
structure BianchiCocycleCert where
  v : Matrix (Fin 3) (Fin 3) ℚ
  w : Matrix (Fin 3) (Fin 3) ℚ
  x : Matrix (Fin 3) (Fin 3) ℚ
  hv1 : v * vᵀ = 1
  hv2 : vᵀ * v = 1
  hw1 : w * wᵀ = 1
  hw2 : wᵀ * w = 1
  hx : frobSq x ≠ 0

/-- Canonical coherent 3-4-5 `SO(3)` rotation witness (`δ_V = 2/5, δ_{V^2} = 32/25`). -/
def canonicalBianchiCocycleCert : BianchiCocycleCert where
  v := so3RotZ345
  w := so3RotZ345
  x := so3GenX
  hv1 := so3RotZ345_orth1
  hv2 := so3RotZ345_orth2
  hw1 := so3RotZ345_orth1
  hw2 := so3RotZ345_orth2
  hx := by
    unfold frobSq so3GenX Matrix.trace
    simp only [Matrix.diag_apply, Matrix.mul_apply, Matrix.transpose_apply,
      Fin.sum_univ_three]
    norm_num

instance : Nonempty BianchiCocycleCert :=
  ⟨canonicalBianchiCocycleCert⟩

/-- Exact normalized loss `2 / 5` for `so3RotZ345` acting on `so3GenX`. -/
theorem canonical_cocycle_dV_eq :
    normalizedLoss so3RotZ345 so3GenX = 2 / 5 := by
  unfold normalizedLoss frobSq matrixComm so3RotZ345 so3GenX Matrix.trace
  simp only [Matrix.diag_apply, Matrix.mul_apply, Matrix.transpose_apply, Matrix.sub_apply,
    Fin.sum_univ_three]
  norm_num

/-- Exact composed normalized loss `32 / 25` for `so3RotZ345 * so3RotZ345` on `so3GenX`. -/
theorem canonical_cocycle_dVV_eq :
    normalizedLoss (so3RotZ345 * so3RotZ345) so3GenX = 32 / 25 := by
  unfold normalizedLoss frobSq matrixComm so3RotZ345 so3GenX Matrix.trace
  simp only [Matrix.diag_apply, Matrix.mul_apply, Matrix.transpose_apply, Matrix.sub_apply,
    Fin.sum_univ_three]
  norm_num

/-- Exact positive cocycle remainder `+16 / 25` showing super-dyadic constructive coherence. -/
theorem canonical_cocycle_eps_eq :
    cocycleRemainder so3RotZ345 so3RotZ345 so3GenX = 16 / 25 := by
  have hsplit := cocycleLoss_split_eq so3RotZ345 so3RotZ345 so3GenX
    so3RotZ345_orth1 so3RotZ345_orth2 so3RotZ345_orth1 so3RotZ345_orth2
    canonicalBianchiCocycleCert.hx
  rw [canonical_cocycle_dV_eq, canonical_cocycle_dVV_eq] at hsplit
  linarith

/-- Super-dyadic witness: composed loss `32/25` strictly exceeds ideal dyadic `16/25`. -/
theorem canonical_cocycle_superdyadic_lt :
    dyadicLossStep (normalizedLoss so3RotZ345 so3GenX) <
      normalizedLoss (so3RotZ345 * so3RotZ345) so3GenX := by
  rw [canonical_cocycle_dV_eq, canonical_cocycle_dVV_eq]
  unfold dyadicLossStep
  norm_num

/-- **CONDITIONAL:** Once 4D Gibbs expectation bounds place normalized step losses in `[d, 1]`
and keep the cocycle remainder bounded below by `-(1 - c) * dyadicLossStep d`, the composed
loss preserves at least a `c`-fraction of the `YM141` dyadic amplification step. -/
theorem cocycle_dyadic_lower_bound_conditional (cert : BianchiCocycleCert) (c d : ℚ)
    (hdV0 : d ≤ normalizedLoss cert.v cert.x)
    (hdW0 : d ≤ normalizedLoss cert.w cert.x)
    (hdV1 : normalizedLoss cert.v cert.x ≤ 1)
    (hdW1 : normalizedLoss cert.w cert.x ≤ 1)
    (hrem : -(1 - c) * dyadicLossStep d ≤ cocycleRemainder cert.v cert.w cert.x) :
    c * dyadicLossStep d ≤ normalizedLoss (cert.v * cert.w) cert.x := by
  have hsplit := cocycleLoss_split_eq cert.v cert.w cert.x
    cert.hv1 cert.hv2 cert.hw1 cert.hw2 cert.hx
  exact dyadic_step_ge_of_remainder_bound hsplit hdV0 hdW0 hdV1 hdW1 hrem

end YangMillsBlueprint.Certificates
