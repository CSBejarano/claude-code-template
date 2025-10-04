# Command: init-project

🚀 **Inicializa un nuevo proyecto de manera COMPLETAMENTE INTERACTIVA y paso a paso.**

## 🎯 Filosofía del Comando

**NUNCA**: Crear todo → Dar 50 pasos al final → Usuario se pierde
**SIEMPRE**: Crear base → Guiar paso a paso → Validar → Probar → Confirmar → Siguiente paso

---

## Usage

```bash
/init-project [optional-goal-hint]
```

## Arguments

- `[optional-goal-hint]`: Optional hint about what you want to build (e.g., "Gmail automation", "API REST", "data processing")

---

## 🧠 INSTRUCCIONES CRÍTICAS PARA @project-initializer

### ⚠️ REGLAS OBLIGATORIAS

#### 1. **SIEMPRE Usar Sequential Thinking**
```
ANTES de cualquier acción importante, DEBES usar:
@mcp__server-sequential-thinking__sequentialthinking

Para:
- Analizar el objetivo del usuario
- Determinar tech stack apropiado
- Planificar estructura del proyecto
- Diseñar flujo de setup interactivo
- Evaluar dependencias y APIs necesarias
```

#### 2. **NUNCA Hacer Todo de Una Vez**
```
❌ NO HAGAS ESTO:
- Crear todos los archivos
- Dar lista de 50 pasos
- Configurar todas las APIs simultáneamente
- Asumir que algo funciona sin probar

✅ HAZ ESTO:
- Crear estructura base primero
- Configurar 1 API a la vez
- Probar cada componente inmediatamente
- Preguntar "¿funcionó?" después de cada paso
- Arreglar errores EN TIEMPO REAL
```

#### 3. **Flujo Interactivo Obligatorio**
Cada setup de API/servicio DEBE seguir este patrón:

```
1. 📋 Explicar qué y por qué
2. 🔗 Dar links EXACTOS (no "ve a la consola...")
3. 📝 Dar comandos EXACTOS para copiar/pegar
4. ⏸️  Esperar confirmación del usuario
5. ✅ Validar credenciales/configuración
6. 🧪 Probar conexión/funcionalidad
7. 🎉 Confirmar éxito antes de continuar
8. ➡️  Solo entonces, pasar al siguiente
```

#### 4. **Sistema de Orquestación de Agentes (OBLIGATORIO)**
```
SIEMPRE al inicio del comando:

1️⃣ Leer agentes existentes en .claude/agents/
2️⃣ Evaluar cuáles son relevantes para el proyecto
3️⃣ Crear agentes personalizados necesarios
4️⃣ Establecer estrategia de delegación:
   - Qué agente hace qué
   - Qué agentes trabajan en paralelo
   - Cómo se comunican entre sí

5️⃣ Actuar como ORQUESTADOR:
   - Delegar tareas a agentes especializados
   - Coordinar trabajo paralelo
   - Consolidar resultados
   - Mantener comunicación con usuario

6️⃣ Integrar ecosistema completo:
   - Hooks
   - PRPs
   - Documentación
   - Comandos personalizados

📊 Ejemplo de delegación:
- @sequential-thinking → Análisis de arquitectura
- @library-researcher → Investigar tech stack
- @[custom]-specialist → Setup de API específica
- @project-validator → Testing de componentes
- @documentation-manager → Generar docs

TODOS coordinados por @project-initializer (tú, el orquestador)
```

---

## 📋 Fases del Comando (Paso a Paso)

### **Fase 0: Análisis con Sequential Thinking** 🧠

```
OBLIGATORIO al inicio:

1. Usar @mcp__server-sequential-thinking__sequentialthinking para:
   - Entender el objetivo del usuario
   - Identificar tipo de proyecto (automation, API, data processing, etc.)
   - Determinar complejidad
   - Listar APIs/servicios probables
   - Proponer tech stack
   - Diseñar flujo de setup interactivo

2. Presentar análisis al usuario:
   "🤔 He analizado tu objetivo. Esto es lo que entendí:

    📊 Tipo: [tipo de proyecto]
    🎯 Objetivo: [objetivo claro]
    📚 APIs necesarias: [lista]
    💻 Tech Stack recomendado: [stack]

    ¿Es correcto? (yes/no/ajustar)"
```

---

## 🤖 SISTEMA DE ORQUESTACIÓN DE AGENTES

### 🎯 Arquitectura del Sistema

```
@project-initializer (ORQUESTADOR)
         |
         ├──> Análisis de Agentes Existentes
         |    └──> Lee .claude/agents/*.md
         |    └──> Evalúa relevancia para el proyecto
         |    └──> Decide: usar, modificar o crear nuevos
         |
         ├──> Creación de Agentes Personalizados
         |    └──> Genera agentes específicos del proyecto
         |    └──> Guarda en .claude/agents/
         |
         ├──> Orquestación Paralela
         |    ├──> @sequential-thinking (análisis)
         |    ├──> @library-researcher (tech stack)
         |    ├──> @codebase-analyst (patrones)
         |    ├──> @[custom-agent-1] (tarea específica)
         |    └──> @[custom-agent-2] (tarea específica)
         |
         ├──> Integración con Ecosistema
         |    ├──> Hooks (.claude/hooks/)
         |    ├──> PRPs (PRPs/templates/)
         |    ├──> Documentación (.md files)
         |    └──> Comandos personalizados
         |
         └──> Interacción Usuario
              └──> Bucle: Usuario ↔ Orquestador ↔ Subagentes
```

---

### **Fase 0.5: Análisis y Gestión de Agentes** 🤖

**OBLIGATORIO antes de crear el proyecto:**

```
1. ANALIZAR AGENTES EXISTENTES:

"🤖 Analizando agentes disponibles...

Leyendo: .claude/agents/"

[Lee todos los archivos .md en .claude/agents/]

Agentes encontrados:
- codebase-analyst.md: Analiza patrones de código
- library-researcher.md: Investiga librerías
- [otros agentes...]

2. EVALUAR RELEVANCIA:

[Usa @mcp__server-sequential-thinking__sequentialthinking]

"Evaluando qué agentes son útiles para tu proyecto:

📊 Análisis de relevancia:

✅ ÚTILES para este proyecto:
   - codebase-analyst: Necesario para [razón específica]
   - library-researcher: Necesario para [razón específica]

⚠️ PARCIALMENTE ÚTILES (necesitan adaptación):
   - [agente-x]: Útil pero requiere [modificación]

❌ NO RELEVANTES:
   - [agente-y]: No aplica para este tipo de proyecto

3. DECIDIR ESTRATEGIA DE AGENTES:

Estrategia para tu proyecto:

1️⃣ Usar agentes existentes:
   - @codebase-analyst
   - @library-researcher

2️⃣ Crear agentes personalizados:
   - @[proyecto]-setup-specialist: Para configurar [tech stack específico]
   - @[proyecto]-validator: Para validar [componente específico]
   - @[proyecto]-debugger: Para debugging especializado

3️⃣ Modificar agentes:
   - [agente-x] → Adaptar para [necesidad específica]

¿Te parece bien esta estrategia de agentes? (yes/no/ajustar)"
```

---

### **Creación de Agentes Personalizados**

Cuando el proyecto requiere agentes especializados:

```
"🔨 Creando agentes personalizados para tu proyecto...

Agente 1/N: @gmail-api-specialist

Propósito:
- Especialista en configuración de Gmail API
- Guía OAuth2 paso a paso
- Debugging de permisos
- Testing de conexión

Herramientas disponibles:
- WebFetch (documentación Gmail API)
- Bash (comandos de validación)
- Read/Write (configuración)

[Crea: .claude/agents/gmail-api-specialist.md]

✅ Agente creado

Agente 2/N: @project-validator

Propósito:
- Validar cada componente después de crearlo
- Ejecutar tests automáticamente
- Verificar configuración
- Reportar problemas

Herramientas disponibles:
- Bash (ejecutar tests)
- Read (leer configuración)
- Grep (buscar errores en logs)

[Crea: .claude/agents/project-validator.md]

✅ Agente creado

📋 Resumen de agentes:
✅ 2 agentes existentes reutilizados
✅ 2 agentes personalizados creados
✅ Sistema de orquestación listo

Estos agentes trabajarán en paralelo durante la creación del proyecto.

Continuar? (yes)"
```

---

### **Orquestación Paralela de Agentes**

Durante la creación del proyecto, el orquestador usa agentes en paralelo:

```
Ejemplo - Fase de Análisis:

"🔄 Ejecutando análisis paralelo con 3 agentes...

[PARALELO]
├──> @sequential-thinking
│    └─> Analizando arquitectura del proyecto...
│
├──> @library-researcher
│    └─> Investigando mejores librerías para Gmail API...
│
└──> @codebase-analyst
     └─> Buscando patrones similares en proyectos existentes...

[ESPERAR RESULTADOS]

✅ Análisis completado (3/3 agentes)

📊 Resultados consolidados:

🧠 Sequential Thinking dice:
   - Arquitectura modular recomendada
   - Separar auth, gmail, rules en módulos
   - SQLite suficiente para este volumen

📚 Library Researcher encontró:
   - google-api-python-client v2.108.0 (recomendado)
   - google-auth-oauthlib v1.2.0
   - APScheduler v3.10.4
   - Best practice: usar service factory pattern

🔍 Codebase Analyst identificó:
   - Patrón similar en proyecto X
   - Estructura de auth reutilizable
   - Error común: no renovar tokens

💡 Recomendación consolidada:
   [Combina insights de los 3 agentes]

¿Te parece bien? (yes/no)"
```

---

### **Ejemplo - Setup de API con Agente Especializado**

```
"📧 Fase: Configurar Gmail API

Delegando a @gmail-api-specialist...

[@gmail-api-specialist toma control]

Gmail API Specialist:
👋 Hola, soy el especialista en Gmail API. Voy a guiarte paso a paso.

1️⃣ Ve a: https://console.cloud.google.com/

[Mientras usuario trabaja...]

[PARALELO]
├──> @project-validator
│    └─> Preparando tests de validación...
│    └─> Creando gmail_test.py
│
└──> @library-researcher
     └─> Buscando documentación de troubleshooting...
     └─> Preparando soluciones a errores comunes

[Usuario confirma paso 1]

Gmail API Specialist:
2️⃣ Ahora habilita la API...

[Continúa interacción...]

✅ Credenciales descargadas

🧪 Pasando control a @project-validator para probar...

[@project-validator]
Validator:
Ejecutando test de OAuth2...

```bash
uv run python tests/test_gmail_auth.py
```

✅ Test pasado
✅ Gmail API funcionando

[De vuelta a @project-initializer]

Project Initializer:
🎉 Gmail API configurada y validada!

Siguiente: [siguiente componente]
```

---

### **Integración con Hooks y PRPs**

El orquestador también usa el ecosistema completo:

```
"🔧 Configurando hooks para el proyecto...

Creando hooks personalizados:

1. pre-commit hook
   └─> Ejecutar tests antes de commit
   └─> Validar credenciales no expuestas

2. post-api-setup hook
   └─> Validar configuración automáticamente
   └─> Generar documentación

[Crea: .claude/hooks/pre-commit.sh]
[Crea: .claude/hooks/post-api-setup.sh]

✅ Hooks configurados

---

📋 Generando PRP template para futuras features...

[Crea: PRPs/templates/gmail-labeler-feature.md]

Template creado para agregar nuevas features con:
- Context del proyecto
- Tech stack
- Patrones establecidos
- Agentes disponibles

Puedes usar: /prp-create nueva-feature

✅ Sistema PRP listo

---

📖 Generando documentación...

[PARALELO]
├──> Agente 1: Genera README.md
├──> Agente 2: Genera CLAUDE.md
├──> Agente 3: Genera PLANNING.md
└──> Agente 4: Genera API_SETUP.md

✅ Documentación completa creada
```

---

### **Bucle de Interacción Usuario-Orquestador-Subagentes**

```
Flujo típico:

Usuario: "Quiero agregar clasificación con IA"

      ↓

@project-initializer (Orquestador):
"Entendido. Analizando..."

[Usa @sequential-thinking]
"Necesitaremos Anthropic API. ¿Lo confirmamos? (yes)"

      ↓

Usuario: "yes"

      ↓

@project-initializer:
"Delegando a agentes especializados..."

[PARALELO]
├──> @library-researcher
│    └─> Busca best practices Claude API
│
├──> @anthropic-api-specialist (crea este agente)
│    └─> Prepara guía de setup
│
└──> @project-validator
     └─> Prepara tests de IA

[Agentes reportan a orquestador]

      ↓

@anthropic-api-specialist (al usuario):
"👋 Soy el especialista en Anthropic API.

1️⃣ Ve a: https://console.anthropic.com/
..."

[Interacción directa con usuario]

      ↓

Usuario: "¿Qué modelo usar?"

      ↓

@anthropic-api-specialist:
[Consulta a @library-researcher]
"Para clasificación de emails, recomiendo Claude 3.5 Haiku porque..."

      ↓

Usuario: "ok"

      ↓

@project-validator:
"Probando IA..."
✅ Funcionando

      ↓

@project-initializer (orquestador):
"🎉 Clasificación con IA agregada exitosamente!

Resumen:
- Claude 3.5 Haiku configurado
- Tests pasados
- Documentación actualizada

¿Algo más? (yes/no)"
```

---

### **📋 Checklist de Orquestación**

Antes de crear cualquier proyecto, el orquestador debe:

- [ ] Leer todos los agentes en `.claude/agents/`
- [ ] Evaluar relevancia de cada agente para el proyecto
- [ ] Decidir qué agentes reutilizar
- [ ] Crear agentes personalizados si es necesario
- [ ] Definir estrategia de delegación de tareas
- [ ] Preparar hooks relevantes
- [ ] Configurar PRPs templates
- [ ] Establecer bucle de comunicación Usuario ↔ Orquestador ↔ Subagentes
- [ ] Validar que todos los agentes tienen herramientas necesarias
- [ ] Documentar qué agente hace qué

---

### **🎯 Ejemplo de Delegación de Tareas**

Para un proyecto de Gmail automation:

```
📋 Plan de delegación:

Fase              | Agente Principal           | Agentes de Apoyo
------------------|----------------------------|------------------
Análisis          | @sequential-thinking       | @library-researcher
Tech Stack        | @library-researcher        | @codebase-analyst
Estructura Base   | @project-initializer       | -
Gmail API Setup   | @gmail-api-specialist*     | @project-validator
OAuth2 Flow       | @gmail-api-specialist*     | @library-researcher
Testing           | @project-validator         | -
Documentación     | @documentation-manager     | @codebase-analyst
Deploy Prep       | @deployment-specialist*    | @project-validator

* = Agentes creados específicamente para este proyecto

Todos reportan a: @project-initializer (orquestador)
```

---

### **🔄 Actualización Dinámica de Agentes**

Durante el proyecto, el orquestador puede crear más agentes:

```
@project-initializer:
"He detectado que necesitamos un componente complejo de OCR.

Voy a crear un agente especializado para esto:

🔨 Creando @ocr-specialist...

Especialista en:
- Google Cloud Vision API
- Extracción de datos de facturas
- Validación de datos extraídos
- Manejo de errores de OCR

✅ Agente @ocr-specialist creado

Delegando configuración de OCR a este agente..."

[@ocr-specialist toma control y guía al usuario]
```

---

## 🌐 Ecosistema Completo

El orquestador integra TODO:

```
.claude/
├── agents/                    ← Agentes (existentes + creados)
│   ├── codebase-analyst.md
│   ├── library-researcher.md
│   ├── gmail-api-specialist.md    ← Creado por proyecto
│   ├── project-validator.md       ← Creado por proyecto
│   └── ocr-specialist.md          ← Creado dinámicamente
│
├── hooks/                     ← Hooks del proyecto
│   ├── pre-commit.sh
│   ├── post-api-setup.sh
│   └── pre-deploy.sh
│
├── commands/                  ← Comandos (este archivo)
│   └── init-project.md
│
├── PLANNING.md               ← Arquitectura del proyecto
├── TASK.md                   ← Tareas actuales
└── MCP_TOOLS.md              ← Herramientas disponibles

PRPs/
├── templates/
│   └── gmail-labeler-feature.md   ← Template del proyecto
└── implementations/
    └── ai-classification.md       ← PRPs generados

[Proyecto creado]
├── README.md                 ← Generado por agentes
├── CLAUDE.md                 ← Context para Claude
├── src/                      ← Código
├── tests/                    ← Tests (generados por @project-validator)
└── config/                   ← Configuración
```

Todo coordinado por @project-initializer como orquestador.

---

### **Fase 0.7: Generación de Documentación Base Contextualizada** 📚

**CRÍTICO**: Esta fase se ejecuta DESPUÉS de entender el objetivo (Fase 0-0.5) pero ANTES de crear archivos.

```
"📚 Generando documentación base para tu proyecto...

Con la información recopilada:
- 🎯 Objetivo: [objetivo del usuario]
- 💻 Tech Stack: [stack determinado]
- 🤖 Agentes: [agentes a crear]
- 📡 APIs: [APIs necesarias]

Voy a generar documentación optimizada que guiará la implementación.

[PARALELO - Usar múltiples agentes]
├──> @context-optimizer (crear si no existe)
│    └─> Genera CLAUDE.md contextualizado
│    └─> Optimiza para máxima claridad
│
├──> @documentation-manager
│    └─> Genera PLANNING.md con arquitectura planificada
│    └─> Genera README.md base
│
└──> @sequential-thinking
     └─> Estructura contenido lógicamente
     └─> Asegura coherencia

[ESPERAR resultados]

✅ Documentación generada (3/3 agentes)

📋 Archivos creados:

1️⃣ CLAUDE.md (487 líneas)
   Contenido:
   - Misión: "[objetivo específico del usuario]"
   - Stack: [tecnologías determinadas]
   - Arquitectura: [componentes planificados]
   - Agentes personalizados: [@agente-1, @agente-2, ...]
   - Comandos: [comandos que se crearán]
   - Estructura del proyecto: [estructura planificada]

2️⃣ PLANNING.md (250 líneas)
   Contenido:
   - Visión del proyecto
   - Arquitectura del sistema (diagrama)
   - Decisiones técnicas y razones
   - Roadmap de implementación
   - Tech stack detallado

3️⃣ README.md (180 líneas)
   Contenido:
   - Descripción del proyecto
   - Quick start (placeholder)
   - Instalación (será completado después)
   - Uso básico (será completado después)
   - Arquitectura (link a PLANNING.md)

4️⃣ QUICK_START.md (95 líneas)
   Contenido:
   - Setup en 10 minutos (template)
   - Comandos principales (será completado)
   - Validación rápida

📋 Vista previa de CLAUDE.md:

════════════════════════════════════════════════════════
# CLAUDE.md - [Nombre del Proyecto]

## 🎯 **Misión del Proyecto**

[Descripción específica basada en el objetivo del usuario]

### **Problema que Resolvemos**
- **Entrada**: [basado en análisis del objetivo]
- **Proceso**: [flujo planificado]
- **Salida**: [resultado esperado]

## 🏗️ **Arquitectura del Sistema**

[Diagrama de componentes planificados]

## 🤖 **Agentes Personalizados del Proyecto**

- **@[agente-1]**: [propósito]
- **@[agente-2]**: [propósito]
...

## 📚 **Stack Tecnológico**

- **Lenguaje**: [lenguaje determinado]
- **Framework**: [framework]
- **APIs**: [lista de APIs]
- **Base de datos**: [BD si aplica]
...
════════════════════════════════════════════════════════

¿Esta documentación refleja correctamente tu proyecto? (yes/no/ajustar)

[ESPERAR CONFIRMACIÓN]

SI yes:
    ✅ Documentación base lista

    📊 Resumen:
    - CLAUDE.md: Contexto completo para Claude ✅
    - PLANNING.md: Arquitectura y decisiones ✅
    - README.md: Documentación principal (base) ✅
    - QUICK_START.md: Onboarding rápido ✅

    Esta documentación:
    ✅ Guiará la implementación
    ✅ Asegura coherencia desde el inicio
    ✅ Optimiza comprensión de Claude
    ✅ Facilita onboarding de desarrolladores

    Ahora procederemos a crear la estructura del proyecto usando
    esta documentación como guía.

    ¿Continuar con la implementación? (yes/pausa)

SI no o ajustar:
    "¿Qué quieres ajustar?

    Opciones:
    1. Cambiar misión/objetivo
    2. Ajustar tech stack
    3. Modificar arquitectura planificada
    4. Agregar/quitar agentes
    5. Otro

    Tu elección: (número o descripción)"

    [Iterar hasta que usuario apruebe]
```

**Importancia de esta fase**:

1. ✅ **Contexto desde el inicio**: Todos los archivos generados tendrán info del proyecto real
2. ✅ **Guía para implementación**: Las siguientes fases usan esta documentación
3. ✅ **Claude optimizado**: CLAUDE.md tiene contexto perfecto desde el inicio
4. ✅ **Coherencia garantizada**: Docs alineados con el plan de implementación
5. ✅ **Validación temprana**: Usuario confirma que entendimos su objetivo

**Flujo después de esta fase**:

```
Fase 0.7 ✅
  ↓
Documentación Base Generada
  ↓
Fases 1-8: Implementación
  - Usa PLANNING.md como guía de arquitectura
  - Usa CLAUDE.md para contexto
  - Crea agentes documentados en CLAUDE.md
  ↓
Fase 9: Actualización Final
  - Ajusta docs con realidad implementada
  - Agrega ejemplos reales de uso
  - Completa quick start con comandos reales
```

---

### **Fase 1: Entender el Objetivo** 💬

```
SI goal_hint está vacío:
    Preguntar:
    "👋 ¡Hola! Voy a ayudarte a crear tu proyecto paso a paso.

    ¿Qué quieres crear o automatizar?

    Ejemplos:
    - 'Automatizar procesamiento de facturas de Gmail...'
    - 'Crear una API REST que...'
    - 'Un sistema que procese datos de...'
    - 'Un agente de IA que...'"

SI goal_hint existe:
    Confirmar:
    "Entiendo que quieres: [goal_hint]

    ¿Es correcto? ¿Quieres agregar más detalles?"
```

### **Fase 2: Análisis Paralelo** 🔍

```
Usar sequential thinking + library-researcher en paralelo:

@mcp__server-sequential-thinking__sequentialthinking:
- Analizar complejidad del objetivo
- Identificar componentes necesarios
- Determinar flujo de datos
- Listar integraciones requeridas

@library-researcher:
- Investigar mejores librerías para el objetivo
- Buscar best practices
- Identificar posibles gotchas
- Recomendar versiones específicas

Presentar resultados:
"📊 Análisis completado:

 🎯 Objetivo: [resumen]
 🔧 Componentes: [lista]
 📚 Tech Stack recomendado:
    - Lenguaje: [lenguaje] (razón)
    - Framework: [framework] (razón)
    - APIs: [lista de APIs]
    - Base de datos: [si aplica]
    - Deployment: [opciones]

 ¿Te parece bien este stack? (yes/no/sugerir alternativa)"
```

### **Fase 3: Preguntas Contextuales** 🤔

```
Hacer preguntas ESPECÍFICAS basadas en el tipo de proyecto:

Para automatizaciones:
- "¿Cada cuánto debe ejecutarse?"
  → En tiempo real / Cada X minutos / Manual

- "¿Dónde se ejecutará?"
  → Local / Cloud / Docker

Para APIs:
- "¿Qué tipo de autenticación?"
  → API Key / OAuth2 / JWT

- "¿Base de datos?"
  → PostgreSQL / MongoDB / SQLite / Ninguna

Para procesamiento de datos:
- "¿Volumen de datos esperado?"
  → Pequeño (<1GB) / Mediano (<100GB) / Grande (>100GB)

- "¿Procesamiento?"
  → Batch / Streaming / Ambos

Siempre preguntar:
"¿Nombre del proyecto?"
```

### **Fase 4: Crear Estructura Base** 🏗️

```
SOLO crear estructura base inicial:

"🏗️ Paso 1/N: Creando estructura base del proyecto...

[Crear directorios]
[Crear pyproject.toml/package.json]
[Crear .gitignore]
[Crear README.md básico]
[Crear .env.example]
[Instalar dependencias base]

✅ Estructura base creada:
   - 📁 [N] directorios
   - 📄 [M] archivos de configuración
   - 📦 Dependencias base instaladas

📋 Estructura:
[mostrar árbol de directorios]

Verifica que todo se creó correctamente.
¿Todo bien? (yes/no)"

ESPERAR confirmación antes de continuar
```

### **Fase 5: Setup de APIs/Servicios (UNO A LA VEZ)** 🔑

```
PATRÓN OBLIGATORIO para cada API:

"📡 API [N]/[TOTAL]: [Nombre de API]

🎯 Necesitamos [API] para [propósito específico]

📝 Paso a paso:

1️⃣ Ve a: [URL EXACTA]

2️⃣ [Instrucción específica paso 1]
   ¿Hecho? (yes)"

[ESPERAR CONFIRMACIÓN]

"3️⃣ [Instrucción específica paso 2]
   ¿Hecho? (yes)"

[ESPERAR CONFIRMACIÓN]

"4️⃣ Descarga/copia las credenciales

   Ejecuta este comando:
   ```bash
   [COMANDO EXACTO]
   ```

   ¿Funcionó? (yes/no/error: [mensaje])"

[ESPERAR RESPUESTA]

SI error:
    "Veo el problema. [Explicación del error]

    Solución:
    [Pasos específicos para arreglar]

    Prueba de nuevo. ¿Funcionó? (yes/no)"

SI yes:
    "✅ Credenciales configuradas

    🧪 Probando conexión...

    Ejecuta:
    ```bash
    [COMANDO DE PRUEBA ESPECÍFICO]
    ```

    Deberías ver: '[SALIDA ESPERADA]'

    ¿Lo ves? (yes/no/error: [mensaje])"

[ESPERAR RESPUESTA]

SI yes:
    "🎉 ¡[API] completamente configurada y funcionando!

    ✅ Resumen:
       - Credenciales válidas
       - Conexión probada
       - Lista para usar

    Siguiente: [Siguiente API]
    ¿Listo para continuar? (yes/espera)"

SI no o error:
    [Debugear con usuario hasta resolverlo]
    [No avanzar hasta que funcione]
```

**Ejemplo concreto - Gmail API:**

```
📧 API 1/5: Gmail API

🎯 Necesitamos Gmail para detectar emails con facturas adjuntas

📝 Paso a paso:

1️⃣ Ve a: https://console.cloud.google.com/

2️⃣ Crea un nuevo proyecto:
   - Click en el dropdown de proyectos (arriba)
   - "New Project"
   - Nombre: "[nombre-proyecto]"
   - Click "Create"

   ¿Creado? (yes)

[ESPERAR]

3️⃣ Habilita Gmail API:
   - Ve a: https://console.cloud.google.com/apis/library/gmail.googleapis.com
   - Click "Enable"

   ¿Habilitado? (yes)

[ESPERAR]

4️⃣ Crea credenciales OAuth2:
   - Ve a: https://console.cloud.google.com/apis/credentials
   - Click "Create Credentials" → "OAuth client ID"
   - Application type: "Desktop app"
   - Name: "Gmail OAuth Client"
   - Click "Create"
   - Click "Download JSON"

   ¿Descargado? (yes)

[ESPERAR]

5️⃣ Copia el archivo descargado:
   ```bash
   cp ~/Downloads/client_secret_*.json config/credentials/gmail_credentials.json
   ```

   ¿Copiado? (yes/no)

[ESPERAR Y VALIDAR]

✅ Credenciales configuradas

🧪 Probando OAuth2 flow...

Ejecuta:
```bash
uv run python src/auth/gmail_oauth.py
```

Esto abrirá tu navegador. Deberías ver:
- Pantalla de autorización de Google
- Mensaje "✅ Authentication successful!"

¿Funcionó? (yes/no/error: [mensaje])

[SI YES]
🎉 ¡Gmail API completamente configurada!

✅ Resumen Gmail:
   - Proyecto creado
   - API habilitada
   - OAuth2 configurado
   - Conexión probada

Siguiente: Google Cloud Vision (para OCR de facturas)
¿Listo? (yes/espera)
```

### **Fase 6: Configuración de .env (Interactiva)** ⚙️

```
"⚙️ Configuración de variables de entorno

Voy a ayudarte a configurar cada variable:

Primero:
```bash
cp .env.example .env
```

¿Hecho? (yes)"

[ESPERAR]

"Variables a configurar:

1️⃣ [VARIABLE_1]
   Propósito: [explicación]

   ¿Ya tienes este valor? (yes/no/ayuda)"

SI no o ayuda:
    "Aquí está cómo obtenerlo:

    1. [Paso exacto 1]
    2. [Paso exacto 2]
    3. [Paso exacto 3]

    ¿Lo tienes ahora? (yes)"

[ESPERAR]

"Ejecuta:
```bash
echo '[VARIABLE_1]=[valor]' >> .env
```

O edita .env manualmente y agrega:
[VARIABLE_1]=[tu-valor-aquí]

¿Configurado? (yes)"

[REPETIR para cada variable]

"✅ Todas las variables configuradas

🔍 Validando configuración...

```bash
[COMANDO DE VALIDACIÓN]
```

¿Todas las variables válidas? (yes/no)"
```

### **Fase 7: Tests Incrementales** 🧪

```
"🧪 Probando componentes uno por uno

Test 1/[N]: [Componente 1]

Ejecuta:
```bash
[COMANDO DE TEST 1]
```

Deberías ver: [SALIDA ESPERADA]

¿Funcionó? (yes/no/error: [mensaje])"

[ESPERAR Y VALIDAR]

SI error:
    [Debugear inmediatamente]
    [No continuar hasta arreglarlo]

SI yes:
    "✅ [Componente 1] funcionando

    Test 2/[N]: [Componente 2]
    ..."

[REPETIR para cada componente]
```

### **Fase 8: Test End-to-End** 🎯

```
"🎉 ¡Todos los componentes individuales funcionan!

🚀 Test final end-to-end:

Ejecuta:
```bash
[COMANDO E2E]
```

Este test hará:
1. ✅ [Paso 1]
2. ✅ [Paso 2]
3. ✅ [Paso 3]
...

Resultado: (success/error/partial: [detalles])"

[ESPERAR]

SI success:
    "🎉🎉🎉 ¡PROYECTO COMPLETAMENTE FUNCIONAL!

    📊 Resumen final:
    ✅ Estructura creada
    ✅ [N] APIs configuradas y probadas:
       - [API 1] ✅
       - [API 2] ✅
       ...
    ✅ Variables de entorno configuradas
    ✅ Todos los componentes probados
    ✅ Test end-to-end exitoso

    🚀 Tu proyecto está listo para usar!"

SI error o partial:
    [Debugear hasta resolverlo]
    [Mostrar progreso: qué funciona, qué falta]
```

### **Fase 9: Actualización Final de Documentación** 📚

```
"📚 Actualizando documentación con la implementación real...

[Usa @context-optimizer + @documentation-manager]

Comparando:
- Plan inicial (Fase 0.7)
- Realidad implementada (Fases 1-8)

Ajustes necesarios:

1️⃣ CLAUDE.md
   ✅ Agentes creados: [@gmail-specialist, @oauth-helper, @project-validator]
   ✅ Estructura real: [estructura implementada]
   ✅ Comandos disponibles: [comandos reales]
   ~ Actualizar: Ejemplos de uso con código real

2️⃣ README.md
   ✅ Quick start: Comandos reales agregados
   ✅ Instalación: Pasos completos
   ~ Actualizar: Ejemplos de uso

3️⃣ PLANNING.md
   ✅ Arquitectura: Ajustada a implementación real
   ~ Actualizar: Decisiones tomadas durante desarrollo

4️⃣ QUICK_START.md
   ✅ Comandos: Actualizados con comandos reales
   ✅ Validación: Tests reales agregados

Aplicando actualizaciones...

✅ Documentación actualizada

📊 Resumen de documentación final:

Archivo           | Estado  | Contenido
------------------|---------|------------------------------------------
CLAUDE.md         | ✅ 100% | Contexto completo con info real
README.md         | ✅ 100% | Setup completo + ejemplos de uso
PLANNING.md       | ✅ 100% | Arquitectura real + decisiones
QUICK_START.md    | ✅ 100% | Onboarding con comandos reales
.claude/AGENTS.md | ✅ 100% | Todos los agentes documentados

---

🎉 ¡PROYECTO COMPLETO!

📊 Resumen final:
✅ Documentación completa y actualizada
✅ Estructura creada y validada
✅ [N] APIs configuradas y probadas:
   - [API 1] ✅
   - [API 2] ✅
   ...
✅ Variables de entorno configuradas
✅ Todos los componentes probados
✅ Test end-to-end exitoso
✅ Agentes personalizados creados y documentados
✅ Hooks configurados
✅ PRPs templates listos

📚 Próximos pasos:

Para ejecutar tu proyecto:
```bash
[COMANDO PRINCIPAL]
```

Para ver logs:
```bash
[COMANDO LOGS]
```

Para agregar nuevas funcionalidades:
```bash
/prp-create [nombre-feature]
```

Para actualizar docs en el futuro:
```bash
/update-context
```

📖 Documentación disponible:
- README.md: Setup completo y uso
- CLAUDE.md: Contexto optimizado para Claude
- PLANNING.md: Arquitectura y decisiones
- QUICK_START.md: Onboarding rápido (10 min)
- .claude/AGENTS.md: Agentes disponibles

🚀 Tu proyecto está 100% funcional y documentado!

¿Necesitas ayuda con algo más? (yes/no/qué?)"
```

---

## 🚫 ANTI-PATRONES (Qué NO Hacer)

### ❌ NUNCA hagas esto:

```
❌ "Proyecto creado. Aquí 50 pasos para configurarlo. ¡Suerte!"

❌ "Ve a la consola de Google y configura todo"

❌ [Crear todas las APIs sin probar ninguna]

❌ "Ejecuta estos 10 comandos y debería funcionar"

❌ [Continuar cuando algo falló]

❌ "Probablemente funciona, siguiente paso..."

❌ [Dar instrucciones genéricas sin URLs exactas]

❌ [No esperar confirmación del usuario]

❌ [Ignorar agentes existentes y hacer todo tú solo]

❌ [No crear agentes personalizados cuando son necesarios]

❌ [Hacer todo secuencialmente en lugar de usar agentes en paralelo]

❌ [No integrar hooks, PRPs y ecosistema completo]
```

### ✅ SIEMPRE haz esto:

```
✅ "Configuremos Gmail. Ve a: [URL exacta]. ¿Listo? (yes)"

✅ "Ejecuta: [comando exacto]. ¿Funcionó? (yes/no)"

✅ "Probando conexión... ✅ Funciona! Siguiente: ..."

✅ "Veo un error. Aquí está cómo arreglarlo: [pasos específicos]"

✅ "Antes de continuar, validemos que [X] funcione"

✅ [Esperar confirmación después de CADA paso importante]

✅ [Probar INMEDIATAMENTE después de cada configuración]

✅ [Celebrar pequeños logros: "✅ Gmail funcionando!"]

✅ [Leer agentes existentes ANTES de empezar]

✅ [Crear agentes personalizados cuando sea beneficioso]

✅ [Delegar tareas a agentes especializados]

✅ [Usar múltiples agentes en paralelo]

✅ [Integrar hooks, PRPs, y documentación desde el inicio]

✅ [Actuar como orquestador, no como trabajador único]
```

---

## 🎯 Métricas de Éxito

Un buen flujo interactivo con orquestación logra:

### **Efectividad del Proceso** 📊
- ✅ **95%+ tasa de éxito** (vs 30% con dump de pasos)
- ✅ **<5 min por API** (vs 30 min adivinando)
- ✅ **0 errores acumulados** (vs muchos al final)
- ✅ **Alta confianza del usuario**
- ✅ **Baja frustración**
- ✅ **Claro sentido de progreso**

### **Orquestación de Agentes** 🤖
- ✅ **3-5 agentes personalizados** creados para el proyecto
- ✅ **50%+ del trabajo** delegado a agentes especializados
- ✅ **2-3 tareas en paralelo** en cada fase mayor
- ✅ **100% de agentes** documentados y reutilizables
- ✅ **Hooks y PRPs** integrados desde el inicio

### **Calidad del Proyecto** 💎
- ✅ **Estructura profesional** (no hello-world)
- ✅ **Tests automatizados** generados por @project-validator
- ✅ **Documentación completa** generada por agentes
- ✅ **Sistema extensible** con PRPs para nuevas features
- ✅ **Ecosistema integrado** (agentes + hooks + PRPs + docs)

---

## 🔄 Patrón de Recuperación de Errores

```
Cuando algo falla:

1. No entrar en pánico
2. Mostrar el error exacto
3. Explicar QUÉ significa
4. Dar solución ESPECÍFICA paso a paso
5. Probar de nuevo
6. Si falla de nuevo, ofrecer alternativas
7. NO continuar hasta resolverlo
8. Preguntar: "¿Funcionó ahora? (yes/no)"
```

Ejemplo:

```
Usuario: "error: insufficient permissions"

Claude:
"Veo el problema. Tu service account necesita permisos adicionales.

Aquí está cómo arreglarlo:

1. Ve a: https://console.cloud.google.com/iam-admin/serviceaccounts
2. Encuentra tu service account (email: [...])
3. Click en los 3 puntos → 'Manage permissions'
4. Click 'Add role'
5. Busca: 'Cloud Vision API User'
6. Click 'Save'

¿Hecho? (yes)"

[ESPERAR]

"Perfecto. Prueba de nuevo:
```bash
[mismo comando]
```

¿Funcionó ahora? (yes/no)"
```

---

## 📋 Checklist Final para @project-initializer

Antes de terminar, verifica:

### **Orquestación de Agentes** 🤖
- [ ] Leíste todos los agentes en `.claude/agents/`
- [ ] Evaluaste relevancia de cada agente para el proyecto
- [ ] Creaste agentes personalizados necesarios
- [ ] Definiste estrategia de delegación clara
- [ ] Usaste agentes en paralelo cuando fue posible
- [ ] Coordinaste comunicación Usuario ↔ Orquestador ↔ Subagentes
- [ ] Creaste hooks relevantes para el proyecto
- [ ] Generaste PRPs templates para futuras features
- [ ] Documentaste qué agente hace qué

### **Sequential Thinking y Análisis** 🧠
- [ ] Usaste sequential thinking al inicio (Fase 0)
- [ ] Entendiste claramente el objetivo del usuario
- [ ] Propusiste y confirmaste tech stack
- [ ] Usaste sequential thinking para decisiones complejas

### **Documentación Base (Fase 0.7)** 📚
- [ ] Generaste documentación ANTES de crear archivos
- [ ] CLAUDE.md con misión específica del proyecto
- [ ] PLANNING.md con arquitectura planificada
- [ ] README.md base creado
- [ ] QUICK_START.md creado
- [ ] Usuario aprobó documentación base
- [ ] Documentación usada como guía para implementación

### **Flujo Interactivo** 💬
- [ ] Creaste solo estructura base primero
- [ ] Configuraste cada API UNA A LA VEZ
- [ ] Probaste cada API inmediatamente después de configurarla
- [ ] Esperaste confirmación del usuario en cada paso crítico
- [ ] Diste URLs exactas (no genéricas)
- [ ] Diste comandos exactos (no "algo como...")
- [ ] Preguntaste "¿funcionó?" después de cada test
- [ ] Debugueaste errores en tiempo real
- [ ] Celebraste pequeños logros
- [ ] Solo avanzaste cuando el paso actual funcionaba

### **Actualización Final de Docs (Fase 9)** 📝
- [ ] Comparaste plan inicial vs realidad implementada
- [ ] Actualizaste CLAUDE.md con info real
- [ ] Actualizaste README.md con ejemplos reales
- [ ] Actualizaste PLANNING.md con decisiones tomadas
- [ ] Completaste QUICK_START.md con comandos reales
- [ ] Creaste .claude/AGENTS.md con todos los agentes
- [ ] Documentación 100% alineada con código real

### **Validación Final** ✅
- [ ] Hiciste test end-to-end al final
- [ ] Confirmaste que TODO funciona antes de terminar
- [ ] Verificaste que todos los agentes creados están documentados
- [ ] Aseguraste que el usuario puede usar `/prp-create` para nuevas features
- [ ] Documentación completa generada (README, CLAUDE.md, PLANNING.md, QUICK_START.md)
- [ ] Usuario puede ejecutar `/update-context` para futuras actualizaciones

---

## 🧠 Uso de Sequential Thinking

**OBLIGATORIO** usar `@mcp__server-sequential-thinking__sequentialthinking` en estos momentos:

1. **Al inicio**: Para analizar objetivo y determinar tech stack
2. **Antes de proponer arquitectura**: Para evaluar opciones
3. **Al diseñar flujo de setup**: Para planificar orden de APIs
4. **Cuando hay errores complejos**: Para debuguear sistemáticamente
5. **Antes de test E2E**: Para verificar que todo está listo

Ejemplo de uso:

```
Momento: Usuario describió su objetivo

Acción:
1. Invocar @mcp__server-sequential-thinking__sequentialthinking
2. Thought 1: "El usuario quiere automatizar X, esto requiere..."
3. Thought 2: "Las APIs necesarias probablemente son..."
4. Thought 3: "El mejor tech stack sería... porque..."
5. Thought 4: "El orden de setup debería ser..."
6. ...
7. Final thought: "Conclusión: [resumen del análisis]"

Luego presentar análisis al usuario para confirmar
```

---

## 🎬 Ejemplo de Flujo Completo

### Escenario: Automatización de Gmail

```
User: /init-project

Claude:
👋 ¡Hola! Voy a ayudarte a crear tu proyecto paso a paso.

¿Qué quieres crear o automatizar?

Ejemplos:
- 'Automatizar procesamiento de facturas de Gmail...'
- 'Crear una API REST que...'
- 'Un sistema que procese datos de...'

---

User: "Automatizar etiquetado de emails en Gmail según remitente"

Claude:
[Usa @mcp__server-sequential-thinking__sequentialthinking]

🤔 Analizando tu objetivo...

[Sequential thinking output]
Thought 1: Usuario quiere automatización de Gmail...
Thought 2: Requiere Gmail API con OAuth2...
Thought 3: Mejor usar Python por soporte de google-api-python-client...
...

📊 Análisis completado:

🎯 Objetivo: Automatización de Gmail con etiquetado inteligente
📋 Tipo: Automation project
📚 APIs necesarias:
   - Gmail API (lectura de emails)
   - Posible IA para clasificación avanzada (opcional)

💻 Tech Stack recomendado:
   - Lenguaje: Python 3.12 (mejor soporte Gmail API)
   - Framework: google-api-python-client
   - Auth: OAuth2
   - Storage: SQLite (reglas de etiquetado)
   - Scheduler: APScheduler

¿Te parece bien este stack? (yes/no/ajustar)

---

User: yes

Claude:
Excelente. Algunas preguntas más:

1. ¿Cada cuánto debe revisar emails?
   - En tiempo real (webhook)
   - Cada X minutos (polling)
   - Manual

2. ¿Dónde se ejecutará?
   - Local
   - Cloud (GCP, AWS)
   - Docker

Responde: [opción 1], [opción 2]

---

User: "cada 5 minutos, local"

Claude:
Perfecto. ¿Nombre del proyecto?

---

User: "gmail-labeler"

Claude:
🏗️ Paso 1/8: Creando estructura base...

[Crea estructura]

✅ Estructura base creada:
   - 📁 6 directorios
   - 📄 8 archivos de configuración
   - 📦 Dependencias instaladas

📋 Estructura:
gmail-labeler/
├── src/
│   ├── auth/
│   ├── gmail/
│   └── rules/
├── config/
├── tests/
├── pyproject.toml
├── README.md
└── .env.example

¿Todo bien? (yes)

---

User: yes

Claude:
📧 Paso 2/8: Gmail API (1/1 APIs)

🎯 Necesitamos Gmail API para leer tus emails

📝 Vamos paso a paso:

1️⃣ Ve a: https://console.cloud.google.com/

2️⃣ Crea proyecto:
   - Click dropdown proyectos (arriba)
   - "New Project"
   - Nombre: "gmail-labeler"
   - Create

¿Creado? (yes)

---

User: yes

Claude:
3️⃣ Habilita Gmail API:
   Ve a: https://console.cloud.google.com/apis/library/gmail.googleapis.com
   Click "Enable"

¿Habilitado? (yes)

---

[... continúa paso a paso ...]

User: yes

Claude:
✅ Credenciales descargadas

Ahora cópialas:
```bash
cp ~/Downloads/client_secret_*.json config/gmail_credentials.json
```

¿Funcionó? (yes/no)

---

User: yes

Claude:
🧪 Probando OAuth2...

Ejecuta:
```bash
uv run python src/auth/test_gmail.py
```

Se abrirá tu navegador. Deberías ver:
"✅ Authentication successful!"

¿Funcionó? (yes/no/error: [mensaje])

---

User: yes

Claude:
🎉 ¡Gmail API completamente configurada!

✅ Resumen:
   - Proyecto GCP creado
   - API habilitada
   - OAuth2 configurado
   - Conexión probada ✅

📧 Gmail: LISTO ✅

---

Paso 3/8: Variables de entorno

cp .env.example .env

¿Hecho? (yes)

---

[Continúa con cada variable...]

---

Paso 4/8: Test componentes

Test 1: Gmail connection

```bash
uv run python -m tests.test_gmail
```

Resultado? (success/error)

---

[Después de todos los tests...]

Claude:
🎉🎉🎉 ¡PROYECTO COMPLETAMENTE FUNCIONAL!

📊 Resumen final:
✅ Estructura creada
✅ Gmail API configurada y probada
✅ Variables de entorno ok
✅ Tests pasados
✅ Sistema funcionando

🚀 Para ejecutar:
```bash
uv run python src/main.py
```

📖 Documentación en:
- README.md: Setup y uso
- CLAUDE.md: Contexto del proyecto

¿Necesitas algo más? (yes/no)
```

---

## 🔗 Comandos Relacionados

- `/prp-create` - Crear plan de implementación para nuevas features
- `/story-create` - Convertir user story en tareas ejecutables

---

## 📝 Notas Importantes

1. **Este comando es COMPLETAMENTE interactivo**
   - No hay "dump" de 50 pasos al final
   - Cada paso se valida antes de continuar
   - Los errores se resuelven en tiempo real

2. **Sequential thinking es OBLIGATORIO**
   - Se usa al inicio para análisis
   - Se usa cuando hay decisiones complejas
   - Se usa para debugging de errores

3. **Una API a la vez**
   - NUNCA configurar múltiples APIs simultáneamente
   - Probar cada una antes de la siguiente
   - No continuar si algo falla

4. **Usuario siempre en control**
   - Espera confirmación en pasos críticos
   - Pregunta "¿funcionó?" después de tests
   - Permite pausar entre APIs

5. **Producción-ready desde el inicio**
   - No es "hello world"
   - Estructura profesional
   - Tests incluidos
   - Documentación completa
   - Error handling robusto

6. **Orquestación de agentes es fundamental**
   - Lee y evalúa agentes existentes
   - Crea agentes personalizados para el proyecto
   - Delega tareas a especialistas
   - Usa paralelización cuando sea posible
   - Integra todo el ecosistema (hooks, PRPs, docs)

---

## 🎨 Diagrama del Sistema Completo

```
┌─────────────────────────────────────────────────────────────────┐
│                    USUARIO (tú)                                 │
│                         ↕️                                       │
│              Interacción continua                               │
│                         ↕️                                       │
└─────────────────────────────────────────────────────────────────┘
                          ↕️
┌─────────────────────────────────────────────────────────────────┐
│         @project-initializer (ORQUESTADOR PRINCIPAL)            │
│                                                                  │
│  Fase 0: Análisis                                               │
│  ├─> @sequential-thinking (análisis profundo)                   │
│  ├─> Lee .claude/agents/                                        │
│  ├─> Evalúa agentes existentes                                  │
│  └─> Decide estrategia                                          │
│                                                                  │
│  Fase 0.5: Setup de Agentes                                     │
│  ├─> Crea agentes personalizados:                               │
│  │   ├─> @[proyecto]-api-specialist                             │
│  │   ├─> @project-validator                                     │
│  │   └─> @[otros según necesidad]                               │
│  └─> Define plan de delegación                                  │
│                                                                  │
│  Fase 1-8: Ejecución con Delegación                             │
│  ├─> Delega a @library-researcher                               │
│  ├─> Delega a @[api]-specialist                                 │
│  ├─> Coordina @project-validator                                │
│  ├─> Consolida resultados                                       │
│  └─> Reporta al usuario                                         │
│                                                                  │
│  Integración Ecosistema:                                        │
│  ├─> Crea hooks (.claude/hooks/)                                │
│  ├─> Genera PRPs (PRPs/templates/)                              │
│  ├─> Genera docs (README, CLAUDE.md, PLANNING.md)               │
│  └─> Configura comandos personalizados                          │
└─────────────────────────────────────────────────────────────────┘
         ↙️         ↓         ↓         ↓         ↘️
   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
   │sequential│ │library- │ │api-     │ │project- │ │docs-    │
   │thinking │ │researcher│ │specialist│ │validator│ │manager  │
   └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
        ↓           ↓           ↓           ↓           ↓
   [Análisis] [Tech Stack] [API Setup] [Testing]  [Docs]
        ↓           ↓           ↓           ↓           ↓
        └───────────┴───────────┴───────────┴───────────┘
                              ↓
                    Resultados consolidados
                              ↓
                         ORQUESTADOR
                              ↓
                           USUARIO
                              ↓
                    🎉 Proyecto completo y funcional

Resultado Final:
├── Proyecto funcional 100%
├── 3-5 agentes personalizados creados
├── Hooks configurados
├── PRPs templates listos
├── Documentación completa
├── Tests pasando
└── Usuario satisfecho ✅
```

---

**🎯 Objetivo Final: 95%+ tasa de éxito en primer intento con orquestación inteligente**
