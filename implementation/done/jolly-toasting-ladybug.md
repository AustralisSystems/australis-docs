# Status: COMPLETED
# Execution Date: 2026-01-13
# Executor: GitHub Copilot (Gemini 3 Pro)
# Outcome: Tool rewritten, Subdirectory preservation implemented & verified.

# Plan: Preserve Subdirectory Structure in Service Extraction

## Problem Statement

The current `adapt_extracted_code.py` tool **flattens** source subdirectories when extracting services to tri-layer structure. This causes:

1. **Loss of domain organization**: `microsoft/services/azure/auth/manager.py` → `core/services/manager.py` (loses azure/auth context)
2. **Potential naming conflicts**: Multiple files with same name from different subdirectories collide
3. **Incorrect fallback**: Unclassified files go to `interface/cli/` instead of `core/services/`

**Current Behavior:**
```
SOURCE: microsoft/services/azure/auth/manager.py
  ↓ (flattened)
TARGET: microsoft/src/microsoft/core/services/manager.py  ❌ Lost structure!
```

**Desired Behavior:**
```
SOURCE: microsoft/services/azure/auth/manager.py
  ↓ (preserved)
TARGET: microsoft/src/microsoft/core/services/azure/auth/manager.py  ✅ Structure intact!
```

## Understanding: Canonical Tri-Layer Structure

Based on analysis of `scaffold_capability.py` and Protocol 205:

**Foundation (created by scaffold):**
```
core/
├── models/
├── schemas/
├── services/       ← Base directory
├── ports/
├── observability/
└── utils/

interface/
├── api/routers/
├── web/
├── cli/
└── mcp/

manifest/
└── config.py
```

**Extension Pattern (for complex capabilities):**
```
core/services/
├── azure/          ← Domain-specific subdirectories
│   ├── auth/       ← Feature-specific subdirectories
│   │   └── manager.py
│   └── provisioning/
└── m365/
    └── search/
```

**Key Insight:** Domain organization happens WITHIN tri-layer components via nested subdirectories, NOT at the capability name level.

## Solution Design

### 1. Preserve Source Subdirectory Structure

**Strategy:** Extract subdirectory path from source, append to target_package

**Implementation Steps:**

#### Step 1.1: Capture Subdirectory Path (classify_file method)

**Location:** `adapt_extracted_code.py` lines 68-229

**Current Code (Line 77-81):**
```python
classification = {
    'file_path': str(file_path.relative_to(self.source_path)),
    'type': 'unknown',
    'target_layer': None,
    'target_package': None,
    'target_filename': file_path.name,  # ❌ Only filename
    ...
}
```

**New Code:**
```python
# Extract relative path from source root
source_rel_path = file_path.relative_to(self.source_path)

# Extract parent subdirectory (preserve structure)
# Example: "services/azure/auth/manager.py" → "services/azure/auth"
subdir_path = str(source_rel_path.parent) if source_rel_path.parent != Path('.') else ''

classification = {
    'file_path': str(source_rel_path),
    'source_subdirs': subdir_path,  # ✅ NEW: Preserve subdirectories
    'type': 'unknown',
    'target_layer': None,
    'target_package': None,
    'target_filename': file_path.name,
    ...
}
```

#### Step 1.2: Merge Subdirectory Path with target_package

**Location:** After classification logic (new helper method)

**Add New Method:**
```python
def _merge_target_package(self, base_package: str, source_subdirs: str) -> str:
    """
    Merge base target_package with source subdirectories.

    Examples:
        base='services', subdirs='azure/auth' → 'services/azure/auth'
        base='api/routers', subdirs='v1/azure' → 'api/routers/v1/azure'
        base='schemas', subdirs='models' → 'schemas/models'

    Args:
        base_package: Target package from classification (e.g., 'services')
        source_subdirs: Subdirectory path from source (e.g., 'azure/auth')

    Returns:
        Merged package path (e.g., 'services/azure/auth')
    """
    if not source_subdirs or source_subdirs == '.':
        return base_package

    if not base_package:
        return source_subdirs

    # Combine base package with preserved subdirectories
    return f"{base_package}/{source_subdirs}".replace('//', '/')
```

#### Step 1.3: Apply Merge After Each Classification

**Location:** Throughout classification logic (lines 108-227)

**Pattern to Apply:**

**Before:**
```python
classification.update({
    'type': 'service',
    'target_layer': 'core',
    'target_package': 'services',  # ❌ Flat
    'confidence': 0.7,
})
```

**After:**
```python
base_package = 'services'
merged_package = self._merge_target_package(base_package, classification['source_subdirs'])

classification.update({
    'type': 'service',
    'target_layer': 'core',
    'target_package': merged_package,  # ✅ 'services/azure/auth'
    'confidence': 0.7,
})
```

