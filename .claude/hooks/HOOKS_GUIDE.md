# Claude Code Hooks - Complete Guide

Comprehensive guide for all hooks in the Claude Code template system.

---

## 📚 **What Are Hooks?**

Hooks are shell commands that execute automatically in response to events during development. They enable:

- **Automated testing** after code changes
- **Auto-formatting** of code files
- **Documentation reminders** for significant changes
- **Operation logging** for audit trails

---

## ⚡ **Active Hooks (4)**

All hooks are **PostToolUse** (non-blocking, execute after Claude uses tools).

### **1. log-tool-usage.sh**

**When**: After every tool use
**Function**: Logs all Claude Code operations
**Log**: `.claude/logs/tool-usage.log`
**ROI**: Medium (useful for debugging and auditing)

```bash
# View today's activity
grep "$(date '+%Y-%m-%d')" .claude/logs/tool-usage.log

# Count operations
wc -l .claude/logs/tool-usage.log
```

---

### **2. test-after-edit.sh** ⭐ **CRITICAL**

**When**: After editing Python files
**Function**: Auto-runs pytest for edited files
**Log**: `.claude/logs/test-results.log`
**ROI**: **VERY HIGH** (immediate error detection)
**Requires**: `pytest` installed

**How it works**:

- Detects changes in `.py` files in `src/` or `tests/`
- Finds corresponding test file (`tests/unit/test_*.py`)
- Runs pytest in background (non-blocking)
- Logs results with timestamps

```bash
# Watch test results in real-time
tail -f .claude/logs/test-results.log

# See only failures
grep "FAILED" .claude/logs/test-results.log

# Install pytest if missing
pip install pytest
```

---

### **3. auto-format.sh**

**When**: After editing code files
**Function**: Auto-formats Python, JS/TS, Markdown
**Log**: `.claude/logs/format.log`
**ROI**: High (maintains code consistency)
**Requires**: `black`/`ruff` (Python), `prettier` (JS/MD)

**Supported formats**:

- **Python**: `black` (preferred) or `ruff format`
- **JS/TS**: `prettier` or `npx prettier`
- **Markdown**: `prettier` or `npx prettier`

```bash
# See what was formatted today
grep "$(date '+%Y-%m-%d')" .claude/logs/format.log

# Install formatters (optional)
pip install black              # Python
npm install -g prettier        # JS/TS/MD
```

---

### **4. doc-update-reminder.sh**

**When**: After significant changes (>50 lines or API changes)
**Function**: Reminds to update relevant documentation
**Log**: `.claude/logs/doc-reminders.log`
**ROI**: Medium (prevents doc drift)

**Smart file mapping**:

- `src/routes/*` → API docs
- `src/services/*` → Architecture docs
- `tests/*` → Testing docs
- `.claude/agents/*` → Agents docs

```bash
# See pending reminders
tail -20 .claude/logs/doc-reminders.log

# Search for specific file reminders
grep "src/routes" .claude/logs/doc-reminders.log
```

---

## 🔧 **Configuration**

### **settings.local.json**

All hooks configured in `.claude/settings.local.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/log-tool-usage.sh"
          },
          {
            "type": "command",
            "command": "bash .claude/hooks/test-after-edit.sh"
          },
          {
            "type": "command",
            "command": "bash .claude/hooks/auto-format.sh"
          },
          {
            "type": "command",
            "command": "bash .claude/hooks/doc-update-reminder.sh"
          }
        ]
      }
    ]
  }
}
```

### **Disable Hooks**

Comment specific hooks to disable:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/log-tool-usage.sh"
          },
          // {
          //   "type": "command",
          //   "command": "bash .claude/hooks/test-after-edit.sh"
          // },
          {
            "type": "command",
            "command": "bash .claude/hooks/auto-format.sh"
          }
        ]
      }
    ]
  }
}
```

---

## 📊 **Logs and Monitoring**

### **Log Structure**

```
.claude/logs/
├── tool-usage.log       # Audit log (all operations)
├── test-results.log     # Test execution results
├── format.log           # Auto-formatting operations
└── doc-reminders.log    # Documentation reminders
```

### **Useful Commands**

```bash
# Watch all logs simultaneously
tail -f .claude/logs/*.log

# View all logs directory
ls -lh .claude/logs/

# Clear old logs (if needed)
rm .claude/logs/*.log && touch .claude/logs/{tool-usage,test-results,format,doc-reminders}.log

# View today's activity across all logs
grep "$(date '+%Y-%m-%d')" .claude/logs/*.log
```

---

## 🔍 **Troubleshooting**

### **Tests not running?**

1. Check pytest is installed:
   ```bash
   pytest --version
   ```
2. Check test files exist:
   ```bash
   ls tests/unit/test_*.py
   ```
3. Check log for errors:
   ```bash
   cat .claude/logs/test-results.log
   ```

### **Formatting not working?**

1. Check formatters installed:
   ```bash
   black --version
   prettier --version
   ```
2. Check log for warnings:
   ```bash
   grep "⚠️" .claude/logs/format.log
   ```
3. Install missing tools (see hook #3 above)

### **Reminders not appearing?**

1. Changes must be >50 lines or contain API changes
2. Check if in git repo:
   ```bash
   git status
   ```
3. Check log:
   ```bash
   cat .claude/logs/doc-reminders.log
   ```

### **Hooks not executing?**

1. Verify hooks are executable:
   ```bash
   ls -l .claude/hooks/*.sh
   ```
2. Make executable if needed:
   ```bash
   chmod +x .claude/hooks/*.sh
   ```
3. Check settings.local.json syntax is valid
4. Restart Claude Code

---

## ⚠️ **Best Practices**

### **1. Keep Hooks Fast**

- Avoid slow operations that block workflow
- Use background processing when possible
- All hooks should return in <1 second

### **2. Error Handling**

All hooks implement graceful degradation:

```bash
#!/bin/bash
set +e  # Don't fail on errors

# Your logic here

exit 0  # Always return success (non-blocking)
```

### **3. Logging**

All hooks log to centralized location:

```bash
LOG_FILE=".claude/logs/[hook-name].log"
echo "[$(date)] Hook executed" >> $LOG_FILE
```

### **4. Testing**

Test hooks manually before activating:

```bash
bash .claude/hooks/test-after-edit.sh
echo $?  # Should return 0
```

---

## ✅ **Validation Status**

### **Implementation Quality**

- ✅ All 4 hooks implemented and tested
- ✅ Non-blocking execution (returns immediately)
- ✅ Graceful error handling (no failures)
- ✅ Centralized logging with timestamps
- ✅ Comprehensive documentation

### **Performance**

- **log-tool-usage.sh**: ~0.005s (instant)
- **test-after-edit.sh**: ~0.050s (background)
- **auto-format.sh**: ~0.200s (npx overhead)
- **doc-update-reminder.sh**: ~0.030s (fast)
- **Total overhead**: ~0.3s per edit (acceptable)

### **Test Results**

All hooks tested manually and in integration:

- ✅ Individual execution: PASS
- ✅ Integration (all together): PASS
- ✅ Error handling: PASS
- ✅ Log file creation: PASS
- ✅ Non-blocking behavior: PASS

---

## 📚 **Available Hook Types**

### **Currently Active**

- **PostToolUse**: After Claude uses any tool (4 active hooks)

### **Available but Not Active**

- **PreToolUse**: Before Claude uses a tool (validation, backups)
- **UserPromptSubmit**: When user sends a message (logging, context updates)
- **SessionStart**: When Claude Code session starts (setup)
- **SessionEnd**: When Claude Code session ends (cleanup)

To activate additional hooks, create scripts in `.claude/hooks/` and update `settings.local.json`.

---

## 🎯 **Common Use Cases**

### **Auto-Test Before Critical Operations**

```json
{
  "PreToolUse": {
    "enabled": true,
    "command": "npm test",
    "blocking": true
  }
}
```

### **Backup Before Destructive Operations**

```json
{
  "PreToolUse": {
    "enabled": true,
    "command": ".claude/hooks/backup.sh",
    "blocking": true
  }
}
```

### **Auto-Commit After Changes** (use with caution)

```json
{
  "PostToolUse": {
    "enabled": true,
    "command": "git add -A && git commit -m 'Auto-commit by Claude'",
    "blocking": false
  }
}
```

---

## 🔗 **Additional Resources**

- **Quick Reference**: Use this guide for quick lookups
- **Hook Scripts**: Located in `.claude/hooks/*.sh`
- **Settings**: `.claude/settings.local.json`
- **Claude Code Docs**: [https://docs.claude.com](https://docs.claude.com)

---

**Status**: ✅ Production Ready
**Hooks Active**: 4
**Total ROI**: HIGH (automation + consistency + quality)
**Last Updated**: 2025-10-07
**Template Version**: 3.1.0

---

_For detailed validation report, see [VALIDATION_M2_IMPROVED.md](../VALIDATION_M2_IMPROVED.md)_
