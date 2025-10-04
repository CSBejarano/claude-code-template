# 🔧 Troubleshooting Guide - Claude Code Template

> **Complete troubleshooting guide** for the hybrid AI project generation system (@project-initializer + Orchestrator SDK)

**Quick Links:** [🚀 Quick Start](../QUICK_START.md) | [📖 User Guide](USER_GUIDE.md) | [✨ Best Practices](BEST_PRACTICES.md)

---

## 📋 Table of Contents

### Quick Navigation
- [🚨 Quick Diagnostic Flowchart](#-quick-diagnostic-flowchart)
- [🔧 Debugging Toolbox](#-debugging-toolbox)
- [🆘 Getting Help](#-getting-help)

### Error Categories
1. [Installation & Setup Errors](#1-installation--setup-errors)
2. [Template Initialization Errors](#2-template-initialization-errors)
3. [Checkpoint Issues](#3-checkpoint-issues)
4. [TDD Loop Errors](#4-tdd-loop-errors)
5. [Memory System Errors](#5-memory-system-errors)
6. [Integration & Performance Issues](#6-integration--performance-issues)
7. [Generated Project Issues](#7-generated-project-issues)

### Additional Resources
- [💡 FAQ](#-faq)
- [🚑 Emergency Recovery](#-emergency-recovery)

---

## 🚨 Quick Diagnostic Flowchart

**What type of problem are you experiencing?**

```
❌ Can't start the template at all?
   └─→ Go to: Installation & Setup Errors

❌ @project-initializer not found or crashes?
   └─→ Go to: Template Initialization Errors

❌ Agent stuck waiting for response?
   └─→ Go to: Checkpoint Issues

❌ Tests failing in TDD loop?
   └─→ Go to: TDD Loop Errors

❌ Memory errors or pattern retrieval fails?
   └─→ Go to: Memory System Errors

❌ Agents timeout or slow performance?
   └─→ Go to: Integration & Performance Issues

❌ Generated project incomplete or broken?
   └─→ Go to: Generated Project Issues
```

---

## 1. Installation & Setup Errors

### Error 1.1: "ModuleNotFoundError: No module named 'orchestrator'"

**🔴 CRITICAL - Most Common Error**

**Síntoma:**
```bash
$ python example_orchestrator_usage.py
Traceback (most recent call last):
  File "example_orchestrator_usage.py", line 1, in <module>
    from orchestrator import OrchestratorAgent
ModuleNotFoundError: No module named 'orchestrator'
```

**Causa:**
Dependencies no instaladas después de clonar el repositorio.

**Solución:**
```bash
# 1. Verify you're in the template directory
pwd
# Should show: /path/to/claude-code-template

# 2. Install dependencies
pip install -r requirements.txt

# 3. Verify installation
python -c "import orchestrator; print(orchestrator.__version__)"
# Should output: 1.0.0

# 4. Test orchestrator
python example_orchestrator_usage.py
```

**Prevención:**
- Always run `pip install -r requirements.txt` after cloning
- Add to your setup checklist
- Consider using virtual environment to isolate dependencies

---

### Error 1.2: "ANTHROPIC_API_KEY not set"

**🔴 CRITICAL - Blocks All Operations**

**Síntoma:**
```bash
$ @project-initializer
Error: ANTHROPIC_API_KEY environment variable not set
Claude API authentication failed
```

**Causa:**
API key no configurada en variables de entorno.

**Solución:**
```bash
# Option A: Set for current session
export ANTHROPIC_API_KEY="sk-ant-api03-..."

# Option B: Set permanently (recommended)
# For bash
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-..."' >> ~/.bashrc
source ~/.bashrc

# For zsh
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-..."' >> ~/.zshrc
source ~/.zshrc

# Verify it's set
echo $ANTHROPIC_API_KEY
# Should output: sk-ant-api03-...

# Test with orchestrator
python example_orchestrator_usage.py
```

**Get API Key:**
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Navigate to API Keys
3. Create new key
4. Copy the key (starts with `sk-ant-api03-`)

**Prevención:**
- Set API key BEFORE starting any work
- Use `.env` file for project-specific keys
- Never commit API keys to git (add `.env` to `.gitignore`)

---

### Error 1.3: "Python version 3.9 not supported"

**Síntoma:**
```bash
$ pip install -r requirements.txt
ERROR: Package 'orchestrator' requires Python >=3.10
You are using Python 3.9.7
```

**Causa:**
Template requires Python 3.10+ for Pydantic v2 features.

**Solución:**
```bash
# 1. Check current version
python --version
# Output: Python 3.9.7

# 2. Install Python 3.10+ (macOS with Homebrew)
brew install python@3.10

# 3. Use specific version
python3.10 -m pip install -r requirements.txt

# 4. Create alias (optional)
alias python=python3.10
alias pip=python3.10 -m pip

# 5. Verify
python --version
# Output: Python 3.10.x
```

**Prevención:**
- Always check prerequisites before installation
- Use `pyenv` for managing multiple Python versions
- Document Python version in project README

---

### Error 1.4: "Pydantic v2 validation error at import"

**Síntoma:**
```python
from orchestrator.models import AutomationIntent
ImportError: cannot import name 'BaseModel' from 'pydantic'
# or
ValidationError: Field required [type=missing]
```

**Causa:**
Pydantic v1 installed instead of v2, or version conflict.

**Solución:**
```bash
# 1. Check Pydantic version
pip show pydantic
# Should show: Version: 2.x.x

# 2. If v1, upgrade to v2
pip install --upgrade 'pydantic>=2.0.0'

# 3. Reinstall orchestrator dependencies
pip install -r requirements.txt --force-reinstall

# 4. Verify
python -c "from pydantic import BaseModel; print(BaseModel.model_config)"
```

**Prevención:**
- Pin Pydantic version in `requirements.txt`: `pydantic>=2.0.0,<3.0.0`
- Use virtual environments to avoid conflicts
- Check `pip list` for conflicting packages

---

### Error 1.5: "MCP tools not available in Claude Code"

**Síntoma:**
```bash
$ @project-initializer
Error: sequential-thinking tool not found
MCP server 'server-sequential-thinking' not configured
```

**Causa:**
MCP tools no configurados en Claude Code settings.

**Solución:**
```bash
# 1. Verify MCP tools list in Claude Code
# Run in Claude Code:
# "List available MCP tools"

# 2. If sequential-thinking missing, configure MCP servers
# Edit Claude Code settings.json:
{
  "mcpServers": {
    "server-sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/sequential-thinking"]
    }
  }
}

# 3. Restart Claude Code

# 4. Verify tools available
# "Show MCP tools"
```

**Prevención:**
- Configure MCP tools during initial setup
- Keep MCP server versions updated
- Test MCP availability before starting projects

---

## 2. Template Initialization Errors

### Error 2.1: "@project-initializer agent not found"

**🔴 HIGH PRIORITY**

**Síntoma:**
```bash
$ @project-initializer
Error: Agent '@project-initializer' not found
Available agents: @codebase-analyst, @library-researcher
```

**Causa:**
Agent file missing or not registered in Claude Code configuration.

**Solución:**
```bash
# 1. Verify agent file exists
ls -la .claude/agents/project-initializer.md
# Should exist

# 2. If missing, restore from template
# The file should be in your claude-code-template repository
cp .claude/agents/project-initializer.md /path/to/your/project/.claude/agents/

# 3. Verify Claude Code recognizes the agent
# In Claude Code, run:
# "@project-initializer"
# Should start the initialization process

# 4. If still not found, check Claude Code configuration
cat ~/.config/claude-code/settings.json | grep agents
```

**Prevención:**
- Always clone the complete repository including `.claude/agents/`
- Don't delete `.claude/` directory
- Verify directory structure after cloning

---

### Error 2.2: "orchestrator.initialize() failed"

**Síntoma:**
```python
Phase 0: Initialize Orchestrator
Error: Failed to initialize orchestrator
FileNotFoundError: .claude/memories/ not found
```

**Causa:**
Memory directory missing or incorrect permissions.

**Solución:**
```bash
# 1. Create memory directory
mkdir -p .claude/memories/

# 2. Set proper permissions
chmod 755 .claude/
chmod 755 .claude/memories/

# 3. Initialize with empty memories
touch .claude/memories/architectural_decisions.json
touch .claude/memories/patterns.json
touch .claude/memories/learnings.json
touch .claude/memories/api_integrations.json

# 4. Add initial content to each file
echo '[]' > .claude/memories/architectural_decisions.json
echo '[]' > .claude/memories/patterns.json
echo '[]' > .claude/memories/learnings.json
echo '{}' > .claude/memories/api_integrations.json

# 5. Verify
ls -la .claude/memories/
# Should show 4 JSON files
```

**Prevención:**
- Run initialization script if provided
- Don't manually delete `.claude/memories/`
- Backup memories before major changes

---

### Error 2.3: "Jinja2 template rendering failed"

**Síntoma:**
```
Phase 8: TDD Implementation
Error: Template rendering failed
jinja2.exceptions.UndefinedError: 'project_name' is undefined
```

**Causa:**
`orchestrator.analyze_intent()` no retornó todos los campos requeridos por templates.

**Solución:**
```bash
# 1. Check what was analyzed
# In the agent output, look for:
# "Intent Analysis Result:"
# Verify all required fields are present:
# - project_name
# - project_type
# - complexity
# - apis_required
# - tech_stack

# 2. If fields missing, restart from Phase 1 with clearer description
# Instead of: "automate emails"
# Use: "Create a Python project to sync Gmail emails to Notion database using Gmail API and Notion API"

# 3. If fields present but rendering fails, check template syntax
cat .claude/templates/base/README.md.j2 | grep project_name
# Verify Jinja2 syntax: {{ project_name }} not ${project_name}

# 4. For debugging, enable verbose mode
ORCHESTRATOR_DEBUG=true @project-initializer
```

**Prevención:**
- Provide detailed, specific project descriptions
- Include technology preferences (Python, Node.js, etc.)
- Mention all APIs/integrations needed
- Review CHECKPOINT 1 summary carefully

---

### Error 2.4: "Variable 'orchestrator_version' not found in template context"

**Síntoma:**
```
Rendering template: orchestrator/__init__.py.j2
KeyError: 'orchestrator_version'
```

**Causa:**
Template expects variable que no está en el context dict.

**Solución:**
```bash
# This is likely a bug in template or orchestrator code
# Check which variables are available:

# 1. Review the available variables in TEMPLATES.md
cat .claude/TEMPLATES.md | grep "Available Variables"

# 2. If variable should exist but doesn't, check orchestrator code
# File: orchestrator/project_generator.py
# Look for: def _get_template_context()

# 3. Temporary workaround: Add variable to context manually
# Edit orchestrator/project_generator.py:
def _get_template_context(self, intent):
    context = {
        "project_name": intent.project_name,
        "orchestrator_version": "1.0.0",  # Add this line
        # ... other variables
    }
    return context

# 4. Report this as a bug with template name and missing variable
```

**Prevención:**
- Use templates from tested versions only
- Check CHANGELOG.md for template changes
- Report template bugs to help improve system

---

### Error 2.5: "Complexity level mismatch - expected MEDIUM, got SIMPLE"

**Síntoma:**
```
CHECKPOINT 1 shows:
Complexity: SIMPLE

But you wanted MEDIUM complexity with orchestrator/ folder.
```

**Causa:**
Intent analyzer classified project as SIMPLE based on description.

**Solución:**
```bash
# At CHECKPOINT 1, use "fix:" response:

# User response at CHECKPOINT 1:
fix: Change complexity to MEDIUM - I need orchestrator capabilities and @self-improve agent

# The agent will:
# 1. Re-analyze with medium complexity forced
# 2. Re-run research phase
# 3. Present new CHECKPOINT 1 with MEDIUM complexity

# Verify in new CHECKPOINT 1:
# - Complexity: MEDIUM ✓
# - Will include orchestrator/ folder ✓
# - Will include @self-improve agent ✓
```

**Prevención:**
- Mention "orchestrator" or "self-improvement" in initial goal if you want MEDIUM
- Review complexity in CHECKPOINT 1 BEFORE approving
- Understand complexity levels:
  - SIMPLE: Basic projects, no orchestrator
  - MEDIUM: Needs orchestrator + @self-improve
  - HIGH: Complex multi-API projects with advanced orchestration

---

## 3. Checkpoint Issues

### Error 3.1: "Agent stuck at CHECKPOINT 1 - no response detected"

**🔴 CRITICAL - Workflow Blocker**

**Síntoma:**
```
CHECKPOINT 1: Research Validation

⏸️  YOUR RESPONSE REQUIRED:
✅ "approve"                    → Proceed to Planning Phase
🔄 "fix: [description]"        → Make corrections to research
❌ "restart"                    → Research fundamentally wrong

[Agent waiting indefinitely, no progress]
```

**Causa:**
Usuario no respondió con uno de los comandos exactos esperados.

**Solución:**
```bash
# WRONG responses (don't work):
# "yes" ❌
# "looks good" ❌
# "ok" ❌
# "approve it" ❌
# "APPROVE" ❌ (case sensitive!)

# CORRECT responses:
"approve"                           # ✅ Exact match
"fix: Add Slack API for notifications"  # ✅ With description
"restart"                          # ✅ Exact match

# If stuck:
# 1. Type EXACTLY one of the three commands
# 2. No extra words, punctuation, or capitalization
# 3. For "fix:", always include description after colon

# Example fix responses:
"fix: Change complexity to SIMPLE"
"fix: Also need Gmail API, not just Notion"
"fix: Project name should be 'email-to-notion' not 'gmail-notion'"
```

**Prevención:**
- Read checkpoint instructions carefully
- Copy-paste exact commands if unsure
- Don't add extra text before/after command
- Use lowercase for "approve" and "restart"

---

### Error 3.2: "Invalid checkpoint response format"

**Síntoma:**
```
Your response: "fix Add more APIs"
Error: Invalid format. Use "fix: [description]" with colon.
```

**Causa:**
Missing colon after "fix" or incorrect syntax.

**Solución:**
```bash
# WRONG:
"fix Add Slack API" ❌
"Fix: Add Slack API" ❌ (capital F)
"fix:" ❌ (no description)
"fix : Add Slack API" ❌ (space before colon)

# CORRECT:
"fix: Add Slack API" ✅

# Format is:
fix: [space] [description]
^   ^         ^
|   |         └─ Description (1+ words)
|   └─────────── Space after colon
└───────────────── Lowercase "fix"

# For restart:
"restart" ✅ (no colon, no description)

# For approve:
"approve" ✅ (no colon, no description)
```

**Prevención:**
- Always include colon AND space for "fix:"
- Always include description after "fix:"
- Don't capitalize commands
- Test with simple "approve" first if unsure

---

### Error 3.3: "Cannot go back from CHECKPOINT 2 to CHECKPOINT 1"

**Síntoma:**
```
At CHECKPOINT 2, you responded:
"back to checkpoint 1"

Error: Invalid response. Use "back to research" to return to Phase 2.
```

**Causa:**
Incorrect command - cada checkpoint tiene diferentes opciones de retroceso.

**Solución:**
```bash
# CHECKPOINT 1 responses:
✅ "approve"          → Continue to Planning
🔄 "fix: [desc]"      → Fix research, stay in CP1
❌ "restart"          → Back to Phase 1 (Goal)

# CHECKPOINT 2 responses:
✅ "approve"          → Continue to Implementation
🔄 "fix: [desc]"      → Fix planning, stay in CP2
⬅️ "back to research" → Back to Phase 2 (Research)

# Note: From CP2 you cannot go directly to CP1
# You can only go "back to research" which returns to Phase 2
# Then the flow will naturally reach CP1 again

# If you need fundamental changes:
# At CP2: "back to research"
# Then at CP1 (when reached again): "restart" or "fix:"
```

**Prevención:**
- Understand checkpoint flow (see USER_GUIDE.md diagrams)
- Read available options carefully at each checkpoint
- Use "back to research" from CP2, not "restart"
- Plan corrections early (at CP1) to avoid backtracking

---

### Error 3.4: "Checkpoint state not saved - lost progress"

**Síntoma:**
```
After "approve" at CHECKPOINT 1, agent restarted
Now back at Phase 0, lost all research
```

**Causa:**
Claude Code session interrupted or memory not persisted.

**Solución:**
```bash
# 1. Check if memories were saved
ls -la .claude/memories/
cat .claude/memories/architectural_decisions.json

# 2. If memories exist, agent should recover
# In Claude Code, say:
"Resume from last checkpoint - I had approved research for [project-name]"

# 3. If memories empty, research is lost
# You'll need to restart, but it's faster the second time
# The agent learns from the interruption

# 4. To prevent data loss mid-checkpoint:
# Don't close Claude Code during checkpoint validation
# Don't interrupt during "Processing..." states
# Wait for explicit "CHECKPOINT X" prompt before pausing
```

**Prevención:**
- Complete checkpoint cycle before closing Claude Code
- Use "pause" instead of closing if you need break
- Memories auto-save after each phase completion
- Don't kill process during "Saving to memory..." messages

---

## 4. TDD Loop Errors

### Error 4.1: "Tests fail with 'No module named pytest'"

**🔴 HIGH PRIORITY**

**Síntoma:**
```bash
Phase 8: TDD Implementation
🔴 STEP 1: Failing Test

$ pytest tests/test_gmail_client.py
bash: pytest: command not found
```

**Causa:**
Dependencies no instaladas en el proyecto GENERADO (diferente del template).

**Solución:**
```bash
# Important: You need to install deps in GENERATED project, not template!

# 1. Navigate to generated project
cd /path/to/gmail-to-notion-sync/  # Your project name

# 2. Verify you're in the right place
ls -la
# Should show: src/, tests/, requirements.txt, README.md

# 3. Install project dependencies
pip install -r requirements.txt

# 4. Verify pytest installed
pytest --version
# Output: pytest 7.x.x

# 5. Run tests
pytest tests/ -v

# 6. If still fails, install explicitly
pip install pytest pytest-cov
```

**Prevención:**
- Always `cd` into generated project first
- Run `pip install -r requirements.txt` immediately
- Use virtual environment per project: `python -m venv venv`
- Document setup steps in generated project README

---

### Error 4.2: "Test fixtures missing - ImportError"

**Síntoma:**
```python
tests/test_gmail_client.py:5: in <module>
    from tests.fixtures import mock_gmail_service
ImportError: cannot import name 'mock_gmail_service' from 'tests.fixtures'
```

**Causa:**
TDD implementation no generó archivo fixtures.py aún, o test importa fixture inexistente.

**Solución:**
```bash
# 1. Check what's in tests directory
ls -la tests/
# Expected: test_*.py files, may also have fixtures.py or conftest.py

# 2. If fixtures.py missing, create it
# tests/fixtures.py
cat > tests/fixtures.py << 'EOF'
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_gmail_service():
    """Mock Gmail API service for testing."""
    service = MagicMock()
    service.users().messages().list().execute.return_value = {
        'messages': [{'id': '123', 'threadId': '456'}]
    }
    return service
EOF

# 3. Or use conftest.py (pytest convention)
# tests/conftest.py contains fixtures automatically discovered

# 4. Re-run tests
pytest tests/ -v
```

**Prevención:**
- TDD Step 1 should show test code before running
- Verify all imports exist before running test
- Ask agent: "Show me the fixture code needed" if unclear
- Use `conftest.py` for shared fixtures across tests

---

### Error 4.3: "TDD stuck at Step 2 - credentials setup"

**Síntoma:**
```
🔴 STEP 1: Failing Test
[test fails]

📋 STEP 2: Setup Guidance
To proceed, you need:
1. Go to console.cloud.google.com
2. Create OAuth credentials
3. Download credentials.json

Ready to continue? (yes/no)

[You responded "yes" but don't actually have credentials]

⚙️ STEP 3: Implementation
[code created]

✅ STEP 4: Test Passes
FAILED - Authentication failed: credentials.json not found
```

**Causa:**
Usuario respondió "yes" sin realmente completar el setup de credenciales.

**Solución:**
```bash
# Be honest about setup status!

# If you DON'T have credentials yet:
# At Step 2, respond: "no"

# The agent should:
# 1. Provide detailed setup instructions
# 2. Wait for you to complete setup
# 3. Ask again: "Ready now? (yes/no)"

# Complete the actual setup:
# 1. Go to console.cloud.google.com
# 2. Create project
# 3. Enable Gmail API
# 4. Create OAuth 2.0 credentials
# 5. Download credentials.json
# 6. Place in project root
# 7. NOW respond "yes"

# If you want to skip API setup for now:
# At Step 2, respond: "skip - use mock data"
# Agent should create test with mocked API instead
```

**Prevención:**
- Don't say "yes" unless setup is ACTUALLY complete
- Use "no" to get more detailed instructions
- Use "skip - use mocks" if you want to defer API setup
- Keep credentials.json in `.gitignore`

---

### Error 4.4: "Coverage shows 0% despite tests passing"

**Síntoma:**
```bash
$ pytest tests/ --cov=src --cov-report=term-missing
tests/test_gmail_client.py::test_oauth_flow PASSED

---------- coverage: platform darwin, python 3.10.9 -----------
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
src/gmail_client.py      45     45     0%   1-67
---------------------------------------------------
TOTAL                    45     45     0%
```

**Causa:**
`pytest-cov` configurado incorrectamente o importando módulo incorrecto.

**Solución:**
```bash
# 1. Verify project structure
ls -la
# Should show both src/ and tests/ at same level

# 2. Check test imports
cat tests/test_gmail_client.py | grep "import"
# Should be: from src.gmail_client import GmailClient
# NOT: from gmail_client import GmailClient

# 3. Fix import paths in tests if wrong
# Change:
from gmail_client import GmailClient  # ❌
# To:
from src.gmail_client import GmailClient  # ✅

# 4. Run coverage with correct source
pytest tests/ --cov=src --cov-report=term-missing

# 5. For detailed report
pytest tests/ --cov=src --cov-report=html
# Open htmlcov/index.html in browser
```

**Prevención:**
- Use consistent import paths (`from src.module import ...`)
- Set up `pytest.ini` with coverage settings
- Verify coverage after EACH test passes
- Target 100% coverage in TDD approach

---

## 5. Memory System Errors

### Error 5.1: "MemoryManager: FileNotFoundError"

**Síntoma:**
```python
orchestrator.get_memory_context(project_type="api_integration")
FileNotFoundError: [Errno 2] No such file or directory: '.claude/memories/patterns.json'
```

**Causa:**
Memory files no inicializados o borrados accidentalmente.

**Solución:**
```bash
# 1. Create memories directory if missing
mkdir -p .claude/memories/

# 2. Initialize all memory files
cat > .claude/memories/architectural_decisions.json << 'EOF'
[]
EOF

cat > .claude/memories/patterns.json << 'EOF'
[]
EOF

cat > .claude/memories/learnings.json << 'EOF'
[]
EOF

cat > .claude/memories/api_integrations.json << 'EOF'
{}
EOF

# 3. Verify files created
ls -la .claude/memories/
# Should show 4 JSON files with sizes > 0

# 4. Test memory system
python -c "
from orchestrator import MemoryManager
mem = MemoryManager('.claude/memories')
print('Memory system OK')
"
```

**Prevención:**
- Don't delete `.claude/memories/` directory
- Backup memories before major changes
- Use `git` to track memory changes
- Add memories to `.gitignore` if they contain sensitive data

---

### Error 5.2: "JSON decode error - memory file corrupted"

**Síntoma:**
```python
orchestrator.store_architectural_decision(decision)
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 15 column 5 (char 387)
```

**Causa:**
Memory JSON file corrupted (invalid syntax, incomplete write).

**Solución:**
```bash
# 1. Identify corrupted file from error
# Error shows: .claude/memories/architectural_decisions.json

# 2. Backup corrupted file
cp .claude/memories/architectural_decisions.json \
   .claude/memories/architectural_decisions.json.backup

# 3. Try to fix JSON
# Validate JSON online: jsonlint.com
cat .claude/memories/architectural_decisions.json | python -m json.tool

# 4. If unfixable, restore from git or reset
git checkout .claude/memories/architectural_decisions.json
# Or reset to empty:
echo '[]' > .claude/memories/architectural_decisions.json

# 5. Verify fix
python -c "
import json
with open('.claude/memories/architectural_decisions.json') as f:
    data = json.load(f)
    print(f'Loaded {len(data)} decisions')
"
```

**Prevención:**
- Commit memories to git after successful phases
- Use atomic writes (write to temp file, then rename)
- Validate JSON after each write
- Keep backups of important memories

---

### Error 5.3: "Memory retrieval returns old/wrong patterns"

**Síntoma:**
```
Phase 2: Research shows:
"Based on previous learnings, using library XYZ for API ABC"

But XYZ is deprecated, and you never used it before.
```

**Causa:**
Memory contains outdated patterns from old projects or incorrect learnings.

**Solución:**
```bash
# 1. Inspect memory files
cat .claude/memories/patterns.json | python -m json.tool

# 2. Find the bad pattern
# Look for mentions of "XYZ library" or "API ABC"

# 3. Edit memory file to remove bad pattern
# Use text editor to remove the entry, or:
python << 'EOF'
import json

with open('.claude/memories/patterns.json', 'r') as f:
    patterns = json.load(f)

# Remove patterns mentioning "XYZ"
patterns = [p for p in patterns if 'XYZ' not in str(p)]

with open('.claude/memories/patterns.json', 'w') as f:
    json.dump(patterns, f, indent=2)
EOF

# 4. Verify removal
cat .claude/memories/patterns.json | grep "XYZ"
# Should return nothing

# 5. Restart research phase
# At CHECKPOINT 1: "restart"
```

**Prevención:**
- Review memory contents periodically
- Clear outdated patterns every few months
- Use memory versioning (add `date_learned` field)
- Provide feedback when agent suggests wrong patterns

---

## 6. Integration & Performance Issues

### Error 6.1: "sequential-thinking agent timeout after 5 minutes"

**Síntoma:**
```
Phase 2: Intelligent Analysis
Running sequential-thinking analysis...
[5 minutes pass]
Error: sequential-thinking agent timeout
Analysis incomplete
```

**Causa:**
Goal description demasiado complejo, agent no puede terminar análisis en tiempo límite.

**Solución:**
```bash
# Option A: Simplify goal description
# Instead of:
"Create system to process invoices from multiple vendors, extract data using OCR and GPT-4,
validate against business rules, store in PostgreSQL, send notifications via Slack and email,
generate reports, sync with Salesforce, and provide real-time dashboard"

# Use:
"Process invoice PDFs, extract data with OCR, store in database"
# Then add features incrementally after initial project works

# Option B: Use orchestrator directly (skip sequential-thinking)
# In Phase 2, if you see timeout, respond:
"skip sequential-thinking - use orchestrator analyze_intent only"

# Option C: Increase timeout (if available)
export SEQUENTIAL_THINKING_TIMEOUT=600  # 10 minutes

# Option D: Break into multiple projects
# Project 1: Invoice processing + OCR
# Project 2: Salesforce integration
# Project 3: Reporting dashboard
```

**Prevención:**
- Start with minimal viable project
- Add one API/integration at a time
- Use iterative approach (basic → advanced)
- Respect 50% context window target

---

### Error 6.2: "Context window exceeded 50% - performance degraded"

**Síntoma:**
```
Phase 3: Tech Stack Analysis
⚠️  WARNING: Context window at 55%
Performance may degrade
Consider simplifying project scope
```

**Causa:**
Project demasiado complejo para generarse en una sesión.

**Solución:**
```bash
# At next checkpoint, simplify:

# At CHECKPOINT 1 (if at 55%):
"fix: Remove Salesforce integration - focus on core invoice processing only"

# At CHECKPOINT 2 (if at 55%):
"fix: Reduce to 2 core tests instead of 10 - we'll add more later"

# General simplification strategies:
1. Reduce number of APIs (2-3 max)
2. Defer non-critical features
3. Use simpler tech stack
4. Reduce test coverage to core paths (80% instead of 100%)
5. Generate base project, then iterate

# If warning appears:
# Don't ignore it - context window affects quality
# Better to generate smaller project successfully
# Than large project with errors
```

**Prevención:**
- Start small, iterate later
- Use SIMPLE complexity for first project
- Limit to 2-3 APIs maximum
- Review context usage at each checkpoint
- See BEST_PRACTICES.md for optimization tips

---

### Error 6.3: "library-researcher agent returns no results"

**Síntoma:**
```
Phase 2: Intelligent Analysis
Researching libraries for Gmail API integration...
library-researcher: No results found for "Gmail API Python"
```

**Causa:**
Network issue, API limite alcanzado, o query mal formado.

**Solución:**
```bash
# 1. Check network connectivity
ping docs.python.org
# Should succeed

# 2. Verify MCP server is running
# In Claude Code settings, check MCP servers status
# Should show: "library-researcher: ✅ Connected"

# 3. If no connectivity, agent will use fallback
# Orchestrator has built-in knowledge of common libraries
# Check CHECKPOINT 1 for recommended libraries

# 4. Manual research if needed
# If agent suggests wrong libraries at CP1, use "fix:"
"fix: Use google-api-python-client and google-auth for Gmail API, not library XYZ"

# 5. Restart MCP server if needed
# Claude Code → Settings → MCP Servers → Restart
```

**Prevención:**
- Ensure stable internet connection
- Use specific API names (not generic terms)
- Trust orchestrator's built-in knowledge for common APIs
- Verify library names at CHECKPOINT 1

---

### Error 6.4: "Parallel agents not completing - stuck in Phase 2"

**Síntoma:**
```
Phase 2: Intelligent Analysis (HYBRID)
✅ orchestrator.analyze_intent() - Complete
⏳ sequential-thinking agent - Running...
⏳ library-researcher agent - Running...
[10 minutes, no progress]
```

**Causa:**
One or more parallel agents hung, bloqueando el workflow.

**Solución:**
```bash
# 1. Check which agents are stuck
# Look for last completed step in output

# 2. If only one agent stuck, try continuing
# In Claude Code, respond:
"skip stuck agents - continue with available results"

# 3. If multiple agents stuck, restart phase
# Respond:
"restart Phase 2 with orchestrator only - skip parallel agents"

# 4. Check MCP server logs for errors
# Claude Code → Developer Tools → Console
# Look for MCP errors

# 5. Nuclear option - restart from Phase 1
# At CHECKPOINT 1 (when you reach it):
"restart"
```

**Prevención:**
- Monitor Phase 2 progress (should complete in 2-3 min)
- If stuck >5 min, interrupt and restart
- Report agent timeout issues
- Use orchestrator-only mode if agents consistently fail

---

## 7. Generated Project Issues

### Error 7.1: "Generated project missing orchestrator/ folder"

**Síntoma:**
```bash
$ ls -la gmail-to-notion-sync/
src/
tests/
.claude/
README.md
requirements.txt

# Missing:
# orchestrator/  ❌
# .claude/agents/@self-improve.md  ❌
```

**Causa:**
Project complexity era SIMPLE - orchestrator solo se incluye en MEDIUM/HIGH.

**Solución:**
```bash
# This is EXPECTED behavior for SIMPLE projects

# Check complexity that was approved:
cat gmail-to-notion-sync/.claude/memories/architectural_decisions.json
# Look for: "complexity": "simple"

# If you wanted MEDIUM:
# Option A: Regenerate with explicit complexity
@project-initializer
# At Phase 1, say:
"Create MEDIUM complexity project for gmail-to-notion sync with orchestrator capabilities"

# Option B: Upgrade existing project manually
# Copy orchestrator template:
cp -r /path/to/claude-code-template/.claude/templates/medium/orchestrator/ \
      gmail-to-notion-sync/orchestrator/

cp /path/to/claude-code-template/.claude/templates/medium/@self-improve.md \
   gmail-to-notion-sync/.claude/agents/

# Edit to customize for your project
```

**Prevención:**
- Understand complexity levels (see USER_GUIDE.md)
- Mention "orchestrator" in goal if you want MEDIUM
- Review complexity in CHECKPOINT 1 BEFORE approving
- Don't expect orchestrator/ in SIMPLE projects

---

### Error 7.2: "Tests show 0% coverage despite TDD approach"

**Síntoma:**
```bash
$ cd gmail-to-notion-sync
$ pytest tests/ --cov=src
PASSED tests/test_gmail_client.py::test_oauth_flow
PASSED tests/test_notion_client.py::test_create_page

Coverage: 0%
```

**Causa:**
pytest-cov no configurado, o pytest.ini missing.

**Solución:**
```bash
# 1. Verify pytest-cov installed
pip show pytest-cov
# If not: pip install pytest-cov

# 2. Create pytest.ini
cat > pytest.ini << 'EOF'
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    --cov=src
    --cov-report=term-missing
    --cov-report=html
    --cov-branch
EOF

# 3. Run tests again
pytest tests/ -v
# Should now show coverage

# 4. If still 0%, check test imports
cat tests/test_gmail_client.py | grep import
# Must import from src.*, not direct import

# Fix imports:
# Before: from gmail_client import GmailClient
# After:  from src.gmail_client import GmailClient
```

**Prevención:**
- TDD loop should configure pytest-cov automatically
- Verify pytest.ini exists in generated project
- Check coverage after EACH test in TDD loop
- Report to agent if coverage not tracked

---

### Error 7.3: "@self-improve agent not working"

**Síntoma:**
```bash
$ cd gmail-to-notion-sync
$ cat .claude/agents/
@self-improve.md  ✅ Exists

# But when trying to use:
$ @self-improve
Error: Agent not found or not configured
```

**Causa:**
Agent file existe pero no está registrado en Claude Code para ESTE proyecto.

**Solución:**
```bash
# 1. Verify you're in the generated project directory
pwd
# Should show: /path/to/gmail-to-notion-sync/

# 2. Check Claude Code recognized the project
# Claude Code reads .claude/ when you open a directory
# Make sure you opened gmail-to-notion-sync/ as project root

# 3. Reload Claude Code window
# Command Palette → "Reload Window"

# 4. Verify agent available
# In Claude Code, type: "@"
# Should show @self-improve in autocomplete

# 5. If still not working, check agent file syntax
head -20 .claude/agents/@self-improve.md
# Should start with proper frontmatter
```

**Prevención:**
- Open generated project as root directory in Claude Code
- Don't try to use @self-improve from template directory
- Reload window after generating new project
- Verify .claude/ directory structure

---

### Error 7.4: "README.md in generated project is generic"

**Síntoma:**
```markdown
# {{ project_name }}

{{ project_description }}

## Installation
{{ installation_instructions }}
```

**Causa:**
Template variables no fueron sustituidas - Jinja2 rendering failed.

**Solución:**
```bash
# 1. Check if this is the template or generated project
pwd
# Template: /path/to/claude-code-template/
# Generated: /path/to/gmail-to-notion-sync/

# If you're in TEMPLATE directory:
# These files SHOULD have {{ variables }} - that's correct!
# Don't edit template files

# If you're in GENERATED project:
# This is a bug - variables should be replaced

# 2. Check generation logs
# Look for errors during Phase 8-9
# Search for: "Template rendering failed"

# 3. Regenerate README manually
# Option A: Ask agent
"@project-initializer regenerate README.md with proper variables"

# Option B: Edit manually
# Replace:
{{ project_name }} → gmail-to-notion-sync
{{ project_description }} → Sync Gmail emails to Notion database
# etc.

# 4. Report bug with:
# - Project complexity
# - Template version
# - Error messages from generation
```

**Prevención:**
- Check CHECKPOINT 2 for template variables list
- Verify all variables have values before approve
- Review generated README in Phase 9 validation
- Report template bugs to improve system

---

### Error 7.5: "requirements.txt missing key dependencies"

**Síntoma:**
```bash
$ cd gmail-to-notion-sync
$ pip install -r requirements.txt
# Installs successfully

$ python src/gmail_client.py
ModuleNotFoundError: No module named 'google.auth'
```

**Causa:**
requirements.txt generado incompleto - falta dependencia identificada en research.

**Solución:**
```bash
# 1. Identify missing dependency
# From error: google.auth → package: google-auth

# 2. Add to requirements.txt
cat >> requirements.txt << 'EOF'
google-auth>=2.16.0
google-auth-oauthlib>=1.0.0
google-api-python-client>=2.80.0
EOF

# 3. Install
pip install -r requirements.txt

# 4. Verify
python -c "from google.auth import credentials; print('OK')"

# 5. Update requirements.txt to include versions
pip freeze | grep google-auth >> requirements.txt.new
# Review and replace old requirements.txt

# 6. Report to agent for future improvements
"The generated requirements.txt was missing google-auth dependencies"
```

**Prevención:**
- Review requirements.txt in Phase 9 validation
- Test installation in fresh virtual environment
- Compare requirements with CHECKPOINT 1 tech stack
- Report missing dependencies to improve templates

---

## 🔧 Debugging Toolbox

### Essential Commands

```bash
# ============================================
# Template Health Check
# ============================================

# 1. Verify Python version
python --version
# Expected: Python 3.10+

# 2. Check orchestrator installation
python -c "import orchestrator; print(orchestrator.__version__)"
# Expected: 1.0.0

# 3. Verify API key
echo $ANTHROPIC_API_KEY
# Should output: sk-ant-api03-...

# 4. List available agents
ls -la .claude/agents/
# Should show: project-initializer.md, codebase-analyst.md, etc.

# 5. Check memory system
ls -la .claude/memories/
cat .claude/memories/patterns.json | python -m json.tool
# Should show valid JSON

# 6. Verify templates exist
ls -la .claude/templates/base/
# Should show: README.md.j2, src/, tests/, etc.

# ============================================
# Generated Project Health Check
# ============================================

# 1. Navigate to project
cd /path/to/generated-project/

# 2. Verify structure
ls -la
# Expected: src/, tests/, .claude/, README.md, requirements.txt

# 3. Check dependencies
pip install -r requirements.txt
pip list

# 4. Run tests
pytest tests/ -v
# All tests should PASS

# 5. Check coverage
pytest tests/ --cov=src --cov-report=term-missing
# Should show >80% coverage (100% if TDD completed)

# 6. Verify orchestrator (MEDIUM/HIGH only)
ls -la orchestrator/
python -c "from orchestrator import OrchestratorAgent; print('OK')"

# 7. Check @self-improve agent (MEDIUM/HIGH only)
cat .claude/agents/@self-improve.md | head -20

# ============================================
# Debugging Tools
# ============================================

# Enable verbose logging
export ORCHESTRATOR_DEBUG=true
export ANTHROPIC_LOG_LEVEL=debug

# Check JSON validity
python -m json.tool < file.json

# Monitor context window usage (approximate)
wc -w .claude/memories/*.json
# Keep total <5000 words for <50% context

# Verify Pydantic models
python -c "
from orchestrator.models import AutomationIntent
from pydantic import ValidationError
intent = AutomationIntent(
    project_name='test',
    project_type='api_integration',
    complexity='simple'
)
print(intent.model_dump_json(indent=2))
"

# Test template rendering
python -c "
from jinja2 import Template
template = Template('Hello {{ name }}!')
print(template.render(name='World'))
"

# Check MCP tools availability
# In Claude Code:
# "List all available MCP tools"
```

---

## 🆘 Getting Help

### Quick Diagnostic Checklist

Before asking for help, verify these 5 items:

```bash
# ✅ 1. Python version >= 3.10
python --version

# ✅ 2. Dependencies installed
pip show orchestrator pydantic jinja2

# ✅ 3. API key configured
echo $ANTHROPIC_API_KEY | grep "sk-ant-"

# ✅ 4. Memory system initialized
ls .claude/memories/*.json

# ✅ 5. No obvious errors in logs
# Check last 20 lines of agent output
```

### How to Report Issues

If you encounter a bug or error:

**1. Gather Information**
```bash
# System info
python --version
pip list | grep -E "orchestrator|pydantic|anthropic"

# Error reproduction
# Copy exact commands that caused error

# Error message
# Copy full error output including stack trace

# Context
# What phase were you in? (Phase 0-10)
# What checkpoint? (CHECKPOINT 1 or 2)
# What was your goal/description?
```

**2. Create GitHub Issue**

Go to: [github.com/your-username/claude-code-template/issues](https://github.com/your-username/claude-code-template/issues)

Use this template:
```markdown
## Bug Description
[Brief description of what went wrong]

## Steps to Reproduce
1. Started @project-initializer
2. Entered goal: "..."
3. At CHECKPOINT 1, responded: "approve"
4. Error occurred in Phase 3

## Error Message
```
[Paste full error here]
```

## System Information
- Python version: 3.10.9
- Orchestrator version: 1.0.0
- OS: macOS 13.2
- Dependencies: [paste output of `pip list`]

## Expected Behavior
[What should have happened]

## Actual Behavior
[What actually happened]

## Additional Context
- Complexity level: MEDIUM
- APIs involved: Gmail API, Notion API
- Context window usage: ~45%
```

**3. Include Relevant Files**

Attach (if relevant):
- `.claude/memories/*.json` (redact sensitive data)
- `requirements.txt`
- Error logs
- Generated project structure (`tree -L 2`)

### Community Resources

- **📖 Documentation**
  - [Quick Start](../QUICK_START.md) - 10-minute walkthrough
  - [User Guide](USER_GUIDE.md) - Complete documentation
  - [Best Practices](BEST_PRACTICES.md) - Optimization tips

- **💬 Get Help**
  - [GitHub Issues](https://github.com/your-username/claude-code-template/issues) - Bug reports
  - [GitHub Discussions](https://github.com/your-username/claude-code-template/discussions) - Q&A
  - [Anthropic Discord](https://discord.gg/anthropic) - Community chat

- **📚 Additional Resources**
  - [Claude Code Docs](https://docs.claude.com/claude-code) - Official documentation
  - [BAML Context Engineering](https://docs.boundaryml.com/docs/snippets/vscode/context-engineering) - Best practices
  - [Pydantic v2 Docs](https://docs.pydantic.dev/) - Data validation

### Emergency Recovery

If everything is broken:

```bash
# ============================================
# NUCLEAR OPTION 1: Reset Memory System
# ============================================
# ⚠️  WARNING: Loses all learned patterns

# Backup current state
cp -r .claude/memories/ .claude/memories.backup/

# Reset to empty
echo '[]' > .claude/memories/architectural_decisions.json
echo '[]' > .claude/memories/patterns.json
echo '[]' > .claude/memories/learnings.json
echo '{}' > .claude/memories/api_integrations.json

# Verify
ls -la .claude/memories/

# ============================================
# NUCLEAR OPTION 2: Fresh Template Clone
# ============================================
# ⚠️  WARNING: Loses all local changes

# Backup your changes
cp -r claude-code-template claude-code-template.backup

# Fresh clone
cd ..
rm -rf claude-code-template
git clone https://github.com/your-username/claude-code-template.git
cd claude-code-template

# Reinstall
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key"

# Test
python example_orchestrator_usage.py

# ============================================
# NUCLEAR OPTION 3: Start Over with New Project
# ============================================

# If current project generation is stuck/broken:
# 1. Exit Claude Code
# 2. Create new directory
mkdir ~/new-project-attempt
cd ~/new-project-attempt

# 3. Copy fresh template
cp -r ~/claude-code-template/.claude .
cp ~/claude-code-template/requirements.txt .

# 4. Install dependencies
pip install -r requirements.txt

# 5. Restart Claude Code in this directory
# 6. Try @project-initializer again with simpler goal
```

---

## 💡 FAQ

### Q1: How do I know if my error is a bug or expected behavior?

**A:** Check these indicators:

**🐛 Likely a BUG:**
- Error message with stack trace
- Undefined variables in templates ({{ project_name }})
- JSON parsing errors in memory files
- Agent crashes or hangs indefinitely
- Missing files in generated project that should exist

**✅ Likely EXPECTED:**
- orchestrator/ missing in SIMPLE projects (only MEDIUM/HIGH get it)
- Agent asks for credentials setup (API keys needed)
- Checkpoint waiting for your response (need to type "approve")
- Tests fail before implementation (TDD red phase)
- Context window warning at 45%+ (simplify scope)

**When in doubt:** Check USER_GUIDE.md or ask in GitHub Discussions.

---

### Q2: What should I do first when I see an error?

**A:** Follow the **5-Second Diagnostic**:

1. **Read the error message** - Often tells you exactly what's wrong
2. **Check which phase** you're in (Phase 0-10)
3. **Look for CRITICAL/HIGH priority** section in this guide matching your error
4. **Try the Quick Fix** if available
5. **If still stuck**, gather info and report issue

**Common first fixes:**
- `pip install -r requirements.txt` (if import errors)
- `export ANTHROPIC_API_KEY="..."` (if API errors)
- Type exact command `"approve"` (if checkpoint stuck)
- `cd` into generated project (if wrong directory)

---

### Q3: Can I skip checkpoints to speed up generation?

**A:** **No, don't skip checkpoints!** Here's why:

**CHECKPOINT 1 (after Research):**
- ROI: **100x** (2-5 min prevents 1,000 bad lines)
- Catches: Wrong APIs, wrong tech stack, impossible scope
- **Critical** - Skipping leads to complete regeneration

**CHECKPOINT 2 (after Planning):**
- ROI: **10-20x** (3-5 min prevents 10-100 bad lines)
- Catches: Missing tests, wrong architecture, scope creep
- **Very Important** - Skipping leads to major refactoring

**If you're in a hurry:**
- Better to simplify scope (SIMPLE complexity, fewer APIs)
- Than skip checkpoints and waste 10x more time fixing errors

**Exception:** If regenerating same project with minor changes, you can "approve" faster.

---

### Q4: How do I customize generated project templates?

**A:** Two approaches:

**Approach A: Before Generation (Template Customization)**
```bash
# 1. Edit template files
cd claude-code-template/.claude/templates/base/

# 2. Modify Jinja2 templates
# Example: Add custom test fixture
edit tests/conftest.py.j2

# 3. Add variables to orchestrator context
edit orchestrator/project_generator.py
# In _get_template_context(), add your variable

# 4. Generate project - your changes apply
@project-initializer
```

**Approach B: After Generation (Project Customization)**
```bash
# 1. Generate project normally
@project-initializer
# ... complete workflow ...

# 2. Modify generated files
cd generated-project/
edit src/custom_module.py  # Add your code
edit tests/test_custom.py  # Add tests

# 3. Use @self-improve agent (MEDIUM/HIGH)
@self-improve "optimize error handling"
```

See [BEST_PRACTICES.md](BEST_PRACTICES.md) for detailed customization guide.

---

### Q5: What's the difference between SIMPLE, MEDIUM, and HIGH complexity?

**A:** Feature comparison:

| Feature | SIMPLE | MEDIUM | HIGH |
|---------|--------|--------|------|
| **Basic project structure** | ✅ | ✅ | ✅ |
| **Tests (100% coverage)** | ✅ | ✅ | ✅ |
| **Documentation** | ✅ | ✅ | ✅ |
| **orchestrator/ folder** | ❌ | ✅ | ✅ |
| **@self-improve agent** | ❌ | ✅ | ✅ |
| **Memory system** | Basic | Advanced | Advanced |
| **Subagents** | 0 | 3 | 5 |
| **Recommended for** | 1-2 APIs, basic logic | 2-3 APIs, moderate logic | 3+ APIs, complex orchestration |
| **Context window usage** | 20-30% | 35-45% | 45-50% |

**Choose based on:**
- **SIMPLE**: Learning the system, basic integrations, quick prototypes
- **MEDIUM**: Production projects, need evolution, multiple APIs
- **HIGH**: Complex multi-API projects, enterprise, need advanced orchestration

You can always upgrade SIMPLE → MEDIUM later by manually adding orchestrator/.

---

### Q6: How do I monitor context window usage?

**A:** Three methods:

**Method 1: Agent Warnings**
```
⚠️  WARNING: Context window at 55%
Performance may degrade
```
If you see this, simplify scope at next checkpoint.

**Method 2: Manual Estimation**
```bash
# Count words in memories
wc -w .claude/memories/*.json
# Target: <5,000 words total

# Count template variables
cat .claude/templates/base/*.j2 | wc -l
# Target: <2,000 lines total

# Rough formula:
# Context% = (memory_words/10000 + template_lines/4000) * 100
```

**Method 3: Ask Agent**
```
"What's my current context window usage?"
```
Agent will estimate based on conversation length + memories + templates.

**Optimization tips:**
- Limit to 2-3 APIs
- Use SIMPLE complexity first
- Clear old memories periodically
- Break large projects into smaller ones

---

### Q7: Can I use this template for non-Python projects?

**A:** **Yes!** The template supports multiple languages:

**Currently supported:**
- **Python** (primary, best support)
- **Node.js/JavaScript** (good support)
- **TypeScript** (good support)

**To use non-Python:**
```
At Phase 1, specify clearly:

"Create a Node.js project to sync Gmail to Notion using TypeScript"

NOT just:
"Sync Gmail to Notion"
```

The orchestrator will:
- Use Node.js templates instead of Python
- Generate `package.json` instead of `requirements.txt`
- Use Jest instead of pytest for TDD
- Adjust all templates for JavaScript/TypeScript

**Verify at CHECKPOINT 1:**
```
Tech Stack:
- Language: Node.js/TypeScript ✅
- Testing: Jest ✅
- Package manager: npm ✅
```

If wrong language, use `"fix: Change to Python instead of Node.js"`

---

## 🚑 Emergency Recovery

### If Agent is Completely Stuck

```bash
# 1. Save current state
# Take screenshot of last agent message
# Copy conversation to text file

# 2. Exit Claude Code gracefully
# Don't force quit if possible

# 3. Check what was saved
ls -la .claude/memories/
cat .claude/memories/architectural_decisions.json | tail -20

# 4. Restart Claude Code

# 5. Resume conversation
@project-initializer
# Say: "Resume from last checkpoint - I had approved research for [project-name]"

# 6. If resume fails, start fresh with lessons learned
# Use simpler description
# Reference what worked from previous attempt
```

### If Generated Project is Broken

```bash
# Don't delete it yet! Can salvage parts

# 1. Identify what works
pytest tests/ -v  # Which tests pass?
ls -la src/       # Which modules exist?

# 2. Save working parts
mkdir ../salvage/
cp src/working_module.py ../salvage/
cp tests/test_working.py ../salvage/

# 3. Regenerate
cd ..
@project-initializer
# Describe project again
# Mention what should be kept from previous attempt

# 4. After generation, merge salvaged code
cp salvage/*.py new-project/src/
```

### If Memory System is Corrupted

```bash
# Symptoms: JSON errors, cannot read memories

# 1. Backup everything
cp -r .claude/ .claude.backup.$(date +%Y%m%d_%H%M%S)/

# 2. Validate each memory file
for file in .claude/memories/*.json; do
    echo "Checking $file..."
    python -m json.tool < "$file" > /dev/null 2>&1 || echo "CORRUPTED: $file"
done

# 3. Fix corrupted files
# Option A: Restore from git
git checkout .claude/memories/[corrupted-file].json

# Option B: Reset to empty
echo '[]' > .claude/memories/[corrupted-file].json

# 4. Verify all files valid
for file in .claude/memories/*.json; do
    python -m json.tool < "$file" | head -5
done
```

---

## 📚 Navigation

**Documentation Map:**

```
🚀 QUICK_START.md (10 min)     ← Start here if new
       ↓
📖 USER_GUIDE.md (deep dive)   ← Understand the system
       ↓
🔧 TROUBLESHOOTING.md          ← You are here
       ↓
✨ BEST_PRACTICES.md           ← Optimize and customize
       ↓
🤝 CONTRIBUTING.md             ← Contribute improvements
```

**Quick Links:**
- [🏠 Home](../README.md)
- [🚀 Quick Start](../QUICK_START.md)
- [📖 User Guide](USER_GUIDE.md)
- [✨ Best Practices](BEST_PRACTICES.md)
- [🤝 Contributing](../CONTRIBUTING.md)
- [📋 Planning](../.claude/PLANNING.md)
- [✅ Current Tasks](../.claude/TASK.md)

---

**Version:** 3.0.0 (M6 - Documentation)
**Last Updated:** 2025-01-03
**Status:** ✅ Production Ready

---

*If this guide helped solve your issue, consider contributing improvements! See [CONTRIBUTING.md](../CONTRIBUTING.md)*
