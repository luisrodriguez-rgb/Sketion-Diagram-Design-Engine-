"""
Sketion 4.0 — Motores de Estrategia, Negocio y Consultoría (engines/strategy_types.py)
Implementa:
6. Consultant 2x2 (Scenario Matrix with Named Quadrant Cells)
7. Quadrant (Two-Axis Impact vs Effort Cartesian Positioning)
8. Loop / Flywheel (Stations around a Central Shared Memory Hub)
9. IT Current-State (Legacy Landscape Modernization)
10. Venn (2 & 3 Set Overlap with Intersections)
11. Pyramid / Funnel (Ranked Hierarchy / Conversion Drop-off)
"""

from typing import Dict, Any, List, Optional, Tuple
import math
from render.excalidraw_builder import ExcalidrawScene

PALETTE = {
    "CANVAS": "#F4F4F4",
    "CARD": "#FFFFFF",
    "CARD_BORDER": "#BDBDBD",
    "INK": "#0C0C0C",
    "MUTED": "#8B8B8B",
    "STICKY": "#FFE95C",
    "PAIN_RED": "#E03A2F",
    "PAIN_BG": "#FDEFEF",
    "PAIN_BORDER": "#F05A5A",
    "BANNER_PINK": "#F5BEC0",
    "PASTEL_BLUE": "#9BC7E4",
    "PASTEL_GREEN": "#C2E5D3"
}


