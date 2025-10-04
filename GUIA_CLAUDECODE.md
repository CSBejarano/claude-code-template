# 🚀 Guía Completa de Uso de Claude Code

¡Todo lo que necesitas saber para dominar la construcción de cualquier cosa con Claude Code! Esta guía te lleva desde la instalación hasta ingeniería de contexto avanzada, subagentes, hooks y flujos de trabajo de agentes paralelos.

## 📋 Requisitos Previos

- Acceso a Terminal/Línea de comandos
- Node.js instalado (para instalación de Claude Code)
- Cuenta de GitHub (para integración con GitHub CLI)
- Editor de texto (VS Code recomendado)

## 🔧 Instalación

**macOS/Linux:**
```bash
npm install -g @anthropic-ai/claude-code
```

**Windows (WSL recomendado):**
Ver instrucciones detalladas en [install_claude_code_windows.md](./install_claude_code_windows.md)

**Verificar instalación:**
```bash
claude --version
```

---

## ✅ CONSEJO 1: CREAR Y OPTIMIZAR ARCHIVOS CLAUDE.md

Configura archivos de contexto que Claude automáticamente carga en cada conversación, conteniendo información específica del proyecto, comandos y directrices.

```bash
mkdir nombre-de-tu-carpeta && cd nombre-de-tu-carpeta
claude
```

Usa el comando integrado:
```
/init
```

O crea tu propio archivo CLAUDE.md basado en la plantilla de este repositorio. Ver `CLAUDE.md` para un ejemplo de estructura específica para Python que incluye:
- Reglas de contexto y conciencia del proyecto
- Directrices de estructura de código
- Requisitos de testing
- Flujo de trabajo de completación de tareas
- Convenciones de estilo
- Estándares de documentación

### Técnicas Avanzadas de Prompting

**Palabras Clave Poderosas**: Claude responde a ciertas palabras clave con comportamiento mejorado (palabras clave densas en información):
- **IMPORTANT**: Enfatiza instrucciones críticas que no deben pasarse por alto
- **Proactively**: Anima a Claude a tomar la iniciativa y sugerir mejoras
- **Ultra-think**: Puede activar un análisis más exhaustivo (usar con moderación)

**Consejos Esenciales de Ingeniería de Prompts**:
- Evita solicitar código "listo para producción" - esto a menudo lleva a sobre-ingeniería
- Solicita a Claude que escriba scripts para verificar su trabajo: "Después de implementar, crea un script de validación"
- Evita compatibilidad hacia atrás a menos que sea específicamente necesaria - Claude tiende a preservar código antiguo innecesariamente
- Enfócate en claridad y requisitos específicos en lugar de descriptores de calidad vagos

### Estrategias de Ubicación de Archivos

Claude automáticamente lee archivos CLAUDE.md desde múltiples ubicaciones:

```bash
# Raíz del repositorio (más común)
./CLAUDE.md              # Incluido en git, compartido con el equipo
./CLAUDE.local.md        # Solo local, agregar a .gitignore

# Directorios padres (para monorepos)
root/CLAUDE.md           # Información general del proyecto
root/frontend/CLAUDE.md  # Contexto específico del frontend
root/backend/CLAUDE.md   # Contexto específico del backend

# Referenciar archivos externos para flexibilidad
echo "Seguir mejores prácticas en: ~/company/engineering-standards.md" > CLAUDE.md
```

**Consejo Pro**: Muchos equipos mantienen su CLAUDE.md mínimo y referencian un documento de estándares compartido. Esto facilita:
- Cambiar entre asistentes de IA para codificación
- Actualizar estándares sin cambiar cada proyecto
- Compartir mejores prácticas entre equipos

*Nota: Mientras Claude Code lee CLAUDE.md automáticamente, otros asistentes de IA pueden usar archivos de contexto similares (como .cursorrules para Cursor)*

---

## ✅ CONSEJO 2: CONFIGURAR GESTIÓN DE PERMISOS

Configura listas de permitidos de herramientas para agilizar el desarrollo mientras mantienes la seguridad para operaciones de archivos y comandos del sistema.

**Método 1: Lista de Permitidos Interactiva**
Cuando Claude solicite permiso, selecciona "Siempre permitir" para operaciones comunes.