**Apply to ALL classification branches:**
- Line 110-114: Pydantic schemas → `schemas/{subdirs}`
- Line 117-122: SQLAlchemy models → `models/{subdirs}`
- Line 127-132: FastAPI routers → `api/routers/{subdirs}`
- Line 137-142: CLI commands → `cli/{subdirs}`
- Line 147-152: MCP tools → `mcp/{subdirs}`
- Line 170-175: Services → `services/{subdirs}` ✅ **PRIMARY USE CASE**
- Line 181-185: Utils → `utils/{subdirs}`
- Line 213-218: Default services → `services/{subdirs}`
- Line 221-226: Default utils → `utils/{subdirs}`

### 2. Fix Fallback Default (interface/cli → core/services)

**Problem:** Files without explicit framework markers incorrectly default to `interface/cli/`

**Root Cause Analysis:**

Looking at the microsoft extraction results:
- 87 files in `interface/cli/`
- Most are factories, managers, provisioners (NOT CLI handlers)
- These files have `has_classes=True` and `has_functions=True` but no framework patterns

**Current Fallback (Lines 210-227):**
```python
elif classification['type'] == 'unknown':
    if classification['has_classes']:
        classification.update({
            'type': 'service',
            'target_layer': 'core',
            'target_package': 'services',  # ✅ Correct!
            'confidence': 0.5,
        })
```

**Question:** Why did these files NOT trigger this fallback?

**Answer:** They were classified BEFORE reaching the fallback! Likely matched:
- Line 136-142: CLI detection (incorrect match)
- OR classification['type'] was set earlier but confidence was too low

**Solution:** Strengthen CLI detection to ONLY match actual CLI files

**Current CLI Detection (Lines 136-142):**
```python
elif 'typer' in frameworks or 'click' in imports:
    classification.update({
        'type': 'cli',
        'target_layer': 'interface',
        'target_package': 'cli',
        'confidence': 0.9,
    })
```

**Enhanced CLI Detection:**
```python
# 3. CLI Commands (Typer/Click ONLY) - Strict detection
cli_indicators = [
    'typer' in frameworks,
    'click' in imports,
    'argparse' in imports,
    '@app.command' in content,
    '@click.command' in content,
    'if __name__ == "__main__"' in content and 'sys.argv' in content,
]

if any(cli_indicators):
    base_package = 'cli'
    merged_package = self._merge_target_package(base_package, classification['source_subdirs'])

    classification.update({
        'type': 'cli',
        'target_layer': 'interface',
        'target_package': merged_package,
        'confidence': 0.9,
        'justification': ['Contains CLI framework or main entry point']
    })
```

### 3. Apply Subdirectory Preservation to All Tri-Layer Components

**Scope:** ALL classification branches (not just core/services)

**Rationale:**
- `core/schemas/`: May have domain-specific schema groupings (azure/, m365/)
- `core/models/`: May have ORM model groupings
- `interface/api/routers/`: Should preserve API versioning (v1/, v2/) and domain groupings
- `interface/web/`: May have feature-specific routers
- Consistency across all components

**Implementation:** Already covered by Step 1.3 (apply merge to ALL branches)

### 4. Update copy_mapped_files Destination Logic

**Current Code (Lines 477-483):**
```python
# Paths
src_file = source_path / source_rel

# Prepare destination
layer = info['target_layer']
pkg_path = info['target_package'].replace('.', '/') if info['target_package'] else ''
dest_dir = package_root / layer / pkg_path
dest_file = dest_dir / info['target_filename']  # ❌ Only filename
```

**No changes needed!** The `target_package` now contains the full path (e.g., `services/azure/auth`), so:
- `pkg_path` = `services/azure/auth`
- `dest_dir` = `package_root/core/services/azure/auth/`
- `dest_file` = `package_root/core/services/azure/auth/manager.py` ✅

The existing logic will automatically create the nested directory structure!

## Critical Files to Modify

### Primary File
**C:/github_development/AustralisSystems/libraries/_ai_agent/tools/adapt_extracted_code.py**

**Sections to Modify:**
1. **Lines 68-88**: Add `source_subdirs` to classification dict
2. **Lines 101-229**: Add `_merge_target_package()` helper method (new)
3. **Lines 108-227**: Apply merge to ALL classification update blocks (12 locations)
4. **Lines 136-142**: Strengthen CLI detection logic

**Estimated Changes:**
- +30 lines (new helper method)
- ~50 line modifications (apply merge pattern)
- Total: ~80 lines changed

