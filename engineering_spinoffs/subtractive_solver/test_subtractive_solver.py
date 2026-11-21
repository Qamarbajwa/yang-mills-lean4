"""
Test Suite for Rosetta Subtractive Quotient Solver
Author: Qamar Munawer
Affiliation: Brandenburg University of Technology Cottbus-Senftenberg
Methodology: ai is being used as a tool
"""

import unittest
import numpy as np
import os
import sys
import json

sys.path.insert(0, os.path.dirname(__file__))

from rosetta_subtractive_solver import (
    SubtractiveQuotientSolver,
    generate_benchmark_illconditioned_system,
    run_solver_benchmark
)

class TestSubtractiveSolver(unittest.TestCase):
    def setUp(self):
        self.A, self.B, self.D, self.M_full, self.b_A, self.b_D = generate_benchmark_illconditioned_system(seed=99)
        self.solver = SubtractiveQuotientSolver(self.A, self.B, self.D)

    def test_condition_number_reduction(self):
        """Verify that the Schur quotient condition number is at least 1000x smaller than full matrix."""
        cond_M = np.linalg.cond(self.M_full)
        cond_S = self.solver.cond_S
        self.assertGreater(cond_M / cond_S, 1000.0, "Condition number must improve by at least 1000x.")

    def test_solution_accuracy(self):
        """Verify that the subtractive solver produces exact solutions matching full M."""
        x_A, x_D = self.solver.solve(self.b_A, self.b_D)
        x_full = np.concatenate([x_A, x_D])
        b_full = np.concatenate([self.b_A, self.b_D])
        res = np.linalg.norm(self.M_full @ x_full - b_full)
        self.assertLess(res, 1e-10, f"Residual {res} must be smaller than 1e-10.")

    def test_benchmark_receipt_generation(self):
        """Verify that run_solver_benchmark generates a valid PASS receipt."""
        receipt_path = "test_solver_receipt.json"
        try:
            res = run_solver_benchmark(receipt_path)
            self.assertEqual(res["performance"]["status"], "PASS")
            self.assertTrue(os.path.exists(receipt_path))
        finally:
            if os.path.exists(receipt_path):
                os.remove(receipt_path)

if __name__ == "__main__":
    unittest.main()
