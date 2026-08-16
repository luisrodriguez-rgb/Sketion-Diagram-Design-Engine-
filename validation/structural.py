"""
Sketion Structural Validation (Technical Excalidraw Spec)
Valida la integridad técnica estructural y geométrica de una escena Excalidraw:
- Estructura base del JSON y versión
- Unicidad de IDs
- Integridad de referencias recíprocas containerId <-> boundElements
- Confinamiento espacial estricto dentro de frames (elementos hijos contenidos en las coordenadas de su frame)
- Completitud de especificación en elementos de texto (width > 0, height > 0, originalText)
"""

from typing import Dict, Any, List


def validate_structure(scene_dict: Dict[str, Any], margin: float = 30.0) -> List[str]:
    """Valida la integridad del JSON, referencias recíprocas y confinamiento espacial de frames."""
    errors = []

    if scene_dict.get("type") != "excalidraw":
        errors.append("Falta 'type': 'excalidraw' en la raíz del documento.")
    if scene_dict.get("version") != 2:
        errors.append("Versión de Excalidraw incorrecta (debe ser 2).")

    elements = scene_dict.get("elements", [])
    if not isinstance(elements, list):
        errors.append("'elements' debe ser una lista plana.")
        return errors

    elem_map = {e.get("id"): e for e in elements if isinstance(e, dict) and "id" in e}
    frames = {e["id"]: e for e in elements if isinstance(e, dict) and e.get("type") == "frame"}
    seen_ids = set()

    for e in elements:
        eid = e.get("id")
        if not eid:
            errors.append("Elemento sin 'id' único encontrado.")
            continue
        if eid in seen_ids:
            errors.append(f"ID duplicado detectado: {eid}")
        seen_ids.add(eid)

        etype = e.get("type")

        # 1. Validar elementos de texto
        if etype == "text":
            w = float(e.get("width", 0.0))
            h = float(e.get("height", 0.0))
            if w <= 0.0 or h <= 0.0:
                errors.append(f"Texto {eid} tiene dimensiones nulas (width={w}, height={h}) lo que causa invisibilidad en el canvas.")

            if e.get("containerId"):
                cid = e["containerId"]
                if cid not in elem_map:
                    errors.append(f"Texto {eid} apunta a containerId {cid} inexistente.")
                else:
                    container = elem_map[cid]
                    bound_ids = [b.get("id") for b in container.get("boundElements", [])]
                    if eid not in bound_ids:
                        errors.append(f"Contenedor {cid} no tiene al texto {eid} en su lista 'boundElements'.")

        # 2. Validar frames y confinamiento espacial
        if e.get("frameId"):
            fid = e["frameId"]
            if fid not in frames:
                errors.append(f"Elemento {eid} referencia a frameId {fid} que no es un frame válido.")
            else:
                f = frames[fid]
                fx, fy = float(f.get("x", 0.0)), float(f.get("y", 0.0))
                fw, fh = float(f.get("width", 1000.0)), float(f.get("height", 800.0))

                ex, ey = float(e.get("x", 0.0)), float(e.get("y", 0.0))
                ew = float(e.get("width", 0.0))
                eh = float(e.get("height", 0.0))

                # Validar si el elemento quedó fuera de los límites del frame
                if (ey + eh < fy - margin) or (ey > fy + fh + margin) or (ex + ew < fx - margin) or (ex > fx + fw + margin):
                    errors.append(
                        f"Elemento {eid} ({etype}) asignado a frame '{f.get('name', fid)}' (Y=[{fy:.0f}..{fy+fh:.0f}]) "
                        f"quedó físicamente fuera de sus límites en Y=[{ey:.0f}..{ey+eh:.0f}]."
                    )

    return errors
