r"""Probe 4 (Schur & Abelian-Subtraction Bridge): Conditional 2^4-Block Dirichlet Schur
Decomposition and Relative Free-Energy Defect at alpha* = 0.188 (Repo 0f3f012 untouched).

Sign convention: F(U) := -ln Z(U) = +(1/2) Tr ln(H_diam + W_para).
Subtracting the calibrated Abelian Gaussian baseline at alpha* = 0.188:
  Delta F_nonAb = F_G - F_Abelian = Delta F_diam (> 0, screening) + F_para (< 0, anti-screening),
where the Test B Dirichlet cavity gap (lam_min(-D^2_Dir) >= 4.0) cancels in F_G - F_Ab0,
and the paramagnetic commutator Schur complement
  F_para = (1/2) Tr ln(I - 2 (-D^2)^{-1} ad(F)) = F_schur < 0
drives Stage 1 asymptotic freedom (Delta beta_2x < 0), while the interior 2x2 adjoint
cocycle contraction (1 - delta_2x2(X)) < 1 drives Stage 2B Gamma_{>=1}^{BLK} < 1.
"""

import math
import os
import sys
import time
import numpy as np

SCRATCH_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRATCH_DIR not in sys.path:
    sys.path.insert(0, SCRATCH_DIR)

from probe_mcrg_matched_vol_sd import (
    qmul,
    qconj,
    q_to_so3,
    u1_sweep,
    su2_sweep,
    so3_sweep,
    compute_beta_sd,
    measure_coarse_grid,
    summarize_coarse_ensemble,
    jackknife_ratio_diff,
)
from probe4_paramagnetic_hessian_2pow4 import (
    so3_dual_vec,
    ad_matrix_from_vec,
    block_config_2x,
    measure_coarse_delta_and_gamma,
)
from probe5_relative_fiber_defect_lemma import eval_fiber_defect


# ---------------------------------------------------------------------------
# 1. Exact Gauge-Invariant Embedded 2^4 Dirichlet Schur & 2x2 Cocycle Operators
# ---------------------------------------------------------------------------
def compute_clover_f_field(R_full):
    """Build exact gauge-covariant 4-leaf clover F_{mu,nu}(x) in so(3) across the L^4 lattice.
    Returns array of shape (L, L, L, L, 4, 4, 3) with exact F_{nu,mu} = -F_{mu,nu}.
    """
    L = R_full.shape[0]
    d = R_full.shape[-1]
    F_all = np.zeros((L, L, L, L, 4, 4, 3), dtype=float)
    if d == 1:
        return F_all

    Rl = [R_full[..., mu, :, :] for mu in range(4)]
    RlT = [np.swapaxes(r, -1, -2) for r in Rl]
    for mu in range(4):
        for nu in range(mu + 1, 4):
            p1 = Rl[mu] @ np.roll(Rl[nu], -1, axis=mu) @ np.roll(RlT[mu], -1, axis=nu) @ RlT[nu]
            p2 = (
                Rl[nu]
                @ np.roll(np.roll(RlT[mu], 1, axis=mu), -1, axis=nu)
                @ np.roll(RlT[nu], 1, axis=mu)
                @ np.roll(Rl[mu], 1, axis=mu)
            )
            p3 = (
                np.roll(RlT[mu], 1, axis=mu)
                @ np.roll(np.roll(RlT[nu], 1, axis=mu), 1, axis=nu)
                @ np.roll(np.roll(Rl[mu], 1, axis=mu), 1, axis=nu)
                @ np.roll(Rl[nu], 1, axis=nu)
            )
            p4 = (
                np.roll(RlT[nu], 1, axis=nu)
                @ np.roll(Rl[mu], 1, axis=nu)
                @ np.roll(np.roll(Rl[nu], 1, axis=nu), -1, axis=mu)
                @ RlT[mu]
            )
            F_mn = 0.25 * (so3_dual_vec(p1) + so3_dual_vec(p2) + so3_dual_vec(p3) + so3_dual_vec(p4))
            F_all[..., mu, nu, :] = F_mn
            F_all[..., nu, mu, :] = -F_mn
    return F_all


