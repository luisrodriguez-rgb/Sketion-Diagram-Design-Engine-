"""
Sketion Frame Containment Repair Engine
Detecta y corrige automáticamente elementos asignados a un frame cuyas coordenadas físicas
hayan quedado desalineadas o fuera del marco contenedor.
"""

from typing import Dict, Any, List


def repair_frame_containment(scene_data: Dict[str, Any], margin: float = 20.0) -> List[str]:
    """
    Verifica que todos los elementos con 'frameId' se encuentren dentro de su frame contenedor.
    Si un elemento tiene coordenadas locales (e.g. y < frame.y) o desbordadas, lo re-ancla
    automáticamente dentro del marco asignado.
    """
    repairs = []
    elements = scene_data.get("elements", [])
    elem_map = {e["id"]: e for e in elements if isinstance(e, dict) and "id" in e}
    frames = {e["id"]: e for e in elements if isinstance(e, dict) and e.get("type") == "frame"}

    for e in elements:
        fid = e.get("frameId")
        if not fid or fid not in frames:
            continue

        f = frames[fid]
        fx, fy = f.get("x", 0.0), f.get("y", 0.0)
        fw, fh = f.get("width", 1000.0), f.get("height", 800.0)

        ex, ey = e.get("x", 0.0), e.get("y", 0.0)
        ew = e.get("width", 0.0)
        eh = e.get("height", 0.0)

        # 1. Caso: Coordenadas relativas/locales pasadas en vez de absolutas
        # e.g., el frame está en Y=2300, pero el elemento fue puesto en Y=150
        if ey < fy - margin and (0.0 <= ey <= fh):
            e["y"] = fy + ey
            repairs.append(f"Auto-Repair: Convertida coordenada Y local ({ey:.1f}) a absoluta ({e['y']:.1f}) para elemento {e['id']} en frame {fid}.")
            ey = e["y"]

        if ex < fx - margin and (0.0 <= ex <= fw):
            e["x"] = fx + ex
            repairs.append(f"Auto-Repair: Convertida coordenada X local ({ex:.1f}) a absoluta ({e['x']:.1f}) para elemento {e['id']} en frame {fid}.")
            ex = e["x"]

        # 2. Caso: Auto-expansión del frame si los elementos desbordan ligeramente por la derecha o abajo
        if ex + ew > fx + fw - margin:
            needed_w = (ex + ew - fx) + margin * 2
            f["width"] = max(f["width"], needed_w)
            repairs.append(f"Auto-Repair: Expandido ancho de frame {fid} a {f['width']:.1f}px para contener elemento {e['id']}.")

        if ey + eh > fy + fh - margin:
            needed_h = (ey + eh - fy) + margin * 2
            f["height"] = max(f["height"], needed_h)
            repairs.append(f"Auto-Repair: Expandido alto de frame {fid} a {f['height']:.1f}px para contener elemento {e['id']}.")

    return repairs
