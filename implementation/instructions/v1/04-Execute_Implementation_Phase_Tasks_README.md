# Execute Implementation Phase Tasks - Execution Guide

This guide provides comprehensive methods for executing `04-Execute_Implementation_Phase_Tasks.yaml`, including full execution and selective parsing by YAML key references.

## Quick Start

### Full Execution (First Time)
```
Execute @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml from the beginning
```

### Continuation Instruction (Subsequent Use)
```
Follow the continuation_instruction from @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml
```

### Selective Parsing (Recommended for Re-execution)
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml and execute only the 'instructions.steps[2]' section (Execute Current Task(s))
```

---

## Execution Methods

### Method 1: Full Execution from Beginning

**Use Case**: First-time execution, need complete context

**Command:**
```
Execute @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml from the beginning
```

**Alternative Formats:**
```
Execute @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml
Load and execute @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml
Follow @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml starting from step 1
```

**What Happens:**
- Loads entire instruction file
- Reads all sections (context, workflow, best practices, etc.)
- Follows all 5 workflow steps sequentially
- Applies all validation checkpoints

---

### Method 2: Continuation Instruction Execution

**Use Case**: File context already available, quick execution

**Command:**
```
Follow the continuation_instruction from @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml
```

**Alternative Formats:**
```
Execute per continuation_instruction in @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml
Continue per @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml continuation_instruction
```

**What Happens:**
- Uses `continuation_instruction` section directly (lines 343-477)
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

**Step 1 (Review Canonical Documentation Standards):**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml and execute only the 'instructions.steps[0]' section (Review Canonical Documentation Standards)
```

**Step 2 (Audit Implementation Plan):**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml and execute only the 'instructions.steps[1]' section (Audit Implementation Plan)
```

**Step 3 (Execute Current Task(s)):**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml and execute only the 'instructions.steps[2]' section (Execute Current Task(s))
```

**Step 4 (Advance if Phase Complete):**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml and execute only the 'instructions.steps[3]' section (Advance if Phase Complete)
```

**Step 5 (Reconcile and Finalise Checklists):**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml and execute only the 'instructions.steps[4]' section (Reconcile and Finalise Checklists)
```

---

### Method 5: Parse, Index, and Execute with Task Type

**Use Case**: Execute Step 3 with specific task type best practices review

**FastAPI Endpoints:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all workflow steps, then execute only Step 3 with task type: fastapi_endpoints
```

**Async/Performance:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all workflow steps, then execute only Step 3 with task type: async_performance
```

**Error Handling:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all workflow steps, then execute only Step 3 with task type: error_handling
```

**Database Operations:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all workflow steps, then execute only Step 3 with task type: database_operations
```

**Security/Authentication:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all workflow steps, then execute only Step 3 with task type: security_authentication
```

**Caching:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all workflow steps, then execute only Step 3 with task type: caching
```

**Background Tasks:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all workflow steps, then execute only Step 3 with task type: background_tasks
```

**Testing:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all workflow steps, then execute only Step 3 with task type: testing
```

**Observability:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all workflow steps, then execute only Step 3 with task type: observability
```

---

### Method 6: Parse and Extract Specific YAML Sections

**Use Case**: Execute specific actions or subsections

**Extract Step 3 Actions Only:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'instructions.steps[2].actions', and execute only those actions
```

**Extract Step 3 Best Practices Review:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'instructions.steps[2].best_practices_review', and execute only the best practices review
```

**Extract FastAPI Endpoints Best Practices:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'instructions.steps[2].best_practices_review.task_specific_reviews.fastapi_endpoints', and execute only that review
```

**Extract Codebase Scaffolding Mandate:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'codebase_scaffolding_mandate', and execute only the scaffolding workflow
```

**Extract Best Practices References:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'context.best_practices_references', and review all best practices documents
```

---

### Method 7: Parse Multiple Steps

**Use Case**: Execute a range of steps

**Steps 1-3:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml and execute only 'instructions.steps[0:3]' (Steps 1-3)
```

**From Step 3 Onwards:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml and execute only 'instructions.steps[2:]' (From Step 3 onwards)
```

**Steps 2 and 3:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml and execute only 'instructions.steps[1]' and 'instructions.steps[2]' (Steps 2 and 3)
```

---

### Method 8: Parse with Best Practices Focus

**Use Case**: Execute with emphasis on specific best practices

**FastAPI Best Practices:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract Step 1 'best_practices_review' for FastAPI, and execute Step 1 with FastAPI best practices focus
```

**Security Best Practices:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract Step 3 'best_practices_review.task_specific_reviews.security_authentication', and execute Step 3 with security best practices focus
```

**All Best Practices:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract all 'best_practices_review' sections, and execute with all best practices review
```

---

### Method 9: Parse Continuation Instruction Only

**Use Case**: Quick execution using continuation instruction without full file load

**Command:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'continuation_instruction' section, and execute that
```

**Alternative:**
```
Read @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract continuation_instruction (lines 343-477), and execute that
```

---

## YAML Structure Reference

Understanding the YAML structure helps you reference specific sections precisely:

```yaml
04-Execute_Implementation_Phase_Tasks.yaml
├── prompt_name
├── version
├── type
├── context
│   ├── role
│   ├── governance
│   ├── doc_references
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
│   └── critical_documentation_rule
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
    └── steps[0-4]
        ├── step (number)
        ├── name
        ├── best_practices_review (Steps 1 & 3 only)
        │   ├── mandatory
        │   ├── documents
        │   ├── requirement
        │   ├── implementation
        │   └── task_specific_reviews (Step 3 only)
        │       ├── fastapi_endpoints
        │       ├── async_performance
        │       ├── error_handling
        │       ├── database_operations
        │       ├── security_authentication
        │       ├── caching
        │       ├── background_tasks
        │       ├── testing
        │       └── observability
        └── actions
├── constraints
├── metadata
└── continuation_instruction
```

---

## YAML Key Reference Examples

### Step References (0-indexed)

- **Step 1**: `instructions.steps[0]` - Review Canonical Documentation Standards
- **Step 2**: `instructions.steps[1]` - Audit Implementation Plan
- **Step 3**: `instructions.steps[2]` - Execute Current Task(s)
- **Step 4**: `instructions.steps[3]` - Advance if Phase Complete
- **Step 5**: `instructions.steps[4]` - Reconcile and Finalise Checklists

### Best Practices References

- **All Best Practices**: `context.best_practices_references`
- **Core FastAPI**: `context.best_practices_references.core_fastapi`
- **Security**: `context.best_practices_references.security_compliance`
- **Step 1 Best Practices**: `instructions.steps[0].best_practices_review`
- **Step 3 FastAPI Review**: `instructions.steps[2].best_practices_review.task_specific_reviews.fastapi_endpoints`

### Codebase Scaffolding

- **Scaffolding Mandate**: `codebase_scaffolding_mandate`
- **Scaffolding Workflow**: `codebase_scaffolding_mandate.instructions.workflow`
- **Step 1 Search**: `codebase_scaffolding_mandate.instructions.workflow.step_1_search`

### Actions

- **Step 3 Actions**: `instructions.steps[2].actions`
- **Step 1 Actions**: `instructions.steps[0].actions`

---

## Recommended Execution Patterns

### Pattern 1: Parse First, Then Execute (Recommended)

**Workflow:**
1. Parse the entire file to understand structure
2. Index all workflow steps
3. Execute full file OR reference specific YAML keys

**Example:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all workflow steps and YAML structure, then execute only 'instructions.steps[2]' with task type: fastapi_endpoints
```

### Pattern 2: Extract and Execute Specific Section

**Workflow:**
1. Extract specific YAML section
2. Execute only that section

**Example:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'instructions.steps[2].best_practices_review.task_specific_reviews.fastapi_endpoints', and execute only that review
```

### Pattern 3: Parse with Context, Execute Selectively

**Workflow:**
1. Parse file with full context
2. Reference specific keys for execution

**Example:**
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml with full context, then execute only 'instructions.steps[2].actions' with 'instructions.steps[2].best_practices_review.task_specific_reviews.fastapi_endpoints' applied
```

---

## Advanced YAML Key Reference Patterns

### Execute Step with Specific Best Practices

```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'instructions.steps[2]' and 'instructions.steps[2].best_practices_review.task_specific_reviews.fastapi_endpoints', then execute Step 3 with FastAPI endpoints best practices review
```

### Execute Multiple Related Sections

```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'instructions.steps[2]', 'codebase_scaffolding_mandate', and 'context.best_practices_references.core_fastapi', then execute Step 3 with scaffolding and FastAPI best practices
```

### Execute with Conditional Logic

```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all steps, if current task type is fastapi_endpoints then execute 'instructions.steps[2]' with 'instructions.steps[2].best_practices_review.task_specific_reviews.fastapi_endpoints'
```

---

## Comparison: Full Load vs Selective Parsing

| Aspect | Full Load | Selective Parsing |
|--------|-----------|-------------------|
| **Speed** | Slower | Faster |
| **Token Usage** | Higher | Lower |
| **Context** | Complete | Focused |
| **Best For** | First-time execution | Re-execution, debugging |
| **Precision** | Broad | Precise |
| **Dependencies** | All loaded | Only needed sections |

---

## Best Practices for Selective Parsing

1. **Always Parse First**: Parse the entire file to understand structure before referencing keys
2. **Use Precise Keys**: Reference exact YAML paths (e.g., `instructions.steps[2]` not "step 3")
3. **Include Context**: When extracting sections, include necessary dependencies (e.g., best practices review with actions)
4. **Index Workflow Steps**: Use "index all workflow steps" to understand available steps before execution
5. **Reference Task Types**: Use task type references for Step 3 (e.g., `task type: fastapi_endpoints`)

---

## Common Execution Scenarios

### Scenario 1: First-Time Execution
```
Execute @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml from the beginning
```

### Scenario 2: Re-execute Step 3 for FastAPI Endpoints
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all workflow steps, then execute only Step 3 with task type: fastapi_endpoints
```

### Scenario 3: Execute Only Best Practices Review
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'instructions.steps[0].best_practices_review', and execute only that review
```

### Scenario 4: Execute Step 3 with Security Focus
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'instructions.steps[2]' and 'instructions.steps[2].best_practices_review.task_specific_reviews.security_authentication', then execute Step 3 with security best practices
```

### Scenario 5: Execute Continuation Instruction Only
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'continuation_instruction', and execute that
```

---

## Quick Reference Cheat Sheet

| What You Want | Command Pattern |
|---------------|----------------|
| **Full execution** | `Execute @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml from the beginning` |
| **Continuation only** | `Follow the continuation_instruction from @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml` |
| **Specific step** | `Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml and execute only 'instructions.steps[2]'` |
| **Step with task type** | `Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, index all workflow steps, then execute only Step 3 with task type: fastapi_endpoints` |
| **Best practices review** | `Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'instructions.steps[2].best_practices_review.task_specific_reviews.fastapi_endpoints', and execute only that review` |
| **Multiple steps** | `Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml and execute only 'instructions.steps[0:3]'` |
| **Scaffolding mandate** | `Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'codebase_scaffolding_mandate', and execute only the scaffolding workflow` |

---

## Tips for Effective Execution

1. **Start with Parse**: Always parse the file first to understand its structure
2. **Use YAML Keys**: Reference exact YAML paths for precision
3. **Index Steps**: Use "index all workflow steps" to see available options
4. **Combine Sections**: Extract multiple related sections for complete context
5. **Specify Task Types**: For Step 3, always specify task type for best practices alignment
6. **Include Dependencies**: When extracting actions, include best practices review sections

---

## Troubleshooting

### Issue: YAML Key Not Found

**Solution**: Parse the file first to see actual structure:
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml and show YAML structure
```

### Issue: Step Execution Missing Context

**Solution**: Include related sections:
```
Parse @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml, extract 'instructions.steps[2]' and 'instructions.steps[2].best_practices_review', then execute Step 3 with best practices review
```

### Issue: Task Type Not Recognized

**Solution**: Use exact task type names from YAML:
- `fastapi_endpoints`
- `async_performance`
- `error_handling`
- `database_operations`
- `security_authentication`
- `caching`
- `background_tasks`
- `testing`
- `observability`

---

**Last Updated**: 2025-12-15
**File**: `04-Execute_Implementation_Phase_Tasks.yaml`
**Version**: 1.0.0
