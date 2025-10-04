# 📋 Comandos Personalizados de Claude Code

Esta carpeta contiene comandos personalizados que extienden las capacidades de Claude Code específicamente para este proyecto.

---

## 🎯 Comandos Disponibles

### **1. `/update-context`** 🔄

**Propósito**: Actualizar y optimizar todos los archivos de contexto (.md) del proyecto.

**⚠️ DOS MODOS DE OPERACIÓN**:

#### **Modo 1: Proyecto Nuevo (Integrado)**
- **Llamado por**: `/init-project` automáticamente en Fase 0.7
- **NO ejecutar manualmente** antes de init-project
- **Fuente**: Objetivo + tech stack planificado (no código)
- **Output**: Docs base que guían implementación

#### **Modo 2: Proyecto Existente (Standalone)**
**Cuándo usar manualmente**:
- ✅ Después de cambios significativos en el código
- ✅ Cuando el contexto de Claude parece desactualizado
- ✅ Periódicamente (cada 2-3 semanas de desarrollo)
- ✅ NUNCA antes de /init-project en proyecto nuevo

**Qué hace**:
- **Modo Nuevo**: Genera docs desde plan (objetivo + tech stack)
- **Modo Existente**: Actualiza docs analizando código real
- Identifica gaps y redundancias
- Genera/actualiza CLAUDE.md, PLANNING.md, README.md, QUICK_START.md
- Valida consistencia entre archivos
- Crea índice de documentación

**Agentes que usa**:
- @sequential-thinking (análisis)
- @codebase-analyst (análisis de código en modo existente)
- @context-optimizer (optimización)
- @documentation-manager (generación de docs)

**Archivo**: [update-context.md](./update-context.md)

---

### **2. `/init-project`** 🚀

**Propósito**: Inicializar un nuevo proyecto de manera completamente interactiva.

**Cuándo usar**:
- ✅ Al crear un nuevo proyecto desde cero
- ✅ Cuando necesitas setup guiado paso a paso
- ✅ Para proyectos que requieren múltiples APIs/servicios

**Qué hace**:
- Analiza tu objetivo con sequential thinking
- Lee y evalúa agentes existentes
- Crea agentes personalizados para el proyecto
- Setup interactivo de cada API (una a la vez)
- Prueba cada componente inmediatamente
- Genera estructura profesional con tests
- Configura hooks y PRPs
- Genera documentación completa

**Agentes que usa**:
- @project-initializer (orquestador principal)
- @sequential-thinking (análisis profundo)
- @library-researcher (tech stack)
- @codebase-analyst (patrones)
- @[custom]-api-specialist (creado dinámicamente)
- @project-validator (testing)
- @documentation-manager (docs)

**Archivo**: [init-project.md](./init-project.md)

---

### **3. `/prp-create`** 📝

**Propósito**: Crear un PRP (Pattern Recognition Protocol) técnico para una nueva funcionalidad.

**Cuándo usar**:
- ✅ Al planificar una nueva feature
- ✅ Para refactorings complejos
- ✅ Cuando necesitas un plan detallado de implementación

**Qué hace**:
- Analiza el codebase actual
- Identifica patrones existentes
- Genera plan de implementación detallado
- Define tests necesarios
- Crea checklist de validación

**Archivo**: `prp/` (sistema PRP)

---

### **4. `/story-create`** 📖

**Propósito**: Convertir una user story en un PRP ejecutable.

**Cuándo usar**:
- ✅ Cuando tienes una historia de usuario
- ✅ Para features descritas en lenguaje natural
- ✅ Al trabajar con requisitos de negocio

**Qué hace**:
- Analiza la user story
- Extrae requisitos técnicos
- Genera PRP estructurado
- Define criterios de aceptación
- Crea plan de testing

**Archivo**: `prp/` (sistema PRP)

---

## 🔄 Flujo de Trabajo Recomendado

### **Al Iniciar un Proyecto Nuevo**

```bash
# UN SOLO COMANDO (hace todo automáticamente)
/init-project "tu objetivo"

# ¿Qué hace internamente?:
# Fase 0: Sequential thinking sobre objetivo
# Fase 0.5: Análisis y creación de agentes
# Fase 0.7: Generación de docs base (llama /update-context en modo nuevo)
# Fases 1-8: Implementación guiada por docs
# Fase 9: Actualización final de docs con realidad

# Resultado:
# - Documentación completa y optimizada (generada en Fase 0.7)
# - Proyecto funcional con estructura profesional
# - Agentes personalizados creados
# - Tests configurados
# - Hooks integrados
```

**⚠️ NO ejecutes `/update-context` antes de `/init-project`**
El contexto se genera automáticamente en la Fase 0.7 de init-project.

### **Durante el Desarrollo**

```bash
# Opción A: Desde descripción técnica
/prp-create agregar-autenticacion

# Opción B: Desde user story
/story-create "Como usuario quiero poder login con Google"

# Resultado:
# - Plan detallado de implementación
# - Tests definidos
# - Checklist de validación
```

### **Mantenimiento Periódico**

```bash
# Cada 2-3 semanas o después de cambios mayores
/update-context

# Resultado:
# - Docs actualizados con cambios recientes
# - Contexto optimizado para Claude
# - Consistencia entre archivos
```

---

## 🤖 Sistema de Orquestación

Todos estos comandos usan un **sistema de orquestación de agentes**:

```
Usuario
   ↓
Comando (Orquestador)
   ↓
┌─────────────┬─────────────┬─────────────┬─────────────┐
│ @sequential │ @library-   │ @codebase-  │ @custom-    │
│ -thinking   │ researcher  │ analyst     │ agents      │
└─────────────┴─────────────┴─────────────┴─────────────┘
   ↓           ↓             ↓             ↓
   └───────────┴─────────────┴─────────────┘
                     ↓
           Resultados consolidados
                     ↓
                  Usuario
```

**Características**:
- Trabajo en paralelo de múltiples agentes
- Creación dinámica de agentes especializados
- Consolidación inteligente de resultados
- Interacción continua con el usuario

---

## 📊 Comparación de Comandos

| Comando | Cuándo | Agentes | Output | Duración |
|---------|--------|---------|--------|----------|
| `/update-context` | Inicio/Mantenimiento | 3-4 | Docs optimizados | 5-10 min |
| `/init-project` | Nuevo proyecto | 5-8 | Proyecto completo | 20-40 min |
| `/prp-create` | Nueva feature | 2-3 | Plan implementación | 5-10 min |
| `/story-create` | User story | 3-4 | PRP ejecutable | 5-10 min |

---

## ✨ Mejores Prácticas

### **1. Empezar con Contexto Optimizado**
```bash
# SIEMPRE al inicio
/update-context

# Esto asegura que Claude entiende tu proyecto
```

### **2. Interactividad Total**
Todos los comandos son interactivos:
- Muestran análisis antes de actuar
- Piden confirmación en pasos críticos
- Esperan feedback del usuario
- Permiten pausar y ajustar

### **3. Aprovechar Agentes**
Los comandos crean agentes especializados:
- Reutilizables en el proyecto
- Documentados automáticamente
- Optimizados para tareas específicas

### **4. Validación Continua**
Cada comando valida:
- ✅ Antes de aplicar cambios
- ✅ Después de cada paso
- ✅ Al final del proceso

---

## 🎯 Objetivos de los Comandos

Todos los comandos apuntan a:

1. **Maximizar efectividad de Claude**
   - Contexto completo y preciso
   - Información siempre actualizada
   - Uso correcto de capacidades

2. **Acelerar desarrollo**
   - Setup automatizado
   - Planificación estructurada
   - Tests desde el inicio

3. **Mantener calidad**
   - Estructura profesional
   - Documentación completa
   - Best practices aplicadas

4. **Facilitar mantenimiento**
   - Contexto siempre actualizado
   - Arquitectura documentada
   - Decisiones registradas

---

## 📝 Crear Nuevos Comandos

Para agregar un nuevo comando:

1. **Crear archivo** en `.claude/commands/nombre-comando.md`

2. **Seguir estructura**:
   ```markdown
   # Command: nombre-comando

   Descripción del comando

   ## Usage
   ## Arguments
   ## Instrucciones para el Agente
   ## Fases del Comando
   ## Anti-patrones
   ## Checklist
   ```

3. **Documentar en CLAUDE.md**:
   - Agregar a lista de comandos
   - Incluir ejemplo de uso
   - Actualizar flujo de trabajo

4. **Actualizar este README**:
   - Agregar a tabla de comandos
   - Describir cuándo usar
   - Documentar agentes que usa

---

## 🔗 Referencias

- [CLAUDE.md](../../CLAUDE.md) - Documentación completa del proyecto
- [.claude/agents/](../agents/) - Agentes especializados disponibles
- [PRPs/templates/](../../PRPs/templates/) - Templates de PRPs
- [INTERACTIVE_APPROACH.md](../../PRPs/INTERACTIVE_APPROACH.md) - Principios de interactividad

---

**Última actualización**: 2025-01-02
**Comandos disponibles**: 4
**Sistema**: Orquestación de agentes con sequential thinking
