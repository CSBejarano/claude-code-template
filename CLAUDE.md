# CLAUDE.md - Claude Code Template (Orchestrator Agent SDK)

> **Documento maestro del proyecto** - Template para generar proyectos de automatización con arquitectura híbrida, TDD approach y checkpoints de validación humana

**⚠️ NOTA**: Este es un template que genera proyectos. Los proyectos generados tendrán su propio CLAUDE.md personalizado.

This file provides guidance to Claude Code (claude.ai/code) when working with the template repository itself.

---

## 📚 **Sistema de Documentación**

```
🚀 QUICK_START.md          → Inicio rápido (10 min)
📖 CLAUDE.md (ESTÁS AQUÍ)  → Documentación principal compacta
📋 README.md               → Documentación del proyecto

.claude/
├── PLANNING.md            → Arquitectura y planificación
├── TASK.md                → Tareas actuales
├── PRP.md                 → Pattern Recognition Protocol
├── MCP_TOOLS.md           → Herramientas MCP disponibles
│
├── docs/                  → 📁 Documentación Modular Detallada
│   ├── AGENTS.md          → Sistema de agentes orquestados
│   ├── CHECKPOINTS.md     → Checkpoints críticos (ROI 100x/10-20x)
│   ├── WORKFLOWS.md       → Flujos de trabajo y diagramas
│   └── COMMANDS.md        → Comandos disponibles y uso
│
├── agents/                → Agentes especializados
├── commands/              → Comandos personalizados
└── hooks/                 → Hooks de eventos

PRPs/
└── templates/             → Plantillas PRP
```

---

## 🎯 **Misión del Proyecto**

**Crear el mejor template del mundo para generar proyectos de automatización de alta calidad usando Claude Code**, implementando best practices de Context Engineering del equipo BAML.

### **Problema que Resolvemos**

- **Entrada**: Solicitud del usuario en lenguaje natural (ej: "Automatizar procesamiento de facturas PDF")
- **Proceso**: Arquitectura híbrida de dos capas:
  - **@project-initializer** (UX Layer): Experiencia interactiva con checkpoints humanos
  - **Orchestrator SDK** (Engine Layer): Motor Python con análisis estructurado y memoria
  - **TDD obligatorio**: Tests PRIMERO, código después
  - **2 Checkpoints críticos**: Research (ROI 100x) + Planning (ROI 10-20x)
- **Salida**: Proyecto completo con tests (100% coverage), docs, agentes, y capacidad de auto-mejora

### **Estado Actual del Sistema**

**Versión:** 3.1.0 (M0-M6 Complete)
**Progreso:** 100% (6 de 6 milestones completados) ✅

```
[████████████████████████] 100% ✅ PRODUCTION READY

Milestones Completados:
  M0-M2: Setup + SDK + Híbrido    ████████████████████████ (100%) ✅
  M2-IMPROVED: Context Engineering ████████████████████████ (100%) ✅
  M3: Templates Jinja2             ████████████████████████ (100%) ✅
  M4: Versionado Semántico         ████████████████████████ (100%) ✅
  M5: Tests de Integración         ████████████████████████ (100%) ✅
  M6: Documentación Final          ████████████████████████ (100%) ✅

🎉 Sistema completo: Version 3.1.0
```

---

## 🏗️ **Arquitectura del Sistema**

**Arquitectura Híbrida de Dos Capas**:

```
┌────────────────────────────────────────────────────┐
│  CAPA UX: @project-initializer (Claude Code Agent)│
│  ├─ Phase 0: Initialize Orchestrator               │
│  ├─ Phase 1-2: Goal + Research                     │
│  ├─ 🔍 CHECKPOINT 1 (ROI 100x) ← HUMAN             │
│  ├─ Phase 3-7: Planning                            │
│  ├─ 📋 CHECKPOINT 2 (ROI 10-20x) ← HUMAN           │
│  ├─ Phase 8: TDD Implementation                    │
│  ├─ Phase 9: Final Validation                      │
│  └─ Phase 10: Self-Improvement Setup               │
└────────────────────────────────────────────────────┘
                     ↕ (usa internamente)
┌────────────────────────────────────────────────────┐
│  CAPA ENGINE: Orchestrator SDK (Python)            │
│  ├── IntentAnalyzer (Pydantic models)              │
│  ├── MemoryManager (shared .claude/memories/)      │
│  ├── ProjectGenerator                              │
│  ├── SubagentManager (5 specialized agents)        │
│  └── CustomTools (MCP)                             │
└────────────────────────────────────────────────────┘
```

**Flujo con Context Engineering**:

1. Research → 2. ✅ CHECKPOINT 1 → 3. Planning → 4. ✅ CHECKPOINT 2 → 5. TDD → 6. Validation

**📖 Ver detalles**: [.claude/docs/WORKFLOWS.md](.claude/docs/WORKFLOWS.md)

---

## 🔍 **CHECKPOINTS CRÍTICOS**

### **Resumen Ejecutivo**

| Checkpoint   | ROI                   | Tiempo    | Previene                             |
| ------------ | --------------------- | --------- | ------------------------------------ |
| Research (1) | **100x**              | 15-30 min | 1000s líneas mal dirigidas           |
| Planning (2) | **10-20x**            | 20-40 min | 10-100 líneas re-trabajo             |
| **Total**    | **Ahorra 3-10 horas** | 35-70 min | Implementación correcta desde inicio |

### **CHECKPOINT 1: Research Phase (ROI 100x)**

**Agentes involucrados (paralelo)**: @library-researcher, @task-planner, @prp-expert, @prp-validator, @codebase-analyst, Sequential-thinking MCP

**Output**: Documento `/research/research_[feature].md` con findings estructurados, best practices validadas, gotchas conocidos

### **CHECKPOINT 2: Planning Phase (ROI 10-20x)**

**Agentes involucrados**: @task-planner, @documentation-manager, @codebase-analyst, @prp-expert, @prp-validator, @archon-expert

**Output**: Documento `/planning/planning_[feature].md` con plan ejecutable, tareas atómicas, validación por tarea

**📖 Ver detalles completos**: [.claude/docs/CHECKPOINTS.md](.claude/docs/CHECKPOINTS.md)

---

## 🤖 **Sistema de Agentes Orquestados**

**ARQUITECTURA AUTOMÁTICA**: @task-planner se ejecuta automáticamente para tareas complejas. No necesitas invocar agentes manualmente.

### **Agentes Principales**

| Agente                     | Rol                       | Trigger             |
| -------------------------- | ------------------------- | ------------------- |
| **@task-planner**          | 🧠 Coordinador Maestro    | Automático >3 pasos |
| **@task-executor**         | ⚙️ Ejecutor Sistemático   | Por @task-planner   |
| **@prp-expert**            | 📋 Especialista PRPs      | Comandos PRP        |
| **@validation-gates**      | ✅ Validador de Calidad   | Por @task-executor  |
| **@documentation-manager** | 📚 Gestor de Docs         | Por @task-executor  |
| **@library-researcher**    | 📖 Investigador (CRÍTICO) | Por @task-planner   |
| **@codebase-analyst**      | 🔍 Analista de Código     | Por @task-planner   |
| **@prp-validator**         | 🛡️ Validador PRPs         | Automático en PRPs  |

**Principios clave**:

1. **Orquestación Automática** - @task-planner coordina todo
2. **Especialización** - Cada agente tiene UN rol claro
3. **Validación Continua** - @validation-gates después de CADA cambio
4. **Checkpoints Humanos** - NUNCA asume "approve"
5. **Research-First** - Investigar ANTES de implementar
6. **TDD Obligatorio** - Tests PRIMERO, código después

**📖 Ver detalles completos**: [.claude/docs/AGENTS.md](.claude/docs/AGENTS.md)

---

## 📋 **Comandos Principales**

### **Gestión de Proyecto**

```bash
/init-project [objetivo]     # Crear proyecto completo desde cero
/update-context              # Actualizar documentación
/compact-context             # Compactar contexto (automático al 10%)
```

### **Sistema PRP**

```bash
/prp:prp-story-task-create [story]   # Crear PRP desde user story
/prp:prp-story-task-execute [file]   # Ejecutar PRP con validación
/prp-validate [file]                 # Validar PRP standalone
```

### **Validación y Optimización**

```bash
/run-tests                    # Suite completa de tests
/optimize-structure [dir]     # Optimizar estructura de archivos
/optimize-commands            # Optimizar comandos personalizados
```

**📖 Ver guía completa**: [.claude/docs/COMMANDS.md](.claude/docs/COMMANDS.md)

---

## ⚠️ **Recordatorios Críticos**

