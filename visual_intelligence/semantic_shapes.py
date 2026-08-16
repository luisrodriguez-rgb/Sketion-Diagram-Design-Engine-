"""
Sketion Semantic Shapes Classifier (v8.1)
Clasifica cualquier entidad conceptual en su representación morfológica óptima:
- DATABASE_CYLINDER: Bases de datos relacionales, columnares, caches (PostgreSQL, ClickHouse, Redis).
- STREAMING_PIPE: Tuberías de streaming y colas de mensajes (Kafka, RabbitMQ, SQS, Flink).
- SECURITY_BARRIER: Barreras Zero-Trust, WAF, Firewalls perimetrales y Bóvedas HSM.
- DECISION_DIAMOND: Puntos de bifurcación condicional, filtros y enrutadores lógicos.
- ACTOR_PILL: Clientes web, SDKs móviles, usuarios, administradores.
- METRIC_CARD: Indicadores clave de rendimiento, SLAs y gauges.
- ACTION_AFFORDANCE: Controles visuales [Authorize], [Capture], [GET /payments].
- EXTERNAL_BOUNDARY: Sistemas externos o bancos con límite discontinuo.
- DATA_VIZ_KPI: Bloques de visualización de datos cuantitativos.
- STANDARD_CARD: Servicios y componentes de lógica general.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, Optional, List


class SemanticShapeType(Enum):
    DATABASE_CYLINDER = "DATABASE_CYLINDER"
    STREAMING_PIPE = "STREAMING_PIPE"
    SECURITY_BARRIER = "SECURITY_BARRIER"
    DECISION_DIAMOND = "DECISION_DIAMOND"
    ACTOR_PILL = "ACTOR_PILL"
    METRIC_CARD = "METRIC_CARD"
    ACTION_AFFORDANCE = "ACTION_AFFORDANCE"
    EXTERNAL_BOUNDARY = "EXTERNAL_BOUNDARY"
    DATA_VIZ_KPI = "DATA_VIZ_KPI"
    DATA_VIZ_FUNNEL = "DATA_VIZ_FUNNEL"
    STANDARD_CARD = "STANDARD_CARD"


@dataclass
class SemanticShapeSpec:
    shape_type: SemanticShapeType
    primary_icon: str
    accent_color: str
    bg_color: str
    border_style: str  # "solid", "dashed", "double"
    has_affordances: bool = False
    affordance_labels: Optional[List[str]] = None


class SemanticShapeClassifier:
    """Clasificador semántico que asigna la forma visual óptima a cada entidad."""

    @classmethod
    def classify_entity(cls, label: str, domain: Optional[str] = None, is_hero: bool = False) -> SemanticShapeSpec:
        lbl = label.lower().strip()
        dom = (domain or "").upper().strip()

        # 1. Base de Datos / Storage -> DATABASE_CYLINDER
        db_keywords = ["postgres", "aurora", "mysql", "database", "clickhouse", "s3", "minio", "dynamo", "redis", "db", "warehouse", "storage", "lakehouse"]
        if any(w in lbl or w in dom.lower() for w in db_keywords):
            return SemanticShapeSpec(
                shape_type=SemanticShapeType.DATABASE_CYLINDER,
                primary_icon="database",
                accent_color="#D93829" if is_hero else "#2563EB",
                bg_color="#FFF5F2" if is_hero else "#EFF6FF",
                border_style="solid"
            )

        # 2. Streaming / Queues -> STREAMING_PIPE
        if any(w in lbl for w in ["kafka", "stream", "flink", "rabbitmq", "queue", "event bus", "sqs", "pulsar"]):
            return SemanticShapeSpec(
                shape_type=SemanticShapeType.STREAMING_PIPE,
                primary_icon="terminal",
                accent_color="#D93829" if is_hero else "#4F46E5",
                bg_color="#FFF5F2" if is_hero else "#EEF2FF",
                border_style="solid"
            )

        # 3. Seguridad / WAF / Firewalls -> SECURITY_BARRIER
        if any(w in lbl for w in ["waf", "ddos", "firewall", "cloudflare", "mtls", "tokenizer vault", "hsm", "secret vault"]):
            return SemanticShapeSpec(
                shape_type=SemanticShapeType.SECURITY_BARRIER,
                primary_icon="shield",
                accent_color="#D93829" if is_hero else "#64748B",
                bg_color="#FFF5F2" if is_hero else "#F8FAFC",
                border_style="dashed"
            )

        # 4. Actores / Clientes -> ACTOR_PILL
        if any(w in lbl for w in ["web client", "ios", "android", "pos", "whatsapp", "user", "customer", "admin dashboard", "dispute desk"]):
            return SemanticShapeSpec(
                shape_type=SemanticShapeType.ACTOR_PILL,
                primary_icon="users" if "desk" in lbl or "whatsapp" in lbl else ("card" if "pos" in lbl else "laptop"),
                accent_color="#D93829" if is_hero else "#2563EB",
                bg_color="#FFF5F2" if is_hero else "#FFFFFF",
                border_style="solid"
            )

        # 5. Métricas & SLAs -> METRIC_CARD / DATA_VIZ_KPI
        if any(w in lbl for w in ["sla:", "latencia:", "throughput:", "volumen:", "uptime", "tps", "p99", "kpi"]):
            return SemanticShapeSpec(
                shape_type=SemanticShapeType.DATA_VIZ_KPI,
                primary_icon="laptop" if "latencia" in lbl else ("server" if "sla" in lbl else "database"),
                accent_color="#059669" if "sla" in lbl else ("#2563EB" if "latencia" in lbl else "#D97706"),
                bg_color="#F0FDF4" if "sla" in lbl else ("#EFF6FF" if "latencia" in lbl else "#FEF3C7"),
                border_style="solid"
            )

        # 6. Sistemas Externos & Redes Bancarias -> EXTERNAL_BOUNDARY
        if any(w in lbl for w in ["visa", "mastercard", "ach", "sepa", "pix", "pse", "sap erp", "dian", "pagerduty"]):
            return SemanticShapeSpec(
                shape_type=SemanticShapeType.EXTERNAL_BOUNDARY,
                primary_icon="card" if "visa" in lbl or "pix" in lbl else "server",
                accent_color="#D93829" if is_hero else "#64748B",
                bg_color="#FFF5F2" if is_hero else "#F8FAFC",
                border_style="dashed"
            )

        # 7. Fallback General -> STANDARD_CARD
        return SemanticShapeSpec(
            shape_type=SemanticShapeType.STANDARD_CARD,
            primary_icon="server",
            accent_color="#D93829" if is_hero else "#2563EB",
            bg_color="#FFF5F2" if is_hero else "#FFFFFF",
            border_style="solid"
        )
