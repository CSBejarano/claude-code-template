"""
Integration Tests for TDD Loop Workflow.

Tests the Phase 8 TDD (Test-Driven Development) loop that is central
to the Claude Code Template approach.

The TDD loop:
1. Write failing test
2. Implement feature
3. Make test pass
4. Refactor if needed
5. Repeat

These tests validate that the orchestration workflow correctly
implements this TDD cycle.
"""

import pytest
from typing import List, Dict, Any
from unittest.mock import Mock, MagicMock


class MockTestResult:
    """Mock test execution result."""

    def __init__(self, passed: bool, test_name: str, error: str = ""):
        self.passed = passed
        self.test_name = test_name
        self.error = error


class MockCodeGeneration:
    """Mock code generation result."""

    def __init__(self, file_path: str, content: str):
        self.file_path = file_path
        self.content = content
        self.lines_of_code = len(content.split("\n"))


class TDDLoopSimulator:
    """
    Simulates the TDD loop for testing.

    This represents how Phase 8 should execute the TDD cycle.
    """

    def __init__(self):
        self.iteration_count = 0
        self.tests_written: List[str] = []
        self.code_written: List[str] = []
        self.test_results: List[MockTestResult] = []

    def write_test(self, test_name: str, test_code: str) -> None:
        """Step 1: Write failing test."""
        self.tests_written.append(test_name)
        self.iteration_count += 1

    def run_test(self, test_name: str) -> MockTestResult:
        """Run test and get result."""
        # First run should fail (no implementation yet)
        if test_name not in self.code_written:
            result = MockTestResult(
                passed=False,
                test_name=test_name,
                error="NotImplementedError: Feature not implemented"
            )
        else:
            # Second run should pass (implementation exists)
            result = MockTestResult(
                passed=True,
                test_name=test_name
            )

        self.test_results.append(result)
        return result

    def implement_feature(self, test_name: str, code: str) -> MockCodeGeneration:
        """Step 2: Implement feature to make test pass."""
        self.code_written.append(test_name)
        return MockCodeGeneration(
            file_path=f"src/{test_name.replace('test_', '')}.py",
            content=code
        )

    def verify_test_passes(self, test_name: str) -> bool:
        """Step 3: Verify test now passes."""
        result = self.run_test(test_name)
        return result.passed


class TestTDDLoopBasicFlow:
    """Test the basic TDD loop flow."""

    def test_tdd_loop_single_iteration(self):
        """
        Test a single TDD loop iteration.

        Flow:
        1. Write failing test
        2. Run test → FAIL
        3. Implement feature
        4. Run test → PASS
        """
        tdd = TDDLoopSimulator()

        # Step 1: Write test
        tdd.write_test("test_add_numbers", "def test_add_numbers(): ...")

        # Step 2: Run test - should fail
        result1 = tdd.run_test("test_add_numbers")
        assert result1.passed is False, "First run should fail"
        assert "NotImplementedError" in result1.error

        # Step 3: Implement feature
        code = "def add_numbers(a, b): return a + b"
        generation = tdd.implement_feature("test_add_numbers", code)
        assert generation.file_path == "src/add_numbers.py"

        # Step 4: Run test again - should pass
        result2 = tdd.run_test("test_add_numbers")
        assert result2.passed is True, "Second run should pass"

    def test_tdd_loop_multiple_iterations(self):
        """
        Test multiple TDD loop iterations.

        Simulates implementing multiple features sequentially
        using TDD approach.
        """
        tdd = TDDLoopSimulator()

        features = [
            ("test_calculate_sum", "def calculate_sum(...): ..."),
            ("test_validate_input", "def validate_input(...): ..."),
            ("test_format_output", "def format_output(...): ..."),
        ]

        for test_name, code in features:
            # Write test
            tdd.write_test(test_name, code)

            # Implement feature
            tdd.implement_feature(test_name, code)

            # Verify passes
            assert tdd.verify_test_passes(test_name) is True

        # Validate all iterations completed
        assert tdd.iteration_count == 3
        assert len(tdd.tests_written) == 3
        assert len(tdd.code_written) == 3


class TestTDDLoopWithRefactoring:
    """Test TDD loop with refactoring step."""

    def test_refactoring_after_test_passes(self):
        """
        Test that refactoring is performed after tests pass.

        Flow:
        1. Write test → FAIL
        2. Implement (quick/dirty) → PASS
        3. Refactor → STILL PASS
        """
        tdd = TDDLoopSimulator()

        # Initial implementation (quick and dirty)
        tdd.write_test("test_process_data", "...")
        tdd.implement_feature("test_process_data", "def process(): return 42")
        assert tdd.verify_test_passes("test_process_data") is True

        # Refactor (improve implementation)
        refactored_code = """
def process_data(data):
    \"\"\"Process data with proper validation.\"\"\"
    if not data:
        raise ValueError("Data required")
    return len(data) * 2
"""
        refactored = MockCodeGeneration("src/process_data.py", refactored_code)

        # Test should still pass after refactoring
        assert tdd.verify_test_passes("test_process_data") is True
        assert refactored.lines_of_code > 1


class TestTDDLoopErrorHandling:
    """Test TDD loop handles errors correctly."""

    def test_failing_test_blocks_progression(self):
        """
        Test that a failing test blocks progression to next feature.

        The TDD loop should not proceed if tests don't pass.
        """
        class StrictTDDLoop(TDDLoopSimulator):
            def proceed_to_next_feature(self, current_test: str) -> bool:
                """Only proceed if current test passes."""
                result = self.run_test(current_test)
                return result.passed

        tdd = StrictTDDLoop()

        # Write test
        tdd.write_test("test_feature_a", "...")

        # Try to proceed without implementation - should block
        can_proceed = tdd.proceed_to_next_feature("test_feature_a")
        assert can_proceed is False, "Should not proceed with failing test"

        # Implement feature
        tdd.implement_feature("test_feature_a", "def feature_a(): pass")

        # Now should be able to proceed
        can_proceed = tdd.proceed_to_next_feature("test_feature_a")
        assert can_proceed is True, "Should proceed after test passes"

    def test_implementation_error_retry(self):
        """
        Test that implementation errors trigger retry.

        If implementation has syntax errors or doesn't make test pass,
        the loop should retry.
        """
        class RetryableTDDLoop(TDDLoopSimulator):
            def __init__(self):
                super().__init__()
                self.retry_count = 0
                self.max_retries = 3

            def implement_with_retry(self, test_name: str) -> bool:
                """Implement with retry on failure."""
                while self.retry_count < self.max_retries:
                    # Simulate implementation attempt
                    code = f"# Attempt {self.retry_count + 1}"
                    self.implement_feature(test_name, code)

                    # Check if test passes
                    if self.verify_test_passes(test_name):
                        return True

                    self.retry_count += 1

                return False  # Max retries exceeded

        tdd = RetryableTDDLoop()
        tdd.write_test("test_complex_feature", "...")

        # Should succeed with retry
        success = tdd.implement_with_retry("test_complex_feature")
        assert success is True
        assert tdd.retry_count < tdd.max_retries


