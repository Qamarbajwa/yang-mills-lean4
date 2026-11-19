"""Focused Deep Test (Tests A & B) on Walls 1-2:
Test A: Exact gauge-invariant r x 1 strip & r x r area cocycle progression BEFORE saturation
        at weak/crossover couplings (U(1), SU(2), adjoint SO(3)) with zero gauge fixing.
        Verifies pointwise YM142 identity delta_{WV} = delta_V + delta_W - delta_V*delta_W + eps_corr.
Test B: Exact zero-Gribov 4D 1-vertex K_{2,2,2,2} reduced star (V_1..V_7 | W_partial) comparing
        flat vs pi-flux/frustrated vs thermalized 4D L=6 boundary ensembles:
        - Conditional opposite-face (+/-t) correlation & Dobrushin sensitivity chi_{partial->partial}
        - Conditional star potential Hessian lambda_min (relaxed minimum) vs intrinsic Ricci curvature.
"""

import math
import time
import numpy as np


# ---------------------------------------------------------------------------
# Group & Lattice Helpers
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


def u1_staple_complex(U, mu):
    S = np.zeros_like(U[..., 0], dtype=complex)
    E = [np.exp(1j * U[..., nu]) for nu in range(4)]
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
    return S


def u1_sweep(rng, U, parities, beta):
    for mu in range(4):
        for parity in (0, 1):
            S = u1_staple_complex(U, mu)
            mask = parities == parity
            Sm = S[mask]
            amp = np.abs(Sm)
            ang = np.angle(Sm)
            U[mask, mu] = ang + rng.vonmises(np.zeros_like(amp), np.maximum(beta * amp, 1e-12))


def su2_staples_list(U, mu):
    U_nu = [U[..., nu, :] for nu in range(4)]
    st_list = []
    for nu in range(4):
        if nu == mu:
            continue
        fwd = qmul(
            qmul(U_nu[nu], np.roll(U_nu[mu], -1, axis=nu)),
            qconj(np.roll(U_nu[nu], -1, axis=mu)),
        )
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
    X = np.stack([
        x0,
        r_vec * sin_th * np.cos(phi),
        r_vec * sin_th * np.sin(phi),
        r_vec * z_ang,
    ], axis=-1)
    return qmul(X, V)


def su2_sweep(rng, U, parities, beta):
    for mu in range(4):
        for parity in (0, 1):
            S = np.sum(su2_staples_list(U, mu), axis=-2)
            mask = parities == parity
            U[mask, mu, :] = su2_kp_sample_vec(rng, S[mask], beta)


def so3_sweep(rng, U, parities, beta_A, n_hits=6):
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
# TEST A: Exact Gauge-Invariant Strip & Area Cocycle Growth BEFORE Saturation
# ---------------------------------------------------------------------------
def rect_holonomy(U, ax1, ax2, r1, r2):
    """Exact gauge-invariant r1 x r2 Wilson loop L(x) in plane (ax1, ax2) based at x:
    W_{r1}(x) * U_{r2, ax2}(x + r1*ax1) * W_{r1}(x + r2*ax2)^(-1) * U_{r2, ax2}(x)^(-1).
    """
    def path_prod(link, axis, r):
        cur = link
        for k in range(1, r):
            cur = qmul(cur, np.roll(link, -k, axis=axis))
        return cur

    w_bot = path_prod(U[..., ax1, :], ax1, r1)
    u_rgt = path_prod(U[..., ax2, :], ax2, r2)
    w_top = np.roll(w_bot, -r2, axis=ax2)
    u_rgt_shifted = np.roll(u_rgt, -r1, axis=ax1)
    return qmul(qmul(w_bot, u_rgt_shifted), qconj(qmul(u_rgt, w_top)))