def build_dirichlet_2pow4_schur_ops(R_full, F_all=None, origin=(0, 0, 0, 0)):
    """Build embedded 2^4 Dirichlet covariant Laplacian (-D^2_Dir >= 4*I),
    H_diam = I_4 otimes (-D^2_Dir), and W_para = -2 ad(F) at a given origin on L^4.
    """
    L = R_full.shape[0]
    d = R_full.shape[-1]
    ox, oy, oz, ot = origin
    if F_all is None:
        F_all = compute_clover_f_field(R_full)

    def site_id(a, b, c, e):
        return a * 8 + b * 4 + c * 2 + e

    Lap = np.zeros((16 * d, 16 * d), dtype=float)
    Id = np.eye(d, dtype=float)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for e in range(2):
                    i = site_id(a, b, c, e)
                    Lap[i * d:(i + 1) * d, i * d:(i + 1) * d] += 8.0 * Id
                    coords = [a, b, c, e]
                    gx = ((ox + a) % L, (oy + b) % L, (oz + c) % L, (ot + e) % L)
                    for mu in range(4):
                        if coords[mu] == 0:
                            nc = list(coords)
                            nc[mu] = 1
                            j = site_id(*nc)
                            Rm = R_full[gx[0], gx[1], gx[2], gx[3], mu]
                            Lap[i * d:(i + 1) * d, j * d:(j + 1) * d] -= Rm
                            Lap[j * d:(j + 1) * d, i * d:(i + 1) * d] -= Rm.T

    H_diam = np.kron(np.eye(4, dtype=float), Lap)
    W_para = np.zeros((64 * d, 64 * d), dtype=float)
    if d == 3:
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for e in range(2):
                        i = site_id(a, b, c, e)
                        gx = ((ox + a) % L, (oy + b) % L, (oz + c) % L, (ot + e) % L)
                        for mu in range(4):
                            for nu in range(mu + 1, 4):
                                blk = -2.0 * ad_matrix_from_vec(F_all[gx[0], gx[1], gx[2], gx[3], mu, nu])
                                rm = (mu * 16 + i) * 3
                                rn = (nu * 16 + i) * 3
                                W_para[rm:rm + 3, rn:rn + 3] = blk
                                W_para[rn:rn + 3, rm:rm + 3] = blk.T
    return Lap, H_diam, W_para


