"""
Sketion Spatial Collision Repair Engine
Detecta y resuelve colisiones y superposiciones accidentales entre tarjetas hermanas
dentro del mismo marco o contenedor de alcance.
"""

from typing import Dict, Any, List, Tuple


def _boxes_overlap(b1: Tuple[float, float, float, float], b2: Tuple[float, float, float, float], margin: float = 5.0) -> bool:
    x1, y1, w1, h1 = b1
    x2, y2, w2, h2 = b2

    # Verificar si una caja es un contenedor que envuelve a la otra (e.g. Scope container)
    is_container_1 = (x1 <= x2 + margin and y1 <= y2 + margin and x1 + w1 >= x2 + w2 - margin and y1 + h1 >= y2 + h2 - margin)
    is_container_2 = (x2 <= x1 + margin and y2 <= y1 + margin and x2 + w2 >= x1 + w1 - margin and y2 + h2 >= y1 + h1 - margin)
    if is_container_1 or is_container_2:
        return False

    overlap_x = not (x1 + w1 <= x2 + margin or x2 + w2 <= x1 + margin)
    overlap_y = not (y1 + h1 <= y2 + margin or y2 + h2 <= y1 + margin)

    return overlap_x and overlap_y


def repair_spatial_collisions(scene_data: Dict[str, Any], min_gap: float = 15.0) -> List[str]:
    """
    Detecta tarjetas rectangulares que colisionan entre sí (no contenedores) y las separa verticalmente.
    """
    repairs = []
    elements = scene_data.get("elements", [])
    if not isinstance(elements, list):
        return repairs

    # Filtrar rectángulos que no sean frames ni scope containers gigantes
    cards = []
    for e in elements:
        if not isinstance(e, dict) or e.get("type") != "rectangle":
            continue
        w = float(e.get("width", 0.0))
        h = float(e.get("height", 0.0))
        # Excluir scope containers gigantes (w >= 400 & h >= 500) y micro-pills
        if (w >= 400.0 and h >= 500.0) or h <= 25.0:
            continue
        cards.append(e)

    # Ordenar por Y
    cards.sort(key=lambda c: (float(c.get("y", 0)), float(c.get("x", 0))))

    for i in range(len(cards)):
        c1 = cards[i]
        c1_box = (float(c1.get("x", 0)), float(c1.get("y", 0)), float(c1.get("width", 0)), float(c1.get("height", 0)))
        for j in range(i + 1, len(cards)):
            c2 = cards[j]
            c2_box = (float(c2.get("x", 0)), float(c2.get("y", 0)), float(c2.get("width", 0)), float(c2.get("height", 0)))

            if _boxes_overlap(c1_box, c2_box):
                # Desplazar c2 hacia abajo para resolver la colisión
                new_y = c1_box[1] + c1_box[3] + min_gap
                dy = new_y - c2_box[1]
                if dy > 0:
                    c2["y"] = new_y
                    repairs.append(f"Auto-Repair: Separada colisión entre tarjeta {c1.get('id')} y {c2.get('id')}, desplazando Y a {new_y:.1f}px.")

                    # Desplazar textos vinculados si existen
                    cid = c2.get("id")
                    for t in elements:
                        if t.get("type") == "text" and t.get("containerId") == cid:
                            t["y"] = float(t.get("y", 0.0)) + dy

                    c2_box = (c2_box[0], new_y, c2_box[2], c2_box[3])

    return repairs
