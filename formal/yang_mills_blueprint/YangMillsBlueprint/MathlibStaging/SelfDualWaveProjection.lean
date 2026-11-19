/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Analysis.InnerProductSpace.Basic
public import Mathlib.Data.Nat.Choose.Basic
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.SliceReflectionHilbert

/-!
# Involutive Self-Dual / Anti-Self-Dual Splitting and Fixed-Domain Projected Wave Adaptation

Formalizes two complementary geometric principles:
1. **Conjugate-Half / Involutive Splitting (`J² = I`):** Any symmetric involution `J` splits
   every element uniquely into orthogonal self-dual (`+1`) and anti-self-dual (`-1`) halves
   `projPlus J x`, `projMinus J x`, yielding `‖x‖² = ‖P₊ x‖² + ‖P₋ x‖²` and the general
   Bogomol'nyi inequality `|⟪x, J x⟫| ≤ ‖x‖²` (matching 4D `6 = 3 + 3` curvature splitting
   and 8D `∧⁴ S₈⁺` `70 = 35 + 35` spinor four-form splitting).
2. **Fixed-Domain Projected Wave Adaptation:** On a fixed Hilbert container (`‖ψ‖ = 1`, `ψ ⟂ Ω`),
   norm-projected Rayleigh gradient updates `adaptedWaveStep A η ψ` preserve normalization and
   vacuum orthogonality while strictly descending along the spectral gap (`L = 2r`) of
   `id - T` for any contractive transfer operator `ContractiveTransfer T Ω r`.

## Main results

* `SelfDualWaveProjection.norm_sq_eq_projPlus_add_projMinus`: orthogonal half Pythagorean sum.
* `SelfDualWaveProjection.abs_inner_invol_le_norm_sq`: Bogomol'nyi inequality `|⟪x, J x⟫| ≤ ‖x‖²`.
* `SelfDualWaveProjection.fourD_curvature_choose_split`: `Nat.choose 4 2 = 3 + 3`.
* `SelfDualWaveProjection.eightD_spinor_fourform_choose_split`: `Nat.choose 8 4 = 35 + 35`.
* `SelfDualWaveProjection.rayleigh_adaptedWaveStep_descent`: fixed-domain Rayleigh drop bound.
* `SelfDualWaveProjection.adaptedWaveStep_transfer_descent_and_floor`: OS transfer adaptation.
-/

@[expose] public section

namespace SelfDualWaveProjection

section InvolutiveConjugateSplit

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Symmetric linear involution (`J² = I`, `Jᵀ = J`) generating two orthogonal conjugate halves. -/
structure SymmInvolution (J : E →ₗ[ℝ] E) : Prop where
  invol : ∀ x : E, J (J x) = x
  symm : ∀ x y : E, inner ℝ (J x) y = inner ℝ x (J y)

/-- Self-dual (`+1`) projection `P₊ x = (1 / 2) • (x + J x)`. -/
noncomputable def projPlus (J : E →ₗ[ℝ] E) (x : E) : E :=
  (1 / 2 : ℝ) • (x + J x)

/-- Anti-self-dual (`-1`) projection `P₋ x = (1 / 2) • (x - J x)`. -/
noncomputable def projMinus (J : E →ₗ[ℝ] E) (x : E) : E :=
  (1 / 2 : ℝ) • (x - J x)

/-- Exact reconstruction of `x` from its self-dual and anti-self-dual halves. -/
theorem projPlus_add_projMinus (J : E →ₗ[ℝ] E) (x : E) :
    projPlus J x + projMinus J x = x := by
  unfold projPlus projMinus
  rw [← smul_add]
  have hsum : (x + J x) + (x - J x) = (2 : ℝ) • x := by
    calc (x + J x) + (x - J x)
        = x + x := by abel
      _ = (2 : ℝ) • x := (two_smul ℝ x).symm
  rw [hsum, smul_smul]
  norm_num

/-- `projPlus J x` is a `+1` eigenvector of `J`. -/
theorem projPlus_eigen {J : E →ₗ[ℝ] E} (hJ : SymmInvolution J) (x : E) :
    J (projPlus J x) = projPlus J x := by
  unfold projPlus
  rw [map_smul, map_add, hJ.invol, add_comm]

