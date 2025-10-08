# Sistema de Agentes Orquestados

**ARQUITECTURA AUTOMÁTICA**: Claude Code ejecuta automáticamente **@task-planner** para coordinar agentes especializados. No necesitas invocar agentes manualmente.

---

## 🔄 **Flujo de Trabajo Automático**

```
Usuario solicita tarea
        ↓
[@task-planner] SIEMPRE se ejecuta primero
        ↓
   Analiza complejidad
        ↓
Coordina agentes especializados (paralelo/secuencial)
        ↓
[@task-executor] Implementa el plan
        ↓
[@validation-gates] Valida resultados
        ↓
[@documentation-manager] Actualiza docs
```

---

## 📊 **Matriz de Agentes**

| Agente                     | Rol                        | Trigger                         | Documentación                                                  |
| -------------------------- | -------------------------- | ------------------------------- | -------------------------------------------------------------- |
| **@task-planner**          | 🧠 Coordinador Maestro     | Automático >3 pasos             | [task-planner.md](../agents/task-planner.md)                   |
| **@task-executor**         | ⚙️ Ejecutor Sistemático    | Por @task-planner               | [task-executor.md](../agents/task-executor.md)                 |
| **@project-initializer**   | 🚀 Inicializador Proyectos | `/init-project`                 | [project-initializer.md](../agents/project-initializer.md)     |
| **@prp-expert**            | 📋 Especialista PRPs       | Comandos `/prp-*`               | [prp-expert.md](../agents/prp-expert.md)                       |
| **@prp-validator**         | 🛡️ Validador PRPs          | Por @prp-expert                 | [prp-validator.md](../agents/prp-validator.md)                 |
| **@archon-expert**         | 📊 Gestor Archon MCP       | Research/Planning phases        | [archon-expert.md](../agents/archon-expert.md)                 |
| **@validation-gates**      | ✅ Validador de Calidad    | Por @task-executor (SIEMPRE)    | [validation-gates.md](../agents/validation-gates.md)           |
| **@documentation-manager** | 📚 Gestor de Docs          | Cambios código + 10% context    | [documentation-manager.md](../agents/documentation-manager.md) |
| **@codebase-analyst**      | 🔍 Analista de Código      | Por @task-planner + @prp-expert | [codebase-analyst.md](../agents/codebase-analyst.md)           |
| **@library-researcher**    | 📖 Investigador ⭐ CRÍTICO | Por @task-planner + @prp-expert | [library-researcher.md](../agents/library-researcher.md)       |
| **@code-executor**         | ⚙️ Experto en Codificación | Por @task-executor              | [code-executor.md](../agents/code-executor.md)                 |
| **@test-expert**           | 🧪 Especialista Tests      | Por @code-executor              | [test-expert.md](../agents/test-expert.md)                     |
| **@file-optimizer**        | 📁 Optimizador Estructura  | Usuario explícito + >400 líneas | [file-optimizer.md](../agents/file-optimizer.md)               |
| **@command-optimizer**     | 🔧 Gestor Comandos         | Por @task-planner + Usuario     | [command-optimizer.md](../agents/command-optimizer.md)         |

---

## 🎯 **Agentes Principales - Resumen**

### **Categoría: Orquestación**

- **[@task-planner](../agents/task-planner.md)** - Coordinador maestro con Sequential Thinking (8-15 thoughts)
- **[@task-executor](../agents/task-executor.md)** - Ejecutor sistemático que implementa planes estructurados
- **[@project-initializer](../agents/project-initializer.md)** - Bootstrap de proyectos nuevos desde template

### **Categoría: Pattern Recognition**

- **[@prp-expert](../agents/prp-expert.md)** - Crea y ejecuta PRPs con análisis profundo
- **[@prp-validator](../agents/prp-validator.md)** - Valida PRPs con scoring Pareto 80-20

### **Categoría: Knowledge & Research**

- **[@archon-expert](../agents/archon-expert.md)** - Gestión de proyectos y RAG knowledge base
- **[@codebase-analyst](../agents/codebase-analyst.md)** - Análisis profundo con Serena MCP
- **[@library-researcher](../agents/library-researcher.md)** ⭐ **CRÍTICO** - Research de bibliotecas externas

### **Categoría: Quality & Validation**

- **[@validation-gates](../agents/validation-gates.md)** - 4 niveles de validación (Syntax → Style → Tests → Build)
- **[@documentation-manager](../agents/documentation-manager.md)** - Sincronización docs-código + compactación automática

### **Categoría: Implementation**

- **[@code-executor](../agents/code-executor.md)** - Implementación de código con TDD
- **[@test-expert](../agents/test-expert.md)** - Generación de tests exhaustivos

### **Categoría: Optimization**

- **[@file-optimizer](../agents/file-optimizer.md)** - Optimización de estructura (límite 500 líneas)
- **[@command-optimizer](../agents/command-optimizer.md)** - Gestión de comandos personalizados

---

## ⚡ **Principios Clave del Sistema**

### **1. Orquestación Automática** 🤖

- @task-planner coordina TODO automáticamente
- Usuario ejecuta comandos, sistema ejecuta agentes
- Paralelo cuando es seguro, secuencial con dependencias

### **2. Especialización** 🎯

- Cada agente tiene UN rol claro
- Delega, no hace trabajo directo
- Right tool for the job

### **3. Validación Continua** ✅

- @validation-gates después de CADA cambio
- 4 niveles: Syntax → Style → Tests → Build
- Itera hasta que TODO pase

### **4. Checkpoints Humanos** ✋

- **CHECKPOINT 1 (Research)**: ROI 100x - Ahorra 1000s líneas mal dirigidas
- **CHECKPOINT 2 (Planning)**: ROI 10-20x - Ahorra 10-100 líneas re-trabajo
- NUNCA asume "approve", espera respuesta explícita

