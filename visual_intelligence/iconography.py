"""
Sketion Semantic Iconography Registry (v8.1)
Biblioteca y catálogo de iconografía semántica categorizada por dominios:
- Personas
- Sistemas
- Acciones
- Estados
- Seguridad
- Datos
"""

from enum import Enum
from typing import Dict, Any, Optional, List


class IconCategory(Enum):
    PERSONAS = "PERSONAS"
    SYSTEMS = "SYSTEMS"
    ACTIONS = "ACTIONS"
    STATES = "STATES"
    SECURITY = "SECURITY"
    DATA = "DATA"


class SemanticIconRegistry:
    """Registro unificado de íconos semánticos vectoriales mapeados a Excalidraw."""

    _ICON_MAP: Dict[str, Dict[str, Any]] = {
        # 1. PERSONAS
        "user": {"category": IconCategory.PERSONAS, "fallback": "users", "glyph": "👤"},
        "admin": {"category": IconCategory.PERSONAS, "fallback": "users", "glyph": "👑"},
        "customer": {"category": IconCategory.PERSONAS, "fallback": "users", "glyph": "🛍️"},
        "developer": {"category": IconCategory.PERSONAS, "fallback": "laptop", "glyph": "💻"},
        "auditor": {"category": IconCategory.PERSONAS, "fallback": "lock", "glyph": "📋"},
        "manager": {"category": IconCategory.PERSONAS, "fallback": "users", "glyph": "📊"},
        "operator": {"category": IconCategory.PERSONAS, "fallback": "server", "glyph": "🛠️"},

        # 2. SISTEMAS
        "api": {"category": IconCategory.SYSTEMS, "fallback": "server", "glyph": "⚡"},
        "server": {"category": IconCategory.SYSTEMS, "fallback": "server", "glyph": "🖥️"},
        "database": {"category": IconCategory.SYSTEMS, "fallback": "database", "glyph": "🗄️"},
        "cloud": {"category": IconCategory.SYSTEMS, "fallback": "server", "glyph": "☁️"},
        "service": {"category": IconCategory.SYSTEMS, "fallback": "server", "glyph": "⚙️"},
        "microservice": {"category": IconCategory.SYSTEMS, "fallback": "server", "glyph": "📦"},
        "gateway": {"category": IconCategory.SYSTEMS, "fallback": "server", "glyph": "🚪"},
        "queue": {"category": IconCategory.SYSTEMS, "fallback": "terminal", "glyph": "📥"},
        "worker": {"category": IconCategory.SYSTEMS, "fallback": "server", "glyph": "🔄"},

        # 3. ACCIONES
        "create": {"category": IconCategory.ACTIONS, "fallback": "file", "glyph": "➕"},
        "update": {"category": IconCategory.ACTIONS, "fallback": "server", "glyph": "✏️"},
        "delete": {"category": IconCategory.ACTIONS, "fallback": "trash", "glyph": "🗑️"},
        "validate": {"category": IconCategory.ACTIONS, "fallback": "shield", "glyph": "✓"},
        "authenticate": {"category": IconCategory.ACTIONS, "fallback": "key", "glyph": "🔑"},
        "process": {"category": IconCategory.ACTIONS, "fallback": "server", "glyph": "⚙️"},
        "send": {"category": IconCategory.ACTIONS, "fallback": "arrow", "glyph": "📤"},
        "receive": {"category": IconCategory.ACTIONS, "fallback": "arrow", "glyph": "📥"},
        "retry": {"category": IconCategory.ACTIONS, "fallback": "server", "glyph": "🔁"},
        "approve": {"category": IconCategory.ACTIONS, "fallback": "shield", "glyph": "✅"},
        "reject": {"category": IconCategory.ACTIONS, "fallback": "alert", "glyph": "❌"},

        # 4. ESTADOS
        "success": {"category": IconCategory.STATES, "fallback": "shield", "glyph": "🟢"},
        "warning": {"category": IconCategory.STATES, "fallback": "alert", "glyph": "⚠️"},
        "error": {"category": IconCategory.STATES, "fallback": "alert", "glyph": "🔴"},
        "pending": {"category": IconCategory.STATES, "fallback": "clock", "glyph": "⏳"},
        "blocked": {"category": IconCategory.STATES, "fallback": "lock", "glyph": "🚫"},
        "processing": {"category": IconCategory.STATES, "fallback": "server", "glyph": "🌀"},
        "failed": {"category": IconCategory.STATES, "fallback": "alert", "glyph": "❌"},
        "completed": {"category": IconCategory.STATES, "fallback": "shield", "glyph": "🏁"},

        # 5. SEGURIDAD
        "shield": {"category": IconCategory.SECURITY, "fallback": "shield", "glyph": "🛡️"},
        "lock": {"category": IconCategory.SECURITY, "fallback": "lock", "glyph": "🔒"},
        "key": {"category": IconCategory.SECURITY, "fallback": "key", "glyph": "🔑"},
        "certificate": {"category": IconCategory.SECURITY, "fallback": "file", "glyph": "📜"},
        "firewall": {"category": IconCategory.SECURITY, "fallback": "shield", "glyph": "🧱"},
        "token": {"category": IconCategory.SECURITY, "fallback": "key", "glyph": "🎫"},
        "encryption": {"category": IconCategory.SECURITY, "fallback": "lock", "glyph": "🔐"},

        # 6. DATOS
        "file": {"category": IconCategory.DATA, "fallback": "file", "glyph": "📄"},
        "document": {"category": IconCategory.DATA, "fallback": "file", "glyph": "📑"},
        "dataset": {"category": IconCategory.DATA, "fallback": "database", "glyph": "📊"},
        "analytics": {"category": IconCategory.DATA, "fallback": "laptop", "glyph": "📈"},
        "logs": {"category": IconCategory.DATA, "fallback": "file", "glyph": "🪵"},
        "event": {"category": IconCategory.DATA, "fallback": "terminal", "glyph": "⚡"},
        "stream": {"category": IconCategory.DATA, "fallback": "terminal", "glyph": "🌊"}
    }

    @classmethod
    def resolve_icon(cls, concept: str) -> str:
        """Resuelve el nombre de ícono más cercano a partir de un concepto semántico."""
        c = concept.lower().strip()
        if c in cls._ICON_MAP:
            return c

        # Mapeos contextuales difusos
        if any(w in c for w in ["user", "client", "customer", "shopper", "buyer", "persona"]):
            return "user"
        if any(w in c for w in ["admin", "root", "super"]):
            return "admin"
        if any(w in c for w in ["auth", "jwt", "session", "key", "token"]):
            return "key"
        if any(w in c for w in ["pci", "vault", "encrypt", "hsm", "secret", "lock"]):
            return "lock"
        if any(w in c for w in ["waf", "ddos", "shield", "protect", "defense", "security"]):
            return "shield"
        if any(w in c for w in ["kafka", "stream", "queue", "rabbitmq", "bus", "event", "topic"]):
            return "stream"
        if any(w in c for w in ["postgres", "aurora", "mysql", "db", "database", "sql", "clickhouse", "mongo", "redis", "dynamo"]):
            return "database"
        if any(w in c for w in ["audit", "compliance", "soc2", "log", "dian", "report"]):
            return "document"
        if any(w in c for w in ["cloud", "aws", "gcp", "azure", "kubernetes", "eks"]):
            return "cloud"
        if any(w in c for w in ["gateway", "kong", "envoy", "alb", "ingress"]):
            return "gateway"
        if any(w in c for w in ["worker", "reconciliation", "cron", "job", "task"]):
            return "worker"
        if any(w in c for w in ["card", "payment", "checkout", "pos", "visa", "mastercard"]):
            return "card"
        if any(w in c for w in ["alert", "warning", "circuit", "timeout", "pagerduty", "error"]):
            return "alert"

        return "server"
