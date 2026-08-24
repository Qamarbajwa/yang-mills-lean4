from pathlib import Path
import yaml

REQUIRED_FILES = [
    "PROJECT_PROFILE.md",
    "CURRENT_SCIENTIFIC_STATE.md",
    "SOURCE_OF_TRUTH.md",
    "OFFICIAL_PROBLEM_SPECIFICATION.md",
    "RESEARCH_LEDGER.md",
    "THEOREM_LEDGER.md",
    "DEFINITION_LEDGER.md",
    "HYPOTHESIS_REGISTER.md",
    "OPEN_LEMMA_REGISTER.md",
    "REJECTION_LEDGER.md",
    "NEGATIVE_EVIDENCE_REGISTER.md",
    "EVIDENCE_LEDGER.md",
    "CLAIM_EVIDENCE_MATRIX.md",
    "TEST_STRATEGY.md",
    "VERIFICATION_LEDGER.md",
    "TASK_GRAPH.md",
    "NEXT_ACTION.md",
    "governance/bootstrap.yaml",
    "governance/risk-policy.yaml",
    "governance/project-governance.yaml",
    "governance/trust-anchor.yaml",
]

def missing_required_files(root: Path):
    return [rel for rel in REQUIRED_FILES if not (root / rel).exists()]

def load_yaml(root: Path, rel: str):
    with (root / rel).open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def governance_project_id(root: Path):
    return load_yaml(root, "governance/project-governance.yaml")["project"]["id"]
