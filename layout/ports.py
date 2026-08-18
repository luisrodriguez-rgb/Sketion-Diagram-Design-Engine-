"""
Sketion Semantic Ports System (v11.0)
Define puertos magnéticos direccionales y semánticos para nodos y contenedores en diagramas.
Permite anclar conectores de forma inteligente según la posición relativa y el rol arquitectónico.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


class PortPosition(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"
    CENTER = "CENTER"


class PortDirection(Enum):
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"
    BIDIRECTIONAL = "BIDIRECTIONAL"


@dataclass
class PortSpec:
    """Especificación de un puerto de conexión magnético en una entidad gráfica."""
    name: str
    position: PortPosition
    direction: PortDirection = PortDirection.BIDIRECTIONAL
    semantic_role: str = "general"
    capacity: int = 4
    current_connections: int = 0
    offset_ratio: float = 0.5  # 0.0 (inicio) a 1.0 (fin) a lo largo del borde
    preferred_connector_type: Optional[str] = None


@dataclass
class NodeBoundary:
    """Delimitación espacial de un nodo o contenedor para cálculo de puertos y obstáculos."""
    x: float
    y: float
    w: float
    h: float
    node_id: str = ""
    label: str = ""
    role: str = "service"

    @property
    def left(self) -> float:
        return self.x

    @property
    def right(self) -> float:
        return self.x + self.w

    @property
    def top(self) -> float:
        return self.y

    @property
    def bottom(self) -> float:
        return self.y + self.h

    @property
    def center_x(self) -> float:
        return self.x + self.w * 0.5

    @property
    def center_y(self) -> float:
        return self.y + self.h * 0.5

    def get_port_coordinates(self, position: PortPosition, offset_ratio: float = 0.5) -> Tuple[float, float]:
        """Calcula la coordenada absoluta (x, y) de un puerto en el perímetro del nodo."""
        if position == PortPosition.NORTH:
            return self.x + self.w * offset_ratio, self.y
        elif position == PortPosition.SOUTH:
            return self.x + self.w * offset_ratio, self.y + self.h
        elif position == PortPosition.EAST:
            return self.x + self.w, self.y + self.h * offset_ratio
        elif position == PortPosition.WEST:
            return self.x, self.y + self.h * offset_ratio
        else:
            return self.center_x, self.center_y

    def get_closest_port(self, target_x: float, target_y: float, direction_intent: PortDirection = PortDirection.OUTBOUND) -> Tuple[PortPosition, Tuple[float, float]]:
        """Determina el puerto óptimo según la posición relativa del destino."""
        dx = target_x - self.center_x
        dy = target_y - self.center_y

        if abs(dx) >= abs(dy):
            pos = PortPosition.EAST if dx > 0 else PortPosition.WEST
        else:
            pos = PortPosition.SOUTH if dy > 0 else PortPosition.NORTH

        coords = self.get_port_coordinates(pos)
        return pos, coords


class PortManager:
    """Gestiona la asignación y resolución de puertos semánticos para cualquier topología."""

    @classmethod
    def get_standard_ports(cls, boundary: NodeBoundary, role: str = "service") -> Dict[PortPosition, PortSpec]:
        """Genera los 4 puertos estándar perimetrales adaptados al rol arquitectónico."""
        r = role.lower()
        if "database" in r or "storage" in r or "db" in r:
            # Bases de datos prefieren entrada por WEST y salida de réplicas por EAST
            return {
                PortPosition.WEST: PortSpec("db_in", PortPosition.WEST, PortDirection.INBOUND, semantic_role="data_write"),
                PortPosition.EAST: PortSpec("db_out", PortPosition.EAST, PortDirection.OUTBOUND, semantic_role="data_read"),
                PortPosition.NORTH: PortSpec("db_admin", PortPosition.NORTH, PortDirection.INBOUND, semantic_role="admin"),
                PortPosition.SOUTH: PortSpec("db_backup", PortPosition.SOUTH, PortDirection.OUTBOUND, semantic_role="backup")
            }
        elif "queue" in r or "broker" in r or "stream" in r:
            # Colas / Streams: Inbound por WEST (Produce) y Outbound por EAST (Consume)
            return {
                PortPosition.WEST: PortSpec("stream_in", PortPosition.WEST, PortDirection.INBOUND, semantic_role="produce"),
                PortPosition.EAST: PortSpec("stream_out", PortPosition.EAST, PortDirection.OUTBOUND, semantic_role="consume"),
                PortPosition.NORTH: PortSpec("stream_dlq", PortPosition.NORTH, PortDirection.OUTBOUND, semantic_role="dlq"),
                PortPosition.SOUTH: PortSpec("stream_mgmt", PortPosition.SOUTH, PortDirection.BIDIRECTIONAL, semantic_role="mgmt")
            }
        elif "actor" in r or "user" in r or "client" in r:
            # Clientes/Actores emiten peticiones por EAST y SOUTH
            return {
                PortPosition.EAST: PortSpec("client_out", PortPosition.EAST, PortDirection.OUTBOUND, semantic_role="request"),
                PortPosition.SOUTH: PortSpec("client_alt", PortPosition.SOUTH, PortDirection.OUTBOUND, semantic_role="request"),
                PortPosition.NORTH: PortSpec("client_in", PortPosition.NORTH, PortDirection.INBOUND, semantic_role="notification"),
                PortPosition.WEST: PortSpec("client_sec", PortPosition.WEST, PortDirection.BIDIRECTIONAL, semantic_role="auth")
            }
        else:
            # Servicios y componentes generales
            return {
                PortPosition.NORTH: PortSpec("srv_n", PortPosition.NORTH, PortDirection.BIDIRECTIONAL, semantic_role="general"),
                PortPosition.SOUTH: PortSpec("srv_s", PortPosition.SOUTH, PortDirection.BIDIRECTIONAL, semantic_role="general"),
                PortPosition.EAST: PortSpec("srv_e", PortPosition.EAST, PortDirection.OUTBOUND, semantic_role="general"),
                PortPosition.WEST: PortSpec("srv_w", PortPosition.WEST, PortDirection.INBOUND, semantic_role="general")
            }
