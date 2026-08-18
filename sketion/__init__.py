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
from visual_intelligence.visual_types_27 import VisualTypes27Engine, VisualType27
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

from layout.ports import PortManager, PortPosition, PortDirection, NodeBoundary, PortSpec
from layout.manhattan_router import ManhattanRouter, RoutingContext, RoutedPath
from layout.layout_solver import LayoutSolver, LayoutAlgorithm, LayoutNode, LayoutEdge
from semantic.content_model import ContentModel, SystemNodeType, RelationshipType, ActorSpec, SystemNodeSpec, RelationshipSpec, MetricSpec
from semantic.reference_compositions import REFERENCE_COMPOSITIONS, ReferenceComposition
from semantic.retrieval import SemanticRetrievalEngine, RetrievalResult
from composition.composition_patterns import CompositionPattern, CompositionPatternRegistry
from composition.diversity_judge import DiversityJudge, DiversityScoreReport
from composition.narrative_composer import NarrativeComposer, NarrativeBoard, NarrativeSection
from design.theme_engine import ThemeEngine, VisualStyleType, StyleIntent, SemanticColorRole

__version__ = "11.0.0"
__all__ = [
    "render",
    "validate",
    "export",
    "SketionResult",
    "ExcalidrawScene",
    "SpatialArchetype",
    "VisualType27",
    "AspectRatioType",
    "VisualLanguageDialect",
    "BrandRegistry",
    "SemanticIconRegistry",
    "VisualCompositionEngine",
    "VisualMatrixEngine",
    "VisualTypes27Engine",
    "DesignDecisionTrace",
    # ── Sketion 11.0 Exports ──
    "compose",
    "SketionCompositionResult",
    "ContentModel",
    "SystemNodeType",
    "RelationshipType",
    "LayoutSolver",
    "LayoutAlgorithm",
    "ManhattanRouter",
    "PortManager",
    "PortPosition",
    "CompositionPattern",
    "CompositionPatternRegistry",
    "DiversityJudge",
    "DiversityScoreReport",
    "SemanticCompositionEvaluator",
    "SemanticCompositionReport",
    "PatternAuthenticityEvaluator",
    "AuthenticityReport",
    "ThemeEngine",
    "VisualStyleType",
    "StyleIntent",
    "SemanticRetrievalEngine",
    "REFERENCE_COMPOSITIONS",
    "NarrativeComposer",
    "NarrativeBoard"
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

    # 2. Selección Autónoma o Explícita del Tipo Visual
    is_27_type = False
    v27_enum = None

    if isinstance(archetype, VisualType27):
        is_27_type = True
        v27_enum = archetype
        arch_rat = f"Tipo Canónico {v27_enum.value} seleccionado explícitamente."
    elif isinstance(archetype, str) and archetype.lower() != "auto":
        arch_clean = archetype.lower().replace("-", "_")
        try:
            v27_enum = VisualType27(arch_clean)
            is_27_type = True
            arch_rat = f"Tipo Canónico {v27_enum.value} seleccionado explícitamente."
        except ValueError:
            try:
                arch_enum = SpatialArchetype[archetype.upper()]
                arch_rat = f"Arquetipo Espacial {arch_enum.value} seleccionado explícitamente."
            except KeyError:
                v27_enum = VisualTypes27Engine.classify_intent(archetype)
                is_27_type = True
                arch_rat = f"Arquetipo clasificado en tipo canónico {v27_enum.value}."
    elif isinstance(archetype, SpatialArchetype):
        arch_enum = archetype
        arch_rat = f"Arquetipo Espacial {arch_enum.value} seleccionado explícitamente."
    else:
        # Modo 'auto': Clasificar inteligentemente
        txt = f"{diagram_title} {payload}".lower()
        v27_enum = VisualTypes27Engine.classify_intent(txt)
        is_27_type = True
        arch_rat = f"Clasificación autónoma de alta fidelidad: Tipo Canónico '{v27_enum.value}'."

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
    
    if is_27_type and v27_enum:
        fid = scene.add_frame(diagram_title.upper(), fx, fy, ratio_spec.base_w, ratio_spec.base_h)
        VisualTypes27Engine.render_by_type(scene, v27_enum, fx, fy, ratio_spec.base_w, ratio_spec.base_h, frame_id=fid)
        scene.auto_fit_frame(fid, padding=35.0)
    else:
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

    selected_arch_str = v27_enum.value if (is_27_type and v27_enum) else (arch_enum.value if 'arch_enum' in locals() else "layered")

    trace = DesignDecisionTrace(
        title=diagram_title,
        target_audience=audience.upper(),
        primary_objective=f"Representar arquitectura {selected_arch_str} con alta fidelidad y consistencia.",
        selected_archetype=selected_arch_str,
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


from composition.pattern_authenticity import PatternAuthenticityEvaluator, AuthenticityReport
from composition.semantic_composition_score import SemanticCompositionEvaluator, SemanticCompositionReport
from repair.closed_loop import ClosedLoopRepairEngine, ClosedLoopReport


@dataclass
class SketionCompositionResult:
    """Resultado de la composición autónoma end-to-end de Sketion 11.0."""
    scene: ExcalidrawScene
    title: str
    pattern: CompositionPattern
    style: VisualStyleType
    content_model: ContentModel
    vcs_score: float
    scs_score: float
    vds_score: float
    pas_score: float
    scs_report: SemanticCompositionReport
    pas_report: AuthenticityReport
    loop_report: ClosedLoopReport

    def explain(self) -> str:
        """Reporte unificado de explicabilidad técnica y métricas de calidad."""
        lines = [
            f"# EXPLICABILIDAD DE COMPOSICIÓN: {self.title}",
            f"* **Patrón Seleccionado:** `{self.pattern.value}`",
            f"* **Estilo Visual:** `{self.style.value}`",
            f"* **VCS (Consistencia Visual):** {self.vcs_score:.1f} / 100",
            f"* **SCS (Ajuste Semántico):** {self.scs_score:.1f} / 100",
            f"* **VDS (Diversidad Visual):** {self.vds_score:.1f} / 100",
            f"* **PAS (Autenticidad Estructural):** {self.pas_score:.1f} / 100",
            "\n---\n",
            self.scs_report.to_markdown(),
            "\n---\n",
            self.pas_report.to_markdown(),
            "\n---\n",
            self.loop_report.to_markdown()
        ]
        return "\n".join(lines)

    def export(self, filepath: str, format: str = "auto") -> str:
        if format == "auto":
            ext = os.path.splitext(filepath)[1].lower()
            fmt = "svg" if ext == ".svg" else "excalidraw"
        else:
            fmt = format
        return export_scene(self.scene, filepath, format=fmt)


def compose(prompt: str,
            domain_hint: Optional[str] = None,
            style: Union[str, VisualStyleType] = VisualStyleType.EDITORIAL,
            frame_width: float = 1440.0,
            frame_height: float = 900.0) -> SketionCompositionResult:
    """
    Pipeline autónomo de composición visual de Sketion 11.0 GA:
    1. Retrieval Semántico Estructural (Bajo consumo de tokens)
    2. Construcción del ContentModel desacoplado
    3. Selección del Patrón Estructural Óptimo
    4. Evaluación de Adecuación Conceptual (SCS)
    5. Renderizado mediante la Firma Geométrica Auténtica del Patrón
    6. Closed-Loop Validation & Autonomous Repair (VCS >= 95.0)
    7. Verificación de Autenticidad de Patrón (PAS)
    """
    # 1. Recuperador Semántico
    retrieval = SemanticRetrievalEngine.match(prompt, domain_hint=domain_hint)
    pat = retrieval.recommended_pattern

    # 2. Resolver Estilo
    if isinstance(style, str):
        try:
            st_enum = VisualStyleType(style.lower())
        except ValueError:
            st_enum = VisualStyleType.EDITORIAL
    else:
        st_enum = style

    # 3. Construir ContentModel
    dom = domain_hint or (retrieval.matched_references[0].domain if retrieval.matched_references else "software")
    cm = ContentModel(title=prompt[:45], goal=prompt, domain=dom, composition_pattern_hint=pat.value)
    
    # Extraer entidades sugeridas
    sample_nodes = retrieval.suggested_primitives or ["Cliente / Usuario", "API Gateway", "Core Orchestrator", "Storage Database"]
    for i, s_label in enumerate(sample_nodes):
        cm.systems.append(SystemNodeSpec(id=f"node_{i}", label=s_label, layer_index=i, is_hero=(i==1 or i==2)))

    # 4. Evaluar SCS
    scs_rep = SemanticCompositionEvaluator.evaluate(pat, cm)

    # 5. Renderizar Escena
    scene = ExcalidrawScene()
    fid = scene.add_frame(cm.title, 0.0, 0.0, frame_width, frame_height)
    CompositionPatternRegistry.render_pattern(pat, cm, scene, frame_id=fid, style=st_enum)

    # 6. Closed Loop Repair & Certification
    cert_scene, loop_rep = ClosedLoopRepairEngine.execute_closed_loop(scene)

    # 7. Evaluar PAS y VDS
    pas_rep = PatternAuthenticityEvaluator.evaluate(pat, cert_scene.to_dict())
    vds_rep = DiversityJudge.evaluate(pat, cm, cert_scene, len(cm.systems)-1, len(cm.systems), len(cm.systems)-1, 4)

    return SketionCompositionResult(
        scene=cert_scene,
        title=cm.title,
        pattern=pat,
        style=st_enum,
        content_model=cm,
        vcs_score=loop_rep.final_vcs,
        scs_score=scs_rep.scs_score,
        vds_score=vds_rep.vds_overall,
        pas_score=pas_rep.authenticity_score,
        scs_report=scs_rep,
        pas_report=pas_rep,
        loop_report=loop_rep
    )