# =============================================================================
# 6. CONSULTANT 2x2 (SCENARIO MATRIX)
# =============================================================================
def render_consultant_2x2(scene: ExcalidrawScene, title: str,
                          x_label: str, y_label: str,
                          quadrants: List[Dict[str, Any]],
                          x: float, y: float, w: float = 2800.0, h: float = 850.0,
                          frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"CONSULTANT 2x2: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, f"matriz de escenarios estrategicos: {y_label} vs {x_label}", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    grid_w = 1250.0
    grid_h = 280.0
    
    # 4 Cuadrantes: [Top-Left, Top-Right, Bottom-Left, Bottom-Right]
    positions = [
        (x + 120.0, y + 140.0),           # Q1: Top-Left
        (x + 120.0 + grid_w + 60.0, y + 140.0), # Q2: Top-Right (Hero)
        (x + 120.0, y + 140.0 + grid_h + 40.0), # Q3: Bottom-Left
        (x + 120.0 + grid_w + 60.0, y + 140.0 + grid_h + 40.0) # Q4: Bottom-Right
    ]

    for qi, qdata in enumerate(quadrants):
        qx, qy = positions[qi]
        q_name = qdata.get("name", f"Cuadrante {qi+1}")
        q_desc = qdata.get("desc", "")
        q_items = qdata.get("items", [])
        is_hero = qdata.get("is_hero", False)
        
        bg = PALETTE["PASTEL_GREEN"] if is_hero else "#FFFFFF"
        stroke = PALETTE["INK"] if is_hero else PALETTE["CARD_BORDER"]
        
        scene.add_scope_container(qx, qy, grid_w, grid_h, label=q_name.upper(), stroke=stroke, bg=bg, frame_id=fid)
        scene.add_text(qx + 20.0, qy + 45.0, q_desc, font_size=12, font_family=3, color=PALETTE["MUTED"], frame_id=fid)
        
        for ii, itxt in enumerate(q_items):
            iy = qy + 75.0 + ii * 65.0
            scene.add_bound_card(qx + 20.0, iy, grid_w - 40.0, 55.0, itxt,
                                 bg="#FFFFFF", stroke=PALETTE["INK"], text_color=PALETTE["INK"],
                                 font_size=12, roundness_type=3, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 7. QUADRANT (TWO-AXIS IMPACT VS EFFORT CARTESIAN)
# =============================================================================
def render_quadrant(scene: ExcalidrawScene, title: str,
                    x_axis: str, y_axis: str, points: List[Dict[str, Any]],
                    x: float, y: float, w: float = 2800.0, h: float = 850.0,
                    frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"QUADRANT: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, f"posicionamiento cartesiano bidimensional: eje horizontal ({x_axis}) vs vertical ({y_axis})", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    qw = 2200.0
    qh = 550.0
    qx = x + 300.0
    qy = y + 140.0

    # Fondo de cuadrícula
    scene.add_rect(qx, qy, qw, qh, bg="#FFFFFF", stroke=PALETTE["CARD_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid)
    
    # Ejes cartesianos cruzados
    mid_qx = qx + qw * 0.5
    mid_qy = qy + qh * 0.5
    scene.add_line(qx, mid_qy, qx + qw, mid_qy, stroke=PALETTE["CARD_BORDER"], stroke_w=1.5, dashed=True, frame_id=fid)
    scene.add_line(mid_qx, qy, mid_qx, qy + qh, stroke=PALETTE["CARD_BORDER"], stroke_w=1.5, dashed=True, frame_id=fid)

    # Etiquetas de ejes
    scene.add_text(qx + qw - 150.0, mid_qy + 15.0, x_axis.upper(), font_size=13, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(mid_qx + 15.0, qy + 15.0, y_axis.upper(), font_size=13, font_family=2, color=PALETTE["INK"], frame_id=fid)

    # Puntos posicionados
    for pt in points:
        px_rel = pt.get("x_val", 0.5) # 0.0 a 1.0
        py_rel = pt.get("y_val", 0.5) # 0.0 a 1.0 (1.0 es arriba)
        plbl = pt.get("label", "Point")
        is_hero = pt.get("is_hero", False)
        
        real_px = qx + px_rel * (qw - 240.0) + 40.0
        real_py = qy + (1.0 - py_rel) * (qh - 100.0) + 30.0
        
        bg = PALETTE["PASTEL_GREEN"] if is_hero else "#FFFFFF"
        stroke = PALETTE["INK"] if is_hero else PALETTE["CARD_BORDER"]
        scene.add_bound_card(real_px, real_py, 220.0, 60.0, plbl,
                             bg=bg, stroke=stroke, text_color=PALETTE["INK"],
                             font_size=11, roundness_type=3, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 8. LOOP / FLYWHEEL (CIRCULAR STATIONS AROUND A HUB)
# =============================================================================
def render_loop_flywheel(scene: ExcalidrawScene, title: str,
                         hub_label: str, stations: List[Dict[str, Any]],
                         x: float, y: float, w: float = 2800.0, h: float = 850.0,
                         frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"FLYWHEEL: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "bucle virtuoso continuo de crecimiento y retroalimentacion de estaciones", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    center_x = x + w * 0.5
    center_y = y + 420.0

    # Hub Central
    scene.add_ellipse(center_x - 180.0, center_y - 90.0, 360.0, 180.0,
                      bg=PALETTE["INK"], stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)
    scene.add_text(center_x - 140.0, center_y - 20.0, hub_label.upper(),
                   font_size=14, font_family=2, color="#FFFFFF", frame_id=fid)

    # Estaciones Perimetrales
    st_count = len(stations)
    radius_x = 850.0
    radius_y = 260.0
    st_coords = []

    for i, st in enumerate(stations):
        angle = (2.0 * math.pi / st_count) * i - (math.pi / 2.0)
        sx = center_x + radius_x * math.cos(angle) - 180.0
        sy = center_y + radius_y * math.sin(angle) - 55.0
        
        st_title = st.get("title", f"Estación {i+1}")
        st_sub = st.get("sub", "")
        is_hero = st.get("is_hero", False)
        
        bg = PALETTE["PASTEL_GREEN"] if is_hero else "#FFFFFF"
        container, _ = scene.add_dual_card(sx, sy, 360.0, 110.0, st_title, sublabel=st_sub,
                                           bg=bg, stroke=PALETTE["INK"], text_color=PALETTE["INK"], frame_id=fid)
        st_coords.append((sx + 180.0, sy + 55.0))

    # Flechas de conexión circular entre estaciones
    for i in range(st_count):
        x1, y1 = st_coords[i]
        x2, y2 = st_coords[(i + 1) % st_count]
        scene.add_arrow(x1, y1, x2, y2, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 9. IT CURRENT-STATE (LEGACY LANDSCAPE VS MODERNIZATION)
# =============================================================================
def render_it_current_state(scene: ExcalidrawScene, title: str,
                            legacy_systems: List[str], pain_points: List[str],
                            target_platform: List[str], x: float, y: float,
                            w: float = 2800.0, h: float = 850.0,
                            frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"IT CURRENT-STATE: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "mapa de modernizacion de sistemas legados: diagnostico de silos caoticos vs arquitectura destino", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # 1. Silos Legados
    scene.add_scope_container(x + 60.0, y + 130.0, 850.0, 520.0, label="1. ECOSISTEMA ACTUAL (SILOS HEREDADOS)", stroke=PALETTE["PAIN_BORDER"], bg=PALETTE["PAIN_BG"], frame_id=fid)
    for li, lsys in enumerate(legacy_systems):
        scene.add_bound_card(x + 90.0, y + 190.0 + li * 95.0, 790.0, 75.0, lsys,
                             bg="#FFFFFF", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"], font_size=12, frame_id=fid)

    # 2. Dolores Operativos (Post-its)
    scene.add_scope_container(x + 970.0, y + 130.0, 800.0, 520.0, label="2. PUNTOS DE DOLOR & FRICCIÓN", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid)
    for pi, pain in enumerate(pain_points):
        scene.add_sticky_note(x + 1010.0, y + 190.0 + pi * 105.0, 720.0, 85.0, pain,
                              angle_deg=-1.0 if pi % 2 == 0 else 1.0, font_size=12, frame_id=fid)

    # 3. Plataforma Destino
    scene.add_scope_container(x + 1830.0, y + 130.0, 900.0, 520.0, label="3. PLATAFORMA DESTINO UNIFICADA", stroke=PALETTE["CARD_BORDER"], bg=PALETTE["PASTEL_GREEN"], frame_id=fid)
    for ti, tgt in enumerate(target_platform):
        scene.add_bound_card(x + 1860.0, y + 190.0 + ti * 95.0, 840.0, 75.0, tgt,
                             bg="#FFFFFF", stroke=PALETTE["INK"], text_color=PALETTE["INK"], font_size=12, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 10. VENN (2 & 3 SET OVERLAPS)
# =============================================================================
def render_venn(scene: ExcalidrawScene, title: str,
                sets_data: List[Dict[str, str]], intersection_text: str,
                x: float, y: float, w: float = 2800.0, h: float = 850.0,
                frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"VENN: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "diagrama de conjuntos y superposicion conceptual", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    cx = x + w * 0.5
    cy = y + 420.0

    # 3 Círculos superpuestos
    c_radius = 280.0
    scene.add_ellipse(cx - 300.0, cy - 120.0, c_radius * 2, c_radius * 2, bg="transparent", stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)
    scene.add_ellipse(cx - 50.0, cy - 120.0, c_radius * 2, c_radius * 2, bg="transparent", stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)
    scene.add_ellipse(cx - 175.0, cy + 80.0, c_radius * 2, c_radius * 2, bg="transparent", stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)

    # Textos de los 3 conjuntos
    if len(sets_data) >= 3:
        scene.add_text(cx - 380.0, cy - 160.0, sets_data[0].get("name", "Set A").upper(), font_size=16, font_family=2, color=PALETTE["INK"], frame_id=fid)
        scene.add_text(cx + 180.0, cy - 160.0, sets_data[1].get("name", "Set B").upper(), font_size=16, font_family=2, color=PALETTE["INK"], frame_id=fid)
        scene.add_text(cx - 100.0, cy + 300.0, sets_data[2].get("name", "Set C").upper(), font_size=16, font_family=2, color=PALETTE["INK"], frame_id=fid)

    # Intersección Central (Sweet Spot)
    scene.add_bound_card(cx - 100.0, cy + 20.0, 200.0, 70.0, intersection_text,
                         bg=PALETTE["PASTEL_GREEN"], stroke=PALETTE["INK"], text_color=PALETTE["INK"],
                         font_size=12, roundness_type=3, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 11. PYRAMID / FUNNEL (RANKED HIERARCHY / DROP-OFF)
# =============================================================================
def render_pyramid_funnel(scene: ExcalidrawScene, title: str,
                          tiers: List[Dict[str, Any]], x: float, y: float,
                          w: float = 2800.0, h: float = 850.0,
                          frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"PYRAMID: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "jerarquia piramidal de capas y embudo de conversion", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    tier_count = len(tiers)
    base_w = 2000.0
    tier_h = 95.0
    start_y = y + 140.0

    for ti, tier in enumerate(tiers):
        t_w = base_w - ti * (base_w * 0.7 / max(1, tier_count))
        tx = x + (w - t_w) * 0.5
        ty = start_y + ti * (tier_h + 15.0)
        
        t_name = tier.get("name", f"Nivel {ti+1}")
        t_stat = tier.get("stat", "")
        is_top = (ti == tier_count - 1)
        
        bg = PALETTE["PASTEL_GREEN"] if is_top else "#FFFFFF"
        scene.add_bound_card(tx, ty, t_w, tier_h, f"{t_name} — {t_stat}",
                             bg=bg, stroke=PALETTE["INK"], text_color=PALETTE["INK"],
                             font_size=14, roundness_type=3, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid
