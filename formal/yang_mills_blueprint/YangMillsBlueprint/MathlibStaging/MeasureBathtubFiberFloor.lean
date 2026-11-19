/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Analysis.SpecialFunctions.Pow.Real
public import Mathlib.MeasureTheory.Integral.Bochner.Set
public import Mathlib.Tactic.FieldSimp
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.LatticeHaarGibbs

/-!
# Measure-Theoretic Lieb-Loss Bathtub Floor and Codimension-`d` Fiber Bounds

Proves the exact measure-theoretic bathtub inequality on arbitrary probability spaces `(Ω, ν)` for
any `L^∞`-bounded probability density `0 ≤ ρ ≤ M` (`∫ ρ dν = 1`):

* `measure_bathtub_pointwise_le`: pointwise majorization separating bulk mass and `{f < t}`.
* `measure_bathtub_integral_ge`: exact Lieb-Loss integral lower bound
  `t * (1 - M * ν.real {y | f y < t}) + M * ∫ y in {y | f y < t}, f y ∂ν ≤ ∫ y, f y * ρ y ∂ν`.
* `measure_bathtub_codim2_sharp_floor`: exact sharp `1 / (2 * c * M)` floor (`4 / M` at `c = 1/8`).
* `measure_bathtub_codim_d_floor` & `codim_bathtub_floor_mono_dim`: higher-rank `M ^ (-2 / d)`
  scaling across transverse root codimensions `d = dim G - rank G` (`SO(3) → E₈`).
* `boltzmann_measure_bathtub_integral_ge` & `boltzmann_measure_bathtub_codim_d_floor`: direct
  instantiation on normalized compact-group Haar product Gibbs measures (`LatticeHaarGibbs`).
-/

@[expose] public section

namespace MeasureBathtubFiberFloor

open LatticeHaarGibbs MeasureTheory

section GeneralProbabilityMeasure

/-- Pointwise Lieb-Loss bathtub inequality on `{y | f y < t}` vs its complement. -/
theorem measure_bathtub_pointwise_le {Ω : Type*} (f ρ : Ω → ℝ) (t M : ℝ) (x : Ω)
    (hρ0 : 0 ≤ ρ x) (hρM : ρ x ≤ M) :
    t * ρ x + M * ({y : Ω | f y < t}.indicator f x) ≤
      f x * ρ x + M * t * ({y : Ω | f y < t}.indicator (fun _ => (1 : ℝ)) x) := by
  by_cases hx : f x < t
  · simp only [Set.indicator, Set.mem_ofPred_eq, hx, ↓reduceIte, mul_one]
    nlinarith
  · have hfx : t ≤ f x := le_of_not_gt hx
    simp only [Set.indicator, Set.mem_ofPred_eq, hx, ↓reduceIte, mul_zero, add_zero]
    nlinarith

/-- Exact measure-theoretic Lieb-Loss bathtub lower bound for any normalized density `0 ≤ ρ ≤ M`
on a probability space `(Ω, ν)`. -/
theorem measure_bathtub_integral_ge {Ω : Type*} [MeasurableSpace Ω] {ν : Measure Ω}
    [IsProbabilityMeasure ν] {f ρ : Ω → ℝ} {t M : ℝ}
    (hA : MeasurableSet {y : Ω | f y < t}) (hf : Integrable f ν) (hρ : Integrable ρ ν)
    (hfρ : Integrable (fun y => f y * ρ y) ν)
    (hρ0 : ∀ y, 0 ≤ ρ y) (hρM : ∀ y, ρ y ≤ M) (hρInt : ∫ y, ρ y ∂ν = 1) :
    t * (1 - M * ν.real {y : Ω | f y < t}) +
        M * (∫ y in {y : Ω | f y < t}, f y ∂ν) ≤
      ∫ y, f y * ρ y ∂ν := by
  let A : Set Ω := {y : Ω | f y < t}
  have h1 : Integrable (fun x => t * ρ x + M * A.indicator f x) ν :=
    (hρ.const_mul t).add ((hf.indicator hA).const_mul M)
  have hind1 : Integrable (A.indicator (fun _ => (1 : ℝ))) ν :=
    (integrable_const (1 : ℝ)).indicator hA
  have h2 : Integrable (fun x => f x * ρ x + M * t * A.indicator (fun _ => (1 : ℝ)) x) ν :=
    hfρ.add (hind1.const_mul (M * t))
  have hpt : ∀ x, t * ρ x + M * A.indicator f x ≤
      f x * ρ x + M * t * A.indicator (fun _ => (1 : ℝ)) x := fun x =>
    measure_bathtub_pointwise_le f ρ t M x (hρ0 x) (hρM x)
  have hint := integral_mono h1 h2 hpt
  have hL : ∫ x, (t * ρ x + M * A.indicator f x) ∂ν =
      t * (∫ x, ρ x ∂ν) + M * (∫ x in A, f x ∂ν) := by
    rw [integral_add (hρ.const_mul t) ((hf.indicator hA).const_mul M),
      integral_const_mul, integral_const_mul, integral_indicator hA]
  have hR : ∫ x, (f x * ρ x + M * t * A.indicator (fun _ => (1 : ℝ)) x) ∂ν =
      (∫ x, f x * ρ x ∂ν) + M * t * ν.real A := by
    rw [integral_add hfρ (hind1.const_mul (M * t)), integral_const_mul, integral_indicator hA,
      setIntegral_const, smul_eq_mul, mul_one]
  rw [hL, hR, hρInt] at hint
  change t * (1 - M * ν.real A) + M * (∫ y in A, f y ∂ν) ≤ ∫ y, f y * ρ y ∂ν
  linarith

