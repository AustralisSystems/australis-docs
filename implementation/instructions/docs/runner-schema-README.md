Runner Prompt Schema & Validation

Files created:
- `runner-prompt-schema.json` - JSON Schema for runner prompts
- `runner-prompt-schema.yaml` - YAML view of the schema
- `tools/validate_mcp_prompt.py` - Validator CLI (requires PyYAML and jsonschema)
- `tests/test_validate_prompts.py` - Pytest test that validates existing prompts

How to run:

1. Install dev deps (recommended):
   pip install pyyaml jsonschema pytest

2. Validate all prompts:
   python tools/validate_mcp_prompt.py docs/implementation/instructions/v2/prompts

3. Run tests:
   pytest -q

Notes:
- The runner schema is intentionally lightweight and maps the common fields used in our prompts.
- The authoritative MCP schema (for tools/messages) is available at `docs/implementation/instructions/docs/mcp-schema-2025-11-25.json`.
