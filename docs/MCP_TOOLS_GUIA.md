# Guía de Herramientas MCP para Claude Code

## 🎯 ¿Qué son los MCP Tools?

**MCP (Model Context Protocol)** es un protocolo que permite a Claude Code acceder a herramientas externas y servicios especializados. Los MCP Tools son servidores que exponen funcionalidades específicas como búsqueda web, análisis de código, acceso a sistemas de archivos, y más.

### Beneficios

- **Capacidades extendidas**: Claude puede acceder a información actualizada, APIs externas, bases de datos
- **Especialización**: Cada tool está optimizado para una tarea específica
- **Modularidad**: Puedes habilitar solo los tools que necesitas
- **Estandarización**: Protocolo común para todas las integraciones

## 🔧 MCP Tools Más Comunes

### 1. Perplexity Ask (`mcp__perplexity-ask__perplexity_ask`)

**Propósito**: Búsqueda de información actualizada usando Perplexity AI

**Casos de uso**:
- Investigar documentación de APIs
- Buscar información técnica reciente
- Obtener respuestas contextuales a preguntas

**Ejemplo**:
```python
# Investigar documentación de API
perplexity_ask(messages=[{
    "role": "user",
    "content": "How to authenticate with GitHub API using personal access tokens in Python?"
}])
```

**Mejores prácticas**:
- ✅ Usar para información actualizada (2024-2025)
- ✅ Preguntas específicas obtienen mejores resultados
- ❌ No usar para cálculos o procesamiento de datos locales

### 2. Tavily Search (`mcp__tavily-mcp__tavily-search`)

**Propósito**: Búsqueda web comprehensiva con resultados estructurados

**Parámetros principales**:
- `query`: Consulta de búsqueda
- `search_depth`: "basic" o "advanced"
- `max_results`: Número de resultados (5-20)
- `include_domains`: Limitar a dominios específicos
- `topic`: "general" o "news"

**Ejemplo**:
```python
# Buscar documentación de FastAPI
tavily_search(
    query="FastAPI dependency injection best practices 2025",
    search_depth="advanced",
    max_results=10,
    include_domains=["fastapi.tiangolo.com"]
)
```

**Mejores prácticas**:
- ✅ Usar `include_domains` para búsquedas en documentación oficial
- ✅ `search_depth="advanced"` para información detallada
- ✅ `topic="news"` para información reciente
- ❌ Evitar queries muy generales

### 3. Tavily Extract (`mcp__tavily-mcp__tavily-extract`)

**Propósito**: Extraer contenido limpio de URLs específicas

**Parámetros**:
- `urls`: Lista de URLs a extraer
- `extract_depth`: "basic" o "advanced"
- `format`: "markdown" o "text"

**Ejemplo**:
```python
# Extraer documentación de API
tavily_extract(
    urls=["https://docs.anthropic.com/claude/reference"],
    extract_depth="advanced",
    format="markdown"
)
```

**Mejores prácticas**:
- ✅ Usar para extraer documentación oficial
- ✅ `format="markdown"` preserva estructura
- ✅ `extract_depth="advanced"` para contenido completo
- ❌ No funciona con contenido JavaScript dinámico

### 4. Tavily Crawl (`mcp__tavily-mcp__tavily-crawl`)

**Propósito**: Rastrear sitios web siguiendo enlaces internos

**Parámetros clave**:
- `url`: URL inicial
- `max_depth`: Profundidad máxima de rastreo
- `max_breadth`: Enlaces por página
- `limit`: Total de páginas a procesar
- `instructions`: Guía en lenguaje natural

**Ejemplo**:
```python
# Rastrear documentación de proyecto
tavily_crawl(
    url="https://docs.myproject.com/",
    max_depth=3,
    max_breadth=10,
    limit=50,
    instructions="Focus on API reference pages and integration guides"
)
```

