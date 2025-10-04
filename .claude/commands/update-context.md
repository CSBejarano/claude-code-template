# Command: update-context

🔄 **Actualiza y optimiza todos los archivos de contexto (.md) del proyecto para maximizar la efectividad de Claude Code.**

## 🎯 Filosofía del Comando

**Objetivo**: Asegurar que CLAUDE.md, README.md, PLANNING.md, TASK.md y todos los archivos de documentación estén actualizados, completos y optimizados para que Claude entienda perfectamente el proyecto.

---

## 🔀 Dos Modos de Operación

Este comando opera en **dos modos diferentes** según el contexto:

### **Modo 1: Proyecto Nuevo (Integrado)**
**Llamado automáticamente por `/init-project` en la Fase 0.7**

**Cuándo**:
- Durante creación de proyecto nuevo
- DESPUÉS de análisis del objetivo
- ANTES de crear estructura de archivos

**Fuente de información**:
- ✅ Objetivo del usuario
- ✅ Tech stack determinado
- ✅ Agentes planificados
- ✅ APIs identificadas
- ❌ NO analiza código (aún no existe)

**Output**:
- CLAUDE.md con misión específica
- PLANNING.md con arquitectura planificada
- README.md base
- QUICK_START.md template
- Documentación que GUÍA la implementación

**Ejemplo**:
```bash
# Usuario NO ejecuta este comando directamente
# Es llamado internamente por /init-project

/init-project "automatizar Gmail"
  ↓
  Fase 0: Sequential thinking
  ↓
  Fase 0.5: Gestión de agentes
  ↓
  Fase 0.7: [LLAMA /update-context en modo nuevo proyecto]
  ↓
  Genera docs basadas en plan, no en código
```

---

### **Modo 2: Proyecto Existente (Standalone/Mantenimiento)**
**Ejecutado manualmente por el usuario**

**Cuándo usar**:
- ✅ Después de cambios significativos en el código
- ✅ Cuando contexto de Claude parece desactualizado
- ✅ Antes de crear nuevas features importantes
- ✅ Periódicamente (cada 2-3 semanas de desarrollo)
- ✅ Cuando arquitectura ha evolucionado

**Fuente de información**:
- ✅ Código real en `src/`
- ✅ Estructura de archivos existente
- ✅ Agentes ya creados en `.claude/agents/`
- ✅ Configuración actual
- ✅ Tests existentes

**Output**:
- Documentación ACTUALIZADA reflejando código real
- Gaps identificados y corregidos
- Redundancias eliminadas
- Cross-referencias validadas
- Información obsoleta removida

**Ejemplo**:
```bash
# Usuario ejecuta directamente
/update-context

# Analiza código existente → Actualiza docs
```

---

## 🔍 Detección Automática de Modo

El comando detecta automáticamente en qué modo operar:

```
SI proyecto tiene src/ con archivos de código:
    → Modo 2: Proyecto Existente (analizar código real)

SI NO hay código o es llamado con --new-project:
    → Modo 1: Proyecto Nuevo (generar desde plan)

SI es llamado desde /init-project:
    → Modo 1: Proyecto Nuevo (recibe objetivo y plan)
```

---

## Usage

```bash
# Actualización completa (recomendado)
/update-context

# Actualizar solo archivos específicos
/update-context --files CLAUDE.md,README.md

# Modo análisis (no modifica, solo reporta)
/update-context --dry-run
```

## Arguments

- `--files`: Lista de archivos específicos a actualizar (opcional)
- `--dry-run`: Solo analiza y reporta, no modifica archivos (opcional)

---

## 🧠 INSTRUCCIONES CRÍTICAS PARA EL AGENTE

### ⚠️ REGLAS OBLIGATORIAS

#### 1. **SIEMPRE Usar Sequential Thinking**
```
OBLIGATORIO al inicio:
@mcp__server-sequential-thinking__sequentialthinking

Para analizar:
- Estado actual de la documentación
- Qué está desactualizado o faltante
- Qué información es crítica para Claude
- Cómo optimizar el contexto
- Orden de actualización de archivos
```

#### 2. **Orquestación de Agentes**
```
Este comando actúa como ORQUESTADOR:

1️⃣ Leer agentes en .claude/agents/
2️⃣ Delegar análisis a:
   - @codebase-analyst: Analizar estructura actual
   - @sequential-thinking: Planificar actualizaciones
   - @documentation-manager: Generar/actualizar docs
   - @context-optimizer* (crear): Optimizar contexto para Claude

3️⃣ Coordinar trabajo paralelo
4️⃣ Consolidar resultados
5️⃣ Presentar al usuario para aprobación
```

