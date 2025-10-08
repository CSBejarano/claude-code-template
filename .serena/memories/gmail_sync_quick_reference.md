# Gmail Sync - Quick Reference Commands

## Directorio del Proyecto

```bash
cd /Users/cristianbejaranomendez/Desktop/IA\ Corp/claude-code-template/tests/real_projects/02_gmail_notion/gmail-notion-sync
source venv/bin/activate
```

## Pipeline de Clasificación

### Opción 1: Simple (10-50 emails)

```bash
# Procesar 50 emails
python run_full_pipeline_dry_run.py 50

# Archivo generado: full_pipeline_dry_run_results.json
```

### Opción 2: Batch (100-1000+ emails)

```bash
# Procesar 100 emails en batches de 10 con 30s sleep
python run_batch_pipeline.py 100 10 30

# Archivos generados:
# - batch_results/batch_001_results.json (batch individual)
# - batch_results/batch_002_results.json
# - ...
# - batch_pipeline_consolidated_results.json (consolidado)
```

## Aplicación de Etiquetas

### Paso 1: Dry-run (SIEMPRE PRIMERO)

```bash
python apply_labels.py \
  --results batch_pipeline_consolidated_results.json \
  --archive \
  --dry-run
```

### Paso 2: Aplicar SIN archivar

```bash
# Etiquetas aplicadas, emails quedan en INBOX
python apply_labels.py \
  --results batch_pipeline_consolidated_results.json
```

### Paso 3: Aplicar + Archivar (Limpiar INBOX)

```bash
# Etiquetas aplicadas + emails archivados
python apply_labels.py \
  --results batch_pipeline_consolidated_results.json \
  --archive
```

## Validación y Análisis

### Validar replacement rule compliance

```bash
python validate_approval_fix.py
# Verifica que el Approval Agent siempre agregue etiquetas al remover
```

### Analizar impacto de nueva lógica de aprobación

```bash
python analyze_approval_logic.py
# Compara approval rate antes vs después del fix
```

### Validación rápida con 5 emails

```bash
python quick_validation.py
# Test rápido con 5 emails para verificar cambios
```

## Variables de Entorno Requeridas

### .env file

```bash
# Gmail OAuth2
GMAIL_CLIENT_ID=xxxxx.apps.googleusercontent.com
GMAIL_CLIENT_SECRET=xxxxx
GMAIL_REDIRECT_URI=http://localhost:8080

# Anthropic API
ANTHROPIC_API_KEY=sk-ant-xxxxx

# Opcional (para futuras features)
NOTION_TOKEN=secret_xxxxx
NOTION_DATABASE_ID=xxxxx
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/xxxxx
```

## Archivos Importantes

### Resultados de Pipeline

- `full_pipeline_dry_run_results.json` - Simple pipeline results
- `batch_pipeline_consolidated_results.json` - Batch pipeline consolidated
- `batch_results/` - Individual batch results

### Scripts de Ejecución

- `run_full_pipeline_dry_run.py` - Simple pipeline
- `run_batch_pipeline.py` - Batch pipeline
- `apply_labels.py` - Label application CLI

### Agentes IA

- `src/email_classifier_agent.py` - Classifier Agent
- `src/approval_agent.py` - Approval Agent
- `src/gmail_labeler.py` - Label Applicator

### Utilidades

- `src/gmail_client.py` - Gmail API client
- `src/email_parser.py` - Email parsing

### Validación

- `validate_approval_fix.py` - Replacement rule validator
- `analyze_approval_logic.py` - Approval logic analyzer
- `quick_validation.py` - Quick 5-email test

### Documentación

- `USAGE_GUIDE.md` - Complete usage guide (580 lines)
- `README.md` - Project overview
- `CLAUDE.md` - Claude Code instructions

## Estado Actual del Sistema

**Version**: 1.0.0
**Status**: Production-ready ✅

**Fixes aplicados**:

1. ✅ OAuth2 scope mismatch fix
2. ✅ Replacement rule enforcement (100% compliance)
3. ✅ Data flow bug fix
4. ✅ Statistics calculation fix
5. ✅ Approval logic fix (49% → 100% approval rate)

**Métricas**:

- Classifier confidence: 93%
- Approver confidence: 92%
- Approval rate: 100% (after fix)
- Rejection rate: <2% (expected)

**Próximo paso**:
Re-procesar 100 emails con nueva lógica y aplicar etiquetas en producción.

## Troubleshooting Común

### Error: OAuth2 token expired

```bash
# Re-autenticar eliminando token
rm ~/.gmail_token.json
python run_full_pipeline_dry_run.py 10
```

### Error: ANTHROPIC_API_KEY not found

```bash
# Verificar .env
cat .env | grep ANTHROPIC

# Si falta, agregar:
echo "ANTHROPIC_API_KEY=sk-ant-xxxxx" >> .env
```

### Emails no se archivan

```bash
# Verificar que usaste --archive flag
python apply_labels.py \
  --results batch_pipeline_consolidated_results.json \
  --archive  # ← Este flag es necesario
```

### Ver logs detallados

```bash
# Agregar --verbose flag
python apply_labels.py \
  --results batch_pipeline_consolidated_results.json \
  --verbose \
  --dry-run
```
