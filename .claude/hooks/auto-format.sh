#!/bin/bash
# PostToolUse hook: Auto-format code after edits (non-blocking)
# Detects file type and applies appropriate formatter

# Exit successfully to never block operations
set +e

timestamp=$(date '+%Y-%m-%d %H:%M:%S')

# Create logs directory if it doesn't exist
mkdir -p .claude/logs

# Function to format Python files
format_python() {
    local file="$1"

    # Try black first (preferred)
    if command -v black &> /dev/null; then
        if black "$file" --quiet 2>&1; then
            echo "[$timestamp] ✅ Formatted $file with black" >> .claude/logs/format.log
            return 0
        fi
    fi

    # Fallback to ruff format
    if command -v ruff &> /dev/null; then
        if ruff format "$file" 2>&1 | grep -q "formatted"; then
            echo "[$timestamp] ✅ Formatted $file with ruff" >> .claude/logs/format.log
            return 0
        fi
    fi

    echo "[$timestamp] ⚠️ No Python formatter found (install black or ruff)" >> .claude/logs/format.log
    return 1
}

# Function to format JavaScript/TypeScript files
format_js_ts() {
    local file="$1"

    # Check if prettier is available
    if command -v prettier &> /dev/null; then
        if prettier --write "$file" &> /dev/null; then
            echo "[$timestamp] ✅ Formatted $file with prettier" >> .claude/logs/format.log
            return 0
        fi
    fi

    # Check if npx is available (for projects without global prettier)
    if command -v npx &> /dev/null; then
        if npx prettier --write "$file" &> /dev/null 2>&1; then
            echo "[$timestamp] ✅ Formatted $file with prettier (npx)" >> .claude/logs/format.log
            return 0
        fi
    fi

    echo "[$timestamp] ⚠️ No JS/TS formatter found (install prettier)" >> .claude/logs/format.log
    return 1
}

# Function to format Markdown files
format_markdown() {
    local file="$1"

    # Use prettier for markdown
    if command -v prettier &> /dev/null; then
        if prettier --write "$file" &> /dev/null; then
            echo "[$timestamp] ✅ Formatted $file with prettier" >> .claude/logs/format.log
            return 0
        fi
    fi

    # Fallback to npx
    if command -v npx &> /dev/null; then
        if npx prettier --write "$file" &> /dev/null 2>&1; then
            echo "[$timestamp] ✅ Formatted $file with prettier (npx)" >> .claude/logs/format.log
            return 0
        fi
    fi

    echo "[$timestamp] ⚠️ No Markdown formatter found" >> .claude/logs/format.log
    return 1
}

# Function to detect file type and format
format_file() {
    local file="$1"

    # Skip if file doesn't exist
    [[ ! -f "$file" ]] && return

    # Get file extension
    local ext="${file##*.}"

    case "$ext" in
        py)
            format_python "$file"
            ;;
        js|jsx|ts|tsx)
            format_js_ts "$file"
            ;;
        md)
            format_markdown "$file"
            ;;
        *)
            echo "[$timestamp] ℹ️ No formatter configured for .$ext files" >> .claude/logs/format.log
            ;;
    esac
}

# Main logic: Get recently modified files and format them
if command -v git &> /dev/null && [[ -d .git ]]; then
    # Get recently modified files (excluding logs and node_modules)
    recent_files=$(git diff --name-only HEAD 2>/dev/null | grep -v 'logs/' | grep -v 'node_modules/' || true)

    if [[ -n "$recent_files" ]]; then
        echo "[$timestamp] 🔧 Auto-formatting triggered" >> .claude/logs/format.log

        while IFS= read -r file; do
            format_file "$file"
        done <<< "$recent_files"

        echo "[$timestamp] ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" >> .claude/logs/format.log
    fi
fi

# Always return success (JSON format expected by Claude Code)
echo "{}"
exit 0
