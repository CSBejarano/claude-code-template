# Comandos Disponibles

## Gestión de Proyecto

### `/update-context`

Actualiza contexto y documentación del proyecto

```bash
/update-context
```

**Lo que hace**:

- Analiza y optimiza CLAUDE.md, README.md, PLANNING.md y todos los .md
- Usa agentes especializados para generar documentación completa
- RECOMENDADO: Ejecutar al inicio del proyecto y periódicamente

**Agentes involucrados**:

- @documentation-manager (principal)
- @codebase-analyst (análisis)
- @task-planner (coordinación)

---

### `/init-project`

Inicializa nuevo proyecto interactivamente

```bash
/init-project [objetivo-opcional]
```

**Lo que hace**:

- Crea proyecto desde cero con orquestación de agentes
- Setup paso a paso de APIs, tests, y documentación
- Genera agentes personalizados para el proyecto

**Fases (11 total)**:

```
Phase 0: Initialize Orchestrator
Phase 1: Goal Understanding
Phase 2: Research (con @library-researcher)
→ CHECKPOINT 1 (ROI 100x)
Phase 3-7: Planning (arquitectura, estructura, dependencies)
→ CHECKPOINT 2 (ROI 10-20x)
Phase 8: TDD Implementation
Phase 9: Validation
Phase 10: Self-Improvement Setup
```

**Agentes involucrados**:

- @project-initializer (principal)
- @library-researcher (research)
- @task-planner (coordinación)
- @validation-gates (validación)
- @documentation-manager (docs)

---

### `/compact-context`

Compactación automática de contexto del chat

```bash
/compact-context
```

**Lo que hace**:

- Se ejecuta AUTOMÁTICAMENTE cuando contexto llega a 10%
- Crea/actualiza `.claude/CONTINUE_SESSION.md`
- Preserva checkpoints, decisiones, código modificado
- Sincroniza con Archon MCP

**Agente involucrado**:

- @documentation-manager (automático)

---

## Sistema PRP (Pattern Recognition Protocol)

### `/prp:prp-story-task-create`

Convierte user story en PRP ejecutable

```bash
/prp:prp-story-task-create "Historia de usuario completa"
```

**Ejemplo**:

```bash
/prp:prp-story-task-create "Agregar endpoint GET /orders con filtros de fecha, estado y paginación"
```

**Lo que hace**:

1. **Descomposición de historia**: Analiza y clasifica en tipo, complejidad, sistemas afectados
2. **Recopilación de inteligencia** (paralelo):
   - Invoca @codebase-analyst → Extrae patrones
   - Invoca @library-researcher → Investiga best practices
3. **Deep thinking**: Sequential Thinking MCP (8-12 thoughts)
4. **Generación de tareas atómicas**: Verbos de acción (CREATE, UPDATE, ADD)
5. **Diseño de validación**: Comandos de validación por tarea
6. **Documentación**: Guarda en `PRPs/story_*.md`

**Output**: `PRPs/story_[nombre].md`

**Agentes involucrados**:

- @prp-expert (principal)
- @codebase-analyst (paralelo)
- @library-researcher (paralelo)

---

### `/prp:prp-story-task-execute`

Ejecuta PRP con validación multinivel

```bash
/prp:prp-story-task-execute PRPs/story_archivo.md
```

**Ejemplo**:

```bash
/prp:prp-story-task-execute PRPs/story_orders_endpoint.md
```

**Lo que hace**:

1. **Pre-validación automática**: @prp-validator valida PRP (score ≥ 80)
2. **Carga y análisis**: Lee PRP completo, entiende intent
3. **Pre-verificación**: Valida archivos, patrones, entorno
4. **Ejecución task-by-task**:
   - Implementa tarea actual
   - @validation-gates valida inmediatamente
   - Solo avanza si PASS
5. **Validación multinivel**: Sintaxis → Unit → Integration → Domain
6. **Finalización**: Mueve a `PRPs/completed/`

**Agentes involucrados**:

- @prp-expert (principal)
- @prp-validator (pre-check obligatorio)
- @validation-gates (cada tarea)
- @documentation-manager (finalización)

---

### `/prp-validate`

Valida PRP sin ejecutarlo

```bash
/prp-validate PRPs/archivo.md
```

**Lo que hace**:

- Valida estructura del PRP (score 0-100)
- Verifica referencias externas e internas
- Chequea lógica específica vs vaguedades
- Valida steps accionables con file paths
- Si score < 80: auto-mejora (max 3 iterations)

**Output**:

- Score final (0-100)
- PASS (ejecutable) o NEEDS REVIEW
- Sugerencias de mejora

**Agente involucrado**:

- @prp-validator (standalone)

---

## Validación y Testing

### `/run-tests`

