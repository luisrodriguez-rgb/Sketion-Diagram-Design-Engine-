"""
Sketion Intelligent Badges & Status Metrics Engine (v8.2 - Pure Vector)
Genera badges y pastillas semánticas enriquecidas:
- METRIC: 99.999% SLA, <35ms P99, 25k TPS
- STATE: ● ACTIVE, ● PENDING, DEGRADED, FAILED
- COMPLIANCE: PCI-DSS, SOC 2, ISO 27001
- RISK: CRITICAL, HIGH RISK, LOW RISK
- ENVIRONMENT: PRODUCTION, STAGING, EU-WEST-1
- AFFORDANCE: [GET] /payments, [Authorize], [Capture]
100% LIBRE DE EMOJIS: Utiliza exclusivamente símbolos vectoriales y tipografía monospaced.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, Optional, Tuple


class BadgeType(Enum):
    METRIC = "METRIC"
    STATE = "STATE"
    COMPLIANCE = "COMPLIANCE"
    RISK = "RISK"
    ENVIRONMENT = "ENVIRONMENT"
    TECH = "TECH"
    AFFORDANCE = "AFFORDANCE"


@dataclass
class SemanticBadge:
    text: str
    badge_type: BadgeType
    bg_color: str
    stroke_color: str
    text_color: str
    symbol_prefix: Optional[str] = None


class StatusBadgeEngine:
    """Motor de generación de insignias inteligentes según función semántica (Cero Emojis)."""

    _PALETTES = {
        BadgeType.METRIC: {"bg": "#EFF6FF", "stroke": "#93C5FD", "text": "#1D4ED8", "prefix": "METRIC"},
        BadgeType.STATE: {
            "ACTIVE": {"bg": "#F0FDF4", "stroke": "#86EFAC", "text": "#15803D", "prefix": "● ACTIVE"},
            "PENDING": {"bg": "#FEF3C7", "stroke": "#FCD34D", "text": "#B45309", "prefix": "● PENDING"},
            "DEGRADED": {"bg": "#FFFBEB", "stroke": "#FDE68A", "text": "#D97706", "prefix": "● DEGRADED"},
            "FAILED": {"bg": "#FFF5F2", "stroke": "#FCA5A5", "text": "#D93829", "prefix": "● FAILED"}
        },
        BadgeType.COMPLIANCE: {"bg": "#F8FAFC", "stroke": "#CBD5E1", "text": "#334155", "prefix": "COMPLIANCE"},
        BadgeType.RISK: {
            "CRITICAL": {"bg": "#FEF2F2", "stroke": "#F87171", "text": "#DC2626", "prefix": "CRITICAL"},
            "HIGH": {"bg": "#FFF5F2", "stroke": "#FCA5A5", "text": "#D93829", "prefix": "HIGH RISK"},
            "MEDIUM": {"bg": "#FEF3C7", "stroke": "#FCD34D", "text": "#D97706", "prefix": "MEDIUM RISK"},
            "LOW": {"bg": "#F0FDF4", "stroke": "#86EFAC", "text": "#16A34A", "prefix": "LOW RISK"}
        },
        BadgeType.ENVIRONMENT: {"bg": "#EEF2FF", "stroke": "#C7D2FE", "text": "#4338CA", "prefix": "ENV"},
        BadgeType.TECH: {"bg": "#F1F5F9", "stroke": "#94A3B8", "text": "#0F172A", "prefix": "TECH"},
        BadgeType.AFFORDANCE: {"bg": "#0F172A", "stroke": "#0F172A", "text": "#FFFFFF", "prefix": "ACTION"}
    }

    @classmethod
    def create_badge(cls, label: str, badge_type: Optional[BadgeType] = None) -> SemanticBadge:
        """Infiere el tipo de badge semántico y devuelve su especificación de estilo."""
        u_label = label.upper().strip()

        # Inferencia automática de tipo si no se proporciona
        if badge_type is None:
            if any(k in u_label for k in ["SLA", "TPS", "MS", "%", "$", "USD", "LATENCIA", "UPTIME"]):
                badge_type = BadgeType.METRIC
            elif any(k in u_label for k in ["ACTIVE", "PENDING", "DEGRADED", "FAILED", "RUNNING", "ONLINE"]):
                badge_type = BadgeType.STATE
            elif any(k in u_label for k in ["PCI", "SOC2", "ISO", "DIAN", "AML", "SOX", "GDPR", "COMPLIANCE"]):
                badge_type = BadgeType.COMPLIANCE
            elif any(k in u_label for k in ["CRITICAL", "HIGH RISK", "MEDIUM", "LOW RISK", "RISK"]):
                badge_type = BadgeType.RISK
            elif any(k in u_label for k in ["PROD", "STAGING", "DEV", "CLUSTER", "REGION", "AWS", "AZURE", "GCP"]):
                badge_type = BadgeType.ENVIRONMENT
            elif any(k in u_label for k in ["GET", "POST", "PUT", "DELETE", "AUTHORIZE", "CAPTURE", "REFUND"]):
                badge_type = BadgeType.AFFORDANCE
            else:
                badge_type = BadgeType.TECH

        # Resolver colores según tipo
        if badge_type == BadgeType.STATE:
            state_key = "ACTIVE"
            for k in ["FAILED", "DEGRADED", "PENDING", "ACTIVE"]:
                if k in u_label:
                    state_key = k
                    break
            palette = cls._PALETTES[BadgeType.STATE][state_key]
        elif badge_type == BadgeType.RISK:
            risk_key = "HIGH"
            for k in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
                if k in u_label:
                    risk_key = k
                    break
            palette = cls._PALETTES[BadgeType.RISK][risk_key]
        else:
            palette = cls._PALETTES.get(badge_type, cls._PALETTES[BadgeType.TECH])

        return SemanticBadge(
            text=label,
            badge_type=badge_type,
            bg_color=palette["bg"],
            stroke_color=palette["stroke"],
            text_color=palette["text"],
            symbol_prefix=palette.get("prefix")
        )


class MetricPillEngine:
    """Motor de pastillas y micro-tarjetas de métricas visuales."""

    @staticmethod
    def format_metric(val: str, unit: str, label: str) -> Dict[str, Any]:
        return {
            "value": val,
            "unit": unit,
            "label": label,
            "formatted": f"{val} {unit}".strip()
        }
