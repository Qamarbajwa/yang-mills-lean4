import pytest
import yaml
import hashlib
from pathlib import Path
from src.ymmg.ros import (
    validate_project_binding,
    compute_closed_world_scientific_tree_hash,
    classify_repository_artifact,
    discover_repository_artifacts,
    validate_scientific_artifact_classification,
    compute_canonical_dependency_hash,
    compute_cited_source_hash,
    evaluate_post_e4_change_class,
    verify_raw_e4_hash_integrity,
    compute_pathway_resonance,
    evaluate_obstruction_transition,
    validate_memory_partition,
    validate_constitutional_amendment,
    SCIENTIFIC_FINGERPRINT_MANIFEST,
    ProjectBindingError,
    ConstitutionalIntegrityError
)

ROOT = Path(__file__).resolve().parents[1]
ROS_DOC_PATH = ROOT / "governance" / "MATHEMATICAL_RESEARCH_OPERATING_SYSTEM_v1.0.md"
TAXONOMY_PATH = ROOT / "governance" / "EPISTEMIC_TAXONOMY_v1.0.yaml"
BINDING_POLICY_PATH = ROOT / "governance" / "PROJECT_BINDING_POLICY.md"

def test_law_0_minimal_read_exception_and_fail_closed_gate(tmp_path):
    # Valid project binding passes
    assert validate_project_binding(ROOT, "YANG_MILLS_MASS_GAP") is True
    assert validate_project_binding(ROOT, "YM-MASS-GAP") is True
    
    # Invalid project ID fails closed
    with pytest.raises(ProjectBindingError):
        validate_project_binding(ROOT, "REVIT-MCP-SERVER")
        
    # Non-existent or mismatched workspace root fails closed
    with pytest.raises(ProjectBindingError):
        validate_project_binding(tmp_path, "YANG_MILLS_MASS_GAP")

def test_closed_world_scientific_fingerprint_manifest():
    assert len(SCIENTIFIC_FINGERPRINT_MANIFEST) == 61
    tree_hash, file_hashes = compute_closed_world_scientific_tree_hash(ROOT)
    assert len(tree_hash) == 64
    assert len(file_hashes) == 61
    for rel_path in SCIENTIFIC_FINGERPRINT_MANIFEST:
        assert rel_path in file_hashes
        assert (ROOT / rel_path).exists()


def test_r3_classifies_existing_repository_without_unknown_artifacts():
    classifications = validate_scientific_artifact_classification(ROOT)
    assert classifications["governance/SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml"] == "SCIENTIFIC"
    assert classifications["literature/primary/solved_modified_analogous/PAPER-ANA-001/record.md"] == "PROVENANCE_CRITICAL"
    assert classifications["verification/raw/YM-ROS-100R2_E4_RAW_20260829T004439Z.md"] == "PROVENANCE_CRITICAL"
    assert classifications["checkpoints/checkpoint_20260829T004511Z.json"] == "GENERATED"


def test_r3_new_scientific_locations_fail_closed():
    assert classify_repository_artifact(ROOT, "proofs/bridge_lemma.md") == "UNKNOWN"
    assert classify_repository_artifact(ROOT, "OPEN_LEMMA_REGISTER_R3.md") == "UNKNOWN"
    assert classify_repository_artifact(
        ROOT, "literature/primary/solved_modified_analogous/PAPER-ANA-011/record.md"
    ) == "UNKNOWN"

    # The discovery API sees an untracked artifact as well as Git-tracked files.
    new_path = ROOT / "proofs" / "bridge_lemma.md"
    new_path.write_text("# unclassified bridge lemma\n", encoding="utf-8")
    try:
        with pytest.raises(ConstitutionalIntegrityError, match="Unknown research artifact"):
            discover_repository_artifacts(ROOT) and validate_scientific_artifact_classification(ROOT)
    finally:
        new_path.unlink()

