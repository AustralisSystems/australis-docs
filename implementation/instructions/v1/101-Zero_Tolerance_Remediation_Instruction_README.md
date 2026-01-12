# Zero Tolerance Remediation Instruction - Execution Guide

This guide provides comprehensive methods for executing `101-Zero_Tolerance_Remediation_Instruction.yaml`, including full execution and selective parsing by YAML key references.

## Quick Start

### Full Execution (First Time)
```
Execute @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml from the beginning
```

### Continuation Instruction (Subsequent Use)
```
Follow the continuation_instruction from @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml
```

### Selective Parsing (Recommended for Re-execution)
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'zero_tolerance_requirements' section
```

---

## Execution Methods

### Method 1: Full Execution from Beginning

**Use Case**: First-time execution, need complete context

**Command:**
```
Execute @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml from the beginning
```

**Alternative Formats:**
```
Execute @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml
Load and obey @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml
Follow @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml
```

**What Happens:**
- Loads entire instruction file
- Enters WAIT MODE (acknowledgement only)
- Reads all sections (zero tolerance, logging, remediation priority, workflow, enforcement)
- Waits for explicit user instruction before executing

---

### Method 2: Continuation Instruction Execution

**Use Case**: File context already available, quick execution

**Command:**
```
Follow the continuation_instruction from @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml
```

**Alternative Formats:**
```
Execute per continuation_instruction in @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml
Continue per @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml continuation_instruction
```

**What Happens:**
- Uses `continuation_instruction` section directly (lines 472-565)
- Follows summarized workflow steps
- Applies zero tolerance requirements
- Enforces logging requirements
- Enforces remediation priority order

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

### Method 4: Parse and Execute Specific Section

**Use Case**: Execute only one section

**Zero Tolerance Requirements:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'zero_tolerance_requirements' section
```

**Development Standards:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'development_standards' section
```

**Logging Requirements:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'logging_requirements' section
```

**Remediation Priority:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'remediation_priority' section
```

**Validation Checkpoint:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'validation_checkpoint' section
```

**Workflow:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'workflow' section
```

**Enforcement:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'enforcement' section
```

---

### Method 5: Parse and Execute Specific Priority

**Use Case**: Execute remediation for specific priority level

**Priority 1 (Security):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'remediation_priority.priority_1_security', and execute Priority 1 remediation
```

**Priority 2 (Core Services):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'remediation_priority.priority_2_core_services', and execute Priority 2 remediation
```

**Priority 3 (API Routers):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'remediation_priority.priority_3_api_routers', and execute Priority 3 remediation
```

**Priority 4 (Other Modules):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'remediation_priority.priority_4_other_modules', and execute Priority 4 remediation
```

---

### Method 6: Parse and Execute Specific Workflow Step

**Use Case**: Execute only one workflow step

**Step 1 (Issue Identification):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'workflow.steps.step_1' section (Issue identification and context gathering)
```

**Step 2 (Issue Reproduction):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'workflow.steps.step_2' section (Issue reproduction)
```

**Step 3 (Root Cause Analysis):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'workflow.steps.step_3' section (Root cause analysis)
```

**Step 4 (Create DEBUG_TROUBLESHOOTING_SPEC):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'workflow.steps.step_4' section (Create DEBUG_TROUBLESHOOTING_SPEC)
```

**Step 5 (Solution Design):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'workflow.steps.step_5' section (Solution design)
```

**Step 6 (Controlled Fix Implementation):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'workflow.steps.step_6' section (Controlled fix implementation)
```

**Step 7 (Fix Validation and Testing):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'workflow.steps.step_7' section (Fix validation and testing)
```

**Step 8 (Regression Prevention):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'workflow.steps.step_8' section (Regression prevention)
```

**Step 9 (Update DEBUG_TROUBLESHOOTING_SPEC):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'workflow.steps.step_9' section (Update DEBUG_TROUBLESHOOTING_SPEC)
```

**Step 10 (Persistence and Audit Logging):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'workflow.steps.step_10' section (Persistence and audit logging)
```

**Step 11 (Completion and Verification):**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only the 'workflow.steps.step_11' section (Completion and verification)
```

---

### Method 7: Parse and Extract Specific Requirements

**Use Case**: Execute specific requirement types

**Absolute Forbidden Items:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'zero_tolerance_requirements.absolute_forbidden', and execute forbidden items validation
```

**Refactoring Mandate:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'zero_tolerance_requirements.refactoring_mandate', and execute refactoring mandate validation
```

**Development Standards:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'development_standards', and execute development standards validation
```

