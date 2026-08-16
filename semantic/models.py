"""
Sketion Semantic Models (v2.6)
Estructuras de datos intermedias tipadas con soporte de Doble Jerarquía, Scopes y Output Presets.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Any, Optional

class DetailLevel(str, Enum):
    SIMPLE = "simple"       # <= 7 nodos, labels cortos, máxima claridad
    BALANCED = "balanced"   # <= 12-15 nodos, subcomponentes, contexto equilibrado
    DETAILED = "detailed"   # Arquitectura exhaustiva, metadata, réplicas, colas

class OutputPreset(str, Enum):
    PRESENTATION = "presentation" # 16:9 (1600x900), fuentes grandes (+30%), baja densidad
    DOCS = "docs"                 # Compacto (1200x650), balanceado para README/Wiki
    DEEP_DIVE = "deep_dive"       # Canvas amplio (1800x1000), alto contexto
    SOCIAL_OG = "social_og"       # 1200x630 (Twitter/LinkedIn card)
    MOBILE = "mobile"             # Formato vertical (900x1600)
    A4 = "a4"                     # Proporción hoja vertical

@dataclass
class Scope:
    """Zona o contenedor de ámbito semántico (ej. EDGE, CORE SERVICES, DATA)."""
    id: str
    label: str
    role: str = "internal"  # internal, external, secure_boundary, data_layer
    node_ids: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class SemanticNode:
    """Nodo con soporte para anatomía de Doble Jerarquía (Title + Mono Sublabel + Metadata)."""
    id: str
    label: str                          # Título principal (Sans Bold)
    sublabel: Optional[str] = None      # Rol o descripción técnica (Cascadia Mono)
    metadata: Optional[str] = None      # Puerto (:8080), protocolo o tag
    role: str = "core"                  # entrypoint, core, storage, gateway, external
    scope_id: Optional[str] = None      # ID del Scope que contiene a este nodo
    is_hero: bool = False
    is_pain: bool = False
    extra: Dict[str, Any] = field(default_factory=dict)

@dataclass
class SemanticEdge:
    from_node: str
    to_node: str
    label: Optional[str] = None
    dashed: bool = False
    is_bidirectional: bool = False

@dataclass
class SemanticFlowStep:
    step_num: str
    label: str
    sublabel: Optional[str] = None
    is_hero: bool = False
    is_pain: bool = False
    edge_label: Optional[str] = None

@dataclass
class SemanticTreeBranch:
    title: str
    subitems: List[str] = field(default_factory=list)
    is_accent: bool = False

@dataclass
class SemanticLane:
    title: str
    items: List[str] = field(default_factory=list)

@dataclass
class SemanticMetric:
    number: str
    label: str
    is_accent: bool = False

@dataclass
class SemanticDiagram:
    title: str
    semantic_type: str
    detail_level: DetailLevel = DetailLevel.BALANCED
    output_preset: OutputPreset = OutputPreset.DOCS
    engine: str = "red"
    scopes: List[Scope] = field(default_factory=list)
    nodes: List[SemanticNode] = field(default_factory=list)
    edges: List[SemanticEdge] = field(default_factory=list)
    steps: List[SemanticFlowStep] = field(default_factory=list)
    branches: List[SemanticTreeBranch] = field(default_factory=list)
    lanes: List[SemanticLane] = field(default_factory=list)
    metrics: List[SemanticMetric] = field(default_factory=list)
    headers: List[str] = field(default_factory=list)
    rows: List[Dict[str, Any]] = field(default_factory=list)
    center_text: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "semantic_type": self.semantic_type,
            "detail_level": self.detail_level.value if isinstance(self.detail_level, DetailLevel) else self.detail_level,
            "output_preset": self.output_preset.value if isinstance(self.output_preset, OutputPreset) else self.output_preset,
            "engine": self.engine,
            "scopes": [s.__dict__ for s in self.scopes],
            "nodes": [n.__dict__ for n in self.nodes],
            "edges": [e.__dict__ for e in self.edges],
            "steps": [s.__dict__ for s in self.steps],
            "branches": [b.__dict__ for b in self.branches],
            "lanes": [l.__dict__ for l in self.lanes],
            "metrics": [m.__dict__ for m in self.metrics],
            "headers": self.headers,
            "rows": self.rows,
            "center_text": self.center_text,
            "metadata": self.metadata
        }
