# Debug and Troubleshoot Codebase - Execution Guide

This guide provides comprehensive methods for executing `08-Debug_And_Troubleshoot_Codebase.yaml`, including full execution and selective parsing by YAML key references.

## Quick Start

### Full Execution (First Time)
```
Execute @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml from the beginning
```

### Continuation Instruction (Subsequent Use)
```
Follow the continuation_instruction from @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml
```

### Selective Parsing (Recommended for Re-execution)
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only the 'instructions.steps[2]' section (Root Cause Analysis)
```

---

## Execution Methods

### Method 1: Full Execution from Beginning

**Use Case**: First-time execution, need complete context

**Command:**
```
Execute @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml from the beginning
```

**Alternative Formats:**
```
Execute @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml
Load and execute @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml
Follow @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml starting from step 1
```

**What Happens:**
- Loads entire instruction file
- Reads all sections (context, workflow, best practices, etc.)
- Follows all 11 workflow steps sequentially
- Applies all validation checkpoints
- Creates DEBUG_TROUBLESHOOTING_SPEC document

---

### Method 2: Continuation Instruction Execution

**Use Case**: File context already available, quick execution

**Command:**
```
Follow the continuation_instruction from @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml
```

**Alternative Formats:**
```
Execute per continuation_instruction in @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml
Continue per @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml continuation_instruction
```

**What Happens:**
- Uses `continuation_instruction` section directly (lines 511-638)
- Follows summarized workflow steps
- Applies all best practices requirements
- Enforces validation checkpoints

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

**Step 1 (Issue Identification and Context Gathering):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only the 'instructions.steps[0]' section (Issue Identification and Context Gathering)
```

**Step 2 (Issue Reproduction):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only the 'instructions.steps[1]' section (Issue Reproduction)
```

**Step 3 (Root Cause Analysis):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only the 'instructions.steps[2]' section (Root Cause Analysis)
```

**Step 4 (Create DEBUG_TROUBLESHOOTING_SPEC):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only the 'instructions.steps[3]' section (Create DEBUG_TROUBLESHOOTING_SPEC)
```

**Step 5 (Solution Design):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only the 'instructions.steps[4]' section (Solution Design)
```

**Step 6 (Controlled Fix Implementation):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only the 'instructions.steps[5]' section (Controlled Fix Implementation)
```

**Step 7 (Fix Validation and Testing):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only the 'instructions.steps[6]' section (Fix Validation and Testing)
```

**Step 8 (Regression Prevention):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only the 'instructions.steps[7]' section (Regression Prevention)
```

**Step 9 (Post-Resolution Documentation):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only the 'instructions.steps[8]' section (Post-Resolution Documentation)
```

**Step 10 (Persistence and Audit Logging):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only the 'instructions.steps[9]' section (Persistence and Audit Logging)
```

**Step 11 (Completion and Verification):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only the 'instructions.steps[10]' section (Completion and Verification)
```

---

### Method 5: Parse, Index, and Execute with Issue Type

**Use Case**: Execute Step 3 (Root Cause Analysis) with specific issue type best practices review

**Error Handling Issues:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, index all workflow steps, then execute only Step 3 with issue type: error_handling
```

**Performance Issues:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, index all workflow steps, then execute only Step 3 with issue type: performance
```

**Security Issues:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, index all workflow steps, then execute only Step 3 with issue type: security
```

**Observability Issues:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, index all workflow steps, then execute only Step 3 with issue type: observability
```

---

### Method 6: Parse and Extract Specific YAML Sections

**Use Case**: Execute specific actions or subsections

**Extract Step 3 Root Cause Analysis Actions Only:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[2].actions', and execute only those actions
```

**Extract Step 3 Best Practices Review:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[2].best_practices_review', and execute only the best practices review
```

**Extract Error Handling Best Practices:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[2].best_practices_review.issue_specific_reviews.error_handling', and execute only that review
```

**Extract Step 5 Solution Design with Best Practices:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[4]' and 'instructions.steps[4].best_practices_review', then execute Step 5 with best practices applied
```

**Extract Step 6 Fix Implementation with Best Practices:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[5]' and 'instructions.steps[5].best_practices_review', then execute Step 6 with best practices applied
```

**Extract Codebase Scaffolding Mandate:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'codebase_scaffolding_mandate', and execute only the scaffolding workflow
```

**Extract Best Practices References:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'context.best_practices_references', and review all best practices documents
```

**Extract Examples Section:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'examples', and review debugging examples
```

---

### Method 7: Parse Multiple Steps

**Use Case**: Execute a range of steps

**Steps 1-3 (Issue Identification through Root Cause Analysis):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[0:3]' (Steps 1-3)
```

**Steps 3-6 (Root Cause Analysis through Fix Implementation):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[2:6]' (Steps 3-6)
```

**From Step 5 Onwards (Solution Design onwards):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[4:]' (From Step 5 onwards)
```

**Steps 3, 5, and 6 (Root Cause, Solution Design, Fix Implementation):**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[2]', 'instructions.steps[4]', and 'instructions.steps[5]' (Steps 3, 5, and 6)
```

---

### Method 8: Parse with Best Practices Focus

**Use Case**: Execute with emphasis on specific best practices

**Error Handling Best Practices:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract Step 3 'best_practices_review.issue_specific_reviews.error_handling', and execute Step 3 with error handling best practices focus
```

**Performance Best Practices:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract Step 3 'best_practices_review.issue_specific_reviews.performance', and execute Step 3 with performance best practices focus
```

**Security Best Practices:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract Step 3 'best_practices_review.issue_specific_reviews.security', and execute Step 3 with security best practices focus
```

**All Best Practices:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract all 'best_practices_review' sections, and execute with all best practices review
```

---

### Method 9: Parse Continuation Instruction Only

**Use Case**: Quick execution using continuation instruction without full file load

**Command:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'continuation_instruction' section, and execute that
```

**Alternative:**
```
Read @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract continuation_instruction (lines 511-638), and execute that
```

---

## YAML Structure Reference

Understanding the YAML structure helps you reference specific sections precisely:

```yaml
08-Debug_And_Troubleshoot_Codebase.yaml
├── prompt_name
├── version
├── type
├── context
│   ├── role
│   ├── governance
│   ├── description
│   ├── critical_documentation_rule
│   ├── doc_references
│   └── best_practices_references
│       ├── core_fastapi
│       ├── async_performance
│       ├── reliability_resilience
│       ├── architecture_patterns
│       ├── security_compliance
│       ├── observability_monitoring
│       ├── data_persistence
│       ├── configuration_deployment
│       ├── background_tasks
│       ├── integration_patterns
│       ├── ui_integration
│       ├── code_quality_testing
│       └── templating_scaffolding
├── codebase_scaffolding_mandate
│   ├── priority
│   ├── description
│   ├── priority_hierarchy
│   └── instructions
│       └── workflow
│           ├── step_1_search
│           ├── step_2_document
│           ├── step_3_clone_bulk
│           ├── step_4_scaffold
│           ├── step_5_delete
│           ├── step_6_validate
│           └── step_7_update_spec
└── instructions
    ├── objective
    ├── best_practices_requirement
    └── steps[0-10]
        ├── step (number)
        ├── name
        ├── best_practices_review (Steps 3, 5, 6 only)
        │   ├── mandatory
        │   ├── requirement
        │   ├── issue_specific_reviews (Step 3 only)
        │   │   ├── error_handling
        │   │   ├── performance
        │   │   ├── security
        │   │   └── observability
        │   └── design_guidance / implementation_guidance (Steps 5, 6)
        ├── actions
        ├── expected_outcome
        ├── success_criteria (Step 7 only)
        └── enforcement (Step 6 only)
├── constraints
├── examples
│   ├── debugging_example_1
│   ├── debugging_example_2
│   └── debugging_example_3
├── output_format
├── execution_protocol
├── metadata
└── continuation_instruction
```

---

## YAML Key Reference Examples

### Step References (0-indexed)

- **Step 1**: `instructions.steps[0]` - Issue Identification and Context Gathering
- **Step 2**: `instructions.steps[1]` - Issue Reproduction
- **Step 3**: `instructions.steps[2]` - Root Cause Analysis
- **Step 4**: `instructions.steps[3]` - Create DEBUG_TROUBLESHOOTING_SPEC
- **Step 5**: `instructions.steps[4]` - Solution Design
- **Step 6**: `instructions.steps[5]` - Controlled Fix Implementation
- **Step 7**: `instructions.steps[6]` - Fix Validation and Testing
- **Step 8**: `instructions.steps[7]` - Regression Prevention
- **Step 9**: `instructions.steps[8]` - Post-Resolution Documentation
- **Step 10**: `instructions.steps[9]` - Persistence and Audit Logging
- **Step 11**: `instructions.steps[10]` - Completion and Verification

### Best Practices References

- **All Best Practices**: `context.best_practices_references`
- **Core FastAPI**: `context.best_practices_references.core_fastapi`
- **Security**: `context.best_practices_references.security_compliance`
- **Step 3 Best Practices**: `instructions.steps[2].best_practices_review`
- **Step 3 Error Handling Review**: `instructions.steps[2].best_practices_review.issue_specific_reviews.error_handling`
- **Step 3 Performance Review**: `instructions.steps[2].best_practices_review.issue_specific_reviews.performance`
- **Step 3 Security Review**: `instructions.steps[2].best_practices_review.issue_specific_reviews.security`
- **Step 3 Observability Review**: `instructions.steps[2].best_practices_review.issue_specific_reviews.observability`
- **Step 5 Best Practices**: `instructions.steps[4].best_practices_review`
- **Step 6 Best Practices**: `instructions.steps[5].best_practices_review`

### Codebase Scaffolding

- **Scaffolding Mandate**: `codebase_scaffolding_mandate`
- **Scaffolding Workflow**: `codebase_scaffolding_mandate.instructions.workflow`
- **Step 1 Search**: `codebase_scaffolding_mandate.instructions.workflow.step_1_search`

### Actions and Outcomes

- **Step 3 Actions**: `instructions.steps[2].actions`
- **Step 3 Expected Outcome**: `instructions.steps[2].expected_outcome`
- **Step 7 Success Criteria**: `instructions.steps[6].success_criteria`
- **Step 6 Enforcement**: `instructions.steps[5].enforcement`

### Examples

- **All Examples**: `examples`
- **Example 1**: `examples.debugging_example_1`
- **Example 2**: `examples.debugging_example_2`
- **Example 3**: `examples.debugging_example_3`

---

## Recommended Execution Patterns

### Pattern 1: Parse First, Then Execute (Recommended)

**Workflow:**
1. Parse the entire file to understand structure
2. Index all workflow steps
3. Execute full file OR reference specific YAML keys

**Example:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, index all workflow steps and YAML structure, then execute only 'instructions.steps[2]' with issue type: error_handling
```

### Pattern 2: Extract and Execute Specific Section

**Workflow:**
1. Extract specific YAML section
2. Execute only that section

**Example:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[2].best_practices_review.issue_specific_reviews.error_handling', and execute only that review
```

### Pattern 3: Parse with Context, Execute Selectively

**Workflow:**
1. Parse file with full context
2. Reference specific keys for execution

**Example:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml with full context, then execute only 'instructions.steps[2].actions' with 'instructions.steps[2].best_practices_review.issue_specific_reviews.error_handling' applied
```

### Pattern 4: Execute Debugging Workflow Phases

**Phase 1: Issue Analysis (Steps 1-3)**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[0:3]' (Issue Identification through Root Cause Analysis)
```

**Phase 2: Solution Design and Implementation (Steps 4-6)**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[3:6]' (Create SPEC through Fix Implementation)
```

**Phase 3: Validation and Documentation (Steps 7-11)**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[6:]' (Validation through Completion)
```

---

## Advanced YAML Key Reference Patterns

### Execute Step with Specific Best Practices

```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[2]' and 'instructions.steps[2].best_practices_review.issue_specific_reviews.error_handling', then execute Step 3 with error handling best practices review
```

### Execute Multiple Related Sections

```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[2]', 'instructions.steps[4]', 'instructions.steps[5]', and 'codebase_scaffolding_mandate', then execute Steps 3, 5, and 6 with scaffolding and best practices
```

### Execute with Conditional Logic

```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, index all steps, if issue type is error_handling then execute 'instructions.steps[2]' with 'instructions.steps[2].best_practices_review.issue_specific_reviews.error_handling'
```

### Execute Solution Design with Best Practices

```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[4]' and 'instructions.steps[4].best_practices_review', then execute Step 5 (Solution Design) with best practices patterns applied
```

### Execute Fix Implementation with Best Practices

```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[5]' and 'instructions.steps[5].best_practices_review', then execute Step 6 (Controlled Fix Implementation) with best practices patterns applied
```

---

## Comparison: Full Load vs Selective Parsing

| Aspect | Full Load | Selective Parsing |
|--------|-----------|-------------------|
| **Speed** | Slower | Faster |
| **Token Usage** | Higher | Lower |
| **Context** | Complete | Focused |
| **Best For** | First-time execution | Re-execution, debugging specific steps |
| **Precision** | Broad | Precise |
| **Dependencies** | All loaded | Only needed sections |

---

## Best Practices for Selective Parsing

1. **Always Parse First**: Parse the entire file to understand structure before referencing keys
2. **Use Precise Keys**: Reference exact YAML paths (e.g., `instructions.steps[2]` not "step 3")
3. **Include Context**: When extracting sections, include necessary dependencies (e.g., best practices review with actions)
4. **Index Workflow Steps**: Use "index all workflow steps" to understand available steps before execution
5. **Reference Issue Types**: Use issue type references for Step 3 (e.g., `issue type: error_handling`)
6. **Include Best Practices**: Always include best practices review sections when executing Steps 3, 5, or 6

---

## Common Execution Scenarios

### Scenario 1: First-Time Execution
```
Execute @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml from the beginning
```

### Scenario 2: Re-execute Root Cause Analysis for Error Handling Issue
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, index all workflow steps, then execute only Step 3 with issue type: error_handling
```

### Scenario 3: Execute Only Best Practices Review
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[2].best_practices_review.issue_specific_reviews.error_handling', and execute only that review
```

### Scenario 4: Execute Solution Design with Security Focus
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[4]' and 'instructions.steps[4].best_practices_review', then execute Step 5 with security best practices focus
```

### Scenario 5: Execute Continuation Instruction Only
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'continuation_instruction', and execute that
```

### Scenario 6: Execute Issue Analysis Phase (Steps 1-3)
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[0:3]' (Issue Identification through Root Cause Analysis)
```

### Scenario 7: Execute Fix Implementation Phase (Steps 5-6)
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[4:6]' (Solution Design through Fix Implementation)
```

### Scenario 8: Execute Validation Phase (Steps 7-11)
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[6:]' (Validation through Completion)
```

---

## Quick Reference Cheat Sheet

| What You Want | Command Pattern |
|---------------|----------------|
| **Full execution** | `Execute @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml from the beginning` |
| **Continuation only** | `Follow the continuation_instruction from @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml` |
| **Specific step** | `Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[2]'` |
| **Step with issue type** | `Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, index all workflow steps, then execute only Step 3 with issue type: error_handling` |
| **Best practices review** | `Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[2].best_practices_review.issue_specific_reviews.error_handling', and execute only that review` |
| **Multiple steps** | `Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[0:3]'` |
| **Solution design** | `Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[4]' and 'instructions.steps[4].best_practices_review', then execute Step 5` |
| **Fix implementation** | `Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[5]' and 'instructions.steps[5].best_practices_review', then execute Step 6` |
| **Scaffolding mandate** | `Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'codebase_scaffolding_mandate', and execute only the scaffolding workflow` |

---

## Issue Type Reference

When executing Step 3 (Root Cause Analysis) or referencing best practices, use these exact issue type names:

- `error_handling` - Error handling and resilience issues
- `performance` - Performance and resource management issues
- `security` - Security and authentication issues
- `observability` - Observability and monitoring issues

---

## Tips for Effective Execution

1. **Start with Parse**: Always parse the file first to understand its structure
2. **Use YAML Keys**: Reference exact YAML paths for precision
3. **Index Steps**: Use "index all workflow steps" to see available options
4. **Combine Sections**: Extract multiple related sections for complete context
5. **Specify Issue Types**: For Step 3, always specify issue type for best practices alignment
6. **Include Dependencies**: When extracting actions, include best practices review sections
7. **Follow Workflow Phases**: Consider executing debugging workflow in phases (Analysis → Design → Implementation → Validation)

---

## Troubleshooting

### Issue: YAML Key Not Found

**Solution**: Parse the file first to see actual structure:
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and show YAML structure
```

### Issue: Step Execution Missing Context

**Solution**: Include related sections:
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[2]' and 'instructions.steps[2].best_practices_review', then execute Step 3 with best practices review
```

### Issue: Issue Type Not Recognized

**Solution**: Use exact issue type names from YAML:
- `error_handling`
- `performance`
- `security`
- `observability`

### Issue: Missing Best Practices Review

**Solution**: Always include best practices review for Steps 3, 5, and 6:
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml, extract 'instructions.steps[2]' and 'instructions.steps[2].best_practices_review', then execute Step 3 with best practices review
```

---

## Workflow Phase Breakdown

### Phase 1: Issue Analysis (Steps 1-3)
- **Step 1**: Issue Identification and Context Gathering
- **Step 2**: Issue Reproduction
- **Step 3**: Root Cause Analysis (with best practices review)

**Execute Phase 1:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[0:3]'
```

### Phase 2: Solution Design and Implementation (Steps 4-6)
- **Step 4**: Create DEBUG_TROUBLESHOOTING_SPEC
- **Step 5**: Solution Design (with best practices review)
- **Step 6**: Controlled Fix Implementation (with best practices review)

**Execute Phase 2:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[3:6]'
```

### Phase 3: Validation and Documentation (Steps 7-11)
- **Step 7**: Fix Validation and Testing
- **Step 8**: Regression Prevention
- **Step 9**: Post-Resolution Documentation
- **Step 10**: Persistence and Audit Logging
- **Step 11**: Completion and Verification

**Execute Phase 3:**
```
Parse @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml and execute only 'instructions.steps[6:]'
```

---

**Last Updated**: 2025-12-15
**File**: `08-Debug_And_Troubleshoot_Codebase.yaml`
**Version**: 1.2.0
