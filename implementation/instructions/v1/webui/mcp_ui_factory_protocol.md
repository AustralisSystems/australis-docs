# MCP Protocol: UI Factory – Web App Layout & Template Generator

## 1. Purpose
This MCP protocol defines how the UI Factory orchestrates LLMs, design tokens, layout rules, and code generators to produce complete web UI applications from:
- an OpenAPI specification
- layout.tokens.json
- motion and layout specifications
- chosen render targets (React and/or HTMX + Jinja2)

The protocol is designed to be:
- deterministic
- auditable
- repeatable
- renderer-agnostic

---

## 2. Roles
The protocol uses a three-role model for reliability:

1. **Creator**
   - Interprets OpenAPI, layout tokens, and conversion rules.
   - Produces the UI Model JSON and initial code scaffolds.

2. **Validator**
   - Verifies that outputs conform to:
     - UI Model schema
     - layout.tokens.json
     - motion and responsive rules
     - OpenAPI binding correctness

3. **Judge**
   - Resolves disagreements between Creator and Validator.
   - Chooses the final approved artefacts.
   - Requests revisions where necessary.

Each role must be implemented by a distinct model or tool.

### 2.1 Execution Limits
To ensure reliable and performant execution:

- **LLM Operation Timeout:** 120 seconds per stage
- **Maximum Retry Count:** 3 attempts per stage before escalation
- **Concurrency Limit:** Maximum 5 pages generated in parallel
- **Judge Retry Limit:** Maximum 2 re-runs of a failed stage

If limits are exceeded:
- Log the timeout/retry event
- Escalate to Judge for manual intervention
- Provide partial results if available

---

## 3. Inputs
The MCP UI Factory requires the following inputs:

1. **OpenAPI Document**
   - JSON or YAML.
   - Fully describes API endpoints, schemas, and security.

2. **Design Tokens** (`layout.tokens.json`)
   - Spacing, breakpoints, layout, elevation, radius, typography, behaviour, motion.

3. **Conversion Rules** (`openapi_ui_model_conversion_rules`)
   - Canonical mapping from OpenAPI → UI Model.

4. **Render Targets**
   - React (Tailwind + TSX) and/or HTMX + Jinja2 (Tailwind).

5. **Project Settings**
   - Project name, package name, base route, output directory structure.

---

## 4. Core Artefacts
The output of this MCP includes:

1. **UI Model JSON**
   - Canonical view of pages, routes, components, layouts, bindings.

2. **Tailwind Config**
   - Generated from layout.tokens.json using the Tailwind Generator Template.

3. **React Code (optional)**
   - Pages, components, layout primitives.

4. **HTMX + Jinja2 Code (optional)**
   - Templates, macros, includes, HTMX endpoints.

5. **Project Structure**
   - Consistent directories for frontend, templates, static assets, config.

6. **Protocol Log** (`protocol-log.json`)
   - Summary of decisions, validations, and any deviations.
   - Schema:
     ```json
     {
       "version": "1.0.0",
       "timestamp": "ISO 8601 datetime",
       "stages": [
         {
           "stage": "string (1-6)",
           "role": "creator|validator|judge",
           "status": "success|warning|error",
           "duration_ms": "number",
           "retry_count": "number",
           "decisions": ["array of decision descriptions"],
           "warnings": ["array of warning messages"],
           "errors": ["array of error messages"]
         }
       ],
       "final_status": "success|partial|failed",
       "total_duration_ms": "number",
       "artefacts_generated": "number"
     }
     ```

---

## 5. High-Level Stages

### Stage 1 – Initialisation
- Load inputs.
- Validate OpenAPI structure.
- Validate layout.tokens.json presence and structure.
- Confirm render targets.

### Stage 2 – UI Model Generation (Creator)
- Apply conversion rules to OpenAPI.
- Generate UI Model JSON.
- Attach responsive and behavioural metadata.

### Stage 3 – UI Model Validation (Validator)
- Validate UI Model against its JSON schema.
- Check for missing pages for CRUD flows.
- Confirm layout choices follow density and responsive rules.

### Stage 4 – Code Generation (Creator)
- For React: generate TSX pages and components.
- For HTMX/Jinja2: generate templates and macros.
- Generate Tailwind config.

### Stage 5 – Code Validation (Validator)
- Static validation against coding rules.
- Check that classes align with Tailwind tokens.
- Ensure all UI Model pages have corresponding templates.

### Stage 6 – Judgment & Finalisation (Judge)
- Compare Creator and Validator outputs.
- Approve or request revision.
- Produce final protocol log and artefact manifest.

---

## 6. Stage Details & Required Behaviour

### 6.1 Stage 1 – Initialisation
- Confirm OpenAPI version is supported.
- Extract:
  - tags
  - operations
  - request/response schemas
