# Flujo de Inicialización Interactiva

## 🎯 Objetivo

Documentar el flujo completo desde "plantilla vacía" hasta "proyecto funcionando" usando el sistema de inicialización inteligente.

## 🚀 Flujo Completo

### Paso 1: Usuario Entra a Claude Code

```bash
# Usuario clona o copia la plantilla
git clone [url-plantilla] mi-nuevo-proyecto
cd mi-nuevo-proyecto

# Inicia Claude Code
claude
```

### Paso 2: Comando de Inicialización

**Usuario**:
```
/init-project
```

O con hint:
```
/init-project fastapi
```

### Paso 3: Claude Pregunta por el Objetivo (Goal Understanding)

**Claude**:
> 👋 ¡Bienvenido! Voy a ayudarte a crear tu proyecto.
>
> **¿Qué quieres crear o automatizar?**
>
> Puedes describirlo con tus propias palabras. Ejemplos:
> - "Automatizar emails en Gmail para etiquetarlos automáticamente"
> - "Crear un agente de IA que analice datos de Google Sheets"
> - "Una API REST para gestión de tareas con autenticación"

**Usuario**: "Quiero automatizar la entrada de emails en mi Gmail para que cada vez que entre un mensaje, me lo etiquete automáticamente según reglas que yo defina"

### Paso 4: Análisis Inteligente (Parallel Agents)

**Claude** ejecuta en paralelo:
- `sequential-thinking`: Analiza el objetivo y descompone componentes
- `library-researcher`: Investiga Gmail API, OAuth2, best practices
- `codebase-analyst`: Busca patrones similares en `docs/ejemplos/`
- `serena-mcp`: Analiza templates y estructuras existentes

**Claude muestra**:
> 🔍 Analizando tu objetivo...
>
> ✅ **Stack recomendado**:
> - **Lenguaje**: Python 3.12
> - **Gmail API**: `google-api-python-client`
> - **Autenticación**: OAuth2
> - **Reglas**: YAML + Pydantic validation
> - **Scheduler**: APScheduler (cada X minutos)
> - **Tests**: pytest con mocks
>
> ¿Te parece bien este stack?

### Paso 5: Preguntas Específicas al Contexto

**Claude** hace preguntas inteligentes basadas en el objetivo:

1. ¿Cada cuánto debe revisar emails? (tiempo real, cada X minutos, manual)
2. ¿Dónde ejecutar? (local, cloud, Docker)
3. ¿Cómo definir reglas? (YAML, base de datos, ambos)

**Usuario responde**: "Cada 5 minutos, local, YAML"

### Paso 6: Creación Incremental

**Claude crea**:
1. ✅ Estructura base (directorios, git init)
2. ✅ Configuración de proyecto (pyproject.toml, .env.example)
3. ✅ Código funcional con ejemplos
4. ✅ Tests con fixtures
5. ✅ Documentación (README.md, CLAUDE.md)

**NO** hace todo de una vez. Crea -> Valida -> Continúa.

### Paso 7: Setup de APIs (ONE AT A TIME)

Para cada API/servicio necesario:

**Patrón interactivo**:
```
Claude:
📧 API 1/3: Gmail API Setup

Te voy a guiar paso a paso:

1. Ve a: https://console.cloud.google.com/
2. Crea proyecto
3. Habilita Gmail API: [link directo]
4. Crea credenciales OAuth2
5. Descarga JSON

¿Completaste esto? (yes/no)
```

**Usuario**: "yes"

```
Claude:
Perfecto. Ahora ejecuta:

```bash
cp ~/Downloads/client_secret_*.json config/credentials.json
```

¿Funcionó? (yes/no)
```

**Usuario**: "yes"

```
Claude:
Excelente. Vamos a testear la autenticación:

```bash
uv run python src/auth/oauth.py
```

Debería abrirse tu navegador. ¿Se autenticó correctamente? (yes/no)
```

**Usuario**: "yes"

```
Claude:
🎉 Gmail API funcionando!

Siguiente: [próxima API si existe]
```

### Paso 8: Validación Final

**Claude ejecuta**:
```bash
# Test estructura
test -d src && test -d tests && echo "✅ Structure"

# Test dependencies
uv sync --dry-run && echo "✅ Dependencies"

# Test Python syntax
python -m py_compile src/*.py && echo "✅ Syntax"

# Test YAML config
python -c "import yaml; yaml.safe_load(open('config/rules.yaml'))" && echo "✅ Config"
```

### Paso 9: Instrucciones Finales

**Claude provee**:
```
🚀 ¡Proyecto creado exitosamente!

📋 Próximos pasos:

1. Instalar dependencias:
   ```bash
   uv sync
   ```

2. Configurar environment:
   ```bash
   cp .env.example .env
   ```

3. Autenticar Gmail (primera vez):
   ```bash
   uv run python src/auth/oauth.py
   ```

4. Configurar reglas:
   ```bash
   nano config/label_rules.yaml
   ```

5. Ejecutar:
   ```bash
   # Una vez (test)
   uv run python src/main.py --once

   # Automático (scheduler)
   uv run python src/main.py
   ```

6. Ver logs:
   ```bash
   tail -f logs/app.log
   ```

¿Necesitas ayuda con algún paso?
```

## 🎯 Principios Clave

### ✅ DO's

1. **Setup APIs ONE AT A TIME**
   - Nunca dar lista de 50 pasos al final
   - Guiar paso a paso, validar, test, confirmar

2. **Proveer links directos**
   - No "ve a la consola"
   - Sí "ve a https://console.cloud.google.com/apis/library/gmail.googleapis.com"

3. **Comandos exactos**
   - No "copia el archivo"
   - Sí "`cp ~/Downloads/file.json config/credentials.json`"

4. **Preguntar después de cada paso**
   - "¿Funcionó? (yes/no)"
   - "¿Necesitas ayuda? (yes/no/help)"

5. **Test inmediatamente**
   - Configurar API → Test → Confirmar → Siguiente
   - No acumular todos los tests al final

6. **Celebrar pequeños logros**
   - "✅ Gmail working!"
   - "🎉 OAuth authenticated!"
   - Genera confianza y momentum

### ❌ DON'Ts

1. **NO dump 50 steps at the end**
   - Abruma al usuario
   - Genera errores acumulados

2. **NO instrucciones generales**
   - "Configura la API" → demasiado vago
   - "Sigue estos 3 pasos con links directos" → específico

3. **NO asumir conocimiento**
   - Usuario puede no saber qué es OAuth2
   - Explicar brevemente cuando sea relevante

4. **NO continuar si algo falló**
   - Si test falla, ayudar a arreglar AHORA
   - No "continúa y arregla al final"

5. **NO crear todo de una vez**
   - Incremental: Base → APIs → Código → Tests
   - No: Todo → Mostrar todo → Usuario se pierde

## 🔧 Extensibilidad

### Agregar Nuevo Tipo de Proyecto

Actualizar `@project-initializer` con:
1. Nuevo template en `project_type_templates`
2. Tech stack detection en `determine_stack()`
3. Context questions en `ask_context_questions()`
4. Generación de código en `create_project()`

### Agregar Nueva API Integration

Actualizar Phase 5 (Research) y Phase 8 (Setup) en `@project-initializer`:
- Agregar API a lista de servicios detectables
- Crear setup guide interactivo específico
- Agregar validación de credenciales
- Incluir test de conexión

### Agregar Herramientas Adicionales

Actualizar Phase 6 en @project-initializer para incluir nuevas tools.

---

**Este flujo transforma la plantilla de pasiva a activa - guiando al usuario desde cero hasta proyecto funcionando en minutos.**