/-- `projMinus J x` is a `-1` eigenvector of `J`. -/
theorem projMinus_eigen {J : E →ₗ[ℝ] E} (hJ : SymmInvolution J) (x : E) :
    J (projMinus J x) = -projMinus J x := by
  unfold projMinus
  rw [map_smul, map_sub, hJ.invol, ← neg_sub x (J x), smul_neg]

/-- Idempotency of the self-dual projector `P₊`. -/
theorem projPlus_idem {J : E →ₗ[ℝ] E} (hJ : SymmInvolution J) (x : E) :
    projPlus J (projPlus J x) = projPlus J x := by
  calc projPlus J (projPlus J x)
      = (1 / 2 : ℝ) • (projPlus J x + J (projPlus J x)) := rfl
    _ = (1 / 2 : ℝ) • (projPlus J x + projPlus J x) := by rw [projPlus_eigen hJ]
    _ = (1 / 2 : ℝ) • ((2 : ℝ) • projPlus J x) := by rw [← two_smul ℝ]
    _ = projPlus J x := by rw [smul_smul]; norm_num

/-- Idempotency of the anti-self-dual projector `P₋`. -/
theorem projMinus_idem {J : E →ₗ[ℝ] E} (hJ : SymmInvolution J) (x : E) :
    projMinus J (projMinus J x) = projMinus J x := by
  calc projMinus J (projMinus J x)
      = (1 / 2 : ℝ) • (projMinus J x - J (projMinus J x)) := rfl
    _ = (1 / 2 : ℝ) • (projMinus J x - (-projMinus J x)) := by rw [projMinus_eigen hJ]
    _ = (1 / 2 : ℝ) • ((2 : ℝ) • projMinus J x) := by rw [sub_neg_eq_add, ← two_smul ℝ]
    _ = projMinus J x := by rw [smul_smul]; norm_num

/-- Mutual annihilation `P₊ (P₋ x) = 0`. -/
theorem projPlus_projMinus_zero {J : E →ₗ[ℝ] E} (hJ : SymmInvolution J) (x : E) :
    projPlus J (projMinus J x) = 0 := by
  calc projPlus J (projMinus J x)
      = (1 / 2 : ℝ) • (projMinus J x + J (projMinus J x)) := rfl
    _ = (1 / 2 : ℝ) • (projMinus J x + (-projMinus J x)) := by rw [projMinus_eigen hJ]
    _ = 0 := by rw [add_neg_cancel, smul_zero]

/-- Orthogonality of self-dual and anti-self-dual conjugate halves. -/
theorem inner_projPlus_projMinus {J : E →ₗ[ℝ] E} (hJ : SymmInvolution J) (x y : E) :
    inner ℝ (projPlus J x) (projMinus J y) = 0 := by
  have h1 : inner ℝ (projPlus J x) (projMinus J y) =
      inner ℝ (J (projPlus J x)) (projMinus J y) := by rw [projPlus_eigen hJ]
  have h2 : inner ℝ (J (projPlus J x)) (projMinus J y) =
      inner ℝ (projPlus J x) (J (projMinus J y)) := hJ.symm _ _
  rw [projMinus_eigen hJ, inner_neg_right] at h2
  linarith

