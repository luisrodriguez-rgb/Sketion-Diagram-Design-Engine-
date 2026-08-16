"""
Sketion 4.0 — Semantic Icon Resolver (semantic/icon_resolver.py)
Resuelve y asigna iconos vectoriales monocromáticos basándose estrictamente
en la semántica y jerarquía del nodo, evitando la saturación decorativa.

Reglas:
1. HERO: Icono de acento protagonista.
2. COMPONENT: Icono pequeño de reconocimiento semántico rápido (DB, Gateway, Queue, Auth, Cache).
3. METADATA / STEPS: Sin icono (NONE).
"""

from typing import Optional, Dict, Any


SEMANTIC_ICON_MAP: Dict[str, str] = {
    # Compute / Ingress
    "mobile": "phone",
    "web": "laptop",
    "client": "desktop",
    "ingress": "ingress",
    "gateway": "gateway",
    "waf": "firewall",
    "load_balancer": "load-balancer",
    
    # Security / Auth
    "auth": "lock",
    "security": "vpn",
    "key": "key",
    
    # Core Services
    "payment": "server",
    "orchestrator": "server",
    "api": "api",
    "service": "server",
    "reconciliation": "sync",
    "alert": "alert",
    
    # Messaging & Queue
    "queue": "queue",
    "kafka": "queue",
    "broker": "queue",
    "event": "pipeline",
    
    # Storage & Cache
    "database": "database",
    "postgres": "postgres",
    "postgresql": "postgres",
    "redis": "redis",
    "cache": "cache",
    "bucket": "bucket",
    "storage": "database",
    
    # Observability & Analytics
    "monitoring": "monitoring",
    "analytics": "monitoring",
    "observability": "monitoring",
    "logs": "log",
    "search": "search",
    
    # External
    "external": "cloud",
    "provider": "cloud",
    "bank": "cloud",
    "terminal": "terminal"
}


def resolve_node_icon(label: str, role: str = "core", sublabel: Optional[str] = None,
                      tier: str = "component") -> Optional[str]:
    """
    Determina si un nodo amerita un icono y cuál es el icono óptimo.
    Retorna el nombre del icono o None si debe permanecer puramente tipográfico.
    """
    if tier.lower() == "none" or tier.lower() == "metadata":
        return None
        
    text_corpus = f"{label} {role} {sublabel or ''}".lower()
    
    # Búsqueda semántica
    for keyword, icon_name in SEMANTIC_ICON_MAP.items():
        if keyword in text_corpus:
            return icon_name
            
    # Si es un componente pero no tiene match específico, no forzar icono
    return None
