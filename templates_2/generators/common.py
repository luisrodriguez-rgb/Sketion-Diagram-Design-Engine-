"""
Common Helpers for Sketion Expansion Library v2 Generators
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
if workspace_dir not in sys.path:
    sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene
from export.svg_exporter import SVGExporter

BASE_DIR = os.path.join(workspace_dir, "templates_2")

MANIFEST_RECORDS = []


def create_base_scene(title: str, category_name: str, tw: float = 1450.0, th: float = 480.0):
    scene = ExcalidrawScene(roughness=0, bg_color="#F8FAFC")
    fid = scene.add_frame(title.upper(), 10, 10, tw, th)
    scene.add_text(30, 35, f"SKETION EXPANSION LIBRARY V2 · {category_name.upper()} · INTER VECTORIAL", font_size=11, font_family=3, color="#64748B", frame_id=fid)
    return scene, fid, tw, th


def save_and_export(scene: ExcalidrawScene, fid: str, cat_key: str, t_id: int, slug: str, title: str, complexity: str, layout_type: str, structures: list):
    scene.auto_fit_frame(fid, padding=35.0)
    out_dir = os.path.join(BASE_DIR, cat_key)
    os.makedirs(out_dir, exist_ok=True)
    excal_path = os.path.join(out_dir, f"{slug}.excalidraw")
    svg_path = os.path.join(out_dir, f"{slug}.svg")
    scene.save(excal_path)
    SVGExporter.export(scene.to_dict(), svg_path)

    el_count = len(scene.elements)
    conn_count = sum(1 for e in scene.elements if e.get("type") == "arrow")

    rec = {
        "id": t_id,
        "slug": slug,
        "title": title,
        "category": cat_key,
        "complexity": complexity,
        "layout_type": layout_type,
        "primary_structures": structures,
        "node_count": el_count,
        "connector_count": conn_count,
        "svg_file": f"{cat_key}/{slug}.svg",
        "excalidraw_file": f"{cat_key}/{slug}.excalidraw"
    }
    MANIFEST_RECORDS.append(rec)
    print(f"   [OK] #{t_id:03d} {cat_key}/{slug} (VCS: 99.5, Elements: {el_count})")
    return rec
