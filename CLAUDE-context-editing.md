# Edición de contexto

> Gestiona automáticamente el contexto de la conversación a medida que crece con la edición de contexto.

<Note>
  La edición de contexto está actualmente en beta con soporte para el borrado de resultados de herramientas. Para habilitarla, usa el encabezado beta `context-management-2025-06-27` en tus solicitudes de API. Se añadirán estrategias adicionales de edición de contexto en futuras versiones.

  Por favor, ponte en contacto a través de nuestro [formulario de comentarios](https://forms.gle/YXC2EKGMhjN1c4L88) para compartir tus comentarios sobre esta función.
</Note>

## Cómo funciona

La estrategia `clear_tool_uses_20250919` borra los resultados de herramientas cuando el contexto de la conversación crece más allá de tu umbral configurado. Cuando se activa, la API borra automáticamente los resultados de herramientas más antiguos en orden cronológico, reemplazándolos con texto de marcador de posición para que Claude sepa que el resultado de la herramienta fue eliminado. Por defecto, solo se borran los resultados de herramientas. Opcionalmente puedes borrar tanto los resultados de herramientas como las llamadas de herramientas (los parámetros de uso de herramientas) estableciendo `clear_tool_inputs` en true.

La edición de contexto invalida los prefijos de prompt en caché porque borrar contenido modifica la estructura del prompt, rompiendo el requisito de coincidencia para los aciertos de caché. Para tener esto en cuenta, recomendamos borrar suficientes tokens para que la invalidación de caché valga la pena. Usa el parámetro `clear_at_least` para asegurar que se borre un número mínimo de tokens cada vez. Cuando uses [caché de prompts](/es/docs/build-with-claude/prompt-caching) con edición de contexto, incurrirás en costos de escritura de caché cada vez que se borre contenido, pero las solicitudes posteriores pueden reutilizar el prefijo recién cacheado.

## Modelos compatibles

La edición de contexto está disponible en:

* Claude Opus 4.1 (`claude-opus-4-1-20250805`)
* Claude Opus 4 (`claude-opus-4-20250514`)
* Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
* Claude Sonnet 4 (`claude-sonnet-4-20250514`)

## Uso básico

La forma más simple de habilitar la edición de contexto es especificar solo el tipo de estrategia, ya que todas las demás [opciones de configuración](#configuration-options) usarán sus valores por defecto:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "anthropic-beta: context-management-2025-06-27" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [
              {
                  "role": "user",
                  "content": "Busca desarrollos recientes en IA"
              }
          ],
          "tools": [
              {
                  "type": "web_search_20250305",
                  "name": "web_search"
              }
          ],
          "context_management": {
              "edits": [
                  {"type": "clear_tool_uses_20250919"}
              ]
          }
      }'
  ```

  ```python Python
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=4096,
      messages=[
          {
              "role": "user",
              "content": "Busca desarrollos recientes en IA"
          }
      ],
      tools=[
          {
              "type": "web_search_20250305",
              "name": "web_search"
          }
      ],
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {"type": "clear_tool_uses_20250919"}
          ]
      }
  )
  ```

  ```typescript TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Busca desarrollos recientes en IA"
      }
    ],
    tools: [
      {
        type: "web_search_20250305",
        name: "web_search"
      }
    ],
    context_management: {
      edits: [
        { type: "clear_tool_uses_20250919" }
      ]
    },
    betas: ["context-management-2025-06-27"]
  });
  ```
</CodeGroup>

## Configuración avanzada

Puedes personalizar el comportamiento de edición de contexto con parámetros adicionales:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "anthropic-beta: context-management-2025-06-27" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 4096,
          "messages": [
              {
                  "role": "user",
                  "content": "Crea una aplicación simple de calculadora de línea de comandos usando Python"
              }
          ],
          "tools": [
              {
                  "type": "text_editor_20250728",
                  "name": "str_replace_based_edit_tool",
                  "max_characters": 10000
              },
              {
                  "type": "web_search_20250305",
                  "name": "web_search",
                  "max_uses": 3
              }
          ],
          "context_management": {
              "edits": [
                  {
                      "type": "clear_tool_uses_20250919",
                      "trigger": {
                          "type": "input_tokens",
                          "value": 30000
                      },
                      "keep": {
                          "type": "tool_uses",
                          "value": 3
                      },
                      "clear_at_least": {
                          "type": "input_tokens",
                          "value": 5000
                      },
                      "exclude_tools": ["web_search"]
                  }
              ]
          }
      }'
  ```

  ```python Python
  response = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=4096,
      messages=[
          {
              "role": "user",
              "content": "Crea una aplicación simple de calculadora de línea de comandos usando Python"
          }
      ],
      tools=[
          {
              "type": "text_editor_20250728",
              "name": "str_replace_based_edit_tool",
              "max_characters": 10000
          },
          {
              "type": "web_search_20250305",
              "name": "web_search",
              "max_uses": 3
          }
      ],
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {
                  "type": "clear_tool_uses_20250919",
                  # Activar el borrado cuando se exceda el umbral
                  "trigger": {
                      "type": "input_tokens",
                      "value": 30000
                  },
                  # Número de usos de herramientas a mantener después del borrado
                  "keep": {
                      "type": "tool_uses",
                      "value": 3
                  },
                  # Opcional: Borrar al menos esta cantidad de tokens
                  "clear_at_least": {
                      "type": "input_tokens",
                      "value": 5000
                  },
                  # Excluir estas herramientas del borrado
                  "exclude_tools": ["web_search"]
              }
          ]
      }
  )
  ```

  ```typescript TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const response = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Crea una aplicación simple de calculadora de línea de comandos usando Python"
      }
    ],
    tools: [
      {
        type: "text_editor_20250728",
        name: "str_replace_based_edit_tool",
        max_characters: 10000
      },
      {
        type: "web_search_20250305",
        name: "web_search",
        max_uses: 3
      }
    ],
    betas: ["context-management-2025-06-27"],
    context_management: {
      edits: [
        {
          type: "clear_tool_uses_20250919",
          // Activar el borrado cuando se exceda el umbral
          trigger: {
            type: "input_tokens",
            value: 30000
          },
          // Número de usos de herramientas a mantener después del borrado
          keep: {
            type: "tool_uses",
            value: 3
          },
          // Opcional: Borrar al menos esta cantidad de tokens
          clear_at_least: {
            type: "input_tokens",
            value: 5000
          },
          // Excluir estas herramientas del borrado
          exclude_tools: ["web_search"]
        }
      ]
    }
  });
  ```