def evaluate_2pow4_schur_observables(R_full, F_ab0_per_d, origins=((0, 0, 0, 0),)):
    """Evaluate Abelian-subtracted F_diam/d, paramagnetic Schur determinant F_para/d,
    exact polarization-block Schur complement check F_schur/d, Tr(K_para^2)/d, and min(1+K_para).
    """
    d = R_full.shape[-1]
    F_all = compute_clover_f_field(R_full)
    # Polarization partition: A = {mu in (0, 3)}, B = {mu in (1, 2)} (32d DOFs each)
    blk_sz = 16 * d
    idx_A = np.concatenate([np.arange(0, blk_sz), np.arange(3 * blk_sz, 4 * blk_sz)])
    idx_B = np.arange(blk_sz, 3 * blk_sz)

    dF_dias, F_paras, F_schurs, tr_k2s, min_lams, min_ipks = [], [], [], [], [], []
    n_unstable = 0
    for orig in origins:
        Lap, H_diam, W_para = build_dirichlet_2pow4_schur_ops(R_full, F_all=F_all, origin=orig)
        ev_lap = np.linalg.eigvalsh(Lap)
        min_lams.append(float(ev_lap[0]))
        F_dia_d = 2.0 * float(np.sum(np.log(ev_lap))) / float(d)
        dF_dia_d = F_dia_d - F_ab0_per_d

        if d == 1:
            dF_dias.append(dF_dia_d)
            F_paras.append(0.0)
            F_schurs.append(0.0)
            tr_k2s.append(0.0)
            min_ipks.append(1.0)
            continue

        ev_d, U_d = np.linalg.eigh(H_diam)
        inv_sqrt = (U_d * (1.0 / np.sqrt(ev_d))) @ U_d.T
        K_para = inv_sqrt @ W_para @ inv_sqrt
        K_para = 0.5 * (K_para + K_para.T)
        ev_k = np.linalg.eigvalsh(K_para)
        min_ipk = 1.0 + float(ev_k[0])
        min_ipks.append(min_ipk)
        tr_k2 = float(np.sum(ev_k ** 2)) / float(d)
        tr_k2s.append(tr_k2)
        dF_dias.append(dF_dia_d)

        if min_ipk <= 1e-12:
            n_unstable += 1
            continue
        F_para_d = 0.5 * float(np.sum(np.log(1.0 + ev_k))) / float(d)

        # Polarization-block Schur complement S_{B|A} = H_BB - W_AB^T H_AA^{-1} W_AB
        H_blk = H_diam + W_para
        H_AA = H_blk[np.ix_(idx_A, idx_A)]
        H_BB = H_blk[np.ix_(idx_B, idx_B)]
        W_AB = H_blk[np.ix_(idx_A, idx_B)]
        S_BA = H_BB - W_AB.T @ np.linalg.solve(H_AA, W_AB)
        S_BA = 0.5 * (S_BA + S_BA.T)
        F_blk_d = 0.5 * (
            float(np.sum(np.log(np.linalg.eigvalsh(H_AA))))
            + float(np.sum(np.log(np.linalg.eigvalsh(S_BA))))
        ) / float(d)
        F_schur_d = F_blk_d - F_dia_d

        F_paras.append(F_para_d)
        F_schurs.append(F_schur_d)

    f_para_mean = float(np.mean(F_paras)) if F_paras else float("nan")
    f_schur_mean = float(np.mean(F_schurs)) if F_schurs else float("nan")
    return {
        "dF_diam": float(np.mean(dF_dias)),
        "F_para": f_para_mean,
        "F_schur": f_schur_mean,
        "schur_diff": abs(f_schur_mean - f_para_mean) if F_paras else float("nan"),
        "Delta_F_nonAb": float(np.mean(dF_dias)) + f_para_mean,
        "tr_k2": float(np.mean(tr_k2s)),
        "min_lam_lap": float(np.min(min_lams)),
        "min_1_plus_k": float(np.min(min_ipks)),
        "n_unstable": n_unstable,
    }


def _axis_projector_so3(P):
    """Smooth, singularity-free adjoint axis projector Q = n_hat n_hat^T in SO(3) (valid at theta -> pi)."""
    trP = np.trace(P, axis1=-2, axis2=-1)
    v = so3_dual_vec(P)
    nv = np.linalg.norm(v, axis=-1, keepdims=True)
    n = v / np.maximum(nv, 1e-12)
    Q_v = n[..., :, None] * n[..., None, :]
    I3 = np.eye(3, dtype=float)
    M = 0.5 * (P + np.swapaxes(P, -1, -2)) - 0.5 * (trP - 1.0)[..., None, None] * I3
    trM = np.maximum(np.trace(M, axis1=-2, axis2=-1), 1e-12)[..., None, None]
    Q_m = M / trM
    Q = np.where((trP < 1.5)[..., None, None], Q_m, Q_v)
    iso = (nv < 1e-10) & ((trP > 2.99)[..., None])
    return np.where(iso[..., None], I3 / 3.0, Q)


