"""
Sketion 8.0 — Native Excalidraw Render Pipeline
Pipeline integral que transforma cualquier intención semántica o JSON estructurado
en un archivo nativo .excalidraw utilizando:
- ExcalidrawScene (motor oficial de renderizado con vinculación containerId <-> boundElements,
  tipografía precisa, baseline, lineHeight y autoResize para garantizar visibilidad al 100%)
- AnchorGeometry (corte exacto de rayos en el perímetro de cada forma)
- OrthogonalRouter (conectores a 90° con evitación de colisiones)
- AdaptiveMultiFrame (partición inteligente de marcos)
- SemanticTextDecomposer (tarjetas jerarquizadas con badges, títulos y subtítulos)
- RenderFidelityAudit (auditoría automática de calidad de renderizado)
"""

import json
from typing import List, Dict, Any, Tuple, Optional
from rendering.anchor_geometry import ShapeBounds
from rendering.orthogonal_router import OrthogonalRouterEngine
from rendering.adaptive_multi_frame import AdaptiveMultiFrameEngine
from rendering.render_fidelity import RenderFidelityEngine, RenderFidelityAudit
from composition.oracle_judge import OracleCompositionJudge
from semantic.text_decomposer import SemanticTextDecomposer
from render.excalidraw_builder import ExcalidrawScene


class SketionRenderPipeline:
    """Pipeline de renderizado físico nativo Excalidraw de Sketion 8.0."""

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

        # 3. Inicializar ExcalidrawScene con motor tipográfico nativo
        scene = ExcalidrawScene(roughness=0, bg_color="#FFFFFF")

        card_width = 260.0
        card_height = 115.0
        gap_x = 75.0
        start_x = 80.0
        start_y = 125.0

        # Marco contenedor
        frame_w = max(1150.0, start_x * 2 + len(steps) * (card_width + gap_x))
        frame_h = 440.0
        frame_id = scene.add_frame(f"01. {title}", 40.0, 40.0, frame_w, frame_h)

        # Título del diagrama (Tipografía 20px Bold, legible)
        scene.add_text(start_x, 65.0, f"PROCESO: {title.upper()}", font_size=20, font_family=2, color="#0F172A", frame_id=frame_id)

        bounds_map = {}

        # 4. Renderizar nodos (Tarjetas estructuradas con containerId y boundElements)
        for idx, step in enumerate(steps):
            cx = start_x + idx * (card_width + gap_x)
            cy = start_y
            is_hero = step.get("is_hero", False)
            step_num = step.get("step_num", f"0{idx+1}")
            raw_label = step.get("label", f"Paso {idx+1}")

            # Descomposición semántica del texto
            dec = SemanticTextDecomposer.decompose(raw_label, is_pain_or_hero=("hero" if is_hero else None))

            badge_text = f"PASO {step_num}" if not is_hero else f"PASO {step_num} · CORE"
            icon_name = "key" if is_hero else ("server" if idx % 2 == 1 else "laptop")

            # Crear tarjeta de 4 esquinas totalmente vinculada y con texto visible
            scene.add_quad_card(
                cx, cy, card_width, card_height,
                title=dec.title,
                sublabel=dec.subtitle,
                badge=badge_text,
                icon=icon_name,
                bg="#FFF5F2" if is_hero else "#FFFFFF",
                stroke="#E03A2F" if is_hero else "#212529",
                text_color="#0F172A",
                font_size=15,
                is_hero=is_hero,
                frame_id=frame_id
            )

            bounds_map[idx] = ShapeBounds(cx, cy, card_width, card_height, "rectangle")

        # 5. Renderizar conectores ortogonales con AnchorGeometry
        for idx in range(len(steps) - 1):
            source_b = bounds_map[idx]
            target_b = bounds_map[idx + 1]
            edge_lbl = steps[idx].get("edge_label", "")

            # Enrutamiento ortogonal libre de colisiones
            routed = OrthogonalRouterEngine.route_connector(source_b, target_b)

            scene.add_arrow(
                routed.start_point[0], routed.start_point[1],
                routed.end_point[0], routed.end_point[1],
                stroke="#212529",
                stroke_w=1.5,
                arrowhead="triangle",
                label=edge_lbl if edge_lbl else None,
                frame_id=frame_id
            )

        scene_data = scene.to_dict()

        # 6. Auditar fidelidad de renderizado
        fidelity_audit = RenderFidelityEngine.audit_scene(scene_data, narrative)

        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(scene_data, f, indent=2, ensure_ascii=False)

        return scene_data, fidelity_audit
