"""
Sketion 5.0 — Composition Search & Candidate Layout Engine
Cuando el margen de confianza entre los dos arquetipos superiores es estrecho (<15%),
el motor genera dos composiciones candidatas y evalúa cuál maximiza la fidelidad y legibilidad.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Tuple
from composition.signal_extractor import SemanticSignalExtractor, InterpretableArchetypeScore


@dataclass
class CandidateComparison:
    is_ambiguous: bool
    primary_candidate: InterpretableArchetypeScore
    secondary_candidate: InterpretableArchetypeScore
    confidence_margin: int
    decision_mode: str  # 'HIGH_CONFIDENCE_DIRECT' o 'DUAL_CANDIDATE_SEARCH'
    recommended_strategy: str


class CompositionSearchEngine:
    """Evalúa la certidumbre de la decisión compositiva y activa búsqueda de candidatos si es ambigua."""

    @classmethod
    def evaluate_decision_confidence(cls, prompt: str) -> CandidateComparison:
        scores = SemanticSignalExtractor.evaluate_archetypes_with_signals(prompt)
        if len(scores) < 2:
            return CandidateComparison(
                is_ambiguous=False,
                primary_candidate=scores[0],
                secondary_candidate=scores[0],
                confidence_margin=100,
                decision_mode="HIGH_CONFIDENCE_DIRECT",
                recommended_strategy="Ejecutar renderizado directo con Arquetipo Principal."
            )

        top1 = scores[0]
        top2 = scores[1]
        margin = top1.confidence - top2.confidence

        is_ambiguous = (margin < 15)
        mode = "DUAL_CANDIDATE_SEARCH" if is_ambiguous else "HIGH_CONFIDENCE_DIRECT"

        if is_ambiguous:
            strat = f"Margen estrecho ({margin}%): Generar y comparar candidato A ({top1.code}: {top1.name}) vs candidato B ({top2.code}: {top2.name})."
        else:
            strat = f"Decisión de alta certidumbre (Margen: {margin}%). Proceder con Arquetipo {top1.code}: {top1.name}."

        return CandidateComparison(
            is_ambiguous=is_ambiguous,
            primary_candidate=top1,
            secondary_candidate=top2,
            confidence_margin=margin,
            decision_mode=mode,
            recommended_strategy=strat
        )