/-- Nonnegative-observable bathtub corollary dropping the sublevel integral `∫_{f<t} f ≥ 0`. -/
theorem measure_bathtub_sublevel_floor {Ω : Type*} [MeasurableSpace Ω] {ν : Measure Ω}
    [IsProbabilityMeasure ν] {f ρ : Ω → ℝ} {t M : ℝ}
    (hA : MeasurableSet {y : Ω | f y < t}) (hf : Integrable f ν) (hρ : Integrable ρ ν)
    (hfρ : Integrable (fun y => f y * ρ y) ν)
    (hf0 : ∀ y, 0 ≤ f y) (hM0 : 0 ≤ M)
    (hρ0 : ∀ y, 0 ≤ ρ y) (hρM : ∀ y, ρ y ≤ M) (hρInt : ∫ y, ρ y ∂ν = 1) :
    t * (1 - M * ν.real {y : Ω | f y < t}) ≤ ∫ y, f y * ρ y ∂ν := by
  have hbt := measure_bathtub_integral_ge hA hf hρ hfρ hρ0 hρM hρInt
  have hset0 : 0 ≤ ∫ y in {y : Ω | f y < t}, f y ∂ν :=
    setIntegral_nonneg hA (fun y _ => hf0 y)
  have hmul0 : 0 ≤ M * ∫ y in {y : Ω | f y < t}, f y ∂ν := mul_nonneg hM0 hset0
  linarith

/-- Sharp codimension-`2` bathtub floor `1 / (2 * c * M) ≤ ∫ f ρ dν` (equals `4 / M` at
`c = 1/8` matching the `SU(2)`/`SO(3)` Hopf commutator observable). -/
theorem measure_bathtub_codim2_sharp_floor {Ω : Type*} [MeasurableSpace Ω] {ν : Measure Ω}
    [IsProbabilityMeasure ν] {f ρ : Ω → ℝ} {c M : ℝ} (hc : 0 < c) (hM : 0 < M)
    (hA : MeasurableSet {y : Ω | f y < 1 / (c * M)}) (hf : Integrable f ν) (hρ : Integrable ρ ν)
    (hfρ : Integrable (fun y => f y * ρ y) ν)
    (hρ0 : ∀ y, 0 ≤ ρ y) (hρM : ∀ y, ρ y ≤ M) (hρInt : ∫ y, ρ y ∂ν = 1)
    (hvol : ν.real {y : Ω | f y < 1 / (c * M)} ≤ c * (1 / (c * M)))
    (hintSub : (c / 2) * (1 / (c * M)) ^ 2 ≤ ∫ y in {y : Ω | f y < 1 / (c * M)}, f y ∂ν) :
    1 / (2 * c * M) ≤ ∫ y, f y * ρ y ∂ν := by
  let t : ℝ := 1 / (c * M)
  have ht0 : 0 ≤ t := by positivity
  have hbt := measure_bathtub_integral_ge hA hf hρ hfρ hρ0 hρM hρInt
  have hmass : M * ν.real {y : Ω | f y < t} ≤ M * (c * t) :=
    mul_le_mul_of_nonneg_left hvol hM.le
  have hMct : M * (c * t) = 1 := by
    dsimp [t]
    field_simp
  have hfirst : 0 ≤ t * (1 - M * ν.real {y : Ω | f y < t}) :=
    mul_nonneg ht0 (by linarith)
  have hsecond : M * ((c / 2) * t ^ 2) ≤ M * ∫ y in {y : Ω | f y < t}, f y ∂ν :=
    mul_le_mul_of_nonneg_left hintSub hM.le
  have hsharp : M * ((c / 2) * t ^ 2) = 1 / (2 * c * M) := by
    dsimp [t]
    field_simp
  linarith

