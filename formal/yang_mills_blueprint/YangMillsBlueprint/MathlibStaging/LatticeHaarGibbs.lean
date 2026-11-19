/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Analysis.SpecialFunctions.ExpDeriv
public import Mathlib.MeasureTheory.Constructions.Pi
public import Mathlib.MeasureTheory.Integral.Bochner.Basic
public import Mathlib.MeasureTheory.Measure.Haar.Basic
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.GibbsDensityCapVariance

/-!
# Finite-Product Compact Group Haar Probability and Bounded-Oscillation Weights

Constructs normalized Haar probability measures on compact topological groups and finite
product spaces `(E → G)`, together with Boltzmann exponential weight bounds and density caps
under bounded action oscillation `vMin ≤ S ≤ vMax`.

## Main results

* `LatticeHaarGibbs.compactHaarProb`: normalized Haar probability measure on compact `G`.
* `LatticeHaarGibbs.productHaarProb`: finite product Haar probability measure on `(E → G)`.
* `LatticeHaarGibbs.partitionIntegral_pos`: positivity of `∫ exp (-S x) ∂ν`.
* `LatticeHaarGibbs.boltzmannDensity_le_exp_osc`: Holley-Stroock cap `≤ Real.exp (vMax - vMin)`.
* `LatticeHaarGibbs.weightedExpectation_ge_exp_neg_osc_mul_integral`: weighted lower bound
  `Real.exp (-(vMax - vMin)) * (∫ x, f x ∂ν) ≤ weightedExpectation ν S f`.
-/

@[expose] public section

namespace LatticeHaarGibbs

open MeasureTheory

section CompactHaarProbability

/-- The full group `Set.univ` as a `PositiveCompacts` witness for a compact group `G`. -/
def compactUnivPosCompact (G : Type*) [Group G] [TopologicalSpace G] [CompactSpace G] :
    TopologicalSpace.PositiveCompacts G where
  carrier := Set.univ
  isCompact' := isCompact_univ
  interior_nonempty' := by simp [Set.univ_nonempty]

/-- Normalized Haar probability measure (`measure univ = 1`) on a compact topological group. -/
noncomputable def compactHaarProb (G : Type*) [Group G] [TopologicalSpace G] [CompactSpace G]
    [IsTopologicalGroup G] [MeasurableSpace G] [BorelSpace G] : Measure G :=
  Measure.haarMeasure (compactUnivPosCompact G)

noncomputable instance isProbabilityMeasure_compactHaarProb (G : Type*) [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] :
    IsProbabilityMeasure (compactHaarProb G) :=
  ⟨by
    unfold compactHaarProb compactUnivPosCompact
    exact Measure.haarMeasure_self⟩

noncomputable instance isHaarMeasure_compactHaarProb (G : Type*) [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] :
    Measure.IsHaarMeasure (compactHaarProb G) := by
  unfold compactHaarProb
  exact Measure.isHaarMeasure_haarMeasure _

/-- Finite-index product Haar probability measure on maps `E → G`. -/
noncomputable def productHaarProb (E G : Type*) [Fintype E] [Group G] [TopologicalSpace G]
    [CompactSpace G] [IsTopologicalGroup G] [MeasurableSpace G] [BorelSpace G] :
    Measure (E → G) :=
  Measure.pi (fun _ : E => compactHaarProb G)

noncomputable instance isProbabilityMeasure_productHaarProb (E G : Type*) [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] :
    IsProbabilityMeasure (productHaarProb E G) := by
  unfold productHaarProb
  exact Measure.pi.instIsProbabilityMeasure _

noncomputable instance isHaarMeasure_productHaarProb (E G : Type*) [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] [MeasurableMul G] :
    Measure.IsHaarMeasure (productHaarProb E G) := by
  unfold productHaarProb
  exact Measure.pi.isHaarMeasure _

end CompactHaarProbability

section BoundedOscillationExpectation

/-- Unnormalized exponential weight `Real.exp (-S x)`. -/
noncomputable def expWeight {Ω : Type*} (S : Ω → ℝ) (x : Ω) : ℝ :=
  Real.exp (-S x)

/-- Normalization integral `∫ x, expWeight S x ∂ν`. -/
noncomputable def partitionIntegral {Ω : Type*} [MeasurableSpace Ω]
    (ν : Measure Ω) (S : Ω → ℝ) : ℝ :=
  ∫ x, expWeight S x ∂ν

/-- Normalized expectation `(∫ x, f x * expWeight S x ∂ν) / partitionIntegral ν S`. -/
noncomputable def weightedExpectation {Ω : Type*} [MeasurableSpace Ω]
    (ν : Measure Ω) (S f : Ω → ℝ) : ℝ :=
  (∫ x, f x * expWeight S x ∂ν) / partitionIntegral ν S

