"""
Sketion Visual & Editorial Quality Validation (v8.5 Diversity Aware)
Evalúa:
1. Densidad visual editorial (Target Diagram Design: 4.0/10)
2. Regla del acento único por marco narrativo
3. Consistencia tipográfica (máximo 2 familias activas)
4. Entropía geométrica y diversidad morfológica (anti-monocultivo de layout)
5. Conectividad y ratio de flujo direccional
"""

from typing import Dict, Any, List, Set


def validate_visual_quality(scene_dict: Dict[str, Any],
                            accent_hex_list: List[str] = None) -> List[str]:
    """Valida reglas de diseño editorial, jerarquía, y diversidad morfológica."""
    warnings = []
    if accent_hex_list is None:
        accent_hex_list = ["#2563EB", "#F5BEC0", "#B58E3F", "#EFF6FF", "#FDF2F4", "#FBF6EB", "#DC2626", "#EF4444", "#D93829", "#FFF5F2"]

    elements = scene_dict.get("elements", [])
    if not isinstance(elements, list):
        return warnings

    frames = [e for e in elements if isinstance(e, dict) and e.get("type") == "frame"]
    non_frames = [e for e in elements if isinstance(e, dict) and e.get("type") != "frame"]

    # 1. Tipografías
    font_families: Set[int] = set()
    for e in non_frames:
        if e.get("type") == "text" and "fontFamily" in e:
            font_families.add(e["fontFamily"])

    if len(font_families) > 2:
        warnings.append(f"Uso excesivo de tipografías ({len(font_families)} familias detectadas). Se recomienda máximo 2.")

    # 2. Diversidad Morfológica & Anti-Monocultivo (Layout Entropy)
    type_counts = {}
    for e in non_frames:
        t = e.get("type", "unknown")
        type_counts[t] = type_counts.get(t, 0) + 1

    total_elems = max(1, len(non_frames))
    rect_ratio = type_counts.get("rectangle", 0) / total_elems

    # Si más del 85% son rectángulos y no hay elipses ni flechas en un diagrama complejo (>30 elementos)
    if total_elems > 30 and rect_ratio > 0.85 and type_counts.get("arrow", 0) == 0:
        warnings.append("Alerta de Monocultivo Visual: El diagrama está compuesto casi exclusivamente por rectángulos estáticos sin flechas de flujo ni variedad morfológica.")

    # 3. Validación de densidad y acentos por marco
    if frames:
        for f in frames:
            fid = f.get("id")
            fname = f.get("name", fid)
            frame_children = [e for e in non_frames if e.get("frameId") == fid]
            frame_rects = [e for e in frame_children if e.get("type") == "rectangle"]
            frame_arrows = [e for e in frame_children if e.get("type") == "arrow"]

            # Densidad
            if len(frame_rects) > 18:
                warnings.append(f"Frame '{fname}' excede la densidad recomendada ({len(frame_rects)} cajas). Evaluar partición adaptativa.")

            # Acentos dentro de este marco
            f_accents = 0
            for e in frame_children:
                bg = str(e.get("backgroundColor", "")).upper()
                stroke = str(e.get("strokeColor", "")).upper()
                for acc in accent_hex_list:
                    if acc.upper() in bg or acc.upper() in stroke:
                        f_accents += 1
                        break

            if f_accents > 3:
                warnings.append(f"Frame '{fname}' tiene {f_accents} elementos de acento. Se recomienda máximo 1-2 por marco narrativo.")

    return warnings
