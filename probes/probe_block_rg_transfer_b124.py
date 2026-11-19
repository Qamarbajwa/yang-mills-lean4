"""Block-Boundary 1+- Transfer, Adjoint Cocycle K_adj(b), and Polymer Sum Gamma(b)
across b = 1 -> 2 -> 3 -> 4 on 4D L=12 Lattices: U(1) vs SU(2) vs Centerless SO(3).

Measures at coarse scale b dividing L=12 (coarse slices L_b = 12, 6, 4, 3):
  M1: Temporal-sheet adjoint kernel K_adj(b) = 1 - delta_{b x b}^{time}
      (0 identically in U(1); measures depolarization across b x b temporal loops
      against both adjacent spatial frame W_{12}^(b) and orthogonal frame W_{23}^(b),
      on bare links and 1-step 3D-smeared links, plus RG-blocked delta_blk for b=1,2,4).
  M2: Gauge-invariant b^3-block-face 1+- correlator C_1pm^GI(b; k) at separation dt = k*b,
      face coherence chi_face(b) = b^3 * <||phi_bar||^2> / <||phi_raw||^2>,
      transfer ratio rho_1pm(b) = C(b; 1)/C(b; 0), and face stiffness Sigma_{1+-}(b) = chi_face * |rho1|.
      For U(1), also reports p_min = (2*pi/L, 0, 0) block-face photon vs exact free lattice photon.
  M3: Coarse-grained polymer sum Gamma_ge2(b) = sum_{k>=2} w_k |r_k(b)| (w_even=5, w_odd=4)
      and full sum Gamma_ge1(b) = sum_{k>=1} w_k |r_k(b)| on both local GI block faces
      and RG-blocked coarse lattices (b = 1, 2, 4).
  M4: Color-singlet 0++ b^3-block-face transfer rho_{0++}(b) and p_min 0++ transfer
      (zero temporal transporters; purely OS reflection-positive control separating true
      IR glueball mass gap from thin-transporter UV perimeter suppression at SU(2) beta=4.0).
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
    """Extract axial dual vector phi in R^3 of skew part (W - W^T)/2."""
    return 0.5 * np.stack([
        W[..., 2, 1] - W[..., 1, 2],
        W[..., 0, 2] - W[..., 2, 0],
        W[..., 1, 0] - W[..., 0, 1],
    ], axis=-1)


# ---------------------------------------------------------------------------
# 3D Spatial APE Smearing & 4D RG Blocking (b -> 2b)
# ---------------------------------------------------------------------------
def smear_3d_spatial(cfg, group, alpha=0.5):
    """1 step of 3D spatial APE smearing preserving time-slice separation."""
    out = cfg.copy()
    if group == "U1":
        E = [np.exp(1j * cfg[..., mu]) for mu in range(4)]
        for mu in (1, 2, 3):
            acc = E[mu].copy()
            for nu in (1, 2, 3):
                if nu == mu:
                    continue
                fwd = E[nu] * np.roll(E[mu], -1, axis=nu) * np.conj(np.roll(E[nu], -1, axis=mu))
                bwd = (
                    np.conj(np.roll(E[nu], 1, axis=nu))
                    * np.roll(E[mu], 1, axis=nu)
                    * np.roll(np.roll(E[nu], 1, axis=nu), -1, axis=mu)
                )
                acc += alpha * (fwd + bwd)
            out[..., mu] = np.angle(acc)
        return out
    elif group == "SU2":
        Ul = [cfg[..., mu, :] for mu in range(4)]
        for mu in (1, 2, 3):
            acc = Ul[mu].copy()
            for nu in (1, 2, 3):
                if nu == mu:
                    continue
                fwd = qmul(qmul(Ul[nu], np.roll(Ul[mu], -1, axis=nu)), qconj(np.roll(Ul[nu], -1, axis=mu)))
                bwd = qmul(
                    qmul(qconj(np.roll(Ul[nu], 1, axis=nu)), np.roll(Ul[mu], 1, axis=nu)),
                    np.roll(np.roll(Ul[nu], 1, axis=nu), -1, axis=mu),
                )
                acc += alpha * (fwd + bwd)
            out[..., mu, :] = acc / np.maximum(np.linalg.norm(acc, axis=-1, keepdims=True), 1e-14)
        return out
    else:
        Rl = [cfg[..., mu, :, :] for mu in range(4)]
        RlT = [np.swapaxes(r, -1, -2) for r in Rl]
        for mu in (1, 2, 3):
            acc = Rl[mu].copy()
            for nu in (1, 2, 3):
                if nu == mu:
                    continue
                fwd = Rl[nu] @ np.roll(Rl[mu], -1, axis=nu) @ np.roll(RlT[nu], -1, axis=mu)
                bwd = (
                    np.roll(RlT[nu], 1, axis=nu)
                    @ np.roll(Rl[mu], 1, axis=nu)
                    @ np.roll(np.roll(Rl[nu], 1, axis=nu), -1, axis=mu)
                )
                acc += alpha * (fwd + bwd)
            out[..., mu, :, :] = project_so3(acc)
        return out


def block_config_2x(cfg, group, alpha_blk=0.5):
    """Exact gauge-covariant factor-2 blocking (L -> L/2) on U(1), SU(2), or SO(3)."""
    if group == "U1":
        E = [np.exp(1j * cfg[..., mu]) for mu in range(4)]
        cols = []
        for mu in range(4):
            P_str = E[mu] * np.roll(E[mu], -1, axis=mu)
            acc = P_str.copy()
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
# Vectorized 4D Updaters (Checkerboard)
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


def so3_sweep(rng, U, parities, beta_A, n_hits=5):
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
# Arbitrary b x b Wilson Loops & Sequential L-Path Face Parallel Transport
# ---------------------------------------------------------------------------
def u1_line_b(theta, mu, b):
    acc = theta[..., mu].copy()
    for s in range(1, b):
        acc = acc + np.roll(theta[..., mu], -s, axis=mu)
    return acc


def so3_line_b(R, mu, b):
    acc = R[..., mu, :, :].copy()
    for s in range(1, b):
        acc = acc @ np.roll(R[..., mu, :, :], -s, axis=mu)
    return acc


def su2_line_b(q, mu, b):
    acc = q[..., mu, :].copy()
    for s in range(1, b):
        acc = qmul(acc, np.roll(q[..., mu, :], -s, axis=mu))
    return acc


def u1_loop_b(lines, mu, nu, b):
    Lm, Ln = lines[mu], lines[nu]
    return Lm + np.roll(Ln, -b, axis=mu) - np.roll(Lm, -b, axis=nu) - Ln


def so3_loop_b(lines, mu, nu, b):
    Lm, Ln = lines[mu], lines[nu]
    Lm_s = np.roll(Lm, -b, axis=nu)
    Ln_s = np.roll(Ln, -b, axis=mu)
    return Lm @ Ln_s @ np.swapaxes(Lm_s, -1, -2) @ np.swapaxes(Ln, -1, -2)


def su2_loop_b(lines, mu, nu, b):
    Lm, Ln = lines[mu], lines[nu]
    return qmul(qmul(Lm, np.roll(Ln, -b, axis=mu)), qconj(qmul(Ln, np.roll(Lm, -b, axis=nu))))


def block_prefix_axis_so3(R_mu, axis, b):
    """Compute cumulative SO(3) L-path segments P(X_axis, d) for d=0..b-1 along spatial axis."""
    L = R_mu.shape[0]
    L_b = L // b
    shape_before = R_mu.shape[:axis] + (L_b, b) + R_mu.shape[axis + 1:]
    blk = R_mu.reshape(shape_before)  # split axis -> (L_b, b) at (axis, axis+1)
    out = np.empty_like(blk)
    eye_shape = R_mu.shape[:axis] + (L_b,) + R_mu.shape[axis + 1:]
    eye = np.broadcast_to(np.eye(3), eye_shape).copy()
    sl_out = [slice(None)] * out.ndim
    sl_in = [slice(None)] * blk.ndim
    sl_out[axis + 1] = 0
    out[tuple(sl_out)] = eye
    cur = eye
    for s in range(1, b):
        sl_in[axis + 1] = s - 1
        cur = cur @ blk[tuple(sl_in)]
        sl_out[axis + 1] = s
        out[tuple(sl_out)] = cur
    return out


def transport_and_avg_face_so3(R, phi_raw, b):
    """Parallel-transport 3D block fluxes phi_raw(..., 3_planes, 3_color) along z -> y -> x to corners b*X0."""
    L = R.shape[0]
    L_b = L // b
    if b == 1:
        return phi_raw.copy()

    # Step 1 (z-axis = 3): split z -> (L_b, b)
    Pz = block_prefix_axis_so3(R[..., 3, :, :], 3, b)  # (L, L, L, L_b, b, 3, 3)
    phi_z = phi_raw.reshape(L, L, L, L_b, b, 3, 3)
    vz = np.sum(np.einsum("txyZdij,txyZdpj->txyZdpi", Pz, phi_z), axis=4)  # (L, L, L, L_b, 3, 3)

    # Step 2 (y-axis = 2): restrict Py to z = b*Z, split y -> (L_b, b)
    R2_sub = R[:, :, :, ::b, 2, :, :]  # (L, L, L, L_b, 3, 3)
    Py = block_prefix_axis_so3(R2_sub, 2, b)  # (L, L, L_b, b, L_b, 3, 3)
    vy_in = vz.reshape(L, L, L_b, b, L_b, 3, 3)
    vyz = np.sum(np.einsum("txYdZij,txYdZpj->txYdZpi", Py, vy_in), axis=3)  # (L, L, L_b, L_b, 3, 3)

    # Step 3 (x-axis = 1): restrict Px to y=b*Y, z=b*Z, split x -> (L_b, b)
    R1_sub = R[:, :, ::b, ::b, 1, :, :]  # (L, L, L_b, L_b, 3, 3)
    Px = block_prefix_axis_so3(R1_sub, 1, b)  # (L, L_b, b, L_b, L_b, 3, 3)
    vx_in = vyz.reshape(L, L_b, b, L_b, L_b, 3, 3)
    vxyz = np.sum(np.einsum("tXdYZij,tXdYZpj->tXdYZpi", Px, vx_in), axis=2)  # (L, L_b, L_b, L_b, 3, 3)

    return vxyz / float(b ** 3)


def k_adj_kernels(R, b):
    """M1: Temporal b x b sheet survival K_adj(b) = 1 - delta_{b x b}^{time}
    against adjacent spatial frame (1, 2) and orthogonal spatial frame (2, 3)."""
    lines = [so3_line_b(R, mu, b) for mu in range(4)]
    W01 = so3_loop_b(lines, 0, 1, b)
    W12 = so3_loop_b(lines, 1, 2, b)
    W23 = so3_loop_b(lines, 2, 3, b)

    v12 = so3_dual_vec(W12)
    n12 = v12 / np.maximum(np.linalg.norm(v12, axis=-1, keepdims=True), 1e-12)
    n12_rot = np.einsum("...ij,...j->...i", W01, n12)
    k_adj = float(np.mean(np.sum(n12 * n12_rot, axis=-1)))

    v23 = so3_dual_vec(W23)
    n23 = v23 / np.maximum(np.linalg.norm(v23, axis=-1, keepdims=True), 1e-12)
    n23_rot = np.einsum("...ij,...j->...i", W01, n23)
    k_orth = float(np.mean(np.sum(n23 * n23_rot, axis=-1)))
    return k_adj, k_orth


# ---------------------------------------------------------------------------
# M2, M3, M4 Scale-b Measurement Bundle (for a Single Config & Scale b)
# ---------------------------------------------------------------------------
SPATIAL_PLANES = [(1, 2), (1, 3), (2, 3)]


def measure_scale_b_observables(cfg_raw, group, b, sm3d_R=None):
    """Compute M1, M2, M4 raw correlator curves (averaged over sites/planes) for scale b."""
    L = cfg_raw.shape[0]
    L_b = L // b
    k_max = L_b // 2

    if group == "U1":
        lines = [u1_line_b(cfg_raw, mu, b) for mu in range(4)]
        loops_sp = [u1_loop_b(lines, i, j, b) for (i, j) in SPATIAL_PLANES]
        phi_raw = np.stack([np.sin(th) for th in loops_sp], axis=-1)  # (L, L, L, L, 3)
        cost_sp = np.mean(np.stack([1.0 - np.cos(th) for th in loops_sp], axis=-1), axis=-1)

        phi_bar = phi_raw.reshape(L, L_b, b, L_b, b, L_b, b, 3).mean(axis=(2, 4, 6))
        s0_bar = cost_sp.reshape(L, L_b, b, L_b, b, L_b, b).mean(axis=(2, 4, 6))

        raw_var_1pm = float(np.mean(phi_raw * phi_raw))
        blk_var_1pm = float(np.mean(phi_bar * phi_bar))
        c_1pm_loc = np.array([
            float(np.mean(phi_bar * np.roll(phi_bar, -k * b, axis=0)))
            for k in range(k_max + 1)
        ])

        # U(1) p_min = (2*pi/L, 0, 0) transverse photon on b^3 block faces (b12 & b13)
        X1_coords = np.arange(L_b) * b
        ph = np.exp(1j * (2.0 * math.pi / L) * X1_coords)[None, :, None, None]
        # (1,2) and (1,3) carry transverse polarization wrt p_min along axis 1
        o_p0 = np.sum(phi_bar[..., 0] * ph, axis=(1, 2, 3))
        o_p1 = np.sum(phi_bar[..., 1] * ph, axis=(1, 2, 3))
        c_1pm_pmin = np.array([
            0.5 * (
                float(np.mean(np.real(o_p0 * np.conj(np.roll(o_p0, -k * b)))))
                + float(np.mean(np.real(o_p1 * np.conj(np.roll(o_p1, -k * b)))))
            )
            for k in range(k_max + 1)
        ])

        k_adj, k_orth, k_adj_sm = 1.0, 1.0, 1.0

    else:
        R = cfg_raw if group == "SO3" else q_to_so3(cfg_raw)
        lines_R = [so3_line_b(R, mu, b) for mu in range(4)]
        loops_sp_R = [so3_loop_b(lines_R, i, j, b) for (i, j) in SPATIAL_PLANES]
        phi_raw = np.stack([so3_dual_vec(W) for W in loops_sp_R], axis=-2)  # (L, L, L, L, 3, 3)

        if group == "SU2":
            lines_q = [su2_line_b(cfg_raw, mu, b) for mu in range(4)]
            loops_q = [su2_loop_b(lines_q, i, j, b) for (i, j) in SPATIAL_PLANES]
            cost_sp = np.mean(np.stack([1.0 - q[..., 0] for q in loops_q], axis=-1), axis=-1)
        else:
            cost_sp = np.mean(
                np.stack([1.0 - np.trace(W, axis1=-2, axis2=-1) / 3.0 for W in loops_sp_R], axis=-1),
                axis=-1,
            )

        phi_bar = transport_and_avg_face_so3(R, phi_raw, b)  # (L, L_b, L_b, L_b, 3, 3)
        s0_bar = cost_sp.reshape(L, L_b, b, L_b, b, L_b, b).mean(axis=(2, 4, 6))

        raw_var_1pm = float(np.mean(np.sum(phi_raw * phi_raw, axis=-1)))
        blk_var_1pm = float(np.mean(np.sum(phi_bar * phi_bar, axis=-1)))

        L0_b = lines_R[0][:, ::b, ::b, ::b, :, :]  # (L, L_b, L_b, L_b, 3, 3)
        c_list = [blk_var_1pm]
        T_cur = None
        for k in range(1, k_max + 1):
            T_cur = L0_b if k == 1 else (T_cur @ np.roll(L0_b, -(k - 1) * b, axis=0))
            phi_sh = np.roll(phi_bar, -k * b, axis=0)
            phi_tr = np.einsum("...ij,...pj->...pi", T_cur, phi_sh)
            c_list.append(float(np.mean(np.sum(phi_bar * phi_tr, axis=-1))))
        c_1pm_loc = np.array(c_list)
        c_1pm_pmin = None

        k_adj, k_orth = k_adj_kernels(R, b)
        k_adj_sm, _ = k_adj_kernels(sm3d_R, b) if sm3d_R is not None else (k_adj, k_orth)

    # M4: Connected 0++ block-face correlator (local and p_min, zero temporal links)
    ds_loc = s0_bar - np.mean(s0_bar)
    c_0pp_loc = np.array([
        float(np.mean(ds_loc * np.roll(ds_loc, -k * b, axis=0)))
        for k in range(k_max + 1)
    ])
    X1_coords = np.arange(L_b) * b
    ph = np.exp(1j * (2.0 * math.pi / L) * X1_coords)[None, :, None, None]
    o_0pp = np.sum(s0_bar * ph, axis=(1, 2, 3))
    c_0pp_pmin = np.array([
        float(np.mean(np.real(o_0pp * np.conj(np.roll(o_0pp, -k * b)))))
        for k in range(k_max + 1)
    ])

    return {
        "k_adj": k_adj,
        "k_orth": k_orth,
        "k_adj_sm": k_adj_sm,
        "raw_var_1pm": raw_var_1pm,
        "blk_var_1pm": blk_var_1pm,
        "c_1pm_loc": c_1pm_loc,
        "c_1pm_pmin": c_1pm_pmin,
        "c_0pp_loc": c_0pp_loc,
        "c_0pp_pmin": c_0pp_pmin,
    }


def extract_rho_gammas(C, L_b):
    """Return rho1 = r_1, Gamma_ge2 (k >= 2 polymer tail), Gamma_ge1 (k >= 1 full sum)."""
    c0 = max(abs(float(C[0])), 1e-15)
    r = [float(C[k]) / c0 for k in range(len(C))]
    rho1 = r[1] if len(r) > 1 else 0.0
    if L_b >= 4:
        gamma_ge2 = sum((5.0 if k % 2 == 0 else 4.0) * abs(r[k]) for k in range(2, len(r)))
    else:
        gamma_ge2 = float("nan")
    gamma_ge1 = sum((5.0 if k % 2 == 0 else 4.0) * abs(r[k]) for k in range(1, len(r)))
    return rho1, gamma_ge2, gamma_ge1


def free_photon_ratios(L, b):
    """Exact 4D massless lattice photon ratios r_k^{free}(b) = cosh(E0*(L/2 - k*b)) / cosh(E0*L/2)."""
    e0 = math.acosh(1.0 + 2.0 * (math.sin(math.pi / L) ** 2))
    L_b = L // b
    denom = math.cosh(0.5 * e0 * L)
    C = [math.cosh(e0 * (0.5 * L - k * b)) / denom for k in range(L_b // 2 + 1)]
    return extract_rho_gammas(C, L_b)


# ---------------------------------------------------------------------------
# Unit Tests: Exact Gauge Invariance & SO(3) Z2 Invariance
# ---------------------------------------------------------------------------
def verify_transfer_invariance():
    rng = np.random.default_rng(17711)
    max_err_u1 = 0.0
    max_err_su2 = 0.0
    max_err_so3_g = 0.0
    max_err_so3_z2 = 0.0

    for L, scales in [(6, [1, 2, 3]), (4, [1, 2, 4])]:
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

        for b in scales:
            m_u1_a = measure_scale_b_observables(U1, "U1", b)
            m_u1_b = measure_scale_b_observables(U1_g, "U1", b)
            for k in ["c_1pm_loc", "c_1pm_pmin", "c_0pp_loc", "c_0pp_pmin"]:
                max_err_u1 = max(max_err_u1, float(np.max(np.abs(m_u1_a[k] - m_u1_b[k]))))

            m_s2_a = measure_scale_b_observables(U2, "SU2", b)
            m_s2_b = measure_scale_b_observables(U2_g, "SU2", b)
            for k in ["c_1pm_loc", "c_0pp_loc", "c_0pp_pmin"]:
                max_err_su2 = max(max_err_su2, float(np.max(np.abs(m_s2_a[k] - m_s2_b[k]))))
            for k in ["k_adj", "k_orth"]:
                max_err_su2 = max(max_err_su2, abs(m_s2_a[k] - m_s2_b[k]))

            m_r3_a = measure_scale_b_observables(R3, "SO3", b)
            m_r3_g = measure_scale_b_observables(R3_g, "SO3", b)
            m_r3_z = measure_scale_b_observables(R3_z2, "SO3", b)
            for k in ["c_1pm_loc", "c_0pp_loc", "c_0pp_pmin"]:
                max_err_so3_g = max(max_err_so3_g, float(np.max(np.abs(m_r3_a[k] - m_r3_g[k]))))
                max_err_so3_z2 = max(max_err_so3_z2, float(np.max(np.abs(m_r3_a[k] - m_r3_z[k]))))
            for k in ["k_adj", "k_orth"]:
                max_err_so3_g = max(max_err_so3_g, abs(m_r3_a[k] - m_r3_g[k]))
                max_err_so3_z2 = max(max_err_so3_z2, abs(m_r3_a[k] - m_r3_z[k]))

    assert max(max_err_u1, max_err_su2, max_err_so3_g, max_err_so3_z2) < 1e-12
    print(
        f"TRANSFER_GAUGE_INV_OK u1={max_err_u1:.1e} su2={max_err_su2:.1e} "
        f"so3_g={max_err_so3_g:.1e} so3_z2={max_err_so3_z2:.1e}"
    )


# ---------------------------------------------------------------------------
# L=12 Simulation Runner
# ---------------------------------------------------------------------------
def simulate_point(rng, group, beta, L=12, n_therm=20, n_meas=18):
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
            so3_sweep(rng, U, parities, beta, n_hits=5)

    scales = [1, 2, 3, 4]
    acc = {b: [] for b in scales}
    blk_acc = {2: [], 4: []}

    for _ in range(n_meas):
        if group == "U1":
            u1_sweep(rng, U, parities, beta)
            cfg = U
            sm3d = None
        elif group == "SU2":
            su2_sweep(rng, U, parities, beta)
            cfg = U
            sm3d = q_to_so3(smear_3d_spatial(U, "SU2", alpha=0.5))
        else:
            so3_sweep(rng, U, parities, beta, n_hits=5)
            cfg = q_to_so3(U)
            sm3d = smear_3d_spatial(cfg, "SO3", alpha=0.5)

        for b in scales:
            acc[b].append(measure_scale_b_observables(cfg, group, b, sm3d_R=sm3d))

        # Blocked RG control (b = 2 and b = 4 coarse lattices, measured at b_inner=1)
        b2 = block_config_2x(cfg, group)
        b4 = block_config_2x(b2, group)
        blk_acc[2].append(measure_scale_b_observables(b2, group, 1))
        blk_acc[4].append(measure_scale_b_observables(b4, group, 1))

    def summarize(items, L_b):
        k_adj = float(np.mean([x["k_adj"] for x in items]))
        k_orth = float(np.mean([x["k_orth"] for x in items]))
        k_adj_sm = float(np.mean([x["k_adj_sm"] for x in items]))
        raw_v = float(np.mean([x["raw_var_1pm"] for x in items]))
        blk_v = float(np.mean([x["blk_var_1pm"] for x in items]))
        chi_face = (float(L // L_b) ** 3) * (blk_v / max(raw_v, 1e-15))

        c_1pm = np.mean([x["c_1pm_loc"] for x in items], axis=0)
        rho1, g2, g1 = extract_rho_gammas(c_1pm, L_b)
        sigma = chi_face * abs(rho1)

        c_0pp_l = np.mean([x["c_0pp_loc"] for x in items], axis=0)
        rho0_l, g0_2_l, g0_1_l = extract_rho_gammas(c_0pp_l, L_b)

        c_0pp_p = np.mean([x["c_0pp_pmin"] for x in items], axis=0)
        rho0_p, g0_2_p, g0_1_p = extract_rho_gammas(c_0pp_p, L_b)

        pmin_res = None
        if items[0]["c_1pm_pmin"] is not None:
            c_pm = np.mean([x["c_1pm_pmin"] for x in items], axis=0)
            pmin_res = extract_rho_gammas(c_pm, L_b)

        return {
            "L_b": L_b,
            "k_adj": k_adj,
            "k_orth": k_orth,
            "k_adj_sm": k_adj_sm,
            "chi_face": chi_face,
            "sigma_1pm": sigma,
            "rho_1pm": rho1,
            "g2_1pm": g2,
            "g1_1pm": g1,
            "rho_0pp_loc": rho0_l,
            "rho_0pp_pmin": rho0_p,
            "g2_0pp_pmin": g0_2_p,
            "u1_pmin": pmin_res,
        }

    out = {b: summarize(acc[b], L // b) for b in scales}
    blk_out = {2: summarize(blk_acc[2], L // 2), 4: summarize(blk_acc[4], L // 4)}
    return out, blk_out


def fmt_g(val):
    return "  na  " if math.isnan(val) else f"{val:6.3f}"


def main():
    t0 = time.time()
    verify_transfer_invariance()
    L = 12
    n_therm, n_meas = 20, 18
    rng = np.random.default_rng(17712)

    print(f"\n=== EXACT FREE MASSLESS 4D LATTICE PHOTON BENCHMARK (L={L}, p_min=2pi/{L}) ===")
    for b in [1, 2, 3, 4]:
        rf, g2f, g1f = free_photon_ratios(L, b)
        print(f"  b={b} (L_b={L // b:2d}): rho_free={rf:.4f} | Gamma_ge2_free={fmt_g(g2f)} | Gamma_ge1_free={g1f:6.3f}")

    suite = [
        ("U1", [0.85, 1.10, 1.30]),
        ("SU2", [2.30, 2.50, 4.00]),
        ("SO3", [2.80, 4.00]),
    ]

    print(f"\n=== BLOCK-BOUNDARY TRANSFER PROBE (L={L}, b in {{1,2,3,4}}, therm={n_therm}, meas={n_meas}) ===")
    for group, betas in suite:
        b_lbl = "bA" if group == "SO3" else "beta"
        for bval in betas:
            pt0 = time.time()
            res, blk = simulate_point(rng, group, bval, L=L, n_therm=n_therm, n_meas=n_meas)
            dt = time.time() - pt0
            print(f"\n  [{group} {b_lbl}={bval:.2f}] ({dt:.1f}s)")
            print(
                "    b | L_b | K_adj(sm)  K_orth | chi_fc | rho_1pm  Sigma_1pm | "
                "G_ge2  G_ge1 | 0++_rho(loc,pm) | extra"
            )
            for b in [1, 2, 3, 4]:
                s = res[b]
                extra = ""
                if group == "U1":
                    rp, g2p, g1p = s["u1_pmin"]
                    extra = f"U1_pmin(rho={rp:.3f}, G2={fmt_g(g2p)}, G1={g1p:.3f})"
                    if b in (2, 4):
                        sb = blk[b]
                        rp_b, _, g1_b = sb["u1_pmin"]
                        extra += f" BLK(loc={sb['rho_1pm']:.3f}, pm={rp_b:.3f}, 0++pm={sb['rho_0pp_pmin']:.3f})"
                elif b in (2, 4):
                    sb = blk[b]
                    extra = (
                        f"BLK_RG(K_adj={sb['k_adj']:.3f}, rho1pm={sb['rho_1pm']:.3f}, "
                        f"G1_1pm={sb['g1_1pm']:.3f}, 0++pm={sb['rho_0pp_pmin']:.3f})"
                    )
                print(
                    f"    {b} | {s['L_b']:3d} | {s['k_adj']:5.3f}({s['k_adj_sm']:4.2f}) {s['k_orth']:5.3f} | "
                    f"{s['chi_face']:6.2f} | {s['rho_1pm']:+6.3f}   {s['sigma_1pm']:7.3f}   | "
                    f"{fmt_g(s['g2_1pm'])} {s['g1_1pm']:6.3f} | "
                    f"({s['rho_0pp_loc']:+.3f},{s['rho_0pp_pmin']:+.3f}) | {extra}"
                )

    print(f"\nPROBE_BLOCK_TRANSFER_DONE elapsed={time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
