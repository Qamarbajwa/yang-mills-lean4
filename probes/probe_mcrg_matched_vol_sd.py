"""Matched-Volume MCRG & Schwinger-Dyson Effective Coupling Probe for E-UV-RG.

Tests whether 4D non-Abelian gauge-covariant RG blocking drives weak coupling
downward toward strong coupling (Delta beta < 0) at fixed coarse torus volume
L_b^4 (3^4 and 4^4), contrasting 4D Coulomb U(1) vs SU(2) vs centerless SO(3).

Components:
  1. Exact gauge-invariant Schwinger-Dyson inverse-coupling estimator beta_SD(cfg)
     with leave-one-out jackknife errors over measured configurations.
  2. Unit tests:
       - Gauge & Z2 invariance to < 1e-12 on L=4 bare and L=6 -> 3^4 blocked.
       - Thermalized L=6 bare (b=1) SD calibration verifying |beta_SD - beta| / beta < 4%.
  3. Part 1: Free/weak U(1) (beta=2.00) alpha-kernel calibration on matched 3^4
     (L=12 -> 3^4 vs L=6 -> 3^4) isolating the tree-level blocking parameter alpha*.
  4. Part 2: Matched-3^4 MCRG & SD comparisons (L=12, b=4 vs L=6, b=2) across
     U(1) (1.30, 2.00), SU(2) (2.50, 3.00, 4.00), and SO(3) (2.80, 4.00) at both
     calibrated alpha* and alpha=0.50, with 3-point Swendsen MCRG matching shifts.
  5. Part 3: Matched-4^4 finite-volume spot check (L=16, b=4 vs L=8, b=2) for
     U(1) (beta=1.30) and SU(2) (beta=3.00).
"""

import math
import time
import numpy as np


# ---------------------------------------------------------------------------
# Group Algebra Primitives
# ---------------------------------------------------------------------------
def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([
        a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
        a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
        a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
        a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0,
    ], axis=-1)


def qconj(a):
    out = np.array(a, dtype=float, copy=True)
    out[..., 1:] *= -1.0
    return out


def q_to_so3(q):
    q0, q1, q2, q3 = q[..., 0], q[..., 1], q[..., 2], q[..., 3]
    r00 = 1.0 - 2.0 * (q2 * q2 + q3 * q3)
    r01 = 2.0 * (q1 * q2 - q0 * q3)
    r02 = 2.0 * (q1 * q3 + q0 * q2)
    r10 = 2.0 * (q1 * q2 + q0 * q3)
    r11 = 1.0 - 2.0 * (q1 * q1 + q3 * q3)
    r12 = 2.0 * (q2 * q3 - q0 * q1)
    r20 = 2.0 * (q1 * q3 - q0 * q2)
    r21 = 2.0 * (q2 * q3 + q0 * q1)
    r22 = 1.0 - 2.0 * (q1 * q1 + q2 * q2)
    return np.stack([
        np.stack([r00, r01, r02], axis=-1),
        np.stack([r10, r11, r12], axis=-1),
        np.stack([r20, r21, r22], axis=-1),
    ], axis=-2)


def random_su2(rng, shape):
    g = rng.normal(size=tuple(shape) + (4,))
    return g / np.linalg.norm(g, axis=-1, keepdims=True)


def project_so3(M):
    """Nearest proper SO(3) matrix via batched SVD, enforcing det(R) = +1."""
    u, _, vt = np.linalg.svd(M)
    r = u @ vt
    neg = np.linalg.det(r) < 0.0
    if np.any(neg):
        u_fix = u.copy()
        u_fix[neg, :, -1] *= -1.0
        r = u_fix @ vt
    return r


def so3_dual_vec(W):
    """Axial dual vector in R^3 of skew part (W - W^T)/2."""
    return 0.5 * np.stack([
        W[..., 2, 1] - W[..., 1, 2],
        W[..., 0, 2] - W[..., 2, 0],
        W[..., 1, 0] - W[..., 0, 1],
    ], axis=-1)


# ---------------------------------------------------------------------------
# Gauge-Covariant Factor-2 Blocking (L -> L/2)
# ---------------------------------------------------------------------------
def block_config_2x(cfg, group, alpha_blk):
    if group == "U1":
        E = [np.exp(1j * cfg[..., mu]) for mu in range(4)]
        cols = []
        for mu in range(4):
            P_str = E[mu] * np.roll(E[mu], -1, axis=mu)
            acc = P_str.copy()
            if alpha_blk != 0.0:
                for nu in range(4):
                    if nu == mu:
                        continue
                    fwd = E[nu] * np.roll(P_str, -1, axis=nu) * np.conj(np.roll(E[nu], -2, axis=mu))
                    bwd = (
                        np.conj(np.roll(E[nu], 1, axis=nu))
                        * np.roll(P_str, 1, axis=nu)
                        * np.roll(np.roll(E[nu], 1, axis=nu), -2, axis=mu)
                    )
                    acc += alpha_blk * (fwd + bwd)
            cols.append(np.angle(acc[::2, ::2, ::2, ::2]))
        return np.stack(cols, axis=-1)
    elif group == "SU2":
        Ul = [cfg[..., mu, :] for mu in range(4)]
        cols = []
        for mu in range(4):
            P_str = qmul(Ul[mu], np.roll(Ul[mu], -1, axis=mu))
            acc = P_str.copy()
            if alpha_blk != 0.0:
                for nu in range(4):
                    if nu == mu:
                        continue
                    fwd = qmul(qmul(Ul[nu], np.roll(P_str, -1, axis=nu)), qconj(np.roll(Ul[nu], -2, axis=mu)))
                    bwd = qmul(
                        qmul(qconj(np.roll(Ul[nu], 1, axis=nu)), np.roll(P_str, 1, axis=nu)),
                        np.roll(np.roll(Ul[nu], 1, axis=nu), -2, axis=mu),
                    )
                    acc += alpha_blk * (fwd + bwd)
            even = acc[::2, ::2, ::2, ::2]
            cols.append(even / np.maximum(np.linalg.norm(even, axis=-1, keepdims=True), 1e-14))
        return np.stack(cols, axis=-2)
    else:
        Rl = [cfg[..., mu, :, :] for mu in range(4)]
        RlT = [np.swapaxes(r, -1, -2) for r in Rl]
        cols = []
        for mu in range(4):
            P_str = Rl[mu] @ np.roll(Rl[mu], -1, axis=mu)
            acc = P_str.copy()
            if alpha_blk != 0.0:
                for nu in range(4):
                    if nu == mu:
                        continue
                    fwd = Rl[nu] @ np.roll(P_str, -1, axis=nu) @ np.roll(RlT[nu], -2, axis=mu)
                    bwd = (
                        np.roll(RlT[nu], 1, axis=nu)
                        @ np.roll(P_str, 1, axis=nu)
                        @ np.roll(np.roll(Rl[nu], 1, axis=nu), -2, axis=mu)
                    )
                    acc += alpha_blk * (fwd + bwd)
            cols.append(project_so3(acc[::2, ::2, ::2, ::2]))
        return np.stack(cols, axis=-3)


