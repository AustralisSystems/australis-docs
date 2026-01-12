# Manual Web UI CLI Regression Testing - Execution Guide

This guide provides comprehensive methods for executing `12-Manual_WebUI_Regression_Testing.yaml`, including full execution and selective parsing by YAML key references.

## Quick Start

### Full Execution (First Time)
```
Execute @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml from the beginning
```

### Continuation Instruction (Subsequent Use)
```
Follow the continuation_instruction from @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml
```

### Selective Parsing (Recommended for Re-execution)
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only the 'instructions.steps[5]' section (Manual CLI Route Testing)
```

---

## Execution Methods

### Method 1: Full Execution from Beginning

**Use Case**: First-time execution, need complete context

**Command:**
```
Execute @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml from the beginning
```

**Alternative Formats:**
```
Execute @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml
Load and execute @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml
Follow @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml starting from step 1
```

**What Happens:**
- Loads entire instruction file
- Reads all sections (context, workflow, best practices, etc.)
- Follows all 10 workflow steps sequentially
- Applies all validation checkpoints
- Enumerates all web UI routes
- Tests routes manually via CLI one at a time

---

### Method 2: Continuation Instruction Execution

**Use Case**: File context already available, quick execution

**Command:**
```
Follow the continuation_instruction from @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml
```

**Alternative Formats:**
```
Execute per continuation_instruction in @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml
Continue per @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml continuation_instruction
```

**What Happens:**
- Uses `continuation_instruction` section directly (lines 326-435)
- Follows summarized workflow steps
- Applies all best practices requirements
- Enforces validation checkpoints
- Enforces manual CLI testing only rule

---

### Method 3: Direct Paste

**Use Case**: Maximum speed, no file lookup needed

**Command:**
```
[Paste the entire continuation_instruction section here]
```

**What Happens:**
- Immediate execution without file access
- Uses pasted continuation instruction content
- Fastest method for repeated execution

---

## Selective Parsing Methods (YAML Key References)

### Method 4: Parse and Execute Specific Step by Index

**Use Case**: Execute only one workflow step

**Step 1 (Review Canonical Documentation):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only the 'instructions.steps[0]' section (Review Canonical Documentation)
```

**Step 2 (Confirm Plan + SPEC Scope):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only the 'instructions.steps[1]' section (Confirm Plan + SPEC Scope)
```

**Step 3 (Verify Web Application Status):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only the 'instructions.steps[2]' section (Verify Web Application Status)
```

**Step 4 (Enumerate Routes & Partials):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only the 'instructions.steps[3]' section (Enumerate Routes & Partials)
```

**Step 5 (Prepare Authentication):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only the 'instructions.steps[4]' section (Prepare Authentication)
```

**Step 6 (Manual CLI Route Testing):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only the 'instructions.steps[5]' section (Manual CLI Route Testing)
```

**Step 7 (Cross-Route Navigation Integrity):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only the 'instructions.steps[6]' section (Cross-Route Navigation Integrity)
```

**Step 8 (Performance + Asset Checks):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only the 'instructions.steps[7]' section (Performance + Asset Checks)
```

**Step 9 (Documentation & Handoff):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only the 'instructions.steps[8]' section (Documentation & Handoff)
```

**Step 10 (Audit Readiness):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only the 'instructions.steps[9]' section (Audit Readiness)
```

---

### Method 5: Parse, Index, and Execute with Best Practices Focus

**Use Case**: Execute steps with specific best practices review

**Route Enumeration with UI Integration Best Practices:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, index all workflow steps, then execute only Step 4 with best practices focus: ui_integration
```

**Testing with HTMX Best Practices:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, index all workflow steps, then execute only Step 6 with best practices focus: htmx
```

**Testing with Security Best Practices:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, index all workflow steps, then execute only Step 6 with best practices focus: security
```

---

### Method 6: Parse and Extract Specific YAML Sections

**Use Case**: Execute specific actions or subsections

**Extract Step 4 Enumeration Actions Only:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[3].actions', and execute only those actions
```

**Extract Step 6 Manual CLI Testing Actions:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[5].actions', and execute only manual CLI testing workflow
```

**Extract Suggested Commands:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[2].suggested_commands', and execute server verification commands
```

**Extract Best Practices References:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'context.best_practices_references', and review all best practices documents
```

**Extract Examples Section:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'examples', and review route CLI testing examples
```

**Extract Scope Constraints:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[1].outputs.scope_constraints', and review test scope constraints
```

