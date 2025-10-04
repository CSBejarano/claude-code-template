# Guía de Serena MCP - Análisis Semántico de Código

## 🎯 ¿Qué es Serena MCP?

Serena es un servidor MCP (Model Context Protocol) que proporciona capacidades avanzadas de análisis semántico de código a Claude Code. Transforma Claude Code en un agente de codificación completo con comprensión profunda del código.

## 🚀 Instalación

Serena ya está configurado en esta plantilla. Si necesitas instalarlo manualmente:

```bash
# Asegurarse de tener uvx instalado
sudo snap install astral-uv --classic  # Linux/WSL
# o
brew install uv  # macOS

# Serena se configura automáticamente via .mcp.json
```

## 🔧 Configuración

La configuración ya está en `.mcp.json`:

```json
{
  "mcpServers": {
    "serena": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/oraios/serena",
        "serena",
        "start-mcp-server",
        "--context",
        "ide-assistant",
        "--project",
        "${workspaceFolder}"
      ]
    }
  }
}
```

## 🛠️ Herramientas Disponibles

### mcp__serena__read_file
Lee archivos con límites de caracteres configurables.

```bash
# Leer archivo completo
mcp__serena__read_file(relative_path="src/main.py")

# Leer rango de líneas
mcp__serena__read_file(
    relative_path="src/main.py",
    start_line=10,
    end_line=50
)
```

### mcp__serena__list_dir
Lista directorios con recursión opcional.

```bash
# Listar directorio
mcp__serena__list_dir(
    relative_path="src",
    recursive=true,
    skip_ignored_files=true
)
```

### mcp__serena__find_symbol
Encuentra símbolos (clases, funciones, métodos) en el código.

```bash
# Buscar una clase
mcp__serena__find_symbol(
    name_path="UserService",
    include_body=true
)

# Buscar método de una clase
mcp__serena__find_symbol(
    name_path="UserService/create_user",
    include_body=true,
    depth=1
)
```

### mcp__serena__find_referencing_symbols
Encuentra todas las referencias a un símbolo.

```bash
# Encontrar quién usa UserService
mcp__serena__find_referencing_symbols(
    name_path="UserService",
    relative_path="src/services/user_service.py"
)
```

### mcp__serena__search_for_pattern
Búsqueda de patrones con regex en el código.

```bash
# Buscar patrón
mcp__serena__search_for_pattern(
    substring_pattern="async def.*",
    relative_path="src/",
    context_lines_before=2,
    context_lines_after=2
)
```

### mcp__serena__replace_symbol_body
Reemplaza el cuerpo de un símbolo.

```bash
# Reemplazar método
mcp__serena__replace_symbol_body(
    name_path="UserService/create_user",
    relative_path="src/services/user_service.py",
    body="async def create_user(self, data: UserCreate) -> User:\n    # New implementation\n    pass"
)
```

### mcp__serena__get_symbols_overview
Obtiene overview de símbolos en un archivo.

```bash
# Ver estructura de archivo
mcp__serena__get_symbols_overview(
    relative_path="src/main.py"
)
```

## 💡 Casos de Uso

### 1. Refactoring Inteligente

```python
# Encontrar símbolo a refactorizar
symbols = find_symbol(name_path="old_function")

# Ver quién lo usa
references = find_referencing_symbols(
    name_path="old_function",
    relative_path="src/utils.py"
)

# Reemplazar en todos los lugares
for ref in references:
    replace_symbol_body(...)
```

### 2. Análisis de Código

```python
# Obtener estructura del proyecto
overview = get_symbols_overview(relative_path="src/main.py")

# Buscar patrones de código
async_functions = search_for_pattern(
    substring_pattern="async def",
    relative_path="src/"
)
```

### 3. Navegación de Código

```python
# Encontrar implementación
impl = find_symbol(
    name_path="UserService/create_user",
    include_body=true
)

# Ver referencias
refs = find_referencing_symbols(
    name_path="UserService",
    relative_path="src/services/user_service.py"
)
```

## 🎓 Mejores Prácticas

### DO's ✅

1. **Usar find_symbol para navegación precisa**
   ```python
   # Mejor que read_file cuando buscas símbolo específico
   symbol = find_symbol(name_path="ClassName/method_name")
   ```

2. **Usar get_symbols_overview antes de editar**
   ```python
   # Entender estructura antes de modificar
   overview = get_symbols_overview(relative_path="file.py")
   ```

3. **Usar find_referencing_symbols antes de refactor**
   ```python
   # Saber impacto de cambios
   refs = find_referencing_symbols(...)
   ```

### DON'Ts ❌

1. **NO usar para archivos no-código**
   - Serena es para código, no para archivos de texto

2. **NO usar read_file si puedes usar find_symbol**
   - find_symbol es más preciso y eficiente

3. **NO modificar código sin verificar referencias**
   - Siempre usar find_referencing_symbols primero

## 🔗 Integración con Otros Agentes

Serena MCP trabaja perfectamente con otros agentes:

```bash
# project-initializer usa Serena para analizar estructura
@project-initializer "crear API"
  ↓ usa Serena para analizar templates
  ↓ usa find_symbol para copiar patrones
  ↓ genera estructura

# codebase-analyst usa Serena para análisis profundo
@codebase-analyst "encontrar patrón de auth"
  ↓ usa Serena search_for_pattern
  ↓ usa find_symbol para detalles
  ↓ reporta hallazgos
```

## 📚 Lenguajes Soportados

- ✅ Python
- ✅ TypeScript/JavaScript
- ✅ PHP
- ✅ Go
- ✅ Rust
- ✅ C/C++
- ✅ Java

## 🆘 Troubleshooting

### Error: "No active project"
```bash
# Verificar que Serena está configurado correctamente
cat .mcp.json | grep serena
```

### Error: "Symbol not found"
```bash
# Verificar que el path es correcto
# usar get_symbols_overview primero para ver estructura
```

## 📖 Referencias

- [Serena GitHub](https://github.com/oraios/serena)
- [MCP Documentation](https://modelcontextprotocol.io/)
- [Serena MCP Guide](https://github.com/oraios/serena/blob/main/docs/mcp.md)

---

**Serena MCP convierte Claude Code en un IDE inteligente con comprensión semántica profunda del código.**
