/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Analysis.InnerProductSpace.PiL2
public import Mathlib.Tactic.FinCases
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.ConcreteHodgeInvolution
public import YangMillsBlueprint.MathlibStaging.LorentzianHodgeAndEnergy
public import YangMillsBlueprint.MathlibStaging.NonAbelianBianchiDefect

/-!
# 4D Quaternionic `Spin(4)` and Chiral Hodge Osterwalder-Schrader Reflection

Formalizes two core structural interactions of 4D Osterwalder-Schrader time reflection `θ`:

1. **Quaternionic `Spin(4) ≅ SU(2)_+ × SU(2)_-` (`QuaternionicSpin4`):**
   Represents `θ(q) = (-q₀, q₁, q₂, q₃) = -conj(q)` on `Quat4 R`, proving norm preservation,
   `2`-to-`1` double cover `(-uL, -uR)` invariance, and the chiral group-factor swap
   `osReflectQuat (spin4Act uL uR q) = spin4Act uR uL (osReflectQuat q)`.
2. **4D Curvature OS Reflection vs. Hodge Duality (`CurvatureOSReflection`):**
   On `(E, B) : EuclideanSpace ℝ (Fin 6)`, `osReflectCurv4D (E, B) = (-E, B)` anticommutes with
   Euclidean `hodge4D`, composes directly to Lorentzian `lorentzHodge4D` (`θ* ∘ ★_E = J_L`), swaps
   self-dual and anti-self-dual halves `P₊ ↔ P₋`, reverses Pontryagin density `⟪F, ★_E F⟫`, and
   renders both single-chirality sectors null (`⟪P₊ F, θ*(P₊ F)⟫ = 0 = ⟪P₋ F, θ*(P₋ F)⟫`) so OS
   reflection positivity necessarily couples both chiral halves.
-/

@[expose] public section

namespace QuaternionicOSReflection

open ConcreteHodgeInvolution LorentzianHodgeAndEnergy NonAbelianBianchiDefect
open SelfDualWaveProjection

section QuaternionicSpin4

/-- Additive negation on quaternions `Quat4 R`. -/
def quatNeg {R : Type*} [Neg R] (q : Quat4 R) : Quat4 R :=
  ⟨-q.q0, -q.q1, -q.q2, -q.q3⟩

/-- Quaternion conjugation `(q₀, q₁, q₂, q₃) ↦ (q₀, -q₁, -q₂, -q₃)`. -/
def quatConj {R : Type*} [Neg R] (q : Quat4 R) : Quat4 R :=
  ⟨q.q0, -q.q1, -q.q2, -q.q3⟩

/-- Standard Hamilton quaternion multiplication over any commutative ring `R`. -/
def quatMul {R : Type*} [Ring R] (a b : Quat4 R) : Quat4 R where
  q0 := a.q0 * b.q0 - a.q1 * b.q1 - a.q2 * b.q2 - a.q3 * b.q3
  q1 := a.q0 * b.q1 + a.q1 * b.q0 + a.q2 * b.q3 - a.q3 * b.q2
  q2 := a.q0 * b.q2 - a.q1 * b.q3 + a.q2 * b.q0 + a.q3 * b.q1
  q3 := a.q0 * b.q3 + a.q1 * b.q2 - a.q2 * b.q1 + a.q3 * b.q0

/-- 4D Osterwalder-Schrader Euclidean time reflection `θ(q) = (-q₀, q₁, q₂, q₃)`. -/
def osReflectQuat {R : Type*} [Neg R] (q : Quat4 R) : Quat4 R :=
  ⟨-q.q0, q.q1, q.q2, q.q3⟩

/-- `Spin(4) ≅ SU(2)_+ × SU(2)_-` action `q ↦ uL * q * conj(uR)`. -/
def spin4Act {R : Type*} [Ring R] (uL uR q : Quat4 R) : Quat4 R :=
  quatMul (quatMul uL q) (quatConj uR)

theorem quatNormSq_neg {R : Type*} [CommRing R] (q : Quat4 R) :
    quatNormSq (quatNeg q) = quatNormSq q := by
  unfold quatNormSq quatNeg
  ring

theorem quatNormSq_conj {R : Type*} [CommRing R] (q : Quat4 R) :
    quatNormSq (quatConj q) = quatNormSq q := by
  unfold quatNormSq quatConj
  ring

theorem quatNormSq_mul {R : Type*} [CommRing R] (a b : Quat4 R) :
    quatNormSq (quatMul a b) = quatNormSq a * quatNormSq b := by
  unfold quatNormSq quatMul
  ring

theorem quatConj_mul {R : Type*} [CommRing R] (a b : Quat4 R) :
    quatConj (quatMul a b) = quatMul (quatConj b) (quatConj a) := by
  unfold quatConj quatMul
  congr 1 <;> ring

