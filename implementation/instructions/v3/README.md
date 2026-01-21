# Instruction System v3 (MCP Prompts)

Canonical v3 standard:

- `docs/implementation/instructions/v3/MCP_PROMPTS_CANONICAL.md`

This directory defines AU-SYS v3 "MCP prompts" as a governed, schema-validated set of artefacts.

## Artefacts

AU-SYS v3 uses a three-tier hierarchy:

- Doctrine (Tier 1): foundational, non-task-specific rules
- Protocol (Tier 2): enforceable directives and validation rules
- Instruction (Tier 3): executable workflows (steps)

Additional v3 artefacts:

- Prompt: MCP-aligned prompt templates (`mcp.prompt/v1`)
- Runbook: orchestration glue that sequences instructions and/or prompts (`mcp.runbook/v1`)
- Prompt registry: repo-local index of prompts (`mcp.prompt-registry/v1`)
 - Doctrine/protocol/instruction registries: repo-local indices of governance artefacts

Catalogue:

- `docs/implementation/instructions/v3/catalogue.yaml` is the single entrypoint to all registry files.

## Non-negotiables (v3)

- Operational artefacts are YAML-only (`.yaml`) and must be a single YAML document.
- No "YAML + free text after" in v3 artefacts.
- Operational meaning lives in structured fields; large `|` blocks are traceability only.
- `mcp_spec_revision` is pinned to `"2025-11-25"`.

## Schemas

Author against these schemas:

- Catalogue: `docs/implementation/instructions/v3/schemas/catalogue.schema.json`
- Doctrine: `docs/implementation/instructions/v3/schemas/doctrine-authoring.schema.json`
- Protocol: `docs/implementation/instructions/v3/schemas/protocol-authoring.schema.json`
- Instruction: `docs/implementation/instructions/v3/schemas/instruction-authoring.schema.json`
- Prompt (repo-governed, MCP-aligned): `docs/implementation/instructions/v3/schemas/prompt-schema.json`
- Prompt (wire-aligned export): `docs/implementation/instructions/v3/schemas/mcp-prompt-authoring.schema.json`
- Prompt registry (repo-local index): `docs/implementation/instructions/v3/schemas/prompt-registry.schema.json`
- Doctrine registry: `docs/implementation/instructions/v3/schemas/doctrine-registry.schema.json`
- Protocol registry: `docs/implementation/instructions/v3/schemas/protocol-registry.schema.json`
- Instruction registry: `docs/implementation/instructions/v3/schemas/instruction-registry.schema.json`
- Runbook: `docs/implementation/instructions/v3/schemas/runbook-authoring.schema.json`

Related docs:

- `docs/implementation/instructions/v3/QUICK_START.md`
- `docs/implementation/instructions/v3/schemas/runbook-authoring.md`

Examples:

- `docs/implementation/instructions/v3/examples/runbook_v3_implementation_session.yaml`
- `docs/implementation/instructions/v3/examples/runbook_code_implementation_session.yaml`

Tooling:

- Generate registries + catalogue: `python tooling/au-sys-tools/tools/generate_v3_mcp_registries.py`
- Validate (optionally strict): `python tooling/au-sys-tools/tools/validate_v3_mcp_artifacts.py --root docs/implementation/instructions/v3 --enforce-registry-completeness`

Legacy v2 material (kept for audit/migration only):

- `docs/implementation/instructions/v3/_archive/`

## Minimal, Schema-Shaped Examples

These are intentionally small and should validate against the schemas.

### Doctrine

```yaml
authoring_schema_version: "1.0.0"
mcp_spec_revision: "2025-11-25"
artifact:
  meta:
    version: "1.0.0"
    schema: "mcp.doctrine/v1"
    id: "enterprise.execution"
    title: "Enterprise Execution Doctrine"
    description: "Non-negotiable operating rules for AU-SYS agents."
    tags: ["execution", "safety"]
  content:
    purpose: "Provide enforceable operating policies."
    scope: ["repo://*"]
    policies:
      - id: "no-yaml-trailing-text"
        title: "Single YAML document"
        description: "v3 artefacts must not include free text after YAML."
        severity: "blocking"
        verification: "Reject files that are not a single YAML document."
    protocols: []
    enforce: true
    notes: []
```

### Protocol

```yaml
authoring_schema_version: "1.0.0"
mcp_spec_revision: "2025-11-25"
artifact:
  meta:
    version: "1.0.0"
    schema: "mcp.protocol/v1"
    id: "validation.golden_rule"
    title: "Golden Rule Validation Protocol"
    description: "Enforce a consistent validation workflow."
    enforce: true
    tags: ["validation"]
  content:
    related_doctrine: "enterprise.execution"
    applies_to: ["repo://*"]
    directives:
      - id: "capture-evidence"
        level: "required"
        statement: "Capture evidence for validations run."
        rationale: "Ensures changes are auditable and repeatable."
        verification: "Provide command + relevant output excerpts."
    inputs: []
    outputs: []
    notes: []
    conflicts: []
```

### Instruction

```yaml
authoring_schema_version: "1.0.0"
mcp_spec_revision: "2025-11-25"
artifact:
  meta:
    version: "1.0.0"
    schema: "mcp.instruction/v1"
    id: "implementation.single_file_fix"
    title: "Single File Fix"
    action: "modify-files"
    tags: ["implementation"]
  content:
    doctrine_refs: ["enterprise.execution"]
    protocol_refs: ["validation.golden_rule"]
    directives: ["capture-evidence"]
    inputs: ["target_file", "acceptance_criteria"]
    outputs: ["diff", "validation_results"]
    steps:
      - id: "edit"
        description: "Apply the minimal required edit to target_file."
      - id: "validate"
        description: "Run required checks and capture evidence."
    halt: true
    notes: []
```

### Prompt (MCP-aligned)

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
    description: "Read the listed files and halt."
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
    conflicts: []
```

### Runbook (Orchestration)

```yaml
authoring_schema_version: "1.0.0"
mcp_spec_revision: "2025-11-25"
artifact:
  meta:
    version: "1.0.0"
    schema: "mcp.runbook/v1"
    id: "au-sys.runbook.code-implementation"
    title: "Code Implementation Session"
    description: "Orchestrate a governed implementation session."
    tags: ["implementation"]
  content:
    governed_by:
      doctrine_refs: ["enterprise.execution"]
      protocol_refs: ["validation.golden_rule"]
    workflow:
      - type: "spec_refs"
        spec_refs: ["docs/implementation/in_progress/your_spec.md"]
      - type: "execute_instruction"
        instruction_ref: "implementation.single_file_fix"
        inputs: ["target_file=src/app.py"]
      - type: "halt"
        reason: "Await operator input"
  halt: true
```