### Supporting Files (Review Only)
- **C:/github_development/AustralisSystems/libraries/_ai_agent/tools/extract_code.py**: No changes needed (extraction logic unchanged)
- **C:/github_development/AustralisSystems/libraries/_ai_agent/tools/standardize_service.py**: No changes needed (SERVICE_MANIFEST unchanged)

## Edge Cases & Considerations

### Edge Case 1: Root-Level Files

**Scenario:** `source/manager.py` (no subdirectories)

**Handling:**
```python
source_subdirs = ''  # Empty string
merged = _merge_target_package('services', '')  → 'services'
Result: core/services/manager.py  ✅ Flat (as intended)
```

### Edge Case 2: Deep Nesting

**Scenario:** `source/services/azure/provisioning/aks/deployment.py`

**Handling:**
```python
source_subdirs = 'services/azure/provisioning/aks'
merged = _merge_target_package('services', 'services/azure/provisioning/aks')
  → 'services/services/azure/provisioning/aks'  ❌ Duplication!
```

**Solution:** Strip common prefix

**Enhanced Merge Method:**
```python
def _merge_target_package(self, base_package: str, source_subdirs: str) -> str:
    """Merge with duplicate prefix handling."""
    if not source_subdirs or source_subdirs == '.':
        return base_package

    if not base_package:
        return source_subdirs

    # Strip base_package prefix if present in source_subdirs
    # Example: base='services', subdirs='services/azure/auth' → 'services/azure/auth'
    if source_subdirs.startswith(f"{base_package}/"):
        source_subdirs = source_subdirs[len(base_package)+1:]  # Remove 'services/'

    # Combine
    if source_subdirs:
        return f"{base_package}/{source_subdirs}".replace('//', '/')
    else:
        return base_package
```

### Edge Case 3: __init__.py Files

**Scenario:** Multiple `__init__.py` files in different subdirectories

**Current Behavior:** All would collide as `__init__.py` in same directory

**Fixed Behavior:**
```
source/azure/__init__.py      → core/services/azure/__init__.py
source/azure/auth/__init__.py → core/services/azure/auth/__init__.py
source/m365/__init__.py       → core/services/m365/__init__.py
```

**Result:** No collision ✅

### Edge Case 4: Mixed Source Structures

**Scenario:** Source has both flat and nested files

```
source/
├── manager.py              ← Flat
├── azure/
│   └── auth.py             ← Nested
└── m365/
    └── search/
        └── client.py       ← Deep nested
```

**Handling:**
```
manager.py      → core/services/manager.py          (flat)
azure/auth.py   → core/services/azure/auth.py       (nested)
m365/search/client.py → core/services/m365/search/client.py (deep)
```

**Result:** Mixed depths preserved correctly ✅

## Verification Strategy

### 1. Unit Tests (New)

Create test file: `libraries/_ai_agent/tools/tests/test_adapt_subdirs.py`

```python
def test_merge_target_package_basic():
    """Test basic subdirectory merging."""
    classifier = FileClassifier(Path('.'))

    assert classifier._merge_target_package('services', 'azure/auth') == 'services/azure/auth'
    assert classifier._merge_target_package('schemas', 'models') == 'schemas/models'
    assert classifier._merge_target_package('api/routers', 'v1/azure') == 'api/routers/v1/azure'

def test_merge_target_package_empty_subdirs():
    """Test with no subdirectories."""
    classifier = FileClassifier(Path('.'))

    assert classifier._merge_target_package('services', '') == 'services'
    assert classifier._merge_target_package('services', '.') == 'services'

def test_merge_target_package_duplicate_prefix():
    """Test stripping duplicate prefix."""
    classifier = FileClassifier(Path('.'))

    # Should NOT create services/services/
    assert classifier._merge_target_package('services', 'services/azure') == 'services/azure'
    assert classifier._merge_target_package('api/routers', 'api/routers/v1') == 'api/routers/v1'

def test_source_subdirs_extraction():
    """Test subdirectory path extraction from source."""
    source_path = Path('/source')

    # Nested file
    file_path = Path('/source/azure/auth/manager.py')
    rel_path = file_path.relative_to(source_path)
    subdir = str(rel_path.parent)  # 'azure/auth'

    assert subdir == 'azure/auth'

    # Root file
    file_path = Path('/source/manager.py')
    rel_path = file_path.relative_to(source_path)
    subdir = str(rel_path.parent) if rel_path.parent != Path('.') else ''

    assert subdir == ''
```

### 2. Integration Test (Re-extract Microsoft Service)

**Prerequisite:** Backup current extracted microsoft service

```bash
cd C:/github_development/AustralisSystems
mv libraries/python/services/microsoft libraries/python/services/microsoft.backup
```

