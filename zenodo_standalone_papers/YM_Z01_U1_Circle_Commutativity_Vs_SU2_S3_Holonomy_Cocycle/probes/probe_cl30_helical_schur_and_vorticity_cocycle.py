#!/usr/bin/env python3
"""Cl(3,0) ~= M_2(C) Helical Schur Complement & Constantin-Fefferman SO(3) Vorticity Cocycle Probe.

Non-destructive diagnostic script on an L=12 3D periodic grid (T^3).
Writes JSON receipt to: ../probe_cl30_helical_schur_results.json

Scientific honesty: 3D Navier-Stokes Global Regularity remains strictly OPEN.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
import numpy as np


def build_grid_and_wavevectors(L: int = 12):
    """Build LxLxL periodic grid and active Fourier shell K = {-5..5}^3 minus {0}."""
    coords = np.arange(L, dtype=np.float64) * (2.0 * np.pi / L)
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")

    freqs = np.fft.fftfreq(L) * L  # integer frequencies
    kx, ky, kz = np.meshgrid(freqs, freqs, freqs, indexing="ij")
    k_vec = np.stack([kx, ky, kz], axis=-1)  # (L, L, L, 3)

    # Active symmetric shell excluding 0 and Nyquist (-6)
    half = L // 2
    active_mask = (
        (np.abs(kx) < half)
        & (np.abs(ky) < half)
        & (np.abs(kz) < half)
        & ((kx != 0) | (ky != 0) | (kz != 0))
    )
    active_k = k_vec[active_mask]  # (N_k, 3)
    return X, Y, Z, k_vec, active_mask, active_k


def helical_frame_and_projectors(k: np.ndarray):
    """For a single wavevector k != 0, return h_+, h_-, P_+, P_-, and Cl(3,0) M_2(C) matrices."""
    knorm = np.linalg.norm(k)
    khat = k / knorm
    ref = np.array([1.0, 0.0, 0.0]) if abs(khat[0]) < 0.9 else np.array([0.0, 1.0, 0.0])
    e1 = np.cross(ref, khat)
    e1 = e1 / np.linalg.norm(e1)
    e2 = np.cross(khat, e1)

    h_plus = (e1 + 1j * e2) / np.sqrt(2.0)
    h_minus = (e1 - 1j * e2) / np.sqrt(2.0)

    P_plus = np.outer(h_plus, h_plus.conj())
    P_minus = np.outer(h_minus, h_minus.conj())

    # Cl(3,0) ~= M_2(C) Pauli representation
    s1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
    s2 = np.array([[0.0, -1j], [1j, 0.0]], dtype=np.complex128)
    s3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)
    sigma_k = khat[0] * s1 + khat[1] * s2 + khat[2] * s3
    P_cl_plus = 0.5 * (np.eye(2, dtype=np.complex128) + sigma_k)
    P_cl_minus = 0.5 * (np.eye(2, dtype=np.complex128) - sigma_k)

    return h_plus, h_minus, P_plus, P_minus, sigma_k, P_cl_plus, P_cl_minus


def curl_matrix(k: np.ndarray) -> np.ndarray:
    """Return 3x3 Hermitian matrix representing i k x (.) in Fourier space."""
    kx, ky, kz = k
    return 1j * np.array(
        [
            [0.0, -kz, ky],
            [kz, 0.0, -kx],
            [-ky, kx, 0.0],
        ],
        dtype=np.complex128,
    )


def verify_cl30_helical_basis(L: int = 12):
    """Part 1: Verify Cl(3,0) ~= M_2(C) Beltrami helical basis and u = u_+ (+) u_- decomposition."""
    X, Y, Z, k_vec, active_mask, active_k = build_grid_and_wavevectors(L)

    max_cl_involution_err = 0.0
    max_cl_ortho_err = 0.0
    max_curl_eig_err = 0.0
    max_div_err = 0.0
    max_helical_ortho_err = 0.0

    # Precompute helical projectors on the full grid
    P_plus_grid = np.zeros((L, L, L, 3, 3), dtype=np.complex128)
    P_minus_grid = np.zeros((L, L, L, 3, 3), dtype=np.complex128)

    indices = np.argwhere(active_mask)
    for idx in indices:
        ix, iy, iz = idx
        k = k_vec[ix, iy, iz]
        knorm = np.linalg.norm(k)
        hp, hm, Pp, Pm, sigma_k, Pclp, Pclm = helical_frame_and_projectors(k)
        P_plus_grid[ix, iy, iz] = Pp
        P_minus_grid[ix, iy, iz] = Pm

        # Check Cl(3,0) identities
        max_cl_involution_err = max(
            max_cl_involution_err,
            float(np.linalg.norm(sigma_k @ sigma_k - np.eye(2))),
        )
        max_cl_ortho_err = max(
            max_cl_ortho_err,
            float(np.linalg.norm(Pclp @ Pclm)),
        )

        # Check Beltrami curl eigenvalues: i k x h_+- = +- |k| h_+-
        Ck = curl_matrix(k)
        err_p = np.linalg.norm(Ck @ hp - knorm * hp)
        err_m = np.linalg.norm(Ck @ hm + knorm * hm)
        max_curl_eig_err = max(max_curl_eig_err, float(err_p), float(err_m))

        # Check divergence-free and orthogonality
        max_div_err = max(
            max_div_err,
            float(abs(np.dot(k, hp))),
            float(abs(np.dot(k, hm))),
        )
        max_helical_ortho_err = max(
            max_helical_ortho_err,
            float(abs(np.vdot(hp, hm))),
        )

    # Test real divergence-free 3D field decomposition u = u_+ (+) u_-
    rng = np.random.default_rng(20261119)
    raw = rng.standard_normal((L, L, L, 3))
    raw_hat = np.fft.fftn(raw, axes=(0, 1, 2))
    u_hat = np.zeros_like(raw_hat)
    for ix, iy, iz in indices:
        k = k_vec[ix, iy, iz]
        khat = k / np.linalg.norm(k)
        proj = np.eye(3) - np.outer(khat, khat)
        u_hat[ix, iy, iz] = proj @ raw_hat[ix, iy, iz]

    u = np.fft.ifftn(u_hat, axes=(0, 1, 2)).real
    u_hat = np.fft.fftn(u, axes=(0, 1, 2))

    u_plus_hat = np.einsum("ijkab,ijkb->ijka", P_plus_grid, u_hat)
    u_minus_hat = np.einsum("ijkab,ijkb->ijka", P_minus_grid, u_hat)

    u_plus = np.fft.ifftn(u_plus_hat, axes=(0, 1, 2)).real
    u_minus = np.fft.ifftn(u_minus_hat, axes=(0, 1, 2)).real

    recon_err = float(np.linalg.norm(u - (u_plus + u_minus)) / np.linalg.norm(u))
    inner_pm = float(abs(np.sum(u_plus * u_minus)) / np.sum(u * u))
    parseval_err = float(
        abs(np.sum(u * u) - (np.sum(u_plus * u_plus) + np.sum(u_minus * u_minus)))
        / np.sum(u * u)
    )

    # Verify real-space curl(u_+-) = +- |nabla| u_+-
    knorm_grid = np.linalg.norm(k_vec, axis=-1, keepdims=True)
    curl_up_hat = np.cross(1j * k_vec, u_plus_hat)
    curl_um_hat = np.cross(1j * k_vec, u_minus_hat)
    beltrami_plus_err = float(
        np.linalg.norm(curl_up_hat - knorm_grid * u_plus_hat)
        / np.linalg.norm(knorm_grid * u_plus_hat)
    )
    beltrami_minus_err = float(
        np.linalg.norm(curl_um_hat + knorm_grid * u_minus_hat)
        / np.linalg.norm(knorm_grid * u_minus_hat)
    )

    return {
        "grid_L": L,
        "active_wavevectors": int(len(indices)),
        "helical_dim": int(2 * len(indices)),
        "max_cl_involution_err": max_cl_involution_err,
        "max_cl_ortho_err": max_cl_ortho_err,
        "max_curl_eig_err": max_curl_eig_err,
        "max_div_err": max_div_err,
        "max_helical_ortho_err": max_helical_ortho_err,
        "field_recon_err": recon_err,
        "helical_orthogonality_err": inner_pm,
        "parseval_err": parseval_err,
        "beltrami_plus_err": beltrami_plus_err,
        "beltrami_minus_err": beltrami_minus_err,
    }


def verify_parity_gram_schur_and_half_op(L: int = 12):
    """Part 2: Certify P: u(x) |-> -u(-x), diagonal Gram matrix of {Q_E, Q_Z, T_hel},
    positive Schur complement, T_hel^2 = I parity-blindness, and K_half + K_half^T = 4 T_hel."""
    _, _, _, k_vec, active_mask, active_k = build_grid_and_wavevectors(L)

    # Collect unique unordered pairs {k, -k} in the active shell
    k_tuples = [tuple(int(x) for x in k) for k in active_k]
    k_set = set(k_tuples)
    pairs = []
    seen = set()
    for kt in k_tuples:
        if kt in seen:
            continue
        mkt = (-kt[0], -kt[1], -kt[2])
        assert mkt in k_set
        seen.add(kt)
        seen.add(mkt)
        pairs.append((np.array(kt, dtype=np.float64), np.array(mkt, dtype=np.float64)))

    k2_vals = np.array([float(np.dot(k, k)) for k, _ in pairs])
    mean_k2 = float(np.mean(k2_vals))

    # Build real-valued 4x4 pair operators in real Fourier basis:
    # For each pair {k, -k}, a real field u has Fourier modes:
    #   u_hat(k) = c_+ h_+(k) + c_- h_-(k),   u_hat(-k) = conj(u_hat(k))
    # Real 4D coordinates: [Re(c_+), Im(c_+), Re(c_-), Im(c_-)] in R^4.
    # Let's verify P: u(x) |-> -u(-x) on this real 4D space!
    # Under P: (Pu)_hat(k) = -u_hat(-k) = -conj(u_hat(k)) = -conj(c_+) conj(h_+(k)) - conj(c_-) conj(h_-(k)).
    # Since conj(h_+(k)) = (e1 - i e2)/sqrt(2) = h_-(k) and conj(h_-(k)) = h_+(k):
    #   (Pu)_hat(k) = -conj(c_-) h_+(k) - conj(c_+) h_-(k).
    # In real 4D coordinates (Re c_+, Im c_+, Re c_-, Im c_-):
    #   P = [[0, 0, -1, 0],
    #        [0, 0,  0, 1],
    #        [-1, 0, 0, 0],
    #        [0,  1, 0, 0]]
    # Notice P^2 = I_4, P^T = P, and P exchanges the + and - chiral subspaces!
    P_pair = np.array(
        [
            [0.0, 0.0, -1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
            [-1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
        ],
        dtype=np.float64,
    )
    P_plus_pair = np.diag([1.0, 1.0, 0.0, 0.0])
    P_minus_pair = np.diag([0.0, 0.0, 1.0, 1.0])
    Q_E_pair = P_plus_pair + P_minus_pair  # I_4
    T_hel_pair = P_plus_pair - P_minus_pair  # diag(1, 1, -1, -1)

    # Verify P intertwines P_+ and P_-: P P_+ P = P_-, P T_hel P = -T_hel
    p_intertwine_err = float(np.linalg.norm(P_pair @ P_plus_pair @ P_pair - P_minus_pair))
    p_t_hel_odd_err = float(np.linalg.norm(P_pair @ T_hel_pair @ P_pair + T_hel_pair))

    # Observable half-operator on each pair: K_half = 2 T_hel + 2 (P_+ P - P_- P)
    K_half_pair = 2.0 * T_hel_pair + 2.0 * (P_plus_pair @ P_pair - P_minus_pair @ P_pair)
    k_half_recon_err = float(
        np.linalg.norm(K_half_pair + K_half_pair.T - 4.0 * T_hel_pair)
    )
    # Also check K_half is genuinely non-symmetric (chiral coupling)
    k_half_asym_norm = float(np.linalg.norm(K_half_pair - K_half_pair.T))

    # Squared density T_hel^2 = I_4
    T_sq_pair = T_hel_pair @ T_hel_pair
    t_sq_id_err = float(np.linalg.norm(T_sq_pair - Q_E_pair))
    t_sq_parity_blind_err = float(np.linalg.norm(P_pair @ T_sq_pair @ P_pair - T_sq_pair))
    t_sq_cross_chirality_err = float(
        np.linalg.norm(P_plus_pair @ T_sq_pair @ P_minus_pair)
    )

    # Full-shell Hilbert-Schmidt Gram matrix of {Q_E, Q_Z, T_hel}
    # On each pair, Q_Z(k) = (|k|^2 - mean_k2) * Q_E_pair
    G = np.zeros((3, 3), dtype=np.float64)
    for k2 in k2_vals:
        ops = [Q_E_pair, (k2 - mean_k2) * Q_E_pair, T_hel_pair]
        for i in range(3):
            for j in range(3):
                G[i, j] += float(np.trace(ops[i].T @ ops[j]))

    # Check diagonality and O(3)-even projection of T_hel
    G_even = G[:2, :2]
    g_cross = G[:2, 2]
    proj_coeffs = np.linalg.solve(G_even, g_cross)
    pi_o3_even_t_hel_norm = float(np.linalg.norm(proj_coeffs))
    schur_complement = float(G[2, 2] - g_cross @ np.linalg.solve(G_even, g_cross))
    gram_offdiag_max = float(np.max(np.abs(G - np.diag(np.diag(G)))))
    diag_sqrt = np.sqrt(np.diag(G))
    G_norm = G / np.outer(diag_sqrt, diag_sqrt)
    gram_normalized_offdiag_max = float(np.max(np.abs(G_norm - np.eye(3))))

    # Also verify parity action directly in real space on a random divergence-free field
    rng = np.random.default_rng(42)
    X, Y, Z, _, _, _ = build_grid_and_wavevectors(L)
    # Real field u(x) = curl(A(x)) on active shell
    A_hat = np.zeros((L, L, L, 3), dtype=np.complex128)
    for k, mk in pairs:
        ix, iy, iz = int(k[0]) % L, int(k[1]) % L, int(k[2]) % L
        mx, my, mz = int(mk[0]) % L, int(mk[1]) % L, int(mk[2]) % L
        val = rng.standard_normal(3) + 1j * rng.standard_normal(3)
        A_hat[ix, iy, iz] = val
        A_hat[mx, my, mz] = np.conj(val)
    u_hat = np.cross(1j * k_vec, A_hat)
    u = np.fft.ifftn(u_hat, axes=(0, 1, 2)).real

    # Spatial parity in real space: (Pu)(x) = -u(-x mod L)
    idx_neg = (-np.arange(L)) % L
    Pu = -u[np.ix_(idx_neg, idx_neg, idx_neg)]

    # Helical decomposition of u and Pu
    P_plus_grid = np.zeros((L, L, L, 3, 3), dtype=np.complex128)
    P_minus_grid = np.zeros((L, L, L, 3, 3), dtype=np.complex128)
    for ix, iy, iz in np.argwhere(active_mask):
        _, _, Pp, Pm, _, _, _ = helical_frame_and_projectors(k_vec[ix, iy, iz])
        P_plus_grid[ix, iy, iz] = Pp
        P_minus_grid[ix, iy, iz] = Pm

    Pu_hat = np.fft.fftn(Pu, axes=(0, 1, 2))
    u_plus_hat = np.einsum("ijkab,ijkb->ijka", P_plus_grid, u_hat)
    u_minus_hat = np.einsum("ijkab,ijkb->ijka", P_minus_grid, u_hat)
    Pu_plus_hat = np.einsum("ijkab,ijkb->ijka", P_plus_grid, Pu_hat)
    Pu_minus_hat = np.einsum("ijkab,ijkb->ijka", P_minus_grid, Pu_hat)

    # Helicity expectation <u, T_hel u> vs <Pu, T_hel Pu>
    hel_u = float(np.sum(np.abs(u_plus_hat) ** 2 - np.abs(u_minus_hat) ** 2))
    hel_Pu = float(np.sum(np.abs(Pu_plus_hat) ** 2 - np.abs(Pu_minus_hat) ** 2))
    realspace_parity_hel_flip_err = float(abs(hel_u + hel_Pu) / (abs(hel_u) + 1e-30))

    return {
        "num_k_pairs": len(pairs),
        "real_helical_dim": 4 * len(pairs),
        "gram_matrix_diag": [float(G[0, 0]), float(G[1, 1]), float(G[2, 2])],
        "gram_offdiag_max": gram_offdiag_max,
        "gram_normalized_offdiag_max": gram_normalized_offdiag_max,
        "pi_o3_even_t_hel_norm": pi_o3_even_t_hel_norm,
        "schur_complement": schur_complement,
        "p_intertwine_err": p_intertwine_err,
        "p_t_hel_odd_err": p_t_hel_odd_err,
        "t_sq_id_err": t_sq_id_err,
        "t_sq_parity_blind_err": t_sq_parity_blind_err,
        "t_sq_cross_chirality_err": t_sq_cross_chirality_err,
        "k_half_recon_err": k_half_recon_err,
        "k_half_asym_norm": k_half_asym_norm,
        "realspace_parity_hel_flip_err": realspace_parity_hel_flip_err,
    }


def compute_vorticity_and_strain(u: np.ndarray, k_vec: np.ndarray):
    """Compute spectral vorticity omega = curl(u) and strain tensor S_ij = 0.5*(du_i/dx_j + du_j/dx_i)."""
    u_hat = np.fft.fftn(u, axes=(0, 1, 2))
    omega_hat = np.cross(1j * k_vec, u_hat)
    omega = np.fft.ifftn(omega_hat, axes=(0, 1, 2)).real

    # Velocity gradient grad_u[..., i, j] = d u_i / d x_j
    grad_u_hat = 1j * u_hat[..., :, None] * k_vec[..., None, :]
    grad_u = np.fft.ifftn(grad_u_hat, axes=(0, 1, 2)).real
    S = 0.5 * (grad_u + np.swapaxes(grad_u, -1, -2))
    return omega, S


def block_average(arr: np.ndarray, b: int) -> np.ndarray:
    """Coarse-grain array over b x b x b periodic blocks (b divides L)."""
    L = arr.shape[0]
    nb = L // b
    rest = arr.shape[3:]
    reshaped = arr.reshape((nb, b, nb, b, nb, b) + rest)
    return reshaped.mean(axis=(1, 3, 5))


def measure_cocycle_and_stretching(u: np.ndarray, k_vec: np.ndarray, scales=(1, 2, 4)):
    """Measure Constantin-Fefferman SO(3) vorticity frame alignment cocycle defect delta_NS(b)
    and coarse-grained block vortex-stretching transfer rho_stretch^BLK(b) across b in {1, 2, 4}."""
    omega, S = compute_vorticity_and_strain(u, k_vec)
    om_norm = np.linalg.norm(omega, axis=-1)
    max_om = float(np.max(om_norm))
    active = om_norm > (1e-10 * max_om if max_om > 0 else 1e-12)

    om_hat = np.zeros_like(omega)
    om_hat[active] = omega[active] / om_norm[active, None]

    # Fine-scale enstrophy-strain normalization denominator
    S_frob = np.linalg.norm(S, axis=(-2, -1))
    fine_denom = float(np.mean((om_norm ** 2) * S_frob))

    results = {}
    for b in scales:
        # 1. Constantin-Fefferman cocycle defect delta_NS(b) = 1 - <(omega_hat(x) . omega_hat(x+b))^2>
        align_vals = []
        for axis in (0, 1, 2):
            shifted_hat = np.roll(om_hat, shift=-b, axis=axis)
            shifted_act = np.roll(active, shift=-b, axis=axis)
            both = active & shifted_act
            if np.any(both):
                dots = np.sum(om_hat[both] * shifted_hat[both], axis=-1)
                align_vals.append(float(np.mean(dots ** 2)))
        mean_align_sq = float(np.mean(align_vals)) if align_vals else 1.0
        delta_ns = float(1.0 - mean_align_sq)

        # 2. Coarse-grained block vortex-stretching transfer rho_stretch^BLK(b)
        om_b = block_average(omega, b)
        S_b = block_average(S, b)
        # omega_b^T S_b omega_b
        stretch_b = np.einsum("...i,...ij,...j->...", om_b, S_b, om_b)
        rho_stretch_blk = float(np.mean(np.abs(stretch_b)) / fine_denom) if fine_denom > 0 else 0.0

        results[str(b)] = {
            "delta_NS": delta_ns,
            "mean_align_sq": mean_align_sq,
            "rho_stretch_BLK": rho_stretch_blk,
        }
    return results


def verify_vorticity_cocycle_fields(L: int = 12):
    """Part 3: Compare 1D/Abelian parallel vortex tube vs 3D heterochiral Taylor-Green / Kida-Pelz tangle."""
    X, Y, Z, k_vec, _, _ = build_grid_and_wavevectors(L)

    # Field A: 1D/Abelian parallel vortex tube (vorticity purely along z-axis)
    # u = (-sin(y), sin(x), 0) -> omega = (0, 0, cos(x) + cos(y)) -> omega_hat = +- e_z
    u_abelian = np.stack(
        [
            -np.sin(Y),
            np.sin(X),
            np.zeros_like(X),
        ],
        axis=-1,
    )

    # Field B: 3D heterochiral Taylor-Green + Kida-Pelz multi-mode vortex tangle
    u_tg = np.stack(
        [
            np.sin(X) * np.cos(Y) * np.cos(Z),
            -np.cos(X) * np.sin(Y) * np.cos(Z),
            np.zeros_like(X),
        ],
        axis=-1,
    )
    # Kida-Pelz cyclic 3D component + higher-harmonic heterochiral modes
    u_kp = np.stack(
        [
            np.sin(X) * (np.cos(3 * Y) * np.cos(Z) - np.cos(Y) * np.cos(3 * Z)),
            np.sin(Y) * (np.cos(3 * Z) * np.cos(X) - np.cos(Z) * np.cos(3 * X)),
            np.sin(Z) * (np.cos(3 * X) * np.cos(Y) - np.cos(X) * np.cos(3 * Y)),
        ],
        axis=-1,
    )
    # Add a divergence-free ABC + multi-k heterochiral tangle perturbation
    u_abc = np.stack(
        [
            np.sin(2 * Z) + 0.7 * np.cos(2 * Y),
            np.sin(2 * X) + 0.7 * np.cos(2 * Z),
            np.sin(2 * Y) + 0.7 * np.cos(2 * X),
        ],
        axis=-1,
    )
    u_tangle = u_tg + 0.6 * u_kp + 0.5 * u_abc

    # Project u_tangle to exact divergence-free on active shell
    u_tangle_hat = np.fft.fftn(u_tangle, axes=(0, 1, 2))
    kn2 = np.sum(k_vec ** 2, axis=-1, keepdims=True)
    kn2_safe = np.where(kn2 > 0, kn2, 1.0)
    k_dot_u = np.sum(k_vec * u_tangle_hat, axis=-1, keepdims=True)
    u_tangle_hat = u_tangle_hat - np.where(kn2 > 0, k_vec * (k_dot_u / kn2_safe), 0.0)
    u_tangle = np.fft.ifftn(u_tangle_hat, axes=(0, 1, 2)).real

    abelian_res = measure_cocycle_and_stretching(u_abelian, k_vec, scales=(1, 2, 4))
    tangle_res = measure_cocycle_and_stretching(u_tangle, k_vec, scales=(1, 2, 4))

    return {
        "abelian_parallel_vortex_tube": abelian_res,
        "heterochiral_tg_kida_pelz_tangle": tangle_res,
    }


def main():
    part1 = verify_cl30_helical_basis(L=12)
    part2 = verify_parity_gram_schur_and_half_op(L=12)
    part3 = verify_vorticity_cocycle_fields(L=12)

    ab = part3["abelian_parallel_vortex_tube"]
    tg = part3["heterochiral_tg_kida_pelz_tangle"]

    checks = {
        "cl30_involution_ok": part1["max_cl_involution_err"] < 1e-14,
        "beltrami_eigen_ok": part1["max_curl_eig_err"] < 1e-13
        and part1["beltrami_plus_err"] < 1e-13
        and part1["beltrami_minus_err"] < 1e-13,
        "helical_orthogonality_ok": part1["helical_orthogonality_err"] < 1e-14
        and part1["parseval_err"] < 1e-14,
        "o3_even_projection_zero_ok": part2["pi_o3_even_t_hel_norm"] < 1e-14,
        "gram_diagonal_ok": part2["gram_normalized_offdiag_max"] < 1e-14,
        "schur_complement_pos_ok": part2["schur_complement"] > 0.0,
        "t_hel_sq_parity_blind_ok": part2["t_sq_id_err"] < 1e-14
        and part2["t_sq_parity_blind_err"] < 1e-14
        and part2["t_sq_cross_chirality_err"] < 1e-14,
        "k_half_reconstruction_ok": part2["k_half_recon_err"] < 1e-14,
        "abelian_delta_ns_zero_ok": all(
            abs(ab[str(b)]["delta_NS"]) < 1e-14 for b in (1, 2, 4)
        ),
        "tangle_delta_ns_grows_and_depletes_stretch_ok": (
            tg["1"]["delta_NS"] < tg["2"]["delta_NS"] < tg["4"]["delta_NS"]
            and tg["4"]["delta_NS"] > 0.5
            and tg["1"]["rho_stretch_BLK"] > tg["2"]["rho_stretch_BLK"] > tg["4"]["rho_stretch_BLK"]
        ),
    }

    all_ok = all(checks.values())
    receipt = {
        "status": "CL30_HELICAL_SCHUR_COCYCLE_OK" if all_ok else "FAILED",
        "NS_GLOBAL_REGULARITY_OPEN": True,
        "checks": checks,
        "part1_cl30_helical_basis": part1,
        "part2_parity_gram_schur_half_op": part2,
        "part3_vorticity_cocycle_and_stretching": part3,
    }

    out_path = Path(__file__).resolve().parent / "probe_cl30_helical_schur_results.json"
    out_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
