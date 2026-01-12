# MCP Runner Prompt Best Practices

Summary of key rules and patterns when authoring runner prompts (for this repo):

- Use the canonical runner prompt schema (`runner-prompt-schema.json`) for validation.
- Required fields: `version`, `schema`, `id`, `title`, `action`.
- Use `id` values that are lowercase, contain only alphanumerics, hyphen, underscore, colon, or dot (e.g., `001-read-fastapi-platform`).
- Keep `raw` field as the verbatim source for traceability when appropriate; for large or sensitive originals prefer `raw_ref` with a `raw_hash` for integrity.
- Use `raw_ref` to reference large or sensitive raw content stored externally (URI or repo path). Include `raw_hash` (SHA-256 hex) when possible for integrity verification.
- When embedding original content in `raw`, ensure sensitive values are redacted; validators will warn if secret-like tokens are detected.
- Use `variables` for templates; define `required` and `default` where applicable.
- `halt: true` indicates the prompt must pause after reading; do not continue automatically.
- `steps` should be explicit, single-action sentences and follow the repo's “one item at a time” directive.
- Preserve original directives and contradictions in `notes` and escalate to the operator for resolution.
- When copying/adapting code, follow the session gating: single-file edit → lint/tests → record evidence → request approval.
- Maintain attribution and licensing when copying examples from cloned repositories (see `docs/index.yaml` for source details).

## Validation & CI
- Use `python tools/validate_mcp_prompt.py docs/implementation/instructions/v2/prompts` to validate all runner prompts.
- Add new prompts only after they validate and include `raw` content for traceability.

## MCP references
- The authoritative MCP JSON schema is saved in `docs/implementation/instructions/docs/mcp-schema-2025-11-25.json`.
- Use the MCP schema for tool/message validation when mapping runner prompts to MCP tools.
