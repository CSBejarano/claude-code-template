# PRP: [Nombre del Feature]

**Fecha**: [YYYY-MM-DD]
**Tipo**: [Feature / Refactor / Bug Fix / Optimization]
**Complejidad**: [Alta / Media / Baja]
**Tiempo Estimado**: [X horas/días]

---

## 🎯 Objetivo

### Meta Principal
[Descripción clara y concisa de qué se quiere lograr con este feature]

### Entregable
[Descripción específica de qué se va a crear/modificar]

### Definición de Éxito
- [ ] [Criterio de éxito 1 - medible]
- [ ] [Criterio de éxito 2 - medible]
- [ ] [Criterio de éxito 3 - medible]

### Métricas de Éxito
| Métrica | Objetivo | Método de Medición |
|---------|----------|-------------------|
| [Ej: Tiempo de respuesta] | [< 200ms] | [Test de performance] |
| [Ej: Cobertura de tests] | [> 80%] | [Coverage report] |

---

## 👤 Persona de Usuario

### Usuario Objetivo
**Rol**: [Desarrollador / Usuario final / Sistema / etc.]
**Nivel técnico**: [Principiante / Intermedio / Avanzado]

### Caso de Uso Principal
[Descripción del escenario principal en el que se usará este feature]

**Flujo esperado**:
1. Usuario [acción 1]
2. Sistema [respuesta 1]
3. Usuario [acción 2]
4. Sistema [respuesta 2]

### Pain Points que Resuelve
- **Pain Point 1**: [Descripción del problema actual]
  - **Impacto**: [Alto / Medio / Bajo]
  - **Frecuencia**: [Cuántas veces ocurre]

- **Pain Point 2**: [Descripción del problema]
  - **Impacto**: [Alto / Medio / Bajo]
  - **Frecuencia**: [Cuántas veces ocurre]

### Casos de Uso Secundarios
- [Caso de uso secundario 1]
- [Caso de uso secundario 2]

---

## 🔍 Contexto Necesario

### Referencias del Proyecto

**Archivos Relevantes**:
- `[ruta/archivo1.ext]`: [Por qué es relevante - qué contiene que necesitamos]
- `[ruta/archivo2.ext]`: [Por qué es relevante - patrón a seguir]
- `[ruta/archivo3.ext]`: [Por qué es relevante - dependencia existente]

**Documentación Relacionada**:
- [Link a docs relevantes del proyecto]
- [Link a referencias externas si aplica]

### Árbol Actual del Codebase

```
proyecto/
├── src/
│   ├── [modulo-existente-1]/
│   │   ├── archivo1.ext
│   │   └── archivo2.ext
│   ├── [modulo-existente-2]/
│   │   └── archivo3.ext
│   └── shared/
│       └── utils.ext
├── tests/
│   └── [tests-existentes]/
└── docs/
    └── [docs-existentes]/
```

### Árbol Deseado (Después de Implementación)

```
proyecto/
├── src/
│   ├── [modulo-existente-1]/
│   ├── [modulo-existente-2]/
│   ├── [NUEVO-MODULO]/              ← NUEVO
│   │   ├── index.ext                ← CREAR
│   │   ├── service.ext              ← CREAR
│   │   ├── models.ext               ← CREAR
│   │   └── utils.ext                ← CREAR
│   └── shared/
│       └── utils.ext                ← MODIFICAR
├── tests/
│   ├── [tests-existentes]/
│   └── [NUEVO-MODULO]/              ← NUEVO
│       ├── service.test.ext         ← CREAR
│       └── integration.test.ext     ← CREAR
└── docs/
    ├── [docs-existentes]/
    └── [nuevo-feature].md           ← CREAR
```

### Dependencias Nuevas

**Packages a instalar**:
```bash
# [Gestor de paquetes] install [paquete1] [paquete2]
```

**Versiones específicas requeridas**:
- `[paquete1]`: `^[version]` - [Razón de esta versión]
- `[paquete2]`: `~[version]` - [Razón de esta versión]

### Gotchas Conocidos

⚠️ **Restricción 1**: [Descripción de limitación técnica]
- **Impacto**: [Qué afecta]
- **Mitigación**: [Cómo manejarlo]

⚠️ **Restricción 2**: [Descripción de consideración importante]
- **Impacto**: [Qué afecta]
- **Mitigación**: [Cómo manejarlo]

⚠️ **Compatibilidad**: [Issues de retrocompatibilidad]
- **Breaking changes**: [Sí/No - Detalles]
- **Migration path**: [Cómo migrar código existente]

---

## 📐 Modelos y Estructura de Datos

### Nuevos Modelos/Tipos/Interfaces

```[lenguaje]
// Modelo principal
[Definición del modelo/tipo/interface principal]

// Modelos auxiliares
[Definiciones de modelos auxiliares]

// Types/Enums
[Definiciones de tipos y enums]
```

