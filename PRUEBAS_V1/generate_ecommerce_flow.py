"""
Script de generación del proceso de compra de e-commerce usando Sketion Engine
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

    title = "Proceso de Compra E-Commerce"
    
    # 1. Definición semántica de los pasos
    steps = [
        {
            "step_num": "01",
            "label": "Catálogo y Carrito\nSelección de Productos",
            "is_hero": False,
            "edge_label": "Checkout"
        },
        {
            "step_num": "02",
            "label": "Datos de Envío\nDirección y Flete",
            "is_hero": False,
            "edge_label": "Pagar"
        },
        {
            "step_num": "03",
            "label": "Pasarela de Pago\nStripe / Tarjeta",
            "is_hero": True,  # 1 solo nodo con color de acento
            "edge_label": "Aprobado 200"
        },
        {
            "step_num": "04",
            "label": "Confirmación\nOrden y Factura",
            "is_hero": False,
            "edge_label": "Almacén"
        },
        {
            "step_num": "05",
            "label": "Despacho y Tracking\nEnvío por Courier",
            "is_hero": False
        }
    ]

    # 2. Render con motor FLUJO
    engine_flujo(scene, title, steps, palette=DEFAULT_PALETTE, wave=False, w=1500, h=450)

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

    output_path = os.path.join(workspace_dir, "proceso_compra_tienda.excalidraw")
    scene.save(output_path)
    print(f"\nArchivo guardado con éxito en: {output_path}")

if __name__ == "__main__":
    generate()
