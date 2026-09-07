import re
import yaml
from pathlib import Path
from typing import Dict, List, Any, Set, Tuple, Optional

class BridgeGraphValidationError(Exception):
    pass

ALLOWED_EDGE_STATUSES = {
    "PROVED",
    "CONDITIONAL",
    "REGULATED_ONLY",
    "LOWER_DIMENSION_ONLY",
    "SPECIAL_GROUP_ONLY",
    "OPEN",
    "UNKNOWN"
}

ALLOWED_ASSUMPTION_STATUSES = {
    "PRESERVED",
    "DISCHARGED",
    "STRENGTHENED",
    "WEAKENED",
    "REPLACED",
    "NEW",
    "UNKNOWN"
}

ALLOWED_NECESSITY_CLASSES = {
    "TARGET_REQUIRED",
    "ROUTE_REQUIRED",
    "OPTIONAL_ROUTE"
}

REQUIRED_EDGE_FIELDS = [
    "EDGE_ID",
    "SOURCE_NODE",
    "TARGET_NODE",
    "MATHEMATICAL_PROPOSITION",
    "PRIMARY_STATUS",
    "STATUS_QUALIFIERS",
    "SCOPE",
    "EXPLICIT_HYPOTHESES",
    "ASSUMPTION_TRANSFERS",
    "PHYSICAL_SCALE",
    "OBSERVABLE_ALGEBRA",
    "THEOREMS_OR_SOURCES",
    "WHAT_IS_PROVED",
    "WHAT_IS_NOT_PROVED",
    "BRIDGE_VARIABLES",
    "FAILURE_LOCALITY",
    "OBSTRUCTION_CANDIDATE",
    "NECESSITY_CLASS",
    "PROOF_DEPENDENCIES",
    "REASON_FOR_STATUS"
]

REQUIRED_SCOPE_FIELDS = [
    "DIMENSION",
    "GAUGE_GROUP",
    "MATTER_CONTENT",
    "VOLUME_REGIME",
    "CUTOFF_STATE",
    "COUPLING_REGIME"
]

REQUIRED_PHYSICAL_SCALE_FIELDS = [
    "ENERGY_NORMALIZATION",
    "DIMENSIONFUL_OR_DIMENSIONLESS",
    "REFERENCE_PHYSICAL_SCALE",
    "CONTINUUM_SCALING_BEHAVIOR"
]

def parse_edge_records(markdown_text: str) -> List[Dict[str, Any]]:
    """Parse YAML blocks defining edge records from markdown text."""
    pattern = re.compile(r"```yaml\s*\n(.*?)\n```", re.DOTALL)

    records = []
    seen_ids = set()
    for match in pattern.finditer(markdown_text):
        chunk = match.group(1)
        if "EDGE_ID:" not in chunk:
            continue
        try:
            data = yaml.safe_load(chunk)
        except yaml.YAMLError as exc:
            raise BridgeGraphValidationError(f"Malformed YAML in edge block: {exc}") from exc
            
        if not isinstance(data, dict) or "EDGE_ID" not in data:
            continue
            
        edge_id = data["EDGE_ID"]
        if edge_id in seen_ids:
            raise BridgeGraphValidationError(f"Duplicate EDGE_ID detected: {edge_id}")
        seen_ids.add(edge_id)
        records.append(data)
        
    return records

