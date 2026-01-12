# Logging Requirements Instruction - Execution Guide

This guide provides comprehensive methods for executing `97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml`, including full execution and selective parsing by YAML key references.

## Quick Start

### Full Execution (First Time)
```
Execute @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml from the beginning
```

### Continuation Instruction (Subsequent Use)
```
Follow the runner prompt from @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml
```

### Selective Parsing (Recommended for Re-execution)
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml and execute only the 'mandatory_patterns' section
```

---

## Execution Methods

### Method 1: Full Execution from Beginning

**Use Case**: First-time execution, need complete context

**Command:**
```
Execute @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml from the beginning
```

**Alternative Formats:**
```
Execute @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml
Load and obey @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml
Follow @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml
```

**What Happens:**
- Loads entire instruction file
- Reads all sections (context, requirements, patterns, compliance, enforcement)
- Applies logging compliance requirements
- Validates logger factory usage
- Checks for prohibited patterns

---

### Method 2: Runner Prompt Execution

**Use Case**: Quick reference for logging requirements

**Command:**
```
Load and obey @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml
```

**What Happens:**
- Uses runner prompt section (lines 106-112)
- Applies core logging requirements
- Enforces logger factory usage
- Validates compliance

---

### Method 3: Direct Paste

**Use Case**: Maximum speed, no file lookup needed

**Command:**
```
[Paste the runner prompt section here]
```

**What Happens:**
- Immediate execution without file access
- Uses pasted runner prompt content
- Fastest method for repeated execution

---

## Selective Parsing Methods (YAML Key References)

### Method 4: Parse and Execute Specific Section

**Use Case**: Execute only one section

**Requirements Section:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml and execute only the 'requirements' section
```

**Mandatory Patterns Section:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml and execute only the 'mandatory_patterns' section
```

**Prohibited Patterns Section:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml and execute only the 'prohibited_patterns' section
```

**Compliance Requirements Section:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml and execute only the 'compliance_requirements' section
```

**Enforcement Section:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml and execute only the 'enforcement' section
```

---

### Method 5: Parse and Extract Specific Requirements

**Use Case**: Execute specific requirement types

**Logger Factory Requirements:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.logger_factory', and execute logger factory validation
```

**Standards Requirements:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.standards', and execute standards validation
```

**Audit Logging Requirements:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.audit_logging', and execute audit logging validation
```

**Debug Logging Requirements:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.debug_logging', and execute debug logging validation
```

---

### Method 6: Parse and Extract Specific Patterns

**Use Case**: Execute specific pattern validation

**Standard Logger Pattern:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'mandatory_patterns.standard_logger', and validate standard logger usage
```

**Component Logger Pattern:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'mandatory_patterns.component_logger', and validate component logger usage
```

**Debug Logger Pattern:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'mandatory_patterns.debug_logger', and validate debug logger usage
```

**All Mandatory Patterns:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'mandatory_patterns', and validate all mandatory patterns
```

---

### Method 7: Parse Compliance Requirements

**Use Case**: Execute compliance validation

**Zero Tolerance Requirements:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'compliance_requirements.zero_tolerance', and execute zero tolerance validation
```

**Coverage Requirements:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'compliance_requirements.coverage', and execute coverage validation
```

**All Compliance Requirements:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'compliance_requirements', and execute all compliance validation
```

---

### Method 8: Parse Enforcement Actions

**Use Case**: Execute enforcement validation

**Validation Actions:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'enforcement.validation', and execute validation actions
```

