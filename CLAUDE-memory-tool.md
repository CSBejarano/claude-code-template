# Herramienta de memoria

> La herramienta de memoria permite a Claude almacenar y recuperar información a través de conversaciones mediante un directorio de archivos de memoria.

La herramienta de memoria permite a Claude almacenar y recuperar información a través de conversaciones mediante un directorio de archivos de memoria. Claude puede crear, leer, actualizar y eliminar archivos que persisten entre sesiones, permitiéndole construir conocimiento a lo largo del tiempo sin mantener todo en la ventana de contexto.

La herramienta de memoria opera del lado del cliente—tú controlas dónde y cómo se almacenan los datos a través de tu propia infraestructura.

<Note>
  La herramienta de memoria está actualmente en beta. Para habilitarla, usa el encabezado beta `context-management-2025-06-27` en tus solicitudes de API.

  Por favor, comunícate a través de nuestro [formulario de comentarios](https://forms.gle/YXC2EKGMhjN1c4L88) para compartir tus comentarios sobre esta característica.
</Note>

## Casos de uso

* Mantener contexto de proyecto a través de múltiples ejecuciones de agente
* Aprender de interacciones pasadas, decisiones y retroalimentación
* Construir bases de conocimiento a lo largo del tiempo
* Habilitar aprendizaje entre conversaciones donde Claude mejora en flujos de trabajo recurrentes

## Cómo funciona

Cuando está habilitada, Claude automáticamente verifica su directorio de memoria antes de comenzar tareas. Claude puede crear, leer, actualizar y eliminar archivos en el directorio `/memories` para almacenar lo que aprende mientras trabaja, luego referenciar esas memorias en conversaciones futuras para manejar tareas similares más efectivamente o continuar donde lo dejó.

Dado que esta es una herramienta del lado del cliente, Claude hace llamadas de herramienta para realizar operaciones de memoria, y tu aplicación ejecuta esas operaciones localmente. Esto te da control completo sobre dónde y cómo se almacena la memoria. Por seguridad, deberías restringir todas las operaciones de memoria al directorio `/memories`.

### Ejemplo: Cómo funcionan las llamadas de herramienta de memoria

Cuando le pides a Claude que ayude con una tarea, Claude automáticamente verifica su directorio de memoria primero. Así es como se ve una interacción típica:

**1. Solicitud del usuario:**

```
"Ayúdame a responder a este ticket de servicio al cliente."
```

**2. Claude verifica el directorio de memoria:**

```
"Te ayudaré a responder al ticket de servicio al cliente. Déjame verificar mi memoria para cualquier contexto previo."
```

Claude llama a la herramienta de memoria:

```json
{
  "type": "tool_use",
  "id": "toolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "name": "memory",
  "input": {
    "command": "view",
    "path": "/memories"
  }
}
```

**3. Tu aplicación devuelve el contenido del directorio:**

```json
{
  "type": "tool_result",
  "tool_use_id": "toolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "content": "Directory: /memories\n- customer_service_guidelines.xml\n- refund_policies.xml"
}
```

**4. Claude lee archivos relevantes:**

```json
{
  "type": "tool_use",
  "id": "toolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "name": "memory",
  "input": {
    "command": "view",
    "path": "/memories/customer_service_guidelines.xml"
  }
}
```

**5. Tu aplicación devuelve el contenido del archivo:**

```json
{
  "type": "tool_result",
  "tool_use_id": "toolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "content": "<guidelines>\n<addressing_customers>\n- Always address customers by their first name\n- Use empathetic language\n..."
}
```

**6. Claude usa la memoria para ayudar:**

```
"Basado en tus pautas de servicio al cliente, puedo ayudarte a elaborar una respuesta. Por favor comparte los detalles del ticket..."
```

## Modelos compatibles

La herramienta de memoria está disponible en:

* Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
* Claude Sonnet 4 (`claude-sonnet-4-20250514`)
* Claude Opus 4.1 (`claude-opus-4-1-20250805`)
* Claude Opus 4 (`claude-opus-4-20250514`)

## Comenzando

Para usar la herramienta de memoria:

1. Incluye el encabezado beta `context-management-2025-06-27` en tus solicitudes de API
2. Agrega la herramienta de memoria a tu solicitud
3. Implementa manejadores del lado del cliente para operaciones de memoria

<Note>
  Para manejar operaciones de herramienta de memoria en tu aplicación, necesitas implementar manejadores para cada comando de memoria. Nuestros SDKs proporcionan ayudantes de herramienta de memoria que manejan la interfaz de herramienta—puedes hacer subclase de `BetaAbstractMemoryTool` (Python) o usar `betaMemoryTool` (TypeScript) para implementar tu propio backend de memoria (basado en archivos, base de datos, almacenamiento en la nube, archivos encriptados, etc.).

  Para ejemplos funcionales, consulta:

  * Python: [examples/memory/basic.py](https://github.com/anthropics/anthropic-sdk-python/blob/main/examples/memory/basic.py)
  * TypeScript: [examples/tools-helpers-memory.ts](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/examples/tools-helpers-memory.ts)
</Note>

## Uso básico

<CodeGroup>
  ````bash cURL
  curl https://api.anthropic.com/v1/messages \
      --header "x-api-key: $ANTHROPIC_API_KEY" \
      --header "anthropic-version: 2023-06-01" \
      --header "content-type: application/json" \
      --header "anthropic-beta: context-management-2025-06-27" \
      --data '{
          "model": "claude-sonnet-4-5",
          "max_tokens": 2048,
          "messages": [
              {
                  "role": "user",
                  "content": "Estoy trabajando en un web scraper de Python que sigue fallando con un error de timeout. Aquí está la función problemática:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPor favor ayúdame a depurar esto."
              }
          ],
          "tools": [{
              "type": "memory_20250818",
              "name": "memory"
          }]
      }'
  ````

  ````python Python
  import anthropic

  client = anthropic.Anthropic()

  message = client.beta.messages.create(
      model="claude-sonnet-4-5",
      max_tokens=2048,
      messages=[
          {
              "role": "user",
              "content": "Estoy trabajando en un web scraper de Python que sigue fallando con un error de timeout. Aquí está la función problemática:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPor favor ayúdame a depurar esto."
          }
      ],
      tools=[{
          "type": "memory_20250818",
          "name": "memory"
      }],
      betas=["context-management-2025-06-27"]
  )
  ````

  ````typescript TypeScript
  import Anthropic from '@anthropic-ai/sdk';

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY,
  });

  const message = await anthropic.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 2048,
    messages: [
      {
        role: "user",
        content: "Estoy trabajando en un web scraper de Python que sigue fallando con un error de timeout. Aquí está la función problemática:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPor favor ayúdame a depurar esto."
      }
    ],
    tools: [{
      type: "memory_20250818",
      name: "memory"
    }],
    betas: ["context-management-2025-06-27"]
  });
  ````
