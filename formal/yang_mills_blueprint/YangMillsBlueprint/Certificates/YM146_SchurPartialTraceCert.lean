/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import YangMillsBlueprint.MathlibStaging.SchurPartialTraceContraction
import Mathlib.Data.Rat.Init
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# YM-146: Half-Observation Schur Partial-Trace Contraction Certificate

Instantiates `SchurPartialTraceContraction` over `ℚ`:
- Starting at single-step neighbor coupling `r = 1 / 2` (inside the golden-ratio contraction
  window `r^2 + r = 3/4 < 1` and stability threshold `2 * r^2 = 1/2 < 1`), eliminating one
  unobserved intermediate slice contracts boundary coupling strictly to
  `schurPrecisionCoupling (1 / 2) = 1 / 3 < 1 / 2`.
- Iterating one further Schur elimination step drops coupling to `1 / 8 < 1 / 3`.
- Conditional theorem `schur_partial_trace_contraction_conditional` proving strict induced
  contraction and stability margin inside the golden-ratio / `2 * r^2 < 1` domain.
-/

namespace YangMillsBlueprint.Certificates

open SchurPartialTraceContraction

/-- Rational certificate bundling half-observation Schur elimination bounds. -/
structure SchurPartialTraceCert where
  r : ℚ
  hr0 : 0 < r
  hgr : r ^ 2 + r < 1
  hstab : 2 * r ^ 2 < 1

/-- Canonical rational witness (`r = 1 / 2`, `schurPrecisionCoupling (1 / 2) = 1 / 3`). -/
def canonicalSchurPartialTraceCert : SchurPartialTraceCert where
  r := 1 / 2
  hr0 := by norm_num
  hgr := by norm_num
  hstab := by norm_num

instance : Nonempty SchurPartialTraceCert :=
  ⟨canonicalSchurPartialTraceCert⟩

/-- One-step Schur elimination evaluation: `schurPrecisionCoupling (1 / 2) = 1 / 3`. -/
theorem canonical_schur_one_step_eq :
    schurPrecisionCoupling canonicalSchurPartialTraceCert.r = 1 / 3 := by
  dsimp [canonicalSchurPartialTraceCert, schurPrecisionCoupling]
  norm_num

/-- Two-step Schur elimination evaluation:
`schurPrecisionCoupling (schurPrecisionCoupling (1 / 2)) = 1 / 8`. -/
theorem canonical_schur_two_step_eq :
    schurPrecisionCoupling (schurPrecisionCoupling canonicalSchurPartialTraceCert.r) = 1 / 8 := by
  rw [canonical_schur_one_step_eq]
  unfold schurPrecisionCoupling
  norm_num

/-- Strict contraction `1 / 8 < 1 / 3 < 1 / 2` across two partial-trace iterations. -/
theorem canonical_schur_monotone_lt :
    schurPrecisionCoupling (schurPrecisionCoupling canonicalSchurPartialTraceCert.r) <
      schurPrecisionCoupling canonicalSchurPartialTraceCert.r ∧
    schurPrecisionCoupling canonicalSchurPartialTraceCert.r < canonicalSchurPartialTraceCert.r := by
  rw [canonical_schur_two_step_eq, canonical_schur_one_step_eq]
  dsimp [canonicalSchurPartialTraceCert]
  norm_num

/-- **CONDITIONAL:** Once coarse blocking places one-step inter-slice coupling inside the
golden-ratio stability domain (`0 < c.r`, `c.r ^ 2 + c.r < 1`, `2 * c.r ^ 2 < 1`), Schur
partial-trace elimination strictly contracts the induced boundary coupling (`r_eff < c.r`)
while keeping stability gap `0 < 1 - r_eff`. -/
theorem schur_partial_trace_contraction_conditional (c : SchurPartialTraceCert) :
    0 < schurPrecisionCoupling c.r ∧
      schurPrecisionCoupling c.r < c.r ∧
      0 < 1 - schurPrecisionCoupling c.r := by
  have hr1 : c.r ^ 2 < 1 := by
    have hsq : 0 ≤ c.r ^ 2 := sq_nonneg c.r
    linarith [c.hstab]
  exact ⟨schurPrecisionCoupling_pos (ne_of_gt c.hr0) hr1,
    schurPrecisionCoupling_lt c.hr0 c.hgr,
    one_sub_schurPrecisionCoupling_pos c.hstab⟩

end YangMillsBlueprint.Certificates
