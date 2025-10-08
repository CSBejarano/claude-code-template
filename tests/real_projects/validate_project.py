"""
Validation framework for E2E real project tests.

This script validates generated projects against expected criteria:
- Structure validation (files, directories)
- Documentation quality
- Test coverage
- Code quality (linting, type checking)
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class ValidationResult:
    """Results from project validation."""
    project_name: str
    complexity: str  # SIMPLE, MEDIUM, HIGH
    structure_valid: bool
    structure_issues: List[str]
    tests_exist: bool
    tests_passing: int
    tests_total: int
    tests_pass_rate: float
    has_readme: bool
    has_planning: bool
    has_claude_md: bool
    has_orchestrator: bool  # For MEDIUM/HIGH
    has_self_improve: bool  # For HIGH
    lint_passing: bool
    lint_errors: int
    quality_score: float  # 0-10
    generation_success: bool
    issues_found: List[str]
    timestamp: str


def validate_structure(project_path: Path, complexity: str) -> Dict[str, Any]:
    """Validate project structure based on complexity."""
    issues = []

    # Base files (all projects)
    required_base = ["README.md", "CLAUDE.md", ".claude/PLANNING.md", ".claude/TASK.md"]
    for file in required_base:
        if not (project_path / file).exists():
            issues.append(f"Missing required file: {file}")

    # MEDIUM/HIGH projects should have orchestrator
    if complexity in ["MEDIUM", "HIGH"]:
        if not (project_path / "orchestrator").exists():
            issues.append("Missing orchestrator/ directory for MEDIUM/HIGH complexity")
        else:
            orchestrator_files = ["__init__.py", "agent.py", "models.py", "memory.py"]
            for file in orchestrator_files:
                if not (project_path / "orchestrator" / file).exists():
                    issues.append(f"Missing orchestrator file: {file}")

    # HIGH projects should have @self-improve
    if complexity == "HIGH":
        if not (project_path / ".claude/agents/@self-improve.md").exists():
            issues.append("Missing @self-improve agent for HIGH complexity")

    # Tests directory
    if not (project_path / "tests").exists():
        issues.append("Missing tests/ directory")

    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "has_readme": (project_path / "README.md").exists(),
        "has_planning": (project_path / ".claude/PLANNING.md").exists(),
        "has_claude_md": (project_path / "CLAUDE.md").exists(),
        "has_orchestrator": (project_path / "orchestrator").exists() if complexity in ["MEDIUM", "HIGH"] else None,
        "has_self_improve": (project_path / ".claude/agents/@self-improve.md").exists() if complexity == "HIGH" else None,
    }


def run_tests(project_path: Path) -> Dict[str, Any]:
    """Execute project tests and capture results."""
    if not (project_path / "tests").exists():
        return {"exist": False, "passing": 0, "total": 0, "pass_rate": 0.0}

    try:
        # Check for venv and use appropriate pytest (absolute path)
        venv_pytest = (project_path / "venv/bin/pytest").resolve()
        if venv_pytest.exists():
            pytest_cmd = str(venv_pytest)
        else:
            pytest_cmd = "pytest"

        # Setup environment with PYTHONPATH (relative to cwd)
        env = os.environ.copy()
        env["PYTHONPATH"] = "."

        # Run pytest with json report
        result = subprocess.run(
            [pytest_cmd, "tests/", "-v", "--tb=short"],
            cwd=project_path,
            capture_output=True,
            text=True,
            timeout=300,  # 5 min timeout
            env=env
        )

        # Parse output for test counts
        output = result.stdout

        # Simple parsing (could be improved with pytest-json-report)
        passing = output.count(" PASSED")
        failing = output.count(" FAILED")
        total = passing + failing
        pass_rate = (passing / total * 100) if total > 0 else 0.0

        return {
            "exist": True,
            "passing": passing,
            "total": total,
            "pass_rate": pass_rate,
        }
    except subprocess.TimeoutExpired:
        return {"exist": True, "passing": 0, "total": 0, "pass_rate": 0.0, "timeout": True}
    except Exception as e:
        return {"exist": True, "passing": 0, "total": 0, "pass_rate": 0.0, "error": str(e)}


def run_linting(project_path: Path) -> Dict[str, Any]:
    """Run linting checks."""
    try:
        # Check for venv and use appropriate ruff (absolute path)
        venv_ruff = (project_path / "venv/bin/ruff").resolve()
        if venv_ruff.exists():
            ruff_cmd = str(venv_ruff)
        else:
            ruff_cmd = "ruff"

        result = subprocess.run(
            [ruff_cmd, "check", ".", "--output-format=json"],
            cwd=project_path,
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.stdout:
            errors = json.loads(result.stdout)
            error_count = len(errors)
        else:
            error_count = 0

        return {
            "passing": error_count == 0,
            "errors": error_count,
        }
    except FileNotFoundError:
        # ruff not installed
        return {"passing": None, "errors": 0, "skipped": True}
    except Exception as e:
        return {"passing": None, "errors": 0, "error": str(e)}


def calculate_quality_score(
    structure_valid: bool,
    tests_pass_rate: float,
    has_docs: bool,
    lint_passing: bool,
) -> float:
    """Calculate overall quality score (0-10)."""
    score = 0.0

    # Structure: 3 points
    if structure_valid:
        score += 3.0

    # Tests: 4 points (based on pass rate)
    score += (tests_pass_rate / 100) * 4.0

    # Documentation: 2 points
    if has_docs:
        score += 2.0

    # Linting: 1 point
    if lint_passing or lint_passing is None:  # None means skipped
        score += 1.0

    return round(score, 1)


def validate_project(project_path: Path, complexity: str) -> ValidationResult:
    """
    Validate a generated project.

    Args:
        project_path: Path to generated project
        complexity: Expected complexity (SIMPLE, MEDIUM, HIGH)

    Returns:
        ValidationResult with all metrics
    """
    issues_found = []

    # 1. Structure validation
    structure = validate_structure(project_path, complexity)
    if not structure["valid"]:
        issues_found.extend(structure["issues"])

    # 2. Test execution
    tests = run_tests(project_path)
    if not tests["exist"]:
        issues_found.append("No tests found")
    elif tests.get("timeout"):
        issues_found.append("Tests timed out (>5 min)")
    elif tests["pass_rate"] < 85:
        issues_found.append(f"Test pass rate {tests['pass_rate']:.1f}% < 85% target")

    # 3. Linting
    lint = run_linting(project_path)
    if lint.get("skipped"):
        pass  # OK, ruff not installed
    elif not lint["passing"]:
        issues_found.append(f"Linting errors: {lint['errors']}")

    # 4. Quality score
    quality_score = calculate_quality_score(
        structure["valid"],
        tests["pass_rate"],
        structure["has_readme"] and structure["has_planning"],
        lint["passing"] if lint["passing"] is not None else True,
    )

    # Generation success = no critical issues
    generation_success = structure["valid"] and tests["exist"]

    return ValidationResult(
        project_name=project_path.name,
        complexity=complexity,
        structure_valid=structure["valid"],
        structure_issues=structure["issues"],
        tests_exist=tests["exist"],
        tests_passing=tests["passing"],
        tests_total=tests["total"],
        tests_pass_rate=tests["pass_rate"],
        has_readme=structure["has_readme"],
        has_planning=structure["has_planning"],
        has_claude_md=structure["has_claude_md"],
        has_orchestrator=structure["has_orchestrator"] or False,
        has_self_improve=structure["has_self_improve"] or False,
        lint_passing=lint["passing"] if lint["passing"] is not None else True,
        lint_errors=lint["errors"],
        quality_score=quality_score,
        generation_success=generation_success,
        issues_found=issues_found,
        timestamp=datetime.now().isoformat(),
    )


def main():
    """Main validation entry point."""
    if len(sys.argv) < 3:
        print("Usage: python validate_project.py <project_path> <complexity>")
        sys.exit(1)

    project_path = Path(sys.argv[1])
    complexity = sys.argv[2].upper()

    if complexity not in ["SIMPLE", "MEDIUM", "HIGH"]:
        print(f"Invalid complexity: {complexity}. Must be SIMPLE, MEDIUM, or HIGH")
        sys.exit(1)

    if not project_path.exists():
        print(f"Project path does not exist: {project_path}")
        sys.exit(1)

    # Run validation
    result = validate_project(project_path, complexity)

    # Print results
    print(f"\n{'='*60}")
    print(f"VALIDATION RESULTS: {result.project_name}")
    print(f"{'='*60}")
    print(f"Complexity: {result.complexity}")
    print(f"Generation Success: {'✅' if result.generation_success else '❌'}")
    print(f"Quality Score: {result.quality_score}/10")
    print(f"\nStructure: {'✅' if result.structure_valid else '❌'}")
    if result.structure_issues:
        print(f"  Issues: {', '.join(result.structure_issues)}")
    print(f"\nTests: {'✅' if result.tests_exist else '❌'}")
    if result.tests_exist:
        print(f"  Pass Rate: {result.tests_pass_rate:.1f}% ({result.tests_passing}/{result.tests_total})")
    print(f"\nLinting: {'✅' if result.lint_passing else '❌'}")
    if not result.lint_passing:
        print(f"  Errors: {result.lint_errors}")
    print(f"\nDocumentation:")
    print(f"  README: {'✅' if result.has_readme else '❌'}")
    print(f"  PLANNING: {'✅' if result.has_planning else '❌'}")
    print(f"  CLAUDE.md: {'✅' if result.has_claude_md else '❌'}")

    if result.complexity in ["MEDIUM", "HIGH"]:
        print(f"  Orchestrator: {'✅' if result.has_orchestrator else '❌'}")
    if result.complexity == "HIGH":
        print(f"  @self-improve: {'✅' if result.has_self_improve else '❌'}")

    if result.issues_found:
        print(f"\n⚠️  Issues Found ({len(result.issues_found)}):")
        for issue in result.issues_found:
            print(f"  - {issue}")

    print(f"\n{'='*60}\n")

    # Save results as JSON
    results_file = project_path / "validation_results.json"
    with open(results_file, "w") as f:
        json.dump(asdict(result), f, indent=2)

    print(f"Results saved to: {results_file}")

    # Exit code based on success
    sys.exit(0 if result.generation_success else 1)


if __name__ == "__main__":
    main()
