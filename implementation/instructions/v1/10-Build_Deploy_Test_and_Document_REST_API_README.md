# Build, Deploy, Test and Document REST API - Execution Guide

This guide provides comprehensive methods for executing `10-Build_Deploy_Test_and_Document_REST_API.yaml`, including full execution and selective parsing by YAML key references.

## Quick Start

### Full Execution (First Time)
```
Execute @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml from the beginning
```

### Continuation Instruction (Subsequent Use)
```
Follow the continuation_instruction from @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml
```

### Selective Parsing (Recommended for Re-execution)
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only the 'instructions.steps[2]' section (Build and Deploy Locally)
```

---

## Execution Methods

### Method 1: Full Execution from Beginning

**Use Case**: First-time execution, need complete context

**Command:**
```
Execute @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml from the beginning
```

**Alternative Formats:**
```
Execute @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml
Load and execute @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml
Follow @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml starting from step 1
```

**What Happens:**
- Loads entire instruction file
- Reads all sections (context, workflow, best practices, etc.)
- Follows all 8 workflow steps sequentially
- Applies all validation checkpoints
- Builds and deploys containers locally
- Tests REST endpoints manually one at a time

---

### Method 2: Continuation Instruction Execution

**Use Case**: File context already available, quick execution

**Command:**
```
Follow the continuation_instruction from @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml
```

**Alternative Formats:**
```
Execute per continuation_instruction in @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml
Continue per @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml continuation_instruction
```

**What Happens:**
- Uses `continuation_instruction` section directly (lines 380-479)
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
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only the 'instructions.steps[0]' section (Review Canonical Documentation)
```

**Step 2 (Read Implementation Plan & Determine CURRENT Work):**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only the 'instructions.steps[1]' section (Read Implementation Plan & Determine CURRENT Work)
```

**Step 3 (Build and Deploy Locally):**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only the 'instructions.steps[2]' section (Build and Deploy Locally)
```

**Step 4 (Initial Runtime Verification):**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only the 'instructions.steps[3]' section (Initial Runtime Verification)
```

**Step 5 (REST API Enumeration):**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only the 'instructions.steps[4]' section (REST API Enumeration)
```

**Step 6 (Manual Functional REST Testing):**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only the 'instructions.steps[5]' section (Manual Functional REST Testing)
```

**Step 7 (Issue Collation & Documentation Update):**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only the 'instructions.steps[6]' section (Issue Collation & Documentation Update)
```

**Step 8 (Audit Readiness & Halt):**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only the 'instructions.steps[7]' section (Audit Readiness & Halt)
```

---

### Method 5: Parse, Index, and Execute with Best Practices Focus

**Use Case**: Execute steps with specific best practices review

**Build and Deploy with Docker Best Practices:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, index all workflow steps, then execute only Step 3 with best practices focus: docker_containerization
```

**Endpoint Enumeration with FastAPI Best Practices:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, index all workflow steps, then execute only Step 5 with best practices focus: fastapi
```

**Testing with Security Best Practices:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, index all workflow steps, then execute only Step 6 with best practices focus: security
```

---

### Method 6: Parse and Extract Specific YAML Sections

**Use Case**: Execute specific actions or subsections

**Extract Step 3 Build Actions Only:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[2].actions', and execute only those actions
```

**Extract Step 6 Manual Testing Actions:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5].actions', and execute only manual testing workflow
```

**Extract Suggested Commands:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[2].suggested_commands', and execute build commands
```

**Extract Forbidden Testing Methods:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5].forbidden_testing_methods', and review forbidden methods
```

**Extract Best Practices References:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'context.best_practices_references', and review all best practices documents
```

**Extract Examples Section:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'examples', and review build/deploy/testing examples
```

---

### Method 7: Parse Multiple Steps

**Use Case**: Execute a range of steps

**Steps 1-3 (Review through Build and Deploy):**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[0:3]' (Steps 1-3)
```

**Steps 3-5 (Build through Enumeration):**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[2:5]' (Steps 3-5)
```

**From Step 5 Onwards (Enumeration onwards):**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[4:]' (From Step 5 onwards)
```

**Steps 3, 5, and 6 (Build, Enumeration, Testing):**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[2]', 'instructions.steps[4]', and 'instructions.steps[5]' (Steps 3, 5, and 6)
```

---

### Method 8: Parse with Best Practices Focus

**Use Case**: Execute with emphasis on specific best practices

**Docker Best Practices:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract Step 3 and 'context.best_practices_references.configuration_deployment', and execute Step 3 with Docker best practices focus
```

**FastAPI Best Practices:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract Step 5 and 'context.best_practices_references.core_fastapi', and execute Step 5 with FastAPI best practices focus
```

**Security Best Practices:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract Step 6 and 'context.best_practices_references.security_compliance', and execute Step 6 with security best practices focus
```

**All Best Practices:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract all 'best_practices_references' sections, and execute with all best practices review
```