---

### Method 7: Parse Multiple Steps

**Use Case**: Execute a range of steps

**Steps 1-3 (Review through Server Verification):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[0:3]' (Steps 1-3)
```

**Steps 3-5 (Server Verification through Authentication):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[2:5]' (Steps 3-5)
```

**Steps 4-6 (Enumeration through Testing):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[3:6]' (Steps 4-6)
```

**From Step 6 Onwards (Testing onwards):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[5:]' (From Step 6 onwards)
```

**Steps 4, 5, and 6 (Enumeration, Authentication, Testing):**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[3]', 'instructions.steps[4]', and 'instructions.steps[5]' (Steps 4, 5, and 6)
```

---

### Method 8: Parse with Best Practices Focus

**Use Case**: Execute with emphasis on specific best practices

**UI Integration Best Practices:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract Step 4 and 'context.best_practices_references.ui_integration', and execute Step 4 with UI integration best practices focus
```

**HTMX Best Practices:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract Step 6 and 'context.best_practices_references.ui_integration', and execute Step 6 with HTMX best practices focus
```

**Security Best Practices:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract Step 6 and 'context.best_practices_references.security_compliance', and execute Step 6 with security best practices focus
```

**All Best Practices:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract all 'best_practices_references' sections, and execute with all best practices review
```

---

### Method 9: Parse Continuation Instruction Only

**Use Case**: Quick execution using continuation instruction without full file load

**Command:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'continuation_instruction' section, and execute that
```

**Alternative:**
```
Read @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract continuation_instruction (lines 326-435), and execute that
```

---

## YAML Structure Reference

Understanding the YAML structure helps you reference specific sections precisely:

```yaml
12-Manual_WebUI_Regression_Testing.yaml
├── prompt_name
├── version
├── type
├── context
│   ├── role
│   ├── governance
│   ├── purpose
│   ├── critical_documentation_rule
│   ├── critical_testing_rule
│   ├── doc_references
│   │   ├── canonical
│   │   └── plan
│   ├── best_practices_references
│   │   ├── core_fastapi
│   │   ├── async_performance
│   │   ├── reliability_resilience
│   │   ├── architecture_patterns
│   │   ├── security_compliance
│   │   ├── observability_monitoring
│   │   ├── data_persistence
│   │   ├── configuration_deployment
│   │   ├── background_tasks
│   │   ├── integration_patterns
│   │   ├── ui_integration
│   │   ├── code_quality_testing
│   │   └── templating_scaffolding
│   └── environment_assumptions
├── prerequisites
│   └── validations
└── instructions
    ├── objective
    ├── best_practices_requirement
    └── steps[0-9]
        ├── step (number)
        ├── name
        ├── actions
        ├── gates (some steps)
        ├── outputs (some steps)
        ├── suggested_commands (Steps 3, 4, 6)
        └── outputs (Step 6)
├── constraints
├── examples
│   ├── route_cli_example
│   └── remediation_example
├── output_format
├── metadata
└── continuation_instruction
```

---

## YAML Key Reference Examples

### Step References (0-indexed)

- **Step 1**: `instructions.steps[0]` - Review Canonical Documentation
- **Step 2**: `instructions.steps[1]` - Confirm Plan + SPEC Scope
- **Step 3**: `instructions.steps[2]` - Verify Web Application Status
- **Step 4**: `instructions.steps[3]` - Enumerate Routes & Partials
- **Step 5**: `instructions.steps[4]` - Prepare Authentication (If Needed)
- **Step 6**: `instructions.steps[5]` - Manual CLI Route Testing
- **Step 7**: `instructions.steps[6]` - Cross-Route Navigation Integrity
- **Step 8**: `instructions.steps[7]` - Performance + Asset Checks
- **Step 9**: `instructions.steps[8]` - Documentation & Handoff
- **Step 10**: `instructions.steps[9]` - Audit Readiness

### Best Practices References

- **All Best Practices**: `context.best_practices_references`
- **UI Integration**: `context.best_practices_references.ui_integration`
- **Core FastAPI**: `context.best_practices_references.core_fastapi`
- **Security**: `context.best_practices_references.security_compliance`
- **Testing**: `context.best_practices_references.code_quality_testing`

### Actions and Outputs

- **Step 4 Actions**: `instructions.steps[3].actions`
- **Step 4 Outputs**: `instructions.steps[3].outputs`
- **Step 6 Actions**: `instructions.steps[5].actions`
- **Step 6 Outputs**: `instructions.steps[5].outputs`
- **Step 2 Outputs**: `instructions.steps[1].outputs`
- **Step 5 Outputs**: `instructions.steps[4].outputs`

### Critical Rules

- **Documentation Rule**: `context.critical_documentation_rule`
- **Testing Rule**: `context.critical_testing_rule`

### Examples

- **All Examples**: `examples`
- **Route CLI Example**: `examples.route_cli_example`
- **Remediation Example**: `examples.remediation_example`

---

## Recommended Execution Patterns

### Pattern 1: Parse First, Then Execute (Recommended)

**Workflow:**
1. Parse the entire file to understand structure
2. Index all workflow steps
3. Execute full file OR reference specific YAML keys

**Example:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, index all workflow steps and YAML structure, then execute only 'instructions.steps[3]' with best practices focus: ui_integration
```

### Pattern 2: Extract and Execute Specific Section

**Workflow:**
1. Extract specific YAML section
2. Execute only that section

**Example:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[5].actions', and execute only manual CLI testing workflow
```

### Pattern 3: Parse with Context, Execute Selectively

**Workflow:**
1. Parse file with full context
2. Reference specific keys for execution

**Example:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml with full context, then execute only 'instructions.steps[3].actions' with 'context.best_practices_references.ui_integration' applied
```

### Pattern 4: Execute Testing Workflow Phases

**Phase 1: Preparation (Steps 1-3)**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[0:3]' (Review Documentation through Server Verification)
```

**Phase 2: Enumeration and Authentication (Steps 4-5)**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[3:5]' (Enumeration through Authentication)
```

**Phase 3: Testing (Steps 6-8)**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[5:8]' (Manual Testing through Performance Checks)
```

**Phase 4: Documentation (Steps 9-10)**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[8:]' (Documentation through Audit Readiness)
```

---

## Advanced YAML Key Reference Patterns

### Execute Step with Specific Best Practices

```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[3]' and 'context.best_practices_references.ui_integration', then execute Step 4 with UI integration best practices review
```

### Execute Multiple Related Sections

```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[3]', 'instructions.steps[5]', and 'context.best_practices_references', then execute Steps 4 and 6 with best practices
```

### Execute with Conditional Logic

```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, index all steps, if enumeration phase then execute 'instructions.steps[3]' with 'context.best_practices_references.ui_integration'
```

### Execute Testing Step with HTMX Focus

```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[5]' and 'context.best_practices_references.ui_integration', then execute Step 6 with HTMX best practices focus
```

### Execute with Scope Constraints

```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[1].outputs.scope_constraints' and 'instructions.steps[3]', then execute Step 4 with scope constraints applied
```

---

## Comparison: Full Load vs Selective Parsing

| Aspect | Full Load | Selective Parsing |
|--------|-----------|-------------------|
| **Speed** | Slower | Faster |
| **Token Usage** | Higher | Lower |
| **Context** | Complete | Focused |
| **Best For** | First-time execution | Re-execution, specific steps |
| **Precision** | Broad | Precise |
| **Dependencies** | All loaded | Only needed sections |

---

## Best Practices for Selective Parsing

1. **Always Parse First**: Parse the entire file to understand structure before referencing keys
2. **Use Precise Keys**: Reference exact YAML paths (e.g., `instructions.steps[3]` not "step 4")
3. **Include Context**: When extracting sections, include necessary dependencies (e.g., best practices review with actions)
4. **Index Workflow Steps**: Use "index all workflow steps" to understand available steps before execution
5. **Reference Best Practices**: Always include best practices review sections when executing Steps 4 or 6
6. **Follow Testing Rules**: Always include `critical_testing_rule` when executing Step 6
7. **Consider Scope Constraints**: Include scope constraints from Step 2 when executing Step 4

---

## Common Execution Scenarios

### Scenario 1: First-Time Execution
```
Execute @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml from the beginning
```

### Scenario 2: Re-execute Route Enumeration Only
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, index all workflow steps, then execute only Step 4 with best practices focus: ui_integration
```

### Scenario 3: Execute Only Manual CLI Testing
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[5].actions', and execute only manual CLI testing workflow
```

### Scenario 4: Execute Testing with HTMX Focus
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[5]' and 'context.best_practices_references.ui_integration', then execute Step 6 with HTMX best practices focus
```

### Scenario 5: Execute Continuation Instruction Only
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'continuation_instruction', and execute that
```

### Scenario 6: Execute Enumeration Phase Only (Steps 4-5)
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[3:5]' (Enumeration through Authentication)
```

### Scenario 7: Execute Testing Phase Only (Steps 6-8)
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[5:8]' (Manual Testing through Performance Checks)
```

### Scenario 8: Execute Documentation Phase Only (Steps 9-10)
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[8:]' (Documentation through Audit Readiness)
```

---

## Quick Reference Cheat Sheet

| What You Want | Command Pattern |
|---------------|----------------|
| **Full execution** | `Execute @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml from the beginning` |
| **Continuation only** | `Follow the continuation_instruction from @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml` |
| **Specific step** | `Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[3]'` |
| **Route enumeration** | `Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, index all workflow steps, then execute only Step 4 with best practices focus: ui_integration` |
| **Manual CLI testing** | `Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[5].actions', and execute only manual CLI testing workflow` |
| **Testing with HTMX** | `Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[5]' and 'context.best_practices_references.ui_integration', then execute Step 6` |
| **Multiple steps** | `Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[3:5]'` |
| **Best practices review** | `Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'context.best_practices_references', and review all best practices documents` |
| **Scope constraints** | `Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[1].outputs.scope_constraints', and review test scope constraints` |

---

## Critical Rules Reference

### Critical Documentation Rule
- **Rule**: `context.critical_documentation_rule`
- **Key Points**:
  - NO temporal documents
  - ALL updates go into SPECs and IMPLEMENTATION_PLAN only
  - NON-NEGOTIABLE

### Critical Testing Rule
- **Rule**: `context.critical_testing_rule`
- **Key Points**:
  - MANUAL CLI TESTING ONLY
  - NO browser automation (Playwright/Cypress/Selenium)
  - NO automated scripts or batch execution
  - Test routes ONE AT A TIME
  - Remediate issues immediately before proceeding
  - Browser automation belongs to Instruction 13, not Instruction 12
  - NON-NEGOTIABLE

---

## Tips for Effective Execution

1. **Start with Parse**: Always parse the file first to understand its structure
2. **Use YAML Keys**: Reference exact YAML paths for precision
3. **Index Steps**: Use "index all workflow steps" to see available options
4. **Combine Sections**: Extract multiple related sections for complete context
5. **Include Best Practices**: Always include best practices review for Steps 4 and 6
6. **Follow Testing Rules**: Always respect the manual CLI testing only rule for Step 6
7. **Follow Workflow Phases**: Consider executing in phases (Preparation → Enumeration → Testing → Documentation)
8. **Consider Scope Constraints**: Check for scope constraints in Step 2 before executing Step 4
9. **Remember Instruction 13**: This instruction is a precursor to Instruction 13 (browser-based testing)

---

## Troubleshooting

### Issue: YAML Key Not Found

**Solution**: Parse the file first to see actual structure:
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and show YAML structure
```

### Issue: Step Execution Missing Context

**Solution**: Include related sections:
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[3]' and 'context.best_practices_references.ui_integration', then execute Step 4 with UI integration best practices review
```

### Issue: Missing Best Practices Review

**Solution**: Always include best practices review for Steps 4 and 6:
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[3]' and 'context.best_practices_references.ui_integration', then execute Step 4 with best practices review
```

### Issue: Testing Rule Violation

**Solution**: Always include critical testing rule when executing Step 6:
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[5]' and 'context.critical_testing_rule', then execute Step 6 with manual CLI testing enforcement
```

### Issue: Scope Constraints Not Applied

**Solution**: Include scope constraints from Step 2 when executing Step 4:
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[1].outputs.scope_constraints' and 'instructions.steps[3]', then execute Step 4 with scope constraints applied
```

---

## Workflow Phase Breakdown

### Phase 1: Preparation (Steps 1-3)
- **Step 1**: Review Canonical Documentation
- **Step 2**: Confirm Plan + SPEC Scope
- **Step 3**: Verify Web Application Status

**Execute Phase 1:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[0:3]'
```

### Phase 2: Enumeration and Authentication (Steps 4-5)
- **Step 4**: Enumerate Routes & Partials (with UI integration best practices)
- **Step 5**: Prepare Authentication (If Needed)

**Execute Phase 2:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[3:5]'
```

### Phase 3: Testing (Steps 6-8)
- **Step 6**: Manual CLI Route Testing (with HTMX/testing best practices, MANUAL CLI ONLY)
- **Step 7**: Cross-Route Navigation Integrity
- **Step 8**: Performance + Asset Checks

**Execute Phase 3:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[5:8]'
```