**Método 2: Usar comando /permissions**
```
/permissions
```
Luego agrega:
- `Edit` (para ediciones de archivos)
- `Bash(git commit:*)` (para commits de git)
- `Bash(npm:*)` (para comandos npm)
- `Read` (para leer archivos)
- `Write` (para crear archivos)

**Método 3: Crear archivo de configuración del proyecto**
Crear `.claude/settings.local.json`:
```json
{
  "allowedTools": [
    "Edit",
    "Read",
    "Write",
    "Bash(git add:*)",
    "Bash(git commit:*)",
    "Bash(npm:*)",
    "Bash(python:*)",
    "Bash(pytest:*)"
  ]
}
```

**Mejores Prácticas de Seguridad**:
- Nunca permitir `Bash(rm -rf:*)` o comandos destructivos similares
- Usar patrones de comandos específicos en lugar de `Bash(*)`
- Revisar permisos regularmente
- Usar diferentes conjuntos de permisos para diferentes proyectos

*Nota: Todos los asistentes de IA para codificación tienen gestión de permisos - algunos integrados, otros requieren aprobación manual para cada acción.*

---

## ✅ CONSEJO 3: DOMINAR COMANDOS SLASH PERSONALIZADOS

Los comandos slash son la clave para agregar tus propios flujos de trabajo en Claude Code. Viven en `.claude/commands/` y te permiten crear flujos de trabajo reutilizables y parametrizados.

### Comandos Integrados
- `/init` - Generar CLAUDE.md inicial
- `/permissions` - Gestionar permisos de herramientas
- `/clear` - Limpiar contexto entre tareas
- `/agents` - Gestionar subagentes
- `/help` - Obtener ayuda con Claude Code

### Ejemplo de Comando Personalizado

**Análisis de Repositorio**:
```
/primer
```
Realiza un análisis integral del repositorio para preparar Claude Code sobre tu base de código para que puedas comenzar a implementar correcciones o nuevas funcionalidades con todo el contexto necesario.

### Crear Tus Propios Comandos

1. Crear un archivo markdown en `.claude/commands/`:
```markdown
# Command: analyze-performance

Analiza el rendimiento del archivo especificado en $ARGUMENTS.

## Pasos:
1. Leer el archivo en la ruta: $ARGUMENTS
2. Identificar cuellos de botella de rendimiento
3. Sugerir optimizaciones
4. Crear un script de benchmark
```

2. Usar el comando:
```
/analyze-performance src/heavy-computation.js
```

Los comandos pueden usar `$ARGUMENTS` para recibir parámetros e invocar cualquiera de las herramientas de Claude.

*Nota: Otros asistentes de IA para codificación pueden usar estos comandos como prompts regulares - solo copia el contenido del comando y pégalo con tus argumentos.*

---

## ✅ CONSEJO 4: INTEGRAR SERVIDORES MCP