**Logger Factory Requirements:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'logging_requirements.logger_factory', and execute logger factory validation
```

**Usage Patterns:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'logging_requirements.usage_patterns', and execute usage patterns validation
```

---

### Method 8: Parse Validation Checkpoints

**Use Case**: Execute specific validation checkpoint

**Protocols Checkpoint:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'validation_checkpoint.before_completion.protocols', and execute protocols validation
```

**Zero Tolerance Checkpoint:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'validation_checkpoint.before_completion.zero_tolerance', and execute zero tolerance validation
```

**Logging Compliance Checkpoint:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'validation_checkpoint.before_completion.logging_compliance', and execute logging compliance validation
```

**Code Quality Checkpoint:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'validation_checkpoint.before_completion.code_quality', and execute code quality validation
```

**Production Readiness Checkpoint:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'validation_checkpoint.before_completion.production_readiness', and execute production readiness validation
```

---

### Method 9: Parse Multiple Steps or Priorities

**Use Case**: Execute a range of steps or priorities

**Workflow Steps 1-4:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only 'workflow.steps.step_1' through 'workflow.steps.step_4'
```

**Workflow Steps 5-8:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only 'workflow.steps.step_5' through 'workflow.steps.step_8'
```

**Priorities 1-2:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and execute only 'remediation_priority.priority_1_security' and 'remediation_priority.priority_2_core_services'
```

---

### Method 10: Parse Continuation Instruction Only

**Use Case**: Quick execution using continuation instruction without full file load

