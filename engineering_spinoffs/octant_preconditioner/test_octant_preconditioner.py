"""
Unit Test Suite for Rosetta 8-Octant Preconditioner
Author: Qamar Munawer
Affiliation: Brandenburg University of Technology Cottbus-Senftenberg
Methodology: ai is being used as a tool
"""

import unittest
import numpy as np
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from rosetta_octant_preconditioner import OctantPreconditioner, run_octant_benchmark

class TestOctantPreconditioner(unittest.TestCase):
    def setUp(self):
        self.n_dim = 64
        self.precond = OctantPreconditioner(self.n_dim)

    def test_partition_of_unity(self):
        """Verify that sum_{i=1}^8 P_i x == x for arbitrary random vectors."""
        x = np.random.randn(self.n_dim)
        recon = np.zeros(self.n_dim)
        for key in self.precond.projectors.keys():
            recon += self.precond.project_octant(x, *key)
        err = np.max(np.abs(recon - x))
        self.assertLess(err, 1e-12, "Partition of unity must reconstruct vector exactly.")

    def test_homochiral_fluid_filtering(self):
        """Verify that homochiral filtering removes exactly 25% of unweighted energy (2/8 octants)."""
        x = np.ones(self.n_dim)
        filtered = self.precond.filter_homochiral_fluid_modes(x)
        ratio = np.sum(filtered ** 2) / np.sum(x ** 2)
        self.assertAlmostEqual(ratio, 0.75, places=10, msg="Homochiral filter must retain exactly 6/8 = 75% energy.")

    def test_benchmark_receipt_generation(self):
        """Verify that run_octant_benchmark produces a valid PASS receipt."""
        receipt_path = "test_octant_receipt.json"
        try:
            res = run_octant_benchmark(receipt_path)
            self.assertEqual(res["status"], "PASS")
            self.assertTrue(os.path.exists(receipt_path))
        finally:
            if os.path.exists(receipt_path):
                os.remove(receipt_path)

if __name__ == "__main__":
    unittest.main()
