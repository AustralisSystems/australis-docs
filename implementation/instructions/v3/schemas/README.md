# v3 Schemas

Canonical v3 standard:

- `docs/implementation/instructions/v3/MCP_PROMPTS_CANONICAL.md`

This directory contains the **canonical v3 schema set** in `docs/implementation/instructions/v3/schemas/`.

These schemas implement the AU-SYS v3 authoring envelope:

* `authoring_schema_version`
* `mcp_spec_revision`
* `artifact.meta`
* `artifact.content`
* optional `artifact.governance`
* optional `artifact.traceability`

Links (as provided):

* Doctrine: [https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/doctrine-authoring.schema.json](https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/doctrine-authoring.schema.json)
* Protocol: [https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/protocol-authoring.schema.json](https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/protocol-authoring.schema.json)
* Instruction: [https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/instruction-authoring.schema.json](https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/instruction-authoring.schema.json)
* Prompt: [https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/prompt-schema.json](https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/prompt-schema.json)
* Prompt registry: [https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/prompt-registry.schema.json](https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/prompt-registry.schema.json)
* Doctrine registry: [https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/doctrine-registry.schema.json](https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/doctrine-registry.schema.json)
* Protocol registry: [https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/protocol-registry.schema.json](https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/protocol-registry.schema.json)
* Instruction registry: [https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/instruction-registry.schema.json](https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/instruction-registry.schema.json)
* Catalogue: [https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/catalogue.schema.json](https://github.com/AustralisSystems/au-sys-docs/blob/master/implementation/instructions/v3/schemas/catalogue.schema.json)

Below is a **verbose “what it is / what it’s for / how to use it”** breakdown, plus the **small schema hardening tweaks** I’d recommend for v3.1 (because your v3 set is *very* close to production-grade).

---

## 1) Doctrine authoring schema

**File:** `doctrine-authoring.schema.json`
**Role in the system:** the *top-level authority layer*.

### What a Doctrine is

A Doctrine is the **non-executable “why” layer**. It defines the values, intent, and high-level governing positions your system must obey. It is where you put:

* *purpose* (“why this exists”)
* *scope* (“where this applies”)
* *policies* (“what is mandatory / expected”), with severity and verification guidance
* *protocols list* (“these protocols implement this doctrine”)
* optional enforce toggle and commentary

### What your schema already does well

* **Strong identity block** (`artifact.meta`) with `schema = "mcp.doctrine/v1"`, `id`, `title`, `description`, `version`, `tags`.
* **Policies are structured** objects with:

  * `id`, `title`, optional `description`
  * `severity` enum (blocking/high/…)
  * `verification` guidance
* Doctrine does not pretend to be executable (good separation from Instruction).

### Recommended v3.1 hardening

1. Make `content.policies` **optional but encourage** it; if present, require `description` (right now only `id` and `title` are required per policy).
2. Consider requiring `content.enforce` at doctrine level, or document that enforcement *defaults* are derived from Protocol.

---

## 2) Protocol authoring schema

**File:** `protocol-authoring.schema.json`
**Role in the system:** the *enforceable rule bundle* sitting under Doctrine.

### What a Protocol is

A Protocol is the operational translation of doctrine into enforceable constraints. It answers:

* what must be enforced (`enforce: true/false`)
* what rules exist (`directives[]`)
* where it applies (`applies_to`)
* what it expects to consume/produce (`inputs[]`, `outputs[]`)
* what conflicts exist and how to resolve them (`conflicts[]`)
* what doctrine it’s attached to (`related_doctrine`)

### What your schema already does well

* `meta.enforce` is **required** (excellent for governance clarity).
* `directives` are **structured objects** (id, level, statement, rationale, verification) — this is the single biggest upgrade over “string directives”.
* `conflicts[]` exists as a first-class concept (your future self will thank you).

### Recommended v3.1 hardening

1. Constrain `content.related_doctrine` to a pattern (same pattern as `meta.id`) so it’s not free text.
2. Consider making `content.directives` required when `meta.enforce=true` (otherwise you can have “enforced protocols” with no actual enforceable directives).

---

## 3) Instruction authoring schema

**File:** `instruction-authoring.schema.json`
**Role in the system:** the *executable sequencing layer*.

### What an Instruction is

An Instruction is a single executable unit of work (or a tightly scoped workflow), designed to be:

* orchestrated
* safely gated
* governed by doctrine/protocol
* auditable and repeatable

It answers:

* what kind of action this is (`meta.action`)
* what it needs (`inputs`, `variables`)
* what it will do (`steps`)
* what it produces (`outputs`)
* what it’s governed by (`doctrine_refs`, `protocol_refs`)
* whether it must stop (`halt`)

### What your schema already does well

* `action` is a strict enum (read/plan/create-file/modify-files/validate/refactor/execute/halt). This is excellent for deterministic orchestration.
* `steps` supports either:

  * simple strings (fast authoring)
  * or structured step objects (`id`, `description`, plus `requires` and `produces`)
* `variables` supports a clean “parameter metadata map”.

### Recommended v3.1 hardening

1. Make `content.doctrine_refs` and/or `content.protocol_refs` **required** (right now they’re optional). Practically, instructions should always be governed.
2. Add a rule: if `meta.action="execute"` or `"modify-files"`, then require `content.halt` to be explicitly present (even if false). That forces conscious safety decisions.
3. Constrain `variables` values so `default` has a sane schema (right now `"default": {}` is overly permissive in JSON Schema terms).

---

## 4) Prompt schema

**File:** `prompt-schema.json`
**Role in the system:** the *LLM invocation contract layer*.

### What a Prompt is

A Prompt is the standardised “invocation template” you expose to an LLM agent (and, if you implement MCP server prompts later, this maps cleanly to `prompts/list` metadata and `prompts/get` messages).

It answers:

* what this prompt is called (`meta.name`) and how it’s identified (`meta.id`)
* what it’s for (`meta.title`, `meta.description`)
* what parameters it accepts (`content.arguments`)
* what governance constrains it (`content.governed_by`)
* what operational safety mode it uses (`content.mode` + `content.halt`)
* what message templates it injects (`content.template.messages[]`)
* what output structure is required (`content.output_contract`)

### What your schema already does well

* **Governance is mandatory**: `content.governed_by.doctrine_refs` is required with `minItems: 1`.
* `mode` enum is explicit and useful (`read_only`, `plan_only`, `validate_only`, `execute`, `halt`).
* The template structure is solid:

  * messages are role-based (user/assistant)
  * message content is typed (`text`, `image`, `audio`, `resource`)
  * annotations support priority/audience metadata
* `output_contract` is optional but present, which is exactly right for predictable agent output.

### Recommended v3.1 hardening

1. Add a consistency constraint:

   * if `mode="halt"` then `halt` must be `true`
   * if `mode="plan_only"` then `halt` should default to `true` (or require an explicit override)
2. Prompt schema alignment note: `prompt-schema.json` is already aligned to MCP `2025-11-25` and supports `meta.icons` and content types `text`, `image`, `audio`, and `resource`.

---

# How these four schemas fit together (the intended workflow)

This is the clean “authoring + enforcement” chain your v3 folder now supports:

1. **Doctrine** defines principles and policy intent
2. **Protocol** defines enforceable directives (with levels + verification)
3. **Instruction** defines stepwise work under protocol/doctrine governance (with halt gates)
4. **Prompt** defines the LLM invocation template used during instruction execution (also under governance)

That is exactly the separation you want if you’re going to standardise prompts to “v3” and keep them auditable.

---

# The one thing I’d add next (optional, but high value)

If you want this to become “self-validating and discoverable” across the repo, add a **registry/index schema**, something like:

* `schemas-index.schema.json` (or `instruction-index.schema.json`)
* lists all doctrine/protocol/instruction/prompt artefacts
* enforces uniqueness of ids/names
* defines allowed dependency edges (doctrine → protocol → instruction → prompt)

That makes it trivial to build a linter or CI check.

---

If you want, send me one real **v3 prompt JSON** (an instance that claims to conform to `prompt-schema.json`), and I’ll run a “human validator” pass: what’s missing, what’s redundant, what’s ambiguous, and how to tighten it so it’s production-grade.
