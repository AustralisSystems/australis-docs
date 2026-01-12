# Implementation Instructions Directory

This directory contains enterprise-grade instruction files that govern all implementation activities within the Digital Angels project. These instructions enforce canonical standards, best practices, and systematic workflows.

## Table of Contents

- [Quick Start](#quick-start)
- [Instruction Categories](#instruction-categories)
- [Execution Methods](#execution-methods)
- [Instruction Reference](#instruction-reference)
- [Best Practices](#best-practices)

---

## Quick Start

### Execute a Full Instruction File

To execute an instruction file from the beginning (loads file and follows all steps):

```
Execute @docs/implementation/instructions/[FILENAME].yaml from the beginning
```

**Example:**
```
Execute @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml from the beginning
```

### Execute Continuation Instructions Only

To execute using only the `continuation_instruction` section (assumes file already loaded):

```
Follow the continuation_instruction from @docs/implementation/instructions/[FILENAME].yaml
```

**Example:**
```
Follow the continuation_instruction from @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml
```

### Alternative: Direct Paste

You can also copy the entire `continuation_instruction` section from any YAML file and paste it directly into your prompt for immediate execution without file lookup.

---

## Execution Methods

### Method 1: Full Execution (Recommended for First-Time Use)

**Command:**
```
Execute @docs/implementation/instructions/[FILENAME].yaml from the beginning
```

**When to Use:**
- First time executing an instruction
- Need complete context and file structure
- Want to ensure all prerequisites are loaded

**What Happens:**
1. Loads the entire instruction file
2. Reads all sections (context, workflow, best practices, etc.)
3. Follows workflow steps sequentially
4. Applies all validation checkpoints

### Method 2: Continuation Instruction Execution (Recommended for Subsequent Use)

**Command:**
```
Follow the continuation_instruction from @docs/implementation/instructions/[FILENAME].yaml
```

**When to Use:**
- File context already available
- Need quick execution without reloading
- Continuing work from a previous session

**What Happens:**
1. Uses the `continuation_instruction` section directly
2. Follows the summarized workflow steps
3. Applies all best practices requirements
4. Enforces validation checkpoints

### Method 3: Direct Paste (Fastest)

**Command:**
```
[Paste the entire continuation_instruction section here]
```

**When to Use:**
- Maximum speed required
- No file lookup needed
- Working offline or with limited file access

---

## Instruction Categories

### 🔷 Foundational Protocols (00-01)

These are the core governance protocols that all other instructions reference.

| File | Purpose | Version |
|------|---------|---------|
| `00-Enterprise_Cannonical_Execution_Protocol.yaml` | Core enterprise governance and execution standards | 1.0.0 |
| `01-The_GoldenRule_Execution_Protocol.yaml` | Golden Rule validation pipeline (context7 → grep → neo4j-memory → code → neo4j-memory) | 1.0.0 |

**Execution:**
```bash
# These are typically loaded automatically by other instructions
# But can be executed explicitly:
Execute @docs/implementation/instructions/00-Enterprise_Cannonical_Execution_Protocol.yaml from the beginning
```

---

### 📋 Documentation & Alignment (02-03)

Instructions for maintaining documentation compliance and session continuity.

| File | Purpose | Version |
|------|---------|---------|
| `02-Align_Implementation_Docs_and_Specs.yaml` | Align implementation documentation and SPECs | 1.0.0 |
| `03-Process_Session_Outcome_and_Documentation_and_Specs.yaml` | Process session outcomes and update documentation/SPECs | 1.0.0 |

**Execution:**
```bash
Execute @docs/implementation/instructions/02-Align_Implementation_Docs_and_Specs.yaml from the beginning
```

---

### 🚀 Task Execution (04-05)

Core instructions for executing implementation tasks.

| File | Purpose | Version |
|------|---------|---------|
| `04-Execute_Implementation_Phase_Tasks.yaml` | Execute implementation phase tasks with documentation-driven workflow | 1.0.0 |
| `05-Run_Locally_and_Test_API_WebUI.yaml` | Run application locally and test API/WebUI | 2.0.0 |

**Execution:**
```bash
Execute @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml from the beginning
```

**Special Notes:**
- `04-Execute_Implementation_Phase_Tasks.yaml` includes best practices review requirements
- All updates must go directly into SPECs and IMPLEMENTATION_PLAN (no temporal documents)

---

### ✅ Validation & Quality (06-09)

Instructions for validating code quality, compliance, and enforcing standards.

| File | Purpose | Version |
|------|---------|---------|
| `06-Validate_Code_Quality_and_Compliance.yaml` | Validate codebase quality, maintainability, and compliance | 1.0.0 |
| `07-Remediate_And_Refactor_Codebase.yaml` | Controlled remediation and refactoring of validation failures | 1.0.0 |
| `08-Debug_And_Troubleshoot_Codebase.yaml` | Controlled debugging and troubleshooting protocol | 1.2.0 |
| `09-Enforce_Workflow_and_Naming_Compliance.yaml` | Enforce workflow and naming compliance | 1.0.0 |

**Execution:**
```bash
# Validation (prerequisite for remediation)
Execute @docs/implementation/instructions/06-Validate_Code_Quality_and_Compliance.yaml from the beginning

# Remediation (after validation failures)
Execute @docs/implementation/instructions/07-Remediate_And_Refactor_Codebase.yaml from the beginning

# Debugging (for runtime issues)
Execute @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml from the beginning
```

**Special Notes:**
- `06-Validate_Code_Quality_and_Compliance.yaml` includes best practices review requirements
- `07-Remediate_And_Refactor_Codebase.yaml` includes best practices review requirements
- `08-Debug_And_Troubleshoot_Codebase.yaml` includes best practices review requirements and requires DEBUG_TROUBLESHOOTING_SPEC creation
- All validation results must go into SPECs and IMPLEMENTATION_PLAN (no VALIDATION_REPORT.md)

---

### 🧪 Testing & Deployment (10-13)

Instructions for building, deploying, and testing REST APIs and Web UI.

| File | Purpose | Version |
|------|---------|---------|
| `10-Build_Deploy_Test_and_Document_REST_API.yaml` | Build, deploy, and manually test REST API endpoints | 1.0.0 |
| `11-Manual_API_Endpoint_Regression_Testing.yaml` | Manual regression testing of all API endpoints | 1.0.0 |
| `12-Manual_WebUI_Regression_Testing.yaml` | Manual CLI-based regression testing of Web UI routes | 1.0.0 |
| `13-Manual_WebUI_Browser_Regression_Testing.yaml` | Manual browser-based regression testing of Web UI routes | 1.0.0 |

**Execution:**
```bash
# Build and deploy
Execute @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml from the beginning

# API regression testing
Execute @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml from the beginning

# Web UI CLI testing (recommended before browser testing)
Execute @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml from the beginning

# Web UI browser testing (recommended after CLI testing)
Execute @docs/implementation/instructions/13-Manual_WebUI_Browser_Regression_Testing.yaml from the beginning
```

**Special Notes:**
- **CRITICAL**: All testing MUST be manual - NO scripted tests allowed
- Test endpoints/routes ONE AT A TIME - never in parallel or batch
- Remediate issues immediately after each failed test before proceeding
- All test results must go into SPECs and IMPLEMENTATION_PLAN (no temporal test reports)
- `13-Manual_WebUI_Browser_Regression_Testing.yaml` requires NON-HEADLESS browser mode (visible window)

**Recommended Flow:**
1. Instruction 12 (CLI) → Instruction 13 (Browser) for Web UI testing
2. Instruction 10 → Instruction 11 for API testing

---

### 🔧 Specialized Instructions (97-103)

Specialized instructions for specific compliance and optimization requirements.

| File | Purpose | Version |
|------|---------|---------|
| `97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml` | Enforce enterprise logging standards compliance | 1.0.0 |
| `98-Codebase_Scaffolding_Mandate.yaml` | Mandatory codebase scaffolding protocol (GitHub repos first) | 1.0.0 |
| `100-Handover_Document_Creation_and_Maintenance_Instruction.yaml` | Create and maintain handover documents for session continuity | 1.0.0 |
| `101-Zero_Tolerance_Remediation_Instruction.yaml` | Zero tolerance remediation (0 TODOs, 0 mocks, 0 stubs) | 1.0.0 |
| `102-TEST_SCRIPT_EXECUTION_PROHIBITION.yaml` | Prohibit creation of scripts that execute test scripts | 1.0.0 |
| `103-FastAPI_Design_Implementation_Refactor.yaml` | FastAPI design optimization and refactoring | 1.0.0 |

**Execution:**
```bash
# Logging compliance
Execute @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml from the beginning

# Codebase scaffolding (integrated into other instructions)
Execute @docs/implementation/instructions/98-Codebase_Scaffolding_Mandate.yaml from the beginning

# Handover document creation
Execute @docs/implementation/instructions/100-Handover_Document_Creation_and_Maintenance_Instruction.yaml from the beginning

# Zero tolerance remediation (WAIT MODE - requires explicit activation)
Execute @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml - begin remediation workflow

# Test script prohibition (always enforced)
Execute @docs/implementation/instructions/102-TEST_SCRIPT_EXECUTION_PROHIBITION.yaml from the beginning

# FastAPI optimization
Execute @docs/implementation/instructions/103-FastAPI_Design_Implementation_Refactor.yaml from the beginning
```

**Special Notes:**
- `97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml`: Enforces logger factory usage (no `logging.getLogger()`)
- `98-Codebase_Scaffolding_Mandate.yaml`: Integrated into most instructions - always search GitHub repos first
- `101-Zero_Tolerance_Remediation_Instruction.yaml`: **WAIT MODE** - requires explicit activation, CODE-ONLY instruction
- `102-TEST_SCRIPT_EXECUTION_PROHIBITION.yaml`: **CRITICAL** - absolute prohibition against test execution scripts
- `103-FastAPI_Design_Implementation_Refactor.yaml`: Includes best practices review requirements

---

## Instruction Reference

### Complete File List

#### Foundational Protocols
- `00-Enterprise_Cannonical_Execution_Protocol.yaml` - Core governance
- `01-The_GoldenRule_Execution_Protocol.yaml` - Golden Rule validation

#### Documentation & Alignment
- `02-Align_Implementation_Docs_and_Specs.yaml` - Documentation alignment
- `03-Process_Session_Outcome_and_Documentation_and_Specs.yaml` - Session processing

#### Task Execution
- `04-Execute_Implementation_Phase_Tasks.yaml` - Phase task execution
- `05-Run_Locally_and_Test_API_WebUI.yaml` - Local execution and testing

#### Validation & Quality
- `06-Validate_Code_Quality_and_Compliance.yaml` - Code quality validation
- `07-Remediate_And_Refactor_Codebase.yaml` - Remediation and refactoring
- `08-Debug_And_Troubleshoot_Codebase.yaml` - Debugging and troubleshooting
- `09-Enforce_Workflow_and_Naming_Compliance.yaml` - Workflow compliance

#### Testing & Deployment
- `10-Build_Deploy_Test_and_Document_REST_API.yaml` - Build, deploy, test API
- `11-Manual_API_Endpoint_Regression_Testing.yaml` - API regression testing
- `12-Manual_WebUI_Regression_Testing.yaml` - Web UI CLI regression testing
- `13-Manual_WebUI_Browser_Regression_Testing.yaml` - Web UI browser regression testing

#### Specialized Instructions
- `97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml` - Logging compliance
- `98-Codebase_Scaffolding_Mandate.yaml` - Codebase scaffolding
- `100-Handover_Document_Creation_and_Maintenance_Instruction.yaml` - Handover documents
- `101-Zero_Tolerance_Remediation_Instruction.yaml` - Zero tolerance remediation
- `102-TEST_SCRIPT_EXECUTION_PROHIBITION.yaml` - Test script prohibition
- `103-FastAPI_Design_Implementation_Refactor.yaml` - FastAPI optimization

#### WebUI Instructions (in `webui/` subdirectory)
- `20-WebUI_Design_Phase_Tasks.yaml` - Web UI design phase
- `21-WebUI_Component_Mapping_Phase.yaml` - Component mapping
- `22-WebUI_Layout_Token_Generation.yaml` - Layout token generation
- `23-WebUI_Template_Scaffolding_Phase.yaml` - Template scaffolding
- `24-WebUI_Router_Service_Integration.yaml` - Router integration
- `25-WebUI_Interactive_Behavior_Implementation.yaml` - Interactive behavior
- `26-WebUI_Motion_Transitions_Implementation.yaml` - Motion transitions
- `27-WebUI_Accessibility_WCAG_Validation.yaml` - Accessibility validation
- `28-WebUI_Cross_Browser_Responsive_Testing.yaml` - Cross-browser testing
- `30-WebUI_Refactoring_Phase.yaml` - Web UI refactoring

---

## Best Practices

### 1. Execution Order

**Recommended Sequence:**
1. **Foundational**: Load `00` and `01` (usually automatic)
2. **Validation**: Run `06` before remediation
3. **Remediation**: Run `07` after validation failures
4. **Testing**: Run `10` → `11` for APIs, `12` → `13` for Web UI
5. **Specialized**: Apply `97`, `98`, `101`, `103` as needed

### 2. Documentation Compliance

**CRITICAL RULE**: All instructions enforce:
- **NO temporal documents** (e.g., `VALIDATION_REPORT_YYYY-MM-DD.md`)
- **ALL updates** go directly into:
  1. SPEC documents (`docs/implementation/in_progress/` or `done/`)
  2. `IMPLEMENTATION_PLAN_v#.#.#.md`

**Exception**: `DEBUG_TROUBLESHOOTING_SPEC` is a SPEC document (enduring), not temporal.

### 3. Best Practices Integration

Many instructions include `best_practices_references` sections listing 40 best practice documents. These are **MANDATORY** to review at specific workflow steps.

**Best Practice Categories:**
- Core FastAPI (3 files)
- Async/Performance (3 files)
- Reliability/Resilience (3 files)
- Architecture Patterns (5 files)
- Security/Compliance (4 files)
- Observability/Monitoring (2 files)
- Data Persistence (6 files)
- Configuration/Deployment (3 files)
- Background Tasks (3 files)
- Integration Patterns (3 files)
- UI Integration (3 files)
- Code Quality/Testing (3 files)
- Templating/Scaffolding (1 file)

### 4. Testing Requirements

**CRITICAL TESTING RULES:**
- **MANUAL TESTING ONLY** - NO scripted tests
- Test **ONE AT A TIME** - never in parallel or batch
- Remediate issues **IMMEDIATELY** after each failed test
- **NO** pytest, unittest, Playwright scripts, or automated test runners
- Use: curl, Postman, MCP fetch, browser (manual interaction only)

### 5. Codebase Scaffolding Mandate

**MANDATORY**: Always search for existing code repositories FIRST before writing custom code.

**Priority Hierarchy:**
1. Golden Template (`C:\github_development\projects\fastapi-enterprise-core-template`)
2. Local Repos (`C:\github_development\projects\*`)
3. tristanaburns GitHub (public/private repos)
4. Public GitHub repositories
5. Official SDKs and APIs
6. CNCF projects
7. Open source libraries
8. Public packages
9. Custom code (LAST RESORT - requires full justification)

### 6. Zero Tolerance Requirements

**ABSOLUTE FORBIDDEN:**
- 0 TODOs
- 0 mocks
- 0 stubs
- 0 hard-coded values
- 0 violations of SOLID/DRY/KISS

**Enforcement**: Finding a violation = STOP current work, FIX violation, VERIFY fix, THEN continue.

### 7. Logging Requirements

**MANDATORY**: Use logger factory ONLY (`@src/services/logging/logger_factory.py`)

**Allowed:**
- `get_logger()`
- `get_component_logger()`
- `create_debug_logger()`

**Forbidden:**
- `logging.getLogger()`
- `logging.basicConfig()`
- `print()` statements

**Security Modules**: MUST use audit logging (`get_component_logger('audit', 'security')`)
**Service Modules**: MUST have debug logging (`create_debug_logger(__name__)`)

### 8. Continuation Instructions

Every instruction file includes a `continuation_instruction` section that:
- Summarizes the entire instruction file
- Lists all best practices documents
- Outlines mandatory workflow steps
- Defines validation checkpoints

**Use Cases:**
- Quick reference without reloading file
- Copy-paste for immediate execution
- Session continuity reminders

---

## Common Workflows

### Workflow 1: Implement New Feature

```bash
# 1. Execute implementation tasks
Execute @docs/implementation/instructions/04-Execute_Implementation_Phase_Tasks.yaml from the beginning

# 2. Validate code quality
Execute @docs/implementation/instructions/06-Validate_Code_Quality_and_Compliance.yaml from the beginning

# 3. If validation fails, remediate
Execute @docs/implementation/instructions/07-Remediate_And_Refactor_Codebase.yaml from the beginning

# 4. Build, deploy, and test
Execute @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml from the beginning

# 5. Regression testing
Execute @docs/implementation/instructions/11-Manual_API_Endpoint_Regression_Testing.yaml from the beginning
```

### Workflow 2: Fix Runtime Issue

```bash
# 1. Debug and troubleshoot
Execute @docs/implementation/instructions/08-Debug_And_Troubleshoot_Codebase.yaml from the beginning

# 2. Validate fix
Execute @docs/implementation/instructions/06-Validate_Code_Quality_and_Compliance.yaml from the beginning

# 3. Test fix
Execute @docs/implementation/instructions/10-Build_Deploy_Test_and_Document_REST_API.yaml from the beginning
```

### Workflow 3: Zero Tolerance Remediation

```bash
# 1. Activate zero tolerance remediation (WAIT MODE requires explicit activation)
Execute @docs/implementation/instructions/101-Zero_Tolerance_Remediation_Instruction.yaml - begin remediation workflow

# 2. Follow workflow steps (11 steps, sequential, blocking)
# 3. Verify all validation checkpoints pass
```

### Workflow 4: Web UI Testing

```bash
# 1. CLI testing first (faster, catches basic issues)
Execute @docs/implementation/instructions/12-Manual_WebUI_Regression_Testing.yaml from the beginning

# 2. Browser testing second (validates visual/interactive behavior)
Execute @docs/implementation/instructions/13-Manual_WebUI_Browser_Regression_Testing.yaml from the beginning
```

---

## Troubleshooting

### Issue: Instruction Not Executing

**Solution:**
- Ensure file path is correct (use `@docs/implementation/instructions/` prefix)
- Check file exists and is readable
- Verify YAML syntax is valid

### Issue: Continuation Instruction Not Found

**Solution:**
- Some older instructions may not have `continuation_instruction` sections
- Use full execution method instead: `Execute @docs/implementation/instructions/[FILENAME].yaml from the beginning`

### Issue: Best Practices Not Being Applied

**Solution:**
- Verify instruction includes `best_practices_references` section
- Check `best_practices_review` requirements in workflow steps
- Ensure best practice documents exist in `docs/implementation/best-practices/`

### Issue: Testing Scripts Being Created

**Solution:**
- Review `102-TEST_SCRIPT_EXECUTION_PROHIBITION.yaml`
- Ensure all testing is manual (curl, Postman, MCP fetch, browser)
- NO pytest, unittest, or automated test runners allowed

---

## Version History

| Instruction | Current Version | Last Updated |
|-------------|----------------|--------------|
| 00-Enterprise_Cannonical_Execution_Protocol | 1.0.0 | - |
| 01-The_GoldenRule_Execution_Protocol | 1.0.0 | - |
| 04-Execute_Implementation_Phase_Tasks | 1.0.0 | - |
| 05-Run_Locally_and_Test_API_WebUI | 2.0.0 | - |
| 08-Debug_And_Troubleshoot_Codebase | 1.2.0 | - |
| 10-Build_Deploy_Test_and_Document_REST_API | 1.0.0 | - |
| 11-Manual_API_Endpoint_Regression_Testing | 1.0.0 | - |
| 12-Manual_WebUI_Regression_Testing | 1.0.0 | - |
| 13-Manual_WebUI_Browser_Regression_Testing | 1.0.0 | - |

---

## Additional Resources

- **Best Practices**: `docs/implementation/best-practices/` (40 documents)
- **SPEC Templates**: `docs/implementation/SPEC_TEMPLATE_v1.0.0.md`
- **Implementation Plans**: `docs/implementation/IMPLEMENTATION_PLAN_v#.#.#.md`
- **Documentation Guide**: `docs/implementation/IMPLEMENTATION_WORKFLOW_GUIDE_v1.0.0.md`

---

## Support

For questions or issues with instruction execution:
1. Review the instruction file's `continuation_instruction` section
2. Check the instruction's `metadata` section for version and compliance info
3. Verify all prerequisites are met (see instruction's `prerequisites` section)
4. Ensure canonical protocols (`00` and `01`) are loaded

---

**Last Updated**: 2025-12-15
**Maintained By**: Shadow Team AI
