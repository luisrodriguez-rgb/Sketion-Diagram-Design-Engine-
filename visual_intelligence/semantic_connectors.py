"""
Sketion Semantic Connectors Engine (v8.1)
Gestiona la semántica visual de los conectores en la arquitectura:
- SYNC_SOLID: Línea sólida azul (#2563EB) para llamadas HTTP/gRPC sincrónicas.
- ASYNC_DASHED: Línea punteada índigo (#4F46E5) para eventos asíncronos en Kafka/colas.
- CRITICAL_DOUBLE: Línea gruesa hero (#D93829) para el flujo financiero principal.
- FAILURE_RED: Línea punteada roja (#DC2626) para excepciones, DLQ y reintentos.
- SUCCESS_GREEN: Línea verde sólida (#059669) para confirmaciones y conciliación exitosa.
- OPTIONAL_GRAY: Línea gris punteada (#94A3B8) para telemetría, métricas y logs.
- BIDIRECTIONAL: Flechas en ambos extremos para sincronización mTLS o doble sentido.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, Optional


class ConnectorSemantics(Enum):
    SYNC_SOLID = "SYNC_SOLID"
    ASYNC_DASHED = "ASYNC_DASHED"
    CRITICAL_DOUBLE = "CRITICAL_DOUBLE"
    FAILURE_RED = "FAILURE_RED"
    SUCCESS_GREEN = "SUCCESS_GREEN"
    OPTIONAL_GRAY = "OPTIONAL_GRAY"
    BIDIRECTIONAL = "BIDIRECTIONAL"


@dataclass
class SemanticConnectorSpec:
    semantics: ConnectorSemantics
    stroke_color: str
    stroke_width: float
    is_dashed: bool
    label_prefix: Optional[str] = None
    bidirectional: bool = False


class SemanticConnectorRouter:
    """Enrutador de estilos de conectores según la relación arquitectónica."""

    _STYLES = {
        ConnectorSemantics.SYNC_SOLID: SemanticConnectorSpec(ConnectorSemantics.SYNC_SOLID, "#2563EB", 1.5, False, "SYNC"),
        ConnectorSemantics.ASYNC_DASHED: SemanticConnectorSpec(ConnectorSemantics.ASYNC_DASHED, "#4F46E5", 1.5, True, "ASYNC"),
        ConnectorSemantics.CRITICAL_DOUBLE: SemanticConnectorSpec(ConnectorSemantics.CRITICAL_DOUBLE, "#D93829", 2.2, False, "CORE FLOW"),
        ConnectorSemantics.FAILURE_RED: SemanticConnectorSpec(ConnectorSemantics.FAILURE_RED, "#DC2626", 1.5, True, "ERROR / DLQ"),
        ConnectorSemantics.SUCCESS_GREEN: SemanticConnectorSpec(ConnectorSemantics.SUCCESS_GREEN, "#059669", 1.8, False, "CONFIRMED"),
        ConnectorSemantics.OPTIONAL_GRAY: SemanticConnectorSpec(ConnectorSemantics.OPTIONAL_GRAY, "#94A3B8", 1.0, True, "TELEMETRY"),
        ConnectorSemantics.BIDIRECTIONAL: SemanticConnectorSpec(ConnectorSemantics.BIDIRECTIONAL, "#0F172A", 1.5, False, "mTLS", bidirectional=True)
    }

    @classmethod
    def get_style(cls, relation_type: str) -> SemanticConnectorSpec:
        rel = relation_type.lower().strip()
        if any(w in rel for w in ["async", "kafka", "queue", "event", "publish", "subscribe", "stream"]):
            return cls._STYLES[ConnectorSemantics.ASYNC_DASHED]
        if any(w in rel for w in ["error", "fail", "dlq", "timeout", "circuit", "rollback", "retry"]):
            return cls._STYLES[ConnectorSemantics.FAILURE_RED]
        if any(w in rel for w in ["success", "settle", "confirm", "reconcile", "cleared"]):
            return cls._STYLES[ConnectorSemantics.SUCCESS_GREEN]
        if any(w in rel for w in ["hero", "critical", "pci", "payment", "money", "transfer"]):
            return cls._STYLES[ConnectorSemantics.CRITICAL_DOUBLE]
        if any(w in rel for w in ["log", "metric", "telemetry", "prometheus", "audit", "trace"]):
            return cls._STYLES[ConnectorSemantics.OPTIONAL_GRAY]
        if any(w in rel for w in ["mtls", "sync_both", "duplex", "handshake"]):
            return cls._STYLES[ConnectorSemantics.BIDIRECTIONAL]

        return cls._STYLES[ConnectorSemantics.SYNC_SOLID]
