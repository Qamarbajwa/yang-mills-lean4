/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Analysis.Complex.Exponential
public import Mathlib.Analysis.SpecialFunctions.ExpDeriv
public import Mathlib.Data.Matrix.Basic
public import Mathlib.LinearAlgebra.Matrix.Trace
public import Mathlib.Logic.Equiv.Fin.Basic
public import Mathlib.MeasureTheory.Integral.DominatedConvergence
public import Mathlib.MeasureTheory.Integral.Prod
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.LatticeHaarGibbs
public import YangMillsBlueprint.MathlibStaging.SliceReflectionHilbert

/-!
# Unconditional Osterwalder-Seiler Finite-Box Wilson Reflection Positivity

Proves **unconditional** Osterwalder-Seiler exponential reflection positivity for finite-box lattice
gauge theory models over compact gauge groups:

* `LatticeReflectionPositivity.IsBoundedMeasurable` and `BoundedMeasurableSubmodule`: the real
  vector space of bounded measurable half-space observables on `(Ω, μ)`.
* `LatticeReflectionPositivity.HasFiniteRankNonneg`: kernels `K : Ω → Ω → ℝ` admitting a finite
  nonnegative bilinear rank decomposition `∑ k, c_k φ_k(x) φ_k(y)` (`c_k ≥ 0`), closed under
  constants, addition, Schur product (`mul`), powers (`pow`), and truncated Taylor series.
* `LatticeReflectionPositivity.integral_prod_exp_crossing_nonneg`: unconditional exponential
  reflection positivity `0 ≤ ∫ f(z.1) f(z.2) exp(K(z.1, z.2)) ∂(μ × μ)` proved via finite-rank
  positivity and Lebesgue dominated convergence.
* `LatticeReflectionPositivity.wilsonCrossingRPForm` and `wilsonOSHilbert`: concrete `4D` Wilson
  crossing-plaquette `SliceReflectionHilbert.ReflectionPositiveForm` and complete OS Hilbert space
  on compact product Haar measure `(E_pos → G, productHaarProb E_pos G)`.
-/

@[expose] public section

namespace LatticeReflectionPositivity

open Filter LatticeHaarGibbs Matrix MeasureTheory SliceReflectionHilbert Topology

section BoundedMeasurableObservables

/-- Bounded measurable real-valued function on a measurable space `Ω`. -/
structure IsBoundedMeasurable {Ω : Type*} [MeasurableSpace Ω] (f : Ω → ℝ) : Prop where
  meas : Measurable f
  bounded : ∃ C : ℝ, ∀ x : Ω, |f x| ≤ C

theorem isBoundedMeasurable_const {Ω : Type*} [MeasurableSpace Ω] (c : ℝ) :
    IsBoundedMeasurable (fun _ : Ω => c) where
  meas := measurable_const
  bounded := ⟨|c|, fun _ => le_rfl⟩

theorem isBoundedMeasurable_zero {Ω : Type*} [MeasurableSpace Ω] :
    IsBoundedMeasurable (fun _ : Ω => (0 : ℝ)) :=
  isBoundedMeasurable_const 0

theorem IsBoundedMeasurable.add {Ω : Type*} [MeasurableSpace Ω] {f g : Ω → ℝ}
    (hf : IsBoundedMeasurable f) (hg : IsBoundedMeasurable g) :
    IsBoundedMeasurable (fun x => f x + g x) where
  meas := hf.meas.add hg.meas
  bounded := by
    obtain ⟨Cf, hCf⟩ := hf.bounded
    obtain ⟨Cg, hCg⟩ := hg.bounded
    exact ⟨Cf + Cg, fun x => (abs_add_le (f x) (g x)).trans (add_le_add (hCf x) (hCg x))⟩

theorem IsBoundedMeasurable.smul {Ω : Type*} [MeasurableSpace Ω] {f : Ω → ℝ}
    (hf : IsBoundedMeasurable f) (c : ℝ) :
    IsBoundedMeasurable (fun x => c * f x) where
  meas := measurable_const.mul hf.meas
  bounded := by
    obtain ⟨C, hC⟩ := hf.bounded
    exact ⟨|c| * C, fun x => by
      simpa [abs_mul] using mul_le_mul_of_nonneg_left (hC x) (abs_nonneg c)⟩

theorem IsBoundedMeasurable.mul {Ω : Type*} [MeasurableSpace Ω] {f g : Ω → ℝ}
    (hf : IsBoundedMeasurable f) (hg : IsBoundedMeasurable g) :
    IsBoundedMeasurable (fun x => f x * g x) where
  meas := hf.meas.mul hg.meas
  bounded := by
    obtain ⟨Cf, hCf⟩ := hf.bounded
    obtain ⟨Cg, hCg⟩ := hg.bounded
    refine ⟨max Cf 0 * max Cg 0, fun x => ?_⟩
    have hf' : |f x| ≤ max Cf 0 := le_trans (hCf x) (le_max_left Cf 0)
    have hg' : |g x| ≤ max Cg 0 := le_trans (hCg x) (le_max_left Cg 0)
    rw [abs_mul]
    exact mul_le_mul hf' hg' (abs_nonneg (g x)) (le_max_right Cf 0)

theorem IsBoundedMeasurable.exp_neg {Ω : Type*} [MeasurableSpace Ω] {f : Ω → ℝ}
    (hf : IsBoundedMeasurable f) :
    IsBoundedMeasurable (fun x => Real.exp (-f x)) where
  meas := Real.continuous_exp.measurable.comp hf.meas.neg
  bounded := by
    obtain ⟨C, hC⟩ := hf.bounded
    refine ⟨Real.exp C, fun x => ?_⟩
    rw [abs_of_pos (Real.exp_pos _)]
    exact Real.exp_le_exp.mpr (le_trans (neg_le_abs (f x)) (hC x))

theorem IsBoundedMeasurable.nonneg_bound {Ω : Type*} [MeasurableSpace Ω] {f : Ω → ℝ}
    (hf : IsBoundedMeasurable f) : ∃ C : ℝ, 0 ≤ C ∧ ∀ x : Ω, |f x| ≤ C := by
  obtain ⟨C, hC⟩ := hf.bounded
  exact ⟨max C 0, le_max_right C 0, fun x => le_trans (hC x) (le_max_left C 0)⟩

theorem IsBoundedMeasurable.integrable {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsFiniteMeasure μ] {f : Ω → ℝ} (hf : IsBoundedMeasurable f) :
    Integrable f μ := by
  obtain ⟨C, hC⟩ := hf.bounded
  exact Integrable.of_mem_Icc (-C) C hf.meas.aemeasurable
    (ae_of_all μ fun x => abs_le.mp (hC x))

/-- Real submodule of bounded measurable half-space observables on `Ω`. -/
def boundedMeasurableSubmodule (Ω : Type*) [MeasurableSpace Ω] : Submodule ℝ (Ω → ℝ) where
  carrier := { f : Ω → ℝ | IsBoundedMeasurable f }
  add_mem' hf hg := hf.add hg
  zero_mem' := isBoundedMeasurable_zero
  smul_mem' c _ hf := hf.smul c

/-- Type alias for `boundedMeasurableSubmodule Ω`, inheriting `AddCommGroup` and `Module ℝ`. -/
abbrev BoundedMeasurableSubmodule (Ω : Type*) [MeasurableSpace Ω] : Type _ :=
  boundedMeasurableSubmodule Ω

end BoundedMeasurableObservables

section FiniteRankNonnegKernels

/-- Data witnessing a finite-rank symmetric nonnegative decomposition
`K x y = ∑ k : Fin rank, coeff k * feat k x * feat k y` with `coeff k ≥ 0`. -/
structure FiniteRankNonnegData {Ω : Type*} [MeasurableSpace Ω] (K : Ω → Ω → ℝ) where
  rank : ℕ
  coeff : Fin rank → ℝ
  feat : Fin rank → Ω → ℝ
  coeff_nonneg : ∀ k : Fin rank, 0 ≤ coeff k
  feat_bdMeas : ∀ k : Fin rank, IsBoundedMeasurable (feat k)
  eq_sum : ∀ x y : Ω, K x y = ∑ k : Fin rank, coeff k * feat k x * feat k y

/-- A kernel `K : Ω → Ω → ℝ` has a finite-rank symmetric nonnegative decomposition if there exists
`FiniteRankNonnegData K`. -/
def HasFiniteRankNonneg {Ω : Type*} [MeasurableSpace Ω] (K : Ω → Ω → ℝ) : Prop :=
  Nonempty (FiniteRankNonnegData K)

theorem HasFiniteRankNonneg.zero {Ω : Type*} [MeasurableSpace Ω] :
    HasFiniteRankNonneg (fun _ _ : Ω => (0 : ℝ)) :=
  ⟨{
    rank := 0
    coeff := Fin.elim0
    feat := Fin.elim0
    coeff_nonneg := fun k => k.elim0
    feat_bdMeas := fun k => k.elim0
    eq_sum := fun _ _ => by simp }⟩

theorem HasFiniteRankNonneg.one {Ω : Type*} [MeasurableSpace Ω] :
    HasFiniteRankNonneg (fun _ _ : Ω => (1 : ℝ)) :=
  ⟨{
    rank := 1
    coeff := fun _ => 1
    feat := fun _ _ => 1
    coeff_nonneg := fun _ => by norm_num
    feat_bdMeas := fun _ => isBoundedMeasurable_const 1
    eq_sum := fun _ _ => by simp }⟩

