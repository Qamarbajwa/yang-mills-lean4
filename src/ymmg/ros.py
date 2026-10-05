import hashlib
import json
import subprocess
import yaml
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Union

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
    "literature/YM-005-PRIMARY-SOURCE-MAP.md",
    "literature/YM-005-LATTICE-FORMALISM-AUDIT.md",
    "literature/YM-005-CLUSTER-EXPANSION-LEDGER.md",
    "literature/YM-005-SPECTRAL-GAP-AND-DECAY-AUDIT.md",
    "literature/YM-005-AREA-LAW-VS-MASS-GAP-AUDIT.md",
    "literature/YM-005-11-DIMENSIONAL-THEOREM-LEDGER.md",
    "literature/YM-005-IR-BOUNDARY-RECORD.md",
    "literature/YM-005-OBSTRUCTION-CANDIDATE-AUDIT.md",
    "literature/YM-005-VISUAL-INTUITION-DATA.md",
    "literature/YM-005-FINAL-SYNTHESIS.md",
    "literature/YM-LEAN-001-FORMALIZATION-AUDIT.md",
    "literature/YM-006-UV-IR-COMPARISON-FRAMEWORK.md",
    "literature/YM-006-CROSSOVER-DISTANCE-ESTIMATE.md",
    "literature/YM-006-CRITICAL-CUT-SET-RECONCILIATION.md",
    "literature/YM-006-MATHEMATICAL-IMPASSE-DIAGNOSIS.md",
    "literature/YM-006-CANONICAL-NON-MEETING-RECORD.md",
    "literature/YM-006-VISUAL-INTUITION-DATA.md",
    "literature/YM-006-FINAL-SYNTHESIS.md",
    "literature/YM-007-EVALUATION-FRAMEWORK.md",
    "literature/YM-007-GEOMETRIC-FLOW-EVALUATION.md",
    "literature/YM-007-STOCHASTIC-QUANTIZATION-EVALUATION.md",
    "literature/YM-007-LOOP-EQUATIONS-EVALUATION.md",
    "literature/YM-007-TOPOLOGICAL-CONDENSATION-EVALUATION.md",
    "literature/YM-007-EXACT-RG-EVALUATION.md",
    "literature/YM-007-COMPARATIVE-MECHANISM-MATRIX.md",
    "literature/YM-007-CANONICAL-MECHANISM-RECORD.md",
    "literature/YM-007-FINAL-SYNTHESIS.md",
    "literature/YM-008-HYBRID-ARCHITECTURE-SPECIFICATION.md",
    "literature/YM-008-SCALE-INTERFACE-ANALYSIS.md",
    "literature/YM-008-ADVERSARIAL-FALSIFICATION-PROTOCOL.md",
    "literature/YM-008-LEAN-FORMALIZATION-BLUEPRINT.md",
    "literature/YM-008-CANONICAL-STRATEGY-RECORD.md",
    "literature/YM-008-FINAL-SYNTHESIS.md",
    "literature/YM-009-QUANTITATIVE-BOOTSTRAP-EXECUTION.md",
    "literature/YM-009-SCALE-GLUING-ANALYSIS.md",
    "literature/YM-009-SPECTRUM-AND-STRING-TENSION-BOUNDS.md",
    "literature/YM-009-CONTINUUM-LIMIT-ROBUSTNESS.md",
    "literature/YM-009-CANONICAL-QUANTITATIVE-RECORD.md",
    "literature/YM-009-FINAL-SYNTHESIS.md",
    "literature/YM-010-PROGRAM-MONOGRAPH-AND-SYNTHESIS.md",
    "literature/YM-010-GLOBAL-THEOREM-AND-BRIDGE-CLOSURE.md",
    "literature/YM-010-FORMAL-VERIFICATION-ROADMAP.md",
    "literature/YM-010-CANONICAL-PROGRAM-RECORD.md",
    "literature/YM-011-FIRST-LOAD-BEARING-LEMMA-SPECIFICATION.md",
    "literature/YM-011-OBS-MAP-CONSTRUCTION.md",
    "literature/YM-011-PLAQUETTE-EXP-ANALYSIS.md",
    "literature/YM-011-TREE-GAUGE-ANALYSIS.md",
    "literature/YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB-ANALYSIS.md",
    "literature/YM-011-DYADIC-FREE-ENERGY-UNIFORMITY-ANALYSIS.md",
    "literature/YM-011-UV-SCALE-TRANSFER-LEMMA.md",
    "literature/YM-012-RECONCILED-19-EDGE-GRAPH.md",
    "literature/YM-012-REPAIRED-HYBRID-STRATEGY.md",
    "literature/YM-012-VISUAL-INTUITION-COMPANION.md",
    "literature/YM-012-CROSSOVER-ANALYSIS.md",
    "literature/YM-012-CROSSOVER-DEPENDENCY-DAG.md",
    "literature/YM-013-LOOP-BOOTSTRAP-TARGET.md",
    "literature/YM-013-FINITE-N-LOOP-HIERARCHY.md",
    "literature/YM-013-CERTIFIED-SDP-ANALYSIS.md",
    "literature/YM-014-RANDOM-SURFACE-DUALITY-TARGET.md",
    "literature/YM-014-REPRESENTATION-LANDSCAPE.md",
    "literature/YM-014-SURFACE-ENTROPY-ENERGY.md",
    "literature/YM-014-CONTINUUM-SCALING.md",
    "literature/YM-014R-EXTERNAL-EVIDENCE-RECONCILIATION.md",
    "literature/CLAIM-AUDIT-FAIZAL-SHABIR-2026.md",
    "literature/YM-014R-SOURCE-EVIDENCE-MATRIX.md",
    "literature/YM-014R-CORRECTED-DAG.md",
    "literature/YM-015-UV-CONTINUUM-TARGET.md",
    "literature/YM-015-BALABAN-UV-LEDGER.md",
    "literature/YM-015-OBSERVABLE-RENORMALIZATION.md",
    "literature/YM-015-DISTRIBUTIONAL-COMPACTNESS.md",
    "literature/YM-015-REFLECTION-POSITIVITY.md",
    "literature/YM-015-O4-TARGET.md",
    "literature/YM-015-O4-RESTORATION.md",
    "literature/CLAIM-AUDIT-KIRK-2026.md",
    "literature/YM-015-NONTRIVIALITY-WITNESS.md",
    "literature/YM-015-SOURCE-EVIDENCE-MATRIX.md",
    "literature/YM-015R-CONTINUUM-RECONCILIATION.md",
    "literature/YM-015R-LOCALITY-REPLACEMENT-ANALYSIS.md",
    "literature/YM-015R-EVIDENCE-MATRIX.md",
    "literature/YM-015R-CORRECTED-DAG.md",
    "literature/YM-015R2-RP-STATUS-AMENDMENT.md",
    "literature/YM-015R2-FLOWED-CONTINUUM-TARGET.md",
    "literature/YM-015R2-SPATIAL-FLOW-ANALYSIS.md",
    "literature/YM-015R2-OBSERVABLE-ROUTE-MATRIX.md",
    "literature/YM-015R2-EVIDENCE-MATRIX.md",
    "literature/YM-015R2-CORRECTED-DAG.md",
    "governance/YM_AUTONOMOUS_DISCOVERY_ARCHITECTURE.md",
    "research/YM_3D4D_FAILURE_ATLAS.md",
    "research/YM_DISCOVERY_TRANSFER_ENGINE.md",
    "research/YM_REPRESENTATION_SEARCH_REGISTRY.md",
    "research/YM_CONSTRUCTION_DEFECT_CORRECTION_LEDGER.md",
    "research/YM_CROSS_DOMAIN_TRANSFER_REGISTRY.md",
    "research/YM_015F_INSERTION_SOURCE_AUDIT.md",
    "research/YM_015F_SOURCE_JET_REDUCTION.md",
    "research/YM_SCIENTIFIC_RECONCILIATION_034.md",
    "research/YM_015F_EXACT_SOURCE_TRANSPORT_035.md",
    "research/YM_015F_PLAQUETTE_SOURCE_COMPATIBILITY_035.md",
    "research/YM_3D4D_PROOF_LOCAL_AUDIT_035.md",
    "research/YM_015F_MARKED_RECURRENCE_036.md",
    "research/YM_015F_QUADRATIC_SOURCE_AUDIT_036.md",
    "research/YM_015F_BALABAN_MAP_EXTRACTION_036.md",
    "research/YM_015F_TERMINAL_SECTOR_NORMALIZATION_037.md",
    "research/YM_3D4D_NUMBERED_LEMMA_AUDIT_037.md",
    "research/YM_3D4D_BPHZ_HYPOTHESIS_AUDIT_038.md",
    "research/YM_015F_CONSTRAINED_COORDINATES_AUDIT_038.md",
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
ADMINISTRATIVE_PREFIXES = ("governance/", "scripts/", "src/", "tests/", "docs/", "formal/", "_staging_gov_v403/", "_staging_gov_v406r3/")

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

    for search_root in (workspace_root / "literature", workspace_root / "proofs", workspace_root / "derivations", workspace_root / "research"):
        if search_root.exists():
            paths.update(path for path in search_root.rglob("*") if path.is_file())
    paths.update(path for path in workspace_root.iterdir() if path.is_file())
    # Explicit canonical files must be discovered before they enter Git as well.
    paths.update(workspace_root / rel for rel in SCIENTIFIC_FINGERPRINT_MANIFEST)
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