# ---------------------------------------------------------------------------
# Vectorized 4D Checkerboard Updaters
# ---------------------------------------------------------------------------
def u1_sweep(rng, U, parities, beta):
    for mu in range(4):
        for parity in (0, 1):
            E = [np.exp(1j * U[..., nu]) for nu in range(4)]
            S = np.zeros_like(E[0])
            for nu in range(4):
                if nu == mu:
                    continue
                fwd = E[nu] * np.roll(E[mu], -1, axis=nu) * np.conj(np.roll(E[nu], -1, axis=mu))
                bwd = (
                    np.conj(np.roll(E[nu], 1, axis=nu))
                    * np.roll(E[mu], 1, axis=nu)
                    * np.roll(np.roll(E[nu], 1, axis=nu), -1, axis=mu)
                )
                S += fwd + bwd
            mask = parities == parity
            Sm = S[mask]
            U[mask, mu] = np.angle(Sm) + rng.vonmises(np.zeros(len(Sm)), np.maximum(beta * np.abs(Sm), 1e-12))


def su2_staples_list(U, mu):
    U_nu = [U[..., nu, :] for nu in range(4)]
    st_list = []
    for nu in range(4):
        if nu == mu:
            continue
        fwd = qmul(qmul(U_nu[nu], np.roll(U_nu[mu], -1, axis=nu)), qconj(np.roll(U_nu[nu], -1, axis=mu)))
        bwd = qmul(
            qmul(qconj(np.roll(U_nu[nu], 1, axis=nu)), np.roll(U_nu[mu], 1, axis=nu)),
            np.roll(np.roll(U_nu[nu], 1, axis=nu), -1, axis=mu),
        )
        st_list.append(fwd)
        st_list.append(bwd)
    return np.stack(st_list, axis=-2)


def su2_kp_sample_vec(rng, A, beta):
    detA = np.sum(A * A, axis=-1)
    alpha = beta * np.sqrt(np.maximum(detA, 1e-30))
    n = alpha.shape
    a_inv = np.where(detA > 1e-30, 1.0 / np.sqrt(np.maximum(detA, 1e-30)), 0.0)
    V = A * a_inv[..., None]
    delta = np.empty(n, dtype=float)
    remaining = np.ones(n, dtype=bool)
    while np.any(remaining):
        idx = np.where(remaining)
        a_rem = alpha[idx]
        m = len(a_rem)
        r1 = np.maximum(rng.random(m), 1e-15)
        r2 = np.maximum(rng.random(m), 1e-15)
        r3 = rng.random(m)
        r4 = rng.random(m)
        lam2 = -(np.log(r1) + np.log(r2) * (np.cos(2.0 * math.pi * r3) ** 2)) / (2.0 * a_rem)
        accept = (r4 * r4 <= 1.0 - lam2) & (lam2 <= 1.0)
        acc_idx = tuple(x[accept] for x in idx)
        delta[acc_idx] = lam2[accept]
        remaining[acc_idx] = False
    x0 = 1.0 - 2.0 * delta
    r_vec = np.sqrt(np.maximum(1.0 - x0 * x0, 0.0))
    z_ang = rng.uniform(-1.0, 1.0, size=n)
    phi = rng.uniform(0.0, 2.0 * math.pi, size=n)
    sin_th = np.sqrt(np.maximum(1.0 - z_ang * z_ang, 0.0))
    X = np.stack([x0, r_vec * sin_th * np.cos(phi), r_vec * sin_th * np.sin(phi), r_vec * z_ang], axis=-1)
    return qmul(X, V)


def su2_sweep(rng, U, parities, beta):
    for mu in range(4):
        for parity in (0, 1):
            S = np.sum(su2_staples_list(U, mu), axis=-2)
            mask = parities == parity
            U[mask, mu, :] = su2_kp_sample_vec(rng, S[mask], beta)


