"""
Sketion Accent Repair
Garantiza la regla del acento único (máximo 1-2 nodos focales por marco narrativo).
"""
from typing import Dict, Any, List

DEFAULT_ACCENTS = ["#2563EB", "#F5BEC0", "#B58E3F", "#EFF6FF", "#FDF2F4", "#FBF6EB", "#DC2626", "#EF4444", "#D93829", "#E03A2F"]


def repair_accents(scene_data: Dict[str, Any],
                   accent_hex_list: List[str] = None,
                   neutral_bg: str = "#FFFFFF",
                   neutral_stroke: str = "#0F172A",
                   primary_hero_id: str = None) -> List[str]:
    """Degrada nodos de acento excedentes para preservar la jerarquía visual por marco."""
    if accent_hex_list is None:
        accent_hex_list = DEFAULT_ACCENTS

    repairs = []
    elements = scene_data.get("elements", [])
    frames = [e for e in elements if isinstance(e, dict) and e.get("type") == "frame"]
    non_frames = [e for e in elements if isinstance(e, dict) and e.get("type") != "frame"]

    # Si hay frames, procesar acentos por cada frame de forma independiente
    frame_ids = [f["id"] for f in frames] if frames else [None]

    for fid in frame_ids:
        if fid is not None:
            scope_cards = [e for e in non_frames if e.get("type") == "rectangle" and e.get("frameId") == fid]
        else:
            scope_cards = [e for e in non_frames if e.get("type") == "rectangle"]

        accent_cards = []
        for e in scope_cards:
            w_c = float(e.get("width", 0))
            h_c = float(e.get("height", 0))
            # Ignorar contenedores grandes de scope, badges micro y leyendas
            if (w_c >= 240 and h_c >= 320) or h_c <= 25 or (w_c <= 35 and h_c <= 25):
                continue

            bg = str(e.get("backgroundColor", "")).upper()
            stroke = str(e.get("strokeColor", "")).upper()
            for acc in accent_hex_list:
                if acc.upper() in bg or acc.upper() in stroke:
                    accent_cards.append(e)
                    break

        if len(accent_cards) > 2:
            kept = 0
            for card in accent_cards:
                cid = card.get("id")
                if primary_hero_id and cid == primary_hero_id:
                    continue
                if kept < 2:
                    kept += 1
                    continue
                card["backgroundColor"] = neutral_bg
                card["strokeColor"] = neutral_stroke
                repairs.append(f"Auto-Repair: Nodo {cid} degradado a neutro (regla 1-2 acentos en marco {fid or 'global'}).")

    return repairs
