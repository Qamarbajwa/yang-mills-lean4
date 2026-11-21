"""
Publish YM_T08 Three-Split Octant Cube Paper to Zenodo
======================================================
Uploads YM_T08_Three_Split_Octant_Cube (.pdf, .tex, .zip) to Zenodo and publishes it
with an authentic permanent DOI.

Author: Qamar Munawer
Affiliation: Brandenburg University of Technology Cottbus-Senftenberg
Methodology: ai is being used as a tool
"""

import sys
import json
from pathlib import Path
from publish_all_zenodo_standalone_papers import get_token, publish_standalone_folder

def main():
    folder = Path("zenodo_theorem_papers/YM_T08_Three_Split_Octant_Cube").resolve()
    print(f"Target folder: {folder}")
    if not folder.exists():
        print(f"Error: folder {folder} does not exist!")
        sys.exit(1)
        
    token = get_token()
    print(f"Acquired Zenodo token (length={len(token)} chars).")
    
    result = publish_standalone_folder(token, folder)
    print("\n" + "=" * 60)
    print("ZENODO PUBLICATION SUCCESSFUL!")
    print(f"Title:       {result.get('title', 'YM_T08')}")
    print(f"DOI:         {result.get('doi')}")
    print(f"Concept DOI: {result.get('concept_doi')}")
    print(f"Record URL:  {result.get('record_url')}")
    print("=" * 60)
    
    receipt_file = Path("dist/YM_T08_ZENODO_PUBLISHED_RECEIPT.json")
    receipt_file.parent.mkdir(parents=True, exist_ok=True)
    with open(receipt_file, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Receipt written to {receipt_file}")

if __name__ == "__main__":
    main()
