"""
Main orchestrator agent for automation project generation.

This module implements the core OrchestratorAgent class that uses
Claude Agent SDK to interpret user requests and generate complete
automation projects.
"""

import asyncio
import json
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

# Conditional import for Claude Agent SDK
# When SDK is not available, provide minimal stub for testing
try:
    from claude_agent_sdk import (
        ClaudeSDKClient,
        ClaudeAgentOptions,
        AgentDefinition
    )
    SDK_AVAILABLE = True
except ImportError:
    SDK_AVAILABLE = False
    # Create type stubs for when SDK is not available
    ClaudeSDKClient = None
    ClaudeAgentOptions = None
    AgentDefinition = None

# Conditional imports for orchestrator components
# These may also fail if dependencies are missing
try:
    from .models import (
        AutomationIntent,
        ProjectStructure,
        ValidationResult,
        OrchestrationResult
    )
    from .memory import MemoryManager
    from .tools import create_orchestrator_tools
    from .subagents import get_subagent_definitions
    from .workflow import OrchestrationWorkflow
    COMPONENTS_AVAILABLE = True
except ImportError:
    COMPONENTS_AVAILABLE = False
    # Create minimal stubs
    AutomationIntent = None
    ProjectStructure = None
    ValidationResult = None
    OrchestrationResult = None
    MemoryManager = None


