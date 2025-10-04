# Técnicas Avanzadas de Ingeniería de Contexto para Agentes de IA con Claude Code

## 📋 Resumen Ejecutivo

Este documento resume las mejores prácticas y técnicas de ingeniería de contexto para maximizar el rendimiento de Claude Code, basado en la experiencia del equipo de BAML que logró enviar miles de líneas de código de alta calidad diariamente.

---

## 🎯 Principio Fundamental: Gestión del Context Window

**Regla de oro**: Mantén el uso del context window al máximo 50% de capacidad (de 200k tokens disponibles).

### ¿Por qué es importante?

- Cada mensaje de usuario envía TODO el context window al modelo
- Cada llamada a herramientas envía TODO el context window
- Mayor contexto = menor densidad de información útil = peor rendimiento

---

## 🔄 Proceso de 3 Fases

### 1. **Research (Investigación)**
- Usa sub-agentes para explorar diferentes partes del codebase en paralelo
- Genera un documento markdown (100-400 líneas) con hallazgos clave
- **Incluye**: paths exactos de archivos, números de línea, flujo de información
- **Revisa manualmente** este documento - es el punto de mayor leverage

**Ejemplo de prompt de investigación**:
```
Find everywhere in [feature/bug] relevant to solving this issue
and figure out how the information flows.
```

### 2. **Planning (Planificación)**
- Crea un plan de implementación por fases basado en el research
- Especifica cambios exactos por archivo y número de línea
- Define tests a crear ANTES de implementar
- Incluye sección "What we're NOT doing" para evitar scope creep

**Estructura del plan**:
- Fase 1: Cambios específicos (archivo:línea)
- Fase 2: Tests a agregar
- Fase 3: Verificación automatizada

### 3. **Implementation (Implementación)**
- Con buen research y plan, la implementación es casi automática
- El agente puede trabajar con auto-accept activado
- Enfócate en revisar los tests, no tanto el código

---

## 🤖 Sub-Agentes: Control de Contexto

**Propósito**: Los sub-agentes NO son para antropomorfizar, son SOLO para control de contexto.

### Cuándo usar sub-agentes:

1. **Búsquedas en paralelo**: "Go find where X happens and where Y happens"
2. **Tareas independientes**: Escribir múltiples tests unitarios
3. **Investigación**: Cada sub-agente investiga una parte específica

### Ventajas:
- Context window limpio y separado para cada tarea
- Resultados compactos y relevantes
- Las herramientas de búsqueda no ensucian el context principal
- Ejecución paralela

**Prompt óptimo**:
```
Use a sub-agent and prompt it like this: [instrucciones específicas]
```

---

## 📦 Compactación Intencional del Contexto

### Estrategias:

1. **Manual Compaction** (Mejor que /compact):
   ```
   Put everything we did so far in a markdown file
   so that an agent can pick up with the task
   ```

2. **Micro Compaction**: Elimina solo tool calls innecesarios

3. **Clear Context**: Inicia sesión nueva con contexto limpio

4. **Estrategia recomendada**:
   - Compacta manualmente el progreso en archivo .md
   - Usa /clear para nueva sesión
   - Lee el archivo compactado y continúa

---

## 🧪 Test-Driven Development (TDD) con Agentes

**Regla crítica**: SIEMPRE usa TDD con agentes de IA.

### Por qué TDD es esencial:

1. **Verificación automática**: El agente sabe si está correcto
2. **Menor revisión humana**: Tests bien diseñados = código confiable
3. **Checkpoints claros**: Cada test es un punto de validación

### Mejores prácticas:

- **Escribe tests PRIMERO**, luego el código
- Asegúrate de que los comandos de test sean triviales de ejecutar
- Usa nombres de test descriptivos para el LLM
- El agente debe poder ejecutar tests individuales fácilmente

**Ejemplo de workflow**:
```
Phase 1: Write failing test
Phase 2: Implement feature
Phase 3: Verify test passes
```

---

## 📝 Importancia de Revisar el Output

