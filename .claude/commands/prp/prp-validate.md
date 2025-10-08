---
description: "Validate a PRP without executing it using @prp-validator"
---

# Validate PRP (No Execution)

## File: $ARGUMENTOS

## Purpose

Validate PRP quality and auto-improve it WITHOUT executing. Use this to:

- Check PRP quality before committing to execution
- Fix common PRP issues automatically
- Understand what needs improvement before running

---

## 🔍 Validation Process

### 1. Invoke @prp-validator

You will call @prp-validator agent with the specified PRP file path.

### 2. @prp-validator Actions

The validator will:

1. **Read PRP** from specified path
2. **Score PRP** using Pareto 80-20 criteria (0-100 points)
3. **Identify Issues** if score < 80/100
4. **Auto-Improve** PRP (max 3 iterations):
   - Add missing "Current vs Desired Structure" section
   - Enhance references (mix external + internal)
   - Clarify vague business logic
   - Make steps actionable with file paths
5. **Create Backup** at `PRPs/[filename].md.backup-[timestamp]`
6. **Generate Report** with score, issues, fixes applied

### 3. Validation Criteria (Pareto 80-20)

**TIER 1 - CRITICAL (80 points total)**:

- Current vs Desired Structure section (20 pts)
- Mixed references (external + internal) (20 pts)
- Specific business logic (no vague terms) (20 pts)
- Actionable steps with file paths (20 pts)

**TIER 2 - HIGH (20 points total)**:

- Validation gates mentioned (10 pts)
- Clear constraints/gotchas (10 pts)

**Passing Score**: 80/100

---

## 📊 Expected Outputs

### Success Case (Score ≥ 80/100)

```
🔍 Validating PRP: PRPs/feature.md...
📊 Initial Score: 65/100
⚠️ Issues found: [3]

🔧 Auto-improving (Iteration 1/3)...
  ✅ Added Current vs Desired Structure
  ✅ Enhanced References
  ✅ Clarified business logic

📊 New Score: 90/100 ✅
✅ VALIDATION PASSED

📄 Report saved to: PRPs/validation_reports/feature_2025-01-06.md
🔙 Backup saved to: PRPs/feature.md.backup-2025-01-06T10-30-45
```

### Needs Manual Review (Score < 80 after 3 iterations)

```
📊 Final Score: 72/100 ❌
⚠️ VALIDATION FAILED - Manual review required

Unfixed Issues:
1. Business logic still too vague
2. Missing specific file paths

💬 Please:
1. Review improved PRP at PRPs/feature.md
2. Address unfixed issues manually
3. Re-run /prp-validate
```

---

## 🛠️ Usage Examples

```bash
# Validate a story PRP
/prp-validate PRPs/story_auth_feature.md

# Validate a technical PRP
/prp-validate PRPs/technical_api_refactor.md

# After validation, execute if passing
/prp-execute PRPs/story_auth_feature.md
```

---

## 📚 See Also

- `.claude/agents/prp-validator.md` - Full validator documentation
- `/prp-execute` - Execute validated PRP
- `.claude/docs/CHECKPOINTS.md` - Why validation matters (ROI 100x)
