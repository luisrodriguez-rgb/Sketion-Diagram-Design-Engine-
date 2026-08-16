"""
Sketion Visual Classifier Engine (v8.1)
El orquestador central de la capa de Inteligencia Visual.
Recibe una entidad conceptual y determina su representación gráfica completa:
1. Forma Semántica (Cilindro, Tubería, Barrera, Diamante, Pastilla, Tarjeta)
2. Ícono Semántico
3. Insignia Inteligente (Métrica, Estado, Compliance, Riesgo)
4. Estilo de Borde y Relleno
5. Acompañamiento Visual (Affordances, Protocolos, Badges)
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, List
from .iconography import SemanticIconRegistry
from .status_metrics import StatusBadgeEngine, SemanticBadge, BadgeType
from .semantic_shapes import SemanticShapeClassifier, SemanticShapeSpec, SemanticShapeType


@dataclass
class VisualComponentSpec:
    entity_id: str
    label: str
    shape_spec: SemanticShapeSpec
    icon_name: str
    badge: SemanticBadge
    is_hero: bool
    affordances: List[str]
    suggested_width: float
    suggested_height: float


class VisualClassifierEngine:
    """Motor maestro de clasificación semántica-a-visual."""

    @classmethod
    def classify(cls, entity: Dict[str, Any], target_audience: str = "ENGINEERING") -> VisualComponentSpec:
        eid = str(entity.get("id", ""))
        lbl = str(entity.get("label", ""))
        dom = str(entity.get("domain", ""))
        is_hero = bool(entity.get("is_hero", False))

        # 1. Forma y Morfología Semántica
        shape_spec = SemanticShapeClassifier.classify_entity(lbl, domain=dom, is_hero=is_hero)

        # 2. Ícono Semántico
        icon_name = SemanticIconRegistry.resolve_icon(lbl)

        # 3. Badge Inteligente
        # Extraer badge sugerido o inferir según la audiencia y el dominio
        badge_text = entity.get("badge")
        if not badge_text:
            if shape_spec.shape_type == SemanticShapeType.DATABASE_CYLINDER:
                badge_text = "DATABASE"
            elif shape_spec.shape_type == SemanticShapeType.STREAMING_PIPE:
                badge_text = "STREAMING"
            elif shape_spec.shape_type == SemanticShapeType.SECURITY_BARRIER:
                badge_text = "ZERO-TRUST"
            elif shape_spec.shape_type == SemanticShapeType.DATA_VIZ_KPI:
                badge_text = "SLA METRIC"
            elif shape_spec.shape_type == SemanticShapeType.EXTERNAL_BOUNDARY:
                badge_text = "EXTERNAL"
            elif shape_spec.shape_type == SemanticShapeType.ACTOR_PILL:
                badge_text = "CLIENT"
            else:
                badge_text = dom if dom else "SERVICE"

        badge = StatusBadgeEngine.create_badge(badge_text)

        # 4. Affordances visuales según tipo
        affordances = []
        lbl_lower = lbl.lower()
        if "checkout" in lbl_lower or "payment" in lbl_lower:
            affordances = ["[Authorize]", "[Capture]", "[Refund]"]
        elif "api gateway" in lbl_lower or "kong" in lbl_lower:
            affordances = ["[GET] /v1/pay", "[POST] /tokens"]
        elif "idempotency" in lbl_lower:
            affordances = ["SETNX Key: 24h"]

        # 5. Dimensiones Sugeridas según Forma
        w_map = {
            SemanticShapeType.DATABASE_CYLINDER: 240.0,
            SemanticShapeType.STREAMING_PIPE: 480.0,
            SemanticShapeType.SECURITY_BARRIER: 320.0,
            SemanticShapeType.DECISION_DIAMOND: 160.0,
            SemanticShapeType.ACTOR_PILL: 220.0,
            SemanticShapeType.DATA_VIZ_KPI: 200.0,
            SemanticShapeType.EXTERNAL_BOUNDARY: 240.0,
            SemanticShapeType.STANDARD_CARD: 240.0
        }
        h_map = {
            SemanticShapeType.DATABASE_CYLINDER: 130.0,
            SemanticShapeType.STREAMING_PIPE: 100.0,
            SemanticShapeType.SECURITY_BARRIER: 280.0,
            SemanticShapeType.DECISION_DIAMOND: 140.0,
            SemanticShapeType.ACTOR_PILL: 65.0,
            SemanticShapeType.DATA_VIZ_KPI: 110.0,
            SemanticShapeType.EXTERNAL_BOUNDARY: 110.0,
            SemanticShapeType.STANDARD_CARD: 120.0
        }

        s_w = w_map.get(shape_spec.shape_type, 240.0)
        s_h = h_map.get(shape_spec.shape_type, 120.0)
        if is_hero:
            s_w = max(s_w, 280.0)
            s_h = max(s_h, 135.0)

        return VisualComponentSpec(
            entity_id=eid,
            label=lbl,
            shape_spec=shape_spec,
            icon_name=icon_name,
            badge=badge,
            is_hero=is_hero,
            affordances=affordances,
            suggested_width=s_w,
            suggested_height=s_h
        )
