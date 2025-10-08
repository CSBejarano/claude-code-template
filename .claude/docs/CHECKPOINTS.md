# CHECKPOINTS CRÍTICOS - ROI 100x y 10-20x

## CHECKPOINT 1: Research Phase (ROI 100x)

**Por qué es crítico**: Un error en research puede generar 1000s de líneas de código mal dirigidas.

### Agentes Involucrados (actúan en paralelo)

- **@library-researcher** - Investiga docs externas, best practices, bibliotecas recomendadas
- **@task-planner** - Coordina research, identifica preguntas críticas
- **@prp-expert** - Analiza patterns necesarios para el PRP
- **@prp-validator** - Valida findings antes de documentar
- **@codebase-analyst** - Analiza código existente, extrae conventions
- **Sequential-thinking MCP** - Análisis profundo de 8-15 thoughts

### MCPs Utilizados

- **Context7** - Contexto de documentación oficial
- **Archon** - Gestión de conocimiento, RAG queries
- **Serena** - Análisis profundo de código existente
- **Tavily** - Búsqueda web avanzada
- **Perplexity** - Research y síntesis de información

### Flujo Completo

1. Agentes actúan en **paralelo**, pasándose información entre ellos
2. Se crea **plan de búsqueda optimizado** (qué buscar, dónde, cómo validar)
3. **@documentation-manager** documenta findings en `/research/research_[nombre].md`
4. **Presentación al usuario** con summary ejecutivo
5. **Validación humana**: approve / fix: [cambios] / restart
6. Si aprueba: **@archon-expert guarda** findings en Archon MCP para reutilización
7. Si no: **iteración hasta aprobación**

### Output Esperado

- Documento `/research/research_[feature].md` con findings estructurados
- Referencias a documentación oficial con URLs específicas
- Patrones identificados en codebase
- Best practices validadas
- Gotchas conocidos documentados

---

## CHECKPOINT 2: Planning Phase (ROI 10-20x)

**Por qué es crítico**: Un plan mal diseñado puede generar 10-100 líneas de re-trabajo.

### Agentes Involucrados

- **@task-planner** - Coordina planning, genera plan YAML detallado
- **@documentation-manager** - Documenta plan en `/planning/planning_[nombre].md`
- **@codebase-analyst** - Analiza patrones para seguir
- **@prp-expert** - Crea PRPs técnicos con tareas atómicas
- **@prp-validator** - Valida PRPs generados (score ≥ 80)
- **@archon-expert** - Sincroniza plan con Archon MCP

### Enfoque - Context Engineering es REY

- ✅ Planificar **archivo por archivo**, código por código
- ✅ Usar **best practices** de ingeniería de software
- ✅ Considerar **todas las variables e hipótesis**
- ✅ Diseñar **validación para cada paso**
- ✅ Identificar **dependencias y orden de ejecución**

### Flujo Completo

1. Se crea **planificación detallada paso a paso** basada en research
2. **@documentation-manager** documenta en `/planning/planning_[nombre].md`
3. Plan incluye: fases, tareas atómicas, validación, tiempo estimado
4. **Presentación al usuario** con plan completo y estimaciones
5. **Validación humana**: approve / fix: [ajustes] / restart
6. Si aprueba: continuar a **implementación con TDD**
7. Si no: **iteración hasta aprobación**

### Output Esperado

- Documento `/planning/planning_[feature].md` con plan ejecutable
- Tareas atómicas con verbos de acción (CREATE, UPDATE, ADD, etc.)
- Comandos de validación para cada tarea
- Estimaciones de tiempo realistas
- Checkpoints intermedios identificados

---

## Impacto de Checkpoints

| Checkpoint   | Inversión Tiempo | ROI                   | Errores Prevenidos                       |
| ------------ | ---------------- | --------------------- | ---------------------------------------- |
| Research (1) | 15-30 min        | **100x**              | 1000s líneas mal dirigidas               |
| Planning (2) | 20-40 min        | **10-20x**            | 10-100 líneas re-trabajo                 |
| **Total**    | **35-70 min**    | **Ahorra 3-10 horas** | **Implementación correcta desde inicio** |

---

## Regla de Oro

**NUNCA omitir checkpoints. NUNCA asumir "approve". SIEMPRE esperar validación humana explícita.**

---

