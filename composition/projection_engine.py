"""
Sketion Multi-Projection Engine (v11.0 GA)
Demuestra la capacidad 'Same Knowledge, Multiple Valid Projections':
A partir de un único ContentModel, genera 5 representaciones gráficas totalmente diferenciadas
en su estructura visual y estilo según la audiencia:
1. Technical (Layered Architecture: Capas con cilindros, WAF, colas y microservicios + Tema Técnico)
2. Executive (Narrative Story Board: 6 Fases ejecutivas conectadas + Tema Ejecutivo)
3. Academic (Hierarchical Tree: Árbol taxonómico de arriba a abajo + Tema Académico)
4. Blueprint (Security Barrier: Perímetro defensivo Zero-Trust con barreras + Tema Blueprint)
5. Minimal (Pipeline Flow: Flujo secuencial limpio + Tema Minimal)
"""

from dataclasses import dataclass
from typing import Dict, Any, List, Tuple, Optional
import os

from semantic.content_model import ContentModel, SystemNodeSpec, RelationshipSpec, SystemNodeType, RelationshipType
from layout.layout_solver import LayoutSolver, LayoutAlgorithm
from design.theme_engine import ThemeEngine, VisualStyleType
from render.excalidraw_builder import ExcalidrawScene
from .composition_patterns import CompositionPattern, CompositionPatternRegistry
from .narrative_composer import NarrativeComposer, NarrativeBoard, NarrativeSection
from repair.closed_loop import ClosedLoopRepairEngine, ClosedLoopReport


@dataclass
class ProjectionResult:
    projection_name: str
    target_audience: str
    pattern: CompositionPattern
    style: VisualStyleType
    scene: ExcalidrawScene
    report: ClosedLoopReport
    file_path: Optional[str] = None


class MultiProjectionEngine:
    """Genera proyecciones polimórficas del mismo modelo semántico."""

    @classmethod
    def project_all(cls,
                    content: ContentModel,
                    output_dir: str) -> List[ProjectionResult]:
        """Genera las 5 proyecciones del ContentModel y las exporta a output_dir."""
        os.makedirs(output_dir, exist_ok=True)
        results: List[ProjectionResult] = []

        # ── 1. PROYECCIÓN TECHNICAL (Layered Architecture con Cilindros y Capas) ──
        s1 = ExcalidrawScene()
        fid1 = s1.add_frame(f"Technical: {content.title}", 0, 0, 1440, 900)
        CompositionPatternRegistry.render_pattern(
            CompositionPattern.LAYERED_ARCHITECTURE, content, s1, frame_id=fid1, style=VisualStyleType.TECHNICAL
        )
        cert_s1, rep1 = ClosedLoopRepairEngine.execute_closed_loop(s1)
        out1_svg = os.path.join(output_dir, "01_projection_technical.svg")
        out1_exc = os.path.join(output_dir, "01_projection_technical.excalidraw")
        cert_s1.export_svg(out1_svg)
        cert_s1.export_excalidraw(out1_exc)
        results.append(ProjectionResult("Technical Architecture", "Senior Engineers & Architects", CompositionPattern.LAYERED_ARCHITECTURE, VisualStyleType.TECHNICAL, cert_s1, rep1, out1_svg))

        # ── 2. PROYECCIÓN EXECUTIVE (Narrative Story Board) ───────────────────
        s2 = ExcalidrawScene()
        n_board = NarrativeComposer.create_standard_story(content.title, domain=content.domain)
        NarrativeComposer.render_deep_dive_board(n_board, s2, style=VisualStyleType.EXECUTIVE)
        cert_s2, rep2 = ClosedLoopRepairEngine.execute_closed_loop(s2)
        out2_svg = os.path.join(output_dir, "02_projection_executive.svg")
        out2_exc = os.path.join(output_dir, "02_projection_executive.excalidraw")
        cert_s2.export_svg(out2_svg)
        cert_s2.export_excalidraw(out2_exc)
        results.append(ProjectionResult("Executive Narrative Story", "C-Level & VP Stakeholders", CompositionPattern.NARRATIVE_BOARD, VisualStyleType.EXECUTIVE, cert_s2, rep2, out2_svg))

        # ── 3. PROYECCIÓN ACADEMIC (Hierarchical Tree de Arriba a Abajo) ──────
        s3 = ExcalidrawScene()
        fid3 = s3.add_frame(f"Academic: {content.title}", 0, 0, 1440, 900)
        CompositionPatternRegistry.render_pattern(
            CompositionPattern.HIERARCHICAL_TREE, content, s3, frame_id=fid3, style=VisualStyleType.ACADEMIC
        )
        cert_s3, rep3 = ClosedLoopRepairEngine.execute_closed_loop(s3)
        out3_svg = os.path.join(output_dir, "03_projection_academic.svg")
        out3_exc = os.path.join(output_dir, "03_projection_academic.excalidraw")
        cert_s3.export_svg(out3_svg)
        cert_s3.export_excalidraw(out3_exc)
        results.append(ProjectionResult("Academic Taxonomical Tree", "Researchers & Students", CompositionPattern.HIERARCHICAL_TREE, VisualStyleType.ACADEMIC, cert_s3, rep3, out3_svg))

        # ── 4. PROYECCIÓN BLUEPRINT (Defense-in-Depth Security Barrier) ────────
        s4 = ExcalidrawScene()
        fid4 = s4.add_frame(f"Blueprint: {content.title}", 0, 0, 1440, 900)
        CompositionPatternRegistry.render_pattern(
            CompositionPattern.SECURITY_BARRIER, content, s4, frame_id=fid4, style=VisualStyleType.BLUEPRINT
        )
        cert_s4, rep4 = ClosedLoopRepairEngine.execute_closed_loop(s4)
        out4_svg = os.path.join(output_dir, "04_projection_blueprint.svg")
        out4_exc = os.path.join(output_dir, "04_projection_blueprint.excalidraw")
        cert_s4.export_svg(out4_svg)
        cert_s4.export_excalidraw(out4_exc)
        results.append(ProjectionResult("Technical Blueprint", "Security Engineers & DevOps", CompositionPattern.SECURITY_BARRIER, VisualStyleType.BLUEPRINT, cert_s4, rep4, out4_svg))

        # ── 5. PROYECCIÓN MINIMAL (Sequential Pipeline Flow) ──────────────────
        s5 = ExcalidrawScene()
        fid5 = s5.add_frame(f"Minimal: {content.title}", 0, 0, 1440, 900)
        CompositionPatternRegistry.render_pattern(
            CompositionPattern.PIPELINE_FLOW, content, s5, frame_id=fid5, style=VisualStyleType.MINIMAL
        )
        cert_s5, rep5 = ClosedLoopRepairEngine.execute_closed_loop(s5)
        out5_svg = os.path.join(output_dir, "05_projection_minimal.svg")
        out5_exc = os.path.join(output_dir, "05_projection_minimal.excalidraw")
        cert_s5.export_svg(out5_svg)
        cert_s5.export_excalidraw(out5_exc)
        results.append(ProjectionResult("Minimal Flow", "General Audience & Documentation", CompositionPattern.PIPELINE_FLOW, VisualStyleType.MINIMAL, cert_s5, rep5, out5_svg))

        return results
