"""
Sketion Adaptive Aspect Ratio & Layout Packing Engine (v9.0)
Calcula y adapta automáticamente la geometría, número de columnas, espaciado
y empaquetado de componentes según la proporción de destino deseada:
- WIDESCREEN_16_9: 16:9 (Presentaciones, Keynote, Figma, Monitores Widescreen)
- STANDARD_4_3: 4:3 (Pitch Decks, Tablets y Documentación horizontal)
- SQUARE_1_1: 1:1 (Embeds de GitHub README, Confluence Cards)
- PORTRAIT_DOCUMENT: 9:16 / 3:4 (Reportes técnicos en PDF, Notion y A4)
- AUTO_CONTENT: Bounding box ceñido al contenido real
"""

from enum import Enum
from dataclasses import dataclass
from typing import Tuple, Dict, Any, List


class AspectRatioType(Enum):
    WIDESCREEN_16_9 = "16:9"
    STANDARD_4_3 = "4:3"
    SQUARE_1_1 = "1:1"
    PORTRAIT_DOCUMENT = "3:4"
    AUTO_CONTENT = "AUTO"


@dataclass
class AspectRatioSpec:
    aspect_type: AspectRatioType
    base_w: float
    base_h: float
    max_cols: int
    optimal_card_h: float
    gap: float
    padding_x: float
    padding_y: float


class AspectRatioAdapter:
    """Adaptador de proporciones y empaquetado inteligente para diagramas."""

    _SPECS: Dict[AspectRatioType, AspectRatioSpec] = {
        AspectRatioType.WIDESCREEN_16_9: AspectRatioSpec(
            aspect_type=AspectRatioType.WIDESCREEN_16_9,
            base_w=1760.0,
            base_h=990.0,
            max_cols=4,
            optimal_card_h=135.0,
            gap=22.0,
            padding_x=50.0,
            padding_y=45.0
        ),
        AspectRatioType.STANDARD_4_3: AspectRatioSpec(
            aspect_type=AspectRatioType.STANDARD_4_3,
            base_w=1440.0,
            base_h=1080.0,
            max_cols=3,
            optimal_card_h=145.0,
            gap=20.0,
            padding_x=45.0,
            padding_y=45.0
        ),
        AspectRatioType.SQUARE_1_1: AspectRatioSpec(
            aspect_type=AspectRatioType.SQUARE_1_1,
            base_w=1200.0,
            base_h=1200.0,
            max_cols=2,
            optimal_card_h=155.0,
            gap=24.0,
            padding_x=45.0,
            padding_y=45.0
        ),
        AspectRatioType.PORTRAIT_DOCUMENT: AspectRatioSpec(
            aspect_type=AspectRatioType.PORTRAIT_DOCUMENT,
            base_w=1100.0,
            base_h=1460.0,
            max_cols=2,
            optimal_card_h=140.0,
            gap=18.0,
            padding_x=40.0,
            padding_y=40.0
        ),
        AspectRatioType.AUTO_CONTENT: AspectRatioSpec(
            aspect_type=AspectRatioType.AUTO_CONTENT,
            base_w=1600.0,
            base_h=600.0,
            max_cols=4,
            optimal_card_h=135.0,
            gap=20.0,
            padding_x=45.0,
            padding_y=40.0
        )
    }

    @classmethod
    def get_spec(cls, aspect_type: AspectRatioType = AspectRatioType.WIDESCREEN_16_9) -> AspectRatioSpec:
        return cls._SPECS.get(aspect_type, cls._SPECS[AspectRatioType.WIDESCREEN_16_9])

    @classmethod
    def calculate_grid_layout(cls, total_items: int,
                              aspect_type: AspectRatioType = AspectRatioType.WIDESCREEN_16_9,
                              override_w: float = None) -> Tuple[int, float, float, float, float]:
        """
        Calcula el número óptimo de columnas, ancho de tarjeta y alturas para llenar el ratio armónicamente.
        Retorna: (cols, card_w, card_h, usable_w, gap)
        """
        spec = cls.get_spec(aspect_type)
        w = override_w or spec.base_w
        usable_w = w - (spec.padding_x * 2.0)

        # Determinar columnas según ratio y cantidad de elementos
        if aspect_type in [AspectRatioType.PORTRAIT_DOCUMENT, AspectRatioType.SQUARE_1_1]:
            cols = min(spec.max_cols, max(1, min(2, total_items)))
        elif total_items <= 2:
            cols = total_items
        elif total_items == 3:
            cols = 3
        elif total_items == 4:
            cols = 4 if aspect_type == AspectRatioType.WIDESCREEN_16_9 else 2
        elif total_items <= 6:
            cols = 3
        else:
            cols = spec.max_cols

        card_w = (usable_w - (cols - 1) * spec.gap) / max(1, cols)
        card_h = spec.optimal_card_h

        return cols, card_w, card_h, usable_w, spec.gap
