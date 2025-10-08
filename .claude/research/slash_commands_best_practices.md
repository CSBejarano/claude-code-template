# Research: Mejores Prácticas para Comandos Slash en Claude Code

**Fecha**: 2025-10-08
**Investigador**: @library-researcher
**Contexto**: Optimización de comandos slash personalizados para invocar agentes de manera eficiente

---

## 📚 Fuentes de Investigación

### Documentación Oficial

- **Claude Docs - Slash Commands**: https://docs.claude.com/en/docs/claude-code/slash-commands
- **Claude Code GitHub Issues**: https://github.com/anthropics/claude-code/issues/4745
- **Dev.to Guide**: Claude Code Part 4 - Slash Commands and Custom Commands

### Análisis de Código Existente

- `.claude/commands/init-project.md` (1864 líneas) - Comando complejo con orquestación
- `.claude/commands/prp/prp-story-task-create.md` (143 líneas) - Comando de research
- `.claude/commands/prp/prp-story-task-execute.md` (187 líneas) - Comando de ejecución
- `.claude/agents/task-planner.md` - Sistema de coordinación de agentes
- `.claude/agents/prp-expert.md` - Especialista en PRPs con delegación

---

## 🎯 Hallazgos Clave

### 1. **Estructura de Archivos Slash Command**

**ENCONTRADO**: Los comandos slash son archivos Markdown en `.claude/commands/` con frontmatter.

**Anatomía de un Comando**:

````markdown
---
description: "Descripción corta que aparece en /help y en tool description"
allowed-tools: ["Read", "Write", "Edit", "Bash"] # Opcional: restringir tools
argument-hint: "path/to/file" # Opcional: hint para argumentos
model: "sonnet" # Opcional: modelo específico
disable-model-invocation: false # Opcional: prevenir ejecución automática
---

# Command: nombre-comando

Descripción detallada del comando

## Usage

```bash
/nombre-comando [argumentos]
```
````

## Arguments

- `$ARGUMENTS` - Todos los argumentos como string
- `$1`, `$2`, etc. - Argumentos individuales

## Contenido del Comando

[Instrucciones específicas para Claude sobre qué hacer cuando se invoca el comando]

````

**CRÍTICO**: La `description` en frontmatter es lo que Claude ve cuando decide si usar el comando via SlashCommand tool.

---

### 2. **Frontmatter y Metadatos**

**OPCIONES DE FRONTMATTER**:

```yaml
---
# REQUERIDO para SlashCommand tool
description: "Breve descripción (1 línea, max 100 chars)"

# OPCIONAL pero recomendado
argument-hint: "file.md"  # Muestra qué espera el comando
model: "sonnet"           # Usar modelo específico (sonnet/opus/haiku)

# CONTROL DE EJECUCIÓN
disable-model-invocation: false  # Si true, previene auto-ejecución

# RESTRICCIÓN DE HERRAMIENTAS
allowed-tools:
  - "Read"
  - "Write"
  - "Bash"
  - "Task"  # CRÍTICO: Incluir Task si comando invoca agentes
---
````

**BEST PRACTICE**:

- **Descripciones cortas**: Max 100 caracteres, clara y accionable
- **`allowed-tools` explícito**: Siempre incluir `Task` si el comando invoca agentes
- **`argument-hint`**: Ayuda a Claude entender qué parámetros esperar

---

### 3. **Invocación de Agentes desde Comandos**

**PATRÓN DESCUBIERTO**: Claude Code NO tiene una API directa para invocar agentes. Los agentes se invocan IMPLÍCITAMENTE a través del contenido del comando.

**MECANISMO REAL**:

1. **Usuario ejecuta comando**: `/mi-comando arg1 arg2`
2. **Claude lee el archivo markdown**: `.claude/commands/mi-comando.md`
3. **Claude sigue las instrucciones**: El markdown contiene instrucciones que MENCIONAN agentes
4. **Claude decide invocar agentes**: Basado en el contexto y las instrucciones

**PATRÓN INCORRECTO** (No funciona):

```markdown
# ❌ NO EXISTE una API directa tipo:

@invoke-agent("library-researcher", query="...")
```

**PATRÓN CORRECTO** (Funciona):

```markdown
# ✅ Instrucciones que GUÍAN a Claude a usar agentes:

## Mission

Research JWT best practices by:

1. **Use @library-researcher** to find official documentation:
   - Query: "JWT authentication best practices security"
   - Focus: Official docs, security considerations, gotchas

2. **Use @codebase-analyst** IN PARALLEL to analyze existing patterns:
   - Find: Authentication patterns in codebase
   - Extract: Naming conventions, structure patterns

3. **WAIT for both agents** to complete before proceeding

4. **Consolidate findings** from both agents
```

**HALLAZGO CRÍTICO**: Los agentes se invocan mediante **instrucciones en lenguaje natural**, NO mediante llamadas a funciones.

---

### 4. **Orquestación Multi-Agente en Comandos**

**PATRÓN ENCONTRADO en `/init-project`**:

Los comandos complejos actúan como **ORCHESTRADORES** que:

1. **Definen estrategia de agentes** (cuáles usar, en qué orden)
2. **Instruyen ejecución paralela** cuando es seguro
3. **Esperan resultados** antes de continuar
4. **Consolidan outputs** de múltiples agentes

**EJEMPLO REAL de `/init-project`** (líneas 170-223):

```markdown
### **Fase 0.5: Análisis y Gestión de Agentes**

**OBLIGATORIO antes de crear el proyecto:**

1. ANALIZAR AGENTES EXISTENTES:

   "🤖 Analizando agentes disponibles...

   Leyendo: .claude/agents/"

   [Lee todos los archivos .md en .claude/agents/]

   Agentes encontrados:
   - codebase-analyst.md: Analiza patrones de código
   - library-researcher.md: Investiga librerías
   - [otros agentes...]

