# Guía General: Personalizar Claude Code Template

Esta guía muestra cómo personalizar la plantilla de Claude Code para cualquier tipo de proyecto.

## 📋 Archivos Clave de Configuración

### 1. CLAUDE.md - Contexto del Proyecto

`CLAUDE.md` es el archivo más importante. Claude lo lee para entender tu proyecto.

**Ubicación**: `/CLAUDE.md` (raíz del proyecto)

**Estructura recomendada**:

```markdown
# [Nombre del Proyecto]

## 🎯 Misión del Proyecto

**Descripción clara del objetivo principal**

### Problema que Resolvemos
- **Entrada**: [Qué recibe el sistema]
- **Proceso**: [Cómo procesa]
- **Salida**: [Qué genera]

### Estado Actual
- [ ] Fase 1: [Descripción] - Estado actual
- [ ] Fase 2: [Descripción] - Estado actual

## 🏗️ Arquitectura del Sistema

**Stack Tecnológico**:
- **Lenguaje**: [Python 3.12, Node.js 20, etc.]
- **Framework**: [FastAPI, Express, etc.]
- **Base de Datos**: [PostgreSQL, MongoDB, etc.]
- **Testing**: [pytest, Jest, etc.]

**Componentes principales**:
- `src/api/`: [Descripción]
- `src/services/`: [Descripción]
- `src/models/`: [Descripción]

## 📋 Estructura del Proyecto

\`\`\`
proyecto/
├── src/
├── tests/
├── docs/
└── .claude/
\`\`\`

## 🛠️ Comandos de Desarrollo

\`\`\`bash
# Desarrollo
[comando-dev]

# Testing
[comando-test]

# Build
[comando-build]
\`\`\`

## 🔧 Variables de Entorno

\`\`\`bash
API_KEY=[descripción]
DATABASE_URL=[descripción]
\`\`\`

## 🎯 Métricas de Performance

| Métrica | Objetivo | Actual | Estado |
|---------|----------|--------|--------|
| [Métrica 1] | [valor] | [valor] | ✅/⚠️ |

## 🐛 Issues Resueltos

1. ✅ **[Bug 1]**
   - **Problema**: [descripción]
   - **Solución**: [solución]
   - **Lección**: [lección aprendida]

## ⚠️ Recordatorios Críticos

1. **[Regla crítica 1]**
2. **[Regla crítica 2]**
```

**Consejos**:
- ✅ Sé específico sobre tu stack tecnológico
- ✅ Documenta decisiones técnicas importantes
- ✅ Actualiza cuando cambies arquitectura
- ✅ Incluye ejemplos de comandos reales
- ❌ No copies plantillas genéricas sin personalizar

### 2. .claude/PLANNING.md - Arquitectura y Planificación

**Ubicación**: `/.claude/PLANNING.md`

**Qué incluir**:

```markdown
# Planning - [Nombre del Proyecto]

## 🎯 Objetivos del Proyecto

### Objetivo Principal
[Descripción del objetivo]

### Objetivos Secundarios
1. [Objetivo 1]
2. [Objetivo 2]

## 📐 Diseño de Arquitectura

### Componentes Principales

#### Componente 1: [Nombre]
**Responsabilidad**: [Qué hace]
**Tecnología**: [Stack usado]
**Dependencias**: [De qué depende]

## 🔄 Flujo de Datos

\`\`\`
Input → Validación → Procesamiento → Storage → Output
\`\`\`

## 🗂️ Estructura de Datos

### Modelo Principal
\`\`\`typescript
interface User {
  id: number;
  name: string;
  email: string;
}
\`\`\`

## 🚀 Roadmap

### Fase 1: MVP (Semana 1-2)
- [ ] Feature 1
- [ ] Feature 2

### Fase 2: Mejoras (Semana 3-4)
- [ ] Feature 3
- [ ] Feature 4

## 🎨 Convenciones de Código

- **Naming**: [Convención]
- **Testing**: [Cobertura mínima]
- **Documentation**: [Estándar]
```

### 3. .claude/TASK.md - Seguimiento de Tareas

**Ubicación**: `/.claude/TASK.md`

**Qué incluir**:

```markdown
# TASK.md - [Nombre del Proyecto]

## 📅 Estado del Proyecto - [Fecha]

**Progreso Actual: XX% Completo**

**Resumen:**
- ✅ **Completadas**: [N] tareas
- 🔄 **En Progreso**: [N] tareas
- 📋 **Pendientes**: [N] tareas

## ✅ FASE 1: [Nombre] - COMPLETADA

### Estado
[Descripción del resultado]

**Implementación:**
- [x] Tarea 1
- [x] Tarea 2

**Archivos afectados:**
- `src/archivo1.ext`
- `src/archivo2.ext`

## 🔄 FASE 2: [Nombre] - EN PROGRESO

### Tareas Pendientes
- [ ] Tarea 1
- [ ] Tarea 2

### Bloqueadores
- ⚠️ [Bloqueador 1]: [Descripción]

### Próximos Pasos
1. [Paso 1]
2. [Paso 2]

## 📋 FASE 3: [Nombre] - PENDIENTE

### Descripción
[Qué se necesita hacer]

### Prerrequisitos
- Depende de: [Fase anterior]

## 📊 Progreso General

\`\`\`
[████████████░░░░░░░░] 60%
  Fase 1: ████████████████████ (100%) ✅
  Fase 2: ████████████░░░░░░░░ (60%)  🔄
  Fase 3: ░░░░░░░░░░░░░░░░░░░░ (0%)   📋
\`\`\`
```

## 🤖 Crear Agentes Personalizados

### Anatomía de un Agente

**Ubicación**: `/.claude/agents/mi-agente.md`

**Estructura**:

```markdown
---
name: "mi-agente"
description: "Descripción corta de cuándo usar este agente"
model: "sonnet"
---

Eres un agente especializado en [tarea específica].

## Tu Misión

[Descripción detallada de la responsabilidad del agente]

## Proceso de Trabajo

### Step 1: [Nombre del paso]
[Descripción de qué hace en este paso]

**Herramientas a usar**:
- `tool_name`: [Para qué]

### Step 2: [Nombre del paso]
[Descripción]

## Patrones de Uso

### Caso de Uso 1: [Nombre]
\`\`\`
[Ejemplo de uso]
\`\`\`

### Caso de Uso 2: [Nombre]
\`\`\`
[Ejemplo de uso]
\`\`\`

## Output Format

[Formato esperado del output del agente]

## Mejores Prácticas

- ✅ DO: [Práctica recomendada]
- ❌ DON'T: [Práctica a evitar]
```

### Ejemplos de Agentes Útiles

#### 1. Code Reviewer
```markdown
---
name: "code-reviewer"
description: "Reviews code changes for best practices and potential issues"
model: "sonnet"
---

You are a senior code reviewer focused on quality and maintainability.

## Review Checklist

- Code follows project conventions (see CLAUDE.md)
- Tests cover new functionality
- No security vulnerabilities
- Performance considerations addressed
- Documentation updated
```

#### 2. API Designer
```markdown
---
name: "api-designer"
description: "Designs REST API endpoints following best practices"
model: "sonnet"
---

You design REST APIs following OpenAPI specifications.

## Design Process

1. Understand the resource
2. Design CRUD operations
3. Define request/response schemas
4. Add validation rules
5. Document endpoints
```

#### 3. Test Generator
```markdown
---
name: "test-generator"
description: "Generates comprehensive test cases for code"
model: "sonnet"
---

You generate test cases covering:
- Happy path
- Edge cases
- Error scenarios
- Integration tests
```

## 📜 Crear Comandos Personalizados

### Anatomía de un Comando

**Ubicación**: `/.claude/commands/mi-comando.md`

**Estructura**:

```markdown
# Command: mi-comando

Descripción breve del comando

## Usage

\`\`\`
/mi-comando [args]
\`\`\`

## Arguments

- `[arg1]`: Descripción del argumento
- `[arg2]`: Descripción del argumento (opcional)

## What This Command Does

1. **Step 1**: [Descripción]
2. **Step 2**: [Descripción]
3. **Step 3**: [Descripción]

## Example Usage

\`\`\`
/mi-comando valor1 valor2
\`\`\`

**Output**:
\`\`\`
[Ejemplo de output]
\`\`\`

## Implementation

When this command is invoked:

\`\`\`python
async def mi_comando(arg1, arg2=None):
    # 1. Validar args
    # 2. Ejecutar lógica
    # 3. Retornar resultado
    return result
\`\`\`

## Related Commands

- `/otro-comando` - [Descripción]

## Notes

- [Nota importante 1]
- [Nota importante 2]
```

### Ejemplos de Comandos Útiles

#### 1. Deploy Command
```markdown
# Command: deploy

Deploys the application to specified environment

## Usage
\`\`\`
/deploy [environment]
\`\`\`

## Arguments
- `[environment]`: production, staging, or dev (default: staging)

## What This Command Does
1. Run tests
2. Build application
3. Push to container registry
4. Update deployment
5. Verify deployment
```

#### 2. Generate Documentation
```markdown
# Command: gen-docs

Generates API documentation from code

## Usage
\`\`\`
/gen-docs [format]
\`\`\`

## Arguments
- `[format]`: openapi, markdown, or html (default: openapi)

## What This Command Does
1. Scan API routes
2. Extract schemas
3. Generate documentation
4. Save to docs/api/
```

## 📐 Usar PRPs (Pattern Recognition Protocols)

### ¿Qué es un PRP?

Un PRP es un documento de planificación detallada para implementar features complejos.

### Crear un PRP

**Ubicación**: `/PRPs/nombre-feature.md`

**Usar comando**:
```bash
/prp-create nombre-feature
```

**Estructura del PRP**:

```markdown
# PRP: [Nombre del Feature]

**Fecha**: [YYYY-MM-DD]
**Tipo**: [Feature/Refactor/Bug Fix]
**Complejidad**: [Alta/Media/Baja]

## 🎯 Objetivo

**Meta**: [Qué se quiere lograr]

**Entregable**: [Qué se va a crear]

**Definición de Éxito**:
- [Criterio 1]
- [Criterio 2]

## 👤 Persona de Usuario

**Usuario**: [Quién lo usa]
**Caso de Uso**: [Cómo lo usa]
**Pain Point**: [Qué problema resuelve]

## 🔍 Contexto Necesario

### Archivos Relevantes
- `src/archivo1.ts`: [Por qué es relevante]
- `src/archivo2.ts`: [Por qué es relevante]

### Árbol Actual
\`\`\`
proyecto/
├── src/
│   └── existing/
\`\`\`

### Árbol Deseado
\`\`\`
proyecto/
├── src/
│   ├── existing/
│   └── new-feature/
\`\`\`

## 📐 Modelos y Estructura de Datos

\`\`\`typescript
interface NewFeature {
  id: string;
  name: string;
  config: FeatureConfig;
}
\`\`\`

## 🔧 Tareas de Implementación

### TAREA 1: CREATE src/new-feature/index.ts

**CONTENIDO**:
\`\`\`typescript
[Código específico]
\`\`\`

**VALIDAR**:
\`\`\`bash
test -f src/new-feature/index.ts && echo "✅"
\`\`\`

### TAREA 2: UPDATE src/main.ts

**MODIFICAR**: Agregar import de new-feature

**VALIDAR**:
\`\`\`bash
grep -q "new-feature" src/main.ts && echo "✅"
\`\`\`

## ✅ Checklist Final

- [ ] Todos los archivos creados
- [ ] Tests pasando
- [ ] Documentación actualizada
- [ ] Sin errores de linting
```

### Ejecutar un PRP

```bash
# Ejecutar PRP
/prp-execute PRPs/nombre-feature.md

# O para PRPs de story
/story-execute PRPs/story-nombre.md
```

## 🎯 Flujo de Trabajo Completo

### 1. Inicio de Proyecto

```bash
# Clonar template
git clone [template-url] mi-proyecto
cd mi-proyecto

# Inicializar con Claude
claude

# Usar comando de inicialización
/init-project
```

### 2. Personalizar Documentación

1. Editar `CLAUDE.md` con contexto del proyecto
2. Actualizar `.claude/PLANNING.md` con arquitectura
3. Configurar `.claude/TASK.md` con fases

### 3. Desarrollo de Features

```bash
# Crear PRP para feature
/prp-create autenticacion

# Claude genera PRP detallado
# Revisar y ajustar PRPs/autenticacion.md

# Ejecutar PRP
/prp-execute PRPs/autenticacion.md

# Claude implementa step by step
```

### 4. Testing y Validación

```bash
# Comando check-all ejecuta:
# - Linting
# - Type checking
# - Tests
# - Build

# Python
uv run check-all

# Node.js
pnpm check-all
```

### 5. Actualizar Progreso

Actualizar `.claude/TASK.md` con:
- Tareas completadas
- Próximos pasos
- Bloqueadores

## 💡 Tips y Mejores Prácticas

### 1. Mantén CLAUDE.md Actualizado

Cada vez que hagas cambios importantes:
- ✅ Actualiza stack tecnológico
- ✅ Documenta decisiones
- ✅ Agrega recordatorios críticos

### 2. Usa Agentes para Tareas Repetitivas

Crea agentes para:
- Code review
- Generación de tests
- Documentación
- Refactoring

### 3. PRPs para Features Complejos

Usa PRPs cuando:
- El feature afecta múltiples archivos
- Requiere planificación detallada
- Necesitas validación step-by-step

### 4. Comandos para Workflows Comunes

Crea comandos para:
- Deployment
- Generación de docs
- Setup de features
- Validación completa

### 5. Aprovecha MCP Tools

Para investigación:
- `perplexity_ask`: Documentación actualizada
- `tavily_search`: Best practices
- `github_search_code`: Ejemplos de código

## 📚 Recursos Adicionales

- `docs/SERENA_MCP.md`: Análisis semántico de código
- `docs/MCP_TOOLS_GUIA.md`: Herramientas MCP disponibles
- `docs/FLUJO_INICIALIZACION.md`: Sistema de inicialización
- `docs/ejemplos/ejemplo_python.md`: Setup Python
- `docs/ejemplos/ejemplo_nodejs.md`: Setup Node.js
- `GUIA_CLAUDECODE.md`: Guía completa de Claude Code

---

**Con estas herramientas puedes personalizar completamente Claude Code para cualquier tipo de proyecto y aprovechar al máximo sus capacidades.**
