/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
module

public import Mathlib.Analysis.InnerProductSpace.PiL2
public import Mathlib.Analysis.Real.Sqrt
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import YangMillsBlueprint.MathlibStaging.ConcreteHodgeInvolution

/-!
# 4D Lorentzian Hodge Complex Structure (`J_L^2 = -id`) and Poynting Light-Cone Causality

Contrasts the Euclidean 4D Hodge involution `hodge4D` (`J_E^2 = +id`, `YM159`) with the concrete
Lorentzian 4D Hodge operator `lorentzHodge4D` (`J_L (E, B) = (-B, E)`) on `Fin 6`:

* `lorentzHodge4D_sq`: `lorentzHodge4D (lorentzHodge4D x) = -x` (`J_L^2 = -id`).
* `lorentzHodge4D_skew` and `lorentzHodge4D_inner_self`: skew-symmetry and `⟪x, J_L x⟫ = 0`.
* `lorentzHodge4D_norm`: isometry `‖lorentzHodge4D x‖ = ‖x‖`.
* `energy_poynting_hyperboloid_eq`, `poynting_norm_le_energy`, `poynting_null_iff`: exact
  Yang-Mills Poynting causality bound `‖E × B‖ ≤ (‖E‖² + ‖B‖²) / 2` with null-cone saturation
  iff `‖E‖² = ‖B‖²` and `E · B = 0`.
-/

@[expose] public section

namespace LorentzianHodgeAndEnergy

open ConcreteHodgeInvolution

section LorentzianHodge

/-- Concrete 4D Lorentzian Hodge dual `J_L (E, B) = (-B, E)` on `EuclideanSpace ℝ (Fin 6)`. -/
def lorentzHodge4D :
    EuclideanSpace ℝ (Fin 6) →ₗ[ℝ] EuclideanSpace ℝ (Fin 6) where
  toFun x := WithLp.toLp 2 fun i : Fin 6 =>
    if h : (i : ℕ) < 3 then -x ⟨(i : ℕ) + 3, by omega⟩ else x ⟨(i : ℕ) - 3, by omega⟩
  map_add' x y := by
    ext i
    by_cases h : (i : ℕ) < 3
    · simp [h]
      ring
    · simp [h]
  map_smul' c x := by
    ext i
    by_cases h : (i : ℕ) < 3 <;> simp [h]

@[simp]
theorem lorentzHodge4D_apply_lt (x : EuclideanSpace ℝ (Fin 6)) {i : Fin 6}
    (h : (i : ℕ) < 3) :
    lorentzHodge4D x i = -x ⟨(i : ℕ) + 3, by omega⟩ := by
  simp [lorentzHodge4D, h]

@[simp]
theorem lorentzHodge4D_apply_ge (x : EuclideanSpace ℝ (Fin 6)) {i : Fin 6}
    (h : ¬ ((i : ℕ) < 3)) :
    lorentzHodge4D x i = x ⟨(i : ℕ) - 3, by omega⟩ := by
  simp [lorentzHodge4D, h]

/-- Unconditional complex-structure identity `J_L^2 = -id` in Lorentzian 4D signature. -/
theorem lorentzHodge4D_sq (x : EuclideanSpace ℝ (Fin 6)) :
    lorentzHodge4D (lorentzHodge4D x) = -x := by
  ext i
  fin_cases i <;> simp [lorentzHodge4D]

/-- Skew-symmetry of `lorentzHodge4D`: `⟪J_L x, y⟫ = -⟪x, J_L y⟫`. -/
theorem lorentzHodge4D_skew (x y : EuclideanSpace ℝ (Fin 6)) :
    inner ℝ (lorentzHodge4D x) y = -inner ℝ x (lorentzHodge4D y) := by
  simp only [EuclideanSpace.inner_eq_star_dotProduct, dotProduct, star_trivial, Fin.sum_univ_six,
    lorentzHodge4D]
  norm_num
  ring

