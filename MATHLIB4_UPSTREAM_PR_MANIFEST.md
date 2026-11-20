# MATHLIB4 UPSTREAM PR MANIFEST

**Status:** `LOCAL_ONLY_ARCHIVED` — No upstream `leanprover-community/mathlib4` PRs or community Zulip announcements; all standalone modules are kept strictly in `Qamarbajwa/yang-mills-lean4` under `formal/yang_mills_blueprint/YangMillsBlueprint/`.

This manifest isolates the self-contained, general-purpose algebraic and rational arithmetic formalizations developed in this project that are suitable for direct contribution to Mathlib 4.

All project-internal bridge specifications (`MissingBridgeInterfaces.lean`), multi-scale renormalization group wrappers (`YM101Closure.lean`, `BlockWeylCollar.lean`), and heuristic physics files are **STRICTLY EXCLUDED** from upstream submission.

---

## 1. Candidate Modules Summary

| Module | Proposed Mathlib Destination | Lines | Axioms | Subject Matter |
| :--- | :--- | :---: | :---: | :--- |
| **Module 1** | `Mathlib.LinearAlgebra.Matrix.SchurComplement` | 188 | `[propext, Quot.sound]` | $2 \times 2$ block Schur complement quadratic completion identity and coercivity. |
| **Module 2** | `Mathlib.Analysis.Calculus.Polynomial` | 100 | `[propext, Quot.sound]` | Discrete 2-point zero-sum Poincaré identity & rational cubic polynomial bounds. |
| **Module 3** | `Mathlib.Algebra.Quaternion` | 82 | `[propext, Classical.choice, Quot.sound]` | Integer quaternion $(\mathbf{i}, \mathbf{j})$ centralizer triviality & adjoint spectral gap. |

---

## 2. Detailed Module Specifications

### Module 1: `MathlibPR_SchurComplementForms.lean`
- **Source Path:** `formal/yang_mills_blueprint/YangMillsBlueprint/MathlibPR_SchurComplementForms.lean`
- **Target Mathlib Location:** `Mathlib/LinearAlgebra/Matrix/SchurComplement.lean`
- **Mathematical Description:**
  Provides the exact algebraic completion of the square for general $2 \times 2$ block quadratic forms:
  $$\delta \cdot z_c^2 + (a_{bb} z_b - a_{cb} z_c)^2 = a_{bb} \cdot Q(z_b, z_c)$$
  where $\delta = a_{cc} a_{bb} - a_{cb}^2$ is the Schur complement determinant. Proves strict block coercivity $Q(z_b, z_c) > 0$ for non-zero vectors when the pivot $a_{bb} > 0$ and Schur determinant $\delta > 0$. Includes exact decidable rational pair structures for geometric remainder tail contraction.
- **Exported Declarations:**
  * `MathlibPR.LinearAlgebra.twoBlockQuadForm`
  * `MathlibPR.LinearAlgebra.twoBlockSchurDet`
  * `MathlibPR.LinearAlgebra.schur_complement_quadratic_identity`
  * `MathlibPR.LinearAlgebra.schur_coercivity_from_block_pivots`
  * `MathlibPR.Data.RationalPairs.geometric_cluster_weight_lt_one`
  * `MathlibPR.Data.RationalPairs.geometric_contraction_margin_gt_one_57th`
  * `MathlibPR.Data.RationalPairs.geometric_margin_conservation`
- **Axioms:** Zero custom axioms (kernel: `propext`, `Quot.sound`). Zero internal imports.

---

### Module 2: `MathlibPR_CubicCollarBounds.lean`
- **Source Path:** `formal/yang_mills_blueprint/YangMillsBlueprint/MathlibPR_CubicCollarBounds.lean`
- **Target Mathlib Location:** `Mathlib/LinearAlgebra/Basic.lean` / `Mathlib/Data/Rat/Basic.lean`
- **Mathematical Description:**
  1. Discrete 2-point Poincaré identity for zero-mean variables:
     $$x_1 + x_2 = 0 \implies (x_1 - x_2)^2 = 2 (x_1^2 + x_2^2).$$
  2. Rational evaluation of cubic polynomials bounding boundary collar measures at rational evaluation points $\delta = 1/5$.
- **Exported Declarations:**
  * `MathlibPR.LinearAlgebra.two_point_zero_sum_sq_diff_eq`
  * `MathlibPR.CubicCollar.cubic_collar_eval_eq`
  * `MathlibPR.CubicCollar.cubic_collar_eval_lt_target_margin`
  * `MathlibPR.CubicCollar.cubic_collar_eval_lt_decimal_bound`
- **Axioms:** Zero custom axioms (kernel: `propext`, `Quot.sound`). Zero internal imports.

---

### Module 3: `MathlibPR_QuaternionTwistRigidity.lean`
- **Source Path:** `formal/yang_mills_blueprint/YangMillsBlueprint/MathlibPR_QuaternionTwistRigidity.lean`
- **Target Mathlib Location:** `Mathlib/Algebra/Quaternion.lean`
- **Mathematical Description:**
  In the algebra of quaternions over the integers $\mathbb{H}(\mathbb{Z})$ (representing $\mathfrak{su}(2)$ via pure imaginary quaternions $X = b\mathbf{i} + c\mathbf{j} + d\mathbf{k}$):
  1. Proves that the simultaneous commutator centralizer of the canonical basis elements $\mathbf{i}$ and $\mathbf{j}$ is trivial:
     $$[\mathbf{i}, X] = 0 \land [\mathbf{j}, X] = 0 \implies b = 0 \land c = 0 \land d = 0.$$
  2. Proves the exact adjoint quadratic norm identity:
     $$\| [\mathbf{i}, X] \|^2 + \| [\mathbf{j}, X] \|^2 = 4 b^2 + 4 c^2 + 8 d^2.$$
  3. Proves the uniform spectral gap lower bound:
     $$\| [\mathbf{i}, X] \|^2 + \| [\mathbf{j}, X] \|^2 \ge 4 (b^2 + c^2 + d^2).$$
- **Exported Declarations:**
  * `MathlibPR.QuaternionAlgebra.quat_imag_comm_i_j_trivial`
  * `MathlibPR.QuaternionAlgebra.quat_imag_ad_norm_sq_eq`
  * `MathlibPR.QuaternionAlgebra.quat_imag_ad_spectral_gap`
- **Axioms:** Zero custom axioms (kernel: `propext`, `Classical.choice`, `Quot.sound`). Zero internal imports.

---

## 3. Explicitly Excluded Non-Mathlib Components

The following modules contain domain-specific quantum field theory constructions, multi-scale RG cluster bounds, or specification checklists, and must NOT be submitted to Mathlib:

1. `MissingBridgeInterfaces.lean`: Contains typed checklists (`ContinuumTransferObligations`) representing open Millennium Problem obligations.
2. `BasicTypes.lean`: Contains project-specific mode count definitions for lattice strata.
3. `YM101Closure.lean`: Contains composite multi-species polymer activity definitions.
4. `BlockWeylCollar.lean`: Contains composite block-Poincaré collar summability theorems combining MathlibPR lemmas with project-specific constants.
5. `TwistedFluxonRigidity.lean`: Contains domain-specific twisted-sector polymer activity combinations.
6. `CheckAllDecls.lean` & `VerifyNoTraps.lean`: Project verification scripts.
