"""
Sketion Design System — Visual Tokens (v8.5)
Definición formal de tokens tipográficos, cromáticos, espaciales y de jerarquía.
Garantiza coherencia visual matemática y elimina variaciones arbitrarias.
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass(frozen=True)
class TypographyScale:
    FRAME_TITLE: int = 22
    FRAME_KICKER: int = 12
    SECTION_HEADER: int = 13
    CARD_TITLE_LARGE: int = 16
    CARD_TITLE_MEDIUM: int = 14
    CARD_TITLE_SMALL: int = 13
    BODY_TEXT: int = 12
    BODY_MUTED: int = 11
    BADGE_TEXT: int = 10
    MICRO_LABEL: int = 9


@dataclass(frozen=True)
class SpacingScale:
    CANVAS_GAP: float = 140.0
    FRAME_PADDING_X: float = 50.0
    FRAME_PADDING_Y: float = 45.0
    SECTION_GAP: float = 38.0
    GRID_GAP_LARGE: float = 24.0
    GRID_GAP_MEDIUM: float = 20.0
    GRID_GAP_SMALL: float = 14.0
    TEXT_STACK_GAP: float = 6.0
    BADGE_AIR_GAP: float = 12.0


@dataclass(frozen=True)
class SemanticColorPalette:
    # Fondos
    CANVAS_BG: str = "#F8FAFC"
    CARD_BG_DEFAULT: str = "#FFFFFF"
    CARD_BG_HERO: str = "#FFF5F2"
    CARD_BG_MUTED: str = "#F1F5F9"
    CARD_BG_STREAM: str = "#EEF2FF"
    CARD_BG_DATABASE: str = "#EFF6FF"

    # Bordes & Trazos
    STROKE_DEFAULT: str = "#CBD5E1"
    STROKE_HERO: str = "#D93829"
    STROKE_PRIMARY: str = "#2563EB"
    STROKE_STREAM: str = "#4F46E5"
    STROKE_SUCCESS: str = "#059669"
    STROKE_WARNING: str = "#D97706"
    STROKE_DANGER: str = "#DC2626"
    STROKE_MUTED: str = "#94A3B8"

    # Textos
    TEXT_PRIMARY: str = "#0F172A"
    TEXT_SECONDARY: str = "#334155"
    TEXT_MUTED: str = "#64748B"
    TEXT_HERO: str = "#991B1B"
    TEXT_WHITE: str = "#FFFFFF"
