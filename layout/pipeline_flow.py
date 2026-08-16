"""
Sketion Pipeline Flow Layout Engine (Arquetipo C & P)
Genera secuencias lineales y continuas con chevrons direccionales,
conectores ortogonales a 90°, pasos numerados y bucles de retorno visibles.
"""

from typing import Dict, Any, List, Optional
from render.excalidraw_builder import ExcalidrawScene


class PipelineFlowLayoutEngine:
    """Generador especializado en Pipelines y Flujos de Procesos Secuenciales."""

    @staticmethod
    def render_pipeline(scene: ExcalidrawScene,
                        x: float, y: float, w: float, h: float,
                        steps: List[Dict[str, Any]],
                        hero_idx: int = 1,
                        return_loop: bool = False,
                        frame_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Renderiza un pipeline continuo con tarjetas direccionales, números de paso
        y flechas ortogonales con pastillas de datos.
        """
        rendered_nodes = []
        step_count = len(steps)
        if step_count == 0:
            return rendered_nodes

        # Disposición horizontal
        gap = 24.0
        step_w = (w - (step_count - 1) * gap) / step_count
        step_h = min(140.0, h - 40.0)
        node_y = y + (h - step_h) * 0.5

        for i, step in enumerate(steps):
            sx = x + i * (step_w + gap)
            is_hero = (i == hero_idx) or step.get("is_hero", False)
            title = step.get("title", f"Step {i+1}")
            sublabel = step.get("sublabel", "")
            badge = step.get("badge", f"PASO {i+1}")
            icon = step.get("icon", "server")

            node = scene.add_quad_card(
                sx, node_y, step_w, step_h,
                title=title, sublabel=sublabel,
                badge=badge, icon=icon,
                is_hero=is_hero, font_size=14,
                frame_id=frame_id
            )
            rendered_nodes.append(node)

            # Conector horizontal hacia el siguiente paso
            if i < step_count - 1:
                edge_label = step.get("edge_label", "")
                scene.add_arrow(
                    sx + step_w, node_y + (step_h * 0.5),
                    sx + step_w + gap, node_y + (step_h * 0.5),
                    stroke="#2563EB" if is_hero else "#64748B",
                    stroke_w=2.0 if is_hero else 1.5,
                    label=edge_label if edge_label else None,
                    frame_id=frame_id
                )

        # Bucle de retorno (Feedback Loop) si aplica
        if return_loop and step_count > 2:
            track_y = node_y - 35.0
            last_x = x + (step_count - 1) * (step_w + gap) + (step_w * 0.5)
            first_x = x + (step_w * 0.5)
            scene.add_arrow(
                last_x, node_y,
                first_x, node_y,
                stroke="#D93829", stroke_w=1.8, dashed=True,
                orthogonal=True, track_y=track_y,
                label="RETRY / FEEDBACK LOOP",
                frame_id=frame_id
            )

        return rendered_nodes