theorem HasFiniteRankNonneg.rankOne {Ω : Type*} [MeasurableSpace Ω] {φ : Ω → ℝ}
    (hφ : IsBoundedMeasurable φ) :
    HasFiniteRankNonneg (fun x y : Ω => φ x * φ y) :=
  ⟨{
    rank := 1
    coeff := fun _ => 1
    feat := fun _ => φ
    coeff_nonneg := fun _ => by norm_num
    feat_bdMeas := fun _ => hφ
    eq_sum := fun x y => by simp }⟩

theorem HasFiniteRankNonneg.const_mul {Ω : Type*} [MeasurableSpace Ω] {α : ℝ}
    (hα : 0 ≤ α) {K : Ω → Ω → ℝ} (hK : HasFiniteRankNonneg K) :
    HasFiniteRankNonneg (fun x y => α * K x y) := by
  obtain ⟨d⟩ := hK
  refine ⟨{
    rank := d.rank
    coeff := fun k => α * d.coeff k
    feat := d.feat
    coeff_nonneg := fun k => mul_nonneg hα (d.coeff_nonneg k)
    feat_bdMeas := d.feat_bdMeas
    eq_sum := fun x y => ?_ }⟩
  rw [d.eq_sum x y, Finset.mul_sum]
  refine Finset.sum_congr rfl ?_
  intro k _
  ring

theorem HasFiniteRankNonneg.add {Ω : Type*} [MeasurableSpace Ω] {K₁ K₂ : Ω → Ω → ℝ}
    (h₁ : HasFiniteRankNonneg K₁) (h₂ : HasFiniteRankNonneg K₂) :
    HasFiniteRankNonneg (fun x y => K₁ x y + K₂ x y) := by
  obtain ⟨d₁⟩ := h₁
  obtain ⟨d₂⟩ := h₂
  refine ⟨{
    rank := d₁.rank + d₂.rank
    coeff := Fin.addCases d₁.coeff d₂.coeff
    feat := Fin.addCases d₁.feat d₂.feat
    coeff_nonneg := Fin.addCases
      (fun i => by simpa using d₁.coeff_nonneg i)
      (fun j => by simpa using d₂.coeff_nonneg j)
    feat_bdMeas := Fin.addCases
      (fun i => by simpa using d₁.feat_bdMeas i)
      (fun j => by simpa using d₂.feat_bdMeas j)
    eq_sum := fun x y => ?_ }⟩
  rw [d₁.eq_sum x y, d₂.eq_sum x y, Fin.sum_univ_add]
  simp

