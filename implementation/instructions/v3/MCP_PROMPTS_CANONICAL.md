# AU-SYS v3 MCP Prompts Canonical Standard

This document is the canonical standard for *all* v3 AU-SYS "MCP prompts" artefacts.

In AU-SYS terminology, "MCP prompts" refers to the v3 three-tier hierarchy:

- Tier 1: Doctrine
- Tier 2: Protocol
- Tier 3: Instruction

Additionally, v3 defines MCP-aligned task prompt templates ("Prompt") and optional orchestration ("Runbook").

The v2 pattern of placing almost all content inside large `instruction: |` / `raw: |` blocks is not permitted in v3 (except for traceability).

---

## Non-Negotiables

- File format: YAML only (`.yaml`).
- MCP reference: align to MCP Prompts spec revision `2025-11-25`.
- Schema validation: every v3 YAML file MUST validate against its corresponding JSON Schema.
- Structure-first: the operational content MUST be expressed as structured YAML key/value fields; freeform blocks are traceability only.
- No "YAML + free text after": v3 files are a single YAML document only.

---

## Canonical v3 Schemas

These schemas are authoritative for v3 authoring:

- Doctrine: `docs/implementation/instructions/v3/schemas/doctrine-authoring.schema.json`
- Protocol: `docs/implementation/instructions/v3/schemas/protocol-authoring.schema.json`
- Instruction: `docs/implementation/instructions/v3/schemas/instruction-authoring.schema.json`

Task prompt templates (MCP-aligned):

- Prompt (AU-SYS governed, MCP-aligned): `docs/implementation/instructions/v3/schemas/prompt-schema.json`
- Prompt (wire-aligned authoring export): `docs/implementation/instructions/v3/schemas/mcp-prompt-authoring.schema.json`

Optional orchestration glue:

- Runbook: `docs/implementation/instructions/v3/schemas/runbook-authoring.schema.json`

Note: `prompt-schema.json` is the canonical "prompt" authoring format inside this repo because it enforces governance (`governed_by.*_refs`), safety mode, and output contracts while remaining mappable to MCP Prompts `2025-11-25`.

---

## Required Authoring Envelope (All v3 artefacts)

Every v3 artefact uses the same authoring envelope:

- `authoring_schema_version`: semver string (e.g., `"1.0.0"`)
- `mcp_spec_revision`: MUST be `"2025-11-25"`
- `artifact.meta`: identity and human-facing metadata
- `artifact.content`: structured operational content
- optional `artifact.governance`: ownership/lifecycle metadata
- optional `artifact.traceability`: legacy linkage

The `artifact.meta.schema` field MUST use the fixed identifier for its type:

- Doctrine: `mcp.doctrine/v1`
- Protocol: `mcp.protocol/v1`
- Instruction: `mcp.instruction/v1`
- Prompt: `mcp.prompt/v1`
- Runbook: `mcp.runbook/v1`

---

## Content Rules (Prevent v2-Style Raw Blocks)

### Rule 1: Structured-first

The core payload must be structured:

- Doctrine MUST use `artifact.content.policies[]` for enforceable statements.
- Protocol MUST use `artifact.content.directives[]` for enforceable directives.
- Instruction MUST use `artifact.content.steps[]` for executable workflow steps.
- Prompt MUST use `artifact.content.template.messages[]` with MCP-aligned `content` blocks.

### Rule 2: Freeform text is traceability only

The only acceptable places for large freeform text are:

- `artifact.traceability.raw` (small excerpts only)
- `artifact.traceability.raw_ref` + `artifact.traceability.raw_hash` (preferred)

Operational intent MUST NOT live primarily inside `traceability.raw`.

### Rule 3: No duplicate policy text

If the same mandates appear in multiple artefacts, they belong in a Doctrine and are referenced by:

- prompts/runbooks: `governed_by.doctrine_refs`
- instructions: `content.doctrine_refs`
- protocols: `content.related_doctrine`

Do not paste the entire mandate repeatedly across protocols/instructions.

---

## MCP Prompt Alignment Details (2025-11-25)

For v3 "Prompt" artefacts:

- `artifact.meta.icons` is supported.
- `template.messages[].content` supports content types:
  - `text`
  - `image`
  - `audio`
  - `resource`
- `annotations.priority` is a number in the range `[0..1]`.

Preferred annotation placement:

- Prefer `content.annotations` (per MCP) rather than `message.annotations`.

---

## Naming and Identifiers

### Canonical IDs

- `artifact.meta.id` MUST be lowercase and stable.
- Use characters matching the schema patterns (safe characters only).

### Prompt names

- `artifact.meta.name` (for Prompt artefacts) is the discovery/invocation key.
- Use kebab-case and keep it stable across versions.

---

## Size and Modularity (Practical Caps)

Line length:

- Target 100 characters/line; hard cap 120.
- Exception: unavoidable long URLs/hashes can exceed (keep them isolated on their own line).

File size soft/hard caps:

- Doctrine: 150-250 soft, 350-400 hard
- Protocol: 200-350 soft, 500 hard
- Instruction: 150-300 soft, 450 hard
- Prompt: 30-80 soft, 150 hard
- Runbook: 30-120 soft, 200 hard

Split rules:

- If an artefact needs 3+ major themes, split it into multiple artefacts and reference them.
- If a Prompt `content.text` grows beyond ~2,000-3,500 chars, move bulk content into a `resource` block or a referenced repo file and keep the prompt itself concise.

---

## Minimal Templates

These are minimal, schema-shaped templates (examples only).

### Doctrine (Tier 1)

```yaml
authoring_schema_version: "1.0.0"
mcp_spec_revision: "2025-11-25"
artifact:
  meta:
    version: "1.0.0"
    schema: "mcp.doctrine/v1"
    id: "enterprise.execution"
    title: "Enterprise Execution Doctrine"
    description: "How the agent must operate (non-task-specific)."
    tags: ["execution", "safety"]
  content:
    purpose: "Provide non-negotiable operating rules."
    scope: ["repo://*"]
    policies:
      - id: "no-speculation"
        title: "No guessing"
        description: "Do not guess; request minimum missing info."
        severity: "blocking"
        verification: "Review outputs for unsupported claims."
    protocols: []
    enforce: true
    notes: []
```

### Protocol (Tier 2)

```yaml
authoring_schema_version: "1.0.0"
mcp_spec_revision: "2025-11-25"
artifact:
  meta:
    version: "1.0.0"
    schema: "mcp.protocol/v1"
    id: "validation.golden_rule"
    title: "Golden Rule Validation Protocol"
    description: "Validation workflow and enforceable directives."
    enforce: true
    tags: ["validation"]
  content:
    related_doctrine: "enterprise.execution"
    applies_to: ["repo://*"]
    directives:
      - id: "follow-workflow"
        level: "required"
        statement: "Follow the required workflow stages."
        rationale: "Prevents hallucination and unsafe changes."
        verification: "Evidence includes commands and outputs."
    inputs: []
    outputs: []
    notes: []
    conflicts: []
```

### Instruction (Tier 3)

```yaml
authoring_schema_version: "1.0.0"
mcp_spec_revision: "2025-11-25"
artifact:
  meta:
    version: "1.0.0"
    schema: "mcp.instruction/v1"
    id: "implementation.single_file_fix"
    title: "Single File Fix"
    description: "Modify one file, validate, then stop for approval."
    action: "modify-files"
    tags: ["implementation"]
  content:
    doctrine_refs: ["enterprise.execution"]
    protocol_refs: ["validation.golden_rule"]
    directives: ["follow-workflow"]
    inputs: ["target_file", "acceptance_criteria"]
    outputs: ["diff", "validation_results"]
    steps:
      - id: "edit"
        description: "Apply the minimal change to the target file."
      - id: "validate"
        description: "Run the required validations and capture evidence."
    halt: true
    notes: []
```

### Prompt (MCP-aligned task prompt)

```yaml
authoring_schema_version: "1.0.0"
mcp_spec_revision: "2025-11-25"
artifact:
  meta:
    version: "1.0.0"
    schema: "mcp.prompt/v1"
    id: "read.platform_docs"
    name: "read-platform-docs"
    title: "Read platform docs"
    description: "Read the listed files and stop."
    tags: ["read"]
    icons: []
  content:
    governed_by:
      doctrine_refs: ["enterprise.execution"]
      protocol_refs: ["validation.golden_rule"]
      directive_refs: []
    mode: "read_only"
    halt: true
    arguments:
      - name: "files"
        description: "Repo-relative paths to read"
        required: true
        type: "json"
    template:
      messages:
        - role: "user"
          content:
            type: "text"
            text: "Read these files: {{files}}. Then halt."
    output_contract:
      format: "markdown"
      required_sections: ["Findings", "Open Questions"]
    notes: []
```

---

## Migration Note (v2 -> v3)

During migration, it is acceptable to preserve v2 raw text for auditing, but only under `artifact.traceability.*`. The v3 operational meaning MUST be represented in the structured `artifact.content` fields.