**Command:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'continuation_instruction' section, and execute that
```

**Alternative:**
```
Read @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract continuation_instruction (lines 472-565), and execute that
```

---

## YAML Structure Reference

Understanding the YAML structure helps you reference specific sections precisely:

```yaml
101-Zero_Tolerance_Remediation_Instruction.yaml
├── prompt_name
├── version
├── type
├── language
├── references
├── context
│   ├── role
│   ├── intent
│   ├── workflow
│   └── execution_mode
├── initialization_mode
│   ├── rule
│   ├── behavior
│   ├── forbidden_on_load
│   ├── required_on_load
│   ├── response_template
│   └── activation_trigger
├── documentation_policy
│   ├── code_only
│   ├── rule
│   ├── explicit_request_definition
│   ├── exceptions
│   ├── forbidden
│   ├── required
│   └── enforcement
├── quick_reference
│   ├── protocols
│   ├── zero_tolerance_summary
│   └── logging_summary
├── zero_tolerance_requirements
│   ├── absolute_forbidden
│   └── refactoring_mandate
│       ├── rule
│       ├── enforcement
│       ├── required_replacements
│       └── verification
├── development_standards
│   ├── backend_first
│   ├── openapi_first
│   ├── naming_synchronization
│   ├── data_retrieval
│   ├── shims_aliases
│   ├── pydantic_version
│   ├── pydantic_fixes
│   ├── hard_coded_variables
│   └── protocol_compliance
├── logging_requirements
│   ├── logger_factory
│   ├── usage_patterns
│   │   ├── allowed
│   │   └── forbidden
│   ├── security_modules
│   ├── service_modules
│   ├── output_formats
│   └── blocking
├── remediation_priority
│   ├── execution_order
│   ├── blocking_rule
│   ├── priority_1_security
│   ├── priority_2_core_services
│   ├── priority_3_api_routers
│   └── priority_4_other_modules
├── validation_checkpoint
│   ├── mandatory
│   ├── rule
│   ├── blocking
│   └── before_completion
│       ├── protocols
│       ├── zero_tolerance
│       ├── logging_compliance
│       ├── code_quality
│       └── production_readiness
├── workflow
│   ├── protocol
│   ├── focus
│   ├── mode
│   ├── execution_rule
│   ├── blocking_rule
│   ├── activation
│   └── steps
│       ├── step_1
│       ├── step_2
│       ├── step_3
│       ├── step_4
│       ├── step_5
│       ├── step_6
│       ├── step_7
│       ├── step_8
│       ├── step_9
│       ├── step_10
│       └── step_11
├── enforcement
│   ├── strict_mode
│   ├── interpretation_policy
│   ├── wiggle_room
│   ├── blocking_rules
│   ├── violation_response
│   └── no_exceptions
├── output_format
│   ├── on_initialization
│   └── on_explicit_instruction
├── metadata
└── continuation_instruction
```

---

## YAML Key Reference Examples

### Zero Tolerance References

- **All Zero Tolerance**: `zero_tolerance_requirements`
- **Absolute Forbidden**: `zero_tolerance_requirements.absolute_forbidden`
- **Refactoring Mandate**: `zero_tolerance_requirements.refactoring_mandate`
- **Required Replacements**: `zero_tolerance_requirements.refactoring_mandate.required_replacements`

### Development Standards References

- **All Development Standards**: `development_standards`
- **Backend First**: `development_standards.backend_first`
- **OpenAPI First**: `development_standards.openapi_first`
- **Naming Synchronization**: `development_standards.naming_synchronization`
- **Data Retrieval**: `development_standards.data_retrieval`
- **Pydantic Version**: `development_standards.pydantic_version`
- **Hard Coded Variables**: `development_standards.hard_coded_variables`

### Logging References

- **All Logging**: `logging_requirements`
- **Logger Factory**: `logging_requirements.logger_factory`
- **Usage Patterns**: `logging_requirements.usage_patterns`
- **Security Modules**: `logging_requirements.security_modules`
- **Service Modules**: `logging_requirements.service_modules`
- **Output Formats**: `logging_requirements.output_formats`

### Remediation Priority References

- **All Priorities**: `remediation_priority`
- **Priority 1 (Security)**: `remediation_priority.priority_1_security`
- **Priority 2 (Core Services)**: `remediation_priority.priority_2_core_services`
- **Priority 3 (API Routers)**: `remediation_priority.priority_3_api_routers`
- **Priority 4 (Other Modules)**: `remediation_priority.priority_4_other_modules`

### Workflow Step References

- **Step 1**: `workflow.steps.step_1` - Issue identification and context gathering
- **Step 2**: `workflow.steps.step_2` - Issue reproduction
- **Step 3**: `workflow.steps.step_3` - Root cause analysis
- **Step 4**: `workflow.steps.step_4` - Create DEBUG_TROUBLESHOOTING_SPEC
- **Step 5**: `workflow.steps.step_5` - Solution design
- **Step 6**: `workflow.steps.step_6` - Controlled fix implementation
- **Step 7**: `workflow.steps.step_7` - Fix validation and testing
- **Step 8**: `workflow.steps.step_8` - Regression prevention
- **Step 9**: `workflow.steps.step_9` - Update DEBUG_TROUBLESHOOTING_SPEC
- **Step 10**: `workflow.steps.step_10` - Persistence and audit logging
- **Step 11**: `workflow.steps.step_11` - Completion and verification

### Validation Checkpoint References

- **All Checkpoints**: `validation_checkpoint.before_completion`
- **Protocols**: `validation_checkpoint.before_completion.protocols`
- **Zero Tolerance**: `validation_checkpoint.before_completion.zero_tolerance`
- **Logging Compliance**: `validation_checkpoint.before_completion.logging_compliance`
- **Code Quality**: `validation_checkpoint.before_completion.code_quality`
- **Production Readiness**: `validation_checkpoint.before_completion.production_readiness`

### Enforcement References

- **All Enforcement**: `enforcement`
- **Blocking Rules**: `enforcement.blocking_rules`
- **Violation Response**: `enforcement.violation_response`
- **No Exceptions**: `enforcement.no_exceptions`

---

## Recommended Execution Patterns

### Pattern 1: Parse First, Then Execute (Recommended)

**Workflow:**
1. Parse the entire file to understand structure
2. Index all requirements, priorities, and workflow steps
3. Execute full workflow OR reference specific YAML keys

**Example:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, index all requirements and priorities, then execute only 'remediation_priority.priority_1_security'
```

### Pattern 2: Extract and Execute Specific Section

**Workflow:**
1. Extract specific YAML section
2. Execute only that section

**Example:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'zero_tolerance_requirements.absolute_forbidden', and execute forbidden items validation
```

### Pattern 3: Parse with Context, Execute Selectively

**Workflow:**
1. Parse file with full context
2. Reference specific keys for execution

**Example:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml with full context, then execute only 'remediation_priority.priority_1_security' with 'zero_tolerance_requirements.absolute_forbidden' applied
```

### Pattern 4: Execute Remediation by Priority

**Priority 1 Only:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'remediation_priority.priority_1_security', then execute Priority 1 remediation
```

**Priorities 1-2:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'remediation_priority.priority_1_security' and 'remediation_priority.priority_2_core_services', then execute Priorities 1-2 remediation
```

