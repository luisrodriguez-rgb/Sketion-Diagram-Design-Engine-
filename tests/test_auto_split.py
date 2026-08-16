"""
Unit Tests para el Motor de Auto-Split Elástico (layout/auto_split.py)
"""

import unittest
import sys
import os

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from layout.auto_split import (
    should_auto_split,
    partition_entities_by_perspective,
    compute_multi_frame_placements
)


class TestAutoSplit(unittest.TestCase):
    
    def test_should_auto_split_thresholds(self):
        self.assertFalse(should_auto_split(nodes_count=8, edges_count=7, estimated_density=3.5))
        self.assertTrue(should_auto_split(nodes_count=20, edges_count=10, estimated_density=4.0))
        self.assertTrue(should_auto_split(nodes_count=12, edges_count=25, estimated_density=4.0))
        self.assertTrue(should_auto_split(nodes_count=8, edges_count=8, estimated_density=6.2))
        
    def test_partition_entities(self):
        entities = [
            {"name": "API Gateway", "category": "Ingress"},
            {"name": "Order Service", "category": "Core Service"},
            {"name": "Paso 1: Checkout", "category": "Secuencia / Flujo"},
            {"name": "Politica de Permisos", "category": "Matriz SLA"},
            {"name": "Throughput 50k", "category": "KPI Rendimiento"}
        ]
        partitions = partition_entities_by_perspective(entities)
        self.assertEqual(len(partitions["TOPOLOGY"]), 2)
        self.assertEqual(len(partitions["LIFECYCLE_FLOW"]), 1)
        self.assertEqual(len(partitions["GOVERNANCE"]), 1)
        self.assertEqual(len(partitions["METRICS"]), 1)
        
    def test_compute_multi_frame_placements(self):
        keys = ["TOPOLOGY", "LIFECYCLE_FLOW", "GOVERNANCE", "METRICS"]
        placements = compute_multi_frame_placements(keys, base_width=2800.0, base_height=850.0, gap_y=100.0)
        self.assertEqual(len(placements), 4)
        self.assertEqual(placements[0]["y"], 0.0)
        self.assertGreater(placements[1]["y"], placements[0]["y"])
        self.assertGreater(placements[2]["y"], placements[1]["y"])
        self.assertGreater(placements[3]["y"], placements[2]["y"])


if __name__ == "__main__":
    unittest.main()
