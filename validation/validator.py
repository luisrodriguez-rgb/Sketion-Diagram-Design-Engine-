"""
Sketion Master Validator 2.6
Integra:
1. Hard Failures (Estructurales)
2. Visual Quality Score (Densidad calibrada, Jerarquía, Readability)
3. Semantic Fidelity Score (Node/Edge/Scope coverage respecto al SemanticDiagram)
4. Dual Sketion Score = 0.5 * VisualQuality + 0.5 * SemanticFidelity
5. Repair Budget (Máximo 3 iteraciones con registro)
"""
from dataclasses import dataclass, field
from typing import Dict, Any, List, Tuple, Optional
from .structural import validate_structure
from .visual import validate_visual_quality
from .quality_score import calculate_quality_score, QualityMetrics
from .fidelity import calculate_semantic_fidelity, SemanticFidelityMetrics
from repair.engine import RepairEngine
from semantic.models import SemanticDiagram

@dataclass
class ValidationReport:
    is_valid: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    visual_metrics: QualityMetrics = None
    fidelity_metrics: Optional[SemanticFidelityMetrics] = None
    sketion_overall_score: int = 0
    repairs_applied: List[str] = field(default_factory=list)
    repair_iterations: int = 0
    elements_count: int = 0
    frames_count: int = 0

    def summary(self) -> str:
        status = "✅ PASS" if self.is_valid and not self.errors else "❌ FAIL"
        lines = [
            f"==================================================",
            f"=== SKETION COMPREHENSIVE REPORT: {status} ===",
            f"==================================================",
            f"Elementos totales: {self.elements_count} | Frames: {self.frames_count}",
            f"PUNTUACIÓN GLOBAL SKETION: {self.sketion_overall_score}/100\n"
        ]

        if self.visual_metrics:
            lines.append(self.visual_metrics.report_table())

        if self.fidelity_metrics:
            lines.append("\n" + self.fidelity_metrics.report_table())

        if self.repairs_applied:
            lines.append(f"\n[AUTO-REPARACIONES APLICADAS (Iteraciones: {self.repair_iterations}/3)]:")
            for rep in self.repairs_applied:
                lines.append(f"  🔧 {rep}")

        if self.errors:
            lines.append("\n[ERRORES CRÍTICOS / HARD FAILURES]:")
            for err in self.errors:
                lines.append(f"  ❌ {err}")

        return "\n".join(lines)

    def get_summary(self) -> str:
        return self.summary()


def validate_scene(scene_data: Any,
                   diagram: Optional[SemanticDiagram] = None,
                   auto_repair: bool = True,
                   max_repair_iterations: int = 3) -> ValidationReport:
    """
    Ejecuta el ciclo integral de validación, fidelidad semántica y reparación acotada (Repair Budget).
    """
    import json
    if isinstance(scene_data, str):
        with open(scene_data, "r", encoding="utf-8") as f:
            scene_data = json.load(f)

    all_repairs = []
    iterations = 0

    hero_id = None
    if diagram and diagram.nodes:
        heroes = [n.id for n in diagram.nodes if n.is_hero]
        if heroes:
            hero_id = heroes[0]

    if auto_repair:
        while iterations < max_repair_iterations:
            iterations += 1
            scene_data, step_repairs = RepairEngine.auto_repair(scene_data, primary_hero_id=hero_id)
            if not step_repairs:
                break
            all_repairs.extend(step_repairs)

    errors = validate_structure(scene_data)
    warnings = validate_visual_quality(scene_data)
    visual_metrics = calculate_quality_score(scene_data)

    fidelity_metrics = None
    if diagram:
        fidelity_metrics = calculate_semantic_fidelity(diagram, scene_data)

    elements = scene_data.get("elements", [])
    frames_count = len([e for e in elements if e.get("type") == "frame"])

    # Hard Failure si densidad excede 7.0
    if visual_metrics.density > 7.0:
        errors.append(f"Hard failure: Densidad {visual_metrics.density:.1f}/10 excede el límite crítico de 7.0/10.")

    # Cálculo del Sketion Overall Score unificado
    if fidelity_metrics:
        sketion_score = int(visual_metrics.overall_score * 0.5 + fidelity_metrics.overall_fidelity_score * 0.5)
    else:
        sketion_score = visual_metrics.overall_score

    is_valid = (len(errors) == 0)
    report = ValidationReport(
        is_valid=is_valid,
        errors=errors,
        warnings=warnings,
        visual_metrics=visual_metrics,
        fidelity_metrics=fidelity_metrics,
        sketion_overall_score=sketion_score,
        repairs_applied=all_repairs,
        repair_iterations=iterations,
        elements_count=len(elements),
        frames_count=frames_count
    )
    return scene_data, report
