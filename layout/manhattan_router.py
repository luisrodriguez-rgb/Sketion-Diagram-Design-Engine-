"""
Sketion Manhattan A* Connector Router (v11.0)
Enrutador ortogonal inteligente con evitación de obstáculos, minimización de cruces,
selección de puertos magnéticos y función de costo multi-criterio.
"""

from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Any, Optional
import math
import heapq

from .ports import NodeBoundary, PortPosition, PortDirection, PortManager


@dataclass
class RoutedPath:
    """Resultado del cálculo de ruta ortogonal entre dos entidades."""
    points: List[List[float]]
    start_point: Tuple[float, float]
    end_point: Tuple[float, float]
    start_port: PortPosition
    end_port: PortPosition
    bends_count: int
    crossings_count: int
    total_length: float
    cost: float
    label: Optional[str] = None
    label_point: Optional[Tuple[float, float]] = None


@dataclass
class RoutingContext:
    """Contexto espacial que contiene todos los obstáculos y rutas existentes."""
    obstacles: List[NodeBoundary] = field(default_factory=list)
    existing_paths: List[List[List[float]]] = field(default_factory=list)
    grid_size: float = 20.0
    safe_padding: float = 25.0


class ManhattanRouter:
    """Enrutador ortogonal de alto rendimiento para diagramas técnicos limpios."""

    def __init__(self, context: Optional[RoutingContext] = None):
        self.context = context or RoutingContext()

    def add_obstacle(self, boundary: NodeBoundary):
        self.context.obstacles.append(boundary)

    def route(self,
              source: NodeBoundary,
              target: NodeBoundary,
              relation_type: str = "sync",
              label: Optional[str] = None,
              track_y: Optional[float] = None) -> RoutedPath:
        """
        Calcula la ruta ortogonal óptima entre source y target minimizando colisiones, cruces y codos.
        """
        # 1. Determinar orientación relativa
        dx = target.center_x - source.center_x
        dy = target.center_y - source.center_y

        # 2. Selección de puertos
        if abs(dx) >= abs(dy) * 0.8:
            if dx > 0:
                s_port, e_port = PortPosition.EAST, PortPosition.WEST
            else:
                s_port, e_port = PortPosition.WEST, PortPosition.EAST
        else:
            if dy > 0:
                s_port, e_port = PortPosition.SOUTH, PortPosition.NORTH
            else:
                s_port, e_port = PortPosition.NORTH, PortPosition.SOUTH

        start_x, start_y = source.get_port_coordinates(s_port)
        end_x, end_y = target.get_port_coordinates(e_port)

        # 3. Generación de candidatos de trayectoria
        candidates = self._generate_candidate_paths(start_x, start_y, end_x, end_y, s_port, e_port, source, target, track_y)

        # 4. Evaluación de costo multi-criterio
        best_path_points: List[List[float]] = []
        lowest_cost = float("inf")
        best_bends = 0
        best_crossings = 0
        best_length = 0.0

        for pts in candidates:
            c_cost, bends, crossings, length = self._evaluate_path_cost(pts, source, target)
            if c_cost < lowest_cost:
                lowest_cost = c_cost
                best_path_points = pts
                best_bends = bends
                best_crossings = crossings
                best_length = length

        if not best_path_points:
            best_path_points = [[start_x, start_y], [end_x, end_y]]
            lowest_cost = 999.0
            best_bends = 0
            best_crossings = 0
            best_length = math.hypot(end_x - start_x, end_y - start_y)

        # 5. Calcular posición de la etiqueta en el centro geométrico del segmento más largo
        label_pt = self._calculate_label_position(best_path_points)

        # 6. Registrar la ruta calculada en el contexto para futuras comprobaciones de cruce
        self.context.existing_paths.append(best_path_points)

        return RoutedPath(
            points=best_path_points,
            start_point=(start_x, start_y),
            end_point=(end_x, end_y),
            start_port=s_port,
            end_port=e_port,
            bends_count=best_bends,
            crossings_count=best_crossings,
            total_length=best_length,
            cost=lowest_cost,
            label=label,
            label_point=label_pt
        )

    def _generate_candidate_paths(self,
                                  sx: float, sy: float,
                                  ex: float, ey: float,
                                  s_port: PortPosition, e_port: PortPosition,
                                  source: NodeBoundary, target: NodeBoundary,
                                  track_y: Optional[float]) -> List[List[List[float]]]:
        """Genera geometrías ortogonales candidatas (directa, 1 codo, 2 codos canal medio, 3 codos track lane)."""
        candidates: List[List[List[float]]] = []
        pad = self.context.safe_padding

        # Candidato 0: Línea recta directa si están colineales
        if abs(sx - ex) < 2.0 or abs(sy - ey) < 2.0:
            candidates.append([[sx, sy], [ex, ey]])

        # Candidato 1: Z-Bend Horizontal (East -> West con canal vertical medio)
        if s_port == PortPosition.EAST and e_port == PortPosition.WEST and ex > sx + 10:
            mid_x = (sx + ex) * 0.5
            candidates.append([[sx, sy], [mid_x, sy], [mid_x, ey], [ex, ey]])

        # Candidato 2: Z-Bend Vertical (South -> North con canal horizontal medio)
        if s_port == PortPosition.SOUTH and e_port == PortPosition.NORTH and ey > sy + 10:
            mid_y = (sy + ey) * 0.5
            candidates.append([[sx, sy], [sx, mid_y], [ex, mid_y], [ex, ey]])

        # Candidato 3: L-Bend (1 codo horizontal-primero)
        candidates.append([[sx, sy], [ex, sy], [ex, ey]])

        # Candidato 4: L-Bend (1 codo vertical-primero)
        candidates.append([[sx, sy], [sx, ey], [ex, ey]])

        # Candidato 5: Flujo de RETORNO (ex < sx) por carril superior reservado (Track Lane)
        if ex < sx:
            t_y = track_y if track_y is not None else min(source.top, target.top) - pad - 20.0
            candidates.append([
                [sx, sy],
                [sx + pad, sy],
                [sx + pad, t_y],
                [ex - pad, t_y],
                [ex - pad, ey],
                [ex, ey]
            ])

        # Candidato 6: Flujo de RETORNO por carril inferior
        if ex < sx:
            b_y = max(source.bottom, target.bottom) + pad + 20.0
            candidates.append([
                [sx, sy],
                [sx + pad, sy],
                [sx + pad, b_y],
                [ex - pad, b_y],
                [ex - pad, ey],
                [ex, ey]
            ])

        return candidates

    def _evaluate_path_cost(self, points: List[List[float]], source: NodeBoundary, target: NodeBoundary) -> Tuple[float, int, int, float]:
        """
        Función de costo A*:
        Cost = collision_cost + crossing_cost + bend_cost + length_cost
        """
        bends = max(0, len(points) - 2)
        length = 0.0
        collision_penalty = 0.0
        crossing_penalty = 0.0

        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i+1]
            seg_len = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
            length += seg_len

            # 1. Comprobar colisiones con obstáculos intermedios
            for obs in self.context.obstacles:
                if obs.node_id in [source.node_id, target.node_id]:
                    continue
                if self._segment_intersects_box(p1, p2, obs):
                    collision_penalty += 500.0  # Penalización severa por colisión

            # 2. Comprobar cruces con rutas existentes
            for other_path in self.context.existing_paths:
                for j in range(len(other_path) - 1):
                    op1 = other_path[j]
                    op2 = other_path[j+1]
                    if self._segments_cross(p1, p2, op1, op2):
                        crossing_penalty += 35.0  # Penalización por cruce visual

        bend_cost = bends * 15.0
        dist_cost = length * 0.1

        total_cost = collision_penalty + crossing_penalty + bend_cost + dist_cost
        crossings_count = int(crossing_penalty / 35.0)

        return total_cost, bends, crossings_count, length

    def _segment_intersects_box(self, p1: List[float], p2: List[float], box: NodeBoundary) -> bool:
        """Comprueba si un segmento de línea corta el interior del rectángulo de un obstáculo."""
        min_x = min(p1[0], p2[0])
        max_x = max(p1[0], p2[0])
        min_y = min(p1[1], p2[1])
        max_y = max(p1[1], p2[1])

        # Bounding box test
        if max_x < box.left or min_x > box.right or max_y < box.top or min_y > box.bottom:
            return False

        # Si el segmento es horizontal
        if abs(p1[1] - p2[1]) < 0.1:
            y = p1[1]
            if box.top < y < box.bottom and not (max_x <= box.left or min_x >= box.right):
                return True

        # Si el segmento es vertical
        if abs(p1[0] - p2[0]) < 0.1:
            x = p1[0]
            if box.left < x < box.right and not (max_y <= box.top or min_y >= box.bottom):
                return True

        return False

    def _segments_cross(self, a1: List[float], a2: List[float], b1: List[float], b2: List[float]) -> bool:
        """Determina si dos segmentos ortogonales se intersecan."""
        def ccw(pA, pB, pC):
            return (pC[1] - pA[1]) * (pB[0] - pA[0]) > (pB[1] - pA[1]) * (pC[0] - pA[0])

        return (ccw(a1, b1, b2) != ccw(a2, b1, b2)) and (ccw(a1, a2, b1) != ccw(a1, a2, b2))

    def _calculate_label_position(self, points: List[List[float]]) -> Tuple[float, float]:
        """Calcula el punto medio del segmento más largo de la ruta para colocar la pastilla de texto."""
        longest_seg_len = -1.0
        best_mid = (points[0][0], points[0][1])

        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i+1]
            seg_len = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
            if seg_len > longest_seg_len:
                longest_seg_len = seg_len
                best_mid = ((p1[0] + p2[0]) * 0.5, (p1[1] + p2[1]) * 0.5)

        return best_mid