</CodeGroup>

## Comandos de herramienta

Tu implementación del lado del cliente necesita manejar estos comandos de herramienta de memoria:

### view

Muestra contenido de directorio o contenido de archivo con rangos de línea opcionales:

```json
{
  "command": "view",
  "path": "/memories",
  "view_range": [1, 10]  // Opcional: ver líneas específicas
}
```

### create

Crear o sobrescribir un archivo:

```json
{
  "command": "create",
  "path": "/memories/notes.txt",
  "file_text": "Notas de reunión:\n- Discutimos cronograma del proyecto\n- Próximos pasos definidos\n"
}
```

### str\_replace

Reemplazar texto en un archivo:

```json
{
  "command": "str_replace",
  "path": "/memories/preferences.txt",
  "old_str": "Color favorito: azul",
  "new_str": "Color favorito: verde"
}
```

### insert

Insertar texto en una línea específica:

```json
{
  "command": "insert",
  "path": "/memories/todo.txt",
  "insert_line": 2,
  "insert_text": "- Revisar documentación de herramienta de memoria\n"
}
```

### delete

Eliminar un archivo o directorio:

```json
{
  "command": "delete",
  "path": "/memories/old_file.txt"
}
```

### rename

Renombrar o mover un archivo/directorio:

```json
{
  "command": "rename",
  "old_path": "/memories/draft.txt",
  "new_path": "/memories/final.txt"
}
```

## Guía de prompting

Automáticamente incluimos esta instrucción al prompt del sistema cuando se incluye la herramienta de memoria:

```
IMPORTANTE: SIEMPRE VE TU DIRECTORIO DE MEMORIA ANTES DE HACER CUALQUIER OTRA COSA.
PROTOCOLO DE MEMORIA:
1. Usa el comando `view` de tu herramienta `memory` para verificar progreso anterior.
2. ... (trabajar en la tarea) ...
     - Mientras haces progreso, registra estado / progreso / pensamientos etc en tu memoria.
ASUME INTERRUPCIÓN: Tu ventana de contexto podría reiniciarse en cualquier momento, así que corres el riesgo de perder cualquier progreso que no esté registrado en tu directorio de memoria.
```

Si observas que Claude crea archivos de memoria desordenados, puedes incluir esta instrucción:

> Nota: cuando edites tu carpeta de memoria, siempre trata de mantener su contenido actualizado, coherente y organizado. Puedes renombrar o eliminar archivos que ya no sean relevantes. No crees nuevos archivos a menos que sea necesario.

También puedes guiar lo que Claude escribe en memoria, por ejemplo, "Solo anota información relevante a \<tema> en tu sistema de memoria."

## Consideraciones de seguridad

Aquí hay preocupaciones importantes de seguridad al implementar tu almacén de memoria:

### Información sensible

Claude usualmente se negará a escribir información sensible en archivos de memoria. Sin embargo, es posible que quieras implementar validación más estricta que elimine información potencialmente sensible.

### Tamaño de almacenamiento de archivos

Considera rastrear tamaños de archivos de memoria y prevenir que los archivos crezcan demasiado. Considera agregar un número máximo de caracteres que el comando de lectura de memoria puede devolver, y deja que Claude pagine a través del contenido.

### Expiración de memoria

Considera limpiar archivos de memoria periódicamente que no hayan sido accedidos en un tiempo extendido.

### Protección contra traversal de rutas

<Warning>
  Entradas de ruta maliciosas podrían intentar acceder archivos fuera del directorio `/memories`. Tu implementación **DEBE** validar todas las rutas para prevenir ataques de traversal de directorio.
</Warning>

Considera estas salvaguardas:

* Validar que todas las rutas comiencen con `/memories`
* Resolver rutas a su forma canónica y verificar que permanezcan dentro del directorio de memoria
* Rechazar rutas que contengan secuencias como `../`, `..\\`, u otros patrones de traversal
* Vigilar secuencias de traversal codificadas en URL (`%2e%2e%2f`)
* Usar las utilidades de seguridad de ruta integradas de tu lenguaje (por ejemplo, `pathlib.Path.resolve()` y `relative_to()` de Python)

## Manejo de errores

La herramienta de memoria usa los mismos patrones de manejo de errores que la [herramienta de editor de texto](/es/docs/agents-and-tools/tool-use/text-editor-tool#handle-errors). Los errores comunes incluyen archivo no encontrado, errores de permisos y rutas inválidas.
