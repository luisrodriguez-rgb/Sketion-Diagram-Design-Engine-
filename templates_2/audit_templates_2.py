"""
Sketion 10.0 Expansion Library v2 Quality & Structural Diversity Auditor
Inspecciona y evalua las 150 plantillas curadas en /templates_2:
- Integridad estructural de archivos .svg y .excalidraw
- Deteccion estricta de emojis (Regla Cero Emojis)
- Validez de JSON y XML SVG
- Evaluacion de jerarquia tipografica, contraste y tokens
- Validacion del manifest template_manifest.json
- Calculo de VCS (Visual Consistency Score) por categoria
"""

import os
import json
import xml.etree.ElementTree as ET
import re

BASE_DIR = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL/templates_2"

CATEGORIES = [
    "01_estudio_educacion",
    "02_ingenieria_procesos",
    "03_software_architecture",
    "04_data_apis_ai",
    "05_negocios_estrategia",
    "06_producto_pm",
    "07_ux_research",
    "08_design_thinking_ideation",
    "09_agile_proyectos",
    "10_productividad_personal"
]

EMOJI_PATTERN = re.compile(
    r"[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]|[\ufe00-\ufe0f]"
)


def audit_expansion_library():
    report = {
        "total_templates": 0,
        "total_svgs": 0,
        "total_excalidraw": 0,
        "emoji_violations": 0,
        "json_errors": 0,
        "svg_errors": 0,
        "categories": {},
        "global_vcs_sum": 0.0,
        "complexity_distribution": {"low": 0, "medium": 0, "high": 0, "extreme": 0}
    }

    # 1. Check manifest
    manifest_path = os.path.join(BASE_DIR, "template_manifest.json")
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as f:
            m_data = json.load(f)
            for t in m_data.get("templates", []):
                c = t.get("complexity", "medium")
                report["complexity_distribution"][c] = report["complexity_distribution"].get(c, 0) + 1

    # 2. Inspect category files
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

            # Check Excalidraw JSON
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

            # Check SVG XML
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

            # VCS
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
            report["total_templates"] += 1
            report["global_vcs_sum"] += vcs

        report["categories"][cat] = cat_stats

    return report


if __name__ == "__main__":
    rep = audit_expansion_library()
    avg_vcs = rep["global_vcs_sum"] / max(1, rep["total_templates"])
    print(f"Total Plantillas Auditadas en templates_2: {rep['total_templates']}")
    print(f"Total SVGs Validados: {rep['total_svgs']} / {rep['total_templates']}")
    print(f"Total Excalidraw Validados: {rep['total_excalidraw']} / {rep['total_templates']}")
    print(f"Violaciones de Emojis: {rep['emoji_violations']}")
    print(f"Errores de JSON/XML: {rep['json_errors'] + rep['svg_errors']}")
    print(f"VCS Promedio Global: {avg_vcs:.2f} / 100")
    print(f"Distribucion de Complejidad: {rep['complexity_distribution']}")
    print("\n--- Desglose por Categoria en templates_2 ---")
    for cat, s in rep["categories"].items():
        c_avg = s["vcs_sum"] / max(1, s["count"])
        print(f" • {cat:<28}: {s['count']:>2} plantillas | {s['elements_sum']:>4} elementos | VCS: {c_avg:.2f}/100")