---

### Method 9: Parse Continuation Instruction Only

**Use Case**: Quick execution using continuation instruction without full file load

**Command:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'continuation_instruction' section, and execute that
```

**Alternative:**
```
Read @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract continuation_instruction (lines 380-479), and execute that
```

---

## YAML Structure Reference

Understanding the YAML structure helps you reference specific sections precisely:

```yaml
10-Build_Deploy_Test_and_Document_REST_API.yaml
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
    └── steps[0-7]
        ├── step (number)
        ├── name
        ├── actions
        ├── gates (some steps)
        ├── outputs (some steps)
        ├── suggested_commands (Steps 3, 4, 6)
        ├── suggested_manual_testing_tools (Step 6)
        ├── forbidden_testing_methods (Step 6)
        └── outputs (Step 6)
├── constraints
├── examples
│   ├── build_deploy_example
│   ├── endpoint_matrix_example
│   ├── manual_testing_example
│   ├── test_result_example
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
- **Step 3**: `instructions.steps[2]` - Build and Deploy Locally
- **Step 4**: `instructions.steps[3]` - Initial Runtime Verification
- **Step 5**: `instructions.steps[4]` - REST API Enumeration
- **Step 6**: `instructions.steps[5]` - Manual Functional REST Testing
- **Step 7**: `instructions.steps[6]` - Issue Collation & Documentation Update
- **Step 8**: `instructions.steps[7]` - Audit Readiness & Halt

### Best Practices References

- **All Best Practices**: `context.best_practices_references`
- **Core FastAPI**: `context.best_practices_references.core_fastapi`
- **Security**: `context.best_practices_references.security_compliance`
- **Docker/Configuration**: `context.best_practices_references.configuration_deployment`
- **Testing**: `context.best_practices_references.code_quality_testing`

### Actions and Outputs

- **Step 3 Actions**: `instructions.steps[2].actions`
- **Step 3 Suggested Commands**: `instructions.steps[2].suggested_commands`
- **Step 6 Actions**: `instructions.steps[5].actions`
- **Step 6 Forbidden Methods**: `instructions.steps[5].forbidden_testing_methods`
- **Step 6 Outputs**: `instructions.steps[5].outputs`
- **Step 2 Outputs**: `instructions.steps[1].outputs`

### Critical Rules

- **Documentation Rule**: `context.critical_documentation_rule`
- **Testing Rule**: `context.critical_testing_rule`

### Examples

- **All Examples**: `examples`
- **Build Deploy Example**: `examples.build_deploy_example`
- **Manual Testing Example**: `examples.manual_testing_example`
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
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, index all workflow steps and YAML structure, then execute only 'instructions.steps[2]' with best practices focus: docker_containerization
```

### Pattern 2: Extract and Execute Specific Section

**Workflow:**
1. Extract specific YAML section
2. Execute only that section

**Example:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5].actions', and execute only manual testing workflow
```

### Pattern 3: Parse with Context, Execute Selectively

**Workflow:**
1. Parse file with full context
2. Reference specific keys for execution

**Example:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml with full context, then execute only 'instructions.steps[2].actions' with 'context.best_practices_references.configuration_deployment' applied
```

### Pattern 4: Execute Build/Deploy/Test Phases

**Phase 1: Preparation (Steps 1-2)**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[0:2]' (Review Documentation through Determine Current Work)
```

**Phase 2: Build and Deploy (Steps 3-4)**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[2:4]' (Build and Deploy through Runtime Verification)
```

**Phase 3: Testing (Steps 5-6)**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[4:6]' (Enumeration through Testing)
```

**Phase 4: Documentation (Steps 7-8)**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[6:]' (Documentation through Audit Readiness)
```

---

## Advanced YAML Key Reference Patterns

### Execute Step with Specific Best Practices

```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[2]' and 'context.best_practices_references.configuration_deployment', then execute Step 3 with Docker best practices review
```

### Execute Multiple Related Sections

```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[2]', 'instructions.steps[5]', and 'context.best_practices_references', then execute Steps 3 and 6 with best practices
```

### Execute with Conditional Logic

```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, index all steps, if build phase then execute 'instructions.steps[2]' with 'context.best_practices_references.configuration_deployment'
```

### Execute Testing Step with Security Focus

```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5]' and 'context.best_practices_references.security_compliance', then execute Step 6 with security best practices focus
```

### Execute Enumeration with FastAPI Focus

```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[4]' and 'context.best_practices_references.core_fastapi', then execute Step 5 with FastAPI best practices focus
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
2. **Use Precise Keys**: Reference exact YAML paths (e.g., `instructions.steps[2]` not "step 3")
3. **Include Context**: When extracting sections, include necessary dependencies (e.g., best practices review with actions)
4. **Index Workflow Steps**: Use "index all workflow steps" to understand available steps before execution
5. **Reference Best Practices**: Always include best practices review sections when executing Steps 3, 5, or 6
6. **Follow Testing Rules**: Always include `critical_testing_rule` when executing Step 6

