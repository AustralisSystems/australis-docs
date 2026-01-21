# MCP Prompt Authoring (v3)

This document explains the AU-SYS **MCP prompt authoring** format, which is a near-direct representation of MCP prompt structures. It conforms to `docs/implementation/instructions/v3/schemas/mcp-prompt-authoring.schema.json`.

Use this schema when you want to author prompts in a shape that maps 1:1 with MCP `prompts/list` + `prompts/get` data, with minimal AU-SYS wrapping.

## What This Schema Represents

- A single MCP prompt definition (`prompt.meta`) and its message template (`prompt.template`).
- Optional AU-SYS governance metadata (`prompt.governance`).

This schema is aligned to MCP Prompts spec revision `2025-11-25`.

## Fields

Top-level:

- `authoring_schema_version`: AU-SYS schema version (SemVer)
- `mcp_spec_revision`: fixed `2025-11-25`
- `prompt`: the MCP-aligned prompt object

`prompt.meta`:

- `name` (required): MCP prompt name (kebab-case)
- `title` (optional, recommended)
- `description` (optional, recommended)
- `icons` (optional): icon objects with `src` and optional `mimeType`, `sizes`, `theme`
- `arguments` (optional): list of MCP `PromptArgument`

`prompt.template`:

- `description` (optional): maps to `prompts/get.result.description`
- `messages` (required): MCP `PromptMessage[]`

`prompt.template.messages[].content` supports MCP content types:

- `text`
- `image`
- `audio`
- `resource` (embedded resource with `uri`, `mimeType`, and either `text` or `blob`)

All content types can carry `annotations` (`audience`, `priority` 0..1, `lastModified`).

## When To Prefer AU-SYS `prompt-schema.json`

If you need any of the following, use `docs/implementation/instructions/v3/schemas/prompt-schema.json` instead:

- explicit governance linkage (`governed_by.doctrine_refs` / `protocol_refs` / `directive_refs`)
- safety gating (`mode`, `halt`)
- output contracts (`output_contract`)
- traceability (`artifact.traceability`)

The MCP authoring schema is best treated as a *wire-format authoring* or *import/export* format.

## Minimal Example

```yaml
authoring_schema_version: 1.0.0
mcp_spec_revision: "2025-11-25"

prompt:
  meta:
    name: code-review
    title: Request Code Review
    description: Asks the LLM to analyze code quality and suggest improvements.
    arguments:
      - name: code
        description: The code to review
        required: true
  template:
    description: Code review prompt
    messages:
      - role: user
        content:
          type: text
          text: |
            Please review this code:

            {{code}}
          annotations:
            priority: 1
  governance:
    owners: ["au-sys"]
    status: draft
```

## References

- Schema: `docs/implementation/instructions/v3/schemas/mcp-prompt-authoring.schema.json`
- MCP Prompts spec (reference copy): `docs/implementation/instructions/reference_repos/modelcontextprotocol/docs/specification/2025-11-25/server/prompts.mdx`
