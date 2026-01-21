# Doctrine Authoring (v3)

This document explains what an AU-SYS **Doctrine** is, where it sits in the v3 instruction hierarchy, and how to author doctrine artefacts that conform to `docs/implementation/instructions/v3/schemas/doctrine-authoring.schema.json`.

## What A Doctrine Is

A Doctrine is the **highest-level, non-executable authority layer** in the AU-SYS instruction stack.

- It defines *why* a set of constraints exist (intent, values, scope).
- It expresses governing **policies** at a human-auditable level.
- It does **not** define step sequences, workflows, or model message templates.

Doctrines are designed to be stable: protocols, instructions, and prompts may evolve faster, but they should remain traceable back to the doctrine(s) they implement.

## Where Doctrine Sits In The Hierarchy

The v3 hierarchy is intentionally layered so that enforcement and execution do not drift from stated intent:

```text
Doctrine  (mcp.doctrine/v1)  ->  Principles + policies (non-executable)
  |
  v
Protocol  (mcp.protocol/v1)  ->  Enforceable directives + conflicts + verification guidance
  |
  v
Instruction (mcp.instruction/v1) -> Sequenced work unit (steps, inputs/outputs, action gating)
  |
  v
Prompt    (mcp.prompt/v1)    -> LLM invocation template (messages, arguments, output contract)
```

Key rule: **lower layers MUST NOT invent policy**. They must declare which doctrine(s) they are operating under and implement them via protocols and directives.

## Doctrine File Shape (Authoring Envelope)

The doctrine artefact uses the same v3 authoring envelope as the other MCP-tier artefacts:

- `authoring_schema_version`: version of AU-SYS authoring schema (SemVer).
- `mcp_spec_revision`: MCP revision this authoring format is aligned to (informational but enforceable).
- `artifact`: the doctrine itself.

Inside `artifact`, the schema splits identity from content:

- `artifact.meta`: stable identity + discoverability
- `artifact.content`: doctrine meaning (purpose, policies, scope)
- `artifact.governance` (optional): lifecycle metadata (owners, status)
- `artifact.traceability` (optional): migration/audit fields

## Required Fields

`artifact.meta` is required and MUST include:

- `version`: doctrine document version (SemVer string).
- `schema`: fixed value `mcp.doctrine/v1`.
- `id`: canonical doctrine identifier (pattern `^[a-z0-9_.:-]+$`).
- `title`: short human-readable name.
- `description`: concise statement of intent and scope.

`artifact.content` exists (required at the `artifact` level), but most of its fields are optional so doctrines can start minimal and grow over time.

## Content Fields (What Doctrine Actually Says)

`artifact.content` may include:

- `purpose` (string): high-level rationale / business intent.
- `scope` (string[]): where this doctrine applies (repo paths, domains, modules, products).
- `policies` (object[]): non-executable policy statements derived from the doctrine.
- `protocols` (string[]): IDs of protocol artefacts that operationalise this doctrine.
- `enforce` (boolean): whether violations are blocking unless explicitly waived.
- `notes` (string[]): clarifications, commentary, governance notes.

### Policies

Each policy entry is a structured object with:

- `id` (required): unique within the doctrine.
- `title` (required)
- `description` (optional): full explanation and rationale.
- `severity` (optional): `blocking|high|medium|low|informational` (default `blocking`).
- `verification` (optional): how a reviewer/tool confirms compliance.

Policies should be phrased so that protocols can translate them into testable directives.

## Governance And Traceability

These blocks exist to support controlled evolution and auditing:

`artifact.governance` (optional)
- `owners` (string[]): responsible parties.
- `status`: `draft|review|approved|deprecated`.
- `changeLog` (string[]): human-readable “what changed and why”.

`artifact.traceability` (optional)
- `raw`: embedded source content (use sparingly).
- `raw_ref`: URI or repo path to source.
- `raw_hash`: SHA-256 hex digest of the source.

## Authoring Guidance (Practical)

- Doctrines should remain **non-executable**: no step lists, no tool calls, no model instructions.
- Prefer fewer, clearer policies over many overlapping ones; keep each policy single-purpose.
- Use `protocols` to explicitly link operational enforcement to doctrine intent.
- Use `scope` to prevent accidental “global” policies that silently apply everywhere.

## Minimal Example

```yaml
authoring_schema_version: 1.0.0
mcp_spec_revision: "2025-11-25"

artifact:
  meta:
    version: 1.0.0
    schema: mcp.doctrine/v1
    id: au-sys.doctrine.safe-repo-changes
    title: Safe Repo Changes
    description: Guardrails for making non-destructive, auditable changes to repositories.
    tags: ["repo", "safety", "governance"]

  content:
    purpose: Ensure changes are reviewable, reversible, and do not destroy history.
    scope:
      - "**/*"
    policies:
      - id: SAFE-001
        title: Avoid destructive git operations
        description: Do not force-push, rewrite history, or delete without explicit approval.
        severity: blocking
        verification: Check commands and git history for force, reset --hard, mass deletes.
    protocols:
      - au-sys.protocol.github-safety
    enforce: true

  governance:
    owners: ["au-sys"]
    status: draft
    changeLog: ["Initial doctrine scaffold"]
```

## References

- Schema: `docs/implementation/instructions/v3/schemas/doctrine-authoring.schema.json`
- Protocol schema (next layer down): `docs/implementation/instructions/v3/schemas/protocol-authoring.schema.json`