/-- General codimension-`d` bathtub floor `(1 / 2) * (1 / (2 * c * M)) ^ (2 / d) ≤ ∫ f ρ dν`
for sublevel volume scaling `ν.real {f < t} ≤ c * t ^ (d / 2)`. -/
theorem measure_bathtub_codim_d_floor {Ω : Type*} [MeasurableSpace Ω] {ν : Measure Ω}
    [IsProbabilityMeasure ν] {f ρ : Ω → ℝ} {c M : ℝ} {d : ℕ}
    (hc : 0 < c) (hM : 0 < M) (hd : 0 < d)
    (hA : MeasurableSet {y : Ω | f y < (1 / (2 * c * M)) ^ ((2 : ℝ) / (d : ℝ))})
    (hf : Integrable f ν) (hρ : Integrable ρ ν)
    (hfρ : Integrable (fun y => f y * ρ y) ν)
    (hf0 : ∀ y, 0 ≤ f y) (hρ0 : ∀ y, 0 ≤ ρ y) (hρM : ∀ y, ρ y ≤ M) (hρInt : ∫ y, ρ y ∂ν = 1)
    (hvol : ν.real {y : Ω | f y < (1 / (2 * c * M)) ^ ((2 : ℝ) / (d : ℝ))} ≤
      c * ((1 / (2 * c * M)) ^ ((2 : ℝ) / (d : ℝ))) ^ ((d : ℝ) / 2)) :
    (1 / 2 : ℝ) * (1 / (2 * c * M)) ^ ((2 : ℝ) / (d : ℝ)) ≤ ∫ y, f y * ρ y ∂ν := by
  let t : ℝ := (1 / (2 * c * M)) ^ ((2 : ℝ) / (d : ℝ))
  have hbase0 : 0 ≤ 1 / (2 * c * M) := by positivity
  have ht0 : 0 ≤ t := Real.rpow_nonneg hbase0 _
  have hdne : (d : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hd.ne'
  have hpowEq : t ^ ((d : ℝ) / 2) = 1 / (2 * c * M) := by
    dsimp [t]
    rw [← Real.rpow_mul hbase0]
    have hexp : ((2 : ℝ) / (d : ℝ)) * ((d : ℝ) / 2) = 1 := by
      field_simp [hdne]
    rw [hexp, Real.rpow_one]
  have hvol' : ν.real {y : Ω | f y < t} ≤ c * (1 / (2 * c * M)) := by
    change ν.real {y : Ω | f y < t} ≤ c * t ^ ((d : ℝ) / 2) at hvol
    rwa [hpowEq] at hvol
  have hMnu : M * ν.real {y : Ω | f y < t} ≤ 1 / 2 := by
    have hmul := mul_le_mul_of_nonneg_left hvol' hM.le
    have heq : M * (c * (1 / (2 * c * M))) = 1 / 2 := by
      field_simp
    linarith
  have hsub := measure_bathtub_sublevel_floor hA hf hρ hfρ hf0 hM.le hρ0 hρM hρInt
  have hcoeff : (1 / 2 : ℝ) ≤ 1 - M * ν.real {y : Ω | f y < t} := by linarith
  have hle : (1 / 2 : ℝ) * t ≤ t * (1 - M * ν.real {y : Ω | f y < t}) := by
    rw [mul_comm (1 / 2 : ℝ) t]
    exact mul_le_mul_of_nonneg_left hcoeff ht0
  exact le_trans hle hsub

/-- Monotone strengthening of the codimension-`d` floor in `d` whenever `1 ≤ 2 * c * M`. -/
theorem codim_bathtub_floor_mono_dim {c M : ℝ} {d₁ d₂ : ℕ}
    (hc : 0 < c) (hM : 0 < M) (hbig : 1 ≤ 2 * c * M) (hd₁ : 0 < d₁) (hle : d₁ ≤ d₂) :
    (1 / 2 : ℝ) * (1 / (2 * c * M)) ^ ((2 : ℝ) / (d₁ : ℝ)) ≤
      (1 / 2 : ℝ) * (1 / (2 * c * M)) ^ ((2 : ℝ) / (d₂ : ℝ)) := by
  have hd₂ : 0 < d₂ := lt_of_lt_of_le hd₁ hle
  have h2cM_pos : 0 < 2 * c * M := by positivity
  have hd1_pos : (0 : ℝ) < (d₁ : ℝ) := Nat.cast_pos.mpr hd₁
  have hd2_pos : (0 : ℝ) < (d₂ : ℝ) := Nat.cast_pos.mpr hd₂
  have hleR : (d₁ : ℝ) ≤ (d₂ : ℝ) := Nat.cast_le.mpr hle
  have hexp : (2 : ℝ) / (d₂ : ℝ) ≤ (2 : ℝ) / (d₁ : ℝ) :=
    div_le_div_of_nonneg_left (by norm_num) hd1_pos hleR
  have hpow : (2 * c * M) ^ ((2 : ℝ) / (d₂ : ℝ)) ≤ (2 * c * M) ^ ((2 : ℝ) / (d₁ : ℝ)) :=
    Real.rpow_le_rpow_of_exponent_le hbig hexp
  have hpowPos : 0 < (2 * c * M) ^ ((2 : ℝ) / (d₂ : ℝ)) :=
    Real.rpow_pos_of_pos h2cM_pos _
  have hinv :
      1 / (2 * c * M) ^ ((2 : ℝ) / (d₁ : ℝ)) ≤ 1 / (2 * c * M) ^ ((2 : ℝ) / (d₂ : ℝ)) :=
    one_div_le_one_div_of_le hpowPos hpow
  have hinv1 :
      (1 / (2 * c * M)) ^ ((2 : ℝ) / (d₁ : ℝ)) = 1 / (2 * c * M) ^ ((2 : ℝ) / (d₁ : ℝ)) := by
    rw [one_div, Real.inv_rpow h2cM_pos.le, one_div]
  have hinv2 :
      (1 / (2 * c * M)) ^ ((2 : ℝ) / (d₂ : ℝ)) = 1 / (2 * c * M) ^ ((2 : ℝ) / (d₂ : ℝ)) := by
    rw [one_div, Real.inv_rpow h2cM_pos.le, one_div]
  rw [hinv1, hinv2]
  exact mul_le_mul_of_nonneg_left hinv (by norm_num)

end GeneralProbabilityMeasure

section BoltzmannGibbsBathtub

private theorem boltzmann_density_spec {Ω : Type*} [MeasurableSpace Ω] {ν : Measure Ω}
    [IsProbabilityMeasure ν] {S f : Ω → ℝ} {vMin vMax : ℝ}
    (hint : Integrable (expWeight S) ν)
    (hfw : Integrable (fun y => f y * expWeight S y) ν)
    (hmin : ∀ y, vMin ≤ S y) (hmax : ∀ y, S y ≤ vMax) :
    let Z : ℝ := partitionIntegral ν S
    let ρ : Ω → ℝ := fun y => expWeight S y / Z
    Integrable ρ ν ∧ Integrable (fun y => f y * ρ y) ν ∧
      (∀ y, 0 ≤ ρ y) ∧ (∀ y, ρ y ≤ Real.exp (vMax - vMin)) ∧
      (∫ y, ρ y ∂ν = 1) ∧ (∫ y, f y * ρ y ∂ν = weightedExpectation ν S f) := by
  let Z : ℝ := partitionIntegral ν S
  have hZpos : 0 < Z := partitionIntegral_pos hint hmax
  have hZne : Z ≠ 0 := ne_of_gt hZpos
  let ρ : Ω → ℝ := fun y => expWeight S y / Z
  have hρ : Integrable ρ ν := hint.div_const Z
  have hfρEq : (fun y => f y * ρ y) = fun y => (f y * expWeight S y) / Z := by
    ext y
    simp only [ρ, mul_div_assoc]
  have hfρ : Integrable (fun y => f y * ρ y) ν := by
    rw [hfρEq]
    exact hfw.div_const Z
  have hρ0 : ∀ y, 0 ≤ ρ y := fun y => by
    dsimp [ρ, expWeight]
    positivity
  have hρM : ∀ y, ρ y ≤ Real.exp (vMax - vMin) := fun y =>
    boltzmannDensity_le_exp_osc hint hmin hmax y
  have hρInt : ∫ y, ρ y ∂ν = 1 := by
    change (∫ y, expWeight S y / Z ∂ν) = 1
    rw [integral_div]
    change Z / Z = 1
    exact div_self hZne
  have hExpEq : ∫ y, f y * ρ y ∂ν = weightedExpectation ν S f := by
    rw [hfρEq, integral_div]
    rfl
  exact ⟨hρ, hfρ, hρ0, hρM, hρInt, hExpEq⟩

/-- Measure-theoretic Lieb-Loss bathtub inequality instantiated directly on the normalized
Boltzmann measure `weightedExpectation ν S f` with oscillation cap `M = Real.exp (vMax - vMin)`. -/
theorem boltzmann_measure_bathtub_integral_ge {Ω : Type*} [MeasurableSpace Ω] {ν : Measure Ω}
    [IsProbabilityMeasure ν] {S f : Ω → ℝ} {t vMin vMax : ℝ}
    (hA : MeasurableSet {y : Ω | f y < t}) (hint : Integrable (expWeight S) ν)
    (hf : Integrable f ν) (hfw : Integrable (fun y => f y * expWeight S y) ν)
    (hmin : ∀ y, vMin ≤ S y) (hmax : ∀ y, S y ≤ vMax) :
    t * (1 - Real.exp (vMax - vMin) * ν.real {y : Ω | f y < t}) +
        Real.exp (vMax - vMin) * (∫ y in {y : Ω | f y < t}, f y ∂ν) ≤
      weightedExpectation ν S f := by
  obtain ⟨hρ, hfρ, hρ0, hρM, hρInt, hExpEq⟩ :=
    boltzmann_density_spec hint hfw hmin hmax
  have hbt := measure_bathtub_integral_ge hA hf hρ hfρ hρ0 hρM hρInt
  rwa [hExpEq] at hbt

/-- Codimension-`d` normalized Boltzmann expectation floor under bounded oscillation `vMax - vMin`
and Haar sublevel scaling `ν.real {f < t} ≤ c * t ^ (d / 2)`. -/
theorem boltzmann_measure_bathtub_codim_d_floor {Ω : Type*} [MeasurableSpace Ω] {ν : Measure Ω}
    [IsProbabilityMeasure ν] {S f : Ω → ℝ} {c vMin vMax : ℝ} {d : ℕ}
    (hc : 0 < c) (hd : 0 < d)
    (hA : MeasurableSet
      {y : Ω | f y < (1 / (2 * c * Real.exp (vMax - vMin))) ^ ((2 : ℝ) / (d : ℝ))})
    (hint : Integrable (expWeight S) ν)
    (hf : Integrable f ν) (hfw : Integrable (fun y => f y * expWeight S y) ν)
    (hf0 : ∀ y, 0 ≤ f y) (hmin : ∀ y, vMin ≤ S y) (hmax : ∀ y, S y ≤ vMax)
    (hvol : ν.real {y : Ω | f y < (1 / (2 * c * Real.exp (vMax - vMin))) ^ ((2 : ℝ) / (d : ℝ))} ≤
      c * ((1 / (2 * c * Real.exp (vMax - vMin))) ^ ((2 : ℝ) / (d : ℝ))) ^ ((d : ℝ) / 2)) :
    (1 / 2 : ℝ) * (1 / (2 * c * Real.exp (vMax - vMin))) ^ ((2 : ℝ) / (d : ℝ)) ≤
      weightedExpectation ν S f := by
  obtain ⟨hρ, hfρ, hρ0, hρM, hρInt, hExpEq⟩ :=
    boltzmann_density_spec hint hfw hmin hmax
  have hbt := measure_bathtub_codim_d_floor hc (Real.exp_pos _) hd hA hf hρ hfρ hf0
    hρ0 hρM hρInt hvol
  rwa [hExpEq] at hbt

end BoltzmannGibbsBathtub

end MeasureBathtubFiberFloor