- Confirm that tokens contain required keys:
  - spacing
  - breakpoints
  - layout
  - elevation
  - radius
  - typography
  - motion

If any required element is missing:
- Halt and emit a structured error.

---

### 6.2 Stage 2 – UI Model Generation (Creator)

**Goal:** Produce a complete UI Model from OpenAPI.

Steps:
1. Group operations by tag or path segment.
2. For each group:
   - create list, detail, create, and edit pages where applicable.
3. For each list page:
   - determine layout (table/grid/cards/list) based on field count and types.
4. Define visibility rules:
   - mustShow: identifying and key fields
   - shouldShow: secondary and semantic fields
   - niceToShow: metadata
5. Attach responsive behaviour:
   - preferredLayouts
   - fallbackLayouts
   - minimum widths and thresholds from layout tokens.

Output: `ui-model.json`.

---

### 6.3 Stage 3 – UI Model Validation (Validator)

Checks:
- JSON schema compliance.
- Every CRUD operation has at least one page.
- Layout decisions comply with density rules.
- Responsive behaviour uses only allowed layouts.
- Route patterns are consistent and conflict-free.

If any validation fails:
- Emit detailed report.
- Return to Creator with required amendments.

---

### 6.4 Stage 4 – Code Generation (Creator)

#### React Mode
Generate:
- `src/pages/{pageId}.tsx`
- layout components (Shell, Sidebar, Header, Footer)
- shared components (Card, Table, List, Accordion)

Rules:
- Use Tailwind classes derived from tokens.
- Use the UI Model layout field to choose components.
- Use motion tokens for transitions.

#### HTMX + Jinja2 Mode
Generate:
- `templates/pages/{pageId}.html`
- `templates/macros/components.html`

Rules:
- Use Jinja2 variables for dynamic fields.
- Use HTMX attributes for interactions.
- Apply Tailwind classes from tokens.

---

### 6.5 Stage 5 – Code Validation (Validator)

Checks:
- File presence for all pages in UI Model.
- No missing fields referenced.
- Tailwind classes are valid and consistent with generated config.
- HTML and TSX syntax is well-formed.
- Routes match the specification in UI Model.

---

### 6.6 Stage 6 – Judgment & Finalisation (Judge)

The Judge:
- Reviews UI Model and code validation reports.
- Confirms that:
  - all flows defined by OpenAPI are represented.
  - design system rules are respected.
  - responsive rules are enforceable.
- On success:
  - emits a manifest of generated artefacts.
  - marks the run as successful.
- On failure:
  - specifies whether the issue is conceptual (UI Model) or technical (code).
  - requests specific re-runs of relevant stages.

---

## 7. Versioning Strategy

The protocol follows semantic versioning:

- **Major Version (X.0.0):** Breaking changes to UI Model schema or stage structure
- **Minor Version (1.X.0):** New features, additional tokens, new render targets
- **Patch Version (1.0.X):** Bug fixes, clarifications, performance improvements

Current Version: **1.0.0**

Backward Compatibility:
- Protocol log includes version number for traceability
- UI Model schema versions are tracked separately
- Older protocol versions supported for 6 months after major version release

---

## 8. Error Handling & Retries

- Each stage must return machine-readable status:
  - `success`, `warning`, `error`.
- On `error`, the protocol:
  - logs full context.
  - stops dependent stages.
  - awaits correction or new inputs.

LLMs participating in Creator/Validator roles must:
- never silently ignore errors.
- always propose a concrete fix.

---

## 9. Outputs & Manifest

The final output includes:

1. `ui-model.json`
2. `tailwind.config.js`
3. React pages (if selected)
4. HTMX + Jinja2 templates (if selected)
5. `protocol-log.json` (summaries of decisions and validations)
6. `manifest.json` listing all generated files with paths and types

---

## 10. Rollback & Undo Mechanism

If the Judge rejects outputs:

1. **Preserve State:** Save UI Model and code snapshots at each stage
2. **Rollback Points:** Allow return to any previous successful stage
3. **Differential Re-generation:** Only regenerate failed components
4. **Snapshot Cleanup:** Remove snapshots after final approval (retain for 24 hours)

Rollback Command Structure:
```json
{
  "action": "rollback",
  "target_stage": "2|3|4|5",
  "reason": "description of rejection",
  "preserve_artifacts": ["list of files to keep"]
}
```

---

## 11. Usage Notes

- This protocol is renderer-agnostic and can be extended to other targets.
- All layout, motion, and responsive behaviour must be derived from tokens and rules, not invented ad hoc.
- LLMs must always consult:
  - layout.tokens.json
  - motion transition spec
  - OpenAPI → UI Model conversion rules
before generating or modifying UI code.

---

End of MCP Protocol for UI Factory.