## Gestión Automática de Contexto - ⚠️ CRÍTICA

**Trigger automático**: Cuando el contexto del chat alcanza **10% de uso**

### Proceso

1. **Monitoreo continuo**: Verifica % de contexto usado en cada mensaje
2. **Trigger al 10%**: Ejecuta automáticamente `/compact-context`
3. **Lógica de CONTINUE_SESSION.md**:

   ```python
   if exists(".claude/CONTINUE_SESSION.md"):
       # UPDATE: Actualizar secciones existentes
       - Agregar nuevo checkpoint si aplica
       - Actualizar "Estado Actual"
       - Agregar tareas pendientes nuevas
       - Actualizar "Código Modificado" con nuevos snippets
       - Actualizar "Cambios desde última actualización"
   else:
       # CREATE: Generar estructura completa
       - Crear todas las secciones desde cero
       - Inicializar historial de checkpoints
       - Documentar estado inicial
   ```

### Estructura de CONTINUE_SESSION.md

````markdown
# Sesión de Trabajo: [Título del Proyecto/Feature]

**Última actualización**: [timestamp]
**Contexto usado**: [X]%

---

## 📊 Historial de Checkpoints

### CHECKPOINT 1: Research Phase

**Timestamp**: [fecha hora]
**Status**: ✅ Aprobado
**Decisión**: [Resumen de decisión tomada]
**Agentes involucrados**: @library-researcher, @codebase-analyst
**Documentos generados**: `/research/research_[nombre].md`

### CHECKPOINT 2: Planning Phase

**Timestamp**: [fecha hora]
**Status**: ✅ Aprobado / ⏳ Pendiente / 🔄 En revisión
**Decisión**: [Resumen de decisión tomada]
**Plan aprobado**: `/planning/planning_[nombre].md`

---

## 🎯 Estado Actual

**Fase actual**: [Phase X: Nombre]
**Progreso**: [X]% completo
**Tareas completadas**: [X/Y]
**Última tarea**: [Descripción de última tarea completada]

**Archivos modificados desde último checkpoint**:

- `src/services/payment.py` - Implementado PaymentService
- `tests/test_payment.py` - Tests unitarios (100% pass)

---

## 📝 Tareas Pendientes

### Alta Prioridad

- [ ] **Task X**: [Descripción detallada]
  - **Agente**: @code-executor
  - **Estimación**: 30 min
  - **Dependencias**: Task Y completada

---

## 💻 Código Modificado (Snippets Clave)

### `src/services/payment.py`

**Líneas**: 1-45
**Patrón aplicado**: Async service pattern
**Coverage**: 100% (8/8 tests)

---

## 🧠 Contexto Importante

### Decisiones Arquitectónicas

- **Patrón de pago**: Stripe API con webhooks para confirmación
- **Idempotencia**: Usar `idempotency_key` en requests

### Patrones Aplicados

- **Async/await**: Todas las operaciones I/O son asíncronas
- **Error handling**: Stripe-specific exceptions + generic fallback

### Referencias Críticas

- `src/auth/base.py`: BaseService pattern
- Stripe API docs: https://stripe.com/docs/api/payments

---

## 📊 Cambios desde Última Actualización

**Desde**: [timestamp anterior]
**Hasta**: [timestamp actual]

**Código agregado**: +234 líneas
**Tests agregados**: 8 unit tests, 3 integration tests
**Documentación**: API.md actualizado con 3 nuevos endpoints

**Métricas**:

- Test coverage: 98% → 100%
- Linting errors: 2 → 0
- Performance: 500ms → 200ms (avg response time)

---

## 🚀 Comandos para Continuar

```bash
# Ver progreso actual
cat .claude/CONTINUE_SESSION.md

# Continuar con siguiente fase
/prp:prp-story-task-execute PRPs/story_payment_system.md

# Validar estado actual
pytest tests/ -v --cov
```
````

---

**Siguiente checkpoint esperado**: CHECKPOINT 3 (Final Validation) - ETA: 30 min

```

### Sincronización con Archon

Coordina con **@archon-expert** para:
- Sincronizar CONTINUE_SESSION.md con Archon documents
- Almacenar versiones de checkpoints en Archon
- Mantener historial de decisiones arquitectónicas

**Nuevo principio crítico**: Contexto >10% sin compactar = Pérdida de información y confusión.
```
