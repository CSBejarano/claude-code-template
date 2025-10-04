# ✨ Best Practices - Claude Code Template

> **Optimization guide for advanced users** - Maximize the effectiveness of your Claude Code Template projects

**Quick Links:** [🚀 Quick Start](../QUICK_START.md) | [📖 User Guide](USER_GUIDE.md) | [🔧 Troubleshooting](TROUBLESHOOTING.md) | [🤝 Contributing](CONTRIBUTING.md) | [🏠 Home](../README.md)

---

## 📑 Table of Contents

1. [Introduction](#-introduction)
2. [TDD Best Practices](#1-tdd-best-practices)
   - [The TDD Mindset](#11-the-tdd-mindset)
   - [Writing Tests FIRST](#12-writing-tests-first)
   - [Test Organization](#13-test-organization)
   - [Mocking External APIs Effectively](#14-mocking-external-apis-effectively)
   - [Coverage Strategies](#15-coverage-strategies)
3. [Checkpoint Strategies](#2-checkpoint-strategies)
   - [Understanding Checkpoint Purpose](#21-understanding-checkpoint-purpose)
   - [CHECKPOINT 1 Deep Dive](#22-checkpoint-1-deep-dive-research-phase)
   - [CHECKPOINT 2 Deep Dive](#23-checkpoint-2-deep-dive-planning-phase)
   - [Response Format Best Practices](#24-response-format-best-practices)
4. [Template Customization](#3-template-customization)
   - [Understanding the Template System](#31-understanding-the-template-system)
   - [Available Template Variables](#32-available-template-variables)
   - [Adding Custom Variables](#33-adding-custom-variables)
   - [Modifying Base Templates](#34-modifying-base-templates)
   - [Creating Project-Specific Templates](#35-creating-project-specific-templates)
5. [Orchestrator Extension](#4-orchestrator-extension)
   - [Understanding Orchestrator Architecture](#41-understanding-orchestrator-architecture)
   - [Adding Custom Subagents](#42-adding-custom-subagents)
   - [Extending IntentAnalyzer](#43-extending-intentanalyzer)
   - [Memory System Customization](#44-memory-system-customization)
6. [Context Engineering Tips](#5-context-engineering-tips)
   - [Context Window Management](#51-context-window-management)
   - [Writing Effective Goal Descriptions](#52-writing-effective-goal-descriptions)
   - [Simplification Strategies](#53-simplification-strategies)
   - [Memory Organization Best Practices](#54-memory-organization-best-practices)
7. [Project Organization](#6-project-organization)
   - [Directory Structure](#61-directory-structure)
   - [Naming Conventions](#62-naming-conventions)
   - [Module Separation](#63-module-separation)
8. [Advanced Scenarios](#7-advanced-scenarios)
   - [Multi-API Projects](#71-multi-api-projects)
   - [Complex Orchestration](#72-complex-orchestration)
   - [Enterprise Patterns](#73-enterprise-patterns)
9. [Navigation](#-navigation)

---

## 🎯 Introduction

This guide is for **advanced users** who have already created at least one project with the Claude Code Template and want to:

- Master the TDD workflow for 100% test coverage
- Make better decisions at CHECKPOINT 1 and CHECKPOINT 2
- Customize templates for specific project types
- Extend the Orchestrator SDK with custom functionality
- Optimize context window usage for better performance
- Handle complex, multi-API enterprise projects

**Prerequisites:**
- ✅ Completed Quick Start guide
- ✅ Created at least one project successfully
- ✅ Understanding of Python 3.10+ and basic software architecture
- ✅ Familiarity with Pydantic and Jinja2 (helpful but not required)

**How to use this guide:**
- Read sections that match your current challenge
- Copy and adapt code examples to your needs
- Refer to [User Guide](USER_GUIDE.md) for foundational concepts
- Check [Troubleshooting](TROUBLESHOOTING.md) if you encounter issues

---

## 1. TDD Best Practices

### 1.1 The TDD Mindset

**Core principle:** Tests define behavior, code implements it.

```
Traditional: Write code → Hope it works → Test to validate
TDD:        Define behavior with test → Code until test passes
```

**Why this matters:**
- Tests become **specifications**, not afterthoughts
- You write exactly what's needed (no over-engineering)
- Refactoring is safe (tests confirm nothing broke)
- Code reviews focus on logic, not "did you test this?"

### 1.2 Writing Tests FIRST

**The 5-Step TDD Loop (from Phase 8):**

```
1. RED    → Write failing test
2. SETUP  → Add test fixtures/mocks
3. IMPL   → Implement minimal code to pass
4. GREEN  → Test passes
5. CONFIRM → Verify and commit
```

**Example: Gmail OAuth Authentication**

**Step 1 - RED (Write failing test):**

```python
# tests/unit/test_gmail_auth.py
import pytest
from src.gmail_service import GmailAuthenticator

def test_gmail_oauth_flow_creates_credentials():
    """Test that OAuth flow creates valid credentials file."""
    authenticator = GmailAuthenticator()

    # This test WILL FAIL because we haven't implemented it yet
    credentials = authenticator.authenticate()

    assert credentials is not None
    assert credentials.valid is True
    assert os.path.exists('.credentials/gmail_token.json')
```

Run: `pytest tests/unit/test_gmail_auth.py` → ❌ **FAILS** (expected)

**Step 2 - SETUP (Add fixtures/mocks):**

```python
# tests/conftest.py
import pytest
from unittest.mock import Mock, patch

@pytest.fixture
def mock_gmail_credentials():
    """Mock Gmail API credentials."""
    mock_creds = Mock()
    mock_creds.valid = True
    mock_creds.to_json.return_value = '{"token": "mock_token"}'
    return mock_creds

@pytest.fixture
def mock_oauth_flow():
    """Mock OAuth2 flow."""
    with patch('google_auth_oauthlib.flow.InstalledAppFlow') as mock:
        yield mock
```

**Step 3 - IMPLEMENT (Minimal code):**

```python
# src/gmail_service.py
import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

class GmailAuthenticator:
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    CREDENTIALS_DIR = '.credentials'
    TOKEN_FILE = 'gmail_token.json'

    def authenticate(self):
        """Authenticate with Gmail API using OAuth2."""
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', self.SCOPES
        )
        credentials = flow.run_local_server(port=0)

        # Save credentials
        os.makedirs(self.CREDENTIALS_DIR, exist_ok=True)
        token_path = os.path.join(self.CREDENTIALS_DIR, self.TOKEN_FILE)
        with open(token_path, 'w') as token:
            token.write(credentials.to_json())

        return credentials
```

**Step 4 - GREEN (Test passes):**

Run: `pytest tests/unit/test_gmail_auth.py` → ✅ **PASSES**

**Step 5 - CONFIRM:**

```bash
# Verify implementation
pytest tests/unit/test_gmail_auth.py -v

# Check coverage
pytest --cov=src.gmail_service tests/unit/test_gmail_auth.py

# Expected output:
# src/gmail_service.py    15    0    100%
```

### 1.3 Test Organization

**Standard structure (generated by template):**

```
tests/
├── unit/                      # Isolated unit tests
│   ├── conftest.py           # Shared fixtures
│   ├── test_gmail_service.py # Gmail functionality
│   └── test_notion_client.py # Notion functionality
│
└── integration/               # End-to-end tests
    ├── conftest.py
    └── test_gmail_to_notion_flow.py
```

**Naming conventions:**

```python
# ✅ GOOD
def test_gmail_auth_creates_token_file():
def test_gmail_auth_handles_invalid_credentials():
def test_gmail_auth_refreshes_expired_token():

# ❌ BAD
def test_gmail():              # Too vague
def test_auth_works():         # Not descriptive
def gmail_authentication():    # Missing test_ prefix
```

**When to use unit vs integration tests:**

| Test Type | When to Use | Example |
|-----------|-------------|---------|
| **Unit** | Testing single function/class in isolation | `test_parse_email_subject()` |
| **Integration** | Testing multiple components together | `test_gmail_fetch_and_notion_create()` |
| **E2E** | Testing complete user workflow | `test_full_automation_pipeline()` |

### 1.4 Mocking External APIs Effectively

**Why mock?** Tests should run without internet, API keys, or rate limits.

**Example: Mocking Gmail API Responses**

```python
# tests/unit/test_gmail_service.py
import pytest
from unittest.mock import Mock, patch
from src.gmail_service import GmailService

@pytest.fixture
def mock_gmail_api():
    """Mock Gmail API responses."""
    with patch('googleapiclient.discovery.build') as mock_build:
        mock_service = Mock()
        mock_build.return_value = mock_service

        # Mock messages().list() response
        mock_service.users().messages().list().execute.return_value = {
            'messages': [
                {'id': 'msg_001', 'threadId': 'thread_001'},
                {'id': 'msg_002', 'threadId': 'thread_002'},
            ]
        }

        # Mock messages().get() response
        mock_service.users().messages().get().execute.return_value = {
            'id': 'msg_001',
            'payload': {
                'headers': [
                    {'name': 'From', 'value': 'sender@example.com'},
                    {'name': 'Subject', 'value': 'Test Email'},
                    {'name': 'Date', 'value': 'Mon, 1 Jan 2025 12:00:00 +0000'},
                ]
            }
        }

        yield mock_service

def test_fetch_unread_emails(mock_gmail_api):
    """Test fetching unread emails from Gmail."""
    service = GmailService()
    emails = service.fetch_unread_emails()

    assert len(emails) == 2
    assert emails[0]['id'] == 'msg_001'
    assert emails[0]['subject'] == 'Test Email'
```

**Best practices for mocking:**

1. **Mock at the boundary** - Mock external libraries, not your own code
2. **Use realistic test data** - Mock responses should match actual API format
3. **Test error cases** - Mock API errors (404, 500, timeout)

```python
# Test error handling
def test_gmail_handles_api_timeout(mock_gmail_api):
    mock_gmail_api.users().messages().list().execute.side_effect = TimeoutError()

    service = GmailService()
    with pytest.raises(GmailAPIError, match="API timeout"):
        service.fetch_unread_emails()
```

### 1.5 Coverage Strategies

**Aim for 100% coverage, but coverage ≠ quality.**

**Check coverage:**

```bash
# Run tests with coverage report
pytest --cov=src --cov-report=term-missing tests/

# Output:
# Name                    Stmts   Miss  Cover   Missing
# ------------------------------------------------------
# src/gmail_service.py       45      2    96%   78-79
# src/notion_client.py       38      0   100%
# ------------------------------------------------------
# TOTAL                      83      2    98%
```

**What to test (priority order):**

1. **Happy path** - Normal, expected usage
2. **Edge cases** - Empty inputs, max values, boundaries
3. **Error cases** - Invalid inputs, API failures, timeouts
4. **Security** - Authentication failures, unauthorized access

**Example: Comprehensive test suite**

```python
# tests/unit/test_notion_client.py

def test_create_page_with_valid_data(notion_client):
    """Test creating Notion page with all required fields."""
    # Happy path
    page = notion_client.create_page(
        title="Test Page",
        content="Test content",
        tags=["automation"]
    )
    assert page['id'] is not None

def test_create_page_with_empty_title(notion_client):
    """Test creating page with empty title (edge case)."""
    with pytest.raises(ValueError, match="Title cannot be empty"):
        notion_client.create_page(title="", content="Content")

def test_create_page_with_unicode_characters(notion_client):
    """Test creating page with Unicode content (edge case)."""
    page = notion_client.create_page(
        title="测试页面",  # Chinese characters
        content="Emoji test: 🎉✨"
    )
    assert page['properties']['title'] == "测试页面"

def test_create_page_api_rate_limit(notion_client, mock_notion_api):
    """Test handling Notion API rate limit (error case)."""
    mock_notion_api.pages.create.side_effect = RateLimitError()

    with pytest.raises(NotionAPIError, match="Rate limit exceeded"):
        notion_client.create_page(title="Test", content="Test")
```

**Coverage != Quality:**

```python
# ❌ 100% coverage but bad test
def test_email_parser():
    parser = EmailParser()
    result = parser.parse("test@example.com")
    assert result is not None  # This tells us NOTHING

# ✅ Good test
def test_email_parser_extracts_username_and_domain():
    parser = EmailParser()
    result = parser.parse("user@example.com")

    assert result['username'] == "user"
    assert result['domain'] == "example.com"
    assert result['is_valid'] is True
```

---

## 2. Checkpoint Strategies

### 2.1 Understanding Checkpoint Purpose

**The Error Impact Hierarchy:**

```
Research Error (CHECKPOINT 1)  → 1,000+ bad lines of code
Planning Error (CHECKPOINT 2)  → 10-100 bad lines of code
Implementation Error           → 1 bad line of code
```

**ROI of catching errors early:**

- **CHECKPOINT 1 (Research):** ROI = **100x** (1 minute review saves 100 minutes implementation)
- **CHECKPOINT 2 (Planning):** ROI = **10-20x** (5 minute review saves 50-100 minutes coding)

**Why checkpoints exist:**
- Prevent building on wrong foundation
- Validate assumptions before heavy implementation
- Give you control over project direction
- Surface misunderstandings early

### 2.2 CHECKPOINT 1 Deep Dive (Research Phase)

**Presented after Phase 2 - typically contains:**

```markdown
## 🔍 CHECKPOINT 1: Research Validation

**Goal:** [Your original goal description]

**APIs Identified:**
1. Gmail API (v1)
   - Scopes: gmail.readonly, gmail.modify
   - Authentication: OAuth2
   - Rate Limits: 250 requests/second/user

2. Notion API (v2023-10-31)
   - Authentication: Internal Integration token
   - Rate Limits: 3 requests/second

**Complexity Assessment:** MEDIUM
- Reason: 2 APIs, OAuth flow, scheduled automation

**Tech Stack:**
- Python 3.11
- Libraries: google-api-python-client, notion-client
- Scheduling: APScheduler

**Ready to proceed with planning?**
Respond: approve | fix: [changes needed] | restart
```

**What to look for (checklist):**

✅ **API Correctness:**
- [ ] Are these the RIGHT APIs for your goal? (not generic/vague)
- [ ] Are API versions specified?
- [ ] Are rate limits reasonable for your use case?
- [ ] Are authentication methods clear?

✅ **Complexity Validation:**
- [ ] Does SIMPLE/MEDIUM/HIGH match your expectation?
- [ ] Are you comfortable with this complexity level?

✅ **Tech Stack Review:**
- [ ] Do you know/can learn these libraries?
- [ ] Is Python the right choice? (vs Node.js, etc.)
- [ ] Are there obvious missing dependencies?

**Common red flags:**

🚩 **Generic API names:**
```
❌ "Generic Email API"       → Should be "Gmail API v1"
❌ "Database API"            → Should be "PostgreSQL" or "MongoDB"
❌ "Notification Service"    → Should be "Slack API" or "Twilio SMS API"
```

🚩 **Vague authentication:**
```
❌ "API key required"        → Should specify OAuth2/token/basic auth
❌ "Login needed"            → Not descriptive enough
```

🚩 **Missing credential info:**
```
❌ No mention of where to get API keys
❌ No mention of setup steps (OAuth consent screen, etc.)
```

**Example responses:**

**✅ APPROVE (everything looks good):**
```
approve: APIs verified (Gmail v1 + Notion v2 are correct),
MEDIUM complexity is appropriate for OAuth + 2 APIs,
tech stack looks good. Proceed with planning.
```

**✅ FIX (specific changes needed):**
```
fix: Use Gmail API instead of generic "email API".
Add Notion API v2 (not v1) for creating pages.
Change complexity to HIGH because we also need Slack
notifications on errors (3rd API not mentioned).
```

**✅ RESTART (major issues, need to rethink):**
```
restart: Goal was unclear. I actually want to sync
Outlook (not Gmail) to Airtable (not Notion).
Let's start over with correct requirements.
```

### 2.3 CHECKPOINT 2 Deep Dive (Planning Phase)

**Presented after Phase 7 - typically contains:**

```markdown
## 📋 CHECKPOINT 2: Planning Validation

**Project Structure:**
```
gmail-notion-sync/
├── src/
│   ├── gmail_service.py
│   ├── notion_client.py
│   ├── email_processor.py
│   └── scheduler.py
├── tests/
│   ├── unit/
│   └── integration/
└── config/
    └── settings.py
```

**Test Plan (TDD):**
1. test_gmail_auth_creates_token() - Gmail OAuth
2. test_fetch_unread_emails() - Fetch logic
3. test_parse_email_metadata() - Parsing
4. test_notion_create_page() - Notion API
5. test_email_to_notion_transformation() - Integration
6. test_scheduler_runs_every_15min() - Scheduling

**Error Handling:**
- Gmail API errors: Retry with exponential backoff (3 attempts)
- Notion API errors: Log and skip email, continue processing
- Network timeouts: 30s timeout, retry once
- Invalid email format: Log warning, skip

**Async Considerations:**
- Sequential processing (one email at a time)
- Reason: Notion API rate limit (3 req/s)

Ready to proceed with TDD implementation?
Respond: approve | fix: [changes needed] | back to research
```

**What to look for (checklist):**

✅ **Architecture Soundness:**
- [ ] Are modules clearly separated by responsibility?
- [ ] Is there a clear data flow? (input → process → output)
- [ ] Are there obvious missing components?

✅ **Test Plan Completeness:**
- [ ] Does every major feature have a test?
- [ ] Are integration tests included?
- [ ] Are error cases covered?

✅ **Error Handling:**
- [ ] Is retry logic specified for API failures?
- [ ] Are timeouts defined?
- [ ] What happens when external service is down?

✅ **Scope Validation:**
- [ ] Is this still aligned with your original goal?
- [ ] Any scope creep? (features you didn't ask for)
- [ ] Any missing features? (things you need but weren't planned)

**Common red flags:**

🚩 **Missing error handling:**
```
❌ No mention of what happens on API failure
❌ No retry logic for network issues
❌ No handling of invalid data
```

🚩 **Vague async approach:**
```
❌ "Will handle concurrency" → How? ThreadPoolExecutor? asyncio?
❌ No consideration of rate limits
```

🚩 **Incomplete test plan:**
```
❌ Only happy path tests listed
❌ No integration tests
❌ Missing tests for critical features
```

**Example responses:**

**✅ APPROVE (planning is solid):**
```
approve: Architecture looks clean with clear separation,
test plan covers all features including error cases,
error handling strategy is appropriate. Ready for TDD.
```

**✅ FIX (specific improvements needed):**
```
fix: Add error_handler.py module for centralized
error handling. Include test for OAuth token refresh
(missing from test plan). Add async processing using
asyncio instead of sequential - Notion rate limit is
3 req/s so we can process 3 emails concurrently.
```

**✅ BACK TO RESEARCH (major scope change):**
```
back to research: I actually need to support multiple
Gmail accounts (not just one), which changes the API
requirements significantly. Need to re-evaluate
complexity and authentication approach.
```

### 2.4 Response Format Best Practices

**DO:**
- ✅ Be specific about what's wrong and what you want
- ✅ Reference specific items (API names, module names, test names)
- ✅ Explain WHY when fixing (helps AI learn)
- ✅ Use `approve:`, `fix:`, `restart:`, `back to research:` prefixes

**DON'T:**
- ❌ Just say "looks good" (validate specific points instead)
- ❌ Make vague requests like "improve this"
- ❌ Assume the AI knows what you meant
- ❌ Skip checkpoints thinking "I'll catch errors later"

**Examples - Good vs Bad:**

**❌ BAD:**
```
"Looks good"                    → Not validating anything
"Fix the APIs"                  → Which APIs? What's wrong?
"This won't work"               → Why not? What should change?
"approve I think"               → Uncertainty = need to review more
```

**✅ GOOD:**
```
"approve: Gmail API v1 verified at developers.google.com/gmail,
Notion API v2 matches current docs, MEDIUM complexity appropriate."

"fix: Change from Slack API to Discord webhook (simpler auth).
Add rate limiting to 10 requests/min on our side to avoid hitting
Notion's 3 req/s limit."

"restart: Scope changed - need to process PDFs not emails.
Gmail API not needed, should use Google Drive API instead."
```

---

## 3. Template Customization

### 3.1 Understanding the Template System

**Three-tier architecture:**

```
.claude/templates/
├── base/          # SIMPLE complexity (11 templates)
│   ├── README.md.j2
│   ├── src/
│   ├── tests/
│   └── ...
│
├── medium/        # MEDIUM complexity (extends base + 2 new)
│   ├── orchestrator/
│   └── ...
│
└── high/          # HIGH complexity (extends medium + 1 new)
    ├── @self-improve.md
    └── ...
```

**Template variables (26+ available):**

All templates use Jinja2 syntax: `{{ variable_name }}`

**Conditional logic:**

```jinja2
{% if complexity == "MEDIUM" or complexity == "HIGH" %}
# This section only appears in MEDIUM/HIGH projects
{% endif %}

{% if "gmail" in apis_list|lower %}
# This appears only if Gmail API is detected
{% endif %}
```

**Template inheritance (Jinja2):**

```jinja2
{# medium/README.md.j2 extends base/README.md.j2 #}
{% extends "base/README.md.j2" %}

{% block additional_sections %}
## Orchestrator Usage
The orchestrator/ directory contains...
{% endblock %}
```

### 3.2 Available Template Variables

**Core variables (always available):**

| Variable | Example Value | Source |
|----------|--------------|--------|
| `{{ project_name }}` | `gmail_notion_sync` | Derived from goal |
| `{{ goal_description }}` | `Automate Gmail to Notion sync` | User input |
| `{{ complexity_level }}` | `MEDIUM` | Orchestrator analysis |
| `{{ creation_date }}` | `2025-01-03` | Timestamp |
| `{{ template_version }}` | `3.0.0` | From CHANGELOG.md |

**API-related variables:**

| Variable | Example Value | Source |
|----------|--------------|--------|
| `{{ apis_list }}` | `['Gmail API', 'Notion API']` | IntentAnalyzer |
| `{{ primary_api }}` | `Gmail API v1` | First in list |
| `{{ api_count }}` | `2` | len(apis_list) |
| `{{ auth_methods }}` | `{'gmail': 'OAuth2', 'notion': 'Token'}` | API research |

**Tech stack variables:**

| Variable | Example Value | Source |
|----------|--------------|--------|
| `{{ python_version }}` | `3.11` | Requirements |
| `{{ tech_stack }}` | `['FastAPI', 'SQLAlchemy']` | Orchestrator |
| `{{ dependencies }}` | `['google-api-python-client', ...]` | requirements.txt |
| `{{ framework }}` | `FastAPI` or `None` | If web API detected |

**Project structure variables:**

| Variable | Example Value | Source |
|----------|--------------|--------|
| `{{ modules_list }}` | `['gmail_service', 'notion_client']` | Planning phase |
| `{{ test_count }}` | `12` | Test plan |
| `{{ has_database }}` | `True` or `False` | Architecture analysis |
| `{{ schedule_type }}` | `cron` or `continuous` or `None` | Automation type |

**Metadata variables:**

| Variable | Example Value | Source |
|----------|--------------|--------|
| `{{ author_name }}` | From git config or ENV |
| `{{ project_description }}` | First sentence of goal |
| `{{ license }}` | `MIT` (default) |
| `{{ repository_url }}` | From git remote or empty |

**Example template using variables:**

```jinja2
{# .claude/templates/base/README.md.j2 #}
# {{ project_name }}

> {{ project_description }}

**Created:** {{ creation_date }}
**Complexity:** {{ complexity_level }}
**Template Version:** {{ template_version }}

## APIs Used

{% for api in apis_list %}
- {{ api }}
  {% if auth_methods[api|lower] %}
  - Authentication: {{ auth_methods[api|lower] }}
  {% endif %}
{% endfor %}

## Tech Stack

- Python {{ python_version }}
{% for tech in tech_stack %}
- {{ tech }}
{% endfor %}

{% if complexity == "MEDIUM" or complexity == "HIGH" %}
## Orchestrator

This project includes the Orchestrator SDK for advanced automation.

See `orchestrator/README.md` for usage.
{% endif %}
```

### 3.3 Adding Custom Variables

**Example: Adding `{{ database_type }}` variable**

**Step 1: Add to Pydantic model**

```python
# orchestrator/models.py
from pydantic import BaseModel, Field
from typing import Optional

class AutomationIntent(BaseModel):
    """Structured representation of user's automation goal."""

    # ... existing fields ...

    # Add new field
    database_type: Optional[str] = Field(
        default=None,
        description="Type of database if detected: postgresql, mongodb, sqlite, etc."
    )
```

**Step 2: Populate in IntentAnalyzer**

```python
# orchestrator/intent_analyzer.py
class IntentAnalyzer:
    def analyze_intent(self, goal: str) -> AutomationIntent:
        """Analyze user goal and extract structured intent."""

        # ... existing analysis ...

        # Detect database type
        database_type = self._detect_database(goal)

        return AutomationIntent(
            # ... existing fields ...
            database_type=database_type
        )

    def _detect_database(self, goal: str) -> Optional[str]:
        """Detect database type from goal description."""
        goal_lower = goal.lower()

        if 'postgresql' in goal_lower or 'postgres' in goal_lower:
            return 'postgresql'
        elif 'mongodb' in goal_lower or 'mongo' in goal_lower:
            return 'mongodb'
        elif 'sqlite' in goal_lower:
            return 'sqlite'
        elif 'mysql' in goal_lower:
            return 'mysql'

        # Check for generic "database" mention
        if 'database' in goal_lower or 'db' in goal_lower:
            return 'generic'  # Will prompt user to specify

        return None
```

**Step 3: Use in template**

```jinja2
{# .claude/templates/base/README.md.j2 #}

{% if database_type %}
## Database

This project uses **{{ database_type|upper }}**.

{% if database_type == "postgresql" %}
### PostgreSQL Setup

```bash
# Install PostgreSQL
brew install postgresql  # macOS
sudo apt install postgresql  # Ubuntu

# Start service
brew services start postgresql  # macOS
sudo systemctl start postgresql  # Ubuntu
```

{% elif database_type == "mongodb" %}
### MongoDB Setup

```bash
# Install MongoDB
brew tap mongodb/brew
brew install mongodb-community

# Start service
brew services start mongodb-community
```

{% elif database_type == "sqlite" %}
### SQLite

No installation needed - SQLite is included with Python.

{% endif %}
{% endif %}
```

**Step 4: Test the new variable**

```python
# tests/unit/test_intent_analyzer.py

def test_detect_postgresql_from_goal():
    """Test detecting PostgreSQL from goal description."""
    analyzer = IntentAnalyzer()

    goal = "Create a REST API with PostgreSQL database for storing user data"
    intent = analyzer.analyze_intent(goal)

    assert intent.database_type == "postgresql"

def test_detect_mongodb_from_goal():
    """Test detecting MongoDB from goal description."""
    analyzer = IntentAnalyzer()

    goal = "Build analytics dashboard with MongoDB backend"
    intent = analyzer.analyze_intent(goal)

    assert intent.database_type == "mongodb"

def test_no_database_detected():
    """Test when no database is mentioned."""
    analyzer = IntentAnalyzer()

    goal = "Automate email sending with SendGrid"
    intent = analyzer.analyze_intent(goal)

    assert intent.database_type is None
```

### 3.4 Modifying Base Templates

**Location:** `.claude/templates/base/`

**Example: Customizing README.md.j2 to add a "Deployment" section**

**Original template (simplified):**

```jinja2
# {{ project_name }}

## Quick Start

...

## Running the Project

...

## Testing

...
```

**Modified template:**

```jinja2
# {{ project_name }}

## Quick Start

...

## Running the Project

...

## Testing

...

## Deployment

### Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
{% for api in apis_list %}
{{ api|upper|replace(' ', '_') }}_API_KEY=your_{{ api|lower|replace(' ', '_') }}_key
{% endfor %}
```

### Production Deployment

**Option 1: Docker**

```bash
docker build -t {{ project_name }} .
docker run -d --env-file .env {{ project_name }}
```

**Option 2: systemd (Linux)**

Create `/etc/systemd/system/{{ project_name }}.service`:

```ini
[Unit]
Description={{ project_description }}
After=network.target

[Service]
Type=simple
User={{ author_name }}
WorkingDirectory=/opt/{{ project_name }}
ExecStart=/usr/bin/python3 src/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable {{ project_name }}
sudo systemctl start {{ project_name }}
```

{% if schedule_type == "cron" %}
**Option 3: Cron Job**

```bash
# Run every 15 minutes
*/15 * * * * cd /opt/{{ project_name }} && /usr/bin/python3 src/main.py
```
{% endif %}
```

**Result:** Every generated project now includes deployment instructions.

### 3.5 Creating Project-Specific Templates

**Use case:** You generate many e-commerce automation projects and want specialized templates.

**Step 1: Create new template directory**

```bash
mkdir -p .claude/templates/ecommerce
```

**Step 2: Create specialized template extending base**

```jinja2
{# .claude/templates/ecommerce/README.md.j2 #}
{% extends "base/README.md.j2" %}

{# Override project description block #}
{% block project_description %}
# {{ project_name }} - E-Commerce Automation

> {{ project_description }}

**E-Commerce Platform:** {{ ecommerce_platform }}
**Payment Gateway:** {{ payment_gateway }}
**Inventory System:** {{ inventory_system }}
{% endblock %}

{# Add e-commerce specific sections #}
{% block additional_sections %}
## E-Commerce Integration

### {{ ecommerce_platform }} Setup

{% if ecommerce_platform == "Shopify" %}
1. Create private app in Shopify admin
2. Copy API key and password
3. Set `SHOPIFY_API_KEY` and `SHOPIFY_PASSWORD` in `.env`
{% elif ecommerce_platform == "WooCommerce" %}
1. Install WooCommerce REST API plugin
2. Generate consumer key and secret
3. Set `WC_CONSUMER_KEY` and `WC_CONSUMER_SECRET` in `.env`
{% endif %}

### Payment Processing

This project integrates with **{{ payment_gateway }}** for payment processing.

Security considerations:
- ✅ PCI DSS compliance required
- ✅ Use webhooks for payment confirmation
- ✅ Never log full credit card numbers
- ✅ Implement idempotency for payment requests

{% endblock %}
```

**Step 3: Configure orchestrator to use custom template**

```python
# orchestrator/project_generator.py
class ProjectGenerator:
    def select_template_tier(self, intent: AutomationIntent) -> str:
        """Select template tier based on project analysis."""

        # Check for e-commerce keywords
        ecommerce_keywords = ['shopify', 'woocommerce', 'magento', 'payment', 'inventory', 'order']
        if any(keyword in intent.goal_description.lower() for keyword in ecommerce_keywords):
            return 'ecommerce'  # Use custom template

        # Default logic
        if intent.complexity_level == "SIMPLE":
            return 'base'
        elif intent.complexity_level == "MEDIUM":
            return 'medium'
        else:
            return 'high'
```

**Step 4: Add e-commerce specific variables to AutomationIntent**

```python
# orchestrator/models.py
class AutomationIntent(BaseModel):
    # ... existing fields ...

    # E-commerce specific
    ecommerce_platform: Optional[str] = None  # Shopify, WooCommerce, etc.
    payment_gateway: Optional[str] = None     # Stripe, PayPal, etc.
    inventory_system: Optional[str] = None    # Internal, TradeGecko, etc.
```

**Result:** When you create a project with e-commerce keywords, it uses the specialized template with payment gateway instructions, PCI compliance notes, etc.

---

## 4. Orchestrator Extension

### 4.1 Understanding Orchestrator Architecture

**Components:**

```
orchestrator/
├── agent.py                  # Main orchestrator agent
├── models.py                 # Pydantic models (AutomationIntent, etc.)
├── intent_analyzer.py        # Goal analysis logic
├── memory.py                 # Memory management
├── project_generator.py      # Template rendering
├── subagent_manager.py       # Manages specialized agents
└── custom_tools.py           # MCP tools (optional)
```

**Data flow:**

```
User Goal
    ↓
IntentAnalyzer → AutomationIntent (Pydantic model)
    ↓
SubagentManager → Parallel analysis (@sequential-thinking, @library-researcher)
    ↓
MemoryManager → Retrieve relevant patterns
    ↓
ProjectGenerator → Render templates with variables
    ↓
Generated Project
```

**When to extend vs fork:**

| Extend (customize) | Fork (separate repo) |
|-------------------|----------------------|
| Add project-specific variables | Fundamentally different architecture |
| Add new subagents | Different programming language |
| Customize templates | Different LLM provider |
| Add memory categories | Commercial product |

### 4.2 Adding Custom Subagents

**Example: Creating `@database-schema-analyzer` subagent**

**Step 1: Create subagent markdown file**

```bash
touch .claude/agents/database-schema-analyzer.md
```

**Step 2: Define subagent behavior**

```markdown
<!-- .claude/agents/database-schema-analyzer.md -->
# @database-schema-analyzer

**Specialized Agent:** Database Schema Analysis and Optimization

## Expertise

- Database schema design (normalized vs denormalized)
- Index optimization strategies
- Migration planning
- Data modeling for common use cases

## When to Use

Use this agent when:
- Project involves database design
- Need to analyze schema for performance
- Planning migrations or schema changes
- Choosing between SQL vs NoSQL

## Tools Available

- Serena MCP (code analysis)
- Sequential thinking (complex schema decisions)
- Web search (database best practices)

## Instructions

When invoked, you should:

1. Analyze the project goal for data requirements
2. Identify entities and relationships
3. Propose normalized schema (SQL) or document structure (NoSQL)
4. Suggest indexes for common queries
5. Identify potential performance bottlenecks
6. Provide migration strategy if modifying existing schema

## Output Format

Return JSON:

```json
{
  "database_type": "postgresql" | "mongodb" | "sqlite",
  "schema": {
    "tables": [ /* for SQL */ ],
    "collections": [ /* for NoSQL */ ]
  },
  "indexes": [
    {"table": "users", "columns": ["email"], "type": "unique"}
  ],
  "migrations": [
    "CREATE TABLE users (...)",
    "CREATE INDEX idx_users_email ..."
  ]
}
```

## Examples

**Example 1: User authentication system**

Input: "Build user authentication with email/password"

Output:
```json
{
  "database_type": "postgresql",
  "schema": {
    "tables": [
      {
        "name": "users",
        "columns": [
          {"name": "id", "type": "SERIAL PRIMARY KEY"},
          {"name": "email", "type": "VARCHAR(255) UNIQUE NOT NULL"},
          {"name": "password_hash", "type": "VARCHAR(255) NOT NULL"},
          {"name": "created_at", "type": "TIMESTAMP DEFAULT NOW()"}
        ]
      }
    ]
  },
  "indexes": [
    {"table": "users", "columns": ["email"], "type": "unique"}
  ]
}
```
```

**Step 3: Register in SubagentManager**

```python
# orchestrator/subagent_manager.py
class SubagentManager:
    def __init__(self):
        self.available_agents = {
            'sequential-thinking': 'mcp__server-sequential-thinking__sequentialthinking',
            'library-researcher': '@library-researcher',
            'codebase-analyst': '@codebase-analyst',

            # Add new subagent
            'database-schema-analyzer': '@database-schema-analyzer',
        }

    async def analyze_with_agents(self, intent: AutomationIntent) -> Dict:
        """Run parallel analysis with specialized agents."""

        tasks = []

        # Always run sequential thinking
        tasks.append(self.run_agent('sequential-thinking', intent))

        # Conditional agents based on project type
        if intent.has_database:  # ← Check if database detected
            tasks.append(self.run_agent('database-schema-analyzer', intent))

        if intent.api_count > 0:
            tasks.append(self.run_agent('library-researcher', intent))

        results = await asyncio.gather(*tasks)
        return self.merge_results(results)
```

**Step 4: Use subagent output in templates**

```jinja2
{# .claude/templates/base/database/schema.sql.j2 #}
{% if database_schema %}
-- Generated by @database-schema-analyzer
-- Database: {{ database_type }}

{% for table in database_schema.tables %}
CREATE TABLE {{ table.name }} (
{% for column in table.columns %}
    {{ column.name }} {{ column.type }}{% if not loop.last %},{% endif %}
{% endfor %}
);

{% endfor %}

-- Indexes
{% for index in database_indexes %}
CREATE {% if index.type == 'unique' %}UNIQUE {% endif %}INDEX {{ index.name }}
ON {{ index.table }} ({{ index.columns|join(', ') }});
{% endfor %}
{% endif %}
```

### 4.3 Extending IntentAnalyzer

**Example: Detecting performance requirements**

**Step 1: Add field to AutomationIntent**

```python
# orchestrator/models.py
from typing import Optional, Dict

class PerformanceRequirements(BaseModel):
    """Performance and scalability requirements."""
    requests_per_second: Optional[int] = None
    concurrent_users: Optional[int] = None
    data_volume: Optional[str] = None  # "small" | "medium" | "large"
    latency_requirement: Optional[str] = None  # "real-time" | "async" | "batch"

class AutomationIntent(BaseModel):
    # ... existing fields ...

    performance: Optional[PerformanceRequirements] = None
```

**Step 2: Add detection logic to IntentAnalyzer**

```python
# orchestrator/intent_analyzer.py
class IntentAnalyzer:
    def analyze_intent(self, goal: str) -> AutomationIntent:
        """Analyze user goal and extract structured intent."""

        # ... existing analysis ...

        # Detect performance requirements
        performance = self._analyze_performance_requirements(goal)

        return AutomationIntent(
            # ... existing fields ...
            performance=performance
        )

    def _analyze_performance_requirements(self, goal: str) -> PerformanceRequirements:
        """Detect performance and scale requirements from goal."""
        perf = PerformanceRequirements()
        goal_lower = goal.lower()

        # Detect throughput requirements
        import re
        rps_match = re.search(r'(\d+)\s*(requests?|req).*per\s*second', goal_lower)
        if rps_match:
            perf.requests_per_second = int(rps_match.group(1))

        # Detect concurrency
        concurrent_match = re.search(r'(\d+)\s*concurrent\s*users?', goal_lower)
        if concurrent_match:
            perf.concurrent_users = int(concurrent_match.group(1))

        # Detect latency requirements
        if any(word in goal_lower for word in ['real-time', 'realtime', 'instant', 'immediate']):
            perf.latency_requirement = "real-time"
        elif any(word in goal_lower for word in ['async', 'asynchronous', 'background']):
            perf.latency_requirement = "async"
        elif any(word in goal_lower for word in ['batch', 'nightly', 'scheduled']):
            perf.latency_requirement = "batch"

        # Detect data volume
        if any(word in goal_lower for word in ['millions', 'tb', 'petabyte', 'big data']):
            perf.data_volume = "large"
        elif any(word in goal_lower for word in ['thousands', 'gb', 'gigabyte']):
            perf.data_volume = "medium"
        else:
            perf.data_volume = "small"

        return perf
```

**Step 3: Use in project generation**

```python
# orchestrator/project_generator.py
class ProjectGenerator:
    def select_architecture(self, intent: AutomationIntent) -> str:
        """Select architecture pattern based on requirements."""

        if intent.performance:
            perf = intent.performance

            # High throughput → Use async architecture
            if perf.requests_per_second and perf.requests_per_second > 100:
                return "async_workers"

            # Real-time latency → Use FastAPI + WebSockets
            if perf.latency_requirement == "real-time":
                return "realtime_api"

            # Large data → Use batch processing
            if perf.data_volume == "large":
                return "batch_etl"

        return "standard"
```

### 4.4 Memory System Customization

**Example: Adding `performance_benchmarks.json` memory**

**Step 1: Define new memory structure**

```python
# orchestrator/memory.py
class MemoryManager:
    def __init__(self, memory_dir: str = ".claude/memories"):
        self.memory_dir = Path(memory_dir)
        self.memory_files = {
            'architectural_decisions': 'architectural_decisions.json',
            'patterns': 'patterns.json',
            'learnings': 'learnings.json',
            'api_integrations': 'api_integrations.json',

            # Add new memory
            'performance_benchmarks': 'performance_benchmarks.json',
        }
```

**Step 2: Add store/retrieve methods**

```python
# orchestrator/memory.py
class MemoryManager:
    # ... existing methods ...

    def store_performance_benchmark(
        self,
        project_name: str,
        metric_name: str,
        value: float,
        context: Dict
    ):
        """Store performance benchmark result."""
        benchmarks = self.get_memory('performance_benchmarks') or []

        benchmarks.append({
            'timestamp': datetime.now().isoformat(),
            'project': project_name,
            'metric': metric_name,
            'value': value,
            'context': context,
        })

        self.save_memory('performance_benchmarks', benchmarks)

    def get_performance_benchmarks(
        self,
        metric_name: Optional[str] = None,
        project_name: Optional[str] = None
    ) -> List[Dict]:
        """Retrieve performance benchmarks with optional filtering."""
        benchmarks = self.get_memory('performance_benchmarks') or []

        if metric_name:
            benchmarks = [b for b in benchmarks if b['metric'] == metric_name]

        if project_name:
            benchmarks = [b for b in benchmarks if b['project'] == project_name]

        return benchmarks
```

**Step 3: Use in project generation**

```python
# In @project-initializer agent (Phase 3: Planning)

# Store benchmark from similar project
memory.store_performance_benchmark(
    project_name="gmail-notion-sync",
    metric_name="emails_processed_per_minute",
    value=120.5,
    context={
        "api_count": 2,
        "complexity": "MEDIUM",
        "async_enabled": True
    }
)

# Retrieve benchmarks for performance estimation
similar_benchmarks = memory.get_performance_benchmarks(
    metric_name="emails_processed_per_minute"
)

if similar_benchmarks:
    avg_rate = sum(b['value'] for b in similar_benchmarks) / len(similar_benchmarks)
    print(f"Expected processing rate: ~{avg_rate:.1f} emails/min based on {len(similar_benchmarks)} similar projects")
```

---

## 5. Context Engineering Tips

### 5.1 Context Window Management

**Target: <50% context window capacity**

**Why it matters:**
- LLMs perform better with more "thinking room"
- Reduces hallucinations
- Faster response times
- Lower API costs

**What counts toward context:**

```
Context Window Usage:
├─ 30%: System instructions (.claude/agents/project-initializer.md)
├─ 15%: Goal description + research results
├─ 10%: Memory retrieval (patterns, API docs)
├─ 5%:  Template metadata
└─ 40%: AVAILABLE for thinking and generation ← Goal
```

**How to measure:**

Currently not automated. Manual observation during Phase 0-2:

```
If you see:
- Agent repeating itself → Context likely >70%
- Generic responses instead of specific → Context >60%
- Forgetting earlier context → Context >80%

Then: Simplify goal or break into phases
```

**Future improvement:** Add context token counter tool.

### 5.2 Writing Effective Goal Descriptions

**Good goal formula:**

```
[ACTION] + [SOURCE] + [DESTINATION] + [SCHEDULE] + [SPECIFICS]

Example:
"Sync unread emails from Gmail to Notion database every 15 minutes.
Extract: sender email, subject, date, body preview (first 200 chars).
Create new page in 'Inbox' database with properties mapped.
Mark email as read in Gmail after successful Notion creation."
```

**Key elements:**

1. **ACTION**: What to do (sync, automate, process, generate, etc.)
2. **SOURCE**: Where data comes from (Gmail, database, API, file, etc.)
3. **DESTINATION**: Where data goes (Notion, Slack, database, file, etc.)
4. **SCHEDULE**: When/how often (real-time, every 15 min, on trigger, manual)
5. **SPECIFICS**: Important details (which fields, error handling, filters)

**Examples - Good vs Bad:**

**❌ BAD (too vague):**
```
"Email automation"
→ Problems: What email system? What should be automated? What's the trigger?

"Notion integration"
→ Problems: Integrate with what? For what purpose?

"Process data from API"
→ Problems: Which API? What processing? Where does output go?
```

**✅ GOOD (specific):**
```
"Fetch weather data from OpenWeatherMap API for San Francisco
every hour. Store temperature, humidity, conditions in PostgreSQL.
Send Slack alert if temperature drops below 50°F."
→ Clear: API, location, schedule, storage, action

"Monitor GitHub issues in repo 'myorg/myrepo' for label 'urgent'.
Every 5 minutes, check for new issues. Post to Slack #alerts channel
with issue title, link, author. Track processed issues in SQLite to avoid duplicates."
→ Clear: Source, filter criteria, schedule, destination, deduplication

"Extract invoices from Gmail attachments (PDF only, subject contains 'Invoice').
Parse: invoice number, date, total amount using OCR. Create record in Airtable
'Invoices' table. Move email to 'Processed' label in Gmail."
→ Clear: Source + filter, processing steps, output format, cleanup action
```

**Length sweet spot: 2-5 sentences (30-150 words)**

Too short (<30 words) → Vague, requires guessing
Too long (>150 words) → Context heavy, likely too complex for one project

### 5.3 Simplification Strategies

**When to break into phases:**

```
🚩 Single project too large if:
- Goal description >150 words
- More than 3 APIs
- Multiple distinct workflows
- Estimated >15 tests needed
- Context window >50% during research
```

**Example: Large project → Phased approach**

**❌ Too Large (single project):**
```
"Build complete e-commerce platform: User registration with email verification,
product catalog with search, shopping cart, Stripe payment processing,
order management, inventory tracking, email notifications for orders,
admin dashboard for analytics, CSV export of sales data, integration
with Shopify for inventory sync."

→ 10+ features, 5+ APIs, easily >50 tests
```

**✅ Phase 1 (Start here):**
```
"Build product catalog API with PostgreSQL. Endpoints:
GET /products (with search), GET /products/:id, POST /products (admin only).
Include: name, description, price, stock_quantity, images.
Basic auth with JWT. Return JSON."

→ Complexity: MEDIUM
→ Estimated: 8-10 tests
→ 1 week implementation
```

**✅ Phase 2 (Next project):**
```
"Add shopping cart to existing product catalog (from Phase 1).
Endpoints: POST /cart/add, GET /cart, DELETE /cart/:item, POST /cart/checkout.
Store cart in Redis (session-based). Calculate totals, apply discount codes.
Integrate with existing JWT auth."

→ Builds on Phase 1 codebase
→ Estimated: 6-8 tests
→ 3-4 days implementation
```

**✅ Phase 3 (After Phase 2 works):**
```
"Add Stripe payment processing to cart checkout (from Phase 2).
Create Stripe customer on first purchase, save payment method.
POST /checkout/pay endpoint. Handle success/failure webhooks.
Send order confirmation email via SendGrid. Store orders in PostgreSQL."

→ Builds on Phase 1 + 2
→ Estimated: 10-12 tests (payment edge cases)
→ 1 week implementation
```

**Using memory between phases:**

```python
# At end of Phase 1, store:
memory.store_architectural_decision(
    decision="Product catalog uses PostgreSQL with SQLAlchemy ORM",
    rationale="Need relational data for products with categories",
    project="ecommerce-platform-phase1"
)

memory.store_pattern(
    pattern_name="JWT authentication",
    implementation="Using PyJWT library, tokens expire after 24h",
    file_location="src/auth.py",
    project="ecommerce-platform-phase1"
)

# At start of Phase 2, retrieve:
relevant_context = memory.get_memory_context("ecommerce-platform")
# Returns: Architecture decisions, auth patterns, database schema
# Use this context in Phase 2 goal description
```

### 5.4 Memory Organization Best Practices

**Memory hygiene schedule:**

```
Weekly:  Review memories for current project (are they helping?)
Monthly: Clean up outdated patterns (old library versions, deprecated APIs)
Quarterly: Full memory audit (delete irrelevant projects)
```

**How to review memories:**

```bash
# View all memories
cd /path/to/claude-code-template

# Architectural decisions
cat .claude/memories/architectural_decisions.json | jq '.[] | {project, decision, date}'

# Patterns
cat .claude/memories/patterns.json | jq '.[] | {pattern_name, project, file}'

# API integrations
cat .claude/memories/api_integrations.json | jq '.[] | {api_name, auth_method, project}'

# Learnings
cat .claude/memories/learnings.json | jq '.[] | {learning, impact, date}'
```

**When to clear memories:**

✅ **Clear when:**
- Starting completely new project type (e.g., switching from web APIs to ML pipelines)
- Library versions changed significantly (e.g., Pydantic v1 → v2)
- API deprecated (e.g., Twitter API v1 → v2)
- After 6+ months of inactivity

❌ **Keep when:**
- Similar project types (e.g., all automation projects)
- Architectural patterns still valid (e.g., "use async for high throughput")
- API integrations still current

**Manual memory cleanup:**

```python
# orchestrator/memory.py - Add cleanup method
class MemoryManager:
    def cleanup_old_memories(self, days: int = 180):
        """Remove memories older than specified days."""
        from datetime import datetime, timedelta

        cutoff_date = datetime.now() - timedelta(days=days)

        for memory_type in self.memory_files.keys():
            memories = self.get_memory(memory_type) or []

            # Filter out old memories
            recent_memories = [
                m for m in memories
                if datetime.fromisoformat(m.get('timestamp', '2000-01-01')) > cutoff_date
            ]

            removed_count = len(memories) - len(recent_memories)
            if removed_count > 0:
                self.save_memory(memory_type, recent_memories)
                print(f"Removed {removed_count} old {memory_type} memories")
```

**Best practice: Tag memories by project type**

```python
# When storing memory, add tags
memory.store_pattern(
    pattern_name="Gmail OAuth flow",
    implementation="...",
    tags=["gmail", "oauth", "email-automation", "google-apis"]
)

# Retrieve by tag
email_patterns = memory.get_patterns_by_tag("email-automation")
```

---

## 6. Project Organization

### 6.1 Directory Structure

**Standard structure (from templates):**

```
project-name/
├── src/                       # All source code
│   ├── __init__.py
│   ├── main.py               # Entry point
│   ├── api/                  # If web API
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── services/             # Business logic
│   │   ├── __init__.py
│   │   ├── gmail_service.py
│   │   └── notion_client.py
│   ├── models/               # Data models
│   │   ├── __init__.py
│   │   └── email.py
│   └── utils/                # Helpers
│       ├── __init__.py
│       └── validators.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py           # Shared fixtures
│   ├── unit/
│   │   ├── test_gmail_service.py
│   │   └── test_notion_client.py
│   └── integration/
│       └── test_gmail_to_notion_flow.py
│
├── orchestrator/             # If MEDIUM/HIGH complexity
├── config/                   # Configuration files
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
```

**When to deviate:**

```
FastAPI project:
└── app/
    ├── api/
    │   └── v1/
    │       ├── endpoints/
    │       └── dependencies.py
    ├── core/
    │   ├── config.py
    │   └── security.py
    └── main.py

Django project:
└── myproject/
    ├── myapp/
    │   ├── models.py
    │   ├── views.py
    │   └── urls.py
    └── settings.py
```

### 6.2 Naming Conventions

**Files and directories:**

```python
# ✅ GOOD
gmail_service.py          # snake_case
notion_client.py
email_processor.py
test_gmail_service.py     # test_ prefix

# ❌ BAD
GmailService.py           # PascalCase is for classes, not files
gmail-service.py          # hyphens not standard in Python
gmailService.py           # camelCase not Pythonic
```

**Classes:**

```python
# ✅ GOOD
class GmailService:
class NotionClient:
class EmailProcessor:

# ❌ BAD
class gmail_service:      # snake_case for classes
class Gmail_Service:      # Underscores in class names
```

**Functions and methods:**

```python
# ✅ GOOD
def fetch_unread_emails():
def create_notion_page():
def parse_email_metadata():

# ❌ BAD
def FetchEmails():        # PascalCase
def fetch_Emails():       # Mixed case
def fetchEmails():        # camelCase
```

**Constants:**

```python
# ✅ GOOD
API_TIMEOUT = 30
MAX_RETRIES = 3
GMAIL_SCOPES = ['gmail.readonly']

# ❌ BAD
api_timeout = 30          # Should be uppercase
ApiTimeout = 30           # Not a constant convention
```

**Test files:**

```python
# ✅ GOOD
test_gmail_service.py
test_notion_client.py
test_email_processor.py

def test_fetch_unread_emails():
def test_create_notion_page_with_valid_data():

# ❌ BAD
gmail_test.py             # test_ prefix missing
test_gmail.py             # Too vague
def gmail_test():         # test_ prefix missing
```

### 6.3 Module Separation

**One responsibility per module:**

```python
# ✅ GOOD - Clear separation

# src/services/gmail_service.py
class GmailService:
    """Handles Gmail API interactions."""
    def fetch_unread_emails(self):
        ...

# src/services/notion_client.py
class NotionClient:
    """Handles Notion API interactions."""
    def create_page(self):
        ...

# src/processors/email_processor.py
class EmailProcessor:
    """Transforms email data for Notion."""
    def extract_metadata(self, email):
        ...

# src/utils/validators.py
def validate_email_format(email: str) -> bool:
    """Validates email string format."""
    ...
```

**❌ BAD - Everything in one file:**

```python
# src/main.py (500+ lines)
class GmailService:
    ...

class NotionClient:
    ...

class EmailProcessor:
    ...

def validate_email(email):
    ...

def main():
    ...

# Too many responsibilities in one file!
```

**When to split files (500-line rule from CLAUDE.md):**

```
File approaching 500 lines?

Option 1: Split by class
    main.py (500 lines, 3 classes)
    → gmail_service.py (GmailService, 150 lines)
    → notion_client.py (NotionClient, 150 lines)
    → email_processor.py (EmailProcessor, 200 lines)

Option 2: Split by feature area
    api_routes.py (500 lines, 20 routes)
    → api/user_routes.py (User routes, 150 lines)
    → api/product_routes.py (Product routes, 200 lines)
    → api/order_routes.py (Order routes, 150 lines)

Option 3: Extract helpers
    processor.py (500 lines, main logic + 10 helpers)
    → processor.py (Main logic, 200 lines)
    → utils/validators.py (Validation helpers, 150 lines)
    → utils/transformers.py (Data transformers, 150 lines)
```

**Shared utilities in `src/shared/`:**

```
src/
├── shared/               # Code used by multiple modules
│   ├── __init__.py
│   ├── exceptions.py    # Custom exceptions
│   ├── logger.py        # Logging configuration
│   └── decorators.py    # Shared decorators (retry, cache, etc.)
│
├── services/
│   ├── gmail_service.py  # Uses shared.exceptions, shared.logger
│   └── notion_client.py  # Uses shared.exceptions, shared.decorators
```

---

## 7. Advanced Scenarios

### 7.1 Multi-API Projects

**Example: Gmail + Notion + Slack integration**

**Challenge:** Three APIs with different auth methods, rate limits, error patterns.

**Best practice: API client separation**

```
src/
├── clients/
│   ├── __init__.py
│   ├── base_client.py        # Shared functionality
│   ├── gmail_client.py
│   ├── notion_client.py
│   └── slack_client.py
│
└── services/
    ├── email_service.py       # Uses gmail_client
    ├── database_service.py    # Uses notion_client
    └── notification_service.py # Uses slack_client
```

**Base client pattern:**

```python
# src/clients/base_client.py
import time
from typing import Optional, Dict
from abc import ABC, abstractmethod

class BaseAPIClient(ABC):
    """Base class for all API clients."""

    def __init__(self, api_name: str, rate_limit: Optional[int] = None):
        self.api_name = api_name
        self.rate_limit = rate_limit  # requests per second
        self.last_request_time = 0

    def _rate_limit_check(self):
        """Enforce rate limiting."""
        if self.rate_limit:
            elapsed = time.time() - self.last_request_time
            min_interval = 1.0 / self.rate_limit
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
        self.last_request_time = time.time()

    def _handle_error(self, error: Exception, context: Dict):
        """Centralized error handling."""
        logger.error(f"{self.api_name} error: {error}", extra=context)

        if isinstance(error, RateLimitError):
            # Exponential backoff
            raise
        elif isinstance(error, AuthenticationError):
            # Refresh token
            raise
        else:
            # Generic error
            raise APIError(f"{self.api_name} request failed: {error}")

    @abstractmethod
    def authenticate(self):
        """Implement authentication logic."""
        pass
```

**Gmail client:**

```python
# src/clients/gmail_client.py
from .base_client import BaseAPIClient

class GmailClient(BaseAPIClient):
    def __init__(self):
        super().__init__(api_name="Gmail", rate_limit=250)  # 250 req/s
        self.credentials = None

    def authenticate(self):
        """OAuth2 flow."""
        # Implementation...
        pass
```

**Notion client:**

```python
# src/clients/notion_client.py
from .base_client import BaseAPIClient

class NotionClient(BaseAPIClient):
    def __init__(self, api_key: str):
        super().__init__(api_name="Notion", rate_limit=3)  # 3 req/s
        self.api_key = api_key

    def authenticate(self):
        """Token-based auth."""
        # Implementation...
        pass
```

**Shared authentication strategies:**

```python
# src/shared/auth.py
from typing import Protocol

class AuthStrategy(Protocol):
    """Protocol for authentication strategies."""
    def get_credentials(self) -> Dict:
        ...
    def refresh_if_needed(self) -> bool:
        ...

class OAuth2Strategy:
    """OAuth2 flow (Gmail, Google Drive, etc.)"""
    def get_credentials(self):
        # Implementation...
        pass

class TokenStrategy:
    """API token (Notion, Slack, etc.)"""
    def get_credentials(self):
        return {"token": os.getenv("API_TOKEN")}
```

### 7.2 Complex Orchestration

**When to use @self-improve (HIGH complexity only):**

```
Use @self-improve when:
- Project has 5+ distinct workflow steps
- Steps depend on results of previous steps
- Complex error recovery needed
- Self-optimization based on metrics

Example: ETL pipeline with 5 stages
    Extract → Validate → Transform → Load → Verify
```

**Example: ETL Pipeline**

```python
# orchestrator/workflows/etl_pipeline.py
from typing import Dict, List
import asyncio

class ETLPipeline:
    """Multi-stage data pipeline with self-improvement."""

    def __init__(self):
        self.stages = [
            ExtractStage(),
            ValidateStage(),
            TransformStage(),
            LoadStage(),
            VerifyStage(),
        ]
        self.metrics = MetricsCollector()

    async def run(self, source: str, destination: str) -> Dict:
        """Run pipeline end-to-end."""
        context = {'source': source, 'destination': destination}

        for stage in self.stages:
            try:
                # Run stage with timeout
                result = await asyncio.wait_for(
                    stage.execute(context),
                    timeout=stage.timeout
                )

                # Update context with results
                context.update(result)

                # Collect metrics
                self.metrics.record(stage.name, result['duration'], result['success'])

            except asyncio.TimeoutError:
                # Stage timeout - retry or skip
                if stage.retry_on_timeout:
                    result = await stage.retry(context)
                else:
                    raise PipelineError(f"{stage.name} timed out")

            except Exception as e:
                # Error handling per stage
                if stage.critical:
                    raise  # Fail entire pipeline
                else:
                    # Log and continue
                    logger.warning(f"{stage.name} failed (non-critical): {e}")

        return context

    def optimize(self):
        """Self-improvement based on metrics."""
        bottleneck = self.metrics.find_slowest_stage()

        if bottleneck:
            # Increase resources for slow stage
            self.stages[bottleneck].allocate_more_resources()

        # Adjust timeouts based on historical data
        for stage in self.stages:
            avg_duration = self.metrics.average_duration(stage.name)
            stage.timeout = avg_duration * 1.5  # 50% buffer
```

**State management between steps:**

```python
# src/state/pipeline_state.py
import json
from pathlib import Path

class PipelineState:
    """Persist state between pipeline steps."""

    def __init__(self, pipeline_id: str):
        self.state_file = Path(f".state/{pipeline_id}.json")
        self.state = self._load()

    def _load(self) -> Dict:
        if self.state_file.exists():
            return json.loads(self.state_file.read_text())
        return {}

    def save(self, stage: str, data: Dict):
        """Save state after stage completion."""
        self.state[stage] = {
            'timestamp': datetime.now().isoformat(),
            'data': data,
            'status': 'completed'
        }
        self.state_file.write_text(json.dumps(self.state, indent=2))

    def resume_from(self, stage: str) -> Dict:
        """Resume pipeline from specific stage."""
        if stage in self.state:
            return self.state[stage]['data']
        raise ValueError(f"No saved state for stage: {stage}")
```

### 7.3 Enterprise Patterns

**Logging infrastructure:**

```python
# src/shared/logger.py
import logging
import json
from pythonjsonlogger import jsonlogger

def setup_logger(name: str, level: str = "INFO") -> logging.Logger:
    """Configure JSON structured logging for production."""

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # JSON formatter for structured logs
    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter(
        '%(timestamp)s %(level)s %(name)s %(message)s %(filename)s %(lineno)d'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

# Usage in services
logger = setup_logger(__name__)
logger.info("Email processed", extra={
    'email_id': 'msg_123',
    'sender': 'user@example.com',
    'processing_time_ms': 150
})
```

**Monitoring and alerting:**

```python
# src/monitoring/metrics.py
from prometheus_client import Counter, Histogram, Gauge
import time

# Define metrics
api_requests = Counter('api_requests_total', 'Total API requests', ['api', 'status'])
request_duration = Histogram('request_duration_seconds', 'Request duration', ['api'])
active_jobs = Gauge('active_jobs', 'Number of active background jobs')

# Usage
class GmailService:
    def fetch_emails(self):
        start = time.time()
        try:
            result = self._fetch()
            api_requests.labels(api='gmail', status='success').inc()
            return result
        except Exception as e:
            api_requests.labels(api='gmail', status='error').inc()
            raise
        finally:
            duration = time.time() - start
            request_duration.labels(api='gmail').observe(duration)
```

**Secrets management (not .env in production):**

```python
# src/config/secrets.py
import os
from typing import Optional

class SecretsManager:
    """Abstract secrets retrieval from different sources."""

    def __init__(self, environment: str = "development"):
        self.environment = environment

        if environment == "production":
            self.backend = AWSSecretsBackend()
        elif environment == "staging":
            self.backend = VaultBackend()
        else:
            self.backend = EnvFileBackend()  # .env for local dev

    def get_secret(self, key: str) -> Optional[str]:
        """Retrieve secret from configured backend."""
        return self.backend.get(key)

# AWS Secrets Manager
class AWSSecretsBackend:
    def get(self, key: str) -> str:
        import boto3
        client = boto3.client('secretsmanager')
        response = client.get_secret_value(SecretId=key)
        return response['SecretString']

# HashiCorp Vault
class VaultBackend:
    def get(self, key: str) -> str:
        import hvac
        client = hvac.Client(url=os.getenv('VAULT_URL'))
        secret = client.secrets.kv.v2.read_secret_version(path=key)
        return secret['data']['data']['value']

# .env file (local only)
class EnvFileBackend:
    def get(self, key: str) -> str:
        return os.getenv(key)
```

**Deployment considerations:**

```python
# src/deployment/health.py
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
async def health_check():
    """Kubernetes/Docker health check endpoint."""
    checks = {
        'database': await check_database_connection(),
        'redis': await check_redis_connection(),
        'gmail_api': await check_gmail_api_health(),
    }

    all_healthy = all(checks.values())

    return JSONResponse(
        status_code=status.HTTP_200_OK if all_healthy else status.HTTP_503_SERVICE_UNAVAILABLE,
        content={
            'status': 'healthy' if all_healthy else 'unhealthy',
            'checks': checks,
            'timestamp': datetime.now().isoformat()
        }
    )

@app.get("/ready")
async def readiness_check():
    """Kubernetes readiness probe."""
    # Check if app is ready to accept traffic
    return {'status': 'ready'}
```

**Scaling beyond single script:**

```
Development (single script):
    python src/main.py

Production (container + orchestration):
    ├── Docker container
    ├── Kubernetes deployment (3 replicas)
    ├── Load balancer
    ├── Auto-scaling (based on CPU/memory)
    ├── Log aggregation (ELK stack)
    ├── Monitoring (Prometheus + Grafana)
    └── Alerting (PagerDuty)
```

---

## 📚 Navigation

**Documentation Map:**

```
🚀 QUICK_START.md          ← Start here (10 min)
       ↓
📖 USER_GUIDE.md           ← Deep dive (architecture, phases, TDD)
       ↓
🔧 TROUBLESHOOTING.md      ← Solve issues (30 common errors)
       ↓
✨ BEST_PRACTICES.md       ← Optimize (YOU ARE HERE)
       ↓
🤝 CONTRIBUTING.md         ← Contribute back
```

**Quick Links:**

- [🏠 Home](../README.md) - Project overview
- [🚀 Quick Start](../QUICK_START.md) - 10-minute onboarding
- [📖 User Guide](USER_GUIDE.md) - Complete system documentation
- [🔧 Troubleshooting](TROUBLESHOOTING.md) - Error solutions
- [🤝 Contributing](CONTRIBUTING.md) - Development guide
- [📋 Planning](../.claude/PLANNING.md) - Architecture details
- [🔄 Changelog](../CHANGELOG.md) - Version history

**External Resources:**

- [Pydantic v2 Documentation](https://docs.pydantic.dev/latest/)
- [Jinja2 Template Designer](https://jinja.palletsprojects.com/en/3.1.x/templates/)
- [pytest Documentation](https://docs.pytest.org/)
- [TDD Best Practices (BAML Team)](https://www.boundaryml.com/blog/context-engineering)

---

**Version:** 3.0.0 (M6 - Documentation)
**Last Updated:** 2025-01-03
**Status:** ✅ Production Ready
**Maintainer:** IA Corp - Claude Code Template Team
