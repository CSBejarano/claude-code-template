# Hooks - Index

Quick index for Claude Code hooks system.

---

## 📖 **Documentation**

**Main Guide**: [HOOKS_GUIDE.md](HOOKS_GUIDE.md) - Complete hooks documentation

---

## ⚡ **Active Hooks (4)**

All hooks are PostToolUse (non-blocking):

1. **log-tool-usage.sh** - Logs all operations
   - **ROI**: Medium
   - **Log**: `.claude/logs/tool-usage.log`

2. **test-after-edit.sh** ⭐ - Auto-runs tests after edits
   - **ROI**: **VERY HIGH**
   - **Log**: `.claude/logs/test-results.log`
   - **Requires**: `pytest`

3. **auto-format.sh** - Auto-formats code
   - **ROI**: High
   - **Log**: `.claude/logs/format.log`
   - **Requires**: `black`/`prettier`

4. **doc-update-reminder.sh** - Documentation reminders
   - **ROI**: Medium
   - **Log**: `.claude/logs/doc-reminders.log`

---

## 🔧 **Quick Commands**

```bash
# View all logs
tail -f .claude/logs/*.log

# Test a hook manually
bash .claude/hooks/test-after-edit.sh

# Make hooks executable
chmod +x .claude/hooks/*.sh

# View configuration
cat .claude/settings.local.json
```

---

## 📁 **Files in This Directory**

```
.claude/hooks/
├── README.md                  # This file (index)
├── HOOKS_GUIDE.md             # Complete documentation
├── log-tool-usage.sh          # Hook 1: Operations logging
├── test-after-edit.sh         # Hook 2: Auto-testing
├── auto-format.sh             # Hook 3: Auto-formatting
└── doc-update-reminder.sh     # Hook 4: Doc reminders
```

---

## 🚀 **Getting Started**

1. **Read the guide**: [HOOKS_GUIDE.md](HOOKS_GUIDE.md)
2. **Check configuration**: `.claude/settings.local.json`
3. **View logs**: `.claude/logs/*.log`
4. **Test hooks**: `bash .claude/hooks/[hook-name].sh`

---

## ⚠️ **Troubleshooting**

See [HOOKS_GUIDE.md#troubleshooting](HOOKS_GUIDE.md#-troubleshooting) for common issues and solutions.

---

**Status**: ✅ 4 hooks active
**Total ROI**: HIGH
**Version**: 3.1.0
