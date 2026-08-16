"""
Sketion 4.0 — Motores de Diagramas de Datos y Lakehouse (engines/data_types.py)
Implementa:
1. Medallion (Raw -> Bronze -> Silver -> Gold -> Archive)
2. Data Flow (Role-Scoped Analytics Pipeline)
3. DP Integration (Sources -> Core Storage -> BI / Consumer APIs)
4. DP Security Matrix (Per-Role Access Permissions)
5. ER / Data Model (Entities + Fields + Types + PK/FK)
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
                     x: float, y: float, w: float = 2800.0, h: float = 850.0,
                     frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"MEDALLION: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "arquitectura lakehouse multi-tier: ingesta raw, sanitizacion, limpieza y agregacion analitica", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    col_count = len(stages)
    gap = 40.0
    col_w = (w - 120.0 - (col_count - 1) * gap) / col_count

    for i, stage in enumerate(stages):
        cx = x + 60.0 + i * (col_w + gap)
        cy = y + 130.0
        s_title = stage.get("name", f"Tier {i+1}")
        s_desc = stage.get("desc", "")
        s_items = stage.get("items", [])
        is_gold = stage.get("is_gold", False)
        
        bg = PALETTE["PASTEL_GREEN"] if is_gold else (PALETTE["PASTEL_BLUE"] if i == 0 else "#FFFFFF")
        scene.add_scope_container(cx, cy, col_w, 520.0, label=s_title, stroke=PALETTE["CARD_BORDER"], bg=bg, frame_id=fid)
        
        # Meta info
        scene.add_text(cx + 20, cy + 50, s_desc, font_size=12, font_family=3, color=PALETTE["MUTED"], frame_id=fid)
        
        # Items
        for ii, item in enumerate(s_items):
            iy = cy + 90.0 + ii * 100.0
            scene.add_bound_card(cx + 20, iy, col_w - 40.0, 80.0, item,
                                 bg="#FFFFFF", stroke=PALETTE["INK"], text_color=PALETTE["INK"],
                                 font_size=13, roundness_type=3, frame_id=fid)

    scene.add_banner(x + 60, y + 680, w - 120, 50,
                     "regla lakehouse: almacenamiento delta/parquet inmutable con transformaciones aciclicas.",
                     bg=PALETTE["BANNER_PINK"], text_color=PALETTE["INK"], font_size=14, frame_id=fid)
    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 2. DATA FLOW (ROLE-SCOPED PIPELINE)
# =============================================================================
def render_data_flow(scene: ExcalidrawScene, title: str, roles: List[str],
                     stages: List[str], tasks: List[Dict[str, Any]],
                     x: float, y: float, w: float = 2800.0, h: float = 850.0,
                     frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"DATA FLOW: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "pipeline analitico segregado por roles funcionales y etapas de transformacion", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Cabeceras de etapas (Columnas)
    stage_w = (w - 360.0) / len(stages)
    for si, s_name in enumerate(stages):
        sx = x + 300.0 + si * stage_w
        scene.add_bound_card(sx, y + 130.0, stage_w - 20.0, 45.0, s_name,
                             bg=PALETTE["INK"], stroke=PALETTE["INK"], text_color="#FFFFFF",
                             font_size=12, roundness_type=None, frame_id=fid)

    # Carriles de roles (Filas)
    role_h = 160.0
    for ri, r_name in enumerate(roles):
        ry = y + 195.0 + ri * (role_h + 15.0)
        # Etiqueta de rol
        scene.add_bound_card(x + 60.0, ry, 220.0, role_h, r_name,
                             bg=PALETTE["PASTEL_BLUE"] if ri == 0 else "#FFFFFF",
                             stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                             font_size=13, roundness_type=3, frame_id=fid)
        
        # Grid line de carril
        scene.add_rect(x + 290.0, ry, w - 350.0, role_h, bg="#FFFFFF",
                       stroke=PALETTE["CARD_BORDER"], stroke_w=1.0, roundness_type=3, frame_id=fid)

    # Posicionar tareas
    for task in tasks:
        r_idx = task.get("role_idx", 0)
        s_idx = task.get("stage_idx", 0)
        t_label = task.get("label", "")
        tx = x + 310.0 + s_idx * stage_w
        ty = y + 215.0 + r_idx * (role_h + 15.0)
        scene.add_bound_card(tx, ty, stage_w - 40.0, 110.0, t_label,
                             bg=PALETTE["PASTEL_GREEN"] if task.get("is_hero") else "#FFFFFF",
                             stroke=PALETTE["INK"], text_color=PALETTE["INK"], font_size=12, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 3. DP INTEGRATION (SOURCES -> CORE -> CONSUMERS)
# =============================================================================
def render_dp_integration(scene: ExcalidrawScene, title: str,
                          sources: List[str], core_services: List[str],
                          consumers: List[str], x: float, y: float,
                          w: float = 2800.0, h: float = 850.0,
                          frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"DP INTEGRATION: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "topologia de integracion: ingesta de fuentes heterogeneas -> almacenamiento core -> consumidores", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    sections = [
        ("1. FUENTES DE DATOS", 700.0, sources, PALETTE["PASTEL_BLUE"]),
        ("2. DATA PLATFORM CORE", 1000.0, core_services, PALETTE["PASTEL_GREEN"]),
        ("3. CONSUMIDORES & BI", 850.0, consumers, "#FFFFFF")
    ]

    curr_x = x + 60.0
    sec_rects = []
    for s_title, sw, s_items, s_bg in sections:
        sy = y + 130.0
        sh = 520.0
        scene.add_scope_container(curr_x, sy, sw, sh, label=s_title, stroke=PALETTE["CARD_BORDER"], bg=s_bg, frame_id=fid)
        sec_rects.append((curr_x, sy, sw, sh))

        for ii, item in enumerate(s_items):
            iy = sy + 70.0 + ii * 105.0
            scene.add_bound_card(curr_x + 30.0, iy, sw - 60.0, 85.0, item,
                                 bg="#FFFFFF", stroke=PALETTE["INK"], text_color=PALETTE["INK"],
                                 font_size=13, roundness_type=3, frame_id=fid)

        curr_x += sw + 65.0

    # Flechas entre scopes
    scene.add_arrow(sec_rects[0][0] + sec_rects[0][2], y + 350.0, sec_rects[1][0], y + 350.0,
                    stroke=PALETTE["INK"], stroke_w=2.0, label="Ingest Pipeline", orthogonal=True, frame_id=fid)
    scene.add_arrow(sec_rects[1][0] + sec_rects[1][2], y + 350.0, sec_rects[2][0], y + 350.0,
                    stroke=PALETTE["INK"], stroke_w=2.0, label="Query & API", orthogonal=True, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid


# =============================================================================
# 4. DP SECURITY MATRIX (PER-ROLE ACCESS PERMISSIONS)
# =============================================================================
def render_dp_security_matrix(scene: ExcalidrawScene, title: str,
                              roles: List[str], components: List[str],
                              matrix_data: List[List[str]], x: float, y: float,
                              w: float = 2800.0, h: float = 850.0,
                              frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"SECURITY MATRIX: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "matriz de control de acceso por rol (rbac): permisos sobre componentes del ecosistema de datos", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    headers = ["Componente / Recurso"] + roles
    rows = []
    for c_idx, comp_name in enumerate(components):
        row_vals = [comp_name] + matrix_data[c_idx]
        rows.append({"values": row_vals})

    grid = compute_matrix_layout(start_x=x + 60.0, start_y=y + 130.0, headers=headers, rows=rows)

    # Cabeceras
    for cell in grid["headers"]:
        c = cell["col"]
        scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], headers[c],
                             bg=PALETTE["INK"], stroke=PALETTE["INK"], text_color="#FFFFFF",
                             font_size=12, roundness_type=None, frame_id=fid)

    # Celdas con Pills de permiso
    for r, row_cells in enumerate(grid["rows"]):
        vals = rows[r]["values"]
        for c, cell in enumerate(row_cells):
            val = str(vals[c])
            bg = "#FFFFFF"
            stroke = PALETTE["CARD_BORDER"]
            text_color = PALETTE["INK"]
            
            # Solo un foco sutil en la celda crítica de partner
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
                    x: float, y: float, w: float = 2800.0, h: float = 850.0,
                    frame_id: Optional[str] = None) -> str:
    fid = frame_id or scene.add_frame(f"DATA MODEL: {title}", x, y, w, h)
    scene.add_text(x + 50, y + 35, title.upper(), font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(x + 50, y + 75, "diagrama entidad-relacion: esquema relacional tipado con claves primarias (pk) y foraneas (fk)", font_size=16, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    ent_coords = {}
    card_w = 480.0
    for idx, ent in enumerate(entities):
        e_id = ent.get("id", f"ent_{idx}")
        e_name = ent.get("name", "Entity")
        e_fields = ent.get("fields", [])
        
        row_i = idx // 4
        col_i = idx % 4
        ex = x + 60.0 + col_i * (card_w + 120.0)
        ey = y + 140.0 + row_i * 380.0
        
        # Header de Entidad
        scene.add_bound_card(ex, ey, card_w, 45.0, e_name.upper(),
                             bg=PALETTE["INK"], stroke=PALETTE["INK"], text_color="#FFFFFF",
                             font_size=13, roundness_type=None, frame_id=fid)
        
        # Cuerpo de Campos
        body_h = max(180.0, len(e_fields) * 35.0 + 20.0)
        scene.add_rect(ex, ey + 45.0, card_w, body_h, bg="#FFFFFF", stroke=PALETTE["CARD_BORDER"], stroke_w=1.0, frame_id=fid)
        
        for fi, f_str in enumerate(e_fields):
            fy = ey + 55.0 + fi * 35.0
            is_pk = "PK" in f_str
            is_fk = "FK" in f_str
            f_color = PALETTE["PAIN_RED"] if is_pk else (PALETTE["INK"] if is_fk else PALETTE["MUTED"])
            scene.add_text(ex + 20.0, fy, f_str, font_size=12, font_family=3, color=f_color, frame_id=fid)
            
        ent_coords[e_id] = (ex, ey, card_w, body_h + 45.0)

    # Relaciones entre entidades
    for from_id, to_id, rel_cardinality in relations:
        if from_id in ent_coords and to_id in ent_coords:
            fx, fy, fw, fh = ent_coords[from_id]
            tx, ty, tw, th = ent_coords[to_id]
            if tx >= fx + fw:
                scene.add_arrow(fx + fw, fy + 50.0, tx, ty + 50.0,
                                stroke=PALETTE["INK"], stroke_w=1.5, label=rel_cardinality, orthogonal=True, frame_id=fid)
            elif tx < fx:
                scene.add_arrow(fx, fy + 50.0, tx + tw, ty + 50.0,
                                stroke=PALETTE["INK"], stroke_w=1.5, label=rel_cardinality, orthogonal=True, frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    return fid
