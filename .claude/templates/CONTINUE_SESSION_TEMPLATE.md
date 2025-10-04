# Continuación de Sesión - {{ timestamp }}

> **Session ID**: {{ session_id }}
> **Context Window Antes**: {{ context_percentage }}%
> **Compactado por**: {{ compacted_by }}

---

## 🎯 Objetivo de la Tarea

{{ task_objective }}

---

## ✅ Progreso Completado

### Fase 1: Research {{ "✅" if research_complete else "🔄" if research_in_progress else "⏭️" }}

{% if research_complete or research_in_progress %}
**Archivos investigados**:
{% for file in files_investigated %}
- `{{ file.path }}`{% if file.key_findings %} - {{ file.key_findings }}{% endif %}
{% endfor %}

**Hallazgos clave**:
{% for finding in key_findings %}
{{ loop.index }}. {{ finding }}
{% endfor %}

**Flujo de información identificado**:
```
{{ information_flow }}
```
{% endif %}

### Fase 2: Planning {{ "✅" if planning_complete else "🔄" if planning_in_progress else "⏭️" }}

{% if planning_complete or planning_in_progress %}
**Plan creado**: {% if plan_file %}{{ plan_file }}{% else %}Ver sección de Próximos Pasos{% endif %}

**Fases definidas**:
{% for phase in phases_defined %}
{{ loop.index }}. {{ phase.name }}: {{ phase.description }}
{% endfor %}

**Tests planificados**:
{% for test in tests_planned %}
- [ ] {{ test.name }} ({{ test.file }})
  - Objetivo: {{ test.objective }}
{% endfor %}
{% endif %}

### Fase 3: Implementation {{ "✅" if implementation_complete else "🔄" if implementation_in_progress else "⏭️" }}

{% if implementation_complete or implementation_in_progress %}
**Archivos modificados**:
{% for file in files_modified %}
- `{{ file.path }}`:{{ file.lines }} - {{ file.change_description }}
{% endfor %}

**Tests creados**:
{% for test in tests_created %}
- ✅ {{ test.name }} ({{ test.file }})
  - Estado: {{ test.status }}
{% endfor %}

**Comandos ejecutados**:
```bash
{% for command in commands_executed %}
# {{ command.description }}
{{ command.command }}
{{ command.result_summary }}

{% endfor %}
```
{% endif %}

---

## 🔍 Decisiones Arquitectónicas

{% for decision in architectural_decisions %}
### {{ loop.index }}. {{ decision.title }}

**Contexto**: {{ decision.context }}

**Opciones consideradas**:
{% for option in decision.options %}
- {{ option.name }}: {{ option.description }}
  - Pros: {{ option.pros }}
  - Contras: {{ option.cons }}
{% endfor %}

**Decisión final**: {{ decision.chosen }}

**Razón**: {{ decision.rationale }}

{% if decision.implementation_notes %}
**Notas de implementación**: {{ decision.implementation_notes }}
{% endif %}

---
{% endfor %}

---

## 🐛 Problemas Encontrados y Soluciones

{% for problem in problems_and_solutions %}
### {{ loop.index }}. {{ problem.title }}

**Problema**: {{ problem.description }}

**Contexto**:
- Archivo: `{{ problem.file }}`{% if problem.line_number %}:{{ problem.line_number }}{% endif %}
- Error: {{ problem.error_message }}

**Intentos fallidos**:
{% for attempt in problem.failed_attempts %}
{{ loop.index }}. {{ attempt.approach }} - {{ attempt.why_failed }}
{% endfor %}

**Solución que funcionó**: {{ problem.solution }}

**Código/Comando**:
```{{ problem.solution_language }}
{{ problem.solution_code }}
```

**Lección aprendida**: {{ problem.lesson }}

---
{% endfor %}

---

## 📍 Estado Actual

**Resumen de progreso**:
- Research: {{ research_progress }}%
- Planning: {{ planning_progress }}%
- Implementation: {{ implementation_progress }}%
- Testing: {{ testing_progress }}%

**Context window antes de compactar**: {{ context_percentage }}%

**Último paso completado**: {{ last_step_completed }}

**Archivos en progreso** (sin completar):
{% for file in files_in_progress %}
- `{{ file.path }}` - {{ file.status }}
  - Pendiente: {{ file.pending_work }}
{% endfor %}

**Tests en estado**:
- ✅ Pasando: {{ tests_passing }} / {{ total_tests }}
- ❌ Fallando: {{ tests_failing }} / {{ total_tests }}
- ⏭️ Pendientes: {{ tests_pending }} / {{ total_tests }}

---

## ⏭️ Próximos Pasos (En Orden de Ejecución)

{% for step in next_steps %}
{{ loop.index }}. [ ] **{{ step.title }}**
   - Acción: {{ step.action }}
   {% if step.file %}
   - Archivo: `{{ step.file }}`{% if step.line_number %}:{{ step.line_number }}{% endif %}
   {% endif %}
   {% if step.command %}
   - Comando: `{{ step.command }}`
   {% endif %}
   {% if step.expected_outcome %}
   - Resultado esperado: {{ step.expected_outcome }}
   {% endif %}
   {% if step.dependencies %}
   - Dependencias: {{ step.dependencies }}
   {% endif %}

{% endfor %}

---

## 📝 Notas Importantes

### ⚠️ Crítico - DEBE Leerse

{% for note in critical_notes %}
- **{{ note.title }}**: {{ note.description }}
{% endfor %}

### 🎯 Contexto Importante

{% for note in important_notes %}
- {{ note }}
{% endfor %}

### 🪤 Trampas Identificadas (Gotchas)

{% for gotcha in gotchas %}
- **{{ gotcha.context }}**: {{ gotcha.trap }} → {{ gotcha.solution }}
{% endfor %}

### ❌ Qué NO Hacer

{% for dont in dont_do %}
- {{ dont.action }} - Razón: {{ dont.reason }}
{% endfor %}

### 💡 Comandos que NO Funcionaron

{% for failed_cmd in failed_commands %}
- `{{ failed_cmd.command }}` - {{ failed_cmd.why_failed }}
  - Usar en su lugar: `{{ failed_cmd.alternative }}`
{% endfor %}

---

## 🔗 Referencias

### Archivos Clave

{% for file in key_files %}
- `{{ file.path }}` - {{ file.description }}
  {% if file.key_functions %}
  - Funciones importantes: {{ file.key_functions | join(", ") }}
  {% endif %}
{% endfor %}

### Documentación Relevante

{% for doc in relevant_docs %}
- [{{ doc.title }}]({{ doc.path }}) - {{ doc.description }}
{% endfor %}

### Tests Relacionados

{% for test in related_tests %}
- `{{ test.path }}` - {{ test.coverage }}
{% endfor %}

### Dependencias y APIs

{% for dep in dependencies %}
- **{{ dep.name }}** ({{ dep.version }})
  - Uso: {{ dep.usage }}
  {% if dep.docs %}
  - Docs: {{ dep.docs }}
  {% endif %}
{% endfor %}

---

## 🔄 Instrucciones para Continuar

### Prompt para Nueva Sesión

```
Estoy continuando desde una sesión anterior.

Lee .claude/CONTINUE_SESSION.md completamente y familiarízate con:
1. El objetivo de la tarea
2. Qué se ha completado hasta ahora
3. Las decisiones arquitectónicas tomadas
4. Los problemas encontrados y sus soluciones

Después de leer, confirma que entiendes el contexto y continúa con el
primer paso de la sección "Próximos Pasos".

IMPORTANTE: Sigue las notas críticas y evita las trampas identificadas.
```

### Checklist de Verificación

Antes de continuar, verifica:

- [ ] Has leído el objetivo completo de la tarea
- [ ] Entiendes las decisiones arquitectónicas tomadas
- [ ] Has revisado los problemas encontrados y soluciones
- [ ] Sabes qué archivos están en progreso
- [ ] Entiendes el estado de los tests
- [ ] Has identificado el próximo paso específico a ejecutar
- [ ] Has notado las trampas y qué NO hacer

---

## 📊 Métricas de Sesión

**Sesión anterior**:
- Duración: {{ session_duration }}
- Mensajes intercambiados: {{ message_count }}
- Tool calls ejecutados: {{ tool_calls_count }}
- Archivos leídos: {{ files_read_count }}
- Archivos modificados: {{ files_modified_count }}
- Tests ejecutados: {{ tests_run_count }}
- Context window final: {{ context_percentage }}%

**Eficiencia**:
- Progress rate: {{ progress_rate }}% por hora
- Error rate: {{ error_rate }}%
- Test success rate: {{ test_success_rate }}%

---

## 🎯 Objetivo de Esta Compactación

{{ compaction_objective }}

---

**Generado**: {{ generation_timestamp }}
**Template version**: 1.0.0
**Claude Code Template**: v3.1.0

---

_Este archivo fue generado por `/compact-context`. Revisa manualmente y agrega cualquier contexto adicional necesario antes de ejecutar `/clear`._
