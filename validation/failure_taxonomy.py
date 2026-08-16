"""
Sketion Failure Taxonomy & Design Advantage Score (DAS) Engine (v10.2)
Estructura formal para auditoría de errores, análisis de causa raíz y cálculo
del Design Advantage Score en evaluaciones comparativas A/B a gran escala (200-500 casos).
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional


class FailureMode(Enum):
    F01_WRONG_ARCHETYPE = ("F01", "Wrong Archetype", "Selección de arquetipo no alineado con la naturaleza del flujo.")
    F02_INCORRECT_HIERARCHY = ("F02", "Incorrect Hierarchy", "Componente secundario opaca al Hero transaccional.")
    F03_EXCESSIVE_DENSITY = ("F03", "Excessive Density", "Densidad superior al umbral cognitivo admisible (>4/10).")
    F04_WEAK_CONNECTOR_ROUTING = ("F04", "Weak Connector Routing", "Conectores que se cruzan o no anclan en el borde periférico.")
    F05_WRONG_VISUAL_PRIMITIVE = ("F05", "Wrong Visual Primitive", "Uso de tarjeta plana para bases de datos o colas de streaming.")
    F06_POOR_BRAND_REPRESENTATION = ("F06", "Poor Brand Representation", "Falta de reconocimiento de marca o paleta errónea.")
    F07_TEXT_OVERFLOW = ("F07", "Text Overflow", "Texto que colisiona con ranuras o badges en tarjetas.")
    F08_POOR_AUDIENCE_ADAPTATION = ("F08", "Poor Audience Adaptation", "Exceso de ruido técnico para ejecutivos o falta de detalle.")
    F09_EXCESSIVE_WHITESPACE = ("F09", "Excessive Whitespace", "Frame desproporcionadamente grande respecto al contenido.")
    F10_INSUFFICIENT_CONTEXT = ("F10", "Insufficient Context", "Ausencia de subtítulos explicativos o tags de protocolo.")
    F11_INCORRECT_GROUPING = ("F11", "Incorrect Grouping", "Componentes de capas distintas agrupados en la misma fila.")
    F12_AESTHETIC_PREFERENCE = ("F12", "Aesthetic Preference", "Discrepancia subjetiva del evaluador.")

    def __init__(self, code: str, title: str, description: str):
        self.code = code
        self.title = title
        self.description = description


@dataclass
class DesignAdvantageScore:
    semantic_fidelity_delta: float
    visual_hierarchy_delta: float
    readability_delta: float
    audience_fit_delta: float
    professional_polish_delta: float
    overall_preference_delta: float

    @property
    def composite_score(self) -> float:
        """Calcula el Design Advantage Score (DAS) ponderado sobre 100."""
        weights = [0.20, 0.20, 0.15, 0.15, 0.15, 0.15]
        deltas = [
            self.semantic_fidelity_delta,
            self.visual_hierarchy_delta,
            self.readability_delta,
            self.audience_fit_delta,
            self.professional_polish_delta,
            self.overall_preference_delta
        ]
        score = sum(w * d for w, d in zip(weights, deltas))
        return round(max(0.0, min(100.0, score)), 1)


class FailureAuditor:
    """Auditor formal de fallos y clasificador de debilidades de diseño."""

    @classmethod
    def audit_comparison(cls,
                         candidate_scores: Dict[str, float],
                         baseline_scores: Dict[str, float]) -> DesignAdvantageScore:
        """Calcula el diferencial de ventaja de diseño entre Sketion y el baseline."""
        return DesignAdvantageScore(
            semantic_fidelity_delta=candidate_scores.get("semantic_fidelity", 0.0) - baseline_scores.get("semantic_fidelity", 0.0),
            visual_hierarchy_delta=candidate_scores.get("visual_hierarchy", 0.0) - baseline_scores.get("visual_hierarchy", 0.0),
            readability_delta=candidate_scores.get("readability", 0.0) - baseline_scores.get("readability", 0.0),
            audience_fit_delta=candidate_scores.get("audience_fit", 0.0) - baseline_scores.get("audience_fit", 0.0),
            professional_polish_delta=candidate_scores.get("visual_quality", 0.0) - baseline_scores.get("visual_quality", 0.0),
            overall_preference_delta=candidate_scores.get("aesthetic_polish", 0.0) - baseline_scores.get("aesthetic_polish", 0.0)
        )
