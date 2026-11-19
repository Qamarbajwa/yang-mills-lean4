/-
Copyright (c) 2026 Qamar Munawer. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Qamar Munawer
-/
import Lean
import YangMillsBlueprint.MathlibPR_SchurComplementForms
import YangMillsBlueprint.MathlibPR_CubicCollarBounds
import YangMillsBlueprint.MathlibPR_QuaternionTwistRigidity
import YangMillsBlueprint.MathlibPR_ClockShiftRigidity
import YangMillsBlueprint.MathlibStaging.PolydiskMajorant
import YangMillsBlueprint.MathlibStaging.CubicSinBounds
import YangMillsBlueprint.MathlibStaging.QuaternionCentralizer
import YangMillsBlueprint.MathlibStaging.ClockShiftMatrices
import YangMillsBlueprint.MathlibStaging.NonAbelianCommutatorStiffness
import YangMillsBlueprint.MathlibStaging.CoprimeSpiralTwist
import YangMillsBlueprint.MathlibStaging.QuarticQuantumStiffness
import YangMillsBlueprint.MathlibStaging.CartanCoxeterRigidity
import YangMillsBlueprint.MathlibStaging.ExponentialAreaScreening
import YangMillsBlueprint.MathlibStaging.AsymptoticFreedomFlow
import YangMillsBlueprint.MathlibStaging.SpectralMassGapBridge
import YangMillsBlueprint.MathlibStaging.TEKFourPlaneLattice
import YangMillsBlueprint.MathlibStaging.ExceptionalE8Cartan
import YangMillsBlueprint.MathlibStaging.ClassicalAndExceptionalCartan
import YangMillsBlueprint.MathlibStaging.LeviStratumCounting
import YangMillsBlueprint.MathlibStaging.LoopBootstrapMomentBounds
import YangMillsBlueprint.MathlibStaging.BCDClassicalCartan
import YangMillsBlueprint.MathlibStaging.CurvedBrascampLiebDefect
import YangMillsBlueprint.MathlibStaging.PeierlsRGContourFlow
import YangMillsBlueprint.MathlibStaging.OsterwalderSchraderBridge
import YangMillsBlueprint.MathlibStaging.UrsellCumulantNonGaussian
import YangMillsBlueprint.MathlibStaging.CurvedGroupLogSobolev
import YangMillsBlueprint.MathlibStaging.InductivePeierlsRGBridge
import YangMillsBlueprint.MathlibStaging.SpatialBlockRP
import YangMillsBlueprint.MathlibStaging.SymanzikRotationalBound
import YangMillsBlueprint.MathlibStaging.ShortDistanceOPEWitness
import YangMillsBlueprint.MathlibStaging.TomboulisCharacterFlow
import YangMillsBlueprint.MathlibStaging.EquicontinuousTightnessBridge
import YangMillsBlueprint.MathlibStaging.CenterlessWeylAlcoveGap
import YangMillsBlueprint.MathlibStaging.ChessboardHolderBound
import YangMillsBlueprint.MathlibStaging.VortexSpreadingBound
import YangMillsBlueprint.MathlibStaging.CosetSignMagnitudeCreutz
import YangMillsBlueprint.MathlibStaging.NonAbelianBianchiDefect
import YangMillsBlueprint.MathlibStaging.EffectiveMassTransferGap
import YangMillsBlueprint.MathlibStaging.AdjointBianchiNorm
import YangMillsBlueprint.MathlibStaging.StokesAdjointDispersion
import YangMillsBlueprint.MathlibStaging.SliceMarkovTensorization
import YangMillsBlueprint.MathlibStaging.ScreenedDipoleVariance
import YangMillsBlueprint.MathlibStaging.CoarseSliceDecoherence
import YangMillsBlueprint.MathlibStaging.BianchiDyadicAccumulation
import YangMillsBlueprint.Certificates.YM101_CauchyPolydiskCert
import YangMillsBlueprint.Certificates.YM102_WeylCollarCert
import YangMillsBlueprint.Certificates.YM103_SU2TwistRigidityCert
import YangMillsBlueprint.Certificates.YM104_SU3ClockShiftCert
import YangMillsBlueprint.Certificates.YM105_ZeroModeStiffnessCert
import YangMillsBlueprint.Certificates.YM106_SpiralTwistCert
import YangMillsBlueprint.Certificates.YM107_LuscherQuantumGapCert
import YangMillsBlueprint.Certificates.YM108_CenterlessGroupCert
import YangMillsBlueprint.Certificates.YM109_VortexAreaScreeningCert
import YangMillsBlueprint.Certificates.YM110_AsymptoticFreedomCert
import YangMillsBlueprint.Certificates.YM111_ClayTargetSpecCert
import YangMillsBlueprint.Certificates.YM112_TEKFourPlaneCert
import YangMillsBlueprint.Certificates.YM113_E8CartanRigidityCert
import YangMillsBlueprint.Certificates.YM114_ClassicalExceptionalCartanCert
import YangMillsBlueprint.Certificates.YM115_LeviStratumCert
import YangMillsBlueprint.Certificates.YM116_CrossoverBootstrapCert
import YangMillsBlueprint.Certificates.YM117_BCDClassicalCartanCert
import YangMillsBlueprint.Certificates.YM118_TreeGaugeBrascampLiebCert
import YangMillsBlueprint.Certificates.YM119_VortexRGPersistenceCert
import YangMillsBlueprint.Certificates.YM120_OSReconstructionCert
import YangMillsBlueprint.Certificates.YM121_NonTrivialityWitnessCert
import YangMillsBlueprint.Certificates.YM122_ClayBoundaryMasterCert
import YangMillsBlueprint.Certificates.YM123_DobrushinMixingBridgeCert
import YangMillsBlueprint.Certificates.YM124_InductiveVortexRGCert
import YangMillsBlueprint.Certificates.YM125_SpatialBlockRPCert
import YangMillsBlueprint.Certificates.YM126_SymanzikContinuumCert
import YangMillsBlueprint.Certificates.YM127_ContinuumOPEWitnessCert
import YangMillsBlueprint.Certificates.YM128_TomboulisRougheningCert
import YangMillsBlueprint.Certificates.YM129_ContinuumTightnessCert
import YangMillsBlueprint.Certificates.YM130_CenterlessGroupGapCert
import YangMillsBlueprint.Certificates.YM131_FILSChessboardCert
import YangMillsBlueprint.Certificates.YM132_ThickVortexSpreadingCert
import YangMillsBlueprint.Certificates.YM133_GaugeInvariantCosetCert
import YangMillsBlueprint.Certificates.YM134_BianchiCubeDefectCert
import YangMillsBlueprint.Certificates.YM135_SliceTransferGapCert
import YangMillsBlueprint.Certificates.YM136_GeneralGroupBianchiCert
import YangMillsBlueprint.Certificates.YM137_StokesBianchiDispersionCert
import YangMillsBlueprint.Certificates.YM138_SliceTensorGapCert
import YangMillsBlueprint.Certificates.YM139_BianchiScreenedVarianceCert
import YangMillsBlueprint.Certificates.YM140_CoarseSliceDobrushinCert
import YangMillsBlueprint.Certificates.YM141_BianchiDyadicAccumulationCert
import YangMillsBlueprint.Certificates.YM142_BianchiCocycleCert
import YangMillsBlueprint.Certificates.YM143_CentralizerCodimensionCert
import YangMillsBlueprint.Certificates.YM144_DensityCapVarianceCert
import YangMillsBlueprint.Certificates.YM145_IsotropicSuperblockCert
import YangMillsBlueprint.Certificates.YM146_SchurPartialTraceCert
import YangMillsBlueprint.Certificates.YM147_BlockSchurHierarchyCert
import YangMillsBlueprint.Certificates.YM148_SimpleGroupUniformCert
import YangMillsBlueprint.Certificates.YM149_LatticeHaarGibbsCert
import YangMillsBlueprint.Certificates.YM150_SliceReflectionHilbertCert
import YangMillsBlueprint.Certificates.YM151_BlueprintClayInterfaceCert
import YangMillsBlueprint.Certificates.YM152_WilsonLatticeActionCert
import YangMillsBlueprint.Certificates.YM153_RigidChordActionCert
import YangMillsBlueprint.Certificates.YM154_TreeFrameGaugeCert
import YangMillsBlueprint.Certificates.YM155_BlockPolymerOscillationCert
import YangMillsBlueprint.Certificates.YM156_SelfDualWaveProjectionCert
import YangMillsBlueprint.Certificates.YM157_RigidTransferSynthesisCert
import YangMillsBlueprint.Certificates.YM158_PerturbedBlockSchurCert
import YangMillsBlueprint.Certificates.YM159_ConcreteHodgeInvolutionCert
import YangMillsBlueprint.Certificates.YM160_LatticeReflectionPositivityCert
import YangMillsBlueprint.Certificates.YM161_LorentzianMetricGroupCert
import YangMillsBlueprint.Certificates.YM162_LorentzianHodgeCert
import YangMillsBlueprint.Certificates.YM163_WickSemigroupMassShellCert
import YangMillsBlueprint.Certificates.YM164_BalabanPolymerCollarCert
import YangMillsBlueprint.Certificates.YM165_ConditionalFiberDensityCert
import YangMillsBlueprint.Certificates.YM166_NonCriticalSlabContractionCert
import YangMillsBlueprint.Certificates.YM167_ContinuumSchwingerLimitCert
import YangMillsBlueprint.Certificates.YM168_LocalizedUrsellNonTrivialityCert
import YangMillsBlueprint.Certificates.YM169_CenterlessWeylCasimirCert
import YangMillsBlueprint.Certificates.YM170_QuaternionicOSReflectionCert
import YangMillsBlueprint.Certificates.YM171_SpinorHermitianWickCert
import YangMillsBlueprint.Certificates.YM172_AbstractPolymerClusterCert
import YangMillsBlueprint.Certificates.YM173_MultiscaleBalabanFlowCert
import YangMillsBlueprint.Certificates.YM174_MeasureBathtubFiberCert
import YangMillsBlueprint.Certificates.YM175_PerturbedCocycleSchurCert
import YangMillsBlueprint.Certificates.YM176_AbelianSubtractedParamagneticSchurCert
import YangMillsBlueprint.Certificates.YM177_TwoStepInductiveRGRemainderCert
import YangMillsBlueprint.Certificates.YM177_InductiveRgRemainderContractionCert
import YangMillsBlueprint.Certificates.YM178_SpectralTaylorAndGribovClearanceCert
import YangMillsBlueprint.Certificates.YM179_ContinuumRGBridgeSynthesisCert
import YangMillsBlueprint.Certificates.YM180_UnifiedCrossoverMasterBridgeCert
import YangMillsBlueprint.Certificates.YM181_ClayBoundaryContinuumSynthesisCert

/-!
# Hardened Metaprogramming AST & Axiom Auditor (`VerifyNoTraps`)

This module performs compile-time `Lean.Meta` verification that every declaration in
`auditedTheorems`:
1. Exists in the environment and is not `opaque` or an `axiom`.
2. Uses strictly a subset of `[propext, Classical.choice, Quot.sound]`.
3. Contains zero `sorryAx`, `Lean.ofReduceBool`, or `Lean.ofReduceNat` in its proof AST.
4. Has a conclusion whose `whnf` is not definitionally `True`.
5. Has a conclusion not `isDefEq` to any single hypothesis in its `forallTelescopeReducing`
   context (blocking projection tautologies).
6. Verifies `Nonempty` instances for all conditional certificate structures.
-/

namespace YangMillsBlueprint.VerifyNoTraps

open Lean Meta Elab Command

private def allowedAxioms : List Name :=
  [``propext, ``Classical.choice, ``Quot.sound]