2. EVALUAR RELEVANCIA:

   [Usa @mcp__server-sequential-thinking__sequentialthinking]

   "Evaluando qué agentes son útiles para tu proyecto:

   📊 Análisis de relevancia:

   ✅ ÚTILES para este proyecto:
   - codebase-analyst: Necesario para [razón específica]
   - library-researcher: Necesario para [razón específica]

   ⚠️ PARCIALMENTE ÚTILES (necesitan adaptación):
   - [agente-x]: Útil pero requiere [modificación]

   ❌ NO RELEVANTES:
   - [agente-y]: No aplica para este tipo de proyecto
```

**BEST PRACTICE**:

- **Fase 0**: Analizar qué agentes existen (leer `.claude/agents/`)
- **Fase 1**: Decidir cuáles usar (Sequential Thinking ayuda)
- **Fase 2**: Definir estrategia de delegación (quién hace qué)
- **Fase 3**: Ejecutar en paralelo o secuencial según dependencias
- **Fase 4**: Consolidar resultados

---

### 5. **Ejecución Paralela vs Secuencial**

**PATRÓN DESCUBIERTO en `/init-project`** (líneas 280-325):

```markdown
### **Orquestación Paralela de Agentes**

Durante la creación del proyecto, el orquestador usa agentes en paralelo:
```

Ejemplo - Fase de Análisis:

"🔄 Ejecutando análisis paralelo con 3 agentes...

[PARALELO]
├──> @sequential-thinking
│ └─> Analizando arquitectura del proyecto...
│
├──> @library-researcher
│ └─> Investigando mejores librerías para Gmail API...
│
└──> @codebase-analyst
└─> Buscando patrones similares en proyectos existentes...

[ESPERAR RESULTADOS]

✅ Análisis completado (3/3 agentes)

📊 Resultados consolidados:
[...]

```

```

**CUÁNDO USAR PARALELO**:

- ✅ Agentes trabajan en **datos diferentes** (ej: uno research externo, otro patterns internos)
- ✅ No hay **dependencias entre outputs**
- ✅ Pueden **fallar independientemente** sin afectar al otro

**CUÁNDO USAR SECUENCIAL**:

- ❌ Output del agente A es **input del agente B**
- ❌ Agente B necesita **decisión humana** del output de A
- ❌ Orden importa para **coherencia**

**SINTAXIS PARA INDICAR PARALELISMO**:

```markdown
## Phase 1: Research (PARALELO)

Execute these agents IN PARALLEL:

**Agent 1: @library-researcher**

- Query: [...]
- MCPs: tavily-search, WebFetch
- Duration: ~15 min

**Agent 2: @codebase-analyst**

- Query: [...]
- MCPs: serena find_symbol, search_for_pattern
- Duration: ~10 min

**WAIT** for BOTH agents to complete before Phase 2.

## Phase 2: Consolidation (SECUENCIAL)

After Phase 1 completes:

1. Analyze findings from @library-researcher
2. Analyze findings from @codebase-analyst
3. Synthesize recommendations
```

---

### 6. **Checkpoints y Validación Humana**

**HALLAZGO CRÍTICO**: Los mejores comandos incluyen **CHECKPOINTS explícitos** donde Claude DEBE esperar aprobación humana.

**PATRÓN ENCONTRADO en `task-planner.md`** (CHECKPOINT 1 y 2):

```markdown
### ✅ CHECKPOINT 1: Research Validation (ROI 100x)

**CRITICAL**: NEVER skip this checkpoint. ROI is 100x.

**Present research findings to user:**
```

═══════════════════════════════════════════════════════
🔍 RESEARCH PHASE COMPLETE (CHECKPOINT 1)
═══════════════════════════════════════════════════════

[... summary de research ...]

⚠️ CRITICAL VALIDATION QUESTIONS:

1. Does the recommended approach align with your vision?
2. Are there any gotchas we missed?
3. Do you have answers to the open questions?
4. Should we research anything else before planning?
5. Is this direction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Options:
✅ "approve" - Research is solid, proceed to planning
🔄 "fix: [description]" - Research needs adjustment
❌ "restart" - Wrong direction, redo research
❓ "answer: [answers to questions]" - Provide missing info
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**WAIT FOR USER RESPONSE** - Do NOT proceed without approval.

```

**IMPORTANT**:
- **WAIT** for user to respond with "approve", "fix", "restart", or "answer"
- **NEVER assume** user approves
- **NEVER skip** this checkpoint - ROI is 100x
```

**BEST PRACTICE para CHECKPOINTS**:

1. **Presentar resumen claro** con viñetas
2. **Hacer preguntas críticas** que requieren decisión humana
3. **Ofrecer opciones explícitas**: approve / fix / restart
4. **WAIT FOR USER RESPONSE** - nunca continuar sin respuesta
5. **Documentar decisión** en memoria o planning doc

**CUÁNDO INCLUIR CHECKPOINTS**:

- ✅ Después de **research phase** (ROI 100x - previene 1000s líneas mal dirigidas)
- ✅ Después de **planning phase** (ROI 10-20x - previene 10-100 líneas re-trabajo)
- ✅ Antes de **decisiones arquitectónicas** irreversibles
- ✅ Antes de **ejecutar cambios destructivos** (eliminación de código, migración)

---

### 7. **Manejo de Contexto y Referencias**

**HALLAZGO**: Los comandos que invocan agentes deben pasar **contexto completo** porque agentes NO tienen acceso al historial del usuario.

**PATRÓN ENCONTRADO en `/prp-story-task-create`** (líneas 19-23):

```markdown
## Mission

Transform a user story or task into a **tactical implementation PRP** through systematic codebase analysis and task decomposition.

We do not write any code in this step, the goal is to create a detailed context-engineered implementation plan for the implementation agent.

