"""
Pydantic models for orchestrator agent.

This module defines the data models used for intent analysis,
project structure, and orchestration workflow.
"""

from typing import List, Dict, Any, Optional, Literal
from pydantic import BaseModel, Field


class AutomationIntent(BaseModel):
    """
    Structured representation of user's automation intent.

    This model is populated via structured output from Claude
    to extract actionable information from vague user requests.
    """

    project_name: str = Field(
        description="Derived project name (kebab-case)"
    )

    project_type: Literal[
        "api_automation",
        "data_processing",
        "workflow_automation",
        "testing_automation",
        "documentation_automation",
        "general_automation"
    ] = Field(
        description="Type of automation project"
    )

    main_objective: str = Field(
        description="Clear statement of what needs to be automated"
    )

    key_requirements: List[str] = Field(
        description="List of specific requirements extracted from user request",
        min_length=1
    )

    required_integrations: List[str] = Field(
        default_factory=list,
        description="External services or APIs that need integration (e.g., 'n8n', 'database', 'email')"
    )

    required_agents: List[str] = Field(
        description="List of specialized agents needed (e.g., 'requirements_analyst', 'code_generator')",
        min_length=1
    )

    complexity_level: Literal["low", "medium", "high"] = Field(
        description="Estimated complexity of the automation"
    )

    estimated_duration: str = Field(
        description="Estimated implementation duration (e.g., '2-3 days')"
    )

    additional_notes: Optional[str] = Field(
        default=None,
        description="Any clarifications or edge cases to consider"
    )


class AgentConfig(BaseModel):
    """Configuration for a specialized subagent."""

    name: str = Field(
        description="Agent name (snake_case)"
    )

    description: str = Field(
        description="When to use this agent"
    )

    prompt: str = Field(
        description="System prompt defining agent behavior"
    )

    tools: List[str] = Field(
        description="List of allowed tools for this agent"
    )

    model: Literal["sonnet", "opus", "haiku", "inherit"] = Field(
        default="sonnet",
        description="Claude model to use"
    )


class FileDefinition(BaseModel):
    """Definition of a file to be created in the project."""

    path: str = Field(
        description="Relative path from project root"
    )

    content: str = Field(
        description="File content"
    )

    file_type: Literal[
        "python",
        "markdown",
        "json",
        "yaml",
        "text",
        "config"
    ] = Field(
        description="Type of file"
    )


class ProjectStructure(BaseModel):
    """
    Complete project structure to be generated.

    This model represents the full automation project that will
    be created based on the user's intent.
    """

    project_name: str = Field(
        description="Project name (kebab-case)"
    )

    project_type: str = Field(
        description="Type of automation project"
    )

    directories: List[str] = Field(
        description="List of directories to create (relative paths)"
    )

    files: List[FileDefinition] = Field(
        description="Files to create with content"
    )

    agents: List[AgentConfig] = Field(
        description="Specialized agents to create"
    )

    dependencies: Dict[str, str] = Field(
        default_factory=dict,
        description="Python package dependencies (name: version)"
    )

    environment_variables: Dict[str, str] = Field(
        default_factory=dict,
        description="Required environment variables (name: description)"
    )

    documentation: Dict[str, str] = Field(
        default_factory=dict,
        description="Documentation files (filename: content)"
    )


class ValidationResult(BaseModel):
    """Result of project validation."""

    is_valid: bool = Field(
        description="Whether the project passed validation"
    )

    errors: List[str] = Field(
        default_factory=list,
        description="List of validation errors"
    )

    warnings: List[str] = Field(
        default_factory=list,
        description="List of validation warnings"
    )

    quality_score: float = Field(
        ge=0.0,
        le=10.0,
        description="Overall quality score (0-10)"
    )

    recommendations: List[str] = Field(
        default_factory=list,
        description="Recommendations for improvement"
    )


class OrchestrationResult(BaseModel):
    """
    Final result of the orchestration workflow.

    This is returned to the user after complete project generation.
    """

    success: bool = Field(
        description="Whether the orchestration succeeded"
    )

    project_path: Optional[str] = Field(
        default=None,
        description="Path to the generated project"
    )

    intent: AutomationIntent = Field(
        description="Analyzed user intent"
    )

    structure: Optional[ProjectStructure] = Field(
        default=None,
        description="Generated project structure"
    )

    validation: Optional[ValidationResult] = Field(
        default=None,
        description="Validation results"
    )

    error: Optional[str] = Field(
        default=None,
        description="Error message if orchestration failed"
    )

    execution_time_seconds: float = Field(
        description="Total execution time"
    )

    artifacts: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional artifacts (logs, metrics, etc.)"
    )


class MemoryEntry(BaseModel):
    """Entry for persistent memory storage."""

    key: str = Field(
        description="Unique identifier for this memory"
    )

    value: str = Field(
        description="Memory content"
    )

    category: Literal[
        "architectural_decision",
        "pattern",
        "learned_preference",
        "error_solution",
        "integration_config"
    ] = Field(
        description="Category of memory"
    )

    timestamp: str = Field(
        description="ISO 8601 timestamp"
    )

    relevance_score: float = Field(
        ge=0.0,
        le=1.0,
        default=1.0,
        description="How relevant this memory is (decays over time)"
    )