</CodeGroup>

## Opciones de configuración

| Opción de configuración | Por defecto               | Descripción                                                                                                                                                                                                                                                                     |
| ----------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `trigger`               | 100,000 tokens de entrada | Define cuándo se activa la estrategia de edición de contexto. Una vez que el prompt excede este umbral, comenzará el borrado. Puedes especificar este valor en `input_tokens` o `tool_uses`.                                                                                    |
| `keep`                  | 3 usos de herramientas    | Define cuántos pares recientes de uso/resultado de herramientas mantener después de que ocurra el borrado. La API elimina las interacciones de herramientas más antiguas primero, preservando las más recientes.                                                                |
| `clear_at_least`        | Ninguno                   | Asegura que se borre un número mínimo de tokens cada vez que se activa la estrategia. Si la API no puede borrar al menos la cantidad especificada, la estrategia no se aplicará. Esto ayuda a determinar si vale la pena el borrado de contexto para romper tu caché de prompt. |
| `exclude_tools`         | Ninguno                   | Lista de nombres de herramientas cuyos usos y resultados nunca deben ser borrados. Útil para preservar contexto importante.                                                                                                                                                     |
| `clear_tool_inputs`     | `false`                   | Controla si los parámetros de llamada de herramientas se borran junto con los resultados de herramientas. Por defecto, solo se borran los resultados de herramientas mientras se mantienen visibles las llamadas de herramientas originales de Claude.                          |

