# TEMPLATES.md - Template System Documentation

> **Complete guide** to the Jinja2 template system for project generation

---

## 🎯 **Overview**

This template uses **Jinja2** to generate complete automation projects from natural language requests. Templates are modular and adapt to project complexity.

**Template Complexity Levels:**
- **Simple**: 1-2 APIs, direct workflow, no orchestration
- **Medium**: 3-5 APIs, orchestrator included, memory system
- **High**: 5+ APIs, advanced orchestration, @self-improve agent

---

## 📁 **Template Structure**

```
.claude/templates/
├── base/                    # COMMON to ALL projects
│   ├── README.md.j2
│   ├── CLAUDE.md.j2
│   ├── .claude/
│   │   ├── PLANNING.md.j2
│   │   ├── TASK.md.j2
│   │   └── PRP.md.j2
│   ├── .gitignore
│   └── requirements.txt.j2  # Python projects
│
├── medium/                  # ADDITIONAL for medium complexity
│   └── orchestrator/
│       ├── __init__.py
│       ├── agent.py.j2      # Main orchestrator
│       ├── models.py.j2     # Pydantic models
│       └── memory.py        # Memory system
│
└── high/                    # ADDITIONAL for high complexity
    └── .claude/agents/
        └── @self-improve.md  # Self-improvement agent
```

**Rendering Logic:**
- **ALL projects** get `base/` templates
- **Medium + High** get `base/` + `medium/` templates
- **High only** gets `base/` + `medium/` + `high/` templates

---

## 🔧 **Template Variables**

### **Available Variables** (from AutomationIntent)

```python
{
    # Project basics
    "project_name": str,              # e.g., "gmail-notion-automation"
    "goal": str,                      # e.g., "Automate emails to Notion"
    "complexity": str,                # "simple" | "medium" | "high"

    # APIs and integrations
    "apis": List[APIIntegration],     # List of API objects
    "tech_stack": List[str],          # ["Python"] or ["Node.js"]

    # Workflow details
    "workflow_steps": List[str],      # Ordered list of steps
    "input_description": str,         # What the system receives
    "output_description": str,        # What the system produces

    # Agents and tools
    "suggested_agents": List[str],    # Recommended agents

    # Metadata
    "current_date": str,              # "2025-01-03"
    "version": str,                   # "1.0.0"
    "status": str,                    # "Development"
    "repo_url": str,                  # Optional
    "license": str,                   # "MIT"
}
```

### **API Integration Object Structure**

```python
{
    "name": str,                      # "Gmail"
    "description": str,               # "Email reading and management"
    "auth_type": str,                 # "OAuth2" | "Token" | "APIKey"
    "endpoints": List[str],           # ["read", "send"]
}
```

---

## 📝 **Using Variables in Templates**

### **Basic Variable Substitution**

```jinja2
# {{ project_name }}

{{ goal }}

**Complexity**: {{ complexity|capitalize }}
```

### **Conditional Logic**

```jinja2
{% if complexity == 'simple' %}
This is a simple project with straightforward architecture.
{% elif complexity == 'medium' %}
This is a medium complexity project with orchestration.
{% elif complexity == 'high' %}
This is a high complexity project with self-improvement.
{% endif %}
```

### **Looping Over Lists**

```jinja2
### Integrated APIs
{% for api in apis %}
- **{{ api.name }}**: {{ api.description }}
  - Authentication: {{ api.auth_type }}
  - Endpoints: {{ api.endpoints|length }} endpoints
{% endfor %}
```

### **Filters**

```jinja2
{{ project_name|title }}                    # Gmail Notion Automation
{{ project_name|upper }}                    # GMAIL-NOTION-AUTOMATION
{{ project_name|replace('-', '_') }}        # gmail_notion_automation
{{ complexity|capitalize }}                 # Simple
{{ tech_stack|join(', ') }}                # Python, Node.js
{{ apis|length }}                          # 3
```

### **Default Values**

```jinja2
{{ repo_url|default("https://github.com/user/" + project_name) }}
{{ license|default("MIT License") }}
{{ version|default("1.0.0") }}
```

---

## 🚀 **How Templates are Rendered**

### **Step-by-Step Process**

#### **1. Initialize Jinja2 Environment**

```python
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

template_dir = Path(".claude/templates/")
env = Environment(loader=FileSystemLoader(template_dir))
```

#### **2. Prepare Template Variables**

```python
from orchestrator import OrchestratorAgent

# Get intent from orchestrator
orchestrator = OrchestratorAgent()
intent = await orchestrator.analyze_intent(user_input)

# Prepare variables
template_vars = {
    "project_name": intent.project_name,
    "goal": intent.goal,
    "complexity": intent.complexity,
    "apis": intent.apis,
    "tech_stack": intent.tech_stack,
    # ... all other fields
}
```

#### **3. Render Base Templates**

```python
base_templates = [
    ("base/README.md.j2", "README.md"),
    ("base/CLAUDE.md.j2", "CLAUDE.md"),
    ("base/.claude/PLANNING.md.j2", ".claude/PLANNING.md"),
    # ... etc
]

for template_path, output_path in base_templates:
    template = env.get_template(template_path)
    rendered = template.render(**template_vars)

    # Write to generated project
    output_file = project_path / output_path
    output_file.write_text(rendered)
```

#### **4. Conditionally Add Medium/High Templates**

```python
# If medium or high complexity
if intent.complexity in ["medium", "high"]:
    # Render orchestrator templates
    template = env.get_template("medium/orchestrator/agent.py.j2")
    rendered = template.render(**template_vars)
    (project_path / "orchestrator/agent.py").write_text(rendered)

# If high complexity
if intent.complexity == "high":
    # Copy @self-improve agent
    import shutil
    shutil.copy(
        ".claude/templates/high/.claude/agents/@self-improve.md",
        project_path / ".claude/agents/@self-improve.md"
    )
```

---

## ✏️ **Creating New Templates**

### **1. Add Template File**

Create file in appropriate directory:
- `base/` for all projects
- `medium/` for medium+ complexity
- `high/` for high complexity only

**Naming convention**:
- Static files: `filename.ext`
- Templates: `filename.ext.j2`

### **2. Use Template Variables**

```jinja2
# my-new-template.md.j2

# {{ project_name }} - My New File

This file is for {{ goal }}.

{% if complexity == 'high' %}
Advanced features enabled!
{% endif %}
```

### **3. Update @project-initializer Phase 8.1**

Add your template to the rendering list:

```python
# In .claude/agents/project-initializer.md, Phase 8.1

base_templates.append(("base/my-new-template.md.j2", "my-new-file.md"))
```

---

## 🧪 **Testing Templates**

### **Manual Testing**

```bash
# Create test environment
python3 -m venv venv
source venv/bin/activate
pip install jinja2 pytest

# Run template tests
pytest tests/test_templates.py -v
```

### **Quick Validation**

```python
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(".claude/templates/"))

# Test render with sample data
sample_data = {
    "project_name": "test-project",
    "goal": "Test goal",
    "complexity": "simple",
    # ... add all required fields
}

template = env.get_template("base/README.md.j2")
rendered = template.render(**sample_data)
print(rendered)  # Should not raise errors
```

---

## 📊 **Template Best Practices**

### **1. Always Provide Defaults**

```jinja2
# Good
{{ license|default("MIT License") }}

# Bad (will error if license is None)
{{ license }}
```

### **2. Use Meaningful Variable Names**

```jinja2
# Good
{% for api in apis %}
  {{ api.name }}: {{ api.description }}
{% endfor %}

# Bad
{% for a in apis %}
  {{ a.n }}: {{ a.d }}
{% endfor %}
```

### **3. Handle Empty Lists**

```jinja2
{% if apis %}
### APIs Integrated
{% for api in apis %}
- {{ api.name }}
{% endfor %}
{% else %}
- No external APIs (self-contained project)
{% endif %}
```

