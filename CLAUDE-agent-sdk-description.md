# Descripción general del SDK de Agente

> Construye agentes de IA personalizados con el SDK de Agente de Claude

<Note>
  El SDK de Código de Claude ha sido renombrado como **SDK de Agente de Claude**. Si estás migrando desde el SDK anterior, consulta la [Guía de Migración](/es/docs/claude-code/sdk/migration-guide).
</Note>

## Instalación

<CodeGroup>
  ```bash TypeScript
  npm install @anthropic-ai/claude-agent-sdk
  ```

  ```bash Python
  pip install claude-agent-sdk
  ```
</CodeGroup>

## Opciones del SDK

El SDK de Agente de Claude está disponible en múltiples formas para adaptarse a diferentes casos de uso:

* **[SDK de TypeScript](/es/api/agent-sdk/typescript)** - Para aplicaciones Node.js y web
* **[SDK de Python](/es/api/agent-sdk/python)** - Para aplicaciones Python y ciencia de datos
* **[Modo de Streaming vs Modo Único](/es/api/agent-sdk/streaming-vs-single-mode)** - Entendiendo los modos de entrada y mejores prácticas

## ¿Por qué usar el SDK de Agente de Claude?

Construido sobre el arnés de agente que impulsa Claude Code, el SDK de Agente de Claude proporciona todos los bloques de construcción que necesitas para construir agentes listos para producción.

Aprovechando el trabajo que hemos hecho en Claude Code incluyendo:

* **Gestión de Contexto**: Compactación automática y gestión de contexto para asegurar que tu agente no se quede sin contexto.
* **Ecosistema de herramientas rico**: Operaciones de archivos, ejecución de código, búsqueda web, y extensibilidad MCP
* **Permisos avanzados**: Control de grano fino sobre las capacidades del agente
* **Elementos esenciales de producción**: Manejo de errores incorporado, gestión de sesiones, y monitoreo
* **Integración optimizada de Claude**: Caché automático de prompts y optimizaciones de rendimiento

## ¿Qué puedes construir con el SDK?

Aquí hay algunos tipos de agentes de ejemplo que puedes crear:

**Agentes de codificación:**

* Agentes SRE que diagnostican y arreglan problemas de producción
* Bots de revisión de seguridad que auditan código para vulnerabilidades
* Asistentes de ingeniería de guardia que clasifican incidentes
* Agentes de revisión de código que hacen cumplir el estilo y mejores prácticas

**Agentes de negocio:**

* Asistentes legales que revisan contratos y cumplimiento
* Asesores financieros que analizan reportes y pronósticos
* Agentes de soporte al cliente que resuelven problemas técnicos
* Asistentes de creación de contenido para equipos de marketing

## Conceptos Centrales

### Autenticación

Para autenticación básica, obtén una clave de API de Claude desde la [Consola de Claude](https://console.anthropic.com/) y establece la variable de entorno `ANTHROPIC_API_KEY`.

El SDK también soporta autenticación a través de proveedores de API de terceros:

* **Amazon Bedrock**: Establece la variable de entorno `CLAUDE_CODE_USE_BEDROCK=1` y configura las credenciales de AWS
* **Google Vertex AI**: Establece la variable de entorno `CLAUDE_CODE_USE_VERTEX=1` y configura las credenciales de Google Cloud

Para instrucciones detalladas de configuración para proveedores de terceros, consulta la documentación de [Amazon Bedrock](/es/docs/claude-code/amazon-bedrock) y [Google Vertex AI](/es/docs/claude-code/google-vertex-ai).

<Note>
  A menos que haya sido previamente aprobado, no permitimos que desarrolladores de terceros apliquen límites de tasa de Claude.ai para sus productos, incluyendo agentes construidos en el SDK de Agente de Claude. Por favor usa los métodos de autenticación de clave API descritos en este documento en su lugar.
</Note>

### Soporte Completo de Características de Claude Code

El SDK proporciona acceso a todas las características predeterminadas disponibles en Claude Code, aprovechando la misma configuración basada en sistema de archivos:

* **Subagentes**: Lanza agentes especializados almacenados como archivos Markdown en `./.claude/agents/`
* **Hooks**: Ejecuta comandos personalizados configurados en `./.claude/settings.json` que responden a eventos de herramientas
* **Comandos de Barra**: Usa comandos personalizados definidos como archivos Markdown en `./.claude/commands/`
* **Memoria (CLAUDE.md)**: Mantén el contexto del proyecto a través de archivos `CLAUDE.md` o `.claude/CLAUDE.md` en tu directorio de proyecto, o `~/.claude/CLAUDE.md` para instrucciones a nivel de usuario. Para cargar estos archivos, debes establecer explícitamente `settingSources: ['project']` (TypeScript) o `setting_sources=["project"]` (Python) en tus opciones. Consulta [Modificando prompts del sistema](/es/api/agent-sdk/modifying-system-prompts#method-1-claudemd-files-project-level-instructions) para detalles.

Estas características funcionan de manera idéntica a sus contrapartes de Claude Code leyendo desde las mismas ubicaciones del sistema de archivos.

### Prompts del Sistema

Los prompts del sistema definen el rol, experiencia y comportamiento de tu agente. Aquí es donde especificas qué tipo de agente estás construyendo.

### Permisos de Herramientas

Controla qué herramientas puede usar tu agente con permisos de grano fino:

* `allowedTools` - Permite explícitamente herramientas específicas
* `disallowedTools` - Bloquea herramientas específicas
* `permissionMode` - Establece la estrategia general de permisos

### Protocolo de Contexto de Modelo (MCP)

Extiende tus agentes con herramientas personalizadas e integraciones a través de servidores MCP. Esto te permite conectarte a bases de datos, APIs, y otros servicios externos.

## Reportando Errores

Si encuentras errores o problemas con el SDK de Agente:

* **SDK de TypeScript**: [Reporta problemas en GitHub](https://github.com/anthropics/claude-agent-sdk-typescript/issues)
* **SDK de Python**: [Reporta problemas en GitHub](https://github.com/anthropics/claude-agent-sdk-python/issues)

## Recursos Relacionados

* [Referencia de CLI](/es/docs/claude-code/cli-reference) - Documentación completa de CLI
* [Integración de GitHub Actions](/es/docs/claude-code/github-actions) - Automatiza tu flujo de trabajo de GitHub
* [Documentación de MCP](/es/docs/claude-code/mcp) - Extiende Claude con herramientas personalizadas
* [Flujos de Trabajo Comunes](/es/docs/claude-code/common-workflows) - Guías paso a paso
* [Solución de Problemas](/es/docs/claude-code/troubleshooting) - Problemas comunes y soluciones