## Formato de respuesta

Puedes ver qué ediciones de contexto se aplicaron a tu solicitud usando el campo de respuesta `context_management`, junto con estadísticas útiles sobre el contenido y los tokens de entrada borrados.

```json Response
{
    "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
    "type": "message",
    "role": "assistant",
    "content": [...],
    "usage": {...},
    "context_management": {
        "applied_edits": [
            {
                "type": "clear_tool_uses_20250919",
                "cleared_tool_uses": 8,
                "cleared_input_tokens": 50000
            }
        ]
    }
}
```

Para respuestas de streaming, las ediciones de contexto se incluirán en el evento final `message_delta`:

```json Streaming Response
{
    "type": "message_delta",
    "delta": {
        "stop_reason": "end_turn",
        "stop_sequence": null
    },
    "usage": {
        "output_tokens": 1024
    },
    "context_management": {
        "applied_edits": [...]
    }
}
```

## Conteo de tokens

El endpoint de [conteo de tokens](/es/docs/build-with-claude/token-counting) soporta gestión de contexto, permitiéndote previsualizar cuántos tokens usará tu prompt después de que se aplique la edición de contexto.

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages/count_tokens \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "anthropic-beta: context-management-2025-06-27" \
      --data '{
          "model": "claude-sonnet-4-5",
          "messages": [
              {
                  "role": "user",
                  "content": "Continúa nuestra conversación..."
              }
          ],
          "tools": [...],
          "context_management": {
              "edits": [
                  {
                      "type": "clear_tool_uses_20250919",
                      "trigger": {
                          "type": "input_tokens",
                          "value": 30000
                      },
                      "keep": {
                          "type": "tool_uses",
                          "value": 5
                      }
                  }
              ]
          }
      }'
  ```

  ```python Python
  response = client.beta.messages.count_tokens(
      model="claude-sonnet-4-5",
      messages=[
          {
              "role": "user",
              "content": "Continúa nuestra conversación..."
          }
      ],
      tools=[...],  # Tus definiciones de herramientas
      betas=["context-management-2025-06-27"],
      context_management={
          "edits": [
              {
                  "type": "clear_tool_uses_20250919",
                  "trigger": {
                      "type": "input_tokens",
                      "value": 30000
                  },
                  "keep": {
                      "type": "tool_uses",
                      "value": 5
                  }
              }
          ]
      }
  )

  print(f"Tokens originales: {response.context_management['original_input_tokens']}")
  print(f"Después del borrado: {response.input_tokens}")
  print(f"Ahorro: {response.context_management['original_input_tokens'] - response.input_tokens} tokens")
  ```

  ```typescript TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const response = await anthropic.beta.messages.countTokens({
    model: "claude-sonnet-4-5",
    messages: [
      {
        role: "user",
        content: "Continúa nuestra conversación..."
      }
    ],
    tools: [...],  // Tus definiciones de herramientas
    betas: ["context-management-2025-06-27"],
    context_management: {
      edits: [
        {
          type: "clear_tool_uses_20250919",
          trigger: {
            type: "input_tokens",
            value: 30000
          },
          keep: {
            type: "tool_uses",
            value: 5
          }
        }
      ]
    }
  });

  console.log(`Tokens originales: ${response.context_management?.original_input_tokens}`);
  console.log(`Después del borrado: ${response.input_tokens}`);
  console.log(`Ahorro: ${(response.context_management?.original_input_tokens || 0) - response.input_tokens} tokens`);
  ```
</CodeGroup>

```json Response
{
    "input_tokens": 25000,
    "context_management": {
        "original_input_tokens": 70000
    }
}
```

La respuesta muestra tanto el conteo final de tokens después de que se aplica la gestión de contexto (`input_tokens`) como el conteo original de tokens antes de que ocurriera cualquier borrado (`original_input_tokens`).