def measure_interior_2x2_cocycle(R_full):
    """Exact gauge-invariant and Z_2-center-invariant interior 2x2 adjoint cocycle defect:
      delta_{2x2}(X) = 1 - <Tr(Q_perp(x) W_{2x2}^{(mu,nu)}(x))>,
    contraction factor = 1 - delta_{2x2}(X). Equals 0 (1 - delta = 1) in U(1).
    """
    d = R_full.shape[-1]
    if d == 1:
        return 0.0, 1.0
    Rl = [R_full[..., mu, :, :] for mu in range(4)]
    RlT = [np.swapaxes(r, -1, -2) for r in Rl]
    L2 = [Rl[mu] @ np.roll(Rl[mu], -1, axis=mu) for mu in range(4)]
    L2T = [np.swapaxes(m, -1, -2) for m in L2]

    dots = []
    # Dual plane pairs: 2x2 (0, 1) <-> (2, 3), (0, 2) <-> (1, 3), (0, 3) <-> (1, 2)
    for (mu, nu), (p_a, p_b) in [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]:
        W2x2 = L2[mu] @ np.roll(L2[nu], -2, axis=mu) @ np.roll(L2T[mu], -2, axis=nu) @ L2T[nu]
        P_perp = Rl[p_a] @ np.roll(Rl[p_b], -1, axis=p_a) @ np.roll(RlT[p_a], -1, axis=p_b) @ RlT[p_b]
        Q = _axis_projector_so3(P_perp)
        dots.append(np.einsum("...ij,...ij->...", Q, W2x2))
    contr = float(np.mean(np.stack(dots, axis=-1)))
    delta_2x2 = 1.0 - contr
    return delta_2x2, contr


def compute_free_abelian_dirichlet_baseline():
    """Exact Abelian zero-field 2^4 Dirichlet baseline (per color DOF):
      F_Ab0 = (1/2) Tr ln(I_4 otimes (-D^2_Dir(1))) = 2 Tr ln(-D^2_Dir(1)).
    """
    R0 = np.ones((2, 2, 2, 2, 4, 1, 1), dtype=float)
    Lap0, H0, W0 = build_dirichlet_2pow4_schur_ops(R0, origin=(0, 0, 0, 0))
    assert float(np.max(np.abs(W0))) == 0.0
    ev_lap0 = np.linalg.eigvalsh(Lap0)
    ev_h0 = np.linalg.eigvalsh(H0)
    f_ab0 = 0.5 * float(np.sum(np.log(ev_h0)))
    assert abs(f_ab0 - 2.0 * float(np.sum(np.log(ev_lap0)))) < 1e-12
    return f_ab0, float(ev_lap0[0])


def cfg_to_so3(cfg, group):
    L = cfg.shape[0]
    if group == "U1":
        return np.ones((L, L, L, L, 4, 1, 1), dtype=float)
    if group == "SU2":
        return q_to_so3(cfg)
    return cfg


def random_gauge_transform(rng, cfg, group):
    L = cfg.shape[0]
    if group == "U1":
        g = rng.uniform(-math.pi, math.pi, size=(L, L, L, L))
        out = cfg.copy()
        for mu in range(4):
            out[..., mu] = np.angle(np.exp(1j * (g + cfg[..., mu] - np.roll(g, -1, axis=mu))))
        return out
    else:
        g = rng.normal(size=(L, L, L, L, 4))
        g /= np.linalg.norm(g, axis=-1, keepdims=True)
        out = np.empty_like(cfg)
        if group == "SU2":
            for mu in range(4):
                out[..., mu, :] = qmul(qmul(g, cfg[..., mu, :]), qconj(np.roll(g, -1, axis=mu)))
        else:
            Rg = q_to_so3(g)
            RgT = np.swapaxes(Rg, -1, -2)
            for mu in range(4):
                out[..., mu, :, :] = Rg @ cfg[..., mu, :, :] @ np.roll(RgT, -1, axis=mu)
        return out


