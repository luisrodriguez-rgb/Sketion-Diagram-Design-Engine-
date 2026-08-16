"""
Sketion Visual Intelligence Layer (v8.1)
Capa de representación semántica visual montada sobre la tríada congelada
(Composition + Information Architecture + Rendering).

Transforma:
"qué mostrar -> dónde -> cómo conectar -> CÓMO REPRESENTARLO VISUALMENTE SEGÚN SU NATURALEZA"
"""

from .iconography import SemanticIconRegistry, IconCategory
from .status_metrics import (
    BadgeType,
    SemanticBadge,
    StatusBadgeEngine,
    MetricPillEngine
)
from .semantic_shapes import (
    SemanticShapeType,
    SemanticShapeSpec,
    SemanticShapeClassifier
)
from .semantic_connectors import (
    ConnectorSemantics,
    SemanticConnectorSpec,
    SemanticConnectorRouter
)
from .data_viz import (
    DataVizType,
    KPICardSpec,
    ComparisonBarSpec,
    FunnelStepSpec,
    LightDataVizEngine
)
from .visual_classifier import (
    VisualComponentSpec,
    VisualClassifierEngine
)

__all__ = [
    "SemanticIconRegistry",
    "IconCategory",
    "BadgeType",
    "SemanticBadge",
    "StatusBadgeEngine",
    "MetricPillEngine",
    "SemanticShapeType",
    "SemanticShapeSpec",
    "SemanticShapeClassifier",
    "ConnectorSemantics",
    "SemanticConnectorSpec",
    "SemanticConnectorRouter",
    "DataVizType",
    "KPICardSpec",
    "ComparisonBarSpec",
    "FunnelStepSpec",
    "LightDataVizEngine",
    "VisualComponentSpec",
    "VisualClassifierEngine"
]
