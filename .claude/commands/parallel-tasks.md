# Command: /parallel-tasks

**Patrón esencial de ejecución paralela de tareas independientes con Task tool**

---

## 🎯 Propósito

Establecer el patrón fundamental de **ejecutar múltiples subagentes en paralelo** para tareas independientes, maximizando eficiencia y reduciendo tiempo de ejecución.

**Principio Core**: Si las tareas NO dependen entre sí, SIEMPRE ejecutarlas en paralelo con múltiples llamadas al Task tool en una sola invocación.

**Basado en**: Capacidades nativas de Claude Code para invocar múltiples tools en una sola llamada de function_calls.

---

## 📖 Usage

Este NO es un comando que ejecutas directamente con `/parallel-tasks`. Es un **patrón de comportamiento** que Claude Code debe aplicar automáticamente.

**Trigger automático**: Cuando identificas que necesitas realizar múltiples tareas que son independientes entre sí.

### Ejemplos de cuándo aplicar:

- Analizar múltiples archivos sin dependencias
- Investigar múltiples librerías o APIs
- Crear múltiples componentes independientes
- Validar múltiples aspectos del código
- Generar múltiples documentos
- Ejecutar tests de diferentes módulos
- Leer documentación de múltiples servicios
- Implementar features paralelas en diferentes módulos

---

## ⚡ Patrón de Ejecución

### ❌ ANTI-PATRÓN: Ejecución Secuencial

**NO HACER ESTO**:

```
Usuario: "Analiza los servicios de Gmail, Notion y Holded"

Claude (mal):
1. Primero investigo Gmail...
   [invoke Task: Gmail API]
   [espera resultado]

2. Ahora investigo Notion...
   [invoke Task: Notion API]
   [espera resultado]

3. Finalmente investigo Holded...
   [invoke Task: Holded API]
   [espera resultado]

Tiempo total: 6-9 minutos (secuencial)
```

**Problemas**:

- 3x más lento de lo necesario
- Desperdicia capacidad de paralelización
- Mala experiencia de usuario (espera innecesaria)
- No aprovecha arquitectura de Claude Code

---

### ✅ PATRÓN CORRECTO: Ejecución Paralela

**HACER ESTO**:

```
Usuario: "Analiza los servicios de Gmail, Notion y Holded"

Claude (bien):
Voy a investigar las 3 APIs en paralelo para ser más eficiente:

[invoke Task 1: Gmail API - OAuth, endpoints, rate limits, librerías Python]
[invoke Task 2: Notion API - autenticación, bases de datos, bloques, SDK]
[invoke Task 3: Holded API - endpoints, autenticación, webhooks, docs]

Tiempo total: 2-3 minutos (paralelo)
Eficiencia: 3x más rápido
```

**Ventajas**:

- 3x más rápido (ejecución simultánea)
- Aprovecha capacidad de Claude Code
- Mejor experiencia de usuario
- Misma calidad de resultados

---

## 🎯 Cuándo Usar Paralelo vs Secuencial

### ✅ Usa PARALELO cuando:

- **Tareas independientes**: No hay dependencia de datos entre tareas
- **Mismo tipo de operación**: Análisis, investigación, creación de archivos
- **Resultados no se bloquean**: La salida de tarea A no es input de tarea B
- **Múltiples recursos**: Diferentes APIs, archivos, módulos

**Ejemplos**:

```
✅ Investigar 3 APIs diferentes (Gmail, Notion, Holded)
✅ Analizar 4 archivos de código independientes
✅ Crear tests para 5 módulos diferentes
✅ Leer documentación de 3 librerías
✅ Validar 4 aspectos diferentes del código
```

### ❌ Usa SECUENCIAL cuando:

- **Dependencia de datos**: Tarea B necesita resultado de tarea A
- **Orden importa**: Pasos que deben ejecutarse en secuencia
- **Estado compartido**: Las tareas modifican el mismo recurso
- **Decisiones condicionales**: La siguiente tarea depende del resultado anterior

**Ejemplos**:

```
❌ 1. Analizar requisitos → 2. Diseñar arquitectura → 3. Implementar
❌ 1. Leer archivo → 2. Procesar datos → 3. Guardar resultado
❌ 1. Ejecutar tests → 2. Analizar fallos → 3. Sugerir fixes
❌ 1. Validar input → 2. Transformar datos → 3. Almacenar
```

---

## 💡 Reglas de Decisión Rápida

### Pregunta Clave:

**"¿Necesito el resultado de la tarea A para empezar la tarea B?"**

- **NO** → Ejecutar en PARALELO ✅
- **SÍ** → Ejecutar en SECUENCIAL ❌

### Checklist Paralelo:

```
□ Las tareas son independientes (no dependen entre sí)
□ Puedo definir claramente cada tarea ahora mismo
□ Los resultados pueden combinarse después
□ No hay modificación de estado compartido

Si todos = ✓ → PARALELO
Si alguno = ✗ → SECUENCIAL
```

---

## 📊 Ejemplos Reales

### Ejemplo 1: Investigación de APIs (PARALELO)

```
Usuario: "Necesito integrar Gmail, Slack y Trello. Investiga sus APIs"

✅ CORRECTO:
[Task 1: Gmail API - OAuth2, scopes, endpoints de correo]
[Task 2: Slack API - Web API, RTM, eventos, webhooks]
[Task 3: Trello API - REST API, boards, cards, autenticación]

3 tareas en paralelo = 2-3 min total
```