/-- Orthogonality of dual field: `⟪x, J_L x⟫ = 0` identically on `EuclideanSpace ℝ (Fin 6)`. -/
theorem lorentzHodge4D_inner_self (x : EuclideanSpace ℝ (Fin 6)) :
    inner ℝ x (lorentzHodge4D x) = 0 := by
  have h := lorentzHodge4D_skew x x
  rw [real_inner_comm] at h
  linarith

/-- Squared-norm preservation under `lorentzHodge4D`. -/
theorem lorentzHodge4D_norm_sq (x : EuclideanSpace ℝ (Fin 6)) :
    ‖lorentzHodge4D x‖ ^ 2 = ‖x‖ ^ 2 := by
  rw [← real_inner_self_eq_norm_sq, ← real_inner_self_eq_norm_sq, lorentzHodge4D_skew,
    lorentzHodge4D_sq, inner_neg_right, neg_neg]

/-- Exact isometry `‖J_L x‖ = ‖x‖`. -/
theorem lorentzHodge4D_norm (x : EuclideanSpace ℝ (Fin 6)) :
    ‖lorentzHodge4D x‖ = ‖x‖ := by
  have hsq : ‖lorentzHodge4D x‖ ^ 2 = ‖x‖ ^ 2 := lorentzHodge4D_norm_sq x
  exact (sq_eq_sq₀ (norm_nonneg _) (norm_nonneg _)).mp hsq

/-- Signature contrast theorem: `hodge4D^2 = +id` (Euclidean `SymmInvolution`) vs
`lorentzHodge4D^2 = -id` (Lorentzian complex structure), both norm-preserving. -/
theorem euclidean_vs_lorentzian_hodge_contrast (x : EuclideanSpace ℝ (Fin 6)) :
    hodge4D (hodge4D x) = x ∧
      lorentzHodge4D (lorentzHodge4D x) = -x ∧
      ‖hodge4D x‖ = ‖x‖ ∧
      ‖lorentzHodge4D x‖ = ‖x‖ := by
  have heuc := symmInvolution_hodge4D.invol x
  have heucNorm : ‖hodge4D x‖ ^ 2 = ‖x‖ ^ 2 := by
    rw [← real_inner_self_eq_norm_sq, ← real_inner_self_eq_norm_sq,
      symmInvolution_hodge4D.symm x (hodge4D x), heuc]
  have heucN : ‖hodge4D x‖ = ‖x‖ :=
    (sq_eq_sq₀ (norm_nonneg _) (norm_nonneg _)).mp heucNorm
  exact ⟨heuc, lorentzHodge4D_sq x, heucN, lorentzHodge4D_norm x⟩

end LorentzianHodge

section PoyntingCausality

/-- Euclidean squared norm of a 3-vector `v : Fin 3 → ℝ`. -/
def normSq3 (v : Fin 3 → ℝ) : ℝ :=
  v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2

/-- Euclidean inner product of two 3-vectors `u, v : Fin 3 → ℝ`. -/
def dot3 (u v : Fin 3 → ℝ) : ℝ :=
  u 0 * v 0 + u 1 * v 1 + u 2 * v 2

/-- 3D cross product `E × B` representing the Poynting momentum flux vector. -/
def cross3 (E B : Fin 3 → ℝ) : Fin 3 → ℝ :=
  ![E 1 * B 2 - E 2 * B 1, E 2 * B 0 - E 0 * B 2, E 0 * B 1 - E 1 * B 0]

/-- Yang-Mills Hamiltonian energy density `(‖E‖² + ‖B‖²) / 2`. -/
noncomputable def energyDensity (E B : Fin 3 → ℝ) : ℝ :=
  (normSq3 E + normSq3 B) / 2

/-- Yang-Mills Lorentzian Lagrangian density `(‖E‖² - ‖B‖²) / 2`. -/
noncomputable def lagrangianDensity (E B : Fin 3 → ℝ) : ℝ :=
  (normSq3 E - normSq3 B) / 2

