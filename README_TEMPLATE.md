# 🚀 Plantilla Universal de Claude Code

> **Plantilla profesional para iniciar proyectos con Claude Code** - Incluye agentes, comandos, documentación y best practices

Esta es una plantilla **lista para usar** que incluye toda la configuración necesaria para trabajar eficientemente con Claude Code en cualquier tipo de proyecto.

---

## 🎯 ¿Qué es esto?

Una plantilla **battle-tested** que incluye:
- ✅ **Agentes especializados** (@codebase-analyst, @library-researcher)
- ✅ **Sistema PRP** (Pattern Recognition Protocol) para features complejos
- ✅ **Comandos personalizados** (/prp-create, /prp-execute, /story-create, /story-execute)
- ✅ **Documentación estructurada** (CLAUDE.md, PLANNING.md, TASK.md)
- ✅ **Hooks configurables** para automatización
- ✅ **Best practices** probadas en proyectos reales

---

## 📦 ¿Qué incluye?

```
claude-code-template/
├── .claude/                      # Configuración Claude Code
│   ├── agents/                   # Agentes especializados (inglés)
│   │   ├── codebase-analyst.md   # Analiza patrones del código
│   │   ├── library-researcher.md # Investiga librerías externas
│   │   └── project-initializer.md # 🆕 Inicializa proyectos goal-oriented
│   │
│   ├── commands/                 # Comandos personalizados
│   │   ├── prp/                  # Sistema PRP
│   │   │   ├── prp-claude-code-create.md
│   │   │   ├── prp-claude-code-execute.md
│   │   │   ├── prp-story-task-create.md
│   │   │   └── prp-story-task-execute.md
│   │   ├── init-project.md       # 🆕 Comando inicialización
│   │   └── continue-restructure.md # Continuar PRPs
│   │
│   ├── hooks/                    # Hooks para automatización
│   │   └── README.md
│   │
│   ├── PLANNING.md               # Template arquitectura (español)
│   ├── TASK.md                   # Template tareas (español)
│   └── settings.local.json       # Configuración + MCP servers
│
├── docs/                         # 🆕 Documentación adicional
│   ├── SERENA_MCP.md            # 🆕 Guía Serena MCP (español)
│   ├── FLUJO_INICIALIZACION.md  # 🆕 Flujo inicialización (español)
│   ├── MCP_TOOLS_GUIA.md        # 🆕 Guía MCP tools (español)
│   └── ejemplos/                 # 🆕 Ejemplos por tipo proyecto
│       ├── ejemplo_python.md     # Setup Python (UV, pytest, ruff)
│       ├── ejemplo_nodejs.md     # Setup Node.js (pnpm, Jest, ESLint)
│       └── ejemplo_general.md    # Personalización general
│
├── PRPs/                         # Pattern Recognition Protocols
│   ├── templates/                # Plantillas base
│   │   ├── prp_tecnico_base.md  # 🆕 Template técnico genérico (español)
│   │   └── prp_story_task.md    # 🔄 Traducido a español
│   ├── completed/                # PRPs completados (usuario)
│   └── ai_docs/                  # Docs curadas (usuario)
│
├── .mcp.json                     # 🆕 Configuración MCP servers (Serena)
├── CLAUDE.md                     # Documento maestro (template español)
├── README.md                     # README del proyecto (template español)
├── QUICK_START.md                # Guía inicio rápido (template español)
├── GUIA_CLAUDECODE.md            # Guía completa Claude Code
├── .gitignore                    # Gitignore completo
└── README_TEMPLATE.md            # Este archivo
```

---

## 🌐 Estrategia Bilingüe

Esta plantilla usa una estrategia bilingüe inteligente:

- **🇬🇧 Inglés**: Componentes técnicos (agents, commands)
  - Mejor compatibilidad con Claude Code ecosystem
  - Terminología técnica más clara
  - Reutilización de código internacional

- **🇪🇸 Español**: Documentación usuario (CLAUDE.md, README.md, templates)
  - Documentación accesible para equipos hispanohablantes
  - Templates y ejemplos en español
  - Guías y tutoriales localizados

**¿Por qué esta estrategia?**
- Claude Code funciona mejor con componentes técnicos en inglés
- La documentación en español facilita el onboarding y mantenimiento
- Los templates PRP en español son más intuitivos para el día a día

---

## 🆕 Sistema de Inicialización Inteligente

La plantilla incluye un sistema de inicialización goal-oriented que entiende tu objetivo en lenguaje natural:

### **Comando /init-project**

```bash
# Solo dile a Claude qué quieres hacer:
/init-project "Quiero crear una API REST con FastAPI y PostgreSQL"

# O sin especificar (Claude te preguntará):
/init-project
```

**Qué hace:**
1. 🎯 **Entiende tu objetivo** en lenguaje natural
2. 🔍 **Investiga** mejores tecnologías (sequential-thinking + library-researcher)
3. 💡 **Determina tech stack** apropiado para tu caso
4. ❓ **Hace preguntas inteligentes** contextuales (NO genéricas)
5. 📚 **Investiga best practices** actualizadas
6. 🏗️ **Crea estructura** completa con código funcional
7. ✅ **Valida** y guía setup paso a paso

**Ejemplo de flujo:**
```
Usuario: /init-project "API para gestión de inventario con autenticación"

Claude:
  → Entiendo: API REST + Auth + Inventario
  → Investigo: FastAPI vs Express, Auth patterns, DB apropiada
  → Determino: FastAPI + JWT + PostgreSQL + SQLAlchemy
  → Pregunto: ¿Necesitas multi-tenancy? ¿Roles de usuario?
  → Investigo: Best practices FastAPI 2025, JWT refresh tokens
  → Creo: Estructura + modelos + auth + endpoints + tests
  → Configuro: UV, pytest, ruff, mypy, pre-commit
  → Valido: Tests pasan, linting OK, servidor levanta
```

**Setup APIs UNO A LA VEZ** - No dump de 50 pasos al final ✅

---

## 🚀 Cómo Usar Esta Plantilla

### **Opción 1: Copiar para Nuevo Proyecto**

```bash
# 1. Copiar la plantilla a tu nuevo proyecto
cp -r claude-code-template/ /ruta/a/tu-nuevo-proyecto/.

# 2. Ir a tu nuevo proyecto
cd /ruta/a/tu-nuevo-proyecto

# 3. Personalizar archivos (ver sección "Personalización")
# Editar: CLAUDE.md, README.md, QUICK_START.md

# 4. Inicializar git (si es nuevo proyecto)
git init
git add .
git commit -m "Initial commit con plantilla Claude Code"

# 5. ¡Empezar a desarrollar con Claude Code!
```

### **Opción 2: Agregar a Proyecto Existente**

```bash
# 1. Copiar solo la carpeta .claude
cp -r claude-code-template/.claude /ruta/a/proyecto-existente/

# 2. Copiar carpeta PRPs
cp -r claude-code-template/PRPs /ruta/a/proyecto-existente/

# 3. Copiar archivos .md (opcional)
cp claude-code-template/CLAUDE.md /ruta/a/proyecto-existente/
cp claude-code-template/QUICK_START.md /ruta/a/proyecto-existente/

# 4. Actualizar .gitignore (merge con el existente)
cat claude-code-template/.gitignore >> /ruta/a/proyecto-existente/.gitignore

# 5. Personalizar archivos para tu proyecto
```

---

## ✏️ Personalización Paso a Paso

### **1. CLAUDE.md - Documento Maestro**

Edita `CLAUDE.md` y reemplaza todos los placeholders:

- `[NOMBRE_DEL_PROYECTO]` → Nombre de tu proyecto
- `[DESCRIBE AQUÍ...]` → Descripción de tu proyecto
- `[comando-dev]` → Tus comandos específicos
- `[API_KEY_1]` → Tus variables de entorno
- Etc.

**Tiempo estimado:** 15-20 minutos

### **2. README.md - Documentación Principal**

Edita `README.md`:

- `[Nombre del Proyecto]` → Tu nombre
- `[Breve descripción...]` → Tu descripción
- Actualiza secciones de instalación, uso, etc.

**Tiempo estimado:** 10-15 minutos

### **3. QUICK_START.md - Guía Rápida**

Edita `QUICK_START.md`:

- Actualiza comandos de setup
- Personaliza pasos de inicio
- Ajusta troubleshooting común

**Tiempo estimado:** 5-10 minutos

### **4. .claude/PLANNING.md - Arquitectura**

Edita `.claude/PLANNING.md`:

- Define tu arquitectura
- Documenta componentes
- Establece roadmap

**Tiempo estimado:** 20-30 minutos

### **5. .claude/TASK.md - Tareas**

Edita `.claude/TASK.md`:

- Lista tus tareas iniciales
- Define hitos
- Establece métricas

**Tiempo estimado:** 10-15 minutos

---

## 📚 Documentación Adicional en docs/

La plantilla incluye guías completas en español en el directorio `docs/`:

### **docs/SERENA_MCP.md**
Guía completa de Serena MCP - análisis semántico de código:
- 🔍 Buscar símbolos (find_symbol)
- 📊 Ver estructura (get_symbols_overview)
- 🔗 Encontrar referencias (find_referencing_symbols)
- 🔄 Reemplazar código (replace_symbol_body)
- 🔎 Buscar patrones (search_for_pattern)

**Cuándo usar:** Para navegación y edición inteligente de código

### **docs/FLUJO_INICIALIZACION.md**
Flujo completo de inicialización interactiva:
- Setup de APIs ONE AT A TIME (no batch)
- Patrón: Explicar → Guiar → Validar → Test → Confirmar → Next
- Ejemplos de flujo Python y Node.js

**Cuándo usar:** Para entender cómo funciona /init-project

### **docs/MCP_TOOLS_GUIA.md**
Guía de todas las herramientas MCP disponibles:
- 🔍 **Perplexity Ask**: Investigación actualizada
- 🌐 **Tavily Search/Extract/Crawl**: Búsqueda web avanzada
- 💾 **Server Filesystem**: Operaciones de archivos
- 🧠 **Sequential Thinking**: Razonamiento paso a paso
- 🐙 **GitHub Integration**: Operaciones con repos
- 🎥 **YouTube Subtitles**: Extraer subtítulos

**Cuándo usar:** Para investigar tecnologías, buscar docs, analizar repos

### **docs/ejemplos/**

#### **ejemplo_python.md**
Setup completo proyecto Python:
- Gestores: UV (recomendado), Poetry, pip
- Testing: pytest + coverage
- Linting: ruff
- Type checking: mypy
- Estructura recomendada
- Comandos clave

#### **ejemplo_nodejs.md**
Setup completo proyecto Node.js/TypeScript:
- Gestores: pnpm (recomendado), npm, yarn
- Testing: Jest
- Linting: ESLint
- Formatting: Prettier
- Validación: Zod
- TypeScript config

#### **ejemplo_general.md**
Personalización para cualquier proyecto:
- Cómo personalizar CLAUDE.md
- Cómo crear agentes custom
- Cómo crear comandos custom
- Cómo usar PRPs
- Workflow completo

**Cuándo usar:** Cuando inicies un proyecto nuevo o quieras personalizar el template

---

## 🤖 Agentes Incluidos

### **@codebase-analyst**
**Qué hace:** Analiza tu código, encuentra patrones, entiende la arquitectura

**Cuándo usarlo:**
- Necesitas entender cómo funciona algo en el código
- Quieres encontrar ejemplos similares
- Buscas patrones de implementación

**Ejemplo:**
```
"@codebase-analyst explica cómo se manejan errores en el módulo de autenticación"
```

---

### **@library-researcher**
**Qué hace:** Investiga documentación de librerías externas, busca best practices

