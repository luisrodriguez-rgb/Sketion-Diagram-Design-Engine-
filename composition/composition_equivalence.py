"""
Sketion 6.0 — Composition Equivalence Engine
Formaliza las clases de equivalencia narrativa entre arquetipos.
Reconoce cuándo dos arquetipos distintos resuelven legítimamente la misma historia
con diferente énfasis compositivo (ej. Duelo VS vs Swimlanes vs Flow).
"""

from dataclasses import dataclass
from typing import List, Dict, Set, Tuple


@dataclass
class EquivalenceEvaluation:
    selected_archetype: str
    primary_expected: str
    is_exact_match: bool
    is_narratively_equivalent: bool
    equivalence_class: str
    rationale: str


class CompositionEquivalenceEngine:
    """Evalúa la equivalencia funcional y narrativa entre soluciones compositivas."""

    # Clases de equivalencia formal
    EQUIVALENCE_CLASSES = {
        "TRANSFORMATION_OPERATIONS": {
            "name": "Transformación & Coordinación Operativa",
            "archetypes": {"D", "E", "C", "P"},
            "description": "Duelo (visión macro dolor vs solución), Swimlanes (coordinación de actores), Flow (pipeline con bucles) y Cadena (flujo de extremo a extremo)."
        },
        "COMPARISON_BENCHMARK": {
            "name": "Comparativa & Análisis de Atributos",
            "archetypes": {"D", "S", "Q"},
            "description": "Duelo (contraste polarizado), Matriz Tabular (evaluación celda por celda) y Benchmark Radar."
        },
        "ECOSYSTEM_ARCHITECTURE": {
            "name": "Ecosistema & Arquitectura Modular",
            "archetypes": {"A", "N", "J", "T"},
            "description": "Cerebro Hub (radial), Paneles Satélite, Cebolla y Caja Explotada."
        },
        "CAUSAL_INVESTIGATION": {
            "name": "Investigación Causal & Post-Mortem",
            "archetypes": {"M", "C", "D"},
            "description": "Ishikawa (espina de pescado causa-raíz), Flow (recorrido de fallo) y Duelo (antes vs después del incidente)."
        },
        "MATURITY_TEMPORAL": {
            "name": "Evolución Temporal & Fases",
            "archetypes": {"G", "B", "R"},
            "description": "Pirámide/Escalera de Madurez, Fases con Gates y Roadmap Temporal."
        },
        "DECISION_BRANCHING": {
            "name": "Triaje & Árbol de Reglas",
            "archetypes": {"O", "C", "E"},
            "description": "Árbol Condicional, Flow con bifurcaciones y Swimlanes con roles de escalado."
        }
    }

    @classmethod
    def evaluate_equivalence(cls, selected: str, primary: str, acceptable_set: List[str]) -> EquivalenceEvaluation:
        is_exact = (selected == primary)
        is_acceptable = (selected in acceptable_set)

        matched_class = "INDEPENDENT"
        for class_id, class_data in cls.EQUIVALENCE_CLASSES.items():
            if primary in class_data["archetypes"] and selected in class_data["archetypes"]:
                matched_class = class_data["name"]
                break

        is_equivalent = is_exact or (is_acceptable and matched_class != "INDEPENDENT")

        if is_exact:
            rationale = f"Acierto exacto con el arquetipo primario '{primary}'."
        elif is_equivalent:
            rationale = f"Equivalencia narrativa en '{matched_class}': {selected} y {primary} son válidos."
        else:
            rationale = f"Composición fuera de la clase de equivalencia esperada ({'/'.join(acceptable_set)})."

        return EquivalenceEvaluation(
            selected_archetype=selected,
            primary_expected=primary,
            is_exact_match=is_exact,
            is_narratively_equivalent=is_equivalent,
            equivalence_class=matched_class,
            rationale=rationale
        )
