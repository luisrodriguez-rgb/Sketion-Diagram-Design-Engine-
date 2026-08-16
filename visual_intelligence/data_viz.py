"""
Sketion Light Data Visualization Engine (v8.1)
Genera componentes de visualización cuantitativa ligera en Excalidraw:
- KPICardSpec: Cajas de KPIs ejecutivos con valor prominente y badge de SLA.
- ComparisonBarSpec: Barras comparativas de rendimiento o disponibilidad.
- FunnelStepSpec: Bloques de conversión de embudo (Funnel) con ratios decrecientes.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, List, Optional
from render.excalidraw_builder import ExcalidrawScene


class DataVizType(Enum):
    KPI_CARD = "KPI_CARD"
    COMPARISON_BARS = "COMPARISON_BARS"
    FUNNEL_STEP = "FUNNEL_STEP"
    PROGRESS_BAR = "PROGRESS_BAR"


@dataclass
class KPICardSpec:
    value: str
    label: str
    subtext: str
    status_color: str = "#059669"
    badge: str = "SLO"


@dataclass
class ComparisonBarSpec:
    category: str
    percentage: float  # 0 to 100
    metric_label: str
    bar_color: str = "#2563EB"


@dataclass
class FunnelStepSpec:
    step_name: str
    volume_label: str
    conversion_pct: str
    is_hero: bool = False


class LightDataVizEngine:
    """Motor de renderizado de elementos de visualización de datos en Excalidraw."""

    @staticmethod
    def render_kpi_card(scene: ExcalidrawScene, x: float, y: float, w: float, h: float,
                        spec: KPICardSpec, frame_id: Optional[str] = None):
        # Contenedor
        scene.add_rect(x, y, w, h, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=frame_id)

        # Badge superior
        bw = len(spec.badge) * 7.0 + 16.0
        scene.add_rect(x + 12.0, y + 10.0, bw, 20.0, bg="#F1F5F9", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
        scene.add_text(x + 16.0, y + 12.0, spec.badge, font_size=10, font_family=2, color="#475569", frame_id=frame_id)

        # Valor Gigante
        scene.add_text(x + 14.0, y + 36.0, spec.value, font_size=24, font_family=2, color=spec.status_color, frame_id=frame_id)

        # Label & Subtexto
        scene.add_text(x + 14.0, y + 72.0, spec.label.upper(), font_size=11, font_family=2, color="#0F172A", frame_id=frame_id)
        if spec.subtext:
            scene.add_text(x + 14.0, y + 90.0, spec.subtext, font_size=10, font_family=3, color="#64748B", frame_id=frame_id)

    @staticmethod
    def render_comparison_strip(scene: ExcalidrawScene, x: float, y: float, w: float, h: float,
                                title: str, bars: List[ComparisonBarSpec], frame_id: Optional[str] = None):
        scene.add_rect(x, y, w, h, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=frame_id)
        scene.add_text(x + 16.0, y + 12.0, title.upper(), font_size=12, font_family=2, color="#0F172A", frame_id=frame_id)

        bar_h = 16.0
        start_y = y + 42.0
        avail_bar_w = w - 180.0

        for idx, bar in enumerate(bars):
            by = start_y + idx * 28.0
            # Nombre de la categoría
            scene.add_text(x + 16.0, by, bar.category, font_size=11, font_family=2, color="#334155", frame_id=frame_id)

            # Fondo de la barra
            scene.add_rect(x + 100.0, by + 2.0, avail_bar_w, bar_h, bg="#F1F5F9", stroke="#E2E8F0", stroke_w=1.0, roundness_type=3, frame_id=frame_id)

            # Relleno de porcentaje
            fill_w = max(5.0, (bar.percentage / 100.0) * avail_bar_w)
            scene.add_rect(x + 100.0, by + 2.0, fill_w, bar_h, bg=bar.bar_color, stroke=bar.bar_color, stroke_w=1.0, roundness_type=3, frame_id=frame_id)

            # Etiqueta métrica al final
            scene.add_text(x + 110.0 + avail_bar_w, by, bar.metric_label, font_size=11, font_family=3, color="#0F172A", frame_id=frame_id)

    @staticmethod
    def render_funnel(scene: ExcalidrawScene, x: float, y: float, w: float, h: float,
                      steps: List[FunnelStepSpec], frame_id: Optional[str] = None):
        step_cnt = len(steps)
        step_h = (h - 20.0 - (step_cnt - 1) * 12.0) / max(1, step_cnt)

        for i, st in enumerate(steps):
            sy = y + 10.0 + i * (step_h + 12.0)
            # Ancho decreciente proporcional
            width_factor = 1.0 - (i * 0.12)
            cur_w = w * width_factor
            cur_x = x + (w - cur_w) * 0.5

            bg = "#FFF5F2" if st.is_hero else "#EFF6FF"
            stroke = "#D93829" if st.is_hero else "#2563EB"

            scene.add_rect(cur_x, sy, cur_w, step_h, bg=bg, stroke=stroke, stroke_w=1.8 if st.is_hero else 1.2, roundness_type=3, frame_id=frame_id)
            scene.add_text(cur_x + 16.0, sy + (step_h * 0.5) - 8.0, st.step_name, font_size=13, font_family=2, color="#0F172A", frame_id=frame_id)
            scene.add_text(cur_x + cur_w - 140.0, sy + (step_h * 0.5) - 8.0, f"{st.volume_label} ({st.conversion_pct})", font_size=11, font_family=3, color=stroke, frame_id=frame_id)