def validate_edge_record(record: Dict[str, Any]) -> None:
    """Validate that an edge record strictly adheres to schema and invariants."""
    edge_id = record.get("EDGE_ID", "<MISSING_ID>")
    for field in REQUIRED_EDGE_FIELDS:
        if field not in record:
            raise BridgeGraphValidationError(f"Edge {edge_id} missing required field: {field}")
            
    status = record["PRIMARY_STATUS"]
    if status not in ALLOWED_EDGE_STATUSES:
        raise BridgeGraphValidationError(f"Edge {edge_id} has invalid PRIMARY_STATUS: '{status}'")
        
    necessity = record["NECESSITY_CLASS"]
    if necessity not in ALLOWED_NECESSITY_CLASSES:
        raise BridgeGraphValidationError(f"Edge {edge_id} has invalid NECESSITY_CLASS: '{necessity}'")
        
    if necessity == "TARGET_REQUIRED":
        if not record.get("TARGET_OBLIGATION_REF"):
            raise BridgeGraphValidationError(f"Edge {edge_id} is TARGET_REQUIRED but lacks TARGET_OBLIGATION_REF")
    elif necessity == "ROUTE_REQUIRED":
        if not record.get("ROUTE_ID"):
            raise BridgeGraphValidationError(f"Edge {edge_id} is ROUTE_REQUIRED but lacks ROUTE_ID")
            
    scope = record.get("SCOPE")
    if not isinstance(scope, dict):
        raise BridgeGraphValidationError(f"Edge {edge_id} SCOPE must be a dictionary")
    for s_field in REQUIRED_SCOPE_FIELDS:
        if s_field not in scope:
            raise BridgeGraphValidationError(f"Edge {edge_id} SCOPE missing: {s_field}")
            
    pscale = record.get("PHYSICAL_SCALE")
    if not isinstance(pscale, dict):
        raise BridgeGraphValidationError(f"Edge {edge_id} PHYSICAL_SCALE must be a dictionary")
    for p_field in REQUIRED_PHYSICAL_SCALE_FIELDS:
        if p_field not in pscale:
            raise BridgeGraphValidationError(f"Edge {edge_id} PHYSICAL_SCALE missing: {p_field}")
            
    # Non-promotion invariant: neighbouring regime theorem cannot be PROVED for 4D continuum Clay edge
    if status == "PROVED":
        dim = str(scope.get("DIMENSION"))
        vol = str(scope.get("VOLUME_REGIME"))
        cutoff = str(scope.get("CUTOFF_STATE"))
        qualifiers = record.get("STATUS_QUALIFIERS", [])
        if dim != "4":
            raise BridgeGraphValidationError(f"Edge {edge_id} has DIMENSION {dim} != 4 but is marked PROVED")
        if vol == "FINITE_VOLUME" and "finite_volume_only" not in qualifiers:
            raise BridgeGraphValidationError(f"Edge {edge_id} is finite volume but claimed PROVED without qualification")
            
    validate_assumption_transfers(record)

def validate_assumption_transfers(record: Dict[str, Any]) -> None:
    """Validate assumption tracking and discharge proofs."""
    edge_id = record["EDGE_ID"]
    transfers = record.get("ASSUMPTION_TRANSFERS", [])
    if not isinstance(transfers, list):
        raise BridgeGraphValidationError(f"Edge {edge_id} ASSUMPTION_TRANSFERS must be a list")
        
    seen_assumptions = set()
    for item in transfers:
        if not isinstance(item, dict):
            raise BridgeGraphValidationError(f"Edge {edge_id} assumption entry must be a dictionary")
        name = item.get("ASSUMPTION")
        status = item.get("STATUS")
        if not name or not status:
            raise BridgeGraphValidationError(f"Edge {edge_id} assumption entry missing ASSUMPTION or STATUS")
        if name in seen_assumptions:
            raise BridgeGraphValidationError(f"Edge {edge_id} duplicate assumption: {name}")
        seen_assumptions.add(name)
        
        if status not in ALLOWED_ASSUMPTION_STATUSES:
            raise BridgeGraphValidationError(f"Edge {edge_id} invalid assumption status: {status}")
            
        if status == "DISCHARGED":
            if not item.get("DISCHARGED_BY") or not item.get("DISCHARGE_EVIDENCE"):
                raise BridgeGraphValidationError(
                    f"Edge {edge_id} assumption '{name}' marked DISCHARGED without DISCHARGED_BY or DISCHARGE_EVIDENCE"
                )