**Mejores prácticas**:
- ✅ Usar `instructions` para guiar el rastreo
- ✅ Combinar con `select_paths` para filtrar URLs
- ⚠️ Limitar `max_depth` y `limit` para evitar rastreos excesivos

### 5. Server Filesystem (`mcp__server-filesystem__*`)

**Propósito**: Operaciones de sistema de archivos

**Herramientas disponibles**:
- `read_text_file`: Leer archivos de texto
- `read_multiple_files`: Leer varios archivos simultáneamente
- `write_file`: Crear o sobrescribir archivos
- `edit_file`: Ediciones basadas en líneas
- `list_directory`: Listar contenido de directorios
- `search_files`: Buscar archivos por patrón

**Ejemplo**:
```python
# Leer configuración
read_text_file(path="/path/to/config.yaml")

# Buscar archivos Python
search_files(
    path="/project",
    pattern="*.py",
    exclude_patterns=["*test*", "*__pycache__*"]
)

# Editar archivo
edit_file(
    path="/path/to/file.py",
    edits=[{
        "oldText": "old_function_name",
        "newText": "new_function_name"
    }]
)
```

**Mejores prácticas**:
- ✅ Verificar permisos antes de operaciones de escritura
- ✅ Usar `read_multiple_files` para eficiencia
- ✅ `search_files` es más rápido que bash find
- ❌ No usar para archivos binarios grandes

### 6. Sequential Thinking (`mcp__server-sequential-thinking__sequentialthinking`)

**Propósito**: Razonamiento paso a paso para problemas complejos

**Parámetros**:
- `thought`: Paso de razonamiento actual
- `thought_number`: Número en secuencia
- `total_thoughts`: Estimación total
- `next_thought_needed`: Si se necesita más razonamiento
- `is_revision`: Si revisa pensamiento previo

**Ejemplo**:
```python
# Analizar arquitectura
sequential_thinking(
    thought="Step 1: Identify main components - API layer, business logic, data access",
    thought_number=1,
    total_thoughts=5,
    next_thought_needed=True
)

sequential_thinking(
    thought="Step 2: Analyze dependencies between components",
    thought_number=2,
    total_thoughts=5,
    next_thought_needed=True
)
```

**Mejores prácticas**:
- ✅ Usar para problemas que requieren múltiples pasos
- ✅ Puede ajustar `total_thoughts` durante el proceso
- ✅ Usar `is_revision=True` para reconsiderar pasos
- ✅ Ideal para diseño de arquitectura, debugging complejo

### 7. GitHub Integration (`mcp__github__*`)

**Propósito**: Operaciones con repositorios GitHub

**Herramientas principales**:
- `search_repositories`: Buscar repos
- `get_file_contents`: Obtener contenido de archivos
- `create_or_update_file`: Crear/actualizar archivos
- `create_pull_request`: Crear PRs
- `search_code`: Buscar código en GitHub

**Ejemplo**:
```python
# Buscar repositorios
search_repositories(
    query="fastapi authentication language:python stars:>100"
)

# Obtener archivo de repo
get_file_contents(
    owner="tiangolo",
    repo="fastapi",
    path="fastapi/security/oauth2.py"
)

# Crear PR
create_pull_request(
    owner="myorg",
    repo="myrepo",
    title="Add authentication middleware",
    head="feature/auth",
    base="main",
    body="## Summary\n- Added JWT middleware\n- Updated docs"
)
```

**Mejores prácticas**:
- ✅ Usar `search_code` para encontrar implementaciones de referencia
- ✅ Combinar con `get_file_contents` para análisis profundo
- ⚠️ Respetar rate limits de GitHub API

### 8. YouTube Subtitles (`mcp__mcp-youtube__download_youtube_url`)

**Propósito**: Descargar subtítulos de videos de YouTube

**Ejemplo**:
```python
# Obtener subtítulos de tutorial
download_youtube_url(
    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
)
```

