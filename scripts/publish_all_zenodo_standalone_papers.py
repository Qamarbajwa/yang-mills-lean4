#!/usr/bin/env python3
"""Publish all standalone theorem papers to Zenodo with dedicated DOIs.

Handles:
- YM_00 through YM_T06 (7 Yang-Mills standalone papers)
- ROSETTA_T13 (Navier-Stokes / Rosetta master engineering paper)
- RH_T09 (Riemann Hypothesis two-piece factorized mollifiers paper)

Verifies remote MD5 checksums, publishes each deposition, records assigned DOIs,
updates local .zenodo.json files, and writes a master receipt.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
import winreg
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ZENODO_API = "https://zenodo.org/api"


def get_token() -> str:
    for var in ("ZENODO_TOKEN", "ZENODO_ACCESS_TOKEN", "ZENODO_API_TOKEN"):
        val = os.environ.get(var, "").strip()
        if val:
            return val
    try:
        k = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment")
        token, _ = winreg.QueryValueEx(k, "ZENODO_TOKEN")
        if token.strip():
            return token.strip()
    except Exception:
        pass
    raise RuntimeError("Missing ZENODO_TOKEN in environment or registry")


def compute_hashes(path: Path) -> tuple[str, str]:
    h_sha = hashlib.sha256()
    h_md5 = hashlib.md5()
    with path.open("rb") as f:
        while chunk := f.read(65536):
            h_sha.update(chunk)
            h_md5.update(chunk)
    return h_sha.hexdigest(), h_md5.hexdigest()


def api_json(method: str, url: str, token: str, payload: Dict[str, Any] | None = None) -> Dict[str, Any]:
    headers = {"Authorization": f"Bearer {token}"}
    data: bytes | None = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
    for attempt in range(5):
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw) if raw.strip() else {}
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            if exc.code in (429, 500, 502, 503, 504) and attempt < 4:
                wait_sec = 4 * (attempt + 1)
                print(f"[RETRY] HTTP {exc.code} on {method} {url}, waiting {wait_sec}s...")
                time.sleep(wait_sec)
                continue
            raise RuntimeError(f"Zenodo HTTP {exc.code} on {method} {url}: {body}") from exc
    raise RuntimeError(f"Zenodo request failed after retries: {method} {url}")


def upload_file_to_bucket(bucket_url: str, token: str, file_path: Path) -> Dict[str, Any]:
    sha256, md5 = compute_hashes(file_path)
    data = file_path.read_bytes()
    url = f"{bucket_url.rstrip('/')}/{file_path.name}"
    for attempt in range(5):
        req = urllib.request.Request(
            url,
            data=data,
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/octet-stream"},
            method="PUT",
        )
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                info = json.loads(resp.read().decode("utf-8"))
            remote_chk = info.get("checksum", "")
            if remote_chk != f"md5:{md5}":
                raise RuntimeError(f"MD5 mismatch for {file_path.name}: {remote_chk} vs md5:{md5}")
            return {
                "filename": file_path.name,
                "size_bytes": file_path.stat().st_size,
                "local_sha256": sha256,
                "local_md5": md5,
                "remote_checksum": remote_chk,
            }
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503, 504) and attempt < 4:
                wait_sec = 4 * (attempt + 1)
                print(f"[RETRY] HTTP {exc.code} on PUT {file_path.name}, waiting {wait_sec}s...")
                time.sleep(wait_sec)
                continue
            raise
    raise RuntimeError(f"Failed uploading {file_path.name}")


def clean_metadata(zenodo_json_path: Path) -> Dict[str, Any]:
    raw = json.loads(zenodo_json_path.read_text(encoding="utf-8"))
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    creators = [
        {
            "name": "Munawer, Qamar",
            "affiliation": "Brandenburg University of Technology Cottbus-Senftenberg",
        }
    ]

    desc = raw.get("description", "")
    if "ai is being used as a tool" not in desc:
        desc += "<p><strong>Methodology:</strong> In accordance with transparent scientific standards, ai is being used as a tool for formal verification and computation.</p>"

    meta: Dict[str, Any] = {
        "title": raw.get("title", ""),
        "upload_type": raw.get("upload_type", "publication"),
        "publication_type": raw.get("publication_type", "workingpaper"),
        "publication_date": today_str,
        "description": desc,
        "creators": creators,
        "license": "cc-by-4.0",
        "access_right": "open",
        "keywords": raw.get("keywords", ["Lean 4", "BTU Cottbus-Senftenberg"]),
    }
    return {"metadata": meta}


def publish_standalone_folder(token: str, folder_path: Path) -> Dict[str, Any]:
    zen_file = folder_path / ".zenodo.json"
    if not zen_file.exists():
        raise FileNotFoundError(f"Missing .zenodo.json in {folder_path}")

    # Gather files: PDF, TeX, ZIP
    pdfs = list(folder_path.glob("*.pdf"))
    texs = list(folder_path.glob("*.tex"))
    zips = list(folder_path.glob("*_ZENODO.zip"))

    if not pdfs:
        raise FileNotFoundError(f"No PDF found in {folder_path}")
    if not texs:
        raise FileNotFoundError(f"No TeX found in {folder_path}")
    if not zips:
        raise FileNotFoundError(f"No _ZENODO.zip found in {folder_path}")

    pdf_file = pdfs[0]
    tex_file = texs[0]
    zip_file = zips[0]

    # Special case: YM_00 was already created and published as 24409870
    if folder_path.name == "YM_00_Common_Person_Guide":
        dep_id = 24409870
        doi = "10.5281/zenodo.24409870"
        concept_doi = "10.5281/zenodo.24409869"
        rec_url = f"https://zenodo.org/records/{dep_id}"
        print(f"\n=======================================================")
        print(f"Skipping recreation for already published: {folder_path.name}")
        print(f"ALREADY PUBLISHED: DOI={doi} | CONCEPT_DOI={concept_doi} | URL={rec_url}")
        local_zen = json.loads(zen_file.read_text(encoding="utf-8"))
        local_zen["doi"] = doi
        local_zen["concept_doi"] = concept_doi
        local_zen["record_url"] = rec_url
        zen_file.write_text(json.dumps(local_zen, indent=2), encoding="utf-8")
        h_sha, _ = compute_hashes(pdf_file)
        return {
            "folder": folder_path.name,
            "folder_path": str(folder_path),
            "deposition_id": dep_id,
            "doi": doi,
            "concept_doi": concept_doi,
            "record_url": rec_url,
            "pdf_name": pdf_file.name,
            "pdf_sha256": h_sha,
            "published_at_utc": datetime.now(timezone.utc).isoformat(),
        }

    meta_payload = clean_metadata(zen_file)
    print(f"\n=======================================================")
    print(f"Publishing: {folder_path.name}")
    print(f"Title: {meta_payload['metadata']['title']}")
    print(f"Files: {pdf_file.name}, {tex_file.name}, {zip_file.name}")

    # Create deposition
    dep = api_json("POST", f"{ZENODO_API}/deposit/depositions", token, meta_payload)
    dep_id = int(dep["id"])
    bucket_url = dep["links"]["bucket"]
    print(f"Deposition created: ID={dep_id}")

    # Upload files
    uploaded_files = []
    for fp in [pdf_file, tex_file, zip_file]:
        print(f"Uploading {fp.name} ({fp.stat().st_size:,} bytes)...")
        u_info = upload_file_to_bucket(bucket_url, token, fp)
        uploaded_files.append(u_info)

    # Publish deposition
    print(f"Publishing deposition ID={dep_id}...")
    pub = api_json("POST", f"{ZENODO_API}/deposit/depositions/{dep_id}/actions/publish", token)
    doi = str(pub.get("doi") or "")
    concept_doi = str(pub.get("conceptdoi") or "")
    rec_url = f"https://zenodo.org/records/{dep_id}"
    print(f"SUCCESS: DOI={doi} | CONCEPT_DOI={concept_doi} | URL={rec_url}")

    # Update local .zenodo.json
    local_zen = json.loads(zen_file.read_text(encoding="utf-8"))
    local_zen["doi"] = doi
    local_zen["concept_doi"] = concept_doi
    local_zen["record_url"] = rec_url
    zen_file.write_text(json.dumps(local_zen, indent=2), encoding="utf-8")

    return {
        "folder": folder_path.name,
        "folder_path": str(folder_path),
        "deposition_id": dep_id,
        "doi": doi,
        "concept_doi": concept_doi,
        "record_url": rec_url,
        "pdf_name": pdf_file.name,
        "pdf_sha256": uploaded_files[0]["local_sha256"],
        "files": uploaded_files,
        "published_at_utc": datetime.now(timezone.utc).isoformat(),
    }


def main():
    token = get_token()
    ym_root = Path(r"d:/Comfy UI/yang mills and the mass gap")
    ns_root = Path(r"d:/Comfy UI/tubulance")
    rh_root = Path(r"d:/Comfy UI/rheihman hypothesis")

    target_folders: List[Path] = [
        # 7 Yang-Mills standalone theorem papers
        ym_root / "zenodo_theorem_papers" / "YM_00_Common_Person_Guide",
        ym_root / "zenodo_theorem_papers" / "YM_T01_Abelian_Circle_Vs_NonAbelian_S3_Holonomy",
        ym_root / "zenodo_theorem_papers" / "YM_T02_Covolume_Fiber_Tare_And_Schur_Split",
        ym_root / "zenodo_theorem_papers" / "YM_T03_Opposite_Side_Contradiction_UV_And_Massless",
        ym_root / "zenodo_theorem_papers" / "YM_T04_S3_Character_Cocycle_And_Polymer_Tree",
        ym_root / "zenodo_theorem_papers" / "YM_T05_Finite_To_Continuum_OS_And_Symanzik",
        ym_root / "zenodo_theorem_papers" / "YM_T06_Balaban_Multiscale_Mass_Floor_And_Area_Law",
        # Navier-Stokes / Rosetta master engineering paper
        ns_root / "zenodo_theorem_papers" / "ROSETTA_T13_Pythagorean_Schur_Energy_Block_Pfaffian_And_Real_Life_Engineering_Paper",
        # Riemann Hypothesis two-piece factorized mollifiers paper
        rh_root / "research" / "interactive_lab" / "monograph_additive_multiplicative" / "zenodo_theorem_papers" / "RH_T09_Two_Piece_Factorized_Mollifiers_And_True_Signed_Weil_Schur_Coercivity",
    ]

    results = []
    for tf in target_folders:
        if not tf.exists():
            print(f"[ERROR] Target folder not found: {tf}")
            sys.exit(1)

    print(f"Starting publication of {len(target_folders)} standalone papers to Zenodo...")
    for tf in target_folders:
        res = publish_standalone_folder(token, tf)
        results.append(res)
        time.sleep(2)  # courteous delay between depositions

    receipt = {
        "status": "ALL_PUBLISHED_SUCCESSFULLY",
        "published_utc": datetime.now(timezone.utc).isoformat(),
        "total_papers": len(results),
        "author": "Qamar Munawer",
        "affiliation": "Brandenburg University of Technology Cottbus-Senftenberg",
        "methodology": "ai is being used as a tool",
        "papers": results,
    }

    receipt_path = ym_root / "dist" / "ZENODO_STANDALONE_PAPERS_PUBLISHED_RECEIPT.json"
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(f"\n=======================================================")
    print(f"ALL PAPERS PUBLISHED SUCCESSFULLY!")
    print(f"Receipt written to: {receipt_path}")


if __name__ == "__main__":
    main()
