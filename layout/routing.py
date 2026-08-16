"""
Sketion Orthogonal Routing
Calculador de puntos de conexión ortogonal (codos a 90 grados).
"""
from typing import List, Tuple, Dict, Any

def compute_orthogonal_arrow(x1: float, y1: float, x2: float, y2: float,
                             mode: str = "auto") -> List[List[float]]:
    """
    Calcula la secuencia de puntos relativos [[0,0], [dx1, dy1], [dx2, dy2], ...]
    para trazar una flecha ortogonal (codos a 90 grados).
    """
    dx = x2 - x1
    dy = y2 - y1

    # Si están prácticamente alineados horizontal o verticalmente, línea recta directa
    if abs(dx) < 5 or abs(dy) < 5:
        return [[0.0, 0.0], [float(dx), float(dy)]]

    # Codo ortogonal estándar (punto medio horizontal)
    mid_dx = dx * 0.5
    points = [
        [0.0, 0.0],
        [float(mid_dx), 0.0],
        [float(mid_dx), float(dy)],
        [float(dx), float(dy)]
    ]
    return points
