MCP Instructions — Doctrine, Protocols, Instructions (Three-tier design)

Purpose
-------
This document describes the three-tier MCP prompt design we use for the
`docs/implementation/instructions/v2` material: **Doctrine → Protocols → Instructions**.
These YAML files should conform to the JSON Schemas saved in this folder.

Tiers
-----
1. Doctrine (mcp.doctrine/v1)
   - High-level, non-code, organizational rules that define enterprise goals
     and canonical execution policies. Example: "000-DOCTRINE-Enterprise_Canonical_Execution".
   - Fields: `id`, `title`, `description`, `purpose`, `scope`, `policies`, `protocols`, `enforce`.
   - Usage: One or more doctrine files act as top-level anchors for the protocol
     documents and instruction sets. Doctrine files are normative and should be
     referenced by `protocols` and `instructions`.

2. Protocol (mcp.protocol/v1)
   - Mid-level prescriptive rules that define how to carry out parts of the doctrine.
     Examples: Zero Tolerance Remediation, FastAPI Implementation Protocols.
   - Fields: `id`, `title`, `description`, `enforce`, `directives`, `inputs`, `outputs`.
   - Usage: Protocols are referenced by instructions; they may be enforced (blocking)
     or advisory.

3. Instruction (mcp.instruction/v1)
   - Operational runner prompts (the instructions that agents or humans execute).
     These are procedural and mapped to runner prompt YAMLs.
   - Fields: `id`, `title`, `description`, `action`, `doctrine_ref`, `protocol_refs`,
     `steps`, `variables`, `halt`.
   - Usage: An instruction file is the unit of execution — it should be single-purpose,
     gated, and explicit. Respect `halt` semantics and the "single-file, sequential" directive.

Schema files
------------
- `doctrine-schema.json` / `.yaml` — JSON Schema + YAML view for doctrine files
- `protocol-schema.json` / `.yaml` — Protocol schema
- `instruction-schema.json` / `.yaml` — Instruction schema

Validation
----------
- Use the validator script to validate any YAML against the proper schema.
- Each YAML must include a `schema` property indicating which schema to use
  (e.g., `schema: "mcp.doctrine/v1"`).

raw* properties usage
---------------------
- `raw` (optional): embed original or extended content directly in the YAML when small and non-sensitive; useful for one-file traceability.
- `raw_ref` (optional): preferred for large or sensitive originals — a URI or repo path referencing the raw content.
- `raw_hash` (optional): SHA-256 hex digest of the raw content; recommended when using `raw_ref` for integrity verification.
- Validators will emit a WARNING if none of `raw`, `raw_ref`, or `raw_hash` are present, and will emit warnings if `raw` appears to contain secret-like tokens.
- For governance, prefer `raw_ref` + `raw_hash` in production doctrine/protocol/instruction files to avoid embedding sensitive material.


Examples
--------
A simple protocol YAML might look like:

```yaml
version: "1.0"
schema: "mcp.protocol/v1"
id: "002-protocol-zero_tolerance_remediation"
title: "Zero Tolerance Remediation"
description: "All TODOs/mocks/stubs/pass placeholders must be eradicated from production code."
enforce: true
directives:
  - "no_todos"
  - "no_mocks_in_prod"
notes:
  - "Blocking enforcement — any violation halts progress."
```

Governance notes
----------------
- Doctrine files are authoritative; changes to doctrine should be reviewed carefully.
- If a protocol conflicts with doctrine, the conflict must be resolved and documented.
- Instructions must not create new doctrine or protocol-level invariants without review.

Files created in this folder
---------------------------
- `doctrine-schema.json` / `.yaml`
- `protocol-schema.json` / `.yaml`
- `instruction-schema.json` / `.yaml`
- `mcp-instructions-README.md` (this file)
- `validate_instruction_schemas.py` (validator; created alongside schema files)

Contact
-------
If you propose changes to the three-tier schemas or the governance model, create a
proposal and attach it to the CODE_IMPLEMENTATION_SPEC for review.
