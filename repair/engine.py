"""
Sketion Repair Engine Orchestrator
"""
from typing import Dict, Any, List, Tuple
from .accent_repair import repair_accents
from .binding_repair import repair_bindings

class RepairEngine:
    """Orquestador de auto-reparaciones para escenas Excalidraw."""

    @staticmethod
    def auto_repair(scene_data: Dict[str, Any],
                    primary_hero_id: str = None,
                    neutral_bg: str = "#FFFFFF",
                    neutral_stroke: str = "#0F172A") -> Tuple[Dict[str, Any], List[str]]:
        all_repairs = []

        # 1. Reparación de Bindings
        binding_repairs = repair_bindings(scene_data)
        all_repairs.extend(binding_repairs)

        # 2. Reparación de Acentos
        accent_repairs = repair_accents(scene_data, primary_hero_id=primary_hero_id,
                                        neutral_bg=neutral_bg, neutral_stroke=neutral_stroke)
        all_repairs.extend(accent_repairs)

        return scene_data, all_repairs


def repair_scene(scene_data: Dict[str, Any], **kwargs) -> Tuple[Dict[str, Any], List[str]]:
    """Función de conveniencia para invocar la auto-reparación."""
    return RepairEngine.auto_repair(scene_data, **kwargs)
