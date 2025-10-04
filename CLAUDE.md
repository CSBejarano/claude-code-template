# CLAUDE.md - Claude Code Template (Orchestrator Agent SDK)

> **Documento maestro del proyecto** - Template para generar proyectos de automatización con arquitectura híbrida, TDD approach y checkpoints de validación humana

**⚠️ NOTA**: Este es un template que genera proyectos. Los proyectos generados tendrán su propio CLAUDE.md personalizado.

This file provides guidance to Claude Code (claude.ai/code) when working with the template repository itself.

---

## 📚 **Sistema de Documentación**

```
🚀 QUICK_START.md          → Inicio rápido (10 min)
📖 CLAUDE.md (ESTÁS AQUÍ)  → Documentación completa
📋 README.md               → Documentación principal del proyecto

.claude/
├── PLANNING.md            → Arquitectura y planificación
├── TASK.md                → Tareas actuales
├── PRP.md                 → Pattern Recognition Protocol
├── MCP_TOOLS.md           → Herramientas MCP disponibles
│
├── agents/                → Agentes especializados
│   ├── codebase-analyst.md
│   └── library-researcher.md
│
├── commands/              → Comandos personalizados
│   └── prp/               → Sistema PRP
│
└── hooks/                 → Hooks de eventos

PRPs/
└── templates/             → Plantillas PRP
    └── prp_story_task.md

docs/                      → Documentación adicional
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

**Progreso por Milestones:**
- [x] M0: Setup Inicial - ✅ COMPLETADO
- [x] M1: Orchestrator SDK base - ✅ COMPLETADO
- [x] M2: Integración con @project-initializer - ✅ COMPLETADO
- [x] M2-IMPROVED: Context Engineering (TDD + Checkpoints) - ✅ COMPLETADO (2025-01-03)
  - [x] TDD Approach implementado en Phase 8
  - [x] CHECKPOINT 1 después de Research (ROI 100x)
  - [x] CHECKPOINT 2 después de Planning (ROI 10-20x)
  - [x] Key Principles actualizados
  - [x] Validación 100% (4/4 tests PASS)
- [x] M3: Templates Jinja2 para proyectos generados - ✅ COMPLETADO (2025-01-03)
  - [x] 11 templates creados (base + medium + high)
  - [x] Sistema de renderizado con 26+ variables
  - [x] Validación real: 10/10 checks PASS
  - [x] Documentación: TEMPLATES.md (515 líneas)
- [x] M4: Sistema de versionado del orchestrator - ✅ COMPLETADO (2025-01-03)
  - [x] Dual versioning: Template v3.0.0 + SDK v1.0.0
  - [x] CHANGELOG.md (180 líneas)
  - [x] MIGRATIONS.md (220 líneas)
  - [x] orchestrator/README.md (340 líneas)
  - [x] Test suite: 18/18 tests PASS
- [x] M5: Tests de integración híbrida - ✅ COMPLETADO (2025-01-03)
  - [x] E2E tests: 6 tests (100% PASS)
  - [x] Checkpoints tests: 14 tests (100% PASS)
  - [x] Hybrid architecture tests: 14 tests (100% PASS)
  - [x] TDD loop tests: 11 tests (100% PASS)
  - [x] Total: 81/81 tests passing (100%)
  - [x] Documentación: VALIDATION_M5.md (443 líneas)
- [x] M6: Documentación final del sistema - ✅ COMPLETADO (2025-01-03)
  - [x] QUICK_START.md (582 líneas)
  - [x] USER_GUIDE.md (1,070 líneas + 5 diagrams)
  - [x] TROUBLESHOOTING.md (680 líneas, 30 errores)
  - [x] BEST_PRACTICES.md (585 líneas)
  - [x] CONTRIBUTING.md (420 líneas)
  - [x] Context Window Metrics (470 líneas en PLANNING.md)
  - [x] 5 Mermaid Diagrams
  - [x] Quality Score: 9.9/10
  - [x] Documentación: VALIDATION_M6.md (410 líneas)

---

## 🏗️ **Arquitectura del Sistema**

**Arquitectura Híbrida de Dos Capas** (decidida en M2 después de análisis con sequential-thinking):

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

**Decisión de Arquitectura (M2)**:
- Opción A (solo orchestrator) - rechazada: perdería UX interactiva
- Opción B (solo @project-initializer) - rechazada: perdería análisis estructurado
- **Opción HÍBRIDA (elegida)**: Combina lo mejor de ambos mundos

**Flujo con Context Engineering**:
1. Research → 2. ✅ CHECKPOINT 1 → 3. Planning → 4. ✅ CHECKPOINT 2 → 5. TDD → 6. Validation

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
├── requirements.txt      # Dependencias (Python)
├── package.json          # Dependencias (Node.js)
└── README.md
```

---

## 🛠️ **Comandos de Desarrollo**

### **Configuración Inicial**
```bash
# Clonar repositorio
git clone [repo-url]
cd [nombre-proyecto]

# [Instrucciones de setup específicas del proyecto]
```

### **Comandos Principales**
```bash
# Desarrollo
[comando-dev]

# Testing
[comando-test]

# Build
[comando-build]

# Linting
[comando-lint]
```

---

## 🔧 **Variables de Entorno Requeridas**

```bash
# APIs Externas
[API_KEY_1]=[descripción]
[API_KEY_2]=[descripción]

# Base de Datos
[DB_CONNECTION]=[descripción]

# Configuración
[CONFIG_VAR]=[descripción]
```

---

## 🎯 **Métricas de Performance**

| Métrica | Objetivo | Actual | Estado |
|---------|----------|--------|--------|
| [Métrica 1] | [valor] | [valor] | [estado] |
| [Métrica 2] | [valor] | [valor] | [estado] |

---

## 📊 **Progreso del Sistema**

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

## 🐛 **Issues Resueltos y Lecciones Aprendidas**

### **Decisiones Arquitectónicas Resueltas**
1. ✅ **Confusión Orchestrator vs @project-initializer**
   - **Problema**: Dos sistemas parecían hacer lo mismo, no estaba claro cuál usar
   - **Solución**: Arquitectura híbrida - @project-initializer (UX) usa orchestrator (Engine) internamente
   - **Lección**: Sequential thinking ayudó a evaluar opciones sistemáticamente

2. ✅ **Falta de validación en puntos críticos**
   - **Problema**: Errores en research/planning resultaban en 1000s de líneas malas
   - **Solución**: 2 checkpoints con human validation (ROI 100x y 10-20x)
   - **Lección**: Error Impact Hierarchy del equipo BAML es real y aplicable

3. ✅ **Testing después de código (Validation approach)**
   - **Problema**: Tests al final no prevenían errores, solo los detectaban tarde
   - **Solución**: TDD obligatorio - tests PRIMERO definen comportamiento
   - **Lección**: TDD reduce review humano en 80% y da verificación automática

### **Best Practices Aplicadas (M2-IMPROVED)**
- ✅ **TDD Approach**: Tests primero, código después (BAML team)
- ✅ **Checkpoints**: Human validation en Research y Planning
- ✅ **Context window**: Target <50% capacity
- ✅ **High-leverage reviews**: Focus en research/planning, no código
- ✅ **Memory compartida**: .claude/memories/ entre template y proyectos
- ✅ **Pydantic models**: Validación estructurada de datos
- ✅ **Sequential thinking**: Para decisiones arquitectónicas complejas
- ✅ **Serena MCP**: Para análisis profundo de código
- ✅ **Documentación validada**: Todos los cambios con validation reports

---

## ⚠️ **Recordatorios Críticos**

1. **TDD ES OBLIGATORIO** - Nunca escribir código antes que tests
2. **NO OMITIR CHECKPOINTS** - CHECKPOINT 1 y 2 son críticos (ROI 100x y 10-20x)
3. **WAIT FOR APPROVAL** - No asumir "approve" en checkpoints, esperar respuesta explícita
4. **MEMORY COMPARTIDA** - `.claude/memories/` es compartida entre template y proyectos generados
5. **ORCHESTRATOR CONDICIONAL** - Solo proyectos medium/high complexity necesitan orchestrator/
6. **CONTEXT WINDOW <50%** - Mantener uso de context window bajo 50% para mejor rendimiento
7. **SEQUENTIAL THINKING** - Usar para decisiones arquitectónicas complejas (como M2 arquitectura)
8. **VALIDATION REPORTS** - Siempre documentar validaciones después de milestones

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
   - Write tests for new features
   - Update tests when refactoring
   - Test edge cases
   - Maintain existing test patterns

### **Code Organization**

- **File Size**: Keep files under 500 lines
- **Modularity**: One responsibility per module
- **Naming**: Use clear, descriptive names
- **Comments**: Explain why, not what

### **Development Workflow**

```bash
# 1. Start development
[dev-command]

# 2. Make changes
# - Write code
# - Add tests
# - Update docs

# 3. Validate changes
[lint-command]
[test-command]
[typecheck-command]

# 4. Commit
git add .
git commit -m "feat: descriptive message"

# 5. Test integration
[integration-test-command]
```

---

## 🤖 **Agentes y Comandos Claude Code**

### **Agentes Disponibles**

#### **`@codebase-analyst`**
Specialized agent for deep codebase pattern analysis and convention discovery.

**When to use:**
- Before implementing new features
- To understand existing patterns
- To find similar implementations
- To extract coding conventions

**Example usage:**
```bash
"@codebase-analyst encuentra cómo se manejan errores en [módulo]"
"@codebase-analyst busca patrones de autenticación en el proyecto"
"@codebase-analyst identifica la estructura de archivos de pruebas"
```

**What it provides:**
- Project structure analysis
- Naming conventions
- Integration patterns
- Similar implementations
- Validation commands

#### **`@library-researcher`**
Specialized agent for researching external libraries and documentation.

**When to use:**
- Before adding new dependencies
- To understand library usage patterns
- To find best practices
- To troubleshoot integration issues

**Example usage:**
```bash
"@library-researcher busca documentación de [librería]"
"@library-researcher investiga cómo integrar [librería] con [framework]"
"@library-researcher encuentra ejemplos de uso de [característica] en [librería]"
```

**What it provides:**
- Official documentation links
- Implementation examples
- Integration patterns
- Known gotchas
- Best practices

### **Comandos Disponibles**

#### **Gestión de Proyecto**

```bash
# Actualizar contexto y documentación del proyecto
/update-context
# Analiza y optimiza CLAUDE.md, README.md, PLANNING.md y todos los .md
# Usa agentes especializados para generar documentación completa
# RECOMENDADO: Ejecutar al inicio del proyecto y periódicamente

# Inicializar nuevo proyecto interactivamente
/init-project [objetivo-opcional]
# Crea proyecto desde cero con orquestación de agentes
# Setup paso a paso de APIs, tests, y documentación
# Genera agentes personalizados para el proyecto
```

#### **Sistema PRP (Pattern Recognition Protocol)**

```bash
# Crear PRP técnico
/prp-create [nombre-funcionalidad]
# Creates a technical implementation plan with codebase analysis

# Ejecutar PRP
/prp-execute PRPs/archivo.md
# Executes an existing PRP with systematic implementation

# Crear Story PRP
/story-create "historia de usuario"
# Converts user story into executable PRP with deep analysis

# Ejecutar Story PRP
/story-execute PRPs/story_archivo.md
# Executes story-based PRP with validation loops
```

#### **Flujo de Trabajo Recomendado**

```bash
# 1. Al iniciar proyecto nuevo (primera vez)
/init-project "mi objetivo"
# Internamente ejecuta:
#   - Fase 0: Sequential thinking sobre objetivo
#   - Fase 0.5: Análisis y creación de agentes
#   - Fase 0.7: Generación de docs base (/update-context modo nuevo)
#   - Fases 1-8: Implementación guiada por docs
#   - Fase 9: Actualización final de docs con realidad

# 2. Durante desarrollo (agregar features)
/prp-create nueva-feature    # Planifica implementación
/story-create "user story"   # O desde user story

# 3. Mantenimiento (cada 2-3 semanas o después de cambios mayores)
/update-context          # Actualiza docs analizando código real
```

**⚠️ Importante**: NO ejecutes `/update-context` antes de `/init-project`.
El comando `/init-project` genera automáticamente la documentación base optimizada en su Fase 0.7.
Solo usa `/update-context` standalone para mantenimiento de proyectos existentes.

### **Flujo de Trabajo con Agentes**

```mermaid
graph TD
    A[New Feature Request] --> B[@codebase-analyst]
    B --> C[Analyze Patterns]
    C --> D[@library-researcher]
    D --> E[Research Libraries]
    E --> F[/story-create]
    F --> G[Create PRP]
    G --> H[/story-execute]
    H --> I[Implement & Validate]
    I --> J[✅ Feature Complete]
```

---

## 📝 **Notas de Desarrollo**

### **Decisiones Técnicas (M2-IMPROVED)**
- **Arquitectura Híbrida**: Combinar @project-initializer + Orchestrator SDK (mejor que usar solo uno)
- **TDD Obligatorio**: Tests PRIMERO, código después (reduce review 80%, da verificación automática)
- **2 Checkpoints**: Research (ROI 100x) + Planning (ROI 10-20x) atrapan errores temprano
- **Pydantic Models**: AutomationIntent, ProjectStructure, etc. para validación estructurada
- **Memoria Compartida**: `.claude/memories/` sincronizada entre template y proyectos generados
- **Orchestrator Condicional**: Solo proyectos medium/high get orchestrator/ y @self-improve
- **Context Window Target**: <50% capacity para mejor rendimiento del LLM
- **Sequential Thinking**: Para decisiones arquitectónicas complejas (16 thoughts para decidir arquitectura)

### **Patrones Implementados (M2-IMPROVED)**
- **5-Step TDD Loop**: Failing test → Setup → Implement → Passing test → Confirm
- **Checkpoint Pattern**: Present summary → Ask critical questions → approve/fix/restart
- **Error Impact Hierarchy**: Research (1000 lines) > Plan (10-100) > Code (1)
- **Phase-based Workflow**: 11 phases (0-10) desde goal understanding hasta self-improvement
- **Memory Learning Loop**: store_architectural_decision() + store_pattern() + get_memory_context()
- **Hybrid Analysis**: orchestrator.analyze_intent() + parallel agents (sequential-thinking, library-researcher)
- **Complexity-based Features**: if complexity=medium/high → include orchestrator/ + @self-improve

---

*Última actualización: 2025-01-04*
*Versión: 3.1.0 (M0-M6 Complete - Production Ready)*
*Estado: ✅ Sistema Completo - All Milestones Completed*
*Mantenedor: IA Corp - Claude Code Template Team*
*M6 Final*: Documentation Complete (~4,500 lines) + Quality Score 9.9/10*
