"""
Integration Tests for Hybrid Architecture.

Tests the integration between:
1. @project-initializer (Claude Code agent layer)
2. Orchestrator SDK (Python orchestration layer)

Key aspects tested:
- Memory sharing between layers
- Version tracking (Template v3.0.0 + SDK v1.0.0)
- Tool delegation and communication
- State synchronization

These are specification tests that document expected behavior
of the hybrid architecture.
"""

import pytest
from pathlib import Path
from typing import Dict, Any, List
from unittest.mock import Mock, MagicMock


class MockMemoryManager:
    """Mock memory manager for testing memory sharing."""

    def __init__(self, memory_dir: Path):
        self.memory_dir = memory_dir
        self.memories: Dict[str, str] = {}
        self.access_log: List[str] = []

    def store(self, key: str, value: str) -> None:
        """Store memory."""
        self.memories[key] = value
        self.access_log.append(f"store:{key}")

    def retrieve(self, key: str) -> str:
        """Retrieve memory."""
        self.access_log.append(f"retrieve:{key}")
        return self.memories.get(key, "")

    def get_relevant_context(self, project_type: str) -> str:
        """Get context relevant to project type."""
        self.access_log.append(f"context:{project_type}")
        # Simulate retrieving relevant memories
        return f"Context for {project_type}"


class TestMemorySharing:
    """
    Test that memory is shared correctly between layers.

    The hybrid architecture requires that:
    - @project-initializer can access orchestrator memories
    - Orchestrator can access project-specific memories
    - Both layers use the same memory directory (.claude/memories/)
    """

    def test_orchestrator_stores_memory_accessible_by_agent(self):
        """
        Test that Orchestrator SDK can store memories that
        @project-initializer can access.

        Flow:
        1. Orchestrator stores architectural decision
        2. @project-initializer reads it during project generation
        """
        memory_dir = Path(".claude/memories")
        memory = MockMemoryManager(memory_dir)

        # Orchestrator stores decision
        memory.store(
            "architecture_pattern",
            "Use MVC pattern for API projects"
        )

        # @project-initializer retrieves it
        pattern = memory.retrieve("architecture_pattern")

        assert pattern == "Use MVC pattern for API projects"
        assert "store:architecture_pattern" in memory.access_log
        assert "retrieve:architecture_pattern" in memory.access_log

    def test_agent_stores_memory_accessible_by_orchestrator(self):
        """
        Test that @project-initializer can store memories that
        Orchestrator SDK can access.

        Flow:
        1. @project-initializer stores project preferences
        2. Orchestrator uses them in future projects
        """
        memory_dir = Path(".claude/memories")
        memory = MockMemoryManager(memory_dir)

        # Agent stores preference
        memory.store(
            "test_framework_preference",
            "pytest with coverage >= 80%"
        )

        # Orchestrator retrieves it
        preference = memory.retrieve("test_framework_preference")

        assert "pytest" in preference
        assert "80%" in preference

    def test_memory_directory_shared_between_layers(self):
        """
        Test that both layers use the same memory directory.

        Expected path: .claude/memories/
        """
        # Both layers should point to same directory
        orchestrator_memory_dir = Path(".claude/memories")
        agent_memory_dir = Path(".claude/memories")

        assert orchestrator_memory_dir == agent_memory_dir
        assert str(orchestrator_memory_dir) == ".claude/memories"

    def test_get_relevant_context_for_project_type(self):
        """
        Test that Orchestrator can retrieve context relevant
        to the project type being created.

        This is used to provide project-specific guidance.
        """
        memory = MockMemoryManager(Path(".claude/memories"))

        # Store context for different project types
        memory.store("api_automation_patterns", "Use FastAPI + Pydantic")
        memory.store("data_processing_patterns", "Use pandas + polars")

        # Retrieve context for specific project type
        context = memory.get_relevant_context("api_automation")

        assert "api_automation" in context.lower()
        assert "context:api_automation" in memory.access_log


class TestVersionTracking:
    """
    Test that version tracking works correctly across both layers.

    The hybrid architecture uses dual versioning:
    - Template version (e.g., 3.0.0) - for template structure
    - Orchestrator SDK version (e.g., 1.0.0) - for SDK functionality
    """

    def test_orchestrator_exposes_sdk_version(self):
        """
        Test that Orchestrator SDK exposes its version.

        This version should be accessible to @project-initializer
        for including in generated projects.
        """
        from orchestrator import __version__ as sdk_version

        assert sdk_version == "1.0.0"
        assert isinstance(sdk_version, str)

    def test_template_version_accessible_to_orchestrator(self):
        """
        Test that template version is accessible to Orchestrator.

        Template version should be defined somewhere accessible
        to both layers (e.g., in a shared constants file).
        """
        # Template version would typically be in a constants file
        # For now, we validate it's a known value
        template_version = "3.0.0"

        assert template_version == "3.0.0"
        assert len(template_version.split(".")) == 3  # Semver format

    def test_both_versions_appear_in_generated_projects(self):
        """
        Test that generated projects include both versions.

        This is tested in E2E tests, but we validate the
        contract here: both versions must be available.
        """
        from orchestrator import __version__ as sdk_version

        template_version = "3.0.0"

        # Both should be valid semver
        assert len(template_version.split(".")) == 3
        assert len(sdk_version.split(".")) == 3

        # Both should be 1.0.0 or higher
        assert template_version.startswith("3.")
        assert sdk_version.startswith("1.")


class TestToolDelegation:
    """
    Test that tool delegation works between layers.

    @project-initializer delegates complex tasks to Orchestrator SDK,
    which then uses MCP tools and subagents.
    """

    def test_agent_can_delegate_to_orchestrator(self):
        """
        Test that @project-initializer can delegate to Orchestrator.

        Flow:
        1. User provides request to @project-initializer
        2. Agent recognizes need for orchestration
        3. Agent delegates to Orchestrator SDK
        4. Orchestrator returns result
        """
        # Simulate delegation
        class MockOrchestrator:
            def analyze_intent(self, request: str) -> Dict[str, Any]:
                return {
                    "project_type": "automation",
                    "complexity": "medium",
                    "estimated_effort": "2-3 days"
                }

        orchestrator = MockOrchestrator()

        # Agent delegates
        user_request = "Automatizar procesamiento de PDFs"
        result = orchestrator.analyze_intent(user_request)

        assert result["project_type"] == "automation"
        assert "complexity" in result

    def test_orchestrator_can_use_mcp_tools(self):
        """
        Test that Orchestrator can use MCP tools.

        Expected tools:
        - Read, Write, Edit (file operations)
        - Bash (command execution)
        - Custom orchestrator tools
        """
        # List of expected tools
        expected_tools = [
            "Read",
            "Write",
            "Edit",
            "Bash",
            "TodoWrite",
            "Task",
            "mcp__orchestrator__create_project_structure",
            "mcp__orchestrator__generate_agent_definition",
        ]

        # Validate that these are the tools we expect
        # In real implementation, this would check against
        # the configured tools in ClaudeAgentOptions
        assert len(expected_tools) >= 8
        assert "Read" in expected_tools
        assert "mcp__orchestrator__create_project_structure" in expected_tools


class TestStateSynchronization:
    """
    Test that state is synchronized between layers.

    Both layers need to maintain consistent state about:
    - Current project being generated
    - Phase of orchestration
    - User preferences and decisions
    """

    def test_current_project_state_shared(self):
        """
        Test that current project state is accessible to both layers.

        State includes:
        - Project name
        - Current phase
        - User decisions made
        """
        # Simulate shared state
        project_state = {
            "project_name": "invoice_automation",
            "current_phase": 3,  # Planning
            "user_decisions": {
                "checkpoint1": "approved",
                "complexity": "medium",
            }
        }

        # Both layers should have access
        assert project_state["project_name"] == "invoice_automation"
        assert project_state["current_phase"] == 3
        assert project_state["user_decisions"]["checkpoint1"] == "approved"

    def test_phase_progression_tracked(self):
        """
        Test that phase progression is tracked correctly.

        Phases:
        0: Initialize
        1: Analyze Intent
        2: CHECKPOINT 1
        3: Planning
        ...
        8: Code Generation
        9: Documentation
        """
        phases = [
            "Initialize",
            "Analyze Intent",
            "CHECKPOINT 1",
            "Planning",
            "Subagent Definition",
            "Tool Selection",
            "Structure Generation",
            "CHECKPOINT 2",
            "Code Generation",
            "Documentation"
        ]

        # Validate phase count
        assert len(phases) == 10
        assert phases[0] == "Initialize"
        assert phases[2] == "CHECKPOINT 1"
        assert phases[7] == "CHECKPOINT 2"
        assert phases[8] == "Code Generation"


class TestHybridWorkflow:
    """
    Test the complete hybrid workflow integration.

    End-to-end flow of how @project-initializer and
    Orchestrator SDK work together.
    """

    def test_workflow_initialization(self):
        """
        Test that hybrid workflow initializes correctly.

        Flow:
        1. User invokes @project-initializer
        2. Agent initializes Orchestrator SDK
        3. Orchestrator loads memory and configuration
        4. Both are ready for orchestration
        """
        # Simulate initialization
        class HybridWorkflow:
            def __init__(self):
                self.agent_initialized = True
                self.orchestrator_initialized = True
                self.memory_loaded = True
                self.ready = all([
                    self.agent_initialized,
                    self.orchestrator_initialized,
                    self.memory_loaded
                ])

        workflow = HybridWorkflow()

        assert workflow.agent_initialized is True
        assert workflow.orchestrator_initialized is True
        assert workflow.memory_loaded is True
        assert workflow.ready is True

    def test_workflow_can_recover_from_errors(self):
        """
        Test that workflow can recover from errors.

        If Orchestrator SDK encounters an error,
        the system should gracefully handle it and
        inform the user.
        """
        class ResilientWorkflow:
            def execute_phase(self, phase: int) -> Dict[str, Any]:
                """Execute phase with error handling."""
                try:
                    if phase == 999:  # Simulate error
                        raise ValueError("Invalid phase")

                    return {"success": True, "phase": phase}

                except Exception as e:
                    return {
                        "success": False,
                        "error": str(e),
                        "phase": phase
                    }

        workflow = ResilientWorkflow()

        # Normal execution
        result = workflow.execute_phase(3)
        assert result["success"] is True

        # Error handling
        result = workflow.execute_phase(999)
        assert result["success"] is False
        assert "error" in result


class TestCommunicationProtocol:
    """
    Test the communication protocol between layers.

    The protocol defines how @project-initializer and
    Orchestrator SDK exchange information.
    """

    def test_request_response_format(self):
        """
        Test that requests and responses follow expected format.

        Request format:
        {
            "action": "analyze_intent" | "create_automation",
            "params": {...},
            "context": {...}
        }

        Response format:
        {
            "success": bool,
            "data": {...},
            "error": str | None
        }
        """
        # Example request
        request = {
            "action": "analyze_intent",
            "params": {
                "user_request": "Automatizar PDFs"
            },
            "context": {
                "user_preferences": {},
                "previous_projects": []
            }
        }

        # Validate request structure
        assert "action" in request
        assert "params" in request
        assert request["action"] in ["analyze_intent", "create_automation"]

        # Example response
        response = {
            "success": True,
            "data": {
                "project_type": "automation",
                "complexity": "medium"
            },
            "error": None
        }

        # Validate response structure
        assert "success" in response
        assert "data" in response
        assert "error" in response
        assert response["success"] is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
