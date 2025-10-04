"""
Orchestrator Agent for Automation Project Generation.

This package provides a complete orchestration system for generating
automation projects based on user requests using Claude Agent SDK.

Main components:
- OrchestratorAgent: Main agent class
- Models: Pydantic models for data structures
- MemoryManager: Persistent memory across sessions
- OrchestrationWorkflow: Workflow coordination
- Specialized subagents: requirements_analyst, code_generator, test_writer, etc.

Example usage:
    >>> from orchestrator import OrchestratorAgent
    >>>
    >>> orchestrator = OrchestratorAgent()
    >>> result = await orchestrator.create_automation(
    ...     "Quiero automatizar el procesamiento de facturas PDF"
    ... )
    >>> print(f"Project created at: {result.project_path}")
"""

# Version must be defined before imports to allow importing without dependencies
__version__ = "1.0.0"
__version_info__ = (1, 0, 0)

# Conditional imports to allow importing version without all dependencies
try:
    from .agent import OrchestratorAgent
    from .models import (
        AutomationIntent,
        ProjectStructure,
        ValidationResult,
        OrchestrationResult,
        FileDefinition,
        AgentConfig,
        MemoryEntry
    )
    from .memory import MemoryManager
    from .workflow import OrchestrationWorkflow
except ImportError:
    # Allow importing __version__ even when dependencies aren't installed
    pass

__all__ = [
    "OrchestratorAgent",
    "AutomationIntent",
    "ProjectStructure",
    "ValidationResult",
    "OrchestrationResult",
    "FileDefinition",
    "AgentConfig",
    "MemoryEntry",
    "MemoryManager",
    "OrchestrationWorkflow"
]