theorem osReflectQuat_eq_neg_conj {R : Type*} [CommRing R] (q : Quat4 R) :
    osReflectQuat q = quatNeg (quatConj q) := by
  unfold osReflectQuat quatNeg quatConj
  congr 1 <;> ring

theorem osReflectQuat_invol {R : Type*} [CommRing R] (q : Quat4 R) :
    osReflectQuat (osReflectQuat q) = q := by
  rcases q with ⟨q0, q1, q2, q3⟩
  simp [osReflectQuat]

theorem quatNormSq_osReflect {R : Type*} [CommRing R] (q : Quat4 R) :
    quatNormSq (osReflectQuat q) = quatNormSq q := by
  unfold quatNormSq osReflectQuat
  ring

theorem quatNormSq_spin4Act {R : Type*} [CommRing R] {uL uR q : Quat4 R}
    (huL : quatNormSq uL = 1) (huR : quatNormSq uR = 1) :
    quatNormSq (spin4Act uL uR q) = quatNormSq q := by
  rw [spin4Act, quatNormSq_mul, quatNormSq_mul, quatNormSq_conj, huL, huR, one_mul, mul_one]

theorem spin4Act_doubleCover {R : Type*} [CommRing R] (uL uR q : Quat4 R) :
    spin4Act (quatNeg uL) (quatNeg uR) q = spin4Act uL uR q := by
  unfold spin4Act quatMul quatNeg quatConj
  congr 1 <;> ring

/-- OS time reflection swaps the left and right `SU(2)` spinor factors of `Spin(4)`. -/
theorem osReflectQuat_spin4Act {R : Type*} [CommRing R] (uL uR q : Quat4 R) :
    osReflectQuat (spin4Act uL uR q) = spin4Act uR uL (osReflectQuat q) := by
  unfold osReflectQuat spin4Act quatMul quatConj
  congr 1 <;> ring

end QuaternionicSpin4

section CurvatureOSReflection

/-- 4D OS time reflection `θ*(E, B) = (-E, B)` on `EuclideanSpace ℝ (Fin 6)`. -/
def osReflectCurv4D :
    EuclideanSpace ℝ (Fin 6) →ₗ[ℝ] EuclideanSpace ℝ (Fin 6) where
  toFun F := WithLp.toLp 2 fun i : Fin 6 => if (i : ℕ) < 3 then -F i else F i
  map_add' F G := by
    ext i
    by_cases h : (i : ℕ) < 3
    · simp [h]
      ring
    · simp [h]
  map_smul' c F := by
    ext i
    by_cases h : (i : ℕ) < 3 <;> simp [h]

@[simp]
theorem osReflectCurv4D_apply_lt (F : EuclideanSpace ℝ (Fin 6)) {i : Fin 6}
    (h : (i : ℕ) < 3) :
    osReflectCurv4D F i = -F i := by
  simp [osReflectCurv4D, h]

@[simp]
theorem osReflectCurv4D_apply_ge (F : EuclideanSpace ℝ (Fin 6)) {i : Fin 6}
    (h : ¬ ((i : ℕ) < 3)) :
    osReflectCurv4D F i = F i := by
  simp [osReflectCurv4D, h]

/-- `osReflectCurv4D` is an unconditional `SymmInvolution` (`(θ*)² = id`, `(θ*)ᵀ = θ*`). -/
theorem symmInvolution_osReflectCurv4D : SymmInvolution osReflectCurv4D where
  invol F := by
    ext i
    fin_cases i <;> simp [osReflectCurv4D]
  symm F G := by
    simp only [EuclideanSpace.inner_eq_star_dotProduct, dotProduct, star_trivial, Fin.sum_univ_six]
    simp [osReflectCurv4D]

/-- Composing OS reflection with Euclidean Hodge yields Lorentzian Hodge: `θ* ∘ ★_E = J_L`. -/
theorem osReflectCurv4D_comp_hodge4D (F : EuclideanSpace ℝ (Fin 6)) :
    osReflectCurv4D (hodge4D F) = lorentzHodge4D F := by
  ext i
  fin_cases i <;> simp [osReflectCurv4D, hodge4D, halfSwap, swapIdx, lorentzHodge4D]

/-- Composing Euclidean Hodge with OS reflection yields negated Lorentzian Hodge:
`★_E ∘ θ* = -J_L`. -/
theorem hodge4D_comp_osReflectCurv4D (F : EuclideanSpace ℝ (Fin 6)) :
    hodge4D (osReflectCurv4D F) = -lorentzHodge4D F := by
  ext i
  fin_cases i <;> simp [osReflectCurv4D, hodge4D, halfSwap, swapIdx, lorentzHodge4D]

/-- OS reflection strictly anticommutes with 4D Euclidean Hodge: `θ*(★_E F) = -★_E(θ* F)`. -/
theorem osReflectCurv4D_anticomm_hodge4D (F : EuclideanSpace ℝ (Fin 6)) :
    osReflectCurv4D (hodge4D F) = -hodge4D (osReflectCurv4D F) := by
  rw [osReflectCurv4D_comp_hodge4D, hodge4D_comp_osReflectCurv4D, neg_neg]

/-- OS reflection maps self-dual 2-forms onto anti-self-dual 2-forms. -/
theorem osReflectCurv4D_projPlus (F : EuclideanSpace ℝ (Fin 6)) :
    osReflectCurv4D (projPlus hodge4D F) = projMinus hodge4D (osReflectCurv4D F) := by
  unfold projPlus projMinus
  rw [map_smul, map_add, osReflectCurv4D_anticomm_hodge4D, ← sub_eq_add_neg]

/-- OS reflection maps anti-self-dual 2-forms onto self-dual 2-forms. -/
theorem osReflectCurv4D_projMinus (F : EuclideanSpace ℝ (Fin 6)) :
    osReflectCurv4D (projMinus hodge4D F) = projPlus hodge4D (osReflectCurv4D F) := by
  unfold projPlus projMinus
  rw [map_smul, map_sub, osReflectCurv4D_anticomm_hodge4D, sub_neg_eq_add]

/-- Euclidean Yang-Mills action norm is OS-reflection invariant: `‖θ* F‖² = ‖F‖²`. -/
theorem osReflectCurv4D_norm_sq (F : EuclideanSpace ℝ (Fin 6)) :
    ‖osReflectCurv4D F‖ ^ 2 = ‖F‖ ^ 2 := by
  rw [← real_inner_self_eq_norm_sq, ← real_inner_self_eq_norm_sq,
    symmInvolution_osReflectCurv4D.symm, symmInvolution_osReflectCurv4D.invol]

/-- Pontryagin topological density is odd under OS reflection:
`⟪θ* F, ★_E(θ* F)⟫ = -⟪F, ★_E F⟫`. -/
theorem osReflectCurv4D_pontryagin_neg (F : EuclideanSpace ℝ (Fin 6)) :
    inner ℝ (osReflectCurv4D F) (hodge4D (osReflectCurv4D F)) = -inner ℝ F (hodge4D F) := by
  have hneg : hodge4D (osReflectCurv4D F) = -osReflectCurv4D (hodge4D F) := by
    rw [osReflectCurv4D_anticomm_hodge4D, neg_neg]
  rw [hneg, inner_neg_right, symmInvolution_osReflectCurv4D.symm,
    symmInvolution_osReflectCurv4D.invol]

/-- Pure self-dual sector is identically null under OS reflection: `⟪P₊ F, θ*(P₊ F)⟫ = 0`. -/
theorem inner_sd_osReflect_eq_zero (F : EuclideanSpace ℝ (Fin 6)) :
    inner ℝ (projPlus hodge4D F) (osReflectCurv4D (projPlus hodge4D F)) = 0 := by
  simp only [EuclideanSpace.inner_eq_star_dotProduct, dotProduct, star_trivial, Fin.sum_univ_six]
  simp [projPlus, osReflectCurv4D, hodge4D, halfSwap, swapIdx]
  ring

/-- Pure anti-self-dual sector is identically null under OS reflection: `⟪P₋ F, θ*(P₋ F)⟫ = 0`. -/
theorem inner_asd_osReflect_eq_zero (F : EuclideanSpace ℝ (Fin 6)) :
    inner ℝ (projMinus hodge4D F) (osReflectCurv4D (projMinus hodge4D F)) = 0 := by
  simp only [EuclideanSpace.inner_eq_star_dotProduct, dotProduct, star_trivial, Fin.sum_univ_six]
  simp [projMinus, osReflectCurv4D, hodge4D, halfSwap, swapIdx]
  ring

/-- OS reflection pairing lives purely in the cross-chiral `P₊ ↔ P₋` pairing:
`⟪F, θ* F⟫ = 2 * ⟪P₊ F, θ*(P₋ F)⟫`. -/
theorem inner_osReflect_eq_two_cross_chiral (F : EuclideanSpace ℝ (Fin 6)) :
    inner ℝ F (osReflectCurv4D F) =
      2 * inner ℝ (projPlus hodge4D F) (osReflectCurv4D (projMinus hodge4D F)) := by
  simp only [EuclideanSpace.inner_eq_star_dotProduct, dotProduct, star_trivial, Fin.sum_univ_six]
  simp [projPlus, projMinus, osReflectCurv4D, hodge4D, halfSwap, swapIdx]
  ring

end CurvatureOSReflection

end QuaternionicOSReflection
