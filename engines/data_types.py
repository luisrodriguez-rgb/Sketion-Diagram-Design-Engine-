"""
Sketion 4.0 — Motores de Diagramas de Datos y Lakehouse (engines/data_types.py)
Incorpora la gramática editorial de Diagram Design:
- Tarjetas de 4 esquinas (add_quad_card) con badges de rol, iconos vectoriales y pills
- Cinta de chevrons concatenados superior (add_chevron_ribbon)
- Rieles verticales y leyendas estructuradas (add_legend_footer)
- Dimensiones compactas anti-stretch (w <= 340px)
"""

from typing import Dict, Any, List, Optional, Tuple
from render.excalidraw_builder import ExcalidrawScene
from layout.grid import compute_matrix_layout

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
# 1. MEDALLION LAKEHOUSE STORAGE
# =============================================================================
def render_medallion(scene: ExcalidrawScene, title: str, stages: List[Dict[str, Any]],
                     x: float, y: float, w: float = 2400.0, h: float = 820.0,
                     frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"MEDALLION: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 72, "arquitectura lakehouse multi-tier: ingesta raw, sanitizacion, limpieza y agregacion analitica", font_size=14, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Chevron Ribbon Superior
    stage_names = [s.get("name", f"Tier {i+1}") for i, s in enumerate(stages)]
    scene.add_chevron_ribbon(x + 50.0, y + 115.0, w - 100.0, h=36.0, stages=stage_names, bg=PALETTE["INK"], text_color="#FFFFFF", frame_id=fid)

    col_count = len(stages)
    gap = 35.0
    col_w = (w - 100.0 - (col_count - 1) * gap) / col_count

    badge_map = ["RAW", "BRZ", "SLV", "GLD", "ARC"]
    icon_map = ["database", "server", "postgres", "monitoring", "bucket"]

    for i, stage in enumerate(stages):
        col_x = x + 50.0 + i * (col_w + gap)
        col_y = y + 175.0
        s_name = stage.get("name", f"Tier {i+1}")
        s_desc = stage.get("desc", "")
        items = stage.get("items", [])
        is_gold = stage.get("is_gold", False)

        bg = PALETTE["PASTEL_GREEN"] if is_gold else "#FFFFFF"
        stroke = PALETTE["INK"] if is_gold else PALETTE["CARD_BORDER"]
        scene.add_scope_container(col_x, col_y, col_w, 550.0, label=s_name.upper(), stroke=stroke, bg=bg, frame_id=fid)

        badge_txt = badge_map[i] if i < len(badge_map) else "DATA"
        icon_name = icon_map[i] if i < len(icon_map) else "database"

        for j, item_text in enumerate(items):
            item_y = col_y + 65.0 + j * 125.0
            card_w = col_w - 40.0
            card_h = 105.0
            is_hero_item = is_gold and (j == 0)
            
            scene.add_quad_card(col_x + 20.0, item_y, card_w, card_h,
                                item_text, sublabel=s_desc,
                                badge=badge_txt, icon=icon_name,
                                is_hero=is_hero_item, frame_id=fid)

        if i < col_count - 1:
            scene.add_arrow(col_x + col_w, col_y + 260.0, col_x + col_w + gap, col_y + 260.0,
                            stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)

    # Leyenda Inferior
    scene.add_legend_footer(x + 50.0, y + 755.0, w - 100.0,
                            swatches=[
                                {"label": "Gold Lakehouse (Focal)", "bg": "#FFF5F2", "stroke": "#E03A2F"},
                                {"label": "Standard Lakehouse Tier", "bg": "#FFFFFF", "stroke": "#0C0C0C"},
                                {"label": "Data Flow", "is_arrow": True, "stroke": "#0C0C0C"}
                            ],
                            note="data contracts enforce schema evolution · lakehouse is the source of truth",
                            frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 2. DATA FLOW (ROLE-SCOPED ANALYTICS PIPELINE)
# =============================================================================
def render_data_flow(scene: ExcalidrawScene, title: str,
                     roles: List[str], stages: List[str],
                     tasks: List[Dict[str, Any]], x: float, y: float,
                     w: float = 2400.0, h: float = 820.0,
                     frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"DATA FLOW: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 72, "pipeline analitico segregado por roles funcionales y etapas de transformacion", font_size=14, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Cabeceras de etapas (Chevron Ribbon)
    scene.add_chevron_ribbon(x + 280.0, y + 115.0, w - 330.0, h=36.0, stages=stages, bg=PALETTE["INK"], text_color="#FFFFFF", frame_id=fid)

    # Carriles de roles
    stage_w = (w - 330.0) / len(stages)
    role_h = 160.0
    for ri, r_name in enumerate(roles):
        ry = y + 175.0 + ri * (role_h + 15.0)
        # Etiqueta de rol lateral
        scene.add_bound_card(x + 50.0, ry, 210.0, role_h, r_name.upper(),
                             bg=PALETTE["PASTEL_BLUE"] if ri == 0 else "#FFFFFF",
                             stroke=PALETTE["INK"], text_color=PALETTE["INK"],
                             font_size=13, roundness_type=3, frame_id=fid)
        
        # Carril contenedor
        scene.add_rect(x + 275.0, ry, w - 325.0, role_h, bg="#FFFFFF",
                       stroke=PALETTE["CARD_BORDER"], stroke_w=1.0, roundness_type=3, frame_id=fid)

    # Posicionar tareas
    for task in tasks:
        r_idx = task.get("role_idx", 0)
        s_idx = task.get("stage_idx", 0)
        t_label = task.get("label", "")
        is_hero = task.get("is_hero", False)
        
        tx = x + 295.0 + s_idx * stage_w
        ty = y + 195.0 + r_idx * (role_h + 15.0)
        card_w = min(320.0, stage_w - 30.0)
        
        scene.add_quad_card(tx, ty, card_w, 120.0, t_label, sublabel=f"Stage {s_idx+1}",
                            badge="TASK", icon="pipeline" if is_hero else "server",
                            is_hero=is_hero, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 3. DP INTEGRATION (SOURCES -> CORE -> CONSUMERS)
# =============================================================================
def render_dp_integration(scene: ExcalidrawScene, title: str,
                          sources: List[str], core_services: List[str],
                          consumers: List[str], x: float, y: float,
                          w: float = 2400.0, h: float = 820.0,
                          frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"DP INTEGRATION: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 72, "topologia de integracion: ingesta de fuentes heterogeneas -> almacenamiento core -> consumidores", font_size=14, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Ribbon Superior
    scene.add_chevron_ribbon(x + 50.0, y + 115.0, w - 100.0, h=36.0,
                             stages=["1. SOURCES", "2. INGESTION", "3. STORAGE & CORE", "4. ANALYTICS", "5. CONSUMERS"],
                             bg=PALETTE["INK"], text_color="#FFFFFF", frame_id=fid)

    sections = [
        ("1. FUENTES DE DATOS", 600.0, sources, "EXT", "database", False),
        ("2. DATA PLATFORM CORE", 850.0, core_services, "CORE", "server", True),
        ("3. CONSUMIDORES & BI", 750.0, consumers, "BI", "monitoring", False)
    ]

    curr_x = x + 50.0
    sec_coords = []
    scope_y = y + 175.0
    scope_h = 550.0

    for s_title, s_w, s_items, s_badge, s_icon, s_is_hero in sections:
        bg = PALETTE["PASTEL_GREEN"] if s_is_hero else "#FFFFFF"
        stroke = PALETTE["INK"] if s_is_hero else PALETTE["CARD_BORDER"]
        scene.add_scope_container(curr_x, scope_y, s_w, scope_h, label=s_title, stroke=stroke, bg=bg, frame_id=fid)

        for j, item_text in enumerate(s_items):
            iy = scope_y + 65.0 + j * 135.0
            cw = s_w - 40.0
            ch = 110.0
            scene.add_quad_card(curr_x + 20.0, iy, cw, ch, item_text, sublabel="CDC · Batch · Real-time",
                                badge=s_badge, icon=s_icon, is_hero=s_is_hero and (j == 1), frame_id=fid)

        sec_coords.append((curr_x, scope_y, s_w, scope_h))
        curr_x += s_w + 40.0

    # Conectores inter-scope
    scene.add_arrow(sec_coords[0][0] + sec_coords[0][2], scope_y + 250.0,
                    sec_coords[1][0], scope_y + 250.0, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)
    scene.add_arrow(sec_coords[1][0] + sec_coords[1][2], scope_y + 250.0,
                    sec_coords[2][0], scope_y + 250.0, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 4. DP SECURITY MATRIX (PER-ROLE ACCESS PERMISSIONS)
# =============================================================================
def render_dp_security_matrix(scene: ExcalidrawScene, title: str,
                              roles: List[str], components: List[str],
                              matrix_data: List[List[str]], x: float, y: float,
                              w: float = 2400.0, h: float = 820.0,
                              frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"SECURITY MATRIX: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 72, "matriz de control de acceso y politicas de seguridad por rol (rbac)", font_size=14, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    headers = ["Componente / Recurso"] + [r.upper() for r in roles]
    rows = []
    for comp_idx, comp_name in enumerate(components):
        row_vals = [comp_name] + matrix_data[comp_idx]
        rows.append({"name": comp_name, "values": row_vals})

    grid = compute_matrix_layout(x + 50.0, y + 130.0, headers, rows, min_col_w=180.0)

    # Cabecera de Matriz
    for c, cell in enumerate(grid["headers"]):
        scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], headers[c],
                             bg=PALETTE["INK"], stroke=PALETTE["INK"], text_color="#FFFFFF",
                             font_size=12, roundness_type=None, frame_id=fid)

    # Celdas
    for r, row_cells in enumerate(grid["rows"]):
        vals = rows[r]["values"]
        for c, cell in enumerate(row_cells):
            val = str(vals[c])
            bg = "#FFFFFF"
            stroke = PALETTE["CARD_BORDER"]
            text_color = PALETTE["INK"]
            
            if c == len(row_cells) - 1 and val.upper() == "READ":
                bg = PALETTE["PAIN_BG"]
                stroke = PALETTE["PAIN_BORDER"]
                text_color = PALETTE["PAIN_RED"]
            elif val.upper() == "ADMIN":
                bg = "#F1F5F9"
                stroke = PALETTE["INK"]
            elif val.upper() == "NONE":
                text_color = PALETTE["MUTED"]
                
            scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], val,
                                 bg=bg, stroke=stroke, text_color=text_color,
                                 font_size=12, roundness_type=3 if c > 0 else None, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 5. ER / DATA MODEL (ENTITIES + FIELDS + PK/FK)
# =============================================================================
def render_er_model(scene: ExcalidrawScene, title: str,
                    entities: List[Dict[str, Any]], relations: List[Tuple[str, str, str]],
                    x: float, y: float, w: float = 2400.0, h: float = 820.0,
                    frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"ER MODEL: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 72, "modelo entidad-relacion relacional con campos tipados, claves primarias (pk) y foraneas (fk)", font_size=14, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    entity_coords = {}
    ent_count = len(entities)
    spacing = (w - 100.0) / max(1, ent_count)

    for ei, ent in enumerate(entities):
        eid = ent.get("id", f"ent_{ei}")
        ename = ent.get("name", f"Entity {ei+1}")
        fields = ent.get("fields", [])
        
        ex = x + 50.0 + ei * spacing
        ey = y + 150.0
        ew = min(320.0, spacing - 30.0)
        eh = 60.0 + len(fields) * 32.0
        
        # Header de Entidad con Badge DB
        scene.add_rect(ex, ey, ew, 40.0, bg=PALETTE["INK"], stroke=PALETTE["INK"], roundness_type=None, frame_id=fid)
        scene.add_text(ex + 15.0, ey + 10.0, ename.upper(), font_size=13, font_family=2, color="#FFFFFF", frame_id=fid)
        scene.add_icon("database", ex + ew - 30.0, ey + 8.0, size=22.0, color="#FFFFFF", frame_id=fid)
        
        # Caja de Campos
        scene.add_rect(ex, ey + 40.0, ew, eh - 40.0, bg="#FFFFFF", stroke=PALETTE["INK"], stroke_w=1.5, roundness_type=3, frame_id=fid)
        for fi, fld in enumerate(fields):
            fy = ey + 50.0 + fi * 28.0
            is_pk = "PK" in fld.upper()
            fcol = PALETTE["PAIN_RED"] if is_pk else PALETTE["INK"]
            scene.add_text(ex + 15.0, fy, fld, font_size=11, font_family=2, color=fcol, frame_id=fid)
            
        entity_coords[eid] = (ex, ey, ew, eh)

    for from_ent, to_ent, rel_label in relations:
        if from_ent in entity_coords and to_ent in entity_coords:
            fx, fy, fw, fh = entity_coords[from_ent]
            tx, ty, tw, th = entity_coords[to_ent]
            scene.add_arrow(fx + fw, fy + 40.0, tx, ty + 40.0,
                            stroke=PALETTE["INK"], stroke_w=1.5, label=rel_label, orthogonal=True, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid
