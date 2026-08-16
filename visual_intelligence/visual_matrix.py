"""
Sketion Visual Matrix Engine (v8.4 - 4x4x4 Multi-Archetype / Multi-Domain / Multi-Audience)
Permite renderizar cualquier carga arquitectónica a través de 4 Arquetipos Espaciales:
1. LAYERED: Arquitectura estratificada por capas con componentes polimórficos.
2. PIPELINE: Flujo lineal continuo con chevrons de macro-etapa, pasos y bucles de retorno.
3. RADIAL_HUB: Núcleo orquestador central (El Cerebro) con nodos satélites orbitando 360°.
4. SPLIT_DUEL: Duelo comparativo (Legacy vs Target Hero) con paneles contrastados.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, List, Optional
import math

from visual_intelligence.visual_composition import VisualCompositionEngine, VisualEntitySpec
from render.excalidraw_builder import ExcalidrawScene, place


class SpatialArchetype(Enum):
    LAYERED = "LAYERED"
    PIPELINE = "PIPELINE"
    RADIAL_HUB = "RADIAL_HUB"
    SPLIT_DUEL = "SPLIT_DUEL"


class VisualMatrixEngine:
    """Motor de orquestación matricial multidominio y multiarquetipo."""

    @classmethod
    def render_archetype(cls, scene: ExcalidrawScene,
                         archetype: SpatialArchetype,
                         title: str,
                         payload: Dict[str, Any],
                         fx: float, fy: float,
                         target_w: float = 1600.0,
                         target_h: float = 650.0) -> str:
        """Renderiza un payload arquitectónico bajo el arquetipo espacial especificado."""
        fid = scene.add_frame(title, fx, fy, target_w, target_h)

        # Cabecera editorial
        scene.add_text(fx + 50.0, fy + 30.0, f"SKETION VISUAL MATRIX · ARQUETIPO {archetype.value}", font_size=12, font_family=2, color="#64748B", frame_id=fid)
        scene.add_text(fx + 50.0, fy + 52.0, title, font_size=22, font_family=2, color="#0F172A", frame_id=fid)

        if archetype == SpatialArchetype.LAYERED:
            cls._render_layered(scene, fid, fx, fy, target_w, payload)
        elif archetype == SpatialArchetype.PIPELINE:
            cls._render_pipeline(scene, fid, fx, fy, target_w, payload)
        elif archetype == SpatialArchetype.RADIAL_HUB:
            cls._render_radial_hub(scene, fid, fx, fy, target_w, target_h, payload)
        elif archetype == SpatialArchetype.SPLIT_DUEL:
            cls._render_split_duel(scene, fid, fx, fy, target_w, payload)

        # Ajuste dinámico ceñido
        scene.auto_fit_frame(fid, padding=45.0)
        return fid

    @classmethod
    def _render_layered(cls, scene: ExcalidrawScene, fid: str, fx: float, fy: float, w: float, payload: Dict[str, Any]):
        layers = payload.get("layers", [])
        padding_x = 50.0
        usable_w = w - (padding_x * 2.0)
        cur_y = fy + 95.0

        for l_idx, layer in enumerate(layers):
            layer_name = layer.get("name", f"Capa {l_idx+1}")
            entities = layer.get("entities", [])
            if not entities:
                continue

            # Ribbon
            scene.add_rect(fx + padding_x, cur_y, usable_w, 28.0, bg="#F1F5F9", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=fid)
            scene.add_text(fx + padding_x + 14.0, cur_y + 7.0, layer_name.upper(), font_size=11, font_family=2, color="#334155", frame_id=fid)
            cur_y += 38.0

            cnt = len(entities)
            cols = min(4, cnt)
            gap = 20.0
            card_w = (usable_w - (cols - 1) * gap) / cols
            card_h = 135.0

            for i, raw_e in enumerate(entities):
                c_idx = i % cols
                r_idx = i // cols
                cx = fx + padding_x + c_idx * (card_w + gap)
                cy = cur_y + r_idx * (card_h + gap)

                spec = VisualCompositionEngine.analyze_entity(raw_e)
                VisualCompositionEngine.render_entity_node(scene, cx, cy, card_w, card_h, spec, frame_id=fid)

            rows = math.ceil(cnt / cols)
            cur_y += rows * (card_h + gap) + 12.0

        scene.add_legend_footer(fx + padding_x, cur_y + 10.0, usable_w, swatches=[
            {"label": "Componente Core Hero", "bg": "#FFF5F2", "stroke": "#D93829"},
            {"label": "Infraestructura & Servicios", "bg": "#EFF6FF", "stroke": "#2563EB"}
        ], note="Layered Architecture: Estratificación por capas funcionales y persistencia ACID.", frame_id=fid)

    @classmethod
    def _render_pipeline(cls, scene: ExcalidrawScene, fid: str, fx: float, fy: float, w: float, payload: Dict[str, Any]):
        stages = payload.get("stages", ["1. INGESTA", "2. ENRIQUECIMIENTO", "3. ORQUESTACIÓN HERO", "4. PERSISTENCIA", "5. ANALYTICS"])
        steps = payload.get("steps", [])
        padding_x = 50.0
        usable_w = w - (padding_x * 2.0)

        # 1. Macro-Ribbon de Chevrons
        scene.add_chevron_ribbon(fx + padding_x, fy + 95.0, usable_w, h=36.0, stages=stages, frame_id=fid)

        # 2. Pasos secuenciales con conectores direccionales
        step_cnt = len(steps)
        gap = 24.0
        step_w = (usable_w - (step_cnt - 1) * gap) / max(1, step_cnt)
        node_y = fy + 160.0
        step_h = 145.0

        for i, st in enumerate(steps):
            sx = fx + padding_x + i * (step_w + gap)
            spec = VisualCompositionEngine.analyze_entity(st)
            VisualCompositionEngine.render_entity_node(scene, sx, node_y, step_w, step_h, spec, frame_id=fid)

            # Conector horizontal
            if i < step_cnt - 1:
                edge_label = st.get("edge_label", "")
                scene.add_arrow(
                    sx + step_w, node_y + (step_h * 0.5),
                    sx + step_w + gap, node_y + (step_h * 0.5),
                    stroke="#D93829" if spec.is_hero else "#2563EB",
                    stroke_w=2.0 if spec.is_hero else 1.5,
                    label=edge_label,
                    frame_id=fid
                )

        # 3. Bucle de retorno / Fallback si aplica
        if payload.get("has_return_loop", True):
            loop_y = node_y + step_h + 30.0
            scene.add_line(fx + padding_x + usable_w - 60.0, node_y + step_h, fx + padding_x + usable_w - 60.0, loop_y, stroke="#DC2626", stroke_w=1.5, dashed=True, frame_id=fid)
            scene.add_line(fx + padding_x + usable_w - 60.0, loop_y, fx + padding_x + 60.0, loop_y, stroke="#DC2626", stroke_w=1.5, dashed=True, frame_id=fid)
            scene.add_arrow(fx + padding_x + 60.0, loop_y, fx + padding_x + 60.0, node_y + step_h, stroke="#DC2626", stroke_w=1.5, dashed=True, label="Fallback / Retry DLQ", frame_id=fid)
            footer_y = loop_y + 35.0
        else:
            footer_y = node_y + step_h + 25.0

        scene.add_legend_footer(fx + padding_x, footer_y, usable_w, swatches=[
            {"label": "Flujo Secuencial Sincrónico", "bg": "#EFF6FF", "stroke": "#2563EB", "is_arrow": True},
            {"label": "Bucle de Reintento / Dead Letter Queue", "bg": "#FFF5F2", "stroke": "#DC2626", "is_arrow": True, "dashed": True}
        ], note="Pipeline Flow: Trazabilidad paso a paso con manejo explícito de fallos y reintentos.", frame_id=fid)

    @classmethod
    def _render_radial_hub(cls, scene: ExcalidrawScene, fid: str, fx: float, fy: float, w: float, h: float, payload: Dict[str, Any]):
        hub_data = payload.get("hub", {"label": "Orchestrator Core", "role": "service", "is_hero": True})
        satellites = payload.get("satellites", [])
        padding_x = 50.0
        usable_w = w - (padding_x * 2.0)

        cx = fx + (w * 0.5)
        cy = fy + 330.0

        # Dimensiones del Hub Central Hero
        hw, hh = 280.0, 120.0
        hub_spec = VisualCompositionEngine.analyze_entity(hub_data)
        VisualCompositionEngine.render_entity_node(scene, cx - (hw * 0.5), cy - (hh * 0.5), hw, hh, hub_spec, frame_id=fid)

        # Radio elíptico seguro (calculado matemáticamente para evitar cualquier solapamiento)
        # Rx considera el ancho del hub (280) + ancho de satélite (230) + margen de aire (90px)
        rx_orbit = 380.0
        # Ry considera el alto del hub (120) + alto de satélite (100) + margen de aire (70px)
        ry_orbit = 210.0

        sat_cnt = len(satellites)
        if sat_cnt > 0:
            angle_step = (2 * math.pi) / sat_cnt
            for i, sat in enumerate(satellites):
                # Desfase angular para distribuir armónicamente en 360 grados
                angle = i * angle_step - (math.pi / 2.0)
                sx = cx + rx_orbit * math.cos(angle)
                sy = cy + ry_orbit * math.sin(angle)
                sw, sh = 230.0, 100.0
                spx = sx - (sw * 0.5)
                spy = sy - (sh * 0.5)

                sat_spec = VisualCompositionEngine.analyze_entity(sat)
                VisualCompositionEngine.render_entity_node(scene, spx, spy, sw, sh, sat_spec, frame_id=fid)

                # Cálculo de puntos de anclaje periféricos exactos (Ray-Box intersection limpio)
                hub_edge_x = cx + math.copysign(min(hw * 0.5, abs((hh * 0.5) / max(0.001, math.tan(angle)))), math.cos(angle)) if abs(math.cos(angle)) > 0.3 else cx
                hub_edge_y = cy + math.copysign(min(hh * 0.5, abs((hw * 0.5) * math.tan(angle))), math.sin(angle)) if abs(math.sin(angle)) > 0.3 else cy

                sat_edge_x = sx - math.copysign(min(sw * 0.5, abs((sh * 0.5) / max(0.001, math.tan(angle)))), math.cos(angle)) if abs(math.cos(angle)) > 0.3 else sx
                sat_edge_y = sy - math.copysign(min(sh * 0.5, abs((sw * 0.5) * math.tan(angle))), math.sin(angle)) if abs(math.sin(angle)) > 0.3 else sy

                # Conector radial sin atravesar los bloques de texto
                scene.add_arrow(
                    hub_edge_x, hub_edge_y,
                    sat_edge_x, sat_edge_y,
                    stroke="#94A3B8", stroke_w=1.2, dashed=True, frame_id=fid
                )

        footer_y = cy + ry_orbit + 80.0
        scene.add_legend_footer(fx + padding_x, footer_y, usable_w, swatches=[
            {"label": "Hub Central Transaccional", "bg": "#FFF5F2", "stroke": "#D93829"},
            {"label": "Satélites Especializados / Adaptadores", "bg": "#EFF6FF", "stroke": "#2563EB"}
        ], note="Radial Hub & Spoke: Topología en estrella elíptica desacoplada sin colisiones.", frame_id=fid)

    @classmethod
    def _render_split_duel(cls, scene: ExcalidrawScene, fid: str, fx: float, fy: float, w: float, payload: Dict[str, Any]):
        padding_x = 50.0
        usable_w = w - (padding_x * 2.0)
        col_w = (usable_w - 60.0) * 0.5
        duel_h = 320.0
        duel_y = fy + 100.0

        left = payload.get("left", {
            "title": "Arquitectura Monolítica Legacy",
            "items": ["Monolito PHP/MySQL con acoplamiento severo", "Bloqueos de tabla globales en transacciones concurrentes", "Despliegues coordinados con downtime de 2h", "Cero tolerancia a caídas de pasarelas adquirentes"]
        })
        right = payload.get("right", {
            "title": "Cloud-Native Event-Driven Target",
            "items": ["Microservicios desacoplados en Kubernetes (EKS)", "Persistencia ACID en PostgreSQL + Caching Redis P99 <15ms", "Pipeline CI/CD con Zero-Downtime y Canary Releases", "Resiliencia activa: Circuit Breaker y fallback multi-pasarela"]
        })

        scene.add_split_duel(
            fx + padding_x, duel_y, usable_w, duel_h,
            left_title=left["title"], left_items=left["items"],
            right_title=right["title"], right_items=right["items"],
            left_label="ANTES (LEGACY)", right_label="DESPUÉS (TARGET HERO)",
            frame_id=fid
        )

        footer_y = duel_y + duel_h + 25.0
        scene.add_legend_footer(fx + padding_x, footer_y, usable_w, swatches=[
            {"label": "Fricción / Deuda Técnica Legacy", "bg": "#F8FAFC", "stroke": "#CBD5E1"},
            {"label": "Arquitectura Target Hero Optimizada", "bg": "#F0FDF4", "stroke": "#86EFAC"}
        ], note="Split Duel (VS): Análisis comparativo de migración y mitigación de deuda técnica.", frame_id=fid)