#### 3. **Interactividad Total**
```
NUNCA actualizar archivos sin confirmación del usuario

Flujo:
1. Analizar → Reportar hallazgos
2. Proponer cambios → Esperar aprobación
3. Aplicar cambios → Confirmar éxito
4. Validar → Mostrar resultado
```

---

## 📋 Fases del Comando (Paso a Paso)

### **Fase 0: Análisis con Sequential Thinking** 🧠

```
OBLIGATORIO al inicio:

"🧠 Analizando contexto del proyecto...

[Usa @mcp__server-sequential-thinking__sequentialthinking]

Thought 1: Leer estructura del proyecto...
Thought 2: Identificar archivos .md existentes...
Thought 3: Evaluar completitud de cada archivo...
Thought 4: Detectar información desactualizada...
Thought 5: Priorizar actualizaciones...
...

📊 Análisis completado:

Archivos .md encontrados:
✅ CLAUDE.md - Existe pero incompleto
✅ README.md - Existe pero desactualizado
❌ PLANNING.md - No existe
✅ TASK.md - Existe y actualizado
❌ QUICK_START.md - No existe
✅ .claude/INTERACTIVE_APPROACH.md - Existe
...

Continuar? (yes)"
```

---

### **Fase 1: Análisis de Agentes Disponibles** 🤖

```
"🤖 Revisando agentes disponibles...

[Lee .claude/agents/]

Agentes encontrados:
- codebase-analyst.md
- library-researcher.md
- [otros...]

Agentes a usar:
✅ @codebase-analyst: Analizar estructura del proyecto
✅ @documentation-manager: Generar/actualizar docs
✅ @sequential-thinking: Planificación

Agentes a crear:
🔨 @context-optimizer: Especialista en optimizar contexto para Claude
   - Analiza qué información es más útil
   - Optimiza formato y estructura
   - Elimina redundancias
   - Agrega secciones faltantes

¿Crear @context-optimizer? (yes/no)"

[ESPERAR CONFIRMACIÓN]
```

---

### **Fase 2: Inventario Completo** 📋

```
"📋 Creando inventario de documentación...

[PARALELO - Usar múltiples agentes]
├──> @codebase-analyst
│    └─> Analiza estructura del código
│    └─> Identifica componentes principales
│    └─> Extrae arquitectura
│
├──> @context-optimizer
│    └─> Lee archivos .md existentes
│    └─> Evalúa completitud
│    └─> Identifica gaps de información
│
└──> Bash/File tools
     └─> Lista todos los .md del proyecto
     └─> Verifica última modificación

✅ Inventario completado (3/3 agentes)

📊 REPORTE DE ESTADO:

┌─────────────────────────────────────────────────────────┐
│                  ESTADO DE DOCUMENTACIÓN                │
├─────────────────────────────────────────────────────────┤
│ Archivo              │ Estado      │ Completitud │ Acción│
├──────────────────────┼─────────────┼─────────────┼───────┤
│ CLAUDE.md            │ ⚠️ Parcial  │ 60%         │ Update│
│ README.md            │ ⚠️ Viejo    │ 70%         │ Update│
│ PLANNING.md          │ ❌ Falta    │ 0%          │ Create│
│ TASK.md              │ ✅ OK       │ 100%        │ Skip  │
│ QUICK_START.md       │ ❌ Falta    │ 0%          │ Create│
│ .claude/MCP_TOOLS.md │ ✅ OK       │ 100%        │ Skip  │
│ PRPs/templates/*.md  │ ✅ OK       │ 100%        │ Skip  │
└──────────────────────┴─────────────┴─────────────┴───────┘

GAPS CRÍTICOS DETECTADOS:
❌ CLAUDE.md falta:
   - Misión específica del proyecto
   - Arquitectura actual
   - Comandos personalizados del proyecto
   - Agentes personalizados creados

❌ README.md falta:
   - Instrucciones de setup actualizadas
   - Ejemplos de uso

❌ PLANNING.md no existe:
   - Arquitectura del sistema
   - Decisiones técnicas
   - Roadmap

INFORMACIÓN REDUNDANTE:
⚠️ Setup instructions duplicadas en CLAUDE.md y README.md
⚠️ Arquitectura mencionada parcialmente en 3 archivos

OPTIMIZACIONES SUGERIDAS:
💡 Consolidar setup en README.md solamente
💡 Mover arquitectura a PLANNING.md
💡 CLAUDE.md enfocado en contexto para Claude
💡 Crear QUICK_START.md para onboarding rápido

¿Proceder con actualizaciones? (yes/no/ajustar)"

[ESPERAR CONFIRMACIÓN]
```

