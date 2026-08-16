"""
Sketion 4.0 — Catálogo Maestro Unificado de los 27 Tipos Visuales (engines/catalog.py)
Registra, mapea y despacha la generación de cualquiera de los 27 tipos de diagramas.
"""

from typing import Dict, Any, Callable, List
from .data_types import (
    render_medallion, render_data_flow, render_dp_integration,
    render_dp_security_matrix, render_er_model
)
from .strategy_types import (
    render_consultant_2x2, render_quadrant, render_loop_flywheel,
    render_it_current_state, render_venn, render_pyramid_funnel
)
from .software_types import (
    render_architecture, render_high_level, render_sequence,
    render_state_machine, render_layer_stack, render_nested, render_flowchart
)
from .operations_types import (
    render_swimlane, render_process, render_gantt,
    render_timeline, render_org_chart, render_tree
)
from .dataviz_types import (
    render_bar_chart, render_line_chart, render_scatter_plot, render_radar_spider
)

VISUAL_TYPES_CATALOG: Dict[str, Dict[str, Any]] = {
    # 1. DATA & LAKEHOUSE
    "medallion": {
        "name": "Medallion Lakehouse",
        "family": "Data & Storage",
        "desc": "Almacenamiento multi-tier (Raw -> Bronze -> Silver -> Gold)",
        "render_fn": render_medallion
    },
    "data_flow": {
        "name": "Role-Scoped Data Flow",
        "family": "Data & Storage",
        "desc": "Pipeline analítico con carriles por rol funcional",
        "render_fn": render_data_flow
    },
    "dp_integration": {
        "name": "Data Platform Integration",
        "family": "Data & Storage",
        "desc": "Fuentes heterogéneas -> Core Platform -> Consumidores",
        "render_fn": render_dp_integration
    },
    "dp_security_matrix": {
        "name": "Data Platform Security Matrix",
        "family": "Data & Storage",
        "desc": "Matriz de control de acceso RBAC granular",
        "render_fn": render_dp_security_matrix
    },
    "er_model": {
        "name": "Entity-Relationship Data Model",
        "family": "Data & Storage",
        "desc": "Modelo de datos relacional con claves PK y FK",
        "render_fn": render_er_model
    },

    # 2. ESTRATEGIA & CONSULTORÍA
    "consultant_2x2": {
        "name": "Consultant 2x2 Scenario Matrix",
        "family": "Estrategia & Negocio",
        "desc": "Matriz de 4 cuadrantes con nombres de celdas",
        "render_fn": render_consultant_2x2
    },
    "quadrant": {
        "name": "Quadrant Cartesian Positioning",
        "family": "Estrategia & Negocio",
        "desc": "Posicionamiento bidimensional de impacto vs esfuerzo",
        "render_fn": render_quadrant
    },
    "loop_flywheel": {
        "name": "Flywheel Growth Loop",
        "family": "Estrategia & Negocio",
        "desc": "Bucle continuo con estaciones alrededor de un hub",
        "render_fn": render_loop_flywheel
    },
    "it_current_state": {
        "name": "IT Current-State Modernization",
        "family": "Estrategia & Negocio",
        "desc": "Diagnóstico de silos legados vs plataforma unificada",
        "render_fn": render_it_current_state
    },
    "venn": {
        "name": "Venn Overlap Diagram",
        "family": "Estrategia & Negocio",
        "desc": "Superposición conceptual y conjuntos intersecados",
        "render_fn": render_venn
    },
    "pyramid_funnel": {
        "name": "Pyramid & Conversion Funnel",
        "family": "Estrategia & Negocio",
        "desc": "Jerarquía piramidal de capas y embudo de conversión",
        "render_fn": render_pyramid_funnel
    },

    # 3. SOFTWARE & NUBE
    "architecture": {
        "name": "Distributed System Architecture",
        "family": "Software & Nube",
        "desc": "Microservicios, boundaries de red y VPCs",
        "render_fn": render_architecture
    },
    "high_level": {
        "name": "High-Level Cluster Stack",
        "family": "Software & Nube",
        "desc": "Stack completo de infraestructura con orquestador",
        "render_fn": render_high_level
    },
    "sequence": {
        "name": "Sequence Diagram",
        "family": "Software & Nube",
        "desc": "Mensajes cronológicos con lifelines y cajas de activación",
        "render_fn": render_sequence
    },
    "state_machine": {
        "name": "State Machine Transitions",
        "family": "Software & Nube",
        "desc": "Máquina de estados finitos y transiciones de ciclo de vida",
        "render_fn": render_state_machine
    },
    "layer_stack": {
        "name": "Technology Layer Stack",
        "family": "Software & Nube",
        "desc": "Pila de capas de abstracción tecnológica",
        "render_fn": render_layer_stack
    },
    "nested": {
        "name": "Nested Scope Hierarchy",
        "family": "Software & Nube",
        "desc": "Jerarquía de contención física y scopes anidados",
        "render_fn": render_nested
    },
    "flowchart": {
        "name": "Logic Decision Flowchart",
        "family": "Software & Nube",
        "desc": "Flujograma con nodos de decisión y bifurcación",
        "render_fn": render_flowchart
    },

    # 4. PROCESOS & OPERACIONES
    "swimlane": {
        "name": "Cross-Functional Swimlane",
        "family": "Procesos & Operaciones",
        "desc": "Carriles horizontales y verticales por departamento",
        "render_fn": render_swimlane
    },
    "process": {
        "name": "Multi-Actor Sequential Process",
        "family": "Procesos & Operaciones",
        "desc": "Proceso secuencial de negocio con traspasos (handoffs)",
        "render_fn": render_process
    },
    "gantt": {
        "name": "Gantt Timeline Schedule",
        "family": "Procesos & Operaciones",
        "desc": "Cronograma de tareas con fechas y gates de aprobación",
        "render_fn": render_gantt
    },
    "timeline": {
        "name": "Strategic Milestone Timeline",
        "family": "Procesos & Operaciones",
        "desc": "Eje cronológico con hitos alternados arriba y abajo",
        "render_fn": render_timeline
    },
    "org_chart": {
        "name": "Organizational Ownership Chart",
        "family": "Procesos & Operaciones",
        "desc": "Organigrama de liderazgo y enrutamiento de equipos",
        "render_fn": render_org_chart
    },
    "tree": {
        "name": "Balanced Hierarchical Tree",
        "family": "Procesos & Operaciones",
        "desc": "Taxonomía de árbol balanceado de clasificación",
        "render_fn": render_tree
    },

    # 5. DATAVIZ NATIVO
    "bar_chart": {
        "name": "Categorical Bar Chart",
        "family": "DataViz Cuantitativo",
        "desc": "Gráfico de barras cuantitativas con acento focal",
        "render_fn": render_bar_chart
    },
    "line_chart": {
        "name": "Time Series Line Chart",
        "family": "DataViz Cuantitativo",
        "desc": "Tendencias temporales continuas con series múltiples",
        "render_fn": render_line_chart
    },
    "scatter_plot": {
        "name": "Distribution Scatter Plot",
        "family": "DataViz Cuantitativo",
        "desc": "Dispersión y correlación en plano cartesiano",
        "render_fn": render_scatter_plot
    },
    "radar_spider": {
        "name": "Multi-Axis Radar Spider",
        "family": "DataViz Cuantitativo",
        "desc": "Comparativa multieje poligonal concéntrica",
        "render_fn": render_radar_spider
    }
}


def list_all_visual_types() -> List[Dict[str, str]]:
    """Retorna la lista de todos los 27 tipos visuales registrados con su metadata."""
    types_list = []
    for key, val in VISUAL_TYPES_CATALOG.items():
        types_list.append({
            "key": key,
            "name": val["name"],
            "family": val["family"],
            "desc": val["desc"]
        })
    return types_list


def get_visual_type(key: str) -> Dict[str, Any]:
    """Retorna la definición y función de renderizado del tipo visual solicitado."""
    k = key.lower().strip()
    if k in VISUAL_TYPES_CATALOG:
        return VISUAL_TYPES_CATALOG[k]
    # Búsqueda difusa
    for catalog_key, val in VISUAL_TYPES_CATALOG.items():
        if catalog_key in k or k in catalog_key:
            return val
    return VISUAL_TYPES_CATALOG["architecture"]
