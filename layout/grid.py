"""
Sketion Grid Layouts (Matrix, Board / Kanban, Dashboard)
"""
from typing import List, Dict, Any

def compute_matrix_layout(start_x: float, start_y: float,
                          col_count: int, row_count: int,
                          col_w: float = 200, row_h: float = 55) -> Dict[str, Any]:
    """Calcula las celdas de una tabla / matriz con cabeceras."""
    headers_coords = [{"x": start_x + c * col_w, "y": start_y, "w": col_w, "h": row_h, "col": c} for c in range(col_count)]
    rows_coords = []
    for r in range(row_count):
        y = start_y + (r + 1) * row_h
        row_cells = [{"x": start_x + c * col_w, "y": y, "w": col_w, "h": row_h, "col": c, "row": r} for c in range(col_count)]
        rows_coords.append(row_cells)
    return {"headers": headers_coords, "rows": rows_coords}

def compute_board_layout(start_x: float, start_y: float,
                         lanes: List[Dict[str, Any]], lane_w: float = 260,
                         card_h: float = 75, gap_x: float = 40,
                         card_gap_y: float = 20) -> List[Dict[str, Any]]:
    """Calcula las posiciones de carriles verticales y tarjetas apiladas."""
    lanes_coords = []
    for li, lane in enumerate(lanes):
        lx = start_x + li * (lane_w + gap_x)
        items_coords = []
        cy = start_y + 85
        for item in lane.get("items", []):
            items_coords.append({"x": lx, "y": cy, "w": lane_w, "h": card_h, "text": item})
            cy += card_h + card_gap_y
        
        lanes_coords.append({
            "idx": li,
            "header": {"x": lx, "y": start_y, "w": lane_w, "h": 55, "title": lane.get("title", "")},
            "items": items_coords
        })
    return lanes_coords

def compute_dashboard_layout(start_x: float, start_y: float,
                             metrics_count: int, cols: int = 4,
                             chip_w: float = 230, chip_h: float = 130,
                             gap: float = 30) -> List[Dict[str, float]]:
    """Calcula la grilla de chips numéricos para KPIs."""
    chips_coords = []
    for i in range(metrics_count):
        col = i % cols
        row = i // cols
        cx = start_x + col * (chip_w + gap)
        cy = start_y + row * (chip_h + gap)
        chips_coords.append({"x": cx, "y": cy, "w": chip_w, "h": chip_h, "idx": i})
    return chips_coords
