import hashlib
import json
import subprocess
import yaml
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

class ProjectBindingError(Exception):
    pass

class ConstitutionalIntegrityError(Exception):
    pass

EXPECTED_PROJECT_IDS = {"YM-MASS-GAP", "YANG_MILLS_MASS_GAP"}
EXPECTED_REPO_DIR_NAME = "yang mills and the mass gap"

ARTIFACT_CLASSES = {
    "SCIENTIFIC",
    "PROVENANCE_CRITICAL",
    "ADMINISTRATIVE",
    "GENERATED",
    "IGNORED_WITH_JUSTIFICATION",
    "UNKNOWN",
}

SCIENTIFIC_ARTIFACT_CLASSIFICATION_PATH = "governance/SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml"

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
    "literature/CROSS_ERA_SYNTHESIS_MATRIX.md",
    "literature/COMMON_OBSTRUCTION_CANDIDATES.md",
    "literature/OBSTRUCTION_RESONANCE_MATRIX.md",
    "literature/UV_IR_BRIDGE_GAP.md",
    "literature/LOAD_BEARING_ESTIMATE_CANDIDATES.md",
    "literature/ASSUMPTION_TRANSFER_MATRIX.md",
    "literature/BRIDGE_EDGE_REGISTER.md",
    "literature/CRITICAL_CUT_SET_REPORT.md",
    "literature/LIMIT_AND_REGIME_MATRIX.md",
    "literature/MINIMAL_SUFFICIENT_ESTIMATE_REGISTER.md",
    "literature/MISSING_BRIDGE_GRAPH.md",
    "literature/OPEN_EDGE_REGISTER.md",
    "literature/SOURCE_TO_EDGE_TRACEABILITY_MATRIX.md",
    "literature/YM-003_NEGATIVE_TRANSFER_TESTS.md",
    "literature/YM-XNS-001-NAVIER-STOKES-STATUS-AUDIT.md",
    "literature/YM-XNS-001-PROOF-ARCHITECTURE.md",
    "literature/YM-XNS-001-MECHANISM-LEDGER.md",
    "literature/YM-XNS-001-YM-TRANSFER-MATRIX.md",
    "literature/YM-XNS-001-NEIGHBORING-PROBLEM-RANKING.md",
    "literature/YM-XNS-001-RESIDUAL-CANCELLATION-AUDIT.md",
    "literature/YM-XNS-001-CLASSICAL-YM-COMPARISON.md",
    "literature/YM-XNS-001-FORMAL-VERIFICATION-ROADMAP.md",
    "literature/YM-XNS-001-MULTI-AGENT-RESEARCH-TOPOLOGY.md",
    "literature/YM-XNS-001-FINAL-SYNTHESIS.md",
    "literature/YM-004-PRIMARY-SOURCE-MAP.md",
    "literature/YM-004-RG-ARCHITECTURE.md",
    "literature/YM-004-SCALE-BY-SCALE-LEDGER.md",
    "literature/YM-004-SMALL-LARGE-FIELD-AUDIT.md",
    "literature/YM-004-FINITE-VOLUME-BOUNDARY-AUDIT.md",
    "literature/YM-004-STOPPING-POINT-ANALYSIS.md",
    "literature/YM-004-UV-BOUNDARY-RECORD.md",
    "literature/YM-004-OBSTRUCTION-CANDIDATE-AUDIT.md",
    "literature/YM-004-VISUAL-INTUITION-DATA.md",
    "literature/YM-004-FINAL-SYNTHESIS.md",
    SCIENTIFIC_ARTIFACT_CLASSIFICATION_PATH,
]

# These files are controlled research/provenance records but are deliberately
# not part of the scientific-content tree. Their paths are explicit so a new
# ledger, lemma register, or source artifact cannot silently join this class.
KNOWN_PROVENANCE_CRITICAL_PATHS = {
    "CLAIM_QUARANTINE_REGISTER.md",
    "CURRENT_SCIENTIFIC_STATE.md",
    "EVIDENCE_LEDGER.md",
    "HYPOTHESIS_REGISTER.md",
    "INTEGRITY_VIOLATION_REGISTER.md",
    "KNOWN_GOOD_CHECKPOINT.md",
    "NEXT_ACTION.md",
    "OPEN_LEMMA_REGISTER.md",
    "OFFICIAL_PROBLEM_STATUS_INVARIANT.md",
    "REJECTION_LEDGER.md",
    "RESEARCH_LEDGER.md",
    "SCIENTIFIC_INTERROGATION_LEDGER.md",
    "SOURCE_OF_TRUTH.md",
    "TASK_GRAPH.md",
    "VERIFICATION_LEDGER.md",
    "literature/CLAIM_QUARANTINE_REGISTER.md",
    "literature/CONSTRUCTIVE_DEPENDENCY_GRAPH.md",
    "literature/FOUNDATIONAL_DEPENDENCY_GRAPH.md",
    "literature/MODERN_DEPENDENCY_GRAPH.md",
}

KNOWN_ADMINISTRATIVE_ROOT_PATHS = {
    ".gitignore",
    "INIT_GIT_WINDOWS.ps1",
    "PROJECT_PROFILE.md",
    "README.md",
    "RUN_VERIFY.ps1",
    "SETUP_WINDOWS.ps1",
    "TEST_STRATEGY.md",
    "pyproject.toml",
    "requirements.txt",
    # Universal Governance v3 project-control artifacts are administrative
    # and must not silently enter the scientific fingerprint.
    "ARCHITECTURE_DECISIONS.md",
    "GOVERNANCE_STATE.yaml",
    "PROJECT_INTENT.md",
    "ROADMAP.md",
}

GENERATED_PREFIXES = ("checkpoints/", "evidence/", "experiments/", "numerical/")
PROVENANCE_PREFIXES = ("verification/",)
ADMINISTRATIVE_PREFIXES = ("governance/", "scripts/", "src/", "tests/", "docs/")

IGNORED_EXACT_PATHS = {
    "checkpoints/.gitkeep",
    "derivations/.gitkeep",
    "evidence/test_runs/.gitkeep",
    "experiments/records/.gitkeep",
    "literature/primary/.gitkeep",
    "literature/reviews/.gitkeep",
    "numerical/.gitkeep",
    "proofs/.gitkeep",
    "verification/.gitkeep",
}


def _normalize_relative_path(path: Path) -> str:
    value = path.as_posix()
    return value[2:] if value.startswith("./") else value


def _workspace_relative_path(workspace_root: Path, path: Path) -> str:
    return _normalize_relative_path(path.resolve().relative_to(workspace_root.resolve()))


def _load_classification_policy(workspace_root: Path) -> Dict[str, Any]:
    policy_path = workspace_root / SCIENTIFIC_ARTIFACT_CLASSIFICATION_PATH
    if not policy_path.exists():
        raise ConstitutionalIntegrityError(
            f"Scientific artifact classification policy missing: {SCIENTIFIC_ARTIFACT_CLASSIFICATION_PATH}"
        )
    try:
        policy = yaml.safe_load(policy_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise ConstitutionalIntegrityError("Scientific artifact classification policy is unreadable") from exc
    if not isinstance(policy, dict) or set(policy.get("classes", [])) != ARTIFACT_CLASSES:
        raise ConstitutionalIntegrityError("Scientific artifact classification policy has an invalid class set")
    declared = policy.get("scientific_fingerprint", {}).get("paths")
    if sorted(declared or []) != sorted(SCIENTIFIC_FINGERPRINT_MANIFEST):
        raise ConstitutionalIntegrityError(
            "Scientific artifact classification policy does not match the canonical fingerprint manifest"
        )
    return policy


@lru_cache(maxsize=8)
def _manifest_referenced_paths(workspace_root: Path) -> set[str]:
    """Return source artifacts explicitly registered by primary manifests."""
    referenced: set[str] = set()
    primary_root = workspace_root / "literature" / "primary"
    manifest_paths = list(primary_root.glob("*/manifest.yaml"))
    manifest_paths.extend(primary_root.glob("*/SOURCE_MANIFEST.yaml"))
    for manifest_path in manifest_paths:
        try:
            data = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
        except (OSError, yaml.YAMLError) as exc:
            raise ConstitutionalIntegrityError(f"Unreadable primary manifest: {manifest_path}") from exc
        for source in data.get("sources", []):
            if not isinstance(source, dict):
                continue
            local_file = source.get("local_file")
            if local_file:
                referenced.add(_workspace_relative_path(workspace_root, manifest_path.parent / local_file))
            file_name = source.get("file_name")
            if file_name:
                referenced.add(_workspace_relative_path(workspace_root, manifest_path.parent / file_name))
    return referenced | {"literature/primary/clay/jaffe_witten_extracted.txt"}


def classify_repository_artifact(workspace_root: Path, relative_path: str) -> str:
    """Classify one repository artifact under the R3 closed-world policy."""
    rel = _normalize_relative_path(Path(relative_path))
    if rel in SCIENTIFIC_FINGERPRINT_MANIFEST:
        return "SCIENTIFIC"
    if rel in IGNORED_EXACT_PATHS:
        return "IGNORED_WITH_JUSTIFICATION"
    if rel in KNOWN_PROVENANCE_CRITICAL_PATHS or rel in _manifest_referenced_paths(workspace_root):
        return "PROVENANCE_CRITICAL"
    if rel.startswith("literature/primary/") and (
        rel.endswith("/manifest.yaml") or rel.endswith("/SOURCE_MANIFEST.yaml")
    ):
        return "PROVENANCE_CRITICAL"
    if rel == "yang_mills_mass_gap_local_scaffold.zip":
        return "GENERATED"
    if any(rel.startswith(prefix) for prefix in GENERATED_PREFIXES):
        return "GENERATED"
    if any(rel.startswith(prefix) for prefix in PROVENANCE_PREFIXES):
        return "PROVENANCE_CRITICAL"
    if rel in KNOWN_ADMINISTRATIVE_ROOT_PATHS or any(
        rel.startswith(prefix) for prefix in ADMINISTRATIVE_PREFIXES
    ):
        return "ADMINISTRATIVE"

    # Research-shaped locations and names are never implicitly administrative.
    # This is the fail-closed boundary for new proofs, lemmas, theorem support,
    # and unregistered primary-source material.
    name = Path(rel).name.upper()
    research_markers = (
        "LEDGER", "THEOREM", "LEMMA", "HYPOTHESIS", "EVIDENCE", "SPECIFICATION",
        "MATRIX", "GRAPH", "PROOF", "SOURCE", "RESEARCH", "PATHWAY",
    )
    research_suffixes = {".MD", ".YAML", ".YML", ".TXT", ".TEX", ".PDF", ".IPYNB"}
    if rel.startswith(("literature/", "proofs/", "derivations/")) or (
        Path(rel).suffix.upper() in research_suffixes and any(marker in name for marker in research_markers)
    ):
        return "UNKNOWN"
    return "UNKNOWN"


def discover_repository_artifacts(workspace_root: Path) -> Dict[str, str]:
    """Discover and classify all files, including untracked research files."""
    _load_classification_policy(workspace_root)
    # Git gives the stable baseline cheaply. The additional bounded scans cover
    # untracked research files in the only locations where they can extend the
    # scientific packet without walking .venv/node_modules/build outputs.
    paths: set[Path] = set()
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=workspace_root,
            capture_output=True,
            check=True,
        )
        paths.update(workspace_root / item.decode("utf-8") for item in result.stdout.split(b"\0") if item)
    except (OSError, subprocess.CalledProcessError):
        paths.update(path for path in workspace_root.iterdir() if path.is_file())

    for search_root in (workspace_root / "literature", workspace_root / "proofs", workspace_root / "derivations"):
        if search_root.exists():
            paths.update(path for path in search_root.rglob("*") if path.is_file())
    paths.update(path for path in workspace_root.iterdir() if path.is_file())
    policy_path = workspace_root / SCIENTIFIC_ARTIFACT_CLASSIFICATION_PATH
    if policy_path.exists():
        paths.add(policy_path)

    classifications: Dict[str, str] = {}
    for path in paths:
        rel = _normalize_relative_path(path.relative_to(workspace_root))
        classifications[rel] = classify_repository_artifact(workspace_root, rel)
    return classifications


def validate_scientific_artifact_classification(workspace_root: Path) -> Dict[str, str]:
    """Reject unknown or out-of-manifest research artifacts before fingerprinting."""
    classifications = discover_repository_artifacts(workspace_root)
    unknown = sorted(path for path, cls in classifications.items() if cls == "UNKNOWN")
    if unknown:
        raise ConstitutionalIntegrityError(
            "Unknown research artifact(s) discovered; classify and bind before acceptance: " + ", ".join(unknown)
        )
    out_of_manifest = sorted(
        path for path, cls in classifications.items()
        if cls == "SCIENTIFIC" and path not in SCIENTIFIC_FINGERPRINT_MANIFEST
    )
    if out_of_manifest:
        raise ConstitutionalIntegrityError(
            "Scientific artifact(s) are outside the canonical fingerprint manifest: " + ", ".join(out_of_manifest)
        )
    return classifications

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
    Discovers the repository under the R3 classification policy, then computes
    a deterministic SHA-256 tree hash over every classified scientific file.
    """
    classifications = validate_scientific_artifact_classification(workspace_root)
    file_hashes = {}
    entries = []
    
    discovered_scientific = sorted(path for path, cls in classifications.items() if cls == "SCIENTIFIC")
    if discovered_scientific != sorted(SCIENTIFIC_FINGERPRINT_MANIFEST):
        raise ConstitutionalIntegrityError(
            "Discovered scientific artifact set does not equal the canonical fingerprint manifest"
        )

    for rel_path in discovered_scientific:
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
    administrative_prefixes = ("governance/", "scripts/", "src/", "tests/")
    provenance_seen = False
    
    for f in changed_files:
        # If any scientific file was changed, it is scientific material
        if f in SCIENTIFIC_FINGERPRINT_MANIFEST:
            return ("SCIENTIFIC_MATERIAL", False)
        if f in KNOWN_PROVENANCE_CRITICAL_PATHS:
            provenance_seen = True
            continue
        if any(f.startswith(p) or f == p for p in provenance_prefixes):
            provenance_seen = True
            continue
        if any(f.startswith(p) or f == p for p in administrative_prefixes):
            continue
        return ("SCIENTIFIC_MATERIAL", False)
            
    return ("PROVENANCE_CRITICAL" if provenance_seen else "ADMINISTRATIVE_ONLY", True)

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
