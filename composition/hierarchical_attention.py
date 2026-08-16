"""
Sketion 4.5 — Hierarchical Attention Model
Gestiona el presupuesto de acentos y foco visual:
1. Intra-Frame: Exactamente 1 Héroe Principal + 0-1 Secundario.
2. Cross-Frame: Jerarquía narrativa global (evita que todos los frames compitan entre sí).
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional


@dataclass
class FrameAttentionPlan:
    frame_index: int
    frame_title: str
    narrative_role: str  # 'context', 'climax', 'resolution'
    max_heroes: int
    max_secondaries: int
    hero_accent_color: str
    rationale: str


class HierarchicalAttentionEngine:
    """Calcula la asignación narrativa de acentos visuales a través de múltiples marcos."""

    @classmethod
    def plan_narrative_attention(cls, frame_types: List[str], dominant_color: str = "#D93829") -> List[FrameAttentionPlan]:
        """
        Determina qué marco es el clímax visual y cuáles son de contexto o resolución.
        """
        plans = []
        total_frames = len(frame_types)

        for idx, f_type in enumerate(frame_types):
            if idx == 0 and total_frames > 1:
                role = "context_contrast"
                max_h = 2  # 1 en el dolor y 1 en la solución
                rationale = "Marco de diagnóstico inicial: foco en el contraste dolor vs solución"
            elif idx == 1 or (idx == total_frames - 2):
                role = "operational_climax"
                max_h = 2
                rationale = "Clímax operativo: foco en los componentes centrales de la arquitectura"
            else:
                role = "resolution_outcome"
                max_h = 1
                rationale = "Resolución y resultado final: 1 único foco en el entregable final"

            plans.append(FrameAttentionPlan(
                frame_index=idx + 1,
                frame_title=f"Frame {idx + 1} ({f_type})",
                narrative_role=role,
                max_heroes=max_h,
                max_secondaries=1,
                hero_accent_color=dominant_color,
                rationale=rationale
            ))

        return plans