# ==============================================================================
# YM-GOV-014: Failure-Driven Scientific Governance & Authority Separation
# ==============================================================================

ROUTINE_SCIENTIFIC_TASK_STATES = {
    "PROPOSED",
    "CANDIDATE",
    "INDEPENDENT_SCIENTIFIC_REVIEW",
    "SCIENTIFICALLY_ACCEPTED",
    "REPAIR_REQUIRED",
    "BOUNDED_REPAIR",
    "REVERIFICATION",
    "REVIEW_HOLD",
    "SCIENTIFIC_REVIEW_HOLD",
}

RESERVED_HUMAN_OWNER_ACTIONS = {
    "CHANGE_PROJECT_MISSION_OR_TARGET",
    "CLAIM_GOAL_COMPLETE_OR_CLAY_SOLUTION",
    "EXTERNAL_PUBLICATION_OR_RELEASE",
    "DESTRUCTIVE_DELETION_OF_HISTORY",
    "MODIFY_EXTERNAL_REPOSITORY",
    "UNBOUNDED_EXTERNAL_RESOURCE_EXPENDITURE",
}

DISQUALIFYING_AUDIT_FINDINGS = {
    "MATHEMATICAL_CONFLATION",
    "SCOPE_PROMOTION",
    "UNIT_FABRICATION",
    "CIRCULARITY",
    "UNPROVEN_TRANSFER",
}


def validate_task_disposition_authority(
    task_id: str,
    proposed_state: str,
    has_scientific_defects: bool = False,
    reserved_owner_action: Optional[str] = None,
) -> str:
    """
    Enforces YM-GOV-014 authority separation:
    - Never use AWAITING_HUMAN_OWNER_ACCEPTANCE for a task that has identified
      mathematical or epistemic defects or routine scientific verification.
    - HUMAN_OWNER_DECISION_REQUIRED is permitted ONLY for reserved owner actions.
    """
    if proposed_state == "AWAITING_HUMAN_OWNER_ACCEPTANCE":
        if has_scientific_defects:
            raise ConstitutionalIntegrityError(
                f"Task {task_id} has scientific defects and cannot enter AWAITING_HUMAN_OWNER_ACCEPTANCE; "
                "must transition to REPAIR_REQUIRED or REVIEW_HOLD."
            )
        raise ConstitutionalIntegrityError(
            f"Deprecated state AWAITING_HUMAN_OWNER_ACCEPTANCE forbidden for routine scientific task {task_id}; "
            "use failure-driven scientific review or HUMAN_OWNER_DECISION_REQUIRED for reserved actions."
        )

    if proposed_state == "HUMAN_OWNER_DECISION_REQUIRED":
        if reserved_owner_action not in RESERVED_HUMAN_OWNER_ACTIONS:
            raise ConstitutionalIntegrityError(
                f"HUMAN_OWNER_DECISION_REQUIRED for {task_id} requires a valid reserved_owner_action "
                f"in {sorted(RESERVED_HUMAN_OWNER_ACTIONS)}, got: {reserved_owner_action!r}"
            )
        return "HUMAN_OWNER_DECISION_REQUIRED"

    if has_scientific_defects and proposed_state == "SCIENTIFICALLY_ACCEPTED":
        raise ConstitutionalIntegrityError(
            f"Task {task_id} with unresolved scientific defects cannot enter SCIENTIFICALLY_ACCEPTED."
        )

    if proposed_state not in ROUTINE_SCIENTIFIC_TASK_STATES:
        raise ConstitutionalIntegrityError(f"Unknown scientific task state: {proposed_state}")

    return proposed_state


