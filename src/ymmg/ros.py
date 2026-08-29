import hashlib
import json
import subprocess
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

class ProjectBindingError(Exception):
    pass

class ConstitutionalIntegrityError(Exception):
    pass

EXPECTED_PROJECT_IDS = {"YM-MASS-GAP", "YANG_MILLS_MASS_GAP"}
EXPECTED_REPO_DIR_NAME = "yang mills and the mass gap"

SCIENTIFIC_FINGERPRINT_MANIFEST = [
    "CLAIM_EVIDENCE_MATRIX.md",
    "DEFINITION_LEDGER.md",
    "NEGATIVE_EVIDENCE_REGISTER.md",
    "OFFICIAL_PROBLEM_SPECIFICATION.md",
    "RESEARCH_LEDGER.md",
    "THEOREM_LEDGER.md",
    "governance/EPISTEMIC_TAXONOMY_v1.0.yaml",
    "governance/MATHEMATICAL_RESEARCH_OPERATING_SYSTEM_v1.0.md",
    "governance/PROJECT_BINDING_POLICY.md",
    "literature/ANALOGUE_DEPENDENCY_GRAPH.md",
    "literature/ANALOGUE_LIMITATION_MATRIX.md",
    "literature/ANALOGUE_MECHANISM_MATRIX.md",
    "literature/CONSTRUCTIVE_LIMITATION_MATRIX.md",
    "literature/FOUNDATIONAL_LIMITATION_MATRIX.md",
    "literature/MODERN_LIMITATION_MATRIX.md",
    "literature/PATHWAY_MEMORY_REGISTER.md",
]

def validate_project_binding(workspace_root: Path, task_project_id: str) -> bool:
    """
    Law 0: Minimal read-only inspection allowed to discover project identity.
    Fails closed if workspace, repository profile, governance project ID, or git root do not match.
    """
    if task_project_id not in EXPECTED_PROJECT_IDS:
        raise ProjectBindingError(f"Task project ID mismatch: '{task_project_id}' not in {EXPECTED_PROJECT_IDS}")
    
    workspace_root = workspace_root.resolve()
    
    # 1. Directory name check
    if workspace_root.name.lower() != EXPECTED_REPO_DIR_NAME.lower():
        raise ProjectBindingError(f"Workspace directory name mismatch: '{workspace_root.name}' != '{EXPECTED_REPO_DIR_NAME}'")
        
    # 2. File presence check
    profile_path = workspace_root / "PROJECT_PROFILE.md"
    gov_path = workspace_root / "governance" / "project-governance.yaml"
    
    if not profile_path.exists():
        raise ProjectBindingError(f"PROJECT_PROFILE.md missing in {workspace_root}")
    if not gov_path.exists():
        raise ProjectBindingError(f"governance/project-governance.yaml missing in {workspace_root}")
        
    # 3. PROJECT_PROFILE.md content check
    profile_text = profile_path.read_text(encoding="utf-8")
    if "YM-MASS-GAP" not in profile_text:
        raise ProjectBindingError("PROJECT_PROFILE.md does not match YM-MASS-GAP")
        
    # 4. governance/project-governance.yaml project.id check
    gov_data = yaml.safe_load(gov_path.read_text(encoding="utf-8"))
    if not isinstance(gov_data, dict) or "project" not in gov_data or gov_data["project"].get("id") != "YM-MASS-GAP":
        raise ProjectBindingError("governance/project-governance.yaml project.id does not match YM-MASS-GAP")
        
    # 5. Git repository root check
    try:
        res = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=workspace_root, capture_output=True, text=True, check=True)
        git_root = Path(res.stdout.strip()).resolve()
        if git_root != workspace_root:
            raise ProjectBindingError(f"Git root mismatch: '{git_root}' != '{workspace_root}'")
    except Exception as e:
        if isinstance(e, ProjectBindingError):
            raise
        raise ProjectBindingError(f"Git repository root discovery failed in {workspace_root}: {e}")
        
    return True

def compute_closed_world_scientific_tree_hash(workspace_root: Path) -> Tuple[str, Dict[str, str]]:
    """
    Computes deterministic closed-world SHA-256 tree hash over all canonical scientific files.
    """
    file_hashes = {}
    entries = []
    
    for rel_path in sorted(SCIENTIFIC_FINGERPRINT_MANIFEST):
        full_path = workspace_root / rel_path
        if not full_path.exists():
            raise ConstitutionalIntegrityError(f"Canonical scientific file missing: {rel_path}")
        content = full_path.read_bytes()
        f_hash = hashlib.sha256(content).hexdigest()
        file_hashes[rel_path] = f_hash
        entries.append(f"{rel_path}::{f_hash}")
        
    tree_payload = "\n".join(entries).encode("utf-8")
    tree_hash = hashlib.sha256(tree_payload).hexdigest()
    return tree_hash, file_hashes

def compute_canonical_dependency_hash(dependencies: List[Dict[str, str]]) -> str:
    """
    Hashes canonical tuples: (dependency_id, dependency_version, dependency_statement_hash)
    Sorted deterministically before hashing.
    """
    normalized = []
    for dep in dependencies:
        dep_id = dep.get("dependency_id", "").strip()
        dep_ver = dep.get("dependency_version", "").strip()
        dep_stmt_hash = dep.get("dependency_statement_hash", "").strip()
        if not dep_id or not dep_ver or not dep_stmt_hash:
            raise ValueError(f"Invalid dependency record: {dep}")
        normalized.append(f"{dep_id}::{dep_ver}::{dep_stmt_hash}")
    
    normalized.sort()
    canonical_payload = "\n".join(normalized).encode("utf-8")
    return hashlib.sha256(canonical_payload).hexdigest()

def compute_cited_source_hash(sources: List[Dict[str, str]]) -> str:
    """
    Hashes canonical tuples: (source_id, source_version, source_content_hash, source_access_level)
    Only for sources cited by the claim.
    """
    normalized = []
    for src in sources:
        s_id = src.get("source_id", "").strip()
        s_ver = src.get("source_version", "").strip()
        s_hash = src.get("source_content_hash", "").strip()
        s_acc = src.get("source_access_level", "").strip()
        if not s_id or not s_ver or not s_hash or not s_acc:
            raise ValueError(f"Invalid source record: {src}")
        normalized.append(f"{s_id}::{s_ver}::{s_hash}::{s_acc}")
        
    normalized.sort()
    canonical_payload = "\n".join(normalized).encode("utf-8")
    return hashlib.sha256(canonical_payload).hexdigest()

def evaluate_post_e4_change_class(
    audited_scientific_hash: str,
    accepted_scientific_hash: str,
    changed_files: List[str]
) -> Tuple[str, bool]:
    """
    Evaluates post-E4 change class:
    - NONE: Identical scientific hash, 0 changed files.
    - ADMINISTRATIVE_ONLY: Identical scientific hash, only administrative metadata modified. E4 valid.
    - PROVENANCE_CRITICAL: Identical scientific hash, verification/task graph/ledger files modified. E4 valid after provenance reconciliation.
    - SCIENTIFIC_MATERIAL: Scientific hash mismatch. E4 STALE.
    """
    if audited_scientific_hash != accepted_scientific_hash:
        return ("SCIENTIFIC_MATERIAL", False) # E4 is STALE
        
    if not changed_files:
        return ("NONE", True)
        
    provenance_prefixes = (
        "verification/",
        "evidence/",
        "checkpoints/",
        "TASK_GRAPH.md",
        "governance/CONTRACT_OWNERSHIP_LEDGER.yaml",
        "KNOWN_GOOD_CHECKPOINT.md",
        "CURRENT_SCIENTIFIC_STATE.md",
        "NEXT_ACTION.md"
    )
    
    for f in changed_files:
        # If any scientific file was changed, it is scientific material
        if f in SCIENTIFIC_FINGERPRINT_MANIFEST:
            return ("SCIENTIFIC_MATERIAL", False)
        if not any(f.startswith(p) or f == p for p in provenance_prefixes):
            return ("SCIENTIFIC_MATERIAL", False)
            
    return ("PROVENANCE_CRITICAL", True)

def verify_raw_e4_hash_integrity(derived_review_path: Path, raw_e4_path: Path) -> bool:
    """
    Verifies that the RAW_SHA256 recorded in the derived review matches the raw E4 receipt.
    """
    if not raw_e4_path.exists():
        raise ConstitutionalIntegrityError(f"Raw E4 file not found: {raw_e4_path}")
    if not derived_review_path.exists():
        raise ConstitutionalIntegrityError(f"Derived review file not found: {derived_review_path}")
        
    raw_bytes = raw_e4_path.read_bytes()
    expected_hash = hashlib.sha256(raw_bytes).hexdigest()
    
    review_text = derived_review_path.read_text(encoding="utf-8")
    if expected_hash not in review_text:
        raise ConstitutionalIntegrityError(f"RAW_SHA256 mismatch in {derived_review_path}: expected {expected_hash}")
        
    return True

RESONANCE_DIMENSIONS = [
    "THESIS",
    "MECHANISM",
    "ASSUMPTIONS",
    "SCALING",
    "BRIDGE_VARIABLE",
    "FAILURE_LOCALITY",
    "OBSERVABLE"
]
ALLOWED_SCORES = {"NONE", "LOW", "MODERATE", "HIGH", "EXACT", "UNKNOWN"}

def compute_pathway_resonance(
    dim_evaluations: Dict[str, Dict[str, Any]],
    new_result_removes_old_blocker: bool = False
) -> Dict[str, Any]:
    """
    Evaluates 7D categorical pathway resonance and deterministic reopening recommendations.
    """
    for dim in RESONANCE_DIMENSIONS:
        if dim not in dim_evaluations:
            raise ValueError(f"Missing resonance dimension: {dim}")
        eval_data = dim_evaluations[dim]
        score = eval_data.get("score")
        justification = eval_data.get("textual_justification", "").strip()
        pointers = eval_data.get("evidence_pointers", [])
        
        if score not in ALLOWED_SCORES:
            raise ValueError(f"Invalid score '{score}' for dimension {dim}")
        if len(justification) < 5:
            raise ValueError(f"Textual justification required for dimension {dim}")
        if not pointers:
            raise ValueError(f"Evidence pointers required for dimension {dim}")
            
    failure_score = dim_evaluations["FAILURE_LOCALITY"]["score"]
    mechanism_score = dim_evaluations["MECHANISM"]["score"]
    
    reopen_recommended = (
        failure_score in {"HIGH", "EXACT"} and
        mechanism_score in {"MODERATE", "HIGH", "EXACT"} and
        new_result_removes_old_blocker is True
    )
    
    return {
        "dimensions": dim_evaluations,
        "reopen_recommended": reopen_recommended,
        "reopen_rationale": (
            "Failure locality matches historical barrier and new result removes blocker"
            if reopen_recommended else "No reopening criteria met"
        )
    }

OBSTRUCTION_TYPES = {
    "METHOD_OBSTRUCTION",
    "MODEL_REGIME_OBSTRUCTION",
    "TRANSFER_OBSTRUCTION",
    "TARGET_THEOREM_OBSTRUCTION",
    "UNKNOWN"
}

OBSTRUCTION_STATES = {
    "CANDIDATE",
    "FALSIFIED",
    "METHOD_LIMITATION",
    "SURVIVED_FALSIFICATION",
    "THEOREM_CANDIDATE",
    "PROVED_OBSTRUCTION_THEOREM"
}

def evaluate_obstruction_transition(
    current_state: str,
    event: str,
    obstruction_type: str
) -> str:
    """
    Evaluates common obstruction state transition fail-closed.
    """
    if obstruction_type not in OBSTRUCTION_TYPES:
        raise ConstitutionalIntegrityError(f"Invalid obstruction type: {obstruction_type}")
    if current_state not in OBSTRUCTION_STATES:
        raise ConstitutionalIntegrityError(f"Invalid current obstruction state: {current_state}")
        
    if current_state == "CANDIDATE":
        if event == "COUNTEREXAMPLE_DISCOVERED":
            return "FALSIFIED"
        elif event == "BOUNDED_TO_METHOD_ONLY":
            return "METHOD_LIMITATION"
        elif event == "FALSIFICATION_ATTACK_SURVIVED":
            return "SURVIVED_FALSIFICATION"
        elif event == "INDEPENDENT_E4_VERIFIED":
            raise ConstitutionalIntegrityError("Illegal jump: CANDIDATE cannot transition directly to PROVED_OBSTRUCTION_THEOREM!")
    elif current_state == "SURVIVED_FALSIFICATION":
        if event == "FORMAL_OBSTRUCTION_LEMMA_CONSTRUCTED":
            return "THEOREM_CANDIDATE"
    elif current_state == "THEOREM_CANDIDATE":
        if event == "INDEPENDENT_E4_VERIFIED":
            return "PROVED_OBSTRUCTION_THEOREM"
            
    return current_state

def validate_memory_partition(partition_name: str, item_type: str) -> bool:
    """
    Enforces contamination barriers between memory partitions.
    """
    if partition_name == "semantic_accepted":
        if item_type in {"QUARANTINED_CLAIM", "CONTESTED_PROOF", "UNRESOLVED_CONJECTURE"}:
            raise ConstitutionalIntegrityError("Quarantined claims cannot be placed in semantic_accepted memory!")
    return True

AMENDMENT_REQUIRED_FIELDS = [
    "CHANGE_PROPOSAL",
    "RATIONALE",
    "IMPACT_ANALYSIS",
    "REGRESSION_TESTS",
    "NEW_VERSION",
    "INDEPENDENT_REVIEW",
    "HUMAN_OWNER_ACCEPTANCE",
    "SEALED_MIGRATION_RECEIPT"
]

def validate_constitutional_amendment(amendment_packet: Dict[str, Any]) -> bool:
    """
    Verifies that a proposed constitutional change adheres to the amendment protocol.
    """
    for field in AMENDMENT_REQUIRED_FIELDS:
        if field not in amendment_packet or not amendment_packet[field]:
            raise ConstitutionalIntegrityError(f"Amendment packet missing required field: {field}")
    return True
