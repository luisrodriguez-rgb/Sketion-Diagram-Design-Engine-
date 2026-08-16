"""
Sketion 4.0 — Reproducción Editorial del Benchmark Diagram Design (Open Data Lake)
Genera la arquitectura Open Data Lake con la exactitud de micro-detalles de Diagram Design:
- Tarjetas Quad-Corner con badges de rol y logos vectoriales
- Scopes estilizados
- Acento hero coral único en MinIO
- Flechas ortogonales con pills de protocolo (SQL, WRITE)
- Leyenda inferior estructurada con notas editoriales
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from validation.validator import validate_scene

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V6")
os.makedirs(OUT_DIR, exist_ok=True)

PALETTE = {
    "CANVAS": "#F8FAFC",
    "CARD": "#FFFFFF",
    "CARD_BORDER": "#E2E8F0",
    "INK": "#0F172A",
    "MUTED": "#64748B",
    "CORAL": "#E03A2F",
    "CORAL_BG": "#FFF5F2",
    "CORAL_BORDER": "#F05A5A"
}


def build_open_data_lake_benchmark():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])
    
    w, h = 2600.0, 950.0
    fx, fy = place(w, h)
    fid = scene.add_frame("ARCHITECTURE · DIAGRAM DESIGN — Open data lake · End-to-end stack", fx, fy, w, h)
    
    # 1. Breadcrumb & Header Editorial Serif
    scene.add_text(fx + 60, fy + 35, "ARCHITECTURE  ·  DIAGRAM DESIGN", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid)
    scene.add_text(fx + 60, fy + 60, "Open data lake · End-to-end stack", font_size=32, font_family=1, color=PALETTE["INK"], frame_id=fid)

    # 2. Definición de Scopes y Tarjetas Quad
    scope_w = 420.0
    scope_h = 580.0
    scope_y = fy + 140.0
    gap = 45.0

    # SCOPE 1: SOURCES
    s1_x = fx + 60.0
    scene.add_scope_container(s1_x, scope_y, scope_w, scope_h, label="SOURCES", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid)
    c1, _ = scene.add_quad_card(s1_x + 25.0, scope_y + 65.0, scope_w - 50.0, 115.0, "App servers", sublabel="Events · logs", badge="EXT", icon="server", frame_id=fid)
    c2, _ = scene.add_quad_card(s1_x + 25.0, scope_y + 225.0, scope_w - 50.0, 115.0, "Databases", sublabel="CDC · exports", badge="EXT", icon="database", frame_id=fid)

    # SCOPE 2: INGEST
    s2_x = s1_x + scope_w + gap
    scene.add_scope_container(s2_x, scope_y, scope_w, scope_h, label="INGEST", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid)
    c3, _ = scene.add_quad_card(s2_x + 25.0, scope_y + 65.0, scope_w - 50.0, 115.0, "Apache NiFi", sublabel="Route · transform", badge="FLOW", icon="airflow", frame_id=fid)
    c4, _ = scene.add_quad_card(s2_x + 25.0, scope_y + 225.0, scope_w - 50.0, 115.0, "Airflow", sublabel="DAG scheduling", badge="ORCH", icon="airflow", frame_id=fid)

    # SCOPE 3: DATA LAKE (HERO CORAL)
    s3_x = s2_x + scope_w + gap
    scene.add_scope_container(s3_x, scope_y, scope_w, scope_h, label="DATA LAKE", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid)
    c5, _ = scene.add_quad_card(s3_x + 25.0, scope_y + 145.0, scope_w - 50.0, 135.0, "MinIO", sublabel="Object store · S3-API", badge="STORE", icon="minio", is_hero=True, frame_id=fid)

    # SCOPE 4: QUERY
    s4_x = s3_x + scope_w + gap
    scene.add_scope_container(s4_x, scope_y, scope_w, scope_h, label="QUERY", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid)
    c6, _ = scene.add_quad_card(s4_x + 25.0, scope_y + 65.0, scope_w - 50.0, 115.0, "Trino", sublabel="SQL · any format", badge="QUERY", icon="server", frame_id=fid)
    c7, _ = scene.add_quad_card(s4_x + 25.0, scope_y + 225.0, scope_w - 50.0, 115.0, "StarRocks", sublabel="MPP · hot layer", badge="OLAP", icon="database", frame_id=fid)

    # SCOPE 5: CONSUME
    s5_x = s4_x + scope_w + gap
    scene.add_scope_container(s5_x, scope_y, scope_w, scope_h, label="CONSUME", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid)
    c8, _ = scene.add_quad_card(s5_x + 25.0, scope_y + 65.0, scope_w - 50.0, 115.0, "Superset", sublabel="Dashboards", badge="BI", icon="monitoring", frame_id=fid)
    c9, _ = scene.add_quad_card(s5_x + 25.0, scope_y + 225.0, scope_w - 50.0, 115.0, "JupyterLab", sublabel="Exploration", badge="NB", icon="python", frame_id=fid)
    c10, _ = scene.add_quad_card(s5_x + 25.0, scope_y + 385.0, scope_w - 50.0, 115.0, "Python", sublabel="Batch · ML", badge="PROC", icon="python", frame_id=fid)

    # 3. Conexiones Ortogonales con Etiquetas
    # Sources -> Ingest
    scene.add_arrow(c1["x"] + c1["width"], c1["y"] + c1["height"]*0.5, c3["x"], c3["y"] + c3["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, frame_id=fid)
    scene.add_arrow(c2["x"] + c2["width"], c2["y"] + c2["height"]*0.5, c4["x"], c4["y"] + c4["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, frame_id=fid)

    # Ingest -> MinIO
    scene.add_arrow(c3["x"] + c3["width"], c3["y"] + c3["height"]*0.5, c5["x"], c5["y"] + 45.0, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid)
    scene.add_arrow(c4["x"] + c4["width"], c4["y"] + c4["height"]*0.5, c5["x"], c5["y"] + 90.0, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid)

    # MinIO -> Query (Trino Orange Arrow & StarRocks)
    scene.add_arrow(c5["x"] + c5["width"], c5["y"] + 45.0, c6["x"], c6["y"] + c6["height"]*0.5, stroke=PALETTE["CORAL"], stroke_w=2.0, label="SQL", orthogonal=True, frame_id=fid)
    scene.add_arrow(c5["x"] + c5["width"], c5["y"] + 90.0, c7["x"], c7["y"] + c7["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid)

    # Query -> Consume
    scene.add_arrow(c6["x"] + c6["width"], c6["y"] + c6["height"]*0.5, c8["x"], c8["y"] + c8["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, frame_id=fid)
    scene.add_arrow(c6["x"] + c6["width"], c6["y"] + c6["height"]*0.5 + 20.0, c9["x"], c9["y"] + c9["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid)
    scene.add_arrow(c7["x"] + c7["width"], c7["y"] + c7["height"]*0.5, c10["x"], c10["y"] + c10["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid)

    # Write-back path from Python to MinIO (dashed gray)
    scene.add_arrow(c10["x"] + c10["width"]*0.5, c10["y"] + c10["height"],
                    c5["x"] + c5["width"]*0.5, c5["y"] + c5["height"],
                    stroke=PALETTE["MUTED"], stroke_w=1.5, dashed=True, label="WRITE", orthogonal=True, frame_id=fid)

    # 4. Leyenda Inferior Estructurada con Nota Editorial
    scene.add_legend_footer(fx + 60.0, fy + 800.0, w - 120.0,
                            swatches=[
                                {"label": "MinIO data lake (focal)", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL"]},
                                {"label": "Ingest · query tools", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]},
                                {"label": "BI · notebooks · pipelines", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]},
                                {"label": "Primary query path", "is_arrow": True, "stroke": PALETTE["CORAL"]},
                                {"label": "Write-back path (batch)", "is_arrow": True, "dashed": True, "stroke": PALETTE["MUTED"]}
                            ],
                            note="One coral. Position is the signal — color reserved for the recommended option.",
                            frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    
    out_path = os.path.join(OUT_DIR, "open_data_lake_editorial.excalidraw")
    scene.save(out_path)
    print(f"[+] Archivo Excalidraw Benchmark guardado en: {out_path}")
    
    _, report = validate_scene(out_path)
    print("\n" + report.summary())
    return out_path


if __name__ == "__main__":
    build_open_data_lake_benchmark()