# ---------------------------------------------------------------------------
# Part 1: Gauge, Z_2-Center & Polarization-Block Schur Invariance Tests
# ---------------------------------------------------------------------------
def verify_invariances(f_ab0):
    print("=== PART 1: GAUGE, Z2-CENTER & POLARIZATION-BLOCK SCHUR INVARIANCE TESTS (L=6) ===")
    rng = np.random.default_rng(177401)
    L = 6
    parities = np.sum(np.indices((L, L, L, L)), axis=0) % 2
    origins = ((0, 0, 0, 0), (2, 2, 2, 2))
    max_g_err = 0.0
    max_z2_err = 0.0
    max_schur_err = 0.0

    for group, beta in [("U1", 1.30), ("SU2", 3.00), ("SO3", 2.80)]:
        if group == "U1":
            U = rng.uniform(-0.8, 0.8, size=(L, L, L, L, 4))
            u1_sweep(rng, U, parities, beta)
            cfg = U
        elif group == "SU2":
            U = np.zeros((L, L, L, L, 4, 4), dtype=float)
            U[..., 0] = 1.0
            for _ in range(5):
                su2_sweep(rng, U, parities, beta)
            cfg = U
        else:
            Uq = np.zeros((L, L, L, L, 4, 4), dtype=float)
            Uq[..., 0] = 1.0
            for _ in range(5):
                so3_sweep(rng, Uq, parities, beta, n_hits=4)
            cfg = q_to_so3(Uq)

        def eval_all(c, grp=group):
            R = cfg_to_so3(c, grp)
            obs = evaluate_2pow4_schur_observables(R, f_ab0, origins=origins)
            d2x2, contr = measure_interior_2x2_cocycle(R)
            blk = block_config_2x(c, grp, alpha_blk=0.188)
            snum, sden = compute_beta_sd(blk, grp)
            db_blk, _, gam_blk = measure_coarse_delta_and_gamma(blk, grp)
            return obs, [
                obs["dF_diam"], obs["F_para"], obs["F_schur"], obs["tr_k2"],
                d2x2, contr, snum / max(sden, 1e-12), db_blk, gam_blk,
            ]

        obs_0, v0 = eval_all(cfg)
        cfg_g = random_gauge_transform(rng, cfg, group)
        obs_g, vg = eval_all(cfg_g)
        err_g = max(abs(a - b) for a, b in zip(v0, vg))
        max_g_err = max(max_g_err, err_g)
        max_schur_err = max(max_schur_err, obs_0["schur_diff"], obs_g["schur_diff"])

        if group == "SO3":
            signs = rng.choice([-1.0, 1.0], size=(L, L, L, L, 4, 1))
            _, vz = eval_all(q_to_so3(Uq * signs), grp="SO3")
            max_z2_err = max(max_z2_err, max(abs(a - b) for a, b in zip(v0, vz)))

    assert max_g_err < 1e-12 and max_z2_err < 1e-12 and max_schur_err < 1e-12
    print(
        f"  PROBE4_INV_OK max_gauge_err={max_g_err:.1e} | max_SO3_Z2_err={max_z2_err:.1e} "
        f"| max_Schur_id_err={max_schur_err:.1e}"
    )