def test_source_bound_official_target_fields():
    assert TAXONOMY_PATH.exists(), "EPISTEMIC_TAXONOMY_v1.0.yaml must exist"
    data = yaml.safe_load(TAXONOMY_PATH.read_text(encoding="utf-8"))
    
    target = data["problem_identity_contract"]
    assert target["problem_id"] == "CLAY-YM-001"
    assert "Jaffe" in target["official_target"]["source"]
    assert "Witten" in target["official_target"]["source"]
    
    gap_cond = target["official_mass_gap_condition"]
    assert gap_cond["source_status"] == "SOURCE_RECONCILED"
    assert "Spec(H)" in gap_cond["spectral_condition"]
    assert "Delta > 0" in gap_cond["spectral_condition"]
    assert gap_cond["vacuum_normalization"] == "H * Omega = 0"

def test_nontriviality_proxy_cannot_be_silently_asserted():
    data = yaml.safe_load(TAXONOMY_PATH.read_text(encoding="utf-8"))
    nt = data["problem_identity_contract"]["nontriviality"]
    assert nt["status"] == "SOURCE_RECONCILIATION_REQUIRED"
    assert "Do not replace 'non-trivial' by scattering, Wilson-loop" in nt["rule"]
    
    doc_text = ROS_DOC_PATH.read_text(encoding="utf-8")
    assert "NONTRIVIALITY_CRITERION" not in doc_text or "SOURCE_RECONCILIATION_REQUIRED" in doc_text

def test_semantic_os_reflection_positivity_has_no_fragile_numbering():
    data = yaml.safe_load(TAXONOMY_PATH.read_text(encoding="utf-8"))
    lib = data["semantic_failure_library"]
    
    assert "FAIL-YM-REFLECTION-POSITIVITY" in lib
    entry = lib["FAIL-YM-REFLECTION-POSITIVITY"]
    assert entry["semantic_name"] == "REQUIRED_OS_REFLECTION_POSITIVITY_NOT_ESTABLISHED"
    assert "OS3" not in entry["semantic_name"]

def test_euclidean_route_classified_as_reconstruction_route():
    data = yaml.safe_load(TAXONOMY_PATH.read_text(encoding="utf-8"))
    euclid = data["problem_identity_contract"]["axiomatic_existence"]["euclidean_route"]
    assert euclid["relation"] == "RECONSTRUCTION_ROUTE"
    assert "Osterwalder" in euclid["description"]

def test_reversible_claim_transitions_preserve_history():
    doc_text = ROS_DOC_PATH.read_text(encoding="utf-8")
    assert "Research history is monotonic; epistemic status is reversible." in doc_text

def test_resonance_schema_and_justification_requirements():
    data = yaml.safe_load(TAXONOMY_PATH.read_text(encoding="utf-8"))
    dims = data["resonance_schema"]["dimensions"]
    assert len(dims) == 7
    for d in ["THESIS", "MECHANISM", "ASSUMPTIONS", "SCALING", "BRIDGE_VARIABLE", "FAILURE_LOCALITY", "OBSERVABLE"]:
        assert d in dims
        
    allowed_scores = data["resonance_schema"]["allowed_scores"]
    assert {"NONE", "LOW", "MODERATE", "HIGH", "EXACT", "UNKNOWN"}.issubset(set(allowed_scores))
    
    # Valid resonance evaluation
    valid_eval = {
        d: {
            "score": "HIGH" if d in ["FAILURE_LOCALITY", "MECHANISM"] else "LOW",
            "textual_justification": f"Detailed justification for {d}",
            "evidence_pointers": ["PAPER-ANA-001/record.md"]
        } for d in dims
    }
    res = compute_pathway_resonance(valid_eval, new_result_removes_old_blocker=True)
    assert res["reopen_recommended"] is True
    
    # Missing justification raises error
    invalid_eval = {
        d: {
            "score": "HIGH",
            "textual_justification": "",
            "evidence_pointers": ["ref"]
        } for d in dims
    }
    with pytest.raises(ValueError, match="Textual justification required"):
        compute_pathway_resonance(invalid_eval)

