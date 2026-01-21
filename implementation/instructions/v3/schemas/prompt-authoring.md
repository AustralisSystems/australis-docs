# Prompt Authoring (v3)

This document explains how AU-SYS authors **Prompt artefacts** that conform to `docs/implementation/instructions/v3/schemas/prompt-schema.json`.

The AU-SYS prompt schema is designed to:

- map cleanly to MCP `prompts/list` and `prompts/get` objects (MCP Prompts spec revision `2025-11-25`)
- preserve AU-SYS governance, traceability, and safe-execution metadata

## What A Prompt Is

A Prompt is an **LLM invocation template**.

- It defines message templates (role + typed content blocks).
- It declares arguments (parameters) that can be provided at invocation time.
- It may declare an output contract so results are testable.

Unlike doctrines and protocols, prompts are closer to the model and change more often.

## Where Prompt Sits In The Hierarchy

```text
Doctrine  -> Protocol  -> Instruction  -> Prompt
```

Key rule: prompts MUST NOT invent policy. They must declare which doctrine/protocol set governs them (`artifact.content.governed_by`).

## Prompt File Shape (Authoring Envelope)

Top-level fields:

- `authoring_schema_version`: AU-SYS authoring schema version (SemVer)
- `mcp_spec_revision`: must be `2025-11-25` (alignment target)
- `artifact`: prompt content + governance metadata

Within `artifact`:

- `artifact.meta`: stable identity and discovery metadata
- `artifact.content`: governance refs + arguments + message template + safety mode
- `artifact.governance` (optional): owners + lifecycle
- `artifact.traceability` (optional): migration/audit fields

## Mapping To MCP

This schema is *authoring-aligned* to MCP:

- MCP `Prompt` (as returned by `prompts/list`) maps from `artifact.meta`:
  - `name` <= `artifact.meta.name`
  - `title` <= `artifact.meta.title`
  - `description` <= `artifact.meta.description`
  - `icons` <= `artifact.meta.icons`
  - `arguments` <= `artifact.content.arguments`

- MCP `prompts/get` maps from `artifact.content.template`:
  - `result.description` <= `artifact.content.template.description`
  - `result.messages[]` <= `artifact.content.template.messages[]`

AU-SYS-only fields (`governed_by`, `mode`, `halt`, `output_contract`, etc.) are intended for orchestrators and review tooling.

## Required Fields

`artifact.meta` MUST include:

- `version`
- `schema`: fixed value `mcp.prompt/v1`
- `id`: canonical id for governance/traceability
- `name`: external prompt name used for discovery/invocation (kebab-case)
- `title`
- `description`

`artifact.content` MUST include:

- `governed_by.doctrine_refs` (>= 1)
- `arguments` (may be empty)
- `template.messages` (>= 1)
- `mode`

## Content Blocks (MCP-aligned)

Each message has `role` (`user` or `assistant`) and `content` (typed).

Supported `content.type` values (aligned to MCP 2025-11-25):

- `text` with `text`
- `image` with `data` (base64) and `mimeType`
- `audio` with `data` (base64) and `mimeType`
- `resource` with `resource` (embedded resource containing `uri`, `mimeType`, and either `text` or `blob`)

All content types may include `annotations`:

- `audience` (string[])
- `priority` (number 0..1)
- `lastModified` (string)

## Safety Mode

`artifact.content.mode` is AU-SYS specific:

- `read_only`: do analysis, no mutations
- `plan_only`: propose changes, do not apply
- `validate_only`: run checks/tests, do not change files
- `execute`: allowed to make changes
- `halt`: emit a stop response (used for guardrails)

`artifact.content.halt: true` is a stronger operational latch: even if other parts of the system chain prompts, this one must stop the pipeline after it runs.

## Minimal Example

```yaml
authoring_schema_version: 1.0.0
mcp_spec_revision: "2025-11-25"

artifact:
  meta:
    version: 1.0.0
    schema: mcp.prompt/v1
    id: au-sys.prompt.code-review
    name: code-review
    title: Request Code Review
    description: Ask the model to review a diff and propose improvements.
    tags: ["review", "quality"]
    icons:
      - src: https://example.com/review-icon.svg
        mimeType: image/svg+xml
        sizes: ["any"]

  content:
    governed_by:
      doctrine_refs: ["au-sys.doctrine.safe-repo-changes"]
      protocol_refs: ["au-sys.protocol.github-safety"]
      directive_refs: ["GIT-002"]
    mode: plan_only
    halt: false
    arguments:
      - name: diff
        description: Git diff to review
        required: true
        type: string
    template:
      description: Code review prompt
      messages:
        - role: user
          content:
            type: text
            text: |
              Please review the following diff and propose improvements.

              {{diff}}
          annotations:
            priority: 0.8
    output_contract:
      format: markdown
      required_sections: ["Findings", "Suggested Changes", "Risks"]

  governance:
    owners: ["au-sys"]
    status: draft
    changeLog: ["Initial prompt scaffold"]
```

## References

- Schema: `docs/implementation/instructions/v3/schemas/prompt-schema.json`
- MCP Prompts spec (reference copy): `docs/implementation/instructions/reference_repos/modelcontextprotocol/docs/specification/2025-11-25/server/prompts.mdx`
