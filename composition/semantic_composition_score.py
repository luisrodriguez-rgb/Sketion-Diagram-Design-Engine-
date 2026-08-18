"""
Sketion Semantic Composition Score (SCS) Engine (v11.0)
Evalúa si la estructura gráfica seleccionada es conceptualmente apropiada para el dominio y la intención del contenido.
Evita 'aberraciones visuales' (ej. microservicios en formato radial o ecosistemas en una sola columna).
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from enum import Enum

from .composition_patterns import CompositionPattern
from semantic.content_model import ContentModel


@dataclass
class SemanticCompositionReport:
    scs_score: float  # 0 a 100
    is_conceptually_sound: bool
    recommended_pattern: CompositionPattern
    actual_pattern: CompositionPattern
    affinity_rating: str  # OPTIMAL, ACCEPTABLE, SUBOPTIMAL, INVALID
    rationale: str
    warnings: List[str] = field(default_factory=list)

    def to_markdown(self) -> str:
        status = "PASSED" if self.is_conceptually_sound else "CONCEPTUAL MISFIT"
        lines = [
            f"### SEMANTIC COMPOSITION SCORE (SCS): {self.scs_score:.1f} / 100 [{status}]",
            f"* **Patrón Actual:** `{self.actual_pattern.value}`",
            f"* **Patrón Recomendado:** `{self.recommended_pattern.value}`",
            f"* **Afinidad Conceptual:** **{self.affinity_rating}**",
            f"* **Justificación:** {self.rationale}"
        ]
        if self.warnings:
            lines.append("\n**Advertencias Conceptuales:**")
            for w in self.warnings:
                lines.append(f"* {w}")
        return "\n".join(lines)


class SemanticCompositionEvaluator:
    """Evaluador de adecuación conceptual entre datos y topología visual."""

    # Matriz de compatibilidad: Dominio/Intención -> Patrones Óptimos, Aceptables e Inválidos
    _AFFINITY_MATRIX: Dict[str, Dict[str, Any]] = {
        "software_architecture": {
            "optimal": [
                CompositionPattern.LAYERED_ARCHITECTURE,
                CompositionPattern.SECURITY_BARRIER,
                CompositionPattern.HEXAGONAL_PORTS,
                CompositionPattern.K8S_TOPOLOGY,
                CompositionPattern.UML_CLASS_MODEL
            ],
            "acceptable": [
                CompositionPattern.PIPELINE_FLOW,
                CompositionPattern.HIERARCHICAL_TREE,
                CompositionPattern.NARRATIVE_BOARD
            ],
            "penalized": [
                CompositionPattern.RADIAL_HUB,
                CompositionPattern.CORNELL_NOTES,
                CompositionPattern.FUNNEL_CONVERSION
            ]
        },
        "data_ai_pipeline": {
            "optimal": [
                CompositionPattern.PIPELINE_FLOW,
                CompositionPattern.DATA_LAKEHOUSE,
                CompositionPattern.HIERARCHICAL_TREE,
                CompositionPattern.RADIAL_HUB
            ],
            "acceptable": [
                CompositionPattern.LAYERED_ARCHITECTURE,
                CompositionPattern.SECURITY_BARRIER
            ],
            "penalized": [
                CompositionPattern.CORNELL_NOTES,
                CompositionPattern.SWIMLANE_PROCESS,
                CompositionPattern.MATRIX_2X2
            ]
        },
        "business_strategy": {
            "optimal": [
                CompositionPattern.MATRIX_2X2,
                CompositionPattern.RADIAL_HUB,
                CompositionPattern.PIPELINE_FLOW,
                CompositionPattern.NARRATIVE_BOARD,
                CompositionPattern.FUNNEL_CONVERSION
            ],
            "acceptable": [
                CompositionPattern.HIERARCHICAL_TREE,
                CompositionPattern.DUAL_SPLIT,
                CompositionPattern.LAYERED_ARCHITECTURE
            ],
            "penalized": [
                CompositionPattern.K8S_TOPOLOGY,
                CompositionPattern.UML_CLASS_MODEL,
                CompositionPattern.SECURITY_BARRIER
            ]
        },
        "engineering_process": {
            "optimal": [
                CompositionPattern.SWIMLANE_PROCESS,
                CompositionPattern.A3_REPORT,
                CompositionPattern.HIERARCHICAL_TREE,
                CompositionPattern.TIMELINE_ROADMAP
            ],
            "acceptable": [
                CompositionPattern.PIPELINE_FLOW,
                CompositionPattern.DUAL_SPLIT,
                CompositionPattern.MATRIX_2X2
            ],
            "penalized": [
                CompositionPattern.RADIAL_HUB,
                CompositionPattern.CORNELL_NOTES,
                CompositionPattern.HEXAGONAL_PORTS
            ]
        },
        "education_study": {
            "optimal": [
                CompositionPattern.CORNELL_NOTES,
                CompositionPattern.RADIAL_HUB,
                CompositionPattern.HIERARCHICAL_TREE,
                CompositionPattern.RADAR_SPIDER
            ],
            "acceptable": [
                CompositionPattern.DUAL_SPLIT,
                CompositionPattern.TIMELINE_ROADMAP,
                CompositionPattern.MATRIX_2X2
            ],
            "penalized": [
                CompositionPattern.K8S_TOPOLOGY,
                CompositionPattern.SECURITY_BARRIER,
                CompositionPattern.SERVICE_BLUEPRINT
            ]
        },
        "ux_research": {
            "optimal": [
                CompositionPattern.SERVICE_BLUEPRINT,
                CompositionPattern.DUAL_SPLIT,
                CompositionPattern.RADAR_SPIDER,
                CompositionPattern.PIPELINE_FLOW,
                CompositionPattern.NARRATIVE_BOARD
            ],
            "acceptable": [
                CompositionPattern.MATRIX_2X2,
                CompositionPattern.SWIMLANE_PROCESS,
                CompositionPattern.RADIAL_HUB
            ],
            "penalized": [
                CompositionPattern.K8S_TOPOLOGY,
                CompositionPattern.UML_CLASS_MODEL,
                CompositionPattern.A3_REPORT
            ]
        },
        "agile_management": {
            "optimal": [
                CompositionPattern.KANBAN_BOARD,
                CompositionPattern.TIMELINE_ROADMAP,
                CompositionPattern.MATRIX_2X2,
                CompositionPattern.PIPELINE_FLOW
            ],
            "acceptable": [
                CompositionPattern.SWIMLANE_PROCESS,
                CompositionPattern.HIERARCHICAL_TREE
            ],
            "penalized": [
                CompositionPattern.RADAR_SPIDER,
                CompositionPattern.HEXAGONAL_PORTS,
                CompositionPattern.K8S_TOPOLOGY
            ]
        }
    }

    @classmethod
    def evaluate(cls, pattern: CompositionPattern, content: ContentModel) -> SemanticCompositionReport:
        """Calcula el Semantic Composition Score (SCS) analizando la adecuación conceptual."""
        d = content.domain.lower()
        title_lower = content.title.lower()

        # Mapear dominio
        if d in ["software", "infra", "cloud"]:
            category_key = "software_architecture"
        elif d in ["data", "ai", "ml"]:
            category_key = "data_ai_pipeline"
        elif d in ["business", "strategy", "finance"]:
            category_key = "business_strategy"
        elif d in ["engineering", "manufacturing", "operations"]:
            category_key = "engineering_process"
        elif d in ["education", "study", "academic"]:
            category_key = "education_study"
        elif d in ["ux", "design"]:
            category_key = "ux_research"
        elif d in ["agile", "project", "product"]:
            category_key = "agile_management"
        else:
            category_key = "software_architecture"

        matrix = cls._AFFINITY_MATRIX.get(category_key, cls._AFFINITY_MATRIX["software_architecture"])
        warnings: List[str] = []

        # Caso especial de intenciones explícitas
        if "radar" in title_lower or "competencia" in title_lower or "evaluacion" in title_lower:
            recommended = CompositionPattern.RADAR_SPIDER
        elif "kanban" in title_lower or "sprint" in title_lower:
            recommended = CompositionPattern.KANBAN_BOARD
        elif "a3" in title_lower or "toyota" in title_lower:
            recommended = CompositionPattern.A3_REPORT
        elif "cornell" in title_lower or "apuntes" in title_lower:
            recommended = CompositionPattern.CORNELL_NOTES
        elif "ecosystem" in title_lower or "ecosistema" in title_lower or "porter" in title_lower:
            recommended = CompositionPattern.RADIAL_HUB
        elif "blueprint" in title_lower:
            recommended = CompositionPattern.SERVICE_BLUEPRINT
        else:
            recommended = matrix["optimal"][0]

        if pattern in matrix["optimal"] or pattern == recommended:
            scs = 98.0
            rating = "OPTIMAL"
            rationale = f"La estructura '{pattern.value}' encaja perfectamente con el dominio '{category_key}'."
        elif pattern in matrix["acceptable"]:
            scs = 85.0
            rating = "ACCEPTABLE"
            rationale = f"La estructura '{pattern.value}' es válida y comprensible para '{category_key}', aunque '{recommended.value}' ofrece mayor poder expresivo."
        else:
            scs = 45.0
            rating = "SUBOPTIMAL"
            rationale = f"Discrepancia semántica: La estructura '{pattern.value}' no es natural para '{category_key}'. Se recomienda '{recommended.value}'."
            warnings.append(f"Riesgo de confusión conceptual: Se forzó '{pattern.value}' en un dominio que típicamente requiere '{recommended.value}'.")

        is_sound = (scs >= 75.0)

        return SemanticCompositionReport(
            scs_score=scs,
            is_conceptually_sound=is_sound,
            recommended_pattern=recommended,
            actual_pattern=pattern,
            affinity_rating=rating,
            rationale=rationale,
            warnings=warnings
        )