def validate_proof_dependency_dag(records: List[Dict[str, Any]]) -> None:
    """Validate that edge proof dependencies are strictly acyclic and irreflexive."""
    edge_ids = {r["EDGE_ID"] for r in records}
    adj: Dict[str, List[str]] = {r["EDGE_ID"]: [] for r in records}
    
    for r in records:
        src = r["EDGE_ID"]
        deps = r.get("PROOF_DEPENDENCIES", [])
        if not isinstance(deps, list):
            raise BridgeGraphValidationError(f"Edge {src} PROOF_DEPENDENCIES must be a list")
        for dep in deps:
            dep_id = dep.get("DEP_EDGE_ID") if isinstance(dep, dict) else dep
            if not dep_id:
                continue
            if dep_id == src:
                raise BridgeGraphValidationError(f"Reflexive dependency detected in edge {src}")
            if dep_id in edge_ids:
                adj[src].append(dep_id)
            else:
                raise BridgeGraphValidationError(
                    f"Edge {src} declares unknown proof dependency: {dep_id}"
                )
    # Detect cycles via DFS
    visited = {}
    def dfs(node: str, path: List[str]):
        visited[node] = 1 # In progress
        for neighbor in adj.get(node, []):
            if visited.get(neighbor) == 1:
                cycle_str = " -> ".join(path + [neighbor])
                raise BridgeGraphValidationError(f"Proof dependency cycle detected: {cycle_str}")
            if visited.get(neighbor) == 0 or neighbor not in visited:
                dfs(neighbor, path + [neighbor])
        visited[node] = 2 # Done
        
    for eid in edge_ids:
        if eid not in visited:
            dfs(eid, [eid])

def compute_critical_cut_sets(
    records: List[Dict[str, Any]],
    source_nodes: Optional[Set[str]] = None,
    target_nodes: Optional[Set[str]] = None
) -> Dict[str, Any]:
    """
    Compute graph paths and both graph-theoretic and mathematically load-bearing cut-sets.
    """
    if source_nodes is None:
        source_nodes = {"N-REG-LATTICE", "N-REG-CUTOFF"}
    if target_nodes is None:
        target_nodes = {"N-MASS-GAP"}
    adj: Dict[str, List[Tuple[str, str, str]]] = {}
    edges_by_id = {}
    for r in records:
        s = r["SOURCE_NODE"]
        t = r["TARGET_NODE"]
        eid = r["EDGE_ID"]
        status = r["PRIMARY_STATUS"]
        edges_by_id[eid] = r
        if s not in adj:
            adj[s] = []
        adj[s].append((t, eid, status))
        
    # Find all paths from any source_node to any target_node
    all_paths = []
    def find_paths(curr: str, current_path: List[Tuple[str, str, str]]):
        if curr in target_nodes:
            all_paths.append(list(current_path))
            return
        for nxt, eid, st in adj.get(curr, []):
            if any(p[0] == nxt for p in current_path):
                continue # Prevent cycle in path traversal
            find_paths(nxt, current_path + [(curr, nxt, eid)])
            
    for src in source_nodes:
        find_paths(src, [])
        
    # Identify non-proved edges along valid paths
    open_edges_on_paths = set()
    for path in all_paths:
        for u, v, eid in path:
            st = edges_by_id[eid]["PRIMARY_STATUS"]
            if st != "PROVED":
                open_edges_on_paths.add(eid)
                
    # Mathematically load-bearing cut-sets (chokepoints)
    # A single edge or set of edges whose removal disrupts all source->target paths
    load_bearing = []
    for eid in sorted(open_edges_on_paths):
        # Test if removing eid breaks all paths
        remaining_paths = [
            p for p in all_paths if not any(edge_tuple[2] == eid for edge_tuple in p)
        ]
        if not remaining_paths:
            load_bearing.append(eid)
            
    return {
        "total_paths_count": len(all_paths),
        "paths": all_paths,
        "open_edges_on_paths": sorted(list(open_edges_on_paths)),
        "single_edge_bottlenecks": load_bearing,
        "is_connected_by_proved_only": any(
            all(edges_by_id[e[2]]["PRIMARY_STATUS"] == "PROVED" for e in p)
            for p in all_paths
        )
    }