### **4. Comment Complex Logic**

```jinja2
{# This section renders different architectures based on complexity #}
{% if complexity == 'simple' %}
  {# Simple: Direct workflow #}
  ...
{% elif complexity == 'medium' %}
  {# Medium: Orchestrator included #}
  ...
{% endif %}
```

### **5. Escape Special Characters**

```jinja2
# To include literal {{ or }}:
Use {% raw %}{{ variable }}{% endraw %}

# To include { in code blocks:
Use proper Markdown code fencing
```

---

## 🔍 **Debugging Templates**

### **Common Errors**

#### **Error: Variable not found**

```
UndefinedError: 'api_count' is undefined
```

**Solution**: Add variable to template_vars or use default:
```jinja2
{{ api_count|default(0) }}
```

#### **Error: Filter not found**

```
TemplateError: no filter named 'my_filter'
```

**Solution**: Use built-in Jinja2 filters only, or define custom filters

#### **Error: Syntax error in template**

```
TemplateSyntaxError: unexpected '}'
```

**Solution**: Check that all {% if %} have matching {% endif %}, all {% for %} have {% endfor %}, etc.

### **Debugging Techniques**

**1. Print rendered output:**
```python
template = env.get_template("base/README.md.j2")
rendered = template.render(**template_vars)
print(rendered)  # Inspect output
```

**2. Validate Jinja2 syntax:**
```python
from jinja2 import Template

template_string = open("template.j2").read()
try:
    Template(template_string)
    print("✅ Syntax valid")
except Exception as e:
    print(f"❌ Syntax error: {e}")
```

---

## 📚 **Jinja2 Reference**

### **Control Structures**

```jinja2
{% if condition %}...{% endif %}
{% if condition %}...{% else %}...{% endif %}
{% if condition %}...{% elif other %}...{% else %}...{% endif %}

{% for item in list %}...{% endfor %}
{% for key, value in dict.items() %}...{% endfor %}
```

### **Common Filters**

```jinja2
{{ variable|default("default") }}
{{ string|upper }}
{{ string|lower }}
{{ string|title }}
{{ string|capitalize }}
{{ string|replace('old', 'new') }}
{{ list|join(', ') }}
{{ list|length }}
{{ number|int }}
{{ number|float }}
```

### **Tests**

```jinja2
{% if variable is defined %}
{% if variable is none %}
{% if list is empty %}
{% if number is even %}
{% if number is odd %}
```

---

## 🎓 **Examples**

### **Example 1: Conditional API Dependencies**

**In requirements.txt.j2:**
```jinja2
{% if apis %}
{% for api in apis %}
{% if 'Gmail' in api.name or 'Google' in api.name %}
google-api-python-client==2.110.0
{% elif 'Notion' in api.name %}
notion-client==2.2.1
{% elif 'Slack' in api.name %}
slack-sdk==3.26.1
{% endif %}
{% endfor %}
{% endif %}
```

### **Example 2: Dynamic Project Structure**

**In PLANNING.md.j2:**
```jinja2
## 🏗️ Arquitectura

{% if complexity == 'simple' %}
**Simple Architecture:**
```
Input → Process → Output
```
{% elif complexity == 'medium' %}
**Orchestrated Architecture:**
```
Input → Orchestrator → APIs → Output
```
{% elif complexity == 'high' %}
**Advanced Architecture with Self-Improvement:**
```
Input → Orchestrator → Subagents → APIs → @self-improve → Output
```
{% endif %}
```

---

## 🔗 **Related Documentation**

- [@project-initializer.md](./../agents/project-initializer.md) - Main agent that uses templates
- [PLANNING.md](./PLANNING.md) - Overall architecture
- [Jinja2 Official Docs](https://jinja.palletsprojects.com/)

---

*Last updated: 2025-01-03*
*Version: 1.0.0*
*Template System: Jinja2*
