# Quick Start - v3 Artefact Authoring

Canonical v3 standard:

- `docs/implementation/instructions/v3/MCP_PROMPTS_CANONICAL.md`

This is a v3-only quick start. Legacy v2 runner templates were moved to:

- `docs/implementation/instructions/v3/_archive/QUICK_START_legacy_v2_style_20260121.md`

## The Five v3 Artefacts

- Doctrine (`mcp.doctrine/v1`): policies
- Protocol (`mcp.protocol/v1`): directives
- Instruction (`mcp.instruction/v1`): executable steps
- Prompt (`mcp.prompt/v1`): MCP-aligned message templates
- Runbook (`mcp.runbook/v1`): orchestration glue

Optional support artefact:

- Prompt registry (`mcp.prompt-registry/v1`): a repo-local index of prompts
- Governance registries:
  - Doctrine registry (`mcp.doctrine-registry/v1`)
  - Protocol registry (`mcp.protocol-registry/v1`)
  - Instruction registry (`mcp.instruction-registry/v1`)

## Rules You Must Follow

- Operational artefacts are YAML-only (`.yaml`) and must be a single YAML document.
- Do not put the operational meaning in large `|` blocks; use structured fields.
- `mcp_spec_revision` MUST be `"2025-11-25"`.

## Validate Against Schemas

Schemas:

- `docs/implementation/instructions/v3/schemas/doctrine-authoring.schema.json`
- `docs/implementation/instructions/v3/schemas/protocol-authoring.schema.json`
- `docs/implementation/instructions/v3/schemas/instruction-authoring.schema.json`
- `docs/implementation/instructions/v3/schemas/prompt-schema.json`
- `docs/implementation/instructions/v3/schemas/prompt-registry.schema.json`
- `docs/implementation/instructions/v3/schemas/doctrine-registry.schema.json`
- `docs/implementation/instructions/v3/schemas/protocol-registry.schema.json`
- `docs/implementation/instructions/v3/schemas/instruction-registry.schema.json`
- `docs/implementation/instructions/v3/schemas/runbook-authoring.schema.json`

How you validate is tooling-dependent. One practical option is `check-jsonschema` (supports YAML inputs if `pyyaml` is installed):

```bash
python -m pip install check-jsonschema pyyaml
check-jsonschema --schemafile docs/implementation/instructions/v3/schemas/runbook-authoring.schema.json your.runbook.yaml
```

Repo-local validator:

```bash
python -m pip install pyyaml jsonschema
python tooling/au-sys-tools/tools/validate_v3_mcp_artifacts.py --root docs/implementation/instructions/v3
```

Strict mode (recommended in CI once registries are adopted):

```bash
python tooling/au-sys-tools/tools/validate_v3_mcp_artifacts.py --root docs/implementation/instructions/v3 --enforce-registry-completeness
```

Generate registries + catalogue:

```bash
python -m pip install pyyaml
python tooling/au-sys-tools/tools/generate_v3_mcp_registries.py
```

Catalogue entrypoint:

- `docs/implementation/instructions/v3/catalogue.yaml`

## Minimal Templates (Copy/Paste)

### 1) Doctrine

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
    tags: []
  content:
    purpose: "Define universal operating policies."
    scope: ["repo://*"]
    policies: []
    protocols: []
    enforce: true
    notes: []
```

### 2) Protocol

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
    tags: []
  content:
    related_doctrine: "enterprise.execution"
    applies_to: ["repo://*"]
    directives: []
    inputs: []
    outputs: []
    notes: []
    conflicts: []
```

### 3) Instruction

```yaml
authoring_schema_version: "1.0.0"
mcp_spec_revision: "2025-11-25"
artifact:
  meta:
    version: "1.0.0"
    schema: "mcp.instruction/v1"
    id: "implementation.session"
    title: "Implementation Session"
    description: "Execute a scoped implementation session against a spec."
    action: "execute"
    tags: []
  content:
    doctrine_refs: ["enterprise.execution"]
    protocol_refs: ["validation.golden_rule"]
    directives: []
    inputs: ["spec_path"]
    outputs: ["changes", "validation_results"]
    steps:
      - id: "prepare"
        description: "Read spec and identify next task."
      - id: "implement"
        description: "Implement the next task (minimal diff)."
      - id: "validate"
        description: "Run checks required by the protocol(s)."
    halt: true
    notes: []
```

### 4) Prompt

Use this for model message templates. Prompts are not policies; they must declare governance.

```yaml
authoring_schema_version: "1.0.0"
mcp_spec_revision: "2025-11-25"
artifact:
  meta:
    version: "1.0.0"
    schema: "mcp.prompt/v1"
    id: "plan.from_spec"
    name: "plan-from-spec"
    title: "Plan from spec"
    description: "Generate a step-by-step implementation plan from a spec."
    tags: ["plan"]
    icons: []
  content:
    governed_by:
      doctrine_refs: ["enterprise.execution"]
      protocol_refs: ["validation.golden_rule"]
      directive_refs: []
    mode: "plan_only"
    halt: true
    arguments:
      - name: "spec_path"
        description: "Repo-relative path to the spec document"
        required: true
        type: "string"
    template:
      messages:
        - role: "user"
          content:
            type: "text"
            text: "Read {{spec_path}} and propose an implementation plan. Then halt."
    output_contract:
      format: "markdown"
      required_sections: ["Plan", "Open Questions"]
    notes: []
    conflicts: []
```

### 5) Runbook

Runbooks sequence instructions and/or prompts.

Example runbooks in-repo:

- `docs/implementation/instructions/v3/examples/runbook_v3_implementation_session.yaml`
- `docs/implementation/instructions/v3/examples/runbook_code_implementation_session.yaml`

```yaml
authoring_schema_version: "1.0.0"
mcp_spec_revision: "2025-11-25"
artifact:
  meta:
    version: "1.0.0"
    schema: "mcp.runbook/v1"
    id: "au-sys.runbook.example"
    title: "Example Runbook"
    description: "Orchestrate planning + execution under governance."
    tags: ["example"]
  content:
    governed_by:
      doctrine_refs: ["enterprise.execution"]
      protocol_refs: ["validation.golden_rule"]
    workflow:
      - id: "spec"
        type: "spec_refs"
        spec_refs: ["docs/implementation/in_progress/your_spec.md"]
      - id: "plan"
        type: "execute_prompt"
        prompt_ref: "plan-from-spec"
        arguments:
          spec_path: "docs/implementation/in_progress/your_spec.md"
      - id: "execute"
        type: "execute_instruction"
        instruction_ref: "implementation.session"
        inputs: ["spec_path=docs/implementation/in_progress/your_spec.md"]
      - id: "halt"
        type: "halt"
        reason: "Await operator input"
  halt: true
```