### Esquemas de Validación

```[lenguaje]
// Schema de entrada
[Schema de validación para inputs]

// Schema de salida
[Schema de validación para outputs]
```

### Estructura de Base de Datos (si aplica)

```sql
-- Nuevas tablas/colecciones
[DDL statements o schema definitions]

-- Índices
[Definición de índices necesarios]

-- Relaciones
[Descripción de relaciones con otras entidades]
```

### Transformaciones de Datos

**Input → Processing → Output**:

```
[Formato de entrada]
    ↓
[Transformación 1]
    ↓
[Transformación 2]
    ↓
[Formato de salida]
```

---

## 🔧 Tareas de Implementación

### FASE 1: Setup y Preparación

#### TAREA 1.1: CREATE [ruta/archivo-config].ext

**CONTENIDO**:
```[lenguaje]
[Código del archivo de configuración]
```

**KEYWORDS**:
- **IMPLEMENT**: [Descripción de qué implementar]
- **PATTERN**: Seguir estructura de `[archivo-referencia]`
- **IMPORTS**: `[dependencias necesarias]`
- **GOTCHA**: [Cuidado especial a tener]

**VALIDAR**:
```bash
test -f [ruta/archivo] && echo "✅ Archivo creado" || echo "❌ Error"
[comando-adicional-validacion]
```

---

#### TAREA 1.2: UPDATE [ruta/archivo-existente].ext

**MODIFICAR**: [Sección específica del archivo]

**AGREGAR**:
```[lenguaje]
[Código a agregar]
```

**KEYWORDS**:
- **IMPLEMENT**: [Qué agregar/modificar]
- **PATTERN**: [Patrón a seguir]
- **LOCATION**: [Dónde en el archivo - después de qué línea/función]
- **GOTCHA**: [Precaución importante]

**VALIDAR**:
```bash
grep -q "[string-a-validar]" [ruta/archivo] && echo "✅ Modificado" || echo "❌ Error"
```

---

### FASE 2: Implementación Core

#### TAREA 2.1: CREATE [ruta/servicio-principal].ext

**CONTENIDO**:
```[lenguaje]
[Implementación completa del servicio principal]
```

**KEYWORDS**:
- **IMPLEMENT**: [Funcionalidad principal]
- **PATTERN**: [Patrón arquitectónico - Ej: Service Pattern, Repository, etc.]
- **DEPENDENCIES**: [Dependencias de otros módulos]
- **ERROR_HANDLING**: [Estrategia de manejo de errores]
- **ASYNC**: [Si es asíncrono - consideraciones]

**VALIDAR**:
```bash
[comando-linting]
[comando-type-check]
test -f [ruta] && echo "✅" || echo "❌"
```

---

#### TAREA 2.2: CREATE [ruta/modelos].ext

**CONTENIDO**:
```[lenguaje]
[Definición de modelos/tipos]
```

**KEYWORDS**:
- **IMPLEMENT**: [Modelos de datos]
- **VALIDATION**: [Esquemas de validación]
- **PATTERN**: [Patrón de modelos usado en el proyecto]

**VALIDAR**:
```bash
[comando-validacion-tipos]
```

---

### FASE 3: Testing

#### TAREA 3.1: CREATE tests/[nombre-test].test.ext

**CONTENIDO**:
```[lenguaje]
[Tests unitarios completos]
```

**KEYWORDS**:
- **IMPLEMENT**: Tests para [funcionalidad]
- **COVERAGE**: Cubrir casos:
  - ✅ Happy path
  - ✅ Edge cases
  - ✅ Error cases
- **PATTERN**: Seguir `tests/[test-referencia].test.ext`
- **MOCKS**: [Qué mockear y por qué]

**VALIDAR**:
```bash
[comando-ejecutar-tests]
[comando-coverage]
```

---

#### TAREA 3.2: CREATE tests/integration/[nombre].test.ext

**CONTENIDO**:
```[lenguaje]
[Tests de integración]
```

**KEYWORDS**:
- **IMPLEMENT**: Tests de integración end-to-end
- **SETUP**: [Setup necesario - DB, mocks, etc.]
- **TEARDOWN**: [Cleanup después de tests]

**VALIDAR**:
```bash
[comando-tests-integracion]
```

---

### FASE 4: Documentación

#### TAREA 4.1: CREATE docs/[nombre-feature].md

**CONTENIDO**:
```markdown
# [Nombre del Feature]

## Descripción
[Descripción del feature]

## Uso
[Ejemplos de uso]

## API Reference
[Referencia de API si aplica]

## Ejemplos
[Ejemplos de código]

## Troubleshooting
[Problemas comunes y soluciones]
```

