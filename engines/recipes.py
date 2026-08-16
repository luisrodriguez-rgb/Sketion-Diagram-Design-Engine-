"""
Sketion Engine Recipes (Desacoplado 2.0)
Conecta los Modelos Semánticos y Motores de Layout con el Render de Excalidraw.
"""

from typing import List, Dict, Any, Optional
from render.excalidraw_builder import ExcalidrawScene, place, rid
from layout.flow import compute_flow_layout, compute_timeline_layout
from layout.hierarchy import compute_tree_layout, compute_radial_layout
from layout.grid import compute_matrix_layout, compute_board_layout, compute_dashboard_layout
from semantic.models import DetailLevel

DEFAULT_PALETTE = {
    "PAPER": "#FFFFFF",
    "PAPER_CARD": "#FFFFFF",
    "PAPER_CONTAINER": "#F8FAFC",
    "INK": "#0F172A",
    "MUTED": "#64748B",
    "RULE": "#CBD5E1",
    "ACCENT": "#2563EB",
    "ACCENT_BG": "#EFF6FF",
    "PAIN": "#EF4444",
    "PAIN_BG": "#FEF2F2",
    "STICKY": "#FEF08A"
}


def engine_cerebro(scene: ExcalidrawScene, title: str, center_text: str,
                   branches: List[Dict[str, Any]], palette: Dict[str, str] = DEFAULT_PALETTE,
                   w: float = 1100, h: float = 650) -> str:
    """Motor CEREBRO: Hub central + ramas radiales calculadas con layout."""
    fx, fy = place(w, h)
    fid = scene.add_frame(f"CEREBRO: {title}", fx, fy, w, h)
    
    scene.add_text(fx + 30, fy + 30, title.upper(), font_size=20, font_family=2, color=palette["INK"], frame_id=fid)
    
    cx, cy = fx + 80, fy + 160
    cw, ch = 240, 240
    center_elem = scene.add_ellipse(cx, cy, cw, ch, bg=palette["ACCENT_BG"], stroke=palette["ACCENT"], stroke_w=2.5, frame_id=fid)
    
    tid = rid()
    center_elem["boundElements"].append({"id": tid, "type": "text"})
    ctext = scene._base_element("text", cx, cy, cw, ch, palette["INK"], "transparent", frame_id=fid)
    ctext["id"] = tid
    ctext.update({
        "fontSize": 18, "fontFamily": 2, "text": center_text,
        "textAlign": "center", "verticalAlign": "middle", "containerId": center_elem["id"],
        "originalText": center_text, "lineHeight": 1.25, "baseline": 18
    })
    scene.elements.append(ctext)

    branch_coords = compute_radial_layout(cx, cy, cw, len(branches), start_x=fx + 400)

    for i, branch in enumerate(branches):
        coord = branch_coords[i]
        bx, by = coord["x"], coord["y"]
        card_w, card_h = coord["w"], coord["h"]

        is_pain = branch.get("is_pain", False)
        is_accent = branch.get("is_accent", False)
        bg = palette["PAIN_BG"] if is_pain else (palette["ACCENT_BG"] if is_accent else palette["PAPER_CARD"])
        stroke = palette["PAIN"] if is_pain else (palette["ACCENT"] if is_accent else palette["INK"])

        scene.add_bound_card(bx, by, card_w, card_h, branch["text"], bg=bg, stroke=stroke,
                             text_color=palette["INK"], font_size=13, frame_id=fid)

        dashed = branch.get("dashed", False)
        scene.add_arrow(cx + cw, cy + ch * 0.5, bx, by + card_h * 0.5,
                        stroke=palette["MUTED"], stroke_w=1.5, dashed=dashed, frame_id=fid)

    return fid