def evaluate_scientific_review_transition(
    current_state: str,
    event: str,
    audit_findings: Optional[List[str]] = None,
) -> str:
    """
    Implements the YM-GOV-014 routine scientific state machine:
    CANDIDATE -> INDEPENDENT_SCIENTIFIC_REVIEW -> {SCIENTIFICALLY_ACCEPTED, REPAIR_REQUIRED, REVIEW_HOLD}
    REPAIR_REQUIRED -> BOUNDED_REPAIR -> REVERIFICATION -> INDEPENDENT_SCIENTIFIC_REVIEW
    """
    findings = set(audit_findings or [])
    if current_state not in ROUTINE_SCIENTIFIC_TASK_STATES:
        raise ConstitutionalIntegrityError(f"Invalid current scientific state: {current_state}")

    if current_state == "CANDIDATE":
        if event == "SUBMIT_FOR_REVIEW":
            return "INDEPENDENT_SCIENTIFIC_REVIEW"
        raise ConstitutionalIntegrityError(f"Illegal transition from CANDIDATE on event {event}")

    if current_state == "INDEPENDENT_SCIENTIFIC_REVIEW":
        if findings & DISQUALIFYING_AUDIT_FINDINGS:
            return "REPAIR_REQUIRED"
        if event in {"INTEGRITY_FAIL", "DEFECT_IDENTIFIED", "REPAIR_REQUIRED"}:
            return "REPAIR_REQUIRED"
        if event == "HOLD_UPSTREAM_DEPENDENCY":
            return "REVIEW_HOLD"
        if event in {"INTEGRITY_PASS", "INTEGRITY_PASS_WITH_LIMITATIONS"}:
            return "SCIENTIFICALLY_ACCEPTED"
        raise ConstitutionalIntegrityError(
            f"Illegal transition from INDEPENDENT_SCIENTIFIC_REVIEW on event {event}"
        )

    if current_state == "REPAIR_REQUIRED":
        if event in {"START_BOUNDED_REPAIR", "AUTO_REPAIR"}:
            return "BOUNDED_REPAIR"
        if event == "ROUTE_TO_OWNER_ACCEPTANCE":
            raise ConstitutionalIntegrityError(
                "REPAIR_REQUIRED must transition to BOUNDED_REPAIR, never to owner acceptance!"
            )
        raise ConstitutionalIntegrityError(f"Illegal transition from REPAIR_REQUIRED on event {event}")

    if current_state == "BOUNDED_REPAIR":
        if event == "COMPLETE_REPAIR":
            return "REVERIFICATION"
        raise ConstitutionalIntegrityError(f"Illegal transition from BOUNDED_REPAIR on event {event}")

    if current_state == "REVERIFICATION":
        if event == "SUBMIT_FOR_REVIEW":
            return "INDEPENDENT_SCIENTIFIC_REVIEW"
        if event == "VERIFICATION_FAILED":
            return "BOUNDED_REPAIR"
        raise ConstitutionalIntegrityError(f"Illegal transition from REVERIFICATION on event {event}")

    return current_state


def verify_candidate_bound_acceptance(
    candidate_sha: str,
    reviewed_sha: str,
    review_verdict: str,
    audit_findings: Optional[List[str]] = None,
    limitations_reflected_in_status: bool = True,
    post_review_changed_files: Optional[List[str]] = None,
    audited_scientific_hash: Optional[str] = None,
    accepted_scientific_hash: Optional[str] = None,
) -> bool:
    """
    Enforces Section 3 (Candidate-Bound Review):
    An independent scientific review is valid for acceptance ONLY if:
    1. review_verdict is INTEGRITY_PASS, or INTEGRITY_PASS_WITH_LIMITATIONS with limitations reflected;
    2. candidate_sha == reviewed_sha, or only explicitly declared non-scientific metadata changed after review;
    3. no audit finding of mathematical conflation, scope promotion, unit fabrication, circularity, or unproven transfer.
    """
    findings = set(audit_findings or [])
    disqualifiers = findings & DISQUALIFYING_AUDIT_FINDINGS
    if disqualifiers:
        raise ConstitutionalIntegrityError(
            f"Audit findings force REPAIR_REQUIRED and forbid acceptance: {sorted(disqualifiers)}"
        )

    if review_verdict not in {"INTEGRITY_PASS", "INTEGRITY_PASS_WITH_LIMITATIONS"}:
        raise ConstitutionalIntegrityError(
            f"Review verdict '{review_verdict}' does not permit SCIENTIFICALLY_ACCEPTED."
        )

    if review_verdict == "INTEGRITY_PASS_WITH_LIMITATIONS" and not limitations_reflected_in_status:
        raise ConstitutionalIntegrityError(
            "INTEGRITY_PASS_WITH_LIMITATIONS requires all limitations to be reflected in claim status."
        )

    if candidate_sha != reviewed_sha:
        if (
            post_review_changed_files is not None
            and audited_scientific_hash is not None
            and accepted_scientific_hash is not None
        ):
            change_class, is_valid = evaluate_post_e4_change_class(
                audited_scientific_hash=audited_scientific_hash,
                accepted_scientific_hash=accepted_scientific_hash,
                changed_files=post_review_changed_files,
            )
            if not is_valid or change_class == "SCIENTIFIC_MATERIAL":
                raise ConstitutionalIntegrityError(
                    f"Candidate SHA mismatch ({candidate_sha} != {reviewed_sha}) with scientific material modification ({change_class})."
                )
        else:
            raise ConstitutionalIntegrityError(
                f"Candidate SHA mismatch: accepted candidate_sha ({candidate_sha}) != reviewed_sha ({reviewed_sha})."
            )

    return True


def enforce_goal_complete_bridge_gate(edge_statuses: Dict[str, str], requested_goal_complete: bool) -> bool:
    """
    Verifies that GOAL_COMPLETE is False whenever any required bridge edge is not PROVED.
    """
    non_proved = {edge_id: status for edge_id, status in edge_statuses.items() if status != "PROVED"}
    if requested_goal_complete and non_proved:
        raise ConstitutionalIntegrityError(
            f"GOAL_COMPLETE cannot be True while bridge edges remain non-PROVED: {non_proved}"
        )
    return False if non_proved else requested_goal_complete


def check_ym011_activation_eligibility(
    ym011_status: str,
    precursor_ym011_pre_verified: bool,
) -> bool:
    """
    Verifies that YM-011 cannot enter active proof execution while its precursor
    lemma (YM-011-PRE) is unverified or while YM-011 is PROPOSED.
    """
    if not precursor_ym011_pre_verified:
        raise ConstitutionalIntegrityError(
            "YM-011 cannot be activated for proof execution while precursor YM-011-PRE is unverified."
        )
    if "PROPOSED" in ym011_status or "NOT_AUTHORIZED" in ym011_status or "NOT AUTHORIZED" in ym011_status:
        raise ConstitutionalIntegrityError(
            f"YM-011 is in status '{ym011_status}' and cannot enter active proof execution."
        )
    return True


# ==============================================================================
# YM-GOV-ADOPT-0406R3: Universal Governance v4.0.6-r3 Project-Bound Strengthening
# ==============================================================================

YANG_MILLS_REQUIRED_HARD_GATES = {
    "candidate_frozen",
    "candidate_bound_review",
    "scientific_review_pass",
    "negative_evidence_preserved",
    "dependencies_satisfied",
    "scientific_tree_identity",
    "state_revision_freshness",
    "no_unresolved_mandatory_blocker",
    "goal_complete_false_invariant",
    "clay_problem_unsolved_invariant",
    "scientific_acceptance_authority_separation",
    "regression_protection_for_consequential_defects",
}


def verify_project_bound_readiness(
    gate_inventory: Dict[str, Any],
    candidate_sha: Optional[str] = None,
    expected_tree_hash: Optional[str] = None,
    actual_tree_hash: Optional[str] = None,
    state: Optional[Dict[str, Any]] = None,
) -> bool:
    """
    Enforces F1 (Hard-Gate Inventory):
    A generic structural PASS cannot establish project readiness. The project-bound
    readiness rule requires all 12 explicit gates to be satisfied.
    """
    if not isinstance(gate_inventory, dict):
        raise ConstitutionalIntegrityError("Hard gate inventory must be a dictionary.")

    missing_gates = YANG_MILLS_REQUIRED_HARD_GATES - set(gate_inventory.keys())
    if missing_gates:
        raise ConstitutionalIntegrityError(
            f"Project-bound readiness rejected: missing required hard gates: {sorted(missing_gates)}"
        )

    for gate_name in YANG_MILLS_REQUIRED_HARD_GATES:
        gate_data = gate_inventory.get(gate_name)
        if not gate_data:
            raise ConstitutionalIntegrityError(f"Hard gate '{gate_name}' is empty or null.")
        status = gate_data.get("status") if isinstance(gate_data, dict) else str(gate_data)
        if status != "PASS":
            raise ConstitutionalIntegrityError(
                f"Hard gate '{gate_name}' failed or unverified with status: {status!r}"
            )

    if expected_tree_hash and actual_tree_hash and expected_tree_hash != actual_tree_hash:
        raise ConstitutionalIntegrityError(
            f"Scientific tree hash mismatch: expected {expected_tree_hash}, got {actual_tree_hash}"
        )

    if state:
        if state.get("goal_complete") is True and state.get("clay_problem") != "SOLVED_AND_VERIFIED":
            raise ConstitutionalIntegrityError("goal_complete cannot be True while clay_problem is unsolved.")
        if state.get("clay_problem") != "OPEN_AND_UNSOLVED":
            raise ConstitutionalIntegrityError(
                f"Clay problem invariant violated: expected 'OPEN_AND_UNSOLVED', got {state.get('clay_problem')!r}"
            )
        if state.get("blockers"):
            unresolved = [
                b for b in state["blockers"]
                if b.get("status") != "RESOLVED" and b.get("mandatory", False) is True
            ]
            if unresolved:
                raise ConstitutionalIntegrityError(f"Unresolved mandatory blockers present: {unresolved}")

    return True


