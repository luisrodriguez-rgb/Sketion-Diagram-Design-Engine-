"""
Sketion 7.0 — Adaptive Multi-Frame Reflow Engine
Determina de forma autónoma cuándo un diagrama debe ser Renderizado en 1 Solo Marco
o Cuándo debe Dividirse en una Narrativa Multi-Marco (2 a 3 marcos),
evitando a toda costa amontonar elementos o reducir fuentes por debajo de 16px.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Tuple


@dataclass
class FramePartitionDecision:
    recommended_frame_count: int
    frame_titles: List[str]
    split_strategy: str  # 'SINGLE_FRAME', 'DUAL_CONTRAST', 'TRIPLE_NARRATIVE'
    estimated_canvas_width: float
    estimated_canvas_height: float
    rationale: str


class AdaptiveMultiFrameEngine:
    """Calcula la partición física de marcos en el lienzo Excalidraw."""

    @classmethod
    def evaluate_partition(cls, node_count: int, intent: str, complexity_signals: int = 1) -> FramePartitionDecision:
        # Regla 1: Menos de 8 nodos e intención simple -> 1 Marco amplio
        if node_count <= 8 and intent not in ["TRANSFORMATION", "MATURITY_ROADMAP"]:
            return FramePartitionDecision(
                recommended_frame_count=1,
                frame_titles=["Diagrama Principal"],
                split_strategy="SINGLE_FRAME",
                estimated_canvas_width=1200.0,
                estimated_canvas_height=800.0,
                rationale=f"Carga semántica baja ({node_count} nodos): 1 solo marco amplio para máxima concentración visual."
            )

        # Regla 2: Intención de Transformación / Contraste con 8-15 nodos -> 2 Marcos (As-Is vs To-Be)
        elif intent in ["TRANSFORMATION", "COMPARISON"] and node_count <= 14:
            return FramePartitionDecision(
                recommended_frame_count=2,
                frame_titles=["01. Diagnóstico & Estado Actual (As-Is)", "02. Arquitectura de Solución (To-Be)"],
                split_strategy="DUAL_CONTRAST",
                estimated_canvas_width=2200.0,
                estimated_canvas_height=850.0,
                rationale="Transformación/Comparativa: 2 marcos lado a lado para máximo impacto narrativo de contraste."
            )

        # Regla 3: Alta densidad / Complejidad (>14 nodos o intención de operaciones/cadena) -> 3 Marcos Narrativos
        else:
            return FramePartitionDecision(
                recommended_frame_count=3,
                frame_titles=[
                    "01. Diagnóstico & Problema",
                    "02. Coordinación Operativa & Arquitectura",
                    "03. Capacidad, Control & Impacto"
                ],
                split_strategy="TRIPLE_NARRATIVE",
                estimated_canvas_width=3200.0,
                estimated_canvas_height=900.0,
                rationale=f"Alta carga semántica ({node_count} nodos): 3 marcos narrativos progresivos para garantizar aire y legibilidad."
            )
