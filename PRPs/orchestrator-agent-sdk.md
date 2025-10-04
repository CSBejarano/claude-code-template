# PRP: Claude Agent SDK Orchestrator

> **Agente Orquestador Autónomo para Generación de Proyectos de Automatización**
>
> **Objetivo**: Crear un agente SDK que interprete solicitudes de automatización del usuario y genere proyectos completos con agentes especializados, documentación y validación automática.

---

## 📋 **Metadata**

- **Feature**: Orchestrator Agent SDK
- **Priority**: P0 - Critical
- **Complexity**: High
- **Estimated Effort**: 3-4 days
- **Dependencies**:
  - `claude-agent-sdk` (Python)
  - `pydantic` >= 2.0
  - `asyncio`
  - Existing Claude Code tools (Read, Write, Edit, Task, etc.)

---

## 🎯 **Objective**

Create an intelligent orchestrator agent that:

1. **Interprets** user automation requests using structured output
2. **Generates** complete project structures with specialized agents
3. **Orchestrates** subagents for parallel development tasks
4. **Manages** context and memory for long-running workflows
5. **Tracks** progress with TodoWrite and validates with hooks
6. **Documents** decisions and architecture automatically

### **Success Criteria**

```python
# User input
"Quiero automatizar el procesamiento de cotizaciones en PDF"

# Expected output
✅ Project structure created
✅ 4 specialized agents generated (parser, validator, normalizer, exporter)
✅ MCP tools configured (PDF parser, Excel writer)
✅ Documentation generated (README, PLANNING, TASK)
✅ Tests scaffolded
✅ Memory initialized with project decisions
```

---

## 📚 **Research & Context**

### **1. Claude Agent SDK Documentation**

**Core Concepts**: [Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview)