/-- Squared Poynting energy-flux magnitude `‖E × B‖²`. -/
def poyntingSq (E B : Fin 3 → ℝ) : ℝ :=
  normSq3 (cross3 E B)

/-- Lagrange's 3D cross-product identity `‖E × B‖² + (E · B)² = ‖E‖² ‖B‖²`. -/
theorem lagrange_cross3_identity (E B : Fin 3 → ℝ) :
    poyntingSq E B + dot3 E B ^ 2 = normSq3 E * normSq3 B := by
  unfold poyntingSq normSq3 dot3 cross3
  norm_num
  ring

/-- Exact Lorentzian energy-momentum hyperboloid identity:
`H² - ‖S‖² = L² + (E · B)²`. -/
theorem energy_poynting_hyperboloid_eq (E B : Fin 3 → ℝ) :
    energyDensity E B ^ 2 - poyntingSq E B =
      lagrangianDensity E B ^ 2 + dot3 E B ^ 2 := by
  unfold energyDensity poyntingSq lagrangianDensity normSq3 dot3 cross3
  norm_num
  ring

/-- Positivity of Hamiltonian energy density `0 ≤ (‖E‖² + ‖B‖²) / 2`. -/
theorem energyDensity_nonneg (E B : Fin 3 → ℝ) : 0 ≤ energyDensity E B := by
  unfold energyDensity normSq3
  positivity

/-- Poynting causality squared inequality `‖E × B‖² ≤ H²`. -/
theorem poynting_le_energy_sq (E B : Fin 3 → ℝ) :
    poyntingSq E B ≤ energyDensity E B ^ 2 := by
  have hid := energy_poynting_hyperboloid_eq E B
  have hnonneg : 0 ≤ lagrangianDensity E B ^ 2 + dot3 E B ^ 2 := by positivity
  linarith

/-- Poynting light-cone causality bound `‖E × B‖ ≤ H` (energy transport never exceeds `c = 1`). -/
theorem poynting_norm_le_energy (E B : Fin 3 → ℝ) :
    Real.sqrt (poyntingSq E B) ≤ energyDensity E B :=
  Real.sqrt_le_iff.mpr ⟨energyDensity_nonneg E B, poynting_le_energy_sq E B⟩

/-- Null-cone saturation characterization: energy flux reaches `c = 1` iff `‖E‖² = ‖B‖²` and
`E · B = 0` (exact Lorentz-invariant null electromagnetic / radiation configuration). -/
theorem poynting_null_iff (E B : Fin 3 → ℝ) :
    poyntingSq E B = energyDensity E B ^ 2 ↔
      normSq3 E = normSq3 B ∧ dot3 E B = 0 := by
  have hid := energy_poynting_hyperboloid_eq E B
  constructor
  · intro heq
    have hsum : lagrangianDensity E B ^ 2 + dot3 E B ^ 2 = 0 := by linarith
    have hL2 : lagrangianDensity E B ^ 2 ≤ 0 := by
      nlinarith [sq_nonneg (dot3 E B)]
    have hD2 : dot3 E B ^ 2 ≤ 0 := by
      nlinarith [sq_nonneg (lagrangianDensity E B)]
    have hL : lagrangianDensity E B = 0 := sq_eq_zero_iff.mp (le_antisymm hL2 (sq_nonneg _))
    have hD : dot3 E B = 0 := sq_eq_zero_iff.mp (le_antisymm hD2 (sq_nonneg _))
    unfold lagrangianDensity at hL
    exact ⟨by linarith, hD⟩
  · rintro ⟨hnorm, hdot⟩
    have hL : lagrangianDensity E B = 0 := by
      unfold lagrangianDensity
      linarith
    rw [hL, hdot] at hid
    linarith

end PoyntingCausality

end LorentzianHodgeAndEnergy