/-- Partition integral lower bound `Real.exp (-vMax) ≤ partitionIntegral ν S`. -/
theorem partitionIntegral_ge_exp_neg_max {Ω : Type*} [MeasurableSpace Ω]
    {ν : Measure Ω} [IsProbabilityMeasure ν] {S : Ω → ℝ} {vMax : ℝ}
    (hint : Integrable (expWeight S) ν) (hmax : ∀ x, S x ≤ vMax) :
    Real.exp (-vMax) ≤ partitionIntegral ν S := by
  unfold partitionIntegral
  have hle : ∀ x, Real.exp (-vMax) ≤ expWeight S x := fun x =>
    Real.exp_le_exp.mpr (neg_le_neg (hmax x))
  have hintc := integral_mono (integrable_const (Real.exp (-vMax))) hint hle
  rwa [integral_const, probReal_univ, one_smul] at hintc

/-- Partition integral upper bound `partitionIntegral ν S ≤ Real.exp (-vMin)`. -/
theorem partitionIntegral_le_exp_neg_min {Ω : Type*} [MeasurableSpace Ω]
    {ν : Measure Ω} [IsProbabilityMeasure ν] {S : Ω → ℝ} {vMin : ℝ}
    (hint : Integrable (expWeight S) ν) (hmin : ∀ x, vMin ≤ S x) :
    partitionIntegral ν S ≤ Real.exp (-vMin) := by
  unfold partitionIntegral
  have hle : ∀ x, expWeight S x ≤ Real.exp (-vMin) := fun x =>
    Real.exp_le_exp.mpr (neg_le_neg (hmin x))
  have hintc := integral_mono hint (integrable_const (Real.exp (-vMin))) hle
  rwa [integral_const, probReal_univ, one_smul] at hintc

/-- Strict positivity of `partitionIntegral ν S` under a finite upper action bound. -/
theorem partitionIntegral_pos {Ω : Type*} [MeasurableSpace Ω]
    {ν : Measure Ω} [IsProbabilityMeasure ν] {S : Ω → ℝ} {vMax : ℝ}
    (hint : Integrable (expWeight S) ν) (hmax : ∀ x, S x ≤ vMax) :
    0 < partitionIntegral ν S :=
  lt_of_lt_of_le (Real.exp_pos (-vMax)) (partitionIntegral_ge_exp_neg_max hint hmax)

/-- Normalized expectation of a constant function equals that constant. -/
theorem weightedExpectation_const {Ω : Type*} [MeasurableSpace Ω]
    {ν : Measure Ω} [IsProbabilityMeasure ν] {S : Ω → ℝ} {vMax : ℝ} (c : ℝ)
    (hint : Integrable (expWeight S) ν) (hmax : ∀ x, S x ≤ vMax) :
    weightedExpectation ν S (fun _ => c) = c := by
  unfold weightedExpectation
  change (∫ x, c * expWeight S x ∂ν) / partitionIntegral ν S = c
  rw [integral_const_mul]
  have hpos : partitionIntegral ν S ≠ 0 := ne_of_gt (partitionIntegral_pos hint hmax)
  change (c * partitionIntegral ν S) / partitionIntegral ν S = c
  rw [mul_div_assoc, div_self hpos, mul_one]

/-- Pointwise Radon-Nikodym density cap `expWeight S x / Z ≤ Real.exp (vMax - vMin)`. -/
theorem boltzmannDensity_le_exp_osc {Ω : Type*} [MeasurableSpace Ω]
    {ν : Measure Ω} [IsProbabilityMeasure ν] {S : Ω → ℝ} {vMin vMax : ℝ}
    (hint : Integrable (expWeight S) ν) (hmin : ∀ y, vMin ≤ S y)
    (hmax : ∀ y, S y ≤ vMax) (x : Ω) :
    expWeight S x / partitionIntegral ν S ≤ Real.exp (vMax - vMin) := by
  have hwmin : 0 < Real.exp (-vMax) := Real.exp_pos (-vMax)
  have hwmax : 0 ≤ expWeight S x := le_of_lt (Real.exp_pos (-S x))
  have hZ : Real.exp (-vMax) ≤ partitionIntegral ν S :=
    partitionIntegral_ge_exp_neg_max hint hmax
  have hle : expWeight S x ≤ Real.exp (-vMin) :=
    Real.exp_le_exp.mpr (neg_le_neg (hmin x))
  have heq : Real.exp (-vMin) = Real.exp (vMax - vMin) * Real.exp (-vMax) := by
    rw [← Real.exp_add]
    congr 1
    ring
  rw [heq] at hle
  exact GibbsDensityCapVariance.gibbsRatio_le_bound hwmin hwmax hZ hle

/-- Oscillation-attenuated expectation lower bound:
`Real.exp (-(vMax - vMin)) * (∫ x, f x ∂ν) ≤ weightedExpectation ν S f`. -/
theorem weightedExpectation_ge_exp_neg_osc_mul_integral {Ω : Type*} [MeasurableSpace Ω]
    {ν : Measure Ω} [IsProbabilityMeasure ν] {S f : Ω → ℝ} {vMin vMax : ℝ}
    (hint : Integrable (expWeight S) ν) (hf : Integrable f ν)
    (hfw : Integrable (fun x => f x * expWeight S x) ν)
    (hf0 : ∀ x, 0 ≤ f x) (hmin : ∀ x, vMin ≤ S x) (hmax : ∀ x, S x ≤ vMax) :
    Real.exp (-(vMax - vMin)) * (∫ x, f x ∂ν) ≤ weightedExpectation ν S f := by
  have hI0 : 0 ≤ ∫ x, f x ∂ν := integral_nonneg hf0
  have hpt : ∀ x, Real.exp (-vMax) * f x ≤ f x * expWeight S x := fun x => by
    have hle : Real.exp (-vMax) ≤ expWeight S x :=
      Real.exp_le_exp.mpr (neg_le_neg (hmax x))
    rw [mul_comm (Real.exp (-vMax)) (f x)]
    exact mul_le_mul_of_nonneg_left hle (hf0 x)
  have hnum_int : ∫ x, Real.exp (-vMax) * f x ∂ν ≤ ∫ x, f x * expWeight S x ∂ν :=
    integral_mono (hf.const_mul _) hfw hpt
  rw [integral_const_mul] at hnum_int
  have hZpos : 0 < partitionIntegral ν S := partitionIntegral_pos hint hmax
  have hZle : partitionIntegral ν S ≤ Real.exp (-vMin) :=
    partitionIntegral_le_exp_neg_min hint hmin
  have hExpPos : 0 < Real.exp (-vMin) := Real.exp_pos (-vMin)
  have hfrac :
      (Real.exp (-vMax) * ∫ x, f x ∂ν) / Real.exp (-vMin) ≤
        (∫ x, f x * expWeight S x ∂ν) / partitionIntegral ν S := by
    rw [div_le_div_iff₀ hExpPos hZpos]
    have hprod0 : 0 ≤ Real.exp (-vMax) * ∫ x, f x ∂ν :=
      mul_nonneg (le_of_lt (Real.exp_pos (-vMax))) hI0
    calc (Real.exp (-vMax) * ∫ x, f x ∂ν) * partitionIntegral ν S
        ≤ (Real.exp (-vMax) * ∫ x, f x ∂ν) * Real.exp (-vMin) :=
          mul_le_mul_of_nonneg_left hZle hprod0
      _ ≤ (∫ x, f x * expWeight S x ∂ν) * Real.exp (-vMin) :=
          mul_le_mul_of_nonneg_right hnum_int (le_of_lt hExpPos)
  have hExpEq : Real.exp (-(vMax - vMin)) = Real.exp (-vMax) / Real.exp (-vMin) := by
    rw [← Real.exp_sub]
    congr 1
    ring
  unfold weightedExpectation
  rw [hExpEq, div_mul_eq_mul_div]
  exact hfrac

end BoundedOscillationExpectation

section CompactGroupProductGibbs

/-- Normalization positivity on finite product Haar probability space `(E → G)`. -/
theorem productHaar_partitionIntegral_pos {E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] {S : (E → G) → ℝ} {vMax : ℝ}
    (hint : Integrable (expWeight S) (productHaarProb E G)) (hmax : ∀ U, S U ≤ vMax) :
    0 < partitionIntegral (productHaarProb E G) S :=
  partitionIntegral_pos hint hmax

/-- Pointwise Boltzmann density cap on `(E → G)` relative to `productHaarProb E G`. -/
theorem productHaar_density_le_exp_osc {E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] {S : (E → G) → ℝ} {vMin vMax : ℝ}
    (hint : Integrable (expWeight S) (productHaarProb E G))
    (hmin : ∀ V, vMin ≤ S V) (hmax : ∀ V, S V ≤ vMax) (U : E → G) :
    expWeight S U / partitionIntegral (productHaarProb E G) S ≤ Real.exp (vMax - vMin) :=
  boltzmannDensity_le_exp_osc hint hmin hmax U

/-- Bounded-oscillation expectation lower bound relative to `productHaarProb E G`. -/
theorem productHaar_expectation_ge_exp_neg_osc {E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] {S f : (E → G) → ℝ} {vMin vMax : ℝ}
    (hint : Integrable (expWeight S) (productHaarProb E G))
    (hf : Integrable f (productHaarProb E G))
    (hfw : Integrable (fun U => f U * expWeight S U) (productHaarProb E G))
    (hf0 : ∀ U, 0 ≤ f U) (hmin : ∀ U, vMin ≤ S U) (hmax : ∀ U, S U ≤ vMax) :
    Real.exp (-(vMax - vMin)) * (∫ U, f U ∂(productHaarProb E G)) ≤
      weightedExpectation (productHaarProb E G) S f :=
  weightedExpectation_ge_exp_neg_osc_mul_integral hint hf hfw hf0 hmin hmax

end CompactGroupProductGibbs

end LatticeHaarGibbs