### Ejemplo 2: Análisis de Código (PARALELO)

```
Usuario: "Analiza los patrones en src/services/, src/utils/ y src/models/"

✅ CORRECTO:
[Task 1: Analizar patrones en src/services/]
[Task 2: Analizar patrones en src/utils/]
[Task 3: Analizar patrones en src/models/]

3 tareas en paralelo = 1-2 min total
```

### Ejemplo 3: Creación de Tests (PARALELO)

```
Usuario: "Crea tests para authService, emailService y logService"

✅ CORRECTO:
[Task 1: Crear tests para authService - login, logout, refresh]
[Task 2: Crear tests para emailService - send, validate, queue]
[Task 3: Crear tests para logService - info, error, debug]

3 tareas en paralelo = 2-3 min total
```

### Ejemplo 4: Pipeline de Datos (SECUENCIAL)

```
Usuario: "Procesa el archivo users.csv: lee, valida, transforma y guarda"

❌ NO PARALELO (hay dependencia):
1. [Task 1: Leer users.csv]
   [espera resultado]
2. [Task 2: Validar datos leídos]
   [espera resultado]
3. [Task 3: Transformar datos válidos]
   [espera resultado]
4. [Task 4: Guardar en base de datos]

Secuencial es correcto aquí (cada paso depende del anterior)
```

---

## 🚀 Best Practices

### 1. Máximo de Tareas Paralelas

**Recomendado**: 3-5 tareas paralelas por invocación
**Límite práctico**: 8 tareas paralelas
**Razón**: Mantener claridad y evitar sobrecarga

```
✅ BUENO: 3 APIs en paralelo
✅ BUENO: 5 archivos en paralelo
⚠️ LÍMITE: 8 componentes en paralelo
❌ EXCESIVO: 15 módulos en paralelo (mejor dividir en 2 rondas)
```

### 2. Descripción Clara de Tareas

Cada tarea debe tener:

- Objetivo claro y específico
- Alcance bien definido
- Criterios de éxito
- Output esperado

```
✅ BUENO: "Investigar Gmail API: OAuth2, endpoints de lectura, rate limits, SDK Python"
❌ MALO: "Investigar Gmail"
```

### 3. Combinación de Resultados

Después de ejecución paralela:

- Resume findings de todas las tareas
- Identifica patrones comunes
- Destaca diferencias importantes
- Provee recomendaciones consolidadas

---

## 🔍 Detección Automática

Claude Code debe **detectar automáticamente** estas situaciones y aplicar ejecución paralela:

### Palabras clave que indican paralelización:

- "múltiples", "varios", "diferentes"
- "analiza X, Y y Z"
- "investiga las APIs de..."
- "crea tests para..."
- "lee los archivos..."
- "valida los módulos..."

### Patrón de lista:

```
Usuario: "Analiza:
- serviceA.js
- serviceB.js
- serviceC.js"

→ Claude detecta lista → Ejecuta 3 Tasks en paralelo
```

---

## ⚙️ Implementación Técnica

### Sintaxis Correcta para Múltiples Tasks:

Invoca múltiples Tasks en un solo bloque de function_calls:

```
Paso 1: Invoca todas las tareas juntas
Paso 2: Espera a que todas completen
Paso 3: Combina y analiza resultados
```

### Flujo de Trabajo:

1. **Identificar** tareas independientes
2. **Invocar** todas las Tasks en paralelo
3. **Esperar** resultados
4. **Analizar** y combinar findings
5. **Presentar** resumen consolidado

---

## 📏 Métricas de Eficiencia

### Impacto en Tiempo:

| Tareas   | Secuencial | Paralelo | Mejora        |
| -------- | ---------- | -------- | ------------- |
| 2 tareas | 4-6 min    | 2-3 min  | 2x más rápido |
| 3 tareas | 6-9 min    | 2-3 min  | 3x más rápido |
| 5 tareas | 10-15 min  | 3-4 min  | 4x más rápido |
| 8 tareas | 16-24 min  | 4-5 min  | 5x más rápido |

### ROI de Paralelización:

- **Tiempo ahorrado**: 50-80% reduction
- **Experiencia de usuario**: Significativamente mejor
- **Throughput**: 3-5x mayor
- **Costo**: Mismo (mismas operaciones, mejor organización)

---

## 🎓 Resumen Ejecutivo

### Regla de Oro:

**"Si puedes hacer las tareas al mismo tiempo sin esperar resultados entre ellas, HAZLAS en paralelo"**

### Quick Decision Tree:

```
¿Múltiples tareas?
    ├─ SÍ → ¿Son independientes?
    │        ├─ SÍ → PARALELO ✅
    │        └─ NO → SECUENCIAL
    └─ NO → Una sola tarea
```

### Impacto:

- ⚡ **3-5x más rápido**
- 🎯 **Mejor UX**
- 📊 **Mismo costo**
- ✨ **Misma calidad**

---

## 📚 Referencias

- Claude Code Tool Documentation: Task tool
- Best Practices: Context Engineering (BAML team)
- Architecture: Hybrid two-layer system
- Template Version: 3.1.0

---

**Última actualización**: 2025-01-04
**Versión**: 1.0.0
**Estado**: Production Ready
**Mantenedor**: IA Corp - Claude Code Template Team
