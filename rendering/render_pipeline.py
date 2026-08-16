"""
Sketion 7.0 — Native Excalidraw Render Pipeline
Pipeline integral que transforma cualquier intención semántica o JSON estructurado
en un archivo nativo .excalidraw utilizando:
- AnchorGeometry (corte exacto de rayos en el perímetro de cada forma)
- OrthogonalRouter (conectores a 90° con evitación de colisiones)
- AdaptiveMultiFrame (partición inteligente de marcos)
- SemanticTextDecomposer (tarjetas jerarquizadas con badges, títulos y subtítulos)
- RenderFidelityAudit (auditoría automática de calidad de renderizado)
"""

import json
import uuid
from typing import List, Dict, Any, Tuple, Optional
from rendering.anchor_geometry import Point, ShapeBounds, AnchorGeometryEngine
from rendering.orthogonal_router import OrthogonalRouterEngine, RoutedPath
from rendering.adaptive_multi_frame import AdaptiveMultiFrameEngine, FramePartitionDecision
from rendering.render_fidelity import RenderFidelityEngine, RenderFidelityAudit
from composition.narrative_model import NarrativeModelEngine, NarrativeModel
from composition.oracle_judge import OracleCompositionJudge, OracleDecision
from semantic.text_decomposer import SemanticTextDecomposer, DecomposedBlock


class SketionRenderPipeline:
    """Pipeline de renderizado físico nativo Excalidraw de Sketion 7.0."""

    @classmethod
    def _gen_id(cls, prefix: str = "el") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @classmethod
    def render_from_structured_spec(cls, spec: Dict[str, Any], output_path: Optional[str] = None) -> Tuple[Dict[str, Any], RenderFidelityAudit]:
        title = spec.get("title", "Diagrama Sketion")
        steps = spec.get("steps", [])
        
        # 1. Inferir modelo narrativo
        raw_text_corpus = title + " " + " ".join([s.get("label", "") for s in steps])
        decision = OracleCompositionJudge.judge_composition(raw_text_corpus, top_k=3)
        narrative = decision.narrative_model

        # 2. Decisión de partición de marcos
        partition = AdaptiveMultiFrameEngine.evaluate_partition(len(steps), narrative.intent)

        elements = []
        bounds_map = {}
        card_width = 240.0
        card_height = 110.0
        gap_x = 70.0
        start_x = 80.0
        start_y = 120.0

        # Marco contenedor
        frame_w = max(1100.0, start_x * 2 + len(steps) * (card_width + gap_x))
        frame_h = 420.0
        frame_id = cls._gen_id("frame")
        
        elements.append({
            "id": frame_id,
            "type": "frame",
            "x": 40.0,
            "y": 40.0,
            "width": frame_w,
            "height": frame_h,
            "name": f"01. {title}",
            "strokeColor": "#CED4DA",
            "backgroundColor": "#F8F9FA"
        })

        # Título del diagrama
        elements.append({
            "id": cls._gen_id("title"),
            "type": "text",
            "x": start_x,
            "y": 65.0,
            "text": f"PROCESO: {title.upper()}",
            "fontSize": 20,
            "fontFamily": 1,
            "textAlign": "left",
            "strokeColor": "#1E1E1E",
            "frameId": frame_id
        })

        # Renderizar nodos (Tarjetas estructuradas)
        for idx, step in enumerate(steps):
            cx = start_x + idx * (card_width + gap_x)
            cy = start_y
            is_hero = step.get("is_hero", False)
            step_num = step.get("step_num", f"0{idx+1}")
            raw_label = step.get("label", f"Paso {idx+1}")

            # Descomposición semántica del texto
            dec = SemanticTextDecomposer.decompose(raw_label, is_pain_or_hero=("hero" if is_hero else None))

            stroke_c = "#D93829" if is_hero else "#212529"
            bg_c = "#FFF5F5" if is_hero else "#FFFFFF"
            node_id = cls._gen_id("card")

            # Rectángulo contenedor
            elements.append({
                "id": node_id,
                "type": "rectangle",
                "x": cx,
                "y": cy,
                "width": card_width,
                "height": card_height,
                "strokeColor": stroke_c,
                "backgroundColor": bg_c,
                "fillStyle": "solid",
                "strokeWidth": 2.0 if is_hero else 1.0,
                "roughness": 0,
                "roundness": {"type": 3},
                "frameId": frame_id
            })

            # Badge / Step Pill
            badge_text = f"PASO {step_num}" if not is_hero else f"PASO {step_num} · CORE"
            elements.append({
                "id": cls._gen_id("badge"),
                "type": "text",
                "x": cx + 14.0,
                "y": cy + 14.0,
                "text": badge_text,
                "fontSize": 12,
                "fontFamily": 1,
                "textAlign": "left",
                "strokeColor": stroke_c,
                "frameId": frame_id
            })

            # Título principal del paso
            display_title = dec.title if len(dec.title) <= 28 else dec.title[:25] + "..."
            elements.append({
                "id": cls._gen_id("label"),
                "type": "text",
                "x": cx + 14.0,
                "y": cy + 38.0,
                "text": display_title,
                "fontSize": 16,
                "fontFamily": 1,
                "textAlign": "left",
                "strokeColor": "#1E1E1E",
                "frameId": frame_id
            })

            # Subtítulo explicativo
            if dec.subtitle:
                sub_disp = dec.subtitle if len(dec.subtitle) <= 32 else dec.subtitle[:29] + "..."
                elements.append({
                    "id": cls._gen_id("sub"),
                    "type": "text",
                    "x": cx + 14.0,
                    "y": cy + 68.0,
                    "text": sub_disp,
                    "fontSize": 12,
                    "fontFamily": 1,
                    "textAlign": "left",
                    "strokeColor": "#495057",
                    "frameId": frame_id
                })

            bounds_map[idx] = ShapeBounds(cx, cy, card_width, card_height, "rectangle")

        # Renderizar conectores ortogonales con AnchorGeometry
        for idx in range(len(steps) - 1):
            source_b = bounds_map[idx]
            target_b = bounds_map[idx + 1]
            edge_lbl = steps[idx].get("edge_label", "")

            # Enrutamiento ortogonal libre de colisiones
            routed = OrthogonalRouterEngine.route_connector(source_b, target_b)
            arrow_id = cls._gen_id("arrow")

            elements.append({
                "id": arrow_id,
                "type": "arrow",
                "x": routed.start_point[0],
                "y": routed.start_point[1],
                "points": routed.intermediate_points,
                "strokeColor": "#212529",
                "strokeWidth": 1.5,
                "roughness": 0,
                "startArrowhead": None,
                "endArrowhead": "arrow",
                "frameId": frame_id
            })

            # Etiqueta de la flecha
            if edge_lbl:
                elements.append({
                    "id": cls._gen_id("edge_txt"),
                    "type": "text",
                    "x": routed.label_position[0] - 20.0,
                    "y": routed.label_position[1],
                    "text": edge_lbl,
                    "fontSize": 12,
                    "fontFamily": 1,
                    "textAlign": "center",
                    "strokeColor": "#495057",
                    "frameId": frame_id
                })

        scene_data = {
            "type": "excalidraw",
            "version": 2,
            "source": "https://sketion.engine.v7",
            "elements": elements,
            "appState": {
                "viewBackgroundColor": "#FFFFFF",
                "gridSize": 20
            }
        }

        # Auditar fidelidad de renderizado
        fidelity_audit = RenderFidelityEngine.audit_scene(scene_data, narrative)

        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(scene_data, f, indent=2, ensure_ascii=False)

        return scene_data, fidelity_audit
