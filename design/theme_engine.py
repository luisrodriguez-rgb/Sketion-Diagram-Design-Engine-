"""
Sketion Semantic Theme & Style Engine (v11.0)
Desacopla totalmente la Estructura Visual del Tema Estético.
Gestiona 8 estilos visuales, resolución de StyleIntent y StyleLock para presentaciones multi-board.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional, Union
from enum import Enum


class VisualStyleType(Enum):
    EDITORIAL = "editorial"
    TECHNICAL = "technical"
    EXECUTIVE = "executive"
    BLUEPRINT = "blueprint"
    ACADEMIC = "academic"
    WORKSHOP = "workshop"
    DATA_DENSE = "data_dense"
    MINIMAL = "minimal"


@dataclass
class SemanticColorRole:
    """Paleta semántica completa asignable a cualquier estructura."""
    background: str
    surface: str
    surface_elevated: str
    border: str
    primary_hero: str
    secondary_accent: str
    success: str
    warning: str
    danger: str
    neutral: str
    connector: str
    text_main: str
    text_muted: str
    font_family: int = 3  # Inter por defecto


@dataclass
class StyleIntent:
    """Parámetros de intención estilística del usuario o de la IA."""
    density: str = "medium"          # low, medium, high, very_high
    contrast: str = "high"           # low, medium, high
    hierarchy: str = "strong"        # subtle, balanced, strong
    ornamentation: str = "minimal"   # clean, minimal, rich
    colorfulness: str = "selective"  # monochrome, selective, vibrant
    formality: str = "high"          # casual, workshop, formal, high


class ThemeEngine:
    """Motor de gestión de temas y aplicación de roles cromáticos."""

    _PALETTES: Dict[VisualStyleType, SemanticColorRole] = {
        VisualStyleType.EDITORIAL: SemanticColorRole(
            background="#FFFFFF", surface="#FFFFFF", surface_elevated="#FFF5F2",
            border="#0F172A", primary_hero="#D93829", secondary_accent="#0284C7",
            success="#059669", warning="#D97706", danger="#DC2626",
            neutral="#64748B", connector="#0F172A", text_main="#0F172A", text_muted="#475569"
        ),
        VisualStyleType.TECHNICAL: SemanticColorRole(
            background="#FFFFFF", surface="#F8FAFC", surface_elevated="#EFF6FF",
            border="#CBD5E1", primary_hero="#2563EB", secondary_accent="#0284C7",
            success="#10B981", warning="#F59E0B", danger="#EF4444",
            neutral="#64748B", connector="#2563EB", text_main="#0F172A", text_muted="#64748B"
        ),
        VisualStyleType.EXECUTIVE: SemanticColorRole(
            background="#FFFFFF", surface="#FFFFFF", surface_elevated="#F8FAFC",
            border="#0F172A", primary_hero="#0F172A", secondary_accent="#D93829",
            success="#059669", warning="#D97706", danger="#DC2626",
            neutral="#94A3B8", connector="#0F172A", text_main="#0F172A", text_muted="#64748B"
        ),
        VisualStyleType.BLUEPRINT: SemanticColorRole(
            background="#0B2545", surface="#134074", surface_elevated="#1D4E89",
            border="#8DA9C4", primary_hero="#EEF4F8", secondary_accent="#00F0FF",
            success="#00FF88", warning="#FFB800", danger="#FF3366",
            neutral="#8DA9C4", connector="#EEF4F8", text_main="#FFFFFF", text_muted="#CBD5E1"
        ),
        VisualStyleType.ACADEMIC: SemanticColorRole(
            background="#FFFFFF", surface="#FFFFFF", surface_elevated="#F1F5F9",
            border="#334155", primary_hero="#475569", secondary_accent="#64748B",
            success="#059669", warning="#D97706", danger="#DC2626",
            neutral="#94A3B8", connector="#334155", text_main="#0F172A", text_muted="#475569"
        ),
        VisualStyleType.WORKSHOP: SemanticColorRole(
            background="#F8FAFC", surface="#FFE95C", surface_elevated="#F5BEC0",
            border="#0F172A", primary_hero="#D93829", secondary_accent="#3B82F6",
            success="#10B981", warning="#F59E0B", danger="#EF4444",
            neutral="#64748B", connector="#0F172A", text_main="#0F172A", text_muted="#334155"
        ),
        VisualStyleType.DATA_DENSE: SemanticColorRole(
            background="#FFFFFF", surface="#F8FAFC", surface_elevated="#FFF5F2",
            border="#CBD5E1", primary_hero="#D93829", secondary_accent="#2563EB",
            success="#059669", warning="#D97706", danger="#DC2626",
            neutral="#64748B", connector="#94A3B8", text_main="#0F172A", text_muted="#475569"
        ),
        VisualStyleType.MINIMAL: SemanticColorRole(
            background="#FFFFFF", surface="#FFFFFF", surface_elevated="#FFFFFF",
            border="#0F172A", primary_hero="#0F172A", secondary_accent="#0F172A",
            success="#059669", warning="#D97706", danger="#DC2626",
            neutral="#CBD5E1", connector="#0F172A", text_main="#0F172A", text_muted="#64748B"
        )
    }

    # StyleLock activo para presentaciones
    _LOCKED_THEME: Optional[SemanticColorRole] = None

    @classmethod
    def get_theme(cls, style: Union[str, VisualStyleType] = VisualStyleType.EDITORIAL) -> SemanticColorRole:
        """Devuelve el tema semántico activo o el locked."""
        if cls._LOCKED_THEME:
            return cls._LOCKED_THEME

        if isinstance(style, str):
            try:
                st = VisualStyleType(style.lower())
            except ValueError:
                st = VisualStyleType.EDITORIAL
        else:
            st = style

        return cls._PALETTES.get(st, cls._PALETTES[VisualStyleType.EDITORIAL])

    @classmethod
    def lock_style(cls, style: Union[str, VisualStyleType]):
        """Bloquea un estilo para mantener coherencia en múltiples tableros/slides."""
        cls._LOCKED_THEME = cls.get_theme(style)

    @classmethod
    def unlock_style(cls):
        """Libera el bloqueo de estilo."""
        cls._LOCKED_THEME = None
