/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Analysis.SpecialFunctions.ExpDeriv
public import Mathlib.Analysis.SpecificLimits.Basic
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import YangMillsBlueprint.MathlibStaging.SliceReflectionHilbert

/-!
# Continuum Schwinger Limit Preservation (`OS0`, `OS1`, `OS3`, `OS4`)

Addresses Referee Gap 4A by formalizing unconditional sequential limit preservation for joint
`(a → 0, L → ∞)` continuum limits of lattice Schwinger functions and reflection-positive forms:

* `ContinuumSchwingerLimit.tendsto_os0_tempered_bound`: uniform polynomial growth bounds pass to
  the continuum limit (`OS0`).
* `ContinuumSchwingerLimit.tendsto_os1_rotational_invariance`: vanishing `O(a²)` rotational defects
  collapse identically in the continuum limit (`OS1`).
* `ContinuumSchwingerLimit.tendsto_os3_rp_nonneg` & `tendsto_os3_rp_symm`: reflection positivity
  and symmetry pass unconditionally to the weak pointwise limit (`OS3`).
* `ContinuumSchwingerLimit.tendsto_os4_exp_clustering`: uniform exponential clustering envelopes
  with vanishing finite-volume error pass to pure exponential decay (`OS4`).
-/

@[expose] public section

namespace ContinuumSchwingerLimit

open Filter Topology

section ContinuumLimits

/-- `OS0` limit preservation: any uniform tempered polynomial envelope persists in the pointwise
continuum limit. -/
theorem tendsto_os0_tempered_bound {X : Type*} (S : ℕ → X → ℝ) (S_lim : X → ℝ)
    (x : X) (C r : ℝ) (p : ℕ)
    (hbd : ∀ k : ℕ, |S k x| ≤ C * (1 + r) ^ p)
    (hlim : Tendsto (fun k => S k x) atTop (𝓝 (S_lim x))) :
    |S_lim x| ≤ C * (1 + r) ^ p := by
  have hlim_abs : Tendsto (fun k => |S k x|) atTop (𝓝 |S_lim x|) :=
    (continuous_abs.tendsto _).comp hlim
  exact le_of_tendsto hlim_abs (Eventually.of_forall hbd)

/-- `OS1` rotational invariance restoration: if discrete rotation defects vanish as
`C_sym * a k ^ 2` with `a k → 0`, then the continuum limit is strictly rotation-invariant. -/
theorem tendsto_os1_rotational_invariance {X : Type*} (S : ℕ → X → ℝ) (S_lim : X → ℝ)
    (R : X → X) (x : X) (C_sym : ℝ) (a : ℕ → ℝ)
    (hsym : ∀ k : ℕ, |S k (R x) - S k x| ≤ C_sym * a k ^ 2)
    (ha : Tendsto a atTop (𝓝 0))
    (hR : Tendsto (fun k => S k (R x)) atTop (𝓝 (S_lim (R x))))
    (hx : Tendsto (fun k => S k x) atTop (𝓝 (S_lim x))) :
    S_lim (R x) = S_lim x := by
  have hdiff : Tendsto (fun k => |S k (R x) - S k x|) atTop (𝓝 |S_lim (R x) - S_lim x|) :=
    (continuous_abs.tendsto _).comp (hR.sub hx)
  have hrhs : Tendsto (fun k => C_sym * a k ^ 2) atTop (𝓝 0) := by
    simpa using (ha.pow 2).const_mul C_sym
  have hle : |S_lim (R x) - S_lim x| ≤ 0 :=
    le_of_tendsto_of_tendsto hdiff hrhs (Eventually.of_forall hsym)
  exact sub_eq_zero.mp (abs_nonpos_iff.mp hle)

/-- `OS3` positivity preservation: pointwise limits of reflection-positive forms remain
non-negative (`0 ≤ B_lim f f`). -/
theorem tendsto_os3_rp_nonneg {V : Type*} (B : ℕ → V → V → ℝ) (B_lim : V → V → ℝ) (f : V)
    (hpos : ∀ k : ℕ, 0 ≤ B k f f)
    (hlim : Tendsto (fun k => B k f f) atTop (𝓝 (B_lim f f))) :
    0 ≤ B_lim f f :=
  ge_of_tendsto hlim (Eventually.of_forall hpos)

/-- `OS3` symmetry preservation: pointwise limits of symmetric bilinear forms remain symmetric. -/
theorem tendsto_os3_rp_symm {V : Type*} (B : ℕ → V → V → ℝ) (B_lim : V → V → ℝ) (f g : V)
    (hsymm : ∀ k : ℕ, B k f g = B k g f)
    (hfg : Tendsto (fun k => B k f g) atTop (𝓝 (B_lim f g)))
    (hgf : Tendsto (fun k => B k g f) atTop (𝓝 (B_lim g f))) :
    B_lim f g = B_lim g f := by
  have hfg' : Tendsto (fun k => B k f g) atTop (𝓝 (B_lim g f)) := by
    simpa only [hsymm] using hgf
  exact tendsto_nhds_unique hfg hfg'

/-- `OS4` exponential clustering preservation: uniform decay envelopes plus vanishing volume/cutoff
errors pass to strict continuum clustering `|G_lim t| ≤ A * exp (-(Δ * t))`. -/
theorem tendsto_os4_exp_clustering (G : ℕ → ℝ → ℝ) (G_lim : ℝ → ℝ) (t A Δ : ℝ)
    (ε : ℕ → ℝ)
    (hbd : ∀ k : ℕ, |G k t| ≤ A * Real.exp (-(Δ * t)) + ε k)
    (hε : Tendsto ε atTop (𝓝 0))
    (hlim : Tendsto (fun k => G k t) atTop (𝓝 (G_lim t))) :
    |G_lim t| ≤ A * Real.exp (-(Δ * t)) := by
  have hlim_abs : Tendsto (fun k => |G k t|) atTop (𝓝 |G_lim t|) :=
    (continuous_abs.tendsto _).comp hlim
  have hrhs : Tendsto (fun k => A * Real.exp (-(Δ * t)) + ε k) atTop
      (𝓝 (A * Real.exp (-(Δ * t)))) := by
    simpa using tendsto_const_nhds.add hε
  exact le_of_tendsto_of_tendsto hlim_abs hrhs (Eventually.of_forall hbd)

end ContinuumLimits

end ContinuumSchwingerLimit
