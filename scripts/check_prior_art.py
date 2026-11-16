#!/usr/bin/env python3
"""
Prior-Art Formalization Status Audit across Mathlib4, PhysLean, and DeepMind formal-conjectures.
Queries live GitHub code search and PR list to determine the state of Lean 4 formalization
for 6 targeted mathematical and physical domains.
Outputs receipt to `prior_art_audit_receipt.json`.
"""

import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from typing import Any, Dict, List

REPOSITORIES = [
    "leanprover-community/mathlib4",
    "HEPLean/PhysLean",
    "google-deepmind/formal-conjectures",
]

TARGETS = [
    {
        "id": "TARGET-1",
        "name": "Yang–Mills Existence & Mass Gap Specification / Wilson Lattice Action",
        "keywords": ["YangMills", "WilsonAction", "massGap"],
    },
    {
        "id": "TARGET-2",
        "name": "Osterwalder–Schrader Axioms & Reflection Positivity",
        "keywords": ["OsterwalderSchrader", "reflectionPositivity", "Schwinger"],
    },
    {
        "id": "TARGET-3",
        "name": "2x2 Block Schur Complement Quadratic Forms",
        "keywords": ["schurComplement", "fromBlocks", "schur_complement_quadratic"],
    },
    {
        "id": "TARGET-4",
        "name": "Quaternion Centralizer & 't Hooft Twisted Boundary Rigidity",
        "keywords": ["Quaternion", "centralizer", "tHooft", "twistedBoundary"],
    },
    {
        "id": "TARGET-5",
        "name": "SU(2) Weyl Integration Measure & Vandermonde Collar Bounds",
        "keywords": ["weylIntegration", "vandermonde", "SU2", "haarMeasure"],
    },
    {
        "id": "TARGET-6",
        "name": "Polymer Cluster Expansion & Kotecký–Preiss Convergence",
        "keywords": ["clusterExpansion", "KoteckyPreiss", "polymer"],
    },
]


def get_gh_token() -> str:
    try:
        res = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            check=True,
        )
        return res.stdout.strip()
    except Exception:
        return os.environ.get("GITHUB_TOKEN", "")


def run_gh_code_search(repo: str, keyword: str) -> List[Dict[str, Any]]:
    cmd = [
        "gh", "search", "code",
        "--repo", repo,
        keyword,
        "--limit", "30",
        "--json", "path,repository",
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if res.returncode == 0:
            return json.loads(res.stdout or "[]")
        elif "rate limit" in res.stderr.lower():
            time.sleep(5)
            res2 = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            if res2.returncode == 0:
                return json.loads(res2.stdout or "[]")
            return []
        else:
            return []
    except Exception:
        return []


def run_gh_pr_search(repo: str, keyword: str) -> List[Dict[str, Any]]:
    cmd = [
        "gh", "pr", "list",
        "--repo", repo,
        "--state", "all",
        "--search", keyword,
        "--limit", "20",
        "--json", "number,title,state,url",
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if res.returncode == 0:
            return json.loads(res.stdout or "[]")
        else:
            return []
    except Exception:
        return []


def perform_audit() -> Dict[str, Any]:
    print("=" * 80)
    print("  LIVE GITHUB PRIOR-ART SCAN: Mathlib4, PhysLean & DeepMind Formal-Conjectures")
    print(f"  Timestamp: {datetime.now(timezone.utc).isoformat()}")
    print("=" * 80)

    audit_results = {
        "audit_version": "1.0.0",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "repositories_scanned": REPOSITORIES,
        "targets": [],
    }

    summary_rows = []

    for target in TARGETS:
        t_id = target["id"]
        t_name = target["name"]
        keywords = target["keywords"]
        print(f"\nScanning {t_id}: {t_name}")

        target_data: Dict[str, Any] = {
            "id": t_id,
            "name": t_name,
            "keywords": keywords,
            "results_by_repo": {},
            "total_code_hits": 0,
            "total_pr_hits": 0,
        }

        for repo in REPOSITORIES:
            target_data["results_by_repo"][repo] = {
                "keywords": {},
                "repo_code_hits": 0,
                "repo_pr_hits": 0,
            }

            for kw in keywords:
                # Small pause to respect secondary rate limits
                time.sleep(1.2)
                code_hits = run_gh_code_search(repo, kw)
                pr_hits = run_gh_pr_search(repo, kw)

                # Filter hits to ensure valid paths
                paths = [h["path"] for h in code_hits if isinstance(h, dict) and "path" in h]
                prs = [{"number": p["number"], "title": p["title"], "state": p["state"]} for p in pr_hits if isinstance(p, dict)]

                target_data["results_by_repo"][repo]["keywords"][kw] = {
                    "code_count": len(paths),
                    "code_paths": paths[:10],
                    "pr_count": len(prs),
                    "prs": prs[:5],
                }
                target_data["results_by_repo"][repo]["repo_code_hits"] += len(paths)
                target_data["results_by_repo"][repo]["repo_pr_hits"] += len(prs)

            r_code = target_data["results_by_repo"][repo]["repo_code_hits"]
            r_pr = target_data["results_by_repo"][repo]["repo_pr_hits"]
            target_data["total_code_hits"] += r_code
            target_data["total_pr_hits"] += r_pr

            print(f"  - {repo:<36}: {r_code} code matches, {r_pr} PRs")

        audit_results["targets"].append(target_data)
        summary_rows.append((t_id, t_name, target_data["total_code_hits"], target_data["total_pr_hits"]))

    receipt_path = "prior_art_audit_receipt.json"
    with open(receipt_path, "w", encoding="utf-8") as f:
        json.dump(audit_results, f, indent=2)

    print("\n" + "=" * 80)
    print(f"{'Target ID':<10} | {'Domain':<50} | {'Code Hits':<10} | {'PR Hits':<8}")
    print("-" * 80)
    for t_id, t_name, code_hits, pr_hits in summary_rows:
        short_name = (t_name[:47] + "...") if len(t_name) > 50 else t_name
        print(f"{t_id:<10} | {short_name:<50} | {code_hits:<10} | {pr_hits:<8}")
    print("=" * 80)
    print(f"Receipt written successfully to {receipt_path}\n")

    return audit_results


if __name__ == "__main__":
    perform_audit()
