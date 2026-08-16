"""
Sketion — Unified Diagram Design Engine (Production SDK v10.0 GA)
API unificada de nivel de producto para generación autónoma de diagramas de arquitectura.

Uso rápido:
    import sketion

    # 1. Renderizar con inteligencia autónoma
    result = sketion.render(
        payload={
            "title": "Fintech Settlement Platform",
            "layers": [
                {"name": "Adquisición", "entities": [{"label": "Cloudflare WAF", "role": "security"}]},
                {"name": "Core", "entities": [{"label": "Payment Orchestrator", "role": "service", "is_hero": True}]}
            ]
        },
        audience="engineer",
        archetype="layered",
        aspect_ratio="16:9"
    )

    # 2. Explicabilidad y métricas
    print(result.explain())

    # 3. Exportación multiformato
    result.export("diagram.excalidraw")
    result.export("diagram.svg", format="svg")
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, List, Union
import os

from visual_intelligence.visual_matrix import VisualMatrixEngine, SpatialArchetype
from visual_intelligence.visual_composition import VisualCompositionEngine, VisualEntitySpec
from visual_intelligence.brand_registry import BrandRegistry
from visual_intelligence.iconography import SemanticIconRegistry
from visual_intelligence.visual_language import VisualLanguageEngine, VisualLanguageDialect
from render.aspect_ratio import AspectRatioAdapter, AspectRatioType
from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from design.consistency import VisualConsistencyEngine, ConsistencyReport
from validation.validator import validate_scene
from export import export_scene
from .explainability import DesignDecisionTrace

__version__ = "10.0.0"
__all__ = [
    "render",
    "validate",
    "export",
    "SketionResult",
    "ExcalidrawScene",
    "SpatialArchetype",
    "AspectRatioType",
    "VisualLanguageDialect",
    "BrandRegistry",
    "SemanticIconRegistry",
    "VisualCompositionEngine",
    "VisualMatrixEngine",
    "DesignDecisionTrace"
]


@dataclass
class SketionResult:
    """Objeto de resultado estructurado del motor de Sketion."""
    scene: ExcalidrawScene
    title: str
    trace: DesignDecisionTrace
    consistency: ConsistencyReport
    output_path: Optional[str] = None

    @property
    def vcs_score(self) -> float:
        return self.consistency.vcs_score

    def to_dict(self) -> Dict[str, Any]:
        return self.scene.to_dict()

    def explain(self) -> str:
        """Devuelve el reporte estructurado de explicabilidad de decisiones de diseño."""
        return self.trace.to_markdown()

    def export(self, path: str, format: str = "auto") -> str:
        """Exporta el diagrama a .excalidraw o .svg."""
        if format == "auto":
            ext = os.path.splitext(path)[1].lower()
            fmt = "svg" if ext == ".svg" else "excalidraw"
        else:
            fmt = format
        return export_scene(self.scene, path, format=fmt)


def render(payload: Dict[str, Any],
           archetype: Union[str, SpatialArchetype] = "auto",
           aspect_ratio: Union[str, AspectRatioType] = AspectRatioType.WIDESCREEN_16_9,
           audience: str = "engineer",
           title: Optional[str] = None,
           output: Optional[str] = None,
           roughness: int = 0,
           bg_color: Optional[str] = None) -> SketionResult:
    """
    Función de renderizado principal del SDK de Sketion v10.0:
    - Resuelve autónomamente el arquetipo espacial si es 'auto'.
    - Aplica el lenguaje visual contextual según la audiencia.
    - Ajusta la proporción geométrica (16:9, 4:3, 1:1, 3:4, AUTO).
    - Aplica tokens de diseño formales, marcas e iconografía vectorial pura.
    - Devuelve un SketionResult con escena, explicabilidad y exportador.
    """
    diagram_title = title or payload.get("title", "SYSTEM ARCHITECTURE")

    # 1. Resolver Lenguaje Visual & Tema
    theme = VisualLanguageEngine.resolve_theme(audience=audience, domain_hint=diagram_title)
    final_bg = bg_color or theme.canvas_bg

    # 2. Selección Autónoma de Arquetipo
    if isinstance(archetype, str) and archetype.lower() == "auto":
        txt = f"{diagram_title} {payload}".lower()
        if any(w in txt for w in ["pipeline", "flow", "transcoder", "sequence", "checkout"]):
            arch_enum = SpatialArchetype.PIPELINE
            arch_rat = "Alta densidad de relaciones secuenciales direccionales en serie."
        elif any(w in txt for w in ["hub", "mesh", "star", "brain", "satellite", "cluster"]):
            arch_enum = SpatialArchetype.RADIAL_HUB
            arch_rat = "Topología en estrella desacoplada con orquestador central (El Cerebro)."
        elif any(w in txt for w in ["migration", "before", "after", "legacy", "vs", "transformation"]):
            arch_enum = SpatialArchetype.SPLIT_DUEL
            arch_rat = "Análisis comparativo de modernización (Legacy vs Target Hero)."
        else:
            arch_enum = SpatialArchetype.LAYERED
            arch_rat = "Estratificación de responsabilidades por capas funcionales y persistencia."
    elif isinstance(archetype, str):
        arch_enum = SpatialArchetype[archetype.upper()]
        arch_rat = f"Arquetipo {arch_enum.value} seleccionado explícitamente."
    else:
        arch_enum = archetype
        arch_rat = f"Arquetipo {arch_enum.value} seleccionado explícitamente."

    # 3. Resolver Proporción
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

    # 4. Construir Escena Excalidraw
    scene = ExcalidrawScene(roughness=roughness, bg_color=final_bg)
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

    # 5. Exportar si se especificó ruta
    if output:
        ext = os.path.splitext(output)[1].lower()
        fmt = "svg" if ext == ".svg" else "excalidraw"
        export_scene(scene, output, format=fmt)

    # 6. Evaluar Consistencia
    consistency_rep = VisualConsistencyEngine.evaluate_scene(scene.to_dict())

    # 7. Identificar Marcas y Componente Hero
    all_labels = []
    hero_label = "Orchestrator Core"
    if "layers" in payload:
        for l in payload["layers"]:
            for e in l.get("entities", []):
                lbl = e.get("label", "")
                all_labels.append(lbl)
                if e.get("is_hero"):
                    hero_label = lbl
    elif "steps" in payload:
        for s in payload["steps"]:
            all_labels.append(s.get("label", ""))
            if s.get("is_hero"):
                hero_label = s.get("label", "")

    matched_brands = []
    for lbl in all_labels:
        b = BrandRegistry.match_brand(lbl)
        if b and b.display_name not in matched_brands:
            matched_brands.append(b.display_name)

    trace = DesignDecisionTrace(
        title=diagram_title,
        target_audience=audience.upper(),
        primary_objective=f"Representar arquitectura {arch_enum.value} con alta fidelidad y consistencia.",
        selected_archetype=arch_enum.value,
        archetype_rationale=arch_rat,
        hero_component=hero_label,
        hero_rationale="Componente central de orquestación transaccional con mayor relevancia de negocio.",
        visual_language=theme.dialect.value,
        aspect_ratio=ratio_enum.value,
        entity_count=len(all_labels) or len(scene.elements),
        recognized_brands=matched_brands,
        vcs_score=consistency_rep.vcs_score,
        repair_dependency=0.0
    )

    return SketionResult(
        scene=scene,
        title=diagram_title,
        trace=trace,
        consistency=consistency_rep,
        output_path=output
    )


def validate(filepath: str):
    """Valida un diagrama generado contra las métricas de calidad de Sketion."""
    return validate_scene(filepath)


def export(scene_input: Union[Dict[str, Any], Any], output_path: str, format: str = "auto") -> str:
    """Exporta directamente una escena al formato indicado."""
    if format == "auto":
        ext = os.path.splitext(output_path)[1].lower()
        fmt = "svg" if ext == ".svg" else "excalidraw"
    else:
        fmt = format
    return export_scene(scene_input, output_path, format=fmt)
