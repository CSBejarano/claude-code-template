"""
Test Versioning System for Orchestrator Agent SDK.

Validates that version tracking works correctly across the SDK.
"""

import re
import pytest
from pathlib import Path

# Check if OrchestratorAgent is available (requires dependencies)
try:
    from orchestrator import OrchestratorAgent
    ORCHESTRATOR_AVAILABLE = True
except ImportError:
    ORCHESTRATOR_AVAILABLE = False


class TestVersionFormat:
    """Test that version strings follow semantic versioning format."""

    def test_version_string_format(self):
        """Test that __version__ follows semver format (X.Y.Z)."""
        from orchestrator import __version__

        # Should match semver pattern: MAJOR.MINOR.PATCH
        pattern = r'^\d+\.\d+\.\d+$'
        assert re.match(pattern, __version__), \
            f"Version '{__version__}' does not match semver format X.Y.Z"

    def test_version_info_tuple(self):
        """Test that __version_info__ is a 3-element tuple of integers."""
        from orchestrator import __version_info__

        assert isinstance(__version_info__, tuple), \
            "__version_info__ must be a tuple"

        assert len(__version_info__) == 3, \
            f"__version_info__ must have 3 elements, got {len(__version_info__)}"

        for component in __version_info__:
            assert isinstance(component, int), \
                f"Version component {component} must be an integer"

    def test_version_consistency(self):
        """Test that __version__ and __version_info__ are consistent."""
        from orchestrator import __version__, __version_info__

        # Convert tuple to string
        version_from_tuple = f"{__version_info__[0]}.{__version_info__[1]}.{__version_info__[2]}"

        assert __version__ == version_from_tuple, \
            f"__version__ ('{__version__}') and __version_info__ ('{version_from_tuple}') must match"


class TestVersionAccessibility:
    """Test that version is accessible from different import patterns."""

    def test_import_from_package(self):
        """Test importing __version__ from package root."""
        from orchestrator import __version__

        assert __version__ is not None
        assert isinstance(__version__, str)

    def test_import_version_info(self):
        """Test importing __version_info__ from package root."""
        from orchestrator import __version_info__

        assert __version_info__ is not None
        assert isinstance(__version_info__, tuple)

    @pytest.mark.skipif(not ORCHESTRATOR_AVAILABLE, reason="OrchestratorAgent requires dependencies")
    def test_version_from_agent_class(self):
        """Test accessing VERSION from OrchestratorAgent class."""
        from orchestrator import OrchestratorAgent

        assert hasattr(OrchestratorAgent, 'VERSION'), \
            "OrchestratorAgent must have VERSION class attribute"

        assert isinstance(OrchestratorAgent.VERSION, str)

    @pytest.mark.skipif(not ORCHESTRATOR_AVAILABLE, reason="OrchestratorAgent requires dependencies")
    def test_version_from_agent_instance(self):
        """Test accessing VERSION from OrchestratorAgent instance."""
        from orchestrator import OrchestratorAgent

        agent = OrchestratorAgent()
        assert hasattr(agent, 'VERSION'), \
            "OrchestratorAgent instance must have VERSION attribute"

        assert agent.VERSION == OrchestratorAgent.VERSION

    @pytest.mark.skipif(not ORCHESTRATOR_AVAILABLE, reason="OrchestratorAgent requires dependencies")
    def test_get_version_method(self):
        """Test get_version() method on OrchestratorAgent."""
        from orchestrator import OrchestratorAgent

        agent = OrchestratorAgent()
        version = agent.get_version()

        assert isinstance(version, str)
        assert re.match(r'^\d+\.\d+\.\d+$', version)

    @pytest.mark.skipif(not ORCHESTRATOR_AVAILABLE, reason="OrchestratorAgent requires dependencies")
    def test_package_and_class_version_match(self):
        """Test that package __version__ matches OrchestratorAgent.VERSION."""
        from orchestrator import __version__, OrchestratorAgent

        assert __version__ == OrchestratorAgent.VERSION, \
            f"Package version '{__version__}' must match class VERSION '{OrchestratorAgent.VERSION}'"


class TestVersionValue:
    """Test that version has expected value."""

    def test_version_is_1_0_0(self):
        """Test that initial release version is 1.0.0."""
        from orchestrator import __version__

        # For M4, we're establishing v1.0.0 as the initial stable release
        assert __version__ == "1.0.0", \
            f"Expected initial version 1.0.0, got {__version__}"

    def test_version_info_is_1_0_0(self):
        """Test that __version_info__ matches (1, 0, 0)."""
        from orchestrator import __version_info__

        assert __version_info__ == (1, 0, 0), \
            f"Expected (1, 0, 0), got {__version_info__}"

    def test_major_version_is_one(self):
        """Test that we're on major version 1."""
        from orchestrator import __version_info__

        major = __version_info__[0]
        assert major == 1, \
            f"Expected major version 1 (stable release), got {major}"


class TestVersionInGeneratedProjects:
    """Test that version appears correctly in generated projects."""

    def test_template_has_version_variables(self):
        """Test that README.md.j2 template includes version variables."""
        template_path = Path(".claude/templates/base/README.md.j2")

        assert template_path.exists(), \
            f"Template not found: {template_path}"

        content = template_path.read_text()

        # Check for version variables
        assert "{{ template_version" in content, \
            "Template must include {{ template_version }}"

        assert "{{ orchestrator_sdk_version" in content, \
            "Template must include {{ orchestrator_sdk_version }}"

        assert "Claude Code Template" in content, \
            "Template must mention Claude Code Template"

    def test_project_initializer_provides_versions(self):
        """Test that @project-initializer provides version variables."""
        initializer_path = Path(".claude/agents/project-initializer.md")

        assert initializer_path.exists(), \
            f"project-initializer not found: {initializer_path}"

        content = initializer_path.read_text()

        # Check that template_vars includes versions
        assert "template_version" in content, \
            "@project-initializer must provide template_version variable"

        assert "orchestrator_sdk_version" in content, \
            "@project-initializer must provide orchestrator_sdk_version variable"

        assert "orchestrator.__version__" in content, \
            "@project-initializer must use orchestrator.__version__"


class TestChangelogExists:
    """Test that CHANGELOG.md exists and has correct format."""

    def test_changelog_exists(self):
        """Test that CHANGELOG.md exists."""
        changelog_path = Path("orchestrator/CHANGELOG.md")

        assert changelog_path.exists(), \
            f"CHANGELOG.md not found: {changelog_path}"

    def test_changelog_has_version_1_0_0(self):
        """Test that CHANGELOG.md documents version 1.0.0."""
        changelog_path = Path("orchestrator/CHANGELOG.md")
        content = changelog_path.read_text()

        assert "[1.0.0]" in content, \
            "CHANGELOG.md must document version [1.0.0]"

        assert "2025-01-03" in content, \
            "CHANGELOG.md must include release date"

        assert "Initial stable release" in content or "initial release" in content.lower(), \
            "CHANGELOG.md must mention this is initial release"

    def test_changelog_has_unreleased_section(self):
        """Test that CHANGELOG.md has [Unreleased] section."""
        changelog_path = Path("orchestrator/CHANGELOG.md")
        content = changelog_path.read_text()

        assert "[Unreleased]" in content, \
            "CHANGELOG.md must have [Unreleased] section for future changes"


class TestMigrationsExists:
    """Test that MIGRATIONS.md exists."""

    def test_migrations_file_exists(self):
        """Test that MIGRATIONS.md exists."""
        migrations_path = Path("orchestrator/MIGRATIONS.md")

        assert migrations_path.exists(), \
            f"MIGRATIONS.md not found: {migrations_path}"

    def test_migrations_mentions_1_0_0(self):
        """Test that MIGRATIONS.md mentions version 1.0.0."""
        migrations_path = Path("orchestrator/MIGRATIONS.md")
        content = migrations_path.read_text()

        assert "1.0.0" in content, \
            "MIGRATIONS.md must mention version 1.0.0"


class TestOrchestratorReadmeExists:
    """Test that orchestrator/README.md exists and is complete."""

    def test_readme_exists(self):
        """Test that orchestrator/README.md exists."""
        readme_path = Path("orchestrator/README.md")

        assert readme_path.exists(), \
            f"orchestrator/README.md not found: {readme_path}"

    def test_readme_documents_version(self):
        """Test that README.md documents the version."""
        readme_path = Path("orchestrator/README.md")
        content = readme_path.read_text()

        assert "1.0.0" in content, \
            "orchestrator/README.md must document version 1.0.0"

        assert "Version" in content or "version" in content, \
            "orchestrator/README.md must mention versioning"

    def test_readme_has_semantic_versioning_info(self):
        """Test that README.md explains semantic versioning."""
        readme_path = Path("orchestrator/README.md")
        content = content = readme_path.read_text()

        assert "Semantic Versioning" in content or "semver" in content.lower(), \
            "orchestrator/README.md must explain Semantic Versioning"

        assert "MAJOR" in content and "MINOR" in content and "PATCH" in content, \
            "orchestrator/README.md must explain MAJOR.MINOR.PATCH"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
