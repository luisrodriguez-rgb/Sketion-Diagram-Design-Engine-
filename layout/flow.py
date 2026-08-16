"""
Sketion Flow Layouts (Linear, Wave, Timeline, Symmetric User Journey)
"""
from typing import List, Dict, Any, Tuple

def compute_flow_layout(steps_count: int, start_x: float, base_y: float,
                        step_w: float = 200, step_h: float = 100,
                        gap_x: float = 60, wave: bool = False,
                        amplitude: float = 40) -> List[Dict[str, float]]:
    """Calcula las posiciones (x, y, w, h) para una secuencia horizontal."""
    coords = []
    for i in range(steps_count):
        sx = start_x + i * (step_w + gap_x)
        sy = base_y
        if wave:
            sy += amplitude if (i % 2 == 1) else -amplitude
        coords.append({"x": sx, "y": sy, "w": step_w, "h": step_h, "idx": i})
    return coords

def compute_timeline_layout(milestones_count: int, start_x: float, axis_y: float,
                            total_width: float, step_w: float = 200,
                            step_h: float = 80, offset_y: float = 120) -> List[Dict[str, float]]:
    """Calcula posiciones para un eje cronológico con tarjetas alternadas arriba/abajo."""
    coords = []
    spacing = total_width / max(1, milestones_count)
    for i in range(milestones_count):
        px = start_x + i * spacing
        is_above = (i % 2 == 0)
        card_y = axis_y - offset_y if is_above else axis_y + 40
        card_x = px - step_w * 0.5 + 10
        coords.append({
            "marker_x": px,
            "axis_y": axis_y,
            "card_x": card_x,
            "card_y": card_y,
            "w": step_w,
            "h": step_h,
            "is_above": is_above
        })
    return coords

def compute_symmetric_journey_layout(steps_count: int, start_x: float, steps_y: float,
                                     slots_y: float, total_width: float,
                                     step_h: float = 95, slot_h: float = 320,
                                     gap_between: float = 40.0) -> Dict[str, Any]:
    """
    Calcula un layout de User Journey con simetría 1:1 estricta entre cada paso
    superior y su correspondiente slot de captura inferior.
    """
    usable_width = total_width - (steps_count - 1) * gap_between
    card_w = max(180.0, usable_width / max(1, steps_count))
    
    steps = []
    slots = []
    
    for i in range(steps_count):
        cx = start_x + i * (card_w + gap_between)
        steps.append({
            "idx": i,
            "x": cx,
            "y": steps_y,
            "w": card_w,
            "h": step_h
        })
        slots.append({
            "idx": i,
            "x": cx,
            "y": slots_y,
            "w": card_w,
            "h": slot_h
        })
        
    return {
        "steps": steps,
        "slots": slots,
        "card_w": card_w,
        "gap": gap_between
    }
