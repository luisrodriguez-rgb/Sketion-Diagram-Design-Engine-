"""
Sketion 3.4 — Motor de Decision de Audiencia (Audience-Aware Inference Engine)
Adapta autonomamente el vocabulario, la densidad de informacion, la seleccion de arquetipos
y los componentes a representar segun la audiencia destinataria del diagrama.
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class AudienceProfile:
    role: str                       # CEO_BOARD, OPERATIONS, PRODUCT_TECH, DEV_DOCS, INVESTOR_PITCH
    primary_archetypes: List[str]   # Codigos de arquetipo recomendados (A-T)
    information_focus: List[str]    # Conceptos clave a maximizar
    information_suppress: List[str] # Conceptos a omitir deliberadamente para evitar ruido
    density_target: float           # Densidad visual objetivo (3.5 - 4.2)
    tone: str                       # STRATEGIC_FINANCIAL, INDUSTRIAL_PHYSICAL, TECHNICAL_CLOUD, API_CONTRACT


AUDIENCE_CATALOG: Dict[str, AudienceProfile] = {
    "CEO_BOARD": AudienceProfile(
        role="CEO_BOARD",
        primary_archetypes=["D", "B", "P", "H"], # Duelo, Fases, Cadena de Valor, Radar 2x2
        information_focus=["ROI", "CAPEX/OPEX", "Retencion de Clientes", "Capacidad Efectiva", "Gobernanza de Fases"],
        information_suppress=["APIs", "Codigo", "Pantallas de Cocina", "Tiempos de Ciclo en Segundos", "Modelos de Datos"],
        density_target=3.6,
        tone="STRATEGIC_FINANCIAL"
    ),
    "OPERATIONS": AudienceProfile(
        role="OPERATIONS",
        primary_archetypes=["E", "M", "S", "K"], # Cadena/Planta, Ishikawa, Matriz CRUD/Takt, Kanban
        information_focus=["Layout de Planta", "Segregacion Fisica", "Takt Time", "Balanceo de Linea", "Batching", "Roles de Turno"],
        information_suppress=["Modelos Financieros Macro", "APIs de Software", "Contratos Legales", "Arquitectura Cloud"],
        density_target=4.0,
        tone="INDUSTRIAL_PHYSICAL"
    ),
    "PRODUCT_TECH": AudienceProfile(
        role="PRODUCT_TECH",
        primary_archetypes=["A", "C", "T", "N"], # Cerebro, Serpiente/Journey, Caja Explotada, Galeria
        information_focus=["Arquitectura Cloud", "Microservicios", "User Journey 1:1", "Slots de Captura UI", "Motor ETA", "KDS"],
        information_suppress=["Negociaciones Laborales", "Costes Fijos de Nómina", "Decisiones Presupuestarias"],
        density_target=3.8,
        tone="TECHNICAL_CLOUD"
    ),
    "DEV_DOCS": AudienceProfile(
        role="DEV_DOCS",
        primary_archetypes=["S", "O", "T"],      # Matriz CRUD, Arbol Decision, Caja Explotada
        information_focus=["Endpoints HTTP", "JSON Schema", "Idempotency Keys", "Codigos de Error", "Transiciones de Estado"],
        information_suppress=["Discursos de Negocio", "Planos Fisicos de Edificio", "Estrategia Comercial"],
        density_target=4.2,
        tone="API_CONTRACT"
    ),
    "INVESTOR_PITCH": AudienceProfile(
        role="INVESTOR_PITCH",
        primary_archetypes=["D", "F", "I"],      # Duelo VS, Embudo, Flywheel
        information_focus=["Tamano de Mercado", "Metricas Heroicas", "Traccion", "Dolor vs Solucion Unica"],
        information_suppress=["Diagramas de Arquitectura Complejos", "Tablas con Mas de 3 Columnas", "Detalles Tecnicos"],
        density_target=3.2,
        tone="STRATEGIC_FINANCIAL"
    )
}


def get_audience_profile(audience_key: str) -> AudienceProfile:
    """Retorna el perfil de audiencia correspondiente o el perfil de CEO_BOARD por defecto."""
    key = audience_key.upper().strip()
    for k, profile in AUDIENCE_CATALOG.items():
        if k in key or key in k:
            return profile
    return AUDIENCE_CATALOG["CEO_BOARD"]


def filter_information_for_audience(raw_entities: List[Dict[str, Any]], audience: AudienceProfile) -> List[Dict[str, Any]]:
    """Filtra y prioriza entidades y relaciones segun el perfil de audiencia."""
    filtered = []
    for ent in raw_entities:
        name = ent.get("name", "")
        category = ent.get("category", "")
        
        # Verificar si la entidad coincide con elementos a suprimir
        suppress = False
        for sup in audience.information_suppress:
            if sup.lower() in name.lower() or sup.lower() in category.lower():
                suppress = True
                break
        
        if not suppress:
            filtered.append(ent)
            
    return filtered