**Blocking Rules:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'enforcement.blocking', and execute blocking rule enforcement
```

---

## YAML Structure Reference

Understanding the YAML structure helps you reference specific sections precisely:

```yaml
97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml
├── prompt_name
├── version
├── type
├── language
├── reference
├── context
│   ├── role
│   ├── mandate
│   └── core_principle
├── requirements
│   ├── logger_factory
│   │   ├── mandatory
│   │   ├── location
│   │   └── rule
│   ├── standards
│   │   ├── syslog_compliance
│   │   ├── console_format
│   │   ├── file_format
│   │   └── syslog_format
│   ├── audit_logging
│   │   ├── mandatory
│   │   ├── purpose
│   │   ├── component
│   │   └── required_for
│   └── debug_logging
│       ├── mandatory
│       ├── purpose
│       ├── logger
│       └── required_for
├── mandatory_patterns
│   ├── standard_logger
│   ├── component_logger
│   └── debug_logger
├── prohibited_patterns
├── compliance_requirements
│   ├── zero_tolerance
│   └── coverage
├── enforcement
│   ├── validation
│   └── blocking
├── output_format
└── metadata
```

---

## YAML Key Reference Examples

### Requirements References

- **All Requirements**: `requirements`
- **Logger Factory**: `requirements.logger_factory`
- **Standards**: `requirements.standards`
- **Audit Logging**: `requirements.audit_logging`
- **Debug Logging**: `requirements.debug_logging`

### Pattern References

- **All Mandatory Patterns**: `mandatory_patterns`
- **Standard Logger**: `mandatory_patterns.standard_logger`
- **Component Logger**: `mandatory_patterns.component_logger`
- **Debug Logger**: `mandatory_patterns.debug_logger`
- **All Prohibited Patterns**: `prohibited_patterns`

### Compliance References

- **All Compliance**: `compliance_requirements`
- **Zero Tolerance**: `compliance_requirements.zero_tolerance`
- **Coverage**: `compliance_requirements.coverage`

### Enforcement References

- **All Enforcement**: `enforcement`
- **Validation**: `enforcement.validation`
- **Blocking**: `enforcement.blocking`

### Context References

- **Core Principle**: `context.core_principle`
- **Mandate**: `context.mandate`
- **Role**: `context.role`

---

## Recommended Execution Patterns

### Pattern 1: Parse First, Then Execute (Recommended)

**Workflow:**
1. Parse the entire file to understand structure
2. Index all requirements and patterns
3. Execute full validation OR reference specific YAML keys

**Example:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, index all requirements and patterns, then execute only 'compliance_requirements.zero_tolerance' validation
```

### Pattern 2: Extract and Execute Specific Section

**Workflow:**
1. Extract specific YAML section
2. Execute only that section

**Example:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'mandatory_patterns', and validate all mandatory patterns
```

### Pattern 3: Parse with Context, Execute Selectively

**Workflow:**
1. Parse file with full context
2. Reference specific keys for execution

**Example:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml with full context, then execute only 'requirements.logger_factory' with 'mandatory_patterns.standard_logger' applied
```

### Pattern 4: Execute Compliance Validation

**Full Compliance Check:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'compliance_requirements' and 'enforcement', then execute full compliance validation
```

**Zero Tolerance Check:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'compliance_requirements.zero_tolerance' and 'enforcement.validation', then execute zero tolerance validation
```

---

## Advanced YAML Key Reference Patterns

### Execute Requirements with Patterns

```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.logger_factory' and 'mandatory_patterns.standard_logger', then execute logger factory validation with standard logger pattern
```

### Execute Compliance with Enforcement

```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'compliance_requirements' and 'enforcement', then execute compliance validation with enforcement rules
```

### Execute Audit Logging Requirements

```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.audit_logging' and 'mandatory_patterns.component_logger', then execute audit logging validation with component logger pattern
```

### Execute Debug Logging Requirements

```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.debug_logging' and 'mandatory_patterns.debug_logger', then execute debug logging validation with debug logger pattern
```

---

## Comparison: Full Load vs Selective Parsing

| Aspect | Full Load | Selective Parsing |
|--------|-----------|-------------------|
| **Speed** | Slower | Faster |
| **Token Usage** | Higher | Lower |
| **Context** | Complete | Focused |
| **Best For** | First-time execution | Re-execution, specific validation |
| **Precision** | Broad | Precise |
| **Dependencies** | All loaded | Only needed sections |

---

## Best Practices for Selective Parsing

1. **Always Parse First**: Parse the entire file to understand structure before referencing keys
2. **Use Precise Keys**: Reference exact YAML paths (e.g., `requirements.logger_factory` not "logger factory")
3. **Include Context**: When extracting sections, include necessary dependencies (e.g., patterns with requirements)
4. **Index Requirements**: Use "index all requirements and patterns" to understand available options before execution
5. **Combine Sections**: Extract multiple related sections for complete validation (e.g., requirements + patterns + compliance)

---

## Common Execution Scenarios

### Scenario 1: First-Time Execution
```
Execute @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml from the beginning
```

### Scenario 2: Validate Logger Factory Usage Only
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.logger_factory' and 'mandatory_patterns.standard_logger', then execute logger factory validation
```

### Scenario 3: Validate Audit Logging Only
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.audit_logging' and 'mandatory_patterns.component_logger', then execute audit logging validation
```

### Scenario 4: Validate Prohibited Patterns Only
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'prohibited_patterns' and 'compliance_requirements.zero_tolerance', then execute prohibited patterns validation
```

### Scenario 5: Execute Full Compliance Check
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'compliance_requirements' and 'enforcement', then execute full compliance validation
```