**All Priorities:**
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'remediation_priority', then execute all priorities sequentially
```

---

## Advanced YAML Key Reference Patterns

### Execute Priority with Zero Tolerance Requirements

```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'remediation_priority.priority_1_security' and 'zero_tolerance_requirements.absolute_forbidden', then execute Priority 1 with zero tolerance requirements
```

### Execute Workflow Step with Validation Checkpoint

```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'workflow.steps.step_11' and 'validation_checkpoint.before_completion', then execute Step 11 with validation checkpoints
```

### Execute Logging Requirements with Development Standards

```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'logging_requirements' and 'development_standards', then execute logging requirements with development standards validation
```

### Execute Enforcement with Blocking Rules

```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'enforcement.blocking_rules' and 'enforcement.violation_response', then execute enforcement with blocking rules
```

---

## Comparison: Full Load vs Selective Parsing

| Aspect | Full Load | Selective Parsing |
|--------|-----------|-------------------|
| **Speed** | Slower | Faster |
| **Token Usage** | Higher | Lower |
| **Context** | Complete | Focused |
| **Best For** | First-time execution | Re-execution, specific priorities/steps |
| **Precision** | Broad | Precise |
| **Dependencies** | All loaded | Only needed sections |

---

## Best Practices for Selective Parsing

1. **Always Parse First**: Parse the entire file to understand structure before referencing keys
2. **Use Precise Keys**: Reference exact YAML paths (e.g., `remediation_priority.priority_1_security`)
3. **Include Context**: When extracting sections, include necessary dependencies (e.g., zero tolerance requirements with priorities)
4. **Index Requirements**: Use "index all requirements and priorities" to understand available options before execution
5. **Follow Priority Order**: Always respect the sequential priority order (Priority 1 → 2 → 3 → 4)
6. **Combine Sections**: Extract multiple related sections for complete validation (e.g., requirements + enforcement)

---

## Common Execution Scenarios

### Scenario 1: First-Time Execution (WAIT MODE)
```
Execute @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml from the beginning
```
**Note**: This enters WAIT MODE - acknowledges loaded, then waits for explicit user instruction.

### Scenario 2: Execute Priority 1 (Security) Only
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'remediation_priority.priority_1_security', and execute Priority 1 remediation
```

### Scenario 3: Execute Zero Tolerance Validation Only
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'zero_tolerance_requirements.absolute_forbidden' and 'validation_checkpoint.before_completion.zero_tolerance', then execute zero tolerance validation
```

### Scenario 4: Execute Logging Compliance Validation Only
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'logging_requirements' and 'validation_checkpoint.before_completion.logging_compliance', then execute logging compliance validation
```

### Scenario 5: Execute Workflow Step 4 (Create SPEC) Only
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'workflow.steps.step_4', and execute Step 4 (Create DEBUG_TROUBLESHOOTING_SPEC)
```

### Scenario 6: Execute Continuation Instruction Only
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'continuation_instruction', and execute that
```

