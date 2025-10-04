"""
{{ project_name }} - Orchestrator Module

This module provides workflow orchestration capabilities.
Generated with Orchestrator Agent SDK Template.
"""

from .agent import {{ project_name|replace('-', '_')|replace(' ', '_')|title }}Orchestrator
from .models import WorkflowIntent, WorkflowResult

__all__ = [
    "{{ project_name|replace('-', '_')|replace(' ', '_')|title }}Orchestrator",
    "WorkflowIntent",
    "WorkflowResult",
]

__version__ = "{{ version|default('1.0.0') }}"