**Key Principle**: We must first gather the context about the story/task before proceeding with the analysis.

When we understand the story/task, we can proceed with the codebase analysis. We systematically dig deep into the codebase to gather intelligence and identify patterns and implementation points. We then use this information to create a PRP that can be executed by a coding agent.

**The contents of the created PRP should encapsulate all the information the agent needs to complete the story/task in one pass.**

Remember that subagents will only receive details from you; the user cannot interact with them directly. Therefore, include all relevant context in the subagent prompt and TODO.
```

**BEST PRACTICE**:

- **Pasar TODA la info necesaria**: User story, archivos relevantes, decisiones tomadas
- **No asumir conocimiento previo**: Agentes solo ven lo que el comando les pasa
- **Usar `$ARGUMENTS` para datos del usuario**: `/comando user-story-aquí`
- **Referenciar archivos explícitamente**: "Analyze src/auth/oauth.py lines 45-67"

**PATRÓN DE PASO DE CONTEXTO**:

```markdown
## Step 2: Invoke @library-researcher

**Context to pass**:

- **User Goal**: $ARGUMENTS (from command invocation)
- **Tech Stack**: [Language/Framework discovered in Step 1]
- **Existing Patterns**: [Patterns from @codebase-analyst]
- **Constraints**: [Any constraints user mentioned]

**Query for agent**:
"Research best practices for JWT authentication in [Language/Framework].

Context:

- User wants to implement: $ARGUMENTS
- Project uses: [tech stack]
- Existing auth patterns: [summary]

Find:

1. Recommended libraries (with security considerations)
2. Implementation best practices
3. Common gotchas and how to avoid them
4. Testing strategies

Focus on: Production-ready patterns, not hello-world examples."
```

---

### 8. **Gestión de Errores y Fallbacks**

**PATRÓN ENCONTRADO en `/prp-story-task-execute`** (líneas 132-146):

```markdown
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
```

**BEST PRACTICE para ERROR HANDLING en comandos**:

```markdown
## Error Handling Strategy

If [operation] fails:

### Step 1: Diagnose

- Read error message carefully
- Identify which phase/task failed
- Check logs/output for root cause

### Step 2: Consult Memory

- Use @archon-expert to query: "similar error: [error type]"
- Check if this error is documented in `.claude/memories/`

### Step 3: Attempt Fix

- Apply known solution if available
- Otherwise, analyze with @sequential-thinking:
  - What went wrong?
  - What are possible causes?
  - What are potential fixes?

### Step 4: Retry with Validation

- Apply fix
- Re-run validation command
- Verify error is resolved

### Step 5: Document Solution (if new)

- Store in `.claude/memories/` via @archon-expert
- Update relevant documentation
- Add to troubleshooting section

**FALLBACK**: If stuck after 3 retries:

- Present error to user with analysis
- Ask for guidance
- Options: ["debug together", "skip and continue", "restart phase"]
```

---

### 9. **SlashCommand Tool (Invocación Programática)**

**HALLAZGO IMPORTANTE**: Claude puede invocar comandos slash **programáticamente** usando el tool `SlashCommand`.

**DOCUMENTACIÓN OFICIAL**:

```
The SlashCommand tool allows Claude to execute custom slash commands
programmatically during a conversation.
```

**CUÁNDO SE USA**:

- Claude decide que un comando es relevante para la tarea actual
- Solo si el comando tiene `description` en frontmatter
- Solo comandos permitidos (no en disable list)

**LIMITACIONES**:

- **Budget de 15,000 caracteres**: El comando expandido no puede exceder este límite
- **Sin interactividad**: Comandos invocados programáticamente NO pueden pedir input intermedio
- **Ejecuta TODO el comando**: No hay control granular de qué partes ejecutar

**ISSUE DESCUBIERTO** (GitHub #4745):

- Algunos comandos están siendo ejecutados automáticamente via SlashCommand tool cuando NO deberían
- Rompe flujos interactivos que esperan input del usuario
- **Workaround temporal**: Usar `disable-model-invocation: true` en frontmatter

**BEST PRACTICE**:

- **Comandos cortos (<15k chars)**: OK para invocación automática
- **Comandos interactivos**: Agregar `disable-model-invocation: true` hasta que issue se resuelva
- **Comandos de orquestación**: Mejor invocar manualmente `/comando arg`

---

### 10. **Naming Conventions y Namespacing**

**PATRÓN ENCONTRADO**:

Los comandos pueden organizarse en **namespaces** usando directorios:

```
.claude/commands/
├── init-project.md          → /init-project
├── update-context.md        → /update-context
└── prp/                     → Namespace "prp:"
    ├── prp-story-task-create.md     → /prp:prp-story-task-create
    ├── prp-story-task-execute.md    → /prp:prp-story-task-execute
    └── prp-validate.md              → /prp:prp-validate
```

**NAMING BEST PRACTICES**:

- **Kebab-case**: `mi-comando.md` → `/mi-comando`
- **Namespaces con `:``**: Carpeta `prp/` → comandos con prefijo `/prp:`
- **Nombres descriptivos**: `/create-feature-prp` mejor que `/cfp`
- **Verbos al inicio**: `/create-*`, `/execute-*`, `/validate-*`

---

## 🎨 Patrones Recomendados

### **Patrón 1: Comando Simple de Research**

**Caso de uso**: Research de una biblioteca específica

````markdown
---
description: "Research [library] best practices and integration patterns"
argument-hint: "library-name"
---

# Command: research-library

## Usage

```bash
/research-library jwt
```
````

## Mission

Research implementation-critical documentation for $ARGUMENTS library.

## Process

### Step 1: Use @library-researcher

Query: "Research $ARGUMENTS best practices, security considerations, gotchas"

Focus:

- Official documentation
- Production-ready patterns
- Security implications
- Common pitfalls

