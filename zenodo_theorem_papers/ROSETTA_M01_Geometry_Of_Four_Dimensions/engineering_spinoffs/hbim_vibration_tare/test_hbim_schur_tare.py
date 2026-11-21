"""
Test Suite for HBIM Schur Vibration Tare
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

from hbim_schur_tare import (
    GuyanSchurCondensation,
    SubGapSpectralFilter,
    HBIMSensorProcessor,
    generate_historic_arch_vibration_data,
    run_hbim_benchmark
)

class TestHBIMSchurTare(unittest.TestCase):
    def setUp(self):
        self.A, self.B, self.D, self.x_A, self.x_D = generate_historic_arch_vibration_data(seed=123)
        self.condensation = GuyanSchurCondensation(self.A, self.B, self.D)
        self.spectral_filter = SubGapSpectralFilter(sampling_rate=100.0, cutoff_freq=5.0)
        self.processor = HBIMSensorProcessor(self.condensation, self.spectral_filter)

    def test_schur_complement_positive_definiteness(self):
        """Verify that condensed Schur complement matrix S = D - B^T A^-1 B is positive definite."""
        eigvals = np.linalg.eigvalsh(self.condensation.Schur)
        self.assertTrue(np.all(eigvals > 0), f"Schur eigenvalues must be positive: {eigvals}")

    def test_spatial_bulk_taring(self):
        """Verify that spatial Schur taring reduces the variance of x_D driven by x_A."""
        x_D_tared = self.condensation.tare_static(self.x_A, self.x_D)
        var_raw = np.var(self.x_D)
        var_tared = np.var(x_D_tared)
        self.assertLess(var_tared, var_raw * 0.1, "Spatial Schur tare should remove over 90% of bulk-driven variance.")

    def test_end_to_end_pipeline_and_crack_recovery(self):
        """Verify that micro-crack frequency at 18.5 Hz is accurately detected after taring."""
        results = self.processor.process_monitoring_data(self.x_A, self.x_D)
        clean = results["clean_signal"]
        
        # Spectral peak detection
        freqs = np.fft.rfftfreq(clean.shape[0], d=1.0/100.0)
        fft_mag = np.abs(np.fft.rfft(clean[:, 0]))
        peak_freq = freqs[np.argmax(fft_mag)]
        
        self.assertAlmostEqual(peak_freq, 18.5, delta=0.2, msg=f"Detected frequency {peak_freq} Hz deviates from 18.5 Hz.")
        self.assertGreater(results["noise_subtraction_percent"], 98.0, "Noise subtraction must exceed 98%.")

    def test_benchmark_receipt_generation(self):
        """Verify that run_hbim_benchmark produces a valid passing JSON receipt."""
        receipt_path = "test_receipt.json"
        try:
            receipt = run_hbim_benchmark(receipt_path)
            self.assertEqual(receipt["performance_metrics"]["status"], "PASS")
            self.assertTrue(os.path.exists(receipt_path))
        finally:
            if os.path.exists(receipt_path):
                os.remove(receipt_path)

if __name__ == "__main__":
    unittest.main()