**Jerarquía de impacto de errores**:

1. **Prompts base**: 1 error = 100,000 líneas malas
2. **Research**: 1 error = 1,000 líneas malas
3. **Plan**: 1 error = 10-100 líneas malas
4. **Código**: 1 error = 1 línea mala

### Proceso de revisión del equipo:

1. ✅ **TODO** el equipo revisa el research
2. ✅ **TODO** el equipo revisa el plan
3. ⚠️ Revisión ligera del código
4. ✅ Revisión detallada de los **tests**

**Workflow en Linear**:
```
To Do → Research Needed → Research in Progress →
Research in Review → Ready for Plan → Plan in Progress →
Plan in Review → Ready for Dev → In Dev →
Code Review → Ready for Deploy
```

---

## 🏗️ Arquitectura del Codebase

### Principios clave:

1. **Nomenclatura consistente**:
   - Usa los MISMOS nombres en todo el codebase
   - Evita 7 formas diferentes de llamar a lo mismo
   - "Field attributes" debe llamarse igual en TODAS partes

2. **Estructura de archivos clara**:
   - ❌ Evita: `page.tsx` en múltiples carpetas (Next.js)
   - ✅ Prefiere: nombres de archivo únicos y descriptivos
   - Considera que el LLM ve una lista de paths, no una jerarquía visual

3. **Monorepo o links simbólicos**:
   - Usa hard links (no symlinks) para que las herramientas de búsqueda funcionen
   - Agrega directorios adicionales en settings.json de Claude Code

4. **Herramientas de build consistentes**:
   - Todos los comandos deben usar la misma herramienta (npm, bun, etc.)
   - Package.json con comandos claros y uniformes
   - Considera Turborepo para workspaces complejos

---

## ⚙️ Configuración y Herramientas

### VS Code + Claude Code:

1. **Terminal integrado**: Abre Claude Code en terminal integrado de VS Code
2. **Extensión de VS Code**: Instala la extensión para acceso a LSP
3. **Intérprete correcto**: Selecciona el intérprete Python con librerías correctas
4. **Type checking**: Activa type checking en Python (off por defecto)

### Hooks y feedback loops:

1. **Claude Code Hooks**: Configura hooks para ejecutar linters automáticamente
2. **LSP Errors Tool**: El agente puede obtener errores del IDE
3. **Automated verification**: Incluye comandos de verificación en el plan

### Claude.md:

⚠️ **IMPORTANTE**: El contenido de Claude.md viene con un disclaimer:
```
"This context may or may not be relevant to your task.
You should not respond to this context unless it is highly relevant."
```

**Solución**: Para instrucciones críticas, ponlas:
- Directamente en el prompt
- En el plan de implementación
- NO solo en Claude.md

---

## 🎨 MCP Tools: Optimización

### Problemas comunes:

- Demasiados tools = context window lleno
- JSON ruidoso en respuestas
- Información irrelevante

### Soluciones:

1. **Custom tools contexto-optimizados**:
   - Ejemplo: Tool de Linear que retorna markdown limpio
   - Comprime la información antes de retornarla
   - Incluye solo datos relevantes

2. **Tool search/RAG**:
   - Para 10,000+ tools, implementa búsqueda de tools
   - El agente busca qué tool usar antes de ejecutar
   - Evita cargar todos los tools en el context window

3. **Limita tools por sesión**:
   - Solo carga tools relevantes para la tarea actual

---

## 🎯 Técnicas de Prompting Avanzadas

### Steering (Dirección):

```
Only use read, glob, grep, search. Never bash
because bash requires permission.
```

### Extended Thinking:

```
Think deeply about [problema]
```
⚠️ Puede ser contraproducente - usa con cuidado

### Iteración cuando falla:

1. Identifica por qué falló
2. Crea un mejor prompt de research
3. Reinicia con contexto limpio
4. Usa compactación manual del intento fallido

### Especificidad de sub-agentes:

```
Use a task/sub-agent to: [tarea específica]
Prompt it with: [instrucciones exactas]
Return: [formato específico de respuesta]
```

---

## 🚀 Workflow Práctico Recomendado

### Para bugs/features pequeños:

1. Ir directo a Planning (skip Research)
2. El plan hará research mínimo necesario
3. Si context > 80% después de research, reinicia con compactación

### Para features complejos:

1. **Research** (con sub-agentes paralelos)
2. Revisar y refinar research manualmente
3. **Planning** basado en research
4. Revisar plan en equipo
5. **Implementation** con auto-accept
6. Revisar tests ejecutados

### Regla de 10 minutos:

- Intenta con Claude Code por 10 minutos
- Si ves camino claro a completar en 30 min, continúa
- Si no, reinicia con nueva estrategia
- Después de 2 intentos, considera hacerlo manual

---

## 📊 Métricas de Éxito

### Indicadores de buen workflow:

- ✅ Context window < 50% al implementar
- ✅ Tests pasan en primer intento
- ✅ Research identifica archivos correctos
- ✅ Plan tiene fases claras y ejecutables
- ✅ Equipo entiende los cambios sin leer código

### Red flags:

- ❌ Context window > 80%
- ❌ Research dice "no hay problema" cuando sí existe
- ❌ Plan vago sin números de línea específicos
- ❌ Múltiples iteraciones sin progreso
- ❌ Scope creep continuo

---

## 💡 Tips Profesionales

### 1. **Reps, reps, reps**
- Practica constantemente para desarrollar intuición
- Como aprender un instrumento musical
- Experimenta con orden de prompts (¿contexto primero o pregunta primero?)

### 2. **Trata el agente como junior engineer**
- Cada nueva sesión/sub-agente = nuevo empleado sin contexto
- Proporciona onboarding claro cada vez
- Documentación y nomenclatura consistente es crítica

### 3. **Enfócate en lo de mayor leverage**
- Invierte tiempo en research y planning
- Menos tiempo revisando código
- Los tests son tu verificación principal

### 4. **Adapta tu codebase**
- Rust/Cargo funcionan excepcionalmente bien (TDD por defecto)
- TypeScript con Turbo es excelente
- Invierte en tooling que facilite testing automático

### 5. **Aprende de los fallos**
- Research incorrecto → mejora el prompt de research
- Plan vago → añade más especificidad requerida
- Código incorrecto → mejora los tests primero

---

## 🔗 Recursos

- **Comandos open-source**: [Human Layer Terminal UI](https://github.com/BoundaryML/baml)
- **Research prompts**: 300+ líneas de markdown con sub-agent instructions
- **Planning prompts**: Estructura de fases con verification steps
- **Linear workflow**: To-do → Research → Plan → Dev → Deploy

---

## 📌 Checklist Rápido

Antes de empezar una tarea con Claude Code:

- [ ] ¿Tengo research si es complejo?
- [ ] ¿Mi plan tiene números de línea específicos?
- [ ] ¿Estoy escribiendo tests PRIMERO?
- [ ] ¿Voy a usar sub-agentes para búsquedas?
- [ ] ¿Mi context window está < 50%?
- [ ] ¿He configurado LSP y type checking?
- [ ] ¿Mis nombres de archivos son únicos y descriptivos?
- [ ] ¿Tengo comandos de test triviales?

---

## 🎓 Conclusión

La ingeniería de contexto para agentes de IA es sobre:

1. **Gestión rigurosa del context window**
2. **Proceso estructurado** (Research → Plan → Implementation)
3. **TDD siempre** con agentes
4. **Review humano en puntos de alto leverage**
5. **Codebase optimizado** para LLMs
6. **Práctica constante** para desarrollar intuición

**Recuerda**: "Context engineering" no es diferente de escribir buenos prompts para LLMs - es aplicar los mismos principios a un flujo de trabajo de desarrollo completo.

---

*Basado en el podcast "Advanced Context Engineering for Coding Agents" - Episode #17*
