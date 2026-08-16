"""
Sketion Accent Repair
Garantiza la regla del acento único (máximo 1-2 nodos focales).
"""
from typing import Dict, Any, List, Tuple

DEFAULT_ACCENTS = ["#2563EB", "#F5BEC0", "#B58E3F", "#EFF6FF", "#FDF2F4", "#FBF6EB", "#DC2626", "#EF4444"]

def repair_accents(scene_data: Dict[str, Any],
                   accent_hex_list: List[str] = None,
                   neutral_bg: str = "#FFFFFF",
                   neutral_stroke: str = "#0F172A",
                   primary_hero_id: str = None) -> List[str]:
    """Degrada nodos de acento excedentes para preservar la jerarquía visual."""
    if accent_hex_list is None:
        accent_hex_list = DEFAULT_ACCENTS

    repairs = []
    elements = scene_data.get("elements", [])
    accent_cards = []

    for e in elements:
        if e.get("type") == "rectangle":
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
            repairs.append(f"Auto-Repair: Nodo {cid} degradado a neutro (regla 1-2 acentos).")

    return repairs
