"""
Sketion Design System Intelligence Package (v8.5 & v8.6)
Proporciona tokens visuales formales, registro de selección contextual de componentes
y motor de consistencia visual (Visual Consistency Score - VCS).
"""

from .visual_tokens import TypographyScale, SpacingScale, SemanticColorPalette
from .component_registry import (
    ImportanceLevel,
    AudienceProfile,
    ResolvedComponentSpec,
    ComponentRegistry
)
from .consistency import ConsistencyReport, VisualConsistencyEngine

__all__ = [
    "TypographyScale",
    "SpacingScale",
    "SemanticColorPalette",
    "ImportanceLevel",
    "AudienceProfile",
    "ResolvedComponentSpec",
    "ComponentRegistry",
    "ConsistencyReport",
    "VisualConsistencyEngine"
]
