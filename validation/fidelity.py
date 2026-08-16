"""
Sketion Semantic Fidelity Engine
Evalúa la fidelidad entre el modelo semántico de entrada (SemanticDiagram)
y la escena renderizada en Excalidraw:
- Node Coverage (¿Todos los nodos pedidos están presentes?)
- Edge Coverage (¿Todas las relaciones fueron trazadas?)
- Scope Coverage (¿Todas las zonas/scopes fueron creadas?)
- Hierarchy Fidelity (¿El nodo héroe retuvo el color de acento?)
- Label Fidelity (¿Se preservaron los títulos y subetiquetas técnicas?)
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Set
from semantic.models import SemanticDiagram

@dataclass
class SemanticFidelityMetrics:
    node_coverage_score: int
    edge_coverage_score: int
    scope_coverage_score: int
    hierarchy_fidelity_score: int
    overall_fidelity_score: int
    missing_nodes: List[str] = field(default_factory=list)
    missing_edges: List[str] = field(default_factory=list)
    missing_scopes: List[str] = field(default_factory=list)
    issues: List[str] = field(default_factory=list)

    def report_table(self) -> str:
        lines = [
            "SEMANTIC FIDELITY SCORE",
            "─────────────────────────────────",
            f"Node Coverage        : {self.node_coverage_score}/100",
            f"Edge Coverage        : {self.edge_coverage_score}/100",
            f"Scope Coverage       : {self.scope_coverage_score}/100",
            f"Hierarchy Fidelity   : {self.hierarchy_fidelity_score}/100",
            "─────────────────────────────────",
            f"OVERALL FIDELITY     : {self.overall_fidelity_score}/100"
        ]
        if self.issues:
            lines.append("\n[DESVIACIONES SEMÁNTICAS]:")
            for issue in self.issues:
                lines.append(f"  ⚠️ {issue}")
        return "\n".join(lines)


def calculate_semantic_fidelity(diagram: SemanticDiagram, scene_data: Dict[str, Any]) -> SemanticFidelityMetrics:
    """Compara el SemanticDiagram original con la escena Excalidraw generada."""
    elements = scene_data.get("elements", [])
    issues = []

    # 1. Node Coverage
    rendered_texts = [e.get("text", "") for e in elements if e.get("type") == "text"]
    all_rendered_text = " ".join(rendered_texts)

    missing_nodes = []
    expected_nodes = diagram.nodes or []
    for node in expected_nodes:
        if node.label not in all_rendered_text:
            missing_nodes.append(node.id)
            issues.append(f"Nodo faltante o etiqueta no renderizada: '{node.label}' ({node.id})")

    node_coverage = 100
    if expected_nodes:
        node_coverage = int(((len(expected_nodes) - len(missing_nodes)) / len(expected_nodes)) * 100)

    # 2. Scope Coverage
    missing_scopes = []
    expected_scopes = diagram.scopes or []
    for scope in expected_scopes:
        if scope.label.upper() not in all_rendered_text.upper():
            missing_scopes.append(scope.id)
            issues.append(f"Scope / Zona faltante en el canvas: '{scope.label}'")

    scope_coverage = 100
    if expected_scopes:
        scope_coverage = int(((len(expected_scopes) - len(missing_scopes)) / len(expected_scopes)) * 100)

    # 3. Edge Coverage
    rendered_arrows = [e for e in elements if e.get("type") == "arrow"]
    expected_edges = diagram.edges or []
    missing_edges = []
    
    # Comprobar conteo mínimo de flechas respecto a lo esperado
    if len(rendered_arrows) < len(expected_edges):
        missing_count = len(expected_edges) - len(rendered_arrows)
        issues.append(f"Faltan {missing_count} conectores/flechas en la escena renderizada.")
        edge_coverage = int((len(rendered_arrows) / max(1, len(expected_edges))) * 100)
    else:
        edge_coverage = 100

    # 4. Hierarchy Fidelity (Hero Node Preservation)
    hierarchy_score = 100
    heroes = [n for n in expected_nodes if n.is_hero]
    accent_cards = [
        e for e in elements
        if e.get("type") == "rectangle" and ("#2563EB" in str(e.get("strokeColor", "")) or "#2563EB" in str(e.get("backgroundColor", "")))
    ]
    if heroes and len(accent_cards) == 0:
        hierarchy_score -= 25
        issues.append("El nodo declarado como héroe ('is_hero=True') no recibió color de acento visual.")

    # Overall Weighted Fidelity
    overall = int(
        node_coverage * 0.40 +
        edge_coverage * 0.30 +
        scope_coverage * 0.15 +
        hierarchy_score * 0.15
    )
    overall = max(0, min(100, overall))

    return SemanticFidelityMetrics(
        node_coverage_score=node_coverage,
        edge_coverage_score=edge_coverage,
        scope_coverage_score=scope_coverage,
        hierarchy_fidelity_score=hierarchy_score,
        overall_fidelity_score=overall,
        missing_nodes=missing_nodes,
        missing_edges=missing_edges,
        missing_scopes=missing_scopes,
        issues=issues
    )
