"""
Sketion — Unified Diagram Design Engine (Python SDK v10.0)
API unificada de alto nivel para generación autónoma de diagramas de arquitectura.

Uso rápido:
    import sketion

    # Generación directa desde especificación
    scene = sketion.render(
        payload={
            "title": "Fintech Settlement Platform",
            "layers": [
                {"name": "Adquisición", "entities": [{"label": "Cloudflare WAF", "role": "security"}]},
                {"name": "Core", "entities": [{"label": "Payment Orchestrator", "role": "service", "is_hero": True}]}
            ]
        },
        archetype="layered",
        aspect_ratio="16:9",
        output="fintech_architecture.excalidraw"
    )
"""

from typing import Dict, Any, Optional, List, Union

from visual_intelligence.visual_matrix import VisualMatrixEngine, SpatialArchetype
from visual_intelligence.visual_composition import VisualCompositionEngine, VisualEntitySpec
from visual_intelligence.brand_registry import BrandRegistry
from visual_intelligence.iconography import SemanticIconRegistry
from render.aspect_ratio import AspectRatioAdapter, AspectRatioType
from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from validation.validator import validate_scene

__version__ = "10.0.0"
__all__ = [
    "render",
    "validate",
    "ExcalidrawScene",
    "SpatialArchetype",
    "AspectRatioType",
    "BrandRegistry",
    "SemanticIconRegistry",
    "VisualCompositionEngine",
    "VisualMatrixEngine"
]


def render(payload: Dict[str, Any],
           archetype: Union[str, SpatialArchetype] = SpatialArchetype.LAYERED,
           aspect_ratio: Union[str, AspectRatioType] = AspectRatioType.WIDESCREEN_16_9,
           title: Optional[str] = None,
           output: Optional[str] = None,
           roughness: int = 0,
           bg_color: str = "#F8FAFC") -> ExcalidrawScene:
    """
    Función de renderizado principal del SDK de Sketion:
    - Resuelve el arquetipo espacial (LAYERED, PIPELINE, RADIAL_HUB, SPLIT_DUEL).
    - Ajusta la proporción geométrica (16:9, 4:3, 1:1, 3:4, AUTO).
    - Aplica reconocimiento de marcas e iconografía vectorial pura.
    - Ejecuta auto-fit dinámico sin colisiones ni espacios sobrantes.
    """
    # 1. Resolver Arquetipo
    if isinstance(archetype, str):
        arch_enum = SpatialArchetype[archetype.upper()]
    else:
        arch_enum = archetype

    # 2. Resolver Proporción
    if isinstance(aspect_ratio, str):
        ratio_str = aspect_ratio.replace(":", "_").upper()
        if "16_9" in ratio_str:
            ratio_enum = AspectRatioType.WIDESCREEN_16_9
        elif "4_3" in ratio_str:
            ratio_enum = AspectRatioType.STANDARD_4_3
        elif "1_1" in ratio_str:
            ratio_enum = AspectRatioType.SQUARE_1_1
        elif "3_4" in ratio_str or "DOC" in ratio_str or "PORTRAIT" in ratio_str:
            ratio_enum = AspectRatioType.PORTRAIT_DOCUMENT
        else:
            ratio_enum = AspectRatioType.AUTO_CONTENT
    else:
        ratio_enum = aspect_ratio

    ratio_spec = AspectRatioAdapter.get_spec(ratio_enum)
    diagram_title = title or payload.get("title", f"ARCHITECTURE DIAGRAM · {arch_enum.value}")

    # 3. Construir Escena Excalidraw
    scene = ExcalidrawScene(roughness=roughness, bg_color=bg_color)
    place_reset(max_row_w=3800, gap=140)

    fx, fy = place(ratio_spec.base_w, ratio_spec.base_h)
    VisualMatrixEngine.render_archetype(
        scene,
        archetype=arch_enum,
        title=diagram_title,
        payload=payload,
        fx=fx,
        fy=fy,
        target_w=ratio_spec.base_w,
        target_h=ratio_spec.base_h
    )

    # 4. Guardar archivo si se especifica
    if output:
        scene.save(output)

    return scene


def validate(filepath: str):
    """Valida un diagrama generado contra las métricas de calidad de Sketion."""
    return validate_scene(filepath)
