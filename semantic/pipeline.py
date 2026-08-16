"""
Sketion 3.4 — Pipeline Semántico y Parser de Audiencia (Fase 2 del Roadmap)
Transforma texto crudo no estructurado en un modelo semántico tipado (SemanticDiagram),
infiriendo automáticamente la audiencia destinataria, seleccionando el arquetipo visual óptimo
y aplicando filtros de información por rol.
"""

import re
from typing import Dict, Any, List, Optional, Tuple
from .models import (
    SemanticDiagram, SemanticNode, SemanticEdge, Scope,
    DetailLevel, OutputPreset, SemanticFlowStep, SemanticMetric
)
from engines.audience import get_audience_profile, AudienceProfile, filter_information_for_audience, AUDIENCE_CATALOG


def infer_audience_from_text(text: str) -> str:
    """Infiere el perfil de audiencia a partir de patrones lingüísticos y palabras clave en el prompt."""
    t = text.lower()
    
    # Patrones para CEO / Directivo / Junta
    if any(k in t for k in ["ceo", "directivo", "director general", "junta directiva", "cfo", "inversionistas", "ejecutivo", "roi", "capex", "opex", "estrategia"]):
        return "CEO_BOARD"
    
    # Patrones para Gerente de Operaciones / Planta
    if any(k in t for k in ["operaciones", "jefe de planta", "planta", "takt", "cuello de botella", "fila fisica", "cajero", "cocina", "receso", "batching", "turnos"]):
        return "OPERATIONS"
    
    # Patrones para Equipo de Producto / Diseñadores
    if any(k in t for k in ["producto", "product manager", "ux", "ui", "journey", "app movil", "pantalla", "kds", "casillero", "interfaz"]):
        return "PRODUCT_TECH"
    
    # Patrones para Desarrolladores / API Docs
    if any(k in t for k in ["desarrolladores", "developers", "devs", "api", "json", "endpoints", "schema", "idempotency", "grpc", "http", "swagger"]):
        return "DEV_DOCS"
    
    # Patrones para Pitch Deck / Inversores
    if any(k in t for k in ["pitch", "inversores", "deck", "tam", "traccion", "mercado", "5 minutos"]):
        return "INVESTOR_PITCH"
    
    # Default equilibrado
    return "CEO_BOARD"


def infer_topology_from_text(text: str) -> str:
    """Infiere la topología del problema (Duelo, Secuencia, Red Distribuida, Matriz, Jerarquía)."""
    t = text.lower()
    
    if any(k in t for k in ["actualmente", "actual", "antes vs despues", "as-is", "to-be", "legacy", "friccion", " vs ", "transformacion", "comparativa"]):
        return "DUEL_VS"
    elif any(k in t for k in ["paso 1", "fases", "primero", "luego", "secuencia", "journey", "etapas"]):
        return "SEQUENCE_FLOW"
    elif any(k in t for k in ["nivel 1", "nivel 2", "jerarquia", "divisiones", "zoom", "subsistema"]):
        return "DEEP_HIERARCHY"
    elif any(k in t for k in ["microservicios", "cluster", "kafka", "ledger", "gateway", "distribuida"]):
        return "DISTRIBUTED_NETWORK"
    elif any(k in t for k in ["matriz", "tabla", "politicas", "restricciones", "takt time", "horarios"]):
        return "MATRIX_TABLE"
    else:
        return "DISTRIBUTED_NETWORK"


def select_optimal_archetype(topology: str, audience_profile: AudienceProfile) -> str:
    """Selecciona el arquetipo visual óptimo cruzando la topología del problema con el perfil de audiencia."""
    p_archetypes = audience_profile.primary_archetypes
    
    if topology == "DUEL_VS":
        return "D" if "D" in p_archetypes else p_archetypes[0]
    elif topology == "SEQUENCE_FLOW":
        if audience_profile.role == "PRODUCT_TECH":
            return "C"  # User Journey 1:1
        elif audience_profile.role == "OPERATIONS":
            return "E"  # Swimlanes / Planta
        else:
            return "B"  # Fases con numerales
    elif topology == "DEEP_HIERARCHY":
        return "T" if "T" in p_archetypes else "J"
    elif topology == "MATRIX_TABLE":
        return "S" if "S" in p_archetypes else "H"
    else:
        return p_archetypes[0]


def parse_prompt_to_semantic_diagram(prompt_text: str, audience_override: Optional[str] = None) -> SemanticDiagram:
    """
    Parser semántico end-to-end: procesa el prompt, infiere la audiencia y genera
    un modelo SemanticDiagram enriquecido y filtrado.
    """
    # 1. Determinar Audiencia
    aud_key = audience_override if audience_override else infer_audience_from_text(prompt_text)
    audience = get_audience_profile(aud_key)
    
    # 2. Determinar Topología y Arquetipo
    topology = infer_topology_from_text(prompt_text)
    archetype = select_optimal_archetype(topology, audience)
    
    # 3. Extraer Título Principal
    first_line = prompt_text.strip().split("\n")[0]
    clean_title = re.sub(r'^[#\s\*\-]+', '', first_line)[:60]
    if len(clean_title) < 5:
        clean_title = "Arquitectura de Sistema & Flujo de Negocio"
        
    # 4. Construir Diagrama Semántico Base
    diagram = SemanticDiagram(
        title=clean_title,
        semantic_type=f"archetype_{archetype.lower()}",
        detail_level=DetailLevel.BALANCED,
        output_preset=OutputPreset.DOCS,
        engine="red" if archetype in ["A", "T"] else ("flujo" if archetype in ["B", "C", "F"] else "grid"),
        metadata={
            "audience": audience.role,
            "archetype_code": archetype,
            "topology": topology,
            "density_target": audience.density_target,
            "tone": audience.tone,
            "suppressed_topics": audience.information_suppress
        }
    )
    
    return diagram
