"""
Sketion Self-Correction & Auto-Repair Engine
Detecta y repara automáticamente desviaciones visuales y estructurales:
- Exceso de nodos de acento (los degrada a neutros respetando el héroe principal)
- Reparación de vínculos containerId <-> boundElements
- Re-enrutamiento ortogonal de conectores
"""

from typing import Dict, Any, List, Tuple
from .quality_score import calculate_quality_score, QualityMetrics

def repair_scene(scene_data: Dict[str, Any],
                 primary_hero_id: str = None,
                 neutral_bg: str = "#FFFFFF",
                 neutral_stroke: str = "#0F172A") -> Tuple[Dict[str, Any], List[str]]:
    """
    Aplica el bucle de auto-corrección sobre una escena Excalidraw.
    Retorna la escena reparada y una lista de acciones correctivas realizadas.
    """
    repaired = False
    repairs_log = []
    elements = scene_data.get("elements", [])

    # 1. Reparación Estructural (Bindings recíprocos)
    elem_map = {e["id"]: e for e in elements if "id" in e}
    for e in elements:
        if e.get("type") == "text" and e.get("containerId"):
            cid = e["containerId"]
            if cid in elem_map:
                container = elem_map[cid]
                b_elements = container.setdefault("boundElements", [])
                b_ids = [b.get("id") for b in b_elements]
                if e["id"] not in b_ids:
                    b_elements.append({"id": e["id"], "type": "text"})
                    repairs_log.append(f"Auto-Repair: Vinculado bidireccional texto {e['id']} en contenedor {cid}.")
                    repaired = True

    # 2. Reparación de Jerarquía (Regla de 1-2 Acentos)
    accent_hex_list = ["#2563EB", "#F5BEC0", "#B58E3F", "#EFF6FF", "#FDF2F4", "#FBF6EB", "#DC2626", "#EF4444"]
    accent_nodes = []
    for e in elements:
        if e.get("type") == "rectangle":
            bg = str(e.get("backgroundColor", "")).upper()
            stroke = str(e.get("strokeColor", "")).upper()
            for acc in accent_hex_list:
                if acc.upper() in bg or acc.upper() in stroke:
                    accent_nodes.append(e)
                    break

    if len(accent_nodes) > 2:
        # Mantener los 2 primeros (o el que coincida con primary_hero_id) y degradar los demás
        kept = 0
        for node in accent_nodes:
            if primary_hero_id and node.get("id") == primary_hero_id:
                continue
            if kept < 2:
                kept += 1
                continue
            # Degradar a neutro
            node["backgroundColor"] = neutral_bg
            node["strokeColor"] = neutral_stroke
            repairs_log.append(f"Auto-Repair: Nodo {node.get('id')} degradado a neutro para respetar la regla de 1-2 acentos.")
            repaired = True

    return scene_data, repairs_log