def so3_sweep(rng, U, parities, beta_A, n_hits=4):
    sigma = min(1.4, 1.2 / math.sqrt(max(0.5, beta_A)))
    coeff = (4.0 / 3.0) * beta_A
    for mu in range(4):
        for parity in (0, 1):
            Vs = su2_staples_list(U, mu)
            mask = parities == parity
            Vs_m = Vs[mask]
            Q = np.einsum("mka,mkb->mab", Vs_m, Vs_m)
            u_cur = U[mask, mu, :].copy()
            e_cur = np.einsum("ma,mab,mb->m", u_cur, Q, u_cur)
            for _ in range(n_hits):
                step = rng.normal(scale=sigma, size=u_cur.shape)
                step[:, 0] += 1.0
                step /= np.linalg.norm(step, axis=-1, keepdims=True)
                u_prop = qmul(step, u_cur)
                e_prop = np.einsum("ma,mab,mb->m", u_prop, Q, u_prop)
                dE = coeff * (e_prop - e_cur)
                acc = (dE >= 0.0) | (rng.random(len(u_cur)) < np.exp(np.minimum(dE, 0.0)))
                u_cur[acc] = u_prop[acc]
                e_cur[acc] = e_prop[acc]
            U[mask, mu, :] = u_cur


# ---------------------------------------------------------------------------
# Exact Gauge-Invariant Schwinger-Dyson Estimator & Coarse Observables
# ---------------------------------------------------------------------------
def so3_staples_sum(R, mu):
    Rl = [R[..., nu, :, :] for nu in range(4)]
    RlT = [np.swapaxes(r, -1, -2) for r in Rl]
    M = np.zeros_like(Rl[0])
    for nu in range(4):
        if nu == mu:
            continue
        fwd = Rl[nu] @ np.roll(Rl[mu], -1, axis=nu) @ np.roll(RlT[nu], -1, axis=mu)
        bwd = (
            np.roll(RlT[nu], 1, axis=nu)
            @ np.roll(Rl[mu], 1, axis=nu)
            @ np.roll(np.roll(Rl[nu], 1, axis=nu), -1, axis=mu)
        )
        M += fwd + bwd
    return M


def compute_beta_sd(cfg, group):
    """Return per-config spatial+direction mean (sd_num, sd_den) for beta_SD = E[num]/E[den]."""
    nums, dens = [], []
    if group == "U1":
        E = [np.exp(1j * cfg[..., nu]) for nu in range(4)]
        for mu in range(4):
            W = np.zeros_like(E[0])
            for nu in range(4):
                if nu == mu:
                    continue
                fwd = E[nu] * np.roll(E[mu], -1, axis=nu) * np.conj(np.roll(E[nu], -1, axis=mu))
                bwd = (
                    np.conj(np.roll(E[nu], 1, axis=nu))
                    * np.roll(E[mu], 1, axis=nu)
                    * np.roll(np.roll(E[nu], 1, axis=nu), -1, axis=mu)
                )
                W += fwd + bwd
            z = E[mu] * np.conj(W)
            nums.append(float(np.mean(np.real(z))))
            dens.append(float(np.mean(np.imag(z) ** 2)))
    elif group == "SU2":
        for mu in range(4):
            W = np.sum(su2_staples_list(cfg, mu), axis=-2)
            q = qmul(cfg[..., mu, :], qconj(W))
            nums.append(float(np.mean(3.0 * q[..., 0])))
            dens.append(float(np.mean(np.sum(q[..., 1:] ** 2, axis=-1))))
    else:
        for mu in range(4):
            M = so3_staples_sum(cfg, mu)
            A = cfg[..., mu, :, :] @ np.swapaxes(M, -1, -2)
            trA = np.trace(A, axis1=-2, axis2=-1)
            skew_sq = np.sum((A - np.swapaxes(A, -1, -2)) ** 2, axis=(-2, -1))
            nums.append(float(np.mean(12.0 * trA)))
            dens.append(float(np.mean(skew_sq)))
    return float(np.mean(nums)), float(np.mean(dens))


