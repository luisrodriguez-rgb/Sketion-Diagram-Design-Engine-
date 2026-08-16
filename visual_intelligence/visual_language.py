"""
Sketion Visual Language Engine (v9.2)
Adapta la estética y el tratamiento holístico del diagrama según el dialecto narrativo:
1. TECHNICAL_ARCHITECTURE: Límites de red, puertos de servicio, contenedores de infraestructura, badges de protocolo.
2. EXECUTIVE_STRATEGY: Hero centralizado, tarjetas de KPI de negocio, alto espacio en blanco, síntesis de valor.
3. OPERATIONS_LOGISTICS: Swimlanes de proceso, estados vivos con pulso, SLAs y trazabilidad de handoffs.
4. SECURITY_COMPLIANCE: Barreras Zero-Trust, bóvedas HSM perimetrales, sellos de auditoría WORM y callouts de riesgo.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, List, Optional


class VisualLanguageDialect(Enum):
    TECHNICAL_ARCHITECTURE = "TECHNICAL_ARCHITECTURE"
    EXECUTIVE_STRATEGY = "EXECUTIVE_STRATEGY"
    OPERATIONS_LOGISTICS = "OPERATIONS_LOGISTICS"
    SECURITY_COMPLIANCE = "SECURITY_COMPLIANCE"


@dataclass
class VisualLanguageTheme:
    dialect: VisualLanguageDialect
    canvas_bg: str
    primary_stroke: str
    secondary_stroke: str
    accent_hero: str
    container_bg: str
    container_border_style: str  # "solid", "dashed"
    kpi_enabled: bool
    status_pulse_enabled: bool
    kicker_tag: str


class VisualLanguageEngine:
    """Motor de adaptación de dialectos y lenguaje visual holístico."""

    _THEMES: Dict[VisualLanguageDialect, VisualLanguageTheme] = {
        VisualLanguageDialect.TECHNICAL_ARCHITECTURE: VisualLanguageTheme(
            dialect=VisualLanguageDialect.TECHNICAL_ARCHITECTURE,
            canvas_bg="#F8FAFC",
            primary_stroke="#2563EB",
            secondary_stroke="#64748B",
            accent_hero="#D93829",
            container_bg="#F1F5F9",
            container_border_style="solid",
            kpi_enabled=False,
            status_pulse_enabled=False,
            kicker_tag="SYSTEM ARCHITECTURE SPECIFICATION"
        ),
        VisualLanguageDialect.EXECUTIVE_STRATEGY: VisualLanguageTheme(
            dialect=VisualLanguageDialect.EXECUTIVE_STRATEGY,
            canvas_bg="#FFFFFF",
            primary_stroke="#0F172A",
            secondary_stroke="#94A3B8",
            accent_hero="#D93829",
            container_bg="#F8FAFC",
            container_border_style="solid",
            kpi_enabled=True,
            status_pulse_enabled=False,
            kicker_tag="EXECUTIVE VALUE CHAIN & STRATEGY"
        ),
        VisualLanguageDialect.OPERATIONS_LOGISTICS: VisualLanguageTheme(
            dialect=VisualLanguageDialect.OPERATIONS_LOGISTICS,
            canvas_bg="#F8FAFC",
            primary_stroke="#0284C7",
            secondary_stroke="#64748B",
            accent_hero="#D93829",
            container_bg="#F0F9FF",
            container_border_style="dashed",
            kpi_enabled=True,
            status_pulse_enabled=True,
            kicker_tag="OPERATIONAL WORKFLOW & SLA DISPATCH"
        ),
        VisualLanguageDialect.SECURITY_COMPLIANCE: VisualLanguageTheme(
            dialect=VisualLanguageDialect.SECURITY_COMPLIANCE,
            canvas_bg="#F8FAFC",
            primary_stroke="#7C3AED",
            secondary_stroke="#64748B",
            accent_hero="#DC2626",
            container_bg="#FAF5FF",
            container_border_style="dashed",
            kpi_enabled=False,
            status_pulse_enabled=False,
            kicker_tag="ZERO-TRUST SECURITY & AUDIT TRAIL"
        )
    }

    @classmethod
    def resolve_theme(cls, audience: str = "ENGINEER", domain_hint: str = "") -> VisualLanguageTheme:
        """Determina el tema de lenguaje visual óptimo para la audiencia y dominio."""
        aud = audience.upper().strip()
        dom = domain_hint.upper().strip()

        if "CEO" in aud or "EXEC" in aud or "INVESTOR" in aud or "STRATEGY" in dom:
            return cls._THEMES[VisualLanguageDialect.EXECUTIVE_STRATEGY]
        elif "OPERAT" in aud or "LOGISTICS" in dom or "SRE" in aud or "NOC" in aud:
            return cls._THEMES[VisualLanguageDialect.OPERATIONS_LOGISTICS]
        elif "AUDIT" in aud or "COMPLIANCE" in aud or "SECURITY" in dom or "HIPAA" in dom or "PCI" in dom:
            return cls._THEMES[VisualLanguageDialect.SECURITY_COMPLIANCE]
        else:
            return cls._THEMES[VisualLanguageDialect.TECHNICAL_ARCHITECTURE]
