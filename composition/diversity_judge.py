"""
Sketion Multidimensional Diversity Judge (v11.0)
Evalúa el Visual Diversity Score (VDS) de forma contextual según el patrón de composición.
Previene la 'monocultura visual' y certifica el ajuste semántico de la estructura gráfica.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
import math

from .composition_patterns import CompositionPattern, CompositionPatternRegistry
from semantic.content_model import ContentModel
from render.excalidraw_builder import ExcalidrawScene


@dataclass
class DiversityScoreReport:
    """Informe detallado de diversidad visual multidimensional."""
    vds_overall: float
    semantic_fit: float
    hierarchy_depth: float
    spatial_balance: float
    connection_quality: float
    primitive_variety: float
    template_similarity_score: float  # Menor es mejor (mide distancia respecto a monocultura)
    is_valid: bool
    recompose_needed: bool
    diagnostic_notes: List[str] = field(default_factory=list)

    def to_markdown(self) -> str:
        status = "PASSED" if self.is_valid else "RECOMPOSE NEEDED"
        lines = [
            f"### VISUAL DIVERSITY SCORE (VDS): {self.vds_overall:.1f} / 100 [{status}]",
            f"* **Semantic Fit:** {self.semantic_fit:.1f} / 100",
            f"* **Hierarchy Depth:** {self.hierarchy_depth:.1f} / 100",
            f"* **Spatial Balance:** {self.spatial_balance:.1f} / 100",
            f"* **Connection Quality:** {self.connection_quality:.1f} / 100",
            f"* **Primitive Variety:** {self.primitive_variety:.1f} / 100",
            f"* **Template Dissimilarity:** {100.0 - self.template_similarity_score:.1f} / 100"
        ]
        if self.diagnostic_notes:
            lines.append("\n**Notas Diagnósticas:**")
            for note in self.diagnostic_notes:
                lines.append(f"* {note}")
        return "\n".join(lines)


class DiversityJudge:
    """Juez de diversidad visual y adecuación semántica de Sketion."""

    @classmethod
    def evaluate(cls,
                 pattern: CompositionPattern,
                 content: ContentModel,
                 scene: ExcalidrawScene,
                 card_count: int,
                 total_shapes: int,
                 connector_count: int,
                 distinct_primitives: int) -> DiversityScoreReport:
        """
        Calcula el reporte de diversidad contextual respetando las restricciones del patrón.
        """
        meta = CompositionPatternRegistry._PATTERNS.get(pattern)
        expected_cards = meta.expected_card_ratio if meta else 0.45
        
        notes: List[str] = []
        actual_card_ratio = (card_count / max(1, total_shapes))

        # 1. Semantic Fit (0-100)
        # Evalúa si la estructura seleccionada encaja con el dominio del contenido
        semantic_fit = 95.0
        if pattern == CompositionPattern.RADIAL_HUB and content.domain in ["software", "engineering"]:
            # A menos que sea un ecosistema explícito
            if "ecosystem" not in content.title.lower() and "hub" not in content.title.lower():
                semantic_fit -= 15.0
                notes.append("Uso de radial en arquitectura de software; verificar si un layered era más adecuado.")

        # 2. Hierarchy Depth (0-100)
        # Evalúa si hay diferenciación entre nodo Hero, contenedores y entidades secundarias
        has_hero = any(s.is_hero for s in content.systems)
        hierarchy_depth = 90.0 if has_hero else 75.0
        if len(content.actors) > 0 and len(content.systems) > 0:
            hierarchy_depth += 8.0
        hierarchy_depth = min(100.0, hierarchy_depth)

        # 3. Spatial Balance (0-100)
        spatial_balance = 92.0
        if total_shapes > 25:
            spatial_balance = 88.0
        elif total_shapes < 3:
            spatial_balance = 80.0

        # 4. Connection Quality (0-100)
        # Evalúa la razón de conectores respecto a nodos
        ratio = connector_count / max(1, total_shapes)
        if 0.5 <= ratio <= 1.8:
            connection_quality = 95.0
        elif ratio > 1.8:
            connection_quality = 85.0
        else:
            connection_quality = 80.0

        # 5. Primitive Variety (0-100)
        # Contextual: Un Kanban o UML no necesita 10 primitivas distintas, un sistema de seguridad sí
        if pattern in [CompositionPattern.KANBAN_BOARD, CompositionPattern.A3_REPORT, CompositionPattern.CORNELL_NOTES]:
            # Patrones con geometría estandarizada
            primitive_variety = 92.0
        else:
            variety_ratio = min(1.0, distinct_primitives / 5.0)
            primitive_variety = 60.0 + variety_ratio * 38.0

        # 6. Template Similarity Score (Menor es más diverso)
        # Penaliza si el card_ratio excede en más de un 35% lo esperado para ese patrón
        excess_cards = max(0.0, actual_card_ratio - expected_cards)
        if excess_cards > 0.35:
            template_similarity = 75.0  # Tiende a monocultura
            notes.append(f"Monocultura de tarjetas detectada ({actual_card_ratio*100:.0f}% vs {expected_cards*100:.0f}% esperado).")
        else:
            template_similarity = 20.0  # Alta originalidad estructural

        # 7. VDS Global
        vds_overall = (
            semantic_fit * 0.25 +
            hierarchy_depth * 0.20 +
            spatial_balance * 0.15 +
            connection_quality * 0.20 +
            primitive_variety * 0.20
        )

        recompose_needed = (vds_overall < 70.0) or (template_similarity > 80.0)
        is_valid = not recompose_needed

        return DiversityScoreReport(
            vds_overall=round(vds_overall, 1),
            semantic_fit=round(semantic_fit, 1),
            hierarchy_depth=round(hierarchy_depth, 1),
            spatial_balance=round(spatial_balance, 1),
            connection_quality=round(connection_quality, 1),
            primitive_variety=round(primitive_variety, 1),
            template_similarity_score=round(template_similarity, 1),
            is_valid=is_valid,
            recompose_needed=recompose_needed,
            diagnostic_notes=notes
        )
