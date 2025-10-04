# Migrar al SDK de Agente Claude

> Guía para migrar los SDKs de TypeScript y Python de Claude Code al SDK de Agente Claude

## Descripción general

El SDK de Claude Code ha sido renombrado como **SDK de Agente Claude** y su documentación ha sido reorganizada. Este cambio refleja las capacidades más amplias del SDK para construir agentes de IA más allá de solo tareas de codificación.

## Qué ha cambiado

| Aspecto                           | Anterior                                | Nuevo                               |
| :-------------------------------- | :-------------------------------------- | :---------------------------------- |
| **Nombre del Paquete (TS/JS)**    | `@anthropic-ai/claude-code`             | `@anthropic-ai/claude-agent-sdk`    |
| **Paquete Python**                | `claude-code-sdk`                       | `claude-agent-sdk`                  |
| **Ubicación de la Documentación** | Documentos de Claude Code → sección SDK | Guía de API → sección SDK de Agente |

<Note>
  **Cambios en la Documentación:** La documentación del SDK de Agente se ha movido de los documentos de Claude Code a la Guía de API bajo una sección dedicada [SDK de Agente](/es/api/agent-sdk/overview). Los documentos de Claude Code ahora se enfocan en la herramienta CLI y características de automatización.
</Note>

## Pasos de migración

### Para proyectos TypeScript/JavaScript

**1. Desinstalar el paquete anterior:**

```bash
npm uninstall @anthropic-ai/claude-code
```

**2. Instalar el nuevo paquete:**

```bash
npm install @anthropic-ai/claude-agent-sdk
```

**3. Actualizar tus importaciones:**

Cambiar todas las importaciones de `@anthropic-ai/claude-code` a `@anthropic-ai/claude-agent-sdk`:

```typescript
// Antes
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-code";

// Después
import {
  query,
  tool,
  createSdkMcpServer,
} from "@anthropic-ai/claude-agent-sdk";
```

**4. Actualizar las dependencias de package.json:**

Si tienes el paquete listado en tu `package.json`, actualízalo:

```json
// Antes
{
  "dependencies": {
    "@anthropic-ai/claude-code": "^1.0.0"
  }
}

// Después
{
  "dependencies": {
    "@anthropic-ai/claude-agent-sdk": "^0.1.0"
  }
}
```

¡Eso es todo! No se requieren otros cambios de código.

### Para proyectos Python

**1. Desinstalar el paquete anterior:**

```bash
pip uninstall claude-code-sdk
```

**2. Instalar el nuevo paquete:**

```bash
pip install claude-agent-sdk
```

**3. Actualizar tus importaciones:**

Cambiar todas las importaciones de `claude_code_sdk` a `claude_agent_sdk`:

```python
# Antes
from claude_code_sdk import query, ClaudeCodeOptions

# Después
from claude_agent_sdk import query, ClaudeAgentOptions
```

**4. Actualizar nombres de tipos:**

Cambiar `ClaudeCodeOptions` a `ClaudeAgentOptions`:

```python
# Antes
from claude_agent_sdk import query, ClaudeCodeOptions

options = ClaudeCodeOptions(
    model="claude-sonnet-4-5"
)

# Después
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(
    model="claude-sonnet-4-5"
)
```

