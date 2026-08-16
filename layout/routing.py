"""
Sketion Orthogonal Routing 3.0
Calculador de puntos de conexión ortogonal y carriles de retorno (Track Lanes).
"""
from typing import List, Tuple, Dict, Any, Optional

def compute_orthogonal_arrow(x1: float, y1: float, x2: float, y2: float,
                             mode: str = "auto", track_y: Optional[float] = None) -> List[List[float]]:
    """
    Calcula la secuencia de puntos relativos [[0,0], [dx1, dy1], [dx2, dy2], ...]
    para trazar una flecha ortogonal (codos a 90 grados).
    Soporta carriles de retorno superiores (Track Lanes) para flujos inversos (x2 < x1).
    """
    dx = x2 - x1
    dy = y2 - y1

    # 1. Si es un flujo de RETORNO (x2 < x1, Feedback / Response)
    if dx < -20:
        # Enrutar por carril superior reservado
        safe_track_y = track_y if track_y is not None else (min(y1, y2) - 40.0)
        up_dy = safe_track_y - y1
        total_dx = dx
        final_down_dy = dy
        return [
            [0.0, 0.0],
            [0.0, float(up_dy)],
            [float(total_dx), float(up_dy)],
            [float(total_dx), float(final_down_dy)]
        ]

    # 2. Si están prácticamente alineados horizontal o verticalmente, línea recta directa
    if abs(dx) < 5 or abs(dy) < 5:
        return [[0.0, 0.0], [float(dx), float(dy)]]

    # 3. Codo ortogonal estándar (punto medio horizontal)
    mid_dx = dx * 0.5
    points = [
        [0.0, 0.0],
        [float(mid_dx), 0.0],
        [float(mid_dx), float(dy)],
        [float(dx), float(dy)]
    ]
    return points
