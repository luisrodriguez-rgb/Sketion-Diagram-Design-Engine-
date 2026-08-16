"""
Sketion Full Pipeline End-to-End Test (Semantic -> Layout -> Render -> Validator)
"""
import os
import sys
import json

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from semantic.models import SemanticDiagram, SemanticNode, SemanticEdge, DetailLevel
from render.excalidraw_builder import ExcalidrawScene, place_reset
from engines.recipes import engine_red, engine_flujo, engine_dashboard, DEFAULT_PALETTE
from validation.validator import validate_scene

def test_pipeline():
    print("Testing Sketion 4-Layer Architecture Pipeline...")
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color="#ffffff")

    # 1. Semantic Model Creation
    diagram = SemanticDiagram(
        title="Plataforma SaaS de E-Commerce",
        semantic_type="architecture",
        detail_level=DetailLevel.BALANCED,
        engine="red",
        nodes=[
            SemanticNode(id="cdn", label="Cloudflare CDN", role="entrypoint"),
            SemanticNode(id="api", label="API Gateway (FastAPI)", role="core", is_hero=True),
            SemanticNode(id="auth", label="Auth Service (JWT)", role="core"),
            SemanticNode(id="db", label="PostgreSQL Primary", role="storage"),
            SemanticNode(id="cache", label="Redis Cache", role="storage")
        ],
        edges=[
            SemanticEdge(from_node="cdn", to_node="api", label="HTTPS / JSON"),
            SemanticEdge(from_node="api", to_node="auth", label="Verify"),
            SemanticEdge(from_node="api", to_node="db", label="SQL Read/Write"),
            SemanticEdge(from_node="api", to_node="cache", label="Session Cache")
        ]
    )

    # 2. Render through Engine Recipes (using Layout & Routing)
    engine_red(scene, diagram.title, [
        {"id": "cdn", "label": "Cloudflare CDN", "rel_x": 50, "rel_y": 150, "is_hero": False},
        {"id": "api", "label": "API Gateway (FastAPI)", "rel_x": 350, "rel_y": 150, "is_hero": True},
        {"id": "auth", "label": "Auth Service (JWT)", "rel_x": 350, "rel_y": 280, "is_hero": False},
        {"id": "db", "label": "PostgreSQL Primary", "rel_x": 700, "rel_y": 100, "is_hero": False},
        {"id": "cache", "label": "Redis Cache", "rel_x": 700, "rel_y": 240, "is_hero": False}
    ], [
        {"from": "cdn", "to": "api", "label": "HTTPS / JSON"},
        {"from": "api", "to": "auth", "label": "Verify"},
        {"from": "api", "to": "db", "label": "SQL Read/Write"},
        {"from": "api", "to": "cache", "label": "Session Cache"}
    ], palette=DEFAULT_PALETTE)

    # 3. Quality Validation Check
    scene_dict = scene.to_dict()
    report = validate_scene(scene_dict)
    print(report.summary())

    assert report.is_valid, f"Validation failed with errors: {report.errors}"
    assert len(report.errors) == 0

    output_path = "/Users/leonfeliperodriguez/.gemini/antigravity-ide/brain/4aecd325-b837-4fa5-a126-056e3c810c01/scratch/pipeline_test.excalidraw"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    scene.save(output_path)
    print(f"\nSUCCESS: Pipeline test complete. Generated {output_path}")

if __name__ == "__main__":
    test_pipeline()