# ---------------------------------------------------------------------------
# Part 2: Exact Cancellation of Test B Dirichlet Cavity Mirage at alpha* = 0.188
# ---------------------------------------------------------------------------
def verify_mirage_cancellation(f_ab0, lam_ab0):
    print("\n=== PART 2: EXACT CANCELLATION OF TEST B DIRICHLET CAVITY MIRAGE (alpha* = 0.188) ===")
    rng = np.random.default_rng(177402)
    L = 6
    origins = ((0, 0, 0, 0), (2, 2, 0, 0), (0, 0, 2, 2), (2, 2, 2, 2))
    # 2A: Rough random pure-gauge (F = 0) across U(1), SU(2), SO(3)
    zeros_theta = np.zeros((L, L, L, L, 4), dtype=float)
    zeros_q = np.zeros((L, L, L, L, 4, 4), dtype=float)
    zeros_q[..., 0] = 1.0
    zeros_so3 = q_to_so3(zeros_q)

    print(f"  2A. Rough pure-gauge F=0 (Abelian 2^4 Dirichlet baseline F_Ab0/d = {f_ab0:.4f}, lam_min = {lam_ab0:.4f}):")
    for group, base in [("U1", zeros_theta), ("SU2", zeros_q), ("SO3", zeros_so3)]:
        pg = random_gauge_transform(rng, base, group)
        R_pg = cfg_to_so3(pg, group)
        obs = evaluate_2pow4_schur_observables(R_pg, f_ab0, origins=origins)
        d2x2, contr = measure_interior_2x2_cocycle(R_pg)
        F_raw = f_ab0 + obs["dF_diam"] + obs["F_para"]
        print(
            f"    {group:3s} (F=0): raw F/d={F_raw:.4f} (mirage) | "
            f"dF_diam/d={obs['dF_diam']:+.1e}, F_para/d={obs['F_para']:+.1e}, "
            f"DeltaF_nonAb/d={obs['Delta_F_nonAb']:+.1e}, 1-delta2x2={contr:.6f}"
        )
        assert abs(F_raw - f_ab0) < 1e-12
        assert abs(obs["Delta_F_nonAb"]) < 1e-12 and abs(d2x2) < 1e-12

    # 2B: Constrained 4^4 -> 2^4 clamped-x1 fiber at alpha* = 0.188 (cancels B=0 cavity gap & Jacobian)
    print("  2B. Constrained 4^4 -> 2^4 clamped-x1 on-shell fiber at alpha*=0.188:")
    print("      B    | lam_min(H_T) | DeltaF_nonAb |  dF_min    | dF_para(<0) | dF_cos     | d_beta_2x_fiber")
    L_fib = 4
    for B in (0.00, 0.05, 0.10):
        th_b = np.zeros((L_fib, L_fib, L_fib, L_fib, 4), dtype=float)
        for x1 in range(L_fib):
            th_b[:, x1, :, :, 2] = B * x1
        lam_min, dF_tot, dF_min, dF_cos, dF_para = eval_fiber_defect(L_fib, th_b, 0.188, open_x1=True)
        if B == 0.0:
            print(
                f"    {B:5.2f}  | {lam_min:12.5f} | {dF_tot:+12.2e} | {dF_min:+10.2e} | "
                f"{dF_para:+11.2e} | {dF_cos:+10.2e} | exact zero cancellation"
            )
            assert lam_min > 1.0 and abs(dF_tot) < 1e-12
        else:
            s_cl = 128.0 * (1.0 - math.cos(0.5 * B))
            db = dF_tot / s_cl
            print(
                f"    {B:5.2f}  | {lam_min:12.5f} | {dF_tot:+12.6f} | {dF_min:+10.6f} | "
                f"{dF_para:+11.6f} | {dF_cos:+10.6f} | {db:+15.4f}"
            )
            assert lam_min > 1.0 and dF_tot < 0.0 and dF_para < 0.0