def measure_coarse_grid(cfg, group):
    """Measure SD terms, c_P, c_1x2, delta_blk, coarse 1+- correlator, and |Polyakov|."""
    L = cfg.shape[0]
    k_max = L // 2
    sd_num, sd_den = compute_beta_sd(cfg, group)

    if group == "U1":
        # 1x1 plaquettes (all 6) and 1+- spatial fluxes
        plaq_costs, sp_fluxes = [], []
        for mu in range(4):
            for nu in range(mu + 1, 4):
                th = cfg[..., mu] + np.roll(cfg[..., nu], -1, axis=mu) - np.roll(cfg[..., mu], -1, axis=nu) - cfg[..., nu]
                plaq_costs.append(1.0 - np.cos(th))
                if mu >= 1 and nu >= 1:
                    sp_fluxes.append(np.sin(th))
        c_P = float(np.mean(np.stack(plaq_costs, axis=-1)))

        # 1x2 planar rectangles (12 oriented rectangles)
        rect_costs = []
        l2 = [cfg[..., d] + np.roll(cfg[..., d], -1, axis=d) for d in range(4)]
        for mu in range(4):
            for nu in range(4):
                if mu == nu:
                    continue
                th12 = l2[mu] + np.roll(cfg[..., nu], -2, axis=mu) - np.roll(l2[mu], -1, axis=nu) - cfg[..., nu]
                rect_costs.append(1.0 - np.cos(th12))
        c_1x2 = float(np.mean(np.stack(rect_costs, axis=-1)))

        delta_blk = 0.0
        phi = np.stack(sp_fluxes, axis=-1)  # (L, L, L, L, 3)
        c_1pm = np.array([float(np.mean(phi * np.roll(phi, -k, axis=0))) for k in range(k_max + 1)])

        ph = np.exp(1j * (2.0 * math.pi / L) * np.arange(L))[None, :, None, None]
        o0 = np.sum(phi[..., 0] * ph, axis=(1, 2, 3))
        o1 = np.sum(phi[..., 1] * ph, axis=(1, 2, 3))
        c_pmin = np.array([
            0.5 * (
                float(np.mean(np.real(o0 * np.conj(np.roll(o0, -k)))))
                + float(np.mean(np.real(o1 * np.conj(np.roll(o1, -k)))))
            )
            for k in range(k_max + 1)
        ])

        p0 = np.zeros((L, L, L), dtype=float)
        for t in range(L):
            p0 += cfg[t, ..., 0]
        poly_abs = float(np.abs(np.mean(np.exp(1j * p0))))

    elif group == "SU2":
        # SU2 fundamental 1x1 & 1x2, adjoint SO(3) for delta_blk and 1+-
        plaq_costs = []
        for mu in range(4):
            for nu in range(mu + 1, 4):
                p = qmul(
                    qmul(cfg[..., mu, :], np.roll(cfg[..., nu, :], -1, axis=mu)),
                    qconj(qmul(cfg[..., nu, :], np.roll(cfg[..., mu, :], -1, axis=nu))),
                )
                plaq_costs.append(1.0 - p[..., 0])
        c_P = float(np.mean(np.stack(plaq_costs, axis=-1)))

        rect_costs = []
        l2_q = [qmul(cfg[..., d, :], np.roll(cfg[..., d, :], -1, axis=d)) for d in range(4)]
        for mu in range(4):
            for nu in range(4):
                if mu == nu:
                    continue
                p12 = qmul(
                    qmul(l2_q[mu], np.roll(cfg[..., nu, :], -2, axis=mu)),
                    qconj(qmul(cfg[..., nu, :], np.roll(l2_q[mu], -1, axis=nu))),
                )
                rect_costs.append(1.0 - p12[..., 0])
        c_1x2 = float(np.mean(np.stack(rect_costs, axis=-1)))

        R = q_to_so3(cfg)
        delta_blk, c_1pm = measure_so3_cocycle_and_1pm(R, L, k_max)
        c_pmin = None

        p0 = cfg[0, ..., 0, :].copy()
        for t in range(1, L):
            p0 = qmul(p0, cfg[t, ..., 0, :])
        poly_abs = float(np.abs(np.mean(p0[..., 0])))

    else:
        R = cfg
        Rl = [R[..., nu, :, :] for nu in range(4)]
        RlT = [np.swapaxes(r, -1, -2) for r in Rl]
        plaq_costs = []
        for mu in range(4):
            for nu in range(mu + 1, 4):
                p = Rl[mu] @ np.roll(Rl[nu], -1, axis=mu) @ np.roll(RlT[mu], -1, axis=nu) @ RlT[nu]
                plaq_costs.append(1.0 - np.trace(p, axis1=-2, axis2=-1) / 3.0)
        c_P = float(np.mean(np.stack(plaq_costs, axis=-1)))

        rect_costs = []
        l2_r = [Rl[d] @ np.roll(Rl[d], -1, axis=d) for d in range(4)]
        l2_rT = [np.swapaxes(r, -1, -2) for r in l2_r]
        for mu in range(4):
            for nu in range(4):
                if mu == nu:
                    continue
                p12 = l2_r[mu] @ np.roll(Rl[nu], -2, axis=mu) @ np.roll(l2_rT[mu], -1, axis=nu) @ RlT[nu]
                rect_costs.append(1.0 - np.trace(p12, axis1=-2, axis2=-1) / 3.0)
        c_1x2 = float(np.mean(np.stack(rect_costs, axis=-1)))

        delta_blk, c_1pm = measure_so3_cocycle_and_1pm(R, L, k_max)
        c_pmin = None

        p0 = R[0, ..., 0, :, :].copy()
        for t in range(1, L):
            p0 = p0 @ R[t, ..., 0, :, :]
        poly_abs = float(np.abs(np.mean(np.trace(p0, axis1=-2, axis2=-1) / 3.0)))

    return {
        "sd_num": sd_num,
        "sd_den": sd_den,
        "c_P": c_P,
        "c_1x2": c_1x2,
        "delta_blk": delta_blk,
        "c_1pm": c_1pm,
        "c_pmin": c_pmin,
        "poly_abs": poly_abs,
    }


def measure_so3_cocycle_and_1pm(R, L, k_max):
    """Coarse cocycle delta(W01 vs W12) and gauge-invariant coarse 1+- correlator."""
    Rl = [R[..., nu, :, :] for nu in range(4)]
    RlT = [np.swapaxes(r, -1, -2) for r in Rl]

    def plaq(mu, nu):
        return Rl[mu] @ np.roll(Rl[nu], -1, axis=mu) @ np.roll(RlT[mu], -1, axis=nu) @ RlT[nu]

    W01 = plaq(0, 1)
    W12 = plaq(1, 2)
    W13 = plaq(1, 3)
    W23 = plaq(2, 3)

    v12 = so3_dual_vec(W12)
    n12 = v12 / np.maximum(np.linalg.norm(v12, axis=-1, keepdims=True), 1e-12)
    n12_rot = np.einsum("...ij,...j->...i", W01, n12)
    delta_blk = float(np.mean(1.0 - np.sum(n12 * n12_rot, axis=-1)))

    phi = np.stack([v12, so3_dual_vec(W13), so3_dual_vec(W23)], axis=-2)  # (L,L,L,L,3,3)
    c_list = [float(np.mean(np.sum(phi * phi, axis=-1)))]
    R0 = Rl[0]
    T_cur = None
    for k in range(1, k_max + 1):
        T_cur = R0 if k == 1 else (T_cur @ np.roll(R0, -(k - 1), axis=0))
        phi_sh = np.roll(phi, -k, axis=0)
        phi_tr = np.einsum("...ij,...pj->...pi", T_cur, phi_sh)
        c_list.append(float(np.mean(np.sum(phi * phi_tr, axis=-1))))
    return delta_blk, np.array(c_list)