---

### **Fase 3: Planificación de Actualizaciones** 📝

```
"📝 Planificando actualizaciones...

[Usa @sequential-thinking + @context-optimizer]

Plan de actualización:

1️⃣ CLAUDE.md (PRIORIDAD ALTA)
   Agregar:
   ├─> Misión específica del proyecto: [extraída del código]
   ├─> Arquitectura actual: [analizada por @codebase-analyst]
   ├─> Stack tecnológico real
   ├─> Comandos personalizados disponibles
   ├─> Agentes personalizados del proyecto
   ├─> Hooks configurados
   ├─> PRPs disponibles
   └─> Patrones de código establecidos

   Actualizar:
   ├─> Variables de entorno (de .env.example)
   ├─> Estructura del proyecto (real)
   └─> Flujo de desarrollo actual

2️⃣ PLANNING.md (CREAR)
   Incluir:
   ├─> Arquitectura completa del sistema
   ├─> Diagrama de componentes
   ├─> Flujo de datos
   ├─> Decisiones técnicas y razones
   ├─> Tech stack detallado
   ├─> Roadmap de features
   └─> Deuda técnica conocida

3️⃣ README.md (ACTUALIZAR)
   Optimizar:
   ├─> Descripción del proyecto
   ├─> Quick start (3 pasos)
   ├─> Setup completo
   ├─> Ejemplos de uso
   ├─> Troubleshooting común
   └─> Links a otra documentación

4️⃣ QUICK_START.md (CREAR)
   Contenido:
   ├─> 5-10 minutos para estar ejecutando
   ├─> Comandos exactos copy-paste
   ├─> Validación de que funciona
   └─> Link a README para más detalles

5️⃣ .claude/AGENTS.md (CREAR)
   Documentar:
   ├─> Lista de agentes disponibles
   ├─> Propósito de cada agente
   ├─> Cuándo usar cada agente
   └─> Ejemplos de invocación

¿Aprobar este plan? (yes/no/modificar)"

[ESPERAR CONFIRMACIÓN]
```

---

### **Fase 4: Actualización Archivo por Archivo** 📄

```
PATRÓN para cada archivo:

"📄 Actualizando [NOMBRE_ARCHIVO]...

[Delegar a @context-optimizer o @documentation-manager]

Agente trabajando...

✅ Borrador generado

📋 Vista previa de cambios:

[Mostrar diff de los cambios principales]

Cambios propuestos:
+ Sección agregada: "Misión del Proyecto"
  - "Este proyecto automatiza el procesamiento de facturas..."

~ Sección actualizada: "Arquitectura"
  - Actualizado diagrama de componentes
  - Agregados 3 servicios nuevos

- Sección removida: "Setup duplicado"
  - Movido a README.md

¿Aplicar estos cambios a [NOMBRE_ARCHIVO]? (yes/no/edit)"

[ESPERAR CONFIRMACIÓN]

SI yes:
    [Aplicar cambios]
    "✅ [NOMBRE_ARCHIVO] actualizado

    Siguiente archivo: [SIGUIENTE]
    ¿Continuar? (yes/pausa)"

SI edit:
    "¿Qué quieres modificar?

    Opciones:
    1. Editar sección específica
    2. Agregar información adicional
    3. Remover algo
    4. Cambiar formato

    Tu elección: (1-4 o descripción)"

    [Interacción para editar]
```

---

### **Ejemplo Concreto - Actualizar CLAUDE.md:**

```
"📄 Actualizando CLAUDE.md...

[Delega a @context-optimizer]

@context-optimizer:
"Analizando CLAUDE.md actual...

Archivo actual: Plantilla genérica (60% completo)

Información del proyecto detectada:
- Nombre: IA Corp - Claude Code Template
- Stack: Python, Node.js, n8n
- Propósito: Sistema de templates para proyectos con Claude Code
- Agentes detectados: codebase-analyst, library-researcher
- Comandos detectados: /init-project, /prp-create, /story-create

Generando CLAUDE.md optimizado..."

✅ Borrador generado

📋 Vista previa:

════════════════════════════════════════════════════════
CAMBIOS PRINCIPALES:

+ NUEVO - Misión del Proyecto (líneas 40-55):

  ## 🎯 **Misión del Proyecto**

  IA Corp - Claude Code Template es un **sistema de templates avanzado
  para proyectos impulsados por IA**, diseñado para maximizar la
  efectividad de Claude Code mediante:

  - Sistema de orquestación de agentes especializados
  - Comandos personalizados para automatización
  - PRPs (Pattern Recognition Protocols) para features
  - Hooks para eventos del ciclo de vida
  - Documentación auto-generada y optimizada

  ### **Problema que Resolvemos**
  - **Entrada**: Idea de proyecto o feature
  - **Proceso**: Análisis con IA → Orquestación de agentes →
                 Generación de código → Validación automática
  - **Salida**: Proyecto funcional con tests, docs y best practices

~ ACTUALIZADO - Agentes Disponibles (líneas 233-318):

  Agregados agentes personalizados del proyecto:
  + @context-optimizer
  + @project-initializer
  + [lista completa de agentes con descripciones]

+ NUEVO - Comandos del Proyecto (después línea 303):

  #### **Comandos de Gestión de Proyecto**

  ```bash
  # Inicializar nuevo proyecto
  /init-project [objetivo]

  # Actualizar contexto y documentación
  /update-context

  # Crear PRP para feature
  /prp-create [feature-name]
  ```

~ ACTUALIZADO - Estructura del Proyecto (líneas 68-87):

  Reflejada estructura real con agentes, hooks, PRPs

~ ACTUALIZADO - Variables de Entorno (líneas 119-131):

  [Si existe .env.example, usar esas variables]

════════════════════════════════════════════════════════

Total de cambios:
+ 4 secciones nuevas
~ 3 secciones actualizadas
- 0 secciones removidas
≈ 150 líneas agregadas

¿Aplicar estos cambios a CLAUDE.md? (yes/no/edit/ver-completo)"

[ESPERAR]

SI ver-completo:
    [Mostrar archivo completo generado]
    "¿Aplicar? (yes/no/edit)"

SI yes:
    "✅ CLAUDE.md actualizado (líneas: 337 → 487)

    Siguiente: PLANNING.md
    ¿Continuar? (yes/pausa)"
```

---

### **Fase 5: Generación de Archivos Nuevos** ✨

```
Para archivos que no existen:

"📄 Creando PLANNING.md...

[Usa @context-optimizer + @codebase-analyst en paralelo]

[PARALELO]
├──> @codebase-analyst
│    └─> Analiza arquitectura del código
│    └─> Identifica componentes y flujos
│    └─> Extrae dependencias
│
└──> @context-optimizer
     └─> Estructura el documento
     └─> Genera secciones apropiadas
     └─> Optimiza para claridad

✅ PLANNING.md generado

📋 Estructura del archivo:

PLANNING.md
├── 🎯 Visión del Proyecto
├── 🏗️ Arquitectura del Sistema
│   ├── Diagrama de Componentes
│   ├── Flujo de Datos
│   └── Tecnologías Usadas
├── 🔧 Decisiones Técnicas
│   ├── Por qué Python + Node.js
│   ├── Por qué sistema de agentes
│   └── Por qué PRPs
├── 📋 Roadmap
│   ├── Fase actual
│   ├── Próximos features
│   └── Backlog
├── 🐛 Deuda Técnica
└── 📊 Métricas y KPIs

Total: ~250 líneas

¿Ver vista previa? (yes/crear-directamente)"

[ESPERAR]

SI yes:
    [Mostrar contenido generado]
    "¿Crear PLANNING.md con este contenido? (yes/no/edit)"

SI crear-directamente:
    [Crear archivo]
    "✅ PLANNING.md creado

    Siguiente: QUICK_START.md
    ¿Continuar? (yes)"
```

---

### **Fase 6: Validación y Cross-Referencias** 🔗

```
"🔗 Validando consistencia entre archivos...

[Usa @context-optimizer]

Verificando:
├─> Referencias entre archivos (links)
├─> Información duplicada
├─> Inconsistencias en descripciones
└─> Completitud del ecosistema

Análisis:

✅ CORRECTO:
   - CLAUDE.md referencia correctamente a README.md
   - QUICK_START.md link a setup completo OK
   - Comandos consistentes en todos los archivos

⚠️ ADVERTENCIAS:
   - CLAUDE.md describe arquitectura brevemente
   - PLANNING.md describe arquitectura en detalle
   → Recomendación: CLAUDE.md link a PLANNING.md

❌ ERRORES:
   - README.md menciona comando /setup que no existe
   → Fix: Cambiar a /init-project

Aplicar fixes automáticos? (yes/no/ver-detalles)"

[ESPERAR]

SI yes:
    [Aplicar correcciones]
    "✅ Correcciones aplicadas

    - Fixed: README.md comando corregido
    - Added: Link CLAUDE.md → PLANNING.md

    Validación completa ✅"
```

---

### **Fase 7: Generación de Índice de Documentación** 📚

```
"📚 Creando índice de documentación...

[Genera .claude/DOCUMENTATION_INDEX.md]

Contenido:

# 📚 Índice de Documentación del Proyecto

## 🚀 Para Empezar
- [QUICK_START.md](../QUICK_START.md) - Setup en 10 minutos
- [README.md](../README.md) - Documentación principal

## 🧠 Para Claude Code
- [CLAUDE.md](../CLAUDE.md) - Contexto completo del proyecto
- [.claude/PLANNING.md](PLANNING.md) - Arquitectura y decisiones
- [.claude/TASK.md](TASK.md) - Tareas actuales

## 🤖 Sistema de Agentes
- [.claude/AGENTS.md](AGENTS.md) - Agentes disponibles
- [.claude/agents/](agents/) - Definiciones de agentes
- [.claude/INTERACTIVE_APPROACH.md](../PRPs/INTERACTIVE_APPROACH.md)

## ⚡ Comandos y PRPs
- [.claude/commands/](commands/) - Comandos personalizados
  - [init-project.md](commands/init-project.md)
  - [update-context.md](commands/update-context.md)
- [PRPs/templates/](../PRPs/templates/) - Templates PRP

## 🔧 Configuración
- [.claude/hooks/](hooks/) - Hooks de eventos
- [.claude/MCP_TOOLS.md](MCP_TOOLS.md) - Herramientas MCP

✅ Índice creado

Guardar como .claude/DOCUMENTATION_INDEX.md? (yes/no)"
```

---

### **Fase 8: Resumen Final** 🎉

```
"🎉 Actualización de contexto completada!

📊 RESUMEN DE CAMBIOS:

Archivos actualizados:
✅ CLAUDE.md (337 → 487 líneas) +150 líneas
   - Agregada misión específica
   - Actualizados agentes y comandos
   - Optimizado para Claude

✅ README.md (245 → 280 líneas) +35 líneas
   - Actualizado quick start
   - Corregidos comandos
   - Agregados ejemplos

Archivos creados:
✨ PLANNING.md (250 líneas)
   - Arquitectura completa
   - Decisiones técnicas
   - Roadmap

✨ QUICK_START.md (95 líneas)
   - Setup en 10 minutos
   - Comandos exactos

✨ .claude/AGENTS.md (180 líneas)
   - Documentación de agentes
   - Cuándo usar cada uno

✨ .claude/DOCUMENTATION_INDEX.md (75 líneas)
   - Índice navegable

Agentes creados:
🤖 @context-optimizer
   - Especialista en optimizar contexto
   - Guardado en .claude/agents/context-optimizer.md

MEJORAS DE CONTEXTO:

Antes:
- 📊 Completitud: 60%
- 🔗 Cross-refs: 30%
- ⚠️ Inconsistencias: 5
- 📄 Archivos: 8

Después:
- 📊 Completitud: 95% (+35%)
- 🔗 Cross-refs: 90% (+60%)
- ⚠️ Inconsistencias: 0 (-5)
- 📄 Archivos: 14 (+6)

🎯 IMPACTO ESPERADO:

Para Claude Code:
✅ Entenderá el proyecto 95% mejor
✅ Sugerencias más precisas
✅ Menos preguntas de clarificación
✅ Código más alineado con arquitectura
✅ Mejor uso de agentes y comandos

Para Desarrolladores:
✅ Onboarding más rápido
✅ Contexto claro del proyecto
✅ Menos búsqueda de información
✅ Arquitectura documentada

PRÓXIMOS PASOS:

1. Revisar archivos generados/actualizados
2. Hacer ajustes si es necesario
3. Commit de cambios:
   ```bash
   git add CLAUDE.md README.md PLANNING.md QUICK_START.md .claude/
   git commit -m "docs: optimize project context for Claude Code"
   ```
4. Empezar a usar contexto mejorado

¿Quieres revisar algún archivo específico? (archivo/no/todo-ok)"

[ESPERAR]

SI todo-ok:
    "✅ ¡Perfecto! Tu proyecto ahora tiene contexto optimizado.

    Puedes ejecutar:
    - /init-project para crear nuevo proyecto
    - /prp-create para agregar features

    Los archivos actualizados maximizarán la efectividad de Claude."
```

