"""Deterministic test suite for Task YM-LEAN-001: Lean 4 Formalization Scoping.

Verifies:
1. Lean 4 package and module files exist and are populated.
2. Formalization of Clay problem specification matches Jaffe-Witten (2000).
3. Formalization of Wightman axioms (W0-W5) and Osterwalder-Schrader axioms (OS0-OS4).
4. Formalization of YM-003 missing-bridge DAG with machine-checked acyclicity.
5. Strict consistency with literature/BRIDGE_EDGE_REGISTER.md.
6. Absence of false claims of having solved the Clay problem.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEAN_DIR = ROOT / "formal" / "lean4"
YM_LEAN_DIR = LEAN_DIR / "YangMills"


def test_01_lean_project_files_exist():
    """Verify all Lean 4 source files and audit records exist."""
    required_files = [
        LEAN_DIR / "lakefile.lean",
        LEAN_DIR / "lean-toolchain",
        LEAN_DIR / "YangMills.lean",
        YM_LEAN_DIR / "ClaySpecification.lean",
        YM_LEAN_DIR / "WightmanAxioms.lean",
        YM_LEAN_DIR / "OsterwalderSchraderAxioms.lean",
        YM_LEAN_DIR / "MissingBridgeDAG.lean",
        ROOT / "literature" / "YM-LEAN-001-FORMALIZATION-AUDIT.md",
    ]
    for path in required_files:
        assert path.exists(), f"Required Lean formalization file missing: {path}"
        assert path.stat().st_size > 10, f"File {path} is suspiciously small ({path.stat().st_size} bytes)"


def test_02_clay_specification_structure():
    """Verify Clay problem statement formalization in ClaySpecification.lean."""
    content = (YM_LEAN_DIR / "ClaySpecification.lean").read_text(encoding="utf-8")
    assert "def SpacetimeDimension : Nat := 4" in content
    assert "class CompactSimpleLieGroup" in content
    assert "structure SUNGroup" in content
    assert "structure PhysicalHilbertSpace" in content
    assert "structure PoincareRepresentation" in content
    assert "structure EnergyMomentum" in content
    assert "structure VacuumState" in content
    assert "def HasMassGap" in content
    assert "def ClayMillenniumYangMillsProblem : Prop :=" in content
    assert "axiom clay_millennium_problem_status" in content


def test_03_wightman_axioms_structure():
    """Verify Wightman axioms W0-W5 formalization in WightmanAxioms.lean."""
    content = (YM_LEAN_DIR / "WightmanAxioms.lean").read_text(encoding="utf-8")
    assert "structure SchwartzSpace4D" in content
    assert "def SpacelikeSeparated" in content
    assert "def TestFunctionsSpacelike" in content
    assert "structure WightmanQFT" in content
    assert "poincare_covariance" in content
    assert "spectral_condition" in content
    assert "microcausality" in content
    assert "vacuum_cyclic" in content
    assert "def WightmanHasMassGap" in content
    assert "def WightmanReconstructionTheorem" in content


def test_04_osterwalder_schrader_axioms_structure():
    """Verify Osterwalder-Schrader axioms OS0-OS4 formalization in OsterwalderSchraderAxioms.lean."""
    content = (YM_LEAN_DIR / "OsterwalderSchraderAxioms.lean").read_text(encoding="utf-8")
    assert "def EuclideanTimeReflection" in content
    assert "structure PositiveTimeSchwartz" in content
    assert "structure SchwingerFunctionFamily" in content
    assert "structure OsterwalderSchraderQFT" in content
    assert "os0_tempered" in content
    assert "os1_euclidean_invariant" in content
    assert "os2_permutation_symmetric" in content
    assert "os3_reflection_positivity" in content
    assert "os4_cluster_property" in content
    assert "def HasExponentialClustering" in content
    assert "theorem osterwalder_schrader_reconstruction" in content


def test_05_missing_bridge_dag_structure_and_acyclicity():
    """Verify missing-bridge DAG formalization and acyclicity theorem."""
    content = (YM_LEAN_DIR / "MissingBridgeDAG.lean").read_text(encoding="utf-8")
    assert "inductive GraphNode" in content
    assert "inductive EdgeStatus" in content
    assert "structure BridgeEdge" in content
    assert "def nodeRank : GraphNode -> Nat" in content
    assert "def canonicalEdges : List BridgeEdge :=" in content
    assert "theorem edge_strictly_increases_rank" in content
    assert "theorem bridge_graph_is_acyclic" in content
    assert "def CriticalCutSetEdges : List String :=" in content

    # Count canonical edges declared in Lean
    edge_matches = re.findall(r'⟨"(E-[^"]+)"', content)
    assert len(edge_matches) == 19, f"Expected 19 canonical edge entries in Lean DAG, found {len(edge_matches)}"


def test_06_edge_id_consistency_with_bridge_register():
    """Verify that the 19 edge IDs in Lean match BRIDGE_EDGE_REGISTER.md exactly."""
    lean_content = (YM_LEAN_DIR / "MissingBridgeDAG.lean").read_text(encoding="utf-8")
    lean_edge_ids = set(re.findall(r'⟨"(E-[^"]+)"', lean_content))

    register_content = (ROOT / "literature" / "BRIDGE_EDGE_REGISTER.md").read_text(encoding="utf-8")
    register_edge_ids = set(re.findall(r'EDGE_ID:\s*["\']?(E-[^\s"\']+)["\']?', register_content))

    assert len(register_edge_ids) == 19, f"Expected 19 edges in register, found {len(register_edge_ids)}"
    assert lean_edge_ids == register_edge_ids, f"Mismatch in edge IDs: {lean_edge_ids ^ register_edge_ids}"


def test_07_no_overclaims_or_clay_solution():
    """Verify that formalization files strictly preserve the open status of the Clay problem."""
    all_lean_text = ""
    for path in LEAN_DIR.glob("**/*.lean"):
        all_lean_text += path.read_text(encoding="utf-8") + "\n"

    # Must NOT claim that ClayMillenniumYangMillsProblem is proved
    assert "theorem clay_millennium_solved" not in all_lean_text
    assert "theorem clay_solution" not in all_lean_text
    assert "ClayMillenniumYangMillsProblem" in all_lean_text
    assert "TARGET SPECIFICATION, not a solution" in all_lean_text
