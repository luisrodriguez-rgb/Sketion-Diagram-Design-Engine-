"""
Sketion Radial Hub Layout Engine (Arquetipo A - El Cerebro)
Genera topologías radiales con un núcleo focal central y satélites orbitando.
"""

from typing import Dict, Any, List, Optional
import math
from render.excalidraw_builder import ExcalidrawScene


class RadialHubLayoutEngine:
    """Generador especializado en Topologías Radiales y Ecosistemas de Hub & Spoke."""

    @staticmethod
    def render_radial_ecosystem(scene: ExcalidrawScene,
                                cx: float, cy: float,
                                radius: float,
                                hub: Dict[str, Any],
                                satellites: List[Dict[str, Any]],
                                frame_id: Optional[str] = None):
        """
        Renderiza un Hub Central con nodos satélites distribuidos uniformemente en circunferencia.
        """
        # 1. Hub Central
        hw, hh = 260.0, 120.0
        hx = cx - (hw * 0.5)
        hy = cy - (hh * 0.5)
        hub_title = hub.get("title", "CORE HUB")
        hub_sub = hub.get("sublabel", "Ecosistema Central")
        hub_badge = hub.get("badge", "CENTRAL")
        hub_icon = hub.get("icon", "server")

        scene.add_quad_card(hx, hy, hw, hh, hub_title, sublabel=hub_sub,
                            badge=hub_badge, icon=hub_icon, is_hero=True, font_size=16, frame_id=frame_id)

        # 2. Satélites
        sat_count = len(satellites)
        if sat_count == 0:
            return

        angle_step = (2 * math.pi) / sat_count
        for i, sat in enumerate(satellites):
            angle = i * angle_step - (math.pi / 2.0)
            sx = cx + radius * math.cos(angle)
            sy = cy + radius * math.sin(angle)
            sw, sh = 210.0, 95.0
            spx = sx - (sw * 0.5)
            spy = sy - (sh * 0.5)

            s_tit = sat.get("title", f"Satellite {i+1}")
            s_sub = sat.get("sublabel", "")
            s_badge = sat.get("badge", f"NODE {i+1}")
            s_icon = sat.get("icon", "laptop")

            scene.add_quad_card(spx, spy, sw, sh, s_tit, sublabel=s_sub, badge=s_badge, icon=s_icon, font_size=13, frame_id=frame_id)

            # Conector bidireccional
            start_x = cx + (hw * 0.45 * math.cos(angle))
            start_y = cy + (hh * 0.45 * math.sin(angle))
            end_x = spx + (sw * 0.5) - (sw * 0.45 * math.cos(angle))
            end_y = spy + (sh * 0.5) - (sh * 0.45 * math.sin(angle))

            scene.add_arrow(start_x, start_y, end_x, end_y, stroke="#94A3B8", stroke_w=1.2, dashed=True, frame_id=frame_id)
