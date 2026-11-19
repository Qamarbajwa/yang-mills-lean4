/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Algebra.BigOperators.Group.Finset.Basic
public import Mathlib.Algebra.Order.BigOperators.Group.Finset
public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.Data.Finset.Powerset
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.BalabanPolymerCollar

/-!
# Abstract Finite Polymer Gas, Dobrushin-Kotecký-Preiss Cluster Bounds & Collar Decoupling

Formalizes the constructive-QFT cluster expansion foundations for signed abstract polymer gases:

* `polymerZ`: finite polymer partition function over compatible subfamilies.
* `polymerZ_eq_erase_add`: exact deletion identity `Z(S) = Z(S \ {x}) + z(x) * Z(S \ N[x])`.
* `polymerZ_union_of_compat`: exact factorization `Z(S₁ ∪ S₂) = Z(S₁) * Z(S₂)` across decoupled
  regions.
* `dobrushin_kp_cluster_bounds`: unconditional induction proving strict positivity `0 < Z(S)` and
  uniform pinned ratio bounds `Z(S \ N[x]) / Z(S) ≤ exp(a(x))` under the Dobrushin-Kotecký-Preiss
  condition.
* `polymerZ_collar_decoupling_le`: `L`-uniform logarithmic boundary-collar decoupling bound
  `|log Z(S₁ ∪ S₂ ∪ B) - (log Z(S₁) + log Z(S₂))| ≤ ∑_{y ∈ B} (-log(1 - |z(y)| * exp(a(y))))`.
-/

@[expose] public section

namespace AbstractPolymerCluster

open scoped Classical
open BalabanPolymerCollar

section PolymerDefinitions

variable {P : Type*} [DecidableEq P]

/-- A finite polymer subset `I` is compatible when distinct elements are not incompatible. -/
def IsCompat (incomp : P → P → Prop) (I : Finset P) : Prop :=
  ∀ x ∈ I, ∀ y ∈ I, x ≠ y → ¬ incomp x y

/-- Incompatible neighborhood `N_S[x] = {y ∈ S | incomp x y}`. -/
noncomputable def nbhd (incomp : P → P → Prop) (S : Finset P) (x : P) : Finset P :=
  S.filter (fun y => incomp x y)

/-- Compatible complement `S \ N[x] = {y ∈ S | ¬ incomp x y}`. -/
noncomputable def withoutNbhd (incomp : P → P → Prop) (S : Finset P) (x : P) : Finset P :=
  S.filter (fun y => ¬ incomp x y)

/-- Finite abstract polymer partition function `Z(S) = ∑_{I ⊆ S compat} ∏_{y ∈ I} z y`. -/
noncomputable def polymerZ (incomp : P → P → Prop) (z : P → ℝ) (S : Finset P) : ℝ :=
  ∑ I ∈ S.powerset.filter (IsCompat incomp), ∏ y ∈ I, z y

/-- Dobrushin-Kotecký-Preiss logarithmic single-polymer weight `-log (1 - |z y| * exp (a y))`. -/
noncomputable def kpLogWeight (z a : P → ℝ) (y : P) : ℝ :=
  -Real.log (1 - |z y| * Real.exp (a y))

omit [DecidableEq P] in
theorem polymerZ_empty (incomp : P → P → Prop) (z : P → ℝ) :
    polymerZ incomp z (∅ : Finset P) = 1 := by
  unfold polymerZ
  have hcompat : IsCompat incomp (∅ : Finset P) := by
    intro x hx
    exact False.elim (Finset.notMem_empty x hx)
  have hfilt :
      ((∅ : Finset P).powerset.filter (IsCompat incomp)) = {(∅ : Finset P)} := by
    ext I
    simp only [Finset.mem_filter, Finset.mem_powerset, Finset.subset_empty, Finset.mem_singleton]
    constructor
    · rintro ⟨rfl, _⟩
      rfl
    · rintro rfl
      exact ⟨rfl, hcompat⟩
  rw [hfilt, Finset.sum_singleton, Finset.prod_empty]

omit [DecidableEq P] in
theorem withoutNbhd_subset (incomp : P → P → Prop) (S : Finset P) (x : P) :
    withoutNbhd incomp S x ⊆ S :=
  Finset.filter_subset _ _

omit [DecidableEq P] in
theorem nbhd_subset (incomp : P → P → Prop) (S : Finset P) (x : P) :
    nbhd incomp S x ⊆ S :=
  Finset.filter_subset _ _

theorem withoutNbhd_eq_sdiff_nbhd (incomp : P → P → Prop) {S U : Finset P} (hSU : S ⊆ U)
    (x : P) :
    withoutNbhd incomp S x = S \ (S ∩ nbhd incomp U x) := by
  ext y
  simp only [withoutNbhd, nbhd, Finset.mem_filter, Finset.mem_sdiff, Finset.mem_inter]
  constructor
  · rintro ⟨hyS, hnot⟩
    refine ⟨hyS, fun ⟨_, _, hin⟩ => hnot hin⟩
  · rintro ⟨hyS, hnot⟩
    exact ⟨hyS, fun hin => hnot ⟨hyS, hSU hyS, hin⟩⟩

omit [DecidableEq P] in
theorem notMem_withoutNbhd {incomp : P → P → Prop} (hrefl : ∀ u, incomp u u)
    (S : Finset P) (x : P) : x ∉ withoutNbhd incomp S x := by
  simp only [withoutNbhd, Finset.mem_filter]
  rintro ⟨_, hnot⟩
  exact hnot (hrefl x)

theorem withoutNbhd_subset_erase {incomp : P → P → Prop} (hrefl : ∀ u, incomp u u)
    (S : Finset P) (x : P) : withoutNbhd incomp S x ⊆ S.erase x := by
  intro y hy
  have hyS : y ∈ S := (Finset.mem_filter.mp hy).1
  have hne : y ≠ x := by
    rintro rfl
    exact notMem_withoutNbhd hrefl S y hy
  exact Finset.mem_erase.mpr ⟨hne, hyS⟩

/-- Exact polymer deletion recurrence `Z(S) = Z(S.erase x) + z x * Z(S \ N[x])`. -/
theorem polymerZ_eq_erase_add {incomp : P → P → Prop} (hrefl : ∀ u, incomp u u)
    (hsym : ∀ u v, incomp u v → incomp v u) (z : P → ℝ) {S : Finset P} (hx : x ∈ S) :
    polymerZ incomp z S =
      polymerZ incomp z (S.erase x) + z x * polymerZ incomp z (withoutNbhd incomp S x) := by
  unfold polymerZ
  let A := S.powerset.filter (IsCompat incomp)
  have hsplit := Finset.sum_filter_add_sum_filter_not A (fun I => x ∈ I)
    (fun I => ∏ y ∈ I, z y)
  have hnot :
      A.filter (fun I => ¬ x ∈ I) = (S.erase x).powerset.filter (IsCompat incomp) := by
    ext I
    simp only [A, Finset.mem_filter, Finset.mem_powerset, Finset.subset_erase]
    tauto
  let B := (withoutNbhd incomp S x).powerset.filter (IsCompat incomp)
  have hbij :
      (∑ I ∈ A.filter (fun I => x ∈ I), ∏ y ∈ I, z y) =
        z x * ∑ J ∈ B, ∏ y ∈ J, z y := by
    rw [Finset.mul_sum]
    refine Finset.sum_bij (fun I _ => I.erase x) ?_ ?_ ?_ ?_
    · intro I hI
      simp only [A, Finset.mem_filter, Finset.mem_powerset] at hI
      rcases hI with ⟨⟨hIS, hcompat⟩, hxI⟩
      simp only [B, withoutNbhd, Finset.mem_filter, Finset.mem_powerset]
      refine ⟨?_, ?_⟩
      · intro y hy
        rw [Finset.mem_erase] at hy
        rw [Finset.mem_filter]
        exact ⟨hIS hy.2, hcompat x hxI y hy.2 (Ne.symm hy.1)⟩
      · intro u hu v hv huv
        exact hcompat u (Finset.mem_of_mem_erase hu) v (Finset.mem_of_mem_erase hv) huv
    · intro I₁ hI₁ I₂ hI₂ heq
      have hx₁ : x ∈ I₁ := (Finset.mem_filter.mp hI₁).2
      have hx₂ : x ∈ I₂ := (Finset.mem_filter.mp hI₂).2
      have h1 := Finset.insert_erase hx₁
      have h2 := Finset.insert_erase hx₂
      rw [← h1, ← h2, heq]
    · intro J hJ
      simp only [B, withoutNbhd, Finset.mem_filter, Finset.mem_powerset] at hJ
      rcases hJ with ⟨hJw, hcompatJ⟩
      refine ⟨insert x J, ?_, ?_⟩
      · simp only [A, Finset.mem_filter, Finset.mem_powerset]
        refine ⟨⟨Finset.insert_subset_iff.mpr ⟨hx, Finset.Subset.trans hJw
            (Finset.filter_subset _ _)⟩, ?_⟩, Finset.mem_insert_self x J⟩
        intro u hu v hv huv
        rcases Finset.mem_insert.mp hu with rfl | huJ
        · rcases Finset.mem_insert.mp hv with rfl | hvJ
          · exact False.elim (huv rfl)
          · exact (Finset.mem_filter.mp (hJw hvJ)).2
        · rcases Finset.mem_insert.mp hv with rfl | hvJ
          · intro hinc
            exact (Finset.mem_filter.mp (hJw huJ)).2 (hsym u v hinc)
          · exact hcompatJ u huJ v hvJ huv
      · have hxnot : x ∉ J := fun hxJ => notMem_withoutNbhd hrefl S x (hJw hxJ)
        exact Finset.erase_insert hxnot
    · intro I hI
      have hxI : x ∈ I := (Finset.mem_filter.mp hI).2
      rw [← Finset.prod_erase_mul I z hxI]
      ring
  rw [← hsplit, hnot, hbij, add_comm]