def extract_rho_gamma(C):
    c0 = max(abs(float(C[0])), 1e-15)
    r = [float(C[k]) / c0 for k in range(len(C))]
    rho1 = r[1] if len(r) > 1 else 0.0
    gamma_ge1 = sum((5.0 if k % 2 == 0 else 4.0) * abs(r[k]) for k in range(1, len(r)))
    return rho1, gamma_ge1


# ---------------------------------------------------------------------------
# Jackknife Aggregation & MCRG Matching Helpers
# ---------------------------------------------------------------------------
def jackknife_mean(arr):
    a = np.asarray(arr, dtype=float)
    n = len(a)
    mu = float(np.mean(a))
    if n <= 1:
        return mu, 0.0
    loo = (n * mu - a) / (n - 1)
    se = math.sqrt((n - 1) / n * float(np.sum((loo - mu) ** 2)))
    return mu, se


def jackknife_ratio(nums, dens):
    nv = np.asarray(nums, dtype=float)
    dv = np.asarray(dens, dtype=float)
    n = len(nv)
    sn, sd = float(np.sum(nv)), float(np.sum(dv))
    mu = sn / sd
    if n <= 1:
        return mu, 0.0
    loo = (sn - nv) / (sd - dv)
    se = math.sqrt((n - 1) / n * float(np.sum((loo - mu) ** 2)))
    return mu, se


def jackknife_ratio_diff(num_a, den_a, num_b, den_b):
    """Exact jackknife SE on difference of independent ratios mu_a - mu_b."""
    ma, sea = jackknife_ratio(num_a, den_a)
    mb, seb = jackknife_ratio(num_b, den_b)
    return ma - mb, math.hypot(sea, seb)


def jackknife_rho1_1pm(c_list):
    arr = np.asarray(c_list, dtype=float)
    n = len(arr)
    c_mean = np.mean(arr, axis=0)
    rho, gamma = extract_rho_gamma(c_mean)
    if n <= 1:
        return rho, 0.0, gamma
    s = np.sum(arr, axis=0)
    loo_r = []
    for i in range(n):
        ci = (s - arr[i]) / (n - 1)
        ri, _ = extract_rho_gamma(ci)
        loo_r.append(ri)
    loo_r = np.asarray(loo_r)
    se = math.sqrt((n - 1) / n * float(np.sum((loo_r - rho) ** 2)))
    return rho, se, gamma


def summarize_coarse_ensemble(records):
    sd_num = [r["sd_num"] for r in records]
    sd_den = [r["sd_den"] for r in records]
    beta_sd, beta_sd_err = jackknife_ratio(sd_num, sd_den)
    c_P, c_P_err = jackknife_mean([r["c_P"] for r in records])
    c_1x2, c_1x2_err = jackknife_mean([r["c_1x2"] for r in records])
    delta, delta_err = jackknife_mean([r["delta_blk"] for r in records])
    rho1, rho1_err, gamma1 = jackknife_rho1_1pm([r["c_1pm"] for r in records])
    poly, poly_err = jackknife_mean([r["poly_abs"] for r in records])
    pmin_rho, pmin_rho_err, pmin_g1 = (None, None, None)
    if records[0]["c_pmin"] is not None:
        pmin_rho, pmin_rho_err, pmin_g1 = jackknife_rho1_1pm([r["c_pmin"] for r in records])
    return {
        "sd_num": sd_num,
        "sd_den": sd_den,
        "beta_SD": (beta_sd, beta_sd_err),
        "c_P": (c_P, c_P_err),
        "c_1x2": (c_1x2, c_1x2_err),
        "delta_blk": (delta, delta_err),
        "rho_1pm": (rho1, rho1_err),
        "gamma_1pm": gamma1,
        "poly_abs": (poly, poly_err),
        "pmin_rho": (pmin_rho, pmin_rho_err),
        "pmin_g1": pmin_g1,
    }


def compute_mcrg_shift(target_val, target_err, beta_target, bracket_pts):
    """Piecewise-linear Swendsen MCRG match from 3 ordered bracket points [(b_i, v_i, e_i)]."""
    pts = sorted(bracket_pts, key=lambda x: x[0])
    b0, v0, e0 = pts[0]
    b1, v1, e1 = pts[1]
    b2, v2, e2 = pts[2]

    # Detect monotonic ordering (either increasing or decreasing with beta)
    inc = v2 > v0
    # Choose segment: check [b0, b1], [b1, b2], or extrapolate nearest end
    in_01 = (v0 <= target_val <= v1) if inc else (v0 >= target_val >= v1)
    in_12 = (v1 <= target_val <= v2) if inc else (v1 >= target_val >= v2)

    extrap = False
    if in_01:
        ba, va, ea, bb, vb, eb = b0, v0, e0, b1, v1, e1
    elif in_12:
        ba, va, ea, bb, vb, eb = b1, v1, e1, b2, v2, e2
    else:
        extrap = True
        if (target_val < v0) == inc:
            ba, va, ea, bb, vb, eb = b0, v0, e0, b1, v1, e1
        else:
            ba, va, ea, bb, vb, eb = b1, v1, e1, b2, v2, e2

    dv = vb - va
    db = bb - ba
    if abs(dv) < 1e-8 or (inc and dv <= 0.0) or ((not inc) and dv >= 0.0):
        return float("nan"), float("nan"), True
    t = (target_val - va) / dv
    beta_match = ba + t * db
    slope = dv / db
    var_y = target_err ** 2 + ((1.0 - t) * ea) ** 2 + (t * eb) ** 2
    err_match = math.sqrt(max(var_y, 0.0)) / abs(slope)
    return (beta_match - beta_target), err_match, extrap


def inv_g2_factor(group):
    if group == "U1":
        return 1.0
    elif group == "SU2":
        return 0.25
    return 2.0 / 3.0


def one_loop_dbeta(group):
    if group == "U1":
        return 0.0
    dg2 = -11.0 * math.log(2.0) / (12.0 * math.pi ** 2)
    return dg2 / inv_g2_factor(group)


