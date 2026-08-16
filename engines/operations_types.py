"""
Sketion 4.0 — Motores de Procesos, Operaciones y Organización (engines/operations_types.py)
Incorpora la gramática editorial de Diagram Design:
- Eje superior de pasos con insignias circulares numeradas (add_step_badge_axis)
- Tarjetas de 4 esquinas (add_quad_card) con badges de rol y datos
- Dimensiones compactas anti-stretch
"""

from typing import Dict, Any, List, Optional, Tuple
from render.excalidraw_builder import ExcalidrawScene
from layout.flow import compute_timeline_layout

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
# 19. SWIMLANE (CROSS-FUNCTIONAL WORKFLOW WITH STEP AXIS)
# =============================================================================
def render_swimlane(scene: ExcalidrawScene, title: str,
                    lanes: List[Dict[str, Any]], x: float, y: float,
                    w: float = 2400.0, h: float = 850.0,
                    frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"SWIMLANE: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 72, "flujo de trabajo interdepartamental segregado por carriles funcionales", font_size=14, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # 1. Eje Superior de Pasos Circulares Numerados
    steps_header = ["Order", "Verify", "Allocate", "Pick", "Pack", "Receive"]
    scene.add_step_badge_axis(x + 280.0, y + 115.0, w - 340.0, steps_header, hero_idx=2, frame_id=fid)

    lane_count = len(lanes)
    lane_h = 160.0
    start_y = y + 175.0

    badge_map = {"Customer": "CUS", "Support": "SUP", "Warehouse": "WHS", "Finance": "FIN", "Kitchen": "KTN", "Runner": "RUN"}

    for li, lane in enumerate(lanes):
        ly = start_y + li * (lane_h + 15.0)
        lname = lane.get("name", f"Lane {li+1}")
        lsteps = lane.get("steps", [])
        badge_txt = badge_map.get(lname, "ROLE")
        
        # Header de carril lateral
        scene.add_bound_card(x + 50.0, ly, 200.0, lane_h, lname.upper(),
                             bg="#FFFFFF", stroke=PALETTE["INK"], text_color=PALETTE["INK"],
                             font_size=13, roundness_type=3, frame_id=fid)
        
        # Carril contenedor
        scene.add_rect(x + 265.0, ly, w - 315.0, lane_h, bg="#FFFFFF",
                       stroke=PALETTE["CARD_BORDER"], stroke_w=1.0, roundness_type=3, frame_id=fid)

        # Pasos dentro del carril
        step_w = min(300.0, (w - 360.0) / max(1, len(lsteps)))
        for si, stxt in enumerate(lsteps):
            sx = x + 285.0 + si * (step_w + 30.0)
            is_hero_step = (li == 1 and si == 1) or (li == 0 and si == 2)
            scene.add_quad_card(sx, ly + 20.0, step_w, 120.0, stxt,
                                sublabel=f"Handoff {si+1}", badge=badge_txt,
                                icon="user" if li == 0 else "container",
                                pills=["DB", "LS"] if is_hero_step else None,
                                is_hero=is_hero_step, frame_id=fid)

    # Leyenda Inferior
    scene.add_legend_footer(x + 50.0, start_y + lane_count * (lane_h + 15.0) + 15.0, w - 100.0,
                            swatches=[
                                {"label": "Critical Handoff", "is_arrow": True, "stroke": "#E03A2F"},
                                {"label": "Sequential Handoff", "is_arrow": True, "stroke": "#0C0C0C"},
                                {"label": "DB · records", "bg": "#E2E8F0", "stroke": "#94A3B8"}
                            ],
                            note="left in · right out · swimlanes enforce responsibility boundaries",
                            frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 20. PROCESS (MULTI-ACTOR SEQUENTIAL WORKFLOW)
# =============================================================================
def render_process(scene: ExcalidrawScene, title: str,
                   steps: List[Dict[str, Any]], x: float, y: float,
                   w: float = 2400.0, h: float = 850.0,
                   frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"PROCESS: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 72, "flujo secuencial de proceso de negocio con handoffs entre actores", font_size=14, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    s_count = len(steps)
    step_w = min(320.0, (w - 100.0 - (s_count - 1) * 40.0) / s_count)
    coords = []

    for si, step in enumerate(steps):
        sx = x + 50.0 + si * (step_w + 40.0)
        sy = y + 320.0
        snum = step.get("num", f"0{si+1}")
        stitle = step.get("title", f"Paso {si+1}")
        sactor = step.get("actor", "Actor")
        is_hero = step.get("is_hero", False)
        
        c, _ = scene.add_quad_card(sx, sy, step_w, 130.0, f"[{snum}] {stitle.upper()}",
                                   sublabel=f"Responsable: {sactor}",
                                   badge=f"ACT-{si+1}", icon="user" if not is_hero else "server",
                                   is_hero=is_hero, frame_id=fid)
        coords.append((c["x"], c["y"], c["width"], c["height"]))

    for i in range(s_count - 1):
        x1 = coords[i][0] + coords[i][2]
        y1 = coords[i][1] + coords[i][3] * 0.5
        x2 = coords[i+1][0]
        y2 = coords[i+1][1] + coords[i+1][3] * 0.5
        scene.add_arrow(x1, y1, x2, y2, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 21. GANTT (TIMELINE WITH PHASES AND MILESTONES)
# =============================================================================
def render_gantt(scene: ExcalidrawScene, title: str,
                 months: List[str], tasks: List[Dict[str, Any]],
                 x: float, y: float, w: float = 2400.0, h: float = 850.0,
                 frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"GANTT: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 72, "cronograma gantt de fases, dependencias y puertas de aprobacion (gates)", font_size=14, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Cabecera de Meses (Chevron Ribbon)
    scene.add_chevron_ribbon(x + 280.0, y + 115.0, w - 330.0, h=36.0, stages=months, bg=PALETTE["INK"], text_color="#FFFFFF", frame_id=fid)

    month_w = (w - 330.0) / len(months)
    for ti, task in enumerate(tasks):
        ty = y + 175.0 + ti * 75.0
        tname = task.get("name", f"Tarea {ti+1}")
        start_m = task.get("start_month", 0.0)
        duration_m = task.get("duration", 1.0)
        is_gate = task.get("is_gate", False)
        
        # Etiqueta izquierda
        scene.add_bound_card(x + 50.0, ty, 210.0, 60.0, tname,
                             bg="#FFFFFF", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                             font_size=12, roundness_type=3, frame_id=fid)
        
        # Barra Gantt
        bx = x + 280.0 + start_m * month_w
        bw = duration_m * month_w - 10.0
        bg = PALETTE["PAIN_BG"] if is_gate else "#F1F5F9"
        stroke = PALETTE["PAIN_BORDER"] if is_gate else PALETTE["INK"]
        text_col = PALETTE["PAIN_RED"] if is_gate else PALETTE["INK"]
        scene.add_bound_card(bx, ty + 10.0, bw, 40.0, "APPROVAL GATE" if is_gate else "In Progress",
                             bg=bg, stroke=stroke, text_color=text_col,
                             font_size=11, roundness_type=3, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 22. TIMELINE (EVENTS ON AN AXIS)
# =============================================================================
def render_timeline(scene: ExcalidrawScene, title: str,
                    milestones: List[Dict[str, str]], x: float, y: float,
                    w: float = 2400.0, h: float = 850.0,
                    frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"TIMELINE: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 72, "eje cronologico de hitos estrategicos con llamadas alternadas", font_size=14, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    axis_y = y + 420.0
    scene.add_line(x + 80.0, axis_y, x + w - 80.0, axis_y, stroke=PALETTE["INK"], stroke_w=2.5, frame_id=fid)

    t_layout = compute_timeline_layout(len(milestones), start_x=x + 120.0, axis_y=axis_y, total_width=w - 240.0, step_w=300.0, step_h=100.0, offset_y=160.0)

    for i, pt in enumerate(t_layout):
        ms = milestones[i]
        m_date = ms.get("date", f"Q{i+1}")
        m_title = ms.get("title", f"Hito {i+1}")
        is_hero = (i == len(milestones) - 1)
        
        scene.add_ellipse(pt["marker_x"] - 8.0, axis_y - 8.0, 16.0, 16.0, bg=PALETTE["INK"], stroke=PALETTE["INK"], frame_id=fid)
        scene.add_line(pt["marker_x"], axis_y, pt["marker_x"], pt["card_y"] + 50.0, stroke=PALETTE["CARD_BORDER"], stroke_w=1.5, dashed=True, frame_id=fid)
        
        scene.add_quad_card(pt["card_x"], pt["card_y"], pt["w"], pt["h"], m_title,
                            sublabel=m_date, badge=m_date, icon="monitoring" if is_hero else "terminal",
                            is_hero=is_hero, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 23. ORG CHART (LEADERSHIP & ROUTING HIERARCHY)
# =============================================================================
def render_org_chart(scene: ExcalidrawScene, title: str,
                     leader: Dict[str, str], departments: List[Dict[str, Any]],
                     x: float, y: float, w: float = 2400.0, h: float = 850.0,
                     frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"ORG CHART: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 72, "organigrama jerarquico de propiedad y enrutamiento de equipos", font_size=14, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Leader Top Center
    leader_w = 360.0
    lx = x + (w - leader_w) * 0.5
    ly = y + 130.0
    scene.add_quad_card(lx, ly, leader_w, 110.0, leader.get("name", "Director").upper(),
                        sublabel=leader.get("role", "CEO / Leadership"), badge="EXEC",
                        icon="user", is_hero=True, frame_id=fid)

    # Departamentos
    dep_count = len(departments)
    dep_w = (w - 100.0 - (dep_count - 1) * 40.0) / dep_count

    for di, dep in enumerate(departments):
        dx = x + 50.0 + di * (dep_w + 40.0)
        dy = y + 320.0
        dname = dep.get("name", f"Depto {di+1}")
        dmembers = dep.get("members", [])
        
        scene.add_scope_container(dx, dy, dep_w, 360.0, label=dname.upper(), stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid)
        scene.add_line(x + w * 0.5, ly + 110.0, dx + dep_w * 0.5, dy, stroke=PALETTE["CARD_BORDER"], stroke_w=1.5, frame_id=fid)

        cw = min(280.0, dep_w - 30.0)
        for mi, memb in enumerate(dmembers):
            scene.add_quad_card(dx + (dep_w - cw)*0.5, dy + 55.0 + mi * 95.0, cw, 80.0, memb,
                                sublabel="Team Member", badge="STAFF", icon="user", frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 24. TREE (BALANCED TAXONOMY)
# =============================================================================
def render_tree(scene: ExcalidrawScene, title: str,
                root_name: str, branches: List[Dict[str, Any]],
                x: float, y: float, w: float = 2400.0, h: float = 850.0,
                frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"TREE: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 72, "arbol balanceado de taxonomias y clasificacion jerarquica", font_size=14, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Root
    rx = x + 80.0
    ry = y + 360.0
    scene.add_quad_card(rx, ry, 280.0, 110.0, root_name.upper(),
                        sublabel="Taxonomy Root", badge="ROOT", icon="server", is_hero=True, frame_id=fid)

    b_count = len(branches)
    b_spacing = 550.0 / max(1, b_count)
    
    for bi, branch in enumerate(branches):
        bx = x + 480.0
        by = y + 160.0 + bi * b_spacing
        bname = branch.get("name", f"Rama {bi+1}")
        subitems = branch.get("subitems", [])
        
        scene.add_quad_card(bx, by, 300.0, 85.0, bname, sublabel="Branch Group", badge="BRANCH", icon="container", frame_id=fid)
        scene.add_line(rx + 280.0, ry + 55.0, bx, by + 42.5, stroke=PALETTE["CARD_BORDER"], stroke_w=1.5, frame_id=fid)

        for si, sitem in enumerate(subitems):
            sx = bx + 380.0
            sy = by - 20.0 + si * 75.0
            scene.add_quad_card(sx, sy, 280.0, 65.0, sitem, badge="LEAF", icon="file", frame_id=fid)
            scene.add_line(bx + 300.0, by + 42.5, sx, sy + 32.5, stroke=PALETTE["CARD_BORDER"], stroke_w=1.0, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid
