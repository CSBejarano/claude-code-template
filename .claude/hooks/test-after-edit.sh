#!/bin/bash
# PostToolUse hook: Run tests after code edits (non-blocking)
# Executes pytest for edited files in background and logs results

# Exit successfully to never block operations
set +e

timestamp=$(date '+%Y-%m-%d %H:%M:%S')

# Create logs directory if it doesn't exist
mkdir -p .claude/logs

# Function to detect if file is in src/ or tests/
is_code_file() {
    local file="$1"
    [[ "$file" == src/* ]] || [[ "$file" == tests/* ]] || [[ "$file" == *.py ]]
}

# Function to find corresponding test file
find_test_file() {
    local src_file="$1"

    # If already a test file, return it
    if [[ "$src_file" == tests/* ]]; then
        echo "$src_file"
        return
    fi

    # Convert src/module/file.py to tests/unit/test_file.py
    local filename=$(basename "$src_file" .py)
    local test_file="tests/unit/test_${filename}.py"

    if [[ -f "$test_file" ]]; then
        echo "$test_file"
        return
    fi

    # Try tests/integration/ as fallback
    test_file="tests/integration/test_${filename}.py"
    if [[ -f "$test_file" ]]; then
        echo "$test_file"
        return
    fi

    # Return empty if no test found
    echo ""
}

# Function to run tests in background
run_tests_bg() {
    local test_file="$1"
    local src_file="$2"

    # Check if pytest is available
    if ! command -v pytest &> /dev/null; then
        echo "[$timestamp] ⚠️ pytest not found - skipping tests for $src_file" >> .claude/logs/test-results.log
        return
    fi

    # Run tests in background and capture output
    {
        echo "[$timestamp] 🧪 Running tests for $src_file..." >> .claude/logs/test-results.log

        if pytest "$test_file" -v --tb=short &> /tmp/pytest-output-$$.txt; then
            echo "[$timestamp] ✅ Tests PASSED for $test_file" >> .claude/logs/test-results.log
            # Optionally include summary
            tail -n 3 /tmp/pytest-output-$$.txt >> .claude/logs/test-results.log
        else
            echo "[$timestamp] ❌ Tests FAILED for $test_file" >> .claude/logs/test-results.log
            # Include failure details
            tail -n 15 /tmp/pytest-output-$$.txt >> .claude/logs/test-results.log
        fi

        # Cleanup
        rm -f /tmp/pytest-output-$$.txt

        echo "[$timestamp] ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >> .claude/logs/test-results.log
    } &
}

# Main logic: Check if recent edit was to code file
# Note: Claude Code doesn't pass file info to hooks yet, so we detect via git diff
if command -v git &> /dev/null && [[ -d .git ]]; then
    # Get recently modified Python files
    recent_files=$(git diff --name-only HEAD 2>/dev/null | grep '\.py$' || true)

    if [[ -n "$recent_files" ]]; then
        while IFS= read -r file; do
            if is_code_file "$file" && [[ -f "$file" ]]; then
                test_file=$(find_test_file "$file")

                if [[ -n "$test_file" ]]; then
                    run_tests_bg "$test_file" "$file"
                else
                    echo "[$timestamp] ⚠️ No test file found for $file" >> .claude/logs/test-results.log
                fi
            fi
        done <<< "$recent_files"
    fi
fi

# Always return success (JSON format expected by Claude Code)
echo "{}"
exit 0