### Scenario 7: Execute All Validation Checkpoints
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'validation_checkpoint.before_completion', then execute all validation checkpoints
```

---

## Quick Reference Cheat Sheet

| What You Want | Command Pattern |
|---------------|----------------|
| **Full execution** | `Execute @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml from the beginning` |
| **Continuation only** | `Follow the continuation_instruction from @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml` |
| **Zero tolerance validation** | `Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'zero_tolerance_requirements.absolute_forbidden', and execute forbidden items validation` |
| **Priority 1 remediation** | `Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'remediation_priority.priority_1_security', and execute Priority 1 remediation` |
| **Logging compliance** | `Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'logging_requirements' and 'validation_checkpoint.before_completion.logging_compliance', then execute logging compliance validation` |
| **Workflow step** | `Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'workflow.steps.step_4', and execute Step 4` |
| **Validation checkpoint** | `Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'validation_checkpoint.before_completion.code_quality', and execute code quality validation` |
| **Enforcement rules** | `Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'enforcement.blocking_rules', and execute enforcement rules validation` |

---

## Critical Rules Reference

### Initialization Mode (WAIT MODE)

**Key**: `initialization_mode`

**Rule**: WAIT MODE - This instruction is a PRE-CURSOR only

**Behavior**:
- MUST acknowledge instruction loaded, then WAIT for explicit user instruction
- DO NOT scan codebase automatically
- DO NOT search for violations automatically
- DO NOT propose remediation plans automatically
- DO NOT start any remediation work automatically

**Activation Trigger**: User must provide EXPLICIT instruction to begin work - loading this file does NOT trigger work

**Response Template**:
```
"Zero Tolerance Remediation Instruction (v1.0.0) loaded and acknowledged.
Ready to execute remediation per this instruction when explicitly instructed.
Waiting for your next explicit instruction."
```

---

### Documentation Policy (CODE-ONLY - ABSOLUTE AUTHORITY)

**Key**: `documentation_policy`

**Override Priority**: **HIGHEST - This directive OVERRIDES ALL other YAML instruction files - NO EXCEPTIONS**

**Rule**: **THIS IS A CODE-ONLY SESSION - NO DOCUMENTATION OF ANY KIND IS PERMITTED UNLESS EXPLICITLY REQUESTED**

**Override Statement**: **NO OTHER INSTRUCTIONS FROM ANY OTHER YAML FILES OVERRIDE THIS DIRECTIVE - This is the ABSOLUTE AUTHORITY on documentation policy for this session**

**Explicit Request Definition**: User must **EXPLICITLY** state 'create documentation' or 'write documentation' - implicit requests DO NOT count, suggestions DO NOT count, hints DO NOT count - **ONLY EXPLICIT REQUESTS COUNT**

**Exceptions**:
- DEBUG_TROUBLESHOOTING_SPEC must ALWAYS be created per Debug and Troubleshoot Protocol (MANDATORY, NO EXCEPTIONS)
- SPEC protocols must ALWAYS be followed (SPEC creation, updates, lifecycle management) - MANDATORY, NO EXCEPTIONS
- Documentation **EXPLICITLY** requested by user with **EXPLICIT** wording (user must say 'create documentation' or 'write documentation' explicitly)

**Forbidden**:
- Creating README files unless **EXPLICITLY** requested with **EXPLICIT** wording
- Creating markdown documentation files unless **EXPLICITLY** requested with **EXPLICIT** wording
- Creating temporal documentation reports unless **EXPLICITLY** requested with **EXPLICIT** wording
- Creating **ANY** documentation files unless **EXPLICITLY** requested with **EXPLICIT** wording
- Writing documentation comments beyond code docstrings (docstrings are REQUIRED, not optional)
- Interpreting 'documentation' requests implicitly - MUST be **EXPLICIT**
- **Following documentation requirements from other YAML files - THIS FILE OVERRIDES ALL OTHERS**
- Creating documentation 'because it's helpful' or 'because it's standard practice' - **ONLY EXPLICIT REQUESTS ALLOWED**

**Required**:
- DEBUG_TROUBLESHOOTING_SPEC creation and updates (mandatory per protocol - FAILURE TO CREATE IS A BLOCKING ISSUE)
- Code docstrings and type hints (standard Python practice - REQUIRED, not optional)
- SPEC lifecycle management (in_progress → done/) - MANDATORY

**Enforcement**: Violation of documentation policy = BLOCKING ISSUE - execution MUST STOP immediately - **NO EXCEPTIONS, NO INTERPRETATIONS, NO OVERRIDES FROM OTHER FILES**

**Precedence**: **This documentation policy takes ABSOLUTE PRECEDENCE over ANY conflicting instructions in ANY other YAML files - NO EXCEPTIONS**

---

### Zero Tolerance Requirements

**Key**: `zero_tolerance_requirements.absolute_forbidden`

**Absolute Forbidden (ZERO TOLERANCE)**:
- 0 TODOs (MUST fix immediately if found, NO exceptions)
- 0 mocks (MUST replace with real code immediately, NO exceptions)
- 0 stub code blocks (MUST implement fully immediately, NO exceptions)
- 0 placeholder/demo data (MUST replace with real data retrieval immediately, NO exceptions)
- 0 hard-coded values for dynamic content (MUST move to config/DB immediately, NO exceptions)
- 0 hard-coded settings that should be in database (MUST move to DB immediately, NO exceptions)
- 0 fixed content where real data must be retrieved (MUST implement real retrieval immediately, NO exceptions)
- 0 business logic in templates (MUST move to backend services immediately, NO exceptions)
- 0 duplicated logic (MUST refactor to shared code immediately, NO exceptions)
- 0 violations of SOLID/DRY/KISS (MUST refactor immediately, NO exceptions)
- 0 deviations from the Golden Rules (MUST fix immediately, NO exceptions)

**Refactoring Mandate**:
- **Key**: `zero_tolerance_requirements.refactoring_mandate`
- **Rule**: If a TODO, mock, or stub exists ANYWHERE, it MUST be refactored into production-ready code IMMEDIATELY - NO DELAYS, NO EXCEPTIONS, NO DEFERRALS
- **Enforcement**: Finding a violation = STOP current work, FIX violation, VERIFY fix, THEN continue - NO WORKAROUNDS ALLOWED

---

### Development Standards

**Backend First**:
- **Key**: `development_standards.backend_first`
- **Rule**: MUST implement backend functionality FIRST, then frontend - NO frontend-only implementations
- **Enforcement**: Frontend code without backend = VIOLATION - MUST create backend first

**OpenAPI First**:
- **Key**: `development_standards.openapi_first`
- **Rule**: MUST define OpenAPI specification FIRST, then implement - NO ad-hoc endpoints
- **Enforcement**: Endpoint without OpenAPI spec = VIOLATION - MUST create spec first

**Naming Synchronization**:
- **Key**: `development_standards.naming_synchronization`
- **Rule**: MUST use identical names between backend and frontend - NO variations, NO aliases, NO shims
- **Enforcement**: Name mismatch = VIOLATION - MUST synchronize immediately

**Data Retrieval**:
- **Key**: `development_standards.data_retrieval`
- **Rule**: MUST retrieve data dynamically from backend - NO static content, NO hard-coded data
- **Enforcement**: Static/hard-coded data = VIOLATION - MUST implement real retrieval

**Pydantic v2 ONLY**:
- **Key**: `development_standards.pydantic_version`
- **Rule**: ONLY Pydantic v2 must be used - NO Pydantic v1 imports or usage
- **Enforcement**: Pydantic v1 usage = VIOLATION - MUST upgrade to v2 immediately

**Hard Coded Variables**:
- **Key**: `development_standards.hard_coded_variables`
- **Rule**: NO hard coded variables in any py files - ALL must be stored in config files or db tables (DB preferred)
- **Enforcement**: Hard-coded variable = VIOLATION - MUST move to config/DB immediately
- **Exception**: NONE - even constants must be in config/DB if they could change

---

### Logging Requirements

**Logger Factory**:
- **Key**: `logging_requirements.logger_factory`
- **Location**: `@src/services/logging/logger_factory.py`
- **Rule**: The logger factory is the ONLY logger that must be used

**Usage Patterns**:
- **Key**: `logging_requirements.usage_patterns`
- **Allowed**: `get_logger`, `get_component_logger`, `create_debug_logger`
- **Forbidden**: `logging.getLogger()`, `logging.basicConfig()`, `print()` statements

**Security Modules**:
- **Key**: `logging_requirements.security_modules`
- **Requirement**: MUST use audit logging
- **Pattern**: `get_component_logger('audit', 'security')`
- **Purpose**: Cybersecurity compliance

**Service Modules**:
- **Key**: `logging_requirements.service_modules`
- **Requirement**: MUST have debug logging capability
- **Pattern**: `create_debug_logger(__name__)`
- **Purpose**: Troubleshooting

**Output Formats**:
- **Key**: `logging_requirements.output_formats`
- **Console**: MUST be JSON formatted
- **File**: MUST be detailed text formatted

**Blocking**: Non-compliance is a blocking issue

---

### Remediation Priority Order

**Key**: `remediation_priority.execution_order`

**Rule**: MANDATORY - MUST follow priority order sequentially - CANNOT skip priorities, CANNOT proceed to next priority until current is 100% complete

**Blocking Rule**: If ANY violation found in current priority, MUST fix before proceeding - NO exceptions

**Priority 1: Security Modules**
- **Key**: `remediation_priority.priority_1_security`
- **Modules**: Security modules (auth, security, compliance)
- **Actions**: Add audit logging, remove all TODOs/mocks/stubs/hard-coded, ensure zero tolerance compliance
- **Validation**: MUST verify: All security events logged, zero violations - VERIFICATION REQUIRED before proceeding
- **Blocking**: Cannot proceed to Priority 2 until Priority 1 is 100% complete and validated

**Priority 2: Core Services**
- **Key**: `remediation_priority.priority_2_core_services`
- **Modules**: Core services (storage, data, integration, core)
- **Prerequisite**: Priority 1 MUST be 100% complete and validated
- **Actions**: Add debug logging, remove all violations, ensure zero tolerance compliance
- **Validation**: MUST verify: All services have debug logging, zero violations - VERIFICATION REQUIRED before proceeding
- **Blocking**: Cannot proceed to Priority 3 until Priority 2 is 100% complete and validated

**Priority 3: API Routers**
- **Key**: `remediation_priority.priority_3_api_routers`
- **Modules**: API routers (routers, fastapi_services_platform/engine/routers)
- **Prerequisite**: Priority 2 MUST be 100% complete and validated
- **Actions**: Add audit logging for API access, add debug logging for request/response flows, remove all violations, ensure zero tolerance compliance
- **Validation**: MUST verify: API access logged, request/response flows logged, zero violations - VERIFICATION REQUIRED before proceeding
- **Blocking**: Cannot proceed to Priority 4 until Priority 3 is 100% complete and validated

**Priority 4: Other Modules**
- **Key**: `remediation_priority.priority_4_other_modules`
- **Modules**: All other modules (CLI, monitoring, utilities, etc.)
- **Prerequisite**: Priority 3 MUST be 100% complete and validated
- **Actions**: Add appropriate logging (logger factory), remove all violations, ensure zero tolerance compliance
- **Validation**: MUST verify: Appropriate logging added (logger factory used), zero violations - VERIFICATION REQUIRED
- **Blocking**: Cannot mark complete until Priority 4 is 100% complete and validated

---

### Validation Checkpoints

**Key**: `validation_checkpoint.before_completion`

**Rule**: MUST verify ALL checkpoints before marking complete - NO exceptions, NO partial completions

**Blocking**: If ANY checkpoint fails, completion is BLOCKED - MUST fix and re-verify ALL checkpoints

**Protocols Checkpoint**:
- **Key**: `validation_checkpoint.before_completion.protocols`
- **Checks**: All protocols followed (00, 01, 08, 97), Golden Rule sequence executed
- **Enforcement**: Protocol violation = BLOCKING - cannot proceed until fixed

**Zero Tolerance Checkpoint**:
- **Key**: `validation_checkpoint.before_completion.zero_tolerance`
- **Checks**: 0 TODOs, 0 mocks, 0 stubs, 0 hard-coded values, 0 SOLID/DRY/KISS violations, 0 deviations from Golden Rules
- **Enforcement**: ANY violation found = BLOCKING - cannot proceed until fixed
- **Verification Method**: MUST use automated scanning tools + manual verification - NO assumptions

**Logging Compliance Checkpoint**:
- **Key**: `validation_checkpoint.before_completion.logging_compliance`
- **Checks**: All logging uses logger factory, security modules have audit logging, service modules have debug logging, console output is JSON formatted, file output is detailed text formatted
- **Enforcement**: ANY logging violation = BLOCKING - cannot proceed until fixed
- **Verification Method**: MUST scan codebase + test output formats - NO assumptions

**Code Quality Checkpoint**:
- **Key**: `validation_checkpoint.before_completion.code_quality`
- **Checks**: All Python validators pass (mypy 0/0, flake8 0/0, bandit 0 high/medium, safety 0, black/isort no changes, radon cc ≤15, radon mi Grade A, xenon no violations)
- **Enforcement**: ANY validator failure = BLOCKING - cannot proceed until ALL pass
- **Verification Method**: MUST run ALL validators and capture results - NO skipping validators

**Production Readiness Checkpoint**:
- **Key**: `validation_checkpoint.before_completion.production_readiness`
- **Checks**: All code is production-ready, no mock/stub/placeholder code, all data retrieval is dynamic, all configuration is externalized, all endpoints are real CRUD, all services are fully implemented
- **Enforcement**: ANY production readiness issue = BLOCKING - cannot proceed until fixed
- **Verification Method**: MUST verify each item systematically - NO assumptions

**Completion Gate**: ALL checkpoints MUST pass with 100% compliance - NO exceptions, NO partial passes, NO 'good enough' - ONLY 100% compliance allows completion

---

### Workflow (11 Steps)

**Key**: `workflow`

**Protocol**: `docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml`

**Focus**: Assisting in troubleshooting and remediation/refactoring specific issues or observations provided in messages

**Mode**: CODE-ONLY - focus on code remediation, not documentation

**Execution Rule**: MUST follow steps sequentially - NO skipping steps, NO parallel execution of steps, NO shortcuts

**Blocking Rule**: If ANY step fails, MUST stop and fix before proceeding - NO workarounds

**Activation**:
- **Rule**: Workflow is ONLY activated by EXPLICIT user instruction - NOT by loading this file
- **Trigger**: User must explicitly instruct to begin remediation work
- **Wait Mode**: If no explicit instruction provided, MUST remain in WAIT MODE - NO automatic activation

**Steps**:
1. **Issue identification and context gathering** - MUST gather complete context before proceeding
2. **Issue reproduction** - MUST reproduce issue reliably
3. **Root cause analysis** - MUST identify exact root cause
4. **Create DEBUG_TROUBLESHOOTING_SPEC** - MANDATORY - SPEC protocols must be followed
5. **Solution design** - MUST design solution before implementation
6. **Controlled fix implementation** - CODE ONLY (no documentation)
7. **Fix validation and testing** - MUST validate fix works
8. **Regression prevention** - MUST add regression prevention
9. **Update DEBUG_TROUBLESHOOTING_SPEC with resolution** - MANDATORY
10. **Persistence and audit logging** - MUST persist to neo4j-memory
11. **Completion and verification** - MUST verify ALL validation checkpoints pass

**Documentation Note**: NO documentation files shall be created unless explicitly requested with explicit wording. SPEC protocols (DEBUG_TROUBLESHOOTING_SPEC) are the ONLY exception and are MANDATORY - NO interpretations allowed.

---

### Enforcement

**Key**: `enforcement`

**Strict Mode**: true

**Interpretation Policy**: NO interpretations allowed - requirements are LITERAL and ABSOLUTE

**Wiggle Room**: ZERO wiggle room - requirements are IRON CLAD

**Blocking Rules**:
- **THIS IS A CODE-ONLY SESSION - NO DOCUMENTATION OF ANY KIND IS PERMITTED UNLESS EXPLICITLY REQUESTED - This directive OVERRIDES ALL other YAML file instructions - NO EXCEPTIONS**
- **Creating documentation files without EXPLICIT request = FORBIDDEN - violation = BLOCKING ISSUE - execution MUST STOP immediately**
- **Following documentation requirements from other YAML files = FORBIDDEN - This file's CODE-ONLY policy OVERRIDES ALL OTHERS - NO EXCEPTIONS**
- Non-compliance with zero tolerance requirements = IMMEDIATE STOP - execution BLOCKED until fixed
- Non-compliance with logging requirements = IMMEDIATE STOP - execution BLOCKED until fixed
- Code MUST NOT proceed until all violations are fixed - NO exceptions, NO workarounds, NO deferrals
- All validators MUST pass with 0 errors, 0 warnings - NO exceptions, NO 'close enough', ONLY 0/0
- SPEC protocols MUST ALWAYS be followed (DEBUG_TROUBLESHOOTING_SPEC is MANDATORY) - NO exceptions, NO interpretations
- Violation of ANY requirement = BLOCKING ISSUE - execution MUST STOP immediately
- Partial compliance = NON-COMPLIANCE - ONLY 100% compliance is acceptable
- Cannot proceed to next step/priority until current is 100% complete - NO exceptions

**Violation Response**:
- **Action**: STOP immediately
- **Required Steps**: Identify violation → Fix violation → Verify fix → Re-run validation → Confirm 100% compliance
- **Then**: ONLY then can execution continue

**No Exceptions**:
- **Rule**: NO exceptions allowed - requirements are ABSOLUTE
- **Examples**: Cannot say 'this is minor, I'll fix it later' - MUST fix immediately; Cannot say 'this is acceptable for now' - MUST fix immediately; Cannot say 'this is good enough' - MUST achieve 100% compliance; Cannot interpret requirements - MUST follow LITERALLY

---

## Tips for Effective Execution

1. **Start with Parse**: Always parse the file first to understand its structure
2. **Use YAML Keys**: Reference exact YAML paths for precision
3. **Index Requirements**: Use "index all requirements and priorities" to see available options
4. **Follow Priority Order**: Always respect the sequential priority order (Priority 1 → 2 → 3 → 4)
5. **Combine Sections**: Extract multiple related sections for complete validation
6. **Respect WAIT MODE**: Remember this instruction enters WAIT MODE on load - requires explicit user instruction
7. **Follow CODE-ONLY Policy**: Remember documentation policy - **THIS IS A CODE-ONLY SESSION - NO DOCUMENTATION OF ANY KIND IS PERMITTED UNLESS EXPLICITLY REQUESTED - This directive OVERRIDES ALL other YAML file instructions**
8. **Validate Checkpoints**: Always execute validation checkpoints before completion
9. **No Exceptions**: Remember enforcement - NO exceptions, NO interpretations, NO wiggle room

---

## Troubleshooting

### Issue: YAML Key Not Found

**Solution**: Parse the file first to see actual structure:
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml and show YAML structure
```

