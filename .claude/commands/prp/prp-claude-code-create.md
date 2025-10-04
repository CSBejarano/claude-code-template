# Crear PRP BASE - Sistema de Cotizaciones Masivas

## Funcionalidad: $ARGUMENTOS

## Misión de Creación de PRP

Crear un PRP comprehensivo que permita **implementación exitosa en un solo intento** mediante investigación sistemática y curación de contexto.

**Comprensión Crítica**: El agente IA que ejecute solo recibirá:

- El contenido del PRP que crees
- Su conocimiento de datos de entrenamiento
- Acceso a archivos del codebase (pero necesita guía sobre cuáles)

**Por lo tanto**: Tu investigación y curación de contexto determina directamente el éxito de la implementación. Contexto incompleto = fallo en implementación.

## Proceso de Investigación

> Durante el proceso de investigación, crea tareas claras y genera tantos agentes y subagentes como sea necesario usando las herramientas batch. Cuanto más profunda sea la investigación, mejor será el PRP. Optimizamos para probabilidad de éxito, no para velocidad.

1. **Análisis Profundo del Codebase**
   - Crear todos claros y generar subagentes para buscar funcionalidades/patrones similares en el Sistema de Cotizaciones
   - Identificar todos los archivos necesarios para referenciar en el PRP (phase1-5, shared, etc.)
   - Notar todas las convenciones existentes del proyecto (Pydantic, async, Redis cache)
   - Revisar patrones de prueba existentes para enfoque de validación con n8n
   - Usar herramientas batch para generar subagentes que busquen funcionalidades similares

2. **Investigación Externa a Escala**
   - Crear todos claros con instrucciones para subagentes que hagan investigación profunda
   - Documentación de librerías (FastAPI, Pydantic, Redis, OpenPyXL)
   - Para documentación crítica, añadir archivo .md en PRPs/ai_docs y referenciarlo en el PRP
   - Ejemplos de implementación (GitHub/StackOverflow/blogs sobre procesamiento Excel)
   - Mejores prácticas y errores comunes encontrados durante la investigación
   - Integración con n8n workflows y webhooks

3. **Aclaración con el Usuario**
   - Preguntar por aclaraciones si es necesario
   - Recordar: El usuario siempre ejecuta pruebas desde n8n, nunca crear archivos de prueba locales

## Proceso de Generación de PRP

### Paso 1: Elegir Template

Usar `PRPs/templates/prp_base.md` como estructura de template - contiene todas las secciones y formato necesarios adaptados al Sistema de Cotizaciones.

### Paso 2: Validación de Completitud del Contexto

Antes de escribir, aplicar la prueba **"Sin Conocimiento Previo"** del template:
_"Si alguien no conociera nada sobre el Sistema de Cotizaciones, ¿tendría todo lo necesario para implementar esto exitosamente?"_

### Paso 3: Integración de Investigación

Transformar tus hallazgos de investigación en las secciones del template:

**Sección Goal**: Usar investigación para definir Goal específico de Fase/Funcionalidad y Entregable concreto
**Sección Context**: Poblar estructura YAML con hallazgos - URLs específicas de docs, patrones de archivos del proyecto, gotchas conocidos
**Tareas de Implementación**: Crear tareas ordenadas por dependencias usando palabras clave del análisis del Sistema
**Gates de Validación**: Usar comandos de validación específicos del proyecto (Redis, n8n webhook, async_processor)

### Paso 4: Estándares de Densidad de Información

Asegurar que cada referencia sea **específica y accionable**:

- URLs incluyen anclas de sección para documentación FastAPI/Pydantic
- Referencias de archivos incluyen patrones específicos de las fases implementadas
- Especificaciones de tareas incluyen convenciones exactas de nomenclatura (phase1_reception, phase2_analysis, etc.)
- Comandos de validación son específicos del proyecto (redis-cli, curl webhook, n8n test)

### Paso 5: ULTRATHINK Antes de Escribir

Después de completar la investigación, crear plan comprehensivo de escritura del PRP usando TodoWrite:

- Planificar cómo estructurar cada sección del template con hallazgos del Sistema de Cotizaciones
- Identificar gaps que necesitan investigación adicional sobre procesamiento Excel o integración n8n
- Crear enfoque sistemático para llenar template con contexto accionable del proyecto

## Output

Guardar como: `PRPs/{nombre-funcionalidad-fase}.md`

Ejemplos:
- `PRPs/phase4-combination-generator.md`
- `PRPs/ninox-api-integration.md`
- `PRPs/excel-result-formatter.md`

## Gates de Calidad del PRP

### Verificación de Completitud del Contexto

- [ ] Pasa prueba "Sin Conocimiento Previo" del template
- [ ] Todas las referencias YAML son específicas y accesibles al Sistema
- [ ] Tareas de implementación incluyen guía exacta de nomenclatura y ubicación según arquitectura 5 fases
- [ ] Comandos de validación son específicos del proyecto y verificados funcionando

### Cumplimiento de Estructura del Template

- [ ] Todas las secciones requeridas del template completadas
- [ ] Sección Goal tiene Goal de Funcionalidad específico, Entregable, Definición de Éxito
- [ ] Tareas de Implementación siguen orden de dependencias del pipeline
- [ ] Checklist de Validación Final es comprehensivo para n8n y Redis

### Estándares de Densidad de Información

- [ ] Sin referencias genéricas - todas son específicas y accionables
- [ ] Patrones de archivos apuntan a ejemplos específicos de fases ya implementadas
- [ ] URLs incluyen anclas de sección para guía exacta
- [ ] Especificaciones de tareas usan palabras clave del codebase del Sistema

## Métricas de Éxito

**Score de Confianza**: Calificar 1-10 la probabilidad de éxito de implementación en un solo intento

**Validación**: El PRP completado debe permitir a un agente IA no familiarizado con el Sistema de Cotizaciones implementar la funcionalidad exitosamente usando solo el contenido del PRP y acceso al codebase.

## Contexto Específico del Sistema de Cotizaciones

### Arquitectura de 5 Fases
- Phase 1: Reception (webhook, async_processor) ✅
- Phase 2: Analysis (excel_analyzer, pattern_detector) ✅
- Phase 3: Extraction (data_extractor, data_normalizer) ✅
- Phase 4: Generation (combination_generator, quotation_engine) 📋
- Phase 5: Delivery (result_formatter, response_sender) 📋

### Restricciones Críticas
- Siempre probar desde n8n (nunca archivos locales)
- Max 10MB archivos, 60s timeout, 50k combinaciones
- Redis cache con categorías específicas
- Pydantic BaseModel para serialización Redis
- Status: reception_completed → processing → completed