/-
  YangMillsBlueprint.CheckAllDecls
  ==============================
  Audits every theorem in Part I and Part II and prints axiom dependencies.
  Expected result: ZERO `sorryAx`, ZERO custom axioms across all declarations.
-/
import YangMillsBlueprint

#check YangMillsBlueprint.levi_stratum_mode_conservation
#print axioms YangMillsBlueprint.levi_stratum_mode_conservation

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

#check YangMillsBlueprint.Interfaces.conditional_clay_mass_gap_of_bridges
#print axioms YangMillsBlueprint.Interfaces.conditional_clay_mass_gap_of_bridges

#check YangMillsBlueprint.Interfaces.bridge_dag_acyclic_rank
#print axioms YangMillsBlueprint.Interfaces.bridge_dag_acyclic_rank