### Issue: Workflow Not Activated

**Solution**: Remember WAIT MODE - workflow only activates with explicit user instruction:
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'workflow.activation', and review activation requirements
```

### Issue: Priority Order Not Clear

**Solution**: Extract priority order:
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'remediation_priority.execution_order', and review priority order
```

### Issue: Validation Checkpoint Failing

**Solution**: Extract specific checkpoint:
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'validation_checkpoint.before_completion.code_quality', and execute code quality validation
```

### Issue: Enforcement Rules Not Applied

**Solution**: Extract enforcement rules:
```
Parse @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml, extract 'enforcement.blocking_rules', and execute enforcement rules validation
```

---

## Quick Reference Summary

### Zero Tolerance Summary
- 0 TODOs
- 0 mocks
- 0 stubs
- 0 hard-coded values
- 0 violations of SOLID/DRY/KISS

### Logging Summary
- Logger factory ONLY
- JSON console, text files
- Audit logging for security
- Debug logging for services

### Protocols
- 00-Enterprise_Cannonical_Execution_Protocol.yaml
- 01-The_GoldenRule_Execution_Protocol.yaml
- 08-Debug_And_Troubleshoot_Codebase.yaml
- 97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml

---

**Last Updated**: 2025-12-15
**File**: `101-Zero_Tolerance_Remediation_Instruction.yaml`
**Version**: 1.0.0
