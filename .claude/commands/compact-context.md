# Command: compact-context

📦 **Compacta manualmente el contexto de la sesión actual en un archivo markdown para continuar en una sesión nueva con context window limpio.**

## 🎯 Filosofía del Comando

**Objetivo**: Implementar la estrategia de "Manual Compaction" del equipo BAML - superior al `/compact` automático porque permite control fino sobre qué información preservar y cómo estructurarla.

**Basado en**: Context Engineering Best Practices (Episode #17)

---

## 🤔 ¿Cuándo Usar Este Comando?

### ✅ Usa `/compact-context` cuando:

- **Context window > 50%** y aún tienes trabajo pendiente
- **Sesión larga** con muchas tool calls acumuladas
- **Cambio de fase** (Research → Planning → Implementation)
- **Múltiples sub-agentes** ejecutados y quieres consolidar resultados
- **Antes de tarea compleja** que necesitará mucho contexto
- **Error o camino equivocado** y quieres reiniciar limpio pero preservar aprendizajes

### ❌ NO uses si:

- Context window < 30% y la tarea es simple
- Estás a punto de terminar la tarea actual
- No has acumulado información valiosa que preservar

---

## 🔄 Cómo Funciona

### Paso 1: Compactación Automática

El comando ejecutará los siguientes pasos automáticamente:

1. **Analiza la sesión actual**:
   - Tool calls ejecutados
   - Archivos leídos/modificados
   - Decisiones arquitectónicas tomadas
   - Problemas encontrados y soluciones
   - Estado actual de la tarea

2. **Genera y/o actualiza archivo de continuación**:
   - `.claude/CONTINUE_SESSION.md`
   - Formato optimizado para que otro agente pueda continuar
   - Incluye paths exactos, números de línea, comandos ejecutados
   - Secciones claramente estructuradas

3. **Proporciona instrucciones de continuación**:
   - Cómo usar `/clear` correctamente
   - Prompt exacto para nueva sesión
   - Checklist de verificación

### Paso 2: Usuario Ejecuta `/clear` (Automatico)

⚠️ **IMPORTANTE**: El comando SI ejecuta `/clear` automáticamente.

**Razón**: Quieres que el contexto sea limpio para continuar en una nueva sesión.

### Paso 3: Nueva Sesión Continúa

En la nueva sesión, el primer prompt será:

```
Estoy continuando desde una sesión anterior.
Lee .claude/CONTINUE_SESSION.md y continúa donde lo dejamos.
```

---

## 📋 Estructura del Archivo de Continuación

El archivo `.claude/CONTINUE_SESSION.md` generado contendrá:

```markdown
# Continuación de Sesión - [Fecha]

## 🎯 Objetivo de la Tarea

[Descripción clara del objetivo original]

## ✅ Progreso Completado

### Fase 1: Research (si aplica)

- Archivos investigados: [lista con paths]
- Hallazgos clave: [resumen]
- Flujo de información identificado: [diagrama o descripción]

### Fase 2: Planning (si aplica)

- Plan creado: [link o resumen]
- Fases definidas: [lista]
- Tests planificados: [lista]

### Fase 3: Implementation (si aplica)

- Archivos modificados: [lista con números de línea]
- Tests creados: [lista]
- Comandos ejecutados: [lista]

## 🔍 Decisiones Arquitectónicas

1. [Decisión 1]: [Razón]
2. [Decisión 2]: [Razón]

## 🐛 Problemas Encontrados y Soluciones

1. **Problema**: [Descripción]
   **Solución**: [Qué funcionó]

## 📍 Estado Actual

- **Context window**: [porcentaje antes de compactar]
- **Último paso completado**: [descripción]
- **Archivos en progreso**: [lista]

## ⏭️ Próximos Pasos (En Orden)

1. [ ] [Paso específico con path:línea si aplica]
2. [ ] [Paso específico]
3. [ ] [Paso específico]

## 📝 Notas Importantes

- [Cualquier cosa crítica que el próximo agente DEBE saber]
- [Trampas o gotchas identificados]
- [Comandos que NO funcionaron y por qué]

## 🔗 Referencias

- Archivos clave: [lista con paths]
- Documentación relevante: [links]
- Tests relacionados: [paths]
```

---

## 🎨 Variantes del Comando

### Micro Compaction (Específica)

```bash
/compact-context --mode=micro --focus="implementación de X"
```

Solo compacta información relacionada con un aspecto específico.

### Full Compaction (Por Defecto)

```bash
/compact-context
```

Compacta toda la sesión desde el inicio.

### Phase Transition

```bash
/compact-context --phase-transition="Research→Planning"
```

Compacta finalizando una fase y preparando para la siguiente.

---

## 💡 Best Practices

### 1. **Revisa Antes de /clear**

```bash
# Después de ejecutar /compact-context:
1. Abre .claude/CONTINUE_SESSION.md
2. Verifica que toda la información crítica está presente
3. Agrega manualmente cualquier detalle importante que falte
4. ENTONCES ejecuta /clear
```

### 2. **Organiza por Leverage**

Ordena la información por impacto:

- Decisiones arquitectónicas primero (mayor leverage)
- Hallazgos de research segundo
- Detalles de implementación tercero

### 3. **Incluye Context Específico**

```markdown
❌ MAL: "Modifiqué el archivo de usuarios"
✅ BIEN: "Modifiqué src/models/user.py:45-67 para agregar campo email_verified"

❌ MAL: "Encontré un bug"
✅ BIEN: "Bug en auth.ts:123 - no valida tokens expirados.
Solución: agregamos check antes de jwt.verify()"
```

### 4. **Próximos Pasos Ejecutables**

```markdown
❌ MAL: "Continuar con la implementación"
✅ BIEN:

1. [ ] Implementar validate_email() en src/utils/validators.py
2. [ ] Agregar test en tests/unit/test_validators.py
3. [ ] Ejecutar: pytest tests/unit/test_validators.py
4. [ ] Si pasa, continuar con integrate en user.py:67
```

---

## 🚀 Workflow Completo Recomendado

### Ejemplo: Feature Complejo

```bash
# Sesión 1: Research (context 45%)
$ /compact-context --phase-transition="Research→Planning"
# Revisa .claude/CONTINUE_SESSION.md
# Agrega hallazgos importantes manualmente si faltan
$ /clear

# Sesión 2: Planning (context limpio)
> "Lee .claude/CONTINUE_SESSION.md y crea plan de implementación"
# ... planificación ...
# (context ahora 50%)
$ /compact-context --phase-transition="Planning→Implementation"
$ /clear

# Sesión 3: Implementation (context limpio)
> "Lee .claude/CONTINUE_SESSION.md y ejecuta el plan con TDD"
# ... implementación con auto-accept ...
# Tests pasan
✅ Feature completo
```

### Ejemplo: Micro Compaction en Sesión Larga

```bash
# Durante research con múltiples sub-agentes
# (context 65% - solo tool calls acumulados)
$ /compact-context --mode=micro
# Solo elimina tool calls innecesarios
# Preserva todo el razonamiento
# Continúa en MISMA sesión (no /clear)
```

---

## ⚙️ Implementación del Comando

Este comando ejecutará internamente:

1. **Análisis de sesión**:
   - Lee historial de mensajes
   - Identifica archivos leídos (tool: Read)
   - Identifica archivos modificados (tool: Edit/Write)
   - Extrae decisiones de thinking blocks
   - Lista comandos ejecutados (tool: Bash)

2. **Generación de documento**:
   - Crea .claude/CONTINUE_SESSION.md
   - Estructura según template
   - Incluye timestamps y versiones

3. **Validación (NUEVO)**:
   - **@validation-gates**: Valida completitud del archivo compactado
   - Verifica que toda la información crítica está presente
   - Confirma que el formato es correcto y legible
   - Muestra resumen de lo compactado
   - Reporta tamaño del archivo generado
   - Sugiere qué revisar manualmente

4. **Actualización de documentación (NUEVO)**:
   - **@documentation-manager**: Actualiza referencias en documentación
   - Si el archivo CONTINUE_SESSION.md referencia nuevos patrones o decisiones
   - Asegura consistencia con PLANNING.md y TASK.md

5. **Instrucciones de continuación**:
   - Muestra prompt exacto para nueva sesión
   - Recuerda ejecutar /clear
   - Checklist de verificación

---

## 📊 Métricas de Éxito

Después de usar `/compact-context`, deberías ver:

- ✅ **Context window** en nueva sesión: <20%
- ✅ **Continuación sin fricción**: El nuevo agente entiende todo inmediatamente
- ✅ **Cero pérdida de información crítica**: Todas las decisiones preservadas
- ✅ **Próximos pasos claros**: No hay ambigüedad sobre qué hacer
- ✅ **Time to productivity**: <2 minutos en nueva sesión

---

## 🔧 Configuración Avanzada

### Personalizar Template de Continuación

Edita `.claude/templates/CONTINUE_SESSION_TEMPLATE.md` para personalizar la estructura.

### Auto-backup

Por defecto, se crean backups:

- `.claude/session_backups/CONTINUE_SESSION_[timestamp].md`
- Últimos 5 backups preservados

### Integración con Git

```bash
# Opcional: Commit de sesión al compactar
$ /compact-context --git-commit
# Crea commit con mensaje: "Session checkpoint: [descripción]"
```

---

## 🎓 Lecciones del Equipo BAML

> "Manual compaction es mejor que /compact porque TÚ decides qué es importante y cómo estructurarlo. El LLM no puede saber qué decisiones arquitectónicas fueron críticas vs qué búsquedas fueron callejones sin salida."

> "Compacta cuando context > 50%. A 80% ya es tarde y el rendimiento se degrada."

> "El archivo de continuación es tu documentación de sesión. Si otro humano no puede entender qué hiciste leyéndolo, el LLM tampoco podrá."

---

## ⚠️ Recordatorios Críticos

1. **SIEMPRE revisa** `.claude/CONTINUE_SESSION.md` antes de `/clear`
2. **NO confíes ciegamente** en la compactación automática - agrega contexto manual
3. **Incluye números de línea** específicos en archivos modificados
4. **Documenta el POR QUÉ**, no solo el qué de las decisiones
5. **Lista comandos exactos** que deben ejecutarse después
6. **Preserva errores** y soluciones - son aprendizajes valiosos

---

## 🔗 Comandos Relacionados

- `/clear` - Limpia context window (ejecutar DESPUÉS de compact)
- `/update-context` - Actualiza documentación del proyecto
- `/init-project` - Inicia nuevo proyecto con contexto limpio

---

**Version**: 1.0.0
**Última actualización**: 2025-01-04
**Basado en**: BAML Context Engineering Best Practices
**Mantenedor**: IA Corp - Claude Code Template Team
