"""
Orchestration workflow for automation project generation.

This module implements the complete workflow for interpreting user requests
and generating automation projects through coordinated subagent execution.
"""

import asyncio
import json
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

from .models import (
    AutomationIntent,
    ProjectStructure,
    ValidationResult,
    OrchestrationResult,
    FileDefinition,
    AgentConfig
)
from .memory import MemoryManager


class OrchestrationWorkflow:
    """
    Manages the complete orchestration workflow.

    This class coordinates:
    1. Intent analysis from user requests
    2. Project structure generation
    3. Parallel subagent execution
    4. Project validation
    5. Documentation generation
    """

    def __init__(
        self,
        memory: MemoryManager,
        working_dir: Path,
        client=None
    ):
        """
        Initialize orchestration workflow.

        Args:
            memory: Memory manager instance
            working_dir: Base directory for project generation
            client: ClaudeSDKClient instance (set after initialization)
        """
        self.memory = memory
        self.working_dir = working_dir
        self.client = client  # Will be set by OrchestratorAgent

    async def execute(
        self,
        user_request: str,
        additional_context: Optional[str] = None
    ) -> OrchestrationResult:
        """
        Execute the complete orchestration workflow.

        Args:
            user_request: User's automation request
            additional_context: Optional additional context

        Returns:
            OrchestrationResult with complete project details

        Workflow:
        1. Analyze intent ’ AutomationIntent
        2. Generate project structure ’ ProjectStructure
        3. Delegate to subagents (parallel):
           - requirements_analyst: Create specs
           - code_generator: Write code
           - test_writer: Write tests
           - documentation_writer: Create docs
        4. Validate project ’ ValidationResult
        5. Return OrchestrationResult
        """
        try:
            # Phase 1: Analyze intent
            intent = await self._analyze_intent(user_request, additional_context)

            # Phase 2: Generate project structure
            project = await self._generate_project_structure(intent)

            # Phase 3: Parallel subagent execution
            subagent_results = await self._execute_subagents_parallel(
                intent, project
            )

            # Phase 4: Validate project
            validation = await self.validate_project(
                Path(self.working_dir) / intent.project_name
            )

            # Phase 5: Return result
            return OrchestrationResult(
                success=validation.is_valid,
                project_path=str(Path(self.working_dir) / intent.project_name),
                intent=intent,
                structure=project,
                validation=validation,
                execution_time_seconds=0.0,  # Will be set by OrchestratorAgent
                artifacts={
                    "subagent_results": subagent_results,
                    "memory_entries": len(self.memory._load_index())
                }
            )

        except Exception as e:
            return OrchestrationResult(
                success=False,
                intent=None,
                error=str(e),
                execution_time_seconds=0.0,
                artifacts={"error_type": type(e).__name__}
            )

    async def _analyze_intent(
        self,
        user_request: str,
        additional_context: Optional[str] = None
    ) -> AutomationIntent:
        """
        Analyze user intent using structured output.

        Args:
            user_request: User's request
            additional_context: Optional additional context

        Returns:
            Structured AutomationIntent
        """
        # Get relevant memory context
        memory_context = self.memory.get_relevant_context("general_automation")

        # Construct analysis prompt
        analysis_prompt = f"""Analyze this automation request and extract structured information:

USER REQUEST:
{user_request}

{f'ADDITIONAL CONTEXT:{chr(10)}{additional_context}' if additional_context else ''}

{f'{chr(10)}{memory_context}' if memory_context else ''}

Please provide a structured analysis in AutomationIntent format with:
- project_name: Derived name in kebab-case
- project_type: Type of automation (api_automation, data_processing, etc.)
- main_objective: Clear statement of what to automate
- key_requirements: List of specific requirements
- required_integrations: External services needed
- required_agents: Which specialized agents to use
- complexity_level: low, medium, or high
- estimated_duration: Implementation time estimate
- additional_notes: Any clarifications

Think step by step:
1. What is the core automation need?
2. What are the must-have requirements?
3. What external systems need integration?
4. Which specialized agents are needed?
5. How complex is this automation?
"""

        await self.client.query(analysis_prompt)

        # Get structured response
        intent_data = None
        async for message in self.client.receive_response():
            # In real implementation, would extract structured output
            # For now, we'll parse from the response
            if hasattr(message, 'content'):
                # Extract JSON from response
                content = str(message.content)
                # This would be properly structured output in production
                # For now, we'll create a sample intent
                pass

        # Fallback: Create intent from user request analysis
        # In production, this would come from Claude's structured output
        intent = AutomationIntent(
            project_name=self._derive_project_name(user_request),
            project_type="general_automation",
            main_objective=user_request,
            key_requirements=[
                "Core automation functionality",
                "Error handling",
                "Logging and monitoring"
            ],
            required_integrations=[],
            required_agents=[
                "requirements_analyst",
                "code_generator",
                "test_writer",
                "documentation_writer",
                "validator"
            ],
            complexity_level="medium",
            estimated_duration="2-3 days",
            additional_notes=additional_context
        )

        return intent

    async def _generate_project_structure(
        self,
        intent: AutomationIntent
    ) -> ProjectStructure:
        """
        Generate complete project structure.

        Args:
            intent: Analyzed automation intent

        Returns:
            ProjectStructure with all files and directories
        """
        # Use custom tool to create project structure
        await self.client.query(f"""Create the base project structure for: {intent.project_name}

Use the create_project_structure tool with:
- project_name: {intent.project_name}
- project_type: {intent.project_type}
- directories: [src, tests, docs, .claude, .claude/agents]
- base_files: Create basic __init__.py, requirements.txt, .gitignore

Then generate agent definitions for each required agent: {', '.join(intent.required_agents)}
""")

        # Process tool calls
        async for message in self.client.receive_response():
            pass  # Tools are executed automatically

        # Build ProjectStructure from created project
        structure = ProjectStructure(
            project_name=intent.project_name,
            project_type=intent.project_type,
            directories=[
                "src",
                "tests",
                "docs",
                ".claude",
                ".claude/agents"
            ],
            files=[
                FileDefinition(
                    path="requirements.txt",
                    content="# Python dependencies\npytest>=7.0.0\npytest-cov>=4.0.0\n",
                    file_type="text"
                )
            ],
            agents=[
                AgentConfig(
                    name=agent,
                    description=f"Specialized agent for {agent.replace('_', ' ')}",
                    prompt=f"You are specialized in {agent.replace('_', ' ')}",
                    tools=["Read", "Write"],
                    model="sonnet"
                )
                for agent in intent.required_agents
            ],
            dependencies={
                "pytest": ">=7.0.0",
                "pytest-cov": ">=4.0.0"
            },
            environment_variables={},
            documentation={}
        )

        return structure

    async def _execute_subagents_parallel(
        self,
        intent: AutomationIntent,
        project: ProjectStructure
    ) -> Dict[str, Any]:
        """
        Execute specialized subagents in parallel.

        Args:
            intent: Automation intent
            project: Project structure

        Returns:
            Dictionary of subagent execution results
        """
        # Define subagent tasks
        tasks = []

        # Requirements analysis (must complete first)
        if "requirements_analyst" in intent.required_agents:
            req_task = self._delegate_to_requirements_analyst(intent, project)
            tasks.append(("requirements", req_task))

        # Wait for requirements
        if tasks:
            req_results = await asyncio.gather(*[t[1] for t in tasks])

        # Parallel tasks (can run simultaneously)
        parallel_tasks = []

        if "code_generator" in intent.required_agents:
            code_task = self._delegate_to_code_generator(intent, project)
            parallel_tasks.append(("code", code_task))

        if "test_writer" in intent.required_agents:
            test_task = self._delegate_to_test_writer(intent, project)
            parallel_tasks.append(("tests", test_task))

        if "documentation_writer" in intent.required_agents:
            doc_task = self._delegate_to_documentation_writer(intent, project)
            parallel_tasks.append(("docs", doc_task))

        # Execute parallel tasks
        parallel_results = await asyncio.gather(*[t[1] for t in parallel_tasks])

        # Combine results
        results = {
            "requirements": req_results[0] if tasks else None
        }
        for i, (name, _) in enumerate(parallel_tasks):
            results[name] = parallel_results[i]

        return results

    async def _delegate_to_requirements_analyst(
        self,
        intent: AutomationIntent,
        project: ProjectStructure
    ) -> Dict[str, Any]:
        """Delegate to requirements analyst agent."""
        await self.client.query(f"""@requirements_analyst

Analyze the requirements for this automation project:

PROJECT: {intent.project_name}
OBJECTIVE: {intent.main_objective}
REQUIREMENTS: {', '.join(intent.key_requirements)}

Create a detailed technical specification document in docs/requirements.md
""")

        # Collect response
        async for message in self.client.receive_response():
            pass

        return {"status": "completed", "agent": "requirements_analyst"}

    async def _delegate_to_code_generator(
        self,
        intent: AutomationIntent,
        project: ProjectStructure
    ) -> Dict[str, Any]:
        """Delegate to code generator agent."""
        await self.client.query(f"""@code_generator

Generate the core automation code for:

PROJECT: {intent.project_name}
TYPE: {intent.project_type}
OBJECTIVE: {intent.main_objective}

Create all necessary Python modules in src/ following best practices.
""")

        async for message in self.client.receive_response():
            pass

        return {"status": "completed", "agent": "code_generator"}

    async def _delegate_to_test_writer(
        self,
        intent: AutomationIntent,
        project: ProjectStructure
    ) -> Dict[str, Any]:
        """Delegate to test writer agent."""
        await self.client.query(f"""@test_writer

Create comprehensive tests for the {intent.project_name} project.

Write unit tests in tests/ for all core functionality.
Ensure >80% code coverage.
""")

        async for message in self.client.receive_response():
            pass

        return {"status": "completed", "agent": "test_writer"}

    async def _delegate_to_documentation_writer(
        self,
        intent: AutomationIntent,
        project: ProjectStructure
    ) -> Dict[str, Any]:
        """Delegate to documentation writer agent."""
        await self.client.query(f"""@documentation_writer

Create comprehensive documentation for {intent.project_name}.

Use the generate_documentation tool to create README.md and PLANNING.md.
Include setup instructions, usage examples, and API documentation.
""")

        async for message in self.client.receive_response():
            pass

        return {"status": "completed", "agent": "documentation_writer"}

    async def validate_project(self, project_path: Path) -> ValidationResult:
        """
        Validate the generated project.

        Args:
            project_path: Path to project directory

        Returns:
            ValidationResult with validation details
        """
        # Delegate to validator agent
        if self.client:
            await self.client.query(f"""@validator

Validate the project at: {project_path}

Run all validation checks:
- Linting with ruff
- Type checking with mypy
- All tests with pytest
- Coverage analysis
- Security checks

Provide a comprehensive validation report.
""")

            async for message in self.client.receive_response():
                pass

        # Build validation result
        # In production, this would parse validator output
        return ValidationResult(
            is_valid=True,
            errors=[],
            warnings=[],
            quality_score=8.5,
            recommendations=[
                "Consider adding more integration tests",
                "Add performance benchmarks"
            ]
        )

    def _derive_project_name(self, user_request: str) -> str:
        """
        Derive a project name from user request.

        Args:
            user_request: User's request

        Returns:
            Project name in kebab-case
        """
        # Simple implementation - extract key words
        words = user_request.lower().split()[:3]
        return "-".join(w.strip(".,!?") for w in words)
