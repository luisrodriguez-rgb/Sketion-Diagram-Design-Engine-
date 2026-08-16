"""
Sketion 4.0 — Motores de Visualización Cuantitativa de Datos (engines/dataviz_types.py)
Implementa:
25. Bar Chart (Categorical Comparison with Hero Accent Bar)
26. Line Chart (Trends Over Time with Series Markers & Legends)
27. Scatter Plot (Distribution and Correlation on Cartesian Plane)
28. Radar / Spider (Multi-Axis Concentric Comparison Polygon)
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
# 25. BAR CHART (CATEGORICAL COMPARISON)
# =============================================================================
def render_bar_chart(scene: ExcalidrawScene, title: str,
                     categories: List[str], values: List[float],
                     hero_idx: int = 2, x: float = 0.0, y: float = 0.0,
                     w: float = 2800.0, h: float = 850.0,
                     frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"BAR CHART: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "grafico comparativo de barras cuantitativas con acento focal", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    chart_x = x + 250.0
    chart_y = y + 160.0
    chart_w = 2300.0
    chart_h = 460.0

    # Ejes
    scene.add_line(chart_x, chart_y + chart_h, chart_x + chart_w, chart_y + chart_h, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)
    scene.add_line(chart_x, chart_y, chart_x, chart_y + chart_h, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)

    # Barras
    bar_count = len(categories)
    spacing = chart_w / max(1, bar_count)
    bar_w = spacing * 0.55
    max_val = max(values) if values else 100.0

    for bi, cat in enumerate(categories):
        val = values[bi] if bi < len(values) else 0.0
        bar_h = (val / max_val) * (chart_h - 60.0)
        bx = chart_x + bi * spacing + spacing * 0.22
        by = chart_y + chart_h - bar_h
        is_hero = (bi == hero_idx)
        
        bg = PALETTE["PASTEL_GREEN"] if is_hero else PALETTE["PASTEL_BLUE"]
        scene.add_rect(bx, by, bar_w, bar_h, bg=bg, stroke=PALETTE["INK"], stroke_w=1.5, roundness_type=3, frame_id=fid)
        
        # Etiqueta numérica arriba
        scene.add_text(bx + bar_w * 0.2, by - 30.0, f"{val:.0f}", font_size=14, font_family=2, color=PALETTE["INK"], frame_id=fid)
        
        # Etiqueta de categoría abajo
        scene.add_text(bx, chart_y + chart_h + 15.0, cat, font_size=12, font_family=2, color=PALETTE["INK"], frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 26. LINE CHART (TRENDS OVER TIME)
# =============================================================================
def render_line_chart(scene: ExcalidrawScene, title: str,
                      x_labels: List[str], series_data: List[Dict[str, Any]],
                      x: float = 0.0, y: float = 0.0,
                      w: float = 2800.0, h: float = 850.0,
                      frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"LINE CHART: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "grafico de lineas continuas y evolucion de tendencias temporales", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    chart_x = x + 250.0
    chart_y = y + 160.0
    chart_w = 2300.0
    chart_h = 460.0

    # Ejes
    scene.add_line(chart_x, chart_y + chart_h, chart_x + chart_w, chart_y + chart_h, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)
    scene.add_line(chart_x, chart_y, chart_x, chart_y + chart_h, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)

    # Etiquetas X
    x_count = len(x_labels)
    step_x = chart_w / max(1, x_count - 1)
    for xi, xlbl in enumerate(x_labels):
        scene.add_text(chart_x + xi * step_x - 15.0, chart_y + chart_h + 15.0, xlbl, font_size=12, font_family=2, color=PALETTE["INK"], frame_id=fid)

    # Series
    for s in series_data:
        vals = s.get("values", [])
        scolor = s.get("color", PALETTE["INK"])
        is_hero = s.get("is_hero", False)
        pts = []
        for vi, val in enumerate(vals):
            px = chart_x + vi * step_x
            py = chart_y + chart_h - (val / 100.0) * (chart_h - 40.0)
            pts.append((px, py))
            scene.add_ellipse(px - 5.0, py - 5.0, 10.0, 10.0, bg=scolor, stroke=scolor, frame_id=fid)

        for pi in range(len(pts) - 1):
            scene.add_line(pts[pi][0], pts[pi][1], pts[pi+1][0], pts[pi+1][1], stroke=scolor, stroke_w=2.5 if is_hero else 1.5, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 27. SCATTER PLOT (DISTRIBUTION & CORRELATION)
# =============================================================================
def render_scatter_plot(scene: ExcalidrawScene, title: str,
                        points: List[Tuple[float, float, str]],
                        x_label: str, y_label: str,
                        x: float = 0.0, y: float = 0.0,
                        w: float = 2800.0, h: float = 850.0,
                        frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"SCATTER PLOT: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, f"diagrama de dispersion y correlacion: {y_label} vs {x_label}", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    chart_x = x + 300.0
    chart_y = y + 160.0
    chart_w = 2200.0
    chart_h = 480.0

    scene.add_rect(chart_x, chart_y, chart_w, chart_h, bg="#FFFFFF", stroke=PALETTE["CARD_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid)
    scene.add_text(chart_x + chart_w - 180.0, chart_y + chart_h - 30.0, x_label.upper(), font_size=13, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(chart_x + 20.0, chart_y + 20.0, y_label.upper(), font_size=13, font_family=2, color=PALETTE["INK"], frame_id=fid)

    for px_rel, py_rel, plbl in points:
        real_x = chart_x + px_rel * (chart_w - 100.0) + 50.0
        real_y = chart_y + (1.0 - py_rel) * (chart_h - 100.0) + 50.0
        scene.add_ellipse(real_x - 6.0, real_y - 6.0, 12.0, 12.0, bg=PALETTE["PAIN_RED"], stroke=PALETTE["PAIN_RED"], frame_id=fid)
        scene.add_text(real_x + 12.0, real_y - 8.0, plbl, font_size=11, font_family=3, color=PALETTE["INK"], frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 28. RADAR / SPIDER (MULTI-AXIS RADIAL COMPARISON)
# =============================================================================
def render_radar_spider(scene: ExcalidrawScene, title: str,
                        axes: List[str], series_values: List[Dict[str, Any]],
                        x: float = 0.0, y: float = 0.0,
                        w: float = 2800.0, h: float = 850.0,
                        frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"RADAR: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "comparativa multieje poligonal sobre coordenadas radiales concentricas", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    center_x = x + w * 0.5
    center_y = y + 430.0
    ax_count = len(axes)
    max_r = 240.0

    # Anillos concéntricos
    for ring in [0.33, 0.66, 1.0]:
        scene.add_ellipse(center_x - max_r * ring, center_y - max_r * ring, max_r * 2 * ring, max_r * 2 * ring,
                          bg="transparent", stroke=PALETTE["CARD_BORDER"], stroke_w=1.0, frame_id=fid)

    # Ejes radiales y etiquetas
    for ai, aname in enumerate(axes):
        angle = (2.0 * math.pi / ax_count) * ai - (math.pi / 2.0)
        ex = center_x + max_r * math.cos(angle)
        ey = center_y + max_r * math.sin(angle)
        scene.add_line(center_x, center_y, ex, ey, stroke=PALETTE["CARD_BORDER"], stroke_w=1.0, frame_id=fid)
        
        lbl_x = center_x + (max_r + 40.0) * math.cos(angle) - 40.0
        lbl_y = center_y + (max_r + 40.0) * math.sin(angle) - 10.0
        scene.add_text(lbl_x, lbl_y, aname, font_size=12, font_family=2, color=PALETTE["INK"], frame_id=fid)

    # Polígono de datos
    for s in series_values:
        vals = s.get("values", []) # 0.0 a 1.0
        scolor = s.get("color", PALETTE["PAIN_RED"])
        pts = []
        for vi, val in enumerate(vals):
            angle = (2.0 * math.pi / ax_count) * vi - (math.pi / 2.0)
            r = max_r * val
            px = center_x + r * math.cos(angle)
            py = center_y + r * math.sin(angle)
            pts.append((px, py))
            scene.add_ellipse(px - 4.0, py - 4.0, 8.0, 8.0, bg=scolor, stroke=scolor, frame_id=fid)

        for pi in range(len(pts)):
            p1 = pts[pi]
            p2 = pts[(pi + 1) % len(pts)]
            scene.add_line(p1[0], p1[1], p2[0], p2[1], stroke=scolor, stroke_w=2.0, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid
