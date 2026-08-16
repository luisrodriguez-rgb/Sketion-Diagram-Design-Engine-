"""
Sketion 7.0 — Polymorphic Anchor Geometry Engine
Calcula de forma exacta el punto de intersección perimetral (Ray-Shape Boundary Intersection)
para cualquier primitiva geométrica de Excalidraw:
- Rectángulo / Tarjeta estándar (AABB Box)
- Diamante / Decisión (Manhattan Diamond)
- Círculo / Elipse / Nodo Radial (Euclidean Boundary)
- Sticky Note (Post-it perimetral)
- Contenedor / Scope Frame

Garantiza que las flechas salgan y entren exactamente en el borde físico,
sin invadir el interior del nodo ni flotar en el espacio vacío.
"""

import math
from dataclasses import dataclass
from typing import Tuple, Dict, Any, Optional


@dataclass
class Point:
    x: float
    y: float


@dataclass
class ShapeBounds:
    x: float
    y: float
    width: float
    height: float
    shape_type: str = "rectangle"  # 'rectangle', 'diamond', 'ellipse', 'sticky_note', 'frame'


class AnchorGeometryEngine:
    """Calcula puntos de anclaje magnéticos y cortes de rayo en el perímetro."""

    @classmethod
    def get_center(cls, bounds: ShapeBounds) -> Point:
        return Point(bounds.x + bounds.width / 2.0, bounds.y + bounds.height / 2.0)

    @classmethod
    def get_boundary_intersection(cls, source_bounds: ShapeBounds, target_point: Point) -> Point:
        """
        Calcula el punto de corte exacto en el perímetro de `source_bounds`
        en dirección hacia `target_point`.
        """
        center = cls.get_center(source_bounds)
        dx = target_point.x - center.x
        dy = target_point.y - center.y

        if abs(dx) < 1e-5 and abs(dy) < 1e-5:
            return center

        shape = source_bounds.shape_type.lower()

        # 1. CÍRCULO / ELIPSE (Geometría Euclidiana)
        if shape in ["ellipse", "circle"]:
            rx = source_bounds.width / 2.0
            ry = source_bounds.height / 2.0
            angle = math.atan2(dy, dx)
            return Point(
                center.x + rx * math.cos(angle),
                center.y + ry * math.sin(angle)
            )

        # 2. DIAMANTE / ROMBO (Manhattan Diamond |x/w| + |y/h| = 1)
        elif shape == "diamond":
            hw = source_bounds.width / 2.0
            hh = source_bounds.height / 2.0
            # Intersección de rayo con |x|/hw + |y|/hh = 1
            scale = 1.0 / ((abs(dx) / hw) + (abs(dy) / hh))
            return Point(center.x + dx * scale, center.y + dy * scale)

        # 3. RECTÁNGULO / STICKY NOTE / FRAME (AABB Ray-Box Clipping)
        else:
            hw = source_bounds.width / 2.0
            hh = source_bounds.height / 2.0
            
            # Factores de escala para tocar bordes verticales y horizontales
            scale_x = (hw / abs(dx)) if abs(dx) > 1e-5 else float('inf')
            scale_y = (hh / abs(dy)) if abs(dy) > 1e-5 else float('inf')
            
            scale = min(scale_x, scale_y)
            return Point(center.x + dx * scale, center.y + dy * scale)

    @classmethod
    def compute_connector_endpoints(cls, source: ShapeBounds, target: ShapeBounds) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """
        Calcula los puntos de salida (start) y llegada (end) exactos entre dos nodos.
        """
        center_source = cls.get_center(source)
        center_target = cls.get_center(target)

        # Salida de source apuntando al centro de target
        start_pt = cls.get_boundary_intersection(source, center_target)
        # Entrada en target apuntando desde el centro de source
        end_pt = cls.get_boundary_intersection(target, center_source)

        return (round(start_pt.x, 1), round(start_pt.y, 1)), (round(end_pt.x, 1), round(end_pt.y, 1))