def test_common_obstruction_candidate_cannot_jump_directly_to_theorem():
    # Attempting to jump directly from CANDIDATE to PROVED_OBSTRUCTION_THEOREM raises ConstitutionalIntegrityError
    with pytest.raises(ConstitutionalIntegrityError, match="Illegal jump"):
        evaluate_obstruction_transition("CANDIDATE", "INDEPENDENT_E4_VERIFIED", "METHOD_OBSTRUCTION")
    
    # Proper progression
    s1 = evaluate_obstruction_transition("CANDIDATE", "FALSIFICATION_ATTACK_SURVIVED", "METHOD_OBSTRUCTION")
    assert s1 == "SURVIVED_FALSIFICATION"
    
    s2 = evaluate_obstruction_transition(s1, "FORMAL_OBSTRUCTION_LEMMA_CONSTRUCTED", "METHOD_OBSTRUCTION")
    assert s2 == "THEOREM_CANDIDATE"
    
    s3 = evaluate_obstruction_transition(s2, "INDEPENDENT_E4_VERIFIED", "METHOD_OBSTRUCTION")
    assert s3 == "PROVED_OBSTRUCTION_THEOREM"

def test_dependency_tuple_mutation_changes_hash():
    deps1 = [
        {"dependency_id": "THM-YM-0001", "dependency_version": "v1.0", "dependency_statement_hash": "hash_a1"},
        {"dependency_id": "THM-YM-0002", "dependency_version": "v1.0", "dependency_statement_hash": "hash_b1"},
    ]
    h1 = compute_canonical_dependency_hash(deps1)
    
    # Mutate statement hash while keeping ID and version
    deps2 = [
        {"dependency_id": "THM-YM-0001", "dependency_version": "v1.0", "dependency_statement_hash": "hash_a2"},
        {"dependency_id": "THM-YM-0002", "dependency_version": "v1.0", "dependency_statement_hash": "hash_b1"},
    ]
    h2 = compute_canonical_dependency_hash(deps2)
    assert h1 != h2, "Dependency hash must change when statement hash changes"
    
    # Mutate version
    deps3 = [
        {"dependency_id": "THM-YM-0001", "dependency_version": "v1.1", "dependency_statement_hash": "hash_a1"},
        {"dependency_id": "THM-YM-0002", "dependency_version": "v1.0", "dependency_statement_hash": "hash_b1"},
    ]
    h3 = compute_canonical_dependency_hash(deps3)
    assert h1 != h3, "Dependency hash must change when version changes"

def test_unrelated_source_mutation_does_not_invalidate_unrelated_claim():
    claim_a_sources = [
        {"source_id": "PAPER-FOUND-001", "source_version": "v1.0", "source_content_hash": "hash_f1", "source_access_level": "PRIMARY_FULL_TEXT"}
    ]
    claim_b_sources = [
        {"source_id": "PAPER-CONST-001", "source_version": "v1.0", "source_content_hash": "hash_c1", "source_access_level": "PRIMARY_FULL_TEXT"}
    ]
    
    h_a1 = compute_cited_source_hash(claim_a_sources)
    h_b1 = compute_cited_source_hash(claim_b_sources)
    
    # Mutate claim B source
    claim_b_sources_mutated = [
        {"source_id": "PAPER-CONST-001", "source_version": "v1.1", "source_content_hash": "hash_c2", "source_access_level": "PRIMARY_FULL_TEXT"}
    ]
    h_b2 = compute_cited_source_hash(claim_b_sources_mutated)
    
    # Claim A source hash remains identical
    assert compute_cited_source_hash(claim_a_sources) == h_a1
    assert h_b1 != h_b2

def test_relevant_cited_source_mutation_invalidates_source_hash():
    sources = [
        {"source_id": "PAPER-FOUND-001", "source_version": "v1.0", "source_content_hash": "hash_old", "source_access_level": "PRIMARY_FULL_TEXT"}
    ]
    h_old = compute_cited_source_hash(sources)
    
    sources_new = [
        {"source_id": "PAPER-FOUND-001", "source_version": "v1.0", "source_content_hash": "hash_new", "source_access_level": "PRIMARY_FULL_TEXT"}
    ]
    h_new = compute_cited_source_hash(sources_new)
    assert h_old != h_new

