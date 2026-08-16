"""
Sketion Stress Testing Suite
Somete el motor a casos difíciles: arquitecturas densas, nombres largos, sobrecarga de acentos y scopes múltiples.
Verifica:
1. Hard Failures
2. Visual Quality Score (Densidad calibrada Target 4.0/10)
3. Semantic Fidelity Score (Cobertura de nodos y relaciones)
4. Sketion Unified Score
5. Repair Budget (Máximo 3 iteraciones)
"""

import os
import sys
import json

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from semantic.models import SemanticDiagram, SemanticNode, SemanticEdge, Scope, DetailLevel, OutputPreset
from render.excalidraw_builder import ExcalidrawScene, place_reset
from engines.recipes import engine_red, engine_flujo, DEFAULT_PALETTE
from validation.validator import validate_scene

STRESS_DIR = os.path.join(workspace_dir, "tests", "fixtures", "stress")

def parse_semantic_diagram(data: dict) -> SemanticDiagram:
    """Convierte un JSON de fixture en un SemanticDiagram fuertemente tipado."""
    nodes = [
        SemanticNode(
            id=n["id"],
            label=n["label"],
            sublabel=n.get("sublabel"),
            metadata=n.get("metadata"),
            role=n.get("role", "core"),
            is_hero=n.get("is_hero", False)
        ) for n in data.get("nodes", [])
    ]
    edges = [
        SemanticEdge(
            from_node=e["from"],
            to_node=e["to"],
            label=e.get("label")
        ) for e in data.get("edges", [])
    ]
    scopes = [
        Scope(
            id=s["id"],
            label=s["label"],
            role=s.get("role", "internal")
        ) for s in data.get("scopes", [])
    ]
    return SemanticDiagram(
        title=data["title"],
        semantic_type=data.get("semantic_type", "architecture"),
        detail_level=DetailLevel(data.get("detail_level", "balanced")),
        output_preset=OutputPreset(data.get("output_preset", "docs")),
        engine=data.get("engine", "red"),
        nodes=nodes,
        edges=edges,
        scopes=scopes
    )

def test_stress_cases():
    print("==================================================")
    print("INICIANDO SUITE DE STRESS TESTING DE SKETION")
    print("==================================================\n")

    # 1. Caso 1: Arquitectura Densa (11 nodos + 3 scopes + 9 edges)
    p1 = os.path.join(STRESS_DIR, "01_dense_architecture.json")
    with open(p1, "r", encoding="utf-8") as f:
        d1 = json.load(f)

    place_reset()
    scene1 = ExcalidrawScene(roughness=0, bg_color="#ffffff")
    engine_red(scene1, d1["title"], d1["nodes"], d1["edges"], scopes=d1.get("scopes"),
               palette=DEFAULT_PALETTE, w=1400, h=720)
    sem_diagram1 = parse_semantic_diagram(d1)
    scene_data1, report1 = validate_scene(scene1.to_dict(), diagram=sem_diagram1)
    print(report1.summary())
    assert report1.is_valid, f"Caso 1 falló: {report1.errors}"
    assert report1.sketion_overall_score >= 85, f"Score insuficiente: {report1.sketion_overall_score}"

    # 2. Caso 2: Nombres Técnicos Extensos
    p2 = os.path.join(STRESS_DIR, "02_long_labels.json")
    with open(p2, "r", encoding="utf-8") as f:
        d2 = json.load(f)

    place_reset()
    scene2 = ExcalidrawScene(roughness=0, bg_color="#ffffff")
    engine_flujo(scene2, d2["title"], d2["steps"], palette=DEFAULT_PALETTE, w=1500, h=500)
    scene_data2, report2 = validate_scene(scene2.to_dict())
    print("\n" + report2.summary())
    assert report2.is_valid, f"Caso 2 falló: {report2.errors}"
    assert report2.sketion_overall_score >= 85

    # 3. Caso 3: Sobrecarga de Acentos (5 acentos iniciales -> Auto-Repair debe degradar 3)
    p3 = os.path.join(STRESS_DIR, "06_many_accent_candidates.json")
    with open(p3, "r", encoding="utf-8") as f:
        d3 = json.load(f)

    place_reset()
    scene3 = ExcalidrawScene(roughness=0, bg_color="#ffffff")
    engine_red(scene3, d3["title"], d3["nodes"], d3["edges"], palette=DEFAULT_PALETTE)
    sem_diagram3 = parse_semantic_diagram(d3)
    scene_data3, report3 = validate_scene(scene3.to_dict(), diagram=sem_diagram3, auto_repair=True)
    print("\n" + report3.summary())
    assert report3.is_valid
    assert len(report3.repairs_applied) > 0, "Auto-Repair debió degradar los acentos excedentes"
    assert report3.visual_metrics.accent_count <= 2, "La escena reparada debe tener máximo 2 acentos"

    print("\n🎉 TODOS LOS CASOS DE STRESS TESTING PASARON CON ÉXITO Y AUTO-CORRECCIÓN VERIFICADA!")

if __name__ == "__main__":
    test_stress_cases()
