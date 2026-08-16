"""
Script para generar el diagrama del Ciclo de Vida de un Producto SaaS usando Sketion Engine
"""
import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset
from engines.recipes import engine_flujo, DEFAULT_PALETTE
from semantic.models import SemanticDiagram, SemanticFlowStep, DetailLevel, OutputPreset
from validation.validator import validate_scene

def generate():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color="#ffffff")

    title = "Ciclo de Vida de un Producto SaaS"

    # 1. Definición semántica de las 5 etapas clave
    steps = [
        {
            "step_num": "01",
            "label": "Ideación y Discovery\nValidación de Problema",
            "is_hero": False,
            "edge_label": "Validar PMF"
        },
        {
            "step_num": "02",
            "label": "MVP y Beta Privada\nCore Features & Feedback",
            "is_hero": False,
            "edge_label": "Lanzamiento"
        },
        {
            "step_num": "03",
            "label": "Product-Market Fit\nTracción y Retención",
            "is_hero": True,  # Nodo Héroe: El hito crítico de cualquier SaaS
            "edge_label": "Escalar PLG"
        },
        {
            "step_num": "04",
            "label": "Crecimiento y Escala\nAdquisición & Expansión",
            "is_hero": False,
            "edge_label": "Madurez"
        },
        {
            "step_num": "05",
            "label": "Madurez y Evolución\nLTV Máximo & Enterprise",
            "is_hero": False
        }
    ]

    # 2. Render con motor FLUJO estructurado
    engine_flujo(scene, title, steps, palette=DEFAULT_PALETTE, wave=False, w=1550, h=480)

    # 3. Validación y Quality Score
    sem_diagram = SemanticDiagram(
        title=title,
        semantic_type="flowchart",
        detail_level=DetailLevel.BALANCED,
        output_preset=OutputPreset.DOCS,
        engine="flujo",
        steps=[
            SemanticFlowStep(step_num=s["step_num"], label=s["label"], is_hero=s.get("is_hero", False))
            for s in steps
        ]
    )

    scene_data, report = validate_scene(scene.to_dict(), diagram=sem_diagram, auto_repair=True)
    print(report.summary())

    output_path = os.path.join(workspace_dir, "ciclo_vida_producto_saas.excalidraw")
    scene.save(output_path)
    print(f"\nArchivo guardado con éxito en: {output_path}")

if __name__ == "__main__":
    generate()
