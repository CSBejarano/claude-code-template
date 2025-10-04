# Orchestrator Agent SDK

> **Python SDK for building automation projects with Claude Agent SDK**

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](./CHANGELOG.md)
[![Python](https://img.shields.io/badge/python-3.10+-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](../LICENSE)

---

## 📚 Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Components](#core-components)
- [Usage Examples](#usage-examples)
- [API Reference](#api-reference)
- [Versioning](#versioning)
- [Contributing](#contributing)

---

## 🎯 Overview

The **Orchestrator Agent SDK** is a Python package that provides a complete orchestration system for generating automation projects based on user requests using the Claude Agent SDK.

### Key Features

✅ **Structured Analysis** - Parse user requests into validated Pydantic models
✅ **Project Generation** - Create complete automation projects from scratch
✅ **Memory System** - Persistent learning across sessions
✅ **Specialized Subagents** - Delegate work to focused agents
✅ **Custom Tools** - MCP tools for project scaffolding
✅ **Validation** - Comprehensive quality checks

### Use Cases

- **Rapid Prototyping**: Generate MVPs in minutes
- **Enterprise Automation**: Build production-ready workflows
- **API Integration**: Connect multiple services seamlessly
- **Data Pipelines**: Create ETL and processing pipelines
- **Learning Tool**: Study modern automation architectures

---

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- Claude API Key ([get one here](https://console.anthropic.com))

### Install from Source

```bash
# Clone the template repository
git clone https://github.com/your-org/claude-code-template.git
cd claude-code-template

# Install dependencies
pip install -r requirements.txt

# The orchestrator package is now available
from orchestrator import OrchestratorAgent
```

### Install as Package (Future)

```bash
# When published to PyPI
pip install orchestrator-agent-sdk
```

---

## 🚀 Quick Start

### Basic Usage

```python
import asyncio
from orchestrator import OrchestratorAgent

async def main():
    # Initialize orchestrator
    orchestrator = OrchestratorAgent()

    # Create automation from natural language
    result = await orchestrator.create_automation(
        "Quiero automatizar el procesamiento de facturas PDF"
    )

    if result.success:
        print(f"✅ Project created at: {result.project_path}")
        print(f"📄 Files generated: {len(result.files_created)}")
    else:
        print(f"❌ Error: {result.error}")

asyncio.run(main())
```

### Analyzing Intent Only

```python
from orchestrator import OrchestratorAgent

async def analyze():
    orchestrator = OrchestratorAgent()

    # Just analyze the intent without generating project
    intent = await orchestrator.analyze_intent(
        "Create a Slack bot that responds to mentions"
    )

    print(f"Project: {intent.project_name}")
    print(f"Complexity: {intent.complexity}")
    print(f"APIs needed: {[api.name for api in intent.apis]}")
    print(f"Workflow: {intent.workflow_steps}")

asyncio.run(analyze())
```

### Using Memory Context

```python
from orchestrator import OrchestratorAgent

async def with_memory():
    orchestrator = OrchestratorAgent()

    # Store a pattern for future use
    orchestrator.memory.store_pattern(
        pattern_type="api_integration",
        pattern_data={
            "name": "Gmail OAuth2 Flow",
            "implementation": "Use google-api-python-client"
        }
    )

    # Retrieve relevant context
    context = orchestrator.get_memory_context(
        query="How to integrate Gmail?"
    )

    print(f"Found {len(context)} relevant memories")

asyncio.run(with_memory())
```

---

## 🧩 Core Components

### 1. OrchestratorAgent

Main orchestration class that coordinates the entire automation generation process.

```python
from orchestrator import OrchestratorAgent

orchestrator = OrchestratorAgent(
    working_dir=Path("./projects"),  # Where to generate projects
    memory_dir=Path("./.claude/memories")  # Where to store memories
)
```

**Key Methods:**
- `create_automation(user_request: str)` → Full project generation
- `analyze_intent(user_request: str)` → Intent analysis only
- `get_version()` → Get SDK version

### 2. Pydantic Models

Structured data models for type-safe orchestration:

```python
from orchestrator import (
    AutomationIntent,      # User request analysis
    ProjectStructure,      # Project architecture
    ValidationResult,      # Quality validation
    OrchestrationResult    # Final result
)
```

### 3. MemoryManager

Persistent memory system for learning across sessions:

```python
from orchestrator import MemoryManager

memory = MemoryManager(memory_dir=Path("./.claude/memories"))

# Store decisions
memory.store_architectural_decision(
    decision="Use FastAPI for REST API",
    rationale="Fast, modern, well-documented"
)

# Store patterns
memory.store_pattern(
    pattern_type="authentication",
    pattern_data={"strategy": "JWT tokens"}
)

# Retrieve context
context = memory.get_memory_context(query="API authentication")
```

### 4. Specialized Subagents

Five focused agents for specific tasks:

- **requirements_analyst** - Analyze and document requirements
- **code_generator** - Generate Python/Node.js code
- **test_writer** - Create comprehensive test suites
- **documentation_writer** - Generate documentation
- **validator** - Validate code quality and functionality

### 5. Custom MCP Tools

Specialized tools for project operations:

```python
from orchestrator.tools import (
    create_project_structure,  # Scaffolding
    generate_agent_definition,  # Agent files
    generate_documentation,     # Auto-docs
    validate_project           # Quality checks
)
```

---

## 💡 Usage Examples

### Example 1: Gmail to Notion Automation

```python
from orchestrator import OrchestratorAgent

async def gmail_to_notion():
    orchestrator = OrchestratorAgent()

    result = await orchestrator.create_automation(
        "Automatizar emails de Gmail importantes a páginas de Notion"
    )

    # Result contains:
    # - result.project_path: Path to generated project
    # - result.files_created: List of generated files
    # - result.validation: Quality validation results
    # - result.intent: Analyzed AutomationIntent

asyncio.run(gmail_to_notion())
```

### Example 2: PDF Processing Pipeline

```python
from orchestrator import OrchestratorAgent

async def pdf_pipeline():
    orchestrator = OrchestratorAgent()

    result = await orchestrator.create_automation(
        "Sistema que procesa facturas PDF, extrae datos con OCR y los guarda en Excel"
    )

    if result.success:
        print("✅ PDF processing pipeline created!")
        print(f"📂 Location: {result.project_path}")
        print(f"🧪 Tests: {result.validation.test_coverage}%")

asyncio.run(pdf_pipeline())
```

### Example 3: Custom Project Structure

```python
from orchestrator import OrchestratorAgent, AutomationIntent

async def custom_structure():
    orchestrator = OrchestratorAgent()

    # Manually create intent
    intent = AutomationIntent(
        project_name="custom-bot",
        goal="Slack bot for team notifications",
        complexity="medium",
        apis=[
            {"name": "Slack", "description": "Team messaging", "auth_type": "OAuth2"},
            {"name": "Google Calendar", "description": "Schedule", "auth_type": "OAuth2"}
        ],
        tech_stack=["Python"],
        workflow_steps=[
            "Listen for Slack events",
            "Check Google Calendar",
            "Send notifications"
        ]
    )

    # Generate with custom intent
    result = await orchestrator.create_automation_from_intent(intent)

asyncio.run(custom_structure())
```

---

## 📖 API Reference

### OrchestratorAgent

#### `__init__(working_dir, memory_dir)`

Initialize the orchestrator.

**Parameters:**
- `working_dir` (Path, optional): Directory for project generation. Default: current directory
- `memory_dir` (Path, optional): Directory for memory storage. Default: `.claude/memories`

#### `async create_automation(user_request: str) → OrchestrationResult`

Create complete automation project from natural language request.

**Parameters:**
- `user_request` (str): User's description of desired automation

**Returns:**
- `OrchestrationResult`: Contains project_path, files_created, validation, success status

#### `async analyze_intent(user_request: str) → AutomationIntent`

Analyze user request and extract structured intent (without generating project).

**Parameters:**
- `user_request` (str): User's description

**Returns:**
- `AutomationIntent`: Structured Pydantic model with parsed intent

#### `get_version() → str`

Get the SDK version.

**Returns:**
- `str`: Version string (e.g., "1.0.0")

---

## 🔄 Versioning

This SDK follows **Semantic Versioning** (semver.org):

- **MAJOR** version: Breaking changes (e.g., 1.0.0 → 2.0.0)
- **MINOR** version: New features, backwards-compatible (e.g., 1.0.0 → 1.1.0)
- **PATCH** version: Bug fixes, backwards-compatible (e.g., 1.0.0 → 1.0.1)

**Current Version:** 1.0.0

**Versioning Policy:**
- Breaking changes require MAJOR bump + migration guide
- New features require MINOR bump
- Bug fixes require PATCH bump
- Deprecation warnings given minimum 1 MINOR version before removal

See [CHANGELOG.md](./CHANGELOG.md) for detailed release history.

See [MIGRATIONS.md](./MIGRATIONS.md) for migration guides between major versions.

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

### Development Setup

```bash
# Clone repository
git clone https://github.com/your-org/claude-code-template.git
cd claude-code-template

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v
```

### Code Standards

- **Python**: PEP 8, type hints required
- **Tests**: Minimum 80% coverage for new code
- **Docstrings**: Google style for all public methods
- **Commits**: Conventional commits (feat, fix, docs, etc.)

### Submitting Changes

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes with tests
4. Ensure all tests pass (`pytest tests/`)
5. Commit with conventional commit message
6. Push to your fork
7. Open a Pull Request

---

## 📄 License

MIT License - see [../LICENSE](../LICENSE) for details.

---

## 📧 Support

- **Issues**: [GitHub Issues](https://github.com/your-org/claude-code-template/issues)
- **Docs**: [Main Documentation](../.claude/PLANNING.md)
- **Changelog**: [CHANGELOG.md](./CHANGELOG.md)
- **Migrations**: [MIGRATIONS.md](./MIGRATIONS.md)

---

## 🎓 Related Documentation

- [Template Documentation](../.claude/PLANNING.md) - Overall system architecture
- [CHANGELOG](./CHANGELOG.md) - Detailed release history
- [MIGRATIONS](./MIGRATIONS.md) - Version migration guides
- [Claude Agent SDK](https://docs.anthropic.com) - Official SDK documentation

---

**Version:** 1.0.0
**Last Updated:** 2025-01-03
**Python:** 3.10+
**Status:** ✅ Stable
