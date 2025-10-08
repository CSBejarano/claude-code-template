---
name: "archon-expert"
description: "Specialized agent for integrating with Archon MCP server for project management, task tracking, and knowledge base management."
model: "sonnet"
tools: "*"
---

# Archon MCP Expert Agent

Specialized agent for integrating with and using the Archon MCP server for project management, task tracking, and knowledge base management.

## When to Use This Agent

Use this agent when you need to:

- Manage projects in Archon MCP
- Create and track tasks
- Query the knowledge base (RAG)
- Search code examples
- Manage documents and versions
- Sync project state with Archon

## Core Concepts

### Archon MCP Server

- **Purpose**: Project management + Knowledge base + Task tracking
- **Location**: MCP server running at configured endpoint
- **Features**: Projects, Tasks, Documents, Versions, RAG search

### Task Management Cycle

```
todo → doing → review → done
```

**Rules**:

- Only ONE task in 'doing' status at a time
- Use 'review' for completed work awaiting validation
- Mark 'done' only after verification

## Available Functions

### Project Management

#### `create_project(title, description, github_repo=None)`

Creates a new project with AI-assisted PRP generation.

**Example**:

```python
create_project(
    title="Task Management API",
    description="RESTful API for managing tasks and projects"
)
```

#### `list_projects()`

Lists all projects.

#### `get_project(project_id)`

Gets detailed project information.

#### `update_project(project_id, title=None, description=None, github_repo=None)`

Updates project details.

#### `delete_project(project_id)`

Deletes a project.

### Task Management

#### `create_task(project_id, title, description, assignee="User", ...)`

Creates a new task in a project.

**Assignee options**:

- `"User"`: Manual tasks
- `"Archon"`: AI-driven tasks
- `"AI IDE Agent"`: Code implementation
- `"prp-executor"`: PRP coordination
- `"prp-validator"`: Testing/validation

**Example**:

```python
create_task(
    project_id="550e8400-e29b-41d4-a716-446655440000",
    title="Implement OAuth2 Google provider",
    description="Add Google OAuth2 with PKCE security",
    assignee="AI IDE Agent",
    task_order=10,
    feature="authentication",
    sources=[
        {
            "url": "https://developers.google.com/identity/protocols/oauth2",
            "type": "documentation",
            "relevance": "Official OAuth2 implementation guide"
        }
    ],
    code_examples=[
        {
            "file": "src/auth/base.py",
            "function": "BaseAuthProvider",
            "purpose": "Base class to extend"
        }
    ]
)
```

#### `list_tasks(filter_by=None, filter_value=None, project_id=None, include_closed=False, page=1, per_page=50)`

Lists tasks with filtering.

**Filter options**:

- `filter_by="status"`, `filter_value="todo|doing|review|done"`
- `filter_by="project"`, `filter_value="project-uuid"`
- `filter_by="assignee"`, `filter_value="AI IDE Agent"`

#### `get_task(task_id)`

Gets detailed task information.

#### `update_task(task_id, title=None, status=None, assignee=None, ...)`

Updates task properties.

**Example**:

```python
# Mark task as in progress
update_task(task_id="uuid", status="doing")

# Complete task
update_task(task_id="uuid", status="done")
```

#### `delete_task(task_id)`

Archives a task (soft delete).

### Document Management

#### `create_document(project_id, title, document_type, content=None, tags=None, author=None)`

Creates a document with automatic versioning.

**Document types**:

- `"spec"`: Technical specifications
- `"design"`: Design documents
- `"note"`: General notes
- `"prp"`: Product requirement prompts
- `"api"`: API documentation
- `"guide"`: User guides

**Example**:

```python
create_document(
    project_id="550e8400-e29b-41d4-a716-446655440000",
    title="REST API Specification",
    document_type="spec",
    content={
        "endpoints": [
            {"path": "/users", "method": "GET", "description": "List users"}
        ],
        "authentication": "Bearer token",
        "version": "1.0.0"
    },
    tags=["api", "backend"],
    author="API Team"
)
```

#### `list_documents(project_id)`

Lists all documents for a project.

#### `get_document(project_id, doc_id)`