1. **TDD ES OBLIGATORIO** - Nunca escribir código antes que tests
2. **NO OMITIR CHECKPOINTS** - CHECKPOINT 1 y 2 son críticos (ROI 100x y 10-20x)
3. **WAIT FOR APPROVAL** - No asumir "approve" en checkpoints, esperar respuesta explícita
4. **MEMORY COMPARTIDA** - `.claude/memories/` es compartida entre template y proyectos generados
5. **ORCHESTRATOR CONDICIONAL** - Solo proyectos medium/high complexity necesitan orchestrator/
6. **CONTEXT WINDOW <50%** - Mantener uso de context window bajo 50% para mejor rendimiento
7. **SEQUENTIAL THINKING** - Usar para decisiones arquitectónicas complejas
8. **VALIDATION REPORTS** - Siempre documentar validaciones después de milestones
9. **RESEARCH PHASE ES CRÍTICA (ROI 100x)** - Invertir tiempo en research ahorra 100x tiempo en implementación
10. **PLANNING PHASE ES CRÍTICA (ROI 10-20x)** - Context engineering es REY, planificar archivo por archivo
11. **DOCUMENTAR EN /research/ Y /planning/** - @documentation-manager crea archivos estructurados en estas carpetas

---

## 📋 **Estructura del Proyecto**

```
[nombre-proyecto]/
├── src/                   # Código fuente
│   ├── [modulo1]/
│   ├── [modulo2]/
│   └── shared/           # Código compartido
│
├── tests/                # Tests
│   ├── unit/
│   └── integration/
│
├── docs/                 # Documentación adicional
│
├── .claude/              # Configuración Claude Code
│   ├── docs/             # Documentación modular
│   ├── agents/           # Agentes especializados
│   ├── commands/         # Comandos personalizados
│   └── hooks/            # Hooks de eventos
│
├── requirements.txt      # Dependencias (Python)
├── package.json          # Dependencias (Node.js)
└── README.md
```

---

## 🎨 **Principios de Desarrollo**

### **Core Principles**

1. **Code Quality**
   - Write clean, readable code
   - Follow project conventions
   - Document complex logic
   - Maintain test coverage

2. **Error Handling**
   - Fail fast with clear error messages
   - Use appropriate exception types
   - Log errors with context
   - Never silently ignore failures

3. **Testing**
   - Write tests for new features (TDD)
   - Update tests when refactoring
   - Test edge cases
   - Maintain existing test patterns

### **Code Organization**

- **File Size**: Keep files under 500 lines
- **Modularity**: One responsibility per module
- **Naming**: Use clear, descriptive names
- **Comments**: Explain why, not what

---

## 🐛 **Issues Resueltos y Lecciones Aprendidas**

### **Decisiones Arquitectónicas Resueltas**

1. ✅ **Confusión Orchestrator vs @project-initializer**
   - **Solución**: Arquitectura híbrida - @project-initializer (UX) usa orchestrator (Engine) internamente
   - **Lección**: Sequential thinking ayudó a evaluar opciones sistemáticamente

2. ✅ **Falta de validación en puntos críticos**
   - **Solución**: 2 checkpoints con human validation (ROI 100x y 10-20x)
   - **Lección**: Error Impact Hierarchy del equipo BAML es real y aplicable

3. ✅ **Testing después de código**
   - **Solución**: TDD obligatorio - tests PRIMERO definen comportamiento
   - **Lección**: TDD reduce review humano en 80% y da verificación automática

### **Best Practices Aplicadas (M2-IMPROVED)**

- ✅ **TDD Approach**: Tests primero, código después
- ✅ **Checkpoints**: Human validation en Research y Planning
- ✅ **Context window**: Target <50% capacity
- ✅ **High-leverage reviews**: Focus en research/planning, no código
- ✅ **Memory compartida**: .claude/memories/ entre template y proyectos
- ✅ **Pydantic models**: Validación estructurada de datos
- ✅ **Sequential thinking**: Para decisiones arquitectónicas complejas
- ✅ **Serena MCP**: Para análisis profundo de código
- ✅ **Documentación validada**: Todos los cambios con validation reports

---

## 📝 **Notas de Desarrollo**

### **Decisiones Técnicas (M2-IMPROVED)**

- **Arquitectura Híbrida**: Combinar @project-initializer + Orchestrator SDK
- **TDD Obligatorio**: Tests PRIMERO, código después (reduce review 80%)
- **2 Checkpoints**: Research (ROI 100x) + Planning (ROI 10-20x)
- **Pydantic Models**: AutomationIntent, ProjectStructure, etc.
- **Memoria Compartida**: `.claude/memories/` sincronizada
- **Orchestrator Condicional**: Solo proyectos medium/high
- **Context Window Target**: <50% capacity
- **Sequential Thinking**: Para decisiones arquitectónicas complejas

### **Patrones Implementados**

- **5-Step TDD Loop**: Failing test → Setup → Implement → Passing test → Confirm
- **Checkpoint Pattern**: Present summary → Ask critical questions → approve/fix/restart
- **Error Impact Hierarchy**: Research (1000 lines) > Plan (10-100) > Code (1)
- **Phase-based Workflow**: 11 phases (0-10) desde goal understanding hasta self-improvement
- **Memory Learning Loop**: store_architectural_decision() + store_pattern()
- **Hybrid Analysis**: orchestrator.analyze_intent() + parallel agents
- **Complexity-based Features**: if complexity=medium/high → include orchestrator/

---

## 📚 **Documentación Detallada**

Para información detallada sobre cada aspecto del sistema, consulta los documentos modulares:

- **[AGENTS.md](.claude/docs/AGENTS.md)** - Sistema completo de agentes orquestados
- **[CHECKPOINTS.md](.claude/docs/CHECKPOINTS.md)** - Checkpoints críticos detallados
- **[WORKFLOWS.md](.claude/docs/WORKFLOWS.md)** - Flujos de trabajo y diagramas
- **[COMMANDS.md](.claude/docs/COMMANDS.md)** - Guía completa de comandos

---

_Última actualización: 2025-01-07_
_Versión: 3.1.0 (M0-M6 Complete - Production Ready)_
_Estado: ✅ Sistema Completo - All Milestones Completed_
_Mantenedor: IA Corp - Claude Code Template Team_
_Optimización: CLAUDE.md modularizado (73k → ~17k chars)_
