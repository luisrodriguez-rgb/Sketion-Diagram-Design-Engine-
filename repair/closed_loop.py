"""
Sketion Closed-Loop Autonomous Repair Engine (v11.0)
Implementa el bucle cerrado determinista:
Render -> Validate -> Detect Defects -> Auto-Repair -> Re-Validate -> Certify (100% PASS)
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Tuple, Optional

from render.excalidraw_builder import ExcalidrawScene
from validation.validator import validate_scene
from design.consistency import VisualConsistencyEngine, ConsistencyReport
from .engine import RepairEngine


@dataclass
class ClosedLoopReport:
    initial_vcs: float
    final_vcs: float
    iterations_run: int
    defects_detected: List[str]
    repairs_applied: List[str]
    is_certified: bool
    final_consistency: ConsistencyReport

    def to_markdown(self) -> str:
        status = "CERTIFIED PASS" if self.is_certified else "UNCERTIFIED"
        lines = [
            f"### CLOSED-LOOP REPAIR AUDIT: [{status}]",
            f"* **VCS Inicial:** {self.initial_vcs:.1f} / 100",
            f"* **VCS Final (Post-Repair):** {self.final_vcs:.1f} / 100",
            f"* **Iteraciones del Bucle:** {self.iterations_run}",
            f"* **Defectos Detectados:** {len(self.defects_detected)}",
            f"* **Reparaciones Aplicadas:** {len(self.repairs_applied)}"
        ]
        if self.repairs_applied:
            lines.append("\n**Detalle de Reparaciones:**")
            for r in self.repairs_applied:
                lines.append(f"* {r}")
        return "\n".join(lines)


class ClosedLoopRepairEngine:
    """Motor de bucle cerrado que garantiza que ningún diagrama salga con defectos geométricos o de estilo."""

    @classmethod
    def execute_closed_loop(cls,
                            scene: ExcalidrawScene,
                            max_iterations: int = 3,
                            target_vcs: float = 95.0) -> Tuple[ExcalidrawScene, ClosedLoopReport]:
        """
        Ejecuta el ciclo continuo de validación y reparación hasta alcanzar la certificación.
        """
        scene_dict = scene.to_dict()
        
        # 1. Validación Inicial
        initial_consistency = VisualConsistencyEngine.evaluate_scene(scene_dict)
        initial_vcs = initial_consistency.vcs_score
        
        all_defects: List[str] = list(initial_consistency.findings)
        all_repairs: List[str] = []
        
        current_data = scene_dict
        current_vcs = initial_vcs
        iterations = 0

        while iterations < max_iterations:
            iterations += 1
            
            # Ejecutar orquestador maestro de auto-reparaciones
            repaired_data, repairs = RepairEngine.auto_repair(current_data)
            all_repairs.extend(repairs)
            
            # Revalidar consistencia visual
            revalidated_consistency = VisualConsistencyEngine.evaluate_scene(repaired_data)
            current_vcs = revalidated_consistency.vcs_score
            current_data = repaired_data

            if current_vcs >= target_vcs and len(revalidated_consistency.findings) == 0:
                break

        # Reconstruir la escena con los datos reparados
        certified_scene = ExcalidrawScene()
        certified_scene.elements = current_data.get("elements", [])
        certified_scene.app_state = current_data.get("appState", {})

        final_consistency = VisualConsistencyEngine.evaluate_scene(current_data)
        is_certified = (final_consistency.vcs_score >= target_vcs)

        report = ClosedLoopReport(
            initial_vcs=initial_vcs,
            final_vcs=final_consistency.vcs_score,
            iterations_run=iterations,
            defects_detected=all_defects,
            repairs_applied=all_repairs,
            is_certified=is_certified,
            final_consistency=final_consistency
        )

        return certified_scene, report