def validate_state_revision_update(current_revision: int, proposed_revision: int) -> int:
    """
    Enforces atomic monotonic state serialization:
    Concurrent or stale state updates with proposed_revision <= current_revision
    are strictly rejected.
    """
    if not isinstance(proposed_revision, int) or not isinstance(current_revision, int):
        raise ConstitutionalIntegrityError("State revisions must be integers.")
    if proposed_revision <= current_revision:
        raise ConstitutionalIntegrityError(
            f"Stale state revision rejected: proposed {proposed_revision} <= current {current_revision}"
        )
    return proposed_revision


def validate_handoff_precedence(
    handoff_dict: Dict[str, Any],
    git_state_dict: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Enforces Cross-Agent Handoff Integrity:
    Handoff prose is never more authoritative than repository/state truth.
    When discrepancies exist, git and state truth strictly supersede handoff claims.
    """
    reconciled = dict(git_state_dict)
    for key, git_val in git_state_dict.items():
        handoff_val = handoff_dict.get(key)
        if handoff_val is not None and handoff_val != git_val:
            # Git and state truth prevail
            reconciled[key] = git_val
    return reconciled


def validate_autonomous_operation_bounds(
    consumed: Dict[str, Union[int, float]],
    limits: Dict[str, Union[int, float]],
    is_retry: bool = False,
    accumulated_retries: int = 0,
    retry_limit: int = 3,
) -> bool:
    """
    Enforces Bounded Autonomous Execution:
    - Operation bounds apply across retries and children;
    - Retries do not reset consumed budget;
    - Exceeding any limit raises ConstitutionalIntegrityError.
    """
    if is_retry and accumulated_retries >= retry_limit:
        raise ConstitutionalIntegrityError(
            f"Retry limit exceeded: {accumulated_retries} >= {retry_limit}"
        )

    for resource, limit in limits.items():
        used = consumed.get(resource, 0)
        if used > limit:
            raise ConstitutionalIntegrityError(
                f"Resource bound exceeded for {resource}: consumed {used} > limit {limit}"
            )
    return True


def validate_prompt_injection_boundary(
    content_type: str,
    attempted_permission_expansion: bool = False,
) -> bool:
    """
    Enforces Prompt-Injection Boundary:
    External text, websites, papers, comments, PDFs, and AI-generated outputs are DATA,
    not governance authority, and cannot expand permissions or authority.
    """
    if attempted_permission_expansion:
        raise ConstitutionalIntegrityError(
            f"Untrusted content of type '{content_type}' attempted unauthorized authority or permission expansion."
        )
    return True


def validate_architecture_stability(
    component_name: str,
    has_demonstrated_defect_or_requirement: bool,
    agent_preference_only: bool = True,
) -> bool:
    """
    Enforces Stable Architecture and Characterize-Before-Rewrite:
    Accepted architecture and verified components are stable by default;
    agent preference alone cannot trigger refactoring.
    """
    if agent_preference_only and not has_demonstrated_defect_or_requirement:
        raise ConstitutionalIntegrityError(
            f"Refactoring of stable component '{component_name}' rejected: "
            "agent preference alone cannot trigger rewrites without demonstrated defect or approved requirement."
        )
    return True


def validate_regression_protection_requirement(
    defect_id: str,
    has_durable_regression_test: bool,
    is_technically_inapplicable: bool = False,
    inapplicability_rationale: Optional[str] = None,
) -> bool:
    """
    Enforces Regression Memory:
    Every consequential defect must receive durable regression protection
    unless technically inapplicable with explicit recorded rationale.
    """
    if not has_durable_regression_test:
        if is_technically_inapplicable and inapplicability_rationale:
            return True
        raise ConstitutionalIntegrityError(
            f"Consequential defect '{defect_id}' lacks mandatory durable regression protection."
        )
    return True


def validate_consequential_effect_receipt(
    receipt: Dict[str, Any],
    deployment_adapter: str = "NONE_BY_DESIGN / NOT_APPLICABLE",
) -> bool:
    """
    Enforces F2 (Effect Receipt Binding):
    Yang-Mills has no live external deployment runtime (NONE_BY_DESIGN / NOT_APPLICABLE).
    Any consequential external effect requires explicit binding of:
    state_revision, frozen_subject_digest, artifact_digest, candidate_sha, scope,
    and effect_boundary_verification.
    """
    if deployment_adapter == "NONE_BY_DESIGN / NOT_APPLICABLE":
        if receipt.get("action") in {"EXTERNAL_DEPLOY", "LIVE_CLOUD_MUTATION", "EXTERNAL_SPEND"}:
            raise ConstitutionalIntegrityError(
                f"Action {receipt.get('action')!r} denied: deployment adapter is NONE_BY_DESIGN / NOT_APPLICABLE."
            )

    required_fields = {
        "state_revision",
        "frozen_subject_digest",
        "artifact_digest",
        "candidate_sha",
        "scope",
        "effect_boundary_verification",
    }
    missing = required_fields - set(receipt.keys())
    if missing:
        raise ConstitutionalIntegrityError(
            f"Consequential effect receipt missing required fields: {sorted(missing)}"
        )
    return True


ALLOWED_BASELINE_TRANSITION_CLASSES = {
    "SAME",
    "DESCENDANT_EVIDENCE_ONLY",
    "DESCENDANT_STATE_ONLY",
    "SUPERSEDED_BY_AMEND",
    "SEMANTIC_REVIEW_REQUIRED",
}


def verify_full_git_object_exists(
    sha: str,
    repo_root: Optional[Path] = None,
    require_commit_type: bool = True,
) -> str:
    """
    Verifies that `sha` is a valid 40-character hexadecimal Git object ID
    and exists in the Git object database of `repo_root`.
    Fails closed via ConstitutionalIntegrityError if abbreviated, malformed,
    or absent from the Git object store.
    """
    import re
    import subprocess

    if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{40}", sha):
        raise ConstitutionalIntegrityError(
            f"Recorded SHA {sha!r} is not a full 40-character lowercase hex Git object ID."
        )

    cwd = str(repo_root) if repo_root is not None else str(Path(__file__).resolve().parents[2])
    res = subprocess.run(
        ["git", "cat-file", "-t", sha],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    obj_type = res.stdout.strip()
    if res.returncode != 0 or not obj_type:
        raise ConstitutionalIntegrityError(
            f"Recorded SHA {sha!r} does not exist in the Git object database (git cat-file -t failed)."
        )
    if require_commit_type and obj_type != "commit":
        raise ConstitutionalIntegrityError(
            f"Recorded SHA {sha!r} exists in Git as {obj_type!r}, expected 'commit'."
        )
    return obj_type


def verify_baseline_lineage_transition(
    prior_closeout_sha: str,
    next_baseline_sha: str,
    transition_class: str,
    changed_files: Optional[List[str]] = None,
    reconciliation_record_path: Optional[str] = None,
    repo_root: Optional[Path] = None,
    verify_git_existence: bool = True,
) -> Dict[str, Any]:
    """
    Enforces YM-011-TREE-GAUGE-R1 Regression Protection Against Baseline SHA Drift:
    1. Both `prior_closeout_sha` and `next_baseline_sha` must be 40-char hex strings
       (and exist in Git when `verify_git_existence=True`, except that `SUPERSEDED_BY_AMEND`
       allows `prior_closeout_sha` to be a documented historical/superseded SHA if and only if
       `reconciliation_record_path` is provided and exists).
    2. `transition_class` must be in ALLOWED_BASELINE_TRANSITION_CLASSES:
       - SAME: `prior_closeout_sha == next_baseline_sha`.
       - DESCENDANT_EVIDENCE_ONLY: `prior_closeout_sha != next_baseline_sha` and all
         `changed_files` classify as EVIDENCE_ONLY or DOCUMENTATION_ONLY.
       - DESCENDANT_STATE_ONLY: `prior_closeout_sha != next_baseline_sha` and all
         `changed_files` classify as STATE_ONLY, EVIDENCE_ONLY, or DOCUMENTATION_ONLY.
       - SUPERSEDED_BY_AMEND: `prior_closeout_sha != next_baseline_sha` and an explicit
         `reconciliation_record_path` is provided and exists on disk.
       - SEMANTIC_REVIEW_REQUIRED: blocks automatic transition and raises
         ConstitutionalIntegrityError requiring a fresh candidate-bound review.
    3. Any unexplained difference between `prior_closeout_sha` and `next_baseline_sha`
       fails closed.
    """
    import re

    for label, val in [("prior_closeout_sha", prior_closeout_sha), ("next_baseline_sha", next_baseline_sha)]:
        if not isinstance(val, str) or not re.fullmatch(r"[0-9a-f]{40}", val):
            raise ConstitutionalIntegrityError(
                f"{label}={val!r} violates 40-character hexadecimal SHA requirement."
            )

    if transition_class not in ALLOWED_BASELINE_TRANSITION_CLASSES:
        raise ConstitutionalIntegrityError(
            f"Invalid baseline transition_class {transition_class!r}; must be one of "
            f"{sorted(ALLOWED_BASELINE_TRANSITION_CLASSES)}."
        )

    if transition_class == "SEMANTIC_REVIEW_REQUIRED":
        raise ConstitutionalIntegrityError(
            f"Baseline transition from {prior_closeout_sha} to {next_baseline_sha} is marked "
            "SEMANTIC_REVIEW_REQUIRED: automatic baseline acceptance is blocked."
        )

    root_dir = repo_root if repo_root is not None else Path(__file__).resolve().parents[2]

    if verify_git_existence:
        verify_full_git_object_exists(next_baseline_sha, repo_root=root_dir, require_commit_type=True)
        if transition_class != "SUPERSEDED_BY_AMEND":
            verify_full_git_object_exists(prior_closeout_sha, repo_root=root_dir, require_commit_type=True)

    if transition_class == "SAME":
        if prior_closeout_sha != next_baseline_sha:
            raise ConstitutionalIntegrityError(
                f"Baseline SHA drift detected under transition_class='SAME': "
                f"prior_closeout_sha={prior_closeout_sha} != next_baseline_sha={next_baseline_sha}."
            )
    elif transition_class in {"DESCENDANT_EVIDENCE_ONLY", "DESCENDANT_STATE_ONLY"}:
        if prior_closeout_sha == next_baseline_sha:
            raise ConstitutionalIntegrityError(
                f"transition_class={transition_class!r} requires distinct SHAs, got identical {prior_closeout_sha}."
            )
        if not changed_files:
            raise ConstitutionalIntegrityError(
                f"transition_class={transition_class!r} requires non-empty changed_files list for audit."
            )
        allowed_cats = (
            {"EVIDENCE_ONLY", "DOCUMENTATION_ONLY"}
            if transition_class == "DESCENDANT_EVIDENCE_ONLY"
            else {"STATE_ONLY", "EVIDENCE_ONLY", "DOCUMENTATION_ONLY"}
        )
        for path in changed_files:
            cat = classify_post_review_change(path)
            if cat not in allowed_cats:
                raise ConstitutionalIntegrityError(
                    f"File {path!r} classified as {cat!r} is forbidden in {transition_class!r} baseline transition."
                )
    elif transition_class == "SUPERSEDED_BY_AMEND":
        if prior_closeout_sha == next_baseline_sha:
            raise ConstitutionalIntegrityError(
                "transition_class='SUPERSEDED_BY_AMEND' requires distinct prior and replacement SHAs."
            )
        if not reconciliation_record_path:
            raise ConstitutionalIntegrityError(
                "transition_class='SUPERSEDED_BY_AMEND' requires an explicit reconciliation_record_path."
            )
        rec_file = Path(reconciliation_record_path)
        if not rec_file.is_absolute():
            rec_file = root_dir / rec_file
        if not rec_file.is_file():
            raise ConstitutionalIntegrityError(
                f"Reconciliation record {str(rec_file)!r} does not exist on disk."
            )

    return {
        "status": "BASELINE_LINEAGE_VERIFIED",
        "prior_closeout_sha": prior_closeout_sha,
        "next_baseline_sha": next_baseline_sha,
        "transition_class": transition_class,
        "reconciliation_record_path": reconciliation_record_path,
    }


