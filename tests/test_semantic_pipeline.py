"""
Unit Tests para el Pipeline Semántico y Motor de Audiencia (semantic/pipeline.py)
"""

import unittest
import sys
import os

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from semantic.pipeline import (
    infer_audience_from_text,
    infer_topology_from_text,
    select_optimal_archetype,
    parse_prompt_to_semantic_diagram
)


class TestSemanticPipeline(unittest.TestCase):
    
    def test_infer_audience_ceo(self):
        prompt = "Presentar al CEO y a la Junta Directiva el plan de expansion y ROI proyectado."
        aud = infer_audience_from_text(prompt)
        self.assertEqual(aud, "CEO_BOARD")
        
    def test_infer_audience_operations(self):
        prompt = "Analizar el layout de planta, cuellos de botella en fila fisica y calcular el takt time del cajero."
        aud = infer_audience_from_text(prompt)
        self.assertEqual(aud, "OPERATIONS")
        
    def test_infer_audience_devs(self):
        prompt = "Documentar los endpoints HTTP, JSON schema de la API y manejo de idempotency keys."
        aud = infer_audience_from_text(prompt)
        self.assertEqual(aud, "DEV_DOCS")
        
    def test_infer_topology_duel(self):
        prompt = "Actualmente el proceso es manual y caotico (as-is) vs la solucion propuesta automatizada."
        top = infer_topology_from_text(prompt)
        self.assertEqual(top, "DUEL_VS")
        
    def test_parse_prompt_end_to_end(self):
        prompt = "Presentar al CEO la transformacion del proceso actual caotico vs la nueva plataforma automatizada."
        diagram = parse_prompt_to_semantic_diagram(prompt)
        self.assertEqual(diagram.metadata["audience"], "CEO_BOARD")
        self.assertEqual(diagram.metadata["topology"], "DUEL_VS")
        self.assertEqual(diagram.metadata["archetype_code"], "D")
        self.assertEqual(diagram.metadata["tone"], "STRATEGIC_FINANCIAL")


if __name__ == "__main__":
    unittest.main()
