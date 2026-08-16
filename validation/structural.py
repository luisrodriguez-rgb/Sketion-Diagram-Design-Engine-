"""
Sketion Structural Validation (Technical Excalidraw Spec)
"""
from typing import Dict, Any, List, Tuple

def validate_structure(scene_dict: Dict[str, Any]) -> List[str]:
    """Valida la integridad del JSON y las referencias recíprocas de Excalidraw."""
    errors = []

    if scene_dict.get("type") != "excalidraw":
        errors.append("Falta 'type': 'excalidraw' en la raíz.")
    if scene_dict.get("version") != 2:
        errors.append("Versión de Excalidraw incorrecta (debe ser 2).")

    elements = scene_dict.get("elements", [])
    if not isinstance(elements, list):
        errors.append("'elements' debe ser una lista plana.")
        return errors

    elem_map = {e.get("id"): e for e in elements if isinstance(e, dict) and "id" in e}
    seen_ids = set()

    for e in elements:
        eid = e.get("id")
        if not eid:
            errors.append("Elemento sin 'id' único encontrado.")
            continue
        if eid in seen_ids:
            errors.append(f"ID duplicado detectado: {eid}")
        seen_ids.add(eid)

        # Validar containerId en textos vinculados
        if e.get("type") == "text" and e.get("containerId"):
            cid = e["containerId"]
            if cid not in elem_map:
                errors.append(f"Texto {eid} apunta a containerId {cid} inexistente.")
            else:
                container = elem_map[cid]
                bound_ids = [b.get("id") for b in container.get("boundElements", [])]
                if eid not in bound_ids:
                    errors.append(f"Contenedor {cid} no tiene a texto {eid} en su boundElements.")

        # Validar frameId
        if e.get("frameId"):
            fid = e["frameId"]
            if fid not in elem_map or elem_map[fid].get("type") != "frame":
                errors.append(f"Elemento {eid} referencia a frameId {fid} que no es un frame válido.")

    return errors
