"""
Sketion Semantic Iconography Registry (v8.2 - 150+ Pure Vector Icons)
Biblioteca unificada de más de 150 íconos semánticos vectoriales mapeados a Excalidraw.
100% LIBRE DE EMOJIS: Utiliza exclusivamente primitivas geométricas vectoriales,
trazos editoriales nativos y simbología tipográfica profesional.
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
    """Registro unificado de íconos semánticos vectoriales nativos para Excalidraw (Cero Emojis)."""

    _ICON_MAP: Dict[str, Dict[str, Any]] = {
        # ═══════════════════════════════════════════════════════════════════════════
        # 1. PERSONAS & ROLES (25+)
        # ═══════════════════════════════════════════════════════════════════════════
        "user": {"category": IconCategory.PERSONAS, "icon": "users", "symbol": "USER"},
        "admin": {"category": IconCategory.PERSONAS, "icon": "users", "symbol": "ADMIN"},
        "customer": {"category": IconCategory.PERSONAS, "icon": "users", "symbol": "CLIENT"},
        "developer": {"category": IconCategory.PERSONAS, "icon": "laptop", "symbol": "DEV"},
        "auditor": {"category": IconCategory.PERSONAS, "icon": "lock", "symbol": "AUDIT"},
        "manager": {"category": IconCategory.PERSONAS, "icon": "users", "symbol": "MGR"},
        "operator": {"category": IconCategory.PERSONAS, "icon": "server", "symbol": "OPS"},
        "ciso": {"category": IconCategory.PERSONAS, "icon": "shield", "symbol": "CISO"},
        "dpo": {"category": IconCategory.PERSONAS, "icon": "lock", "symbol": "DPO"},
        "analyst": {"category": IconCategory.PERSONAS, "icon": "laptop", "symbol": "DATA"},
        "architect": {"category": IconCategory.PERSONAS, "icon": "laptop", "symbol": "ARCH"},
        "devops": {"category": IconCategory.PERSONAS, "icon": "server", "symbol": "DEVOPS"},
        "qa_engineer": {"category": IconCategory.PERSONAS, "icon": "shield", "symbol": "QA"},
        "finance_director": {"category": IconCategory.PERSONAS, "icon": "card", "symbol": "CFO"},
        "sales_rep": {"category": IconCategory.PERSONAS, "icon": "users", "symbol": "SALES"},
        "support_agent": {"category": IconCategory.PERSONAS, "icon": "users", "symbol": "SUPP"},
        "compliance_officer": {"category": IconCategory.PERSONAS, "icon": "file", "symbol": "COMPL"},
        "ceo": {"category": IconCategory.PERSONAS, "icon": "users", "symbol": "EXEC"},
        "cto": {"category": IconCategory.PERSONAS, "icon": "laptop", "symbol": "TECH"},
        "merchant": {"category": IconCategory.PERSONAS, "icon": "users", "symbol": "MERCH"},
        "partner": {"category": IconCategory.PERSONAS, "icon": "users", "symbol": "PARTNER"},
        "bot": {"category": IconCategory.PERSONAS, "icon": "laptop", "symbol": "BOT"},
        "guest": {"category": IconCategory.PERSONAS, "icon": "users", "symbol": "GUEST"},
        "subscriber": {"category": IconCategory.PERSONAS, "icon": "users", "symbol": "SUB"},
        "lead": {"category": IconCategory.PERSONAS, "icon": "users", "symbol": "LEAD"},

        # ═══════════════════════════════════════════════════════════════════════════
        # 2. SISTEMAS & INFRAESTRUCTURA (35+)
        # ═══════════════════════════════════════════════════════════════════════════
        "api": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "API"},
        "server": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "SRV"},
        "database": {"category": IconCategory.SYSTEMS, "icon": "database", "symbol": "DB"},
        "cloud": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "CLOUD"},
        "service": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "SVC"},
        "microservice": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "MSVC"},
        "gateway": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "GW"},
        "queue": {"category": IconCategory.SYSTEMS, "icon": "terminal", "symbol": "QUEUE"},
        "worker": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "WRK"},
        "router": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "ROUTER"},
        "load_balancer": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "ALB"},
        "firewall": {"category": IconCategory.SYSTEMS, "icon": "shield", "symbol": "FW"},
        "cdn": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "CDN"},
        "cluster": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "CLUSTER"},
        "pod": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "POD"},
        "container": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "DOCKER"},
        "lambda_func": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "LAMBDA"},
        "vm": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "VM"},
        "vpc": {"category": IconCategory.SYSTEMS, "icon": "shield", "symbol": "VPC"},
        "dns": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "DNS"},
        "switch": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "SWITCH"},
        "hub": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "HUB"},
        "lakehouse": {"category": IconCategory.SYSTEMS, "icon": "database", "symbol": "LAKE"},
        "warehouse": {"category": IconCategory.SYSTEMS, "icon": "database", "symbol": "DWH"},
        "cache": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "CACHE"},
        "broker": {"category": IconCategory.SYSTEMS, "icon": "terminal", "symbol": "BROKER"},
        "proxy": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "PROXY"},
        "mesh": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "MESH"},
        "edge": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "EDGE"},
        "endpoint": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "EP"},
        "iot_device": {"category": IconCategory.SYSTEMS, "icon": "laptop", "symbol": "IOT"},
        "pos_terminal": {"category": IconCategory.SYSTEMS, "icon": "card", "symbol": "POS"},
        "mobile_app": {"category": IconCategory.SYSTEMS, "icon": "laptop", "symbol": "APP"},
        "spa_web": {"category": IconCategory.SYSTEMS, "icon": "laptop", "symbol": "WEB"},
        "webhook": {"category": IconCategory.SYSTEMS, "icon": "server", "symbol": "HOOK"},

        # ═══════════════════════════════════════════════════════════════════════════
        # 3. ACCIONES & OPERACIONES (30+)
        # ═══════════════════════════════════════════════════════════════════════════
        "create": {"category": IconCategory.ACTIONS, "icon": "file", "symbol": "[+]"},
        "update": {"category": IconCategory.ACTIONS, "icon": "server", "symbol": "[*]"},
        "delete": {"category": IconCategory.ACTIONS, "icon": "trash", "symbol": "[-]"},
        "validate": {"category": IconCategory.ACTIONS, "icon": "shield", "symbol": "VAL"},
        "authenticate": {"category": IconCategory.ACTIONS, "icon": "key", "symbol": "AUTH"},
        "process": {"category": IconCategory.ACTIONS, "icon": "server", "symbol": "EXEC"},
        "send": {"category": IconCategory.ACTIONS, "icon": "arrow", "symbol": "OUT"},
        "receive": {"category": IconCategory.ACTIONS, "icon": "arrow", "symbol": "IN"},
        "retry": {"category": IconCategory.ACTIONS, "icon": "server", "symbol": "RETRY"},
        "approve": {"category": IconCategory.ACTIONS, "icon": "shield", "symbol": "OK"},
        "reject": {"category": IconCategory.ACTIONS, "icon": "alert", "symbol": "REJ"},
        "filter": {"category": IconCategory.ACTIONS, "icon": "server", "symbol": "FILTER"},
        "transform": {"category": IconCategory.ACTIONS, "icon": "server", "symbol": "MAP"},
        "route": {"category": IconCategory.ACTIONS, "icon": "arrow", "symbol": "ROUTE"},
        "encrypt": {"category": IconCategory.ACTIONS, "icon": "lock", "symbol": "ENC"},
        "decrypt": {"category": IconCategory.ACTIONS, "icon": "key", "symbol": "DEC"},
        "tokenize": {"category": IconCategory.ACTIONS, "icon": "key", "symbol": "TOKEN"},
        "detokenize": {"category": IconCategory.ACTIONS, "icon": "key", "symbol": "DETOK"},
        "sync": {"category": IconCategory.ACTIONS, "icon": "server", "symbol": "SYNC"},
        "async_emit": {"category": IconCategory.ACTIONS, "icon": "terminal", "symbol": "EMIT"},
        "rollback": {"category": IconCategory.ACTIONS, "icon": "server", "symbol": "ROLLBACK"},
        "commit": {"category": IconCategory.ACTIONS, "icon": "database", "symbol": "COMMIT"},
        "reconcile": {"category": IconCategory.ACTIONS, "icon": "server", "symbol": "REC"},
        "alert_notify": {"category": IconCategory.ACTIONS, "icon": "alert", "symbol": "ALERT"},
        "deploy": {"category": IconCategory.ACTIONS, "icon": "server", "symbol": "DEPLOY"},
        "scale": {"category": IconCategory.ACTIONS, "icon": "server", "symbol": "SCALE"},
        "backup": {"category": IconCategory.ACTIONS, "icon": "database", "symbol": "BACKUP"},
        "restore": {"category": IconCategory.ACTIONS, "icon": "database", "symbol": "RESTORE"},
        "isolate": {"category": IconCategory.ACTIONS, "icon": "shield", "symbol": "ISOLATE"},
        "audit_log": {"category": IconCategory.ACTIONS, "icon": "file", "symbol": "AUDIT"},

        # ═══════════════════════════════════════════════════════════════════════════
        # 4. ESTADOS & CICLO DE VIDA (20+)
        # ═══════════════════════════════════════════════════════════════════════════
        "success": {"category": IconCategory.STATES, "icon": "shield", "symbol": "[OK]"},
        "warning": {"category": IconCategory.STATES, "icon": "alert", "symbol": "[WARN]"},
        "error": {"category": IconCategory.STATES, "icon": "alert", "symbol": "[ERR]"},
        "pending": {"category": IconCategory.STATES, "icon": "clock", "symbol": "[PEND]"},
        "blocked": {"category": IconCategory.STATES, "icon": "lock", "symbol": "[BLOCK]"},
        "processing": {"category": IconCategory.STATES, "icon": "server", "symbol": "[PROC]"},
        "failed": {"category": IconCategory.STATES, "icon": "alert", "symbol": "[FAIL]"},
        "completed": {"category": IconCategory.STATES, "icon": "shield", "symbol": "[DONE]"},
        "healthy": {"category": IconCategory.STATES, "icon": "shield", "symbol": "[HEALTHY]"},
        "degraded": {"category": IconCategory.STATES, "icon": "alert", "symbol": "[DEGRADED]"},
        "critical": {"category": IconCategory.STATES, "icon": "alert", "symbol": "[CRITICAL]"},
        "offline": {"category": IconCategory.STATES, "icon": "server", "symbol": "[OFFLINE]"},
        "online": {"category": IconCategory.STATES, "icon": "server", "symbol": "[ONLINE]"},
        "archived": {"category": IconCategory.STATES, "icon": "file", "symbol": "[ARCHIVE]"},
        "quarantined": {"category": IconCategory.STATES, "icon": "lock", "symbol": "[QUARANTINE]"},
        "expired": {"category": IconCategory.STATES, "icon": "clock", "symbol": "[EXPIRED]"},
        "locked": {"category": IconCategory.STATES, "icon": "lock", "symbol": "[LOCKED]"},
        "unlocked": {"category": IconCategory.STATES, "icon": "key", "symbol": "[UNLOCKED]"},
        "throttled": {"category": IconCategory.STATES, "icon": "alert", "symbol": "[THROTTLED]"},
        "timeout": {"category": IconCategory.STATES, "icon": "clock", "symbol": "[TIMEOUT]"},

        # ═══════════════════════════════════════════════════════════════════════════
        # 5. SEGURIDAD & COMPLIANCE (20+)
        # ═══════════════════════════════════════════════════════════════════════════
        "shield": {"category": IconCategory.SECURITY, "icon": "shield", "symbol": "SEC"},
        "lock": {"category": IconCategory.SECURITY, "icon": "lock", "symbol": "LOCK"},
        "key": {"category": IconCategory.SECURITY, "icon": "key", "symbol": "KEY"},
        "certificate": {"category": IconCategory.SECURITY, "icon": "file", "symbol": "X509"},
        "token": {"category": IconCategory.SECURITY, "icon": "key", "symbol": "TOKEN"},
        "encryption": {"category": IconCategory.SECURITY, "icon": "lock", "symbol": "AES256"},
        "vault": {"category": IconCategory.SECURITY, "icon": "lock", "symbol": "VAULT"},
        "signature": {"category": IconCategory.SECURITY, "icon": "file", "symbol": "SIG"},
        "biometric": {"category": IconCategory.SECURITY, "icon": "shield", "symbol": "BIOMETRIC"},
        "acl": {"category": IconCategory.SECURITY, "icon": "file", "symbol": "ACL"},
        "rbac": {"category": IconCategory.SECURITY, "icon": "users", "symbol": "RBAC"},
        "zero_trust": {"category": IconCategory.SECURITY, "icon": "shield", "symbol": "ZERO_TRUST"},
        "audit_trail": {"category": IconCategory.SECURITY, "icon": "file", "symbol": "TRAIL"},
        "honey_pot": {"category": IconCategory.SECURITY, "icon": "shield", "symbol": "TRAP"},
        "scanner": {"category": IconCategory.SECURITY, "icon": "laptop", "symbol": "SCAN"},
        "vulnerability": {"category": IconCategory.SECURITY, "icon": "alert", "symbol": "CVE"},
        "seal": {"category": IconCategory.SECURITY, "icon": "shield", "symbol": "SEAL"},
        "compliance": {"category": IconCategory.SECURITY, "icon": "file", "symbol": "COMPL"},
        "hsm": {"category": IconCategory.SECURITY, "icon": "lock", "symbol": "HSM"},
        "sanctions": {"category": IconCategory.SECURITY, "icon": "alert", "symbol": "OFAC"},

        # ═══════════════════════════════════════════════════════════════════════════
        # 6. DATOS, ANALÍTICA & FORMATOS (25+)
        # ═══════════════════════════════════════════════════════════════════════════
        "file": {"category": IconCategory.DATA, "icon": "file", "symbol": "FILE"},
        "document": {"category": IconCategory.DATA, "icon": "file", "symbol": "DOC"},
        "dataset": {"category": IconCategory.DATA, "icon": "database", "symbol": "DATASET"},
        "analytics": {"category": IconCategory.DATA, "icon": "laptop", "symbol": "OLAP"},
        "logs": {"category": IconCategory.DATA, "icon": "file", "symbol": "LOGS"},
        "event": {"category": IconCategory.DATA, "icon": "terminal", "symbol": "EVENT"},
        "stream": {"category": IconCategory.DATA, "icon": "terminal", "symbol": "STREAM"},
        "table": {"category": IconCategory.DATA, "icon": "database", "symbol": "TABLE"},
        "column": {"category": IconCategory.DATA, "icon": "database", "symbol": "COL"},
        "row": {"category": IconCategory.DATA, "icon": "file", "symbol": "ROW"},
        "json_doc": {"category": IconCategory.DATA, "icon": "file", "symbol": "JSON"},
        "xml_doc": {"category": IconCategory.DATA, "icon": "file", "symbol": "XML"},
        "csv_file": {"category": IconCategory.DATA, "icon": "file", "symbol": "CSV"},
        "parquet": {"category": IconCategory.DATA, "icon": "database", "symbol": "PARQUET"},
        "binary": {"category": IconCategory.DATA, "icon": "file", "symbol": "BIN"},
        "report": {"category": IconCategory.DATA, "icon": "file", "symbol": "REPORT"},
        "metric": {"category": IconCategory.DATA, "icon": "laptop", "symbol": "METRIC"},
        "kpi": {"category": IconCategory.DATA, "icon": "laptop", "symbol": "KPI"},
        "query": {"category": IconCategory.DATA, "icon": "database", "symbol": "SQL"},
        "transaction": {"category": IconCategory.DATA, "icon": "card", "symbol": "TX"},
        "ledger": {"category": IconCategory.DATA, "icon": "database", "symbol": "LEDGER"},
        "tax_record": {"category": IconCategory.DATA, "icon": "file", "symbol": "TAX"},
        "dispute": {"category": IconCategory.DATA, "icon": "alert", "symbol": "DISPUTE"},
        "invoice": {"category": IconCategory.DATA, "icon": "file", "symbol": "INVOICE"},
        "token_cache": {"category": IconCategory.DATA, "icon": "server", "symbol": "TOKEN_CACHE"}
    }

    @classmethod
    def resolve_icon(cls, concept: str) -> str:
        """Resuelve el ícono vectorial nativo más cercano a partir de un concepto semántico."""
        c = concept.lower().strip()
        if c in cls._ICON_MAP:
            return cls._ICON_MAP[c]["icon"]

        # Mapeos contextuales limpios
        if any(w in c for w in ["user", "client", "customer", "shopper", "buyer", "persona"]):
            return "users"
        if any(w in c for w in ["admin", "root", "super"]):
            return "users"
        if any(w in c for w in ["ciso", "security_officer", "dpo"]):
            return "shield"
        if any(w in c for w in ["auth", "jwt", "session", "key", "token"]):
            return "key"
        if any(w in c for w in ["pci", "vault", "encrypt", "hsm", "secret", "lock"]):
            return "lock"
        if any(w in c for w in ["waf", "ddos", "shield", "protect", "defense", "zero_trust"]):
            return "shield"
        if any(w in c for w in ["kafka", "stream", "queue", "rabbitmq", "bus", "event", "topic"]):
            return "terminal"
        if any(w in c for w in ["postgres", "aurora", "mysql", "db", "database", "sql", "clickhouse", "mongo", "redis", "dynamo"]):
            return "database"
        if any(w in c for w in ["audit", "compliance", "soc2", "log", "dian", "report", "tax"]):
            return "file"
        if any(w in c for w in ["cloud", "aws", "gcp", "azure", "kubernetes", "eks", "vpc"]):
            return "server"
        if any(w in c for w in ["gateway", "kong", "envoy", "alb", "ingress", "router", "load_balancer"]):
            return "server"
        if any(w in c for w in ["worker", "reconciliation", "cron", "job", "task"]):
            return "server"
        if any(w in c for w in ["card", "payment", "checkout", "pos", "visa", "mastercard"]):
            return "card"
        if any(w in c for w in ["alert", "warning", "circuit", "timeout", "pagerduty", "error"]):
            return "alert"
        if any(w in c for w in ["ledger", "double_entry", "accounting"]):
            return "database"

        return "server"

    @classmethod
    def get_total_count(cls) -> int:
        return len(cls._ICON_MAP)
