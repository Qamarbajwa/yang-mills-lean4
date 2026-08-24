from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
from ymmg.repo import missing_required_files, load_yaml

def main():
    missing = missing_required_files(ROOT)
    if missing:
        print("FAIL: missing required files")
        for item in missing:
            print(f" - {item}")
        return 1

    for rel in [
        "governance/bootstrap.yaml",
        "governance/risk-policy.yaml",
        "governance/project-governance.yaml",
        "governance/trust-anchor.yaml",
    ]:
        load_yaml(ROOT, rel)

    print("PASS: repository invariants and governance YAML are readable.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
