# Protocol Index and Cross-Reference Guide
**Version**: 1.0.0
**Status**: ACTIVE & AUTHORITATIVE
**Generated**: 2026-01-12
**Session**: 20260112_CODE_IMPLEMENTATION

---

## Overview

This document provides a comprehensive index of all Australis Systems protocols, their purposes, relationships, and current versions. It serves as the authoritative reference for protocol discovery and cross-referencing.

---

## Protocol Inventory

### Active Protocols

| Protocol ID | Name | Version | Status | Domain | Purpose |
|-------------|------|---------|--------|--------|---------|
| **001** | Library Capability Discovery | v1.0.0 | ✅ Active | Capabilities | READ-ONLY analysis for discovering capabilities in libraries |
| **002** | Library Capability Onboarding Prep | v1.0.0 | ✅ Active | Capabilities | READ-ONLY validation precursor to Protocol 205 execution |
| **003** | Service Extraction & Integration | v1.0.0 | ✅ Active | Services | 7-phase workflow for extracting and integrating services |
| **202** | Pure Code Implementation | v2.0.0 | ✅ Active | Code Quality | Zero-tolerance code implementation standards |
| **205** | Sovereign Capability Construction | v1.1.0 | ✅ Active | Capabilities | Capability and service lifecycle protocol |

---

## Protocol Details

### Protocol 001: Library Capability Discovery
**File**: `libraries/_ai_agent/instructions/001-INSTRUCTION-Library_Capability_Discovery-v1.0.0.yaml`
**Version**: v1.0.0
**Type**: READ-ONLY Instruction
**Status**: ✅ Active

**Purpose**:
- Analyze existing libraries for potential capabilities
- Apply structured discovery methodology
- Identify capability extraction candidates
- Output capability inventory for Protocol 205 consumption

**Key Features**:
- **READ-ONLY**: Does not modify codebase
- **Precursor to Protocol 205**: Discovery before construction
- **Domain Categorization**: Uses 14 standardized domains
- **Structured Analysis**: PHASE 1-4 methodology (Inventory → Assessment → Categorization → Output)

**Domain Categorization** (14 domains):
- api_endpoint, auth, cli, config, core, data, discovery, fastapi_services_platform, integration, replication, sync, testing, validation, workflow

**Workflow Position**:
```
Protocol 001 (Discovery) → Protocol 002 (Prep) → Protocol 205 (Construction)
```

**References**:
- References Protocol 205 (Lines 9, 39, 41)
- Referenced by Protocol 002 (implied workflow)

**Use Cases**:
- Discovering capabilities in newly added libraries
- Auditing existing libraries for extraction opportunities
- Planning capability construction roadmap
- Identifying gaps in library coverage

---

### Protocol 002: Library Capability Onboarding Prep
**File**: `libraries/_ai_agent/instructions/002-INSTRUCTION-Library_Capability_Onboarding_Prep-v1.0.0.yaml`
**Version**: v1.0.0
**Type**: READ-ONLY/VALIDATION Instruction
**Status**: ✅ Active

**Purpose**:
- Validate prerequisites before Protocol 205 execution
- Check environment readiness (Python, tools, dependencies)
- Verify domain categorization is assigned
- Generate step-by-step execution checklist
- Ensure all blocking issues resolved

**Key Features**:
- **READ-ONLY/VALIDATION**: Does not modify codebase
- **Precursor to Protocol 205**: Preparation before construction
- **Blocking Validation**: MUST pass all checks before Protocol 205
- **Domain Categorization**: Uses same 14 domains as Protocol 001
- **Checklist Generation**: Outputs ready-to-execute commands

**Domain Categorization** (14 domains + descriptions):
```yaml
Valid Domains:
  - api_endpoint      # API/REST service implementations
  - auth             # Authentication & authorization
  - cli              # Command-line interface services
  - config           # Configuration management
  - core             # Core infrastructure
  - data             # Data processing & transformation
  - discovery        # Service discovery & registration
  - fastapi_services_platform # Core platform orchestration services
  - integration      # External system integration
  - replication      # Data replication
  - sync             # Synchronization services
  - testing          # Testing infrastructure
  - validation       # Validation & verification
  - workflow         # Workflow orchestration
```

**Workflow Position**:
```
Protocol 001 (Discovery) → Protocol 002 (Prep) → Protocol 205 (Construction)
```

**References**:
- References Protocol 205 (Lines 8, 18, 22, 38, 42, 47, 364, 403, 409, 472, 477, 491, 492)
- Referenced by None (workflow implies use after Protocol 001)