# ---------------------------------------------------------------------------
# Monte Carlo Trajectory Runners
# ---------------------------------------------------------------------------
def sample_chain(rng, group, beta, L, n_therm, n_meas):
    parities = np.sum(np.indices((L, L, L, L)), axis=0) % 2
    if group == "U1":
        U = np.zeros((L, L, L, L, 4), dtype=float)
    else:
        U = np.zeros((L, L, L, L, 4, 4), dtype=float)
        U[..., 0] = 1.0

    for _ in range(n_therm):
        if group == "U1":
            u1_sweep(rng, U, parities, beta)
        elif group == "SU2":
            su2_sweep(rng, U, parities, beta)
        else:
            so3_sweep(rng, U, parities, beta, n_hits=4)

    snaps = []
    for _ in range(n_meas):
        if group == "U1":
            u1_sweep(rng, U, parities, beta)
            snaps.append(U.copy())
        elif group == "SU2":
            su2_sweep(rng, U, parities, beta)
            snaps.append(U.copy())
        else:
            so3_sweep(rng, U, parities, beta, n_hits=4)
            snaps.append(q_to_so3(U))
    return snaps


def block_and_summarize(snaps, group, n_steps, alpha_blk):
    records = []
    for cfg in snaps:
        cur = cfg
        for _ in range(n_steps):
            cur = block_config_2x(cur, group, alpha_blk)
        records.append(measure_coarse_grid(cur, group))
    return summarize_coarse_ensemble(records)


# ---------------------------------------------------------------------------
# Unit Tests: Exact Gauge & Z2 Invariance + Bare (b=1) SD Calibration
# ---------------------------------------------------------------------------
def verify_sd_and_observables(rng):
    max_u1 = max_su2 = max_so3_g = max_so3_z2 = 0.0
    L = 6
    U1 = rng.uniform(-math.pi, math.pi, size=(L, L, L, L, 4))
    g1 = rng.uniform(-math.pi, math.pi, size=(L, L, L, L))
    U1_g = np.stack([U1[..., mu] + g1 - np.roll(g1, -1, axis=mu) for mu in range(4)], axis=-1)

    U2 = random_su2(rng, (L, L, L, L, 4))
    g2 = random_su2(rng, (L, L, L, L))
    U2_g = np.stack([qmul(qmul(g2, U2[..., mu, :]), qconj(np.roll(g2, -1, axis=mu))) for mu in range(4)], axis=-2)

    signs = np.where(rng.random((L, L, L, L, 4, 1)) < 0.5, -1.0, 1.0)
    R3 = q_to_so3(U2)
    R3_g = q_to_so3(U2_g)
    R3_z2 = q_to_so3(U2 * signs)

    scalar_keys = ["sd_num", "sd_den", "c_P", "c_1x2", "delta_blk", "poly_abs"]
    for alpha in (0.20, 0.50):
        # Test on L=6 -> 3^4 blocked
        m1a = measure_coarse_grid(block_config_2x(U1, "U1", alpha), "U1")
        m1b = measure_coarse_grid(block_config_2x(U1_g, "U1", alpha), "U1")
        for k in scalar_keys + ["c_1pm", "c_pmin"]:
            max_u1 = max(max_u1, float(np.max(np.abs(np.asarray(m1a[k]) - np.asarray(m1b[k])))))

        m2a = measure_coarse_grid(block_config_2x(U2, "SU2", alpha), "SU2")
        m2b = measure_coarse_grid(block_config_2x(U2_g, "SU2", alpha), "SU2")
        for k in scalar_keys + ["c_1pm"]:
            max_su2 = max(max_su2, float(np.max(np.abs(np.asarray(m2a[k]) - np.asarray(m2b[k])))))

        m3a = measure_coarse_grid(block_config_2x(R3, "SO3", alpha), "SO3")
        m3g = measure_coarse_grid(block_config_2x(R3_g, "SO3", alpha), "SO3")
        m3z = measure_coarse_grid(block_config_2x(R3_z2, "SO3", alpha), "SO3")
        for k in scalar_keys + ["c_1pm"]:
            max_so3_g = max(max_so3_g, float(np.max(np.abs(np.asarray(m3a[k]) - np.asarray(m3g[k])))))
            max_so3_z2 = max(max_so3_z2, float(np.max(np.abs(np.asarray(m3a[k]) - np.asarray(m3z[k])))))

    # Also test bare L=6 directly (periodic boundary conditions)
    for grp, a, b in [("U1", U1, U1_g), ("SU2", U2, U2_g), ("SO3", R3, R3_g)]:
        ma = measure_coarse_grid(a, grp)
        mb = measure_coarse_grid(b, grp)
        for k in scalar_keys + ["c_1pm"]:
            val = float(np.max(np.abs(np.asarray(ma[k]) - np.asarray(mb[k]))))
            if grp == "U1":
                max_u1 = max(max_u1, val)
            elif grp == "SU2":
                max_su2 = max(max_su2, val)
            else:
                max_so3_g = max(max_so3_g, val)
    ma_z = measure_coarse_grid(R3, "SO3")
    mb_z = measure_coarse_grid(R3_z2, "SO3")
    for k in scalar_keys + ["c_1pm"]:
        max_so3_z2 = max(max_so3_z2, float(np.max(np.abs(np.asarray(ma_z[k]) - np.asarray(mb_z[k])))))

    assert max(max_u1, max_su2, max_so3_g, max_so3_z2) < 1e-12
    print(f"MCRG_INV_OK u1={max_u1:.1e} su2={max_su2:.1e} so3_g={max_so3_g:.1e} so3_z2={max_so3_z2:.1e}")

    # Bare (b=1) Schwinger-Dyson calibration on L=6
    print("\n=== BARE (b=1) SCHWINGER-DYSON CALIBRATION ON L=6 (therm=30, meas=40) ===")
    for group, beta_in in [("U1", 1.30), ("SU2", 3.00), ("SO3", 2.80)]:
        snaps = sample_chain(rng, group, beta_in, L=6, n_therm=30, n_meas=40)
        res = block_and_summarize(snaps, group, n_steps=0, alpha_blk=0.0)
        b_sd, b_se = res["beta_SD"]
        rel = abs(b_sd - beta_in) / beta_in
        print(f"  {group:3s} bare input={beta_in:.4f} -> beta_SD={b_sd:.4f} +/- {b_se:.4f} (rel_err={100*rel:.2f}%)")
        assert rel < 0.04, f"SD calibration failed for {group}: {rel:.3f}"


