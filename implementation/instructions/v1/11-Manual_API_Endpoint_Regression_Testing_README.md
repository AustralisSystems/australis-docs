# Manual API Endpoint Regression Testing - Execution Guide

This guide provides comprehensive methods for executing `11-Manual_API_Endpoint_Regression_Testing.yaml`, including full execution and selective parsing by YAML key references.

## Quick Start

### Full Execution (First Time)
```
Execute @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml from the beginning
```

### Continuation Instruction (Subsequent Use)
```
Follow the continuation_instruction from @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml
```

### Selective Parsing (Recommended for Re-execution)
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only the 'instructions.steps[5]' section (Manual Endpoint Testing)
```

---

## Execution Methods

### Method 1: Full Execution from Beginning

**Use Case**: First-time execution, need complete context

**Command:**
```
Execute @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml from the beginning
```

**Alternative Formats:**
```
Execute @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml
Load and execute @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml
Follow @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml starting from step 1
```

**What Happens:**
- Loads entire instruction file
- Reads all sections (context, workflow, best practices, etc.)
- Follows all 9 workflow steps sequentially
- Applies all validation checkpoints
- Enumerates all API endpoints
- Tests endpoints manually one at a time

---

### Method 2: Continuation Instruction Execution

**Use Case**: File context already available, quick execution

**Command:**
```
Follow the continuation_instruction from @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml
```

**Alternative Formats:**
```
Execute per continuation_instruction in @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml
Continue per @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml continuation_instruction
```

**What Happens:**
- Uses `continuation_instruction` section directly (lines 453-565)
- Follows summarized workflow steps
- Applies all best practices requirements
- Enforces validation checkpoints
- Enforces manual testing only rule

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
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only the 'instructions.steps[0]' section (Review Canonical Documentation)
```

**Step 2 (Read Implementation Plan & Determine CURRENT Work):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only the 'instructions.steps[1]' section (Read Implementation Plan & Determine CURRENT Work)
```

**Step 3 (Verify API Server Status):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only the 'instructions.steps[2]' section (Verify API Server Status)
```

**Step 4 (Enumerate All API Endpoints):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only the 'instructions.steps[3]' section (Enumerate All API Endpoints)
```

**Step 5 (Prepare Authentication):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only the 'instructions.steps[4]' section (Prepare Authentication)
```

**Step 6 (Manual Endpoint Testing):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only the 'instructions.steps[5]' section (Manual Endpoint Testing)
```

**Step 7 (Performance Validation):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only the 'instructions.steps[6]' section (Performance Validation)
```

**Step 8 (Issue Collation & Documentation Update):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only the 'instructions.steps[7]' section (Issue Collation & Documentation Update)
```

**Step 9 (Audit Readiness & Halt):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only the 'instructions.steps[8]' section (Audit Readiness & Halt)
```

---

### Method 5: Parse, Index, and Execute with Best Practices Focus

**Use Case**: Execute steps with specific best practices review

**Endpoint Enumeration with FastAPI Best Practices:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, index all workflow steps, then execute only Step 4 with best practices focus: fastapi
```

**Testing with Security Best Practices:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, index all workflow steps, then execute only Step 6 with best practices focus: security
```

**Testing with Performance Best Practices:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, index all workflow steps, then execute only Step 6 with best practices focus: performance
```

---

### Method 6: Parse and Extract Specific YAML Sections

**Use Case**: Execute specific actions or subsections

**Extract Step 4 Enumeration Actions Only:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[3].actions', and execute only those actions
```

**Extract Step 6 Manual Testing Actions:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5].actions', and execute only manual testing workflow
```

**Extract Suggested Commands:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[2].suggested_commands', and execute server verification commands
```

**Extract Forbidden Testing Methods:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5].forbidden_testing_methods', and review forbidden methods
```

**Extract Best Practices References:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'context.best_practices_references', and review all best practices documents
```

**Extract Examples Section:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'examples', and review endpoint enumeration and testing examples
```

**Extract Scope Constraints:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[1].outputs.scope_constraints', and review test scope constraints
```

---

### Method 7: Parse Multiple Steps

**Use Case**: Execute a range of steps

**Steps 1-3 (Review through Server Verification):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[0:3]' (Steps 1-3)
```

**Steps 3-5 (Server Verification through Authentication):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[2:5]' (Steps 3-5)
```

**Steps 4-6 (Enumeration through Testing):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[3:6]' (Steps 4-6)
```

**From Step 6 Onwards (Testing onwards):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[5:]' (From Step 6 onwards)
```

**Steps 4, 5, and 6 (Enumeration, Authentication, Testing):**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[3]', 'instructions.steps[4]', and 'instructions.steps[5]' (Steps 4, 5, and 6)
```

---

### Method 8: Parse with Best Practices Focus

**Use Case**: Execute with emphasis on specific best practices

**FastAPI Best Practices:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract Step 4 and 'context.best_practices_references.core_fastapi', and execute Step 4 with FastAPI best practices focus
```

**Security Best Practices:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract Step 6 and 'context.best_practices_references.security_compliance', and execute Step 6 with security best practices focus
```

**Testing Best Practices:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract Step 6 and 'context.best_practices_references.code_quality_testing', and execute Step 6 with testing best practices focus
```

**All Best Practices:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract all 'best_practices_references' sections, and execute with all best practices review
```

---

### Method 9: Parse Continuation Instruction Only

**Use Case**: Quick execution using continuation instruction without full file load

**Command:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'continuation_instruction' section, and execute that
```

**Alternative:**
```
Read @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract continuation_instruction (lines 453-565), and execute that
```

---

## YAML Structure Reference

Understanding the YAML structure helps you reference specific sections precisely:

```yaml
11-Manual_API_Endpoint_Regression_Testing.yaml
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
    └── steps[0-8]
        ├── step (number)
        ├── name
        ├── actions
        ├── gates (some steps)
        ├── outputs (some steps)
        ├── suggested_commands (Steps 3, 4, 5)
        ├── suggested_manual_testing_tools (Step 6)
        ├── forbidden_testing_methods (Step 6)
        └── outputs (Step 6)
├── constraints
├── examples
│   ├── endpoint_enumeration_example
│   ├── manual_testing_example
│   ├── remediation_example
│   ├── scope_constraint_example
│   └── forbidden_testing_example
├── output_format
├── metadata
└── continuation_instruction
```

---

## YAML Key Reference Examples

### Step References (0-indexed)

- **Step 1**: `instructions.steps[0]` - Review Canonical Documentation
- **Step 2**: `instructions.steps[1]` - Read Implementation Plan & Determine CURRENT Work
- **Step 3**: `instructions.steps[2]` - Verify API Server Status
- **Step 4**: `instructions.steps[3]` - Enumerate All API Endpoints
- **Step 5**: `instructions.steps[4]` - Prepare Authentication (If Required)
- **Step 6**: `instructions.steps[5]` - Manual Endpoint Testing
- **Step 7**: `instructions.steps[6]` - Performance Validation (If Baseline Available)
- **Step 8**: `instructions.steps[7]` - Issue Collation & Documentation Update
- **Step 9**: `instructions.steps[8]` - Audit Readiness & Halt

### Best Practices References

- **All Best Practices**: `context.best_practices_references`
- **Core FastAPI**: `context.best_practices_references.core_fastapi`
- **Security**: `context.best_practices_references.security_compliance`
- **Testing**: `context.best_practices_references.code_quality_testing`
- **Performance**: `context.best_practices_references.async_performance`

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
- **Endpoint Enumeration Example**: `examples.endpoint_enumeration_example`
- **Manual Testing Example**: `examples.manual_testing_example`
- **Remediation Example**: `examples.remediation_example`
- **Scope Constraint Example**: `examples.scope_constraint_example`
- **Forbidden Testing Example**: `examples.forbidden_testing_example`

---

## Recommended Execution Patterns

### Pattern 1: Parse First, Then Execute (Recommended)

**Workflow:**
1. Parse the entire file to understand structure
2. Index all workflow steps
3. Execute full file OR reference specific YAML keys

**Example:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, index all workflow steps and YAML structure, then execute only 'instructions.steps[3]' with best practices focus: fastapi
```

### Pattern 2: Extract and Execute Specific Section

**Workflow:**
1. Extract specific YAML section
2. Execute only that section

**Example:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5].actions', and execute only manual testing workflow
```

### Pattern 3: Parse with Context, Execute Selectively

**Workflow:**
1. Parse file with full context
2. Reference specific keys for execution

**Example:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml with full context, then execute only 'instructions.steps[3].actions' with 'context.best_practices_references.core_fastapi' applied
```

### Pattern 4: Execute Testing Workflow Phases

**Phase 1: Preparation (Steps 1-3)**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[0:3]' (Review Documentation through Server Verification)
```

**Phase 2: Enumeration and Authentication (Steps 4-5)**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[3:5]' (Enumeration through Authentication)
```

**Phase 3: Testing (Steps 6-7)**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[5:7]' (Manual Testing through Performance Validation)
```

**Phase 4: Documentation (Steps 8-9)**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[7:]' (Documentation through Audit Readiness)
```

---

## Advanced YAML Key Reference Patterns

### Execute Step with Specific Best Practices

```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[3]' and 'context.best_practices_references.core_fastapi', then execute Step 4 with FastAPI best practices review
```

### Execute Multiple Related Sections

```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[3]', 'instructions.steps[5]', and 'context.best_practices_references', then execute Steps 4 and 6 with best practices
```

### Execute with Conditional Logic

```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, index all steps, if enumeration phase then execute 'instructions.steps[3]' with 'context.best_practices_references.core_fastapi'
```

### Execute Testing Step with Security Focus

```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5]' and 'context.best_practices_references.security_compliance', then execute Step 6 with security best practices focus
```

### Execute with Scope Constraints

```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[1].outputs.scope_constraints' and 'instructions.steps[3]', then execute Step 4 with scope constraints applied
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
Execute @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml from the beginning
```

### Scenario 2: Re-execute Endpoint Enumeration Only
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, index all workflow steps, then execute only Step 4 with best practices focus: fastapi
```

### Scenario 3: Execute Only Manual Testing
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5].actions', and execute only manual testing workflow
```

### Scenario 4: Execute Testing with Security Focus
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5]' and 'context.best_practices_references.security_compliance', then execute Step 6 with security best practices focus
```

### Scenario 5: Execute Continuation Instruction Only
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'continuation_instruction', and execute that
```

### Scenario 6: Execute Enumeration Phase Only (Steps 4-5)
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[3:5]' (Enumeration through Authentication)
```

### Scenario 7: Execute Testing Phase Only (Steps 6-7)
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[5:7]' (Manual Testing through Performance Validation)
```

### Scenario 8: Execute Documentation Phase Only (Steps 8-9)
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[7:]' (Documentation through Audit Readiness)
```

---

## Quick Reference Cheat Sheet

| What You Want | Command Pattern |
|---------------|----------------|
| **Full execution** | `Execute @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml from the beginning` |
| **Continuation only** | `Follow the continuation_instruction from @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml` |
| **Specific step** | `Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[3]'` |
| **Endpoint enumeration** | `Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, index all workflow steps, then execute only Step 4 with best practices focus: fastapi` |
| **Manual testing** | `Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5].actions', and execute only manual testing workflow` |
| **Testing with security** | `Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5]' and 'context.best_practices_references.security_compliance', then execute Step 6` |
| **Multiple steps** | `Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[3:5]'` |
| **Best practices review** | `Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'context.best_practices_references', and review all best practices documents` |
| **Forbidden methods** | `Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5].forbidden_testing_methods', and review forbidden methods` |
| **Scope constraints** | `Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[1].outputs.scope_constraints', and review test scope constraints` |

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
  - MANUAL TESTING ONLY
  - NO scripted tests (pytest, unittest, Postman auto-run, etc.)
  - Test endpoints ONE AT A TIME
  - Remediate issues immediately before proceeding
  - NON-NEGOTIABLE

---

## Tips for Effective Execution

1. **Start with Parse**: Always parse the file first to understand its structure
2. **Use YAML Keys**: Reference exact YAML paths for precision
3. **Index Steps**: Use "index all workflow steps" to see available options
4. **Combine Sections**: Extract multiple related sections for complete context
5. **Include Best Practices**: Always include best practices review for Steps 4 and 6
6. **Follow Testing Rules**: Always respect the manual testing only rule for Step 6
7. **Follow Workflow Phases**: Consider executing in phases (Preparation → Enumeration → Testing → Documentation)
8. **Consider Scope Constraints**: Check for scope constraints in Step 2 before executing Step 4

---

## Troubleshooting

### Issue: YAML Key Not Found

**Solution**: Parse the file first to see actual structure:
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and show YAML structure
```

### Issue: Step Execution Missing Context

**Solution**: Include related sections:
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[3]' and 'context.best_practices_references.core_fastapi', then execute Step 4 with FastAPI best practices review
```

### Issue: Missing Best Practices Review

**Solution**: Always include best practices review for Steps 4 and 6:
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[3]' and 'context.best_practices_references.core_fastapi', then execute Step 4 with best practices review
```

### Issue: Testing Rule Violation

**Solution**: Always include critical testing rule when executing Step 6:
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5]' and 'context.critical_testing_rule', then execute Step 6 with manual testing enforcement
```

### Issue: Scope Constraints Not Applied

**Solution**: Include scope constraints from Step 2 when executing Step 4:
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[1].outputs.scope_constraints' and 'instructions.steps[3]', then execute Step 4 with scope constraints applied
```

---

## Workflow Phase Breakdown

### Phase 1: Preparation (Steps 1-3)
- **Step 1**: Review Canonical Documentation
- **Step 2**: Read Implementation Plan & Determine CURRENT Work
- **Step 3**: Verify API Server Status

**Execute Phase 1:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[0:3]'
```

