#!/bin/bash
# PostToolUse hook: Remind about documentation updates (non-blocking)
# Detects significant code changes and suggests relevant docs to update

# Exit successfully to never block operations
set +e

timestamp=$(date '+%Y-%m-%d %H:%M:%S')

# Create logs directory if it doesn't exist
mkdir -p .claude/logs

# Function to check if changes are significant
is_significant_change() {
    local file="$1"

    # Count added/removed lines in the file
    local changes=$(git diff HEAD "$file" 2>/dev/null | grep -E '^\+|^-' | grep -v '^\+\+\+|^---' | wc -l || echo "0")

    # Consider significant if >50 lines changed
    [[ $changes -gt 50 ]]
}

# Function to detect API changes
has_api_changes() {
    local file="$1"

    # Check for function/class definitions, decorators, exports
    git diff HEAD "$file" 2>/dev/null | grep -E '^\+.*def |^\+.*class |^\+.*@app\.|^\+.*export ' > /dev/null
}

# Function to suggest docs based on file type
suggest_docs() {
    local file="$1"
    local suggestions=""

    # Map files to relevant documentation
    case "$file" in
        src/routes/*|src/api/*)
            suggestions="docs/api/README.md, docs/api/endpoints.md"
            ;;
        src/services/*|src/models/*)
            suggestions="docs/architecture.md, README.md (Architecture section)"
            ;;
        src/utils/*|src/helpers/*)
            suggestions="docs/utilities.md, README.md (Utils section)"
            ;;
        tests/*)
            suggestions="docs/testing.md, README.md (Testing section)"
            ;;
        .claude/agents/*|.claude/commands/*)
            suggestions="docs/agents.md, .claude/README.md"
            ;;
        README.md|CLAUDE.md|PLANNING.md)
            # These are docs themselves, no suggestion needed
            return
            ;;
        *)
            suggestions="README.md, docs/ (relevant sections)"
            ;;
    esac

    echo "$suggestions"
}

# Function to create reminder
create_reminder() {
    local file="$1"
    local reason="$2"
    local docs="$3"

    echo "[$timestamp] 📝 DOCUMENTATION REMINDER" >> .claude/logs/doc-reminders.log
    echo "  File changed: $file" >> .claude/logs/doc-reminders.log
    echo "  Reason: $reason" >> .claude/logs/doc-reminders.log
    echo "  Suggested docs to update:" >> .claude/logs/doc-reminders.log
    echo "    - $docs" | tr ',' '\n' | sed 's/^/    /' >> .claude/logs/doc-reminders.log
    echo "" >> .claude/logs/doc-reminders.log
}

# Main logic: Check for significant changes
if command -v git &> /dev/null && [[ -d .git ]]; then
    # Get recently modified non-documentation files
    recent_files=$(git diff --name-only HEAD 2>/dev/null | grep -v 'docs/' | grep -v '\.log$' | grep -v 'node_modules/' || true)

    if [[ -n "$recent_files" ]]; then
        reminder_count=0

        while IFS= read -r file; do
            # Skip if file doesn't exist
            [[ ! -f "$file" ]] && continue

            reason=""

            # Check if significant change (>50 lines)
            if is_significant_change "$file"; then
                reason="Significant change (>50 lines modified)"
            fi

            # Check if API change
            if has_api_changes "$file"; then
                if [[ -n "$reason" ]]; then
                    reason="$reason + API changes detected"
                else
                    reason="API changes detected (new/modified functions/classes)"
                fi
            fi

            # Create reminder if we have a reason
            if [[ -n "$reason" ]]; then
                docs=$(suggest_docs "$file")
                if [[ -n "$docs" ]]; then
                    create_reminder "$file" "$reason" "$docs"
                    reminder_count=$((reminder_count + 1))
                fi
            fi
        done <<< "$recent_files"

        # Summary log entry
        if [[ $reminder_count -gt 0 ]]; then
            echo "[$timestamp] ℹ️ Created $reminder_count documentation reminder(s)" >> .claude/logs/doc-reminders.log
            echo "[$timestamp] ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >> .claude/logs/doc-reminders.log
        fi
    fi
fi

# Always return success (JSON format expected by Claude Code)
echo "{}"
exit 0
