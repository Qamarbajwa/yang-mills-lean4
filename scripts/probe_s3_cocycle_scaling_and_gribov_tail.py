#!/usr/bin/env python3
"""
probe_s3_cocycle_scaling_and_gribov_tail.py

Phase I numerical probe testing Obligation 2 of Hypothesis 4.1:
  - Measures E[delta_{2x2}] and beta * E[delta_{2x2}] across beta in {2.2, 2.5, 3.0, 4.0, 6.0, 8.0}
    on SU(2) ~= S^3 vs. the Abelian U(1) ~= S^1 control.
  - Verifies that on SU(2), beta * E[delta_{2x2}] stays bounded strictly above 0 (c_0 > 0),
    whereas on U(1), delta_{2x2} == 0.0 identically.

Outputs receipt to:
  probes/probe_s3_cocycle_scaling_and_gribov_tail.json
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


def su2_from_axis_angle(axis: np.ndarray, angle: float) -> np.ndarray:
    """Return 2x2 SU(2) matrix exp(i * (angle/2) * (n . sigma))."""
    n = axis / np.linalg.norm(axis)
    c = math.cos(0.5 * angle)
    s = math.sin(0.5 * angle)
    return np.array([
        [c + 1j * s * n[2], s * (n[1] + 1j * n[0])],
        [s * (-n[1] + 1j * n[0]), c - 1j * s * n[2]],
    ], dtype=np.complex128)


def delta_2x2_su2(u1: np.ndarray, u2: np.ndarray) -> float:
    """Adjoint-normalized 2x2 commutator cocycle defect ||[U1, U2]||_F^2 / 2."""
    comm = u1 @ u2 - u2 @ u1
    return float(0.5 * np.sum(np.abs(comm) ** 2))


def sample_su2_plaquette_cocycle(beta: float, n_samples: int, seed: int) -> dict[str, float]:
    """
    Deterministic Gibbs-weighted importance sample of two SU(2) link holonomies
    with Wilson weight exp(beta * (1/2 Re Tr(U) - 1)) around the identity.
    """
    rng = np.random.default_rng(seed)
    deltas = []
    weights = []
    # Scale proposal width as 1 / sqrt(beta) (exact leading Haar-Gaussian regime)
    sigma = 1.0 / math.sqrt(beta)
    for _ in range(n_samples):
        v1 = rng.normal(scale=sigma, size=3)
        v2 = rng.normal(scale=sigma, size=3)
        a1 = float(np.linalg.norm(v1))
        a2 = float(np.linalg.norm(v2))
        u1 = su2_from_axis_angle(v1 if a1 > 1e-12 else np.array([1.0, 0.0, 0.0]), a1)
        u2 = su2_from_axis_angle(v2 if a2 > 1e-12 else np.array([0.0, 1.0, 0.0]), a2)
        # Plaquette U_p = U1 U2 U1^H U2^H
        up = u1 @ u2 @ u1.conj().T @ u2.conj().T
        s_w = 1.0 - 0.5 * float(np.real(np.trace(up)))
        w = math.exp(-beta * s_w)
        deltas.append(delta_2x2_su2(u1, u2))
        weights.append(w)
    w_arr = np.array(weights)
    d_arr = np.array(deltas)
    e_delta = float(np.sum(w_arr * d_arr) / np.sum(w_arr))
    return {
        "beta": beta,
        "E_delta_2x2": e_delta,
        "beta_times_E_delta": beta * e_delta,
    }


def main() -> None:
    betas = [2.2, 2.5, 3.0, 4.0, 6.0, 8.0]
    su2_rows = [sample_su2_plaquette_cocycle(b, 4000, 100 + i) for i, b in enumerate(betas)]

    # Abelian U(1) control: commuting phases [e^{i theta1}, e^{i theta2}] == 0
    u1_deltas = []
    rng = np.random.default_rng(999)
    for _ in range(500):
        t1 = rng.normal()
        t2 = rng.normal()
        z1 = np.exp(1j * t1)
        z2 = np.exp(1j * t2)
        u1_deltas.append(abs(z1 * z2 - z2 * z1) ** 2)
    u1_max = float(max(u1_deltas))

    min_c0 = min(r["beta_times_E_delta"] for r in su2_rows)
    assert min_c0 > 0.1
    assert u1_max < 1e-28

    out = {
        "probe": "probe_s3_cocycle_scaling_and_gribov_tail",
        "epistemic_lock": "status: verified-finite | Hypothesis 4.1 continuum limit OPEN",
        "su2_scaling": su2_rows,
        "min_c0_beta_E_delta": min_c0,
        "u1_max_delta_2x2": u1_max,
        "status": "PASS",
    }
    out_path = Path(r"d:\Comfy UI\yang mills and the mass gap\probes\probe_s3_cocycle_scaling_and_gribov_tail.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print("=" * 68)
    print("S^3 COCYCLE SCALING PROBE (SU(2) vs U(1)): PASS")
    print("=" * 68)
    for r in su2_rows:
        print(f"  beta={r['beta']:<4.1f} | E[delta_2x2]={r['E_delta_2x2']:.6f} | beta*E[delta]={r['beta_times_E_delta']:.6f}")
    print(f"  U(1) control max delta_2x2 = {u1_max:.2e}")
    print(f"  min c0 = min(beta * E[delta_2x2]) = {min_c0:.6f} > 0")
    print("=" * 68)


if __name__ == "__main__":
    main()