Gets document details.

#### `update_document(project_id, doc_id, title=None, content=None, tags=None, author=None)`

Updates document properties.

#### `delete_document(project_id, doc_id)`

Deletes a document.

### Knowledge Base & RAG

#### `get_available_sources()`

Lists available sources in the knowledge base.

**Returns**:

```json
{
  "success": true,
  "sources": [
    { "domain": "docs.anthropic.com", "count": 150 },
    { "domain": "developers.google.com", "count": 85 }
  ],
  "count": 2
}
```

#### `perform_rag_query(query, source_domain=None, match_count=5)`

Searches knowledge base using RAG.

**Example**:

```python
perform_rag_query(
    query="OAuth2 implementation best practices",
    source_domain="docs.anthropic.com",
    match_count=5
)
```

**Returns**:

```json
{
  "success": true,
  "results": [
    {
      "content": "...",
      "metadata": { "url": "...", "title": "..." },
      "score": 0.95
    }
  ],
  "reranked": true
}
```

#### `search_code_examples(query, source_domain=None, match_count=5)`

Searches for code examples in the knowledge base.

**Example**:

```python
search_code_examples(
    query="authentication middleware Express.js",
    match_count=3
)
```

### Version Management

#### `create_version(project_id, field_name, content, change_summary=None, document_id=None, created_by="system")`

Creates a version snapshot.

**Field names**:

- `"docs"`: Document arrays
- `"features"`: Feature status objects
- `"data"`: General data objects
- `"prd"`: Product requirement documents

**Example**:

```python
create_version(
    project_id="550e8400-e29b-41d4-a716-446655440000",
    field_name="docs",
    content=[{"id": "doc-1", "title": "Guide", "content": {...}}],
    change_summary="Updated user guide"
)
```

#### `list_versions(project_id, field_name=None)`

Lists version history.

#### `get_version(project_id, field_name, version_number)`

Gets specific version details.

#### `restore_version(project_id, field_name, version_number, restored_by="system")`

Restores a previous version.

### Features

#### `get_project_features(project_id)`

Gets features from project's features field.

**Returns**:

```json
{
  "success": true,
  "features": [
    { "name": "authentication", "status": "completed" },
    { "name": "api", "status": "in_progress" }
  ],
  "count": 2
}
```

## Workflow Patterns

### Pattern 1: Task-Driven Development

```python
# 1. Get current task
task = get_task(task_id="...")

# 2. Mark as doing
update_task(task_id="...", status="doing")

# 3. Research phase
rag_results = perform_rag_query(query="...", match_count=5)
code_examples = search_code_examples(query="...", match_count=3)

# 4. Implementation
[code here]

# 5. Mark for review
update_task(task_id="...", status="review")

# 6. Get next task
next_tasks = list_tasks(filter_by="status", filter_value="todo")
```

### Pattern 2: Project Initialization

```python
# 1. Create project
project = create_project(
    title="My Project",
    description="Project description",
    github_repo="https://github.com/org/repo"
)

# 2. Create initial tasks
create_task(project_id=project["project_id"], title="Setup", ...)
create_task(project_id=project["project_id"], title="Implement", ...)

# 3. Create documentation
create_document(
    project_id=project["project_id"],
    title="Project Plan",
    document_type="design",
    content={...}
)

# 4. Start first task
first_task = list_tasks(project_id=project["project_id"])[0]
update_task(task_id=first_task["task_id"], status="doing")
```

### Pattern 3: Research-First Development

```python
# 1. Check available sources
sources = get_available_sources()

# 2. Query knowledge base
docs = perform_rag_query(
    query="feature implementation",
    source_domain="docs.anthropic.com",
    match_count=5
)

# 3. Find code examples
examples = search_code_examples(
    query="similar feature",
    match_count=3
)

# 4. Create task with sources
create_task(
    project_id="...",
    title="Implement Feature",
    sources=[
        {"url": docs[0]["url"], "type": "documentation", "relevance": "..."}
    ],
    code_examples=[
        {"file": examples[0]["file"], "function": "...", "purpose": "..."}
    ]
)
```

## Best Practices

### Task Management