**Use Cases**:
- Validating environment before capability construction
- Generating execution checklists for Protocol 205
- Resolving blocking issues before construction begins
- Documenting prerequisites for capability construction

---

### Protocol 003: Service Extraction & Integration
**File**: `libraries/_ai_agent/instructions/003-INSTRUCTION-Service_Extraction_and_Integration-v1.0.0.yaml`
**Version**: v1.0.0
**Type**: Service Lifecycle Workflow
**Status**: ✅ Active

**Purpose**:
- Extract services from external repositories or chassis templates
- Adapt extracted code to Australis Systems standards
- Apply zero-tolerance compliance enforcement
- Generate SERVICE_MANIFEST.yaml metadata
- Validate and integrate services into library ecosystem

**Key Features**:
- **7-Phase Workflow**: Analysis → Planning → Extraction → Adaptation → Manifest → Build → Validation
- **Extraction Candidate Scoring**: 10-dimension assessment (>= 0.7 threshold)
- **Domain Categorization**: Uses same 14 domains as other protocols
- **Zero-Tolerance Enforcement**: No TODOs, stubs, or silent exceptions
- **SERVICE_MANIFEST.yaml**: Comprehensive service metadata tracking
- **Bidirectional with Protocol 205**: Services can evolve into capabilities

**7 Phases**:
1. Analysis & Discovery - Identify extraction candidates
2. Extraction Planning - Score candidates, resolve dependencies
3. Code Extraction - Copy source code to target structure
4. Code Adaptation - Apply standards and zero-tolerance
5. Manifest Generation - Create SERVICE_MANIFEST.yaml
6. Build & Dependency Management - Configure pyproject.toml
7. Validation & Integration - Verify compilation, YAML, imports

**Domain Categorization** (14 domains):
```yaml
Valid Domains:
  - api_endpoint      # API/REST service implementations
  - auth             # Authentication & authorization
  - cli              # Command-line interface services
  - config           # Configuration management
  - core             # Core infrastructure
  - data             # Data processing & transformation
  - discovery        # Service discovery & registration
  - fastapi_services_platform # Core platform orchestration services
  - integration      # External system integration
  - replication      # Data replication
  - sync             # Synchronization services
  - testing          # Testing infrastructure
  - validation       # Validation & verification
  - workflow         # Workflow orchestration
```

**Workflow Position**:
```
Protocol 003 (Service Extraction) ↔ Protocol 205 (Capability Construction)
                                   Bidirectional
                                 Complementary
                                  Relationship
```

**References**:
- References Protocol 205 (Line 48: "complementary to Protocol 205")
- Referenced by Protocol 205 (Line 109: "MUST follow Protocol 003")

**Use Cases**:
- Extracting services from external GitHub repositories
- Migrating services from chassis templates to library services
- Consolidating duplicate services across templates
- Adapting third-party code to Australis Systems standards
- Creating reusable service components from monoliths

**Additional Documentation**:
- **Workflow Guide**: `docs/implementation/guides/SERVICE_EXTRACTION_WORKFLOW_GUIDE_v1.0.0.md`

---

### Protocol 202: Pure Code Implementation
**File**: `governance/au-sys-governance/implementation/python/python-code-implementation/instructions/v2/202-INSTRUCTIONS-Pure_Code_Implementation_Execution_Protocol-v2.0.0.yaml`
**Version**: v2.0.0
**Type**: Code Quality Standard
**Status**: ✅ Active

**Purpose**:
- Enforce zero-tolerance code quality standards
- Eliminate incomplete implementations (TODOs, FIXMEs, XXXs)
- Prohibit silent exception handling
- Remove stub errors (NotImplementedError in production)
- Ensure production-ready code only

**Key Features**:
- **Zero Tolerance**: No exceptions to quality rules
- **Forbidden Patterns**:
  - Silent exception handling: `except Exception: pass`
  - Incomplete implementations: `TODO`, `FIXME`, `XXX`
  - Stub errors: `raise NotImplementedError`
  - Redundant pass statements (where docstring exists)
- **Acceptable Exceptions**:
  - `examples/` directory (tutorial/demo code)
  - `reference_repos/` directory (external reference code)
  - Detection tools (tools that search for violations)
- **Enforcement**: Applied during Protocol 003 and Protocol 205 execution

**Workflow Position**:
```
Protocol 202 (Zero Tolerance) is enforced BY:
  - Protocol 003 (Service Extraction) - Phase 4: Code Adaptation
  - Protocol 205 (Capability Construction) - adaptation_protocol section
```

**References**:
- Referenced by Protocol 003 (implicit enforcement)
- Referenced by Protocol 205 (Line: "MUST follow Protocol 202")

**Use Cases**:
- Validating code quality during service extraction
- Remediating zero-tolerance violations in existing code
- Ensuring capability construction meets production standards
- Enforcing code quality in CI/CD pipelines

---

### Protocol 205: Sovereign Capability Construction
**File**: `libraries/_ai_agent/instructions/205-PROTOCOL-Sovereign_Capability_Construction-v1.1.0.yaml`
**Version**: v1.1.0 (Updated 2026-01-12)
**Type**: Capability & Service Lifecycle Protocol
**Status**: ✅ Active

**Purpose**:
- Construct sovereign capabilities with tri-layer architecture (core/interface/manifest)
- Define service and capability lifecycle standards
- Enforce zero-tolerance compliance
- Integrate service extraction workflow (Protocol 003)
- Provide validation and verification standards

**Key Features**:
- **Tri-Layer Architecture**: core/ (domain logic), interface/ (API/Web/CLI/MCP), manifest/ (config/plugin)
- **Service Extraction Integration**: Mandates Protocol 003 for service extraction steps
- **Domain Categorization**: Uses same 14 domains as other protocols
- **Zero-Tolerance Enforcement**: Inherits Protocol 202 standards
- **Capability Validation**: Comprehensive validation checks (compilation, imports, structure)
- **Service → Capability Evolution**: Services extracted via Protocol 003 can be promoted to capabilities

**Domain Categorization** (14 domains):
```yaml
valid_domains:
  - api_endpoint      # API/REST service implementations
  - auth             # Authentication & authorization
  - cli              # Command-line interface services
  - config           # Configuration management
  - core             # Core infrastructure
  - data             # Data processing & transformation
  - discovery        # Service discovery & registration
  - fastapi_services_platform # Core platform orchestration services
  - integration      # External system integration
  - replication      # Data replication
  - sync             # Synchronization services
  - testing          # Testing infrastructure
  - validation       # Validation & verification
  - workflow         # Workflow orchestration
```

**Workflow Position**:
```
Protocol 001 (Discovery) → Protocol 002 (Prep) → Protocol 205 (Construction)
                                                         ↕
                                                   Bidirectional
                                                   Complementary
                                                         ↕
                                              Protocol 003 (Extraction)
```

**Version History**:
- **v1.0.0**: Initial capability construction protocol
- **v1.1.0** (2026-01-12): Added service extraction lifecycle integration, Protocol 003 reference, fastapi_services_platform domain

**References**:
- References Protocol 003 (Line 109: "MUST follow Protocol 003")
- Referenced by Protocols 001, 002, 003

**Use Cases**:
- Constructing new sovereign capabilities from scratch
- Promoting extracted services to full capabilities
- Enforcing tri-layer architecture for high-complexity domains
- Building function aggregates (Identity, Storage, Audit, etc.)
- Validating capability structure and compliance

**Additional Documentation**:
- **Generator Guide**: `tooling/au-sys-python-factory/docs/CAPABILITY_GENERATOR_GUIDE_v1.0.0.md`
- **Update Summary**: `libraries/_ai_agent/instructions/205-PROTOCOL-UPDATE-SUMMARY.md`

---

## Protocol Relationships

### Workflow Dependencies

```
CAPABILITY LIFECYCLE WORKFLOW
═════════════════════════════

┌──────────────────┐
│  Protocol 001    │  READ-ONLY Discovery
│  Discovery       │  • Analyze library for capabilities
│  v1.0.0          │  • Apply 14-domain categorization
└────────┬─────────┘  • Output: Capability inventory
         │
         ▼
┌──────────────────┐
│  Protocol 002    │  READ-ONLY/VALIDATION Preparation
│  Onboarding Prep │  • Validate prerequisites
│  v1.0.0          │  • Check domain categorization
└────────┬─────────┘  • Output: Readiness checklist
         │
         ▼
┌──────────────────┐  ┌──────────────────┐
│  Protocol 205    │◄─┤  Protocol 003    │
│  Capability      │  │  Service Extract │
│  Construction    │──►  & Integration   │
│  v1.1.0          │  │  v1.0.0          │
└──────────────────┘  └──────────────────┘
         │                     │
         │  Bidirectional      │
         │  Complementary      │
         │  Relationship       │
         │                     │
         │  Protocol 202       │
         │  Zero Tolerance     │
         │  v2.0.0             │
         │  (enforced by both) │
         └─────────────────────┘
```