/-- Partition function factorizes identically over two mutually compatible disjoint regions. -/
theorem polymerZ_union_of_compat {incomp : P → P → Prop}
    (hsym : ∀ u v, incomp u v → incomp v u) (z : P → ℝ)
    {S₁ S₂ : Finset P} (hdisj : Disjoint S₁ S₂)
    (hcompat : ∀ u ∈ S₁, ∀ v ∈ S₂, ¬ incomp u v) :
    polymerZ incomp z (S₁ ∪ S₂) = polymerZ incomp z S₁ * polymerZ incomp z S₂ := by
  unfold polymerZ
  let C₁ := S₁.powerset.filter (IsCompat incomp)
  let C₂ := S₂.powerset.filter (IsCompat incomp)
  rw [Finset.sum_mul_sum, ← Finset.sum_product']
  symm
  refine Finset.sum_bij (fun p _ => p.1 ∪ p.2) ?_ ?_ ?_ ?_
  · intro p hp
    rcases Finset.mem_product.mp hp with ⟨hp1, hp2⟩
    simp only [Finset.mem_filter, Finset.mem_powerset] at hp1 hp2
    simp only [Finset.mem_filter, Finset.mem_powerset]
    refine ⟨Finset.union_subset_union hp1.1 hp2.1, ?_⟩
    intro u hu v hv huv
    rcases Finset.mem_union.mp hu with hu1 | hu2
    · rcases Finset.mem_union.mp hv with hv1 | hv2
      · exact hp1.2 u hu1 v hv1 huv
      · exact hcompat u (hp1.1 hu1) v (hp2.1 hv2)
    · rcases Finset.mem_union.mp hv with hv1 | hv2
      · intro hinc
        exact hcompat v (hp1.1 hv1) u (hp2.1 hu2) (hsym u v hinc)
      · exact hp2.2 u hu2 v hv2 huv
  · intro p hp q hq heq
    rcases Finset.mem_product.mp hp with ⟨hp1, hp2⟩
    rcases Finset.mem_product.mp hq with ⟨hq1, hq2⟩
    have hp1s : p.1 ⊆ S₁ := (Finset.mem_powerset.mp (Finset.mem_filter.mp hp1).1)
    have hp2s : p.2 ⊆ S₂ := (Finset.mem_powerset.mp (Finset.mem_filter.mp hp2).1)
    have hq1s : q.1 ⊆ S₁ := (Finset.mem_powerset.mp (Finset.mem_filter.mp hq1).1)
    have hq2s : q.2 ⊆ S₂ := (Finset.mem_powerset.mp (Finset.mem_filter.mp hq2).1)
    have h1 : p.1 = q.1 := by
      have hi := congrArg (fun T : Finset P => T ∩ S₁) heq
      have hd1 : p.2 ∩ S₁ = ∅ :=
        Finset.disjoint_iff_inter_eq_empty.mp (Finset.disjoint_of_subset_left hp2s hdisj.symm)
      have hd2 : q.2 ∩ S₁ = ∅ :=
        Finset.disjoint_iff_inter_eq_empty.mp (Finset.disjoint_of_subset_left hq2s hdisj.symm)
      rwa [Finset.union_inter_distrib_right, Finset.union_inter_distrib_right, hd1, hd2,
        Finset.union_empty, Finset.union_empty, Finset.inter_eq_left.mpr hp1s,
        Finset.inter_eq_left.mpr hq1s] at hi
    have h2 : p.2 = q.2 := by
      have hi := congrArg (fun T : Finset P => T ∩ S₂) heq
      have hd1 : p.1 ∩ S₂ = ∅ :=
        Finset.disjoint_iff_inter_eq_empty.mp (Finset.disjoint_of_subset_left hp1s hdisj)
      have hd2 : q.1 ∩ S₂ = ∅ :=
        Finset.disjoint_iff_inter_eq_empty.mp (Finset.disjoint_of_subset_left hq1s hdisj)
      rwa [Finset.union_inter_distrib_right, Finset.union_inter_distrib_right, hd1, hd2,
        Finset.empty_union, Finset.empty_union, Finset.inter_eq_left.mpr hp2s,
        Finset.inter_eq_left.mpr hq2s] at hi
    exact Prod.ext h1 h2
  · intro I hI
    simp only [Finset.mem_filter, Finset.mem_powerset] at hI
    refine ⟨(I ∩ S₁, I ∩ S₂), ?_, ?_⟩
    · simp only [Finset.mem_product, Finset.mem_filter, Finset.mem_powerset]
      refine ⟨⟨Finset.inter_subset_right, ?_⟩, ⟨Finset.inter_subset_right, ?_⟩⟩
      · intro u hu v hv huv
        exact hI.2 u (Finset.mem_inter.mp hu).1 v (Finset.mem_inter.mp hv).1 huv
      · intro u hu v hv huv
        exact hI.2 u (Finset.mem_inter.mp hu).1 v (Finset.mem_inter.mp hv).1 huv
    · rw [← Finset.inter_union_distrib_left]
      exact Finset.inter_eq_left.mpr hI.1
  · intro p hp
    rcases Finset.mem_product.mp hp with ⟨hp1, hp2⟩
    have hp1s : p.1 ⊆ S₁ := Finset.mem_powerset.mp (Finset.mem_filter.mp hp1).1
    have hp2s : p.2 ⊆ S₂ := Finset.mem_powerset.mp (Finset.mem_filter.mp hp2).1
    have hdp : Disjoint p.1 p.2 :=
      Finset.disjoint_of_subset_right hp2s (Finset.disjoint_of_subset_left hp1s hdisj)
    exact (Finset.prod_union hdp).symm

end PolymerDefinitions

section ClusterConvergence

variable {P : Type*} [DecidableEq P]

/-- Classical small-activity bound `-log (1 - t) ≤ 2 * t` on `[0, 1/2]`. -/
theorem neg_log_one_sub_le_two_mul {t : ℝ} (ht0 : 0 ≤ t) (ht1 : t ≤ 1 / 2) :
    -Real.log (1 - t) ≤ 2 * t := by
  have h1t : 0 < 1 - t := by linarith
  have h2t : 0 < 1 + 2 * t := by linarith
  have hexp : 1 + 2 * t ≤ Real.exp (2 * t) := by
    linarith [Real.add_one_le_exp (2 * t)]
  have hinv1 : Real.exp (-(2 * t)) ≤ (1 + 2 * t)⁻¹ := by
    rw [Real.exp_neg]
    exact (inv_anti₀ h2t hexp)
  have hinv2 : (1 + 2 * t)⁻¹ ≤ 1 - t := by
    have hmul : 1 ≤ (1 - t) * (1 + 2 * t) := by
      have hdiff : (1 - t) * (1 + 2 * t) = 1 + t * (1 - 2 * t) := by ring
      have hnn : 0 ≤ t * (1 - 2 * t) := mul_nonneg ht0 (by linarith)
      linarith
    exact (inv_le_iff_one_le_mul₀' h2t).mpr (by linarith)
  have hle : Real.exp (-(2 * t)) ≤ 1 - t := le_trans hinv1 hinv2
  have hlog : -(2 * t) ≤ Real.log (1 - t) := by
    simpa [Real.log_exp] using Real.log_le_log (Real.exp_pos _) hle
  linarith

omit [DecidableEq P] in
private theorem kpLogWeight_nonneg {z a : P → ℝ} {y : P}
    (hr : |z y| * Real.exp (a y) < 1) :
    0 ≤ kpLogWeight z a y := by
  unfold kpLogWeight
  have hr0 : 0 ≤ |z y| * Real.exp (a y) := mul_nonneg (abs_nonneg _) (Real.exp_pos _).le
  have h1 : 0 < 1 - |z y| * Real.exp (a y) := sub_pos.mpr hr
  have h2 : 1 - |z y| * Real.exp (a y) ≤ 1 := by linarith
  have hlog : Real.log (1 - |z y| * Real.exp (a y)) ≤ 0 := Real.log_nonpos h1.le h2
  linarith

private theorem dobrushin_kp_ind {incomp : P → P → Prop} (hrefl : ∀ u, incomp u u)
    (hsym : ∀ u v, incomp u v → incomp v u) {U : Finset P} {z a : P → ℝ}
    (_ha : ∀ x ∈ U, 0 ≤ a x) (hr : ∀ x ∈ U, |z x| * Real.exp (a x) < 1)
    (hdkp : ∀ x ∈ U, (∑ y ∈ nbhd incomp U x, kpLogWeight z a y) ≤ a x) :
    ∀ n : ℕ, ∀ S : Finset P, S ⊆ U → S.card ≤ n →
      0 < polymerZ incomp z S ∧
      (∀ T : Finset P, T ⊆ S →
        polymerZ incomp z (S \ T) / polymerZ incomp z S ≤
          ∏ y ∈ T, (1 - |z y| * Real.exp (a y))⁻¹) := by
  intro n
  induction n with
  | zero =>
      intro S hSU hcard
      have hSempty : S = ∅ := Finset.card_eq_zero.mp (Nat.le_zero.mp hcard)
      subst hSempty
      refine ⟨by rw [polymerZ_empty]; norm_num, ?_⟩
      intro T hT
      have hTe : T = ∅ := Finset.subset_empty.mp hT
      subst hTe
      simp [polymerZ_empty]
  | succ n ih =>
      have ih_step : ∀ {S' : Finset P}, S' ⊆ U → S'.card ≤ n →
          ∀ x ∈ U, polymerZ incomp z (withoutNbhd incomp S' x) / polymerZ incomp z S' ≤
            Real.exp (a x) := by
        intro S' hS'U hS'card x hxU
        obtain ⟨hpos', hprod'⟩ := ih S' hS'U hS'card
        let T := S' ∩ nbhd incomp U x
        have hTS' : T ⊆ S' := Finset.inter_subset_left
        have heqW : withoutNbhd incomp S' x = S' \ T := withoutNbhd_eq_sdiff_nbhd incomp hS'U x
        have hbd := hprod' T hTS'
        have hexpEq :
            (∏ y ∈ T, (1 - |z y| * Real.exp (a y))⁻¹) =
              Real.exp (∑ y ∈ T, kpLogWeight z a y) := by
          rw [Real.exp_sum]
          refine Finset.prod_congr rfl ?_
          intro y hy
          have hyU : y ∈ U := hS'U (hTS' hy)
          have h1m : 0 < 1 - |z y| * Real.exp (a y) := sub_pos.mpr (hr y hyU)
          unfold kpLogWeight
          rw [Real.exp_neg, Real.exp_log h1m]
        have hsumLe : (∑ y ∈ T, kpLogWeight z a y) ≤
            ∑ y ∈ nbhd incomp U x, kpLogWeight z a y := by
          refine Finset.sum_le_sum_of_subset_of_nonneg Finset.inter_subset_right ?_
          intro y hyN _
          have hyU : y ∈ U := (nbhd_subset incomp U x) hyN
          exact kpLogWeight_nonneg (hr y hyU)
        have hexpLe : Real.exp (∑ y ∈ T, kpLogWeight z a y) ≤ Real.exp (a x) :=
          Real.exp_le_exp.mpr (le_trans hsumLe (hdkp x hxU))
        rw [← heqW] at hbd
        exact le_trans (hbd.trans_eq hexpEq) hexpLe
      have hposStep : ∀ {S : Finset P}, S ⊆ U → S.card ≤ n + 1 →
          0 < polymerZ incomp z S ∧
          ∀ x ∈ S, (1 - |z x| * Real.exp (a x)) * polymerZ incomp z (S.erase x) ≤
            polymerZ incomp z S := by
        intro S hSU hcard
        by_cases hS : S = ∅
        · subst hS
          exact ⟨by rw [polymerZ_empty]; norm_num,
            fun x hx => False.elim (Finset.notMem_empty x hx)⟩
        · have hne : S.Nonempty := Finset.nonempty_iff_ne_empty.mpr hS
          have hlower : ∀ x ∈ S,
              (1 - |z x| * Real.exp (a x)) * polymerZ incomp z (S.erase x) ≤
                polymerZ incomp z S := by
            intro x hxS
            have hxU : x ∈ U := hSU hxS
            let S' := S.erase x
            have hS'U : S' ⊆ U := Finset.Subset.trans (Finset.erase_subset _ _) hSU
            have hS'card : S'.card ≤ n := by
              have hc : S'.card + 1 = S.card := Finset.card_erase_add_one hxS
              omega
            have hposS' : 0 < polymerZ incomp z S' := (ih S' hS'U hS'card).1
            have hnoN_sub_S' : withoutNbhd incomp S x ⊆ S' := withoutNbhd_subset_erase hrefl S x
            have hnoN_card : (withoutNbhd incomp S x).card ≤ n :=
              le_trans (Finset.card_le_card hnoN_sub_S') hS'card
            have hposNoN : 0 < polymerZ incomp z (withoutNbhd incomp S x) :=
              (ih (withoutNbhd incomp S x) (Finset.Subset.trans hnoN_sub_S' hS'U) hnoN_card).1
            have hnoNeq : withoutNbhd incomp S x = withoutNbhd incomp S' x := by
              ext y
              simp only [withoutNbhd, S', Finset.mem_filter, Finset.mem_erase]
              constructor
              · rintro ⟨hyS, hnot⟩
                have hne : y ≠ x := by
                  rintro rfl
                  exact hnot (hrefl y)
                exact ⟨⟨hne, hyS⟩, hnot⟩
              · rintro ⟨⟨_, hyS⟩, hnot⟩
                exact ⟨hyS, hnot⟩
            have hdivLe := ih_step hS'U hS'card x hxU
            rw [← hnoNeq] at hdivLe
            have hZnoN_le :
                polymerZ incomp z (withoutNbhd incomp S x) ≤
                  Real.exp (a x) * polymerZ incomp z S' := by
              rwa [div_le_iff₀ hposS'] at hdivLe
            have habsTerm :
                |z x * polymerZ incomp z (withoutNbhd incomp S x)| ≤
                  |z x| * (Real.exp (a x) * polymerZ incomp z S') := by
              rw [abs_mul, abs_of_pos hposNoN]
              exact mul_le_mul_of_nonneg_left hZnoN_le (abs_nonneg _)
            have hlowTerm :
                -(|z x| * Real.exp (a x) * polymerZ incomp z S') ≤
                  z x * polymerZ incomp z (withoutNbhd incomp S x) := by
              have hlo := (abs_le.mp habsTerm).1
              linarith
            have hdel := polymerZ_eq_erase_add hrefl hsym z hxS
            linarith
          rcases hne with ⟨x0, hx0⟩
          have hS'card : (S.erase x0).card ≤ n := by
            have hc : (S.erase x0).card + 1 = S.card := Finset.card_erase_add_one hx0
            omega
          have hpos' : 0 < polymerZ incomp z (S.erase x0) :=
            (ih (S.erase x0) (Finset.Subset.trans (Finset.erase_subset _ _) hSU) hS'card).1
          have h1m : 0 < 1 - |z x0| * Real.exp (a x0) := sub_pos.mpr (hr x0 (hSU hx0))
          have hposS : 0 < polymerZ incomp z S :=
            lt_of_lt_of_le (mul_pos h1m hpos') (hlower x0 hx0)
          exact ⟨hposS, hlower⟩
      intro S hSU hcard
      obtain ⟨hposS, hlower⟩ := hposStep hSU hcard
      refine ⟨hposS, ?_⟩
      intro T hTS
      by_cases hT : T = ∅
      · subst hT
        simp [div_self (ne_of_gt hposS)]
      · rcases Finset.nonempty_iff_ne_empty.mpr hT with ⟨x, hxT⟩
        have hxS : x ∈ S := hTS hxT
        have hxU : x ∈ U := hSU hxS
        let S' := S.erase x
        let T' := T.erase x
        have hS'U : S' ⊆ U := Finset.Subset.trans (Finset.erase_subset _ _) hSU
        have hS'card : S'.card ≤ n := by
          have hc : S'.card + 1 = S.card := Finset.card_erase_add_one hxS
          omega
        have hT'S' : T' ⊆ S' := Finset.erase_subset_erase x hTS
        have hih' := (ih S' hS'U hS'card).2 T' hT'S'
        have hposS' : 0 < polymerZ incomp z S' := (ih S' hS'U hS'card).1
        have hSTeq : S \ T = S' \ T' := by
          ext y
          by_cases h : y = x <;> simp [S', T', h, hxT]
        have h1m : 0 < 1 - |z x| * Real.exp (a x) := sub_pos.mpr (hr x hxU)
        have hZS'div :
            polymerZ incomp z S' / polymerZ incomp z S ≤ (1 - |z x| * Real.exp (a x))⁻¹ := by
          rw [div_le_iff₀ hposS]
          calc
            polymerZ incomp z S'
                = (1 - |z x| * Real.exp (a x))⁻¹ *
                    ((1 - |z x| * Real.exp (a x)) * polymerZ incomp z S') := by
                  field_simp [ne_of_gt h1m]
            _ ≤ (1 - |z x| * Real.exp (a x))⁻¹ * polymerZ incomp z S :=
                  mul_le_mul_of_nonneg_left (hlower x hxS) (inv_pos.mpr h1m).le
            _ = (1 - |z x| * Real.exp (a x))⁻¹ * polymerZ incomp z S := rfl
        have hZdiffPos : 0 < polymerZ incomp z (S' \ T') :=
          (ih (S' \ T') (Finset.Subset.trans Finset.sdiff_subset hS'U)
            (le_trans (Finset.card_le_card Finset.sdiff_subset) hS'card)).1
        have hprodNonneg : 0 ≤ ∏ y ∈ T', (1 - |z y| * Real.exp (a y))⁻¹ := by
          refine Finset.prod_nonneg ?_
          intro y hy
          have hyU : y ∈ U := hS'U (hT'S' hy)
          exact (inv_pos.mpr (sub_pos.mpr (hr y hyU))).le
        have hfac :
            polymerZ incomp z (S \ T) / polymerZ incomp z S =
              (polymerZ incomp z (S' \ T') / polymerZ incomp z S') *
                (polymerZ incomp z S' / polymerZ incomp z S) := by
          rw [hSTeq]
          field_simp [ne_of_gt hposS', ne_of_gt hposS]
        have hmul :
            polymerZ incomp z (S \ T) / polymerZ incomp z S ≤
              (∏ y ∈ T', (1 - |z y| * Real.exp (a y))⁻¹) *
                (1 - |z x| * Real.exp (a x))⁻¹ := by
          rw [hfac]
          exact mul_le_mul hih' hZS'div (div_pos hposS' hposS).le hprodNonneg
        have hTins : insert x T' = T := Finset.insert_erase hxT
        have hxnot : x ∉ T' := Finset.notMem_erase x T
        rw [← hTins, Finset.prod_insert hxnot]
        simpa [hTins, mul_comm] using hmul

/-- **UNCONDITIONAL (`YM172`):** Under the Dobrushin-Kotecký-Preiss condition on `U`, every
subfamily `S ⊆ U` satisfies `0 < polymerZ S`, multi-site deletion bounds, and uniform pinned ratio
bounds `polymerZ (S \ N[x]) / polymerZ S ≤ exp (a x)`. -/
theorem dobrushin_kp_cluster_bounds {incomp : P → P → Prop} (hrefl : ∀ u, incomp u u)
    (hsym : ∀ u v, incomp u v → incomp v u) {U : Finset P} {z a : P → ℝ}
    (ha : ∀ x ∈ U, 0 ≤ a x) (hr : ∀ x ∈ U, |z x| * Real.exp (a x) < 1)
    (hdkp : ∀ x ∈ U, (∑ y ∈ nbhd incomp U x, kpLogWeight z a y) ≤ a x)
    {S : Finset P} (hSU : S ⊆ U) :
    0 < polymerZ incomp z S ∧
      (∀ T ⊆ S,
        polymerZ incomp z (S \ T) / polymerZ incomp z S ≤
          ∏ y ∈ T, (1 - |z y| * Real.exp (a y))⁻¹) ∧
      (∀ x ∈ U, polymerZ incomp z (withoutNbhd incomp S x) / polymerZ incomp z S ≤
        Real.exp (a x)) := by
  obtain ⟨hpos, hprod⟩ := dobrushin_kp_ind hrefl hsym ha hr hdkp S.card S hSU le_rfl
  refine ⟨hpos, hprod, ?_⟩
  intro x hxU
  let T := S ∩ nbhd incomp U x
  have hTS : T ⊆ S := Finset.inter_subset_left
  have heqW := withoutNbhd_eq_sdiff_nbhd incomp hSU x
  have hbd := hprod T hTS
  have hexpEq :
      (∏ y ∈ T, (1 - |z y| * Real.exp (a y))⁻¹) =
        Real.exp (∑ y ∈ T, kpLogWeight z a y) := by
    rw [Real.exp_sum]
    refine Finset.prod_congr rfl ?_
    intro y hy
    have hyU : y ∈ U := hSU (hTS hy)
    have h1m : 0 < 1 - |z y| * Real.exp (a y) := sub_pos.mpr (hr y hyU)
    unfold kpLogWeight
    rw [Real.exp_neg, Real.exp_log h1m]
  have hsumLe : (∑ y ∈ T, kpLogWeight z a y) ≤ ∑ y ∈ nbhd incomp U x, kpLogWeight z a y := by
    refine Finset.sum_le_sum_of_subset_of_nonneg Finset.inter_subset_right ?_
    intro y hyN _
    have hyU : y ∈ U := (nbhd_subset incomp U x) hyN
    exact kpLogWeight_nonneg (hr y hyU)
  rw [← heqW] at hbd
  exact le_trans (hbd.trans_eq hexpEq) (Real.exp_le_exp.mpr (le_trans hsumLe (hdkp x hxU)))

omit [DecidableEq P] in
/-- Classical Kotecký-Preiss `1/2` criterion unconditionally implies Dobrushin-Kotecký-Preiss. -/
theorem kotecky_preiss_half_condition_implies_dkp (incomp : P → P → Prop) {U : Finset P}
    {z a : P → ℝ} (hrHalf : ∀ x ∈ U, |z x| * Real.exp (a x) ≤ 1 / 2)
    (hkp : ∀ x ∈ U, (∑ y ∈ nbhd incomp U x, |z y| * Real.exp (a y)) ≤ a x / 2) :
    (∀ x ∈ U, |z x| * Real.exp (a x) < 1) ∧
      (∀ x ∈ U, (∑ y ∈ nbhd incomp U x, kpLogWeight z a y) ≤ a x) := by
  refine ⟨fun x hx => lt_of_le_of_lt (hrHalf x hx) (by norm_num), ?_⟩
  intro x hxU
  have hsum1 :
      (∑ y ∈ nbhd incomp U x, kpLogWeight z a y) ≤
        ∑ y ∈ nbhd incomp U x, 2 * (|z y| * Real.exp (a y)) := by
    refine Finset.sum_le_sum ?_
    intro y hyN
    have hyU : y ∈ U := (nbhd_subset incomp U x) hyN
    have hr0 : 0 ≤ |z y| * Real.exp (a y) := mul_nonneg (abs_nonneg _) (Real.exp_pos _).le
    exact neg_log_one_sub_le_two_mul hr0 (hrHalf y hyU)
  rw [← Finset.mul_sum] at hsum1
  linarith [hkp x hxU]

/-- Single-polymer deletion bound on `log Z(S)`:
`|log Z(S) - log Z(S.erase x)| ≤ -log (1 - |z x| * exp (a x))`. -/
theorem polymerZ_log_erase_sub_le {incomp : P → P → Prop} (hrefl : ∀ u, incomp u u)
    (hsym : ∀ u v, incomp u v → incomp v u) {U : Finset P} {z a : P → ℝ}
    (ha : ∀ x ∈ U, 0 ≤ a x) (hr : ∀ x ∈ U, |z x| * Real.exp (a x) < 1)
    (hdkp : ∀ x ∈ U, (∑ y ∈ nbhd incomp U x, kpLogWeight z a y) ≤ a x)
    {S : Finset P} (hSU : S ⊆ U) {x : P} (hxS : x ∈ S) :
    |Real.log (polymerZ incomp z S) - Real.log (polymerZ incomp z (S.erase x))| ≤
      kpLogWeight z a x := by
  have hxU : x ∈ U := hSU hxS
  let S' := S.erase x
  have hS'U : S' ⊆ U := Finset.Subset.trans (Finset.erase_subset _ _) hSU
  have hnoNS : withoutNbhd incomp S x ⊆ S' := withoutNbhd_subset_erase hrefl S x
  have hnoNU : withoutNbhd incomp S x ⊆ U := Finset.Subset.trans hnoNS hS'U
  have hnoNeq : withoutNbhd incomp S x = withoutNbhd incomp S' x := by
    ext y
    simp only [withoutNbhd, S', Finset.mem_filter, Finset.mem_erase]
    constructor
    · rintro ⟨hyS, hnot⟩
      have hne : y ≠ x := fun hyx => hnot (hyx ▸ hrefl x)
      exact ⟨⟨hne, hyS⟩, hnot⟩
    · rintro ⟨⟨_, hyS⟩, hnot⟩
      exact ⟨hyS, hnot⟩
  have hZposS : 0 < polymerZ incomp z S :=
    (dobrushin_kp_cluster_bounds hrefl hsym ha hr hdkp hSU).1
  have hboundsS' := dobrushin_kp_cluster_bounds hrefl hsym ha hr hdkp hS'U
  have hZposS' : 0 < polymerZ incomp z S' := hboundsS'.1
  have hZposNoN : 0 < polymerZ incomp z (withoutNbhd incomp S x) :=
    (dobrushin_kp_cluster_bounds hrefl hsym ha hr hdkp hnoNU).1
  have hratio := hboundsS'.2.2 x hxU
  rw [← hnoNeq] at hratio
  have hZnoN_le :
      polymerZ incomp z (withoutNbhd incomp S x) ≤ Real.exp (a x) * polymerZ incomp z S' := by
    rwa [div_le_iff₀ hZposS'] at hratio
  have hdel := polymerZ_eq_erase_add hrefl hsym z hxS
  let rx := |z x| * Real.exp (a x)
  have hrx0 : 0 ≤ rx := mul_nonneg (abs_nonneg _) (Real.exp_pos _).le
  have hrx1 : rx < 1 := hr x hxU
  have habsDiff :
      |z x * polymerZ incomp z (withoutNbhd incomp S x)| ≤ rx * polymerZ incomp z S' := by
    rw [abs_mul, abs_of_pos hZposNoN]
    have hmul := mul_le_mul_of_nonneg_left hZnoN_le (abs_nonneg (z x))
    dsimp [rx]
    linarith
  have hband := abs_le.mp habsDiff
  have hSlo : (1 - rx) * polymerZ incomp z S' ≤ polymerZ incomp z S := by linarith [hband.1]
  have hShi : polymerZ incomp z S ≤ (1 + rx) * polymerZ incomp z S' := by linarith [hband.2]
  have hdivLo : 1 - rx ≤ polymerZ incomp z S / polymerZ incomp z S' := by
    rwa [le_div_iff₀ hZposS']
  have hdivHi : polymerZ incomp z S / polymerZ incomp z S' ≤ 1 + rx := by
    rwa [div_le_iff₀ hZposS']
  have hlogEq :
      Real.log (polymerZ incomp z S) - Real.log (polymerZ incomp z S') =
        Real.log (polymerZ incomp z S / polymerZ incomp z S') :=
    (Real.log_div (ne_of_gt hZposS) (ne_of_gt hZposS')).symm
  have h1m : 0 < 1 - rx := sub_pos.mpr hrx1
  have hlogLo : Real.log (1 - rx) ≤ Real.log (polymerZ incomp z S / polymerZ incomp z S') :=
    Real.log_le_log h1m hdivLo
  have hlogHi : Real.log (polymerZ incomp z S / polymerZ incomp z S') ≤ Real.log (1 + rx) :=
    Real.log_le_log (div_pos hZposS hZposS') hdivHi
  have hlogWrap := log_one_add_le_neg_log_one_sub hrx0 hrx1
  rw [hlogEq]
  unfold kpLogWeight
  exact abs_le.mpr ⟨by linarith, by linarith⟩

/-- **`L`-uniform polymer collar decoupling (`YM172`):** For pairwise disjoint `S₁, S₂, B` in `U`
with `S₁` compatible with `S₂`, `|log Z(S₁ ∪ S₂ ∪ B) - (log Z(S₁) + log Z(S₂))|` is bounded
exclusively by the boundary collar weights `∑ y ∈ B, kpLogWeight z a y` independent of `S₂`. -/
theorem polymerZ_collar_decoupling_le {incomp : P → P → Prop} (hrefl : ∀ u, incomp u u)
    (hsym : ∀ u v, incomp u v → incomp v u) {U : Finset P} {z a : P → ℝ}
    (ha : ∀ x ∈ U, 0 ≤ a x) (hr : ∀ x ∈ U, |z x| * Real.exp (a x) < 1)
    (hdkp : ∀ x ∈ U, (∑ y ∈ nbhd incomp U x, kpLogWeight z a y) ≤ a x)
    {S₁ S₂ B : Finset P} (h12 : Disjoint S₁ S₂) (h1B : Disjoint S₁ B) (h2B : Disjoint S₂ B)
    (hcompat : ∀ u ∈ S₁, ∀ v ∈ S₂, ¬ incomp u v) (hsub : S₁ ∪ S₂ ∪ B ⊆ U) :
    |Real.log (polymerZ incomp z (S₁ ∪ S₂ ∪ B)) -
        (Real.log (polymerZ incomp z S₁) + Real.log (polymerZ incomp z S₂))| ≤
      ∑ y ∈ B, kpLogWeight z a y := by
  induction B using Finset.induction with
  | empty =>
      simp only [Finset.union_empty, Finset.sum_empty]
      have hsub1 : S₁ ⊆ U := Finset.Subset.trans Finset.subset_union_left
        (Finset.Subset.trans Finset.subset_union_left hsub)
      have hsub2 : S₂ ⊆ U := Finset.Subset.trans Finset.subset_union_right
        (Finset.Subset.trans Finset.subset_union_left hsub)
      have hpos1 : 0 < polymerZ incomp z S₁ :=
        (dobrushin_kp_cluster_bounds hrefl hsym ha hr hdkp hsub1).1
      have hpos2 : 0 < polymerZ incomp z S₂ :=
        (dobrushin_kp_cluster_bounds hrefl hsym ha hr hdkp hsub2).1
      rw [polymerZ_union_of_compat hsym z h12 hcompat,
        Real.log_mul (ne_of_gt hpos1) (ne_of_gt hpos2)]
      simp
  | @insert b B' hb ih =>
      have h1B' : Disjoint S₁ B' := Finset.disjoint_of_subset_right (Finset.subset_insert b B') h1B
      have h2B' : Disjoint S₂ B' := Finset.disjoint_of_subset_right (Finset.subset_insert b B') h2B
      have hsub' : S₁ ∪ S₂ ∪ B' ⊆ U :=
        Finset.Subset.trans (Finset.union_subset Finset.subset_union_left
          (Finset.Subset.trans (Finset.subset_insert b B') Finset.subset_union_right)) hsub
      have hih := ih h1B' h2B' hsub'
      have hbnot1 : b ∉ S₁ :=
        Finset.disjoint_right.mp h1B (Finset.mem_insert_self b B')
      have hbnot2 : b ∉ S₂ :=
        Finset.disjoint_right.mp h2B (Finset.mem_insert_self b B')
      have hbnot12 : b ∉ S₁ ∪ S₂ ∪ B' := by
        simp [hbnot1, hbnot2, hb]
      have hinsEq : S₁ ∪ S₂ ∪ insert b B' = insert b (S₁ ∪ S₂ ∪ B') := by
        ext y
        simp [Finset.mem_union, Finset.mem_insert]
      have herase : (insert b (S₁ ∪ S₂ ∪ B')).erase b = S₁ ∪ S₂ ∪ B' :=
        Finset.erase_insert hbnot12
      have hstep := polymerZ_log_erase_sub_le hrefl hsym ha hr hdkp (S := S₁ ∪ S₂ ∪ insert b B')
        hsub (x := b) (by rw [hinsEq]; exact Finset.mem_insert_self _ _)
      rw [hinsEq, herase] at hstep
      rw [Finset.sum_insert hb, hinsEq]
      have htri :
          |Real.log (polymerZ incomp z (insert b (S₁ ∪ S₂ ∪ B'))) -
              (Real.log (polymerZ incomp z S₁) + Real.log (polymerZ incomp z S₂))| ≤
            |Real.log (polymerZ incomp z (insert b (S₁ ∪ S₂ ∪ B'))) -
                Real.log (polymerZ incomp z (S₁ ∪ S₂ ∪ B'))| +
              |Real.log (polymerZ incomp z (S₁ ∪ S₂ ∪ B')) -
                (Real.log (polymerZ incomp z S₁) + Real.log (polymerZ incomp z S₂))| := by
        have hsubAdd :
            Real.log (polymerZ incomp z (insert b (S₁ ∪ S₂ ∪ B'))) -
                (Real.log (polymerZ incomp z S₁) + Real.log (polymerZ incomp z S₂)) =
              (Real.log (polymerZ incomp z (insert b (S₁ ∪ S₂ ∪ B'))) -
                  Real.log (polymerZ incomp z (S₁ ∪ S₂ ∪ B'))) +
                (Real.log (polymerZ incomp z (S₁ ∪ S₂ ∪ B')) -
                  (Real.log (polymerZ incomp z S₁) + Real.log (polymerZ incomp z S₂))) := by
          ring
        rw [hsubAdd]
        exact abs_add_le _ _
      linarith

end ClusterConvergence

end AbstractPolymerCluster
