# 🚀 Quick Start - Claude Code Template

> **Generate complete automation projects in 10 minutes** - From idea to production-ready code with hybrid architecture

---

## 📖 What is This?

The **Claude Code Template** is a hybrid AI system that generates complete automation projects from natural language descriptions. It combines:

- **@project-initializer** (UX Layer) - Interactive guided experience with human validation checkpoints
- **Orchestrator Agent SDK** (Engine Layer) - Structured analysis, persistent memory, and automatic validation
- **TDD Approach** - Tests define behavior, code follows (100% coverage guaranteed)
- **Context Engineering** - Best practices from BAML team applied

**What you get:** Complete projects with src/, tests/, docs/, and optional self-improvement capabilities.

---

## 📦 Prerequisites

Before starting, ensure you have:

- **Python 3.10+** - Check with `python --version`
- **Claude API Key** - Get it from [console.anthropic.com](https://console.anthropic.com)
- **Git** - For cloning the repository
- **Basic Claude Code knowledge** - Familiar with agents and tools

---

## 🛠️ Installation (2 minutes)

### Step 1: Clone Repository

```bash
# Clone the template
git clone https://github.com/tu-usuario/claude-code-template.git
cd claude-code-template
```

### Step 2: Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt
```

Expected output:
```
✅ Successfully installed anthropic pydantic jinja2 ...
```

### Step 3: Configure API Key

```bash
# Set your Claude API key
export ANTHROPIC_API_KEY="your-api-key-here"

# Or add to ~/.bashrc or ~/.zshrc for persistence
echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
```

### Step 4: Verify Installation

```bash
# Test the orchestrator
python example_orchestrator_usage.py
```

Expected output:
```
✅ Orchestrator SDK initialized
✅ Version: 1.0.0
✅ Memory system ready
✅ All components available
```

**Troubleshooting:** If you see errors, check [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

---

## 🎯 Your First Project (10 minutes)

Let's create a real automation project: **Gmail to Notion integration**.

### Step 1: Start @project-initializer

In Claude Code, invoke the project initializer agent:

```
@project-initializer
```

The agent will greet you and start **Phase 0** (internal orchestrator initialization).

---

### Step 2: Describe Your Goal

**Agent asks:**
```
🎯 What automation project do you want to create?
```

**You respond:**
```
I want to automate reading emails from Gmail and saving them to Notion
```

---

### Step 3: Answer Clarifying Questions (Phase 1)

The agent will ask follow-up questions:

**Agent:**
```
📋 To better understand your needs:

1. Which Gmail labels/folders should I monitor?
2. What information from emails do you want in Notion?
3. How often should it check for new emails?
4. Do you need OAuth authentication setup?
```

**Example answers:**
```
1. Monitor the "Important" label
2. Save: sender, subject, date, body text
3. Every 5 minutes
4. Yes, I'll need OAuth for both Gmail and Notion
```

The agent proceeds to **Phase 2: Intelligent Analysis** (hybrid approach using orchestrator + parallel agents).

---

### Step 4: Review Research (CHECKPOINT 1) ⚠️

After ~2 minutes of analysis, the agent presents:

```
🔍 CHECKPOINT 1: Research Validation (CRITICAL - Human Review Required)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 RESEARCH SUMMARY

Project: gmail-to-notion-sync
Type: API Integration (Medium Complexity)
APIs Required: Gmail API, Notion API

Key Findings:
- Gmail API: google-auth + google-api-python-client
- Notion API: notion-client library
- OAuth 2.0 flow needed for both
- Polling strategy: 5-min intervals with rate limiting
- Storage: Notion database for emails

Estimated Complexity: MEDIUM
- Will include: orchestrator/ + @self-improve agent
- Test coverage: 100% (TDD approach)
- Context window projection: ~35% (well under 50% target)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❓ VALIDATION QUESTIONS

1. Is the project name "gmail-to-notion-sync" appropriate?
2. Are Gmail API and Notion API the correct integrations?
3. Is MEDIUM complexity accurate for your skill level?
4. Is 35% context window acceptable (<50% target)?
5. Did I capture your intention correctly?
6. Is this checkpoint valuable before planning?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏸️  YOUR RESPONSE REQUIRED:

✅ "approve"                    → Proceed to Planning Phase
🔄 "fix: [description]"        → Make corrections to research
❌ "restart"                    → Research fundamentally wrong

ROI: 2-5 minutes prevents 1,000 bad lines of code (100x ROI)
```

**You respond:**
```
approve
```

The agent proceeds to **Phase 3-7: Planning & Analysis**.

---

### Step 5: Review Plan (CHECKPOINT 2) ⚠️

After ~3 minutes of planning, the agent presents:

```
📋 CHECKPOINT 2: Planning Validation (CRITICAL - Human Review Required)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📐 IMPLEMENTATION PLAN

Phase 8.1: Create Base Structure
- src/gmail_client.py
- src/notion_client.py
- src/sync_engine.py
- tests/ with 100% coverage
- .claude/ with agents + memories
- orchestrator/ (MEDIUM complexity)
- @self-improve agent (auto-evolution)

Phase 8.2: Define Test Suite FIRST (TDD)
✅ test_gmail_oauth_flow()
✅ test_fetch_emails_from_label()
✅ test_notion_database_creation()
✅ test_notion_page_creation()
✅ test_sync_engine_end_to_end()
✅ test_rate_limiting()

Phase 8.3: TDD Loop (5 steps per test)
1. Show failing test
2. Guide OAuth setup (credentials.json)
3. Implement feature
4. Run test → PASS ✅
5. Confirm → Next feature

Tech Stack:
- Python 3.10+
- google-auth, google-api-python-client
- notion-client
- pytest, pytest-cov
- python-dotenv

What We're NOT Doing (Scope Control):
❌ Email sending (only reading)
❌ Notion → Gmail sync (one-way only)
❌ Real-time webhooks (polling only)
❌ Email attachments (text only)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❓ VALIDATION QUESTIONS

1. Are phases clear with specific file names?
2. Are tests defined BEFORE implementation (TDD)?
3. Is orchestrator correctly included (MEDIUM complexity)?
4. Is scope clear (what we're NOT doing)?
5. Are verification steps (5-step TDD loop) included?
6. Is context window projection <50% for implementation?
7. Is this checkpoint valuable before coding?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⏸️  YOUR RESPONSE REQUIRED:

✅ "approve"                    → Begin TDD Implementation
🔄 "fix: [description]"        → Adjust plan
❌ "back to research"          → Plan reveals research was wrong

ROI: 3-5 minutes prevents 10-100 bad lines of code (10-20x ROI)
```

**You respond:**
```
approve
```

The agent proceeds to **Phase 8: TDD Implementation**.

---

### Step 6: Watch TDD Implementation (Phase 8)

The agent now implements each feature using the **5-step TDD loop**:

**Example for Gmail OAuth:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 STEP 1: Failing Test

Running: tests/test_gmail_client.py::test_gmail_oauth_flow

FAILED - GmailClient class not found
Expected: Successful OAuth authentication
Actual: ImportError

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 STEP 2: Setup Guidance

To proceed, you need:

1. Go to console.cloud.google.com
2. Create project "gmail-notion-sync"
3. Enable Gmail API
4. Create OAuth 2.0 credentials
5. Download credentials.json → project root

Ready to continue? (yes/no)
```

**You respond:** `yes`

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚙️  STEP 3: Implementation

Creating src/gmail_client.py...

[Code implementation happens]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ STEP 4: Test Passes

Running: tests/test_gmail_client.py::test_gmail_oauth_flow

PASSED ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 STEP 5: Confirmation

Gmail OAuth flow implemented and tested!

Ready for next feature (Notion API)? (yes/no)
```

**You respond:** `yes`

This loop repeats for each feature until **100% test coverage** achieved.

---

### Step 7: Explore Generated Project

After ~5 minutes of TDD implementation:

```
✅ PROJECT GENERATED SUCCESSFULLY!

Location: /path/to/gmail-to-notion-sync/

📊 Quality Metrics:
- Test Coverage: 100% ✅
- Tests Passing: 6/6 ✅
- Linting: 0 errors ✅
- Type Checking: 0 errors ✅
- Quality Score: 9.5/10 ✅

🚀 Next Steps:
1. cd gmail-to-notion-sync
2. Review README.md for setup instructions
3. Run: python src/sync_engine.py
```

---

## 📁 Understanding the Output

Your generated project has this structure:

```
gmail-to-notion-sync/
├── src/                          # Source code
│   ├── gmail_client.py          # Gmail API integration
│   ├── notion_client.py         # Notion API integration
│   └── sync_engine.py           # Main orchestration
│
├── tests/                        # Tests (100% coverage)
│   ├── test_gmail_client.py
│   ├── test_notion_client.py
│   └── test_sync_engine.py
│
├── orchestrator/                 # Self-improvement engine (MEDIUM)
│   ├── __init__.py
│   ├── agent.py
│   ├── models.py
│   └── memory.py
│
├── .claude/                      # Claude Code configuration
│   ├── agents/
│   │   └── @self-improve.md     # Auto-evolution agent
│   ├── memories/                # Shared learnings
│   ├── PLANNING.md
│   ├── TASK.md
│   └── PRP.md
│
├── README.md                     # Complete documentation
├── CLAUDE.md                     # Claude Code instructions
├── requirements.txt              # Python dependencies
└── .env.example                  # Environment template
```

### Key Files Explained

**src/gmail_client.py**
- Handles Gmail OAuth authentication
- Fetches emails from specified label
- Rate limiting and error handling

**src/notion_client.py**
- Notion API authentication
- Creates database and pages
- Data transformation

**src/sync_engine.py**
- Main orchestration logic
- Polling every 5 minutes
- End-to-end sync workflow

**tests/**
- 100% coverage (TDD approach)
- Unit tests + integration tests
- Real API mocking

**orchestrator/** (MEDIUM complexity only)
- Self-improvement capabilities
- Memory system for learnings
- Can evolve based on usage

**.claude/agents/@self-improve.md** (MEDIUM/HIGH only)
- Analyzes project performance
- Suggests improvements
- Can implement optimizations

---

## 🎓 How to Run Your Project

```bash
# Navigate to project
cd gmail-to-notion-sync

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run tests (verify everything works)
pytest tests/ -v

# Run the sync
python src/sync_engine.py
```

---

## 📚 Next Steps

Congratulations! You've generated your first project. Here's your learning path:

### 1. **Deep Dive** → [USER_GUIDE.md](docs/USER_GUIDE.md)
   - Understand all 11 phases in detail
   - Learn checkpoint strategies (approve/fix/restart)
   - Master TDD workflow
   - Customize templates
   - **Time:** 30-45 minutes

### 2. **Troubleshooting** → [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
   - Common errors and solutions
   - Debugging techniques
   - Getting help
   - **Time:** 10-15 minutes (when needed)

### 3. **Advanced Usage** → [BEST_PRACTICES.md](docs/BEST_PRACTICES.md)
   - Template customization
   - Orchestrator extension
   - Context Engineering tips
   - Memory system usage
   - **Time:** 20-30 minutes

### 4. **Contribute** → [CONTRIBUTING.md](CONTRIBUTING.md)
   - Development setup
   - Pull request process
   - Code standards
   - **Time:** 15-20 minutes

---

## 🔗 Quick Reference

### Essential Commands

```bash
# Generate new project
@project-initializer

# Test orchestrator
python example_orchestrator_usage.py

# Run tests
pytest tests/ -v

# Check version
python -c "import orchestrator; print(orchestrator.__version__)"
```

### Checkpoint Responses

```bash
# At CHECKPOINT 1 or CHECKPOINT 2:
approve                    # Everything looks good
fix: [description]        # Needs corrections
restart                   # Fundamentally wrong
back to research          # (CHECKPOINT 2 only) Plan reveals research error
```

### TDD Loop Responses

```bash
# During Phase 8 (TDD Implementation):
yes                       # Continue to next feature
no                        # Pause implementation
```

---

## 🆘 Need Help?

### Common First-Time Issues

**"ANTHROPIC_API_KEY not set"**
```bash
export ANTHROPIC_API_KEY="your-key"
```

**"Module 'orchestrator' not found"**
```bash
pip install -r requirements.txt
```

**"Tests failing in generated project"**
- Check .env is configured
- Verify API credentials
- See [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

### Get Support

- 📖 [Full Documentation](docs/USER_GUIDE.md)
- 🔧 [Troubleshooting Guide](docs/TROUBLESHOOTING.md)
- 🐛 [Report Issues](https://github.com/tu-usuario/claude-code-template/issues)
- 💬 [Anthropic Discord](https://discord.gg/anthropic)

---

## 📚 Documentation Navigation

**Quick Links:**
- 🏠 [Home](README.md)
- 🚀 [Quick Start](QUICK_START.md) ← **You are here**
- 📖 [User Guide](docs/USER_GUIDE.md)
- 🔧 [Troubleshooting](docs/TROUBLESHOOTING.md)
- ✨ [Best Practices](docs/BEST_PRACTICES.md)
- 🤝 [Contributing](CONTRIBUTING.md)

**Learning Path:**
1. ✅ **QUICK_START.md** (10 min) ← **Current**
2. 📖 USER_GUIDE.md (deep dive)
3. 🔧 TROUBLESHOOTING.md (when stuck)
4. ✨ BEST_PRACTICES.md (advanced)
5. 🤝 CONTRIBUTING.md (contribute)

**Technical Docs:**
- Architecture: [PLANNING.md](.claude/PLANNING.md)
- Current Tasks: [TASK.md](.claude/TASK.md)
- Templates: [TEMPLATES.md](.claude/TEMPLATES.md)
- Validation: [VALIDATION_M5.md](.claude/VALIDATION_M5.md)

---

**Version:** 3.0.0 (M3 + M4 + M5 + M6)
**Last Updated:** 2025-01-03
**Status:** ✅ Production Ready with Complete Documentation

---

*Built with ❤️ using [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) + [Pydantic](https://docs.pydantic.dev/)*
