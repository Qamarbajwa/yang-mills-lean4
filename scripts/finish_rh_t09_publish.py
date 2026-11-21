import json
import os
import time
import urllib.request
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from publish_all_zenodo_standalone_papers import get_token, api_json, upload_file_to_bucket, compute_hashes

token = get_token()
dep_id = 24409899

base_dir = r"d:\Comfy UI\rheihman hypothesis\research\interactive_lab\monograph_additive_multiplicative\zenodo_theorem_papers\RH_T09_Two_Piece_Factorized_Mollifiers_And_True_Signed_Weil_Schur_Coercivity"
ext_base = "\\\\?\\" + os.path.abspath(base_dir)

pdf_path = Path(ext_base + "\\RH_T09_Two_Piece_Factorized_Mollifiers_And_True_Signed_Weil_Schur_Coercivity_Paper.pdf")
tex_path = Path(ext_base + "\\RH_T09_Two_Piece_Factorized_Mollifiers_And_True_Signed_Weil_Schur_Coercivity_Paper.tex")
zip_path = Path(ext_base + "\\RH_T09_ZENODO.zip")
zen_path = Path(ext_base + "\\.zenodo.json")

print(f"Checking files for RH_T09 in {ext_base}...")
print("PDF exists:", pdf_path.exists(), f"({pdf_path.stat().st_size:,} bytes)")
print("TeX exists:", tex_path.exists(), f"({tex_path.stat().st_size:,} bytes)")
print("ZIP exists:", zip_path.exists(), f"({zip_path.stat().st_size:,} bytes)")

# Get deposition bucket
dep = api_json("GET", f"https://zenodo.org/api/deposit/depositions/{dep_id}", token)
bucket_url = dep["links"]["bucket"]
print(f"Bucket URL: {bucket_url}")

# Upload each file
uploaded = []
for fp in [pdf_path, tex_path, zip_path]:
    print(f"Uploading {fp.name}...")
    u = upload_file_to_bucket(bucket_url, token, fp)
    uploaded.append(u)

# Publish
print(f"Publishing deposition {dep_id}...")
pub = api_json("POST", f"https://zenodo.org/api/deposit/depositions/{dep_id}/actions/publish", token)
doi = pub.get("doi")
concept_doi = pub.get("conceptdoi")
rec_url = f"https://zenodo.org/records/{dep_id}"
print(f"SUCCESS: DOI={doi} | CONCEPT_DOI={concept_doi} | URL={rec_url}")

# Update local .zenodo.json
local_zen = json.loads(zen_path.read_text(encoding="utf-8"))
local_zen["doi"] = doi
local_zen["concept_doi"] = concept_doi
local_zen["record_url"] = rec_url
zen_path.write_text(json.dumps(local_zen, indent=2), encoding="utf-8")
print("Updated local .zenodo.json for RH_T09")
