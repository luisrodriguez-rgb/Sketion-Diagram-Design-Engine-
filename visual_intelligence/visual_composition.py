"""
Sketion Visual Composition Intelligence Engine (v8.3)
Orquestador de Composición Visual Autónoma:
Transforma grafos de arquitectura y payloads de entidades semánticas en diagramas
Excalidraw enriquecidos polimórficamente, seleccionando automáticamente:
- Arquetipo espacial (Layered, Pipeline Flow, Radial Hub, Split Duel)
- Morfología de componente (Cilindros, Tuberías Kafka, Barreras WAF, Pastillas de Actor, Tarjetas Quad, KPIs)
- Reconocimiento de Marcas (BrandRegistry) e Íconos Vectoriales (SemanticIconRegistry)
- Conectores semánticos tipados (Síncronos, Asíncronos, Reintentos, Auditoría)
- Layout ceñido con zonas verticales estrictas y auto-fit de frames.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Tuple
import math

from visual_intelligence.iconography import SemanticIconRegistry
from visual_intelligence.brand_registry import BrandRegistry, BrandSpec
from visual_intelligence.status_metrics import StatusBadgeEngine, BadgeType
from visual_intelligence.semantic_shapes import SemanticShapeType, SemanticShapeClassifier
from visual_intelligence.semantic_connectors import SemanticConnectorRouter, ConnectorSemantics
from visual_intelligence.data_viz import LightDataVizEngine, KPICardSpec, FunnelStepSpec
from render.excalidraw_builder import ExcalidrawScene, place_reset, place


@dataclass
class VisualEntitySpec:
    id: str
    label: str
    role: str
    tier: str
    shape_type: SemanticShapeType
    brand: Optional[BrandSpec]
    icon: str
    badge: str
    badge_type: BadgeType
    is_hero: bool
    description: str
    tech_tags: List[str]
    metadata: Dict[str, Any] = field(default_factory=dict)


class VisualCompositionEngine:
    """Motor autónomo de Composición Visual Inteligente (Sketion 8.3)."""

    @classmethod
    def analyze_entity(cls, raw_entity: Dict[str, Any]) -> VisualEntitySpec:
        """Analiza una entidad semántica y resuelve su especificación visual polimórfica completa."""
        eid = str(raw_entity.get("id", ""))
        label = str(raw_entity.get("label", raw_entity.get("name", "Component")))
        role = str(raw_entity.get("role", "service")).lower()
        tier = str(raw_entity.get("tier", "core")).lower()
        desc = str(raw_entity.get("description", raw_entity.get("sublabel", "")))
        is_hero = bool(raw_entity.get("is_hero", False) or tier == "hero" or "core" in role and "payment" in label.lower())

        # 1. Reconocimiento de Marca / Plataforma
        brand = BrandRegistry.match_brand(label)
        if not brand and desc:
            brand = BrandRegistry.match_brand(desc)

        # 2. Resolución de Ícono Vectorial
        if brand:
            icon = brand.vector_icon
        else:
            icon = SemanticIconRegistry.resolve_icon(f"{label} {role} {desc}")

        # 3. Clasificación Morfológica de Forma
        shape_spec = SemanticShapeClassifier.classify_entity(f"{label} {desc}", domain=role, is_hero=is_hero)
        shape_type = shape_spec.shape_type

        # 4. Generación de Badge Semántico
        badge_text = raw_entity.get("badge")
        if not badge_text:
            if brand:
                badge_text = brand.category.replace("_", " ")
            elif "db" in role or "database" in role or "storage" in role:
                badge_text = "ACID PERSISTENCE" if "sql" in desc.lower() or "postgre" in label.lower() else "DATA STORE"
            elif "queue" in role or "stream" in role or "broker" in role:
                badge_text = "EVENT STREAM"
            elif "security" in role or "waf" in role or "auth" in role or "vault" in role:
                badge_text = "SECURITY ZERO-TRUST"
            elif "actor" in role or "user" in role or "client" in role:
                badge_text = "● ACTIVE"
            elif is_hero:
                badge_text = "HERO CORE"
            else:
                badge_text = role.upper()

        badge_obj = StatusBadgeEngine.create_badge(badge_text)

        # 5. Tech tags
        tags = brand.tech_tags if brand else raw_entity.get("tech_tags", [])

        return VisualEntitySpec(
            id=eid,
            label=label,
            role=role,
            tier=tier,
            shape_type=shape_type,
            brand=brand,
            icon=icon,
            badge=badge_obj.symbol_prefix or badge_text,
            badge_type=badge_obj.badge_type,
            is_hero=is_hero,
            description=desc,
            tech_tags=tags,
            metadata=raw_entity
        )

    @classmethod
    def render_entity_node(cls, scene: ExcalidrawScene,
                           x: float, y: float, w: float, h: float,
                           spec: VisualEntitySpec,
                           frame_id: Optional[str] = None) -> Dict[str, Any]:
        """Renderiza una entidad con la primitiva visual geométrica exacta que le corresponde."""
        # Colores personalizados si tiene marca
        bg_col = spec.brand.bg_color if spec.brand else "#FFFFFF"
        stroke_col = spec.brand.brand_color if spec.brand else "#CBD5E1"

        if spec.shape_type == SemanticShapeType.DATABASE_CYLINDER:
            return scene.add_database_cylinder(
                x, y, w, h,
                title=spec.label,
                sublabel=spec.description,
                badge=spec.badge,
                is_hero=spec.is_hero,
                bg=spec.brand.bg_color if spec.brand else "#EFF6FF",
                stroke=spec.brand.brand_color if spec.brand else "#2563EB",
                frame_id=frame_id
            )

        elif spec.shape_type == SemanticShapeType.STREAMING_PIPE:
            topics = spec.metadata.get("topics", ["event.created", "event.processed", "event.settled"])
            return scene.add_streaming_pipe(
                x, y, w, h,
                title=spec.label,
                topics=topics,
                badge=spec.badge,
                is_hero=spec.is_hero,
                bg=spec.brand.bg_color if spec.brand else "#EEF2FF",
                stroke=spec.brand.brand_color if spec.brand else "#4F46E5",
                frame_id=frame_id
            )

        elif spec.shape_type == SemanticShapeType.SECURITY_BARRIER:
            rules = spec.metadata.get("rules", [
                "mTLS Mutual Authentication X.509",
                "Cloudflare DDoS & Global WAF",
                "Token-Bucket Rate Limiter"
            ])
            return scene.add_security_barrier(
                x, y, w, h,
                title=spec.label,
                rules=rules,
                badge=spec.badge,
                frame_id=frame_id
            )

        elif spec.shape_type == SemanticShapeType.ACTOR_PILL:
            return scene.add_actor_node(
                x, y, w, h,
                name=spec.label,
                role=spec.description or "USER / CLIENT",
                icon=spec.icon,
                is_hero=spec.is_hero,
                frame_id=frame_id
            )

        elif spec.shape_type == SemanticShapeType.DATA_VIZ_KPI:
            val = spec.metadata.get("kpi_value", "99.99%")
            unit = spec.metadata.get("kpi_unit", "SLA")
            sub = spec.metadata.get("kpi_sub", "High Availability")
            col = spec.brand.brand_color if spec.brand else "#059669"
            kpi_spec = KPICardSpec(val, unit, sub, col, spec.badge)
            return LightDataVizEngine.render_kpi_card(scene, x, y, w, h, kpi_spec, frame_id=frame_id)

        elif spec.is_hero or len(spec.description) > 60:
            bullets = [l.strip() for l in spec.description.split("\n") if l.strip()]
            if not bullets:
                bullets = [spec.description]
            return scene.add_feature_card(
                x, y, w, h,
                title=spec.label,
                bullets=bullets,
                badge=spec.badge,
                icon=spec.icon,
                is_hero=spec.is_hero,
                bg=bg_col,
                stroke=stroke_col,
                frame_id=frame_id
            )

        else:
            # Tarjeta Quad estándar con zonas limpias
            container, _ = scene.add_quad_card(
                x, y, w, h,
                title=spec.label,
                sublabel=spec.description,
                badge=spec.badge,
                icon=spec.icon,
                bg=bg_col,
                stroke=stroke_col,
                is_hero=spec.is_hero,
                frame_id=frame_id
            )
            return container

    @classmethod
    def compose_layered_board(cls, scene: ExcalidrawScene,
                              frame_title: str,
                              layers_spec: List[Dict[str, Any]],
                              fx: float, fy: float,
                              w: float = 1600.0,
                              frame_id: Optional[str] = None) -> str:
        """Compone un tablero arquitectónico por capas con componentes semánticos y auto-dimensionado."""
        if not frame_id:
            fid = scene.add_frame(frame_title, fx, fy, w, 600.0)
        else:
            fid = frame_id

        # Cabecera editorial del Frame
        scene.add_text(fx + 50.0, fy + 30.0, "VISUAL COMPOSITION INTELLIGENCE · LAYERED TOPOLOGY", font_size=12, font_family=2, color="#64748B", frame_id=fid)
        scene.add_text(fx + 50.0, fy + 52.0, frame_title, font_size=22, font_family=2, color="#0F172A", frame_id=fid)

        cur_y = fy + 100.0
        padding_x = 50.0
        usable_w = w - (padding_x * 2.0)

        for l_idx, layer in enumerate(layers_spec):
            layer_name = layer.get("name", f"CAPA {l_idx+1}")
            entities = layer.get("entities", [])
            if not entities:
                continue

            # Ribbon / Título de capa
            scene.add_rect(fx + padding_x, cur_y, usable_w, 28.0, bg="#F1F5F9", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=fid)
            scene.add_text(fx + padding_x + 14.0, cur_y + 7.0, layer_name.upper(), font_size=11, font_family=2, color="#334155", frame_id=fid)
            cur_y += 38.0

            # Renderizar entidades de la capa en cuadrícula responsiva
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

                spec = cls.analyze_entity(raw_e)
                cls.render_entity_node(scene, cx, cy, card_w, card_h, spec, frame_id=fid)

            rows = math.ceil(cnt / cols)
            cur_y += rows * (card_h + gap) + 15.0

        # Footer con leyenda
        scene.add_legend_footer(fx + padding_x, cur_y + 10.0, usable_w, swatches=[
            {"label": "Componente Core Hero", "bg": "#FFF5F2", "stroke": "#D93829"},
            {"label": "Infraestructura & Servicios", "bg": "#EFF6FF", "stroke": "#2563EB"}
        ], note="Visual Composition Intelligence: Despliegue semántico polimórfico sin colisiones.", frame_id=fid)

        # Ajuste ceñido final
        scene.auto_fit_frame(fid, padding=45.0)
        return fid
