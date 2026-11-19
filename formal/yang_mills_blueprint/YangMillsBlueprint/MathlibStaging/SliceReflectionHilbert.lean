/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Analysis.InnerProductSpace.Basic
public import Mathlib.Analysis.InnerProductSpace.Completion
public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.SpectralMassGapBridge

/-!
# Reflection-Positive Pre-Hilbert Quotient Completion and Transfer Contraction Gap

Constructs the genuine complete real Hilbert space `OSHilbert B := UniformSpace.Completion
(RPVector B)` associated to any symmetric positive-semidefinite bilinear form `B` on a real
vector space `V` (automatically quotienting out zero-norm null vectors via `SeparationQuotient`
and Cauchy completion), and proves exponential clustering and orthogonal coercivity
(`SpectralMassGapBridge.HasOrthogonalCoercivity`) for any symmetric contractive transfer map `T`.

## Main results

* `SliceReflectionHilbert.OSHilbert`: complete real inner-product space built from `(V, B)`.
* `SliceReflectionHilbert.osEmbed_inner`, `osEmbed_norm_sq`, `osEmbed_eq_zero_of_null`:
  isometric embedding and automatic annihilation of null vectors.
* `SliceReflectionHilbert.transfer_correlator_exp_decay`: geometric decay with rate `log (1 / r)`.
* `SliceReflectionHilbert.transfer_to_coercivity`: coercivity of `id - T` with gap `1 - r`.
-/

@[expose] public section

namespace SliceReflectionHilbert

section OSCompletion

/-- Symmetric positive-semidefinite real bilinear form on a real vector space `V`. -/
structure ReflectionPositiveForm (V : Type*) [AddCommGroup V] [Module ℝ V] where
  form : V →ₗ[ℝ] V →ₗ[ℝ] ℝ
  symm : ∀ x y : V, form y x = form x y
  pos : ∀ x : V, 0 ≤ form x x

/-- Semireducible type wrapper carrying the pre-inner-product structure induced by `B`. -/
def RPVector {V : Type*} [AddCommGroup V] [Module ℝ V]
    (_B : ReflectionPositiveForm V) : Type _ := V

instance instAddCommGroupRPVector {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : ReflectionPositiveForm V) : AddCommGroup (RPVector B) :=
  inferInstanceAs (AddCommGroup V)

instance instModuleRPVector {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : ReflectionPositiveForm V) : Module ℝ (RPVector B) :=
  inferInstanceAs (Module ℝ V)

/-- Positive-semidefinite real inner product core on `RPVector B`. -/
@[instance_reducible]
def toPreInnerCore {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : ReflectionPositiveForm V) : PreInnerProductSpace.Core ℝ (RPVector B) where
  inner x y := B.form x y
  conj_inner_symm x y := by
    change starRingEnd ℝ (B.form y x) = B.form x y
    simpa using B.symm x y
  re_inner_nonneg x := B.pos x
  add_left x y z := by
    let hx : V := x
    let hy : V := y
    let hz : V := z
    change B.form (hx + hy) hz = B.form hx hz + B.form hy hz
    rw [map_add, LinearMap.add_apply]
  smul_left x y c := by
    let hx : V := x
    let hy : V := y
    change B.form (c • hx) hy = starRingEnd ℝ c * B.form hx hy
    rw [starRingEnd_apply, star_trivial, map_smul, LinearMap.smul_apply, smul_eq_mul]

noncomputable instance instSeminormedAddCommGroupRPVector {V : Type*} [AddCommGroup V]
    [Module ℝ V] (B : ReflectionPositiveForm V) : SeminormedAddCommGroup (RPVector B) :=
  @InnerProductSpace.Core.toSeminormedAddCommGroup ℝ (RPVector B) _ _ _ (toPreInnerCore B)

noncomputable instance instInnerProductSpaceRPVector {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : ReflectionPositiveForm V) : InnerProductSpace ℝ (RPVector B) :=
  @InnerProductSpace.ofCore ℝ (RPVector B) _ _ _ (toPreInnerCore B)

/-- Complete real physical Hilbert space obtained by Hausdorff quotient & completion. -/
abbrev OSHilbert {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : ReflectionPositiveForm V) : Type _ :=
  UniformSpace.Completion (RPVector B)

/-- Canonical coercion helper `V → RPVector B`. -/
def toRP {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : ReflectionPositiveForm V) (x : V) : RPVector B :=
  x

/-- Canonical linear embedding from pre-Hilbert observables `V` into `OSHilbert B`. -/
noncomputable def osEmbed {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : ReflectionPositiveForm V) (x : V) : OSHilbert B :=
  (toRP B x : OSHilbert B)

/-- Inner product of embedded observables equals the reflection-positive bilinear form. -/
theorem osEmbed_inner {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : ReflectionPositiveForm V) (x y : V) :
    inner ℝ (osEmbed B x) (osEmbed B y) = B.form x y := by
  unfold osEmbed
  rw [UniformSpace.Completion.inner_coe (toRP B x) (toRP B y)]
  rfl

/-- Hilbert norm squared of an embedded observable equals its diagonal RP form value. -/
theorem osEmbed_norm_sq {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : ReflectionPositiveForm V) (x : V) :
    ‖osEmbed B x‖ ^ 2 = B.form x x := by
  rw [← real_inner_self_eq_norm_sq, osEmbed_inner]

/-- Any zero-norm null vector maps identically to `0` in `OSHilbert B`. -/
theorem osEmbed_eq_zero_of_null {V : Type*} [AddCommGroup V] [Module ℝ V]
    (B : ReflectionPositiveForm V) {x : V} (hx : B.form x x = 0) :
    osEmbed B x = 0 := by
  have hsq : ‖osEmbed B x‖ ^ 2 = 0 := by rw [osEmbed_norm_sq, hx]
  exact norm_eq_zero.mp (sq_eq_zero_iff.mp hsq)

end OSCompletion

section TransferContractionGap

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]

/-- Symmetric Markov / transfer operator fixing unit vacuum `Ω` with spectral contraction
`‖T ψ‖ ≤ r * ‖ψ‖` (`0 < r < 1`) on the orthogonal complement `Ωᗮ`. -/
structure ContractiveTransfer (T : H →ₗ[ℝ] H) (Ω : H) (r : ℝ) : Prop where
  r_pos : 0 < r
  r_lt_one : r < 1
  norm_vac : ‖Ω‖ = 1
  fixes_vac : T Ω = Ω
  symm : ∀ u v : H, inner ℝ u (T v) = inner ℝ (T u) v
  contractive : ∀ ψ : H, inner ℝ Ω ψ = 0 → ‖T ψ‖ ≤ r * ‖ψ‖

/-- Contractive symmetric transfer preserves orthogonality to the vacuum state `Ω`. -/
theorem transfer_preserves_orth {T : H →ₗ[ℝ] H} {Ω : H} {r : ℝ}
    (hT : ContractiveTransfer T Ω r) {ψ : H} (hψ : inner ℝ Ω ψ = 0) :
    inner ℝ Ω (T ψ) = 0 := by
  rw [hT.symm, hT.fixes_vac, hψ]

/-- Iterated transfer powers `T ^ n` preserve orthogonality to `Ω`. -/
theorem transfer_pow_preserves_orth {T : H →ₗ[ℝ] H} {Ω : H} {r : ℝ}
    (hT : ContractiveTransfer T Ω r) {ψ : H} (hψ : inner ℝ Ω ψ = 0) (n : ℕ) :
    inner ℝ Ω ((T ^ n) ψ) = 0 := by
  induction n with
  | zero => simpa using hψ
  | succ n ih =>
      rw [pow_succ', Module.End.mul_apply]
      exact transfer_preserves_orth hT ih

/-- Exponential norm contraction `‖(T ^ n) ψ‖ ≤ r ^ n * ‖ψ‖` on `Ωᗮ`. -/
theorem transfer_pow_norm_le {T : H →ₗ[ℝ] H} {Ω : H} {r : ℝ}
    (hT : ContractiveTransfer T Ω r) {ψ : H} (hψ : inner ℝ Ω ψ = 0) (n : ℕ) :
    ‖(T ^ n) ψ‖ ≤ r ^ n * ‖ψ‖ := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [pow_succ', Module.End.mul_apply]
      have horth := transfer_pow_preserves_orth hT hψ n
      have hstep := hT.contractive ((T ^ n) ψ) horth
      have hmul := mul_le_mul_of_nonneg_left ih (le_of_lt hT.r_pos)
      calc ‖T ((T ^ n) ψ)‖ ≤ r * ‖(T ^ n) ψ‖ := hstep
        _ ≤ r * (r ^ n * ‖ψ‖) := hmul
        _ = r ^ (n + 1) * ‖ψ‖ := by rw [pow_succ']; ring

/-- Exponential clustering bound with strictly positive decay rate `Δ = Real.log (1 / r)`:
`|⟪u, (T ^ n) v⟫_ℝ| ≤ exp (-Δ * n) * (‖u‖ * ‖v‖)` for `v ⟂ Ω`. -/
theorem transfer_correlator_exp_decay {T : H →ₗ[ℝ] H} {Ω : H} {r : ℝ}
    (hT : ContractiveTransfer T Ω r) (u : H) {v : H} (hv : inner ℝ Ω v = 0) (n : ℕ) :
    |inner ℝ u ((T ^ n) v)| ≤ Real.exp (-(Real.log (1 / r) * (n : ℝ))) * (‖u‖ * ‖v‖) ∧
      0 < Real.log (1 / r) := by
  have hcs : |inner ℝ u ((T ^ n) v)| ≤ ‖u‖ * ‖(T ^ n) v‖ :=
    abs_real_inner_le_norm u ((T ^ n) v)
  have hpow := transfer_pow_norm_le hT hv n
  have hbound : |inner ℝ u ((T ^ n) v)| ≤ r ^ n * (‖u‖ * ‖v‖) := by
    have hmul := mul_le_mul_of_nonneg_left hpow (norm_nonneg u)
    have hrw : ‖u‖ * (r ^ n * ‖v‖) = r ^ n * (‖u‖ * ‖v‖) := by ring
    linarith
  have hExpEq : r ^ n = Real.exp (-(Real.log (1 / r) * (n : ℝ))) := by
    rw [one_div, Real.log_inv]
    have hneg : -(-Real.log r * (n : ℝ)) = (n : ℝ) * Real.log r := by ring
    rw [hneg, Real.exp_nat_mul, Real.exp_log hT.r_pos]
  have hrate : 0 < Real.log (1 / r) :=
    Real.log_pos (one_lt_one_div hT.r_pos hT.r_lt_one)
  rw [← hExpEq]
  exact ⟨hbound, hrate⟩

/-- Any symmetric contractive transfer `T` induces orthogonal Hamiltonian coercivity
`SpectralMassGapBridge.HasOrthogonalCoercivity (id - T) Ω (1 - r)` on `H`. -/
theorem transfer_to_coercivity {T : H →ₗ[ℝ] H} {Ω : H} {r : ℝ}
    (hT : ContractiveTransfer T Ω r) :
    SpectralMassGapBridge.HasOrthogonalCoercivity (LinearMap.id - T) Ω (1 - r) where
  gap_pos := sub_pos.mpr hT.r_lt_one
  norm_vacuum := hT.norm_vac
  annihilates := by simp [hT.fixes_vac]
  symmetric_on_vacuum ψ := by
    simp only [LinearMap.sub_apply, LinearMap.id_apply, inner_sub_right, inner_sub_left,
      hT.symm ψ Ω]
  coercive ψ hψ := by
    simp only [LinearMap.sub_apply, LinearMap.id_apply, inner_sub_right,
      real_inner_self_eq_norm_sq]
    have hcs : inner ℝ ψ (T ψ) ≤ |inner ℝ ψ (T ψ)| := le_abs_self _
    have hnorm : |inner ℝ ψ (T ψ)| ≤ ‖ψ‖ * ‖T ψ‖ := abs_real_inner_le_norm ψ (T ψ)
    have hstep : ‖ψ‖ * ‖T ψ‖ ≤ ‖ψ‖ * (r * ‖ψ‖) :=
      mul_le_mul_of_nonneg_left (hT.contractive ψ hψ) (norm_nonneg ψ)
    have hsq : ‖ψ‖ * (r * ‖ψ‖) = r * ‖ψ‖ ^ 2 := by ring
    nlinarith

end TransferContractionGap

end SliceReflectionHilbert