def test_post_e4_change_classification_logic():
    h_sci_1 = "hash_scientific_v1"
    h_sci_2 = "hash_scientific_v2"
    
    # 1. Identical hash, no files changed
    c1, v1 = evaluate_post_e4_change_class(h_sci_1, h_sci_1, [])
    assert c1 == "NONE" and v1 is True
    
    # 2. Identical hash, provenance/administrative files changed
    c2, v2 = evaluate_post_e4_change_class(h_sci_1, h_sci_1, ["verification/raw/E4.md", "TASK_GRAPH.md"])
    assert c2 == "PROVENANCE_CRITICAL" and v2 is True
    c2b, v2b = evaluate_post_e4_change_class(h_sci_1, h_sci_1, ["EVIDENCE_LEDGER.md"])
    assert c2b == "PROVENANCE_CRITICAL" and v2b is True
    c2c, v2c = evaluate_post_e4_change_class(h_sci_1, h_sci_1, ["src/ymmg/ros.py"])
    assert c2c == "ADMINISTRATIVE_ONLY" and v2c is True
    
    # 3. Scientific hash modified
    c3, v3 = evaluate_post_e4_change_class(h_sci_1, h_sci_2, ["THEOREM_LEDGER.md"])
    assert c3 == "SCIENTIFIC_MATERIAL" and v3 is False # E4 is STALE

def test_raw_e4_hash_integrity_verification(tmp_path):
    raw_file = tmp_path / "raw_e4.md"
    raw_content = b"VERDICT: INTEGRITY_PASS\nDETAILS: Verified all 10 questions."
    raw_file.write_bytes(raw_content)
    raw_hash = hashlib.sha256(raw_content).hexdigest()
    
    # Derived review with matching hash passes
    review_file = tmp_path / "review.md"
    review_file.write_text(f"# REVIEW\n- RAW_SHA256: `{raw_hash}`\n", encoding="utf-8")
    assert verify_raw_e4_hash_integrity(review_file, raw_file) is True
    
    # Derived review with mismatched hash fails closed
    review_bad = tmp_path / "review_bad.md"
    review_bad.write_text("# REVIEW\n- RAW_SHA256: `badhash123`\n", encoding="utf-8")
    with pytest.raises(ConstitutionalIntegrityError, match="RAW_SHA256 mismatch"):
        verify_raw_e4_hash_integrity(review_bad, raw_file)

def test_quarantined_claims_cannot_enter_accepted_semantic_memory():
    with pytest.raises(ConstitutionalIntegrityError, match="Quarantined claims cannot be placed in semantic_accepted memory"):
        validate_memory_partition("semantic_accepted", "QUARANTINED_CLAIM")
        
    assert validate_memory_partition("semantic_quarantined", "QUARANTINED_CLAIM") is True

def test_constitutional_amendment_requires_all_eight_fields():
    valid_amendment = {
        "CHANGE_PROPOSAL": "Refine Law 6 independence vector",
        "RATIONALE": "Incorporate Lean 4 proof verification status",
        "IMPACT_ANALYSIS": "Zero regression on existing theorem ledger",
        "REGRESSION_TESTS": "tests/test_research_operating_system.py passing",
        "NEW_VERSION": "v1.1.0",
        "INDEPENDENT_REVIEW": "E4 verified by independent auditor",
        "HUMAN_OWNER_ACCEPTANCE": "Approved by Human Owner",
        "SEALED_MIGRATION_RECEIPT": "checkpoints/checkpoint_20260828T000000Z.json"
    }
    assert validate_constitutional_amendment(valid_amendment) is True
    
    # Incomplete amendment fails closed
    incomplete = valid_amendment.copy()
    del incomplete["HUMAN_OWNER_ACCEPTANCE"]
    with pytest.raises(ConstitutionalIntegrityError, match="missing required field"):
        validate_constitutional_amendment(incomplete)