# ---------------------------------------------------------------------------
# Part 3: Head-to-Head 8-Coupling Thermalized Conditional 2^4 Schur Table
# ---------------------------------------------------------------------------
def run_thermalized_suite(f_ab0):
    print("\n=== PART 3: THERMALIZED L=6 -> 3^4 CONDITIONAL 2^4 SCHUR & ABELIAN-SUBTRACTION TABLE (alpha* = 0.188) ===")
    print("  Free-energy sign: F := -ln Z; Delta F_nonAb = F_G - F_Ab0 = dF_diam (>0) + F_para (<0)")
    rng = np.random.default_rng(177403)
    L = 6
    parities = np.sum(np.indices((L, L, L, L)), axis=0) % 2
    origins = ((0, 0, 0, 0), (2, 2, 0, 0), (0, 0, 2, 2), (2, 2, 2, 2))
    n_therm = 40
    n_meas = 30
    n_skip = 2

    suite = [
        ("U1", 1.30),
        ("U1", 2.00),
        ("SU2", 2.30),
        ("SU2", 2.50),
        ("SU2", 3.00),
        ("SU2", 4.00),
        ("SO3", 2.80),
        ("SO3", 4.00),
    ]

    max_all_schur_err = 0.0
    rows = []
    summaries_b2 = {}

    for group, beta in suite:
        if group == "U1":
            U = np.zeros((L, L, L, L, 4), dtype=float)
        else:
            U = np.zeros((L, L, L, L, 4, 4), dtype=float)
            U[..., 0] = 1.0

        def sweep(n, grp=group, bt=beta, arr=U):
            for _ in range(n):
                if grp == "U1":
                    u1_sweep(rng, arr, parities, bt)
                elif grp == "SU2":
                    su2_sweep(rng, arr, parities, bt)
                else:
                    so3_sweep(rng, arr, parities, bt, n_hits=4)

        sweep(n_therm)

        df_dias, f_pars, f_nons, schur_errs, k2s = [], [], [], [], []
        contrs, d_blks, coarse_recs = [], [], []
        total_unstable = 0

        for _ in range(n_meas):
            sweep(n_skip)
            cfg = q_to_so3(U) if group == "SO3" else U
            R = cfg_to_so3(cfg, group)
            obs = evaluate_2pow4_schur_observables(R, f_ab0, origins=origins)
            total_unstable += obs["n_unstable"]
            _, contr = measure_interior_2x2_cocycle(R)
            blk = block_config_2x(cfg, group, alpha_blk=0.188)
            rec = measure_coarse_grid(blk, group)

            df_dias.append(obs["dF_diam"])
            if not math.isnan(obs["F_para"]):
                f_pars.append(obs["F_para"])
                f_nons.append(obs["Delta_F_nonAb"])
                schur_errs.append(obs["schur_diff"])
            k2s.append(obs["tr_k2"])
            contrs.append(contr)
            d_blks.append(rec["delta_blk"])
            coarse_recs.append(rec)

        summ = summarize_coarse_ensemble(coarse_recs)
        summaries_b2[(group, beta)] = summ
        m_sch = float(np.max(schur_errs))
        max_all_schur_err = max(max_all_schur_err, m_sch)
        rows.append({
            "group": group,
            "beta": beta,
            "m_dia": float(np.mean(df_dias)),
            "m_par": float(np.mean(f_pars)),
            "m_non": float(np.mean(f_nons)),
            "m_sch": m_sch,
            "m_k2": float(np.mean(k2s)),
            "m_ctr": float(np.mean(contrs)),
            "m_dblk": float(np.mean(d_blks)),
            "m_gam": summ["gamma_1pm"],
            "b_sd": summ["beta_SD"][0],
            "b_se": summ["beta_SD"][1],
            "total_unstable": total_unstable,
        })

    b2_u1_200 = summaries_b2[("U1", 2.00)]["beta_SD"][0]
    kappa_u1 = b2_u1_200 / 2.00
    print(f"  Calibrated U(1)(2.00) b=1->b=2 UV stencil factor kappa_U1(alpha*) = {b2_u1_200:.4f}/2.00 = {kappa_u1:.4f}")

    hdr = (
        "  Group(beta) | dF_diam/d | F_para/d  | DeltaF_nA |  SchurErr | Tr(K^2)/d | "
        "1-d_2x2 | d_blk  | Gamma_BLK | d_beta(b2-b1) | d_beta_rel"
    )
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))

    for r in rows:
        group = r["group"]
        beta = r["beta"]
        d_raw = r["b_sd"] - beta
        d_rel = r["b_sd"] - kappa_u1 * beta
        lbl = f"{group}({beta:.2f})"
        unst_tag = f" [u={r['total_unstable']}]" if r["total_unstable"] > 0 else ""
        print(
            f"  {lbl:11s} | {r['m_dia']:+9.4f} | {r['m_par']:+9.4f} | {r['m_non']:+9.4f} | "
            f"{r['m_sch']:9.1e} | {r['m_k2']:9.4f} | {r['m_ctr']:7.4f} | {r['m_dblk']:6.4f} | "
            f"{r['m_gam']:9.4f} | {d_raw:+6.3f}+/-{r['b_se']:.3f} | {d_rel:+10.3f}{unst_tag}"
        )

        assert r["m_sch"] < 1e-11
        if group == "U1":
            assert abs(r["m_dia"]) < 1e-12 and abs(r["m_par"]) < 1e-12 and abs(r["m_non"]) < 1e-12
            assert abs(r["m_ctr"] - 1.0) < 1e-12 and abs(r["m_dblk"]) < 1e-12
        else:
            assert r["m_dia"] > 0.0 and r["m_par"] < 0.0 and r["m_non"] < 0.0
            assert r["m_k2"] > 0.0 and r["m_ctr"] < 1.0 and r["m_gam"] < 1.0
            assert d_rel < 0.0

    print(f"  Max polarization-block Schur identity error across all 8 ensembles: {max_all_schur_err:.1e}")
    return summaries_b2


