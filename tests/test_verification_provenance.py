import re
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_independent_review_references_raw_artifact_and_sha256():
    review_path = ROOT / "verification" / "YM-001R1_INDEPENDENT_REVIEW.md"
    assert review_path.exists(), "YM-001R1_INDEPENDENT_REVIEW.md must exist"
    content = review_path.read_text(encoding="utf-8")
    
    # 1. Reference raw artifact
    m_raw = re.search(r"DERIVED FROM[:\* ]*`([^`]+)`", content)
    assert m_raw, "Must declare DERIVED FROM raw verifier file"
    raw_rel = m_raw.group(1)
    raw_path = ROOT / raw_rel
    assert raw_path.exists(), f"Raw verifier artifact {raw_path} must exist on disk"
    
    # 2. Raw SHA-256 recorded and matches disk
    m_sha = re.search(r"RAW_SHA256[:\* ]*`([a-f0-9]{64})`", content)
    assert m_sha, "Must record RAW_SHA256"
    recorded_sha = m_sha.group(1)
    actual_sha = hashlib.sha256(raw_path.read_bytes()).hexdigest()
    assert recorded_sha == actual_sha, f"Raw artifact hash mismatch: {recorded_sha} != {actual_sha}"

def test_verifier_identity_and_candidate_sha_present():
    review_path = ROOT / "verification" / "YM-001R1_INDEPENDENT_REVIEW.md"
    content = review_path.read_text(encoding="utf-8")
    
    # 3. Verifier identity exists
    m_verifier = re.search(r"VERIFIER CONVERSATION ID[:\* ]*`([^`]+)`", content)
    assert m_verifier, "Must record VERIFIER CONVERSATION ID"
    assert len(m_verifier.group(1)) > 5
    
    # 4. Candidate SHA exists
    m_sha = re.search(r"CANDIDATE GIT SHA AUDITED[:\* ]*`([a-f0-9]+)`", content)
    assert m_sha, "Must record CANDIDATE GIT SHA AUDITED"
    candidate_sha = m_sha.group(1)
    assert candidate_sha == "24af7f9c9b648269be7438af10480c036f177dd4"


def test_worker_authored_review_cannot_satisfy_e4():
    # Verify that historical worker-authored reviews are explicitly marked NOT_E4
    hist_ym001 = ROOT / "verification" / "historical" / "YM-001_INDEPENDENT_REVIEW_WORKER_AUTHORED.md"
    assert hist_ym001.exists(), "Historical YM-001 worker-authored review must be preserved"
    
    old_ym001_rev = ROOT / "verification" / "YM-001_INDEPENDENT_REVIEW.md"
    if old_ym001_rev.exists():
        assert "EVIDENCE_LEVEL: NOT_E4" in old_ym001_rev.read_text(encoding="utf-8")
    
    hist_ym002a = ROOT / "verification" / "historical" / "YM-002A_INDEPENDENT_REVIEW_WORKER_AUTHORED.md"
    assert hist_ym002a.exists(), "Historical YM-002A worker-authored review must be preserved"
    
    old_ym002a_rev = ROOT / "verification" / "YM-002A_INDEPENDENT_REVIEW.md"
    if old_ym002a_rev.exists():
        assert "EVIDENCE_LEVEL: NOT_E4" in old_ym002a_rev.read_text(encoding="utf-8")


def test_integrity_violation_register_records_ivr001_and_ivr002():
    ivr_path = ROOT / "INTEGRITY_VIOLATION_REGISTER.md"
    assert ivr_path.exists(), "INTEGRITY_VIOLATION_REGISTER.md must exist"
    content = ivr_path.read_text(encoding="utf-8")
    assert "IVR-001" in content
    assert "I1 — Unsupported material claim" in content
    assert "YM-001R1" in content
    assert "IVR-002" in content
    assert "I2 — REPEATED UNSUPPORTED INDEPENDENT-VERIFICATION CLAIM" in content
    assert "YM-002AR1" in content

def test_ym002ar1_independent_review_provenance_if_present():
    review_path = ROOT / "verification" / "YM-002AR1_INDEPENDENT_REVIEW.md"
    if not review_path.exists():
        return
    content = review_path.read_text(encoding="utf-8")
    
    # Raw file reference
    m_raw = re.search(r"DERIVED FROM[:\* ]*`([^`]+)`", content)
    assert m_raw, "Must declare DERIVED FROM raw verifier file"
    raw_rel = m_raw.group(1)
    raw_path = ROOT / raw_rel
    assert raw_path.exists(), f"Raw verifier artifact {raw_path} must exist on disk"
    
    # Raw hash match
    m_sha = re.search(r"RAW_SHA256[:\* ]*`([a-f0-9]{64})`", content)
    assert m_sha, "Must record RAW_SHA256"
    recorded_sha = m_sha.group(1)
    actual_sha = hashlib.sha256(raw_path.read_bytes()).hexdigest()
    assert recorded_sha == actual_sha, f"Raw artifact hash mismatch: {recorded_sha} != {actual_sha}"
    
    # Verifier ID
    m_verifier = re.search(r"VERIFIER CONVERSATION ID[:\* ]*`([^`]+)`", content)
    assert m_verifier, "Must record VERIFIER CONVERSATION ID"
    assert len(m_verifier.group(1)) > 5
    
    # Candidate SHA
    m_sha = re.search(r"CANDIDATE GIT SHA AUDITED[:\* ]*`([a-f0-9]+)`", content)
    assert m_sha, "Must record CANDIDATE GIT SHA AUDITED"
    assert len(m_sha.group(1)) >= 7


def test_ym002b_independent_review_provenance_if_present():
    review_path = ROOT / "verification" / "YM-002B_INDEPENDENT_REVIEW.md"
    if not review_path.exists():
        return
    content = review_path.read_text(encoding="utf-8")

    # Raw file reference
    m_raw = re.search(r"DERIVED FROM[:\* ]*`([^`]+)`", content)
    assert m_raw, "Must declare DERIVED FROM raw verifier file"
    raw_rel = m_raw.group(1)
    raw_path = ROOT / raw_rel
    assert raw_path.exists(), f"Raw verifier artifact {raw_path} must exist on disk"

    # Raw hash match
    m_sha = re.search(r"RAW_SHA256[:\* ]*`([a-f0-9]{64})`", content)
    assert m_sha, "Must record RAW_SHA256"
    recorded_sha = m_sha.group(1)
    actual_sha = hashlib.sha256(raw_path.read_bytes()).hexdigest()
    assert recorded_sha == actual_sha, f"Raw artifact hash mismatch: {recorded_sha} != {actual_sha}"

    # Verifier ID
    m_verifier = re.search(r"VERIFIER CONVERSATION ID[:\* ]*`([^`]+)`", content)
    assert m_verifier, "Must record VERIFIER CONVERSATION ID"
    assert len(m_verifier.group(1)) > 5

    # Candidate SHA
    m_sha = re.search(r"CANDIDATE GIT SHA AUDITED[:\* ]*`([a-f0-9]+)`", content)
    assert m_sha, "Must record CANDIDATE GIT SHA AUDITED"
    assert len(m_sha.group(1)) >= 7


def test_ym002br1_independent_review_provenance_if_present():
    review_path = ROOT / "verification" / "YM-002BR1_INDEPENDENT_REVIEW.md"
    if not review_path.exists():
        return
    content = review_path.read_text(encoding="utf-8")

    # Raw file reference
    m_raw = re.search(r"DERIVED FROM[:\* ]*`([^`]+)`", content)
    assert m_raw, "Must declare DERIVED FROM raw verifier file"
    raw_rel = m_raw.group(1)
    raw_path = ROOT / raw_rel
    assert raw_path.exists(), f"Raw verifier artifact {raw_path} must exist on disk"

    # Raw hash match
    m_sha = re.search(r"RAW_SHA256[:\* ]*`([a-f0-9]{64})`", content)
    assert m_sha, "Must record RAW_SHA256"
    recorded_sha = m_sha.group(1)
    actual_sha = hashlib.sha256(raw_path.read_bytes()).hexdigest()
    assert recorded_sha == actual_sha, f"Raw artifact hash mismatch: {recorded_sha} != {actual_sha}"

    # Verifier ID
    m_verifier = re.search(r"VERIFIER CONVERSATION ID[:\* ]*`([^`]+)`", content)
    assert m_verifier, "Must record VERIFIER CONVERSATION ID"
    assert len(m_verifier.group(1)) > 5

    # Candidate SHA
    m_sha = re.search(r"CANDIDATE GIT SHA AUDITED[:\* ]*`([a-f0-9]+)`", content)
    assert m_sha, "Must record CANDIDATE GIT SHA AUDITED"
    assert len(m_sha.group(1)) >= 7


