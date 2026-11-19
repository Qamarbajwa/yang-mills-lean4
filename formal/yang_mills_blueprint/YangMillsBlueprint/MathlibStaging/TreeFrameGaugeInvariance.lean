/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.MeasureTheory.Constructions.Pi
public import Mathlib.MeasureTheory.Group.Measure
public import Mathlib.MeasureTheory.Integral.Bochner.Basic
public import Mathlib.MeasureTheory.Measure.Haar.Unique
public import YangMillsBlueprint.MathlibStaging.LatticeHaarGibbs

/-!
# Local Frame Gauge Transformations, Tree-Gauge Trivialization, and Product Haar Invariance

Formalizes vertex frame reassignments
`gaugeTransform src dst g U e = g (src e) * U e * (g (dst e))⁻¹`
on an oriented finite lattice `(V, E)`, proves link trivialization (`= 1`) along spanning trees
and loop conjugation invariance, establishes unimodular right-invariance of `compactHaarProb G`,
and lifts two-sided link translations to `MeasurePreserving` equivalence and exact invariance of
`partitionIntegral` and `weightedExpectation` on `productHaarProb E G`.

## Main results

* `TreeFrameGaugeInvariance.gaugeTransform_eq_one_of_tree_frame`: spanning-tree link flattening.
* `TreeFrameGaugeInvariance.closed_plaquette_gauge_conj`: closed-loop holonomy conjugation.
* `TreeFrameGaugeInvariance.isMulRightInvariant_compactHaarProb`: compact Haar unimodularity.
* `TreeFrameGaugeInvariance.measurePreserving_gaugeTransform`: product Haar preservation.
* `TreeFrameGaugeInvariance.weightedExpectation_gauge_invariant`: exact Gibbs invariance.
-/

@[expose] public section

namespace TreeFrameGaugeInvariance

open MeasureTheory LatticeHaarGibbs

section AlgebraicGaugeTransform

/-- Vertex-frame gauge transformation acting on link variables `U : E → G`. -/
def gaugeTransform {V E G : Type*} [Group G] (src dst : E → V)
    (g : V → G) (U : E → G) : E → G :=
  fun e => g (src e) * U e * (g (dst e))⁻¹

/-- Trivial identity frame `fun _ => 1` acts as the identity gauge transformation. -/
theorem gaugeTransform_one {V E G : Type*} [Group G] (src dst : E → V) (U : E → G) :
    gaugeTransform src dst (fun _ => (1 : G)) U = U := by
  funext e
  simp [gaugeTransform]

/-- Composition of two local frame assignments equals the pointwise product frame. -/
theorem gaugeTransform_comp {V E G : Type*} [Group G] (src dst : E → V)
    (g h : V → G) (U : E → G) :
    gaugeTransform src dst g (gaugeTransform src dst h U) =
      gaugeTransform src dst (fun v => g v * h v) U := by
  funext e
  simp [gaugeTransform, mul_assoc, mul_inv_rev]

/-- Left inverse cancellation for `gaugeTransform`. -/
theorem gaugeTransform_inv_left {V E G : Type*} [Group G] (src dst : E → V)
    (g : V → G) (U : E → G) :
    gaugeTransform src dst (fun v => (g v)⁻¹) (gaugeTransform src dst g U) = U := by
  rw [gaugeTransform_comp]
  have h1 : (fun v => (g v)⁻¹ * g v) = fun _ => (1 : G) := by
    funext v
    exact inv_mul_cancel (g v)
  rw [h1, gaugeTransform_one]

/-- Right inverse cancellation for `gaugeTransform`. -/
theorem gaugeTransform_inv_right {V E G : Type*} [Group G] (src dst : E → V)
    (g : V → G) (U : E → G) :
    gaugeTransform src dst g (gaugeTransform src dst (fun v => (g v)⁻¹) U) = U := by
  rw [gaugeTransform_comp]
  have h1 : (fun v => g v * (g v)⁻¹) = fun _ => (1 : G) := by
    funext v
    exact mul_inv_cancel (g v)
  rw [h1, gaugeTransform_one]

/-- Assigning recursive tree frames `g (dst e) = g (src e) * U e` flattens every tree edge
identically to `1`. -/
theorem gaugeTransform_eq_one_of_tree_frame {V E G : Type*} [Group G] (src dst : E → V)
    (g : V → G) (U : E → G) (e : E) (htree : g (dst e) = g (src e) * U e) :
    gaugeTransform src dst g U e = 1 := by
  unfold gaugeTransform
  rw [htree, mul_inv_cancel]