### Cross-Reference Matrix

| Protocol | References → | Referenced By ← | Relationship Type |
|----------|--------------|-----------------|-------------------|
| **001** Discovery | 205 | None | Precursor (one-way) |
| **002** Onboarding Prep | 205 | None | Precursor (one-way) |
| **003** Service Extraction | 205 | 205 | Complementary (bidirectional) |
| **202** Zero Tolerance | None | 003, 205 | Standard (enforced by others) |
| **205** Capability Construction | 003 | 001, 002, 003 | Central protocol (multiple relationships) |

### Relationship Details

**001 → 205 (Precursor)**:
- Protocol 001 discovers capabilities FOR Protocol 205 construction
- One-way relationship: 001 outputs inventory consumed by 205
- No reverse dependency

**002 → 205 (Precursor)**:
- Protocol 002 validates prerequisites FOR Protocol 205 execution
- One-way relationship: 002 gates 205 execution (blocking validation)
- No reverse dependency

**003 ↔ 205 (Bidirectional)**:
- Protocol 003 extracts services that can become capabilities (003 → 205)
- Protocol 205 mandates use of Protocol 003 for service extraction (205 → 003)
- Complementary: Services (003) and Capabilities (205) are related but distinct
- Services can evolve into capabilities via Protocol 205

**202 → 003, 205 (Enforced Standard)**:
- Protocol 202 defines zero-tolerance standards
- Enforced during Protocol 003 Phase 4 (Code Adaptation)
- Enforced during Protocol 205 adaptation_protocol
- No explicit references in 003/205, but implicitly required

---

## Domain Categorization Standard

All protocols use the **same 14 domains** for consistency:

| Domain | Description | Protocols Using |
|--------|-------------|-----------------|
| `api_endpoint` | API/REST service implementations | 001, 002, 003, 205 |
| `auth` | Authentication & authorization | 001, 002, 003, 205 |
| `cli` | Command-line interface services | 001, 002, 003, 205 |
| `config` | Configuration management | 001, 002, 003, 205 |
| `core` | Core infrastructure | 001, 002, 003, 205 |
| `data` | Data processing & transformation | 001, 002, 003, 205 |
| `discovery` | Service discovery & registration | 001, 002, 003, 205 |
| `fastapi_services_platform` | Core platform orchestration | 001, 002, 003, 205 |
| `integration` | External system integration | 001, 002, 003, 205 |
| `replication` | Data replication | 001, 002, 003, 205 |
| `sync` | Synchronization services | 001, 002, 003, 205 |
| `testing` | Testing infrastructure | 001, 002, 003, 205 |
| `validation` | Validation & verification | 001, 002, 003, 205 |
| `workflow` | Workflow orchestration | 001, 002, 003, 205 |

**Verification Status**: ✅ All 4 protocols contain identical 14-domain categorization (verified 2026-01-12)

**Alignment Document**: `docs/implementation/in_progress/20260112_PROTOCOL_CROSS_REFERENCE_MATRIX.md`

---

## Protocol Selection Guide

### Decision Tree

```
WHICH PROTOCOL SHOULD I USE?
═══════════════════════════════

Question 1: What are you trying to do?

├─► Discover capabilities in existing library
│   └─► Use Protocol 001 (Discovery)
│       Then: Protocol 002 (Prep) → Protocol 205 (Construction)
│
├─► Validate prerequisites before capability construction
│   └─► Use Protocol 002 (Onboarding Prep)
│       Then: Protocol 205 (Construction)
│
├─► Extract service from external repo or chassis
│   └─► Use Protocol 003 (Service Extraction)
│       Optionally: Promote to capability with Protocol 205
│
├─► Enforce zero-tolerance code quality
│   └─► Use Protocol 202 (Zero Tolerance)
│       Applied during Protocol 003 or Protocol 205
│
└─► Construct new capability or promote service to capability
    └─► Use Protocol 205 (Capability Construction)
        May invoke Protocol 003 for service extraction steps
```

### Use Case Examples

**Example 1: Extracting Service from External Repo**
```
1. Run Protocol 003 (Service Extraction & Integration)
   - Follow 7-phase workflow
   - Apply zero-tolerance remediation (Protocol 202)
   - Generate SERVICE_MANIFEST.yaml
   - Validate compilation and integration

Result: Service in libraries/python/services/<domain>/<service_name>/
```

