"""
Sketion Repair Engine Orchestrator
Orquestador central de auto-reparaciones para escenas Excalidraw:
1. Reparación de Elementos de Texto y Tipografía
2. Reparación de Vinculaciones (containerId <-> boundElements)
3. Reparación de Confinamiento de Frames (coordenadas relativas -> absolutas y auto-expansión)
4. Reparación de Colisiones Espaciales (separación de tarjetas superpuestas)
5. Reparación de Acentos Visuales (Regla del Acento Único por marco)
"""

from typing import Dict, Any, List, Tuple
from .accent_repair import repair_accents
from .binding_repair import repair_bindings
from .frame_repair import repair_frame_containment
from .text_repair import repair_text_elements
from .spatial_repair import repair_spatial_collisions


class RepairEngine:
    """Orquestador maestro de auto-reparaciones para escenas Excalidraw."""

    @staticmethod
    def auto_repair(scene_data: Dict[str, Any],
                    primary_hero_id: str = None,
                    neutral_bg: str = "#FFFFFF",
                    neutral_stroke: str = "#0F172A") -> Tuple[Dict[str, Any], List[str]]:
        all_repairs = []

        # 1. Reparación de Elementos de Texto y Tipografía
        text_repairs = repair_text_elements(scene_data)
        all_repairs.extend(text_repairs)

        # 2. Reparación de Vinculaciones bidireccionales
        binding_repairs = repair_bindings(scene_data)
        all_repairs.extend(binding_repairs)

        # 3. Reparación de Colisiones Espaciales entre Tarjetas
        collision_repairs = repair_spatial_collisions(scene_data)
        all_repairs.extend(collision_repairs)

        # 4. Reparación de Confinamiento y Posicionamiento de Frames
        frame_repairs = repair_frame_containment(scene_data)
        all_repairs.extend(frame_repairs)

        # 5. Reparación de Acentos Visuales (Hero único por marco)
        accent_repairs = repair_accents(scene_data, primary_hero_id=primary_hero_id,
                                        neutral_bg=neutral_bg, neutral_stroke=neutral_stroke)
        all_repairs.extend(accent_repairs)

        return scene_data, all_repairs


def repair_scene(scene_data: Dict[str, Any], **kwargs) -> Tuple[Dict[str, Any], List[str]]:
    """Función de conveniencia para invocar la auto-reparación."""
    return RepairEngine.auto_repair(scene_data, **kwargs)
