# Protocol Authoring (v3)

This document explains what an AU-SYS **Protocol** is, where it sits in the v3 instruction hierarchy, and how to author protocol artefacts that conform to `docs/implementation/instructions/v3/schemas/protocol-authoring.schema.json`.

## What A Protocol Is

A Protocol is the **enforcement layer** between doctrine intent and execution.

- It turns doctrine policies into **testable directives**.
- It defines conflicts and verification guidance.
- It is still **non-executable** (no step sequences; no prompt templates).

Protocols are intended to be stable enough to govern many instructions/prompts, but more concrete than doctrines.

## Where Protocol Sits In The Hierarchy

```text
Doctrine  (mcp.doctrine/v1)     -> Principles + policies (non-executable)
  |
  v
Protocol  (mcp.protocol/v1)     -> Enforceable directives + conflicts + verification
  |
  v
Instruction (mcp.instruction/v1)-> Sequenced work unit (steps, inputs/outputs, action gating)
  |
  v
Prompt    (mcp.prompt/v1)       -> LLM invocation template (messages, arguments, output contract)
```

Key rule: protocols **MUST** be traceable to doctrine intent. If the protocol introduces a new constraint, it should be justified by a doctrine policy or an explicit governance decision.

## Protocol File Shape (Authoring Envelope)

Protocols use the standard v3 authoring envelope:

- `authoring_schema_version`: AU-SYS authoring schema version (SemVer)
- `mcp_spec_revision`: MCP revision this authoring format is aligned to (informational but enforceable)
- `artifact`: the protocol itself

Inside `artifact`:

- `artifact.meta`: identity + enforcement toggle
- `artifact.content`: directives + applicability + conflicts
- `artifact.governance` (optional): owners + lifecycle
- `artifact.traceability` (optional): migration/audit fields

## Required Fields

`artifact.meta` MUST include:

- `version`: protocol document version
- `schema`: fixed value `mcp.protocol/v1`
- `id`: canonical protocol id (pattern `^[a-z0-9_.:-]+$`)
- `title`: short display name
- `description`: what the protocol governs
- `enforce`: if true, violations are blocking unless explicitly waived

`artifact.content` exists (required at the `artifact` level) and typically includes directives.

## Content Fields (Operational Meaning)

`artifact.content` may include:

- `related_doctrine` (string): doctrine id this protocol supports/implements
- `applies_to` (string[]): paths/domains this protocol governs (recommended)
- `directives` (object[]): the core of a protocol; structured requirements
- `inputs` (string[]): required context that must exist when applying the protocol
- `outputs` (string[]): expected artefacts produced when following the protocol
- `conflicts` (object[]): known incompatibilities requiring explicit resolution
- `notes` (string[]): clarifications

### Directives

Each directive is a structured object with:

- `id` (required): stable identifier for cross-referencing (instructions/prompts should reference this)
- `level` (required): `required|recommended|warning|optional`
- `statement` (required): phrased as a testable requirement
- `rationale` (optional): why it exists
- `verification` (optional): how to confirm compliance

Directive statements should be single-purpose and measurable ("Do X" / "Do not Y" / "Always Z").

## Governance And Traceability

`artifact.governance` (optional)
- `owners` (string[]): responsible parties
- `status`: `draft|review|approved|deprecated`
- `changeLog` (string[]): “what changed and why”

`artifact.traceability` (optional)
- `raw`: embedded original content (use sparingly)
- `raw_ref`: URI or repo path to source
- `raw_hash`: SHA-256 hex digest

## Minimal Example

```yaml
authoring_schema_version: 1.0.0
mcp_spec_revision: "2025-11-25"

artifact:
  meta:
    version: 1.0.0
    schema: mcp.protocol/v1
    id: au-sys.protocol.github-safety
    title: Git Safety Protocol
    description: Guardrails for non-destructive git operations in automation.
    enforce: true
    tags: ["git", "safety", "repo"]

  content:
    related_doctrine: au-sys.doctrine.safe-repo-changes
    applies_to:
      - "**/*"
    directives:
      - id: GIT-001
        level: required
        statement: Never use force-push, history rewrite, or hard reset unless explicitly requested.
        rationale: Prevent irreversible loss of work and audit trail.
        verification: Check executed commands for --force, reset --hard, rebase -i.
      - id: GIT-002
        level: required
        statement: Do not commit secrets or credential files.
        verification: Review staged files for .env, credentials.json, private keys.

  governance:
    owners: ["au-sys"]
    status: draft
    changeLog: ["Initial protocol scaffold"]
```

## References

- Schema: `docs/implementation/instructions/v3/schemas/protocol-authoring.schema.json`
- Doctrine docs (layer above): `docs/implementation/instructions/v3/schemas/doctrine-authoring.md`
- Instruction schema (layer below): `docs/implementation/instructions/v3/schemas/instruction-authoring.schema.json`