**Mejores prácticas**:
- ✅ Usar para tutoriales técnicos y conferencias
- ✅ Permite analizar contenido sin ver el video
- ❌ Solo funciona con videos que tienen subtítulos

## 💡 Mejores Prácticas Generales

### 1. Combinación de Tools

Usa múltiples tools en paralelo para eficiencia:

```python
# Investigación completa
results = await asyncio.gather(
    perplexity_ask("Latest FastAPI features 2025"),
    tavily_search("FastAPI async performance"),
    github_search_code("FastAPI dependency injection")
)
```

### 2. Caché y Eficiencia

- **Tavily** incluye caché automático de 15 minutos
- **GitHub** tiene rate limits - usa con moderación
- **Filesystem** - leer múltiples archivos en una llamada

### 3. Manejo de Errores

```python
try:
    result = tavily_extract(urls=["https://example.com"])
except Exception as e:
    # Fallback a tavily_search o método alternativo
    result = tavily_search(query="example.com content")
```

### 4. Privacidad y Seguridad

- ❌ No envíes credenciales a tools de búsqueda web
- ✅ Usa filesystem tools para archivos locales sensibles
- ✅ Verifica permisos antes de operaciones destructivas

### 5. Optimización de Costos

- Usa `search_depth="basic"` cuando sea suficiente
- Limita `max_results` a lo necesario
- Prefiere tools específicos sobre generales

## 📚 Referencias y Recursos

### Documentación Oficial

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Tavily MCP](https://github.com/tavily-ai/tavily-mcp)
- [Perplexity API](https://docs.perplexity.ai/)
- [GitHub MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/github)

### Configuración

Los MCP servers se configuran en `.mcp.json`:

```json
{
  "mcpServers": {
    "serena": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server"]
    }
  }
}
```

Habilitar en `.claude/settings.local.json`:

```json
{
  "enableAllProjectMcpServers": true
}
```

### Ejemplos de Uso

Ver:
- `docs/SERENA_MCP.md` - Análisis semántico de código
- `docs/FLUJO_INICIALIZACION.md` - Uso de tools en project-initializer
- `.claude/agents/project-initializer.md` - Ejemplo de uso combinado

## 🎯 Casos de Uso Comunes

### Investigar Nueva Librería

```python
# 1. Buscar información general
overview = perplexity_ask("What is Pydantic AI and how does it work?")

# 2. Encontrar documentación oficial
docs = tavily_search(
    query="Pydantic AI official documentation",
    include_domains=["docs.pydantic.dev"]
)

# 3. Buscar ejemplos en GitHub
examples = github_search_code(
    q="pydantic-ai agent example language:python"
)

# 4. Extraer documentación
detailed = tavily_extract(
    urls=["https://docs.pydantic.dev/latest/"],
    extract_depth="advanced"
)
```

### Analizar Proyecto Existente

```python
# 1. Listar estructura
structure = list_directory(path="/project", recursive=True)

# 2. Buscar archivos de configuración
configs = search_files(
    path="/project",
    pattern="*.{yaml,json,toml,ini}"
)

# 3. Leer archivos clave
key_files = read_multiple_files(
    paths=["pyproject.toml", "README.md", "src/main.py"]
)

# 4. Analizar con Serena (si disponible)
overview = get_symbols_overview(relative_path="src/main.py")
```

### Crear Documentación de API

```python
# 1. Rastrear API docs de referencia
reference = tavily_crawl(
    url="https://docs.stripe.com/api",
    instructions="Focus on authentication and payment endpoints",
    max_depth=2
)

# 2. Buscar best practices
best_practices = tavily_search(
    query="REST API documentation best practices 2025",
    search_depth="advanced"
)

# 3. Generar con sequential-thinking
structure = sequential_thinking(
    thought="Design API docs structure based on Stripe reference",
    ...
)
```

---

**Los MCP Tools convierten Claude Code en un asistente universal capaz de investigar, analizar y crear con acceso a información actualizada y herramientas especializadas.**
