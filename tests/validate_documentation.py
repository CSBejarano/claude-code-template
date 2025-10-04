"""
Validación exhaustiva de consistencia en documentación global.

Este script valida que toda la documentación del template esté consistente:
- Versiones (Template v3.0.0, SDK v1.0.0)
- Progreso (67% - 4 de 6 milestones)
- Milestones M3 y M4 documentados correctamente
- Referencias cruzadas entre documentos
- Métricas consistentes
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple

# Ruta base del proyecto
BASE_DIR = Path("/Users/cristianbejaranomendez/Desktop/IA Corp/claude-code-template")

# Archivos a validar
DOCS_TO_VALIDATE = {
    "README.md": BASE_DIR / "README.md",
    "CLAUDE.md": BASE_DIR / "CLAUDE.md",
    "PLANNING.md": BASE_DIR / ".claude" / "PLANNING.md",
    "TASK.md": BASE_DIR / ".claude" / "TASK.md",
}

# Valores esperados
EXPECTED_VALUES = {
    "template_version": "3.0.0",
    "sdk_version": "1.0.0",
    "progress_percentage": "67",
    "milestones_completed": 4,
    "milestones_total": 6,
}


class DocumentationValidator:
    """Validador de documentación del template."""

    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.checks_passed: List[str] = []
        self.docs_content: Dict[str, str] = {}

    def load_documents(self) -> bool:
        """Carga todos los documentos a validar."""
        print("📚 Cargando documentos...")

        for doc_name, doc_path in DOCS_TO_VALIDATE.items():
            if not doc_path.exists():
                self.errors.append(f"❌ Documento no encontrado: {doc_name}")
                return False

            with open(doc_path, 'r', encoding='utf-8') as f:
                self.docs_content[doc_name] = f.read()
            print(f"  ✅ {doc_name} cargado ({len(self.docs_content[doc_name])} chars)")

        return True

    def validate_versions(self) -> bool:
        """Valida que las versiones sean consistentes."""
        print("\n🔢 Validando versiones...")

        version_patterns = {
            "3.0.0": r'[Vv]ersi[oó]n[:\s]+3\.0\.0|[Vv]3\.0\.0|badge/Version-3\.0\.0',
            "1.0.0": r'SDK[:\s]+v?1\.0\.0|__version__["\s]*=["\s]*1\.0\.0',
        }

        for version, pattern in version_patterns.items():
            found_in = []
            for doc_name, content in self.docs_content.items():
                if re.search(pattern, content, re.IGNORECASE):
                    found_in.append(doc_name)

            if version == "3.0.0":
                # Template version debe estar en README, CLAUDE, PLANNING, TASK
                expected_docs = ["README.md", "CLAUDE.md", "PLANNING.md", "TASK.md"]
                missing = [doc for doc in expected_docs if doc not in found_in]

                if missing:
                    self.errors.append(f"❌ Versión 3.0.0 NO encontrada en: {', '.join(missing)}")
                else:
                    self.checks_passed.append(f"✅ Versión 3.0.0 encontrada en todos los docs principales")

            elif version == "1.0.0":
                # SDK version debe estar en algunos docs
                if not found_in:
                    self.warnings.append(f"⚠️  SDK v1.0.0 no mencionado en documentación principal")
                else:
                    self.checks_passed.append(f"✅ SDK v1.0.0 encontrado en: {', '.join(found_in)}")

        return len(self.errors) == 0

    def validate_progress(self) -> bool:
        """Valida que el progreso sea consistente (67%)."""
        print("\n📊 Validando progreso...")

        progress_patterns = [
            r'67%',
            r'67\s*%',
            r'Progreso[:\s]+67',
            r'Progress-67',
        ]

        for doc_name, content in self.docs_content.items():
            found = False
            for pattern in progress_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    found = True
                    break

            if doc_name in ["README.md", "CLAUDE.md", "PLANNING.md", "TASK.md"]:
                if not found:
                    self.errors.append(f"❌ Progreso 67% NO encontrado en {doc_name}")
                else:
                    self.checks_passed.append(f"✅ Progreso 67% encontrado en {doc_name}")

        return len(self.errors) == 0

    def validate_milestones(self) -> bool:
        """Valida que M3 y M4 estén documentados como completados."""
        print("\n🎯 Validando milestones M3 y M4...")

        # Patrones para buscar M3 completado
        m3_patterns = [
            r'M3.*Templates.*✅|✅.*M3.*Templates',
            r'MILESTONE 3.*Completad|Completad.*MILESTONE 3',
            r'\[x\].*M3:.*Templates',
        ]

        # Patrones para buscar M4 completado
        m4_patterns = [
            r'M4.*Versionad.*✅|✅.*M4.*Versionad',
            r'MILESTONE 4.*Completad|Completad.*MILESTONE 4',
            r'\[x\].*M4:.*Versionad',
        ]

        for doc_name, content in self.docs_content.items():
            # Validar M3
            m3_found = any(re.search(pattern, content, re.IGNORECASE) for pattern in m3_patterns)
            # Validar M4
            m4_found = any(re.search(pattern, content, re.IGNORECASE) for pattern in m4_patterns)

            if doc_name in ["README.md", "CLAUDE.md", "PLANNING.md", "TASK.md"]:
                if not m3_found:
                    self.errors.append(f"❌ M3 (Templates) NO marcado como completado en {doc_name}")
                else:
                    self.checks_passed.append(f"✅ M3 completado en {doc_name}")

                if not m4_found:
                    self.errors.append(f"❌ M4 (Versionado) NO marcado como completado en {doc_name}")
                else:
                    self.checks_passed.append(f"✅ M4 completado en {doc_name}")

        return len(self.errors) == 0

    def validate_cross_references(self) -> bool:
        """Valida referencias cruzadas entre documentos."""
        print("\n🔗 Validando referencias cruzadas...")

        # Referencias esperadas
        expected_refs = {
            "README.md": [
                ("QUICK_START.md", r'QUICK_START\.md'),
                ("CLAUDE.md", r'CLAUDE\.md'),
                ("PLANNING.md", r'PLANNING\.md'),
                ("TASK.md", r'TASK\.md'),
            ],
            "CLAUDE.md": [
                ("PLANNING.md", r'PLANNING\.md'),
                ("TASK.md", r'TASK\.md'),
            ],
            "TASK.md": [
                ("README.md", r'README\.md'),
                ("PLANNING.md", r'PLANNING\.md'),
            ],
        }

        for doc_name, refs in expected_refs.items():
            content = self.docs_content.get(doc_name, "")
            for ref_name, ref_pattern in refs:
                if not re.search(ref_pattern, content):
                    self.warnings.append(f"⚠️  {doc_name} no referencia a {ref_name}")
                else:
                    self.checks_passed.append(f"✅ {doc_name} → {ref_name}")

        return True

    def validate_milestone_metrics(self) -> bool:
        """Valida métricas de milestones (4 de 6 completados)."""
        print("\n📈 Validando métricas de milestones...")

        # Buscar "4 de 6" o similar
        metrics_pattern = r'4\s+de\s+6|4/6|4\s+of\s+6'

        for doc_name, content in self.docs_content.items():
            if doc_name in ["README.md", "CLAUDE.md", "TASK.md"]:
                if re.search(metrics_pattern, content, re.IGNORECASE):
                    self.checks_passed.append(f"✅ Métrica '4 de 6 milestones' en {doc_name}")
                else:
                    self.warnings.append(f"⚠️  Métrica '4 de 6 milestones' no clara en {doc_name}")

        return True

    def generate_report(self) -> str:
        """Genera reporte final de validación."""
        report = []
        report.append("=" * 80)
        report.append("📋 REPORTE DE VALIDACIÓN DE DOCUMENTACIÓN")
        report.append("=" * 80)
        report.append("")

        # Resumen
        total_checks = len(self.checks_passed) + len(self.errors) + len(self.warnings)
        report.append(f"📊 **RESUMEN**")
        report.append(f"  Total de checks: {total_checks}")
        report.append(f"  ✅ Pasados: {len(self.checks_passed)}")
        report.append(f"  ❌ Errores: {len(self.errors)}")
        report.append(f"  ⚠️  Warnings: {len(self.warnings)}")
        report.append("")

        # Errores
        if self.errors:
            report.append("❌ **ERRORES CRÍTICOS**")
            for error in self.errors:
                report.append(f"  {error}")
            report.append("")

        # Warnings
        if self.warnings:
            report.append("⚠️  **WARNINGS**")
            for warning in self.warnings:
                report.append(f"  {warning}")
            report.append("")

        # Checks pasados
        if self.checks_passed:
            report.append("✅ **CHECKS PASADOS**")
            for check in self.checks_passed:
                report.append(f"  {check}")
            report.append("")

        # Resultado final
        report.append("=" * 80)
        if len(self.errors) == 0:
            report.append("✅ **VALIDACIÓN EXITOSA** - Documentación consistente")
        else:
            report.append("❌ **VALIDACIÓN FALLIDA** - Se encontraron errores críticos")
        report.append("=" * 80)

        return "\n".join(report)

    def run_validation(self) -> bool:
        """Ejecuta toda la validación."""
        print("🚀 Iniciando validación de documentación...")
        print("=" * 80)

        # Cargar documentos
        if not self.load_documents():
            return False

        # Ejecutar validaciones
        self.validate_versions()
        self.validate_progress()
        self.validate_milestones()
        self.validate_cross_references()
        self.validate_milestone_metrics()

        # Generar y mostrar reporte
        print("\n")
        report = self.generate_report()
        print(report)

        # Guardar reporte
        report_path = BASE_DIR / ".claude" / "VALIDATION_DOCS.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n📄 Reporte guardado en: {report_path}")

        return len(self.errors) == 0


if __name__ == "__main__":
    validator = DocumentationValidator()
    success = validator.run_validation()

    exit(0 if success else 1)
