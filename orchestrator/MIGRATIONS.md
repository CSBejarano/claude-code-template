# Migration Guides - Orchestrator Agent SDK

This document provides step-by-step migration guides for major version upgrades of the Orchestrator Agent SDK.

---

## Table of Contents

- [Migrating from 0.x to 1.0.0](#migrating-from-0x-to-100)
- [Future Migrations](#future-migrations)
- [Getting Help](#getting-help)

---

## Migrating from 0.x to 1.0.0

**N/A** - Version 1.0.0 is the initial stable release.

There is no migration required as there were no public pre-1.0.0 versions.

---

## Future Migrations

Migration guides will be added here when major version bumps occur.

### Template for Future Migrations

When a new major version is released, this section will include:

#### Example: Migrating from 1.x to 2.0.0

**Overview:**
- Brief description of what changed
- Why the breaking change was necessary
- Timeline (deprecation warnings, removal date)

**Breaking Changes:**

1. **Change Description**
   - **What changed**: Detailed explanation
   - **Why**: Rationale for the change
   - **Impact**: Who is affected

**Migration Steps:**

**Step 1: Update Dependencies**
```bash
# Update to new version
pip install orchestrator-agent-sdk==2.0.0
```

**Step 2: Update Code**

**Before (v1.x):**
```python
# Old code example
from orchestrator import OrchestratorAgent

orchestrator = OrchestratorAgent()
result = await orchestrator.old_method(data)
```

**After (v2.0.0):**
```python
# New code example
from orchestrator import OrchestratorAgent

orchestrator = OrchestratorAgent()
result = await orchestrator.new_method(data)  # New API
```

**Step 3: Update Pydantic Models** (if applicable)

**Before (v1.x):**
```python
class MyModel(BaseModel):
    field1: str
    # old_field was required
```

**After (v2.0.0):**
```python
class MyModel(BaseModel):
    field1: str
    new_field: str  # New required field
    # old_field removed
```

**Step 4: Test Your Changes**
```bash
# Run your test suite
pytest tests/

# Verify functionality
python your_script.py
```

**Common Migration Issues:**

**Issue 1: Method Not Found**
- **Symptom**: `AttributeError: 'OrchestratorAgent' object has no attribute 'old_method'`
- **Solution**: Replace `old_method()` with `new_method()`

**Issue 2: Model Validation Error**
- **Symptom**: `ValidationError: field required`
- **Solution**: Add required new fields to your model instances

---

## Deprecation Timeline

When features are deprecated, they will be listed here with removal timelines:

| Feature | Deprecated In | Removed In | Alternative | Notes |
|---------|---------------|------------|-------------|-------|
| (none yet) | - | - | - | - |

**Example entry:**
| `old_method()` | v1.5.0 | v2.0.0 | `new_method()` | Use new_method() for better performance |

---

## Versioning Strategy

### Backwards Compatibility

We strive to maintain backwards compatibility whenever possible:

- **MINOR versions** (1.X.0) are always backwards compatible
- **PATCH versions** (1.0.X) are always backwards compatible
- **MAJOR versions** (X.0.0) may introduce breaking changes

### Deprecation Process

1. **Announcement** (MINOR version):
   - Feature marked as deprecated
   - Warning added via `warnings.warn()`
   - Alternative documented
   - Timeline announced

2. **Grace Period**:
   - Minimum: 1 MINOR version + 30 days
   - Deprecation warnings in every release note
   - Migration guide provided

3. **Removal** (MAJOR version):
   - Feature removed
   - Migration guide enforced
   - Release notes highlight removal

---

## Getting Help

If you encounter issues during migration:

1. **Check CHANGELOG.md** for detailed release notes
2. **Review this migration guide** for specific version upgrades
3. **Check examples/** folder for updated code examples
4. **Open an issue** on GitHub with:
   - Your current version
   - Target version
   - Error message or unexpected behavior
   - Minimal reproducible example

---

## Best Practices for Smooth Migrations

1. **Pin Your Version**:
   ```
   # requirements.txt
   orchestrator-agent-sdk==1.0.0  # Exact version
   ```

2. **Test Before Upgrading**:
   ```bash
   # Create test environment
   python -m venv test_env
   source test_env/bin/activate
   pip install orchestrator-agent-sdk==2.0.0
   pytest tests/
   ```

3. **Read Release Notes**:
   - Always review CHANGELOG.md before upgrading
   - Pay attention to "Breaking Changes" section

4. **Upgrade Incrementally**:
   - Don't skip major versions
   - Migrate 1.x → 2.0 → 3.0, not 1.x → 3.0

5. **Monitor Deprecation Warnings**:
   ```python
   import warnings
   warnings.filterwarnings('default', category=DeprecationWarning)
   ```

---

## Version-Specific Notes

### Version 1.0.0
- **Release Date**: 2025-01-03
- **Status**: Current stable release
- **Python**: Requires Python 3.10+
- **Dependencies**: See requirements.txt
- **Breaking Changes**: None (initial release)

---

*For complete changelog, see [CHANGELOG.md](./CHANGELOG.md)*

*For SDK documentation, see [README.md](./README.md)*

*Last updated: 2025-01-03*