def test_ym002c_independent_review_provenance_if_present():
    review_path = ROOT / "verification" / "YM-002C_INDEPENDENT_REVIEW.md"
    if not review_path.exists():
        return
    content = review_path.read_text(encoding="utf-8")

    # Raw file reference
    m_raw = re.search(r"DERIVED FROM[:\* ]*`([^`]+)`", content)
    assert m_raw, "Must declare DERIVED FROM raw verifier file"
    raw_rel = m_raw.group(1)
    raw_path = ROOT / raw_rel
    assert raw_path.exists(), f"Raw verifier artifact {raw_path} must exist on disk"

    # Raw hash match
    m_sha = re.search(r"RAW_SHA256[:\* ]*`([a-f0-9]{64})`", content)
    assert m_sha, "Must record RAW_SHA256"
    recorded_sha = m_sha.group(1)
    actual_sha = hashlib.sha256(raw_path.read_bytes()).hexdigest()
    assert recorded_sha == actual_sha, f"Raw artifact hash mismatch: {recorded_sha} != {actual_sha}"

    # Verifier ID
    m_verifier = re.search(r"VERIFIER CONVERSATION ID[:\* ]*`([^`]+)`", content)
    assert m_verifier, "Must record VERIFIER CONVERSATION ID"
    assert len(m_verifier.group(1)) > 5

    # Candidate SHA
    m_sha = re.search(r"CANDIDATE GIT SHA AUDITED[:\* ]*`([a-f0-9]+)`", content)
    assert m_sha, "Must record CANDIDATE GIT SHA AUDITED"
    assert len(m_sha.group(1)) >= 7


def test_ym002cr1_independent_review_provenance_if_present():
    review_path = ROOT / "verification" / "YM-002CR1_INDEPENDENT_REVIEW.md"
    if not review_path.exists():
        return
    content = review_path.read_text(encoding="utf-8")

    # Raw file reference
    m_raw = re.search(r"DERIVED FROM[:\* ]*`([^`]+)`", content)
    assert m_raw, "Must declare DERIVED FROM raw verifier file"
    raw_rel = m_raw.group(1)
    raw_path = ROOT / raw_rel
    assert raw_path.exists(), f"Raw verifier artifact {raw_path} must exist on disk"

    # Raw hash match
    m_sha = re.search(r"RAW_SHA256[:\* ]*`([a-f0-9]{64})`", content)
    assert m_sha, "Must record RAW_SHA256"
    recorded_sha = m_sha.group(1)
    actual_sha = hashlib.sha256(raw_path.read_bytes()).hexdigest()
    assert recorded_sha == actual_sha, f"Raw artifact hash mismatch: {recorded_sha} != {actual_sha}"

    # Verifier ID
    m_verifier = re.search(r"VERIFIER CONVERSATION ID[:\* ]*`([^`]+)`", content)
    assert m_verifier, "Must record VERIFIER CONVERSATION ID"
    assert len(m_verifier.group(1)) > 5

    # Candidate SHA
    m_sha = re.search(r"CANDIDATE GIT SHA AUDITED[:\* ]*`([a-f0-9]+)`", content)
    assert m_sha, "Must record CANDIDATE GIT SHA AUDITED"
    assert len(m_sha.group(1)) >= 7