/-- Four-edge closed loop holonomy conjugates by `g v1` under arbitrary local frame assignments. -/
theorem closed_plaquette_gauge_conj {V E G : Type*} [Group G] (src dst : E → V)
    (g : V → G) (U : E → G) {v1 v2 v3 v4 : V} {e1 e2 e3 e4 : E}
    (hs1 : src e1 = v1) (hd1 : dst e1 = v2)
    (hs2 : src e2 = v2) (hd2 : dst e2 = v3)
    (hs3 : src e3 = v3) (hd3 : dst e3 = v4)
    (hs4 : src e4 = v4) (hd4 : dst e4 = v1) :
    gaugeTransform src dst g U e1 * gaugeTransform src dst g U e2 *
        gaugeTransform src dst g U e3 * gaugeTransform src dst g U e4 =
      g v1 * (U e1 * U e2 * U e3 * U e4) * (g v1)⁻¹ := by
  unfold gaugeTransform
  rw [hs1, hd1, hs2, hd2, hs3, hd3, hs4, hd4]
  simp only [mul_assoc, inv_mul_cancel_left]

end AlgebraicGaugeTransform

section CompactUnimodularHaar

/-- Normalized Haar probability measure on a compact topological group is right-invariant
(unimodular), proved via uniqueness of normalized Haar measure. -/
theorem map_mul_right_compactHaarProb {G : Type*} [Group G] [TopologicalSpace G]
    [CompactSpace G] [IsTopologicalGroup G] [MeasurableSpace G] [BorelSpace G] (g : G) :
    Measure.map (· * g) (compactHaarProb G) = compactHaarProb G := by
  let μ : Measure G := compactHaarProb G
  let μ' : Measure G := Measure.map (· * g) μ
  have hgMeas : Measurable (fun x : G => x * g) := (continuous_mul_const g).measurable
  have : IsProbabilityMeasure μ' := ⟨by
    dsimp only [μ']
    rw [Measure.map_apply hgMeas MeasurableSet.univ, Set.preimage_univ, measure_univ]⟩
  have : Measure.IsMulLeftInvariant μ' := ⟨fun h => by
    have hhMeas : Measurable (fun x : G => h * x) := (continuous_const_mul h).measurable
    dsimp only [μ']
    rw [Measure.map_map hhMeas hgMeas]
    have hcomp : ((fun x : G => h * x) ∘ fun x => x * g) =
        ((fun x : G => x * g) ∘ fun x => h * x) := by
      funext x
      simp [Function.comp, mul_assoc]
    rw [hcomp, ← Measure.map_map hgMeas hhMeas, map_mul_left_eq_self]⟩
  have hsmul : μ' = Measure.haarScalarFactor μ' μ • μ :=
    Measure.isMulInvariant_eq_smul_of_compactSpace μ' μ
  have huniv := congrArg (fun m : Measure G => m Set.univ) hsmul
  simp only [Measure.coe_smul, Pi.smul_apply, measure_univ, ENNReal.smul_def,
    smul_eq_mul, mul_one] at huniv
  have hc : Measure.haarScalarFactor μ' μ = 1 := ENNReal.coe_eq_one.mp huniv.symm
  rw [hc, one_smul] at hsmul
  exact hsmul

/-- `Measure.IsMulRightInvariant` instance for `compactHaarProb G` on any compact group `G`. -/
noncomputable instance isMulRightInvariant_compactHaarProb (G : Type*) [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] :
    Measure.IsMulRightInvariant (compactHaarProb G) :=
  ⟨map_mul_right_compactHaarProb⟩

/-- Left translation `a * ·` preserves `compactHaarProb G`. -/
theorem measurePreserving_mul_left_compactHaarProb {G : Type*} [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (a : G) :
    MeasurePreserving (fun u : G => a * u) (compactHaarProb G) (compactHaarProb G) :=
  ⟨(continuous_const_mul a).measurable, map_mul_left_eq_self (compactHaarProb G) a⟩

/-- Right translation `· * b` preserves `compactHaarProb G`. -/
theorem measurePreserving_mul_right_compactHaarProb {G : Type*} [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (b : G) :
    MeasurePreserving (fun u : G => u * b) (compactHaarProb G) (compactHaarProb G) :=
  ⟨(continuous_mul_const b).measurable, map_mul_right_compactHaarProb b⟩

/-- Two-sided multiplication `u ↦ a * u * b` preserves `compactHaarProb G`. -/
theorem measurePreserving_twoSided_compactHaarProb {G : Type*} [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (a b : G) :
    MeasurePreserving (fun u : G => a * u * b) (compactHaarProb G) (compactHaarProb G) :=
  (measurePreserving_mul_right_compactHaarProb b).comp
    (measurePreserving_mul_left_compactHaarProb a)

end CompactUnimodularHaar

section ProductLatticeGaugeInvariance

/-- Measurable equivalence on `(E → G)` induced by vertex frame transformation `g : V → G`. -/
def gaugeTransformMeasurableEquiv {V E G : Type*} [Group G] [TopologicalSpace G]
    [IsTopologicalGroup G] [MeasurableSpace G] [BorelSpace G]
    (src dst : E → V) (g : V → G) : (E → G) ≃ᵐ (E → G) where
  toFun := gaugeTransform src dst g
  invFun := gaugeTransform src dst (fun v => (g v)⁻¹)
  left_inv U := gaugeTransform_inv_left src dst g U
  right_inv U := gaugeTransform_inv_right src dst g U
  measurable_toFun := by
    refine measurable_pi_iff.mpr fun e => ?_
    exact ((continuous_mul_const (g (dst e))⁻¹).comp
      (continuous_const_mul (g (src e)))).measurable.comp (measurable_pi_apply e)
  measurable_invFun := by
    refine measurable_pi_iff.mpr fun e => ?_
    exact ((continuous_mul_const ((g (dst e))⁻¹)⁻¹).comp
      (continuous_const_mul (g (src e))⁻¹)).measurable.comp (measurable_pi_apply e)

/-- Any local frame assignment preserves the finite-product Haar probability measure on
`(E → G)` identically (with zero Jacobian or Gribov ambiguity). -/
theorem measurePreserving_gaugeTransform {V E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (src dst : E → V) (g : V → G) :
    MeasurePreserving (gaugeTransformMeasurableEquiv src dst g)
      (productHaarProb E G) (productHaarProb E G) :=
  MeasureTheory.measurePreserving_pi _ _ fun e =>
    measurePreserving_twoSided_compactHaarProb (g (src e)) (g (dst e))⁻¹

/-- Integrability of a function on `(E → G)` is preserved under arbitrary gauge transforms. -/
theorem integrable_gaugeTransform_iff {V E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (src dst : E → V) (g : V → G)
    (F : (E → G) → ℝ) :
    Integrable (fun U => F (gaugeTransform src dst g U)) (productHaarProb E G) ↔
      Integrable F (productHaarProb E G) :=
  (measurePreserving_gaugeTransform src dst g).integrable_comp_emb
    (gaugeTransformMeasurableEquiv src dst g).measurableEmbedding

/-- Exact Haar integral invariance under arbitrary local frame assignments `g : V → G`. -/
theorem integral_gaugeTransform {V E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (src dst : E → V) (g : V → G)
    (F : (E → G) → ℝ) :
    (∫ U, F (gaugeTransform src dst g U) ∂(productHaarProb E G)) =
      ∫ U, F U ∂(productHaarProb E G) :=
  (measurePreserving_gaugeTransform src dst g).integral_comp' F

/-- Partition integral `∫ exp (-S U) ∂μ` is invariant under pulling back `S` along `g`. -/
theorem partitionIntegral_gaugeTransform {V E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (src dst : E → V) (g : V → G)
    (S : (E → G) → ℝ) :
    partitionIntegral (productHaarProb E G) (fun U => S (gaugeTransform src dst g U)) =
      partitionIntegral (productHaarProb E G) S := by
  unfold partitionIntegral expWeight
  exact integral_gaugeTransform src dst g (fun U => Real.exp (-S U))

/-- Normalized Boltzmann expectation is invariant under pulling back `(S, f)` along `g`. -/
theorem weightedExpectation_gaugeTransform {V E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (src dst : E → V) (g : V → G)
    (S f : (E → G) → ℝ) :
    weightedExpectation (productHaarProb E G)
        (fun U => S (gaugeTransform src dst g U))
        (fun U => f (gaugeTransform src dst g U)) =
      weightedExpectation (productHaarProb E G) S f := by
  unfold weightedExpectation
  have hnum :=
    integral_gaugeTransform src dst g (fun U => f U * expWeight S U)
  have hden := partitionIntegral_gaugeTransform src dst g S
  change (∫ U, f (gaugeTransform src dst g U) *
      expWeight (fun V => S (gaugeTransform src dst g V)) U ∂(productHaarProb E G)) /
      partitionIntegral (productHaarProb E G) (fun V => S (gaugeTransform src dst g V)) =
    (∫ U, f U * expWeight S U ∂(productHaarProb E G)) /
      partitionIntegral (productHaarProb E G) S
  have hexp :
      (fun U => f (gaugeTransform src dst g U) *
          expWeight (fun V => S (gaugeTransform src dst g V)) U) =
        fun U => f (gaugeTransform src dst g U) * expWeight S (gaugeTransform src dst g U) := rfl
  rw [hexp, hnum, hden]

/-- For any gauge-invariant action `S` (`∀ U, S (gaugeTransform src dst g U) = S U`) and any
observable `f`, evaluating `f` in the reassigned frame `g` yields the identical normalized
Boltzmann expectation under `productHaarProb E G`. -/
theorem weightedExpectation_gauge_invariant {V E G : Type*} [Fintype E] [Group G]
    [TopologicalSpace G] [CompactSpace G] [IsTopologicalGroup G]
    [MeasurableSpace G] [BorelSpace G] (src dst : E → V) (g : V → G)
    {S f : (E → G) → ℝ} (hS : ∀ U, S (gaugeTransform src dst g U) = S U) :
    weightedExpectation (productHaarProb E G) S (fun U => f (gaugeTransform src dst g U)) =
      weightedExpectation (productHaarProb E G) S f := by
  have hSfn : (fun U => S (gaugeTransform src dst g U)) = S := funext hS
  simpa only [hSfn] using weightedExpectation_gaugeTransform src dst g S f

end ProductLatticeGaugeInvariance

end TreeFrameGaugeInvariance