### Step 2: Use @archon-expert (Parallel)

Query RAG knowledge base: "previous implementations using $ARGUMENTS"

### Step 3: Consolidate Findings

Create document: `/research/research_$ARGUMENTS.md`

Include:

- Best practices discovered
- Recommended approach
- Critical gotchas
- Integration examples

### Step 4: Present to User

Show findings summary and ask for approval before using in implementation.

````

---

### **Patrón 2: Comando de Orquestación Multi-Fase**

**Caso de uso**: Creación de feature completa con checkpoints

```markdown
---
description: "Create and execute complete feature implementation with checkpoints"
argument-hint: "feature-description"
allowed-tools: ["Read", "Write", "Edit", "Bash", "Task", "TodoWrite"]
---

# Command: create-feature

## Usage
```bash
/create-feature "Add payment processing with Stripe"
````

## Mission

Implement complete feature with research → planning → implementation → validation flow.

## Process (4 Phases with 2 Checkpoints)

### Phase 1: Research (45-60 min, PARALLEL)

**Invoke BOTH agents in parallel:**

#### Agent 1: @library-researcher

- Research: External best practices for feature
- Duration: ~30 min
- MCPs: tavily-search, WebFetch, perplexity-ask

#### Agent 2: @codebase-analyst

- Analyze: Internal patterns for similar features
- Duration: ~20 min
- MCPs: serena find_symbol, search_for_pattern

**WAIT** for both agents to complete.

**Output**: Create `/research/research_[feature].md`

### ✅ CHECKPOINT 1: Research Validation (ROI 100x)

```
═══════════════════════════════════════════════════════
🔍 RESEARCH COMPLETE - CHECKPOINT 1
═══════════════════════════════════════════════════════

Summary: [Consolidated findings from both agents]

Critical Questions:
1. Is the recommended approach correct?
2. Any missing considerations?
3. Should we proceed to planning?

Options: approve / fix: [desc] / restart

**WAIT FOR USER RESPONSE**
═══════════════════════════════════════════════════════
```

### Phase 2: Planning (30-45 min)

Use @task-planner with Sequential Thinking:

- Decompose feature into atomic tasks
- Define validation strategy
- Estimate time
- Identify dependencies

**Output**: Create `/planning/planning_[feature].md`

### ✅ CHECKPOINT 2: Planning Validation (ROI 10-20x)

```
═══════════════════════════════════════════════════════
📋 PLANNING COMPLETE - CHECKPOINT 2
═══════════════════════════════════════════════════════

Summary: [Task breakdown, file structure, estimates]

Critical Questions:
1. Does file structure make sense?
2. Are tasks atomic enough?
3. Time estimates realistic?

Options: approve / fix: [desc] / restart

**WAIT FOR USER RESPONSE**
═══════════════════════════════════════════════════════
```

### Phase 3: TDD Implementation (2-4 hours)

Delegate to @task-executor:

- Execute plan from Phase 2
- TDD approach (tests FIRST)
- Validate after EACH task
- Track progress with TodoList

### Phase 4: Final Validation (30 min)

Use @validation-gates:

- Level 1: Syntax/style
- Level 2: Unit tests
- Level 3: Integration tests
- Level 4: Build

**Success**: All levels pass → Feature complete ✅

````

---

### **Patrón 3: Comando de Validación Standalone**

**Caso de uso**: Validar PRPs, código, o documentación

```markdown
---
description: "Validate [artifact] using [criteria]"
argument-hint: "path/to/artifact.md"
---

# Command: validate-prp

## Usage
```bash
/validate-prp PRPs/story_auth.md
````

## Mission

Validate PRP using Pareto 80-20 scoring criteria.

## Process

### Step 1: Read PRP

Read file: $1

### Step 2: Use @prp-validator

Invoke agent with PRP contents:

- Score using Pareto 80-20 (80 critical + 20 nice-to-have)
- Tier 1 (80 pts): Current vs Desired, Mixed References, Specific Logic, Actionable Steps
- Tier 2 (20 pts): Validation gates, Clear constraints

### Step 3: Present Results

If score >= 80:

```
✅ VALIDATION PASSED (Score: [X]/100)

The PRP meets critical requirements and is ready for execution.

Breakdown:
- Tier 1 Critical: [X]/80 pts
- Tier 2 High: [X]/20 pts

Strengths: [list]
Suggestions: [optional improvements]
```

If score < 80:

```
⚠️ VALIDATION FAILED (Score: [X]/100)

The PRP needs improvement before execution.

Issues Found:
- [Issue 1]: [Description] (-[Y] pts)
- [Issue 2]: [Description] (-[Z] pts)

Recommended Fixes:
1. [Fix for issue 1]
2. [Fix for issue 2]

Auto-improve? (yes/no)
```

### Step 4: Auto-Improvement Loop (if requested)

If user says "yes":

- Apply fixes using @prp-expert
- Re-validate
- Max 3 iterations
- If stuck after 3: Request manual review

### Step 5: Backup & Document

- Create backup: `[file].backup-[timestamp]`
- Document validation in: `/validation/validation_[file]_[date].md`

````

---

### **Patrón 4: Comando de Setup Interactivo**

**Caso de uso**: Configurar API, servicio, o herramienta paso a paso

```markdown
---
description: "Setup [service] with interactive step-by-step guidance"
argument-hint: "service-name"
disable-model-invocation: true  # Prevent auto-execution (interactive)
---

# Command: setup-service

## Usage
```bash
/setup-service stripe
````

## Mission

Guide user through $ARGUMENTS setup with interactive validation.

## Philosophy

**NEVER**: Dump 50 steps → User gets lost
**ALWAYS**: Step → Validate → Confirm → Next step

## Process

### Step 1: Research Service

Use @library-researcher:

- Query: "$ARGUMENTS setup guide official documentation"
- Find: Step-by-step setup instructions
- Extract: Required credentials, configuration

**Output**: List of setup steps with exact URLs

### Step 2: Interactive Setup Loop

For each setup step:

```
📡 $ARGUMENTS Setup - Step [N]/[TOTAL]

[Step description]

1️⃣ Go to: [EXACT URL]

2️⃣ [Specific action]

3️⃣ [Next action]

✅ Done? (yes/no/error: [message])
```

**WAIT** for user response.

If "yes": Continue to next step
If "no": Ask "What went wrong?"
If "error: [msg]": Debug error, provide solution, retry

### Step 3: Validate Configuration

After all steps complete:

```bash
# Test $ARGUMENTS connection
[validation command]
```

Expected output: [describe expected result]

Did you see this? (yes/no)

### Step 4: Celebrate & Document

If validation passes:

```
🎉 $ARGUMENTS completely configured!

✅ Summary:
   - [Step 1] ✓
   - [Step 2] ✓
   - [Step 3] ✓
   - Validation passed ✓

Next: [What user can do now]
```

Update documentation:

- Add setup to README.md
- Add env vars to .env.example
- Create usage guide in docs/

````

---

## 📋 Recomendaciones Específicas por Tipo de Comando

### **Comandos de Research**

**Características**:
- Deben invocar @library-researcher (externo) + @codebase-analyst (interno)
- Ejecución en **PARALELO** para eficiencia
- Generar documento `/research/research_[topic].md`
- Incluir CHECKPOINT con findings para validación humana

**Template**:
```markdown
---
description: "Research [topic] with parallel external + internal analysis"
argument-hint: "topic"
---

# Research [Topic]

## Phase 1: Parallel Research (15-30 min)

[PARALELO]
├─> @library-researcher: External best practices
└─> @codebase-analyst: Internal patterns

## Phase 2: Consolidate

Combine findings from both agents

## ✅ CHECKPOINT: Present findings

WAIT FOR APPROVAL before using in implementation
````

---

### **Comandos de Planning**

**Características**:

- Deben usar **Sequential Thinking** (8-15 adaptive thoughts)
- Generar YAML plan estructurado
- Incluir validation strategy
- Definir checkpoints humanos
- Generar documento `/planning/planning_[feature].md`

**Template**:

```markdown
---
description: "Plan [feature] with Sequential Thinking and structured output"
argument-hint: "feature-description"
allowed-tools: ["Task", "TodoWrite"]
---

# Plan [Feature]

## Phase 1: Sequential Thinking Analysis

Use @mcp**server-sequential-thinking**sequentialthinking:

- Thought 1-3: Understand scope
- Thought 4-7: Identify dependencies
- Thought 8-12: Design approach
- Thought 13-15: Validate coherence

## Phase 2: Generate YAML Plan

Structure:

- Phases with tasks
- Dependencies
- Validation commands
- Checkpoints

## ✅ CHECKPOINT: Validate Plan

Present plan for approval with critical questions
```

---

### **Comandos de Execution**

**Características**:

- Deben usar **TDD approach** (tests FIRST)
- Invocar @validation-gates **después de CADA cambio**
- Track progress con TodoWrite tool
- Handle errors con retry logic
- Document deviations from plan

**Template**:

```markdown
---
description: "Execute [plan] with TDD and continuous validation"
argument-hint: "path/to/plan.md"
allowed-tools: ["Read", "Write", "Edit", "Bash", "TodoWrite", "Task"]
---

# Execute [Plan]

## Phase 1: Load Plan

Read: $1

## Phase 2: Task-by-Task Execution

For each task:

1. Write failing test (TDD)
2. Implement minimum code
3. Run test (should pass)
4. Invoke @validation-gates
5. Mark task complete in TodoList
6. ONLY proceed if validation passes

## Phase 3: Final Validation

@validation-gates full suite:

- Level 1: Syntax
- Level 2: Style
- Level 3: Tests
- Level 4: Build

## Phase 4: Document Completion

Move plan to completed/
Update relevant docs
```

---

### **Comandos de Validation**

**Características**:

- Deben tener **criterios claros de pass/fail**
- Generar **validation reports**
- Ofrecer **auto-improvement** cuando falla
- Limitar iterations (max 3) para evitar loops infinitos

**Template**:

```markdown
---
description: "Validate [artifact] using [criteria]"
argument-hint: "path/to/artifact"
---

# Validate [Artifact]

## Step 1: Load Artifact

Read: $1

## Step 2: Apply Validation Criteria

Check:

- [ ] Criterion 1 (critical)
- [ ] Criterion 2 (critical)
- [ ] Criterion 3 (nice-to-have)

Score: [X]/100 (80 critical + 20 nice-to-have)

## Step 3: Report Results

If pass (>=80): ✅ Report strengths, optional improvements
If fail (<80): ⚠️ Report issues, recommended fixes

## Step 4: Auto-Improvement (Optional)

If user approves:

- Apply fixes
- Re-validate
- Max 3 iterations
- Document all changes
```

---

### **Comandos Interactivos**

**Características**:

- Deben tener `disable-model-invocation: true` (hasta que issue #4745 se resuelva)
- **WAIT FOR USER** después de cada paso crítico
- Ofrecer opciones claras: yes/no/error
- Include **debugging guidance** cuando falla
- **Celebrar pequeños logros** para mantener motivación

**Template**:

```markdown
---
description: "Setup [service] with interactive step-by-step guidance"
disable-model-invocation: true
---

# Interactive Setup: [Service]

## Philosophy

NEVER: Dump all steps
ALWAYS: Step → Validate → Confirm → Next

## Loop Pattern

For each step:
```

[N]/[TOTAL]: [Step description]

1️⃣ Action: [Specific instruction]
2️⃣ Go to: [EXACT URL if applicable]
3️⃣ Expected result: [What user should see]

✅ Done? (yes/no/error: [msg])

```

WAIT for response

If yes: Next step
If no: "What went wrong?"
If error: Debug → Fix → Retry

## Validation After All Steps

Run test command
WAIT for confirmation
Celebrate success 🎉
```

---

## ⚠️ Anti-Patrones (Qué NO Hacer)

### ❌ **Anti-Patrón 1: Invocar Agentes sin Contexto**

**MAL**:

```markdown
## Step 1: Research

Use @library-researcher to find JWT best practices.
```

**BIEN**:

```markdown
## Step 1: Research with Full Context

Use @library-researcher to research JWT authentication:

**Context**:

- User wants to implement: $ARGUMENTS
- Project uses: [tech stack from analysis]
- Existing auth patterns: [summary from @codebase-analyst]

**Query**:
"Research JWT authentication best practices for [tech stack].

Focus:

1. Production-ready libraries (security track record)
2. Common pitfalls and how to avoid them
3. Testing strategies for JWT flows
4. Token refresh patterns

Constraints:

- Must integrate with existing auth in src/auth/
- Performance target: <50ms token validation

Output: `/research/research_jwt.md` with findings"
```

---

### ❌ **Anti-Patrón 2: Asumir Aprobación en Checkpoints**

**MAL**:

```markdown
## Checkpoint

Present findings to user.

## Next Phase

Continue with implementation...
```

**BIEN**:

```markdown
## ✅ CHECKPOINT: Research Validation

Present findings:
```

[... summary ...]

Critical Questions:

1. [Question 1]
2. [Question 2]

Options: approve / fix: [desc] / restart

**WAIT FOR USER RESPONSE - Do NOT proceed without approval**

```

**IMPORTANT**: NEVER assume user approved. ALWAYS wait for explicit response.

## Next Phase (ONLY after "approve")

Continue with implementation...
```

---

### ❌ **Anti-Patrón 3: Comandos Monolíticos Sin Fases**

**MAL**:

```markdown
## Mission

Create feature, run tests, update docs, and deploy.

[Giant block of instructions without structure]
```

**BIEN**:

```markdown
## Mission

Implement feature with structured phases and validation.

## Phase 1: Research (30 min)

[...] → CHECKPOINT 1

## Phase 2: Planning (20 min)

[...] → CHECKPOINT 2

## Phase 3: Implementation (2 hrs)

[...] → Validation gates after each task

## Phase 4: Documentation (15 min)

[...] → Final validation
```

---

### ❌ **Anti-Patrón 4: Ignorar Capacidades de Agentes**

**MAL**:

```markdown
## Step 1

Read all files in src/ to understand patterns.
[Manual file reading with Read tool]
```

**BIEN**:

```markdown
## Step 1: Pattern Analysis

Use @codebase-analyst to systematically analyze patterns:

Query: "Analyze authentication patterns in src/auth/"

The agent will:

- Use serena find_symbol to find auth classes
- Use serena search_for_pattern to extract conventions
- Use serena get_symbols_overview for structure
- Consolidate into pattern summary

This is MUCH more efficient than manual file reading.
```

---

### ❌ **Anti-Patrón 5: Olvidar `allowed-tools` para Agentes**

**MAL**:

```markdown
---
description: "Command that invokes agents"
---

[Command invokes @library-researcher, but Task tool not in allowed-tools]
```

**BIEN**:

```markdown
---
description: "Command that invokes agents"
allowed-tools:
  - "Task" # CRÍTICO: Needed to invoke agents
  - "Read" # For reading files
  - "Write" # For creating outputs
  - "TodoWrite" # For tracking progress
---
```

---

### ❌ **Anti-Patrón 6: Descriptions Vagas en Frontmatter**

**MAL**:

```markdown
---
description: "Do stuff with code"
---
```

**BIEN**:

```markdown
---
description: "Research JWT authentication best practices and create implementation PRP"
---
```

La description es CRÍTICA porque es lo que Claude ve cuando decide si usar el comando via SlashCommand tool.

---

## 🎯 Checklist de Calidad para Comandos Slash

### **Estructura Básica**

- [ ] Frontmatter completo con `description`
- [ ] `argument-hint` si el comando espera argumentos
- [ ] `allowed-tools` incluye "Task" si invoca agentes
- [ ] Uso claro de `$ARGUMENTS`, `$1`, `$2` para parámetros
- [ ] Secciones organizadas: Usage, Arguments, Mission, Process

### **Invocación de Agentes**

- [ ] Agentes especificados explícitamente (@nombre-agente)
- [ ] Contexto completo pasado a cada agente (no asumir conocimiento)
- [ ] Indica PARALELO o SECUENCIAL claramente
- [ ] WAIT statements antes de continuar después de agentes
- [ ] Consolidación de resultados de múltiples agentes

### **Checkpoints y Validación**

- [ ] CHECKPOINT después de research (ROI 100x)
- [ ] CHECKPOINT después de planning (ROI 10-20x)
- [ ] Presenta opciones claras (approve/fix/restart)
- [ ] **WAIT FOR USER RESPONSE** explícito
- [ ] NUNCA asume aprobación, siempre espera respuesta

### **Manejo de Errores**

- [ ] Estrategia de error handling definida
- [ ] Retry logic con límite (max 3 iterations)
- [ ] Fallback plan si stuck
- [ ] Documentación de soluciones en memoria
- [ ] Debugging guidance para errores comunes

### **Documentación de Outputs**

- [ ] Outputs guardados en estructura clara (/research/, /planning/, etc.)
- [ ] Formato consistente (markdown, YAML, etc.)
- [ ] Validation reports generados
- [ ] Memoria actualizada con learnings

### **Performance y Eficiencia**

- [ ] Uso de ejecución paralela cuando es seguro
- [ ] Time estimates incluidos por fase
- [ ] Context window management (<50% usage)
- [ ] Reutilización de agentes existentes (no reinventar)

---

## 📊 Comparación: Antes vs Después

### **Comando ANTES de aplicar best practices**

```markdown
---
description: "Create feature"
---