Conecta Claude Code a servidores del Model Context Protocol (MCP) para funcionalidad mejorada. Aprende más en la [documentación de MCP](https://docs.anthropic.com/en/docs/claude-code/mcp).

**Agregar Servidor Serena MCP** - El toolkit de codificación más poderoso:

Asegúrate de [instalar uvx](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer) primero. Así es como lo haces en WSL con Windows:
```bash
sudo snap install astral-uv --classic
```

Luego agrega Serena usando el comando:
```bash
# Instalar Serena para análisis semántico de código y edición
claude mcp add serena -- uvx --from git+https://github.com/oraios/serena serena start-mcp-server --context ide-assistant --project $(pwd)
```

[Serena](https://github.com/oraios/serena) transforma Claude Code en un agente de codificación completo con:
- Recuperación y análisis semántico de código
- Capacidades de edición avanzadas usando Language Server Protocol (LSP)
- Soporte para Python, TypeScript/JavaScript, PHP, Go, Rust, C/C++, Java
- Alternativa gratuita y de código abierto a asistentes de codificación basados en suscripción

**Gestionar servidores MCP:**
```bash
# Listar todos los servidores configurados
claude mcp list

# Obtener detalles sobre un servidor específico
claude mcp get serena

# Eliminar un servidor
claude mcp remove serena
```

**Próximamente**: Archon V2 (GRAN Renovación) - Una columna vertebral integral de gestión de conocimiento y tareas para asistentes de IA de codificación - permitiendo verdadera colaboración humano-IA en código por primera vez.

*Nota: MCP está integrado con cada asistente de IA de codificación principal y los servidores se gestionan de manera muy similar.*

---

## ✅ CONSEJO 5: INGENIERÍA DE CONTEXTO CON EJEMPLOS

Transforma tu flujo de trabajo de desarrollo de simple prompting a ingeniería de contexto integral - proporcionando a la IA toda la información necesaria para implementación de extremo a extremo.

### Inicio Rápido

El framework PRP (Product Requirements Prompt) es una estrategia simple de 3 pasos para ingeniería de contexto:

```bash
# 1. Define tus requisitos con ejemplos y contexto
# Edita INITIAL.md para incluir código de ejemplo y patrones

# 2. Genera un PRP integral
/generate-prp INITIAL.md

# 3. Ejecuta el PRP para implementar tu funcionalidad
/execute-prp PRPs/nombre-de-tu-funcionalidad.md
```

### Definir Tus Requisitos

Tu INITIAL.md siempre debe incluir:

```markdown
## FEATURE
Construir un sistema de autenticación de usuarios

## EXAMPLES
- Flujo de autenticación: `examples/auth-flow.js`
- Endpoint API similar: `src/api/users.js`
- Patrón de esquema de base de datos: `src/models/base-model.js`
- Enfoque de validación: `src/validators/user-validator.js`

## DOCUMENTATION
- Docs de biblioteca JWT: https://github.com/auth0/node-jsonwebtoken
- Nuestros estándares de API: `docs/api-guidelines.md`

## OTHER CONSIDERATIONS
- Usar patrones existentes de manejo de errores
- Seguir nuestro formato estándar de respuesta
- Incluir limitación de velocidad
```

### Estrategias Críticas de PRP

**Ejemplos**: La herramienta más poderosa - proporciona fragmentos de código, funcionalidades similares y patrones a seguir

**Compuertas de Validación**: Asegura pruebas integrales e iteración hasta que todas las pruebas pasen

**No Codificación por Vibra**: ¡Valida PRPs antes de ejecutarlos y el código después de la ejecución!

Mientras más ejemplos específicos proporciones, mejor puede Claude igualar tus patrones y estilo existentes.

*Nota: La ingeniería de contexto funciona con cualquier asistente de IA para codificación - el framework PRP y el enfoque basado en ejemplos son principios universales.*

---

## ✅ CONSEJO 6: APROVECHAR SUBAGENTES PARA TAREAS ESPECIALIZADAS

Los subagentes son asistentes de IA especializados que operan en ventanas de contexto separadas con experiencia enfocada. Permiten a Claude delegar tareas específicas a expertos, mejorando la calidad y eficiencia.

### Entender los Subagentes

Cada subagente:
- Tiene su propia ventana de contexto (sin contaminación de la conversación principal)
- Opera con prompts de sistema especializados
- Puede limitarse a herramientas específicas
- Trabaja autónomamente en tareas delegadas

### Ejemplos de Subagentes en Este Repositorio

**Gestor de Documentación** (`.claude/agents/documentation-manager.md`):
- Actualiza automáticamente docs cuando el código cambia
- Asegura la precisión del README
- Mantiene documentación de API
- Crea guías de migración

**Compuertas de Validación** (`.claude/agents/validation-gates.md`):
- Ejecuta todas las pruebas después de cambios
- Itera en correcciones hasta que las pruebas pasen
- Hace cumplir estándares de calidad de código
- Nunca marca tareas completas con pruebas fallidas

### Crear Tus Propios Subagentes

1. Usa el comando `/agents` o crea un archivo en `.claude/agents/`:

```markdown
---
name: security-auditor
description: "Especialista en seguridad. Revisa proactivamente el código en busca de vulnerabilidades y sugiere mejoras."
tools: Read, Grep, Glob
---

Eres un especialista en auditoría de seguridad enfocado en identificar y prevenir vulnerabilidades de seguridad...

## Responsabilidades Principales
1. Revisar código en busca de vulnerabilidades OWASP Top 10
2. Verificar secretos o credenciales expuestas
3. Validar sanitización de entradas
4. Asegurar autenticación/autorización apropiada
...
```

### Mejores Prácticas de Subagentes

**1. Experiencia Enfocada**: Cada subagente debe tener una especialidad clara

**2. Descripciones Proactivas**: Usa "proactivamente" en descripciones para invocación automática:
```yaml
description: "Revisor de código. Revisa proactivamente todos los cambios de código para calidad."
```

**3. Limitaciones de Herramientas**: Solo da a los subagentes las herramientas que necesitan:
```yaml
tools: Read, Grep  # Sin acceso de escritura para agentes solo de revisión
```

**4. Diseño de Flujo de Información**: Entiende cómo fluye la información desde agente primario → subagente → agente primario. La descripción del subagente es crucial porque le dice a tu agente principal de Claude Code cuándo y cómo usarlo. Incluye instrucciones claras en la descripción sobre cómo el agente primario debe indicar este subagente.

**5. Contexto de Una Sola Vez**: Los subagentes no tienen historial completo de conversación - reciben un solo prompt de tu agente primario. Diseña tus subagentes con esta limitación en mente.

Aprende más en la [documentación de Subagentes](https://docs.anthropic.com/en/docs/claude-code/sub-agents).

*Nota: Aunque otros asistentes de IA no tienen subagentes formales, puedes lograr resultados similares creando prompts especializados y cambiando entre diferentes contextos de conversación.*

---

## ✅ CONSEJO 7: AUTOMATIZAR CON HOOKS

Los Hooks proporcionan control determinístico sobre el comportamiento de Claude Code a través de comandos de shell definidos por el usuario que se ejecutan en eventos de ciclo de vida predefinidos.

### Eventos de Hook Disponibles

Claude Code proporciona varias acciones predefinidas en las que puedes engancharte:
- **PreToolUse**: Antes de la ejecución de herramientas (puede bloquear operaciones)
- **PostToolUse**: Después de la finalización exitosa de herramientas
- **UserPromptSubmit**: Cuando el usuario envía un prompt
- **SubagentStop**: Cuando un subagente completa su tarea
- **Stop**: Cuando el agente principal termina de responder
- **SessionStart**: Al inicio de sesión
- **PreCompact**: Antes de compactación de contexto
- **Notification**: Durante notificaciones del sistema

Aprende más en la [documentación de Hooks](https://docs.anthropic.com/en/docs/claude-code/hooks).

### Ejemplo de Hook: Registro de Uso de Herramientas

Este repositorio incluye un ejemplo simple de hook en `.claude/hooks/`:

**log-tool-usage.sh** - Registra todo el uso de herramientas para seguimiento y depuración:
```bash
#!/bin/bash
# Registra uso de herramientas con timestamps
# Crea .claude/logs/tool-usage.log
# No requiere dependencias externas
```

### Configurar Hooks

1. **Crear script de hook** en `.claude/hooks/`
2. **Hacerlo ejecutable**: `chmod +x tu-hook.sh`
3. **Agregar a configuración** en `.claude/settings.local.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": ".*",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/log-tool-usage.sh"
          }
        ]
      }
    ]
  }
}
```

Los Hooks aseguran que ciertas acciones siempre ocurran, en lugar de depender de que la IA lo recuerde - perfecto para registro, validaciones de seguridad y disparadores de construcción.

*Nota: Otros asistentes de IA no tienen hooks (¡aunque Kiro sí!), puedo casi garantizar que llegarán pronto para todos los demás.*

---

## ✅ CONSEJO 8: INTEGRACIÓN CON GITHUB CLI

Configura GitHub CLI para permitir que Claude interactúe con GitHub para issues, pull requests y gestión de repositorios.

```bash
# Instalar GitHub CLI
# Visitar: https://github.com/cli/cli#installation

# Autenticar
gh auth login

# Verificar configuración
gh repo list
```

### Comandos GitHub Personalizados

Usa el comando `/fix-github-issue` para correcciones automatizadas:

```
/fix-github-issue 123
```

Esto hará:
1. Obtener detalles del issue
2. Analizar el problema
3. Buscar código relevante
4. Implementar la corrección
5. Ejecutar pruebas
6. Crear un PR

*Nota: GitHub CLI funciona con cualquier asistente de IA para codificación - solo instálalo y la IA puede usar comandos `gh` para interactuar con tus repositorios.*

---

## ✅ CONSEJO 9: MODO YOLO SEGURO CON DEV CONTAINERS

Permite a Claude Code realizar cualquier acción mientras mantienes la seguridad a través de contenedores. Esto habilita desarrollo rápido sin comportamiento destructivo en tu máquina host.

**Requisitos Previos:**
- Instalar [Docker](https://www.docker.com/)
- VS Code (o editores compatibles)

**Características de Seguridad:**
- Aislamiento de red con lista de permitidos
- Sin acceso al sistema de archivos del host
- Conexiones salientes restringidas
- Entorno de experimentación seguro

**Proceso de Configuración:**

1. **Abrir en VS Code** y presionar `F1`
2. **Seleccionar** "Dev Containers: Reopen in Container"
3. **Esperar** construcción del contenedor
4. **Abrir terminal** (`Ctrl+J`)
5. **Autenticar** Claude Code en el contenedor
6. **Ejecutar en modo YOLO**:
   ```bash
   claude --dangerously-skip-permissions
   ```

**¿Por Qué Usar Dev Containers?**
- Probar operaciones peligrosas de forma segura
- Experimentar con cambios de sistema
- Prototipado rápido
- Entorno de desarrollo consistente
- Sin miedo a romper tu sistema

---

## ✅ CONSEJO 10: DESARROLLO PARALELO CON GIT WORKTREES

Usa Git worktrees para habilitar múltiples instancias de Claude trabajando en tareas independientes simultáneamente, o automatiza implementaciones paralelas de la misma funcionalidad.

### Configuración Manual de Worktree

```bash
# Crear worktrees para diferentes funcionalidades
git worktree add ../proyecto-auth feature/auth
git worktree add ../proyecto-api feature/api

# Lanzar Claude en cada worktree
cd ../proyecto-auth && claude  # Terminal 1
cd ../proyecto-api && claude   # Terminal 2
```

### Agentes Paralelos Automatizados

Los asistentes de IA para codificación son no-determinísticos. Ejecutar múltiples intentos aumenta la probabilidad de éxito y proporciona opciones de implementación.

**Configurar worktrees paralelos:**
```bash
/prep-parallel sistema-usuario 3
```

**Ejecutar implementaciones paralelas:**
1. Crear un archivo de plan (`plan.md`)
2. Ejecutar ejecución paralela:

```bash
/execute-parallel sistema-usuario plan.md 3
```

**Seleccionar la mejor implementación:**
```bash
# Revisar resultados
cat trees/sistema-usuario-*/RESULTS.md

# Probar cada implementación
cd trees/sistema-usuario-1 && npm test

# Fusionar la mejor
git checkout main
git merge sistema-usuario-2
```

### Beneficios

- **Sin Conflictos**: Cada instancia trabaja en aislamiento
- **Múltiples Enfoques**: Comparar diferentes implementaciones
- **Compuertas de Calidad**: Solo considerar implementaciones donde las pruebas pasan
- **Integración Fácil**: Fusionar la mejor solución

---

## 🎯 Referencia Rápida de Comandos

| Comando | Propósito |
|---------|-----------|
| `/init` | Generar CLAUDE.md inicial |
| `/permissions` | Gestionar permisos de herramientas |
| `/clear` | Limpiar contexto entre tareas |
| `/agents` | Crear y gestionar subagentes |
| `/primer` | Analizar estructura del repositorio |
| `ESC` | Interrumpir Claude |
| `Shift+Tab` | Entrar en modo planificación |
| `/generate-prp INITIAL.md` | Crear blueprint de implementación |
| `/execute-prp PRPs/feature.md` | Implementar desde blueprint |
| `/prep-parallel [funcionalidad] [cantidad]` | Configurar worktrees paralelos |
| `/execute-parallel [funcionalidad] [plan] [cantidad]` | Ejecutar implementaciones paralelas |
| `/fix-github-issue [número]` | Auto-corregir issues de GitHub |

---

## 📚 Recursos Adicionales

- [Documentación de Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- [Mejores Prácticas de Claude Code](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Biblioteca de Servidores MCP](https://github.com/modelcontextprotocol)

---

## 🚀 Próximos Pasos

1. **Comienza Simple**: Configura CLAUDE.md y permisos básicos
2. **Agrega Comandos Slash**: Crea comandos personalizados para tu flujo de trabajo
3. **Instala Servidores MCP**: Agrega Serena para capacidades de codificación mejoradas
4. **Implementa Subagentes**: Agrega especialistas para tu stack tecnológico
5. **Configura Hooks**: Automatiza tareas repetitivas
6. **Prueba Desarrollo Paralelo**: Experimenta con múltiples enfoques

Recuerda: Claude Code es más poderoso cuando proporcionas contexto claro, ejemplos específicos y validación integral. ¡Feliz codificación! 🎉