### **5. Research-First** 🔍

- @archon-expert consulta RAG knowledge base
- @codebase-analyst encuentra patterns existentes
- @library-researcher investiga best practices
- ANTES de implementar

### **6. TDD Obligatorio** 🧪

- Tests PRIMERO, código después
- @validation-gates asegura compliance
- Target: 100% coverage

### **7. Documentación Sincronizada** 📚

- @documentation-manager actualiza SIEMPRE
- Out-of-date docs = peor que no docs
- Compactación automática al 10% context

---

## 🔄 **Flujos de Trabajo Típicos**

### **Feature Nueva Compleja**

```
Usuario: "Implementar autenticación JWT"
    ↓
@task-planner (Sequential Thinking 8-15 thoughts)
    ↓
Phase 1: Research (45-60 min, PARALELO)
    → @library-researcher (JWT best practices)
    → @codebase-analyst (patterns existentes)
    → @archon-expert (RAG query)
    ↓
✅ CHECKPOINT 1 (ROI 100x) - WAIT FOR APPROVAL
    ↓
Phase 2: Planning (30-45 min)
    → @documentation-manager (create /planning/planning_auth.md)
    ↓
✅ CHECKPOINT 2 (ROI 10-20x) - WAIT FOR APPROVAL
    ↓
Phase 3: TDD Implementation (2-3 hours)
    → @task-executor orchestrates:
        → @test-expert (tests FIRST)
        → @code-executor (código to pass tests)
        → @validation-gates (AFTER each component)
    ↓
Phase 4: Final Validation (30 min)
    → @validation-gates (full suite)
    → @documentation-manager (update README, CLAUDE.md)
    ↓
✅ DONE
```

### **PRP Execution**

```
Usuario: "/prp:prp-story-task-create [story]"
    ↓
@prp-expert
    ↓
Research Phase (PARALELO):
    → @library-researcher (external docs)
    → @codebase-analyst (internal patterns)
    ↓
Generate PRP markdown
    ↓
@prp-validator (Pareto 80-20 scoring)
    ↓
✅ CHECKPOINT - Present PRP for approval
    ↓
Execute PRP fase por fase:
    → @test-expert (tests first)
    → @code-executor (implementation)
    → @validation-gates (AFTER each task)
    ↓
✅ DONE
```

### **Nuevo Proyecto**

```
Usuario: "/init-project mi-app ~/Desktop"
    ↓
@project-initializer
    ↓
Phase 0-2: Goal + Research
    → @archon-expert (create project in Archon)
    → @library-researcher (research tech stack)
    ↓
✅ CHECKPOINT 1 (Research findings)
    ↓
Phase 3-7: Planning
    → @codebase-analyst (analyze template patterns)
    → @documentation-manager (create planning docs)
    ↓
✅ CHECKPOINT 2 (Architecture plan)
    ↓
Phase 8: TDD Implementation
    → Copy template structure
    → @command-optimizer (setup commands)
    → @validation-gates (validate setup)
    ↓
Phase 9: Final Validation
    → @validation-gates (full test suite)
    ↓
Phase 10: Self-Improvement Setup
    → @documentation-manager (finalize docs)
    ↓
✅ DONE - Project ready
```

---

## 📖 **Documentación Detallada**

Para información completa sobre cada agente, consulta los archivos individuales en `.claude/agents/`:

```
.claude/agents/
├── task-planner.md          # Coordinador maestro (Sequential Thinking)
├── task-executor.md         # Ejecutor sistemático
├── project-initializer.md   # Bootstrap de proyectos
├── prp-expert.md            # Pattern Recognition Protocols
├── prp-validator.md         # Validación de PRPs
├── archon-expert.md         # Archon MCP + RAG
├── validation-gates.md      # 4 niveles de validación
├── documentation-manager.md # Docs + context management
├── codebase-analyst.md      # Análisis con Serena MCP
├── library-researcher.md    # Research externo (CRÍTICO)
├── code-executor.md         # Implementación TDD
├── test-expert.md           # Generación de tests
├── file-optimizer.md        # Optimización de estructura
└── command-optimizer.md     # Gestión de comandos
```

Cada archivo `.md` contiene:

- **ROL** detallado del agente
- **Se activa cuando** (triggers específicos)
- **Lo que hace** (paso a paso)
- **Agentes que coordina/delega**
- **MCPs que utiliza**
- **Principios clave**
- **Anti-patterns** (lo que NUNCA hace)
- **Ejemplos de uso**

---

## 🚀 **Comandos Relacionados**

- `/init-project [nombre]` - Inicializar nuevo proyecto (@project-initializer)
- `/prp:prp-story-task-create [story]` - Crear PRP (@prp-expert)
- `/prp:prp-story-task-execute [file]` - Ejecutar PRP (@prp-expert)
- `/prp-validate [file]` - Validar PRP (@prp-validator)
- `/update-context` - Actualizar documentación (@documentation-manager)
- `/compact-context` - Compactar contexto (@documentation-manager)

Ver guía completa: [.claude/docs/COMMANDS.md](COMMANDS.md)

---

## 🔗 **Referencias Relacionadas**

- **[CHECKPOINTS.md](CHECKPOINTS.md)** - Checkpoints críticos detallados (ROI 100x y 10-20x)
- **[WORKFLOWS.md](WORKFLOWS.md)** - Flujos de trabajo y diagramas completos
- **[COMMANDS.md](COMMANDS.md)** - Guía completa de comandos

---

**Versión**: 3.1.0
**Total Agentes**: 14
**Última Actualización**: 2025-10-07

---

_Este archivo es un índice. Para documentación completa de cada agente, ver `.claude/agents/[nombre-agente].md`_
