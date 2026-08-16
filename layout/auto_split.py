"""
Sketion 3.4 — Motor de Particionado y Auto-Split Elástico (Fase 3 del Roadmap)
Detecta automáticamente la sobresaturación de información (nodos > 15 o densidad > 5.5/10)
y descompone el lienzo en marcos especializados coordinados.
"""

from typing import List, Dict, Any, Tuple, Optional


def should_auto_split(nodes_count: int, edges_count: int = 0, estimated_density: float = 0.0) -> bool:
    """
    Determina si un conjunto de entidades debe particionarse automáticamente en multi-frame
    para evitar colapsar la legibilidad visual.
    """
    if nodes_count > 15:
        return True
    if nodes_count > 10 and edges_count > 18:
        return True
    if estimated_density > 5.5:
        return True
    return False


def partition_entities_by_perspective(entities: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Clasifica y distribuye entidades en 4 dimensiones funcionales coordinadas:
    1. TOPOLOGY: Nodos de infraestructura, gateways, servicios core y almacenamiento.
    2. LIFECYCLE_FLOW: Pasos secuenciales, estados, transiciones y preemption.
    3. GOVERNANCE: Matrices de políticas, roles, restricciones y SLAs.
    4. METRICS: KPIs, métricas numéricas, conteos y alertas.
    """
    partitions: Dict[str, List[Dict[str, Any]]] = {
        "TOPOLOGY": [],
        "LIFECYCLE_FLOW": [],
        "GOVERNANCE": [],
        "METRICS": []
    }
    
    for ent in entities:
        cat = str(ent.get("category", "")).lower()
        role = str(ent.get("role", "")).lower()
        name = str(ent.get("name", "")).lower()
        
        if any(k in cat or k in role or k in name for k in ["kpi", "metrica", "rendimiento", "%", "tasa", "tiempo total", "throughput", "deficit"]):
            partitions["METRICS"].append(ent)
        elif any(k in cat or k in role or k in name for k in ["matriz", "tabla", "politica", "restriccion", "sla", "permiso", "horario"]):
            partitions["GOVERNANCE"].append(ent)
        elif any(k in cat or k in role or k in name for k in ["estado", "paso", "flujo", "secuencia", "transicion", "preemption", "journey"]):
            partitions["LIFECYCLE_FLOW"].append(ent)
        else:
            partitions["TOPOLOGY"].append(ent)
            
    return partitions


def compute_multi_frame_placements(frame_keys: List[str], base_width: float = 2800.0,
                                   base_height: float = 850.0, gap_y: float = 140.0) -> List[Dict[str, Any]]:
    """
    Calcula las coordenadas verticales coordinadas para una secuencia de marcos apilados.
    """
    placements = []
    current_y = 0.0
    
    for idx, key in enumerate(frame_keys):
        # Ajustar altura según tipo de marco
        if key == "METRICS":
            h = min(base_height, 700.0)
        elif key == "GOVERNANCE":
            h = min(base_height, 780.0)
        elif key == "TOPOLOGY":
            h = max(base_height, 950.0)
        else:
            h = base_height
            
        placements.append({
            "idx": idx,
            "key": key,
            "x": 0.0,
            "y": current_y,
            "width": base_width,
            "height": h
        })
        
        current_y += h + gap_y
        
    return placements
