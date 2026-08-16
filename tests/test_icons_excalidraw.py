"""
Sketion 4.0 — Test de Integración de Iconos Vectoriales Nativos en Excalidraw
Demuestra la incrustación de iconos monocromáticos (Tabler / SimpleIcons)
directamente en tarjetas y scopes dentro de .excalidraw sin dependencias externas.
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from validation.validator import validate_scene

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_27_TYPES")
os.makedirs(OUT_DIR, exist_ok=True)

MIRO_PALETTE = {
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


def build_icon_demo_scene():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color=MIRO_PALETTE["CANVAS"])
    
    w, h = 2800, 950
    fx, fy = place(w, h)
    fid = scene.add_frame("DEMO: Biblioteca de Iconos Monocromáticos Nativos (.excalidraw)", fx, fy, w, h)
    
    scene.add_text(fx + 50, fy + 35, "BIBLIOTECA DE ICONOS VECTORIALES MONOCROMÁTICOS NATIVOS", font_size=30, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid)
    scene.add_text(fx + 50, fy + 75, "iconos vectoriales tabler y marcas incrustados directamente en el archivo .excalidraw (cero dependencias)", font_size=16, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid)

    categories = [
        ("1. COMPUTE & SERVERS", [("server", "API Server Node", "Node.js / Express"), ("container", "Docker Container", "Isolated Process"), ("vm", "Virtual Machine", "Linux KVM Cluster")]),
        ("2. DATA & STORAGE", [("database", "PostgreSQL DB", "Relational Primary"), ("redis", "Redis In-Memory", "Sub-millisecond Cache"), ("bucket", "MinIO S3 Bucket", "Object Media Storage")]),
        ("3. NETWORK & SECURITY", [("cloud", "AWS Cloud VPC", "Region us-east-1"), ("gateway", "Kong API Gateway", "Rate Limit & Auth"), ("lock", "Zero Trust Auth", "Mutual TLS & JWT")]),
        ("4. DEVOPS & STACK", [("kubernetes", "K8s Cluster EKS", "Auto-scaling Pods"), ("terminal", "CLI Automation", "Bash & Python SDK"), ("monitoring", "Prometheus Metrics", "Alerting & Grafana")])
    ]

    col_w = (w - 120.0 - 3 * 50.0) / 4.0
    for ci, (cat_name, cat_items) in enumerate(categories):
        cx = fx + 60.0 + ci * (col_w + 50.0)
        cy = fy + 140.0
        
        is_hero_col = (ci == 1)
        bg = MIRO_PALETTE["PASTEL_GREEN"] if is_hero_col else "#FFFFFF"
        scene.add_scope_container(cx, cy, col_w, 650.0, label=cat_name, stroke=MIRO_PALETTE["CARD_BORDER"], bg=bg, frame_id=fid)

        for ii, (icon_name, item_title, item_sub) in enumerate(cat_items):
            iy = cy + 70.0 + ii * 180.0
            
            # Tarjeta con icono integrado
            scene.add_card_with_icon(cx + 25.0, iy, col_w - 50.0, 140.0,
                                     item_title, sublabel=item_sub, icon=icon_name,
                                     bg="#FFFFFF", stroke=MIRO_PALETTE["INK"],
                                     text_color=MIRO_PALETTE["INK"], frame_id=fid)

    scene.auto_fit_frame(fid, padding=50.0)
    
    out_path = os.path.join(OUT_DIR, "demo_icon_library.excalidraw")
    scene.save(out_path)
    print(f"[+] Archivo Excalidraw con Iconos guardado en: {out_path}")
    
    _, report = validate_scene(out_path)
    print("\n" + report.summary())
    return out_path


if __name__ == "__main__":
    build_icon_demo_scene()
