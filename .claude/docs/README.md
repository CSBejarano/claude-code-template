# Documentación Modular del Sistema

Esta carpeta contiene la documentación detallada del sistema de agentes y workflows del template, extraída de CLAUDE.md para optimizar el rendimiento.

## Estructura

```
.claude/docs/
├── README.md           → Este archivo
├── AGENTS.md           → Sistema completo de agentes orquestados
├── CHECKPOINTS.md      → Checkpoints críticos detallados (ROI 100x/10-20x)
├── WORKFLOWS.md        → Flujos de trabajo y diagramas mermaid
└── COMMANDS.md         → Guía completa de comandos disponibles
```

## Tamaños de Archivos

| Archivo        | Tamaño | Contenido                               |
| -------------- | ------ | --------------------------------------- |
| CLAUDE.md      | ~15k   | Documento principal (optimizado)        |
| AGENTS.md      | ~12k   | Sistema de agentes detallado            |
| WORKFLOWS.md   | ~13k   | Flujos de trabajo + diagramas           |
| CHECKPOINTS.md | ~8k    | Checkpoints críticos + CONTINUE_SESSION |
| COMMANDS.md    | ~8k    | Comandos disponibles + ejemplos         |

## Propósito de la Modularización

**Antes**: CLAUDE.md tenía 73k caracteres (>40k límite recomendado)
**Después**: CLAUDE.md tiene 15k caracteres (**79% de reducción**)

**Beneficios**:

1. ✅ CLAUDE.md se carga en cada interacción (ahora solo 15k)
2. ✅ Archivos modulares solo se cargan cuando se necesitan
3. ✅ Mejor organización y navegabilidad
4. ✅ Mejor rendimiento del sistema
5. ✅ Más fácil de mantener

## Cómo Usar

CLAUDE.md contiene referencias a estos archivos:

```markdown
**📖 Ver detalles**: [.claude/docs/WORKFLOWS.md](.claude/docs/WORKFLOWS.md)
```

Cuando Claude Code necesita información detallada, puede leer el archivo modular correspondiente.

## Principios de Organización

- **AGENTS.md**: Todo sobre agentes especializados y su orquestación
- **CHECKPOINTS.md**: Checkpoints críticos + gestión de contexto
- **WORKFLOWS.md**: Flujos de trabajo detallados + diagramas + best practices
- **COMMANDS.md**: Todos los comandos disponibles con ejemplos completos

---

_Optimización realizada: 2025-01-07_
_Mejora de rendimiento: 79% reducción en CLAUDE.md_