---

## Common Execution Scenarios

### Scenario 1: First-Time Execution
```
Execute @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml from the beginning
```

### Scenario 2: Re-execute Build and Deploy Only
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, index all workflow steps, then execute only Step 3 with best practices focus: docker_containerization
```

### Scenario 3: Execute Only Manual Testing
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5].actions', and execute only manual testing workflow
```

### Scenario 4: Execute Testing with Security Focus
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5]' and 'context.best_practices_references.security_compliance', then execute Step 6 with security best practices focus
```

### Scenario 5: Execute Continuation Instruction Only
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'continuation_instruction', and execute that
```

### Scenario 6: Execute Build Phase Only (Steps 3-4)
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[2:4]' (Build and Deploy through Runtime Verification)
```

### Scenario 7: Execute Testing Phase Only (Steps 5-6)
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[4:6]' (Enumeration through Testing)
```

### Scenario 8: Execute Documentation Phase Only (Steps 7-8)
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[6:]' (Documentation through Audit Readiness)
```

---

## Quick Reference Cheat Sheet

| What You Want | Command Pattern |
|---------------|----------------|
| **Full execution** | `Execute @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml from the beginning` |
| **Continuation only** | `Follow the continuation_instruction from @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml` |
| **Specific step** | `Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[2]'` |
| **Build and deploy** | `Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, index all workflow steps, then execute only Step 3 with best practices focus: docker_containerization` |
| **Manual testing** | `Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5].actions', and execute only manual testing workflow` |
| **Testing with security** | `Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5]' and 'context.best_practices_references.security_compliance', then execute Step 6` |
| **Multiple steps** | `Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[2:4]'` |
| **Best practices review** | `Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'context.best_practices_references', and review all best practices documents` |
| **Forbidden methods** | `Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5].forbidden_testing_methods', and review forbidden methods` |

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
5. **Include Best Practices**: Always include best practices review for Steps 3, 5, and 6
6. **Follow Testing Rules**: Always respect the manual testing only rule for Step 6
7. **Follow Workflow Phases**: Consider executing in phases (Preparation → Build/Deploy → Testing → Documentation)

---

## Troubleshooting

### Issue: YAML Key Not Found

**Solution**: Parse the file first to see actual structure:
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and show YAML structure
```

### Issue: Step Execution Missing Context

**Solution**: Include related sections:
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[2]' and 'context.best_practices_references.configuration_deployment', then execute Step 3 with Docker best practices review
```

### Issue: Missing Best Practices Review

**Solution**: Always include best practices review for Steps 3, 5, and 6:
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[2]' and 'context.best_practices_references.configuration_deployment', then execute Step 3 with best practices review
```

### Issue: Testing Rule Violation

**Solution**: Always include critical testing rule when executing Step 6:
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5]' and 'context.critical_testing_rule', then execute Step 6 with manual testing enforcement
```

---

## Workflow Phase Breakdown

### Phase 1: Preparation (Steps 1-2)
- **Step 1**: Review Canonical Documentation
- **Step 2**: Read Implementation Plan & Determine CURRENT Work

**Execute Phase 1:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[0:2]'
```

### Phase 2: Build and Deploy (Steps 3-4)
- **Step 3**: Build and Deploy Locally (with Docker best practices)
- **Step 4**: Initial Runtime Verification

**Execute Phase 2:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[2:4]'
```

### Phase 3: Testing (Steps 5-6)
- **Step 5**: REST API Enumeration (with FastAPI best practices)
- **Step 6**: Manual Functional REST Testing (with security/testing best practices, MANUAL ONLY)

**Execute Phase 3:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[4:6]'
```

### Phase 4: Documentation (Steps 7-8)
- **Step 7**: Issue Collation & Documentation Update
- **Step 8**: Audit Readiness & Halt

**Execute Phase 4:**
```
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml and execute only 'instructions.steps[6:]'
```

---

## Manual Testing Workflow (Step 6)

Step 6 has a detailed sub-workflow for manual testing:

**STEP 6.1: Execute manual test**
- Manually construct HTTP request (curl, Postman, MCP fetch)
- Manually execute the request
- Manually observe HTTP status code, response body, response time, Docker logs

**STEP 6.2: Validate response**
- Compare HTTP status code with expected value
- Validate response body schema/structure
- Check response time against baseline/tolerance
- Review Docker logs for errors/warnings

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
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5]', and execute Step 6 manual testing workflow
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
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5].forbidden_testing_methods', and review forbidden methods
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
Parse @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml, extract 'instructions.steps[5].suggested_manual_testing_tools', and review allowed tools
```

---

**Last Updated**: 2025-12-15
**File**: `10-Build_Deploy_Test_and_Document_REST_API.yaml`
**Version**: 1.0.0
