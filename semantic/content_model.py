"""
Sketion Semantic Content Model (v11.0)
Estructura de datos tipada intermedia que desacopla la interpretación de lenguaje natural
del motor de composición gráfica y del layout solver.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


class SystemNodeType(Enum):
    SERVICE = "service"
    DATABASE = "database"
    QUEUE = "queue"
    ACTOR = "actor"
    SECURITY_GATE = "security_gate"
    INFRASTRUCTURE = "infrastructure"
    CONTAINER = "container"
    ANALYTICS = "analytics"


class RelationshipType(Enum):
    SYNC = "sync"
    ASYNC = "async"
    CRITICAL = "critical"
    RETRY_DLQ = "retry_dlq"
    TELEMETRY = "telemetry"
    MTLS = "mtls"
    DATA_FLOW = "data_flow"
    DEPENDENCY = "dependency"


@dataclass
class ActorSpec:
    id: str
    label: str
    role: str = "user"
    description: str = ""
    badge: Optional[str] = None


@dataclass
class SystemNodeSpec:
    id: str
    label: str
    node_type: SystemNodeType = SystemNodeType.SERVICE
    role: str = "service"
    description: str = ""
    layer_index: int = 0
    group: Optional[str] = None
    is_hero: bool = False
    badge: Optional[str] = None
    tech_tags: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class RelationshipSpec:
    source_id: str
    target_id: str
    relation_type: RelationshipType = RelationshipType.SYNC
    label: Optional[str] = None
    bidirectional: bool = False
    protocol: Optional[str] = None


@dataclass
class MetricSpec:
    label: str
    value: str
    change: Optional[str] = None
    is_positive: bool = True
    context: str = ""


@dataclass
class MilestoneSpec:
    id: str
    title: str
    date_or_sprint: str
    status: str = "pending"
    description: str = ""
    deliverables: List[str] = field(default_factory=list)


@dataclass
class ContentModel:
    """Modelo semántico intermedio desacoplado del motor de renderizado."""
    title: str
    goal: str = ""
    domain: str = "software"  # software, engineering, business, education, ux, agile, data
    composition_pattern_hint: Optional[str] = None
    complexity_level: str = "structured"  # simple, structured, narrative
    density: str = "medium"  # low, medium, high, very_high
    
    actors: List[ActorSpec] = field(default_factory=list)
    systems: List[SystemNodeSpec] = field(default_factory=list)
    relationships: List[RelationshipSpec] = field(default_factory=list)
    metrics: List[MetricSpec] = field(default_factory=list)
    timeline_milestones: List[MilestoneSpec] = field(default_factory=list)
    sections: List[Dict[str, Any]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Serializa el ContentModel a diccionario estándar JSON."""
        return {
            "title": self.title,
            "goal": self.goal,
            "domain": self.domain,
            "composition_pattern_hint": self.composition_pattern_hint,
            "complexity_level": self.complexity_level,
            "density": self.density,
            "actors": [{"id": a.id, "label": a.label, "role": a.role, "desc": a.description} for a in self.actors],
            "systems": [{"id": s.id, "label": s.label, "type": s.node_type.value, "is_hero": s.is_hero} for s in self.systems],
            "relationships": [{"from": r.source_id, "to": r.target_id, "type": r.relation_type.value, "label": r.label} for r in self.relationships],
            "metrics": [{"label": m.label, "value": m.value} for m in self.metrics],
            "milestones": [{"title": ml.title, "sprint": ml.date_or_sprint} for ml in self.timeline_milestones]
        }