**Re-run Extraction:**
```bash
python libraries/_ai_agent/tools/extract_code.py \
  --analysis-report outputs/repo_analysis_digital_angels_20260113_010007.yaml \
  --candidate microsoft \
  --name microsoft \
  --extract-to libraries/python/services/extracted/

python libraries/_ai_agent/tools/adapt_extracted_code.py \
  --source libraries/python/services/extracted/microsoft \
  --target libraries/python/services/microsoft
```

**Expected Structure After Fix:**
```
libraries/python/services/microsoft/src/microsoft/
├── core/
│   ├── models/
│   ├── schemas/
│   └── services/
│       ├── ai_foundry/              ✅ Domain preserved!
│       │   ├── manager.py
│       │   ├── agent_provisioning.py
│       │   └── [24 more files]
│       ├── azure/                   ✅ Domain preserved!
│       │   ├── auth/                ✅ Feature subdirectory!
│       │   │   ├── manager.py
│       │   │   ├── factory.py
│       │   │   └── service.py
│       │   ├── provisioning/        ✅ Feature subdirectory!
│       │   └── [46 more files]
│       └── m365/                    ✅ Domain preserved!
│           ├── factories/
│           ├── onboarding/
│           ├── search/
│           └── user_services/
└── interface/
    ├── api/
    │   └── routers/
    │       ├── v1/                  ✅ API versioning preserved!
    │       │   ├── azure/
    │       │   └── m365/
    │       └── [19 files]
    └── cli/                         ✅ Should be empty or minimal!
        └── [only actual CLI handlers]
```

**Validation Commands:**
```bash
# Count files in each layer
find libraries/python/services/microsoft/src/microsoft/core/services -name "*.py" | wc -l
# Expected: ~156 (all service files from source/services/)

find libraries/python/services/microsoft/src/microsoft/interface/cli -name "*.py" | wc -l
# Expected: 0-5 (only true CLI handlers)

# Verify subdirectories preserved
ls libraries/python/services/microsoft/src/microsoft/core/services/
# Expected: ai_foundry/  azure/  m365/  (+ possibly root files)

ls libraries/python/services/microsoft/src/microsoft/core/services/azure/
# Expected: auth/  provisioning/  config/  key_vault/  (subdomain folders)

# Check no flattening occurred
find libraries/python/services/microsoft/src/microsoft/core/services -maxdepth 1 -name "*.py" | wc -l
# Expected: 0-10 (only root-level service files, not 156!)
```

### 3. Compare Before/After

**Before (Current Broken State):**
```
core/services/           ← 59 files FLATTENED
interface/cli/           ← 87 files (WRONG - mostly managers/factories)
interface/api/routers/   ← 19 files
```

**After (Fixed State):**
```
core/services/
  ├── ai_foundry/        ← ~26 files
  ├── azure/             ← ~48 files (+ subdirs)
  └── m365/              ← ~20 files (+ subdirs)
interface/cli/           ← 0-5 files (ONLY true CLI)
interface/api/routers/   ← 19 files (possibly with v1/ subdirs)
```

## Rollback Strategy

If extraction fails or produces incorrect structure:

```bash
# Restore backup
rm -rf libraries/python/services/microsoft
mv libraries/python/services/microsoft.backup libraries/python/services/microsoft

# Revert tool changes
git checkout libraries/_ai_agent/tools/adapt_extracted_code.py
```

## Success Criteria

✅ **Structure Preservation:** Source subdirectories fully preserved in tri-layer structure

✅ **No Flattening:** Files maintain domain organization (ai_foundry/, azure/, m365/)

✅ **Correct Defaults:** Unclassified files go to `core/services/`, NOT `interface/cli/`

✅ **No Collisions:** `__init__.py` and common filenames don't collide

✅ **Consistent Pattern:** All tri-layer components preserve subdirectories uniformly

✅ **Microsoft Service:** Re-extraction produces clean 3-domain structure in core/services/

## Implementation Order

1. **Add helper method**: `_merge_target_package()` with duplicate prefix handling
2. **Update classification dict**: Add `source_subdirs` field
3. **Apply merge pattern**: Update all 12 classification branches
4. **Strengthen CLI detection**: Require explicit CLI framework/patterns
5. **Test with unit tests**: Verify merge logic edge cases
6. **Re-extract microsoft**: Integration test with real service
7. **Validate structure**: Confirm 3-domain organization in core/services/
8. **Update other extracted services**: Re-run extraction for all 17 services if needed

## Notes

- **No changes to extract_code.py**: Extraction logic unchanged (still copies all files)
- **No changes to copy_mapped_files**: Existing path building logic works with merged package paths
- **No changes to SERVICE_MANIFEST**: Manifest generation unchanged
- **Protocol 205 compliant**: Maintains mandatory tri-layer foundation, extends with subdirs
- **Backward compatible**: Services without subdirectories work as before (flat structure)
