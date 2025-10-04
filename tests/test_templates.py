"""
Test Template Rendering and Validation

Validates that all Jinja2 templates render correctly with sample data.
"""

import pytest
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from datetime import datetime
import tempfile
import shutil


@pytest.fixture
def template_env():
    """Setup Jinja2 environment for templates."""
    template_dir = Path(".claude/templates/")
    return Environment(loader=FileSystemLoader(template_dir))


@pytest.fixture
def sample_simple_intent():
    """Sample data for SIMPLE complexity project."""
    return {
        "project_name": "gmail-to-notion",
        "goal": "Automatizar emails de Gmail a Notion",
        "complexity": "simple",
        "apis": [
            {
                "name": "Gmail",
                "description": "Email reading and management",
                "auth_type": "OAuth2",
                "endpoints": ["read", "send"]
            },
            {
                "name": "Notion",
                "description": "Note-taking and database",
                "auth_type": "Token",
                "endpoints": ["create_page", "update_database"]
            }
        ],
        "tech_stack": ["Python"],
        "workflow_steps": [
            "Read emails from Gmail",
            "Parse email content",
            "Create Notion page with content"
        ],
        "input_description": "Gmail emails matching filter",
        "output_description": "Notion pages created",
        "suggested_agents": ["@codebase-analyst", "@library-researcher"],
        "current_date": datetime.now().strftime("%Y-%m-%d"),
        "version": "1.0.0",
        "status": "Development",
        "repo_url": "https://github.com/user/gmail-to-notion",
        "license": "MIT"
    }


@pytest.fixture
def sample_medium_intent(sample_simple_intent):
    """Sample data for MEDIUM complexity project."""
    data = sample_simple_intent.copy()
    data["complexity"] = "medium"
    data["apis"].extend([
        {
            "name": "Slack",
            "description": "Team messaging",
            "auth_type": "OAuth2",
            "endpoints": ["post_message", "list_channels"]
        }
    ])
    return data


@pytest.fixture
def sample_high_intent(sample_medium_intent):
    """Sample data for HIGH complexity project."""
    data = sample_medium_intent.copy()
    data["complexity"] = "high"
    data["apis"].extend([
        {
            "name": "OpenAI",
            "description": "AI processing",
            "auth_type": "Token",
            "endpoints": ["chat", "embeddings"]
        },
        {
            "name": "Anthropic",
            "description": "Claude API",
            "auth_type": "Token",
            "endpoints": ["messages"]
        }
    ])
    return data


class TestBaseTemplates:
    """Test base templates that are common to all projects."""

    def test_readme_template_renders(self, template_env, sample_simple_intent):
        """Test that README.md.j2 renders without errors."""
        template = template_env.get_template("base/README.md.j2")
        rendered = template.render(**sample_simple_intent)

        # Validate basic content
        assert "gmail-to-notion" in rendered
        assert "Automatizar emails de Gmail a Notion" in rendered
        assert "Gmail" in rendered
        assert "Notion" in rendered
        assert "Python" in rendered

    def test_claude_md_template_renders(self, template_env, sample_simple_intent):
        """Test that CLAUDE.md.j2 renders without errors."""
        template = template_env.get_template("base/CLAUDE.md.j2")
        rendered = template.render(**sample_simple_intent)

        # Validate content
        assert "CLAUDE.md - gmail-to-notion" in rendered
        assert "TDD" in rendered.upper()
        assert "requirements.txt" in rendered

    def test_planning_md_template_renders(self, template_env, sample_simple_intent):
        """Test that PLANNING.md.j2 renders without errors."""
        template = template_env.get_template("base/.claude/PLANNING.md.j2")
        rendered = template.render(**sample_simple_intent)

        # Validate content
        assert "PLANNING.md - gmail-to-notion" in rendered
        assert "Arquitectura" in rendered

    def test_task_md_template_renders(self, template_env, sample_simple_intent):
        """Test that TASK.md.j2 renders without errors."""
        template = template_env.get_template("base/.claude/TASK.md.j2")
        rendered = template.render(**sample_simple_intent)

        # Validate content
        assert "TASK.md - gmail-to-notion" in rendered
        assert "Gmail" in rendered

    def test_prp_md_template_renders(self, template_env, sample_simple_intent):
        """Test that PRP.md.j2 renders without errors."""
        template = template_env.get_template("base/.claude/PRP.md.j2")
        rendered = template.render(**sample_simple_intent)

        # Validate content
        assert "PRP Template" in rendered

    def test_requirements_txt_template_renders(self, template_env, sample_simple_intent):
        """Test that requirements.txt.j2 renders without errors."""
        template = template_env.get_template("base/requirements.txt.j2")
        rendered = template.render(**sample_simple_intent)

        # Validate Python dependencies
        assert "pydantic" in rendered
        assert "pytest" in rendered
        # API-specific dependencies
        assert "google-api-python-client" in rendered  # Gmail
        assert "notion-client" in rendered  # Notion


class TestMediumTemplates:
    """Test medium complexity templates (orchestrator/)."""

    def test_orchestrator_agent_renders(self, template_env, sample_medium_intent):
        """Test that orchestrator/agent.py.j2 renders without errors."""
        template = template_env.get_template("medium/orchestrator/agent.py.j2")
        rendered = template.render(**sample_medium_intent)

        # Validate Python syntax
        assert "class" in rendered
        assert "def" in rendered
        assert "async def" in rendered
        # Validate imports
        assert "from .models import" in rendered
        assert "from .memory import" in rendered

    def test_orchestrator_models_renders(self, template_env, sample_medium_intent):
        """Test that orchestrator/models.py.j2 renders without errors."""
        template = template_env.get_template("medium/orchestrator/models.py.j2")
        rendered = template.render(**sample_medium_intent)

        # Validate Pydantic models
        assert "from pydantic import" in rendered
        assert "class WorkflowIntent" in rendered
        assert "class WorkflowResult" in rendered
        # Validate API configs
        assert "GmailConfig" in rendered
        assert "NotionConfig" in rendered


class TestHighTemplates:
    """Test high complexity templates (@self-improve)."""

    def test_self_improve_agent_exists(self):
        """Test that @self-improve.md exists."""
        template_path = Path(".claude/templates/high/.claude/agents/@self-improve.md")
        assert template_path.exists()

    def test_self_improve_content(self):
        """Test that @self-improve.md has expected content."""
        template_path = Path(".claude/templates/high/.claude/agents/@self-improve.md")
        content = template_path.read_text()

        # Validate key sections
        assert "@self-improve" in content
        assert "Performance Analysis" in content
        assert "Code Quality" in content
        assert "Self-Improvement" in content


class TestFullProjectGeneration:
    """Test full project generation for each complexity level."""

    def _generate_project(self, template_env, intent_data):
        """Helper to generate a complete project."""
        project_path = Path(tempfile.mkdtemp()) / intent_data["project_name"]
        project_path.mkdir(parents=True)

        try:
            # Render base templates
            base_templates = [
                ("base/README.md.j2", "README.md"),
                ("base/CLAUDE.md.j2", "CLAUDE.md"),
                ("base/.claude/PLANNING.md.j2", ".claude/PLANNING.md"),
                ("base/.claude/TASK.md.j2", ".claude/TASK.md"),
            ]

            for template_path, output_path in base_templates:
                template = template_env.get_template(template_path)
                rendered = template.render(**intent_data)

                output_file = project_path / output_path
                output_file.parent.mkdir(parents=True, exist_ok=True)
                output_file.write_text(rendered)

            # Add orchestrator for medium/high
            if intent_data["complexity"] in ["medium", "high"]:
                orchestrator_templates = [
                    ("medium/orchestrator/agent.py.j2", "orchestrator/agent.py"),
                    ("medium/orchestrator/models.py.j2", "orchestrator/models.py"),
                ]

                for template_path, output_path in orchestrator_templates:
                    template = template_env.get_template(template_path)
                    rendered = template.render(**intent_data)

                    output_file = project_path / output_path
                    output_file.parent.mkdir(parents=True, exist_ok=True)
                    output_file.write_text(rendered)

            return project_path

        except Exception as e:
            # Cleanup on error
            shutil.rmtree(project_path.parent)
            raise e

    def test_simple_project_generation(self, template_env, sample_simple_intent):
        """Test generating a complete SIMPLE project."""
        project_path = self._generate_project(template_env, sample_simple_intent)

        try:
            # Validate structure
            assert (project_path / "README.md").exists()
            assert (project_path / "CLAUDE.md").exists()
            assert (project_path / ".claude" / "PLANNING.md").exists()

            # Should NOT have orchestrator
            assert not (project_path / "orchestrator").exists()

        finally:
            shutil.rmtree(project_path.parent)

    def test_medium_project_generation(self, template_env, sample_medium_intent):
        """Test generating a complete MEDIUM project."""
        project_path = self._generate_project(template_env, sample_medium_intent)

        try:
            # Validate base structure
            assert (project_path / "README.md").exists()
            assert (project_path / "CLAUDE.md").exists()

            # SHOULD have orchestrator
            assert (project_path / "orchestrator" / "agent.py").exists()
            assert (project_path / "orchestrator" / "models.py").exists()

        finally:
            shutil.rmtree(project_path.parent)

    def test_high_project_generation(self, template_env, sample_high_intent):
        """Test generating a complete HIGH project."""
        project_path = self._generate_project(template_env, sample_high_intent)

        try:
            # Validate base structure
            assert (project_path / "README.md").exists()

            # SHOULD have orchestrator
            assert (project_path / "orchestrator" / "agent.py").exists()

            # Note: @self-improve is copied without rendering, so we don't test it here

        finally:
            shutil.rmtree(project_path.parent)


class TestTemplateVariables:
    """Test that all template variables are properly used."""

    def test_all_required_variables_present(self, template_env, sample_simple_intent):
        """Test that all templates can be rendered with required variables."""
        # List of all .j2 templates
        templates_to_test = [
            "base/README.md.j2",
            "base/CLAUDE.md.j2",
            "base/.claude/PLANNING.md.j2",
            "base/.claude/TASK.md.j2",
            "base/.claude/PRP.md.j2",
            "base/requirements.txt.j2",
            "medium/orchestrator/agent.py.j2",
            "medium/orchestrator/models.py.j2",
        ]

        for template_path in templates_to_test:
            template = template_env.get_template(template_path)
            # Should not raise any errors
            rendered = template.render(**sample_simple_intent)
            assert len(rendered) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
