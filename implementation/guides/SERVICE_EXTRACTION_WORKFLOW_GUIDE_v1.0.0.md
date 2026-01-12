# Service Extraction Workflow Guide
**Protocol**: 003-INSTRUCTION-Service_Extraction_and_Integration-v1.0.0  
**Version**: 1.0.0  
**Status**: ACTIVE & AUTHORITATIVE  
**Generated**: 2026-01-12  
**Session**: 20260112_CODE_IMPLEMENTATION

---

## Table of Contents
1. [Overview](#overview)
2. [When to Use This Workflow](#when-to-use-this-workflow)
3. [Prerequisites](#prerequisites)
4. [7-Phase Workflow](#7-phase-workflow)
5. [Extraction Candidate Scoring](#extraction-candidate-scoring)
6. [Domain Categorization](#domain-categorization)
7. [Zero-Tolerance Requirements](#zero-tolerance-requirements)
8. [SERVICE_MANIFEST.yaml Specification](#service_manifestyaml-specification)
9. [Integration with Protocol 205](#integration-with-protocol-205)
10. [Troubleshooting](#troubleshooting)

---

## Overview

The **Service Extraction Workflow** (Protocol 003) is the authoritative methodology for extracting, adapting, and integrating services from external repositories or chassis templates into the Australis Systems library ecosystem.

### Key Features
- **7-Phase Structured Workflow**: From analysis to validation
- **Extraction Candidate Scoring**: Objective assessment (>= 0.7 threshold)
- **Domain Categorization**: 14 standardized domains
- **Zero-Tolerance Compliance**: No TODOs, stubs, or silent exceptions
- **SERVICE_MANIFEST.yaml**: Comprehensive service metadata
- **Protocol 205 Integration**: Services can evolve into capabilities

### Relationship to Protocol 205

```
Protocol 003: Service Extraction & Integration  ↔  Protocol 205: Capability Construction
        (Services lifecycle)                          (Capabilities lifecycle)
                                 
                                 Bidirectional
                               Complementary
                                Relationship

- Services extracted via Protocol 003 can evolve into capabilities via Protocol 205
- Protocol 205 mandates use of Protocol 003 for service extraction steps
- Both protocols enforce 14-domain categorization
- Both protocols require zero-tolerance compliance
```

---

## When to Use This Workflow

**Use Protocol 003 When**:
- ✅ Extracting services from external GitHub repositories
- ✅ Migrating services from chassis templates to library services
- ✅ Consolidating duplicate services across templates
- ✅ Adapting third-party code for Australis Systems standards
- ✅ Creating reusable service components from monoliths
- ✅ Standardizing service structures for library integration

**Use Protocol 205 When**:
- ✅ Creating new sovereign capabilities from scratch
- ✅ Evolving extracted services into full capabilities
- ✅ Building function aggregates for high-complexity domains
- ✅ Constructing tri-layer (core/interface/manifest) architectures

**Use Both When**:
- ✅ Extracting service from external repo (Protocol 003) then promoting to capability (Protocol 205)
- ✅ Protocol 205 requires service extraction as a construction step

---

## Prerequisites

### Required Tools
1. **Python 3.12+**: `python --version`
2. **Git**: `git --version`
3. **MCP Grep**: For code pattern discovery (optional but recommended)
4. **YAML Linter**: `pip install pyyaml`
5. **Compilation Validator**: Built-in `python -m py_compile`

### Required Directory Structure
```
C:/github_development/AustralisSystems/
├── libraries/
│   └── python/
│       └── services/              # TARGET OUTPUT DIRECTORY
│           ├── api_endpoint/
│           ├── auth/
│           ├── cli/
│           ├── config/
│           ├── core/
│           ├── data/
│           ├── discovery/
│           ├── fastapi_services_platform/
│           ├── integration/
│           ├── replication/
│           ├── sync/
│           ├── testing/
│           ├── validation/
│           └── workflow/
├── platforms/
│   └── _templates/                # SOURCE TEMPLATES (optional)
│       ├── au-sys-fastapi-domain-services-tmpl/
│       └── au-sys-fastapi-services-platform-tmpl/
└── libraries/
    └── _ai_agent/
        └── instructions/
            └── 003-INSTRUCTION-Service_Extraction_and_Integration-v1.0.0.yaml
```

### Required Context
- **Protocol 003 YAML**: Read the full protocol before starting
- **Domain Categorization**: Understand all 14 domains
- **Zero-Tolerance Standards**: No exceptions to code quality rules
- **SERVICE_MANIFEST.yaml Spec**: Know required fields

---

## 7-Phase Workflow

### Phase 1: Analysis & Discovery

**Objective**: Identify extraction candidates and assess their readiness

**Steps**:
1. **Repository Analysis**
   ```bash
   # Clone source repository (if external)
   git clone <repo_url>
   cd <repo_name>
   
   # Analyze directory structure
   tree -L 3 -d
   ```

2. **Service Discovery**
   - Scan for service-like directories (e.g., `services/`, `modules/`, `packages/`)
   - Identify service entry points (`__init__.py`, `main.py`, `app.py`)
   - Map dependencies and import relationships
   - Document service purposes and responsibilities

3. **Initial Assessment**
   - Count Python files: `find . -name "*.py" | wc -l`
   - Measure lines of code: `find . -name "*.py" -exec wc -l {} + | tail -1`
   - Identify external dependencies: `cat requirements.txt` or `grep "import" -r . --include="*.py" | sort -u`

4. **Output**: Extraction candidate inventory with initial scores

---

### Phase 2: Extraction Planning

**Objective**: Score candidates, resolve dependencies, and plan extraction sequence

**Steps**:
1. **Candidate Scoring** (See [Extraction Candidate Scoring](#extraction-candidate-scoring))
   - Apply 10-dimension scoring methodology
   - Calculate composite scores (0.0-1.0 range)
   - Filter candidates with score >= 0.7
   - Prioritize by score descending

2. **Dependency Resolution**
   ```bash
   # Identify import dependencies
   grep "^from " <service_file>.py | sort -u
   grep "^import " <service_file>.py | sort -u
   
   # Map dependency chains
   # Use MCP Grep or pipdeptree if available
   ```

3. **Extraction Sequencing**
   - **Rule**: Extract dependencies before dependents
   - **Example**: If `service_b` imports `service_a`, extract `service_a` first
   - Create extraction order list
   - Identify circular dependencies (resolve manually)

4. **Target Structure Planning**
   - Assign domain categories (See [Domain Categorization](#domain-categorization))
   - Define target paths in `libraries/python/services/<domain>/<service_name>/`
   - Plan SERVICE_MANIFEST.yaml content
   - Identify required adaptations

5. **Output**: Detailed extraction plan with prioritized sequence

---

### Phase 3: Code Extraction

**Objective**: Copy source code to target structure with minimal modification

**Steps**:
1. **Create Target Directory**
   ```bash
   # Example: Extracting "auth_service" to auth domain
   mkdir -p C:/github_development/AustralisSystems/libraries/python/services/auth/au_sys_auth
   cd C:/github_development/AustralisSystems/libraries/python/services/auth/au_sys_auth
   ```

2. **Copy Source Files**
   ```bash
   # Copy service code
   cp -r <source_path>/auth_service/* .
   
   # Verify file structure
   tree -L 2
   ```

3. **Create Src Layout** (MANDATORY for production services)
   ```bash
   # Move code into src/ layout for namespace protection
   mkdir -p src/au_sys_auth
   mv *.py src/au_sys_auth/
   mv modules/ src/au_sys_auth/ # Move subdirectories
   
   # Create src/__init__.py if missing
   touch src/au_sys_auth/__init__.py
   ```

4. **Preserve Git History** (Optional but recommended)
   ```bash
   # If you want to preserve commit history
   git log --oneline <original_file_path>
   # Document original commit SHAs in SERVICE_MANIFEST.yaml
   ```

5. **Output**: Copied code in target directory with src/ layout

---

### Phase 4: Code Adaptation

**Objective**: Adapt extracted code to Australis Systems standards with zero-tolerance compliance

**Steps**:
1. **Import Path Updates**
   ```python
   # OLD (external repo structure)
   from auth_service.models import User
   from auth_service.utils import hash_password
   
   # NEW (Australis Systems library structure)
   from au_sys_auth.models import User
   from au_sys_auth.utils import hash_password
   ```

2. **Zero-Tolerance Remediation** (See [Zero-Tolerance Requirements](#zero-tolerance-requirements))
   ```bash
   # Search for violations
   grep -r "TODO\|FIXME\|XXX" src/ --include="*.py"
   grep -r "except.*:.*pass" src/ --include="*.py"
   grep -r "raise NotImplementedError" src/ --include="*.py"
   
   # Remediate all findings (NO EXCEPTIONS)
   ```

3. **Standards Alignment**
   - **Logging**: Replace `print()` with `logging.getLogger(__name__)`
   - **Error Handling**: Add `logger.debug()` to all except blocks with context
   - **Type Hints**: Add type annotations where missing
   - **Docstrings**: Add/update docstrings for all public functions/classes

4. **Configuration Externalization**
   - Move hardcoded values to `config.py` or environment variables
   - Use Pydantic BaseSettings for configuration
   - Document all configuration variables

5. **Output**: Adapted code meeting Australis Systems standards

---

### Phase 5: Manifest Generation

**Objective**: Create comprehensive SERVICE_MANIFEST.yaml for metadata tracking

**Steps**:
1. **Create SERVICE_MANIFEST.yaml**
   ```bash
   touch SERVICE_MANIFEST.yaml
   ```

2. **Populate Metadata** (See [SERVICE_MANIFEST.yaml Specification](#service_manifestyaml-specification))
   ```yaml
   service_name: "au_sys_auth"
   version: "0.1.0"
   domain: "auth"
   description: "Authentication and authorization service"
   # ... see full spec below
   ```

3. **Document Dependencies**
   ```bash
   # Extract dependencies from imports
   grep "^from \|^import " src/**/*.py | sort -u > dependencies.txt
   
   # Categorize: internal_dependencies vs external_dependencies
   ```

4. **Record Extraction Metadata**
   - Source repository URL
   - Source commit SHA
   - Extraction date
   - Extraction candidate score
   - Modifications applied

5. **Output**: Complete SERVICE_MANIFEST.yaml

---

### Phase 6: Build & Dependency Management

**Objective**: Configure Python packaging and dependency management

**Steps**:
1. **Create pyproject.toml** (MANDATORY for library services)
   ```toml
   [build-system]
   requires = ["hatchling"]
   build-backend = "hatchling.build"
   
   [project]
   name = "au-sys-auth"
   version = "0.1.0"
   description = "Authentication and authorization service"
   requires-python = ">=3.12"
   dependencies = [
       "fastapi>=0.104.0",
       "pydantic>=2.0.0",
       # ... extracted dependencies
   ]
   
   [tool.hatch.build.targets.wheel]
   packages = ["src/au_sys_auth"]
   ```

2. **Extract Dependencies from Source**
   ```bash
   # If source has requirements.txt
   cat <source_path>/requirements.txt
   
   # Convert to pyproject.toml dependencies format
   # Add version constraints if known
   ```

3. **Validate Dependency Versions**
   ```bash
   # Install in virtual environment for testing
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e .
   
   # Run tests if available
   pytest
   ```

4. **Output**: pyproject.toml with validated dependencies

---

### Phase 7: Validation & Integration

**Objective**: Verify service meets all quality standards and integrates successfully

**Steps**:
1. **Compilation Validation**
   ```bash
   # Validate all Python files compile without syntax errors
   find src/ -name "*.py" -exec python -m py_compile {} \;
   
   # Check for compilation errors
   echo $?  # Should output 0 (success)
   ```

2. **YAML Validation**
   ```bash
   # Validate SERVICE_MANIFEST.yaml parses correctly
   python -c "import yaml; yaml.safe_load(open('SERVICE_MANIFEST.yaml'))"
   
   # Check for YAML parsing errors
   echo $?  # Should output 0 (success)
   ```

3. **Import Validation**
   ```python
   # Test service can be imported
   python -c "import au_sys_auth; print(f'✅ au_sys_auth v{au_sys_auth.__version__}')"
   ```

4. **Zero-Tolerance Final Check**
   ```bash
   # Final scan for any violations
   grep -r "TODO\|FIXME\|XXX" src/ --include="*.py"
   grep -r "except.*:.*pass" src/ --include="*.py"
   grep -r "raise NotImplementedError" src/ --include="*.py"
   
   # Expected: Zero matches (except in examples/ or reference_repos/)
   ```

5. **Integration Testing** (if applicable)
   - Test service in isolation
   - Test service with dependent services
   - Verify FastAPI routes work (if applicable)
   - Check database connections (if applicable)

6. **Documentation Generation**
   ```bash
   # Generate API documentation if applicable
   # Update library service index
   # Create extraction summary report
   ```

7. **Output**: Validated, integrated service ready for production use

---

## Extraction Candidate Scoring

### Scoring Methodology

Each extraction candidate is scored across 10 dimensions (0.0-1.0 each):

| Dimension | Weight | Description | How to Score |
|-----------|--------|-------------|--------------|
| **Functional Completeness** | 0.15 | Service implements complete workflow | 0.0 = stub only, 0.5 = partial, 1.0 = complete |
| **Self-Containment** | 0.15 | Minimal external dependencies | 0.0 = tightly coupled, 0.5 = moderate, 1.0 = standalone |
| **Code Quality** | 0.15 | Clean, maintainable, documented | 0.0 = poor quality, 0.5 = acceptable, 1.0 = excellent |
| **Dependency Complexity** | 0.10 | Simple dependency graph | 0.0 = many dependencies, 0.5 = moderate, 1.0 = few dependencies |
| **Domain Clarity** | 0.10 | Clear domain categorization | 0.0 = ambiguous, 0.5 = somewhat clear, 1.0 = obvious |
| **Reusability Potential** | 0.10 | Applicable to multiple use cases | 0.0 = single-use, 0.5 = some reuse, 1.0 = highly reusable |
| **Test Coverage** | 0.10 | Existing tests included | 0.0 = no tests, 0.5 = partial, 1.0 = comprehensive |
| **Configuration Externalization** | 0.05 | Config separated from code | 0.0 = hardcoded, 0.5 = partial, 1.0 = fully external |
| **Documentation Quality** | 0.05 | Docstrings and README present | 0.0 = none, 0.5 = minimal, 1.0 = comprehensive |
| **Adaptation Effort** | 0.05 | Low effort to meet standards | 0.0 = major work, 0.5 = moderate, 1.0 = minimal |

**Composite Score Calculation**:
```python
composite_score = (
    functional_completeness * 0.15 +
    self_containment * 0.15 +
    code_quality * 0.15 +
    dependency_complexity * 0.10 +
    domain_clarity * 0.10 +
    reusability_potential * 0.10 +
    test_coverage * 0.10 +
    configuration_externalization * 0.05 +
    documentation_quality * 0.05 +
    adaptation_effort * 0.05
)
```

### Extraction Threshold

**Extraction Criteria**:
- **Score >= 0.7**: Extract immediately (high-quality candidate)
- **Score 0.5-0.7**: Extract if strategic value high, plan extra adaptation effort
- **Score < 0.5**: Do NOT extract - requires excessive work, high risk

### Example Scoring

**Example 1: High-Quality Candidate**
```yaml
service_name: "authentication_service"
scores:
  functional_completeness: 0.9  # Complete JWT auth implementation
  self_containment: 0.8          # Only depends on FastAPI and pydantic
  code_quality: 0.9              # Clean, type-hinted, documented
  dependency_complexity: 0.9     # Simple dependency graph
  domain_clarity: 1.0            # Clearly belongs to "auth" domain
  reusability_potential: 1.0     # Applicable to any FastAPI project
  test_coverage: 0.7             # Some tests present
  configuration_externalization: 0.8
  documentation_quality: 0.6
  adaptation_effort: 0.8         # Minor import path updates needed
  
composite_score: 0.86  # EXTRACT IMMEDIATELY ✅
```

**Example 2: Low-Quality Candidate**
```yaml
service_name: "utility_functions"
scores:
  functional_completeness: 0.3   # Mix of unrelated utilities
  self_containment: 0.4           # Imports from many places
  code_quality: 0.3               # Poorly documented, no type hints
  dependency_complexity: 0.3      # Depends on 20+ packages
  domain_clarity: 0.2             # Unclear which domain this belongs to
  reusability_potential: 0.4      # Very specific to original project
  test_coverage: 0.1              # Minimal tests
  configuration_externalization: 0.2
  documentation_quality: 0.1
  adaptation_effort: 0.2          # Major refactoring required
  
composite_score: 0.28  # DO NOT EXTRACT ❌
```

---

## Domain Categorization

### 14 Valid Domains

Every service MUST be assigned to exactly ONE domain:

| Domain | Description | Examples |
|--------|-------------|----------|
| `api_endpoint` | API/REST service implementations | REST API handlers, GraphQL endpoints |
| `auth` | Authentication & authorization | JWT auth, OAuth2, RBAC, session management |
| `cli` | Command-line interface services | CLI tools, scripts, terminal applications |
| `config` | Configuration management | Config loaders, settings management, env vars |
| `core` | Core infrastructure | Kernel services, base abstractions, foundational utilities |
| `data` | Data processing & transformation | ETL pipelines, data mappers, transformers |
| `discovery` | Service discovery & registration | Service registries, health checks, discovery clients |
| `fastapi_services_platform` | Core platform orchestration services | FastAPI engines, routers, lifecycle managers, platform infra |
| `integration` | External system integration | Third-party API clients, webhooks, integrations |
| `replication` | Data replication | Database replication, cache sync, data mirrors |
| `sync` | Synchronization services | State synchronization, distributed coordination |
| `testing` | Testing infrastructure | Test frameworks, fixtures, mocks, test utilities |
| `validation` | Validation & verification | Data validators, schema validators, integrity checks |
| `workflow` | Workflow orchestration | Workflow engines, state machines, automation |

### Decision Tree

```
SERVICE DOMAIN CATEGORIZATION
═════════════════════════════

Question 1: What is the service's PRIMARY responsibility?

├─► Authentication/Authorization logic?
│   └─► Domain: auth
│
├─► API endpoint implementation (REST/GraphQL)?
│   └─► Domain: api_endpoint
│
├─► Command-line interface?
│   └─► Domain: cli
│
├─► Configuration management?
│   └─► Domain: config
│
├─► Core infrastructure (kernel, base services)?
│   └─► Domain: core
│
├─► Data processing/transformation?
│   └─► Domain: data
│
├─► Service discovery/registration?
│   └─► Domain: discovery
│
├─► FastAPI platform orchestration (engines, routers, lifecycle)?
│   └─► Domain: fastapi_services_platform
│
├─► External system integration?
│   └─► Domain: integration
│
├─► Data replication across systems?
│   └─► Domain: replication
│
├─► Synchronization between services?
│   └─► Domain: sync
│
├─► Testing infrastructure/frameworks?
│   └─► Domain: testing
│
├─► Validation/verification logic?
│   └─► Domain: validation
│
└─► Workflow orchestration/automation?
    └─► Domain: workflow

CRITICAL RULES:
1. Each service MUST have exactly ONE domain
2. Choose the MOST SPECIFIC domain that matches primary function
3. If multiple domains seem applicable, choose based on PRIMARY responsibility
4. Domain categorization is MANDATORY for Protocol 003 compliance
```

---

## Zero-Tolerance Requirements

### Forbidden Patterns

**ZERO INSTANCES ALLOWED** in production service code:

1. **Silent Exception Handling**
   ```python
   # ❌ FORBIDDEN
   try:
       risky_operation()
   except Exception:
       pass  # Silent failure
   
   # ✅ REQUIRED
   try:
       risky_operation()
   except Exception as e:
       logger.debug(
           f"Operation failed but continuing: {e}",
           extra={"error": str(e), "context": "operation_name"}
       )
   ```

2. **Incomplete Implementations**
   ```python
   # ❌ FORBIDDEN
   def feature():
       # TODO: Implement this
       pass
   
   def feature():
       # FIXME: This is broken
       return None
   
   def feature():
       # XXX: Hack, needs proper solution
       return workaround()
   
   # ✅ REQUIRED
   def feature():
       """Fully implemented feature with proper logic."""
       result = complete_implementation()
       logger.info("Feature executed successfully")
       return result
   ```

3. **Stub Errors**
   ```python
   # ❌ FORBIDDEN (in production code)
   def feature():
       raise NotImplementedError("Not implemented yet")
   
   # ✅ ACCEPTABLE (only as sentinel/guard pattern)
   def _enforce_override():
       raise NotImplementedError(
           "CRITICAL: This method must be overridden. "
           "See Protocol 203 for proper dependency injection."
       )
   
   # ✅ REQUIRED (for production)
   def feature():
       """Complete implementation."""
       return implemented_logic()
   ```

4. **Redundant Pass Statements**
   ```python
   # ❌ FORBIDDEN (where docstring exists)
   class MyClass:
       """This is a class."""
       pass  # Redundant
   
   # ✅ REQUIRED
   class MyClass:
       """This is a class."""
       # No pass needed - docstring is sufficient
   ```

### Acceptable Exceptions

**ONLY ACCEPTABLE** in these contexts:

- `examples/` directory - tutorial/demo code may contain TODOs
- `reference_repos/` directory - external reference code unchanged
- Detection tools (e.g., `scaffold_detection_service.py`) - tools that search for violations

**PRODUCTION SERVICE CODE**: **ZERO TOLERANCE - NO EXCEPTIONS**

---

## SERVICE_MANIFEST.yaml Specification

### Mandatory Fields

```yaml
# SERVICE_MANIFEST.yaml v1.0.0
# MANDATORY for all library services

service_name: "au_sys_<service_name>"  # MUST match directory name
version: "0.1.0"                        # Semantic versioning
domain: "<domain_category>"             # One of 14 valid domains
description: "Service purpose summary"  # Clear, concise description

# Source metadata
source:
  repository_url: "https://github.com/org/repo"  # Original source (if applicable)
  commit_sha: "abc123def456"                    # Source commit (if tracked)
  extraction_date: "2026-01-12"                 # When extracted
  extraction_method: "Protocol 003 v1.0.0"      # Methodology used

# Extraction candidate assessment
extraction_candidate_score:
  composite: 0.86                               # Overall score (0.0-1.0)
  functional_completeness: 0.9
  self_containment: 0.8
  code_quality: 0.9
  dependency_complexity: 0.9
  domain_clarity: 1.0
  reusability_potential: 1.0
  test_coverage: 0.7
  configuration_externalization: 0.8
  documentation_quality: 0.6
  adaptation_effort: 0.8

# File structure
structure:
  entry_point: "src/au_sys_<service>/main.py"   # Primary entry point
  src_layout: true                               # Uses src/ layout (MANDATORY)
  core_modules:                                  # Core service modules
    - "src/au_sys_<service>/core/"
  interface_modules:                             # Interface modules (if any)
    - "src/au_sys_<service>/api/"
  config_modules:                                # Configuration modules
    - "src/au_sys_<service>/config.py"

# Dependencies
dependencies:
  internal_dependencies:                         # Other AU-SYS services
    - "au_sys_logging"
    - "au_sys_config"
  external_dependencies:                         # PyPI packages
    - name: "fastapi"
      version: ">=0.104.0"
      purpose: "API framework"
    - name: "pydantic"
      version: ">=2.0.0"
      purpose: "Data validation"

# Modifications applied during extraction
modifications:
  - type: "import_path_update"
    description: "Updated imports from original structure to AU-SYS library paths"
  - type: "zero_tolerance_remediation"
    description: "Removed 3 TODO comments, implemented placeholder functions"
  - type: "logging_standardization"
    description: "Replaced print() with logging.getLogger(__name__)"
  - type: "configuration_externalization"
    description: "Moved hardcoded values to config.py"

# Compliance
compliance:
  zero_tolerance: true                           # Meets zero-tolerance standards
  protocol_003: "v1.0.0"                        # Protocol 003 compliant
  protocol_205_ready: false                      # Not yet a full capability
  compilation_validated: true                    # All files compile
  yaml_validated: true                           # This YAML parses

# Status
status: "active"                                 # active | deprecated | archived
maturity: "alpha"                               # alpha | beta | stable | mature
maintainer: "Australis Systems Factory Team"
created: "2026-01-12"
updated: "2026-01-12"

# Notes
notes:
  - "Extracted from au-sys-fastapi-services-platform-tmpl chassis"
  - "Candidate for promotion to full capability via Protocol 205"
  - "Requires additional testing before production deployment"
```

### Validation

```bash
# Validate SERVICE_MANIFEST.yaml
python -c "import yaml; manifest = yaml.safe_load(open('SERVICE_MANIFEST.yaml')); print(f'✅ Valid: {manifest[\"service_name\"]}')"

# Check required fields
python -c "
import yaml
manifest = yaml.safe_load(open('SERVICE_MANIFEST.yaml'))
required = ['service_name', 'version', 'domain', 'description', 'source', 'structure', 'dependencies', 'compliance', 'status']
missing = [f for f in required if f not in manifest]
if missing:
    print(f'❌ Missing fields: {missing}')
else:
    print('✅ All required fields present')
"
```

---

## Integration with Protocol 205

### When to Use Protocol 205 After Extraction

After successfully extracting a service via Protocol 003, consider promoting it to a **Sovereign Capability** via Protocol 205 if:

1. **High Complexity Domain**: Service operates in domain requiring tri-layer architecture (core/interface/manifest)
2. **Function Aggregate**: Service aggregates multiple related functions (not single-purpose)
3. **Multi-Interface Support**: Service needs API, Web, CLI, and MCP interfaces
4. **Strategic Importance**: Service is foundational to platform architecture
5. **Capability Standards**: Service should enforce capability-level standards

### Promotion Workflow

```
Phase 1: Service Extraction (Protocol 003)
    ↓
[Service in libraries/python/services/<domain>/au_sys_<name>/]
    ↓
Phase 2: Assessment for Capability Promotion
    ↓
Decision: Promote to Capability?
    ↓ YES
Phase 3: Capability Construction (Protocol 205)
    ↓
[Capability in libraries/python/capabilities/au_sys_<name>/]
with full tri-layer structure (core/interface/manifest)
```

### Protocol 003 → 205 Transition Checklist

- [ ] Service meets zero-tolerance standards (Protocol 003 compliance)
- [ ] Service has clear domain categorization
- [ ] Service has SERVICE_MANIFEST.yaml
- [ ] Service compiled and tested successfully
- [ ] Decision made: Service qualifies for capability promotion
- [ ] Run Protocol 001 (Capability Discovery) to identify capability structure
- [ ] Run Protocol 002 (Onboarding Prep) to validate prerequisites
- [ ] Execute Protocol 205 (Capability Construction) to build tri-layer structure
- [ ] Migrate service code to capability core/services/
- [ ] Build interface layers (API, Web, CLI, MCP as needed)
- [ ] Create manifest layer (config.py, plugin.py)
- [ ] Validate capability with verify_capability.py
- [ ] Archive original service or mark as deprecated

---

## Troubleshooting

### Common Issues

#### Issue 1: "Service fails compilation after extraction"

**Symptoms**: `python -m py_compile` returns syntax errors

**Causes**:
- Import paths not updated correctly
- Missing `__init__.py` files
- Python version incompatibility (< 3.12)

**Solutions**:
```bash
# Verify Python version
python --version  # Must be 3.12+

# Check all __init__.py files exist
find src/ -type d -exec test -f {}/__init__.py \; -print

# Update import paths systematically
grep -r "from <old_import_path>" src/ --include="*.py"
# Replace with new paths
```

#### Issue 2: "SERVICE_MANIFEST.yaml fails validation"

**Symptoms**: YAML parsing error or missing required fields

**Causes**:
- Incorrect YAML syntax (indentation, missing colons)
- Missing mandatory fields
- Invalid domain category

**Solutions**:
```bash
# Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('SERVICE_MANIFEST.yaml'))"

# Check required fields
python -c "
import yaml
manifest = yaml.safe_load(open('SERVICE_MANIFEST.yaml'))
print('Domain:', manifest.get('domain'))
print('Valid domains:', ['api_endpoint', 'auth', 'cli', 'config', 'core', 'data', 'discovery', 'fastapi_services_platform', 'integration', 'replication', 'sync', 'testing', 'validation', 'workflow'])
"

# Fix indentation issues (use 2 spaces per level)
```

#### Issue 3: "Zero-tolerance violations found"

**Symptoms**: grep searches find TODO, FIXME, XXX, or silent pass statements

**Causes**:
- Incomplete code adaptation
- Overlooked TODOs in source code
- Silent exception handlers not remediated

**Solutions**:
```bash
# Find all violations
grep -r "TODO\|FIXME\|XXX" src/ --include="*.py" -n
grep -r "except.*:.*pass" src/ --include="*.py" -n
grep -r "raise NotImplementedError" src/ --include="*.py" -n

# Remediate each violation
# - Remove TODOs: Implement the feature or document as future enhancement
# - Fix silent passes: Add logger.debug() with context
# - Replace NotImplementedError: Implement the method or remove it

# Re-validate after remediation
```

#### Issue 4: "Circular dependency detected"

**Symptoms**: Service A imports Service B, Service B imports Service A

**Causes**:
- Tight coupling between services
- Poor separation of concerns in original code

**Solutions**:
1. **Refactor to remove circular dependency**:
   - Extract shared code to new `core` service
   - Use dependency injection instead of direct imports
   - Reorganize module structure

2. **Defer import** (temporary workaround):
   ```python
   # Instead of top-level import
   # from au_sys_service_b import function
   
   # Use local import
   def my_function():
       from au_sys_service_b import function
       return function()
   ```

3. **Document and prioritize refactoring**:
   - Add note to SERVICE_MANIFEST.yaml
   - Plan refactoring in next iteration

#### Issue 5: "Domain categorization unclear"

**Symptoms**: Service seems to fit multiple domains

**Causes**:
- Service has multiple responsibilities (violates Single Responsibility Principle)
- Service is poorly defined in original codebase

**Solutions**:
1. **Identify PRIMARY responsibility**:
   - What is the service's MAIN purpose?
   - What would break if this service was removed?
   - Which domain is most affected by this service?

2. **Split service if necessary**:
   - If service has 2+ distinct responsibilities, extract each into separate services
   - Example: "auth_and_logging_service" → split into "auth" and "logging" services

3. **Use decision tree** (See [Domain Categorization](#domain-categorization))

---

## Additional Resources

### Protocol Files
- **Protocol 003**: `libraries/_ai_agent/instructions/003-INSTRUCTION-Service_Extraction_and_Integration-v1.0.0.yaml`
- **Protocol 205**: `libraries/_ai_agent/instructions/205-PROTOCOL-Sovereign_Capability_Construction-v1.1.0.yaml`
- **Protocol 001**: `libraries/_ai_agent/instructions/001-INSTRUCTION-Library_Capability_Discovery-v1.0.0.yaml`
- **Protocol 002**: `libraries/_ai_agent/instructions/002-INSTRUCTION-Library_Capability_Onboarding_Prep-v1.0.0.yaml`

### Cross-Reference Documentation
- **Protocol Cross-Reference Matrix**: `docs/implementation/in_progress/20260112_PROTOCOL_CROSS_REFERENCE_MATRIX.md`
- **Capability Generator Guide**: `tooling/au-sys-python-factory/docs/CAPABILITY_GENERATOR_GUIDE_v1.0.0.md`

### Architecture Standards
- **Codebase Structure Blueprint**: `governance/au-sys-governance/architecture/python/CODEBASE_STRUCTURE_BLUEPRINT_v1.0.0.md`
- **Libraries Standard**: `governance/au-sys-governance/architecture/python/CODEBASE_LIBRARIES_STANDARD_v1.0.0.md`

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Author** | GitHub Copilot (Claude Sonnet 4.5) |
| **Session** | 20260112_CODE_IMPLEMENTATION |
| **Generated** | 2026-01-12 |
| **Version** | 1.0.0 |
| **Status** | ACTIVE & AUTHORITATIVE |
| **Protocol** | 003-INSTRUCTION-Service_Extraction_and_Integration-v1.0.0 |

---

**END OF SERVICE EXTRACTION WORKFLOW GUIDE**