### Phase 2: Enumeration and Authentication (Steps 4-5)
- **Step 4**: Enumerate All API Endpoints (with FastAPI best practices)
- **Step 5**: Prepare Authentication (If Required)

**Execute Phase 2:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[3:5]'
```

### Phase 3: Testing (Steps 6-7)
- **Step 6**: Manual Endpoint Testing (with security/testing best practices, MANUAL ONLY)
- **Step 7**: Performance Validation (If Baseline Available)

**Execute Phase 3:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[5:7]'
```

### Phase 4: Documentation (Steps 8-9)
- **Step 8**: Issue Collation & Documentation Update
- **Step 9**: Audit Readiness & Halt

**Execute Phase 4:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml and execute only 'instructions.steps[7:]'
```

---

## Manual Testing Workflow (Step 6)

Step 6 has a detailed sub-workflow for manual testing:

**STEP 6.1: Execute manual test sequence**
- Manually construct HTTP request (curl, Postman, MCP fetch)
- Manually execute the request
- Manually observe HTTP status code, response body, response time, Docker logs
- Simulate real-world flows: (i) list resources, (ii) fetch individual resource, (iii) create new resources, (iv) read created resources, (v) update resources, (vi) delete and verify removal

**STEP 6.2: Validate response**
- Compare HTTP status code with expected value
- Validate response body schema/structure
- Check response time against baseline/tolerance
- Review Docker logs for errors/warnings
- Verify response data matches expected format

**STEP 6.3: Identify issues**
- Document any errors, warnings, or unexpected behaviour
- Categorise issues (functional, performance, schema, etc.)
- Note severity (critical, high, medium, low)

**STEP 6.4: Remediate issues (if any found)**
- CRITICAL: STOP testing and remediate issues ONE AT A TIME
- Analyse root cause of each issue
- Fix code, configuration, or infrastructure issues
- Restart API server if necessary
- Re-execute the SAME endpoint test manually
- Verify fix resolves the issue
- Continue remediation cycle until test passes

**STEP 6.5: Mark test as passed**
- Only mark test as PASSED when all criteria met:
  * HTTP status code matches expected
  * Response body validates correctly
  * Response time within tolerance (if applicable)
  * Docker logs show 0 errors, 0 warnings
  * All issues remediated and verified

**STEP 6.6: Document results**
- Record test result (PASSED/FAILED)
- Document issues found and remediated
- Record response time and performance metrics
- Update SPEC file with test result

**STEP 6.7: Proceed to next endpoint**
- Only proceed to next endpoint after current test is PASSED
- If test fails after remediation attempts, escalate but do not skip

**Execute Step 6 Manual Testing:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5]', and execute Step 6 manual testing workflow
```

---

## Forbidden Testing Methods

When executing Step 6, these methods are FORBIDDEN:

- `pytest`, `unittest`, or any Python test framework
- Postman collections with auto-run or Newman
- Automated test scripts or batch test execution
- Test runners or CI/CD test pipelines
- Parallel or concurrent test execution
- Any form of automated test execution

**Review Forbidden Methods:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5].forbidden_testing_methods', and review forbidden methods
```

---

## Allowed Manual Testing Tools

When executing Step 6, these tools are ALLOWED:

- `curl` - Manual HTTP requests from command line
- `Postman` - Manual GUI-based API testing
- `mcp_fetch_fetch` - MCP tool for manual HTTP requests
- `Browser` - Manual GET requests and form submissions
- `docker logs` - Manual log inspection

**Review Allowed Tools:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[5].suggested_manual_testing_tools', and review allowed tools
```

---

## Scope Constraints

By default, ALL endpoints MUST be tested unless scope constraints are specified in Step 2. Scope constraints can be:
- Endpoint patterns (e.g., `/api/v1/auth/*`, `/api/v1/storage/*`)
- Endpoint categories (e.g., Authentication, Storage)
- Specific endpoint lists

**Review Scope Constraints:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[1].outputs.scope_constraints', and review test scope constraints
```

**Execute with Scope Constraints:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[1].outputs.scope_constraints' and 'instructions.steps[3]', then execute Step 4 with scope constraints applied
```

---

## Performance Validation

Step 7 validates performance if baseline data is available:
- Compare response times against baseline
- Identify performance regressions (>20% degradation)
- Remediate performance regressions before marking test suite complete

**Execute Performance Validation:**
```
Parse @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml, extract 'instructions.steps[6]', and execute Step 7 performance validation
```

---

**Last Updated**: 2025-12-15
**File**: `11-Manual_API_Endpoint_Regression_Testing.yaml`
**Version**: 1.0.0