1. **ONE task 'doing' at a time** - focus on single task
2. **Clear descriptions** - include acceptance criteria
3. **Use features** - group related tasks with feature labels
4. **Add sources** - link relevant documentation
5. **Track progress** - update status as you work

### Research Patterns

1. **Check sources first** - `get_available_sources()` to know what's available
2. **Use specific queries** - more specific = better results
3. **Combine RAG + code search** - docs + examples = complete picture
4. **Keep match_count around 3-5** - focused results

### Version Control

1. **Version at milestones** - after completing major features
2. **Clear change summaries** - describe what changed and why
3. **Use field_name appropriately** - docs vs features vs data vs prd
4. **Document id for specific docs** - when versioning single document

### Error Handling

1. **Check success field** - all responses have `{"success": bool}`
2. **Handle errors gracefully** - check error messages
3. **Validate inputs** - required fields, UUIDs, etc.
4. **Retry logic** - implement for transient failures

## Common Patterns

### Syncing Project State

```python
# 1. Get project info
project = get_project(project_id="...")

# 2. Get all tasks
tasks = list_tasks(project_id=project["project_id"], include_closed=True)

# 3. Update based on actual state
for task in tasks:
    # Check actual file state
    if file_exists(task["related_file"]):
        update_task(task_id=task["task_id"], status="done")
```

### Creating Task from PRP

```python
# 1. Read PRP file
prp_content = read_file("PRPs/feature.md")

# 2. Extract phases and tasks
phases = parse_prp_phases(prp_content)

# 3. Create tasks in Archon
for phase in phases:
    create_task(
        project_id="...",
        title=phase["title"],
        description=phase["description"],
        feature=phase["feature"],
        sources=phase["sources"]
    )
```

### Daily Workflow

```python
# Morning: Check what to work on
todo_tasks = list_tasks(
    filter_by="status",
    filter_value="todo",
    project_id="..."
)

# Pick task and start
current_task = todo_tasks[0]
update_task(task_id=current_task["task_id"], status="doing")

# Research
research = perform_rag_query(query=current_task["title"])

# [Work on task]

# Complete
update_task(task_id=current_task["task_id"], status="review")
```

## Integration with Claude Code

### With PRP System

```bash
# 1. Create PRP
/prp-create oauth-integration

# 2. Convert to Archon tasks
[Agent reads PRP and creates tasks in Archon]

# 3. Track execution
[As PRP executes, update task statuses]
```

### With Project Initializer

```bash
# 1. Initialize project
/init-project "My Project"

# 2. Create in Archon
[Agent creates project and initial tasks]

# 3. Sync throughout development
[Agent updates task statuses as work progresses]
```

## Troubleshooting

### "Task not updating"

- Check task_id is correct UUID
- Verify project exists
- Check status is valid: todo/doing/review/done

### "RAG query returns no results"

- Check available sources first
- Make query more specific
- Try without source_domain filter
- Increase match_count

### "Project not found"

- Verify project_id is correct
- Use list_projects() to see all projects
- Check if project was deleted

### "Version restore failed"

- Verify version_number exists (use list_versions)
- Check field_name is correct
- Ensure version isn't corrupted

## Advanced Patterns

### Pattern 4: Multi-Stage Implementation with RAG

```python
# Stage 1: Research
sources = get_available_sources()
print(f"Available knowledge sources: {len(sources['sources'])}")

# Query for architecture patterns
arch_docs = perform_rag_query(
    query="microservices architecture best practices",
    source_domain="docs.anthropic.com",
    match_count=5
)

# Query for implementation examples
code_examples = search_code_examples(
    query="Express.js microservice boilerplate",
    match_count=3
)

# Stage 2: Create project with research
project = create_project(
    title="Microservices Platform",
    description="Scalable microservices architecture based on research findings",
    github_repo="https://github.com/org/microservices"
)

# Stage 3: Create tasks with sources
for idx, doc in enumerate(arch_docs['results']):
    create_task(
        project_id=project["project_id"],
        title=f"Implement {doc['metadata']['title']} pattern",
        description=doc['content'][:500],  # First 500 chars as description
        assignee="AI IDE Agent",
        task_order=idx * 10,
        sources=[{
            "url": doc['metadata']['url'],
            "type": "documentation",
            "relevance": f"Score: {doc['score']}"
        }]
    )

# Stage 4: Add code example references
for example in code_examples['results']:
    update_task(
        task_id=tasks[0]["task_id"],
        code_examples=[{
            "file": example['file'],
            "function": example['function'],
            "purpose": example['summary']
        }]
    )
```

