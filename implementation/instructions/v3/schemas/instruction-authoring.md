# Instruction Authoring (v3)

This document explains what an AU-SYS **Instruction** is, where it sits in the v3 hierarchy, and how to author instruction artefacts that conform to `docs/implementation/instructions/v3/schemas/instruction-authoring.schema.json`.

## What An Instruction Is

An Instruction is a **sequenced work unit**.

- It translates protocols into a concrete set of steps.
- It declares inputs/outputs so execution is auditable.
- It declares a controlled `action` so orchestrators can apply safety rules.

An instruction is not a prompt template; it describes *what must be done*, not *exactly what messages to send*.

## Where Instruction Sits In The Hierarchy

```text
Doctrine  (mcp.doctrine/v1)      -> Principles + policies (non-executable)
  |
  v
Protocol  (mcp.protocol/v1)      -> Enforceable directives + conflicts + verification
  |
  v
Instruction (mcp.instruction/v1) -> Sequenced work unit (steps, inputs/outputs, action gating)
  |
  v
Prompt    (mcp.prompt/v1)        -> LLM invocation template (messages, arguments, output contract)
```

Key rule: instructions MUST declare which doctrine/protocol set they operate under so review and enforcement are not guesswork.

## Instruction File Shape (Authoring Envelope)

Instructions use the standard v3 authoring envelope:

- `authoring_schema_version`: AU-SYS authoring schema version (SemVer)
- `mcp_spec_revision`: MCP revision this authoring format is aligned to (informational but enforceable)
- `artifact`: the instruction itself

Inside `artifact`:

- `artifact.meta`: identity + controlled `action`
- `artifact.content`: governance refs + steps + IO contract
- `artifact.governance` (optional): owners + lifecycle
- `artifact.traceability` (optional): migration/audit fields

## Required Fields

`artifact.meta` MUST include:

- `version`
- `schema`: fixed value `mcp.instruction/v1`
- `id`: canonical instruction id (pattern `^[a-z0-9_.:-]+$`)
- `title`
- `action`: one of `read|plan|create-file|modify-files|validate|refactor|execute|halt`

`artifact.content` exists (required at the `artifact` level). Most of its fields are optional, but practical instructions should declare refs and steps.

## Content Fields (Execution Contract)

`artifact.content` may include:

- `doctrine_refs` (string[]): doctrine ids that govern this instruction
- `protocol_refs` (string[]): protocol ids that constrain execution
- `directives` (string[]): directive keys to apply (should correspond to protocol directives)
- `inputs` (string[]): required context/resources (paths, ids, artefacts)
- `outputs` (string[]): artefacts produced by execution
- `steps` (array): ordered steps
- `variables` (object): template variables used during execution
- `halt` (boolean): pause after completion pending explicit operator authorization
- `notes` (string[]): clarifications

### Steps

`steps[]` supports either:

- a string (simple step text)
- an object with:
  - `id` (required)
  - `description` (required)
  - `requires` (optional string[])
  - `produces` (optional string[])

Prefer object steps for anything you want to validate automatically.

## Minimal Example

```yaml
authoring_schema_version: 1.0.0
mcp_spec_revision: "2025-11-25"

artifact:
  meta:
    version: 1.0.0
    schema: mcp.instruction/v1
    id: au-sys.instruction.update-mcp-prompt-schema
    title: Align prompt schema to MCP 2025-11-25
    action: modify-files
    tags: ["mcp", "schemas", "governance"]

  content:
    doctrine_refs: ["au-sys.doctrine.safe-repo-changes"]
    protocol_refs: ["au-sys.protocol.github-safety"]
    directives: ["GIT-001", "GIT-002"]
    inputs:
      - "docs/implementation/instructions/v3/schemas/prompt-schema.json"
      - "docs/implementation/instructions/reference_repos/modelcontextprotocol/docs/specification/2025-11-25/server/prompts.mdx"
    outputs:
      - "Updated prompt-schema.json aligned to MCP 2025-11-25"
    steps:
      - id: STEP-001
        description: Compare current schema to MCP prompts spec content types and metadata.
      - id: STEP-002
        description: Update schema for icons + image/audio/resource content types.
      - id: STEP-003
        description: Update annotations priority to number 0..1.
      - id: STEP-004
        description: Add docs describing prompt authoring.
    halt: false

  governance:
    owners: ["au-sys"]
    status: draft
    changeLog: ["Initial instruction scaffold"]
```

## References

- Schema: `docs/implementation/instructions/v3/schemas/instruction-authoring.schema.json`
- Protocol docs (layer above): `docs/implementation/instructions/v3/schemas/protocol-authoring.md`
- Prompt schema (layer below): `docs/implementation/instructions/v3/schemas/prompt-schema.json`