**Cuándo usarlo:**
- Vas a integrar una nueva librería
- Necesitas ejemplos de uso
- Quieres entender API externa

**Ejemplo:**
```
"@library-researcher busca documentación de FastAPI async patterns"
```

---

## ⚡ Comandos Incluidos

### **Sistema PRP (Pattern Recognition Protocol)**

#### **/prp-create [funcionalidad]**
Crea un PRP técnico para implementar una funcionalidad compleja.

**Cuándo usar:**
- Vas a implementar un feature complejo
- Necesitas planificar antes de codear
- Quieres mantener consistencia con el codebase

**Ejemplo:**
```
/prp-create autenticacion-jwt
```

**Resultado:** Genera `PRPs/prp_autenticacion-jwt.md` con plan detallado

---

#### **/prp-execute PRPs/archivo.md**
Ejecuta un PRP técnico generado previamente.

**Cuándo usar:**
- Ya tienes un PRP creado
- Quieres implementar según el plan
- Necesitas validación paso a paso

**Ejemplo:**
```
/prp-execute PRPs/prp_autenticacion-jwt.md
```

---

#### **/story-create "historia de usuario"**
Convierte una historia de usuario en un PRP ejecutable.

**Cuándo usar:**
- Recibes una historia de usuario o tarea
- Necesitas descomponerla en tareas técnicas
- Quieres análisis de impacto en el codebase

**Ejemplo:**
```
/story-create "Como usuario quiero poder resetear mi contraseña via email"
```

**Resultado:** Genera `PRPs/story_reset-password.md`

---

#### **/story-execute PRPs/story_archivo.md**
Ejecuta un Story PRP generado.

**Ejemplo:**
```
/story-execute PRPs/story_reset-password.md
```

---

## 📚 Flujo de Trabajo Recomendado

### **Para Features Nuevos**

```
1. Recibir requerimiento
   ↓
2. /story-create "descripción del requerimiento"
   → Claude analiza codebase y genera plan
   ↓
3. Revisar PRPs/story_*.md generado
   → Ajustar si es necesario
   ↓
4. /story-execute PRPs/story_*.md
   → Claude implementa paso a paso
   ↓
5. Testing manual desde tu entorno
```

### **Para Implementaciones Técnicas**

```
1. Identificar necesidad técnica
   ↓
2. /prp-create nombre-funcionalidad
   → Claude investiga y planea
   ↓
3. Revisar PRPs/prp_*.md
   → Validar approach técnico
   ↓
4. /prp-execute PRPs/prp_*.md
   → Implementación con validación
```

---

## 🎓 Best Practices

### **1. Mantén CLAUDE.md Actualizado**
Es el "cerebro" del proyecto. Claude lo lee al inicio de cada conversación.

```bash
# Actualizar después de cambios importantes:
- Nueva arquitectura
- Cambios en comandos
- Lecciones aprendidas
- Issues resueltos
```

### **2. Usa Agentes Proactivamente**
No esperes a estar bloqueado. Úsalos para investigar antes de implementar.

```bash
# Antes de implementar:
"@library-researcher busca best practices de [tecnología]"
"@codebase-analyst muestra implementaciones similares"
```

### **3. Documenta en TASK.md Regularmente**
Mantén un log de lo que haces. Es valioso para:
- Recordar decisiones
- Onboarding de nuevos devs
- Reportes de progreso

### **4. Guarda Docs de Librerías en ai_docs/**
Cuando investigues algo, guárdalo:

```bash
"@library-researcher busca docs de X y guárdalas en PRPs/ai_docs/"
```

---

## 🔧 Personalización Avanzada

### **Agregar Nuevos Agentes**

1. Crear archivo en `.claude/agents/nuevo-agente.md`
2. Seguir estructura de agentes existentes
3. Documentar en CLAUDE.md

### **Agregar Nuevos Comandos**

1. Crear archivo en `.claude/commands/nuevo-comando.md`
2. Seguir formato de comandos PRP
3. Actualizar `.claude/settings.local.json`

### **Configurar Hooks**

1. Editar `.claude/settings.local.json`
2. Crear scripts en `.claude/hooks/`
3. Probar manualmente antes de activar

---

## 📊 Métricas de Éxito

Después de usar esta plantilla, deberías ver:

- ⚡ **50-70% menos tiempo** en onboarding de nuevos features
- 📉 **Reducción de bugs** por seguir patrones consistentes
- 📚 **Documentación automática** actualizada
- 🎯 **Mayor consistency** en el codebase
- 🚀 **Desarrollo más rápido** con comandos y agentes

---

## 🆘 Troubleshooting

### **Claude no reconoce los agentes**
```bash
# Verificar que .claude/agents/ existe y tiene los .md
ls -la .claude/agents/

# Reiniciar Claude Code (cerrar y abrir)
```

### **Comandos /prp-* no funcionan**
```bash
# Verificar que .claude/commands/prp/ existe
ls -la .claude/commands/prp/

# Verificar settings.local.json
cat .claude/settings.local.json
```

### **Claude no lee CLAUDE.md automáticamente**
```bash
# Pedirle explícitamente:
"Lee CLAUDE.md y familiarízate con el proyecto"
```

### **Serena MCP no funciona**
```bash
# Verificar configuración MCP
cat .mcp.json

# Verificar que enableAllProjectMcpServers está en true
cat .claude/settings.local.json | grep enableAllProjectMcpServers

# Verificar que Serena está instalado
uvx --from git+https://github.com/oraios/serena serena --version

# Reiniciar Claude Code
```

### **Comando /init-project no funciona**
```bash
# Verificar que existe el agente
test -f .claude/agents/project-initializer.md && echo "✅ Existe" || echo "❌ No existe"

# Verificar que existe el comando
test -f .claude/commands/init-project.md && echo "✅ Existe" || echo "❌ No existe"

# Reiniciar Claude Code
```

---

## 🌟 Proyectos de Ejemplo

Esta plantilla ha sido usada exitosamente en:

- **Sistemas de automatización empresarial**: Proyectos complejos con múltiples fases
- **APIs REST con FastAPI/Express**: Inicialización y desarrollo rápido
- **Aplicaciones full-stack**: Con frontend y backend coordinados
- **[Tu proyecto aquí]**: [Comparte tus resultados]

---

## 🤝 Contribuir

¿Mejoras a la plantilla? ¡Bienvenidas!

1. Haz tus cambios
2. Documenta qué mejoraste
3. Comparte con el equipo

---

## 📄 Licencia

Esta plantilla es de uso libre. Úsala, modifícala, compártela.

---

## 📚 Recursos Adicionales

- [Documentación Oficial de Claude Code](https://docs.claude.com/claude-code)
- [Best Practices Claude Code 2024](https://medium.com/@terrycho/best-practices-for-maximizing-claude-code-performance)
- [Pattern Recognition Protocol (PRP)](https://github.com/Cole-Medin/context-engineering-intro)

---

## ✅ Checklist de Setup

Después de copiar la plantilla, verifica:

- [ ] CLAUDE.md personalizado con tu proyecto
- [ ] README.md actualizado
- [ ] QUICK_START.md con tus comandos
- [ ] .claude/PLANNING.md con tu arquitectura
- [ ] .claude/TASK.md con tus tareas iniciales
- [ ] .gitignore revisado
- [ ] Agentes funcionando (@codebase-analyst, @library-researcher)
- [ ] Comandos funcionando (/prp-create, /prp-execute)
- [ ] Primera conversación con Claude: "Lee CLAUDE.md"

---

**¡Listo! Ahora tienes un proyecto profesionalmente configurado para Claude Code** 🚀

---

*Plantilla universal para Claude Code*
*Última actualización: Octubre 2025*
*Versión: 2.0.0*
*Estrategia bilingüe: 🇬🇧 Componentes técnicos / 🇪🇸 Documentación usuario*