**Key Resources**:
- [Python SDK Reference](https://docs.claude.com/en/api/agent-sdk/python)
- [Custom Tools Guide](https://docs.claude.com/en/api/agent-sdk/custom-tools)
- [Subagents Documentation](https://docs.claude.com/en/api/agent-sdk/subagents)
- [Memory Tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool)
- [Context Editing](https://docs.claude.com/en/docs/build-with-claude/context-editing)

### **2. Codebase Patterns**

**Existing Patterns to Follow**:
```bash
# Search for existing agent patterns
grep -r "ClaudeSDKClient" --include="*.py"
grep -r "AgentDefinition" --include="*.py"
grep -r "@tool" --include="*.py"
```

**Project Structure Convention**:
```
claude-code-template/
├── .claude/
│   ├── agents/              # Specialized agents (existing pattern)
│   ├── commands/            # Slash commands (existing pattern)
│   └── hooks/               # Event hooks (existing pattern)
├── orchestrator/            # NEW: Orchestrator agent
│   ├── agent.py            # Main orchestrator
│   ├── tools.py            # Custom MCP tools
│   ├── subagents.py        # Subagent definitions
│   ├── models.py           # Pydantic models
│   └── memory.py           # Memory management
├── PRPs/                    # PRP templates (existing)
└── docs/                    # Documentation (existing)
```

### **3. External Research**

**Pydantic AI Patterns**:
- [Pydantic AI Docs](https://ai.pydantic.dev/)
- Search for agent orchestration patterns
- Look for multi-agent coordination examples

**LangGraph/CrewAI Inspiration**:
- Research orchestration patterns from similar frameworks
- Study task delegation strategies
- Analyze memory management approaches

**MCP Server Examples**:
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)
- Study filesystem, database, and API integration patterns

### **4. Critical SDK Features to Use**

#### **a) Context Management**
```python
# Automatic context editing (built-in with Sonnet 4.5)
# Memory tool for persistent decisions
options = ClaudeAgentOptions(
    # Memory tool enabled by default
    # Context editing automatic
)
```

#### **b) Structured Output for Intent Analysis**
```python
from pydantic import BaseModel
from claude_agent_sdk import query

class AutomationIntent(BaseModel):
    """User's automation intent"""
    task_type: str  # "document_processing", "api_integration", "workflow"
    input_format: str  # "pdf", "excel", "json", "api"
    output_format: str  # "normalized_data", "api_response", "report"
    required_tools: list[str]  # ["pdf_parser", "geocoding", "database"]
    complexity: str  # "simple", "medium", "complex"

# Use structured output to analyze intent
async for message in query(
    prompt=f"Analyze this automation request: {user_input}",
    options=ClaudeAgentOptions(
        system_prompt="Extract automation intent as AutomationIntent model"
    )
):
    intent = AutomationIntent.model_validate_json(message.content)
```

#### **c) Subagent Delegation**
```python
from claude_agent_sdk import AgentDefinition

agents = {
    'requirements_analyst': AgentDefinition(
        description='Analyzes user requirements and creates detailed specs',
        prompt='''Analyze automation requirements. Extract:
        - Input sources and formats
        - Processing steps needed
        - Output requirements
        - Integration points
        Document findings in memory.''',
        tools=['Read', 'Write', 'Grep'],
        model='sonnet'
    ),
    'code_generator': AgentDefinition(
        description='Generates implementation code based on specs',
        prompt='''Generate production-ready code following project conventions.
        Read memory for requirements. Create modular, tested code.''',
        tools=['Read', 'Write', 'Edit', 'Grep', 'Glob'],
        model='sonnet'
    ),
    'test_writer': AgentDefinition(
        description='Creates comprehensive test suites',
        prompt='''Generate tests following pytest patterns.
        Cover happy path, edge cases, and failures.''',
        tools=['Read', 'Write', 'Bash'],
        model='sonnet'
    ),
    'documentation_writer': AgentDefinition(
        description='Generates project documentation',
        prompt='''Create clear, comprehensive documentation.
        Update README, PLANNING, and TASK files.''',
        tools=['Read', 'Write', 'Edit'],
        model='sonnet'
    )
}
```

#### **d) Custom MCP Tools**
```python
from claude_agent_sdk import tool, create_sdk_mcp_server
from typing import Any

@tool("create_project_structure", "Creates base project structure",
      {"project_name": str, "project_type": str})
async def create_project_structure(args: dict[str, Any]) -> dict[str, Any]:
    """Creates base directory structure for automation project"""
    # Implementation
    return {"content": [{"type": "text", "text": "Structure created"}]}

@tool("generate_agent_definition", "Generates specialized agent config",
      {"agent_purpose": str, "required_tools": list})
async def generate_agent_definition(args: dict[str, Any]) -> dict[str, Any]:
    """Creates AgentDefinition for specialized tasks"""
    # Implementation
    return {"content": [{"type": "text", "text": "Agent defined"}]}

orchestrator_server = create_sdk_mcp_server(
    name="orchestrator-tools",
    version="1.0.0",
    tools=[create_project_structure, generate_agent_definition]
)
```

#### **e) Progress Tracking with TodoWrite**
```python
from claude_agent_sdk import ClaudeSDKClient

async with ClaudeSDKClient(options=options) as client:
    # Create todos for orchestration workflow
    await client.query("""
    Create todo list for this automation project:
    1. Analyze requirements
    2. Generate project structure
    3. Create specialized agents
    4. Implement core logic
    5. Write tests
    6. Generate documentation
    """)
```

#### **f) Validation Hooks**
```python
from claude_agent_sdk import HookMatcher

async def validate_code_hook(input_data, tool_use_id, context):
    """Validates generated code"""
    if 'Write' in input_data.get('tool_name', ''):
        # Run linter
        import subprocess
        result = subprocess.run(['ruff', 'check'], capture_output=True)
        return {'systemMessage': f'Validation: {result.stdout.decode()}'}
    return {}

hooks = {
    'PostToolUse': [
        HookMatcher(matcher='Write', hooks=[validate_code_hook])
    ]
}
```

---

## 🏗️ **Implementation Blueprint**

### **Phase 1: Core Orchestrator Setup**

#### **1.1 Create Base Orchestrator Class**

**File**: `orchestrator/agent.py`

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, AgentDefinition
from typing import Optional, Dict, Any
import asyncio

class OrchestratorAgent:
    """
    Main orchestrator agent for automation project generation.

    Capabilities:
    - Intent analysis via structured output
    - Project generation with subagents
    - Memory management for decisions
    - Progress tracking with todos
    - Validation with hooks
    """

    def __init__(self, memory_dir: str = "./orchestrator-memory"):
        self.memory_dir = memory_dir
        self.client: Optional[ClaudeSDKClient] = None
        self.options = self._build_options()

    def _build_options(self) -> ClaudeAgentOptions:
        """Build orchestrator configuration"""
        return ClaudeAgentOptions(
            system_prompt={
                "type": "preset",
                "preset": "claude_code",
                "append": self._get_orchestrator_prompt()
            },
            agents=self._get_subagents(),
            mcp_servers={"orchestrator": self._get_orchestrator_tools()},
            hooks=self._get_validation_hooks(),
            allowed_tools=[
                'Read', 'Write', 'Edit', 'Grep', 'Glob',
                'Bash', 'Task', 'TodoWrite',
                'mcp__orchestrator__create_project_structure',
                'mcp__orchestrator__generate_agent_definition'
            ],
            permission_mode='acceptEdits',
            setting_sources=['project', 'local']
        )

    def _get_orchestrator_prompt(self) -> str:
        """System prompt for orchestrator"""
        return """
        You are an intelligent orchestrator agent for automation projects.

        Your responsibilities:
        1. Analyze user automation requests with structured output
        2. Break down complex automations into components
        3. Delegate to specialized subagents (parallel when possible)
        4. Track progress with TodoWrite
        5. Store critical decisions in memory
        6. Generate complete, production-ready projects

        Process:
        1. Analyze intent → classify task type, complexity, required tools
        2. Create project structure → directories, configs, base files
        3. Delegate to subagents → requirements, code, tests, docs
        4. Validate outputs → run linters, type checks, tests
        5. Generate documentation → README, PLANNING, TASK
        6. Store learnings → save patterns to memory

        Always use memory to:
        - Save architectural decisions
        - Store learned patterns
        - Track project conventions
        - Document tool configurations
        """

    def _get_subagents(self) -> Dict[str, AgentDefinition]:
        """Define specialized subagents"""
        # Implementation from research
        pass

    def _get_orchestrator_tools(self):
        """Get custom MCP tools"""
        # Implementation from tools.py
        pass

    def _get_validation_hooks(self) -> Dict[str, list]:
        """Configure validation hooks"""
        # Implementation
        pass

    async def orchestrate(self, user_request: str) -> Dict[str, Any]:
        """
        Main orchestration method.

        Args:
            user_request: User's automation request

        Returns:
            Dict with project info, generated files, and metrics
        """
        async with ClaudeSDKClient(options=self.options) as client:
            self.client = client

            # Phase 1: Analyze intent
            intent = await self._analyze_intent(user_request)

            # Phase 2: Create project structure
            project_info = await self._create_project(intent)

            # Phase 3: Delegate to subagents (parallel)
            results = await asyncio.gather(
                self._generate_requirements(intent),
                self._generate_code(intent, project_info),
                self._generate_tests(intent, project_info),
                self._generate_docs(intent, project_info)
            )

            # Phase 4: Validate and finalize
            validation = await self._validate_project(project_info)

            return {
                'project': project_info,
                'intent': intent,
                'results': results,
                'validation': validation
            }
```

#### **1.2 Implement Intent Analysis**

**File**: `orchestrator/models.py`

```python
from pydantic import BaseModel, Field
from typing import List, Literal

class AutomationIntent(BaseModel):
    """Structured representation of user's automation intent"""

    task_type: Literal[
        "document_processing",
        "api_integration",
        "workflow_automation",
        "data_pipeline",
        "multi_agent_system"
    ] = Field(..., description="Primary automation category")

    input_format: List[str] = Field(
        ...,
        description="Input data formats (pdf, excel, json, api, etc.)"
    )

    output_format: str = Field(
        ...,
        description="Desired output format"
    )

    required_tools: List[str] = Field(
        ...,
        description="External tools/APIs needed (geocoding, pdf_parser, etc.)"
    )

    complexity: Literal["simple", "medium", "complex"] = Field(
        ...,
        description="Estimated complexity level"
    )

    key_requirements: List[str] = Field(
        ...,
        description="Core functional requirements"
    )

    constraints: List[str] = Field(
        default_factory=list,
        description="Technical constraints or limitations"
    )

    estimated_agents: int = Field(
        ...,
        description="Estimated number of specialized agents needed"
    )

class ProjectStructure(BaseModel):
    """Generated project structure definition"""

    project_name: str
    base_path: str
    directories: List[str]
    config_files: List[str]
    agent_definitions: List[Dict[str, Any]]
    mcp_tools: List[str]
```

#### **1.3 Create Custom MCP Tools**

**File**: `orchestrator/tools.py`

```python
from claude_agent_sdk import tool, create_sdk_mcp_server
from typing import Any, Dict
import os
from pathlib import Path

@tool(
    "create_project_structure",
    "Creates complete project directory structure",
    {
        "project_name": str,
        "project_type": str,
        "required_agents": list
    }
)
async def create_project_structure(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Creates base project structure with:
    - Directory tree
    - Config files (.env, settings.json)
    - Agent definitions
    - PRP templates
    """
    project_name = args['project_name']
    project_type = args['project_type']

    base_path = Path(f"./{project_name}")

    # Create directory structure
    dirs = [
        f"{project_name}/src",
        f"{project_name}/tests",
        f"{project_name}/.claude/agents",
        f"{project_name}/.claude/commands",
        f"{project_name}/PRPs",
        f"{project_name}/docs",
        f"{project_name}/orchestrator-memory"
    ]

    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)

    # Create base files
    files_created = []

    # .env template
    env_content = """# Environment Configuration
ANTHROPIC_API_KEY=your_key_here
LOG_LEVEL=INFO
"""
    (base_path / ".env.example").write_text(env_content)
    files_created.append(".env.example")

    # settings.json
    settings_content = """{
  "hooks": {},
  "agents": {},
  "mcpServers": {}
}"""
    (base_path / ".claude" / "settings.json").write_text(settings_content)
    files_created.append(".claude/settings.json")

    return {
        "content": [{
            "type": "text",
            "text": f"✅ Project structure created at {base_path}\n" +
                   f"Directories: {len(dirs)}\n" +
                   f"Files: {len(files_created)}\n" +
                   f"Created: {', '.join(files_created)}"
        }]
    }

@tool(
    "generate_agent_definition",
    "Generates specialized agent configuration",
    {
        "agent_name": str,
        "agent_purpose": str,
        "required_tools": list,
        "model": str
    }
)
async def generate_agent_definition(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Creates AgentDefinition for specialized tasks.
    Returns markdown file with frontmatter.
    """
    agent_name = args['agent_name']
    purpose = args['agent_purpose']
    tools = args['required_tools']
    model = args.get('model', 'sonnet')

    # Generate agent markdown
    agent_md = f"""---
name: {agent_name}
description: {purpose}
tools: {', '.join(tools)}
model: {model}
---

# {agent_name.replace('_', ' ').title()}

## Purpose
{purpose}

## Capabilities
- Access to tools: {', '.join(tools)}
- Model: Claude {model}

## Usage Pattern
This agent should be invoked when:
[Auto-generated based on purpose]

## Memory Integration
This agent uses memory to:
- Store learned patterns
- Cache processing decisions
- Track successful strategies
"""

    return {
        "content": [{
            "type": "text",
            "text": f"Agent definition generated:\n\n{agent_md}"
        }]
    }

@tool(
    "generate_documentation",
    "Generates project documentation (README, PLANNING, TASK)",
    {
        "project_info": dict,
        "intent": dict
    }
)
async def generate_documentation(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates comprehensive project documentation.
    """
    # Implementation
    pass

def get_orchestrator_server():
    """Returns configured orchestrator MCP server"""
    return create_sdk_mcp_server(
        name="orchestrator-tools",
        version="1.0.0",
        tools=[
            create_project_structure,
            generate_agent_definition,
            generate_documentation
        ]
    )
```

### **Phase 2: Subagent Definitions**

**File**: `orchestrator/subagents.py`

```python
from claude_agent_sdk import AgentDefinition
from typing import Dict

def get_subagent_definitions() -> Dict[str, AgentDefinition]:
    """
    Returns all specialized subagent definitions.

    Subagents:
    - requirements_analyst: Analyzes and documents requirements
    - code_generator: Generates implementation code
    - test_writer: Creates test suites
    - documentation_writer: Generates docs
    - validator: Runs validation checks
    """

    return {
        'requirements_analyst': AgentDefinition(
            description='Analyzes user requirements and creates detailed specifications. Use for initial project analysis.',
            prompt='''You are a requirements analyst agent.

            Your task:
            1. Analyze the automation request deeply
            2. Extract all functional requirements
            3. Identify required external integrations
            4. Document constraints and edge cases
            5. Estimate complexity and effort
            6. Save findings to memory for other agents

            Output format:
            - Structured requirements document
            - Integration points list
            - Risk assessment
            - Implementation recommendations

            Always save critical decisions to memory.
            ''',
            tools=['Read', 'Write', 'Grep', 'Glob'],
            model='sonnet'
        ),

        'code_generator': AgentDefinition(
            description='Generates production-ready implementation code following project conventions. Use after requirements are analyzed.',
            prompt='''You are a code generation agent.

            Your task:
            1. Read requirements from memory
            2. Follow existing codebase patterns
            3. Generate modular, clean code
            4. Include error handling and logging
            5. Add type hints and docstrings
            6. Create async/await patterns where appropriate

            Code quality standards:
            - Files < 500 lines
            - Clear separation of concerns
            - Comprehensive error handling
            - Type safety with Pydantic
            - Async-first design

            Always check existing patterns before generating.
            ''',
            tools=['Read', 'Write', 'Edit', 'Grep', 'Glob'],
            model='sonnet'
        ),

        'test_writer': AgentDefinition(
            description='Creates comprehensive test suites with pytest. Use after code generation.',
            prompt='''You are a test generation agent.

            Your task:
            1. Read generated code
            2. Create pytest test suites
            3. Cover happy path, edge cases, failures
            4. Include fixtures and mocks
            5. Test async operations properly
            6. Aim for >80% coverage

            Test structure:
            - tests/unit/ for unit tests
            - tests/integration/ for integration tests
            - Use pytest fixtures
            - Mock external dependencies
            - Test error conditions

            Always run tests after generation to verify.
            ''',
            tools=['Read', 'Write', 'Bash'],
            model='sonnet'
        ),

        'documentation_writer': AgentDefinition(
            description='Generates comprehensive project documentation. Use after implementation is complete.',
            prompt='''You are a documentation agent.

            Your task:
            1. Read project structure and code
            2. Update README with setup instructions
            3. Update PLANNING with architecture
            4. Update TASK with completed tasks
            5. Generate API documentation
            6. Create usage examples

            Documentation standards:
            - Clear, concise language
            - Code examples for all APIs
            - Architecture diagrams where helpful
            - Complete setup instructions
            - Troubleshooting section

            Read memory for project decisions to document.
            ''',
            tools=['Read', 'Write', 'Edit', 'Grep'],
            model='sonnet'
        ),

        'validator': AgentDefinition(
            description='Runs validation checks on generated code. Use before finalization.',
            prompt='''You are a validation agent.

            Your task:
            1. Run linters (ruff, mypy)
            2. Execute test suite
            3. Check type coverage
            4. Validate file structure
            5. Verify documentation completeness
            6. Report issues clearly

            Validation gates:
            - All linters pass
            - All tests pass
            - Type checking passes
            - Documentation complete
            - No security issues

            Report results in structured format.
            ''',
            tools=['Bash', 'Read', 'Grep'],
            model='sonnet'
        )
    }
```

### **Phase 3: Memory Management**

**File**: `orchestrator/memory.py`

```python
from pathlib import Path
from typing import Dict, Any, Optional
import json
from datetime import datetime

class OrchestratorMemory:
    """
    Manages orchestrator memory for:
    - Architectural decisions
    - Learned patterns
    - Project configurations
    - Success/failure tracking
    """

    def __init__(self, memory_dir: str = "./orchestrator-memory"):
        self.memory_dir = Path(memory_dir)
        self.memory_dir.mkdir(parents=True, exist_ok=True)

    async def save_decision(
        self,
        decision_type: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Saves architectural decision to memory.

        Args:
            decision_type: Type of decision (architecture, tool_choice, pattern)
            content: Decision content
            metadata: Additional context
        """
        timestamp = datetime.now().isoformat()
        decision_file = self.memory_dir / f"{decision_type}_{timestamp}.md"

        decision_content = f"""# {decision_type.replace('_', ' ').title()}

**Date**: {timestamp}
**Type**: {decision_type}

## Decision
{content}

## Context
{json.dumps(metadata or {}, indent=2)}
"""

        decision_file.write_text(decision_content)

    async def save_pattern(
        self,
        pattern_name: str,
        pattern_code: str,
        use_cases: list[str]
    ):
        """Saves successful pattern for reuse"""
        pattern_file = self.memory_dir / f"pattern_{pattern_name}.md"

        content = f"""# Pattern: {pattern_name}

## Code
```python
{pattern_code}
```

## Use Cases
{chr(10).join(f'- {uc}' for uc in use_cases)}

## Last Updated
{datetime.now().isoformat()}
"""
        pattern_file.write_text(content)

    async def get_patterns(self, pattern_type: Optional[str] = None) -> list[str]:
        """Retrieves saved patterns"""
        pattern_files = list(self.memory_dir.glob("pattern_*.md"))

        if pattern_type:
            pattern_files = [
                f for f in pattern_files
                if pattern_type in f.stem
            ]

        return [f.read_text() for f in pattern_files]

    async def save_project_config(
        self,
        project_name: str,
        config: Dict[str, Any]
    ):
        """Saves project configuration"""
        config_file = self.memory_dir / f"project_{project_name}.json"
        config_file.write_text(json.dumps(config, indent=2))

    async def track_metrics(
        self,
        project_name: str,
        metrics: Dict[str, Any]
    ):
        """Tracks project generation metrics"""
        metrics_file = self.memory_dir / "metrics.jsonl"

        metric_entry = {
            "timestamp": datetime.now().isoformat(),
            "project": project_name,
            **metrics
        }

        with metrics_file.open('a') as f:
            f.write(json.dumps(metric_entry) + '\n')
```

### **Phase 4: Main Orchestration Flow**

**File**: `orchestrator/workflow.py`

```python
from claude_agent_sdk import ClaudeSDKClient, AssistantMessage, ResultMessage
from typing import Dict, Any
import asyncio

from .agent import OrchestratorAgent
from .models import AutomationIntent, ProjectStructure
from .memory import OrchestratorMemory

class OrchestrationWorkflow:
    """
    Main orchestration workflow that:
    1. Analyzes intent
    2. Generates project
    3. Delegates to subagents
    4. Validates results
    5. Tracks metrics
    """

    def __init__(self):
        self.orchestrator = OrchestratorAgent()
        self.memory = OrchestratorMemory()

    async def execute(self, user_request: str) -> Dict[str, Any]:
        """
        Execute full orchestration workflow.

        Workflow:
        1. Analyze intent with structured output
        2. Create project structure
        3. Parallel subagent execution:
           - Requirements analyst
           - Code generator
           - Test writer
           - Documentation writer
        4. Validation checks
        5. Memory persistence
        6. Metrics tracking
        """

        # Phase 1: Intent Analysis
        print("🔍 Analyzing automation intent...")
        intent = await self._analyze_intent(user_request)
        await self.memory.save_decision(
            "intent_analysis",
            f"User wants: {user_request}",
            intent.model_dump()
        )

        # Phase 2: Project Generation
        print("📁 Generating project structure...")
        project = await self._generate_project(intent)
        await self.memory.save_project_config(
            project['name'],
            project
        )

        # Phase 3: Parallel Subagent Execution
        print("🤖 Delegating to specialized agents...")
        tasks = [
            self._run_requirements_analysis(intent),
            self._run_code_generation(intent, project),
            self._run_test_generation(intent, project),
            self._run_documentation(intent, project)
        ]

        results = await asyncio.gather(*tasks)

        # Phase 4: Validation
        print("✅ Validating outputs...")
        validation = await self._validate_project(project)

        # Phase 5: Metrics
        metrics = {
            "complexity": intent.complexity,
            "agents_used": len(results),
            "validation_passed": validation['passed'],
            "generation_time_ms": validation.get('time_ms', 0)
        }
        await self.memory.track_metrics(project['name'], metrics)

        return {
            'intent': intent.model_dump(),
            'project': project,
            'results': results,
            'validation': validation,
            'metrics': metrics
        }

    async def _analyze_intent(self, user_request: str) -> AutomationIntent:
        """Analyze intent using structured output"""
        async with ClaudeSDKClient(options=self.orchestrator.options) as client:
            await client.query(f"""
            Analyze this automation request and extract structured intent:

            Request: {user_request}

            Return AutomationIntent JSON with:
            - task_type (document_processing, api_integration, etc.)
            - input_format (list of formats)
            - output_format (desired output)
            - required_tools (external APIs/services needed)
            - complexity (simple, medium, complex)
            - key_requirements (functional requirements list)
            - constraints (technical limitations)
            - estimated_agents (number of agents needed)
            """)

            response_text = ""
            async for message in client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if hasattr(block, 'text'):
                            response_text += block.text

            # Parse structured output
            intent = AutomationIntent.model_validate_json(response_text)
            return intent

    async def _generate_project(self, intent: AutomationIntent) -> Dict[str, Any]:
        """Generate project structure using custom tools"""
        async with ClaudeSDKClient(options=self.orchestrator.options) as client:
            await client.query(f"""
            Create project structure for: {intent.task_type}

            Required agents: {intent.estimated_agents}
            Required tools: {', '.join(intent.required_tools)}

            Use the create_project_structure tool.
            """)

            project_info = {}
            async for message in client.receive_response():
                if isinstance(message, ResultMessage):
                    project_info = {
                        'name': f"automation_{intent.task_type}",
                        'type': intent.task_type,
                        'status': 'created'
                    }

            return project_info

    async def _run_requirements_analysis(self, intent: AutomationIntent):
        """Delegate to requirements analyst agent"""
        async with ClaudeSDKClient(options=self.orchestrator.options) as client:
            await client.query(f"""
            @requirements_analyst

            Analyze requirements for {intent.task_type} automation.

            Input formats: {intent.input_format}
            Output format: {intent.output_format}
            Key requirements: {', '.join(intent.key_requirements)}

            Save detailed analysis to memory.
            """)

            # Collect results
            results = []
            async for message in client.receive_response():
                results.append(message)

            return {'phase': 'requirements', 'results': results}

    async def _run_code_generation(self, intent: AutomationIntent, project: Dict):
        """Delegate to code generator agent"""
        async with ClaudeSDKClient(options=self.orchestrator.options) as client:
            await client.query(f"""
            @code_generator

            Generate implementation for {project['name']}.
            Read requirements from memory.

            Follow project conventions:
            - Files < 500 lines
            - Type hints with Pydantic
            - Async/await patterns
            - Comprehensive error handling

            Generate modular code in src/ directory.
            """)

            results = []
            async for message in client.receive_response():
                results.append(message)

            return {'phase': 'code_generation', 'results': results}

    async def _run_test_generation(self, intent: AutomationIntent, project: Dict):
        """Delegate to test writer agent"""
        async with ClaudeSDKClient(options=self.orchestrator.options) as client:
            await client.query(f"""
            @test_writer

            Create test suite for {project['name']}.

            Test structure:
            - tests/unit/ for unit tests
            - tests/integration/ for integration tests

            Coverage requirements:
            - Happy path
            - Edge cases
            - Error conditions
            - Async operations

            Use pytest patterns.
            """)

            results = []
            async for message in client.receive_response():
                results.append(message)

            return {'phase': 'test_generation', 'results': results}

    async def _run_documentation(self, intent: AutomationIntent, project: Dict):
        """Delegate to documentation writer agent"""
        async with ClaudeSDKClient(options=self.orchestrator.options) as client:
            await client.query(f"""
            @documentation_writer

            Generate comprehensive documentation for {project['name']}.

            Update:
            - README.md with setup and usage
            - PLANNING.md with architecture
            - TASK.md with completed tasks

            Include:
            - API documentation
            - Usage examples
            - Troubleshooting guide

            Read memory for architectural decisions.
            """)

            results = []
            async for message in client.receive_response():
                results.append(message)

            return {'phase': 'documentation', 'results': results}

    async def _validate_project(self, project: Dict) -> Dict[str, Any]:
        """Run validation checks"""
        async with ClaudeSDKClient(options=self.orchestrator.options) as client:
            await client.query(f"""
            @validator

            Validate {project['name']} project.

            Run:
            1. ruff check --fix
            2. mypy .
            3. pytest tests/ -v

            Report:
            - Linting issues
            - Type errors
            - Test failures
            - Overall pass/fail
            """)

            validation_passed = True
            issues = []

            async for message in client.receive_response():
                if isinstance(message, ResultMessage):
                    validation_passed = not message.is_error

            return {
                'passed': validation_passed,
                'issues': issues
            }
```

---

## 🧪 **Testing Strategy**

### **Test Files Structure**
```
tests/
├── unit/
│   ├── test_intent_analysis.py
│   ├── test_project_generation.py
│   ├── test_memory.py
│   └── test_tools.py
├── integration/
│   ├── test_orchestration_flow.py
│   ├── test_subagent_delegation.py
│   └── test_validation.py
└── fixtures/
    ├── sample_requests.py
    └── mock_responses.py
```

### **Unit Tests**

**File**: `tests/unit/test_intent_analysis.py`

```python
import pytest
from orchestrator.models import AutomationIntent
from orchestrator.workflow import OrchestrationWorkflow

@pytest.mark.asyncio
async def test_intent_analysis_document_processing():
    """Test intent analysis for document processing request"""
    workflow = OrchestrationWorkflow()

    request = "Automatizar procesamiento de cotizaciones en PDF a Excel normalizado"

    intent = await workflow._analyze_intent(request)

    assert intent.task_type == "document_processing"
    assert "pdf" in intent.input_format
    assert intent.output_format in ["excel", "normalized_data"]
    assert intent.complexity in ["simple", "medium", "complex"]
    assert len(intent.key_requirements) > 0

@pytest.mark.asyncio
async def test_intent_analysis_api_integration():
    """Test intent analysis for API integration"""
    workflow = OrchestrationWorkflow()

    request = "Crear API REST para consultar datos de geocoding y guardar en base de datos"

    intent = await workflow._analyze_intent(request)

    assert intent.task_type == "api_integration"
    assert "geocoding" in intent.required_tools or "database" in intent.required_tools
```

**File**: `tests/unit/test_memory.py`

```python
import pytest
from pathlib import Path
from orchestrator.memory import OrchestratorMemory

@pytest.fixture
def temp_memory_dir(tmp_path):
    """Temporary memory directory"""
    return str(tmp_path / "test-memory")

@pytest.mark.asyncio
async def test_save_decision(temp_memory_dir):
    """Test saving architectural decision"""
    memory = OrchestratorMemory(temp_memory_dir)

    await memory.save_decision(
        "architecture",
        "Use async/await pattern for all I/O operations",
        {"reason": "Better performance for I/O bound tasks"}
    )

    decision_files = list(Path(temp_memory_dir).glob("architecture_*.md"))
    assert len(decision_files) == 1

    content = decision_files[0].read_text()
    assert "async/await" in content
    assert "Better performance" in content

@pytest.mark.asyncio
async def test_save_pattern(temp_memory_dir):
    """Test saving code pattern"""
    memory = OrchestratorMemory(temp_memory_dir)

    pattern_code = """
async def process_batch(items: list) -> list:
    tasks = [process_item(item) for item in items]
    return await asyncio.gather(*tasks)
"""

    await memory.save_pattern(
        "batch_processing",
        pattern_code,
        ["Process multiple items concurrently", "Async batch operations"]
    )

    pattern_files = list(Path(temp_memory_dir).glob("pattern_*.md"))
    assert len(pattern_files) == 1

    content = pattern_files[0].read_text()
    assert "asyncio.gather" in content
```

### **Integration Tests**

**File**: `tests/integration/test_orchestration_flow.py`

```python
import pytest
from orchestrator.workflow import OrchestrationWorkflow

@pytest.mark.asyncio
async def test_full_orchestration_simple_project():
    """Test complete orchestration flow for simple project"""
    workflow = OrchestrationWorkflow()

    request = "Crear script para convertir CSV a JSON"

    result = await workflow.execute(request)

    # Verify intent
    assert result['intent']['task_type'] in ['document_processing', 'data_pipeline']
    assert result['intent']['complexity'] == 'simple'

    # Verify project created
    assert 'project' in result
    assert result['project']['status'] == 'created'

    # Verify subagent results
    assert len(result['results']) >= 4  # requirements, code, tests, docs

    # Verify validation
    assert result['validation']['passed'] == True

    # Verify metrics
    assert 'metrics' in result
    assert result['metrics']['agents_used'] >= 4

@pytest.mark.asyncio
async def test_parallel_subagent_execution():
    """Test that subagents execute in parallel"""
    import time
    workflow = OrchestrationWorkflow()

    request = "Crear API para procesar documentos PDF"

    start = time.time()
    result = await workflow.execute(request)
    duration = time.time() - start

    # Should complete faster than sequential (rough check)
    # If 4 agents each take 10s, parallel should be ~10s not 40s
    assert duration < 30  # Generous threshold
    assert len(result['results']) >= 4
```

### **Validation Gates**

```bash
# All checks must pass before considering implementation complete

# 1. Linting
ruff check --fix orchestrator/ tests/

# 2. Type checking
mypy orchestrator/ tests/

# 3. Unit tests
pytest tests/unit/ -v --cov=orchestrator --cov-report=term-missing

# 4. Integration tests
pytest tests/integration/ -v

# 5. Full test suite
pytest tests/ -v --cov=orchestrator --cov-report=html

# Coverage threshold: >80%
```

---

## 📊 **Implementation Tasks**

### **Phase 1: Core Setup (Day 1)**
- [ ] Create `orchestrator/` directory structure
- [ ] Implement `models.py` with Pydantic models
- [ ] Create base `OrchestratorAgent` class
- [ ] Setup memory management in `memory.py`
- [ ] Write unit tests for models and memory

### **Phase 2: Custom Tools (Day 1-2)**
- [ ] Implement `create_project_structure` tool
- [ ] Implement `generate_agent_definition` tool
- [ ] Implement `generate_documentation` tool
- [ ] Create MCP server configuration
- [ ] Write unit tests for tools

### **Phase 3: Subagents (Day 2)**
- [ ] Define requirements_analyst agent
- [ ] Define code_generator agent
- [ ] Define test_writer agent
- [ ] Define documentation_writer agent
- [ ] Define validator agent
- [ ] Test subagent invocation

### **Phase 4: Orchestration Flow (Day 2-3)**
- [ ] Implement intent analysis workflow
- [ ] Implement project generation workflow
- [ ] Implement parallel subagent execution
- [ ] Implement validation workflow
- [ ] Add progress tracking with TodoWrite
- [ ] Write integration tests

### **Phase 5: Validation & Hooks (Day 3)**
- [ ] Implement validation hooks
- [ ] Add linting checks
- [ ] Add type checking
- [ ] Add test execution
- [ ] Test hook integration

### **Phase 6: Documentation & Examples (Day 3-4)**
- [ ] Write comprehensive README
- [ ] Create usage examples
- [ ] Document API reference
- [ ] Create troubleshooting guide
- [ ] Add architecture diagrams

### **Phase 7: Testing & Refinement (Day 4)**
- [ ] Complete test coverage (>80%)
- [ ] Fix any failing tests
- [ ] Performance optimization
- [ ] Error handling improvements
- [ ] Final validation pass

---

## 🎯 **Success Metrics**

### **Quality Gates**
- ✅ All linting checks pass (ruff, mypy)
- ✅ Test coverage >80%
- ✅ All integration tests pass
- ✅ Documentation complete
- ✅ Example projects generate successfully

### **Performance Targets**
- Simple project: <30s generation time
- Medium project: <2min generation time
- Complex project: <5min generation time

### **Functional Requirements**
- ✅ Correctly analyzes automation intent
- ✅ Generates valid project structure
- ✅ Delegates to appropriate subagents
- ✅ Validates generated code
- ✅ Persists decisions to memory
- ✅ Tracks metrics accurately

---

## 🚨 **Known Gotchas & Considerations**

### **1. Context Management**
**Issue**: Long orchestration workflows may hit token limits

**Solution**:
- Use context editing (automatic with Sonnet 4.5)
- Store critical info in memory, not context
- Clear temporary data after each phase

### **2. Parallel Subagent Coordination**
**Issue**: Subagents may have dependencies

**Solution**:
- Use `asyncio.gather()` only for truly independent tasks
- Sequence dependent tasks (requirements → code → tests → docs)
- Share state via memory, not context

### **3. Memory File Organization**
**Issue**: Memory directory can get cluttered

**Solution**:
- Use structured naming: `{type}_{timestamp}.md`
- Implement cleanup for old decisions
- Regular archival of completed projects

### **4. Error Propagation**
**Issue**: Subagent failures may not bubble up

**Solution**:
- Wrap all subagent calls in try/except
- Log errors to memory
- Continue with degraded functionality if possible
- Report all errors in validation phase

### **5. API Rate Limiting**
**Issue**: Multiple parallel subagents may hit rate limits

**Solution**:
- Implement backoff retry logic
- Queue requests if needed
- Monitor usage in metrics

---

## 📚 **References & Resources**

### **Official Documentation**
- [Claude Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview)
- [Python SDK Reference](https://docs.claude.com/en/api/agent-sdk/python)
- [Custom Tools Guide](https://docs.claude.com/en/api/agent-sdk/custom-tools)
- [Subagents Documentation](https://docs.claude.com/en/api/agent-sdk/subagents)
- [Memory Tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool)
- [Context Editing](https://docs.claude.com/en/docs/build-with-claude/context-editing)

### **Code Examples**
- [Memory Cookbook](https://github.com/anthropics/claude-cookbooks/blob/main/tool_use/memory_cookbook.ipynb)
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)

### **External Research**
- [Pydantic AI Documentation](https://ai.pydantic.dev/)
- [AsyncIO Patterns](https://docs.python.org/3/library/asyncio.html)
- [Pytest Async Testing](https://pytest-asyncio.readthedocs.io/)

### **Related PRPs**
- Check existing PRPs in `PRPs/` directory for patterns
- Reference `PRPs/templates/` for PRP structure

---

## ✅ **PRP Quality Score**

**Confidence Level: 8.5/10**

**Strengths**:
- ✅ Comprehensive research and documentation references
- ✅ Clear implementation blueprint with code examples
- ✅ Detailed testing strategy with validation gates
- ✅ Memory management and context handling planned
- ✅ Known gotchas documented with solutions
- ✅ Realistic task breakdown and timeline

**Areas for Improvement**:
- ⚠️ Complex orchestration logic may need iteration
- ⚠️ Subagent coordination patterns need real-world validation
- ⚠️ Performance optimization may require tuning

**Recommendation**: Proceed with implementation. High confidence in one-pass success with potential for minor adjustments in subagent coordination logic.

---

*PRP Created: 2025-10-03*
*Target Implementation: 3-4 days*
*Estimated Lines of Code: ~2000 (excluding tests)*
*Test Coverage Target: >80%*