### Scenario 6: Execute Zero Tolerance Check
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'compliance_requirements.zero_tolerance' and 'enforcement.validation', then execute zero tolerance validation
```

---

## Quick Reference Cheat Sheet

| What You Want | Command Pattern |
|---------------|----------------|
| **Full execution** | `Execute @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml from the beginning` |
| **Runner prompt** | `Load and obey @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml` |
| **Logger factory validation** | `Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.logger_factory' and 'mandatory_patterns.standard_logger', then execute logger factory validation` |
| **Audit logging validation** | `Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.audit_logging' and 'mandatory_patterns.component_logger', then execute audit logging validation` |
| **Debug logging validation** | `Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.debug_logging' and 'mandatory_patterns.debug_logger', then execute debug logging validation` |
| **Prohibited patterns check** | `Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'prohibited_patterns' and 'compliance_requirements.zero_tolerance', then execute prohibited patterns validation` |
| **Full compliance check** | `Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'compliance_requirements' and 'enforcement', then execute full compliance validation` |
| **Zero tolerance check** | `Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'compliance_requirements.zero_tolerance' and 'enforcement.validation', then execute zero tolerance validation` |

---

## Critical Rules Reference

### Core Principle
- **Rule**: `context.core_principle`
- **Key Point**:
  - Logger factory is the ONLY authorized logging mechanism
  - NON-NEGOTIABLE

### Logger Factory Rule
- **Rule**: `requirements.logger_factory.rule`
- **Key Points**:
  - ALL logging MUST use logger factory
  - NO exceptions
  - Location: `src/services/logging/logger_factory.py` (or project-specific path)

### Zero Tolerance Requirements
- **Rule**: `compliance_requirements.zero_tolerance`
- **Key Points**:
  - 0 direct `logging.getLogger()` calls (except in logger_factory itself)
  - 0 `logging.basicConfig()` calls (except in logger_factory itself)
  - 0 `print()` statements for operational logging (test scripts exempt)

### Coverage Requirements
- **Rule**: `compliance_requirements.coverage`
- **Key Points**:
  - 100% of security modules use audit logging
  - 100% of service modules have debug logging capability
  - 100% console output is JSON formatted
  - 100% file output is detailed text formatted

### Blocking Rule
- **Rule**: `enforcement.blocking.rule`
- **Key Point**:
  - Non-compliance is a blocking issue
  - Code MUST NOT proceed until fixed

---

## Mandatory Patterns

### Standard Logger Pattern
- **Key**: `mandatory_patterns.standard_logger`
- **Usage**: Standard application logging
- **Pattern**:
```python
from src.services.logging.logger_factory import get_logger
logger = get_logger(__name__)
logger.info("Message")
```

**Execute Standard Logger Validation:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'mandatory_patterns.standard_logger', and validate standard logger usage
```

### Component Logger Pattern
- **Key**: `mandatory_patterns.component_logger`
- **Usage**: Audit logging for security/compliance
- **Pattern**:
```python
from src.services.logging.logger_factory import get_component_logger
audit_logger = get_component_logger("audit", "security")
audit_logger.info("Security event", extra={"user_id": user_id, "event_type": "authentication"})
```

**Execute Component Logger Validation:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'mandatory_patterns.component_logger', and validate component logger usage
```

### Debug Logger Pattern
- **Key**: `mandatory_patterns.debug_logger`
- **Usage**: Debug logging for development/troubleshooting
- **Pattern**:
```python
from src.services.logging.logger_factory import create_debug_logger
debug_logger = create_debug_logger(__name__)
debug_logger.debug("Detailed execution flow", extra={"variable": value})
```

**Execute Debug Logger Validation:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'mandatory_patterns.debug_logger', and validate debug logger usage
```

---

## Prohibited Patterns

The following patterns are FORBIDDEN:

- **Direct `logging.getLogger(__name__)` usage**
- **`logging.basicConfig()` calls**
- **`print()` statements for operational logging** (test scripts exempt)
- **Direct `logging.info()`, `logging.error()`, etc. calls**
- **Custom logger creation outside factory**

**Key**: `prohibited_patterns`

**Execute Prohibited Patterns Validation:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'prohibited_patterns' and 'compliance_requirements.zero_tolerance', then execute prohibited patterns validation
```

---

## Compliance Requirements

### Zero Tolerance Requirements

Must achieve:
- 0 direct `logging.getLogger()` calls (except in logger_factory itself)
- 0 `logging.basicConfig()` calls (except in logger_factory itself)
- 0 `print()` statements for operational logging (test scripts exempt)

**Key**: `compliance_requirements.zero_tolerance`

**Execute Zero Tolerance Validation:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'compliance_requirements.zero_tolerance' and 'enforcement.validation', then execute zero tolerance validation
```

### Coverage Requirements

Must achieve:
- 100% of security modules use audit logging
- 100% of service modules have debug logging capability
- 100% console output is JSON formatted
- 100% file output is detailed text formatted

**Key**: `compliance_requirements.coverage`

**Execute Coverage Validation:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'compliance_requirements.coverage' and 'enforcement.validation', then execute coverage validation
```

---

## Enforcement Actions

