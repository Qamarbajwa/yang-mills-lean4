# PROJECT BINDING & REALITY POLICY (LAW 0)

- **Standard:** ROS v1.0 / Constitutional Law 0
- **Scope:** Execution Environment, Workspace Binding, Candidate Integrity
- **Target Project:** YANG_MILLS_MASS_GAP
- **Expected Repository Path:** d:/Comfy UI/yang mills and the mass gap

---

## 1. Constitutional Law 0 Statement

\\boxed{\\text{TASK\\_PROJECT\\_ID} = \\text{REPOSITORY\\_PROJECT\\_ID} = \\text{WORKSPACE\\_PROJECT\\_ID} = \\text{YANG\\_MILLS\\_MASS\\_GAP}}

Before any agent, tool, or process executes any mutating action, scientific experiment, test execution intended as evidence, review audit, acceptance evaluation, git commit, checkpoint sealing, or remote push: the identity of the task, the repository profile, and the active workspace directory must be verified.

---

## 2. Minimal Read-Only Discovery Exception

To establish identity, minimal read-only inspection of the local environment is strictly permitted and required:
1. Discover current working directory (pwd / Path.cwd()).
2. Discover Git root (git rev-parse --show-toplevel).
3. Read PROJECT_PROFILE.md and governance/project-governance.yaml to extract project.id.

No mutation, execution of non-inspection commands, candidate promotion, review generation, or git writing may occur until this discovery confirms that the workspace is bound to YM-MASS-GAP / YANG_MILLS_MASS_GAP.

---

## 3. Fail-Closed Mismatch Policy

If any of the following conditions occur:
- Active directory belongs to another project (e.g. d:/Comfy UI/revit mcp server or other external project).
- project.id in governance/project-governance.yaml is missing or mismatched.
- Git repository top-level does not match expected project path.
- Task ID does not belong to the governed Yang–Mills task graph.

The system MUST **FAIL CLOSED IMMEDIATELY**:
- Abort execution without making any file changes.
- Emit a formal PROJECT_IDENTITY_MISMATCH alert.
- Do not attempt cross-project execution or silent path redirections.

---

## 4. Immutable Scientific Candidate Identity

Every mathematical claim, lemma, theorem, or pathway candidate carries a deterministic fingerprint:

\\boxed{ \\text{Accepted Scientific State Valid} \\iff F_{\\rm scientific}^{\\rm audit} = F_{\\rm scientific}^{\\rm acceptance} }

Where {\\rm scientific}$ is computed over:
- Exact theorem statements and formal definitions.
- Derivations, proof texts, and formalization scripts.
- Canonical dependency tuples: (dependency_id, dependency_version, dependency_statement_hash).
- Cited source bundles: (source_id, source_version, source_content_hash, source_access_level).
- Associated pathway memory entries.

R3 adds discovery before hashing. Every discovered repository artifact is
classified by `governance/SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml` as
`SCIENTIFIC`, `PROVENANCE_CRITICAL`, `ADMINISTRATIVE`, `GENERATED`, or
`IGNORED_WITH_JUSTIFICATION`. `UNKNOWN` is terminal: a new research-shaped
file in `literature/`, `proofs/`, `derivations/`, or a research-named file
elsewhere fails closed. A `SCIENTIFIC` artifact is valid only when it is also
present in the canonical fingerprint manifest.

Post-E4 changes are strictly classified:
- NONE: Identical Git tree.
- ADMINISTRATIVE_ONLY: Modification strictly confined to review summaries, task graph status, contract ledger metadata, and checkpoint seals. Scientific tree hash is identical; E4 review remains valid.
- SCIENTIFIC_MATERIAL: Any change to scientific statements, proofs, dependencies, or source records. **E4 is marked STALE immediately and requires a fresh blind audit**.
