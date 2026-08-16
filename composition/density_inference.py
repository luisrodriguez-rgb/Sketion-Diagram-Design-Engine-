"""
Sketion 4.5 — Inferred Density Target Engine
Calcula de forma determinista y autónoma la densidad ideal (Target Density)
evitando flags manuales arbitrarios.
"""

from typing import Dict, Any, Optional


class DensityInferenceEngine:
    """Infiere la densidad visual óptima de un lienzo."""

    AUDIENCE_DENSITY_WEIGHTS = {
        "CEO": 2.0,
        "DIRECTIVO": 2.2,
        "OPERACIONES": 3.8,
        "PLANTA": 4.0,
        "TECH": 4.8,
        "DATA_ENGINEER": 5.2,
        "WORKSHOP": 3.2
    }

    ARCHETYPE_DENSITY_BASE = {
        "A": 3.0,  # El Cerebro
        "B": 3.5,  # Fases
        "C": 3.2,  # Flow con bucle
        "D": 2.8,  # El Duelo VS
        "E": 3.8,  # Swimlanes
        "F": 2.5,  # Embudo
        "G": 3.0,  # Escalera
        "S": 4.5   # Matriz Tabular
    }

    @classmethod
    def infer_target_density(cls,
                             audience_profile: str = "OPERACIONES",
                             archetype_code: str = "E",
                             node_count: int = 15,
                             frame_count: int = 3) -> Dict[str, Any]:
        """Calcula el rango y el target exacto de densidad."""
        aud_weight = cls.AUDIENCE_DENSITY_WEIGHTS.get(audience_profile.upper(), 3.5)
        arch_base = cls.ARCHETYPE_DENSITY_BASE.get(archetype_code.upper(), 3.2)

        # Factor de escala por número de nodos
        complexity_factor = min(1.5, max(0.8, (node_count / 12.0) ** 0.3))
        
        target_density = round((aud_weight * 0.4 + arch_base * 0.6) * complexity_factor, 1)
        
        # Rango admisible
        min_density = max(1.2, round(target_density - 1.2, 1))
        max_density = min(6.5, round(target_density + 1.2, 1))

        return {
            "target_density": target_density,
            "min_acceptable": min_density,
            "max_acceptable": max_density,
            "audience": audience_profile,
            "archetype": archetype_code,
            "rationale": f"Inferido por Audiencia {audience_profile} ({aud_weight}) y Arquetipo {archetype_code} ({arch_base})"
        }
