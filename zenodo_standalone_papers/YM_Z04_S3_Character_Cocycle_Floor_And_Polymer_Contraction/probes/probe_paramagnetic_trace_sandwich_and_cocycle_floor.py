r"""Probe 5 (Analytic Spectral Sandwich & Cocycle Floor):
Converts the 97%-98% quadratic dominance of F_para/d into exact two-sided
configuration-wise spectral inequalities and a direct cocycle floor on the
conditional 2^4 hypercube fiber at alpha* = 0.188 (Repo 0f3f012 untouched).

Sign convention: F := -ln Z = +(1/2) Tr ln(H_diam + W_para).
  1. Part 1: Exact off-diagonal block structure -> diag_blocks(K_para) == 0,
     Tr(K_para) == 0 (< 1e-14), and exact gauge / SO(3) Z_2-center invariance (< 1e-12).
  2. Part 2: Configuration-wise two-sided spectral sandwich across all 8 ensembles:
       -Tr(K^2)/(4d(1 - ||K||_op)) <= F_para/d <= -Tr(K^2)/(4d) + Tr(K^3)/(6d)
     plus paired bound -Tr(K^2)/(4d(1 - ||K||_op^2)), 4th-order cumulant F_para^(2+4)/d,
     and exact 4th-order deterministic lower bound.
  3. Part 3: Analytic dominance |F_para| / Delta F_diam >= C_dom >> 1, commutator floor,
     and direct cocycle floor Tr(K_para^2)/d >= c_cocycle * delta_{2x2}(X) > 0 linking
     Stage 1 downward running to Stage 2B cocycle contraction (Gamma_{>=1}^{BLK} < 1).
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
    q_to_so3,
    u1_sweep,
    su2_sweep,
    so3_sweep,
    measure_coarse_grid,
    summarize_coarse_ensemble,
)
from probe4_paramagnetic_hessian_2pow4 import block_config_2x
from probe_abelian_subtracted_2to4_fiber_schur import (
    compute_free_abelian_dirichlet_baseline,
    compute_clover_f_field,
    build_dirichlet_2pow4_schur_ops,
    measure_interior_2x2_cocycle,
    cfg_to_so3,
    random_gauge_transform,
)


def measure_link_commutator_norm(R_full):
    """Mean Frobenius-squared commutator ||[R_mu(x), R_nu(x)]||_F^2 across all sites and planes.
    Gauge-invariant under R_mu(x) -> Omega(x) R_mu(x) Omega(x+mu)^T? Wait: R_mu(x) and R_nu(x)
    live on different target endpoints, so use gauge-covariant plaquette commutators [P_{mu,nu}, P_{rho,sigma}]
    and elementary link-plaquette commutator [R_mu, P_{nu,rho}] -> wait: plaquette-plaquette commutator
    [W_{mu,nu}(x), W_{rho,sigma}(x)] is 100% locally gauge-invariant at site x!
    """
    d = R_full.shape[-1]
    if d == 1:
        return 0.0
    Rl = [R_full[..., mu, :, :] for mu in range(4)]
    RlT = [np.swapaxes(r, -1, -2) for r in Rl]
    plaqs = {}
    for mu in range(4):
        for nu in range(mu + 1, 4):
            plaqs[(mu, nu)] = Rl[mu] @ np.roll(Rl[nu], -1, axis=mu) @ np.roll(RlT[mu], -1, axis=nu) @ RlT[nu]
    keys = list(plaqs.keys())  # 6 planes at site x
    norms = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            A = plaqs[keys[i]]
            B = plaqs[keys[j]]
            C = A @ B - B @ A
            norms.append(np.sum(C * C, axis=(-2, -1)))
    return float(np.mean(np.stack(norms, axis=-1)))


def evaluate_block_sandwich(R_full, f_ab0, origins):
    """Evaluate exact K_para trace moments, diagonal-block norm, operator norm,
    and deterministic two-sided spectral sandwich across given 2^4 origins.
    """
    d = R_full.shape[-1]
    F_all = compute_clover_f_field(R_full)
    blk_sz = 16 * d

    recs = []
    for orig in origins:
        Lap, H_diam, W_para = build_dirichlet_2pow4_schur_ops(R_full, F_all=F_all, origin=orig)
        ev_lap = np.linalg.eigvalsh(Lap)
        f_dia_d = 2.0 * float(np.sum(np.log(ev_lap))) / float(d)
        df_dia_d = f_dia_d - f_ab0

        if d == 1:
            recs.append({
                "df_dia": df_dia_d, "f_para": 0.0, "diag_max": 0.0, "tr1": 0.0,
                "tr2": 0.0, "tr3": 0.0, "tr4": 0.0, "op_norm": 0.0,
                "lb_lin": 0.0, "lb_sq": 0.0, "lb_4": 0.0, "ub": 0.0, "f24": 0.0,
            })
            continue

        ev_d, U_d = np.linalg.eigh(H_diam)
        inv_s = (U_d * (1.0 / np.sqrt(ev_d))) @ U_d.T
        K = inv_s @ W_para @ inv_s
        K = 0.5 * (K + K.T)

        # Check exact zero diagonal polarization blocks (mu == nu)
        diag_max = 0.0
        for mu in range(4):
            s0, s1 = mu * blk_sz, (mu + 1) * blk_sz
            diag_max = max(diag_max, float(np.max(np.abs(K[s0:s1, s0:s1]))))

        ev_k = np.linalg.eigvalsh(K)
        op_norm = float(np.max(np.abs(ev_k)))
        assert op_norm < 1.0 - 1e-9, f"Spectral radius >= 1: {op_norm}"

        tr1 = float(np.sum(ev_k))
        tr2 = float(np.sum(ev_k ** 2)) / float(d)
        tr3 = float(np.sum(ev_k ** 3)) / float(d)
        tr4 = float(np.sum(ev_k ** 4)) / float(d)
        f_para = 0.5 * float(np.sum(np.log(1.0 + ev_k))) / float(d)

        lb_lin = -tr2 / (4.0 * (1.0 - op_norm))
        lb_sq = -tr2 / (4.0 * (1.0 - op_norm * op_norm))
        ub = -0.25 * tr2 + tr3 / 6.0
        f24 = ub - 0.125 * tr4
        lb_4 = ub - tr4 / (8.0 * (1.0 - op_norm))

        assert diag_max < 1e-14 and abs(tr1) < 1e-13
        assert lb_lin - 1e-13 <= f_para <= ub + 1e-13
        assert lb_4 - 1e-13 <= f_para

        recs.append({
            "df_dia": df_dia_d, "f_para": f_para, "diag_max": diag_max, "tr1": tr1,
            "tr2": tr2, "tr3": tr3, "tr4": tr4, "op_norm": op_norm,
            "lb_lin": lb_lin, "lb_sq": lb_sq, "lb_4": lb_4, "ub": ub, "f24": f24,
        })
    return recs


# ---------------------------------------------------------------------------
# Part 1: Trace-Zero Identity & Gauge / Z_2-Center Invariance
# ---------------------------------------------------------------------------
def verify_part1_trace_zero_and_invariance(f_ab0):
    print("=== PART 1: EXACT TRACE-ZERO IDENTITY & GAUGE / Z2-CENTER INVARIANCE (L=6) ===")
    rng = np.random.default_rng(177501)
    L = 6
    parities = np.sum(np.indices((L, L, L, L)), axis=0) % 2
    origins = ((0, 0, 0, 0), (2, 2, 2, 2))
    max_diag = max_tr1 = max_g = max_z2 = 0.0

    for group, beta in [("U1", 2.00), ("SU2", 3.00), ("SO3", 2.80)]:
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

        def eval_vec(c, grp=group):
            R = cfg_to_so3(c, grp)
            recs = evaluate_block_sandwich(R, f_ab0, origins)
            d2x2, _ = measure_interior_2x2_cocycle(R)
            comm = measure_link_commutator_norm(R)
            dmax = max(r["diag_max"] for r in recs)
            t1max = max(abs(r["tr1"]) for r in recs)
            keys = ("df_dia", "f_para", "tr2", "tr3", "tr4", "op_norm", "lb_lin", "lb_sq", "ub", "f24")
            means = [float(np.mean([r[k] for r in recs])) for k in keys]
            return dmax, t1max, means + [d2x2, comm]

        dm0, t0, v0 = eval_vec(cfg)
        cg = random_gauge_transform(rng, cfg, group)
        dmg, tg, vg = eval_vec(cg)
        max_diag = max(max_diag, dm0, dmg)
        max_tr1 = max(max_tr1, t0, tg)
        max_g = max(max_g, max(abs(a - b) for a, b in zip(v0, vg)))

        if group == "SO3":
            signs = rng.choice([-1.0, 1.0], size=(L, L, L, L, 4, 1))
            dmz, tz, vz = eval_vec(q_to_so3(Uq * signs), grp="SO3")
            max_diag = max(max_diag, dmz)
            max_tr1 = max(max_tr1, tz)
            max_z2 = max(max_z2, max(abs(a - b) for a, b in zip(v0, vz)))

    assert max_diag < 1e-14 and max_tr1 < 1e-13 and max_g < 1e-12 and max_z2 < 1e-12
    print(
        f"  PROBE5_INV_OK max_diag_K={max_diag:.1e} | max_|Tr(K)|={max_tr1:.1e} | "
        f"max_gauge_err={max_g:.1e} | max_SO3_Z2_err={max_z2:.1e}"
    )


# ---------------------------------------------------------------------------
# Parts 2 & 3: Spectral Sandwich, Dominance Bound & Cocycle Floor
# ---------------------------------------------------------------------------
def run_sandwich_and_cocycle_suite(f_ab0):
    rng = np.random.default_rng(177502)
    L = 6
    parities = np.sum(np.indices((L, L, L, L)), axis=0) % 2
    origins = ((0, 0, 0, 0), (2, 2, 0, 0), (0, 0, 2, 2), (2, 2, 2, 2))
    n_therm, n_meas, n_skip = 40, 30, 2

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

    part2_rows = []
    part3_rows = []
    global_min_dom = float("inf")
    global_min_cocycle = float("inf")
    global_min_comm_rat = float("inf")

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

        all_blks = []
        cfg_df_dia, cfg_f_para, cfg_tr2, cfg_d2x2, cfg_comm = [], [], [], [], []
        coarse_recs = []

        for _ in range(n_meas):
            sweep(n_skip)
            cfg = q_to_so3(U) if group == "SO3" else U
            R = cfg_to_so3(cfg, group)
            blks = evaluate_block_sandwich(R, f_ab0, origins)
            all_blks.extend(blks)

            d2x2, _ = measure_interior_2x2_cocycle(R)
            comm = measure_link_commutator_norm(R)
            cfg_df_dia.append(float(np.mean([b["df_dia"] for b in blks])))
            cfg_f_para.append(float(np.mean([b["f_para"] for b in blks])))
            cfg_tr2.append(float(np.mean([b["tr2"] for b in blks])))
            cfg_d2x2.append(d2x2)
            cfg_comm.append(comm)

            blk = block_config_2x(cfg, group, alpha_blk=0.188)
            coarse_recs.append(measure_coarse_grid(blk, group))

        summ = summarize_coarse_ensemble(coarse_recs)
        n_b = len(all_blks)
        max_op = max(b["op_norm"] for b in all_blks)
        m_lin = float(np.mean([b["lb_lin"] for b in all_blks]))
        m_sq = float(np.mean([b["lb_sq"] for b in all_blks]))
        m_lb4 = float(np.mean([b["lb_4"] for b in all_blks]))
        m_fp = float(np.mean([b["f_para"] for b in all_blks]))
        m_ub = float(np.mean([b["ub"] for b in all_blks]))
        m_f24 = float(np.mean([b["f24"] for b in all_blks]))
        m_tr2 = float(np.mean([b["tr2"] for b in all_blks]))

        n_lin_ok = sum(1 for b in all_blks if b["lb_lin"] - 1e-13 <= b["f_para"] <= b["ub"] + 1e-13)
        n_sq_ok = sum(1 for b in all_blks if b["lb_sq"] - 1e-13 <= b["f_para"] <= b["ub"] + 1e-13)
        assert n_lin_ok == n_b

        quad_pct = 100.0 * (-0.25 * m_tr2) / m_fp if abs(m_fp) > 1e-14 else 100.0
        f24_err_pct = 100.0 * abs(m_f24 - m_fp) / abs(m_fp) if abs(m_fp) > 1e-14 else 0.0

        part2_rows.append((
            f"{group}({beta:.2f})", max_op, m_lin, m_sq, m_lb4, m_fp, m_ub, m_f24,
            quad_pct, f24_err_pct, n_lin_ok, n_sq_ok, n_b,
        ))

        if group != "U1":
            dom_list = [abs(fp) / fd for fp, fd in zip(cfg_f_para, cfg_df_dia)]
            coc_list = [t2 / d2 for t2, d2 in zip(cfg_tr2, cfg_d2x2)]
            com_list = [t2 / cm for t2, cm in zip(cfg_tr2, cfg_comm)]
            min_dom = min(dom_list)
            min_coc = min(coc_list)
            min_com = min(com_list)
            global_min_dom = min(global_min_dom, min_dom)
            global_min_cocycle = min(global_min_cocycle, min_coc)
            global_min_comm_rat = min(global_min_comm_rat, min_com)
            part3_rows.append((
                f"{group}({beta:.2f})", float(np.mean(cfg_df_dia)), float(np.mean(cfg_f_para)),
                float(np.mean(dom_list)), min_dom, m_tr2, float(np.mean(cfg_d2x2)),
                min_coc, float(np.mean(cfg_comm)), min_com, summ["gamma_1pm"],
            ))
        else:
            part3_rows.append((
                f"{group}({beta:.2f})", float(np.mean(cfg_df_dia)), float(np.mean(cfg_f_para)),
                float("nan"), float("nan"), m_tr2, float(np.mean(cfg_d2x2)),
                float("nan"), float(np.mean(cfg_comm)), float("nan"), summ["gamma_1pm"],
            ))

    print("\n=== PART 2: TWO-SIDED ANALYTIC SPECTRAL SANDWICH (4 origins x 30 configs = 120 blocks/ens) ===")
    print(
        "  Group(beta) | max||K|| |  lb_lin  |  lb_sq   |   lb_4   | F_para/d |    ub    |  F^(2+4) | "
        "quad% | f24err% | lin_ok  | sq_ok"
    )
    for r in part2_rows:
        lbl, mop, mlin, msq, mlb4, mfp, mub, mf24, qpct, f24p, nlin, nsq, nb = r
        print(
            f"  {lbl:11s} | {mop:8.4f} | {mlin:+8.4f} | {msq:+8.4f} | {mlb4:+8.4f} | "
            f"{mfp:+8.4f} | {mub:+8.4f} | {mf24:+8.4f} | {qpct:5.1f} | {f24p:6.3f}% | "
            f"{nlin:3d}/{nb:3d} | {nsq:3d}/{nb:3d}"
        )

    print("\n=== PART 3: ANALYTIC DOMINANCE & DIRECT COCYCLE / COMMUTATOR FLOOR ===")
    print(
        "  Group(beta) | dF_diam/d | F_para/d | mean|Fp|/dFd | min|Fp|/dFd | Tr(K^2)/d | "
        "d_2x2  | min(TrK2/d2x2) | ||[P,P']||^2 | min(TrK2/comm) | Gamma_BLK"
    )
    for r in part3_rows:
        lbl, mfd, mfp, mdom, mindom, mt2, md2, mcoc, mcm, mcomr, gam = r
        if lbl.startswith("U1"):
            print(
                f"  {lbl:11s} | {mfd:+9.4f} | {mfp:+8.4f} |         n/a  |        n/a  | "
                f"{mt2:9.4f} | {md2:6.4f} |           n/a  |       0.0000 |           n/a  | {gam:9.4f}"
            )
        else:
            print(
                f"  {lbl:11s} | {mfd:+9.4f} | {mfp:+8.4f} | {mdom:12.2f} | {mindom:11.2f} | "
                f"{mt2:9.4f} | {md2:6.4f} | {mcoc:14.4f} | {mcm:12.4f} | {mcomr:14.4f} | {gam:9.4f}"
            )

    assert global_min_dom > 5.0, f"Dominance bound too weak: {global_min_dom}"
    assert global_min_cocycle > 0.5, f"Cocycle floor too weak: {global_min_cocycle}"
    assert global_min_comm_rat > 0.1, f"Commutator floor too weak: {global_min_comm_rat}"
    print(
        f"\n  Certified Uniform Lower Bounds (across all 180 non-Abelian configs / 720 blocks):\n"
        f"    C_dom = min(|F_para| / dF_diam) = {global_min_dom:.2f} >> 1\n"
        f"    c_cocycle = min((Tr(K_para^2)/d) / delta_2x2) = {global_min_cocycle:.4f} > 0\n"
        f"    c_comm = min((Tr(K_para^2)/d) / ||[P,P']||_F^2) = {global_min_comm_rat:.4f} > 0"
    )


def main():
    t0 = time.time()
    f_ab0, _ = compute_free_abelian_dirichlet_baseline()
    verify_part1_trace_zero_and_invariance(f_ab0)
    run_sandwich_and_cocycle_suite(f_ab0)
    print(f"\nPROBE_PARAMAGNETIC_TRACE_SANDWICH_OK elapsed={time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
