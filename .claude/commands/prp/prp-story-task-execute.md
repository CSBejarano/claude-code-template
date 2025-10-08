---
description: "Ejecutar un Story PRP con implementación enfocada en tareas del Sistema de Cotizaciones"
---

# Ejecutar Story PRP - Sistema de Cotizaciones Masivas

## Archivo PRP: $ARGUMENTOS

## Misión

Ejecutar un story/task PRP mediante **completación secuencial de tareas** con validación inmediata.

**Filosofía de Ejecución**: Completar una tarea, validarla, luego mover a la siguiente. Ninguna tarea queda atrás.

## 🔍 PRE-EXECUTION: PRP Validation (MANDATORY)

**CRITICAL**: Before executing this PRP, it MUST be validated by @prp-validator.

### Automatic Validation Workflow

1. **Invoke @prp-validator** with PRP file path
2. **Validation Process**:
   - @prp-validator scores PRP using Pareto 80-20 criteria (0-100 points)
   - If score < 80/100: Auto-improvement loop (max 3 iterations)
   - If score ≥ 80/100: Proceed to execution
   - If stuck after 3 iterations: Request manual review

3. **Validation Outputs**:
   - ✅ PASS (score ≥ 80): Continue with execution below
   - ⚠️ NEEDS REVIEW (score < 80 after 3 loops): Show issues to user, ask guidance
   - Backup created: `PRPs/[filename].md.backup-[timestamp]`

4. **User Override** (NOT recommended):
   - If user explicitly requests, can skip validation
   - Use command: `/prp-execute [file] --skip-validation`

### What @prp-validator Checks

**TIER 1 - CRITICAL (80 points)**:

1. "Current vs Desired Structure" section exists (20 pts)
2. References include BOTH external + internal (20 pts)
3. Business logic is SPECIFIC, not vague (20 pts)
4. Implementation steps are ACTIONABLE (20 pts)

**TIER 2 - HIGH (20 points)**: 5. Validation gates mentioned (10 pts) 6. Clear constraints/gotchas (10 pts)

**Minimum Score**: 80/100 to proceed

---

## Proceso de Ejecución

### 1. Cargar Story PRP

- Leer el archivo story PRP especificado
- Entender el intent original de la historia en el contexto del Sistema
- Revisar todas las referencias de contexto (fases, patrones, etc.)
- Notar comandos de validación para cada tarea

### 2. Verificación Pre-Implementación

- Ultrathink sobre el intent de la historia y requisitos de tarea
- Verificar que todos los archivos de fase referenciados existen
- Verificar que los patrones del Sistema mencionados son accesibles
- Asegurar que el ambiente de desarrollo está listo:
  - Redis ejecutándose
  - Webhook server activo
  - Async processor funcionando
- Ejecutar comandos de setup prerequisitos si es necesario

### 3. Implementación Tarea por Tarea

Para cada tarea en el PRP:

**a) Entender Tarea**

- Leer requisitos de tarea completamente
- Revisar patrones de fases implementadas referenciados
- Verificar gotchas y restricciones del Sistema (timeout 60s, max 50k combinaciones)

**b) Implementar Tarea**

**Agent**: @code-executor (TDD specialist - writes tests FIRST, then implementation)

- Seguir el patrón especificado de fases existentes
- Usar convenciones de nomenclatura del Sistema (phase1*reception, async*, data\_)
- Aplicar el enfoque documentado (Pydantic models, Redis cache)
- Manejar casos edge mencionados (status "reception_completed", no "processing")

**c) Validar Inmediatamente**

- Ejecutar comando de validación de la tarea:
  ```bash
  python3 -m py_compile src/phase*/*.py
  redis-cli ping
  curl http://localhost:8000/health
  ```
- Si validación falla, arreglar y re-validar
- No proceder hasta que tarea actual pase

**d) Marcar Completa**

- Actualizar lista de todos para rastrear progreso
- Documentar desviaciones si es necesario

### 4. Validación Completa

Después de completar todas las tareas:

- Ejecutar gates de validación del PRP:
  - Nivel 1: Sintaxis Python
  - Nivel 2: Tests unitarios (si existen)
  - Nivel 3: Integración (Redis, webhook)
  - Nivel 4: n8n workflow (usuario ejecuta)
- Ejecutar suite de tests comprehensiva
- Verificar que todos los criterios de aceptación se cumplieron

### 5. Completitud

- Trabajar el checklist de completitud del PRP
- Asegurar requisitos de historia satisfechos
- Verificar integración con async_processor
- Confirmar compatibilidad n8n
- Mover PRP completado a PRPs/completed/ (crear carpeta si no existe)

## Reglas de Ejecución del Sistema

**Gates de Validación**: Cada tarea debe pasar validación, iterar hasta pasar
**Adherencia a Patrones**: Seguir patrones de fases existentes, no crear nuevos
**Sin Atajos**: Completar todos los pasos de validación
**Test n8n**: Siempre esperar que usuario ejecute desde n8n

## Manejo de Fallos

Cuando una tarea falla validación:

1. Leer mensaje de error cuidadosamente
2. Verificar referencia de patrón nuevamente en fases implementadas
3. Validar investigando el codebase del Sistema
4. Arreglar y re-validar
5. Si atascado, verificar implementaciones similares en Phase 1-3
6. Revisar errores comunes documentados en CLAUDE.md:
   - Bucles infinitos (status incorrecto)
   - Serialización Redis (usar BaseModel)
   - Imports cross-phase (sys.path.append)

## Criterios de Éxito

- Cada comando de validación pasa
- Suite de tests completa verde (si existe)
- Criterios de aceptación de historia cumplidos
- Código sigue convenciones del Sistema de Cotizaciones
- Integración n8n funcional
- Redis cache operando correctamente
- Procesamiento dentro de límites (60s, 50k combinaciones)

## Comandos de Validación Específicos

```bash
# Verificación básica del Sistema
python3 -m py_compile src/phase*/*.py
redis-cli ping

# Webhook health
curl http://localhost:8000/health

# Status check
curl http://localhost:8000/status/{process_id}

# Logs del processor
tail -f src/phase1_reception/async_processor.log

# Redis cache inspection
redis-cli KEYS "status:*"
redis-cli KEYS "processing:*"

# n8n test (usuario ejecuta)
echo "Por favor, ejecuta prueba desde n8n en http://localhost:8000/webhook/cotizaciones"
```

## Notas Finales

- Siempre seguir arquitectura de 5 fases
- Mantener compatibilidad con n8n
- Respetar límites del sistema
- Usar patrones probados de Phase 1-3
- Documentar cualquier desviación significativa