# Create Feature

Use @library-researcher and @codebase-analyst to research.
Then create PRP.
Then execute PRP.
```

**Problemas**:

- ❌ No context para agentes
- ❌ No checkpoints
- ❌ No validation strategy
- ❌ No error handling
- ❌ No outputs definidos
- ❌ No parallel execution
- ❌ Descripción vaga

---

### **Comando DESPUÉS de aplicar best practices**

````markdown
---
description: "Research, plan, and implement feature with checkpoints and validation"
argument-hint: "feature-description"
allowed-tools: ["Read", "Write", "Edit", "Bash", "Task", "TodoWrite"]
---

# Command: create-feature-complete

## Usage

```bash
/create-feature-complete "Add payment processing with Stripe"
```
````

## Mission

Transform feature request into production-ready implementation with:

- Research phase (ROI 100x)
- Planning phase (ROI 10-20x)
- TDD implementation
- Multi-level validation

## Process (4 Phases, 2 Checkpoints)

### Phase 1: Research (45-60 min, PARALLEL)

**Context**:

- Feature request: $ARGUMENTS
- Project tech stack: [will be detected]

**Execute in PARALLEL**:

#### Agent 1: @library-researcher (~30 min)

Query: "Research best practices for implementing: $ARGUMENTS

Focus:

1. Production-ready libraries (security + maintenance)
2. Common pitfalls and solutions
3. Testing strategies
4. Integration patterns

Output: External best practices"

#### Agent 2: @codebase-analyst (~20 min)

Query: "Analyze existing patterns similar to: $ARGUMENTS

Find:

1. Naming conventions (classes, functions, files)
2. Code structure patterns
3. Integration patterns
4. Testing patterns

Output: Internal conventions"

**WAIT** for both agents to complete.

**Consolidate**: Create `/research/research_[feature].md`

### ✅ CHECKPOINT 1: Research Validation (ROI 100x)

```
═══════════════════════════════════════════════════════
🔍 RESEARCH COMPLETE - CHECKPOINT 1
═══════════════════════════════════════════════════════

📚 FINDINGS SUMMARY:

**External Best Practices** (@library-researcher):
- [Practice 1]
- [Practice 2]
- [Critical Gotcha 1]

**Internal Patterns** (@codebase-analyst):
- Naming: [conventions]
- Structure: [patterns]
- Testing: [approach]

**Recommended Approach**:
[Synthesis of findings]

⚠️ CRITICAL QUESTIONS:

1. Does recommended approach align with your vision?
2. Any gotchas we missed?
3. Should we research anything else?
4. Is this direction correct?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Options:
✅ "approve" - Proceed to planning
🔄 "fix: [description]" - Adjust research
❌ "restart" - Wrong direction, redo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**WAIT FOR USER RESPONSE** - Do NOT proceed without approval.
═══════════════════════════════════════════════════════
```

**IF user responds "approve"**, continue. **IF "fix" or "restart"**, adjust and re-present.

### Phase 2: Planning (30-45 min)

Use @task-planner with Sequential Thinking:

Query: "Create detailed implementation plan for: $ARGUMENTS

Context:

- Research findings: [from Phase 1]
- Recommended approach: [from Checkpoint 1]

Output: Structured YAML plan with:

- Phases with atomic tasks
- Dependencies
- Validation commands
- Time estimates
- Success criteria"

**Output**: Create `/planning/planning_[feature].md`

### ✅ CHECKPOINT 2: Planning Validation (ROI 10-20x)

```
═══════════════════════════════════════════════════════
📋 PLANNING COMPLETE - CHECKPOINT 2
═══════════════════════════════════════════════════════

🎯 PLAN SUMMARY:

**Total Phases**: [N]
**Total Tasks**: [M]
**Estimated Time**: [X hours]

**Phase Breakdown**:
- Phase 1: [description] (~[Y] min)
- Phase 2: [description] (~[Z] min)
- ...

**Files to Create/Modify**:
- [file1]: [purpose]
- [file2]: [purpose]

**Dependencies to Add**:
- [package1]: [version] - [reason]
- [package2]: [version] - [reason]

⚠️ CRITICAL QUESTIONS:

1. Does file structure make sense?
2. Are tasks atomic enough?
3. Time estimates realistic?
4. Any missing steps?
5. Approve plan for execution?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Options:
✅ "approve" - Execute plan
🔄 "fix: [description]" - Adjust plan
❌ "restart" - Redo planning
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**WAIT FOR USER RESPONSE** - Do NOT proceed without approval.
═══════════════════════════════════════════════════════
```

**IF user responds "approve"**, continue. **IF "fix" or "restart"**, adjust and re-present.

### Phase 3: TDD Implementation (2-4 hours)

Delegate to @task-executor:

Query: "Execute plan from: /planning/planning\_[feature].md

Approach:

- TDD: Write failing tests FIRST
- Implement: Minimum code to pass tests
- Validate: Use @validation-gates after EACH task
- Track: Update TodoList for progress

Stop if: Any validation fails (iterate until passes)

Output: Implemented feature with passing tests"

@task-executor will:

1. Parse YAML plan
2. Create TodoList from tasks
3. For each task:
   - Write failing test
   - Implement code
   - Run test (should pass)
   - Run @validation-gates
   - Mark complete
4. Report progress continuously

### Phase 4: Final Validation (30 min)

Use @validation-gates full suite:

```bash
# Level 1: Syntax
[linting command]

# Level 2: Style
[formatting command]

# Level 3: Tests
[test suite command]

# Level 4: Build
[build command]
```

**Success Criteria**: All 4 levels pass ✅

### Phase 5: Documentation & Completion

Update documentation:

- README.md: Add feature usage
- CLAUDE.md: Update if architecture changed
- API docs: Document new endpoints/functions

Store learnings in memory:

- Pattern used: /`.claude/memories/pattern_[feature].md`
- Decisions made: `.claude/memories/decision_[feature].md`

Move plan to completed:

- `PRPs/completed/planning_[feature].md`

## Error Handling

### If Research Phase Fails

- Retry with more specific query
- Consult different sources
- Ask user for clarification
- Max 2 retries, then present partial findings

### If Planning Phase Fails

- Use Sequential Thinking to debug
- Simplify into smaller phases
- Consult @archon-expert for similar patterns
- Present adjusted plan for approval

### If Implementation Fails

- @validation-gates identifies exact failure
- Retry fix with @code-executor
- Max 3 retries per task
- If stuck: Present to user with analysis

### If Validation Fails

- Analyze failure reason
- Apply known fixes
- Document new solutions in memory
- Iterate until all levels pass

## Success Metrics

Feature is complete when:

- [ ] All tasks in plan executed
- [ ] All tests passing (100% of new code)
- [ ] All 4 validation levels pass
- [ ] Documentation updated
- [ ] Learnings stored in memory
- [ ] Plan moved to completed/

```

**Ventajas**:
- ✅ Full context para agentes
- ✅ 2 Checkpoints críticos (ROI 100x + 10-20x)
- ✅ Validation strategy clara (4 levels)
- ✅ Error handling comprehensivo
- ✅ Outputs estructurados y documentados
- ✅ Parallel execution donde es seguro
- ✅ Descripción accionable en frontmatter

---

## 🔗 Referencias y Recursos

### Documentación Oficial
- [Claude Docs - Slash Commands](https://docs.claude.com/en/docs/claude-code/slash-commands)
- [Claude Code GitHub](https://github.com/anthropics/claude-code)

### Ejemplos en Este Proyecto
- `.claude/commands/init-project.md` - Orquestación compleja
- `.claude/commands/prp/prp-story-task-create.md` - Research command
- `.claude/commands/prp/prp-story-task-execute.md` - Execution command
- `.claude/agents/task-planner.md` - Coordinación de agentes
- `.claude/agents/prp-expert.md` - Delegación de tareas

### Artículos y Guías
- [Claude Code Part 4 - Slash Commands](https://dev.to/letanure/claude-code-part-4-slash-commands-and-custom-commands-4fkf)
- [Practical Guide to Claude Code Slash Commands](https://www.eesel.ai/blog/claude-code-slash-commands)

---

## ✅ Conclusiones y Próximos Pasos

### **Hallazgos Principales**

1. **No hay API directa para invocar agentes** - Se usan instrucciones en lenguaje natural
2. **Checkpoints son críticos** - ROI 100x (research) y 10-20x (planning)
3. **Contexto completo es obligatorio** - Agentes no ven historial del usuario
4. **Parallel execution ahorra tiempo** - Cuando tareas son independientes
5. **Validation continua previene errores** - @validation-gates después de cada cambio
6. **SlashCommand tool tiene limitaciones** - 15k chars, no interactivo aún
7. **Frontmatter es crucial** - `description` determina cuándo Claude usa comando

### **Patrones Validados**

| Patrón | Caso de Uso | ROI |
|--------|-------------|-----|
| Research (Parallel) | Investigar bibliotecas/features | 100x |
| Planning (Sequential Thinking) | Diseñar arquitectura | 10-20x |
| Execution (TDD + Validation) | Implementar feature | 5-10x |
| Interactive Setup | Configurar servicios | 3-5x |
| Validation Standalone | Verificar calidad | 2-3x |

### **Recomendaciones para el Proyecto**

#### **Comandos Existentes a Optimizar**

1. **`/prp:prp-story-task-create`**:
   - ✅ Ya usa parallel research (@library-researcher + @codebase-analyst)
   - ✅ Ya genera documento estructurado
   - ⚠️ Falta CHECKPOINT explícito después de research
   - ⚠️ Podría usar Sequential Thinking para análisis profundo

2. **`/prp:prp-story-task-execute`**:
   - ✅ Ya tiene validación multi-nivel
   - ✅ Ya documenta deviations
   - ⚠️ Falta error handling con retry logic explícito
   - ⚠️ Podría beneficiarse de auto-improvement loop

3. **`/init-project`**:
   - ✅ Excelente orquestación de agentes
   - ✅ Flujo interactivo bien diseñado
   - ✅ 2 Checkpoints implementados
   - ✅ Parallel execution usado
   - ⚠️ `disable-model-invocation: true` podría ser necesario (issue #4745)

#### **Nuevos Comandos Recomendados**

1. **`/create-feature-tdd`**: Feature completa con research → planning → TDD → validation
2. **`/optimize-command [nombre]`**: Optimizar comando existente con best practices
3. **`/validate-command [nombre]`**: Validar que comando sigue best practices
4. **`/research-parallel [topic]`**: Research rápido con @library-researcher + @codebase-analyst

### **Próximos Pasos**

1. **Aplicar CHECKPOINTS** a comandos existentes que no los tienen
2. **Agregar `allowed-tools`** explícitamente a todos los comandos
3. **Documentar error handling** en comandos complejos
4. **Crear templates** para tipos comunes de comandos
5. **Implementar auto-improvement loops** en comandos de validación
6. **Monitorear issue #4745** sobre SlashCommand tool interactivo

---

**Este documento será actualizado** conforme descubramos nuevos patrones o la API de Claude Code evolucione.

**Versión**: 1.0
**Última Actualización**: 2025-10-08
**Investigador**: @library-researcher
**Validado por**: Claude Code Template Team
```