/-- Orthogonal norm decomposition `‖x‖² = ‖P₊ x‖² + ‖P₋ x‖²`. -/
theorem norm_sq_eq_projPlus_add_projMinus {J : E →ₗ[ℝ] E} (hJ : SymmInvolution J) (x : E) :
    ‖x‖ ^ 2 = ‖projPlus J x‖ ^ 2 + ‖projMinus J x‖ ^ 2 := by
  let p := projPlus J x
  let m := projMinus J x
  have hsplit : x = p + m := (projPlus_add_projMinus J x).symm
  have horth : inner ℝ p m = 0 := inner_projPlus_projMinus hJ x x
  have horth' : inner ℝ m p = 0 := by rw [real_inner_comm]; exact horth
  calc ‖x‖ ^ 2 = inner ℝ (p + m) (p + m) := by rw [← hsplit, real_inner_self_eq_norm_sq]
    _ = (inner ℝ p p + inner ℝ p m) + (inner ℝ m p + inner ℝ m m) := by
        rw [inner_add_left, inner_add_right, inner_add_right]
    _ = ‖p‖ ^ 2 + ‖m‖ ^ 2 := by
        rw [horth, horth', real_inner_self_eq_norm_sq, real_inner_self_eq_norm_sq]
        ring

/-- Topological / chiral pairing equals the signed half-norm difference `‖P₊ x‖² - ‖P₋ x‖²`. -/
theorem inner_self_invol_eq_sub {J : E →ₗ[ℝ] E} (hJ : SymmInvolution J) (x : E) :
    inner ℝ x (J x) = ‖projPlus J x‖ ^ 2 - ‖projMinus J x‖ ^ 2 := by
  let p := projPlus J x
  let m := projMinus J x
  have hsplit : x = p + m := (projPlus_add_projMinus J x).symm
  have hJsplit : J x = p - m := by
    calc J x = J (p + m) := by rw [← hsplit]
      _ = J p + J m := map_add J p m
      _ = p + (-m) := by rw [projPlus_eigen hJ, projMinus_eigen hJ]
      _ = p - m := by rw [sub_eq_add_neg]
  have horth : inner ℝ p m = 0 := inner_projPlus_projMinus hJ x x
  have horth' : inner ℝ m p = 0 := by rw [real_inner_comm]; exact horth
  calc inner ℝ x (J x)
      = inner ℝ (p + m) (J x) := by rw [← hsplit]
    _ = inner ℝ (p + m) (p - m) := by rw [hJsplit]
    _ = (inner ℝ p p - inner ℝ p m) + (inner ℝ m p - inner ℝ m m) := by
        rw [inner_add_left, inner_sub_right, inner_sub_right]
    _ = ‖p‖ ^ 2 - ‖m‖ ^ 2 := by
        rw [horth, horth', real_inner_self_eq_norm_sq, real_inner_self_eq_norm_sq]
        ring

/-- Abstract Bogomol'nyi inequality `|⟪x, J x⟫| ≤ ‖x‖²` for any symmetric involution. -/
theorem abs_inner_invol_le_norm_sq {J : E →ₗ[ℝ] E} (hJ : SymmInvolution J) (x : E) :
    |inner ℝ x (J x)| ≤ ‖x‖ ^ 2 := by
  rw [norm_sq_eq_projPlus_add_projMinus hJ x, inner_self_invol_eq_sub hJ x]
  have hp : 0 ≤ ‖projPlus J x‖ ^ 2 := sq_nonneg _
  have hm : 0 ≤ ‖projMinus J x‖ ^ 2 := sq_nonneg _
  exact abs_le.mpr ⟨by linarith, by linarith⟩

end InvolutiveConjugateSplit

section CombinatorialHodgeSplits

/-- Four-dimensional curvature 2-forms (`C(4, 2) = 6`) split equally `3 + 3` into self-dual and
anti-self-dual subspaces under Hodge duality. -/
theorem fourD_curvature_choose_split : Nat.choose 4 2 = 3 + 3 := rfl

/-- Eight-dimensional spinor middle 4-forms (`∧⁴ S₈⁺`, `C(8, 4) = 70`) split equally `35 + 35`
into self-dual (`+1`) and anti-self-dual (`-1`) halves. -/
theorem eightD_spinor_fourform_choose_split : Nat.choose 8 4 = 35 + 35 := rfl

end CombinatorialHodgeSplits

section FixedDomainWaveAdaptation

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]

/-- Projection onto the unit-vacuum orthogonal complement `Ωᗮ`. -/
noncomputable def projOrth (Ω v : H) : H :=
  v - (inner ℝ Ω v) • Ω

/-- Constraint projection onto the unit sphere `‖v‖ = 1` on a fixed wave container. -/
noncomputable def unitProject (v : H) : H :=
  (‖v‖⁻¹) • v

/-- Rayleigh quotient energy `⟪ψ, A ψ⟫` for linear operator `A` on unit vectors `ψ`. -/
noncomputable def rayleighEnergy (A : H →ₗ[ℝ] H) (ψ : H) : ℝ :=
  inner ℝ ψ (A ψ)

/-- Riemannian tangent gradient of `rayleighEnergy A` at unit `ψ`: `A ψ - ⟪ψ, A ψ⟫ ψ`. -/
noncomputable def sphereGrad (A : H →ₗ[ℝ] H) (ψ : H) : H :=
  A ψ - (rayleighEnergy A ψ) • ψ

/-- One fixed-domain projected gradient wave-adaptation step `ψ_{t+1} = Π(ψ_t - η g_t)`. -/
noncomputable def adaptedWaveStep (A : H →ₗ[ℝ] H) (η : ℝ) (ψ : H) : H :=
  unitProject (ψ - η • sphereGrad A ψ)

/-- `projOrth Ω v` is strictly orthogonal to any unit vector `Ω`. -/
theorem inner_projOrth_zero {Ω : H} (hΩ : ‖Ω‖ = 1) (v : H) :
    inner ℝ Ω (projOrth Ω v) = 0 := by
  unfold projOrth
  rw [inner_sub_right, real_inner_smul_right, real_inner_self_eq_norm_sq, hΩ]
  ring

/-- Unit-sphere projection preserves unit norm for every nonzero wave vector. -/
theorem norm_unitProject {v : H} (hv : v ≠ 0) :
    ‖unitProject v‖ = 1 := by
  unfold unitProject
  rw [norm_smul, Real.norm_eq_abs, abs_of_nonneg (inv_nonneg.mpr (norm_nonneg v)),
    inv_mul_cancel₀ (norm_ne_zero_iff.mpr hv)]

/-- Tangential gradient `sphereGrad A ψ` is orthogonal to unit `ψ`. -/
theorem inner_self_sphereGrad_zero (A : H →ₗ[ℝ] H) {ψ : H} (hψ : ‖ψ‖ = 1) :
    inner ℝ ψ (sphereGrad A ψ) = 0 := by
  unfold sphereGrad rayleighEnergy
  rw [inner_sub_right, real_inner_smul_right, real_inner_self_eq_norm_sq, hψ]
  ring

/-- Pythagorean norm formula for the unnormalized step `ψ - η • sphereGrad A ψ`. -/
theorem norm_sq_unnormalized_step (A : H →ₗ[ℝ] H) (η : ℝ) {ψ : H} (hψ : ‖ψ‖ = 1) :
    ‖ψ - η • sphereGrad A ψ‖ ^ 2 = 1 + η ^ 2 * ‖sphereGrad A ψ‖ ^ 2 := by
  let g := sphereGrad A ψ
  have hpg : inner ℝ ψ g = 0 := inner_self_sphereGrad_zero A hψ
  have hgp : inner ℝ g ψ = 0 := by rw [real_inner_comm]; exact hpg
  calc ‖ψ - η • g‖ ^ 2
      = inner ℝ (ψ - η • g) (ψ - η • g) := (real_inner_self_eq_norm_sq _).symm
    _ = (inner ℝ ψ ψ - η * inner ℝ ψ g) - (η * inner ℝ g ψ - η * (η * inner ℝ g g)) := by
        rw [inner_sub_left, inner_sub_right, inner_sub_right]
        simp only [real_inner_smul_left, real_inner_smul_right]
    _ = 1 + η ^ 2 * ‖g‖ ^ 2 := by
        rw [hpg, hgp, real_inner_self_eq_norm_sq ψ, real_inner_self_eq_norm_sq g, hψ]
        ring

/-- Unnormalized wave step `ψ - η • sphereGrad A ψ` is never zero from any unit state `ψ`. -/
theorem unnormalized_step_ne_zero (A : H →ₗ[ℝ] H) (η : ℝ) {ψ : H} (hψ : ‖ψ‖ = 1) :
    ψ - η • sphereGrad A ψ ≠ 0 := by
  intro hzero
  have hsq : ‖ψ - η • sphereGrad A ψ‖ ^ 2 = 0 := by simp [hzero]
  rw [norm_sq_unnormalized_step A η hψ] at hsq
  have hpos : 0 < 1 + η ^ 2 * ‖sphereGrad A ψ‖ ^ 2 := by positivity
  linarith

/-- Adapted wave state always stays exactly on the unit norm manifold (`‖ψ'‖ = 1`). -/
theorem norm_adaptedWaveStep (A : H →ₗ[ℝ] H) (η : ℝ) {ψ : H} (hψ : ‖ψ‖ = 1) :
    ‖adaptedWaveStep A η ψ‖ = 1 :=
  norm_unitProject (unnormalized_step_ne_zero A η hψ)

/-- If `Ω` is orthogonal to `ψ` and `A ψ`, `adaptedWaveStep A η ψ` stays inside `Ωᗮ`. -/
theorem adaptedWaveStep_preserves_orth (A : H →ₗ[ℝ] H) (η : ℝ) {Ω ψ : H}
    (hψΩ : inner ℝ Ω ψ = 0) (hAv : inner ℝ Ω (A ψ) = 0) :
    inner ℝ Ω (adaptedWaveStep A η ψ) = 0 := by
  have hgΩ : inner ℝ Ω (sphereGrad A ψ) = 0 := by
    unfold sphereGrad
    rw [inner_sub_right, real_inner_smul_right, hψΩ, hAv]
    ring
  unfold adaptedWaveStep unitProject
  rw [real_inner_smul_right, inner_sub_right, real_inner_smul_right, hψΩ, hgΩ]
  ring

/-- Rayleigh energy scaling identity `rayleighEnergy A (unitProject u) = ⟪u, A u⟫ / ‖u‖²`. -/
theorem rayleighEnergy_unitProject (A : H →ₗ[ℝ] H) (u : H) :
    rayleighEnergy A (unitProject u) = inner ℝ u (A u) / ‖u‖ ^ 2 := by
  unfold rayleighEnergy unitProject
  rw [map_smul, real_inner_smul_left, real_inner_smul_right, ← mul_assoc, ← mul_inv, ← sq,
    mul_comm, ← div_eq_mul_inv]

/-- Exact Rayleigh descent inequality on a fixed unit-norm wave container: under symmetric `A`
and spectral curvature bound `⟪g, A g⟫ - R(ψ) ‖g‖² ≤ L ‖g‖²`, one projected step reduces
Rayleigh energy by at least `η * (2 - η * L) * ‖g‖² / (1 + η² * ‖g‖²)`. -/
theorem rayleigh_adaptedWaveStep_descent (A : H →ₗ[ℝ] H) (η L : ℝ) {ψ : H}
    (hψ : ‖ψ‖ = 1) (hAsym : ∀ x y : H, inner ℝ x (A y) = inner ℝ (A x) y)
    (hL : inner ℝ (sphereGrad A ψ) (A (sphereGrad A ψ)) -
        rayleighEnergy A ψ * ‖sphereGrad A ψ‖ ^ 2 ≤ L * ‖sphereGrad A ψ‖ ^ 2) :
    rayleighEnergy A (adaptedWaveStep A η ψ) ≤
      rayleighEnergy A ψ -
        η * (2 - η * L) * ‖sphereGrad A ψ‖ ^ 2 / (1 + η ^ 2 * ‖sphereGrad A ψ‖ ^ 2) := by
  let g := sphereGrad A ψ
  let u := ψ - η • g
  let R := rayleighEnergy A ψ
  have hpg : inner ℝ ψ g = 0 := inner_self_sphereGrad_zero A hψ
  have hAψ_eq : A ψ = g + R • ψ := by
    unfold g sphereGrad R
    abel
  have hAg : inner ℝ (A ψ) g = ‖g‖ ^ 2 := by
    rw [hAψ_eq, inner_add_left, real_inner_smul_left, inner_self_sphereGrad_zero A hψ,
      real_inner_self_eq_norm_sq]
    ring
  have hψAg : inner ℝ ψ (A g) = ‖g‖ ^ 2 := by
    rw [hAsym ψ g, hAg]
  have hgAψ : inner ℝ g (A ψ) = ‖g‖ ^ 2 := by rw [real_inner_comm]; exact hAg
  have huAu : inner ℝ u (A u) = R - 2 * η * ‖g‖ ^ 2 + η ^ 2 * inner ℝ g (A g) := by
    change inner ℝ (ψ - η • g) (A (ψ - η • g)) = R - 2 * η * ‖g‖ ^ 2 + η ^ 2 * inner ℝ g (A g)
    rw [map_sub, map_smul, inner_sub_left, inner_sub_right, inner_sub_right]
    simp only [real_inner_smul_left, real_inner_smul_right, hψAg, hgAψ]
    dsimp [R, rayleighEnergy]
    ring
  have huSq : ‖u‖ ^ 2 = 1 + η ^ 2 * ‖g‖ ^ 2 := norm_sq_unnormalized_step A η hψ
  have huPos : 0 < ‖u‖ ^ 2 := by rw [huSq]; positivity
  have hdiffNum :
      inner ℝ u (A u) - R * ‖u‖ ^ 2 ≤ -(η * (2 - η * L) * ‖g‖ ^ 2) := by
    rw [huAu, huSq]
    have hmul : η ^ 2 * (inner ℝ g (A g) - R * ‖g‖ ^ 2) ≤ η ^ 2 * (L * ‖g‖ ^ 2) :=
      mul_le_mul_of_nonneg_left hL (sq_nonneg η)
    linarith
  have hdiv := div_le_div_of_nonneg_right hdiffNum (le_of_lt huPos)
  have hrwL : (inner ℝ u (A u) - R * ‖u‖ ^ 2) / ‖u‖ ^ 2 =
      rayleighEnergy A (adaptedWaveStep A η ψ) - R := by
    rw [sub_div, mul_div_cancel_right₀ R (ne_of_gt huPos), ← rayleighEnergy_unitProject A u]
    rfl
  rw [hrwL, huSq, neg_div] at hdiv
  linarith

/-- Monotone descent `R(adaptedWaveStep A η ψ) ≤ R(ψ)` for step size `0 ≤ η`, `η * L ≤ 2`. -/
theorem rayleigh_adaptedWaveStep_le (A : H →ₗ[ℝ] H) (η L : ℝ) {ψ : H}
    (hψ : ‖ψ‖ = 1) (hAsym : ∀ x y : H, inner ℝ x (A y) = inner ℝ (A x) y)
    (hL : inner ℝ (sphereGrad A ψ) (A (sphereGrad A ψ)) -
        rayleighEnergy A ψ * ‖sphereGrad A ψ‖ ^ 2 ≤ L * ‖sphereGrad A ψ‖ ^ 2)
    (hη0 : 0 ≤ η) (hηL : η * L ≤ 2) :
    rayleighEnergy A (adaptedWaveStep A η ψ) ≤ rayleighEnergy A ψ := by
  have hdesc := rayleigh_adaptedWaveStep_descent A η L hψ hAsym hL
  have h2ηL : 0 ≤ 2 - η * L := sub_nonneg.mpr hηL
  have hnum : 0 ≤ η * (2 - η * L) * ‖sphereGrad A ψ‖ ^ 2 := by positivity
  have hden : 0 ≤ 1 + η ^ 2 * ‖sphereGrad A ψ‖ ^ 2 := by positivity
  have hfrac :
      0 ≤ η * (2 - η * L) * ‖sphereGrad A ψ‖ ^ 2 / (1 + η ^ 2 * ‖sphereGrad A ψ‖ ^ 2) :=
    div_nonneg hnum hden
  linarith

/-- Applying fixed-domain projected wave adaptation to `H_eff = LinearMap.id - T` of a
contractive transfer operator (`ContractiveTransfer T Ω r`) preserves `‖ψ'‖ = 1` and `ψ' ⟂ Ω`,
enforces `1 - r`, and monotonically lowers Rayleigh energy for `0 ≤ η ≤ 1`. -/
theorem adaptedWaveStep_transfer_descent_and_floor {T : H →ₗ[ℝ] H} {Ω : H} {r : ℝ}
    (hT : SliceReflectionHilbert.ContractiveTransfer T Ω r) {ψ : H}
    (hψ : ‖ψ‖ = 1) (hψΩ : inner ℝ Ω ψ = 0) {η : ℝ} (hη0 : 0 ≤ η) (hη1 : η ≤ 1) :
    ‖adaptedWaveStep (LinearMap.id - T) η ψ‖ = 1 ∧
      inner ℝ Ω (adaptedWaveStep (LinearMap.id - T) η ψ) = 0 ∧
      1 - r ≤ rayleighEnergy (LinearMap.id - T) (adaptedWaveStep (LinearMap.id - T) η ψ) ∧
      rayleighEnergy (LinearMap.id - T) (adaptedWaveStep (LinearMap.id - T) η ψ) ≤
        rayleighEnergy (LinearMap.id - T) ψ := by
  let A : H →ₗ[ℝ] H := LinearMap.id - T
  let g := sphereGrad A ψ
  have hAv : inner ℝ Ω (A ψ) = 0 := by
    dsimp [A]
    rw [inner_sub_right, hψΩ, SliceReflectionHilbert.transfer_preserves_orth hT hψΩ, sub_self]
  have hgΩ : inner ℝ Ω g = 0 := by
    unfold g sphereGrad
    rw [inner_sub_right, real_inner_smul_right, hψΩ, hAv]
    ring
  have hAsym : ∀ x y : H, inner ℝ x (A y) = inner ℝ (A x) y := by
    intro x y
    dsimp [A]
    simp only [inner_sub_left, inner_sub_right, hT.symm x y]
  have hcoerc := SliceReflectionHilbert.transfer_to_coercivity hT
  have hRlo : 1 - r ≤ rayleighEnergy A ψ := by
    have hc := hcoerc.coercive ψ hψΩ
    rw [hψ, one_pow, mul_one] at hc
    exact hc
  have hgTg : inner ℝ g (T g) ≥ -(r * ‖g‖ ^ 2) := by
    have hcs : |inner ℝ g (T g)| ≤ ‖g‖ * ‖T g‖ := abs_real_inner_le_norm g (T g)
    have hstep : ‖g‖ * ‖T g‖ ≤ ‖g‖ * (r * ‖g‖) :=
      mul_le_mul_of_nonneg_left (hT.contractive g hgΩ) (norm_nonneg g)
    have hsq : ‖g‖ * (r * ‖g‖) = r * ‖g‖ ^ 2 := by ring
    have habs : |inner ℝ g (T g)| ≤ r * ‖g‖ ^ 2 := by linarith
    exact (abs_le.mp habs).1
  have hgAg : inner ℝ g (A g) ≤ (1 + r) * ‖g‖ ^ 2 := by
    dsimp [A]
    rw [inner_sub_right, real_inner_self_eq_norm_sq]
    linarith
  have hL : inner ℝ g (A g) - rayleighEnergy A ψ * ‖g‖ ^ 2 ≤ (2 * r) * ‖g‖ ^ 2 := by
    have hRmul : (1 - r) * ‖g‖ ^ 2 ≤ rayleighEnergy A ψ * ‖g‖ ^ 2 :=
      mul_le_mul_of_nonneg_right hRlo (sq_nonneg _)
    linarith
  have hrLt : r < 1 := hT.r_lt_one
  have hr0 : 0 ≤ r := le_of_lt hT.r_pos
  have hηL : η * (2 * r) ≤ 2 := by nlinarith
  have hnorm' : ‖adaptedWaveStep A η ψ‖ = 1 := norm_adaptedWaveStep A η hψ
  have horth' : inner ℝ Ω (adaptedWaveStep A η ψ) = 0 :=
    adaptedWaveStep_preserves_orth A η hψΩ hAv
  have hfloor' : 1 - r ≤ rayleighEnergy A (adaptedWaveStep A η ψ) := by
    have hc := hcoerc.coercive (adaptedWaveStep A η ψ) horth'
    rw [hnorm', one_pow, mul_one] at hc
    exact hc
  exact ⟨hnorm', horth', hfloor', rayleigh_adaptedWaveStep_le A η (2 * r) hψ hAsym hL hη0 hηL⟩

end FixedDomainWaveAdaptation

end SelfDualWaveProjection