def run_matched_3pow4_control(summaries_b2):
    print("\n=== PART 3B: MATCHED-VOLUME 3^4 CONTROL (L=12 b=4 vs L=6 b=2 AT alpha* = 0.188) ===")
    rng = np.random.default_rng(177404)
    L = 12
    parities = np.sum(np.indices((L, L, L, L)), axis=0) % 2
    n_therm = 25
    n_meas = 18
    n_skip = 2

    ctrl_pts = [
        ("U1", 2.00),
        ("SU2", 3.00),
        ("SU2", 4.00),
        ("SO3", 2.80),
        ("SO3", 4.00),
    ]
    print("  Group(beta) | beta_SD(b=2) | beta_SD(b=4) | d_beta(b2->b4) | Gamma_BLK(b=2 -> b=4) | delta_blk(b=2 -> b=4)")
    for group, beta in ctrl_pts:
        if group == "U1":
            U = np.zeros((L, L, L, L, 4), dtype=float)
        else:
            U = np.zeros((L, L, L, L, 4, 4), dtype=float)
            U[..., 0] = 1.0

        def sweep(n, grp=group, bt=beta, arr=U):
            for _ in range(n):
                if grp == "U1":
                    u1_sweep(rng, arr, parities, bt)
                elif grp == "SU2":
                    su2_sweep(rng, arr, parities, bt)
                else:
                    so3_sweep(rng, arr, parities, bt, n_hits=4)

        sweep(n_therm)
        recs_4 = []
        for _ in range(n_meas):
            sweep(n_skip)
            cfg = q_to_so3(U) if group == "SO3" else U
            blk1 = block_config_2x(cfg, group, alpha_blk=0.188)
            blk2 = block_config_2x(blk1, group, alpha_blk=0.188)
            recs_4.append(measure_coarse_grid(blk2, group))

        s4 = summarize_coarse_ensemble(recs_4)
        s2 = summaries_b2[(group, beta)]
        d_b, d_b_se = jackknife_ratio_diff(s4["sd_num"], s4["sd_den"], s2["sd_num"], s2["sd_den"])
        lbl = f"{group}({beta:.2f})"
        print(
            f"  {lbl:11s} | {s2['beta_SD'][0]:12.4f} | {s4['beta_SD'][0]:12.4f} | "
            f"{d_b:+6.3f}+/-{d_b_se:.3f} | {s2['gamma_1pm']:6.4f} -> {s4['gamma_1pm']:6.4f}      | "
            f"{s2['delta_blk'][0]:.4f} -> {s4['delta_blk'][0]:.4f}"
        )
        if group == "U1":
            assert abs(d_b) < 0.12 and abs(s4["delta_blk"][0]) < 1e-12 and s4["gamma_1pm"] > 0.30
        elif group == "SO3" and abs(beta - 4.00) < 1e-9:
            assert s4["delta_blk"][0] > s2["delta_blk"][0] and s4["gamma_1pm"] < s2["gamma_1pm"]
        else:
            assert d_b < 0.0 and s4["delta_blk"][0] > s2["delta_blk"][0] and s4["gamma_1pm"] < s2["gamma_1pm"]


def main():
    t0 = time.time()
    f_ab0, lam_ab0 = compute_free_abelian_dirichlet_baseline()
    verify_invariances(f_ab0)
    verify_mirage_cancellation(f_ab0, lam_ab0)
    summaries_b2 = run_thermalized_suite(f_ab0)
    run_matched_3pow4_control(summaries_b2)
    print(f"\nPROBE_ABELIAN_SUBTRACTED_2TO4_FIBER_SCHUR_OK elapsed={time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
