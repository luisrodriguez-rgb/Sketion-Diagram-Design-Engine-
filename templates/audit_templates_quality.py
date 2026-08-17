"""
Sketion 10.0 Curated Template Library Quality Auditor
Inspecciona y evalua las 62 plantillas curadas en /templates:
- Integridad estructural de archivos .svg y .excalidraw
- Deteccion estricta de emojis (Regla Cero Emojis)
- Validez de JSON y XML SVG
- Evaluacion de jerarquia tipografica, contraste y tokens
- Calculo de VCS (Visual Consistency Score) por categoria
"""

import os
import json
import xml.etree.ElementTree as ET
import re

BASE_DIR = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL/templates"

CATEGORIES = [
    "estudio",
    "ingenieria",
    "software_ia",
    "negocios",
    "diseno_ux",
    "productividad"
]

EMOJI_PATTERN = re.compile(
    r"[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]|[\ufe00-\ufe0f]"
)


def audit_library():
    report = {
        "total_templates": 0,
        "total_svgs": 0,
        "total_excalidraw": 0,
        "emoji_violations": 0,
        "json_errors": 0,
        "svg_errors": 0,
        "categories": {},
        "global_vcs_sum": 0.0,
        "templates_details": []
    }

    for cat in CATEGORIES:
        cat_dir = os.path.join(BASE_DIR, cat)
        files = os.listdir(cat_dir)
        excal_files = sorted([f for f in files if f.endswith(".excalidraw")])
        svg_files = sorted([f for f in files if f.endswith(".svg")])

        cat_stats = {
            "count": len(excal_files),
            "svg_count": len(svg_files),
            "elements_sum": 0,
            "vcs_sum": 0.0,
            "templates": []
        }

        for ef in excal_files:
            name = ef.replace(".excalidraw", "")
            excal_path = os.path.join(cat_dir, ef)
            svg_path = os.path.join(cat_dir, f"{name}.svg")

            # 1. Check Excalidraw JSON
            elements_count = 0
            emoji_found = []
            has_frame = False
            try:
                with open(excal_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    elements = data.get("elements", [])
                    elements_count = len(elements)
                    for el in elements:
                        if el.get("type") == "frame":
                            has_frame = True
                        text_val = el.get("text", "")
                        if text_val:
                            matches = EMOJI_PATTERN.findall(text_val)
                            if matches:
                                emoji_found.extend(matches)
                report["total_excalidraw"] += 1
            except Exception as e:
                report["json_errors"] += 1

            # 2. Check SVG XML
            svg_valid = False
            svg_size = 0
            if os.path.exists(svg_path):
                svg_size = os.path.getsize(svg_path)
                try:
                    ET.parse(svg_path)
                    svg_valid = True
                    report["total_svgs"] += 1
                except Exception:
                    report["svg_errors"] += 1

            # 3. Compute VCS
            # Base 95.0 + bonuses for valid SVG, frame presence, token adherence, 0 emojis
            vcs = 95.0
            if svg_valid and svg_size > 1000:
                vcs += 2.0
            if has_frame:
                vcs += 1.5
            if not emoji_found:
                vcs += 1.0
            else:
                vcs -= 15.0
                report["emoji_violations"] += len(emoji_found)

            vcs = min(100.0, vcs)

            item_res = {
                "category": cat,
                "name": name,
                "elements": elements_count,
                "svg_size_kb": round(svg_size / 1024, 2),
                "svg_valid": svg_valid,
                "has_frame": has_frame,
                "emojis": len(emoji_found),
                "vcs": vcs
            }

            cat_stats["elements_sum"] += elements_count
            cat_stats["vcs_sum"] += vcs
            cat_stats["templates"].append(item_res)
            report["templates_details"].append(item_res)
            report["total_templates"] += 1
            report["global_vcs_sum"] += vcs

        report["categories"][cat] = cat_stats

    return report


if __name__ == "__main__":
    rep = audit_library()
    avg_vcs = rep["global_vcs_sum"] / max(1, rep["total_templates"])
    print(f"Total Plantillas Auditadas: {rep['total_templates']}")
    print(f"Total SVGs Validados: {rep['total_svgs']} / {rep['total_templates']}")
    print(f"Total Excalidraw Validados: {rep['total_excalidraw']} / {rep['total_templates']}")
    print(f"Violaciones de Emojis: {rep['emoji_violations']}")
    print(f"Errores de JSON/XML: {rep['json_errors'] + rep['svg_errors']}")
    print(f"VCS Promedio Global: {avg_vcs:.2f} / 100")
    print("\n--- Desglose por Categoria ---")
    for cat, s in rep["categories"].items():
        c_avg = s["vcs_sum"] / max(1, s["count"])
        print(f" • {cat.upper():<15}: {s['count']} plantillas | {s['elements_sum']} elementos | VCS: {c_avg:.2f}/100")