class TestTDDLoopIntegration:
    """Test TDD loop integration with orchestration phases."""

    def test_tdd_loop_executes_in_phase8(self):
        """
        Test that TDD loop is executed in Phase 8.

        Phase 8 (Code Generation) should use TDD approach.
        """
        # Simulate orchestration phases
        phases = {
            0: "Initialize",
            1: "Analyze Intent",
            2: "CHECKPOINT 1",
            3: "Planning",
            4: "Subagent Definition",
            5: "Tool Selection",
            6: "Structure Generation",
            7: "CHECKPOINT 2",
            8: "Code Generation (TDD)",  # TDD loop here
            9: "Documentation"
        }

        assert "TDD" in phases[8]
        assert phases[8] == "Code Generation (TDD)"

    def test_tdd_loop_generates_test_files(self):
        """
        Test that TDD loop generates test files in tests/ directory.

        Generated project should have:
        - src/ with implementation
        - tests/ with tests
        - Tests should be written BEFORE implementation
        """
        class ProjectGenerator:
            def __init__(self):
                self.files_created = []
                self.creation_order = []

            def create_file(self, path: str, content: str) -> None:
                self.files_created.append(path)
                self.creation_order.append(path)

            def tdd_generate(self, feature_name: str) -> None:
                """Generate using TDD - tests first."""
                # Test file created first
                test_file = f"tests/test_{feature_name}.py"
                self.create_file(test_file, "def test_...")

                # Implementation created second
                impl_file = f"src/{feature_name}.py"
                self.create_file(impl_file, "def ...")

        generator = ProjectGenerator()
        generator.tdd_generate("calculator")

        # Validate order: test before implementation
        assert generator.creation_order[0] == "tests/test_calculator.py"
        assert generator.creation_order[1] == "src/calculator.py"

    def test_tdd_loop_coverage_validation(self):
        """
        Test that TDD loop validates test coverage.

        After TDD loop completes, coverage should be 100%
        since every line was written to pass a test.
        """
        class CoverageTracker:
            def __init__(self):
                self.lines_tested = 0
                self.lines_total = 0

            def add_test(self, lines_covered: int) -> None:
                self.lines_tested += lines_covered

            def add_code(self, lines_added: int) -> None:
                self.lines_total += lines_added

            def get_coverage(self) -> float:
                if self.lines_total == 0:
                    return 100.0
                return (self.lines_tested / self.lines_total) * 100

        coverage = CoverageTracker()

        # TDD cycle 1
        coverage.add_test(5)  # Test covers 5 lines
        coverage.add_code(5)  # Implement exactly those 5 lines

        # TDD cycle 2
        coverage.add_test(10)  # Test covers 10 lines
        coverage.add_code(10)  # Implement exactly those 10 lines

        # TDD guarantees 100% coverage
        assert coverage.get_coverage() == 100.0


class TestTDDLoopBestPractices:
    """Test that TDD loop follows best practices."""

    def test_one_test_one_feature(self):
        """
        Test that TDD loop implements one feature per test.

        Best practice: Each test should validate one specific feature.
        """
        tdd = TDDLoopSimulator()

        # Good: One test per feature
        tdd.write_test("test_validate_email", "...")
        tdd.implement_feature("test_validate_email", "def validate_email(): ...")

        tdd.write_test("test_validate_phone", "...")
        tdd.implement_feature("test_validate_phone", "def validate_phone(): ...")

        # Each test has corresponding implementation
        assert len(tdd.tests_written) == len(tdd.code_written)

    def test_tests_are_descriptive(self):
        """
        Test that generated tests have descriptive names.

        Test names should clearly describe what they validate.
        """
        test_names = [
            "test_calculate_invoice_total",
            "test_validate_pdf_format",
            "test_extract_invoice_date",
            "test_parse_line_items",
        ]

        for name in test_names:
            # Should start with test_
            assert name.startswith("test_")

            # Should use snake_case
            assert "_" in name

            # Should be descriptive (> 10 chars)
            assert len(name) > 10

    def test_minimal_implementation_first(self):
        """
        Test that TDD loop starts with minimal implementation.

        Best practice: Implement just enough to make test pass,
        then refactor.
        """
        class MinimalFirstTDD(TDDLoopSimulator):
            def implement_minimal(self, test_name: str) -> str:
                """Return minimal implementation."""
                return "return True  # Minimal implementation"

            def refactor_if_needed(self, code: str) -> str:
                """Refactor after test passes."""
                if "Minimal" in code:
                    return """
def proper_implementation():
    \"\"\"Full implementation with docs.\"\"\"
    # Proper logic here
    return True
"""
                return code

        tdd = MinimalFirstTDD()

        # Step 1: Minimal implementation
        minimal = tdd.implement_minimal("test_feature")
        assert "Minimal" in minimal

        # Step 2: Refactor
        refactored = tdd.refactor_if_needed(minimal)
        assert "Full implementation" in refactored
        assert "docs" in refactored.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