# ---------------------------------------------------------------------------
# Part 1: Free/Weak U(1) Blocking Kernel alpha* Calibration
# ---------------------------------------------------------------------------
def run_u1_alpha_calibration(rng):
    print("\n=== PART 1: U(1) (beta=2.00) BLOCKING-KERNEL alpha* CALIBRATION (Matched 3^4) ===")
    snaps_12 = sample_chain(rng, "U1", 2.00, L=12, n_therm=25, n_meas=40)
    snaps_6 = sample_chain(rng, "U1", 2.00, L=6, n_therm=40, n_meas=120)

    alphas = [0.00, 0.06, 0.10, 0.14, 0.18, 0.22, 0.30, 0.50]
    rows = []
    print("  alpha | beta_SD(12->3^4)    | beta_SD(6->3^4)     | Delta_beta_SD       | Delta_c_P")
    for al in alphas:
        r12 = block_and_summarize(snaps_12, "U1", n_steps=2, alpha_blk=al)
        r6 = block_and_summarize(snaps_6, "U1", n_steps=1, alpha_blk=al)
        b12, e12 = r12["beta_SD"]
        b6, e6 = r6["beta_SD"]
        db, edb = jackknife_ratio_diff(r12["sd_num"], r12["sd_den"], r6["sd_num"], r6["sd_den"])
        cp12, ecp12 = r12["c_P"]
        cp6, ecp6 = r6["c_P"]
        dcp = cp12 - cp6
        edcp = math.hypot(ecp12, ecp6)
        rows.append((al, db, dcp))
        print(
            f"  {al:5.2f} | {b12:7.4f} +/- {e12:6.4f} | {b6:7.4f} +/- {e6:6.4f} | "
            f"{db:+7.4f} +/- {edb:6.4f} | {dcp:+.5f} +/- {edcp:.5f}"
        )

    def zero_crossing(pts):
        for (a0, y0), (a1, y1) in zip(pts[:-1], pts[1:]):
            if y0 == 0.0:
                return a0
            if (y0 < 0.0 < y1) or (y0 > 0.0 > y1):
                return a0 - y0 * (a1 - a0) / (y1 - y0)
        return None

    a_sd = zero_crossing([(al, db) for al, db, _ in rows])
    a_cp = zero_crossing([(al, dcp) for al, _, dcp in rows])
    alpha_star = 0.20 if a_sd is None else round(min(max(a_sd, 0.05), 0.45), 3)
    print(
        f"  -> U(1) zero-crossings: alpha_SD*={a_sd if a_sd is not None else float('nan'):.4f}, "
        f"alpha_P*={a_cp if a_cp is not None else float('nan'):.4f}; selected alpha*={alpha_star:.3f}"
    )
    return alpha_star


# ---------------------------------------------------------------------------
# Shared Report Formatting for Matched-Volume Runs
# ---------------------------------------------------------------------------
def evaluate_matched_pair(group, beta_target, snaps_big, snaps_brackets, alpha, L_big, L_small):
    L_b = L_big // 4
    b_lbl = "bA" if group == "SO3" else "beta"
    s12 = block_and_summarize(snaps_big, group, n_steps=2, alpha_blk=alpha)

    br_summ = {}
    for bp, sn in sorted(snaps_brackets.items()):
        br_summ[bp] = block_and_summarize(sn, group, n_steps=1, alpha_blk=alpha)

    s6 = br_summ[beta_target]
    f_g2 = inv_g2_factor(group)
    db_1loop = one_loop_dbeta(group)
    dg2_1loop = db_1loop * f_g2

    db_sd, db_sd_err = jackknife_ratio_diff(s12["sd_num"], s12["sd_den"], s6["sd_num"], s6["sd_den"])
    dg2_sd, dg2_sd_err = db_sd * f_g2, db_sd_err * f_g2

    print(f"    [alpha={alpha:.3f} | 1-loop 2x ref: d{b_lbl}={db_1loop:+.4f}, d(1/g^2)={dg2_1loop:+.4f}]")
    print(
        f"      Direct {L_big}->{L_b}^4 vs {L_small}->{L_b}^4 @ {b_lbl}={beta_target:.2f}:\n"
        f"        beta_SD  : {s12['beta_SD'][0]:6.4f}+/-{s12['beta_SD'][1]:.4f} vs {s6['beta_SD'][0]:6.4f}+/-{s6['beta_SD'][1]:.4f} "
        f"| Delta={db_sd:+.4f}+/-{db_sd_err:.4f} | d(1/g^2)={dg2_sd:+.4f}+/-{dg2_sd_err:.4f}\n"
        f"        c_P      : {s12['c_P'][0]:.5f}+/-{s12['c_P'][1]:.5f} vs {s6['c_P'][0]:.5f}+/-{s6['c_P'][1]:.5f}\n"
        f"        c_1x2    : {s12['c_1x2'][0]:.5f}+/-{s12['c_1x2'][1]:.5f} vs {s6['c_1x2'][0]:.5f}+/-{s6['c_1x2'][1]:.5f}\n"
        f"        delta_blk: {s12['delta_blk'][0]:.5f}+/-{s12['delta_blk'][1]:.5f} vs {s6['delta_blk'][0]:.5f}+/-{s6['delta_blk'][1]:.5f}\n"
        f"        rho_1pm  : {s12['rho_1pm'][0]:+.4f}+/-{s12['rho_1pm'][1]:.4f} (G1={s12['gamma_1pm']:.3f}) "
        f"vs {s6['rho_1pm'][0]:+.4f}+/-{s6['rho_1pm'][1]:.4f} (G1={s6['gamma_1pm']:.3f})\n"
        f"        poly_abs : {s12['poly_abs'][0]:.4f}+/-{s12['poly_abs'][1]:.4f} vs {s6['poly_abs'][0]:.4f}+/-{s6['poly_abs'][1]:.4f}"
    )
    if group == "U1":
        print(
            f"        U1_pmin  : {s12['pmin_rho'][0]:+.4f} (G1={s12['pmin_g1']:.3f}) "
            f"vs {s6['pmin_rho'][0]:+.4f} (G1={s6['pmin_g1']:.3f})"
        )

    # Swendsen MCRG 3-point bracket shifts
    obs_list = ["beta_SD", "c_P", "c_1x2"] + (["delta_blk"] if group != "U1" else [])
    mcrg_parts = []
    for obs in obs_list:
        val12, err12 = s12[obs]
        pts = [(bp, br_summ[bp][obs][0], br_summ[bp][obs][1]) for bp in sorted(br_summ)]
        db_m, eb_m, ex = compute_mcrg_shift(val12, err12, beta_target, pts)
        tag = "*" if ex else ""
        if math.isnan(db_m):
            mcrg_parts.append(f"{obs}=nan")
        else:
            mcrg_parts.append(
                f"{obs}:{db_m:+.3f}+/-{eb_m:.3f}{tag}(dg2={db_m * f_g2:+.4f})"
            )
    print(f"      Swendsen MCRG d{b_lbl}_2x: " + " | ".join(mcrg_parts))


