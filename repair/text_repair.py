"""
Sketion Text Element Completeness & Typography Repair Engine
Garantiza que el 100% de los elementos de texto en cualquier escena Excalidraw cuenten
con atributos requeridos por la especificación oficial de Excalidraw para renderizar
glifos visibles en pantalla:
- 'originalText' sincronizado con 'text'
- Dimensiones 'width' y 'height' no nulas calculadas matemáticamente
- 'lineHeight' = 1.25 y 'baseline' = fontSize
- Vinculación bidireccional 'containerId' <-> 'boundElements' en rectángulos contenedores
"""

from typing import Dict, Any, List


def repair_text_elements(scene_data: Dict[str, Any]) -> List[str]:
    """Repara y normaliza elementos de texto incompletos o invisibles."""
    repairs = []
    elements = scene_data.get("elements", [])
    if not isinstance(elements, list):
        return repairs

    elem_map = {e["id"]: e for e in elements if isinstance(e, dict) and "id" in e}

    for e in elements:
        if not isinstance(e, dict) or e.get("type") != "text":
            continue

        eid = e.get("id", "unknown")
        raw_text = str(e.get("text", "") or e.get("originalText", ""))
        font_size = int(e.get("fontSize", 14))

        # 1. Asegurar originalText
        if not e.get("originalText") and raw_text:
            e["originalText"] = raw_text
            repairs.append(f"Auto-Repair: Sincronizado originalText para elemento {eid}.")

        # 2. Asegurar lineHeight y baseline
        if not e.get("lineHeight"):
            e["lineHeight"] = 1.25
            repairs.append(f"Auto-Repair: Establecido lineHeight=1.25 para elemento {eid}.")

        if not e.get("baseline"):
            e["baseline"] = font_size
            repairs.append(f"Auto-Repair: Establecido baseline={font_size} para elemento {eid}.")

        # 3. Asegurar dimensiones no-cero para renderizado de glifos en Excalidraw
        cur_w = float(e.get("width", 0.0))
        cur_h = float(e.get("height", 0.0))

        lines = raw_text.split("\n") if raw_text else [" "]
        max_line_len = max((len(l) for l in lines), default=1)

        # Estimación aproximada de ancho (8.5px por char a 14px)
        char_w = (font_size * 0.62)
        calc_w = max(40.0, max_line_len * char_w + 10.0)
        calc_h = max(20.0, len(lines) * font_size * 1.35)

        if cur_w <= 0.0:
            e["width"] = calc_w
            repairs.append(f"Auto-Repair: Calculado width={calc_w:.1f}px para texto {eid}.")

        if cur_h <= 0.0:
            e["height"] = calc_h
            repairs.append(f"Auto-Repair: Calculado height={calc_h:.1f}px para texto {eid}.")

        # 4. Asegurar autoResize
        if "autoResize" not in e:
            e["autoResize"] = True

        # 5. Si tiene containerId, validar y asegurar vinculación bidireccional
        cid = e.get("containerId")
        if cid and cid in elem_map:
            container = elem_map[cid]
            b_elements = container.setdefault("boundElements", [])
            b_ids = [b.get("id") for b in b_elements]
            if eid not in b_ids:
                b_elements.append({"id": eid, "type": "text"})
                repairs.append(f"Auto-Repair: Vinculado texto {eid} en boundElements del contenedor {cid}.")

    return repairs
