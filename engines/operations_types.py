"""
Sketion 4.0 — Motores de Procesos, Operaciones y Organización (engines/operations_types.py)
Implementa:
19. Swimlane (Cross-Functional Flow Across Actors/Departments)
20. Process (Multi-Actor Sequential Workflow)
21. Gantt (Tasks and Phases on a Horizontal Timeline with Milestones)
22. Timeline (Events on an Axis with Alternating Milestone Callouts)
23. Org Chart (Ownership, Routing and Leadership Hierarchy)
24. Tree (Balanced Hierarchical Taxonomy)
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
# 19. SWIMLANE (CROSS-FUNCTIONAL WORKFLOW)
# =============================================================================
def render_swimlane(scene: ExcalidrawScene, title: str,
                    lanes: List[Dict[str, Any]], x: float, y: float,
                    w: float = 2800.0, h: float = 850.0,
                    frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"SWIMLANE: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "flujo de trabajo interdepartamental segregado por carriles funcionales", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    lane_count = len(lanes)
    lane_h = 160.0
    start_y = y + 130.0

    for li, lane in enumerate(lanes):
        ly = start_y + li * (lane_h + 15.0)
        lname = lane.get("name", f"Lane {li+1}")
        lsteps = lane.get("steps", [])
        
        # Header de carril
        scene.add_bound_card(x + 60.0, ly, 240.0, lane_h, lname.upper(),
                             bg=PALETTE["INK"], stroke=PALETTE["INK"], text_color="#FFFFFF",
                             font_size=13, roundness_type=3, frame_id=fid)
        
        # Carril contenedor
        scene.add_rect(x + 315.0, ly, w - 375.0, lane_h, bg="#FFFFFF",
                       stroke=PALETTE["CARD_BORDER"], stroke_w=1.0, roundness_type=3, frame_id=fid)

        # Pasos dentro del carril
        step_w = (w - 420.0) / max(1, len(lsteps))
        for si, stxt in enumerate(lsteps):
            sx = x + 335.0 + si * step_w
            scene.add_bound_card(sx, ly + 25.0, step_w - 30.0, 110.0, stxt,
                                 bg="#FFFFFF", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                                 font_size=12, roundness_type=3, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 20. PROCESS (MULTI-ACTOR SEQUENTIAL WORKFLOW)
# =============================================================================
def render_process(scene: ExcalidrawScene, title: str,
                   steps: List[Dict[str, Any]], x: float, y: float,
                   w: float = 2800.0, h: float = 850.0,
                   frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"PROCESS: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "flujo secuencial de proceso de negocio con handoffs entre actores", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    s_count = len(steps)
    step_w = (w - 120.0 - (s_count - 1) * 60.0) / s_count
    coords = []

    for si, step in enumerate(steps):
        sx = x + 60.0 + si * (step_w + 60.0)
        sy = y + 340.0
        snum = step.get("num", f"0{si+1}")
        stitle = step.get("title", f"Paso {si+1}")
        sactor = step.get("actor", "")
        is_hero = step.get("is_hero", False)
        
        bg = PALETTE["PASTEL_GREEN"] if is_hero else "#FFFFFF"
        c, _ = scene.add_dual_card(sx, sy, step_w, 130.0, f"[{snum}] {stitle.upper()}", sublabel=f"Actor: {sactor}",
                                   bg=bg, stroke=PALETTE["INK"], text_color=PALETTE["INK"], frame_id=fid)
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
                 x: float, y: float, w: float = 2800.0, h: float = 850.0,
                 frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"GANTT: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "cronograma gantt de fases, dependencias y puertas de aprobacion (gates)", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Cabecera de Meses
    month_w = (w - 380.0) / len(months)
    for mi, mname in enumerate(months):
        mx = x + 320.0 + mi * month_w
        scene.add_bound_card(mx, y + 130.0, month_w - 10.0, 45.0, mname.upper(),
                             bg=PALETTE["INK"], stroke=PALETTE["INK"], text_color="#FFFFFF",
                             font_size=12, roundness_type=None, frame_id=fid)

    # Filas de Tareas
    for ti, task in enumerate(tasks):
        ty = y + 190.0 + ti * 75.0
        tname = task.get("name", f"Tarea {ti+1}")
        start_m = task.get("start_month", 0.0) # 0 a len(months)
        duration_m = task.get("duration", 1.0)
        is_gate = task.get("is_gate", False)
        
        # Etiqueta izquierda
        scene.add_bound_card(x + 60.0, ty, 240.0, 60.0, tname,
                             bg="#FFFFFF", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                             font_size=12, roundness_type=3, frame_id=fid)
        
        # Barra Gantt
        bx = x + 320.0 + start_m * month_w
        bw = duration_m * month_w - 10.0
        bg = PALETTE["PAIN_BG"] if is_gate else PALETTE["PASTEL_BLUE"]
        stroke = PALETTE["PAIN_BORDER"] if is_gate else PALETTE["INK"]
        scene.add_bound_card(bx, ty + 10.0, bw, 40.0, "GATE" if is_gate else "",
                             bg=bg, stroke=stroke, text_color=PALETTE["INK"],
                             font_size=11, roundness_type=3, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 22. TIMELINE (EVENTS ON AN AXIS)
# =============================================================================
def render_timeline(scene: ExcalidrawScene, title: str,
                    milestones: List[Dict[str, str]], x: float, y: float,
                    w: float = 2800.0, h: float = 850.0,
                    frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"TIMELINE: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "eje cronologico de hitos estrategicos con llamadas alternadas", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    axis_y = y + 420.0
    scene.add_line(x + 100.0, axis_y, x + w - 100.0, axis_y, stroke=PALETTE["INK"], stroke_w=2.5, frame_id=fid)

    t_layout = compute_timeline_layout(len(milestones), start_x=x + 150.0, axis_y=axis_y, total_width=w - 300.0, step_w=320.0, step_h=95.0, offset_y=160.0)

    for i, pt in enumerate(t_layout):
        ms = milestones[i]
        m_date = ms.get("date", f"Q{i+1}")
        m_title = ms.get("title", f"Hito {i+1}")
        
        # Marcador en el eje
        scene.add_ellipse(pt["marker_x"] - 8.0, axis_y - 8.0, 16.0, 16.0, bg=PALETTE["INK"], stroke=PALETTE["INK"], frame_id=fid)
        
        # Conector vertical al hito
        scene.add_line(pt["marker_x"], axis_y, pt["marker_x"], pt["card_y"] + 45.0, stroke=PALETTE["CARD_BORDER"], stroke_w=1.5, dashed=True, frame_id=fid)
        
        # Tarjeta de Hito
        scene.add_bound_card(pt["card_x"], pt["card_y"], pt["w"], pt["h"], f"{m_date}\n{m_title}",
                             bg="#FFFFFF", stroke=PALETTE["INK"], text_color=PALETTE["INK"],
                             font_size=13, roundness_type=3, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 23. ORG CHART (LEADERSHIP & ROUTING HIERARCHY)
# =============================================================================
def render_org_chart(scene: ExcalidrawScene, title: str,
                     leader: Dict[str, str], departments: List[Dict[str, Any]],
                     x: float, y: float, w: float = 2800.0, h: float = 850.0,
                     frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"ORG CHART: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "organigrama jerarquico de propiedad y enrutamiento de equipos", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Leader Top Center
    leader_w = 400.0
    lx = x + (w - leader_w) * 0.5
    ly = y + 140.0
    scene.add_dual_card(lx, ly, leader_w, 100.0, leader.get("name", "Director").upper(), sublabel=leader.get("role", "CEO / Leadership"),
                        bg=PALETTE["INK"], stroke=PALETTE["INK"], text_color="#FFFFFF", frame_id=fid)

    # Departamentos
    dep_count = len(departments)
    dep_w = (w - 120.0 - (dep_count - 1) * 50.0) / dep_count

    for di, dep in enumerate(departments):
        dx = x + 60.0 + di * (dep_w + 50.0)
        dy = y + 340.0
        dname = dep.get("name", f"Depto {di+1}")
        dmembers = dep.get("members", [])
        
        # Caja de Departamento
        scene.add_scope_container(dx, dy, dep_w, 340.0, label=dname.upper(), stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid)
        
        # Conexión desde líder
        scene.add_line(x + w * 0.5, ly + 100.0, dx + dep_w * 0.5, dy, stroke=PALETTE["CARD_BORDER"], stroke_w=1.5, frame_id=fid)

        for mi, memb in enumerate(dmembers):
            scene.add_bound_card(dx + 20.0, dy + 55.0 + mi * 80.0, dep_w - 40.0, 65.0, memb,
                                 bg="#FFFFFF", stroke=PALETTE["INK"], text_color=PALETTE["INK"], font_size=12, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 24. TREE (BALANCED TAXONOMY)
# =============================================================================
def render_tree(scene: ExcalidrawScene, title: str,
                root_name: str, branches: List[Dict[str, Any]],
                x: float, y: float, w: float = 2800.0, h: float = 850.0,
                frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"TREE: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "arbol balanceado de taxonomias y clasificacion jerarquica", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Root
    rx = x + 100.0
    ry = y + 380.0
    scene.add_bound_card(rx, ry, 300.0, 110.0, root_name.upper(),
                         bg=PALETTE["INK"], stroke=PALETTE["INK"], text_color="#FFFFFF",
                         font_size=14, roundness_type=3, frame_id=fid)

    # Branches
    b_count = len(branches)
    b_spacing = 550.0 / max(1, b_count)
    
    for bi, branch in enumerate(branches):
        bx = x + 600.0
        by = y + 160.0 + bi * b_spacing
        bname = branch.get("name", f"Rama {bi+1}")
        subitems = branch.get("subitems", [])
        
        scene.add_bound_card(bx, by, 320.0, 75.0, bname,
                             bg=PALETTE["PASTEL_BLUE"], stroke=PALETTE["INK"], text_color=PALETTE["INK"],
                             font_size=13, roundness_type=3, frame_id=fid)
        scene.add_line(rx + 300.0, ry + 55.0, bx, by + 37.5, stroke=PALETTE["CARD_BORDER"], stroke_w=1.5, frame_id=fid)

        for si, sitem in enumerate(subitems):
            sx = bx + 420.0
            sy = by - 20.0 + si * 65.0
            scene.add_bound_card(sx, sy, 320.0, 55.0, sitem,
                                 bg="#FFFFFF", stroke=PALETTE["INK"], text_color=PALETTE["INK"], font_size=12, frame_id=fid)
            scene.add_line(bx + 320.0, by + 37.5, sx, sy + 27.5, stroke=PALETTE["CARD_BORDER"], stroke_w=1.0, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid
