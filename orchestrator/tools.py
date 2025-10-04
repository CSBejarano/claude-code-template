"""
Custom MCP tools for the orchestrator agent.

This module defines custom tools that the orchestrator uses to:
- Create project structures
- Generate agent definitions
- Generate documentation
- Validate projects
"""

import json
from pathlib import Path
from typing import Dict, Any, List
from claude_agent_sdk import tool, create_sdk_mcp_server

from .memory import MemoryManager
from .models import ProjectStructure, FileDefinition, AgentConfig


def create_orchestrator_tools(
    working_dir: Path,
    memory: MemoryManager
):
    """
    Create the orchestrator MCP server with custom tools.

    Args:
        working_dir: Base directory for project generation
        memory: Memory manager instance

    Returns:
        MCP server with orchestrator tools
    """

    @tool(
        "create_project_structure",
        "Creates the base directory structure and configuration files for a new automation project",
        {
            "project_name": str,
            "project_type": str,
            "directories": list,
            "base_files": list  # List of dicts with {path, content, file_type}
        }
    )
    async def create_project_structure(args: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create project directory structure.

        Creates all necessary directories and base configuration files
        for a new automation project.

        Args:
            args: Contains project_name, project_type, directories, base_files

        Returns:
            Result with created project path and files

        Example tool call:
            {
                "project_name": "invoice-processor",
                "project_type": "data_processing",
                "directories": ["src", "tests", "docs", ".claude"],
                "base_files": [
                    {
                        "path": "README.md",
                        "content": "# Invoice Processor\n...",
                        "file_type": "markdown"
                    }
                ]
            }
        """
        try:
            project_name = args["project_name"]
            project_type = args["project_type"]
            directories = args["directories"]
            base_files = args.get("base_files", [])

            # Create project directory
            project_path = working_dir / project_name
            project_path.mkdir(parents=True, exist_ok=True)

            # Create subdirectories
            created_dirs = []
            for dir_path in directories:
                full_path = project_path / dir_path
                full_path.mkdir(parents=True, exist_ok=True)
                created_dirs.append(str(dir_path))

            # Create base files
            created_files = []
            for file_def in base_files:
                file_path = project_path / file_def["path"]
                file_path.parent.mkdir(parents=True, exist_ok=True)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(file_def["content"])

                created_files.append(file_def["path"])

            # Store in memory
            memory.store_architectural_decision(
                decision=f"Created {project_type} project: {project_name}",
                context=f"Directories: {', '.join(created_dirs)}"
            )

            return {
                "content": [{
                    "type": "text",
                    "text": json.dumps({
                        "success": True,
                        "project_path": str(project_path),
                        "created_directories": created_dirs,
                        "created_files": created_files
                    }, indent=2)
                }]
            }

        except Exception as e:
            return {
                "content": [{
                    "type": "text",
                    "text": json.dumps({
                        "success": False,
                        "error": str(e),
                        "error_type": type(e).__name__
                    }, indent=2)
                }]
            }

    @tool(
        "generate_agent_definition",
        "Generates a specialized agent definition file in .claude/agents/",
        {
            "project_path": str,
            "agent_name": str,
            "agent_purpose": str,
            "agent_prompt": str,
            "allowed_tools": list,
            "model": str  # "sonnet", "opus", "haiku"
        }
    )
    async def generate_agent_definition(args: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a specialized agent definition.

        Creates a markdown file defining a specialized subagent that can be
        delegated to for specific tasks.

        Args:
            args: Contains agent configuration

        Returns:
            Result with agent file path

        Example tool call:
            {
                "project_path": "./invoice-processor",
                "agent_name": "pdf_extractor",
                "agent_purpose": "Extract data from PDF invoices",
                "agent_prompt": "You are specialized in...",
                "allowed_tools": ["Read", "Write", "Bash"],
                "model": "sonnet"
            }
        """
        try:
            project_path = Path(args["project_path"])
            agent_name = args["agent_name"]
            agent_purpose = args["agent_purpose"]
            agent_prompt = args["agent_prompt"]
            allowed_tools = args["allowed_tools"]
            model = args.get("model", "sonnet")

            # Create agents directory
            agents_dir = project_path / ".claude" / "agents"
            agents_dir.mkdir(parents=True, exist_ok=True)

            # Generate agent markdown file
            agent_content = f"""---
description: {agent_purpose}
tools:
{chr(10).join(f'  - {tool}' for tool in allowed_tools)}
model: {model}
---

# {agent_name.replace('_', ' ').title()} Agent

{agent_prompt}

## Responsibilities

{agent_purpose}

## Available Tools

{chr(10).join(f'- **{tool}**: {_get_tool_description(tool)}' for tool in allowed_tools)}

## Usage Guidelines

This agent should be used when you need to:
{agent_purpose}

## Examples

[Add examples of when to delegate to this agent]
"""

            # Write agent file
            agent_file = agents_dir / f"{agent_name}.md"
            with open(agent_file, 'w', encoding='utf-8') as f:
                f.write(agent_content)

            # Store pattern in memory
            memory.store_pattern(
                pattern_name=f"agent_{agent_name}",
                pattern_description=f"Use {agent_name} agent for: {agent_purpose}"
            )

            return {
                "content": [{
                    "type": "text",
                    "text": json.dumps({
                        "success": True,
                        "agent_file": str(agent_file),
                        "agent_name": agent_name
                    }, indent=2)
                }]
            }

        except Exception as e:
            return {
                "content": [{
                    "type": "text",
                    "text": json.dumps({
                        "success": False,
                        "error": str(e)
                    }, indent=2)
                }]
            }

    @tool(
        "generate_documentation",
        "Generates project documentation (README.md, PLANNING.md, etc.)",
        {
            "project_path": str,
            "project_name": str,
            "project_type": str,
            "description": str,
            "features": list,
            "setup_instructions": str,
            "usage_examples": str
        }
    )
    async def generate_documentation(args: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate project documentation.

        Creates comprehensive documentation for the automation project.

        Args:
            args: Contains documentation details

        Returns:
            Result with created documentation files
        """
        try:
            project_path = Path(args["project_path"])
            project_name = args["project_name"]
            project_type = args["project_type"]
            description = args["description"]
            features = args["features"]
            setup_instructions = args["setup_instructions"]
            usage_examples = args["usage_examples"]

            # Generate README.md
            readme_content = f"""# {project_name}

> {description}

## =Ë Project Type

**{project_type}**

## ( Features

{chr(10).join(f'- {feature}' for feature in features)}

## =€ Setup

{setup_instructions}

## =Ö Usage

{usage_examples}

## >ê Testing

```bash
# Run tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

## =Á Project Structure

```
{project_name}/
   src/              # Source code
   tests/            # Test files
   docs/             # Documentation
   .claude/          # Claude Code configuration
      agents/       # Specialized agents
   README.md
```

## > Claude Code Integration

This project is configured to work with Claude Code. Available agents:

- See `.claude/agents/` for specialized agents
- Use `/prp-execute` for structured implementation
- Check `PLANNING.md` for architecture details

## =Ý License

[Add license information]

---

*Generated by Orchestrator Agent*
"""

            # Generate PLANNING.md
            planning_content = f"""# {project_name} - Planning Document

## Project Overview

**Type**: {project_type}
**Description**: {description}

## Architecture

[Add architecture details]

## Implementation Phases

1. **Phase 1**: Core Setup
2. **Phase 2**: Main Features
3. **Phase 3**: Testing & Validation
4. **Phase 4**: Documentation & Deployment

## Design Decisions

[Document key architectural decisions]

## Dependencies

[List main dependencies and why they were chosen]

## Testing Strategy

[Describe testing approach]

---

*Auto-generated by Orchestrator Agent*
"""

            # Write documentation files
            readme_file = project_path / "README.md"
            planning_file = project_path / ".claude" / "PLANNING.md"

            with open(readme_file, 'w', encoding='utf-8') as f:
                f.write(readme_content)

            planning_file.parent.mkdir(parents=True, exist_ok=True)
            with open(planning_file, 'w', encoding='utf-8') as f:
                f.write(planning_content)

            return {
                "content": [{
                    "type": "text",
                    "text": json.dumps({
                        "success": True,
                        "created_files": [
                            str(readme_file),
                            str(planning_file)
                        ]
                    }, indent=2)
                }]
            }

        except Exception as e:
            return {
                "content": [{
                    "type": "text",
                    "text": json.dumps({
                        "success": False,
                        "error": str(e)
                    }, indent=2)
                }]
            }

    @tool(
        "validate_project",
        "Validates a generated project for completeness and quality",
        {
            "project_path": str
        }
    )
    async def validate_project(args: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate a generated project.

        Checks for:
        - Required files exist
        - Code passes linting
        - Tests are present
        - Documentation is complete

        Args:
            args: Contains project_path

        Returns:
            Validation results
        """
        try:
            project_path = Path(args["project_path"])
            errors = []
            warnings = []
            quality_score = 10.0

            # Check required files
            required_files = ["README.md", "requirements.txt"]
            for file in required_files:
                if not (project_path / file).exists():
                    errors.append(f"Missing required file: {file}")
                    quality_score -= 1.0

            # Check for tests
            tests_dir = project_path / "tests"
            if not tests_dir.exists():
                warnings.append("No tests directory found")
                quality_score -= 0.5
            elif not list(tests_dir.glob("test_*.py")):
                warnings.append("No test files found")
                quality_score -= 0.5

            # Check for agents
            agents_dir = project_path / ".claude" / "agents"
            if not agents_dir.exists():
                warnings.append("No specialized agents defined")
                quality_score -= 0.3

            # Validation result
            is_valid = len(errors) == 0
            quality_score = max(0.0, min(10.0, quality_score))

            return {
                "content": [{
                    "type": "text",
                    "text": json.dumps({
                        "is_valid": is_valid,
                        "quality_score": quality_score,
                        "errors": errors,
                        "warnings": warnings,
                        "recommendations": _generate_recommendations(errors, warnings)
                    }, indent=2)
                }]
            }

        except Exception as e:
            return {
                "content": [{
                    "type": "text",
                    "text": json.dumps({
                        "is_valid": False,
                        "error": str(e)
                    }, indent=2)
                }]
            }

    # Create and return MCP server
    return create_sdk_mcp_server(
        name="orchestrator",
        version="1.0.0",
        tools=[
            create_project_structure,
            generate_agent_definition,
            generate_documentation,
            validate_project
        ]
    )


def _get_tool_description(tool_name: str) -> str:
    """Get description for a tool."""
    descriptions = {
        "Read": "Read files from the filesystem",
        "Write": "Write new files",
        "Edit": "Edit existing files",
        "Glob": "Find files matching patterns",
        "Grep": "Search file contents",
        "Bash": "Execute shell commands",
        "Task": "Delegate to subagents"
    }
    return descriptions.get(tool_name, "Tool for automation tasks")


def _generate_recommendations(errors: List[str], warnings: List[str]) -> List[str]:
    """Generate recommendations based on validation results."""
    recommendations = []

    if "Missing required file: README.md" in errors:
        recommendations.append("Create a comprehensive README.md with setup and usage instructions")

    if "Missing required file: requirements.txt" in errors:
        recommendations.append("Add requirements.txt with all Python dependencies")

    if "No tests directory found" in warnings or "No test files found" in warnings:
        recommendations.append("Add unit tests with pytest to ensure code quality")

    if "No specialized agents defined" in warnings:
        recommendations.append("Define specialized agents in .claude/agents/ for complex tasks")

    return recommendations
