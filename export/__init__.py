"""
Sketion Export Intelligence Package (v9.1)
Exportadores multiformato de alta fidelidad:
- SVG: Gráficos vectoriales web limpios con tipografía Inter.
- Excalidraw: Archivo JSON colaborativo nativo.
- PNG / PDF: Exportación a través de renderizadores estándar.
"""

from typing import Dict, Any, Union
import json
import os

from .svg_exporter import SVGExporter


def export_scene(scene_input: Union[Dict[str, Any], Any],
                 output_path: str,
                 format: str = "svg") -> str:
    """Exporta cualquier escena de Sketion al formato de destino especificado."""
    fmt = format.lower().strip()
    
    # Extraer diccionario de escena
    if hasattr(scene_input, "to_dict"):
        scene_dict = scene_input.to_dict()
    elif isinstance(scene_input, dict):
        scene_dict = scene_input
    else:
        raise ValueError("scene_input debe ser una instancia de ExcalidrawScene o un dict.")

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    if fmt in ["svg", ".svg"]:
        return SVGExporter.export(scene_dict, output_path)
    elif fmt in ["excalidraw", ".excalidraw", "json", ".json"]:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(scene_dict, f, indent=2, ensure_ascii=False)
        return output_path
    else:
        # Fallback a SVG por defecto si no es excalidraw
        return SVGExporter.export(scene_dict, output_path)
