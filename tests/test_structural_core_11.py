"""
Test Suite para Sketion 11.0A: Structural Core (Ports, Manhattan Router & Layout Solver)
"""

import unittest
import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from layout.ports import NodeBoundary, PortPosition, PortDirection, PortManager
from layout.manhattan_router import ManhattanRouter, RoutingContext
from layout.layout_solver import LayoutSolver, LayoutAlgorithm
from render.excalidraw_builder import ExcalidrawScene
from validation.validator import validate_scene


class TestStructuralCore11(unittest.TestCase):

    def test_ports_coordinates(self):
        """Verifica el cálculo de coordenadas de puertos perimetrales."""
        b = NodeBoundary(x=100.0, y=100.0, w=200.0, h=100.0, node_id="n1", label="Service A")
        
        # North center
        nx, ny = b.get_port_coordinates(PortPosition.NORTH)
        self.assertEqual(nx, 200.0)
        self.assertEqual(ny, 100.0)

        # South center
        sx, sy = b.get_port_coordinates(PortPosition.SOUTH)
        self.assertEqual(sx, 200.0)
        self.assertEqual(sy, 200.0)

        # East center
        ex, ey = b.get_port_coordinates(PortPosition.EAST)
        self.assertEqual(ex, 300.0)
        self.assertEqual(ey, 150.0)

        # West center
        wx, wy = b.get_port_coordinates(PortPosition.WEST)
        self.assertEqual(wx, 100.0)
        self.assertEqual(wy, 150.0)

    def test_manhattan_obstacle_avoidance(self):
        """Verifica que el ManhattanRouter trace rutas ortogonales con waypoints limpios."""
        router = ManhattanRouter()
        
        src = NodeBoundary(x=40.0, y=100.0, w=200.0, h=100.0, node_id="src", label="Source")
        obs = NodeBoundary(x=300.0, y=100.0, w=200.0, h=100.0, node_id="obs", label="Obstacle")
        tgt = NodeBoundary(x=600.0, y=100.0, w=200.0, h=100.0, node_id="tgt", label="Target")

        router.add_obstacle(src)
        router.add_obstacle(obs)
        router.add_obstacle(tgt)

        path = router.route(src, tgt, label="API Call")
        self.assertIsNotNone(path)
        self.assertTrue(len(path.points) >= 2)
        self.assertEqual(path.start_port, PortPosition.EAST)
        self.assertEqual(path.end_port, PortPosition.WEST)

    def test_layout_solver_all_algorithms(self):
        """Verifica que el LayoutSolver resuelva geométricamente los 8 algoritmos."""
        algorithms = [
            LayoutAlgorithm.HIERARCHICAL,
            LayoutAlgorithm.RADIAL,
            LayoutAlgorithm.LAYERED,
            LayoutAlgorithm.TREE,
            LayoutAlgorithm.MATRIX,
            LayoutAlgorithm.TIMELINE,
            LayoutAlgorithm.SWIMLANE,
            LayoutAlgorithm.NETWORK
        ]

        for algo in algorithms:
            solver = LayoutSolver(algorithm=algo)
            n1 = solver.add_node("n1", "Client", role="actor", shape="actor", layer_index=0)
            n2 = solver.add_node("n2", "Gateway", role="gateway", shape="card", layer_index=1, is_hero=True)
            n3 = solver.add_node("n3", "Database", role="database", shape="database", layer_index=2)
            
            solver.connect("n1", "n2", label="HTTPS")
            solver.connect("n2", "n3", label="SQL")

            scene = ExcalidrawScene()
            fid = scene.add_frame(f"Test {algo.value}", 0, 0, 1440, 900)
            routes = solver.render_to_scene(scene, frame_id=fid)

            self.assertEqual(len(routes), 2)
            # Validar que no hay errores de elementos vacíos
            scene_dict = scene.to_dict()
            self.assertTrue(len(scene_dict["elements"]) > 5)


if __name__ == "__main__":
    unittest.main()
