"""
Sketion Repair Engine Package
Módulo desacoplado de auto-reparación y auto-corrección de diagramas.
"""
from .engine import RepairEngine, repair_scene
from .accent_repair import repair_accents
from .binding_repair import repair_bindings

__all__ = [
    "RepairEngine",
    "repair_scene",
    "repair_accents",
    "repair_bindings"
]
