"""
Sketion Visual & Editorial Quality Validation
"""
from typing import Dict, Any, List, Set

def validate_visual_quality(scene_dict: Dict[str, Any],
                            accent_hex_list: List[str] = None) -> List[str]:
    """Valida reglas de diseño editorial (densidad, regla del acento único, tipografía)."""
    warnings = []
    if accent_hex_list is None:
        accent_hex_list = ["#2563EB", "#F5BEC0", "#B58E3F", "#EFF6FF", "#FDF2F4", "#FBF6EB", "#DC2626", "#EF4444"]

    elements = scene_dict.get("elements", [])
    frames = [e for e in elements if e.get("type") == "frame"]
    non_frames = [e for e in elements if e.get("type") != "frame"]

    # Conteo de acentos por frame
    accent_count = 0
    font_families: Set[int] = set()

    for e in non_frames:
        bg = str(e.get("backgroundColor", "")).upper()
        stroke = str(e.get("strokeColor", "")).upper()
        
        for acc in accent_hex_list:
            acc_upper = acc.upper()
            if acc_upper in bg or acc_upper in stroke:
                accent_count += 1
                break

        if e.get("type") == "text" and "fontFamily" in e:
            font_families.add(e["fontFamily"])

    if len(font_families) > 2:
        warnings.append(f"Uso excesivo de tipografías ({len(font_families)} familias detectadas). Se recomienda máximo 2.")

    # Validar densidad por frame
    if frames:
        for f in frames:
            fid = f.get("id")
            frame_children = [e for e in non_frames if e.get("frameId") == fid and e.get("type") == "rectangle"]
            if len(frame_children) > 12:
                warnings.append(f"Frame '{f.get('name')}' excede la densidad recomendada ({len(frame_children)} nodos). Evaluar dividir en dos tableros.")

    return warnings