### Validation Actions

- Scan for logging violations
- Verify logger factory usage
- Check audit logging in security modules
- Check debug logging in service modules
- Validate output formats (JSON console, text files)

**Key**: `enforcement.validation`

**Execute Validation Actions:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'enforcement.validation', and execute validation actions
```

### Blocking Rule

- Non-compliance is a blocking issue
- Code MUST NOT proceed until fixed

**Key**: `enforcement.blocking`

**Execute Blocking Rule Enforcement:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'enforcement.blocking', and execute blocking rule enforcement
```

---

## Standards Requirements

### Syslog Compliance
- **Key**: `requirements.standards.syslog_compliance`
- **Requirement**: RFC 3164/RFC 5424 compliant structured logging

### Console Format
- **Key**: `requirements.standards.console_format`
- **Requirement**: Structured JSON (machine-readable)

### File Format
- **Key**: `requirements.standards.file_format`
- **Requirement**: Detailed text (human-readable)

### Syslog Format
- **Key**: `requirements.standards.syslog_format`
- **Requirement**: Structured JSON (RFC compliant)

**Execute Standards Validation:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.standards', and execute standards validation
```

---

## Audit Logging Requirements

### Purpose
- **Key**: `requirements.audit_logging.purpose`
- **Requirement**: Cybersecurity compliance

### Component
- **Key**: `requirements.audit_logging.component`
- **Requirement**: `get_component_logger('audit', 'security')` or `get_component_logger('audit', 'compliance')`

### Required For
- **Key**: `requirements.audit_logging.required_for`
- **Requirements**:
  - Authentication events
  - Authorization events
  - Data access events
  - Security policy violations
  - Compliance events

**Execute Audit Logging Validation:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.audit_logging' and 'mandatory_patterns.component_logger', then execute audit logging validation
```

---

## Debug Logging Requirements

### Purpose
- **Key**: `requirements.debug_logging.purpose`
- **Requirement**: Development and troubleshooting

### Logger
- **Key**: `requirements.debug_logging.logger`
- **Requirement**: `create_debug_logger(__name__)` or standard logger with DEBUG level

### Required For
- **Key**: `requirements.debug_logging.required_for`
- **Requirements**:
  - Detailed execution flow
  - Variable states
  - Decision points
  - Performance metrics

**Execute Debug Logging Validation:**
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.debug_logging' and 'mandatory_patterns.debug_logger', then execute debug logging validation
```

---

## Tips for Effective Execution

1. **Start with Parse**: Always parse the file first to understand its structure
2. **Use YAML Keys**: Reference exact YAML paths for precision
3. **Index Requirements**: Use "index all requirements and patterns" to see available options
4. **Combine Sections**: Extract multiple related sections for complete validation
5. **Follow Patterns**: Always use mandatory patterns when implementing logging
6. **Avoid Prohibited Patterns**: Never use prohibited patterns
7. **Validate Compliance**: Always execute compliance validation after changes

---

## Troubleshooting

### Issue: YAML Key Not Found

**Solution**: Parse the file first to see actual structure:
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml and show YAML structure
```

### Issue: Logger Factory Not Found

**Solution**: Check logger factory location:
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.logger_factory.location', and verify logger factory location
```

### Issue: Prohibited Pattern Detected

**Solution**: Replace with mandatory pattern:
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'prohibited_patterns' and 'mandatory_patterns.standard_logger', then replace prohibited pattern with mandatory pattern
```

### Issue: Audit Logging Missing

**Solution**: Add audit logging using component logger:
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.audit_logging' and 'mandatory_patterns.component_logger', then add audit logging
```

### Issue: Debug Logging Missing

**Solution**: Add debug logging using debug logger:
```
Parse @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml, extract 'requirements.debug_logging' and 'mandatory_patterns.debug_logger', then add debug logging
```

---

## Runner Prompt (Quick Reference)

The runner prompt provides a 6-line quick reference:

```
Load and obey @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml
The logger factory (@src/services/logging/logger_factory.py) is the ONLY logger that must be used.
ALL logging MUST use logger factory functions (get_logger, get_component_logger, create_debug_logger) - NO direct logging.getLogger(), logging.basicConfig(), or print() statements.
Security modules MUST use audit logging (get_component_logger("audit", "security")) for cybersecurity compliance.
Service modules MUST have debug logging capability (create_debug_logger(__name__)) for troubleshooting.
Console output MUST be JSON formatted, file output MUST be detailed text formatted. Non-compliance is a blocking issue.
```

**Execute Runner Prompt:**
```
Load and obey @docs/implementation/instructions/97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml
```

---

**Last Updated**: 2025-12-15
**File**: `97-LOGGING_REQUIREMENTS_INSTRUCTION.yaml`
**Version**: 1.0.0