**5. Revisar [cambios disruptivos](#breaking-changes)**

Hacer cualquier cambio de código necesario para completar la migración.

## Cambios disruptivos

<Warning>
  Para mejorar el aislamiento y la configuración explícita, el SDK de Agente Claude v0.1.0 introduce cambios disruptivos para usuarios que migran desde el SDK de Claude Code. Revisa esta sección cuidadosamente antes de migrar.
</Warning>

### Python: ClaudeCodeOptions renombrado a ClaudeAgentOptions

**Qué cambió:** El tipo `ClaudeCodeOptions` del SDK de Python ha sido renombrado a `ClaudeAgentOptions`.

**Migración:**

```python
# ANTES (v0.0.x)
from claude_agent_sdk import query, ClaudeCodeOptions

options = ClaudeCodeOptions(
    model="claude-sonnet-4-5",
    permission_mode="acceptEdits"
)

# DESPUÉS (v0.1.0)
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(
    model="claude-sonnet-4-5",
    permission_mode="acceptEdits"
)
```

**Por qué cambió esto:** El nombre del tipo ahora coincide con la marca "SDK de Agente Claude" y proporciona consistencia a través de las convenciones de nomenclatura del SDK.

### El prompt del sistema ya no es predeterminado

**Qué cambió:** El SDK ya no usa el prompt del sistema de Claude Code por defecto.

**Migración:**

<CodeGroup>
  ```typescript TypeScript
  // ANTES (v0.0.x) - Usaba el prompt del sistema de Claude Code por defecto
  const result = query({ prompt: "Hola" });

  // DESPUÉS (v0.1.0) - Usa prompt del sistema vacío por defecto
  // Para obtener el comportamiento anterior, solicita explícitamente el preset de Claude Code:
  const result = query({
    prompt: "Hola",
    options: {
      systemPrompt: { type: "preset", preset: "claude_code" }
    }
  });

  // O usa un prompt del sistema personalizado:
  const result = query({
    prompt: "Hola",
    options: {
      systemPrompt: "Eres un asistente de codificación útil"
    }
  });
  ```

  ```python Python
  # ANTES (v0.0.x) - Usaba el prompt del sistema de Claude Code por defecto
  async for message in query(prompt="Hola"):
      print(message)

  # DESPUÉS (v0.1.0) - Usa prompt del sistema vacío por defecto
  # Para obtener el comportamiento anterior, solicita explícitamente el preset de Claude Code:
  from claude_agent_sdk import query, ClaudeAgentOptions

  async for message in query(
      prompt="Hola",
      options=ClaudeAgentOptions(
          system_prompt={"type": "preset", "preset": "claude_code"}  # Usar el preset
      )
  ):
      print(message)

  # O usa un prompt del sistema personalizado:
  async for message in query(
      prompt="Hola",
      options=ClaudeAgentOptions(
          system_prompt="Eres un asistente de codificación útil"
      )
  ):
      print(message)
  ```
</CodeGroup>

**Por qué cambió esto:** Proporciona mejor control y aislamiento para aplicaciones del SDK. Ahora puedes construir agentes con comportamiento personalizado sin heredar las instrucciones enfocadas en CLI de Claude Code.

### Las fuentes de configuración ya no se cargan por defecto

**Qué cambió:** El SDK ya no lee de configuraciones del sistema de archivos (CLAUDE.md, settings.json, comandos slash, etc.) por defecto.

**Migración:**

<CodeGroup>
  ```typescript TypeScript
  // ANTES (v0.0.x) - Cargaba todas las configuraciones automáticamente
  const result = query({ prompt: "Hola" });
  // Leería de:
  // - ~/.claude/settings.json (usuario)
  // - .claude/settings.json (proyecto)
  // - .claude/settings.local.json (local)
  // - archivos CLAUDE.md
  // - Comandos slash personalizados

  // DESPUÉS (v0.1.0) - No se cargan configuraciones por defecto
  // Para obtener el comportamiento anterior:
  const result = query({
    prompt: "Hola",
    options: {
      settingSources: ["user", "project", "local"]
    }
  });

  // O cargar solo fuentes específicas:
  const result = query({
    prompt: "Hola",
    options: {
      settingSources: ["project"]  // Solo configuraciones del proyecto
    }
  });
  ```

  ```python Python
  # ANTES (v0.0.x) - Cargaba todas las configuraciones automáticamente
  async for message in query(prompt="Hola"):
      print(message)
  # Leería de:
  # - ~/.claude/settings.json (usuario)
  # - .claude/settings.json (proyecto)
  # - .claude/settings.local.json (local)
  # - archivos CLAUDE.md
  # - Comandos slash personalizados

  # DESPUÉS (v0.1.0) - No se cargan configuraciones por defecto
  # Para obtener el comportamiento anterior:
  from claude_agent_sdk import query, ClaudeAgentOptions

  async for message in query(
      prompt="Hola",
      options=ClaudeAgentOptions(
          setting_sources=["user", "project", "local"]
      )
  ):
      print(message)

  # O cargar solo fuentes específicas:
  async for message in query(
      prompt="Hola",
      options=ClaudeAgentOptions(
          setting_sources=["project"]  # Solo configuraciones del proyecto
      )
  ):
      print(message)
  ```
</CodeGroup>

**Por qué cambió esto:** Asegura que las aplicaciones del SDK tengan comportamiento predecible independiente de configuraciones locales del sistema de archivos. Esto es especialmente importante para:

* **Entornos CI/CD** - Comportamiento consistente sin personalizaciones locales
* **Aplicaciones desplegadas** - Sin dependencia de configuraciones del sistema de archivos
* **Pruebas** - Entornos de prueba aislados
* **Sistemas multi-inquilino** - Prevenir filtración de configuraciones entre usuarios

<Note>
  **Compatibilidad hacia atrás:** Si tu aplicación dependía de configuraciones del sistema de archivos (comandos slash personalizados, instrucciones CLAUDE.md, etc.), agrega `settingSources: ['user', 'project', 'local']` a tus opciones.
</Note>

## ¿Por qué el cambio de nombre?

El SDK de Claude Code fue originalmente diseñado para tareas de codificación, pero ha evolucionado hacia un marco poderoso para construir todo tipo de agentes de IA. El nuevo nombre "SDK de Agente Claude" refleja mejor sus capacidades:

* Construir agentes de negocio (asistentes legales, asesores financieros, soporte al cliente)
* Crear agentes de codificación especializados (bots SRE, revisores de seguridad, agentes de revisión de código)
* Desarrollar agentes personalizados para cualquier dominio con uso de herramientas, integración MCP, y más

## Obtener ayuda

Si encuentras algún problema durante la migración:

**Para TypeScript/JavaScript:**

1. Verifica que todas las importaciones estén actualizadas para usar `@anthropic-ai/claude-agent-sdk`
2. Verifica que tu package.json tenga el nuevo nombre del paquete
3. Ejecuta `npm install` para asegurar que las dependencias estén actualizadas

**Para Python:**

1. Verifica que todas las importaciones estén actualizadas para usar `claude_agent_sdk`
2. Verifica que tu requirements.txt o pyproject.toml tenga el nuevo nombre del paquete
3. Ejecuta `pip install claude-agent-sdk` para asegurar que el paquete esté instalado

Ve la guía de [Solución de problemas](/es/docs/claude-code/troubleshooting) para problemas comunes.

## Próximos pasos

* Explora la [Descripción general del SDK de Agente](/es/api/agent-sdk/overview) para aprender sobre las características disponibles
* Revisa la [Referencia del SDK de TypeScript](/es/api/agent-sdk/typescript) para documentación detallada de la API
* Revisa la [Referencia del SDK de Python](/es/api/agent-sdk/python) para documentación específica de Python
* Aprende sobre [Herramientas personalizadas](/es/api/agent-sdk/custom-tools) e [Integración MCP](/es/api/agent-sdk/mcp)
