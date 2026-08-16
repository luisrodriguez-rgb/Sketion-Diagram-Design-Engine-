"""
Sketion 4.0 — Evaluador de Idoneidad de Arquetipos (validation/fitness_score.py)
Calcula el Archetype Fitness Score (0-100) evaluando si la composición visual
y los arquetipos seleccionados resuelven intrínsecamente la naturaleza del problema
(socio-técnico, físico-digital, temporal, estratégico o cuantitativo)
en lugar de forzar un template genérico.
"""

from typing import Dict, Any, List, Tuple


def calculate_archetype_fitness(problem_domain: str,
                                chosen_structures: List[str],
                                covered_dimensions: List[str],
                                has_physical_space: bool = False,
                                has_user_journey: bool = False,
                                has_supply_chain: bool = False,
                                has_restrictions_matrix: bool = False) -> Tuple[int, List[str]]:
    """
    Evalúa si la composición visual resuelve multidimensionalmente el problema.
    """
    score = 100
    critiques = []
    
    # 1. Evaluación de Dominio Socio-Operacional / Físico
    if problem_domain in ["OPERATIONS_CAMPUS", "PHYSICAL_LOGISTICS", "RETAIL_QUEUE"]:
        # Debe contemplar espacio físico y jornada de personas
        if not has_physical_space:
            score -= 25
            critiques.append("Falta representación del espacio físico/planta en un problema de congestión de colas.")
        if not has_user_journey:
            score -= 20
            critiques.append("Falta mapa de experiencia/journey comparativo (As-Is vs To-Be).")
        if not has_supply_chain:
            score -= 15
            critiques.append("No se representó el flujo de abastecimiento entre CEDI y satélites.")
        if not has_restrictions_matrix:
            score -= 15
            critiques.append("Falta matriz de restricciones de capacidad horaria y picos.")
            
    # 2. Evaluación de Riqueza de Arquetipos (Anti-Monocultivo de Templates)
    unique_structures = set(chosen_structures)
    if len(unique_structures) < 2 and len(covered_dimensions) > 3:
        score -= 25
        critiques.append(f"Monocultivo estructural: se usó solo 1 tipo ({list(unique_structures)}) para un problema complejo multifacético.")
        
    return max(0, min(100, score)), critiques