**VALIDAR**:
```bash
test -f docs/[nombre].md && echo "✅" || echo "❌"
```

---

#### TAREA 4.2: UPDATE README.md

**AGREGAR**: Sección sobre nuevo feature en README principal

**VALIDAR**:
```bash
grep -q "[nombre-feature]" README.md && echo "✅" || echo "❌"
```

---

## ✅ Loop de Validación

### Nivel 1: Sintaxis y Estilo

```bash
# Linting
[comando-lint]

# Formatting
[comando-format]

# Type checking
[comando-typecheck]
```

**Criterios de Paso**:
- ✅ Sin errores de linting
- ✅ Código formateado correctamente
- ✅ Sin errores de tipos

---

### Nivel 2: Tests Unitarios

```bash
# Ejecutar tests unitarios
[comando-test-unit]

# Coverage
[comando-coverage]
```

**Criterios de Paso**:
- ✅ Todos los tests pasan
- ✅ Cobertura > [X]%
- ✅ Sin tests flakey

---

### Nivel 3: Tests de Integración

```bash
# Ejecutar tests de integración
[comando-test-integration]

# Tests E2E (si aplica)
[comando-test-e2e]
```

**Criterios de Paso**:
- ✅ Tests de integración pasan
- ✅ Tests E2E pasan
- ✅ Sin race conditions

---

### Nivel 4: Validación de Dominio

```bash
# Build de producción
[comando-build]

# Tests de performance (si aplica)
[comando-perf-test]

# Tests de seguridad (si aplica)
[comando-security-test]
```

**Criterios de Paso**:
- ✅ Build exitoso
- ✅ Performance dentro de objetivos
- ✅ Sin vulnerabilidades críticas

---

### Nivel 5: Revisión Manual

**Checklist de Revisión**:
- [ ] Código revisado por par
- [ ] Documentación clara y completa
- [ ] Ejemplos de uso funcionan
- [ ] Breaking changes documentados (si aplica)
- [ ] Migration guide creado (si aplica)

---

## 📋 Checklist Final

### Implementación
- [ ] Todos los archivos creados
- [ ] Todos los archivos modificados correctamente
- [ ] Código sigue convenciones del proyecto
- [ ] No hay código duplicado
- [ ] No hay código muerto (dead code)

### Testing
- [ ] Tests unitarios completos
- [ ] Tests de integración completos
- [ ] Coverage > [X]%
- [ ] Todos los tests pasan

### Documentación
- [ ] README actualizado
- [ ] Docs del feature creados
- [ ] Comentarios JSDoc/docstrings añadidos
- [ ] CHANGELOG actualizado

### Calidad
- [ ] Linting pasa
- [ ] Type checking pasa
- [ ] Build de producción exitoso
- [ ] Performance aceptable

### Integración
- [ ] Compatible con código existente
- [ ] Breaking changes documentados
- [ ] Migration path claro (si aplica)
- [ ] Dependencias actualizadas en package.json/requirements.txt

---

## 🚫 Anti-Patrones a Evitar

### ❌ NO hacer:

1. **No hardcodear valores**
   - ❌ `const API_KEY = "abc123"`
   - ✅ `const API_KEY = process.env.API_KEY`

2. **No ignorar errores silenciosamente**
   - ❌ `try { ... } catch(e) {}`
   - ✅ `try { ... } catch(e) { logger.error(e); throw e; }`

3. **No crear archivos > 500 líneas**
   - ❌ Un archivo monolítico
   - ✅ Modularizar en archivos más pequeños

4. **No saltarse tests**
   - ❌ Implementar sin tests
   - ✅ Tests primero o junto con implementación

5. **No duplicar código**
   - ❌ Copy-paste de lógica
   - ✅ Crear funciones/módulos reutilizables

6. **No usar `any` o tipos genéricos innecesarios**
   - ❌ `function process(data: any)`
   - ✅ `function process(data: SpecificType)`

7. **No dejar console.logs en producción**
   - ❌ `console.log("debug info")`
   - ✅ Usar logger apropiado o remover

8. **No ignorar edge cases**
   - ❌ Solo testear happy path
   - ✅ Testear casos límite y errores

---

## 📝 Notas Adicionales

### Consideraciones de Performance
[Notas sobre optimizaciones, caching, lazy loading, etc.]

### Consideraciones de Seguridad
[Notas sobre validación de inputs, sanitización, autenticación, etc.]

### Deuda Técnica
[Compromisos temporales que deben ser abordados en el futuro]

### Referencias
- [Link a documentación externa relevante]
- [Link a issues/tickets relacionados]
- [Link a diseños/mockups si aplica]

---

**Status**: [Draft / In Progress / Ready for Review / Completed]
**Autor**: [Nombre]
**Última actualización**: [YYYY-MM-DD]
