"""
Sketion Grid Layouts (Matrix, Board / Kanban, Dashboard)
Calculadores de grillas tabulares proporcionales y dinámicas.
"""
from typing import List, Dict, Any, Optional
import math

def compute_matrix_layout(start_x: float, start_y: float,
                          headers: List[str], rows: List[Dict[str, Any]],
                          min_col_w: float = 180.0) -> Dict[str, Any]:
    """
    Calcula las celdas de una tabla / matriz con anchos de columna y
    alturas de fila dinámicas calculadas a partir del contenido real.
    """
    col_count = len(headers)
    row_count = len(rows)

    # 1. Extraer matriz de textos (headers + celdas)
    table_texts = [[h for h in headers]]
    for r in range(row_count):
        row_data = rows[r]
        if "values" in row_data:
            vals = row_data["values"]
        else:
            vals = [str(row_data.get(h, "")) for h in headers]
        table_texts.append([str(v) for v in vals])

    # 2. Calcular ancho proporcional por columna
    col_widths = []
    for c in range(col_count):
        max_len = max(len(table_texts[r][c]) for r in range(len(table_texts)))
        if c == col_count - 1:
            # Última columna (usualmente explicaciones largas/mecanismos): ancho generoso
            w = max(380.0, min(560.0, max_len * 6.5 + 40.0))
        elif c == 0:
            w = max(240.0, min_col_w)
        else:
            w = max(min_col_w, min(280.0, max_len * 7.5 + 35.0))
        col_widths.append(w)

    # 3. Calcular altura por fila (incluyendo cabecera)
    row_heights = [50.0]  # Cabecera
    for r in range(1, len(table_texts)):
        max_lines_in_row = 1
        for c in range(col_count):
            txt = table_texts[r][c]
            approx_chars_per_line = max(15, int(col_widths[c] / 8.5))
            lines = math.ceil(len(txt) / approx_chars_per_line)
            if lines > max_lines_in_row:
                max_lines_in_row = lines
        h = max(50.0, max_lines_in_row * 20.0 + 18.0)
        row_heights.append(h)

    # 4. Generar coordenadas exactas de celdas
    col_x_offsets = [start_x]
    for w in col_widths:
        col_x_offsets.append(col_x_offsets[-1] + w)

    row_y_offsets = [start_y]
    for h in row_heights:
        row_y_offsets.append(row_y_offsets[-1] + h)

    headers_coords = []
    for c in range(col_count):
        headers_coords.append({
            "x": col_x_offsets[c],
            "y": row_y_offsets[0],
            "w": col_widths[c],
            "h": row_heights[0],
            "col": c
        })

    rows_coords = []
    for r in range(row_count):
        row_cells = []
        for c in range(col_count):
            row_cells.append({
                "x": col_x_offsets[c],
                "y": row_y_offsets[r + 1],
                "w": col_widths[c],
                "h": row_heights[r + 1],
                "col": c,
                "row": r
            })
        rows_coords.append(row_cells)

    total_w = col_x_offsets[-1] - start_x
    total_h = row_y_offsets[-1] - start_y

    return {
        "headers": headers_coords,
        "rows": rows_coords,
        "total_w": total_w,
        "total_h": total_h,
        "col_widths": col_widths,
        "row_heights": row_heights
    }

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
                             chip_w: float = 240, chip_h: float = 110,
                             gap_x: float = 30, gap_y: float = 25) -> List[Dict[str, float]]:
    """Calcula la grilla de chips numéricos para KPIs."""
    chips_coords = []
    for i in range(metrics_count):
        col = i % cols
        row = i // cols
        cx = start_x + col * (chip_w + gap_x)
        cy = start_y + row * (chip_h + gap_y)
        chips_coords.append({"x": cx, "y": cy, "w": chip_w, "h": chip_h, "idx": i})
    return chips_coords
