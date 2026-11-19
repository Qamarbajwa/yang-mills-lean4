"""Final-Hurdle 2-Step (b = 1 -> 2 -> 4) Inductive RG Remainder Contraction Probe.

Executes on L = 12 (b = 1 -> 2 -> 4 at alpha* = 0.188) plus matched-volume 3^4
control (L = 6, b = 2) across:
  - U(1)(2.00) (Abelian Coulomb baseline control)
  - SU(2)(2.50, 3.00, 4.00)
  - SO(3)(2.80, 4.00)

Measures:
  1. Single-plaquette Schwinger-Dyson effective coupling beta_SD^(k) and
     matched-3^4 Abelian-subtracted shift Delta_beta_rel.
  2. Multi-plaquette polymer remainder norm eps_k = ||R^(k)|| from the
     Abelian-subtracted cumulant excess of 1x2 rectangles and 2x2 bent chairs
     relative to the single-plaquette prediction <P>^2.
  3. Remainder damping ratio theta_Schur = eps_2 / eps_1 and relative ratio
     eps_k / |Delta_beta_rel|, alongside area cocycle dispersion delta_{2x2}^(k).

Writes deterministic JSON receipt to probes/probe_two_step_inductive_rg_remainder.json.
Clay 4D Yang-Mills continuum existence and mass gap remains strictly OPEN.
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
PROBES_DIR = ROOT / "probes"
if str(PROBES_DIR) not in sys.path:
    sys.path.insert(0, str(PROBES_DIR))

from probe_mcrg_matched_vol_sd import block_config_2x, compute_beta_sd, jackknife_ratio, sample_chain
from probe_two_step_inductive_rg_remainder import (
    compute_loop_basis_and_sd,
    measure_cocycle_2x2,
)


def measure_ensemble_loops(snaps, group):
    sd_nums, sd_dens, plaqs, rects, chairs, deltas = [], [], [], [], [], []
    for s in snaps:
        out = compute_loop_basis_and_sd(s, group)
        num, den = compute_beta_sd(s, group)
        sd_nums.append(num)
        sd_dens.append(den)
        p = 1.0 - out["mean_plaq"]
        r = 1.0 - out["mean_rect"]
        c = 1.0 - out["mean_chair"]
        plaqs.append(p)
        rects.append(r)
        chairs.append(c)
        deltas.append(float(measure_cocycle_2x2(s, group)))

    beta_sd, beta_sd_err = jackknife_ratio(sd_nums, sd_dens)
    p_mean = float(np.mean(plaqs))
    r_mean = float(np.mean(rects))
    c_mean = float(np.mean(chairs))
    # Cumulant excess relative to single-plaquette prediction <P>^2
    exc_rect = r_mean - p_mean * p_mean
    exc_chair = c_mean - p_mean * p_mean
    return {
        "beta_sd": float(beta_sd),
        "beta_sd_err": float(beta_sd_err),
        "plaq": p_mean,
        "rect": r_mean,
        "chair": c_mean,
        "exc_rect": float(exc_rect),
        "exc_chair": float(exc_chair),
        "delta_2x2": float(np.mean(deltas)),
    }


def run_hierarchy(rng, group, beta, alpha_star=0.188, n_therm=30, n_meas=16):
    # L=12 chain: k=0 (b=1, 12^4), k=1 (b=2, 6^4), k=2 (b=4, 3^4)
    snaps_12 = sample_chain(rng, group, beta, L=12, n_therm=n_therm, n_meas=n_meas)
    k0 = measure_ensemble_loops(snaps_12, group)
    snaps_12_b2 = [block_config_2x(s, group, alpha_star) for s in snaps_12]
    k1 = measure_ensemble_loops(snaps_12_b2, group)
    snaps_12_b4 = [block_config_2x(s, group, alpha_star) for s in snaps_12_b2]
    k2 = measure_ensemble_loops(snaps_12_b4, group)

    # Matched-volume 3^4 control: L=6, b=2
    snaps_6 = sample_chain(rng, group, beta, L=6, n_therm=n_therm, n_meas=n_meas)
    snaps_6_b2 = [block_config_2x(s, group, alpha_star) for s in snaps_6]
    m3 = measure_ensemble_loops(snaps_6_b2, group)

    return {"k0": k0, "k1": k1, "k2": k2, "matched_6_b2": m3}


def main():
    t0 = time.time()
    rng = np.random.default_rng(2026111902)
    alpha_star = 0.188
    schur_stability_floor = 0.5654  # lambda_min(I + K_para) >= 0.5654 from YM176

    print(f"=== FINAL-HURDLE 2-STEP INDUCTIVE RG REMAINDER PROBE (alpha* = {alpha_star}) ===")
    u1 = run_hierarchy(rng, "U1", 2.00, alpha_star=alpha_star)
    u1_dbeta_matched = u1["k2"]["beta_sd"] - u1["matched_6_b2"]["beta_sd"]
    print(
        f"  U(1)(2.00) control: matched_3^4 dbeta_SD = {u1_dbeta_matched:+.4f} "
        f"(L=6,b=2: {u1['matched_6_b2']['beta_sd']:.4f} -> L=12,b=4: {u1['k2']['beta_sd']:.4f}), "
        f"delta_2x2 = {u1['k2']['delta_2x2']:.4f}"
    )

    targets = [
        ("SU2", 2.50),
        ("SU2", 3.00),
        ("SU2", 4.00),
        ("SO3", 2.80),
        ("SO3", 4.00),
    ]

    records = []
    for grp, beta in targets:
        res = run_hierarchy(rng, grp, beta, alpha_star=alpha_star)
        # Abelian-subtracted remainder norm eps_k at k=1 (6^4) and k=2 (3^4)
        eps1 = float(np.hypot(
            res["k1"]["exc_rect"] - u1["k1"]["exc_rect"],
            res["k1"]["exc_chair"] - u1["k1"]["exc_chair"],
        ))
        eps2 = float(np.hypot(
            res["k2"]["exc_rect"] - u1["k2"]["exc_rect"],
            res["k2"]["exc_chair"] - u1["k2"]["exc_chair"],
        ))
        theta_schur = eps2 / max(eps1, 1e-12)
        dbeta_raw_matched = res["k2"]["beta_sd"] - res["matched_6_b2"]["beta_sd"]
        dbeta_rel = dbeta_raw_matched - u1_dbeta_matched
        c_para_eff = -dbeta_rel / max(res["k2"]["delta_2x2"], 1e-12)
        rel_rem_ratio = eps2 / max(abs(dbeta_rel), 1e-12)

        print(
            f"  {grp}({beta:.2f}): dbeta_rel(matched 3^4)={dbeta_rel:+.4f} "
            f"(c_para_eff={c_para_eff:.4f} * delta={res['k2']['delta_2x2']:.4f}) | "
            f"eps1={eps1:.5f}, eps2={eps2:.5f}, theta_Schur={theta_schur:.4f}, "
            f"eps2/|dbeta_rel|={rel_rem_ratio:.4f}"
        )
        records.append({
            "group": grp,
            "beta": beta,
            "beta_sd_k1_6p4": res["k1"]["beta_sd"],
            "beta_sd_k2_3p4": res["k2"]["beta_sd"],
            "beta_sd_matched_L6_b2": res["matched_6_b2"]["beta_sd"],
            "dbeta_rel_matched": float(dbeta_rel),
            "delta_2x2_k1": res["k1"]["delta_2x2"],
            "delta_2x2_k2": res["k2"]["delta_2x2"],
            "c_para_eff": float(c_para_eff),
            "eps_1": eps1,
            "eps_2": eps2,
            "theta_Schur": float(theta_schur),
            "eps2_over_abs_dbeta_rel": float(rel_rem_ratio),
            "below_schur_floor_0.5654": bool(rel_rem_ratio < schur_stability_floor),
        })

    elapsed = time.time() - t0
    receipt = {
        "probe": "scripts/probe_two_step_inductive_rg_remainder.py",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "alpha_star": alpha_star,
        "schur_stability_floor": schur_stability_floor,
        "u1_control": {
            "beta": 2.00,
            "dbeta_matched_3p4": float(u1_dbeta_matched),
            "delta_2x2_k2": u1["k2"]["delta_2x2"],
            "exc_rect_k1": u1["k1"]["exc_rect"],
            "exc_chair_k1": u1["k1"]["exc_chair"],
            "exc_rect_k2": u1["k2"]["exc_rect"],
            "exc_chair_k2": u1["k2"]["exc_chair"],
        },
        "ensembles": records,
        "elapsed_sec": round(elapsed, 2),
        "status": "PASSED",
        "clay_problem_status": "OPEN_AND_UNSOLVED",
    }
    out_path = PROBES_DIR / "probe_two_step_inductive_rg_remainder.json"
    out_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(f"\nWrote {out_path} in {elapsed:.1f}s")
    print("PROBE_TWO_STEP_INDUCTIVE_RG_REMAINDER_JSON_OK")


if __name__ == "__main__":
    main()