def commutator_delta(L_loop, n_hat):
    """Exact YM142 normalized commutator loss:
    delta_U(X) = ||[R(U), L(n_hat)]||_F^2 / (2 ||L(n_hat)||_F^2) = 1 - n_hat . (R(U) n_hat) in [0, 2].
    Invariant under U -> -U (purely SO(3)/SU(2)/Z2) and g(x) U g(x)^(-1), g(x) X g(x)^(-1)!
    """
    Ru = q_to_so3(L_loop)
    n_rot = np.einsum("...ij,...j->...i", Ru, n_hat)
    return 1.0 - np.sum(n_hat * n_rot, axis=-1)


def measure_cocycle_progression(U):
    # Curvature generator X(x) from local spatial (1, 2) plaquette; axis n_hat = vec / ||vec||
    P12 = rect_holonomy(U, 1, 2, 1, 1)
    vec = P12[..., 1:]
    vnorm = np.linalg.norm(vec, axis=-1, keepdims=True)
    n_hat = vec / np.maximum(vnorm, 1e-12)

    # Strip holonomies in (1, 3) plane at r = 1, 2, 4
    L11 = rect_holonomy(U, 1, 3, 1, 1)
    L21 = rect_holonomy(U, 1, 3, 2, 1)
    L41 = rect_holonomy(U, 1, 3, 4, 1)

    # Exact YM142 horizontal doubling identity: L21 = W * V
    u1_len1 = U[..., 1, :]
    V1 = L11
    W1 = qmul(qmul(u1_len1, np.roll(L11, -1, axis=1)), qconj(u1_len1))
    id_err_12 = float(np.max(np.abs(qmul(W1, V1) - L21)))

    u1_len2 = qmul(u1_len1, np.roll(u1_len1, -1, axis=1))
    V2 = L21
    W2 = qmul(qmul(u1_len2, np.roll(L21, -2, axis=1)), qconj(u1_len2))
    id_err_24 = float(np.max(np.abs(qmul(W2, V2) - L41)))

    # Vertical strip thickening: L12 = B * T
    L12 = rect_holonomy(U, 1, 3, 1, 2)
    L22 = rect_holonomy(U, 1, 3, 2, 2)
    L44 = rect_holonomy(U, 1, 3, 4, 4)
    u3_len1 = U[..., 3, :]
    T1 = qmul(qmul(u3_len1, np.roll(L11, -1, axis=3)), qconj(u3_len1))
    id_err_v12 = float(np.max(np.abs(qmul(L11, T1) - L12)))

    assert max(id_err_12, id_err_24, id_err_v12) < 1e-13

    d11 = commutator_delta(L11, n_hat)
    dW1 = commutator_delta(W1, n_hat)
    d21 = commutator_delta(L21, n_hat)
    eps12 = d21 - (d11 + dW1 - d11 * dW1)

    dW2 = commutator_delta(W2, n_hat)
    d41 = commutator_delta(L41, n_hat)
    eps24 = d41 - (d21 + dW2 - d21 * dW2)

    dT1 = commutator_delta(T1, n_hat)
    d12 = commutator_delta(L12, n_hat)
    eps_v12 = d12 - (d11 + dT1 - d11 * dT1)

    d22 = commutator_delta(L22, n_hat)
    d44 = commutator_delta(L44, n_hat)

    # Check pointwise YM142 identity against explicit inner product <R(W) Delta_V(X), Delta_W(X)> / ||X||^2
    Ru_W1 = q_to_so3(W1)
    Ru_V1 = q_to_so3(V1)
    n_V1 = np.einsum("...ij,...j->...i", Ru_V1, n_hat)
    n_WV1 = np.einsum("...ij,...j->...i", Ru_W1, n_V1)
    n_W1 = np.einsum("...ij,...j->...i", Ru_W1, n_hat)
    inner_term = np.sum((n_WV1 - n_W1) * (n_W1 - n_hat), axis=-1)
    ym142_pt_err = float(np.max(np.abs(eps12 - (inner_term + d11 * dW1))))
    assert ym142_pt_err < 1e-13

    m_d11 = float(np.mean(d11))
    m_d21 = float(np.mean(d21))
    m_d41 = float(np.mean(d41))
    m_d12 = float(np.mean(d12))
    m_d22 = float(np.mean(d22))
    m_d44 = float(np.mean(d44))
    m_eps12 = float(np.mean(eps12))
    m_eps24 = float(np.mean(eps24))
    m_eps_v = float(np.mean(eps_v12))
    # Linear survival ratio c_eff = (d_{2r} - d_r) / (d_r * (1 - d_r))
    c_12 = (m_d21 - m_d11) / max(m_d11 * (1.0 - m_d11), 1e-12)
    c_24 = (m_d41 - m_d21) / max(m_d21 * (1.0 - m_d21), 1e-12)
    return {
        "pt_err": max(id_err_12, id_err_24, id_err_v12, ym142_pt_err),
        "d11": m_d11, "d21": m_d21, "d41": m_d41,
        "d12": m_d12, "d22": m_d22, "d44": m_d44,
        "eps12": m_eps12, "eps24": m_eps24, "eps_v": m_eps_v,
        "c_12": c_12, "c_24": c_24,
        "area_vs_strip": m_d22 / max(m_d21, 1e-12),
    }


def run_test_a():
    rng = np.random.default_rng(17640)
    L = 8
    parities = np.sum(np.indices((L, L, L, L)), axis=0) % 2
    print("=== TEST A: PRE-SATURATION STRIP & AREA COCYCLE GROWTH (L=8, 0-Gribov GI) ===")
    print("  Note: U(1) yields delta_U(X) == 0.0000 identically for all loops (r x s) & all beta.")

    max_pt_err = 0.0
    print("\n  SU(2) 4D (beta = 2.2 .. 8.0):")
    for beta in [2.2, 2.5, 4.0, 6.0, 8.0]:
        U = np.zeros((L, L, L, L, 4, 4), dtype=float)
        U[..., 0] = 1.0
        for _ in range(25):
            su2_sweep(rng, U, parities, beta)
        accs = []
        for _ in range(15):
            su2_sweep(rng, U, parities, beta)
            accs.append(measure_cocycle_progression(U))
        agg = {k: float(np.mean([a[k] for a in accs])) for k in accs[0]}
        max_pt_err = max(max_pt_err, max(a["pt_err"] for a in accs))
        print(
            f"    beta={beta:4.1f}  strip(1->2->4)=({agg['d11']:.4f} -> {agg['d21']:.4f} -> {agg['d41']:.4f})  "
            f"area(1->2->4)=({agg['d11']:.4f} -> {agg['d22']:.4f} -> {agg['d44']:.4f})  "
            f"eps(12,24,v)=({agg['eps12']:+.4f}, {agg['eps24']:+.4f}, {agg['eps_v']:+.4f})  "
            f"c_eff=({agg['c_12']:.3f},{agg['c_24']:.3f})  d22/d21={agg['area_vs_strip']:.3f}"
        )

    print("\n  Adjoint SO(3) 4D continuum side (beta_A = 2.8 .. 6.0):")
    for beta_A in [2.8, 4.0, 6.0]:
        U = np.zeros((L, L, L, L, 4, 4), dtype=float)
        U[..., 0] = 1.0
        for _ in range(30):
            so3_sweep(rng, U, parities, beta_A, n_hits=6)
        accs = []
        for _ in range(15):
            so3_sweep(rng, U, parities, beta_A, n_hits=6)
            accs.append(measure_cocycle_progression(U))
        agg = {k: float(np.mean([a[k] for a in accs])) for k in accs[0]}
        max_pt_err = max(max_pt_err, max(a["pt_err"] for a in accs))
        print(
            f"    bA  ={beta_A:4.1f}  strip(1->2->4)=({agg['d11']:.4f} -> {agg['d21']:.4f} -> {agg['d41']:.4f})  "
            f"area(1->2->4)=({agg['d11']:.4f} -> {agg['d22']:.4f} -> {agg['d44']:.4f})  "
            f"eps(12,24,v)=({agg['eps12']:+.4f}, {agg['eps24']:+.4f}, {agg['eps_v']:+.4f})  "
            f"c_eff=({agg['c_12']:.3f},{agg['c_24']:.3f})  d22/d21={agg['area_vs_strip']:.3f}"
        )
    print(f"  YM142 pointwise gauge-invariant identity max error: {max_pt_err:.2e}")


# ---------------------------------------------------------------------------
# TEST B: Exact Zero-Gribov 1-Vertex 4D Star Boundary-to-Boundary Influence
# ---------------------------------------------------------------------------
def build_star_graph():
    # 8 links a=0..7 corresponding to (mu=a//2, s=+1 if a%2==0 else -1)
    # a=0: +t, a=1: -t, a=2,3: +/-x, a=4,5: +/-y, a=6,7: +/-z
    edges = [(a, b) for a in range(8) for b in range(a + 1, 8) if (a // 2) != (b // 2)]
    inc = {v: [] for v in range(1, 8)}
    for idx, (a, b) in enumerate(edges):
        if a > 0:
            inc[a].append((idx, b, True))
        if b > 0:
            inc[b].append((idx, a, False))
    top_idxs = [idx for idx, (a, b) in enumerate(edges) if a == 0]
    bot_idxs = [idx for idx, (a, b) in enumerate(edges) if a == 1]
    assert len(top_idxs) == 6 and len(bot_idxs) == 6
    return edges, inc, top_idxs, bot_idxs


def extract_thermal_boundary(rng, group, beta, L=6):
    """Run L=6 4D simulation and extract the 24 boundary corner paths W_{ab} around site x0=(1,1,1,1)."""
    edges, _, _, _ = build_star_graph()
    parities = np.sum(np.indices((L, L, L, L)), axis=0) % 2
    x0 = np.array([1, 1, 1, 1])

    def vec_dir(a):
        v = np.zeros(4, dtype=int)
        v[a // 2] = 1 if (a % 2 == 0) else -1
        return v

    if group == "U1":
        U = np.zeros((L, L, L, L, 4), dtype=float)
        for _ in range(30):
            u1_sweep(rng, U, parities, beta)
        def step(pos, a):
            mu = a // 2
            p = pos % L
            if a % 2 == 0:
                return float(U[p[0], p[1], p[2], p[3], mu])
            q = (pos + vec_dir(a)) % L     # Since vec_dir(a) = -e_mu when a%2==1!
            return -float(U[q[0], q[1], q[2], q[3], mu])
        W = np.empty(24, dtype=float)
        for idx, (a, b) in enumerate(edges):
            # W_{ab} = step(x0 + e_a, b) - step(x0 + e_b, a)
            W[idx] = step(x0 + vec_dir(a), b) - step(x0 + vec_dir(b), a)
        return W
    else:
        U = np.zeros((L, L, L, L, 4, 4), dtype=float)
        U[..., 0] = 1.0
        for _ in range(35):
            if group == "SU2":
                su2_sweep(rng, U, parities, beta)
            else:
                so3_sweep(rng, U, parities, beta, n_hits=6)
        def step_q(pos, a):
            mu = a // 2
            if a % 2 == 0:
                p = pos % L
                return U[p[0], p[1], p[2], p[3], mu, :]
            q = (pos + vec_dir(a)) % L
            return qconj(U[q[0], q[1], q[2], q[3], mu, :])
        W = np.empty((24, 4), dtype=float)
        for idx, (a, b) in enumerate(edges):
            W[idx] = qmul(step_q(x0 + vec_dir(a), b), qconj(step_q(x0 + vec_dir(b), a)))
        return W


def star_observables_u1(rng, edges, inc, top_idxs, bot_idxs, W, beta, n_therm=400, n_meas=2500):
    V = np.zeros(8, dtype=float)
    def plaqs(v_arr):
        return np.array([v_arr[a] + W[idx] - v_arr[b] for idx, (a, b) in enumerate(edges)])
    def total_action(v_arr):
        return beta * float(np.sum(1.0 - np.cos(plaqs(v_arr))))

    # Relax from 0 to check saddle/minimum Hessian
    Vr = np.zeros(8, dtype=float)
    for _ in range(60):
        for v in range(1, 8):
            num = sum((W[idx] - Vr[other]) if is_l else (Vr[other] + W[idx]) for idx, other, is_l in inc[v])
            # Exact gradient 0 for quadratic part, refine with 1D Newton on cos
            num_s = sum(math.sin(Vr[v] + W[idx] - Vr[o]) if is_l else math.sin(Vr[v] - Vr[o] - W[idx])
                        for idx, o, is_l in inc[v])
            den_c = sum(math.cos(Vr[v] + W[idx] - Vr[o]) if is_l else math.cos(Vr[v] - Vr[o] - W[idx])
                        for idx, o, is_l in inc[v])
            if abs(den_c) > 1e-8:
                Vr[v] -= num_s / max(abs(den_c), 0.5)
    H = np.zeros((7, 7), dtype=float)
    eps = 1e-4
    for i in range(7):
        ei = np.zeros(8); ei[i + 1] = eps
        for j in range(i, 7):
            ej = np.zeros(8); ej[j + 1] = eps
            val = (total_action(Vr + ei + ej) - total_action(Vr + ei - ej)
                   - total_action(Vr - ei + ej) + total_action(Vr - ei - ej)) / (4.0 * eps * eps)
            H[i, j] = H[j, i] = val
    lam_min = float(np.min(np.linalg.eigvalsh(H)))

    # MCMC on reduced U(1)^7 star using exact von Mises conditional updates
    ot_list, ob_list = [], []
    for sw in range(n_therm + n_meas):
        for v in range(1, 8):
            s_c = 0.0 + 0.0j
            for idx, other, is_left in inc[v]:
                ang = (V[other] - W[idx]) if is_left else (V[other] + W[idx])
                s_c += np.exp(1j * ang)
            amp = abs(s_c)
            V[v] = np.angle(s_c) + rng.vonmises(0.0, max(beta * amp, 1e-12))
        if sw >= n_therm:
            c_all = 1.0 - np.cos(plaqs(V))
            ot_list.append(float(np.mean(c_all[top_idxs])))
            ob_list.append(float(np.mean(c_all[bot_idxs])))
    ot = np.array(ot_list); ob = np.array(ob_list)
    cov = float(np.mean((ot - np.mean(ot)) * (ob - np.mean(ob))))
    std_t = max(float(np.std(ot)), 1e-12); std_b = max(float(np.std(ob)), 1e-12)
    rho_corr = cov / (std_t * std_b)
    chi_sens = beta * 6.0 * abs(cov)
    return rho_corr, chi_sens, lam_min


def su2_kp_single(rng, st, beta):
    sn = float(np.linalg.norm(st))
    alpha = beta * max(sn, 1e-30)
    V = st / max(sn, 1e-30)
    while True:
        r1 = max(rng.random(), 1e-15); r2 = max(rng.random(), 1e-15)
        r3 = rng.random(); r4 = rng.random()
        lam2 = -(math.log(r1) + math.log(r2) * (math.cos(2.0 * math.pi * r3) ** 2)) / (2.0 * alpha)
        if lam2 <= 1.0 and r4 * r4 <= 1.0 - lam2:
            break
    x0 = 1.0 - 2.0 * lam2
    rv = math.sqrt(max(1.0 - x0 * x0, 0.0))
    z = rng.uniform(-1.0, 1.0); phi = rng.uniform(0.0, 2.0 * math.pi)
    sth = math.sqrt(max(1.0 - z * z, 0.0))
    X = np.array([x0, rv * sth * math.cos(phi), rv * sth * math.sin(phi), rv * z])
    return qmul(X, V)


def star_observables_nonabelian(rng, group, edges, inc, top_idxs, bot_idxs, W, beta, n_therm=400, n_meas=2500):
    V = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (8, 1))
    coeff = beta if group == "SU2" else (4.0 / 3.0) * beta

    def total_action(v_arr):
        tot = 0.0
        for idx, (a, b) in enumerate(edges):
            p = qmul(qmul(v_arr[a], W[idx]), qconj(v_arr[b]))
            tot += beta * (1.0 - float(p[0])) if group == "SU2" else coeff * (1.0 - float(p[0]) ** 2)
        return tot

    # Relax Vr with sweeps toward local minimum for tangent Hessian calculation
    Vr = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (8, 1))
    for _ in range(40):
        for v in range(1, 8):
            if group == "SU2":
                st = np.zeros(4)
                for idx, o, is_l in inc[v]:
                    st += qmul(Vr[o], qconj(W[idx])) if is_l else qmul(Vr[o], W[idx])
                sn = float(np.linalg.norm(st))
                if sn > 1e-12:
                    Vr[v] = st / sn
            else:
                vs = [qmul(Vr[o], qconj(W[idx])) if is_l else qmul(Vr[o], W[idx]) for idx, o, is_l in inc[v]]
                Q = np.stack(vs, axis=0)
                Qmat = Q.T @ Q
                _, ev = np.linalg.eigh(Qmat)
                cand = ev[:, 3]
                if float(cand @ Vr[v]) < 0:
                    cand = -cand
                Vr[v] = cand

    def apply_tan(v_arr, eta):
        # eta has shape (7, 3), exponential map u' = exp(eta) * u
        out = v_arr.copy()
        for v in range(1, 8):
            th = float(np.linalg.norm(eta[v - 1]))
            if th < 1e-12:
                dq = np.array([1.0, 0.0, 0.0, 0.0])
            else:
                ax = eta[v - 1] / th
                dq = np.array([math.cos(th), math.sin(th) * ax[0], math.sin(th) * ax[1], math.sin(th) * ax[2]])
            out[v] = qmul(dq, out[v])
        return out

    H = np.zeros((21, 21), dtype=float)
    eps = 2e-4
    for i in range(21):
        ei = np.zeros((7, 3)); ei[i // 3, i % 3] = eps
        for j in range(i, 21):
            ej = np.zeros((7, 3)); ej[j // 3, j % 3] = eps
            val = (total_action(apply_tan(Vr, ei + ej)) - total_action(apply_tan(Vr, ei - ej))
                   - total_action(apply_tan(Vr, -ei + ej)) + total_action(apply_tan(Vr, -ei - ej))) / (4.0 * eps * eps)
            H[i, j] = H[j, i] = val
    lam_min = float(np.min(np.linalg.eigvalsh(H)))

    ot_list, ob_list = [], []
    for sw in range(n_therm + n_meas):
        for v in range(1, 8):
            if group == "SU2":
                st = np.zeros(4)
                for idx, o, is_l in inc[v]:
                    st += qmul(V[o], qconj(W[idx])) if is_l else qmul(V[o], W[idx])
                V[v] = su2_kp_single(rng, st, beta)
            else:
                vs = [qmul(V[o], qconj(W[idx])) if is_l else qmul(V[o], W[idx]) for idx, o, is_l in inc[v]]
                Vs = np.stack(vs, axis=0)
                Q = Vs.T @ Vs
                for _ in range(5):
                    g = rng.normal(scale=0.45, size=4); g[0] += 1.0
                    g /= np.linalg.norm(g)
                    prop = qmul(g, V[v])
                    dE = coeff * float(prop @ Q @ prop - V[v] @ Q @ V[v])
                    if dE >= 0.0 or rng.random() < math.exp(dE):
                        V[v] = prop
        if sw >= n_therm:
            p0s = np.array([float(qmul(qmul(V[a], W[idx]), qconj(V[b]))[0]) for idx, (a, b) in enumerate(edges)])
            c_all = (1.0 - p0s) if group == "SU2" else (4.0 / 3.0) * (1.0 - p0s * p0s)
            ot_list.append(float(np.mean(c_all[top_idxs])))
            ob_list.append(float(np.mean(c_all[bot_idxs])))
    ot = np.array(ot_list); ob = np.array(ob_list)
    cov = float(np.mean((ot - np.mean(ot)) * (ob - np.mean(ob))))
    std_t = max(float(np.std(ot)), 1e-12); std_b = max(float(np.std(ob)), 1e-12)
    rho_corr = cov / (std_t * std_b)
    chi_sens = beta * 6.0 * abs(cov)
    return rho_corr, chi_sens, lam_min


def run_test_b():
    rng = np.random.default_rng(17650)
    edges, inc, top_idxs, bot_idxs = build_star_graph()

    print("\n=== TEST B: EXACT 1-VERTEX K_{2,2,2,2} STAR BOUNDARY SENSITIVITY & HESSIAN (Ricci vs Frustration) ===")

    # 1. U(1): flat, pi-flux frustrated, and thermalized boundaries
    W_u1_flat = np.zeros(24, dtype=float)
    W_u1_pi = np.array([math.pi if (idx % 2 == 1) else 0.0 for idx in range(24)], dtype=float)
    print("\n  U(1) Star (Ric(S^1) = 0):")
    for label, b, W in [
        ("Flat W=I", 1.01, W_u1_flat),
        ("Pi-Flux W", 1.01, W_u1_pi),
        ("Thermal b=0.80", 0.80, extract_thermal_boundary(rng, "U1", 0.80)),
        ("Thermal b=1.10", 1.10, extract_thermal_boundary(rng, "U1", 1.10)),
        ("Thermal b=6.00", 6.00, extract_thermal_boundary(rng, "U1", 6.00)),
    ]:
        rho, chi, lmin = star_observables_u1(rng, edges, inc, top_idxs, bot_idxs, W, b)
        print(f"    {label:16s} beta={b:4.2f}  rho_+-t={rho:+.4f}  chi_d->d={chi:.4f}  Hess_lam_min={lmin:+.3f}")

    # 2. SU(2): flat, frustrated non-commuting pi/2, and thermalized boundaries
    W_su2_flat = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (24, 1))
    qx = np.array([math.cos(math.pi / 4.0), math.sin(math.pi / 4.0), 0.0, 0.0])  # pi/2 rot around x
    qy = np.array([math.cos(math.pi / 4.0), 0.0, math.sin(math.pi / 4.0), 0.0])  # pi/2 rot around y
    qz = np.array([0.0, 0.0, 0.0, 1.0])  # pi Z2 monopole flux
    W_su2_frust = np.stack([[qx, qy, qz][idx % 3] for idx in range(24)], axis=0)
    print("\n  SU(2) Star (Ric(S^3) = 1/2 > 0, d=2):")
    for label, b, W in [
        ("Flat W=I", 2.30, W_su2_flat),
        ("Frustrated W", 2.30, W_su2_frust),
        ("Thermal b=2.30", 2.30, extract_thermal_boundary(rng, "SU2", 2.30)),
        ("Thermal b=6.00", 6.00, extract_thermal_boundary(rng, "SU2", 6.00)),
    ]:
        rho, chi, lmin = star_observables_nonabelian(rng, "SU2", edges, inc, top_idxs, bot_idxs, W, b)
        print(f"    {label:16s} beta={b:4.2f}  rho_+-t={rho:+.4f}  chi_d->d={chi:.4f}  Hess_lam_min={lmin:+.3f}")

    # 3. SO(3): flat, frustrated, and thermalized boundaries
    print("\n  Adjoint SO(3) Star (Ric > 0, d=2, centerless):")
    for label, b, W in [
        ("Flat W=I", 2.80, W_su2_flat),
        ("Frustrated W", 2.80, W_su2_frust),
        ("Thermal bA=2.80", 2.80, extract_thermal_boundary(rng, "SO3", 2.80)),
        ("Thermal bA=6.00", 6.00, extract_thermal_boundary(rng, "SO3", 6.00)),
    ]:
        rho, chi, lmin = star_observables_nonabelian(rng, "SO3", edges, inc, top_idxs, bot_idxs, W, b)
        print(f"    {label:16s} bA  ={b:4.2f}  rho_+-t={rho:+.4f}  chi_d->d={chi:.4f}  Hess_lam_min={lmin:+.3f}")


def main():
    t0 = time.time()
    run_test_a()
    run_test_b()
    print(f"\nDEEP_PROBE_DONE elapsed={time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