/-- Schur product closure: the pointwise product of two finite-rank nonnegative kernels again has
finite-rank nonnegative decomposition. -/
theorem HasFiniteRankNonneg.mul {Ω : Type*} [MeasurableSpace Ω] {K₁ K₂ : Ω → Ω → ℝ}
    (h₁ : HasFiniteRankNonneg K₁) (h₂ : HasFiniteRankNonneg K₂) :
    HasFiniteRankNonneg (fun x y => K₁ x y * K₂ x y) := by
  obtain ⟨d₁⟩ := h₁
  obtain ⟨d₂⟩ := h₂
  refine ⟨{
    rank := d₁.rank * d₂.rank
    coeff := fun k => d₁.coeff (finProdFinEquiv.symm k).1 * d₂.coeff (finProdFinEquiv.symm k).2
    feat := fun k x =>
      d₁.feat (finProdFinEquiv.symm k).1 x * d₂.feat (finProdFinEquiv.symm k).2 x
    coeff_nonneg := fun k => mul_nonneg
      (d₁.coeff_nonneg (finProdFinEquiv.symm k).1)
      (d₂.coeff_nonneg (finProdFinEquiv.symm k).2)
    feat_bdMeas := fun k =>
      (d₁.feat_bdMeas (finProdFinEquiv.symm k).1).mul
        (d₂.feat_bdMeas (finProdFinEquiv.symm k).2)
    eq_sum := fun x y => ?_ }⟩
  rw [d₁.eq_sum x y, d₂.eq_sum x y, Finset.sum_mul_sum, ← Fintype.sum_prod_type']
  refine Fintype.sum_equiv finProdFinEquiv
    (fun p : Fin d₁.rank × Fin d₂.rank =>
      (d₁.coeff p.1 * d₁.feat p.1 x * d₁.feat p.1 y) *
        (d₂.coeff p.2 * d₂.feat p.2 x * d₂.feat p.2 y))
    (fun k : Fin (d₁.rank * d₂.rank) =>
      (d₁.coeff (finProdFinEquiv.symm k).1 * d₂.coeff (finProdFinEquiv.symm k).2) *
        (d₁.feat (finProdFinEquiv.symm k).1 x * d₂.feat (finProdFinEquiv.symm k).2 x) *
        (d₁.feat (finProdFinEquiv.symm k).1 y * d₂.feat (finProdFinEquiv.symm k).2 y))
    ?_
  intro p
  simp only [Equiv.symm_apply_apply]
  ring

theorem HasFiniteRankNonneg.pow {Ω : Type*} [MeasurableSpace Ω] {K : Ω → Ω → ℝ}
    (hK : HasFiniteRankNonneg K) : ∀ n : ℕ, HasFiniteRankNonneg (fun x y => K x y ^ n)
  | 0 => by simpa [pow_zero] using HasFiniteRankNonneg.one
  | n + 1 => by simpa [pow_succ] using (hK.pow n).mul hK

theorem HasFiniteRankNonneg.finset_sum {Ω ι : Type*} [MeasurableSpace Ω] (s : Finset ι)
    (K : ι → Ω → Ω → ℝ) (hK : ∀ r ∈ s, HasFiniteRankNonneg (K r)) :
    HasFiniteRankNonneg (fun x y => ∑ r ∈ s, K r x y) := by
  classical
  induction s using Finset.induction with
  | empty => simpa using HasFiniteRankNonneg.zero
  | @insert a s ha ih =>
      have haK : HasFiniteRankNonneg (K a) := hK a (Finset.mem_insert_self a s)
      have hsK : HasFiniteRankNonneg (fun x y => ∑ r ∈ s, K r x y) :=
        ih fun r hr => hK r (Finset.mem_insert_of_mem hr)
      simpa [Finset.sum_insert ha] using haK.add hsK

theorem HasFiniteRankNonneg.symm {Ω : Type*} [MeasurableSpace Ω] {K : Ω → Ω → ℝ}
    (hK : HasFiniteRankNonneg K) (x y : Ω) : K x y = K y x := by
  obtain ⟨d⟩ := hK
  rw [d.eq_sum x y, d.eq_sum y x]
  refine Finset.sum_congr rfl ?_
  intro k _
  ring

theorem HasFiniteRankNonneg.bdMeas_uncurry {Ω : Type*} [MeasurableSpace Ω] {K : Ω → Ω → ℝ}
    (hK : HasFiniteRankNonneg K) :
    IsBoundedMeasurable (fun z : Ω × Ω => K z.1 z.2) := by
  obtain ⟨d⟩ := hK
  have hterm : ∀ k : Fin d.rank,
      IsBoundedMeasurable (fun z : Ω × Ω => d.coeff k * d.feat k z.1 * d.feat k z.2) := by
    intro k
    have hf1 : IsBoundedMeasurable (fun z : Ω × Ω => d.feat k z.1) := by
      obtain ⟨C, hC⟩ := (d.feat_bdMeas k).bounded
      exact ⟨(d.feat_bdMeas k).meas.comp measurable_fst, ⟨C, fun z => hC z.1⟩⟩
    have hf2 : IsBoundedMeasurable (fun z : Ω × Ω => d.feat k z.2) := by
      obtain ⟨C, hC⟩ := (d.feat_bdMeas k).bounded
      exact ⟨(d.feat_bdMeas k).meas.comp measurable_snd, ⟨C, fun z => hC z.2⟩⟩
    exact (hf1.smul (d.coeff k)).mul hf2
  have hsum :
      IsBoundedMeasurable
        (fun z : Ω × Ω => ∑ k : Fin d.rank, d.coeff k * d.feat k z.1 * d.feat k z.2) := by
    have hin : ∀ (t : Finset (Fin d.rank)),
        IsBoundedMeasurable (fun z : Ω × Ω =>
          ∑ k ∈ t, d.coeff k * d.feat k z.1 * d.feat k z.2) := by
      intro t
      induction t using Finset.induction with
      | empty => simpa using isBoundedMeasurable_zero
      | @insert a t ha ih => simpa [Finset.sum_insert ha] using (hterm a).add ih
    exact hin Finset.univ
  have heq : (fun z : Ω × Ω => K z.1 z.2) =
      fun z : Ω × Ω => ∑ k : Fin d.rank, d.coeff k * d.feat k z.1 * d.feat k z.2 := by
    funext z
    exact d.eq_sum z.1 z.2
  rwa [heq]

/-- Truncated exponential Taylor series `∑_{n < N} t^n / n!`. -/
noncomputable def taylorExp (N : ℕ) (t : ℝ) : ℝ :=
  ∑ n ∈ Finset.range N, t ^ n / (Nat.factorial n : ℝ)

theorem HasFiniteRankNonneg.taylorExp {Ω : Type*} [MeasurableSpace Ω] {K : Ω → Ω → ℝ}
    (hK : HasFiniteRankNonneg K) (N : ℕ) :
    HasFiniteRankNonneg (fun x y => LatticeReflectionPositivity.taylorExp N (K x y)) := by
  have hrewrite :
      (fun x y : Ω => LatticeReflectionPositivity.taylorExp N (K x y)) =
        fun x y => ∑ n ∈ Finset.range N, ((Nat.factorial n : ℝ)⁻¹ * K x y ^ n) := by
    funext x y
    unfold LatticeReflectionPositivity.taylorExp
    refine Finset.sum_congr rfl ?_
    intro n _
    rw [div_eq_inv_mul]
  rw [hrewrite]
  exact HasFiniteRankNonneg.finset_sum (Finset.range N)
    (fun n x y => (Nat.factorial n : ℝ)⁻¹ * K x y ^ n)
    fun n _ => HasFiniteRankNonneg.const_mul (by positivity) (hK.pow n)

end FiniteRankNonnegKernels

section ExponentialReflectionPositivity

/-- Product-integral reflection positivity for any finite-rank nonnegative kernel `K`. -/
theorem integral_prod_factorized_nonneg {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsFiniteMeasure μ] {f : Ω → ℝ} (hf : IsBoundedMeasurable f)
    {K : Ω → Ω → ℝ} (hK : HasFiniteRankNonneg K) :
    0 ≤ ∫ z : Ω × Ω, f z.1 * f z.2 * K z.1 z.2 ∂(μ.prod μ) := by
  obtain ⟨d⟩ := hK
  have hint_term : ∀ k : Fin d.rank,
      Integrable (fun z : Ω × Ω =>
        d.coeff k * ((f z.1 * d.feat k z.1) * (f z.2 * d.feat k z.2))) (μ.prod μ) := by
    intro k
    have hk := hf.mul (d.feat_bdMeas k)
    obtain ⟨C, hC⟩ := hk.bounded
    have hf1 : IsBoundedMeasurable (fun z : Ω × Ω => f z.1 * d.feat k z.1) :=
      ⟨hk.meas.comp measurable_fst, ⟨C, fun z => hC z.1⟩⟩
    have hf2 : IsBoundedMeasurable (fun z : Ω × Ω => f z.2 * d.feat k z.2) :=
      ⟨hk.meas.comp measurable_snd, ⟨C, fun z => hC z.2⟩⟩
    exact ((hf1.mul hf2).smul (d.coeff k)).integrable (μ.prod μ)
  have heq :
      (fun z : Ω × Ω => f z.1 * f z.2 * K z.1 z.2) =
        fun z => ∑ k : Fin d.rank,
          d.coeff k * ((f z.1 * d.feat k z.1) * (f z.2 * d.feat k z.2)) := by
    funext z
    rw [d.eq_sum z.1 z.2, Finset.mul_sum]
    refine Finset.sum_congr rfl ?_
    intro k _
    ring
  rw [heq, MeasureTheory.integral_finsetSum _ (fun k _ => hint_term k)]
  refine Finset.sum_nonneg ?_
  intro k _
  rw [MeasureTheory.integral_const_mul,
    MeasureTheory.integral_prod_mul (fun x => f x * d.feat k x) (fun y => f y * d.feat k y)]
  exact mul_nonneg (d.coeff_nonneg k) (mul_self_nonneg _)

theorem abs_taylorExp_le_exp_abs (N : ℕ) (t : ℝ) :
    |taylorExp N t| ≤ Real.exp |t| := by
  calc
    |taylorExp N t|
        ≤ ∑ n ∈ Finset.range N, |t ^ n / (Nat.factorial n : ℝ)| :=
          Finset.abs_sum_le_sum_abs _ _
    _ = ∑ n ∈ Finset.range N, |t| ^ n / (Nat.factorial n : ℝ) := by
          refine Finset.sum_congr rfl ?_
          intro n _
          rw [abs_div, abs_pow, Nat.abs_cast]
    _ ≤ Real.exp |t| := Real.sum_le_exp_of_nonneg (abs_nonneg t) N

theorem tendsto_taylorExp_real (t : ℝ) :
    Tendsto (fun N => taylorExp N t) atTop (𝓝 (Real.exp t)) := by
  have hsum : HasSum (fun n : ℕ => t ^ n / (Nat.factorial n : ℝ)) (Real.exp t) := by
    rw [Real.exp_eq_exp_ℝ]
    exact NormedSpace.expSeries_div_hasSum_exp t
  exact hsum.tendsto_sum_nat

/-- **UNCONDITIONAL OSTERWALDER-SEILER EXPONENTIAL REFLECTION POSITIVITY:** For any finite
measure `(Ω, μ)`, bounded measurable `f`, and finite-rank nonnegative crossing kernel `K`,
`0 ≤ ∫ z, f z.1 * f z.2 * Real.exp (K z.1 z.2) ∂(μ.prod μ)`. -/
theorem integral_prod_exp_crossing_nonneg {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsFiniteMeasure μ] {f : Ω → ℝ} (hf : IsBoundedMeasurable f)
    {K : Ω → Ω → ℝ} (hK : HasFiniteRankNonneg K) :
    0 ≤ ∫ z : Ω × Ω, f z.1 * f z.2 * Real.exp (K z.1 z.2) ∂(μ.prod μ) := by
  obtain ⟨Cf, hCf0, hCf⟩ := hf.nonneg_bound
  obtain ⟨MK, _, hMK⟩ := hK.bdMeas_uncurry.nonneg_bound
  let F : ℕ → Ω × Ω → ℝ := fun N z => f z.1 * f z.2 * taylorExp N (K z.1 z.2)
  have hF_meas : ∀ N : ℕ, AEStronglyMeasurable (F N) (μ.prod μ) := by
    intro N
    have hK_meas : Measurable (fun z : Ω × Ω => K z.1 z.2) := hK.bdMeas_uncurry.meas
    have hT_meas : Measurable (fun z : Ω × Ω => taylorExp N (K z.1 z.2)) :=
      Finset.measurable_sum (Finset.range N) fun n _ => (hK_meas.pow_const n).div_const _
    exact ((hf.meas.comp measurable_fst).mul (hf.meas.comp measurable_snd) |>.mul
      hT_meas).aestronglyMeasurable
  have hbound_int : Integrable (fun _ : Ω × Ω => Cf * Cf * Real.exp MK) (μ.prod μ) :=
    integrable_const _
  have hbound : ∀ N : ℕ, ∀ᵐ z ∂(μ.prod μ), ‖F N z‖ ≤ Cf * Cf * Real.exp MK := by
    intro N
    refine ae_of_all _ fun z => ?_
    rw [Real.norm_eq_abs, abs_mul, abs_mul]
    have h1 : |f z.1| * |f z.2| ≤ Cf * Cf :=
      mul_le_mul (hCf z.1) (hCf z.2) (abs_nonneg _) hCf0
    have h2 : |taylorExp N (K z.1 z.2)| ≤ Real.exp MK :=
      (abs_taylorExp_le_exp_abs N (K z.1 z.2)).trans (Real.exp_le_exp.mpr (hMK z))
    exact mul_le_mul h1 h2 (abs_nonneg _) (mul_nonneg hCf0 hCf0)
  have hlim : ∀ᵐ z ∂(μ.prod μ),
      Tendsto (fun N => F N z) atTop (𝓝 (f z.1 * f z.2 * Real.exp (K z.1 z.2))) :=
    ae_of_all _ fun z => tendsto_const_nhds.mul (tendsto_taylorExp_real (K z.1 z.2))
  have htend := tendsto_integral_of_dominated_convergence
    (fun _ : Ω × Ω => Cf * Cf * Real.exp MK) hF_meas hbound_int hbound hlim
  exact ge_of_tendsto htend <|
    Eventually.of_forall fun N => integral_prod_factorized_nonneg μ hf (hK.taylorExp N)

/-- Exact swap symmetry of the exponential crossing product integral. -/
theorem integral_prod_exp_crossing_symm {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsFiniteMeasure μ] (f g : Ω → ℝ) {K : Ω → Ω → ℝ} (hK : HasFiniteRankNonneg K) :
    (∫ z : Ω × Ω, f z.1 * g z.2 * Real.exp (K z.1 z.2) ∂(μ.prod μ)) =
      ∫ z : Ω × Ω, g z.1 * f z.2 * Real.exp (K z.1 z.2) ∂(μ.prod μ) := by
  have hswap := MeasureTheory.integral_prod_swap (μ := μ) (ν := μ)
    (fun z : Ω × Ω => g z.1 * f z.2 * Real.exp (K z.1 z.2))
  rw [← hswap]
  refine MeasureTheory.integral_congr_ae (ae_of_all _ fun z => ?_)
  simp only [Prod.fst_swap, Prod.snd_swap]
  rw [hK.symm z.2 z.1, mul_comm (f z.1) (g z.2)]

theorem integrable_exp_crossing_prod {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsFiniteMeasure μ] {u v : Ω → ℝ} (hu : IsBoundedMeasurable u) (hv : IsBoundedMeasurable v)
    {K : Ω → Ω → ℝ} (hK : HasFiniteRankNonneg K) :
    Integrable (fun z : Ω × Ω => u z.1 * v z.2 * Real.exp (K z.1 z.2)) (μ.prod μ) := by
  obtain ⟨MK, hMK⟩ := hK.bdMeas_uncurry.bounded
  have hexp : IsBoundedMeasurable (fun z : Ω × Ω => Real.exp (K z.1 z.2)) :=
    ⟨Real.continuous_exp.measurable.comp hK.bdMeas_uncurry.meas,
      ⟨Real.exp MK, fun z => by
        rw [abs_of_pos (Real.exp_pos _)]
        exact Real.exp_le_exp.mpr ((le_abs_self (K z.1 z.2)).trans (hMK z))⟩⟩
  have hu' : IsBoundedMeasurable (fun z : Ω × Ω => u z.1) := by
    obtain ⟨Cu, hCu⟩ := hu.bounded
    exact ⟨hu.meas.comp measurable_fst, ⟨Cu, fun z => hCu z.1⟩⟩
  have hv' : IsBoundedMeasurable (fun z : Ω × Ω => v z.2) := by
    obtain ⟨Cv, hCv⟩ := hv.bounded
    exact ⟨hv.meas.comp measurable_snd, ⟨Cv, fun z => hCv z.2⟩⟩
  exact ((hu'.mul hv').mul hexp).integrable (μ.prod μ)

/-- Concrete `SliceReflectionHilbert.ReflectionPositiveForm` constructed from any half-space
weight `w` and finite-rank nonnegative crossing kernel `K` on `(Ω, μ)`. -/
noncomputable def expCrossingRPForm {Ω : Type*} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsFiniteMeasure μ] (w : Ω → ℝ) (hw : IsBoundedMeasurable w)
    (K : Ω → Ω → ℝ) (hK : HasFiniteRankNonneg K) :
    ReflectionPositiveForm (BoundedMeasurableSubmodule Ω) where
  form :=
    { toFun := fun f =>
        { toFun := fun g =>
            ∫ z : Ω × Ω,
              (f.1 z.1 * w z.1) * (g.1 z.2 * w z.2) * Real.exp (K z.1 z.2) ∂(μ.prod μ)
          map_add' := fun g₁ g₂ => by
            have h1 := integrable_exp_crossing_prod μ (f.2.mul hw) (g₁.2.mul hw) hK
            have h2 := integrable_exp_crossing_prod μ (f.2.mul hw) (g₂.2.mul hw) hK
            rw [← MeasureTheory.integral_add h1 h2]
            refine MeasureTheory.integral_congr_ae (ae_of_all _ fun z => ?_)
            change
              (f.1 z.1 * w z.1) * ((g₁.1 z.2 + g₂.1 z.2) * w z.2) * Real.exp (K z.1 z.2) = _
            ring
          map_smul' := fun c g => by
            simp only [RingHom.id_apply, smul_eq_mul]
            rw [← MeasureTheory.integral_const_mul]
            refine MeasureTheory.integral_congr_ae (ae_of_all _ fun z => ?_)
            change (f.1 z.1 * w z.1) * ((c * g.1 z.2) * w z.2) * Real.exp (K z.1 z.2) = _
            ring }
      map_add' := fun f₁ f₂ => by
        ext g
        simp only [LinearMap.coe_mk, AddHom.coe_mk, LinearMap.add_apply]
        have h1 := integrable_exp_crossing_prod μ (f₁.2.mul hw) (g.2.mul hw) hK
        have h2 := integrable_exp_crossing_prod μ (f₂.2.mul hw) (g.2.mul hw) hK
        rw [← MeasureTheory.integral_add h1 h2]
        refine MeasureTheory.integral_congr_ae (ae_of_all _ fun z => ?_)
        change
          ((f₁.1 z.1 + f₂.1 z.1) * w z.1) * (g.1 z.2 * w z.2) * Real.exp (K z.1 z.2) = _
        ring
      map_smul' := fun c f => by
        ext g
        simp only [RingHom.id_apply, LinearMap.coe_mk, AddHom.coe_mk,
          LinearMap.smul_apply, smul_eq_mul]
        rw [← MeasureTheory.integral_const_mul]
        refine MeasureTheory.integral_congr_ae (ae_of_all _ fun z => ?_)
        change ((c * f.1 z.1) * w z.1) * (g.1 z.2 * w z.2) * Real.exp (K z.1 z.2) = _
        ring }
  symm f g :=
    integral_prod_exp_crossing_symm μ (fun x => g.1 x * w x) (fun x => f.1 x * w x) hK
  pos f := integral_prod_exp_crossing_nonneg μ (f.2.mul hw) hK

end ExponentialReflectionPositivity

section WilsonFiniteBoxRP

/-- Unconditional entrywise bound `|M i j| ≤ 1` for any real orthogonal matrix `M * Mᵀ = 1`. -/
theorem orth_entry_abs_le_one {n : ℕ} {M : Matrix (Fin n) (Fin n) ℝ} (hM : M * Mᵀ = 1)
    (i j : Fin n) : |M i j| ≤ 1 := by
  have hsq : M i j ^ 2 ≤ 1 := by
    calc
      M i j ^ 2 = M i j * M i j := sq (M i j)
      _ ≤ ∑ k : Fin n, M i k * M i k :=
          Finset.single_le_sum (fun k _ => mul_self_nonneg (M i k)) (Finset.mem_univ j)
      _ = (M * Mᵀ) i i := by simp [Matrix.mul_apply, Matrix.transpose_apply]
      _ = 1 := by rw [hM, Matrix.one_apply_eq]
  have hsq1 : M i j ^ 2 ≤ (1 : ℝ) ^ 2 := by simpa using hsq
  exact abs_le.mpr (abs_le_of_sq_le_sq' hsq1 (by norm_num))

/-- Trace inner product expansion `(A * Bᵀ).trace = ∑ p : Fin n × Fin n, A p.1 p.2 * B p.1 p.2`. -/
theorem trace_mul_transpose_eq_sum {n : ℕ} (A B : Matrix (Fin n) (Fin n) ℝ) :
    (A * Bᵀ).trace = ∑ p : Fin n × Fin n, A p.1 p.2 * B p.1 p.2 := by
  simp only [Matrix.trace, Matrix.diag, Matrix.mul_apply, Matrix.transpose_apply,
    Fintype.sum_prod_type]

/-- Wilson crossing-plaquette coupling kernel across the `t = 0` reflection hyperplane. -/
def wilsonCrossingKernel {Ω : Type*} {n R : ℕ} (β : ℝ)
    (A : Fin R → Ω → Matrix (Fin n) (Fin n) ℝ) (u v : Ω) : ℝ :=
  β * ∑ r : Fin R, (A r u * (A r v)ᵀ).trace

/-- Every Wilson crossing-plaquette kernel for orthogonal link products `A r` and `β ≥ 0`
admits a finite-rank symmetric nonnegative decomposition (`HasFiniteRankNonneg`). -/
theorem hasFiniteRankNonneg_wilsonCrossingKernel {Ω : Type*} [MeasurableSpace Ω] {n R : ℕ}
    {β : ℝ} (hβ : 0 ≤ β) (A : Fin R → Ω → Matrix (Fin n) (Fin n) ℝ)
    (horth : ∀ r : Fin R, ∀ u : Ω, A r u * (A r u)ᵀ = 1)
    (hmeas : ∀ r : Fin R, ∀ i j : Fin n, Measurable (fun u => A r u i j)) :
    HasFiniteRankNonneg (wilsonCrossingKernel β A) := by
  have heq :
      wilsonCrossingKernel β A =
        fun u v => ∑ r : Fin R, ∑ p : Fin n × Fin n,
          β * (A r u p.1 p.2 * A r v p.1 p.2) := by
    funext u v
    unfold wilsonCrossingKernel
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl ?_
    intro r _
    rw [trace_mul_transpose_eq_sum, Finset.mul_sum]
  rw [heq]
  refine HasFiniteRankNonneg.finset_sum Finset.univ _ fun r _ => ?_
  refine HasFiniteRankNonneg.finset_sum Finset.univ _ fun p _ => ?_
  refine HasFiniteRankNonneg.const_mul hβ (HasFiniteRankNonneg.rankOne ?_)
  exact ⟨hmeas r p.1 p.2, ⟨1, fun u => orth_entry_abs_le_one (horth r u) p.1 p.2⟩⟩

/-- Half-lattice intra-region Wilson Boltzmann factor `Real.exp (- S_half u)`. -/
noncomputable def wilsonHalfWeight {E_pos G : Type*} (S_half : (E_pos → G) → ℝ)
    (u : E_pos → G) : ℝ :=
  Real.exp (-S_half u)

/-- Concrete unconditional 4D finite-box Wilson crossing
`SliceReflectionHilbert.ReflectionPositiveForm` on `(E_pos → G, productHaarProb E_pos G)`. -/
noncomputable def wilsonCrossingRPForm {E_pos G : Type*} [Fintype E_pos] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] {n R : ℕ} {β : ℝ} (hβ : 0 ≤ β)
    (A : Fin R → (E_pos → G) → Matrix (Fin n) (Fin n) ℝ)
    (horth : ∀ r : Fin R, ∀ u : E_pos → G, A r u * (A r u)ᵀ = 1)
    (hmeas : ∀ r : Fin R, ∀ i j : Fin n, Measurable (fun u => A r u i j))
    (S_half : (E_pos → G) → ℝ) (hS : IsBoundedMeasurable S_half) :
    ReflectionPositiveForm (BoundedMeasurableSubmodule (E_pos → G)) :=
  expCrossingRPForm (productHaarProb E_pos G) (wilsonHalfWeight S_half) hS.exp_neg
    (wilsonCrossingKernel β A) (hasFiniteRankNonneg_wilsonCrossingKernel hβ A horth hmeas)

/-- Concrete complete OS Hilbert space associated with `wilsonCrossingRPForm`. -/
noncomputable abbrev wilsonOSHilbert {E_pos G : Type*} [Fintype E_pos] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] {n R : ℕ} {β : ℝ} (hβ : 0 ≤ β)
    (A : Fin R → (E_pos → G) → Matrix (Fin n) (Fin n) ℝ)
    (horth : ∀ r : Fin R, ∀ u : E_pos → G, A r u * (A r u)ᵀ = 1)
    (hmeas : ∀ r : Fin R, ∀ i j : Fin n, Measurable (fun u => A r u i j))
    (S_half : (E_pos → G) → ℝ) (hS : IsBoundedMeasurable S_half) :=
  OSHilbert (wilsonCrossingRPForm hβ A horth hmeas S_half hS)

end WilsonFiniteBoxRP

end LatticeReflectionPositivity