private def forbiddenConsts : List Name :=
  [`sorryAx, `Lean.ofReduceBool, `Lean.ofReduceNat]

private def auditedTheorems : List Name :=
  [ ``PolydiskMajorant.total_weight_lt_one
  , ``PolydiskMajorant.one_sub_weight_pos
  , ``PolydiskMajorant.geometric_defect_le
  , ``PolydiskMajorant.summable_geometric_tail
  , ``PolydiskMajorant.tsum_geometric_tail_eq
  , ``PolydiskMajorant.tsum_geometric_tail_le
  , ``CubicSinBounds.cubicCollarWeight_nonneg
  , ``CubicSinBounds.cubicCollarWeight_anti_left
  , ``CubicSinBounds.sin_sq_le_sq
  , ``CubicSinBounds.integral_sin_sq_le_cubic
  , ``CubicSinBounds.normalized_sin_sq_integral_le_cubicCollarWeight
  , ``QuaternionCentralizer.adjointTwistQuadraticForm_eq
  , ``QuaternionCentralizer.adjointTwistQuadraticForm_ge_three
  , ``ClockShiftMatrices.shift3Perm_cube
  , ``ClockShiftMatrices.clock3_mul_shift3_eq
  , ``ClockShiftMatrices.eisenstein_chord_normSq_one
  , ``ClockShiftMatrices.eisenstein_chord_normSq_two
  , ``ClockShiftMatrices.eisensteinNormSq_nonneg
  , ``ClockShiftMatrices.chord_normSq_eq_four_mul_sin_sq
  , ``ClockShiftMatrices.mul_le_sin_of_mem_Icc
  , ``ClockShiftMatrices.jordan_sin_le_of_mem_Icc
  , ``ClockShiftMatrices.jordan_spectral_gap_le_four_mul_sin_sq
  , ``ClockShiftMatrices.secant_pi_div_six_sin_le_of_mem_Icc
  , ``ClockShiftMatrices.secant_spectral_gap_le_four_mul_sin_sq
  , ``ClockShiftMatrices.cos_pi_div_five_eq
  , ``ClockShiftMatrices.four_mul_sin_pi_div_five_sq_eq
  , ``ClockShiftMatrices.four_mul_sin_pi_div_five_sq_gt
  , ``NonAbelianCommutatorStiffness.lagrange_identity
  , ``NonAbelianCommutatorStiffness.cross_normSq_eq_of_ortho
  , ``NonAbelianCommutatorStiffness.triadQuarticEnergy_eq_of_ortho
  , ``NonAbelianCommutatorStiffness.triadQuarticEnergy_ge_three_mul_sq
  , ``CoprimeSpiralTwist.isUnit_coe_of_coprime
  , ``CoprimeSpiralTwist.spiralMap_eq_zero_iff
  , ``CoprimeSpiralTwist.spiralMap_ne_zero_of_ne_zero
  , ``CoprimeSpiralTwist.spiral_both_coords_ne_zero
  , ``CoprimeSpiralTwist.spiralMap_bijective
  , ``CoprimeSpiralTwist.two_plane_gap_lower_bound
  , ``QuarticQuantumStiffness.cubic_defect_factorization
  , ``QuarticQuantumStiffness.variationalEnergy_sub_min_eq
  , ``QuarticQuantumStiffness.three_mul_sq_le_variationalEnergy
  , ``QuarticQuantumStiffness.variationalEnergy_pos
  , ``CartanCoxeterRigidity.g2CartanDet_eq_one
  , ``CartanCoxeterRigidity.two_mul_g2CartanForm_eq
  , ``CartanCoxeterRigidity.six_mul_f4CartanForm_eq
  , ``CartanCoxeterRigidity.g2CartanForm_eq_zero_iff
  , ``CartanCoxeterRigidity.f4CartanForm_eq_zero_iff
  , ``ExponentialAreaScreening.exp_div_three_cubed
  , ``ExponentialAreaScreening.one_add_div_three_cubed_le_exp
  , ``ExponentialAreaScreening.cubic_div_twenty_seven_le_exp
  , ``ExponentialAreaScreening.quartic_mul_exp_neg_sq_le
  , ``AsymptoticFreedomFlow.inv_runningCoupling_eq
  , ``AsymptoticFreedomFlow.runningCoupling_pos
  , ``AsymptoticFreedomFlow.runningCoupling_le_inv_mul
  , ``AsymptoticFreedomFlow.telescoping_step_eq
  , ``AsymptoticFreedomFlow.telescoped_sum_lt_one
  , ``YangMillsBlueprint.Certificates.small_field_contraction_lt_one_conditional
  , ``YangMillsBlueprint.Certificates.canonical_polymer_weight_lt_one
  , ``YangMillsBlueprint.Certificates.canonical_polymer_tsum_bound
  , ``YangMillsBlueprint.Certificates.weyl_collar_rational_eval
  , ``YangMillsBlueprint.Certificates.weyl_collar_lt_margin
  , ``YangMillsBlueprint.Certificates.weyl_collar_strict_upper_bound_lt_margin
  , ``YangMillsBlueprint.Certificates.su2_real_weyl_collar_integral_lt_margin
  , ``YangMillsBlueprint.Certificates.su2_twisted_laplacian_exact
  , ``YangMillsBlueprint.Certificates.su2_twisted_laplacian_gap_ge_three
  , ``YangMillsBlueprint.Certificates.su2_toron_zero_mode_eliminated
  , ``YangMillsBlueprint.Certificates.su3_clock_shift_spectral_gap_eq_three
  , ``YangMillsBlueprint.Certificates.su3_clock_shift_second_chord_eq_three
  , ``YangMillsBlueprint.Certificates.su3_clock_shift_commutation
  , ``YangMillsBlueprint.Certificates.su5_real_spectral_gap_gt
  , ``YangMillsBlueprint.Certificates.sun_real_jordan_gap_le
  , ``YangMillsBlueprint.Certificates.sun_real_secant_gap_le
  , ``YangMillsBlueprint.Certificates.su2_zero_mode_quartic_stiffness_pos_conditional
  , ``YangMillsBlueprint.Certificates.canonical_zero_mode_energy_eq_three
  , ``YangMillsBlueprint.Certificates.spiral_twist_both_planes_nonzero
  , ``YangMillsBlueprint.Certificates.sun_coprime_spiral_two_plane_gap_le
  , ``YangMillsBlueprint.Certificates.luscher_zero_mode_quantum_gap_ge_conditional
  , ``YangMillsBlueprint.Certificates.canonical_luscher_quantum_gap_pos
  , ``YangMillsBlueprint.Certificates.g2_coxeter_cartan_zero_mode_eliminated
  , ``YangMillsBlueprint.Certificates.f4_coxeter_cartan_zero_mode_eliminated
  , ``YangMillsBlueprint.Certificates.g2_unit_root_stiffness
  , ``YangMillsBlueprint.Certificates.vortex_free_energy_defect_le_real
  , ``YangMillsBlueprint.Certificates.canonical_vortex_defect_lt_one
  , ``YangMillsBlueprint.Certificates.uv_running_coupling_contraction_conditional
  , ``YangMillsBlueprint.Certificates.canonical_uv_coupling_lt_one
  , ``MathlibPR.LinearAlgebra.schur_complement_quadratic_identity
  , ``MathlibPR.LinearAlgebra.schur_coercivity_from_block_pivots
  , ``MathlibPR.LinearAlgebra.two_point_zero_sum_sq_diff_eq
  , ``MathlibPR.Data.RationalPairs.geometric_cluster_weight_lt_one
  , ``MathlibPR.CubicCollar.cubic_collar_eval_lt_target_margin
  , ``MathlibPR.QuaternionAlgebra.quat_imag_comm_i_j_trivial
  , ``MathlibPR.QuaternionAlgebra.quat_imag_ad_spectral_gap
  , ``MathlibPR.ClockShiftAlgebra.mode_pair_norm_sq_pos
  , ``MathlibPR.ClockShiftAlgebra.su3_twisted_eigenvalue_table_min
  , ``MathlibPR.ClockShiftAlgebra.jordan_spectral_gap_pos
  , ``MathlibPR.ClockShiftAlgebra.secant_asymptotic_gap_pos
  , ``MathlibPR.ClockShiftAlgebra.secant_asymptotic_gap_six_eval
  , ``MathlibPR.ClockShiftAlgebra.su5_rational_gap_witness
  , ``MathlibPR.ClockShiftAlgebra.su5_gap_gt_jordan
  , ``SpectralMassGapBridge.exp_neg_mul_anti
  , ``SpectralMassGapBridge.exp_decay_product_le
  , ``SpectralMassGapBridge.coercivity_orthogonal_decomp
  , ``SpectralMassGapBridge.coercivity_pos_of_perp_ne_zero
  , ``TEKFourPlaneLattice.shearMap_bijective
  , ``TEKFourPlaneLattice.shearMap_eq_zero_iff
  , ``TEKFourPlaneLattice.quadratic_rank_gap_le_four_mul_sin_sq
  , ``TEKFourPlaneLattice.four_plane_additive_gap_le
  , ``ExceptionalE8Cartan.e8_sum_of_squares_eq
  , ``ExceptionalE8Cartan.e8CartanForm_nonneg
  , ``ExceptionalE8Cartan.e8CartanForm_eq_zero_iff
  , ``YangMillsBlueprint.Certificates.real_mass_gap_spec_excited_pos
  , ``YangMillsBlueprint.Certificates.canonical_clustering_decay_le
  , ``YangMillsBlueprint.Certificates.tek_shear_bijective
  , ``YangMillsBlueprint.Certificates.tek_quadratic_rank_gap_le
  , ``YangMillsBlueprint.Certificates.tek_four_plane_additive_gap_le
  , ``YangMillsBlueprint.Certificates.canonical_tek_four_plane_gap_gt_one
  , ``YangMillsBlueprint.Certificates.e8_coxeter_cartan_zero_mode_eliminated
  , ``YangMillsBlueprint.Certificates.e8_cartan_form_nonneg
  , ``YangMillsBlueprint.Certificates.e8_unit_simple_root_stiffness
  , ``ClassicalAndExceptionalCartan.aCartanForm_eq_sum_sq
  , ``ClassicalAndExceptionalCartan.aCartanForm_nonneg
  , ``ClassicalAndExceptionalCartan.aCartanForm_eq_zero_iff
  , ``ClassicalAndExceptionalCartan.e6_sum_of_squares_eq
  , ``ClassicalAndExceptionalCartan.e6CartanForm_eq_zero_iff
  , ``ClassicalAndExceptionalCartan.e7_sum_of_squares_eq
  , ``ClassicalAndExceptionalCartan.e7CartanForm_eq_zero_iff
  , ``LeviStratumCounting.stratum_dimension_conservation
  , ``LeviStratumCounting.four_mul_alphaReg_sub_alphaHarm_eq
  , ``LeviStratumCounting.alphaHarm_central_le_alphaReg
  , ``LoopBootstrapMomentBounds.sq_le_moment_of_schur
  , ``LoopBootstrapMomentBounds.loop_eq_level4_quadratic_le
  , ``LoopBootstrapMomentBounds.completed_square_identity
  , ``LoopBootstrapMomentBounds.loop_eq_level4_completed_square_le
  , ``LoopBootstrapMomentBounds.domino_reflection_positivity_bound
  , ``YangMillsBlueprint.Certificates.su_an_cartan_zero_mode_eliminated
  , ``YangMillsBlueprint.Certificates.su_an_cartan_form_nonneg
  , ``YangMillsBlueprint.Certificates.e6_coxeter_cartan_zero_mode_eliminated
  , ``YangMillsBlueprint.Certificates.e7_coxeter_cartan_zero_mode_eliminated
  , ``YangMillsBlueprint.Certificates.e6_e7_unit_simple_root_stiffness
  , ``YangMillsBlueprint.Certificates.su_n_levi_stratum_mode_balance
  , ``YangMillsBlueprint.Certificates.central_toron_harmonic_exponent_le_regular
  , ``YangMillsBlueprint.Certificates.su3_central_vs_regular_exponent_eval
  , ``YangMillsBlueprint.Certificates.crossover_level4_bootstrap_window
  , ``YangMillsBlueprint.Certificates.canonical_crossover_rhs_eval
  , ``YangMillsBlueprint.Certificates.crossover_level4_domino_coupling_conditional
  , ``BCDClassicalCartan.bCartanForm_eq_sum_sq
  , ``BCDClassicalCartan.cCartanForm_eq_sum_sq
  , ``BCDClassicalCartan.dCartanForm_eq_sum_sq
  , ``BCDClassicalCartan.bCartanForm_nonneg
  , ``BCDClassicalCartan.cCartanForm_nonneg
  , ``BCDClassicalCartan.dCartanForm_nonneg
  , ``BCDClassicalCartan.bCartanForm_eq_zero_iff
  , ``BCDClassicalCartan.cCartanForm_eq_zero_iff
  , ``BCDClassicalCartan.dCartanForm_eq_zero_iff
  , ``BCDClassicalCartan.d4CartanForm_eq_zero_iff
  , ``YangMillsBlueprint.Certificates.so_odd_bn_cartan_zero_mode_eliminated
  , ``YangMillsBlueprint.Certificates.sp_cn_cartan_zero_mode_eliminated
  , ``YangMillsBlueprint.Certificates.spin_dn_cartan_zero_mode_eliminated
  , ``YangMillsBlueprint.Certificates.spin8_d4_cartan_zero_mode_eliminated
  , ``CurvedBrascampLiebDefect.tree_gauge_dof_conservation
  , ``CurvedBrascampLiebDefect.effectiveStiffness_pos
  , ``CurvedBrascampLiebDefect.curvedVarianceBound_pos
  , ``CurvedBrascampLiebDefect.curvedVarianceBound_le_of_margin
  , ``PeierlsRGContourFlow.rgTensionStep_sub_critical
  , ``PeierlsRGContourFlow.criticalTension_lt_rgTensionStep
  , ``PeierlsRGContourFlow.lt_rgTensionStep_of_gt_critical
  , ``OsterwalderSchraderBridge.finiteVolumeCorrelatorBound_nonneg
  , ``OsterwalderSchraderBridge.finiteVolumeCorrelatorBound_anti_time
  , ``OsterwalderSchraderBridge.finiteVolumeCorrelatorBound_anti_volume
  , ``OsterwalderSchraderBridge.clustering_extraction_le
  , ``UrsellCumulantNonGaussian.ursellFour_eq_zero_iff
  , ``UrsellCumulantNonGaussian.ursellFour_neg_of_subgaussian
  , ``UrsellCumulantNonGaussian.ursellFour_ne_zero_of_subgaussian
  , ``YangMillsBlueprint.Certificates.tree_gauge_dof_balance
  , ``YangMillsBlueprint.Certificates.curved_variance_bound_le_conditional
  , ``YangMillsBlueprint.Certificates.canonical_curved_brascamp_lieb_eval
  , ``YangMillsBlueprint.Certificates.peierls_rg_tension_amplifies_conditional
  , ``YangMillsBlueprint.Certificates.canonical_vortex_rg_persistence_eval
  , ``YangMillsBlueprint.Certificates.os_clustering_and_vortex_suppression_conditional
  , ``YangMillsBlueprint.Certificates.canonical_os_correlator_envelope_le
  , ``YangMillsBlueprint.Certificates.subgaussian_ursell_nontrivial_conditional
  , ``YangMillsBlueprint.Certificates.canonical_ursell_four_eval
  , ``YangMillsBlueprint.Certificates.clay_millennium_boundary_master_conditional
  , ``CurvedGroupLogSobolev.dobrushinGlobalGap_pos
  , ``CurvedGroupLogSobolev.dobrushinGlobalGap_ge_of_bounds
  , ``CurvedGroupLogSobolev.holleyStroockFactor_pos
  , ``CurvedGroupLogSobolev.holleyStroockFactor_anti
  , ``CurvedGroupLogSobolev.dobrushin_holley_stroock_pos
  , ``InductivePeierlsRGBridge.floor_le_rgStep_of_le
  , ``InductivePeierlsRGBridge.rgTrajectory_ge_floor
  , ``InductivePeierlsRGBridge.rgTrajectory_strict_above_critical
  , ``SpatialBlockRP.rpKernelForm_nonneg
  , ``SpatialBlockRP.rpKernelForm_add_nonneg
  , ``SpatialBlockRP.rpKernelForm_convex_comb_nonneg
  , ``YangMillsBlueprint.Certificates.dobrushin_global_log_sobolev_gap_conditional
  , ``YangMillsBlueprint.Certificates.canonical_dobrushin_mixing_eval
  , ``YangMillsBlueprint.Certificates.inductive_peierls_tension_floor_conditional
  , ``YangMillsBlueprint.Certificates.canonical_inductive_vortex_rg_eval
  , ``YangMillsBlueprint.Certificates.spatial_block_reflection_positivity_conditional
  , ``YangMillsBlueprint.Certificates.canonical_spatial_block_rp_nonneg
  , ``SymanzikRotationalBound.symanzikBound_nonneg
  , ``SymanzikRotationalBound.symanzikBound_le_linear
  , ``SymanzikRotationalBound.symanzikBound_lt_of_cutoff
  , ``ShortDistanceOPEWitness.opeFourPointLower_pos
  , ``ShortDistanceOPEWitness.ne_zero_of_abs_ge_ope
  , ``YangMillsBlueprint.Certificates.symanzik_rotational_restoration_conditional
  , ``YangMillsBlueprint.Certificates.canonical_symanzik_rotational_lt_tenth
  , ``YangMillsBlueprint.Certificates.continuum_ope_four_point_nontrivial_conditional
  , ``YangMillsBlueprint.Certificates.canonical_ope_lower_pos
  , ``TomboulisCharacterFlow.characterWeightStep_le_mul
  , ``TomboulisCharacterFlow.characterTrajectory_le_geom
  , ``EquicontinuousTightnessBridge.limit_le_of_forall_pos_add
  , ``EquicontinuousTightnessBridge.clustering_limit_of_vanishing_cutoffs
  , ``EquicontinuousTightnessBridge.joint_cutoff_sum_lt
  , ``CenterlessWeylAlcoveGap.adjointGapFloor_pos
  , ``CenterlessWeylAlcoveGap.weylAlcoveCoerciveGap_pos
  , ``YangMillsBlueprint.Certificates.tomboulis_character_flow_decays_conditional
  , ``YangMillsBlueprint.Certificates.canonical_tomboulis_blocked_step_eval
  , ``YangMillsBlueprint.Certificates.continuum_clustering_limit_conditional
  , ``YangMillsBlueprint.Certificates.canonical_joint_cutoff_lt_tenth
  , ``YangMillsBlueprint.Certificates.centerless_adjoint_gap_pos_conditional
  , ``YangMillsBlueprint.Certificates.canonical_centerless_g2_combined_gap_pos
  , ``ChessboardHolderBound.chessboard_defect_le_of_pow
  , ``ChessboardHolderBound.chessboard_cluster_suppression
  , ``ChessboardHolderBound.chessboard_strict_threshold_lt
  , ``YangMillsBlueprint.Certificates.fils_chessboard_cluster_decay_conditional
  , ``YangMillsBlueprint.Certificates.canonical_fils_chessboard_eval
  , ``VortexSpreadingBound.one_sub_cos_le_sq_div_two
  , ``VortexSpreadingBound.spreadTrigCost_le
  , ``VortexSpreadingBound.spreadTrigCost_lt_of_cutoff
  , ``YangMillsBlueprint.Certificates.thick_vortex_spread_cost_lt_conditional
  , ``YangMillsBlueprint.Certificates.canonical_thick_vortex_w16_lt_tenth
  , ``CosetSignMagnitudeCreutz.centerSign_mul_abs
  , ``CosetSignMagnitudeCreutz.coset_energy_decomposition
  , ``CosetSignMagnitudeCreutz.coset_defects_nonneg
  , ``CosetSignMagnitudeCreutz.creutzRatio_factorization
  , ``CosetSignMagnitudeCreutz.creutzRatio_pos_of_sign_dominance
  , ``YangMillsBlueprint.Certificates.gauge_invariant_coset_creutz_gap_conditional
  , ``YangMillsBlueprint.Certificates.canonical_gauge_invariant_coset_creutz_pos
  , ``NonAbelianBianchiDefect.transportDiffNormSq_eq
  , ``NonAbelianBianchiDefect.unit_transportDiffNormSq_eq
  , ``NonAbelianBianchiDefect.unit_transportDiffNormSq_ge
  , ``NonAbelianBianchiDefect.unit_transport_zero_of_cross_zero
  , ``YangMillsBlueprint.Certificates.nonabelian_bianchi_transport_defect_pos
  , ``YangMillsBlueprint.Certificates.canonical_bianchi_transport_defect_gt_one
  , ``YangMillsBlueprint.Certificates.abelian_collinear_bianchi_defect_zero
  , ``EffectiveMassTransferGap.spectralCorr_nonneg
  , ``EffectiveMassTransferGap.spectralCorr_succ_le
  , ``EffectiveMassTransferGap.spectralCorr_le_pow_mul_zero
  , ``EffectiveMassTransferGap.spectralCorr_log_convex
  , ``EffectiveMassTransferGap.effectiveMassRatio_mono
  , ``YangMillsBlueprint.Certificates.slice_transfer_exponential_decay_conditional
  , ``YangMillsBlueprint.Certificates.slice_transfer_log_convex
  , ``YangMillsBlueprint.Certificates.canonical_slice_glueball_t4_decay
  , ``AdjointBianchiNorm.frobSq_nonneg
  , ``AdjointBianchiNorm.frobSq_adjAction
  , ``AdjointBianchiNorm.adjAction_sub_eq
  , ``AdjointBianchiNorm.frobSq_adjAction_sub_eq
  , ``AdjointBianchiNorm.frobSq_adjAction_sub_zero_of_comm
  , ``YangMillsBlueprint.Certificates.general_adjoint_bianchi_defect_pos
  , ``YangMillsBlueprint.Certificates.canonical_so3_adjoint_bianchi_defect_gt_three
  , ``YangMillsBlueprint.Certificates.canonical_cartan_commuting_bianchi_zero
  , ``StokesAdjointDispersion.frobInner_comm
  , ``StokesAdjointDispersion.frobSq_sub_eq
  , ``StokesAdjointDispersion.frobSq_add_eq
  , ``StokesAdjointDispersion.frobInner_adjAction_self_mul_two
  , ``StokesAdjointDispersion.frobSq_coulomb_dipole_noncancellation
  , ``StokesAdjointDispersion.frobSq_exact_cancellation_eq_comm
  , ``StokesAdjointDispersion.stokes_sum_frobSq_ge_of_bianchi_floor
  , ``YangMillsBlueprint.Certificates.stokes_coulomb_dipole_broken_pos
  , ``YangMillsBlueprint.Certificates.canonical_so3_dipole_broken_gt_three
  , ``YangMillsBlueprint.Certificates.canonical_cartan_dipole_cancels_zero
  , ``YangMillsBlueprint.Certificates.stokes_area_variance_persists_conditional
  , ``SliceMarkovTensorization.weighted_cs_sq_le
  , ``SliceMarkovTensorization.schur_symmetric_operator_sq_le
  , ``SliceMarkovTensorization.rayleigh_abs_le_of_schur
  , ``SliceMarkovTensorization.slice_tensor_contraction_le
  , ``YangMillsBlueprint.Certificates.slice_tensor_margin_pos
  , ``YangMillsBlueprint.Certificates.canonical_slice_tensor_margin_gt_third
  , ``YangMillsBlueprint.Certificates.slice_tensor_uniform_gap_conditional
  , ``ScreenedDipoleVariance.screenedVarianceRatio_abelian_collapse
  , ``ScreenedDipoleVariance.delta_le_screenedVarianceRatio
  , ``ScreenedDipoleVariance.one_sub_alpha_le_screenedVarianceRatio
  , ``ScreenedDipoleVariance.screenedVarianceRatio_pos_of_loss
  , ``ScreenedDipoleVariance.screenedSurfaceVariance_ge_area_floor
  , ``YangMillsBlueprint.Certificates.canonical_screened_ratio_nn_eq
  , ``YangMillsBlueprint.Certificates.canonical_screened_ratio_full_eq
  , ``YangMillsBlueprint.Certificates.screened_ratio_pos_of_cert
  , ``YangMillsBlueprint.Certificates.bianchi_screened_area_law_variance_conditional
  , ``CoarseSliceDecoherence.coarseSliceCoupling_zero
  , ``CoarseSliceDecoherence.coarseSliceCoupling_anti_step
  , ``CoarseSliceDecoherence.coarseSliceCoupling_le_margin
  , ``YangMillsBlueprint.Certificates.canonical_coarse_slice_k3_eval
  , ``YangMillsBlueprint.Certificates.coarse_slice_sq_margin_pos
  , ``YangMillsBlueprint.Certificates.coarse_slice_dobrushin_gap_conditional
  , ``BianchiDyadicAccumulation.one_sub_dyadicLossStep
  , ``BianchiDyadicAccumulation.one_sub_iteratedDyadicLoss_eq
  , ``BianchiDyadicAccumulation.lt_dyadicLossStep_of_pos_of_lt_one
  , ``BianchiDyadicAccumulation.dyadicLossStep_lt_one
  , ``BianchiDyadicAccumulation.iteratedDyadicLoss_zero
  , ``BianchiDyadicAccumulation.iteratedDyadicLoss_mem_Ioo
  , ``YangMillsBlueprint.Certificates.canonical_dyadic_k1_eq
  , ``YangMillsBlueprint.Certificates.canonical_dyadic_k2_eq
  , ``YangMillsBlueprint.Certificates.canonical_dyadic_k2_gt_third
  , ``YangMillsBlueprint.Certificates.abelian_dyadic_loss_zero
  , ``YangMillsBlueprint.Certificates.dyadic_bianchi_step_amplifies
  , ``YangMillsBlueprint.Certificates.dyadic_bianchi_saturation_conditional
  , ``BianchiCocycleDecomposition.adjAction_mul
  , ``BianchiCocycleDecomposition.adjDelta_mul
  , ``BianchiCocycleDecomposition.frobSq_matrixComm_mul_eq
  , ``BianchiCocycleDecomposition.cocycleLoss_split_eq
  , ``BianchiCocycleDecomposition.dyadic_step_ge_of_remainder_bound
  , ``YangMillsBlueprint.Certificates.so3RotZ345_orth1
  , ``YangMillsBlueprint.Certificates.so3RotZ345_orth2
  , ``YangMillsBlueprint.Certificates.canonical_cocycle_dV_eq
  , ``YangMillsBlueprint.Certificates.canonical_cocycle_dVV_eq
  , ``YangMillsBlueprint.Certificates.canonical_cocycle_eps_eq
  , ``YangMillsBlueprint.Certificates.canonical_cocycle_superdyadic_lt
  , ``YangMillsBlueprint.Certificates.cocycle_dyadic_lower_bound_conditional
  , ``CentralizerCodimensionBound.so3OfQuat_orth_right
  , ``CentralizerCodimensionBound.frobSq_so3OfQuat_comm_axisZ
  , ``CentralizerCodimensionBound.transverse_sq_le_of_comm_le
  , ``CentralizerCodimensionBound.bathtub_expectation_floor
  , ``CentralizerCodimensionBound.bathtub_integral_eval
  , ``YangMillsBlueprint.Certificates.canonical_transverse_quat_comm_eq
  , ``YangMillsBlueprint.Certificates.cartan_quat_comm_zero
  , ``YangMillsBlueprint.Certificates.canonical_bathtub_m4_eval
  , ``YangMillsBlueprint.Certificates.centralizer_bathtub_floor_conditional
  , ``GibbsDensityCapVariance.gibbsRatio_le_bound
  , ``GibbsDensityCapVariance.exp_neg_ratio_eq_exp_sub
  , ``GibbsDensityCapVariance.four_div_exp_eq_four_mul_exp_neg
  , ``GibbsDensityCapVariance.variance_floor_of_bounded_osc
  , ``YangMillsBlueprint.Certificates.canonical_density_cap_le
  , ``YangMillsBlueprint.Certificates.canonical_variance_floor_half
  , ``YangMillsBlueprint.Certificates.crossover_variance_floor_of_bounded_osc_conditional
  , ``IsotropicSuperblockDobrushin.total_div_in_eq_superblockM0
  , ``IsotropicSuperblockDobrushin.superblockM0_le_of_leakage_ratio
  , ``IsotropicSuperblockDobrushin.superblockM0_nonneg
  , ``IsotropicSuperblockDobrushin.superblock_coupling_le_margin
  , ``YangMillsBlueprint.Certificates.canonical_superblock_m0_eq
  , ``YangMillsBlueprint.Certificates.canonical_superblock_coupling_eval
  , ``YangMillsBlueprint.Certificates.canonical_superblock_coupling_lt_third
  , ``YangMillsBlueprint.Certificates.superblock_uniform_gap_conditional
  , ``SchurPartialTraceContraction.schur_complete_sq
  , ``SchurPartialTraceContraction.schur_three_slice_complete_sq
  , ``SchurPartialTraceContraction.one_sub_schurPrecisionCoupling_eq
  , ``SchurPartialTraceContraction.schurEff_pos
  , ``SchurPartialTraceContraction.schurPrecisionCoupling_lt
  , ``SchurPartialTraceContraction.schurPrecisionCoupling_pos
  , ``SchurPartialTraceContraction.one_sub_schurPrecisionCoupling_pos
  , ``YangMillsBlueprint.Certificates.canonical_schur_one_step_eq
  , ``YangMillsBlueprint.Certificates.canonical_schur_two_step_eq
  , ``YangMillsBlueprint.Certificates.canonical_schur_monotone_lt
  , ``YangMillsBlueprint.Certificates.schur_partial_trace_contraction_conditional
  , ``BlockSchurHierarchy.even_block_chain_complete_sq
  , ``BlockSchurHierarchy.schur_chain_margin_eq
  , ``BlockSchurHierarchy.blockRatio_renorm_eq
  , ``BlockSchurHierarchy.blockRatioNext_lt_sq
  , ``BlockSchurHierarchy.blockRatioNext_lt_self
  , ``BlockSchurHierarchy.iteratedBlockRatio_mem_Ico
  , ``BlockSchurHierarchy.blockChain_margin_monotone
  , ``YangMillsBlueprint.Certificates.canonical_block_ratio_k1_eq
  , ``YangMillsBlueprint.Certificates.canonical_block_ratio_k2_eq
  , ``YangMillsBlueprint.Certificates.canonical_block_ratio_k2_lt_eighth
  , ``YangMillsBlueprint.Certificates.canonical_margin_amplified
  , ``YangMillsBlueprint.Certificates.block_hierarchy_gap_conditional
  , ``SimpleGroupUniformClosure.transverseCodim_ge_two
  , ``SimpleGroupUniformClosure.codimNormalizedFloor_ge_base
  , ``SimpleGroupUniformClosure.codimNormalizedFloor_pos
  , ``SimpleGroupUniformClosure.uniform_superblock_ratio_lt_one
  , ``SimpleGroupUniformClosure.uniform_block_schur_gap_pos
  , ``YangMillsBlueprint.Certificates.canonical_so3_codim_floor_eq
  , ``YangMillsBlueprint.Certificates.canonical_g2_codim_floor_eq
  , ``YangMillsBlueprint.Certificates.canonical_f4_codim_floor_eq
  , ``YangMillsBlueprint.Certificates.canonical_e8_codim_floor_eq
  , ``YangMillsBlueprint.Certificates.canonical_exceptional_floor_monotone
  , ``YangMillsBlueprint.Certificates.simple_group_uniform_gap_conditional
  , ``LatticeHaarGibbs.partitionIntegral_ge_exp_neg_max
  , ``LatticeHaarGibbs.partitionIntegral_le_exp_neg_min
  , ``LatticeHaarGibbs.partitionIntegral_pos
  , ``LatticeHaarGibbs.weightedExpectation_const
  , ``LatticeHaarGibbs.boltzmannDensity_le_exp_osc
  , ``LatticeHaarGibbs.weightedExpectation_ge_exp_neg_osc_mul_integral
  , ``LatticeHaarGibbs.productHaar_partitionIntegral_pos
  , ``LatticeHaarGibbs.productHaar_density_le_exp_osc
  , ``LatticeHaarGibbs.productHaar_expectation_ge_exp_neg_osc
  , ``YangMillsBlueprint.Certificates.canonical_haar_osc_density_cap_eq
  , ``YangMillsBlueprint.Certificates.canonical_haar_exp_floor_eq
  , ``YangMillsBlueprint.Certificates.lattice_haar_gibbs_variance_floor_conditional
  , ``SliceReflectionHilbert.osEmbed_inner
  , ``SliceReflectionHilbert.osEmbed_norm_sq
  , ``SliceReflectionHilbert.osEmbed_eq_zero_of_null
  , ``SliceReflectionHilbert.transfer_preserves_orth
  , ``SliceReflectionHilbert.transfer_pow_preserves_orth
  , ``SliceReflectionHilbert.transfer_pow_norm_le
  , ``SliceReflectionHilbert.transfer_correlator_exp_decay
  , ``SliceReflectionHilbert.transfer_to_coercivity
  , ``YangMillsBlueprint.Certificates.canonical_transfer_gap_eq
  , ``YangMillsBlueprint.Certificates.canonical_transfer_log_gap_eq
  , ``YangMillsBlueprint.Certificates.slice_reflection_hilbert_gap_conditional
  , ``YangMillsBlueprint.Certificates.canonical_clay_interface_witness_eval
  , ``YangMillsBlueprint.Certificates.blueprint_clay_hilbert_interface_conditional
  , ``WilsonPlaquetteAction.orth_mul_orth
  , ``WilsonPlaquetteAction.plaquette_trace_gauge_invariant
  , ``WilsonPlaquetteAction.frobSq_sub_one_eq_of_orth
  , ``WilsonPlaquetteAction.frobSq_add_one_eq_of_orth
  , ``WilsonPlaquetteAction.orth_trace_bounds
  , ``WilsonPlaquetteAction.plaquetteCost_mem_Icc
  , ``WilsonPlaquetteAction.stapleAction_mem_Icc
  , ``WilsonPlaquetteAction.singleLink_conditional_density_cap
  , ``WilsonPlaquetteAction.singleLink_conditional_variance_floor
  , ``YangMillsBlueprint.Certificates.canonical_4d_staple_osc_eq
  , ``YangMillsBlueprint.Certificates.wilson_4d_single_link_unconditional
  , ``YangMillsBlueprint.Certificates.wilson_crossover_continuum_gap_conditional
  , ``RigidChordAction.orth_left_mul_orth
  , ``RigidChordAction.neg_one_orth
  , ``RigidChordAction.frobSq_add_frobSq_sub
  , ``RigidChordAction.frobSq_conj_sub_one
  , ``RigidChordAction.mul_sub_one_eq
  , ``RigidChordAction.frobSq_add_le_two_mul
  , ``RigidChordAction.frobSq_mul_sub_one_le
  , ``RigidChordAction.frobSq_plaquette_le_four_sum
  , ``RigidChordAction.plaquetteCost_eq_frobSq_div
  , ``RigidChordAction.plaquetteCost_one_eq_zero
  , ``RigidChordAction.plaquetteCost_neg_one_eq_two
  , ``RigidChordAction.plaquetteCost_conj_invariant
  , ``YangMillsBlueprint.Certificates.canonical_identity_and_antipodal_cost
  , ``YangMillsBlueprint.Certificates.rigid_plaquette_cost_le_two_div_n_mul_link_chords
  , ``YangMillsBlueprint.Certificates.rigid_small_field_plaquette_cap_conditional
  , ``TreeFrameGaugeInvariance.gaugeTransform_one
  , ``TreeFrameGaugeInvariance.gaugeTransform_comp
  , ``TreeFrameGaugeInvariance.gaugeTransform_inv_left
  , ``TreeFrameGaugeInvariance.gaugeTransform_inv_right
  , ``TreeFrameGaugeInvariance.gaugeTransform_eq_one_of_tree_frame
  , ``TreeFrameGaugeInvariance.closed_plaquette_gauge_conj
  , ``TreeFrameGaugeInvariance.map_mul_right_compactHaarProb
  , ``TreeFrameGaugeInvariance.measurePreserving_mul_left_compactHaarProb
  , ``TreeFrameGaugeInvariance.measurePreserving_mul_right_compactHaarProb
  , ``TreeFrameGaugeInvariance.measurePreserving_twoSided_compactHaarProb
  , ``TreeFrameGaugeInvariance.measurePreserving_gaugeTransform
  , ``TreeFrameGaugeInvariance.integrable_gaugeTransform_iff
  , ``TreeFrameGaugeInvariance.integral_gaugeTransform
  , ``TreeFrameGaugeInvariance.partitionIntegral_gaugeTransform
  , ``TreeFrameGaugeInvariance.weightedExpectation_gaugeTransform
  , ``TreeFrameGaugeInvariance.weightedExpectation_gauge_invariant
  , ``YangMillsBlueprint.Certificates.canonical_tree_frame_floor_eq
  , ``YangMillsBlueprint.Certificates.tree_frame_gauge_expectation_unconditional
  , ``YangMillsBlueprint.Certificates.tree_frame_oscillation_floor_conditional
  , ``BlockPolymerOscillation.polymerTailBound_nonneg
  , ``BlockPolymerOscillation.effectiveBlockOsc_nonneg
  , ``BlockPolymerOscillation.finset_geom_tail_le_polymerTailBound
  , ``BlockPolymerOscillation.block_action_mem_Icc_of_polymer_tail
  , ``BlockPolymerOscillation.productHaar_polymer_density_cap
  , ``BlockPolymerOscillation.productHaar_polymer_expectation_floor
  , ``YangMillsBlueprint.Certificates.canonical_polymer_osc_eq
  , ``YangMillsBlueprint.Certificates.block_polymer_oscillation_gibbs_conditional
  , ``SelfDualWaveProjection.projPlus_add_projMinus
  , ``SelfDualWaveProjection.projPlus_eigen
  , ``SelfDualWaveProjection.projMinus_eigen
  , ``SelfDualWaveProjection.projPlus_idem
  , ``SelfDualWaveProjection.projMinus_idem
  , ``SelfDualWaveProjection.projPlus_projMinus_zero
  , ``SelfDualWaveProjection.inner_projPlus_projMinus
  , ``SelfDualWaveProjection.norm_sq_eq_projPlus_add_projMinus
  , ``SelfDualWaveProjection.inner_self_invol_eq_sub
  , ``SelfDualWaveProjection.abs_inner_invol_le_norm_sq
  , ``SelfDualWaveProjection.fourD_curvature_choose_split
  , ``SelfDualWaveProjection.eightD_spinor_fourform_choose_split
  , ``SelfDualWaveProjection.inner_projOrth_zero
  , ``SelfDualWaveProjection.norm_unitProject
  , ``SelfDualWaveProjection.inner_self_sphereGrad_zero
  , ``SelfDualWaveProjection.norm_sq_unnormalized_step
  , ``SelfDualWaveProjection.unnormalized_step_ne_zero
  , ``SelfDualWaveProjection.norm_adaptedWaveStep
  , ``SelfDualWaveProjection.adaptedWaveStep_preserves_orth
  , ``SelfDualWaveProjection.rayleighEnergy_unitProject
  , ``SelfDualWaveProjection.rayleigh_adaptedWaveStep_descent
  , ``SelfDualWaveProjection.rayleigh_adaptedWaveStep_le
  , ``SelfDualWaveProjection.adaptedWaveStep_transfer_descent_and_floor
  , ``YangMillsBlueprint.Certificates.canonical_hodge_dimension_splits
  , ``YangMillsBlueprint.Certificates.self_dual_bogomolnyi_unconditional
  , ``YangMillsBlueprint.Certificates.projected_wave_adaptation_transfer_conditional
  , ``YangMillsBlueprint.Certificates.canonical_synthesis_witness_eval
  , ``YangMillsBlueprint.Certificates.rigid_transfer_synthesis_conditional
  , ``YangMillsBlueprint.Certificates.canonical_perturbed_schur_eval
  , ``YangMillsBlueprint.Certificates.perturbed_schur_tail_contraction_conditional
  , ``YangMillsBlueprint.Certificates.hodge4D_and_8D_unconditional
  , ``YangMillsBlueprint.Certificates.hodge4D_8D_energy_bogomolnyi_unconditional
  , ``YangMillsBlueprint.Certificates.wilson_finite_box_reflection_positivity_unconditional
  , ``YangMillsBlueprint.Certificates.lorentzian_metric_and_boost_group_unconditional
  , ``YangMillsBlueprint.Certificates.lorentzian_hodge_complex_structure_unconditional
  , ``YangMillsBlueprint.Certificates.lorentzian_energy_poynting_causality_unconditional
  , ``YangMillsBlueprint.Certificates.wick_semigroup_mass_shell_unconditional
  , ``YangMillsBlueprint.Certificates.wick_mass_shell_gap_conditional
  , ``YangMillsBlueprint.Certificates.balaban_fp_jacobian_and_kp_unconditional
  , ``YangMillsBlueprint.Certificates.balaban_stage1_collar_gibbs_conditional
  , ``YangMillsBlueprint.Certificates.canonical_fiber_tail_eval
  , ``YangMillsBlueprint.Certificates.stage2a_conditional_fiber_density_conditional
  , ``YangMillsBlueprint.Certificates.powerLaw_fails_uniform_contraction_unconditional
  , ``YangMillsBlueprint.Certificates.stage2b_noncritical_slab_dobrushin_conditional
  , ``YangMillsBlueprint.Certificates.continuum_os0_os1_os3_os4_limit_preservation_unconditional
  , ``YangMillsBlueprint.Certificates.continuum_schwinger_limit_bridge_conditional
  , ``YangMillsBlueprint.Certificates.localized_ursell_rules_out_gaussian_unconditional
  , ``YangMillsBlueprint.Certificates.continuum_localized_nontriviality_conditional
  , ``YangMillsBlueprint.Certificates.all_simple_lie_invariants_unconditional
  , ``YangMillsBlueprint.Certificates.universal_simple_group_mass_shell_conditional
  , ``YangMillsBlueprint.Certificates.quaternionic_spin4_os_swap_unconditional
  , ``YangMillsBlueprint.Certificates.os_chiral_hodge_lorentz_unification_unconditional
  , ``YangMillsBlueprint.Certificates.spinor_hermitian_wick_double_cover_unconditional
  , ``YangMillsBlueprint.Certificates.spinor_mass_shell_os_gap_conditional
  , ``YangMillsBlueprint.Certificates.abstract_polymer_kp_collar_decoupling_unconditional
  , ``YangMillsBlueprint.Certificates.stage1_polymer_gas_gibbs_decoupling_conditional
  , ``YangMillsBlueprint.Certificates.multiscale_balaban_summability_vs_harmonic_unconditional
  , ``YangMillsBlueprint.Certificates.balaban_multiscale_stage1_bridge_conditional
  , ``YangMillsBlueprint.Certificates.measure_bathtub_sharp_and_codim_d_unconditional
  , ``YangMillsBlueprint.Certificates.stage2a_fiber_measure_bathtub_conditional
  , ``YangMillsBlueprint.Certificates.stage2a_cocycle_and_schur_thresholds_unconditional
  , ``YangMillsBlueprint.Certificates.stage2a_full_crossover_basin_conditional
  , ``YangMillsBlueprint.Certificates.offdiag_polarization_trace_zero_unconditional
  , ``YangMillsBlueprint.Certificates.paramagnetic_trace_sandwich_and_gribov_clearance_unconditional
  , ``YangMillsBlueprint.Certificates.paramagnetic_dominance_negative_defect_unconditional
  , ``YangMillsBlueprint.Certificates.cocycle_and_commutator_floor_unconditional
  , ``YangMillsBlueprint.Certificates.remainder_trap_invariant_unconditional
  , ``YangMillsBlueprint.Certificates.strict_coupling_descent_step_unconditional
  , ``YangMillsBlueprint.Certificates.inductive_rg_basin_entry_unconditional
  , ``YangMillsBlueprint.Certificates.inductive_rg_remainder_uniform_bound_unconditional
  , ``YangMillsBlueprint.Certificates.inductive_rg_strict_coupling_descent_unconditional
  , ``YangMillsBlueprint.Certificates.small_field_gribov_clearance_unconditional
  , ``YangMillsBlueprint.Certificates.real_log_fourth_order_sandwich_unconditional
  , ``YangMillsBlueprint.Certificates.trace_log_schur_sandwich_unconditional
  , ``YangMillsBlueprint.Certificates.large_field_small_field_gibbs_split_unconditional
  , ``YangMillsBlueprint.Certificates.renormalized_cocycle_one_loop_descent_unconditional
  , ``YangMillsBlueprint.Certificates.continuum_mass_gap_from_uniform_bridges_conditional
  , ``YangMillsBlueprint.Certificates.peierls_exponential_threshold_unconditional
  , ``YangMillsBlueprint.Certificates.master_uv_to_continuum_gap_conditional
  , ``YangMillsBlueprint.Certificates.clay_hilbert_and_rg_crossover_synthesis_conditional
  ]

private def requiredNonemptyStructs : List Name :=
  [ ``YangMillsBlueprint.Certificates.PolydiskContractionCert
  , ``YangMillsBlueprint.Certificates.SU3AdjointModeVec
  , ``YangMillsBlueprint.Certificates.ZeroModeStiffnessCert
  , ``YangMillsBlueprint.Certificates.SpiralTwistCert
  , ``YangMillsBlueprint.Certificates.LuscherQuantumGapCert
  , ``YangMillsBlueprint.Certificates.CenterlessGroupRigidityCert
  , ``YangMillsBlueprint.Certificates.VortexAreaScreeningCert
  , ``YangMillsBlueprint.Certificates.AsymptoticFreedomCert
  , ``YangMillsBlueprint.Certificates.RealMassGapSpecCert
  , ``YangMillsBlueprint.Certificates.TEKFourPlaneCert
  , ``YangMillsBlueprint.Certificates.ExceptionalE8RigidityCert
  , ``YangMillsBlueprint.Certificates.ClassicalExceptionalCartanCert
  , ``YangMillsBlueprint.Certificates.LeviStratumCert
  , ``YangMillsBlueprint.Certificates.CrossoverBootstrapCert
  , ``YangMillsBlueprint.Certificates.BCDClassicalCartanCert
  , ``YangMillsBlueprint.Certificates.TreeGaugeBrascampLiebCert
  , ``YangMillsBlueprint.Certificates.VortexRGPersistenceCert
  , ``YangMillsBlueprint.Certificates.OSReconstructionCert
  , ``YangMillsBlueprint.Certificates.NonTrivialityWitnessCert
  , ``YangMillsBlueprint.Certificates.ClayBoundaryMasterBundle
  , ``YangMillsBlueprint.Certificates.DobrushinMixingBridgeCert
  , ``YangMillsBlueprint.Certificates.InductiveVortexRGCert
  , ``YangMillsBlueprint.Certificates.SpatialBlockRPCert
  , ``YangMillsBlueprint.Certificates.SymanzikContinuumCert
  , ``YangMillsBlueprint.Certificates.ContinuumOPEWitnessCert
  , ``YangMillsBlueprint.Certificates.TomboulisRougheningCert
  , ``YangMillsBlueprint.Certificates.ContinuumTightnessCert
  , ``YangMillsBlueprint.Certificates.CenterlessGroupGapCert
  , ``YangMillsBlueprint.Certificates.FILSChessboardCert
  , ``YangMillsBlueprint.Certificates.ThickVortexSpreadingCert
  , ``YangMillsBlueprint.Certificates.GaugeInvariantCosetCert
  , ``YangMillsBlueprint.Certificates.BianchiCubeDefectCert
  , ``YangMillsBlueprint.Certificates.SliceTransferGapCert
  , ``YangMillsBlueprint.Certificates.GeneralGroupBianchiCert
  , ``YangMillsBlueprint.Certificates.StokesBianchiDispersionCert
  , ``YangMillsBlueprint.Certificates.SliceTensorGapCert
  , ``YangMillsBlueprint.Certificates.BianchiScreenedVarianceCert
  , ``YangMillsBlueprint.Certificates.CoarseSliceDobrushinCert
  , ``YangMillsBlueprint.Certificates.BianchiDyadicAccumulationCert
  , ``YangMillsBlueprint.Certificates.BianchiCocycleCert
  , ``YangMillsBlueprint.Certificates.CentralizerCodimensionCert
  , ``YangMillsBlueprint.Certificates.DensityCapVarianceCert
  , ``YangMillsBlueprint.Certificates.IsotropicSuperblockCert
  , ``YangMillsBlueprint.Certificates.SchurPartialTraceCert
  , ``YangMillsBlueprint.Certificates.BlockSchurHierarchyCert
  , ``YangMillsBlueprint.Certificates.SimpleGroupUniformCert
  , ``YangMillsBlueprint.Certificates.LatticeHaarGibbsCert
  , ``YangMillsBlueprint.Certificates.SliceReflectionHilbertCert
  , ``YangMillsBlueprint.Certificates.BlueprintClayInterfaceCert
  , ``YangMillsBlueprint.Certificates.WilsonSingleLinkCert
  , ``YangMillsBlueprint.Certificates.RigidChordCert
  , ``YangMillsBlueprint.Certificates.TreeFrameGaugeCert
  , ``YangMillsBlueprint.Certificates.BlockPolymerOscCert
  , ``YangMillsBlueprint.Certificates.SelfDualWaveCert
  , ``YangMillsBlueprint.Certificates.RigidTransferSynthesisCert
  , ``YangMillsBlueprint.Certificates.PerturbedBlockSchurCert
  , ``YangMillsBlueprint.Certificates.ConcreteHodgeCert
  , ``YangMillsBlueprint.Certificates.LatticeRPCert
  , ``YangMillsBlueprint.Certificates.LorentzianMetricCert
  , ``YangMillsBlueprint.Certificates.LorentzianHodgeCert
  , ``YangMillsBlueprint.Certificates.WickMassShellCert
  , ``YangMillsBlueprint.Certificates.BalabanCollarCert
  , ``YangMillsBlueprint.Certificates.ConditionalFiberCert
  , ``YangMillsBlueprint.Certificates.NonCriticalSlabCert
  , ``YangMillsBlueprint.Certificates.ContinuumOSLimitCert
  , ``YangMillsBlueprint.Certificates.LocalizedUrsellCert
  , ``YangMillsBlueprint.Certificates.CenterlessCasimirCert
  , ``YangMillsBlueprint.Certificates.QuaternionicOSCert
  , ``YangMillsBlueprint.Certificates.SpinorWickCert
  , ``YangMillsBlueprint.Certificates.AbstractPolymerCert
  , ``YangMillsBlueprint.Certificates.MultiscaleBalabanCert
  , ``YangMillsBlueprint.Certificates.MeasureBathtubCert
  , ``YangMillsBlueprint.Certificates.Stage2ABasinCert
  , ``YangMillsBlueprint.Certificates.AbelianSubtractedSchurCert
  , ``YangMillsBlueprint.Certificates.TwoStepInductiveRGCert
  , ``YangMillsBlueprint.Certificates.InductiveRgRemainderCert
  , ``YangMillsBlueprint.Certificates.SpectralGribovCert
  , ``YangMillsBlueprint.Certificates.ContinuumRGBridgeCert
  , ``YangMillsBlueprint.Certificates.UnifiedMasterBridgeCert
  , ``YangMillsBlueprint.Certificates.ClayBoundaryContinuumCert
  ]

private def auditSingleTheorem (declName : Name) : MetaM Unit := do
  let env ← getEnv
  let some info := env.find? declName
    | throwError "VerifyNoTraps: missing declaration `{declName}`"
  match info with
  | .opaqueInfo _ =>
    throwError "VerifyNoTraps: `{declName}` is marked opaque"
  | .axiomInfo _ =>
    throwError "VerifyNoTraps: `{declName}` is a raw axiom"
  | _ => pure ()
  let usedAxioms ← collectAxioms declName
  for ax in usedAxioms do
    unless allowedAxioms.contains ax do
      throwError "VerifyNoTraps: `{declName}` uses forbidden axiom `{ax}`"
  if let some val := info.value? then
    let foundForbidden := val.foldConsts ([] : List Name) fun c acc =>
      if forbiddenConsts.contains c && !acc.contains c then c :: acc else acc
    unless foundForbidden.isEmpty do
      throwError "VerifyNoTraps: `{declName}` contains forbidden constants {foundForbidden}"
  forallTelescopeReducing info.type fun xs body => do
    let bodyWhnf ← whnf body
    if bodyWhnf.isConstOf ``True then
      throwError "VerifyNoTraps: `{declName}` conclusion reduces to `True`"
    for x in xs do
      let xType ← inferType x
      if ← isDefEq xType body then
        throwError "VerifyNoTraps: `{declName}` conclusion is defeq to hypothesis (tautology)"

private def auditNonemptyInstance (structName : Name) : MetaM Unit := do
  let target ← mkAppM ``Nonempty #[mkConst structName]
  let _ ← synthInstance target

#eval show CommandElabM Unit from liftTermElabM do
  for declName in auditedTheorems do
    auditSingleTheorem declName
  for structName in requiredNonemptyStructs do
    auditNonemptyInstance structName

-- Backward-compatible unconditional type bindings for regression test suite
theorem check_schur_identity_unconditional :
    (∀ a_bb a_cb a_cc z_b z_c : Int,
      MathlibPR.LinearAlgebra.twoBlockSchurDet a_bb a_cb a_cc * (z_c * z_c) +
          (a_bb * z_b - a_cb * z_c) * (a_bb * z_b - a_cb * z_c) =
        a_bb * MathlibPR.LinearAlgebra.twoBlockQuadForm a_bb a_cb a_cc z_b z_c) :=
  MathlibPR.LinearAlgebra.schur_complement_quadratic_identity

theorem check_schur_coercivity_unconditional :
    (∀ a_bb a_cb a_cc z_b z_c : Int,
      0 < a_bb →
      0 < MathlibPR.LinearAlgebra.twoBlockSchurDet a_bb a_cb a_cc →
      (z_b ≠ 0 ∨ z_c ≠ 0) →
      0 < MathlibPR.LinearAlgebra.twoBlockQuadForm a_bb a_cb a_cc z_b z_c) :=
  MathlibPR.LinearAlgebra.schur_coercivity_from_block_pivots

theorem check_poincare_block_identity_unconditional :
    (∀ x1 x2 : Int, x1 + x2 = 0 → (x1 - x2) * (x1 - x2) = 2 * (x1 * x1 + x2 * x2)) :=
  MathlibPR.LinearAlgebra.two_point_zero_sum_sq_diff_eq

theorem check_geometric_cluster_weight_unconditional :
    MathlibPR.Data.RationalPairs.RatPair.lt
      MathlibPR.Data.RationalPairs.totalGeometricClusterWeight
      (MathlibPR.Data.RationalPairs.RatPair.ofNat 1) :=
  MathlibPR.Data.RationalPairs.geometric_cluster_weight_lt_one

theorem check_geometric_margin_unconditional :
    MathlibPR.Data.RationalPairs.RatPair.lt
      ⟨1, 57, by omega⟩
      MathlibPR.Data.RationalPairs.geometricContractionMargin :=
  MathlibPR.Data.RationalPairs.geometric_contraction_margin_gt_one_57th

theorem check_cubic_collar_bound_unconditional :
    MathlibPR.CubicCollar.RatPair.lt
      MathlibPR.CubicCollar.cubicCollarEval
      MathlibPR.CubicCollar.collarReferenceMargin :=
  MathlibPR.CubicCollar.cubic_collar_eval_lt_target_margin

theorem check_quat_centralizer_rigidity_unconditional :
    (∀ b c d : Int,
      -2 * d = 0 → 2 * c = 0 → 2 * d = 0 → -2 * b = 0 →
      b = 0 ∧ c = 0 ∧ d = 0) :=
  MathlibPR.QuaternionAlgebra.quat_imag_comm_i_j_trivial

theorem check_quat_adjoint_spectral_gap_unconditional :
    (∀ b c d : Int,
      4 * (b * b + c * c + d * d) ≤
        -2 * d * (-2 * d) + 2 * c * (2 * c) + 2 * d * (2 * d) + -2 * b * (-2 * b)) :=
  MathlibPR.QuaternionAlgebra.quat_imag_ad_spectral_gap

theorem check_mode_pair_norm_sq_unconditional :
    (∀ m1 m2 : Int, m1 ≠ 0 ∨ m2 ≠ 0 → 1 ≤ m1 * m1 + m2 * m2) :=
  MathlibPR.ClockShiftAlgebra.mode_pair_norm_sq_pos

theorem check_su3_twisted_eigenvalue_table_min_unconditional :
    (∀ m1 m2 : Int, m1 ≠ 0 ∨ m2 ≠ 0 → 3 ≤ 3 * (m1 * m1) + 3 * (m2 * m2)) :=
  MathlibPR.ClockShiftAlgebra.su3_twisted_eigenvalue_table_min

theorem check_su3_cyclotomic_norm_sq_eval_unconditional :
    MathlibPR.ClockShiftAlgebra.RatPair.eqv
      (MathlibPR.ClockShiftAlgebra.RatPair.add
        MathlibPR.ClockShiftAlgebra.cyclotomicOrder3RealSq
        MathlibPR.ClockShiftAlgebra.cyclotomicOrder3ImagSq)
      MathlibPR.ClockShiftAlgebra.cyclotomicOrder3NormSq :=
  MathlibPR.ClockShiftAlgebra.su3_cyclotomic_norm_sq_eval

theorem check_jordan_spectral_gap_pos_unconditional :
    (∀ (N : Nat) (hN : 2 ≤ N),
      MathlibPR.ClockShiftAlgebra.RatPair.lt
        (MathlibPR.ClockShiftAlgebra.RatPair.ofNat 0)
        (MathlibPR.ClockShiftAlgebra.jordanBoundPair N hN)) :=
  MathlibPR.ClockShiftAlgebra.jordan_spectral_gap_pos

theorem check_secant_asymptotic_gap_pos_unconditional :
    (∀ (N : Nat) (hN : 6 ≤ N),
      MathlibPR.ClockShiftAlgebra.RatPair.lt
        (MathlibPR.ClockShiftAlgebra.RatPair.ofNat 0)
        (MathlibPR.ClockShiftAlgebra.secantBoundPair N hN)) :=
  MathlibPR.ClockShiftAlgebra.secant_asymptotic_gap_pos

theorem check_secant_asymptotic_gap_six_eval_unconditional :
    MathlibPR.ClockShiftAlgebra.RatPair.eqv
      (MathlibPR.ClockShiftAlgebra.secantBoundPair 6 (by omega))
      (MathlibPR.ClockShiftAlgebra.RatPair.ofNat 1) :=
  MathlibPR.ClockShiftAlgebra.secant_asymptotic_gap_six_eval

theorem check_su5_rational_gap_witness_unconditional :
    (5 : Nat) * (72 * 72) < 161 * 161 ∧ 5 * 72 - 161 = 199 :=
  MathlibPR.ClockShiftAlgebra.su5_rational_gap_witness

theorem check_su5_gap_gt_jordan_unconditional :
    MathlibPR.ClockShiftAlgebra.RatPair.lt
      (MathlibPR.ClockShiftAlgebra.jordanBoundPair 5 (by omega))
      MathlibPR.ClockShiftAlgebra.su5LowerBoundPair :=
  MathlibPR.ClockShiftAlgebra.su5_gap_gt_jordan

-- Verbatim kernel axiom footprints for real-analysis, calculus, matrix, and certificate theorems
#print axioms PolydiskMajorant.tsum_geometric_tail_le
#print axioms CubicSinBounds.sin_sq_le_sq
#print axioms CubicSinBounds.integral_sin_sq_le_cubic
#print axioms CubicSinBounds.normalized_sin_sq_integral_le_cubicCollarWeight
#print axioms QuaternionCentralizer.adjointTwistQuadraticForm_eq
#print axioms QuaternionCentralizer.adjointTwistQuadraticForm_ge_three
#print axioms ClockShiftMatrices.clock3_mul_shift3_eq
#print axioms ClockShiftMatrices.chord_normSq_eq_four_mul_sin_sq
#print axioms ClockShiftMatrices.mul_le_sin_of_mem_Icc
#print axioms ClockShiftMatrices.jordan_spectral_gap_le_four_mul_sin_sq
#print axioms ClockShiftMatrices.secant_spectral_gap_le_four_mul_sin_sq
#print axioms ClockShiftMatrices.four_mul_sin_pi_div_five_sq_eq
#print axioms ClockShiftMatrices.four_mul_sin_pi_div_five_sq_gt
#print axioms YangMillsBlueprint.Certificates.canonical_polymer_tsum_bound
#print axioms YangMillsBlueprint.Certificates.su2_real_weyl_collar_integral_lt_margin
#print axioms YangMillsBlueprint.Certificates.su3_clock_shift_commutation
#print axioms YangMillsBlueprint.Certificates.su5_real_spectral_gap_gt
#print axioms YangMillsBlueprint.Certificates.sun_real_jordan_gap_le
#print axioms YangMillsBlueprint.Certificates.sun_real_secant_gap_le
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.ZeroModeStiffnessCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.SpiralTwistCert)
#print axioms NonAbelianCommutatorStiffness.lagrange_identity
#print axioms NonAbelianCommutatorStiffness.cross_normSq_eq_of_ortho
#print axioms NonAbelianCommutatorStiffness.triadQuarticEnergy_ge_three_mul_sq
#print axioms CoprimeSpiralTwist.spiralMap_eq_zero_iff
#print axioms CoprimeSpiralTwist.spiral_both_coords_ne_zero
#print axioms CoprimeSpiralTwist.spiralMap_bijective
#print axioms CoprimeSpiralTwist.two_plane_gap_lower_bound
#print axioms YangMillsBlueprint.Certificates.su2_zero_mode_quartic_stiffness_pos_conditional
#print axioms YangMillsBlueprint.Certificates.canonical_zero_mode_energy_eq_three
#print axioms YangMillsBlueprint.Certificates.spiral_twist_both_planes_nonzero
#print axioms YangMillsBlueprint.Certificates.sun_coprime_spiral_two_plane_gap_le
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.LuscherQuantumGapCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.CenterlessGroupRigidityCert)
#print axioms QuarticQuantumStiffness.cubic_defect_factorization
#print axioms QuarticQuantumStiffness.variationalEnergy_sub_min_eq
#print axioms QuarticQuantumStiffness.three_mul_sq_le_variationalEnergy
#print axioms QuarticQuantumStiffness.variationalEnergy_pos
#print axioms CartanCoxeterRigidity.g2CartanDet_eq_one
#print axioms CartanCoxeterRigidity.two_mul_g2CartanForm_eq
#print axioms CartanCoxeterRigidity.six_mul_f4CartanForm_eq
#print axioms CartanCoxeterRigidity.g2CartanForm_eq_zero_iff
#print axioms CartanCoxeterRigidity.f4CartanForm_eq_zero_iff
#print axioms YangMillsBlueprint.Certificates.luscher_zero_mode_quantum_gap_ge_conditional
#print axioms YangMillsBlueprint.Certificates.canonical_luscher_quantum_gap_pos
#print axioms YangMillsBlueprint.Certificates.g2_coxeter_cartan_zero_mode_eliminated
#print axioms YangMillsBlueprint.Certificates.f4_coxeter_cartan_zero_mode_eliminated
#print axioms YangMillsBlueprint.Certificates.g2_unit_root_stiffness
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.VortexAreaScreeningCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.AsymptoticFreedomCert)
#print axioms ExponentialAreaScreening.cubic_div_twenty_seven_le_exp
#print axioms ExponentialAreaScreening.quartic_mul_exp_neg_sq_le
#print axioms AsymptoticFreedomFlow.inv_runningCoupling_eq
#print axioms AsymptoticFreedomFlow.runningCoupling_le_inv_mul
#print axioms AsymptoticFreedomFlow.telescoping_step_eq
#print axioms AsymptoticFreedomFlow.telescoped_sum_lt_one
#print axioms YangMillsBlueprint.Certificates.vortex_free_energy_defect_le_real
#print axioms YangMillsBlueprint.Certificates.canonical_vortex_defect_lt_one
#print axioms YangMillsBlueprint.Certificates.uv_running_coupling_contraction_conditional
#print axioms YangMillsBlueprint.Certificates.canonical_uv_coupling_lt_one
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.BCDClassicalCartanCert)
#print axioms BCDClassicalCartan.bCartanForm_eq_sum_sq
#print axioms BCDClassicalCartan.cCartanForm_eq_sum_sq
#print axioms BCDClassicalCartan.dCartanForm_eq_sum_sq
#print axioms BCDClassicalCartan.bCartanForm_nonneg
#print axioms BCDClassicalCartan.cCartanForm_nonneg
#print axioms BCDClassicalCartan.dCartanForm_nonneg
#print axioms BCDClassicalCartan.bCartanForm_eq_zero_iff
#print axioms BCDClassicalCartan.cCartanForm_eq_zero_iff
#print axioms BCDClassicalCartan.dCartanForm_eq_zero_iff
#print axioms BCDClassicalCartan.d4CartanForm_eq_zero_iff
#print axioms YangMillsBlueprint.Certificates.so_odd_bn_cartan_zero_mode_eliminated
#print axioms YangMillsBlueprint.Certificates.sp_cn_cartan_zero_mode_eliminated
#print axioms YangMillsBlueprint.Certificates.spin_dn_cartan_zero_mode_eliminated
#print axioms YangMillsBlueprint.Certificates.spin8_d4_cartan_zero_mode_eliminated
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.TreeGaugeBrascampLiebCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.VortexRGPersistenceCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.OSReconstructionCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.NonTrivialityWitnessCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.ClayBoundaryMasterBundle)
#print axioms CurvedBrascampLiebDefect.tree_gauge_dof_conservation
#print axioms CurvedBrascampLiebDefect.curvedVarianceBound_le_of_margin
#print axioms PeierlsRGContourFlow.lt_rgTensionStep_of_gt_critical
#print axioms OsterwalderSchraderBridge.clustering_extraction_le
#print axioms UrsellCumulantNonGaussian.ursellFour_ne_zero_of_subgaussian
#print axioms YangMillsBlueprint.Certificates.canonical_curved_brascamp_lieb_eval
#print axioms YangMillsBlueprint.Certificates.canonical_vortex_rg_persistence_eval
#print axioms YangMillsBlueprint.Certificates.canonical_os_correlator_envelope_le
#print axioms YangMillsBlueprint.Certificates.canonical_ursell_four_eval
#print axioms YangMillsBlueprint.Certificates.clay_millennium_boundary_master_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.DobrushinMixingBridgeCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.InductiveVortexRGCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.SpatialBlockRPCert)
#print axioms CurvedGroupLogSobolev.dobrushin_holley_stroock_pos
#print axioms InductivePeierlsRGBridge.rgTrajectory_ge_floor
#print axioms SpatialBlockRP.rpKernelForm_convex_comb_nonneg
#print axioms YangMillsBlueprint.Certificates.dobrushin_global_log_sobolev_gap_conditional
#print axioms YangMillsBlueprint.Certificates.inductive_peierls_tension_floor_conditional
#print axioms YangMillsBlueprint.Certificates.canonical_spatial_block_rp_nonneg
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.SymanzikContinuumCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.ContinuumOPEWitnessCert)
#print axioms SymanzikRotationalBound.symanzikBound_le_linear
#print axioms SymanzikRotationalBound.symanzikBound_lt_of_cutoff
#print axioms ShortDistanceOPEWitness.ne_zero_of_abs_ge_ope
#print axioms YangMillsBlueprint.Certificates.canonical_symanzik_rotational_lt_tenth
#print axioms YangMillsBlueprint.Certificates.continuum_ope_four_point_nontrivial_conditional
#print axioms YangMillsBlueprint.Certificates.canonical_ope_lower_pos
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.TomboulisRougheningCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.ContinuumTightnessCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.CenterlessGroupGapCert)
#print axioms TomboulisCharacterFlow.characterTrajectory_le_geom
#print axioms EquicontinuousTightnessBridge.clustering_limit_of_vanishing_cutoffs
#print axioms CenterlessWeylAlcoveGap.weylAlcoveCoerciveGap_pos
#print axioms YangMillsBlueprint.Certificates.tomboulis_character_flow_decays_conditional
#print axioms YangMillsBlueprint.Certificates.continuum_clustering_limit_conditional
#print axioms YangMillsBlueprint.Certificates.canonical_centerless_g2_combined_gap_pos
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.FILSChessboardCert)
#print axioms ChessboardHolderBound.chessboard_defect_le_of_pow
#print axioms ChessboardHolderBound.chessboard_cluster_suppression
#print axioms YangMillsBlueprint.Certificates.fils_chessboard_cluster_decay_conditional
#print axioms YangMillsBlueprint.Certificates.canonical_fils_chessboard_eval
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.ThickVortexSpreadingCert)
#print axioms VortexSpreadingBound.spreadTrigCost_le
#print axioms VortexSpreadingBound.spreadTrigCost_lt_of_cutoff
#print axioms YangMillsBlueprint.Certificates.thick_vortex_spread_cost_lt_conditional
#print axioms YangMillsBlueprint.Certificates.canonical_thick_vortex_w16_lt_tenth
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.GaugeInvariantCosetCert)
#print axioms CosetSignMagnitudeCreutz.creutzRatio_factorization
#print axioms CosetSignMagnitudeCreutz.creutzRatio_pos_of_sign_dominance
#print axioms YangMillsBlueprint.Certificates.gauge_invariant_coset_creutz_gap_conditional
#print axioms YangMillsBlueprint.Certificates.canonical_gauge_invariant_coset_creutz_pos
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.BianchiCubeDefectCert)
#print axioms NonAbelianBianchiDefect.transportDiffNormSq_eq
#print axioms NonAbelianBianchiDefect.unit_transportDiffNormSq_ge
#print axioms YangMillsBlueprint.Certificates.nonabelian_bianchi_transport_defect_pos
#print axioms YangMillsBlueprint.Certificates.canonical_bianchi_transport_defect_gt_one
#print axioms YangMillsBlueprint.Certificates.abelian_collinear_bianchi_defect_zero
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.SliceTransferGapCert)
#print axioms EffectiveMassTransferGap.spectralCorr_le_pow_mul_zero
#print axioms EffectiveMassTransferGap.spectralCorr_log_convex
#print axioms EffectiveMassTransferGap.effectiveMassRatio_mono
#print axioms YangMillsBlueprint.Certificates.slice_transfer_exponential_decay_conditional
#print axioms YangMillsBlueprint.Certificates.canonical_slice_glueball_t4_decay
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.GeneralGroupBianchiCert)
#print axioms AdjointBianchiNorm.frobSq_adjAction_sub_eq
#print axioms AdjointBianchiNorm.frobSq_adjAction_sub_zero_of_comm
#print axioms YangMillsBlueprint.Certificates.general_adjoint_bianchi_defect_pos
#print axioms YangMillsBlueprint.Certificates.canonical_so3_adjoint_bianchi_defect_gt_three
#print axioms YangMillsBlueprint.Certificates.canonical_cartan_commuting_bianchi_zero
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.StokesBianchiDispersionCert)
#print axioms StokesAdjointDispersion.frobInner_adjAction_self_mul_two
#print axioms StokesAdjointDispersion.frobSq_coulomb_dipole_noncancellation
#print axioms StokesAdjointDispersion.frobSq_exact_cancellation_eq_comm
#print axioms StokesAdjointDispersion.stokes_sum_frobSq_ge_of_bianchi_floor
#print axioms YangMillsBlueprint.Certificates.stokes_coulomb_dipole_broken_pos
#print axioms YangMillsBlueprint.Certificates.canonical_so3_dipole_broken_gt_three
#print axioms YangMillsBlueprint.Certificates.canonical_cartan_dipole_cancels_zero
#print axioms YangMillsBlueprint.Certificates.stokes_area_variance_persists_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.SliceTensorGapCert)
#print axioms SliceMarkovTensorization.schur_symmetric_operator_sq_le
#print axioms SliceMarkovTensorization.rayleigh_abs_le_of_schur
#print axioms SliceMarkovTensorization.slice_tensor_contraction_le
#print axioms YangMillsBlueprint.Certificates.slice_tensor_margin_pos
#print axioms YangMillsBlueprint.Certificates.canonical_slice_tensor_margin_gt_third
#print axioms YangMillsBlueprint.Certificates.slice_tensor_uniform_gap_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.BianchiScreenedVarianceCert)
#print axioms ScreenedDipoleVariance.screenedVarianceRatio_abelian_collapse
#print axioms ScreenedDipoleVariance.delta_le_screenedVarianceRatio
#print axioms ScreenedDipoleVariance.screenedVarianceRatio_pos_of_loss
#print axioms ScreenedDipoleVariance.screenedSurfaceVariance_ge_area_floor
#print axioms YangMillsBlueprint.Certificates.canonical_screened_ratio_nn_eq
#print axioms YangMillsBlueprint.Certificates.canonical_screened_ratio_full_eq
#print axioms YangMillsBlueprint.Certificates.screened_ratio_pos_of_cert
#print axioms YangMillsBlueprint.Certificates.bianchi_screened_area_law_variance_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.CoarseSliceDobrushinCert)
#print axioms CoarseSliceDecoherence.coarseSliceCoupling_zero
#print axioms CoarseSliceDecoherence.coarseSliceCoupling_anti_step
#print axioms CoarseSliceDecoherence.coarseSliceCoupling_le_margin
#print axioms YangMillsBlueprint.Certificates.canonical_coarse_slice_k3_eval
#print axioms YangMillsBlueprint.Certificates.coarse_slice_sq_margin_pos
#print axioms YangMillsBlueprint.Certificates.coarse_slice_dobrushin_gap_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.BianchiDyadicAccumulationCert)
#print axioms BianchiDyadicAccumulation.one_sub_dyadicLossStep
#print axioms BianchiDyadicAccumulation.one_sub_iteratedDyadicLoss_eq
#print axioms BianchiDyadicAccumulation.lt_dyadicLossStep_of_pos_of_lt_one
#print axioms BianchiDyadicAccumulation.dyadicLossStep_lt_one
#print axioms BianchiDyadicAccumulation.iteratedDyadicLoss_zero
#print axioms BianchiDyadicAccumulation.iteratedDyadicLoss_mem_Ioo
#print axioms YangMillsBlueprint.Certificates.canonical_dyadic_k1_eq
#print axioms YangMillsBlueprint.Certificates.canonical_dyadic_k2_eq
#print axioms YangMillsBlueprint.Certificates.canonical_dyadic_k2_gt_third
#print axioms YangMillsBlueprint.Certificates.abelian_dyadic_loss_zero
#print axioms YangMillsBlueprint.Certificates.dyadic_bianchi_step_amplifies
#print axioms YangMillsBlueprint.Certificates.dyadic_bianchi_saturation_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.BianchiCocycleCert)
#print axioms BianchiCocycleDecomposition.adjAction_mul
#print axioms BianchiCocycleDecomposition.adjDelta_mul
#print axioms BianchiCocycleDecomposition.frobSq_matrixComm_mul_eq
#print axioms BianchiCocycleDecomposition.cocycleLoss_split_eq
#print axioms BianchiCocycleDecomposition.dyadic_step_ge_of_remainder_bound
#print axioms YangMillsBlueprint.Certificates.so3RotZ345_orth1
#print axioms YangMillsBlueprint.Certificates.so3RotZ345_orth2
#print axioms YangMillsBlueprint.Certificates.canonical_cocycle_dV_eq
#print axioms YangMillsBlueprint.Certificates.canonical_cocycle_dVV_eq
#print axioms YangMillsBlueprint.Certificates.canonical_cocycle_eps_eq
#print axioms YangMillsBlueprint.Certificates.canonical_cocycle_superdyadic_lt
#print axioms YangMillsBlueprint.Certificates.cocycle_dyadic_lower_bound_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.CentralizerCodimensionCert)
#print axioms CentralizerCodimensionBound.so3OfQuat_orth_right
#print axioms CentralizerCodimensionBound.frobSq_so3OfQuat_comm_axisZ
#print axioms CentralizerCodimensionBound.transverse_sq_le_of_comm_le
#print axioms CentralizerCodimensionBound.bathtub_expectation_floor
#print axioms CentralizerCodimensionBound.bathtub_integral_eval
#print axioms YangMillsBlueprint.Certificates.canonical_transverse_quat_comm_eq
#print axioms YangMillsBlueprint.Certificates.cartan_quat_comm_zero
#print axioms YangMillsBlueprint.Certificates.canonical_bathtub_m4_eval
#print axioms YangMillsBlueprint.Certificates.centralizer_bathtub_floor_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.DensityCapVarianceCert)
#print axioms GibbsDensityCapVariance.gibbsRatio_le_bound
#print axioms GibbsDensityCapVariance.exp_neg_ratio_eq_exp_sub
#print axioms GibbsDensityCapVariance.four_div_exp_eq_four_mul_exp_neg
#print axioms GibbsDensityCapVariance.variance_floor_of_bounded_osc
#print axioms YangMillsBlueprint.Certificates.canonical_density_cap_le
#print axioms YangMillsBlueprint.Certificates.canonical_variance_floor_half
#print axioms YangMillsBlueprint.Certificates.crossover_variance_floor_of_bounded_osc_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.IsotropicSuperblockCert)
#print axioms IsotropicSuperblockDobrushin.total_div_in_eq_superblockM0
#print axioms IsotropicSuperblockDobrushin.superblockM0_le_of_leakage_ratio
#print axioms IsotropicSuperblockDobrushin.superblockM0_nonneg
#print axioms IsotropicSuperblockDobrushin.superblock_coupling_le_margin
#print axioms YangMillsBlueprint.Certificates.canonical_superblock_m0_eq
#print axioms YangMillsBlueprint.Certificates.canonical_superblock_coupling_eval
#print axioms YangMillsBlueprint.Certificates.canonical_superblock_coupling_lt_third
#print axioms YangMillsBlueprint.Certificates.superblock_uniform_gap_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.SchurPartialTraceCert)
#print axioms SchurPartialTraceContraction.schur_complete_sq
#print axioms SchurPartialTraceContraction.schur_three_slice_complete_sq
#print axioms SchurPartialTraceContraction.one_sub_schurPrecisionCoupling_eq
#print axioms SchurPartialTraceContraction.schurEff_pos
#print axioms SchurPartialTraceContraction.schurPrecisionCoupling_lt
#print axioms SchurPartialTraceContraction.schurPrecisionCoupling_pos
#print axioms SchurPartialTraceContraction.one_sub_schurPrecisionCoupling_pos
#print axioms YangMillsBlueprint.Certificates.canonical_schur_one_step_eq
#print axioms YangMillsBlueprint.Certificates.canonical_schur_two_step_eq
#print axioms YangMillsBlueprint.Certificates.canonical_schur_monotone_lt
#print axioms YangMillsBlueprint.Certificates.schur_partial_trace_contraction_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.BlockSchurHierarchyCert)
#print axioms BlockSchurHierarchy.even_block_chain_complete_sq
#print axioms BlockSchurHierarchy.schur_chain_margin_eq
#print axioms BlockSchurHierarchy.blockRatio_renorm_eq
#print axioms BlockSchurHierarchy.blockRatioNext_lt_sq
#print axioms BlockSchurHierarchy.blockRatioNext_lt_self
#print axioms BlockSchurHierarchy.iteratedBlockRatio_mem_Ico
#print axioms BlockSchurHierarchy.blockChain_margin_monotone
#print axioms YangMillsBlueprint.Certificates.canonical_block_ratio_k1_eq
#print axioms YangMillsBlueprint.Certificates.canonical_block_ratio_k2_eq
#print axioms YangMillsBlueprint.Certificates.canonical_block_ratio_k2_lt_eighth
#print axioms YangMillsBlueprint.Certificates.canonical_margin_amplified
#print axioms YangMillsBlueprint.Certificates.block_hierarchy_gap_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.SimpleGroupUniformCert)
#print axioms SimpleGroupUniformClosure.transverseCodim_ge_two
#print axioms SimpleGroupUniformClosure.codimNormalizedFloor_ge_base
#print axioms SimpleGroupUniformClosure.codimNormalizedFloor_pos
#print axioms SimpleGroupUniformClosure.uniform_superblock_ratio_lt_one
#print axioms SimpleGroupUniformClosure.uniform_block_schur_gap_pos
#print axioms YangMillsBlueprint.Certificates.canonical_so3_codim_floor_eq
#print axioms YangMillsBlueprint.Certificates.canonical_g2_codim_floor_eq
#print axioms YangMillsBlueprint.Certificates.canonical_f4_codim_floor_eq
#print axioms YangMillsBlueprint.Certificates.canonical_e8_codim_floor_eq
#print axioms YangMillsBlueprint.Certificates.canonical_exceptional_floor_monotone
#print axioms YangMillsBlueprint.Certificates.simple_group_uniform_gap_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.LatticeHaarGibbsCert)
#print axioms LatticeHaarGibbs.partitionIntegral_ge_exp_neg_max
#print axioms LatticeHaarGibbs.partitionIntegral_le_exp_neg_min
#print axioms LatticeHaarGibbs.partitionIntegral_pos
#print axioms LatticeHaarGibbs.weightedExpectation_const
#print axioms LatticeHaarGibbs.boltzmannDensity_le_exp_osc
#print axioms LatticeHaarGibbs.weightedExpectation_ge_exp_neg_osc_mul_integral
#print axioms LatticeHaarGibbs.productHaar_partitionIntegral_pos
#print axioms LatticeHaarGibbs.productHaar_density_le_exp_osc
#print axioms LatticeHaarGibbs.productHaar_expectation_ge_exp_neg_osc
#print axioms YangMillsBlueprint.Certificates.canonical_haar_osc_density_cap_eq
#print axioms YangMillsBlueprint.Certificates.canonical_haar_exp_floor_eq
#print axioms YangMillsBlueprint.Certificates.lattice_haar_gibbs_variance_floor_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.SliceReflectionHilbertCert)
#print axioms SliceReflectionHilbert.osEmbed_inner
#print axioms SliceReflectionHilbert.osEmbed_norm_sq
#print axioms SliceReflectionHilbert.osEmbed_eq_zero_of_null
#print axioms SliceReflectionHilbert.transfer_preserves_orth
#print axioms SliceReflectionHilbert.transfer_pow_preserves_orth
#print axioms SliceReflectionHilbert.transfer_pow_norm_le
#print axioms SliceReflectionHilbert.transfer_correlator_exp_decay
#print axioms SliceReflectionHilbert.transfer_to_coercivity
#print axioms YangMillsBlueprint.Certificates.canonical_transfer_gap_eq
#print axioms YangMillsBlueprint.Certificates.canonical_transfer_log_gap_eq
#print axioms YangMillsBlueprint.Certificates.slice_reflection_hilbert_gap_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.BlueprintClayInterfaceCert)
#print axioms YangMillsBlueprint.Certificates.canonical_clay_interface_witness_eval
#print axioms YangMillsBlueprint.Certificates.blueprint_clay_hilbert_interface_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.WilsonSingleLinkCert)
#print axioms WilsonPlaquetteAction.orth_mul_orth
#print axioms WilsonPlaquetteAction.plaquette_trace_gauge_invariant
#print axioms WilsonPlaquetteAction.frobSq_sub_one_eq_of_orth
#print axioms WilsonPlaquetteAction.frobSq_add_one_eq_of_orth
#print axioms WilsonPlaquetteAction.orth_trace_bounds
#print axioms WilsonPlaquetteAction.plaquetteCost_mem_Icc
#print axioms WilsonPlaquetteAction.stapleAction_mem_Icc
#print axioms WilsonPlaquetteAction.singleLink_conditional_density_cap
#print axioms WilsonPlaquetteAction.singleLink_conditional_variance_floor
#print axioms YangMillsBlueprint.Certificates.canonical_4d_staple_osc_eq
#print axioms YangMillsBlueprint.Certificates.wilson_4d_single_link_unconditional
#print axioms YangMillsBlueprint.Certificates.wilson_crossover_continuum_gap_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.RigidChordCert)
#print axioms RigidChordAction.orth_left_mul_orth
#print axioms RigidChordAction.neg_one_orth
#print axioms RigidChordAction.frobSq_add_frobSq_sub
#print axioms RigidChordAction.frobSq_conj_sub_one
#print axioms RigidChordAction.mul_sub_one_eq
#print axioms RigidChordAction.frobSq_add_le_two_mul
#print axioms RigidChordAction.frobSq_mul_sub_one_le
#print axioms RigidChordAction.frobSq_plaquette_le_four_sum
#print axioms RigidChordAction.plaquetteCost_eq_frobSq_div
#print axioms RigidChordAction.plaquetteCost_one_eq_zero
#print axioms RigidChordAction.plaquetteCost_neg_one_eq_two
#print axioms RigidChordAction.plaquetteCost_conj_invariant
#print axioms YangMillsBlueprint.Certificates.canonical_identity_and_antipodal_cost
#print axioms YangMillsBlueprint.Certificates.rigid_plaquette_cost_le_two_div_n_mul_link_chords
#print axioms YangMillsBlueprint.Certificates.rigid_small_field_plaquette_cap_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.TreeFrameGaugeCert)
#print axioms TreeFrameGaugeInvariance.gaugeTransform_one
#print axioms TreeFrameGaugeInvariance.gaugeTransform_comp
#print axioms TreeFrameGaugeInvariance.gaugeTransform_inv_left
#print axioms TreeFrameGaugeInvariance.gaugeTransform_inv_right
#print axioms TreeFrameGaugeInvariance.gaugeTransform_eq_one_of_tree_frame
#print axioms TreeFrameGaugeInvariance.closed_plaquette_gauge_conj
#print axioms TreeFrameGaugeInvariance.map_mul_right_compactHaarProb
#print axioms TreeFrameGaugeInvariance.measurePreserving_mul_left_compactHaarProb
#print axioms TreeFrameGaugeInvariance.measurePreserving_mul_right_compactHaarProb
#print axioms TreeFrameGaugeInvariance.measurePreserving_twoSided_compactHaarProb
#print axioms TreeFrameGaugeInvariance.measurePreserving_gaugeTransform
#print axioms TreeFrameGaugeInvariance.integrable_gaugeTransform_iff
#print axioms TreeFrameGaugeInvariance.integral_gaugeTransform
#print axioms TreeFrameGaugeInvariance.partitionIntegral_gaugeTransform
#print axioms TreeFrameGaugeInvariance.weightedExpectation_gaugeTransform
#print axioms TreeFrameGaugeInvariance.weightedExpectation_gauge_invariant
#print axioms YangMillsBlueprint.Certificates.canonical_tree_frame_floor_eq
#print axioms YangMillsBlueprint.Certificates.tree_frame_gauge_expectation_unconditional
#print axioms YangMillsBlueprint.Certificates.tree_frame_oscillation_floor_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.BlockPolymerOscCert)
#print axioms BlockPolymerOscillation.polymerTailBound_nonneg
#print axioms BlockPolymerOscillation.effectiveBlockOsc_nonneg
#print axioms BlockPolymerOscillation.finset_geom_tail_le_polymerTailBound
#print axioms BlockPolymerOscillation.block_action_mem_Icc_of_polymer_tail
#print axioms BlockPolymerOscillation.productHaar_polymer_density_cap
#print axioms BlockPolymerOscillation.productHaar_polymer_expectation_floor
#print axioms YangMillsBlueprint.Certificates.canonical_polymer_osc_eq
#print axioms YangMillsBlueprint.Certificates.block_polymer_oscillation_gibbs_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.SelfDualWaveCert)
#print axioms SelfDualWaveProjection.projPlus_add_projMinus
#print axioms SelfDualWaveProjection.projPlus_eigen
#print axioms SelfDualWaveProjection.projMinus_eigen
#print axioms SelfDualWaveProjection.projPlus_idem
#print axioms SelfDualWaveProjection.projMinus_idem
#print axioms SelfDualWaveProjection.projPlus_projMinus_zero
#print axioms SelfDualWaveProjection.inner_projPlus_projMinus
#print axioms SelfDualWaveProjection.norm_sq_eq_projPlus_add_projMinus
#print axioms SelfDualWaveProjection.inner_self_invol_eq_sub
#print axioms SelfDualWaveProjection.abs_inner_invol_le_norm_sq
#print axioms SelfDualWaveProjection.fourD_curvature_choose_split
#print axioms SelfDualWaveProjection.eightD_spinor_fourform_choose_split
#print axioms SelfDualWaveProjection.inner_projOrth_zero
#print axioms SelfDualWaveProjection.norm_unitProject
#print axioms SelfDualWaveProjection.inner_self_sphereGrad_zero
#print axioms SelfDualWaveProjection.norm_sq_unnormalized_step
#print axioms SelfDualWaveProjection.unnormalized_step_ne_zero
#print axioms SelfDualWaveProjection.norm_adaptedWaveStep
#print axioms SelfDualWaveProjection.adaptedWaveStep_preserves_orth
#print axioms SelfDualWaveProjection.rayleighEnergy_unitProject
#print axioms SelfDualWaveProjection.rayleigh_adaptedWaveStep_descent
#print axioms SelfDualWaveProjection.rayleigh_adaptedWaveStep_le
#print axioms SelfDualWaveProjection.adaptedWaveStep_transfer_descent_and_floor
#print axioms YangMillsBlueprint.Certificates.canonical_hodge_dimension_splits
#print axioms YangMillsBlueprint.Certificates.self_dual_bogomolnyi_unconditional
#print axioms YangMillsBlueprint.Certificates.projected_wave_adaptation_transfer_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.RigidTransferSynthesisCert)
#print axioms YangMillsBlueprint.Certificates.canonical_synthesis_witness_eval
#print axioms YangMillsBlueprint.Certificates.rigid_transfer_synthesis_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.PerturbedBlockSchurCert)
#print axioms YangMillsBlueprint.Certificates.canonical_perturbed_schur_eval
#print axioms YangMillsBlueprint.Certificates.perturbed_schur_tail_contraction_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.ConcreteHodgeCert)
#print axioms YangMillsBlueprint.Certificates.hodge4D_and_8D_unconditional
#print axioms YangMillsBlueprint.Certificates.hodge4D_8D_energy_bogomolnyi_unconditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.LatticeRPCert)
#print axioms YangMillsBlueprint.Certificates.wilson_finite_box_reflection_positivity_unconditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.LorentzianMetricCert)
#print axioms YangMillsBlueprint.Certificates.lorentzian_metric_and_boost_group_unconditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.LorentzianHodgeCert)
#print axioms YangMillsBlueprint.Certificates.lorentzian_hodge_complex_structure_unconditional
#print axioms YangMillsBlueprint.Certificates.lorentzian_energy_poynting_causality_unconditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.WickMassShellCert)
#print axioms YangMillsBlueprint.Certificates.wick_semigroup_mass_shell_unconditional
#print axioms YangMillsBlueprint.Certificates.wick_mass_shell_gap_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.BalabanCollarCert)
#print axioms YangMillsBlueprint.Certificates.balaban_fp_jacobian_and_kp_unconditional
#print axioms YangMillsBlueprint.Certificates.balaban_stage1_collar_gibbs_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.ConditionalFiberCert)
#print axioms YangMillsBlueprint.Certificates.canonical_fiber_tail_eval
#print axioms YangMillsBlueprint.Certificates.stage2a_conditional_fiber_density_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.NonCriticalSlabCert)
#print axioms YangMillsBlueprint.Certificates.powerLaw_fails_uniform_contraction_unconditional
#print axioms YangMillsBlueprint.Certificates.stage2b_noncritical_slab_dobrushin_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.ContinuumOSLimitCert)
#print axioms YangMillsBlueprint.Certificates.continuum_os0_os1_os3_os4_limit_preservation_unconditional
#print axioms YangMillsBlueprint.Certificates.continuum_schwinger_limit_bridge_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.LocalizedUrsellCert)
#print axioms YangMillsBlueprint.Certificates.localized_ursell_rules_out_gaussian_unconditional
#print axioms YangMillsBlueprint.Certificates.continuum_localized_nontriviality_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.CenterlessCasimirCert)
#print axioms YangMillsBlueprint.Certificates.all_simple_lie_invariants_unconditional
#print axioms YangMillsBlueprint.Certificates.universal_simple_group_mass_shell_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.QuaternionicOSCert)
#print axioms YangMillsBlueprint.Certificates.quaternionic_spin4_os_swap_unconditional
#print axioms YangMillsBlueprint.Certificates.os_chiral_hodge_lorentz_unification_unconditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.SpinorWickCert)
#print axioms YangMillsBlueprint.Certificates.spinor_hermitian_wick_double_cover_unconditional
#print axioms YangMillsBlueprint.Certificates.spinor_mass_shell_os_gap_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.AbstractPolymerCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.MultiscaleBalabanCert)
#print axioms YangMillsBlueprint.Certificates.abstract_polymer_kp_collar_decoupling_unconditional
#print axioms YangMillsBlueprint.Certificates.stage1_polymer_gas_gibbs_decoupling_conditional
#print axioms YangMillsBlueprint.Certificates.multiscale_balaban_summability_vs_harmonic_unconditional
#print axioms YangMillsBlueprint.Certificates.balaban_multiscale_stage1_bridge_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.MeasureBathtubCert)
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.Stage2ABasinCert)
#print axioms YangMillsBlueprint.Certificates.measure_bathtub_sharp_and_codim_d_unconditional
#print axioms YangMillsBlueprint.Certificates.stage2a_fiber_measure_bathtub_conditional
#print axioms YangMillsBlueprint.Certificates.stage2a_cocycle_and_schur_thresholds_unconditional
#print axioms YangMillsBlueprint.Certificates.stage2a_full_crossover_basin_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.AbelianSubtractedSchurCert)
#print axioms YangMillsBlueprint.Certificates.offdiag_polarization_trace_zero_unconditional
#print axioms YangMillsBlueprint.Certificates.paramagnetic_trace_sandwich_and_gribov_clearance_unconditional
#print axioms YangMillsBlueprint.Certificates.paramagnetic_dominance_negative_defect_unconditional
#print axioms YangMillsBlueprint.Certificates.cocycle_and_commutator_floor_unconditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.TwoStepInductiveRGCert)
#print axioms YangMillsBlueprint.Certificates.remainder_trap_invariant_unconditional
#print axioms YangMillsBlueprint.Certificates.strict_coupling_descent_step_unconditional
#print axioms YangMillsBlueprint.Certificates.inductive_rg_basin_entry_unconditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.InductiveRgRemainderCert)
#print axioms YangMillsBlueprint.Certificates.inductive_rg_remainder_uniform_bound_unconditional
#print axioms YangMillsBlueprint.Certificates.inductive_rg_strict_coupling_descent_unconditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.SpectralGribovCert)
#print axioms YangMillsBlueprint.Certificates.small_field_gribov_clearance_unconditional
#print axioms YangMillsBlueprint.Certificates.real_log_fourth_order_sandwich_unconditional
#print axioms YangMillsBlueprint.Certificates.trace_log_schur_sandwich_unconditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.ContinuumRGBridgeCert)
#print axioms YangMillsBlueprint.Certificates.large_field_small_field_gibbs_split_unconditional
#print axioms YangMillsBlueprint.Certificates.renormalized_cocycle_one_loop_descent_unconditional
#print axioms YangMillsBlueprint.Certificates.continuum_mass_gap_from_uniform_bridges_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.UnifiedMasterBridgeCert)
#print axioms YangMillsBlueprint.Certificates.peierls_exponential_threshold_unconditional
#print axioms YangMillsBlueprint.Certificates.master_uv_to_continuum_gap_conditional
#check (inferInstance : Nonempty YangMillsBlueprint.Certificates.ClayBoundaryContinuumCert)
#print axioms YangMillsBlueprint.Certificates.clay_hilbert_and_rg_crossover_synthesis_conditional

end YangMillsBlueprint.VerifyNoTraps