def engine_flujo(scene: ExcalidrawScene, title: str,
                 steps: List[Dict[str, Any]], palette: Dict[str, str] = DEFAULT_PALETTE,
                 wave: bool = False, w: float = 1400, h: float = 450) -> str:
    """Motor FLUJO: Pasos calculados mediante compute_flow_layout."""
    fx, fy = place(w, h)
    fid = scene.add_frame(f"FLUJO: {title}", fx, fy, w, h)
    
    scene.add_text(fx + 30, fy + 30, title.upper(), font_size=20, font_family=2, color=palette["INK"], frame_id=fid)

    step_coords = compute_flow_layout(len(steps), start_x=fx + 50, base_y=fy + 180, wave=wave)

    for i, step in enumerate(steps):
        coord = step_coords[i]
        sx, sy = coord["x"], coord["y"]
        step_w, step_h = coord["w"], coord["h"]

        is_hero = step.get("is_hero", False)
        is_pain = step.get("is_pain", False)
        bg = palette["ACCENT_BG"] if is_hero else (palette["PAIN_BG"] if is_pain else palette["PAPER_CARD"])
        stroke = palette["ACCENT"] if is_hero else (palette["PAIN"] if is_pain else palette["INK"])

        scene.add_bound_card(sx, sy, step_w, step_h, step["label"], bg=bg, stroke=stroke,
                             text_color=palette["INK"], font_size=13, frame_id=fid)
        
        step_num = step.get("step_num", f"0{i+1}")
        scene.add_text(sx, sy - 24, step_num, font_size=12, font_family=3, color=palette["MUTED"], frame_id=fid)

    for i in range(len(step_coords) - 1):
        x1 = step_coords[i]["x"] + step_coords[i]["w"]
        y1 = step_coords[i]["y"] + step_coords[i]["h"] * 0.5
        x2 = step_coords[i+1]["x"]
        y2 = step_coords[i+1]["y"] + step_coords[i+1]["h"] * 0.5
        label = steps[i].get("edge_label", None)
        scene.add_arrow(x1, y1, x2, y2, stroke=palette["INK"], stroke_w=1.5, label=label, orthogonal=True, frame_id=fid)

    return fid


def engine_red(scene: ExcalidrawScene, title: str,
               nodes: List[Dict[str, Any]], edges: List[Dict[str, Any]],
               scopes: Optional[List[Dict[str, Any]]] = None,
               palette: Dict[str, str] = DEFAULT_PALETTE,
               w: float = 1200, h: float = 700) -> str:
    """Motor RED: Arquitectura distribuida con soporte de Scopes y Doble Jerarquía."""
    fx, fy = place(w, h)
    fid = scene.add_frame(f"ARQUITECTURA: {title}", fx, fy, w, h)
    
    scene.add_text(fx + 30, fy + 30, title.upper(), font_size=20, font_family=2, color=palette["INK"], frame_id=fid)

    # 1. Render de Scopes (Zonas de infraestructura)
    if scopes:
        for scope in scopes:
            sx = fx + scope.get("rel_x", 30)
            sy = fy + scope.get("rel_y", 80)
            sw = scope.get("w", 400)
            sh = scope.get("h", 550)
            s_label = scope.get("label", "SCOPE")
            scene.add_scope_container(sx, sy, sw, sh, label=s_label, stroke=palette["RULE"],
                                      bg=palette["PAPER_CONTAINER"], frame_id=fid)

    # 2. Render de Nodos con Doble Jerarquía
    node_map = {}
    for node in nodes:
        nx = fx + node.get("rel_x", 50)
        ny = fy + node.get("rel_y", 100)
        nw = node.get("w", 220)
        nh = node.get("h", 85)
        
        is_hero = node.get("is_hero", False)
        is_pain = node.get("is_pain", False)
        bg = palette["ACCENT_BG"] if is_hero else (palette["PAIN_BG"] if is_pain else palette["PAPER_CARD"])
        stroke = palette["ACCENT"] if is_hero else (palette["PAIN"] if is_pain else palette["INK"])

        scene.add_dual_card(nx, ny, nw, nh,
                            title=node["label"],
                            sublabel=node.get("sublabel"),
                            metadata=node.get("metadata"),
                            bg=bg, stroke=stroke,
                            text_color=palette["INK"], frame_id=fid)
        node_map[node["id"]] = (nx, ny, nw, nh)

    # 3. Conexiones ortogonales
    for edge in edges:
        from_node = node_map.get(edge["from"])
        to_node = node_map.get(edge["to"])
        if from_node and to_node:
            fx1, fy1, fw1, fh1 = from_node
            tx2, ty2, tw2, th2 = to_node
            
            start_x = fx1 + fw1 if tx2 > fx1 else fx1
            start_y = fy1 + fh1 * 0.5
            end_x = tx2 if tx2 > fx1 else tx2 + tw2
            end_y = ty2 + th2 * 0.5

            scene.add_arrow(start_x, start_y, end_x, end_y, stroke=palette["MUTED"],
                            stroke_w=1.5, label=edge.get("label"), orthogonal=True, frame_id=fid)

    return fid


def engine_matriz(scene: ExcalidrawScene, title: str,
                  headers: List[str], rows: List[Dict[str, Any]],
                  palette: Dict[str, str] = DEFAULT_PALETTE,
                  w: float = 1200, h: float = 600) -> str:
    """Motor MATRIZ: Grilla tabular con compute_matrix_layout."""
    fx, fy = place(w, h)
    fid = scene.add_frame(f"MATRIZ: {title}", fx, fy, w, h)
    
    scene.add_text(fx + 30, fy + 30, title.upper(), font_size=20, font_family=2, color=palette["INK"], frame_id=fid)

    grid = compute_matrix_layout(start_x=fx + 40, start_y=fy + 90,
                                 col_count=len(headers), row_count=len(rows))

    for cell in grid["headers"]:
        c = cell["col"]
        scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], headers[c],
                             bg=palette["INK"], stroke=palette["INK"], text_color=palette["PAPER"],
                             font_size=13, roundness_type=None, frame_id=fid)

    for r, row_cells in enumerate(grid["rows"]):
        row_data = rows[r]
        values = row_data.get("values", [])
        for c, cell in enumerate(row_cells):
            val = values[c] if c < len(values) else ""
            is_hero_col = (c == row_data.get("hero_col_idx", -1))
            bg = palette["ACCENT_BG"] if is_hero_col else palette["PAPER_CARD"]
            scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], str(val),
                                 bg=bg, stroke=palette["RULE"], text_color=palette["INK"],
                                 font_size=13, roundness_type=None, frame_id=fid)

    return fid


def engine_arbol(scene: ExcalidrawScene, title: str,
                 root_text: str, branches: List[Dict[str, Any]],
                 palette: Dict[str, str] = DEFAULT_PALETTE,
                 w: float = 1300, h: float = 700) -> str:
    """Motor ÁRBOL: Distribución jerárquica con compute_tree_layout."""
    fx, fy = place(w, h)
    fid = scene.add_frame(f"ÁRBOL: {title}", fx, fy, w, h)
    
    scene.add_text(fx + 30, fy + 30, title.upper(), font_size=20, font_family=2, color=palette["INK"], frame_id=fid)

    root_w, root_h = 260, 75
    rx = fx + (w - root_w) * 0.5
    ry = fy + 90

    tree_data = compute_tree_layout(rx, ry, root_w, root_h, branches, frame_w=w)

    scene.add_bound_card(rx, ry, root_w, root_h, root_text, bg=palette["ACCENT_BG"],
                         stroke=palette["ACCENT"], text_color=palette["INK"], font_size=15, frame_id=fid)

    for branch in tree_data["branches"]:
        bx, by = branch["x"], branch["y"]
        bw, bh = branch["w"], branch["h"]
        scene.add_bound_card(bx, by, bw, bh, branch["title"], bg=palette["PAPER_CARD"],
                             stroke=palette["INK"], text_color=palette["INK"], font_size=13, frame_id=fid)
        
        scene.add_line(rx + root_w * 0.5, ry + root_h, bx + bw * 0.5, by, stroke=palette["RULE"], frame_id=fid)

        for sub in branch["subitems"]:
            sx, sy = sub["x"], sub["y"]
            sw, sh = sub["w"], sub["h"]
            scene.add_bound_card(sx, sy, sw, sh, sub["text"], bg=palette["PAPER_CONTAINER"],
                                 stroke=palette["RULE"], text_color=palette["MUTED"], font_size=11, frame_id=fid)
            scene.add_line(bx + bw * 0.5, by + bh, sx + sw * 0.5, sy, stroke=palette["RULE"], dashed=True, frame_id=fid)

    return fid


def engine_timeline(scene: ExcalidrawScene, title: str,
                    milestones: List[Dict[str, Any]],
                    palette: Dict[str, str] = DEFAULT_PALETTE,
                    w: float = 1400, h: float = 500) -> str:
    """Motor TIMELINE: Eje cronológico calculado con compute_timeline_layout."""
    fx, fy = place(w, h)
    fid = scene.add_frame(f"TIMELINE: {title}", fx, fy, w, h)
    
    scene.add_text(fx + 30, fy + 30, title.upper(), font_size=20, font_family=2, color=palette["INK"], frame_id=fid)

    axis_y = fy + 260
    scene.add_line(fx + 60, axis_y, fx + w - 60, axis_y, stroke=palette["INK"], stroke_w=2, frame_id=fid)

    layout_items = compute_timeline_layout(len(milestones), start_x=fx + 100, axis_y=axis_y,
                                          total_width=w - 200)

    for i, item in enumerate(layout_items):
        m = milestones[i]
        px = item["marker_x"]
        card_x, card_y = item["card_x"], item["card_y"]
        step_w, step_h = item["w"], item["h"]
        is_above = item["is_above"]

        scene.add_ellipse(px - 10, axis_y - 10, 20, 20, bg=palette["ACCENT"], stroke=palette["INK"], frame_id=fid)

        scene.add_bound_card(card_x, card_y, step_w, step_h,
                             f"{m.get('date','')}\n{m.get('title','')}",
                             bg=palette["PAPER_CARD"], stroke=palette["INK"],
                             text_color=palette["INK"], font_size=12, frame_id=fid)

        v_start = card_y + step_h if is_above else axis_y
        v_end = axis_y if is_above else card_y
        scene.add_line(px, v_start, px, v_end, stroke=palette["MUTED"], dashed=True, frame_id=fid)

    return fid


def engine_board(scene: ExcalidrawScene, title: str,
                 lanes: List[Dict[str, Any]],
                 palette: Dict[str, str] = DEFAULT_PALETTE,
                 w: float = 1300, h: float = 750) -> str:
    """Motor BOARD: Carriles calculados con compute_board_layout."""
    fx, fy = place(w, h)
    fid = scene.add_frame(f"BOARD: {title}", fx, fy, w, h)
    
    scene.add_text(fx + 30, fy + 30, title.upper(), font_size=20, font_family=2, color=palette["INK"], frame_id=fid)

    board_lanes = compute_board_layout(start_x=fx + 50, start_y=fy + 90, lanes=lanes)

    for li, lane in enumerate(board_lanes):
        hdr = lane["header"]
        rot = -2.0 if li % 2 == 0 else 2.0
        scene.add_sticky_label(hdr["x"], hdr["y"], hdr["title"], bg=palette["STICKY"],
                               stroke=palette["INK"], font_size=15, angle_deg=rot, frame_id=fid)

        for itm in lane["items"]:
            scene.add_bound_card(itm["x"], itm["y"], itm["w"], itm["h"], itm["text"],
                                 bg=palette["PAPER_CARD"], stroke=palette["INK"],
                                 text_color=palette["INK"], font_size=13, frame_id=fid)

        if li < len(board_lanes) - 1:
            sep_x = hdr["x"] + hdr["w"] + 20
            scene.add_line(sep_x, fy + 90, sep_x, fy + h - 40, stroke=palette["RULE"], dashed=True, frame_id=fid)

    return fid


def engine_dashboard(scene: ExcalidrawScene, title: str,
                     metrics: List[Dict[str, Any]],
                     palette: Dict[str, str] = DEFAULT_PALETTE,
                     w: float = 1100, h: float = 480) -> str:
    """Motor DASHBOARD: Grilla de chips numéricos con compute_dashboard_layout."""
    fx, fy = place(w, h)
    fid = scene.add_frame(f"DASHBOARD: {title}", fx, fy, w, h)
    
    scene.add_text(fx + 30, fy + 30, title.upper(), font_size=20, font_family=2, color=palette["INK"], frame_id=fid)

    chips = compute_dashboard_layout(start_x=fx + 40, start_y=fy + 100, metrics_count=len(metrics))

    for i, chip in enumerate(chips):
        m = metrics[i]
        bg = palette["ACCENT"] if m.get("is_accent", False) else palette["INK"]
        scene.add_chip(chip["x"], chip["y"], chip["w"], chip["h"], m["number"], m["label"],
                       bg=bg, text_color=palette["PAPER"], frame_id=fid)

    return fid


def engine_storyboard(scene: ExcalidrawScene, title: str,
                      slides: List[Dict[str, Any]],
                      palette: Dict[str, str] = DEFAULT_PALETTE) -> List[str]:
    """Motor STORYBOARD: Diapositivas 1600x900 para presentaciones."""
    frame_ids = []
    w, h = 1600, 900
    
    for i, slide in enumerate(slides):
        fx, fy = place(w, h)
        fid = scene.add_frame(f"SLIDE 0{i+1}: {slide.get('title', title)}", fx, fy, w, h)
        frame_ids.append(fid)

        scene.add_text(fx + 60, fy + 60, slide.get("title", f"Paso 0{i+1}").upper(),
                       font_size=28, font_family=2, color=palette["INK"], frame_id=fid)
        
        if "subtitle" in slide:
            scene.add_text(fx + 60, fy + 110, slide["subtitle"],
                           font_size=16, font_family=2, color=palette["MUTED"], frame_id=fid)

        main_text = slide.get("content", "")
        if main_text:
            scene.add_bound_card(fx + 60, fy + 180, w - 120, h - 280, main_text,
                                 bg=palette["PAPER_CONTAINER"], stroke=palette["RULE"],
                                 text_color=palette["INK"], font_size=18, align="left", frame_id=fid)

    return frame_ids
