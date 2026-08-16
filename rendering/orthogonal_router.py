"""
Sketion 7.0 — Collision-Aware Orthogonal Router
Calcula trayectorias ortogonales a 90 grados entre nodos evitando colisiones
con cajas intermedias y generando carriles dedicados (highways) de despeje visual.
"""

from dataclasses import dataclass
from typing import List, Tuple, Dict, Any, Optional
from rendering.anchor_geometry import Point, ShapeBounds, AnchorGeometryEngine


@dataclass
class RoutedPath:
    start_point: Tuple[float, float]
    end_point: Tuple[float, float]
    intermediate_points: List[Tuple[float, float]]  # Puntos de quiebre ortogonales [ [0,0], [dx1, dy1], [dx2, dy2] ]
    label_position: Tuple[float, float]
    has_collision_avoidance: bool = False


class OrthogonalRouterEngine:
    """Enrutador ortogonal con evasión de obstáculos y canales de paso libres."""

    @classmethod
    def route_connector(cls,
                        source: ShapeBounds,
                        target: ShapeBounds,
                        obstacles: Optional[List[ShapeBounds]] = None) -> RoutedPath:
        (sx, sy), (tx, ty) = AnchorGeometryEngine.compute_connector_endpoints(source, target)
        
        dx = tx - sx
        dy = ty - sy

        points = [[0.0, 0.0]]
        has_avoidance = False

        # Caso 1: Prácticamente alineados en horizontal o vertical
        if abs(dy) < 5:
            # Línea recta horizontal
            points.append([dx, 0.0])
            label_pos = (sx + dx / 2.0, sy - 18.0)
        elif abs(dx) < 5:
            # Línea recta vertical
            points.append([0.0, dy])
            label_pos = (sx + 15.0, sy + dy / 2.0)
        
        # Caso 2: Conexión Lado a Lado (Horizontal predominante: flujo L -> R)
        elif abs(dx) >= abs(dy):
            mid_x = dx / 2.0
            points.append([mid_x, 0.0])
            points.append([mid_x, dy])
            points.append([dx, dy])
            label_pos = (sx + mid_x, sy + dy / 2.0 - 15.0)

        # Caso 3: Conexión Vertical predominante (flujo Top -> Bottom)
        else:
            mid_y = dy / 2.0
            points.append([0.0, mid_y])
            points.append([dx, mid_y])
            points.append([dx, dy])
            label_pos = (sx + dx / 2.0 + 15.0, sy + mid_y)

        # Verificar si algún obstáculo cruza el punto medio
        if obstacles:
            for obs in obstacles:
                # Comprobar si el segmento medio colisiona con el obstáculo
                if (obs.x <= sx + dx/2.0 <= obs.x + obs.width) and (obs.y <= sy + dy/2.0 <= obs.y + obs.height):
                    has_avoidance = True
                    # Desviar el canal 40px por encima o por debajo
                    offset_y = -50.0 if dy >= 0 else 50.0
                    points = [
                        [0.0, 0.0],
                        [0.0, offset_y],
                        [dx, offset_y],
                        [dx, dy]
                    ]
                    break

        return RoutedPath(
            start_point=(sx, sy),
            end_point=(tx, ty),
            intermediate_points=points,
            label_position=label_pos,
            has_collision_avoidance=has_avoidance
        )
