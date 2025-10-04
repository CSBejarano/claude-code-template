# Ejecutar PRP BASE - Sistema de Cotizaciones Masivas

## Archivo PRP: $ARGUMENTOS

## Misión: Éxito de Implementación en Un Solo Intento

Los PRPs permiten código funcional en el primer intento mediante:

- **Completitud del Contexto**: Todo lo necesario, nada adivinado
- **Validación Progresiva**: Gates de 4 niveles detectan errores temprano
- **Consistencia de Patrones**: Seguir enfoques existentes del Sistema de Cotizaciones

**Tu Objetivo**: Transformar el PRP en código funcional que pase todos los gates de validación.

## Proceso de Ejecución

1. **Cargar PRP**
   - Leer el archivo PRP especificado completamente
   - Absorber todo el contexto, patrones, requisitos del Sistema de Cotizaciones
   - Usar las referencias de documentación y patrones de archivos provistos
   - Confiar en el contexto y guía del PRP - está diseñado para éxito en un intento
   - Si es necesario, hacer exploración adicional del codebase del proyecto

2. **ULTRATHINK & Planificar**
   - Crear plan de implementación comprehensivo siguiendo orden de tareas del PRP
   - Desglosar en todos claros usando herramienta TodoWrite
   - Usar subagentes para trabajo paralelo cuando sea beneficioso (siempre crear prompts inspirados en PRP para subagentes)
   - Seguir los patrones de fases ya implementadas referenciados en el PRP
   - Usar rutas de archivos específicas (phase1_reception/, phase2_analysis/, etc.)
   - Nunca adivinar - siempre verificar los patrones del Sistema referenciados

3. **Ejecutar Implementación**
   - Seguir la secuencia de Tareas de Implementación del PRP
   - Usar los patrones de las fases completadas (Phase 1-3) como ejemplos
   - Crear archivos en ubicaciones especificadas por estructura del proyecto
   - Aplicar convenciones de nomenclatura (async_, data_, pattern_) del Sistema
   - Integrar con async_processor siguiendo patrón de Phase 3

4. **Validación Progresiva**

   **Ejecutar el sistema de validación por niveles del PRP:**
   - **Nivel 1**: Ejecutar comandos de sintaxis y estilo (Python syntax check)
   - **Nivel 2**: Ejecutar validación de pruebas unitarias del PRP
   - **Nivel 3**: Ejecutar comandos de testing de integración (Redis, webhook)
   - **Nivel 4**: Ejecutar validación n8n especificada (user ejecuta desde n8n)

   **Cada nivel debe pasar antes de proceder al siguiente.**

5. **Verificación de Completitud**
   - Trabajar el Checklist de Validación Final del PRP
   - Verificar que todos los Criterios de Éxito estén cumplidos
   - Confirmar que todos los Anti-Patterns fueron evitados
   - Verificar integración con n8n webhook y Redis cache
   - Implementación lista y funcionando

## Protocolo de Fallo

Cuando la validación falla:
1. Usar los patrones y gotchas del PRP para arreglar problemas
2. Verificar errores comunes del Sistema:
   - Status "reception_completed" (no "processing")
   - Usar Pydantic BaseModel para Redis
   - Imports con sys.path.append para cross-phase
3. Re-ejecutar validación hasta que pase
4. Si es test n8n: Esperar que usuario ejecute desde n8n

## Contexto Específico del Sistema

### Comandos de Validación Comunes
```bash
# Sintaxis Python
python3 -m py_compile src/phase*/*.py

# Redis
redis-cli ping
redis-cli KEYS "status:*"

# Webhook
curl http://localhost:8000/health
curl http://localhost:8000/status/{process_id}

# Logs
tail -f src/phase1_reception/async_processor.log

# n8n (usuario ejecuta)
echo "Esperando prueba desde n8n..."
```

### Patrones Críticos a Seguir
- FastAPI async endpoints (webhook_receiver.py)
- Pydantic models para todo (BaseModel, no dataclass)
- Redis cache con categorías (processing, status, analysis)
- Structlog para logging estructurado
- Integración con async_processor para nuevas fases