# ---------------------------------------------------------------------------
# Part 2 & Part 3 Suites
# ---------------------------------------------------------------------------
def run_matched_3_suite(rng, alpha_star):
    print("\n=== PART 2: MATCHED-3^4 MCRG & SCHWINGER-DYSON SUITE (L=12,b=4 vs L=6,b=2) ===")
    configs = [
        ("U1", 1.30, 25, 36, 40, 100, [1.15, 1.30, 1.45]),
        ("U1", 2.00, 25, 36, 40, 100, [1.85, 2.00, 2.15]),
        ("SU2", 2.50, 25, 32, 40, 100, [2.00, 2.25, 2.50]),
        ("SU2", 3.00, 25, 32, 40, 100, [2.50, 2.75, 3.00]),
        ("SU2", 4.00, 25, 32, 40, 100, [3.50, 3.75, 4.00]),
        ("SO3", 2.80, 25, 30, 40, 100, [2.56, 2.68, 2.80]),
        ("SO3", 4.00, 25, 30, 40, 100, [3.76, 3.88, 4.00]),
    ]
    for group, beta_t, t12, m12, t6, m6, br_betas in configs:
        pt0 = time.time()
        b_lbl = "bA" if group == "SO3" else "beta"
        snaps_12 = sample_chain(rng, group, beta_t, L=12, n_therm=t12, n_meas=m12)
        snaps_br = {bp: sample_chain(rng, group, bp, L=6, n_therm=t6, n_meas=m6) for bp in br_betas}
        print(f"\n  >>> {group} {b_lbl}={beta_t:.2f} (MCMC+blk {time.time() - pt0:.1f}s setup) <<<")
        alphas = [alpha_star] + ([0.15] if abs(alpha_star - 0.15) >= 0.02 else []) + [0.50]
        for al in alphas:
            evaluate_matched_pair(group, beta_t, snaps_12, snaps_br, al, L_big=12, L_small=6)


def run_matched_4_spotcheck(rng, alpha_star):
    print("\n=== PART 3: MATCHED-4^4 FINITE-VOLUME SPOT CHECK (L=16,b=4 vs L=8,b=2) ===")
    configs = [
        ("U1", 1.30, 20, 20, 30, 50, [1.15, 1.30, 1.45]),
        ("SU2", 3.00, 16, 16, 30, 50, [2.50, 2.75, 3.00]),
    ]
    alphas = [alpha_star] + ([0.15] if abs(alpha_star - 0.15) >= 0.02 else []) + [0.50]
    for group, beta_t, t16, m16, t8, m8, br_betas in configs:
        pt0 = time.time()
        b_lbl = "bA" if group == "SO3" else "beta"
        snaps_16 = sample_chain(rng, group, beta_t, L=16, n_therm=t16, n_meas=m16)
        snaps_br = {bp: sample_chain(rng, group, bp, L=8, n_therm=t8, n_meas=m8) for bp in br_betas}
        print(f"\n  >>> {group} {b_lbl}={beta_t:.2f} MATCHED-4^4 (MCMC {time.time() - pt0:.1f}s) <<<")
        for al in alphas:
            evaluate_matched_pair(group, beta_t, snaps_16, snaps_br, al, L_big=16, L_small=8)


def main():
    t0 = time.time()
    rng = np.random.default_rng(17720)
    verify_sd_and_observables(rng)
    alpha_star = run_u1_alpha_calibration(rng)
    run_matched_3_suite(rng, alpha_star)
    run_matched_4_spotcheck(rng, alpha_star)
    print(f"\nPROBE_MCRG_SD_DONE elapsed={time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