Ejecuta suite completa de tests

```bash
/run-tests
```

**Lo que hace**:

- Ejecuta unit tests
- Ejecuta integration tests
- Corre linting y formatting
- Verifica type checking
- Valida build sin warnings
- ITERA hasta que TODO pase

**Agente involucrado**:

- @validation-gates

---

## Optimización

### `/optimize-structure`

Optimiza estructura de archivos

```bash
/optimize-structure [directorio-opcional]
```

**Ejemplo**:

```bash
/optimize-structure src/services/
```

**Lo que hace**:

1. Analiza estructura actual
2. Identifica archivos grandes (>500 líneas)
3. Propone refactorización modular
4. Ejecuta refactoring con validación continua
5. Actualiza imports automáticamente

**Agente involucrado**:

- @file-optimizer

---

### `/optimize-commands`

Optimiza comandos personalizados

```bash
/optimize-commands
```

**Lo que hace**:

1. Analiza comandos existentes en `.claude/commands/`
2. Identifica comandos redundantes
3. Propone nuevos comandos basados en patrones
4. Genera archivos de comandos con sintaxis correcta
5. Asigna comandos a agentes automáticamente

**Agente involucrado**:

- @command-optimizer

**Nota**: Este comando también se ejecuta AUTOMÁTICAMENTE cuando @task-planner lo invoca al inicio de planning phase.

---

## Flujo de Trabajo Recomendado

### 1. Al Iniciar Proyecto Nuevo (primera vez)

```bash
/init-project "mi objetivo"
```

**Internamente ejecuta**:

- Fase 0: Sequential thinking sobre objetivo
- Fase 0.5: Análisis y creación de agentes
- Fase 0.7: Generación de docs base (/update-context modo nuevo)
- Fases 1-8: Implementación guiada por docs
- Fase 9: Actualización final de docs con realidad

---

### 2. Durante Desarrollo (agregar features)

**Opción A - PRP Técnico**:

```bash
/prp:prp-story-task-create "Nueva feature específica"
/prp:prp-story-task-execute PRPs/story_feature.md
```

**Opción B - Tarea Compleja** (sin PRP directo):

```
Usuario: "Implementar OAuth2 completo con JWT"
→ @task-planner se ejecuta AUTOMÁTICAMENTE
→ Genera plan con checkpoints
→ Coordina agentes especializados
```

---

### 3. Mantenimiento (cada 2-3 semanas)

```bash
/update-context          # Actualiza docs analizando código real
/optimize-structure      # Opcional: si archivos >400 líneas
```

---

## ⚠️ Importante

**NO ejecutes `/update-context` antes de `/init-project`**.

El comando `/init-project` genera automáticamente la documentación base optimizada en su Fase 0.7.

Solo usa `/update-context` standalone para mantenimiento de proyectos existentes.

---

## Ejemplos Completos

### Ejemplo 1: Feature Nueva con PRP

```bash
# Paso 1: Crear PRP
/prp:prp-story-task-create "Agregar sistema de notificaciones push con Firebase y rate limiting"

→ Output: PRPs/story_push_notifications.md

# Paso 2: Revisar PRP generado (manual)
# Paso 3: Ejecutar PRP
/prp:prp-story-task-execute PRPs/story_push_notifications.md

→ @prp-validator valida (score ≥ 80)
→ @prp-expert ejecuta task-by-task
→ @validation-gates valida cada paso
→ @documentation-manager actualiza docs
→ ✅ Feature completo
```

---

### Ejemplo 2: Bug Fix Urgente

```bash
# No usar PRP para bugs simples - dejar que @task-planner orqueste
Usuario: "Arreglar error de autenticación en endpoint POST /login"

→ Claude Code detecta: tarea simple (1-2 archivos)
→ Implementación directa sin PRP
→ @validation-gates valida automáticamente
→ ✅ Bug fix completo
```

---

### Ejemplo 3: Refactorización

```bash
# Paso 1: Optimizar estructura si archivos >400 líneas
/optimize-structure src/services/

→ @file-optimizer analiza
→ Propone split modular
→ Ejecuta refactoring
→ @validation-gates valida

# Paso 2: Actualizar documentación
/update-context

→ @documentation-manager sincroniza docs con código real
```

---

## Comandos Automáticos (No Invocar Directamente)

Estos comandos se ejecutan AUTOMÁTICAMENTE por el sistema:

- **@task-planner** - Se ejecuta automáticamente para tareas complejas
- **@validation-gates** - Se ejecuta después de cada implementación
- **@documentation-manager** - Se ejecuta al 10% de contexto usado
- **@command-optimizer** - Se ejecuta durante planning phase

**No necesitas invocarlos manualmente** - el sistema los orquesta.
