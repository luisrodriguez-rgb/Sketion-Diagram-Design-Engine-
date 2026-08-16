"""
Sketion Binding Repair
Re-sincroniza vínculos containerId <-> boundElements rotos o incompletos.
"""
from typing import Dict, Any, List

def repair_bindings(scene_data: Dict[str, Any]) -> List[str]:
    """Repara cualquier texto o contenedor con referencias de vinculación incompletas."""
    repairs = []
    elements = scene_data.get("elements", [])
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
                    repairs.append(f"Auto-Repair: Vinculado bidireccional texto {e['id']} en contenedor {cid}.")

    return repairs
