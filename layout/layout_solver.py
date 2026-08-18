"""
Sketion Declarative Layout Solver (v11.0)
Motor geométrico multi-algorítmico para posicionamiento automático de nodos y contenedores.
Soporta: Hierarchical (DAG), Radial, Layered, Tree, Matrix, Timeline, Swimlane y Network Mesh.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Tuple, Union
from enum import Enum
import math

from .ports import NodeBoundary, PortPosition
from .manhattan_router import ManhattanRouter, RoutingContext, RoutedPath
from render.excalidraw_builder import ExcalidrawScene


class LayoutAlgorithm(Enum):
    HIERARCHICAL = "hierarchical"
    RADIAL = "radial"
    LAYERED = "layered"
    TREE = "tree"
    MATRIX = "matrix"
    TIMELINE = "timeline"
    SWIMLANE = "swimlane"
    NETWORK = "network"
    FREEFORM = "freeform"


@dataclass
class LayoutNode:
    """Nodo declarativo en el grafo del LayoutSolver."""
    id: str
    label: str
    role: str = "service"
    shape: str = "card"
    width: float = 240.0
    height: float = 110.0
    layer_index: int = 0
    group: Optional[str] = None
    is_hero: bool = False
    badge: Optional[str] = None
    description: str = ""
    properties: Dict[str, Any] = field(default_factory=dict)
    
    # Coordenadas resueltas por el solver
    x: float = 0.0
    y: float = 0.0

    @property
    def boundary(self) -> NodeBoundary:
        return NodeBoundary(self.x, self.y, self.width, self.height, self.id, self.label, self.role)


@dataclass
class LayoutEdge:
    """Relación o conector declarativo entre dos nodos."""
    source_id: str
    target_id: str
    relation_type: str = "sync"
    label: Optional[str] = None
    bidirectional: bool = False


class LayoutSolver:
    """Solver geométrico multi-algorítmico para diagramación técnica sin coordenadas fijas."""

    def __init__(self,
                 algorithm: Union[str, LayoutAlgorithm] = LayoutAlgorithm.HIERARCHICAL,
                 direction: str = "LR",
                 origin_x: float = 80.0,
                 origin_y: float = 100.0,
                 spacing_x: float = 120.0,
                 spacing_y: float = 90.0,
                 canvas_width: float = 1440.0,
                 canvas_height: float = 900.0):
        if isinstance(algorithm, str):
            self.algorithm = LayoutAlgorithm(algorithm.lower())
        else:
            self.algorithm = algorithm
        self.direction = direction.upper()
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.spacing_x = spacing_x
        self.spacing_y = spacing_y
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        
        self.nodes: Dict[str, LayoutNode] = {}
        self.edges: List[LayoutEdge] = []
        self.groups: Dict[str, List[str]] = {}

    def add_node(self,
                 node_id: str,
                 label: str,
                 role: str = "service",
                 shape: str = "card",
                 width: float = 240.0,
                 height: float = 110.0,
                 layer_index: int = 0,
                 group: Optional[str] = None,
                 is_hero: bool = False,
                 badge: Optional[str] = None,
                 description: str = "") -> LayoutNode:
        """Añade un nodo declarativo al solver."""
        node = LayoutNode(
            id=node_id,
            label=label,
            role=role,
            shape=shape,
            width=width,
            height=height,
            layer_index=layer_index,
            group=group,
            is_hero=is_hero,
            badge=badge,
            description=description
        )
        self.nodes[node_id] = node
        if group:
            if group not in self.groups:
                self.groups[group] = []
            self.groups[group].append(node_id)
        return node

    def connect(self, source_id: str, target_id: str, relation_type: str = "sync", label: Optional[str] = None, bidirectional: bool = False):
        """Añade una conexión entre nodos."""
        self.edges.append(LayoutEdge(source_id, target_id, relation_type, label, bidirectional))

    def solve(self):
        """Ejecuta el algoritmo de distribución espacial seleccionado."""
        if self.algorithm == LayoutAlgorithm.HIERARCHICAL or self.algorithm == LayoutAlgorithm.LAYERED:
            self._solve_hierarchical()
        elif self.algorithm == LayoutAlgorithm.RADIAL:
            self._solve_radial()
        elif self.algorithm == LayoutAlgorithm.TREE:
            self._solve_tree()
        elif self.algorithm == LayoutAlgorithm.MATRIX:
            self._solve_matrix()
        elif self.algorithm == LayoutAlgorithm.TIMELINE or self.algorithm == LayoutAlgorithm.SWIMLANE:
            self._solve_timeline()
        elif self.algorithm == LayoutAlgorithm.NETWORK:
            self._solve_network()
        else:
            self._solve_hierarchical()

    def _solve_hierarchical(self):
        """Distribución en capas ordenadas (Sugiyama DAG) horizontal o vertical."""
        # Agrupar nodos por layer_index
        layers: Dict[int, List[LayoutNode]] = {}
        for node in self.nodes.values():
            l_idx = node.layer_index
            if l_idx not in layers:
                layers[l_idx] = []
            layers[l_idx].append(node)

        sorted_layers = sorted(layers.keys())

        if self.direction == "LR":
            curr_x = self.origin_x
            for l_idx in sorted_layers:
                layer_nodes = layers[l_idx]
                max_w = max((n.width for n in layer_nodes), default=240.0)
                total_h = sum(n.height for n in layer_nodes) + (len(layer_nodes) - 1) * self.spacing_y
                start_y = max(self.origin_y, (self.canvas_height - total_h) * 0.5)

                curr_y = start_y
                for n in layer_nodes:
                    n.x = curr_x
                    n.y = curr_y
                    curr_y += n.height + self.spacing_y

                curr_x += max_w + self.spacing_x
        else:  # TB (Top to Bottom)
            curr_y = self.origin_y
            for l_idx in sorted_layers:
                layer_nodes = layers[l_idx]
                max_h = max((n.height for n in layer_nodes), default=110.0)
                total_w = sum(n.width for n in layer_nodes) + (len(layer_nodes) - 1) * self.spacing_x
                start_x = max(self.origin_x, (self.canvas_width - total_w) * 0.5)

                curr_x = start_x
                for n in layer_nodes:
                    n.x = curr_x
                    n.y = curr_y
                    curr_x += n.width + self.spacing_x

                curr_y += max_h + self.spacing_y

    def _solve_radial(self):
        """Distribución angular polar alrededor de un nodo central (Hub)."""
        node_list = list(self.nodes.values())
        if not node_list:
            return

        # El primer nodo o el marcado como hero es el centro
        center_node = next((n for n in node_list if n.is_hero), node_list[0])
        cx = self.origin_x + (self.canvas_width - self.origin_x * 2) * 0.5
        cy = self.origin_y + (self.canvas_height - self.origin_y * 2) * 0.5

        center_node.x = cx - center_node.width * 0.5
        center_node.y = cy - center_node.height * 0.5

        outer_nodes = [n for n in node_list if n.id != center_node.id]
        n_outer = len(outer_nodes)
        if n_outer == 0:
            return

        radius = min(self.canvas_width, self.canvas_height) * 0.35
        for i, n in enumerate(outer_nodes):
            angle = (i * 2.0 * math.pi / n_outer) - (math.pi / 2.0)
            nx = cx + radius * math.cos(angle) - n.width * 0.5
            ny = cy + radius * math.sin(angle) - n.height * 0.5
            n.x = nx
            n.y = ny

    def _solve_tree(self):
        """Distribución en árbol jerárquico estricto."""
        # Top-down tree
        self.direction = "TB"
        self._solve_hierarchical()

    def _solve_matrix(self):
        """Distribución en matriz de cuadrículas regulares (ej. 2x2, 3x3)."""
        node_list = list(self.nodes.values())
        n = len(node_list)
        if n == 0:
            return

        cols = 2 if n <= 4 else 3
        cell_w = (self.canvas_width - self.origin_x * 2 - (cols - 1) * self.spacing_x) / cols
        
        for i, node in enumerate(node_list):
            c = i % cols
            r = i // cols
            node.width = min(node.width, cell_w)
            node.x = self.origin_x + c * (cell_w + self.spacing_x)
            node.y = self.origin_y + r * (node.height + self.spacing_y)

    def _solve_timeline(self):
        """Distribución horizontal secuencial para líneas de tiempo y pipelines."""
        node_list = list(self.nodes.values())
        if not node_list:
            return

        curr_x = self.origin_x
        fixed_y = self.origin_y + 80.0
        for node in node_list:
            node.x = curr_x
            node.y = fixed_y
            curr_x += node.width + self.spacing_x

    def _solve_network(self):
        """Distribución basada en fuerzas simuladas para grafos densos."""
        self._solve_radial()

    def render_to_scene(self, scene: ExcalidrawScene, frame_id: Optional[str] = None) -> List[RoutedPath]:
        """
        Ejecuta el layout solver, coloca los nodos en la escena y enruta todas las conexiones
        usando el ManhattanRouter sin colisiones.
        """
        self.solve()

        # 1. Configurar contexto de enrutamiento y registrar obstáculos
        router = ManhattanRouter()
        for node in self.nodes.values():
            router.add_obstacle(node.boundary)

        # 2. Renderizar nodos según su forma declarada
        for node in self.nodes.values():
            self._render_node_shape(scene, node, frame_id)

        # 3. Enrutar y renderizar conexiones ortogonales
        routed_paths: List[RoutedPath] = []
        for edge in self.edges:
            if edge.source_id not in self.nodes or edge.target_id not in self.nodes:
                continue

            src_node = self.nodes[edge.source_id]
            tgt_node = self.nodes[edge.target_id]

            path = router.route(
                src_node.boundary,
                tgt_node.boundary,
                relation_type=edge.relation_type,
                label=edge.label
            )
            routed_paths.append(path)

            # Dibujar la ruta en la escena
            pts = path.points
            for i in range(len(pts) - 1):
                p1 = pts[i]
                p2 = pts[i+1]
                is_last_segment = (i == len(pts) - 2)
                stroke_color = "#D93829" if edge.relation_type == "critical" or src_node.is_hero else "#0F172A"
                stroke_w = 2.0 if edge.relation_type == "critical" else 1.5

                if is_last_segment:
                    # Flecha en el segmento final
                    scene.add_arrow(p1[0], p1[1], p2[0], p2[1], stroke=stroke_color, stroke_w=stroke_w, frame_id=frame_id)
                else:
                    # Segmento de línea intermedio
                    scene.add_line(p1[0], p1[1], p2[0], p2[1], stroke=stroke_color, stroke_w=stroke_w, frame_id=frame_id)

            # Dibujar pastilla de etiqueta si existe
            if path.label and path.label_point:
                lx, ly = path.label_point
                label_w = min(160.0, max(60.0, len(path.label) * 8.0 + 20.0))
                scene.add_rect(lx - label_w * 0.5, ly - 12.0, label_w, 24.0, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=frame_id)
                scene.add_text(lx - label_w * 0.5 + 8.0, ly - 7.0, path.label, font_size=9, font_family=3, color="#475569", frame_id=frame_id)

        return routed_paths

    def _render_node_shape(self, scene: ExcalidrawScene, node: LayoutNode, frame_id: Optional[str]):
        """Renderiza la forma geométrica adecuada según el tipo de nodo."""
        s = node.shape.lower()
        if s == "database" or "db" in s:
            scene.add_database_cylinder(node.x, node.y, node.width, node.height, node.label, node.description, frame_id=frame_id)
        elif s == "queue" or s == "pipe" or "stream" in s:
            scene.add_streaming_pipe(node.x, node.y, node.width, node.height, node.label, [node.description] if node.description else [], is_hero=node.is_hero, frame_id=frame_id)
        elif s == "actor" or s == "user":
            scene.add_actor_node(node.x, node.y, node.width, node.height, node.label, node.description, frame_id=frame_id)
        elif s == "security" or s == "waf":
            scene.add_security_barrier(node.x, node.y, node.width, node.height, node.label, [node.description] if node.description else [], badge=node.badge or "SECURITY", frame_id=frame_id)
        else:
            # Card estándar o hero
            scene.add_quad_card(
                node.x, node.y, node.width, node.height,
                node.label, node.description,
                badge=node.badge or node.role.upper(),
                is_hero=node.is_hero,
                frame_id=frame_id
            )
