"""
Sketion Design System — Component Registry & Contextual Selection Rules (v8.5)
Selecciona el componente visual exacto evaluando la intersección multidimensional:
(Tipo Semántico + Nivel de Importancia + Perfil de Audiencia + Marca + Arquetipo Espacial + Estado Operativo).
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Dict, Any, List

from visual_intelligence.semantic_shapes import SemanticShapeType, SemanticShapeClassifier
from visual_intelligence.brand_registry import BrandRegistry, BrandSpec
from visual_intelligence.iconography import SemanticIconRegistry
from design.visual_tokens import TypographyScale, SpacingScale, SemanticColorPalette


class ImportanceLevel(Enum):
    HERO = "HERO"
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"
    TERTIARY = "TERTIARY"


class AudienceProfile(Enum):
    EXECUTIVE = "EXECUTIVE"
    ENGINEER = "ENGINEER"
    AUDITOR = "AUDITOR"
    OPERATOR = "OPERATOR"
    UNIVERSAL = "UNIVERSAL"


@dataclass
class ResolvedComponentSpec:
    shape_type: SemanticShapeType
    title: str
    sublabel: str
    badge: str
    icon: str
    bg_color: str
    stroke_color: str
    stroke_width: float
    is_hero: bool
    font_size: int
    tech_tags: List[str]


class ComponentRegistry:
    """Registro maestro de reglas de diseño del sistema."""

    @classmethod
    def resolve(cls,
                label: str,
                role: str = "service",
                importance: ImportanceLevel = ImportanceLevel.PRIMARY,
                audience: AudienceProfile = AudienceProfile.UNIVERSAL,
                archetype: str = "LAYERED",
                description: str = "",
                status: str = "ACTIVE") -> ResolvedComponentSpec:
        """Resuelve contextual y deterministamente el componente visual del Design System."""
        lbl_clean = label.strip()
        is_hero = (importance == ImportanceLevel.HERO)

        # 1. Detección de Marca
        brand = BrandRegistry.match_brand(lbl_clean) or BrandRegistry.match_brand(description)

        # 2. Resolución de Ícono
        icon = brand.vector_icon if brand else SemanticIconRegistry.resolve_icon(f"{lbl_clean} {role} {description}")

        # 3. Forma Semántica
        shape_spec = SemanticShapeClassifier.classify_entity(f"{lbl_clean} {description}", domain=role, is_hero=is_hero)
        shape_type = shape_spec.shape_type

        # 4. Paleta Cromática y Tokens
        if is_hero:
            bg_col = SemanticColorPalette.CARD_BG_HERO
            stroke_col = SemanticColorPalette.STROKE_HERO
            stroke_w = 2.0
            badge = "HERO CORE"
            font_size = TypographyScale.CARD_TITLE_LARGE
        elif brand:
            bg_col = brand.bg_color
            stroke_col = brand.brand_color
            stroke_w = 1.5
            badge = brand.category.replace("_", " ")
            font_size = TypographyScale.CARD_TITLE_MEDIUM
        elif shape_type == SemanticShapeType.DATABASE_CYLINDER:
            bg_col = SemanticColorPalette.CARD_BG_DATABASE
            stroke_col = SemanticColorPalette.STROKE_PRIMARY
            stroke_w = 1.5
            badge = "ACID DB"
            font_size = TypographyScale.CARD_TITLE_MEDIUM
        elif shape_type == SemanticShapeType.STREAMING_PIPE:
            bg_col = SemanticColorPalette.CARD_BG_STREAM
            stroke_col = SemanticColorPalette.STROKE_STREAM
            stroke_w = 1.8
            badge = "EVENT STREAM"
            font_size = TypographyScale.CARD_TITLE_MEDIUM
        else:
            bg_col = SemanticColorPalette.CARD_BG_DEFAULT
            stroke_col = SemanticColorPalette.STROKE_DEFAULT
            stroke_w = 1.5
            badge = role.upper()
            font_size = TypographyScale.CARD_TITLE_MEDIUM

        # 5. Adaptación según Audiencia
        if audience == AudienceProfile.EXECUTIVE:
            # Simplificar subtítulo para ejecutivos (menos ruido técnico)
            sublabel = description.split(".")[0] if "." in description else description
        elif audience == AudienceProfile.AUDITOR:
            badge = f"AUDIT · {badge}"
            sublabel = description
        else:
            sublabel = description

        tags = brand.tech_tags if brand else []

        return ResolvedComponentSpec(
            shape_type=shape_type,
            title=lbl_clean,
            sublabel=sublabel,
            badge=badge,
            icon=icon,
            bg_color=bg_col,
            stroke_color=stroke_col,
            stroke_width=stroke_w,
            is_hero=is_hero,
            font_size=font_size,
            tech_tags=tags
        )