---

## 🚫 ANTI-PATRONES

### ❌ NUNCA hagas esto:

```
❌ Actualizar archivos sin mostrar cambios primero
❌ Sobrescribir sin backup
❌ Generar documentación genérica (plantillas sin contenido real)
❌ Ignorar información existente en el proyecto
❌ Crear inconsistencias entre archivos
❌ Documentar features que no existen
❌ Copiar descripciones sin analizar código real
❌ No usar agentes especializados
❌ Hacer todo secuencialmente en lugar de paralelo
```

### ✅ SIEMPRE haz esto:

```
✅ Analizar código real antes de documentar
✅ Mostrar preview de cambios antes de aplicar
✅ Pedir confirmación en cada archivo
✅ Usar agentes en paralelo
✅ Extraer información del código, no inventarla
✅ Mantener consistencia entre archivos
✅ Crear cross-referencias apropiadas
✅ Optimizar para claridad y utilidad
✅ Documentar decisiones técnicas con razones
✅ Incluir ejemplos reales del proyecto
```

---

## 🎯 Checklist Final

Antes de terminar, verifica:

### **Análisis** 🧠
- [ ] Usaste sequential thinking al inicio
- [ ] Analizaste todos los archivos .md existentes
- [ ] Identificaste gaps y redundancias
- [ ] Extrajiste información real del código

### **Orquestación de Agentes** 🤖
- [ ] Leíste agentes en `.claude/agents/`
- [ ] Creaste @context-optimizer
- [ ] Usaste agentes en paralelo
- [ ] Delegaste tareas apropiadamente

### **Actualización de Archivos** 📄
- [ ] Mostraste preview de cada cambio
- [ ] Esperaste confirmación del usuario
- [ ] Aplicaste solo cambios aprobados
- [ ] Validaste consistencia entre archivos

### **Calidad del Contexto** 💎
- [ ] CLAUDE.md completo con info real del proyecto
- [ ] PLANNING.md con arquitectura actual
- [ ] README.md actualizado
- [ ] QUICK_START.md creado (si no existía)
- [ ] Cross-referencias correctas
- [ ] Sin inconsistencias
- [ ] Ejemplos reales incluidos

### **Resultado** ✅
- [ ] Completitud >90%
- [ ] Usuario satisfecho con cambios
- [ ] Archivos listos para commit
- [ ] Claude tendrá contexto óptimo

---

## 📊 Métricas de Éxito

Un buen update-context logra:

### **Completitud** 📈
- ✅ **90%+ completitud** en archivos principales
- ✅ **100% info real** extraída del código
- ✅ **0 inconsistencias** entre archivos
- ✅ **Cross-refs completas** y funcionando

### **Impacto en Claude** 🤖
- ✅ **95%+ comprensión** del proyecto
- ✅ **3x menos preguntas** de clarificación
- ✅ **2x mejor precisión** en sugerencias
- ✅ **Uso correcto** de agentes y comandos

### **Impacto en Desarrollo** 👨‍💻
- ✅ **<10 min onboarding** para nuevos devs
- ✅ **1 fuente de verdad** para arquitectura
- ✅ **0 búsqueda** de información básica

---

## 🔗 Comandos Relacionados

- `/init-project` - Crear nuevo proyecto (usa contexto optimizado)
- `/prp-create` - Crear PRP para feature (usa info de PLANNING.md)
- `/story-create` - Convertir user story (usa contexto de CLAUDE.md)

---

## 📝 Notas Importantes

1. **Ejecutar periódicamente**
   - Después de features importantes
   - Cuando arquitectura cambia
   - Cada 2-3 semanas de desarrollo activo

2. **Información real siempre**
   - Extrae del código, no inventes
   - Analiza archivos reales
   - Documenta estado actual, no ideal

3. **Contexto optimizado para Claude**
   - CLAUDE.md es el archivo más importante
   - Debe tener info precisa y completa
   - Usar lenguaje claro y estructurado

4. **Consistencia es clave**
   - Un archivo por tema
   - Cross-referencias claras
   - Sin duplicación innecesaria

5. **Agentes especializados**
   - @context-optimizer es crítico
   - Usar paralelización
   - Consolidar resultados

---

**🎯 Objetivo: Maximizar la efectividad de Claude Code con contexto perfecto**