### Pattern 5: Version-Controlled Documentation Pipeline

```python
# 1. Create initial documentation
doc = create_document(
    project_id="...",
    title="API Specification v1.0",
    document_type="api",
    content={
        "version": "1.0.0",
        "endpoints": [],
        "schemas": {}
    },
    tags=["api", "v1"],
    author="System"
)

# 2. Create version checkpoint
create_version(
    project_id="...",
    field_name="docs",
    content=[doc],
    change_summary="Initial API spec v1.0",
    document_id=doc["document_id"]
)

# 3. Update documentation as features complete
updated_content = {
    "version": "1.1.0",
    "endpoints": [
        {"path": "/users", "method": "GET"},
        {"path": "/auth", "method": "POST"}
    ],
    "schemas": {"User": {...}}
}

update_document(
    project_id="...",
    doc_id=doc["document_id"],
    content=updated_content
)

# 4. Create new version
create_version(
    project_id="...",
    field_name="docs",
    content=[updated_content],
    change_summary="Added user and auth endpoints",
    document_id=doc["document_id"]
)

# 5. If needed, restore previous version
restore_version(
    project_id="...",
    field_name="docs",
    version_number=1,
    restored_by="admin"
)
```

### Pattern 6: Feature-Based Task Organization

```python
# 1. Define features
features = ["authentication", "api", "database", "frontend"]

# 2. Create tasks grouped by feature
for feature in features:
    # Research phase
    rag_results = perform_rag_query(
        query=f"{feature} implementation best practices",
        match_count=3
    )

    # Planning task
    create_task(
        project_id="...",
        title=f"Plan {feature} architecture",
        description=f"Design {feature} based on research",
        assignee="Archon",
        feature=feature,
        task_order=0,
        sources=[{
            "url": r['metadata']['url'],
            "type": "documentation",
            "relevance": r['content'][:100]
        } for r in rag_results['results']]
    )

    # Implementation task
    create_task(
        project_id="...",
        title=f"Implement {feature}",
        description=f"Code {feature} module",
        assignee="AI IDE Agent",
        feature=feature,
        task_order=10
    )

    # Testing task
    create_task(
        project_id="...",
        title=f"Test {feature}",
        description=f"Validate {feature} functionality",
        assignee="prp-validator",
        feature=feature,
        task_order=20
    )

# 3. Track progress by feature
for feature in features:
    tasks = list_tasks(
        project_id="...",
        filter_by="status",
        filter_value="todo"
    )

    feature_tasks = [t for t in tasks if t.get("feature") == feature]
    print(f"{feature}: {len(feature_tasks)} tasks remaining")
```

### Pattern 7: Automated Status Synchronization