### Phase 4: Documentation (Steps 9-10)
- **Step 9**: Documentation & Handoff
- **Step 10**: Audit Readiness

**Execute Phase 4:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml and execute only 'instructions.steps[8:]'
```

---

## Manual CLI Testing Workflow (Step 6)

Step 6 has a detailed workflow for manual CLI testing:

**For each route in cli_test_plan (grouped logically):**

**a. Build the exact HTTP call**
- Method, headers, query params
- Include authentication cookies/tokens if required
- Add HTMX headers (HX-Request:true) for HTMX endpoints

**b. Execute via curl/HTTPie/MCP fetch**
- Capture status code, headers, HTML payload
- Save HTML to file for inspection if needed

**c. Inspect HTML for required elements**
- Macros/blocks rendered correctly
- Placeholder text replaced
- HTMX targets present
- Required widgets appear

**d. Validate content**
- Content-length headers
- Caching headers (Cache-Control, ETag)
- Response time (use Measure-Command or curl -w)

**e. Tail service logs**
- Check for WARN/ERROR tied to request timestamp
- Verify zero warnings/errors

**f. Verify HTMX fragments (if partial)**
- If response is a partial (hx-get), verify expected fragments
- Check table rows, modals, etc. are present

**g. Simulate realistic CRUD/navigation flows**
- Retrieve collections
- Fetch individual detail fragments
- Submit create/edit payloads
- Re-fetch to confirm persistence
- Trigger delete/reset endpoints to ensure cleanup

**h. Document findings**
- PASS/FAIL status
- Snippet references
- Remediation notes

**i. Remediate issues immediately**
- STOP testing and remediate issues ONE AT A TIME
- Re-run same route until PASS
- Do not proceed to next route until current route passes

**Execute Step 6 Manual CLI Testing:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[5]', and execute Step 6 manual CLI testing workflow
```

---

## Forbidden Testing Methods

When executing Step 6, these methods are FORBIDDEN:

- Browser automation (Playwright, Cypress, Selenium)
- Automated regression frameworks
- Playwright scripts
- pytest scripts
- Automated/batch CLI scripts
- Any form of automated test execution

**Note**: Browser automation belongs to Instruction 13, not Instruction 12.

---

## Allowed Manual CLI Testing Tools

When executing Step 6, these tools are ALLOWED:

- `curl` - Manual HTTP requests from command line
- `HTTPie` - Manual HTTP client
- `MCP fetch` - MCP tool for manual HTTP requests
- `MCP browser extension` - In raw mode (not automation mode)
- Manual log inspection (docker logs, service logs)

**Review Allowed Tools:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'context.critical_testing_rule', and review allowed CLI testing tools
```

---

## Scope Constraints

By default, ALL routes MUST be tested unless scope constraints are specified in Step 2. Scope constraints can be:
- Route patterns (e.g., `/api-management/*`, `/storage/*`)
- Route categories (e.g., Dashboard, Storage, Workflows)
- Specific route lists

**Review Scope Constraints:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[1].outputs.scope_constraints', and review test scope constraints
```

**Execute with Scope Constraints:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[1].outputs.scope_constraints' and 'instructions.steps[3]', then execute Step 4 with scope constraints applied
```

---

## Performance Validation

Step 8 validates performance:
- Compare response time + payload size against baseline (±20%)
- Verify static assets (CSS/JS) return 200 via curl -I
- >20% regression requires remediation or documented exception

**Execute Performance Validation:**
```
Parse @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml, extract 'instructions.steps[7]', and execute Step 8 performance validation
```

---

## Instruction 12 vs Instruction 13

**Instruction 12 (This Instruction):**
- CLI-based testing only
- Manual HTTP tools (curl, HTTPie, MCP fetch)
- HTML inspection and validation
- HTMX fragment verification
- NO browser automation

**Instruction 13 (Browser-Based Testing):**
- Browser-based testing
- Visual rendering verification
- User interaction simulation
- Browser automation tools (Playwright, MCP browser)
- Recommended as follow-up to Instruction 12

**Recommended Flow:**
1. Execute Instruction 12 (CLI testing)
2. Execute Instruction 13 (browser testing) for the same scope

---

**Last Updated**: 2025-12-15
**File**: `12-Manual_WebUI_Regression_Testing.yaml`
**Version**: 1.0.0
