# Real Projects E2E Testing Suite

> Validación del claude-code-template con 10 proyectos reales de diferentes complejidades y dominios

## 📋 Overview

Esta suite valida el template generando 10 proyectos reales que cubren casos de uso comunes:

| #   | Proyecto                   | Complexity | APIs                   | Est. Tests | Status     |
| --- | -------------------------- | ---------- | ---------------------- | ---------- | ---------- |
| 1   | Weather API Fetcher        | SIMPLE     | 1 (OpenWeatherMap)     | 5+         | ⏳ Pending |
| 2   | Gmail→Notion Sync          | MEDIUM     | 2 (Gmail, Notion)      | 8+         | ⏳ Pending |
| 3   | Slack→Google Sheets Logger | MEDIUM     | 2 (Slack, Sheets)      | 8+         | ⏳ Pending |
| 4   | PDF Invoice Processor      | MEDIUM     | 2 (OCR, Holded)        | 10+        | ⏳ Pending |
| 5   | E-commerce MVP             | HIGH       | 3+ (Stripe, DB, Email) | 15+        | ⏳ Pending |
| 6   | Multi-API Dashboard        | HIGH       | 3+ (Various)           | 15+        | ⏳ Pending |
| 7   | WhatsApp Bot               | MEDIUM     | 2 (Twilio, OpenAI)     | 10+        | ⏳ Pending |
| 8   | Twitter Analytics          | MEDIUM     | 2 (Twitter, DB)        | 10+        | ⏳ Pending |
| 9   | Payment Webhook Handler    | MEDIUM     | 2 (Stripe, DB)         | 8+         | ⏳ Pending |
| 10  | Data Pipeline ETL          | HIGH       | 3+ (APIs, DB, Storage) | 15+        | ⏳ Pending |

## 🎯 Success Criteria

- ✅ 10/10 proyectos generados exitosamente
- ✅ Success rate >90%
- ✅ Test pass rate >85%
- ✅ Quality score >7.5/10 promedio
- ✅ Issues documentados y priorizados

## 🏗️ Structure

```
tests/real_projects/
├── README.md (this file)
├── validate_project.py (validation framework)
├── run_all_validations.sh (batch validation)
├── generate_report.py (aggregate results)
│
├── 01_weather_api/
│   ├── spec.md (project specification)
│   └── [generated project will go here]
│
├── 02_gmail_notion/
│   ├── spec.md
│   └── [generated project]
│
├── ... (03-10)
│
└── results/
    ├── validation_summary.json
    ├── validation_report.md
    └── issues_found.md
```

## 🚀 Execution Workflow

### Phase 1: Project Generation (1 week)

Para cada proyecto:

```bash
# 1. Leer especificación
cat tests/real_projects/01_weather_api/spec.md

# 2. Generar proyecto usando @project-initializer
# (manual en Claude Code UI)

# 3. Validar proyecto generado
python tests/real_projects/validate_project.py \
    tests/real_projects/01_weather_api/weather-api-fetcher \
    SIMPLE

# 4. Documentar resultados
# Results saved to validation_results.json
```

**Estimación:** ~4-6 horas por proyecto × 10 = 40-60 horas

### Phase 2: Analysis & Reporting (2-3 días)

```bash
# Generate aggregate report
python tests/real_projects/generate_report.py

# Output:
# - results/validation_summary.json
# - results/validation_report.md
# - results/issues_found.md
```

### Phase 3: Issue Remediation (variable)

Basado en issues encontrados, crear tareas en Archon para mejoras del template.

## 📊 Validation Framework

El script `validate_project.py` valida:

### 1. Structure Validation

- ✅ Base files (README, CLAUDE.md, PLANNING.md, TASK.md)
- ✅ Orchestrator/ for MEDIUM/HIGH projects
- ✅ @self-improve agent for HIGH projects
- ✅ Tests directory exists

### 2. Test Execution

- ✅ Tests exist and are runnable
- ✅ Pass rate >85% target
- ✅ No timeouts (>5 min)

### 3. Code Quality

- ✅ Linting passes (ruff)
- ✅ No critical errors

### 4. Documentation

- ✅ README complete
- ✅ PLANNING.md exists
- ✅ API setup guides present

### 5. Quality Score (0-10)

- Structure: 3 points
- Tests: 4 points (pass rate based)
- Documentation: 2 points
- Linting: 1 point

## 🛠️ Usage

### Validate Single Project

```bash
python tests/real_projects/validate_project.py \
    <project_path> \
    <complexity>

# Example:
python tests/real_projects/validate_project.py \
    tests/real_projects/01_weather_api/weather-api-fetcher \
    SIMPLE
```

### Batch Validation

```bash
# Validate all generated projects
bash tests/real_projects/run_all_validations.sh
```

### Generate Report

```bash
# Aggregate all validation results
python tests/real_projects/generate_report.py
```

## 📝 Project Specifications

Cada proyecto tiene un `spec.md` con:

- **Goal**: Descripción del objetivo
- **Expected Complexity**: SIMPLE, MEDIUM, o HIGH
- **APIs**: Lista de APIs a integrar
- **Features Esperadas**: Funcionalidades clave
- **Test Cases Esperados**: Tests mínimos esperados
- **Expected Structure**: Estructura de archivos
- **Success Criteria**: Criterios de aceptación

## 📈 Expected Results

Basado en el sistema actual (v3.1.0):

| Complexity | Estimated Context | Pass Rate | Quality Score |
| ---------- | ----------------- | --------- | ------------- |
| SIMPLE     | 35-40%            | >95%      | >8.5/10       |
| MEDIUM     | 45-55%            | >85%      | >7.5/10       |
| HIGH       | 60-70%            | >80%      | >7.0/10       |

**Overall Success Rate Target:** >90% (9/10 proyectos generados correctamente)

## 🐛 Known Issues to Watch

Basado en PLANNING.md, monitorear:

1. **Context Window**: HIGH projects approaching 70% limit
2. **OAuth Flows**: Complex authentication puede fallar
3. **API Rate Limiting**: Tests pueden fallar si rate limited
4. **Timeouts**: Long-running tests (>5 min)

## 🔄 Next Steps

1. ✅ Framework de validación creado (`validate_project.py`)
2. ✅ Especificaciones de proyectos definidas (spec.md)
3. ⏳ Generar proyectos 1-10 usando @project-initializer
4. ⏳ Ejecutar validaciones
5. ⏳ Generar report agregado
6. ⏳ Documentar issues y crear tareas de mejora

---

**Total Estimated Time:** 1-2 semanas
**Owner:** prp-validator
**Priority:** HIGH
**Archon Task ID:** e4394796-9c64-4d2b-b3d8-e42ec4386302