class OrchestratorAgent:
    """
    Main orchestrator agent for automation project generation.

    This agent uses Claude Agent SDK to:
    1. Analyze user intent via structured output
    2. Generate complete project structure
    3. Delegate work to specialized subagents
    4. Validate and document the generated project

    Example:
        >>> orchestrator = OrchestratorAgent()
        >>> result = await orchestrator.create_automation(
        ...     "Quiero automatizar el procesamiento de facturas PDF"
        ... )
        >>> print(result.project_path)
    """

    VERSION = "1.0.0"

    def __init__(
        self,
        working_dir: Optional[Path] = None,
        memory_dir: Optional[Path] = None
    ):
        """
        Initialize the orchestrator agent.

        Args:
            working_dir: Base directory for generating projects (default: current dir)
            memory_dir: Directory for persistent memory (default: .claude/memories)
        """
        self.working_dir = working_dir or Path.cwd()

        # Only initialize components if available
        if COMPONENTS_AVAILABLE:
            self.memory = MemoryManager(
                memory_dir or Path(".claude/memories")
            )
        else:
            self.memory = None

        # Will be set during orchestration
        self.client = None
        self.workflow = None

    def get_version(self) -> str:
        """
        Get the current version of the Orchestrator Agent SDK.

        Returns:
            str: Version string in semver format (e.g., "1.0.0")
        """
        return self.VERSION

    def _check_sdk_available(self) -> None:
        """
        Check if Claude Agent SDK is available.

        Raises:
            RuntimeError: If SDK is not available
        """
        if not SDK_AVAILABLE:
            raise RuntimeError(
                "Claude Agent SDK is not installed. "
                "This is expected during development. "
                "Full functionality requires claude_agent_sdk package."
            )

    def _check_components_available(self) -> None:
        """
        Check if orchestrator components are available.

        Raises:
            RuntimeError: If components are not available
        """
        if not COMPONENTS_AVAILABLE:
            raise RuntimeError(
                "Orchestrator components are not available. "
                "Some dependencies may be missing."
            )

    def _get_orchestrator_prompt(self) -> str:
        """
        Get the system prompt for the orchestrator agent.

        This defines the agent's role and behavior.
        """
        return """
You are an expert orchestrator agent specialized in creating complete automation projects.

Your role:
1. Analyze user requests to understand what they want to automate
2. Design appropriate project structure with necessary agents and tools
3. Generate all required code, tests, and documentation
4. Ensure the project follows best practices and is production-ready

Guidelines:
- Always start by analyzing the user's intent with structured output
- Break down complex automations into specialized subagents
- Generate complete, working code - never use placeholders or TODOs
- Include comprehensive tests for all functionality
- Create clear documentation explaining how to use the automation
- Follow the project's coding standards and patterns
- Store architectural decisions in memory for future projects

When uncertain, ask clarifying questions before proceeding.
When you make architectural decisions, store them in memory.
"""

    def _build_options(self):
        """
        Build ClaudeAgentOptions for the orchestrator.

        Returns:
            Configured options for ClaudeSDKClient

        Raises:
            RuntimeError: If SDK is not available
        """
        self._check_sdk_available()
        self._check_components_available()

        return ClaudeAgentOptions(
            # Use claude_code preset with orchestrator-specific instructions
            system_prompt={
                "type": "preset",
                "preset": "claude_code",
                "append": self._get_orchestrator_prompt()
            },

            # Define specialized subagents
            agents=get_subagent_definitions(),

            # Add custom MCP tools for project generation
            mcp_servers={
                "orchestrator": create_orchestrator_tools(
                    working_dir=self.working_dir,
                    memory=self.memory
                )
            },

            # Configure allowed tools
            allowed_tools=[
                # Core tools
                "Read", "Write", "Edit", "Glob", "Grep", "Bash",
                # MCP tools (will be prefixed with mcp__orchestrator__)
                "mcp__orchestrator__create_project_structure",
                "mcp__orchestrator__generate_agent_definition",
                "mcp__orchestrator__generate_documentation",
                "mcp__orchestrator__validate_project",
                # Memory tool
                "memory",
                # Todo tracking
                "TodoWrite",
                # Subagent delegation
                "Task"
            ],

            # Permission mode
            permission_mode='acceptEdits',

            # Load project configuration
            setting_sources=['project', 'local'],

            # Model selection
            model='sonnet'  # Use Sonnet 4.5 for orchestration
        )

    async def create_automation(
        self,
        user_request: str,
        additional_context: Optional[str] = None
    ) -> OrchestrationResult:
        """
        Create a complete automation project from user request.

        This is the main entry point for the orchestrator.

        Args:
            user_request: User's description of what they want to automate
            additional_context: Optional additional context or requirements

        Returns:
            OrchestrationResult with success status and project details

        Example:
            >>> orchestrator = OrchestratorAgent()
            >>> result = await orchestrator.create_automation(
            ...     user_request="Automatizar generaci�n de reportes semanales",
            ...     additional_context="Los reportes deben enviarse por email"
            ... )
            >>> if result.success:
            ...     print(f"Project created at: {result.project_path}")
            ... else:
            ...     print(f"Error: {result.error}")
        """
        self._check_sdk_available()
        self._check_components_available()

        start_time = datetime.now()

        try:
            # Build options
            options = self._build_options()

            # Create workflow
            self.workflow = OrchestrationWorkflow(
                memory=self.memory,
                working_dir=self.working_dir
            )

            # Execute orchestration workflow
            async with ClaudeSDKClient(options=options) as client:
                self.client = client

                # Pass client to workflow
                self.workflow.client = client

                # Execute workflow
                result = await self.workflow.execute(
                    user_request=user_request,
                    additional_context=additional_context
                )

                # Calculate execution time
                execution_time = (datetime.now() - start_time).total_seconds()
                result.execution_time_seconds = execution_time

                return result

        except Exception as e:
            # Handle errors gracefully
            execution_time = (datetime.now() - start_time).total_seconds()

            return OrchestrationResult(
                success=False,
                intent=None,  # Intent analysis may have failed
                structure=None,
                validation=None,
                error=str(e),
                execution_time_seconds=execution_time,
                artifacts={"error_type": type(e).__name__}
            )

    async def analyze_intent(self, user_request: str) -> AutomationIntent:
        """
        Analyze user intent with structured output.

        This method can be used standalone to understand what the user wants
        without generating a full project.

        Args:
            user_request: User's request

        Returns:
            Structured AutomationIntent

        Example:
            >>> intent = await orchestrator.analyze_intent(
            ...     "Necesito procesar PDFs y extraer datos"
            ... )
            >>> print(intent.project_type)
            'data_processing'
            >>> print(intent.required_agents)
            ['requirements_analyst', 'code_generator']
        """
        self._check_sdk_available()
        self._check_components_available()

        options = self._build_options()

        async with ClaudeSDKClient(options=options) as client:
            # Use structured output to extract intent
            await client.query(
                f"""Analyze this automation request and extract structured information:

{user_request}

Please provide a structured analysis using AutomationIntent format."""
            )

            # Process response
            async for message in client.receive_response():
                if hasattr(message, 'structured_output'):
                    # Parse structured output
                    intent_data = message.structured_output
                    return AutomationIntent(**intent_data)

            # Fallback: parse from text response
            raise ValueError("Failed to extract structured intent")

    async def validate_project(
        self,
        project_path: Path
    ) -> ValidationResult:
        """
        Validate a generated project.

        Args:
            project_path: Path to the project to validate

        Returns:
            ValidationResult with validation details

        Example:
            >>> result = await orchestrator.validate_project(
            ...     Path("./generated-project")
            ... )
            >>> if not result.is_valid:
            ...     for error in result.errors:
            ...         print(f"Error: {error}")
        """
        self._check_components_available()

        if not self.workflow:
            self.workflow = OrchestrationWorkflow(
                memory=self.memory,
                working_dir=self.working_dir
            )

        return await self.workflow.validate_project(project_path)

    def get_memory_context(self, project_type: str) -> str:
        """
        Get relevant memory context for a project type.

        Args:
            project_type: Type of project being created

        Returns:
            Formatted context string

        Example:
            >>> context = orchestrator.get_memory_context("api_automation")
            >>> print(context)
        """
        self._check_components_available()
        return self.memory.get_relevant_context(project_type)

    async def cleanup(self) -> None:
        """
        Cleanup resources.

        Should be called when done with the orchestrator.
        """
        if self.client:
            # Client will be closed by context manager
            pass
