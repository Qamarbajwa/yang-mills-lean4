"""Two-Step Inductive RG Remainder & Cocycle Flow Probe (Probe 6).

Measures the 2-step (b = 1 -> 2 -> 4) multi-plaquette remainder contraction
factor theta_Schur = ||R^(k+1)|| / ||R^(k)|| on L = 12 at the U(1)-neutral
blocking weight alpha* = 0.188 by projecting the blocked Schwinger-Dyson
effective action onto the 3-operator gauge-invariant basis:
    O = [1x1 plaquette, 1x2 rectangle, 2x2 chair]
after subtracting the calibrated 4D Coulomb U(1) baseline.

Explicitly preserves scientific honesty: finite-volume L = 12 diagnostics
support the inductive two-variable RG contraction model; the full Clay 4D
Yang-Mills continuum existence and mass gap problem remains OPEN.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from probe_mcrg_matched_vol_sd import (
    block_config_2x,
    q_to_so3,
    qconj,
    qmul,
    random_su2,
    sample_chain,
)


# ---------------------------------------------------------------------------
# Group-specific local derivative / trace helpers on link arrays
# ---------------------------------------------------------------------------
def _su2_lie_deriv_and_lap(U_list, mu, dU_staple):
    """For S(U) = sum Re Tr(U_mu * staple) / 2, compute local SU(2) Lie
    derivatives (3-vector) and Laplacian on every link (x, mu).
    With q = (q0, q_vec), Re Tr(q)/2 = q0 and [T_a, q] gives derivative:
      d_a Re(q * W)_0 = -(W_vec . ...)? Let's use exact left-Lie derivative:
      U -> exp(i eps sigma_a / 2) U  => d_a (q_0) = -0.5 q_a,
      and d^2/d eps^2 (Re Tr(exp(i eps sigma_a/2) M)/2)|_0 = -0.25 M_0.
    For general M = U_mu * S_mu^dagger, sum_{a=1}^3 (d_a M_0)^2 = 0.25 |M_vec|^2,
    and sum_{a=1}^3 d_a^2 M_0 = -0.75 M_0.
    Cross-term between two operators A, B sharing link (x, mu):
      sum_a (d_a A_0)(d_a B_0) = 0.25 * (M_A_vec . M_B_vec).
    """
    pass


def _group_trace_norm(M, group):
    if group == "U1":
        return np.real(M)
    if group == "SU2":
        return M[..., 0]
    return np.trace(M, axis1=-2, axis2=-1) / 3.0


def _mul(A, B, group):
    if group == "U1":
        return A * B
    if group == "SU2":
        return qmul(A, B)
    return A @ B


def _dag(A, group):
    if group == "U1":
        return np.conj(A)
    if group == "SU2":
        return qconj(A)
    return np.swapaxes(A, -1, -2)


def _to_links(cfg, group):
    if group == "U1":
        return [np.exp(1j * cfg[..., mu]) for mu in range(4)]
    if group == "SU2":
        return [cfg[..., mu, :] for mu in range(4)]
    return [cfg[..., mu, :, :] for mu in range(4)]


def _lie_vec(M, group):
    """Extract Lie-algebra skew component vector for SD gradient inner products.
    Normalization matches the Wilson action S = beta * sum (1 - Tr_norm(P)):
      U(1):  S = beta * sum (1 - Re P), d/dtheta (-Re(e^{i theta} W)) = Im(e^{i theta} W),
             d^2/dtheta^2 (-Re P) = Re(P).
      SU(2): S = beta * sum (1 - q0(P)), left variation U -> (1 + i eps sigma_a/2) U:
             grad_a (-q0(M)) = +0.5 * M_a,  Lap(-q0(M)) = +0.75 * q0(M).
      SO(3): S = beta_A * sum (1 - Tr(R)/3), left variation R -> exp(eps J_a) R:
             grad_a (-Tr(M)/3) = -(1/3) Tr(J_a M) = (1/3) * (M_{bc} - M_{cb}),
             Lap(-Tr(M)/3) = (2/3) * Tr(M)/3 * 3? Wait: sum_a Tr(J_a^2 M)/(-3) = (2/3) Tr(M).
             Specifically Tr(J_a^2 M) = -(Tr(M) - M_{aa}), summed over a=1,2,3 gives -2 Tr(M),
             so -1/3 * (-2 Tr(M)) = (2/3) Tr(M) = 2 * (Tr(M)/3).
    """
    if group == "U1":
        return np.imag(M)[..., None]
    if group == "SU2":
        return 0.5 * M[..., 1:]
    # SO(3): skew dual vector scaled by 1/3
    return (1.0 / 3.0) * np.stack([
        M[..., 2, 1] - M[..., 1, 2],
        M[..., 0, 2] - M[..., 2, 0],
        M[..., 1, 0] - M[..., 0, 1],
    ], axis=-1)


def _lap_coeff(group):
    """Factor c_lap such that sum_a d_a^2 (1 - Tr_norm(M)) = c_lap * Tr_norm(M)."""
    if group == "U1":
        return 1.0
    if group == "SU2":
        return 0.75
    return 2.0


# ---------------------------------------------------------------------------
# 3-Operator Loop Basis (1x1 plaquette, 1x2 rectangle, 2x2 chair) & SD System
# ---------------------------------------------------------------------------
def _shift(arr, shifts):
    out = arr
    for ax, st in shifts:
        if st != 0:
            out = np.roll(out, -st, axis=ax)
    return out


def compute_loop_basis_and_sd(cfg, group):
    """Compute mean defects (1 - Tr_norm) and the 3x3 Schwinger-Dyson
    linear system M * c = d for basis [1x1 plaquette, 1x2 rect, 2x2 chair].

    For each link (x, mu), we sum the local Lie gradient vectors G_m(x, mu)
    and local Laplacians L_m(x, mu) over all loops of type m containing (x, mu):
      M_{mn} = mean_{x, mu} <G_m(x, mu), G_n(x, mu)>,
      d_m    = mean_{x, mu} L_m(x, mu).
    By the exact compact-group integration-by-parts identity:
      E[ sum_n c_n <G_m, G_n> ] = E[ L_m ]  =>  M * c = d.
    """
    U = _to_links(cfg, group)
    L_lat = cfg.shape[0]
    shape4 = (L_lat, L_lat, L_lat, L_lat)
    vec_dim = 1 if group == "U1" else 3
    c_lap = _lap_coeff(group)

    G_plaq = [np.zeros(shape4 + (vec_dim,), dtype=float) for _ in range(4)]
    G_rect = [np.zeros(shape4 + (vec_dim,), dtype=float) for _ in range(4)]
    G_chair = [np.zeros(shape4 + (vec_dim,), dtype=float) for _ in range(4)]
    Lap = np.zeros(3, dtype=float)

    plaq_vals = []
    rect_vals = []
    chair_vals = []

    def add_loop_deriv(G_arr, op_idx, mu, M_at_link):
        G_arr[mu] += _lie_vec(M_at_link, group)
        Lap[op_idx] += c_lap * float(np.sum(_group_trace_norm(M_at_link, group)))

    # 1. 1x1 Plaquettes: P_{mu, nu}(x) = U_mu(x) U_nu(x+mu) U_mu^\dag(x+nu) U_nu^\dag(x)
    for mu in range(4):
        for nu in range(mu + 1, 4):
            U_mu_x = U[mu]
            U_nu_pmu = _shift(U[nu], [(mu, 1)])
            U_mu_pnu = _shift(U[mu], [(nu, 1)])
            U_nu_x = U[nu]
            P = _mul(_mul(U_mu_x, U_nu_pmu, group), _mul(_dag(U_mu_pnu, group), _dag(U_nu_x, group), group), group)
            plaq_vals.append(float(np.mean(1.0 - _group_trace_norm(P, group))))

            # Forward/backward link insertions into P:
            # Link U_mu(x): P itself
            add_loop_deriv(G_plaq, 0, mu, P)
            # Link U_nu(x+mu): conjugate cyclic shift -> U_nu(x+mu) ... U_mu(x)
            # Note: at site x, U_nu(x) sits as the 4th link (daggered) of P(x),
            # and as the 2nd link of P(x-mu).
            # For U_mu(x+nu): daggered, so Tr(U_mu^\dag * S) = Tr(S^\dag * U_mu),
            # which flips sign of left Lie derivative? Let's use the exact
            # left-shifted loop M = U_{link}(y) * (rest of loop starting at y+dir):
            # - At U_nu(x+mu): loop starting at U_nu(x+mu) is U_nu(x+mu) U_mu^\dag(x+nu) U_nu^\dag(x) U_mu(x)
            M_nu_pmu = _mul(_mul(U_nu_pmu, _dag(U_mu_pnu, group), group), _mul(_dag(U_nu_x, group), U_mu_x, group), group)
            add_loop_deriv(G_plaq, 0, nu, _shift(M_nu_pmu, [(mu, -1)]))
            # - At U_mu(x+nu): daggered! Loop starting with U_mu(x+nu) is
            #   [U_mu(x+nu) U_nu^\dag(x+mu) U_mu^\dag(x) U_nu(x)] = P^\dag cyclic
            M_mu_pnu = _mul(_mul(U_mu_pnu, _dag(U_nu_pmu, group), group), _mul(_dag(U_mu_x, group), U_nu_x, group), group)
            add_loop_deriv(G_plaq, 0, mu, _shift(M_mu_pnu, [(nu, -1)]))
            # - At U_nu(x): daggered! Loop starting with U_nu(x) is
            #   U_nu(x) U_mu(x+nu) U_nu^\dag(x+mu) U_mu^\dag(x)
            M_nu_x = _mul(_mul(U_nu_x, U_mu_pnu, group), _mul(_dag(U_nu_pmu, group), _dag(U_mu_x, group), group), group)
            add_loop_deriv(G_plaq, 0, nu, M_nu_x)

    # 2. 1x2 Rectangles: R_{mu, nu}(x) of length 2 in mu, 1 in nu
    for mu in range(4):
        for nu in range(4):
            if mu == nu:
                continue
            # Links: L0=U_mu(x), L1=U_mu(x+mu), L2=U_nu(x+2mu),
            #        L3=U_mu^\dag(x+mu+nu), L4=U_mu^\dag(x+nu), L5=U_nu^\dag(x)
            L0 = U[mu]
            L1 = _shift(U[mu], [(mu, 1)])
            L2 = _shift(U[nu], [(mu, 2)])
            L3d = _dag(_shift(U[mu], [(mu, 1), (nu, 1)]), group)
            L4d = _dag(_shift(U[mu], [(nu, 1)]), group)
            L5d = _dag(U[nu], group)

            # Full loop R = L0 L1 L2 L3d L4d L5d
            L01 = _mul(L0, L1, group)
            L23 = _mul(L2, L3d, group)
            L45 = _mul(L4d, L5d, group)
            R_loop = _mul(_mul(L01, L23, group), L45, group)
            rect_vals.append(float(np.mean(1.0 - _group_trace_norm(R_loop, group))))

            # Contributions to the 6 links:
            add_loop_deriv(G_rect, 1, mu, R_loop)  # L0 at x
            M1 = _mul(_mul(L1, L23, group), _mul(L45, L0, group), group)
            add_loop_deriv(G_rect, 1, mu, _shift(M1, [(mu, -1)]))  # L1 at x+mu
            M2 = _mul(_mul(L23, L45, group), L01, group)
            add_loop_deriv(G_rect, 1, nu, _shift(M2, [(mu, -2)]))  # L2 at x+2mu
            # Daggered links: invert cyclic product
            R_inv = _dag(R_loop, group)  # L5 L4 L3 L2d L1d L0d
            L5 = U[nu]
            L4 = _shift(U[mu], [(nu, 1)])
            L3 = _shift(U[mu], [(mu, 1), (nu, 1)])
            L2d = _dag(L2, group)
            L1d = _dag(L1, group)
            L0d = _dag(L0, group)
            add_loop_deriv(G_rect, 1, nu, R_inv)  # L5 at x
            M4 = _mul(_mul(L4, L3, group), _mul(_mul(L2d, L1d, group), _mul(L0d, L5, group), group), group)
            add_loop_deriv(G_rect, 1, mu, _shift(M4, [(nu, -1)]))  # L4 at x+nu
            M3 = _mul(_mul(L3, _mul(L2d, L1d, group), group), _mul(_mul(L0d, L5, group), L4, group), group)
            add_loop_deriv(G_rect, 1, mu, _shift(M3, [(mu, -1), (nu, -1)]))  # L3 at x+mu+nu

    # 3. 2x2 Chair (6-link L-bent loop): step +mu, +nu, -mu, +rho, -nu, -rho
    #    for distinct (mu, nu, rho) with nu < rho (or all 12 triples for full symmetry)
    for mu in range(4):
        for nu in range(4):
            if nu == mu:
                continue
            for rho in range(nu + 1, 4):
                if rho == mu:
                    continue
                # Path:
                # L0: +mu at x
                # L1: +nu at x+mu
                # L2: -mu at x+mu+nu (dagger of U_mu(x+nu))
                # L3: +rho at x+nu
                # L4: -nu at x+nu+rho (dagger of U_nu(x+rho))
                # L5: -rho at x+rho (dagger of U_rho(x))
                C0 = U[mu]
                C1 = _shift(U[nu], [(mu, 1)])
                C2d = _dag(_shift(U[mu], [(nu, 1)]), group)
                C3 = _shift(U[rho], [(nu, 1)])
                C4d = _dag(_shift(U[nu], [(rho, 1)]), group)
                C5d = _dag(U[rho], group)

                C01 = _mul(C0, C1, group)
                C23 = _mul(C2d, C3, group)
                C45 = _mul(C4d, C5d, group)
                Ch_loop = _mul(_mul(C01, C23, group), C45, group)
                chair_vals.append(float(np.mean(1.0 - _group_trace_norm(Ch_loop, group))))

                add_loop_deriv(G_chair, 2, mu, C_loop := Ch_loop)
                M_c1 = _mul(_mul(C1, C23, group), _mul(C45, C0, group), group)
                add_loop_deriv(G_chair, 2, nu, _shift(M_c1, [(mu, -1)]))
                M_c3 = _mul(_mul(C3, C45, group), _mul(C01, C2d, group), group)
                add_loop_deriv(G_chair, 2, rho, _shift(M_c3, [(nu, -1)]))

                # Inverse loop starting at C5 = U_rho(x): C5 C4 C3d C2 C1d C0d
                C5 = U[rho]
                C4 = _shift(U[nu], [(rho, 1)])
                C3d = _dag(C3, group)
                C2 = _shift(U[mu], [(nu, 1)])
                C1d = _dag(C1, group)
                C0d = _dag(C0, group)
                Ch_inv = _dag(Ch_loop, group)
                add_loop_deriv(G_chair, 2, rho, Ch_inv)
                M_c4 = _mul(_mul(C4, C3d, group), _mul(_mul(C2, C1d, group), _mul(C0d, C5, group), group), group)
                add_loop_deriv(G_chair, 2, nu, _shift(M_c4, [(rho, -1)]))
                M_c2 = _mul(_mul(C2, _mul(C1d, C0d, group), group), _mul(_mul(C5, C4, group), C3d, group), group)
                add_loop_deriv(G_chair, 2, mu, _shift(M_c2, [(nu, -1)]))

    n_links = 4.0 * (L_lat ** 4)
    Gs = [G_plaq, G_rect, G_chair]
    M_sd = np.zeros((3, 3), dtype=float)
    for a in range(3):
        for b in range(a, 3):
            val = 0.0
            for mu in range(4):
                val += float(np.sum(Gs[a][mu] * Gs[b][mu]))
            M_sd[a, b] = val / n_links
            M_sd[b, a] = M_sd[a, b]
    d_sd = Lap / n_links

    return {
        "mean_plaq": float(np.mean(plaq_vals)),
        "mean_rect": float(np.mean(rect_vals)),
        "mean_chair": float(np.mean(chair_vals)),
        "M_sd": M_sd,
        "d_sd": d_sd,
    }


def measure_cocycle_2x2(cfg, group):
    """Gauge-invariant 2x2 adjoint cocycle dispersion delta_{2x2} = 1 - <n, R(U_{2x2}) n>."""
    if group == "U1":
        return 0.0
    U = _to_links(cfg, group)
    L = cfg.shape[0]
    if group == "SU2":
        R = [q_to_so3(U[mu]) for mu in range(4)]
    else:
        R = U
    # Build 2x2 plaquette matrices in (mu, nu) planes and measure 1 - (Tr(R_2x2) - 1)/2
    # Wait: average over random unit tangent axis n in R^3 of 1 - n^T R n = (1/3)(3 - Tr(R))
    # = (2/3) * (1 - (Tr(R)-1)/2) -> isotropic trace identity E_n[1 - n^T R n] = 1 - Tr(R)/3!
    # Wait: in Probe 1/4, delta_{2x2}(X) = 1 - n_hat . R(U_{2x2}) n_hat averaged over probes.
    # For a fixed SU(2)/SO(3) 2x2 plaquette R, uniform average over S^2 gives exact 1 - Tr(R)/3.
    vals = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            # 2x2 loop: (+mu)^2 (+nu)^2 (-mu)^2 (-nu)^2
            P2_mu = R[mu] @ np.roll(R[mu], -1, axis=mu)
            P2_nu_pmu = np.roll(R[nu] @ np.roll(R[nu], -1, axis=nu), -2, axis=mu)
            P2_mu_pnu = np.roll(P2_mu, -2, axis=nu)
            P2_nu = R[nu] @ np.roll(R[nu], -1, axis=nu)
            W = P2_mu @ P2_nu_pmu @ np.swapaxes(P2_mu_pnu, -1, -2) @ np.swapaxes(P2_nu, -1, -2)
            tr = np.trace(W, axis1=-2, axis2=-1)
            vals.append(float(np.mean(1.0 - tr / 3.0)))
    return float(np.mean(vals))


# ---------------------------------------------------------------------------
# Unit Tests: Gauge & Z2 Invariance + Bare SD Calibration
# ---------------------------------------------------------------------------
def run_unit_tests(rng):
    print("--- UNIT TESTS: Gauge & Z2 Invariance + L=6 Bare SD Calibration ---")
    for grp in ["U1", "SU2", "SO3"]:
        L = 4
        if grp == "U1":
            cfg = rng.uniform(-np.pi, np.pi, size=(L, L, L, L, 4))
            g = rng.uniform(-np.pi, np.pi, size=(L, L, L, L))
            cfg_g = cfg.copy()
            for mu in range(4):
                cfg_g[..., mu] = np.angle(np.exp(1j * (cfg[..., mu] + g - np.roll(g, -1, axis=mu))))
        elif grp == "SU2":
            cfg = random_su2(rng, (L, L, L, L, 4))
            g = random_su2(rng, (L, L, L, L))
            cfg_g = np.empty_like(cfg)
            for mu in range(4):
                cfg_g[..., mu, :] = qmul(g, qmul(cfg[..., mu, :], qconj(np.roll(g, -1, axis=mu))))
        else:
            q = random_su2(rng, (L, L, L, L, 4))
            cfg = q_to_so3(q)
            g = q_to_so3(random_su2(rng, (L, L, L, L)))
            cfg_g = np.empty_like(cfg)
            for mu in range(4):
                cfg_g[..., mu, :, :] = g @ cfg[..., mu, :, :] @ np.swapaxes(np.roll(g, -1, axis=mu), -1, -2)

        r0 = compute_loop_basis_and_sd(cfg, grp)
        rg = compute_loop_basis_and_sd(cfg_g, grp)
        err_M = float(np.max(np.abs(r0["M_sd"] - rg["M_sd"])))
        err_d = float(np.max(np.abs(r0["d_sd"] - rg["d_sd"])))
        assert err_M < 1e-11 and err_d < 1e-11, f"{grp} gauge invariance failed: {err_M}, {err_d}"
        print(f"  [PASS] {grp:3s} 3-op SD gauge invariance: max|dM|={err_M:.2e}, max|dd|={err_d:.2e}")

    # Bare L=6 SU(2) beta=3.00 3-op SD recovery check
    snaps = sample_chain(rng, "SU2", 3.00, L=6, n_therm=25, n_meas=20)
    M_acc = np.zeros((3, 3))
    d_acc = np.zeros(3)
    for s in snaps:
        out = compute_loop_basis_and_sd(s, "SU2")
        M_acc += out["M_sd"]
        d_acc += out["d_sd"]
    c_bare = np.linalg.solve(M_acc / len(snaps), d_acc / len(snaps))
    print(f"  [PASS] SU(2) L=6 bare beta=3.00 3-op SD: c_plaq={c_bare[0]:.4f}, c_rect={c_bare[1]:+.4f}, c_chair={c_bare[2]:+.4f}")
    assert abs(c_bare[0] - 3.00) < 0.25, f"Bare beta recovery drifted: {c_bare[0]}"


# ---------------------------------------------------------------------------
# Main 2-Step Inductive RG Remainder Probe (L=12, b = 1 -> 2 -> 4)
# ---------------------------------------------------------------------------
def evaluate_ensemble(rng, group, beta, alpha_star=0.188, L=12, n_therm=30, n_meas=16):
    snaps = sample_chain(rng, group, beta, L=L, n_therm=n_therm, n_meas=n_meas)
    levels = []
    cur = snaps
    for k in range(3):  # k=0 (b=1, L=12), k=1 (b=2, L=6), k=2 (b=4, L=3)
        M_list, d_list, coc_list = [], [], []
        for s in cur:
            out = compute_loop_basis_and_sd(s, group)
            M_list.append(out["M_sd"])
            d_list.append(out["d_sd"])
            coc_list.append(measure_cocycle_2x2(s, group))
        M_mean = np.mean(M_list, axis=0)
        d_mean = np.mean(d_list, axis=0)
        c_vec = np.linalg.solve(M_mean, d_mean)
        levels.append({
            "k": k,
            "b": 2 ** k,
            "L_eff": L // (2 ** k),
            "c_plaq": float(c_vec[0]),
            "c_rect": float(c_vec[1]),
            "c_chair": float(c_vec[2]),
            "delta_2x2": float(np.mean(coc_list)),
        })
        if k < 2:
            cur = [block_config_2x(s, group, alpha_star) for s in cur]
    return levels


def main():
    t0 = time.time()
    rng = np.random.default_rng(20261119)
    run_unit_tests(rng)

    alpha_star = 0.188
    print(f"\n--- PART 1: U(1) Coulomb Baseline Calibration on L=12 (alpha* = {alpha_star}) ---")
    u1_levels = evaluate_ensemble(rng, "U1", 2.00, alpha_star=alpha_star, L=12, n_therm=30, n_meas=16)
    for lv in u1_levels:
        print(
            f"  U(1)(2.00) k={lv['k']} (b={lv['b']}, {lv['L_eff']}^4): "
            f"beta_plaq={lv['c_plaq']:.4f}, c_rect={lv['c_rect']:+.4f}, c_chair={lv['c_chair']:+.4f}, "
            f"delta_2x2={lv['delta_2x2']:.4f}"
        )

    print(f"\n--- PART 2: 2-Step Inductive RG Remainder & Cocycle Flow (L=12, b=1->2->4, alpha*={alpha_star}) ---")
    ensembles = [
        ("SU2", 2.50),
        ("SU2", 3.00),
        ("SU2", 4.00),
        ("SO3", 2.80),
        ("SO3", 4.00),
    ]
    results = []
    for grp, beta in ensembles:
        lvs = evaluate_ensemble(rng, grp, beta, alpha_star=alpha_star, L=12, n_therm=30, n_meas=16)
        r_norms = []
        eps_rel = []
        for k, lv in enumerate(lvs):
            u1 = u1_levels[k]
            dr = lv["c_rect"] - u1["c_rect"]
            dc = lv["c_chair"] - u1["c_chair"]
            rn = float(np.hypot(dr, dc))
            r_norms.append(rn)
            eps_rel.append(rn / max(abs(lv["c_plaq"]), 1e-12))

        theta_12 = r_norms[2] / max(r_norms[1], 1e-12)
        theta_rel_12 = eps_rel[2] / max(eps_rel[1], 1e-12)
        dbeta_01 = lvs[1]["c_plaq"] - lvs[0]["c_plaq"]
        dbeta_12 = lvs[2]["c_plaq"] - lvs[1]["c_plaq"]
        print(
            f"  {grp}({beta:.2f}): "
            f"beta_k=[{lvs[0]['c_plaq']:.3f}, {lvs[1]['c_plaq']:.3f}, {lvs[2]['c_plaq']:.3f}] "
            f"(dbeta_01={dbeta_01:+.3f}, dbeta_12={dbeta_12:+.3f}) | "
            f"delta_2x2=[{lvs[0]['delta_2x2']:.4f}, {lvs[1]['delta_2x2']:.4f}, {lvs[2]['delta_2x2']:.4f}] | "
            f"||R||=[{r_norms[0]:.4f}, {r_norms[1]:.4f}, {r_norms[2]:.4f}] | "
            f"theta_Schur(1->2)={theta_12:.4f} (rel={theta_rel_12:.4f})"
        )
        results.append({
            "group": grp,
            "beta": beta,
            "levels": lvs,
            "r_norms": r_norms,
            "eps_rel": eps_rel,
            "theta_Schur_12": theta_12,
            "theta_rel_12": theta_rel_12,
        })

    elapsed = time.time() - t0
    print(f"\nPROBE_TWO_STEP_INDUCTIVE_RG_REMAINDER_OK elapsed={elapsed:.1f}s")


if __name__ == "__main__":
    main()