**Example 2: Building New Capability from Scratch**
```
1. Run Protocol 001 (Discovery) - Analyze what exists
2. Run Protocol 002 (Onboarding Prep) - Validate prerequisites
3. Run Protocol 205 (Capability Construction)
   - Build tri-layer structure (core/interface/manifest)
   - Apply zero-tolerance (Protocol 202)
   - Generate complete capability

Result: Capability in libraries/python/capabilities/au_sys_<name>/
```

**Example 3: Promoting Extracted Service to Capability**
```
1. Run Protocol 003 (Service Extraction) - Extract service first
   - Validate service meets zero-tolerance standards
   - Ensure SERVICE_MANIFEST.yaml complete

2. Run Protocol 001 (Discovery) - Identify capability structure
3. Run Protocol 002 (Prep) - Validate capability prerequisites
4. Run Protocol 205 (Capability Construction) - Promote to capability
   - Migrate service code to capability core/services/
   - Build interface layers (API, Web, CLI, MCP)
   - Create manifest layer (config.py, plugin.py)

Result: Capability in libraries/python/capabilities/au_sys_<name>/
         (Original service archived or deprecated)
```

---

## Additional Documentation

### Protocol Files
- **Protocol 001**: `libraries/_ai_agent/instructions/001-INSTRUCTION-Library_Capability_Discovery-v1.0.0.yaml`
- **Protocol 002**: `libraries/_ai_agent/instructions/002-INSTRUCTION-Library_Capability_Onboarding_Prep-v1.0.0.yaml`
- **Protocol 003**: `libraries/_ai_agent/instructions/003-INSTRUCTION-Service_Extraction_and_Integration-v1.0.0.yaml`
- **Protocol 202**: `governance/au-sys-governance/implementation/python/python-code-implementation/instructions/v2/202-INSTRUCTIONS-Pure_Code_Implementation_Execution_Protocol-v2.0.0.yaml`
- **Protocol 205**: `libraries/_ai_agent/instructions/205-PROTOCOL-Sovereign_Capability_Construction-v1.1.0.yaml`

### Workflow Guides
- **Service Extraction Workflow**: `docs/implementation/guides/SERVICE_EXTRACTION_WORKFLOW_GUIDE_v1.0.0.md`
- **Capability Generator Guide**: `tooling/au-sys-python-factory/docs/CAPABILITY_GENERATOR_GUIDE_v1.0.0.md`

### Cross-Reference Documents
- **Protocol Cross-Reference Matrix**: `docs/implementation/in_progress/20260112_PROTOCOL_CROSS_REFERENCE_MATRIX.md`
- **Protocol 205 Update Summary**: `libraries/_ai_agent/instructions/205-PROTOCOL-UPDATE-SUMMARY.md`

### Architecture Standards
- **Codebase Structure Blueprint**: `governance/au-sys-governance/architecture/python/CODEBASE_STRUCTURE_BLUEPRINT_v1.0.0.md`
- **Libraries Standard**: `governance/au-sys-governance/architecture/python/CODEBASE_LIBRARIES_STANDARD_v1.0.0.md`

---

## Maintenance and Updates

### Version Control

All protocols follow semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Breaking changes to protocol structure or requirements
- **MINOR**: New features, backward-compatible additions
- **PATCH**: Bug fixes, clarifications, minor corrections

### Update Procedures

**When updating a protocol**:
1. Update protocol YAML file with new version number
2. Document changes in version history section
3. Update this Protocol Index document
4. Update Protocol Cross-Reference Matrix if relationships change
5. Update affected workflow guides
6. Run cross-protocol alignment verification
7. Communicate changes to all stakeholders

**When adding a new protocol**:
1. Create protocol YAML file with version v1.0.0
2. Add entry to this Protocol Index document
3. Update Protocol Cross-Reference Matrix with relationships
4. Create workflow guide if applicable
5. Update capability/service generator guides if applicable
6. Run cross-protocol alignment verification

### Verification Schedule

- **Monthly**: Review protocol cross-references for accuracy
- **Quarterly**: Audit domain categorization consistency
- **Per Update**: Re-run alignment verification after any protocol change
- **Annual**: Comprehensive protocol ecosystem review

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Author** | GitHub Copilot (Claude Sonnet 4.5) |
| **Session** | 20260112_CODE_IMPLEMENTATION |
| **Generated** | 2026-01-12 |
| **Version** | 1.0.0 |
| **Status** | ACTIVE & AUTHORITATIVE |
| **Next Review** | 2026-02-12 (monthly) |

---

**END OF PROTOCOL INDEX**
