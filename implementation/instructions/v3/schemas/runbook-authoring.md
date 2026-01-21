# Runbook Authoring (v3)

This document explains the AU-SYS **Runbook** artefact and how it replaces the v2 “combined” YAML that glued together doctrine + protocols + execution directives + instructions.

The runbook schema is: `docs/implementation/instructions/v3/schemas/runbook-authoring.schema.json`.

## What A Runbook Is

A Runbook is an **orchestration wrapper**.

- It declares the governing doctrine/protocol set.
- It references SPEC documents.
- It defines an ordered workflow that points at instruction artefacts and/or prompt artefacts.

Runbooks are deliberately *not* policy sources. They are “how to run” wiring.

## Why This Exists (Mapping From v2)

In v2, a single YAML often contained:

- `READ_AND_ACKNOWLEDGE` doctrine + protocols
- `DIRECTIVE` / `DIRECTIVES`
- `CODE_IMPLEMENTATION_SPEC` references
- `READ_AND_EXECUTE` / `LOAD_AND_EXECUTE` instruction file names

That is useful operationally, but it mixes:

- governance (doctrine/protocol)
- execution sequencing (instruction/runbook)
- model invocation templates (prompts)

v3 keeps these separate, and the runbook becomes the “glue” artefact.

## Runbook File Shape

Top level:

- `authoring_schema_version` (SemVer)
- `mcp_spec_revision` (enforced: `2025-11-25`)
- `artifact`

Inside `artifact`:

- `artifact.meta` (required): identity + title/description
- `artifact.content` (required): governance linkage + workflow
- `artifact.governance` (optional): owners/status
- `artifact.traceability` (optional): migration/audit fields

## Governance Linkage

`artifact.content.governed_by` MUST include:

- `doctrine_refs` (>= 1)

It MAY include:

- `protocol_refs`
- `directive_refs`

## Workflow

`artifact.content.workflow[]` is an ordered list of steps.

Supported step `type` values:

- `acknowledge`: legacy-friendly structure for “read and acknowledge” lists
- `spec_refs`: references SPEC documents used in this run
- `directives`: freeform operational directives for this run
- `remember`: reminders (non-binding guidance)
- `execute_instruction`: points to an instruction artefact
- `execute_prompt`: points to a prompt artefact (maps naturally to MCP prompts)
- `halt`: explicit stop point

Semantics:

- Use `execute_instruction` + `instruction_ref` for instruction artefacts (`mcp.instruction/v1`).
- Use `execute_prompt` + `prompt_ref` for prompt artefacts (`mcp.prompt/v1`).
- Do not mix these. If a legacy v2 "instruction" file is actually a message template, migrate it to a v3 prompt.

## Practical Guidance

- Put *policy* in doctrine/protocol artefacts.
- Put *message templates* in prompt artefacts.
- Put *sequenced execution* in instruction artefacts.
- Put *“what do we run today”* in the runbook.

If your legacy “instruction” is actually a model prompt template (like many v2 `INSTRUCTIONS-*.yaml` files with a big `instruction: |` block), represent it as a v3 prompt and reference it via `execute_prompt`.

## Minimal Example

```yaml
authoring_schema_version: "1.0.0"
mcp_spec_revision: "2025-11-25"

artifact:
  meta:
    version: "1.0.0"
    schema: "mcp.runbook/v1"
    id: "au-sys.runbook.code-implementation"
    title: Code Implementation Session Runbook
    description: Combine doctrine + protocols + spec + execution prompts for a governed implementation session.

  content:
    governed_by:
      doctrine_refs: ["000-DOCTRINE-Enterprise_Canonical_Execution"]
      protocol_refs:
        - "001-PROTOCOL-The_GoldenRule_Execution"
        - "002-PROTOCOL-Zero_Tolerance_Remediation"
    variables:
      spec_directory: "docs/implementation/in_progress"
      spec_extension: ".md"
    workflow:
      - type: acknowledge
        acknowledge:
          doctrine: "000-DOCTRINE-Enterprise_Canonical_Execution"
          protocols:
            - "001-PROTOCOL-The_GoldenRule_Execution"
      - type: spec_refs
        spec_refs: ["docs/implementation/in_progress/2026-01-21-CODE_IMPLEMENTATION_SPEC.md"]
      - type: directives
        directives:
          - "No mass modifications"
          - "Implement one step at a time"
      - type: execute_prompt
        prompt_ref: "plan-from-spec"
        inputs: ["Continue with the current CODE_IMPLEMENTATION_SPEC"]
      - type: execute_instruction
        instruction_ref: "104-INSTRUCTIONS-Execute_Implementation_Phase_Tasks"
        inputs: ["Continue with the current CODE_IMPLEMENTATION_SPEC"]
      - type: halt
        reason: "Await operator instruction"
```

## References

- Schema: `docs/implementation/instructions/v3/schemas/runbook-authoring.schema.json`
- Protocol schema: `docs/implementation/instructions/v3/schemas/protocol-authoring.schema.json`
- Instruction schema: `docs/implementation/instructions/v3/schemas/instruction-authoring.schema.json`
- Prompt schema: `docs/implementation/instructions/v3/schemas/prompt-schema.json`
