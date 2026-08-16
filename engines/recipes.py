"""
Sketion Engine Recipes (Desacoplado 2.0)
Conecta los Modelos Semánticos y Motores de Layout con el Render de Excalidraw.
"""

from typing import List, Dict, Any, Optional
from render.excalidraw_builder import ExcalidrawScene, place, rid, compute_card_dimensions
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
                 wave: bool = False, w: float = 1400, h: float = 400) -> str:
    """Motor FLUJO: Pasos calculados secuencialmente con 90px de separación limpia."""
    fx, fy = place(w, h)
    fid = scene.add_frame(f"FLUJO: {title}", fx, fy, w, h)
    
    scene.add_text(fx + 35, fy + 30, title.upper(), font_size=20, font_family=2, color=palette["INK"], frame_id=fid)

    curr_x = fx + 45.0
    step_coords = []

    for i, step in enumerate(steps):
        step_w, step_h = compute_card_dimensions(step["label"], font_size=13, min_w=190.0)
        sy = fy + 140.0
        if wave:
            sy += 30.0 if (i % 2 == 1) else -30.0

        is_hero = step.get("is_hero", False)
        is_pain = step.get("is_pain", False)
        bg = palette["ACCENT_BG"] if is_hero else (palette["PAIN_BG"] if is_pain else palette["PAPER_CARD"])
        stroke = palette["ACCENT"] if is_hero else (palette["PAIN"] if is_pain else palette["INK"])

        scene.add_bound_card(curr_x, sy, step_w, step_h, step["label"], bg=bg, stroke=stroke,
                             text_color=palette["INK"], font_size=13, frame_id=fid)
        
        step_num = step.get("step_num", f"0{i+1}")
        scene.add_text(curr_x, sy - 24, step_num, font_size=12, font_family=3, color=palette["MUTED"], frame_id=fid)

        step_coords.append({"x": curr_x, "y": sy, "w": step_w, "h": step_h})
        curr_x += step_w + 95.0  # Espacio exacto para flecha y pastilla protectora

    for i in range(len(step_coords) - 1):
        x1 = step_coords[i]["x"] + step_coords[i]["w"]
        y1 = step_coords[i]["y"] + step_coords[i]["h"] * 0.5
        x2 = step_coords[i+1]["x"]
        y2 = step_coords[i+1]["y"] + step_coords[i+1]["h"] * 0.5
        label = steps[i].get("edge_label", None)
        scene.add_arrow(x1, y1, x2, y2, stroke=palette["INK"], stroke_w=1.5, label=label, orthogonal=False, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


def engine_red(scene: ExcalidrawScene, title: str,
               nodes: List[Dict[str, Any]], edges: List[Dict[str, Any]],
               scopes: Optional[List[Dict[str, Any]]] = None,
               palette: Dict[str, str] = DEFAULT_PALETTE,
               w: float = 1200, h: float = 700) -> str:
    """Motor RED: Arquitectura distribuida con anchos uniformes, Scopes con Gutter seguro y Track Lanes."""
    fx, fy = place(w, h)
    fid = scene.add_frame(f"ARQUITECTURA: {title}", fx, fy, w, h)
    
    scene.add_text(fx + 35, fy + 30, title.upper(), font_size=20, font_family=2, color=palette["INK"], frame_id=fid)

    # 1. Agrupar nodos por scope_id
    scope_order = [s["id"] for s in (scopes or [])]
    scope_nodes_map: Dict[str, List[Dict[str, Any]]] = {sid: [] for sid in scope_order}
    orphan_nodes: List[Dict[str, Any]] = []

    for node in nodes:
        sid = node.get("scope_id")
        if sid in scope_nodes_map:
            scope_nodes_map[sid].append(node)
        else:
            orphan_nodes.append(node)

    # Calcular ancho uniforme por columna
    for sid, s_nodes in scope_nodes_map.items():
        if s_nodes:
            max_col_w = max(
                compute_card_dimensions(n["label"], n.get("sublabel"), n.get("metadata"), font_size=13, min_w=240.0)[0]
                for n in s_nodes
            )
            uniform_w = max(250.0, max_col_w)
            for n in s_nodes:
                n["computed_w"] = uniform_w

    # 2. Calcular layout consecutivo de scopes con Gutter de 65px para cero solapamiento
    curr_scope_x = fx + 35.0
    coords_map = {}
    scope_bounds = []

    for scope in (scopes or []):
        sid = scope["id"]
        s_nodes = scope_nodes_map.get(sid, [])
        if s_nodes:
            card_w = s_nodes[0].get("computed_w", 250.0)
            scope_w = card_w + 60.0
            
            for n in s_nodes:
                nx = curr_scope_x + 30.0
                ny = fy + n.get("rel_y", 120.0)
                calc_w, calc_h = compute_card_dimensions(n["label"], n.get("sublabel"), n.get("metadata"), font_size=13, min_w=card_w)
                coords_map[n["id"]] = (nx, ny, card_w, max(85.0, calc_h))

            min_y = min(coords_map[n["id"]][1] for n in s_nodes) - 52.0
            max_y = max(coords_map[n["id"]][1] + coords_map[n["id"]][3] for n in s_nodes) + 28.0
            scope_h = max_y - min_y
            
            scope_bounds.append({
                "id": sid,
                "label": scope.get("label", "SCOPE"),
                "x": curr_scope_x,
                "y": min_y,
                "w": scope_w,
                "h": scope_h
            })
            curr_scope_x += scope_w + 65.0
        else:
            # Scope sin nodos hijos directos
            sx = curr_scope_x
            sy = fy + scope.get("rel_y", 80.0)
            sw = scope.get("w", 320.0)
            sh = scope.get("h", 450.0)
            scope_bounds.append({"id": sid, "label": scope.get("label", "SCOPE"), "x": sx, "y": sy, "w": sw, "h": sh})
            curr_scope_x += sw + 65.0

    # Nodos huérfanos sin scope
    for node in orphan_nodes:
        nx = fx + node.get("rel_x", 50.0)
        ny = fy + node.get("rel_y", 100.0)
        card_w = node.get("w", 240.0)
        calc_w, calc_h = compute_card_dimensions(node["label"], node.get("sublabel"), node.get("metadata"), font_size=13, min_w=card_w)
        coords_map[node["id"]] = (nx, ny, max(card_w, calc_w), max(85.0, calc_h))

    # 3. Render de Scopes PRIMERO (Z-Index 0: Fondo)
    for sb in scope_bounds:
        scene.add_scope_container(sb["x"], sb["y"], sb["w"], sb["h"], label=sb["label"],
                                  stroke=palette["RULE"], bg=palette["PAPER_CONTAINER"], frame_id=fid)

    # 4. Render de Nodos (Z-Index 1: Encima de los Scopes)
    node_map = {}
    for node in nodes:
        nx, ny, card_w, card_h = coords_map[node["id"]]
        is_hero = node.get("is_hero", False)
        is_pain = node.get("is_pain", False)
        bg = palette["ACCENT_BG"] if is_hero else (palette["PAIN_BG"] if is_pain else palette["PAPER_CARD"])
        stroke = palette["ACCENT"] if is_hero else (palette["PAIN"] if is_pain else palette["INK"])

        container, _ = scene.add_dual_card(nx, ny, card_w, card_h,
                                           title=node["label"],
                                           sublabel=node.get("sublabel"),
                                           metadata=node.get("metadata"),
                                           bg=bg, stroke=stroke,
                                           text_color=palette["INK"], frame_id=fid)
        node_map[node["id"]] = (container["x"], container["y"], container["width"], container["height"])

    # 5. Conexiones ortogonales con Carriles de Retorno (Track Lanes)
    min_scope_y = min((sb["y"] for sb in scope_bounds), default=fy + 80.0)

    for edge in edges:
        from_node = node_map.get(edge["from"])
        to_node = node_map.get(edge["to"])
        if from_node and to_node:
            fx1, fy1, fw1, fh1 = from_node
            tx2, ty2, tw2, th2 = to_node
            
            # Flujo de Retorno (Retroceso horizontal): usar carril superior por encima de los scopes
            if tx2 < fx1:
                start_x = fx1
                start_y = fy1 + 18.0
                end_x = tx2 + tw2
                end_y = ty2 + 18.0
                return_track_y = min_scope_y - 20.0
                scene.add_arrow(start_x, start_y, end_x, end_y, stroke=palette["MUTED"],
                                stroke_w=1.5, label=edge.get("label"), orthogonal=True,
                                track_y=return_track_y, frame_id=fid)
            elif tx2 >= fx1 + fw1:
                start_x = fx1 + fw1
                start_y = fy1 + fh1 * 0.5
                end_x = tx2
                end_y = ty2 + th2 * 0.5
                scene.add_arrow(start_x, start_y, end_x, end_y, stroke=palette["MUTED"],
                                stroke_w=1.5, label=edge.get("label"), orthogonal=True, frame_id=fid)
            else:
                # Vertical en la misma columna
                start_x = fx1 + fw1 * 0.5
                start_y = fy1 + fh1 if ty2 > fy1 else fy1
                end_x = tx2 + tw2 * 0.5
                end_y = ty2 if ty2 > fy1 else ty2 + th2
                scene.add_arrow(start_x, start_y, end_x, end_y, stroke=palette["MUTED"],
                                stroke_w=1.5, label=edge.get("label"), orthogonal=True, frame_id=fid)

    scene.auto_fit_frame(fid, padding=60.0)
    return fid


def engine_matriz(scene: ExcalidrawScene, title: str,
                  headers: List[str], rows: List[Dict[str, Any]],
                  palette: Dict[str, str] = DEFAULT_PALETTE,
                  w: float = 1400, h: float = 700) -> str:
    """Motor MATRIZ: Grilla tabular con anchos y alturas proporcionales al texto."""
    fx, fy = place(w, h)
    fid = scene.add_frame(f"MATRIZ: {title}", fx, fy, w, h)
    
    scene.add_text(fx + 30, fy + 30, title.upper(), font_size=20, font_family=2, color=palette["INK"], frame_id=fid)

    grid = compute_matrix_layout(start_x=fx + 40, start_y=fy + 90,
                                 headers=headers, rows=rows)

    for cell in grid["headers"]:
        c = cell["col"]
        scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], headers[c],
                             bg=palette["INK"], stroke=palette["INK"], text_color=palette["PAPER"],
                             font_size=13, roundness_type=None, frame_id=fid)

    for r, row_cells in enumerate(grid["rows"]):
        row_data = rows[r]
        if "values" in row_data:
            values = row_data["values"]
        else:
            values = [row_data.get(h, "") for h in headers]

        for c, cell in enumerate(row_cells):
            val = values[c] if c < len(values) else ""
            is_hero_col = (c == row_data.get("hero_col_idx", -1))
            bg = palette["ACCENT_BG"] if is_hero_col else palette["PAPER_CARD"]
            scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], str(val),
                                 bg=bg, stroke=palette["RULE"], text_color=palette["INK"],
                                 font_size=12, roundness_type=None, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
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
        step_w, step_h = item.get("w", item.get("card_w", 160)), item.get("h", item.get("card_h", 65))
        is_above = item["is_above"]

        scene.add_ellipse(px - 6, axis_y - 6, 12, 12, bg=palette["ACCENT"], stroke=palette["ACCENT"], frame_id=fid)

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
    """Motor DASHBOARD: Grilla de chips numéricos con compute_dashboard_layout y auto-fit."""
    fx, fy = place(w, h)
    fid = scene.add_frame(f"DASHBOARD: {title}", fx, fy, w, h)
    
    scene.add_text(fx + 30, fy + 30, title.upper(), font_size=20, font_family=2, color=palette["INK"], frame_id=fid)

    chips = compute_dashboard_layout(start_x=fx + 40, start_y=fy + 100, metrics_count=len(metrics))

    for i, chip in enumerate(chips):
        m = metrics[i]
        bg = palette["ACCENT_BG"] if m.get("is_accent", False) else palette["PAPER_CARD"]
        stroke = palette["ACCENT"] if m.get("is_accent", False) else palette["RULE"]
        scene.add_chip(chip["x"], chip["y"], chip["w"], chip["h"], m["number"], m["label"],
                       bg=bg, text_color=palette["INK"], frame_id=fid)

    scene.auto_fit_frame(fid, padding=60.0)
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