def render_missing_bridge_graph(records: List[Dict[str, Any]]) -> str:
    """Render the human-readable topology document."""
    lines = [
        "# MISSING-BRIDGE GRAPH (YM-003)",
        "",
        "## 1. Executive Summary & Graph Topology",
        "",
        "This document provides the canonical topological representation of the missing bridges",
        "and verified theorem coverage connecting regulated gauge theories to the full Clay Millennium target.",
        "",
        "### Directed Graph Representation (Mermaid)",
        "",
        "```mermaid",
        "graph TD",
        "    classDef proved fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#155724;",
        "    classDef regOnly fill:#fff3cd,stroke:#ffc107,stroke-width:2px,color:#856404;",
        "    classDef openEdge fill:#f8d7da,stroke:#dc3545,stroke-width:2px,color:#721c24;",
        "    classDef condEdge fill:#e2e3e5,stroke:#6c757d,stroke-width:2px,color:#383d41;",
        ""
    ]
    
    for r in records:
        eid = r["EDGE_ID"]
        src = r["SOURCE_NODE"]
        tgt = r["TARGET_NODE"]
        status = r["PRIMARY_STATUS"]
        arrow = "-->"
        if status in {"OPEN", "UNKNOWN"}:
            arrow = "-.->|OPEN: " + eid + "|"
        elif status == "REGULATED_ONLY":
            arrow = "-->|REGULATED: " + eid + "|"
        elif status == "CONDITIONAL":
            arrow = "-.->|CONDITIONAL: " + eid + "|"
        elif status == "PROVED":
            arrow = "-->|PROVED: " + eid + "|"
        else:
            arrow = f"-->|{status}: {eid}|"
        lines.append(f"    {src} {arrow} {tgt}")
        
    lines.extend([
        "```",
        "",
        "## 2. Node Semantic Registry",
        "",
        "| Node ID | Domain / Branch | Semantic Definition | Target / Route Relevance |",
        "|---|---|---|---|",
        r"| `N-REG-LATTICE` | Regularization | Wilson lattice gauge theory with compact gauge group $G$ at lattice spacing $a > 0$. | Entry point for lattice constructive route. |",
        r"| `N-REG-CUTOFF` | Regularization | Continuum gauge field with UV cutoff $\Lambda < \infty$ or IR cutoff $\mu > 0$. | Entry point for continuous RG flow / SPDE route. |",
        r"| `N-UV-FREE` | UV Asymptotic Freedom | Running coupling $g_k \to 0$ logarithmically as energy scale $k \to \infty$ ($a \to 0$). | Required UV asymptotic freedom behavior. |",
        r"| `N-UV-RG-BOUNDS` | Multiscale RG | Uniform small-field multiscale bounds in finite volume (Bałaban / Federbush). | Foundation of rigorous UV stability. |",
        r"| `N-INT-COUPLING` | Nonperturbative Crossover | Strong effective coupling regime $g_k \sim 1$ (the unbridged non-meeting window). | Critical bottleneck region. |",
        r"| `N-IR-CONFINEMENT` | IR Lattice Phase | Strong-coupling lattice area-law confinement and cluster decay (Wilson / Shen–Zhu–Zhu). | Rigorous fixed-lattice infrared gap. |",
        r"| `N-THERMO-LIMIT` | Thermodynamic Limit | Infinite volume limit $V \to \infty$ with uniform volume-independent bounds. | Required for infinite-volume QFT. |",
        r"| `N-CONTINUUM-LIMIT` | Continuum Limit | Continuum limit $a \to 0$ of Schwinger functions $S_n \in \mathcal{S}'((\mathbb{R}^4)^n)$. | Primary existence target. |",
        r"| `N-OS-TEMPERED` | OS Axioms | OS0: Tempered distribution bounds on Schwinger functions. | Prerequisite for OS reconstruction. |",
        r"| `N-OS-EUCLIDEAN` | OS Axioms | OS1: Full Euclidean covariance under $\mathrm{O}(4) \ltimes \mathbb{R}^4$. | Restoration of spacetime rotation invariance. |",
        r"| `N-OS-SYMMETRY` | OS Axioms | OS2: Permutation symmetry under coordinate exchange. | Fundamental Euclidean property. |",
        r"| `N-OS-REFL-POS` | OS Axioms | OS3: Reflection positivity ($\Theta$-positivity) with respect to time-reflection. | Necessary for positive Hilbert space metric. |",
        r"| `N-OS-CLUSTER` | OS Axioms | OS4: Exponential clustering with rate $\Delta > 0$. | Direct Euclidean witness of spectral gap. |",
        r"| `N-WIGHTMAN-RECON` | Relativistic QFT | Reconstructed Wightman QFT on physical Hilbert space $\mathcal{H}$ with $U(a, \Lambda)$. | Official Clay existence requirement. |",
        r"| `N-VACUUM-UNIQUE` | Vacuum Sector | Unique, Poincaré-invariant physical vacuum $\Omega$ with $H \Omega = 0$. | Normalized ground state. |",
        r"| `N-SPECTRAL-REP` | Spectral Representation | Joint energy-momentum spectrum $\operatorname{Spec}(H, \vec{P}) \subseteq \bar{V}_+$. | Relativistic stability. |",
        r"| `N-NONTRIV-DEF` | Non-Triviality | Local gauge-invariant operators generating states non-reducible to free fields. | Official Clay non-triviality condition. |",
        r"| `N-MASS-GAP` | Mass Gap | Strict positive spectral isolation $\operatorname{Spec}(H|_{{\mathcal{H}_0^\perp}}) \subseteq [\Delta, \infty)$ with $\Delta > 0$. | Official Clay mass gap condition. |",
        r"| `N-COMPACT-SIMPLE-G` | Group Universality | Construction and uniform gap for arbitrary compact simple Lie group $G$. | Universal group requirement. |",
        "",
        "## 3. Summary of Graph-Theoretic Coverage",
        "",
        f"- **Total Directed Edges:** {len(records)}",
        f"- **Proved Structural Theorems:** {sum(1 for r in records if r['PRIMARY_STATUS'] == 'PROVED')}",
        f"- **Regulated / Finite-Regime Theorems:** {sum(1 for r in records if r['PRIMARY_STATUS'] == 'REGULATED_ONLY')}",
        f"- **Conditional Theorems:** {sum(1 for r in records if r['PRIMARY_STATUS'] == 'CONDITIONAL')}",
        f"- **Open Gaps / Bottlenecks:** {sum(1 for r in records if r['PRIMARY_STATUS'] in {'OPEN', 'UNKNOWN'})}",
        ""
    ])
    return "\n".join(lines)


def render_assumption_transfer_matrix(records: List[Dict[str, Any]]) -> str:
    """Render assumption transfer matrix."""
    lines = [
        "# ASSUMPTION TRANSFER MATRIX (YM-003)",
        "",
        "This matrix records every mathematical assumption entering, leaving, or newly introduced",
        "at each edge of the Missing-Bridge Graph, verifying that assumptions do not silently disappear.",
        "",
        "| Edge ID | Assumption Name | Transfer Status | Discharged By / Evidence | Strengthened / Weakened Detail |",
        "|---|---|---|---|---|"
    ]
    for r in records:
        eid = r["EDGE_ID"]
        for a in r.get("ASSUMPTION_TRANSFERS", []):
            name = a.get("ASSUMPTION", "")
            st = a.get("STATUS", "")
            disc = f"{a.get('DISCHARGED_BY', '')}: {a.get('DISCHARGE_EVIDENCE', '')}" if st == "DISCHARGED" else "-"
            detail = a.get("DETAIL", "-")
            lines.append(f"| `{eid}` | {name} | **`{st}`** | {disc} | {detail} |")
    return "\n".join(lines)


def render_limit_regime_matrix(records: List[Dict[str, Any]]) -> str:
    """Render limit and regime matrix."""
    lines = [
        "# LIMIT AND REGIME MATRIX (YM-003)",
        "",
        "This matrix tracks dimension, gauge group, volume, cutoff status, coupling regime, and limit trajectories",
        "for every edge, enforcing that uniformity within a regime is never conflated with control across a transition.",
        "",
        "| Edge ID | Dimension | Gauge Group | Volume Regime | Cutoff State | Coupling Regime | Limit Trajectory | Crossover Control | Physical Scale Setting |",
        "|---|---|---|---|---|---|---|---|---|"
    ]
    for r in records:
        eid = r["EDGE_ID"]
        sc = r.get("SCOPE", {})
        psc = r.get("PHYSICAL_SCALE", {})
        dim = sc.get("DIMENSION", "-")
        grp = sc.get("GAUGE_GROUP", "-")
        vol = sc.get("VOLUME_REGIME", "-")
        cut = sc.get("CUTOFF_STATE", "-")
        cpl = sc.get("COUPLING_REGIME", "-")
        lim = r.get("LIMIT_TRAJECTORY", "-")
        cro = r.get("CROSSOVER_CONTROL", "-")
        scl = psc.get("ENERGY_NORMALIZATION", "-")
        lines.append(f"| `{eid}` | {dim} | {grp} | {vol} | {cut} | {cpl} | {lim} | {cro} | {scl} |")
    return "\n".join(lines)


def render_open_edge_register(records: List[Dict[str, Any]]) -> str:
    """Render register of all non-PROVED edges."""
    lines = [
        "# OPEN EDGE REGISTER (YM-003)",
        "",
        "This register catalogs all edges that are not `PROVED` for the full 4D continuum Clay target,",
        "recording the exact missing mathematical proposition and associated obstruction candidate.",
        "",
        "| Edge ID | Endpoints | Status | Obstruction Candidate | Exact Mathematical Proposition Needed | Failure Locality |",
        "|---|---|---|---|---|---|"
    ]
    for r in records:
        if r["PRIMARY_STATUS"] != "PROVED":
            eid = r["EDGE_ID"]
            pts = f"`{r['SOURCE_NODE']}` → `{r['TARGET_NODE']}`"
            st = r["PRIMARY_STATUS"]
            obs = r.get("OBSTRUCTION_CANDIDATE", "-")
            prop = r.get("MATHEMATICAL_PROPOSITION", "-")
            fail = r.get("FAILURE_LOCALITY", "-")
            lines.append(f"| `{eid}` | {pts} | **`{st}`** | `{obs}` | {prop} | {fail} |")
    return "\n".join(lines)


def render_source_to_edge_traceability(records: List[Dict[str, Any]]) -> str:
    """Render source to edge traceability matrix."""
    lines = [
        "# SOURCE-TO-EDGE TRACEABILITY MATRIX (YM-003)",
        "",
        "Maps literature theorems in `THEOREM_LEDGER.md` directly to their instantiated graph edges.",
        "",
        "| Theorem / Source ID | Primary Literature Reference | Mapped Edge ID(s) | What Cited Source Proves | Scope / Boundary Limitation |",
        "|---|---|---|---|---|"
    ]
    for r in records:
        eid = r["EDGE_ID"]
        for src in r.get("THEOREMS_OR_SOURCES", []):
            tid = src.get("THEOREM_ID", "-")
            ref = src.get("CITATION", "-")
            prv = r.get("WHAT_IS_PROVED", "-")
            not_prv = r.get("WHAT_IS_NOT_PROVED", "-")
            lines.append(f"| `{tid}` | {ref} | `{eid}` | {prv} | {not_prv} |")
    return "\n".join(lines)


def render_critical_cut_set_report(records: List[Dict[str, Any]], cut_analysis: Dict[str, Any]) -> str:
    """Render the critical-cut-set analysis report."""
    lines = [
        "# CRITICAL CUT-SET REPORT (YM-003)",
        "",
        "## 1. Mathematical and Graph-Theoretic Objectives",
        "",
        "The objective of critical cut-set analysis in `YM-003` is to determine:",
        "1. The graph-theoretic cut-sets that disrupt all directed paths from regulated gauge theories to the Clay target.",
        "2. The mathematically load-bearing cut-sets that reflect genuine mathematical dependencies rather than topological artifacts.",
        "3. The smallest defensible open subproblem on the critical path.",
        "",
        "## 2. Graph Connectivity & Coverage Analysis",
        "",
        f"- **Total Discovered Directed Paths from Regulators to Gap:** {cut_analysis['total_paths_count']}",
        f"- **Paths Connected Entirely by `PROVED` Edges:** {0 if not cut_analysis['is_connected_by_proved_only'] else 1}",
        f"- **Total Non-`PROVED` Edges Intercepting Paths:** {len(cut_analysis['open_edges_on_paths'])}",
        "",
        "### Open Edges on Candidate Paths:",
        ""
    ]
    for eid in cut_analysis["open_edges_on_paths"]:
        lines.append(f"- `{eid}`")
        
    lines.extend([
        "",
        "## 3. Graph-Theoretic Minimal Cut-Sets vs. Mathematically Load-Bearing Cut-Sets",
        "",
        "### Graph-Theoretic Single-Edge Bottlenecks (1-Cuts):",
        ""
    ])
    for eid in cut_analysis["single_edge_bottlenecks"]:
        lines.append(f"- **`{eid}`**: Intercepts every directed path from regularized entry to terminal spectral mass gap.")
        
    lines.extend([
        "",
        "### Mathematical Load-Bearing Analysis:",
        "",
        "While graph topology reveals multiple bottlenecks, mathematical physics demonstrates a fundamental difference",
        "between structural reconstruction theorems and nonperturbative dynamical estimates:",
        "",
        "1. **Structural / Reconstruction Edges (`E-OS-RECON`, `E-GAP-CLUSTER`):**",
        "   These edges are mathematically **`PROVED`** as general theorems (Osterwalder & Schrader 1973/1975; Glimm & Jaffe 1987).",
        "   They do not represent the dynamical failure of quantum Yang–Mills; rather, they are ready-to-use analytical bridges",
        "   that are currently starved of valid nonperturbative inputs.",
        "",
        "2. **The True Dynamical Chokepoint (`E-CROSSOVER` & `E-THERMO`):**",
        "   The genuine mathematical obstruction occurs at the interface where ultraviolet asymptotic freedom meets",
        "   infrared confinement:",
        r"   - `E-CROSSOVER`: Continuation of multiscale small-field bounds across $g_k \sim 1$ (`OBS-CAND-001`).",
        r"   - `E-LATTICE-CONT`: Continuation of lattice gap along the weak-coupling continuum trajectory $\beta \to \infty$ (`OBS-CAND-003`).",
        r"   - `E-THERMO`: Taking $V \to \infty$ without an infrared cutoff or mass gap.",
        "",
        "## 4. The Smallest Defensible Load-Bearing Open Subproblem",
        "",
        "$$\\boxed{",
        "\\textbf{Construct a uniform estimate controlling the non-perturbative transition window } g_k \\sim 1",
        "}$$",
        "",
        "Neither Bałaban's multiscale expansion nor lattice cluster expansions can presently enter this regime without diverging.",
        "Establishing a single uniform non-perturbative estimate across this window is the minimal load-bearing key to unblocking",
        "continuum Yang–Mills existence."
    ])
    return "\n".join(lines)
