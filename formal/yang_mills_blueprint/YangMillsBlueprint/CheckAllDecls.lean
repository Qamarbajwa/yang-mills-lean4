/-
  YangMillsBlueprint.CheckAllDecls
  ==============================
  Audits every theorem in Part I and Part II and prints axiom dependencies.
  Expected result: ZERO `sorryAx`, ZERO custom axioms across all declarations.
-/
import YangMillsBlueprint

#check YangMillsBlueprint.block_mode_dimension_additivity
#print axioms YangMillsBlueprint.block_mode_dimension_additivity

#check YangMillsBlueprint.levi_stratum_mode_conservation
#print axioms YangMillsBlueprint.levi_stratum_mode_conservation

#check YangMillsBlueprint.schur_complement_quadratic_identity
#print axioms YangMillsBlueprint.schur_complement_quadratic_identity

#check YangMillsBlueprint.schur_quadratic_residual_identity
#print axioms YangMillsBlueprint.schur_quadratic_residual_identity

#check YangMillsBlueprint.schur_coercivity_from_block_pivots
#print axioms YangMillsBlueprint.schur_coercivity_from_block_pivots

#check YangMillsBlueprint.YM101.ym101_w2loop_exact
#print axioms YangMillsBlueprint.YM101.ym101_w2loop_exact

#check YangMillsBlueprint.YM101.ym101_cauchy_remainder_exact
#print axioms YangMillsBlueprint.YM101.ym101_cauchy_remainder_exact

#check YangMillsBlueprint.YM101.ym101_all_orders_reduced_eq
#print axioms YangMillsBlueprint.YM101.ym101_all_orders_reduced_eq

#check YangMillsBlueprint.YM101.polydisk_geometric_remainder_bound
#print axioms YangMillsBlueprint.YM101.polydisk_geometric_remainder_bound

#check YangMillsBlueprint.YM101.ym101_all_orders_contraction
#print axioms YangMillsBlueprint.YM101.ym101_all_orders_contraction

#check YangMillsBlueprint.YM101.ym101_margin_conservation
#print axioms YangMillsBlueprint.YM101.ym101_margin_conservation

#check YangMillsBlueprint.YM101.ym101_all_orders_margin_gt_one_57th
#print axioms YangMillsBlueprint.YM101.ym101_all_orders_margin_gt_one_57th

#check YangMillsBlueprint.YM101.ym101_all_orders_margin_gt_decimal_floor
#print axioms YangMillsBlueprint.YM101.ym101_all_orders_margin_gt_decimal_floor

#check YangMillsBlueprint.YM101.ym101_toron_barrier_exceeds_margin
#print axioms YangMillsBlueprint.YM101.ym101_toron_barrier_exceeds_margin

#check YangMillsBlueprint.YM101.ym101_suppressed_toron_fits_margin
#print axioms YangMillsBlueprint.YM101.ym101_suppressed_toron_fits_margin

#check YangMillsBlueprint.Interfaces.check_continuum_obligations_deduction
#print axioms YangMillsBlueprint.Interfaces.check_continuum_obligations_deduction

#check YangMillsBlueprint.Interfaces.conditional_clay_mass_gap_of_bridges
#print axioms YangMillsBlueprint.Interfaces.conditional_clay_mass_gap_of_bridges

#check YangMillsBlueprint.Interfaces.bridge_dag_acyclic_rank
#print axioms YangMillsBlueprint.Interfaces.bridge_dag_acyclic_rank

#check MathlibPR.LinearAlgebra.schur_complement_quadratic_identity
#print axioms MathlibPR.LinearAlgebra.schur_complement_quadratic_identity

#check MathlibPR.LinearAlgebra.schur_coercivity_from_block_pivots
#print axioms MathlibPR.LinearAlgebra.schur_coercivity_from_block_pivots

#check MathlibPR.Data.RationalPairs.geometric_cluster_weight_lt_one
#print axioms MathlibPR.Data.RationalPairs.geometric_cluster_weight_lt_one

#check MathlibPR.Data.RationalPairs.geometric_contraction_margin_gt_one_57th
#print axioms MathlibPR.Data.RationalPairs.geometric_contraction_margin_gt_one_57th

#check MathlibPR.Data.RationalPairs.geometric_margin_conservation
#print axioms MathlibPR.Data.RationalPairs.geometric_margin_conservation