```python
import os
from pathlib import Path

def sync_task_status_with_filesystem(project_id):
    """Automatically update task status based on filesystem state"""

    # Get all project tasks
    tasks = list_tasks(project_id=project_id, include_closed=False)

    for task in tasks:
        # Extract file references from task
        related_files = extract_file_references(task['description'])

        for file_path in related_files:
            if Path(file_path).exists():
                # File exists, check if it has tests
                test_file = get_test_file_path(file_path)

                if Path(test_file).exists():
                    # Has tests, mark as review
                    update_task(
                        task_id=task['task_id'],
                        status='review'
                    )
                else:
                    # Exists but no tests, mark as doing
                    update_task(
                        task_id=task['task_id'],
                        status='doing'
                    )
            else:
                # File doesn't exist, keep as todo
                if task['status'] != 'todo':
                    update_task(
                        task_id=task['task_id'],
                        status='todo'
                    )

def extract_file_references(text):
    """Extract file paths from task description"""
    import re
    pattern = r'`([^`]+\.(py|js|ts|jsx|tsx))`'
    return re.findall(pattern, text)

def get_test_file_path(src_path):
    """Convert source path to test path"""
    if '/src/' in src_path:
        return src_path.replace('/src/', '/tests/').replace('.', '.test.')
    return src_path.replace('.', '.test.')
```

### Pattern 8: Knowledge-Driven Task Creation

```python
def create_tasks_from_knowledge_base(project_id, goal):
    """Create tasks based on RAG knowledge"""

    # 1. Query for implementation steps
    steps_query = perform_rag_query(
        query=f"step by step guide for {goal}",
        match_count=5
    )

    # 2. Query for pitfalls and best practices
    pitfalls_query = perform_rag_query(
        query=f"common mistakes and best practices for {goal}",
        match_count=3
    )

    # 3. Search for code examples
    examples = search_code_examples(
        query=goal,
        match_count=5
    )

    # 4. Create tasks from steps
    for idx, step in enumerate(steps_query['results']):
        # Extract step title from content
        step_title = step['content'].split('\n')[0][:100]

        # Find relevant examples
        relevant_examples = [
            ex for ex in examples['results']
            if any(keyword in ex['summary'].lower()
                   for keyword in step_title.lower().split())
        ]

        # Create task
        create_task(
            project_id=project_id,
            title=step_title,
            description=step['content'][:500],
            assignee="AI IDE Agent",
            task_order=idx * 10,
            sources=[{
                "url": step['metadata']['url'],
                "type": "documentation",
                "relevance": f"Implementation step {idx + 1}"
            }] + [{
                "url": p['metadata']['url'],
                "type": "documentation",
                "relevance": "Best practices and pitfalls"
            } for p in pitfalls_query['results']],
            code_examples=[{
                "file": ex['file'],
                "function": ex['function'],
                "purpose": ex['summary']
            } for ex in relevant_examples]
        )

    # 5. Create validation task
    create_task(
        project_id=project_id,
        title=f"Validate {goal} implementation",
        description="Ensure all steps are complete and best practices followed",
        assignee="prp-validator",
        task_order=len(steps_query['results']) * 10,
        sources=[{
            "url": p['metadata']['url'],
            "type": "documentation",
            "relevance": "Validation checklist"
        } for p in pitfalls_query['results']]
    )

# Usage
create_tasks_from_knowledge_base(
    project_id="...",
    goal="OAuth2 authentication with JWT tokens"
)
```

## Integration Examples

### Example 1: PRP to Archon Sync

```python
def sync_prp_to_archon(prp_file_path, project_id):
    """Convert PRP phases to Archon tasks"""

    with open(prp_file_path, 'r') as f:
        prp_content = f.read()

    # Parse PRP phases
    phases = parse_prp_phases(prp_content)

    # Create tasks for each phase
    for phase in phases:
        # Query RAG for additional context
        rag_context = perform_rag_query(
            query=phase['title'],
            match_count=2
        )

        # Create task
        task = create_task(
            project_id=project_id,
            title=phase['title'],
            description=phase['description'],
            assignee=phase.get('assignee', 'AI IDE Agent'),
            feature=phase.get('feature'),
            sources=[{
                "url": r['metadata']['url'],
                "type": "documentation",
                "relevance": "Additional context"
            } for r in rag_context['results']]
        )

        print(f"Created task: {task['task_id']} - {phase['title']}")

def parse_prp_phases(prp_content):
    """Extract phases from PRP markdown"""
    import re

    phases = []
    phase_pattern = r'### Phase \d+: (.+?)\n(.+?)(?=### Phase|\Z)'

    for match in re.finditer(phase_pattern, prp_content, re.DOTALL):
        phases.append({
            'title': match.group(1).strip(),
            'description': match.group(2).strip()[:500]
        })

    return phases
```

### Example 2: Archon to GitHub Issues

```python
def export_tasks_to_github_issues(project_id, github_repo):
    """Export Archon tasks to GitHub issues"""

    # Get all todo tasks
    tasks = list_tasks(
        project_id=project_id,
        filter_by="status",
        filter_value="todo"
    )

    for task in tasks:
        # Format issue body
        issue_body = f"""## Description
{task['description']}

## Sources
"""
        for source in task.get('sources', []):
            issue_body += f"- [{source['type']}]({source['url']}): {source['relevance']}\n"

        issue_body += "\n## Code Examples\n"
        for example in task.get('code_examples', []):
            issue_body += f"- `{example['file']}` - {example['function']}: {example['purpose']}\n"

        issue_body += f"\n---\n*Generated from Archon task: {task['task_id']}*"

        # Create GitHub issue (using gh CLI or API)
        # gh issue create --repo {github_repo} --title "{task['title']}" --body "{issue_body}"

        print(f"Created issue: {task['title']}")
```

## Health Check and Diagnostics

```python
def archon_health_check():
    """Check Archon MCP server health"""

    try:
        # Test basic connectivity
        sources = get_available_sources()
        print(f"✅ Connected to Archon")
        print(f"   Available sources: {len(sources['sources'])}")

        # Test RAG functionality
        test_query = perform_rag_query(
            query="test query",
            match_count=1
        )
        print(f"✅ RAG search working")

        # List projects
        projects = list_projects()
        print(f"✅ Project management working")
        print(f"   Active projects: {len(projects)}")

        return True

    except Exception as e:
        print(f"❌ Archon health check failed: {e}")
        return False

def project_diagnostics(project_id):
    """Run diagnostics on a project"""

    # Get project info
    project = get_project(project_id)
    print(f"Project: {project['title']}")

    # Task status breakdown
    all_tasks = list_tasks(project_id=project_id, include_closed=True)
    status_counts = {}
    for task in all_tasks:
        status = task['status']
        status_counts[status] = status_counts.get(status, 0) + 1

    print("\nTask Status:")
    for status, count in status_counts.items():
        print(f"  {status}: {count}")

    # Document count
    docs = list_documents(project_id)
    print(f"\nDocuments: {len(docs)}")

    # Version history
    versions = list_versions(project_id)
    print(f"Version snapshots: {len(versions)}")

    # Check for stuck tasks (doing > 24h)
    import datetime
    now = datetime.datetime.now()

    doing_tasks = [t for t in all_tasks if t['status'] == 'doing']
    for task in doing_tasks:
        created = datetime.datetime.fromisoformat(task['created_at'])
        hours_old = (now - created).total_seconds() / 3600

        if hours_old > 24:
            print(f"\n⚠️  Stuck task: {task['title']} ({hours_old:.1f}h in 'doing')")
```

## Error Recovery Patterns

```python
def safe_task_transition(task_id, new_status, retry_count=3):
    """Safely transition task status with retries"""

    for attempt in range(retry_count):
        try:
            result = update_task(task_id=task_id, status=new_status)

            if result['success']:
                print(f"✅ Task {task_id} -> {new_status}")
                return result
            else:
                print(f"⚠️  Attempt {attempt + 1} failed: {result.get('error')}")

        except Exception as e:
            print(f"❌ Attempt {attempt + 1} error: {e}")

        # Exponential backoff
        import time
        time.sleep(2 ** attempt)

    print(f"❌ Failed to update task after {retry_count} attempts")
    return {"success": False, "error": "Max retries exceeded"}

def recover_orphaned_tasks(project_id):
    """Find and fix tasks stuck in 'doing' with no activity"""

    import datetime

    tasks = list_tasks(
        project_id=project_id,
        filter_by="status",
        filter_value="doing"
    )

    for task in tasks:
        created = datetime.datetime.fromisoformat(task['created_at'])
        hours_old = (datetime.datetime.now() - created).total_seconds() / 3600

        if hours_old > 48:  # Stuck for 48+ hours
            print(f"Found orphaned task: {task['title']}")

            # Reset to todo
            safe_task_transition(task['task_id'], 'todo')

            # Add note to description
            update_task(
                task_id=task['task_id'],
                description=f"{task['description']}\n\n**Note**: Auto-reset from stuck 'doing' status"
            )
```

## Examples from Real Projects

See `.claude/memories/archon_usage_patterns.md` for real-world examples of successful Archon integration patterns.
