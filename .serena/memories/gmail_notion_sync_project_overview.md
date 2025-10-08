# Gmail→Notion Sync Project - Overview

## Project Summary

Sistema completo de clasificación automática de emails de Gmail usando 2 agentes IA (Claude Sonnet 4.5) con aplicación automática de etiquetas a Gmail.

**Estado actual**: Production-ready, label application module completo
**Versión**: 1.0.0
**Complejidad**: MEDIUM (con Orchestrator)

## Architecture

### Two-Agent System

```
Email → Agent 1 (Classifier) → Agent 2 (Approver) → Final Labels → Gmail
```

**Agent 1: EmailClassifierAgent**

- Model: Claude Sonnet 4.5 (`claude-sonnet-4-20250514`)
- Temperature: 0.3
- Purpose: Analiza emails y sugiere etiquetas + urgencia
- Average confidence: ~93%
- File: `src/email_classifier_agent.py` (343 lines)

**Agent 2: EmailApprovalAgent**

- Model: Claude Sonnet 4.5 (`claude-sonnet-4-20250514`)
- Temperature: 0.3
- Purpose: Revisa clasificaciones y aprueba/modifica
- Average confidence: ~92%
- **CRITICAL FIX APPLIED**: Nueva lógica de aprobación (approved=true si final_labels no está vacío)
- File: `src/approval_agent.py` (456 lines)

### Available Labels (15 total)

1. Skool/Comunidades
2. LinkedIn
3. Trabajos/Empleo
4. Emprende/Formación
5. Finanzas
6. Amazon/Compras
7. Spotify/Música
8. AEAT
9. Google/Servicios
10. URGENTE (24-48h action required)
11. Advero Properties (personal)
12. VIETNAM (personal travel)
13. Mensajes YouTube
14. Newsletter's
15. Regalo Mamá (personal)

## Key Files and Their Purposes

### Core Agent Files

- `src/email_classifier_agent.py` - Classifier agent with Pydantic models
- `src/approval_agent.py` - Approval agent with CRITICAL replacement rule
- `src/gmail_client.py` - Gmail OAuth2 + email fetch + label management (540 lines)
- `src/gmail_labeler.py` - Label application logic (330 lines)
- `src/email_parser.py` - HTML/multipart email parsing

### Pipeline Scripts

- `run_full_pipeline_dry_run.py` - Simple pipeline (10-50 emails)
- `run_batch_pipeline.py` - Batch pipeline (100-1000+ emails with sleep)
- `apply_labels.py` - CLI for applying labels to Gmail (350+ lines)

### Validation Scripts

- `validate_approval_fix.py` - Validates replacement rule compliance
- `analyze_approval_logic.py` - Analyzes old vs new approval logic

### Documentation

- `USAGE_GUIDE.md` - Complete usage guide (580 lines)
- `README.md` - Project setup and overview
- `CLAUDE.md` - Claude Code instructions

## Critical Technical Decisions

### 1. OAuth2 Scope Fix (Production-Ready)

**Problem**: Token refresh failures due to scope mismatch
**Solution**: Standardized on `https://mail.google.com/` full access
**Location**: `src/gmail_client.py:51`
**Auto-refresh**: Lines 140-148 prevent token expiry in production

### 2. Replacement Rule (Approval Agent)

**Problem**: Agent removed labels without adding replacements
**Solution**: CRITICAL instructions in system prompt
**Location**: `src/approval_agent.py:253-298`
**Validation**: 100% compliance (0 violations in 150 emails)

### 3. Approval Logic Fix (LATEST - 2025-10-05)

**Problem**: 51 of 100 emails rejected despite having valid final_labels
**Root Cause**: Approval Agent marked approved=false when Classifier didn't classify (even if Approver added valid labels)
**Solution**: Changed approval rule to: approved=true if final_labels is not empty
**Location**: `src/approval_agent.py:265-273` and `291-294`
**Result**: Approval rate improved from 49% to 100%

### 4. Data Flow Fix

**Problem**: Approver received entire classification object instead of just classification field
**Solution**: Changed to `classification_results[i]["classification"]`
**Location**: `run_full_pipeline_dry_run.py:256`

### 5. Statistics Fix

**Problem**: Confidence showed 0% instead of ~95%
**Solution**: Fixed nested dict access: `r["classification"].get("confidence", 0)`
**Location**: `run_full_pipeline_dry_run.py:295`

## Performance Metrics

### Processing Times

| Emails | Mode          | Time    | Cost (est) |
| ------ | ------------- | ------- | ---------- |
| 10     | Simple        | ~30s    | $0.20      |
| 50     | Simple        | ~5 min  | $1.00      |
| 100    | Batch (10x10) | ~15 min | $2.00      |
| 500    | Batch (25x20) | ~90 min | $10.00     |

### Approval Rates (After Fix)

- **Expected approval rate**: ~98-100%
- **Modification rate**: 50-60%
- **True rejection rate**: <2%

## Usage Workflows

### 1. Classification Pipeline

```bash
# Simple (10-50 emails)
python run_full_pipeline_dry_run.py 50

# Batch (100-1000+ emails)
python run_batch_pipeline.py 100 10 30  # 100 emails, batches of 10, 30s sleep
```

### 2. Label Application

```bash
# Dry run first (always!)
python apply_labels.py --results batch_pipeline_consolidated_results.json --archive --dry-run

# Apply without archiving
python apply_labels.py --results full_pipeline_dry_run_results.json

# Apply + archive (clean inbox)
python apply_labels.py --results batch_pipeline_consolidated_results.json --archive
```

## Current Status

**Completed**:

- ✅ Two-agent architecture implemented
- ✅ OAuth2 production-ready with auto-refresh
- ✅ Replacement rule enforced (100% compliance)
- ✅ Approval logic fixed (49% → 100% approval rate)
- ✅ Label application module complete
- ✅ Dry-run validation successful
- ✅ Complete documentation (USAGE_GUIDE.md)

**Next Steps** (User roadmap):

1. Re-process emails with new approval logic
2. Apply labels in production
3. Fine-tuning (optimize criteria based on results)
4. Cron job for daily automation
5. Webhooks for real-time processing
6. Urgent email alerts
7. Notion database synchronization

## Environment Variables Required

```bash
# Gmail OAuth2
GMAIL_CLIENT_ID=xxxxx.apps.googleusercontent.com
GMAIL_CLIENT_SECRET=xxxxx
GMAIL_REDIRECT_URI=http://localhost:8080

# Anthropic API
ANTHROPIC_API_KEY=sk-ant-xxxxx
```

## Important Notes

- **TDD approach**: Tests first, code second
- **Rate limiting**: Respect Gmail (60/min) and Anthropic API limits
- **Dry-run first**: Always test before production
- **Token persistence**: ~/.gmail_token.json cached between runs
- **Deduplication**: Email ID used to prevent duplicates
