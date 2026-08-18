"""
Sketion Semantic Structural Retrieval Engine (v11.0)
Recupera las composiciones de referencia más afines a partir de un prompt o ContentModel.
Devuelve: Candidatos de Plantilla + Patrones de Composición + Vocabulario de Primitivas + Restricciones.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import re

from .reference_compositions import REFERENCE_COMPOSITIONS, ReferenceComposition
from .content_model import ContentModel
from composition.composition_patterns import CompositionPattern, CompositionPatternRegistry


@dataclass
class RetrievalResult:
    matched_references: List[ReferenceComposition]
    recommended_pattern: CompositionPattern
    recommended_layout: str
    suggested_primitives: List[str]
    suggested_connectors: List[str]
    complexity: str
    tokens_saved_ratio: float = 0.85  # Ahorro de tokens al enviar solo esquema relevante


class SemanticRetrievalEngine:
    """Motor de búsqueda semántica estructural optimizado para bajo consumo de tokens."""

    @classmethod
    def match(cls, query_or_content: str, domain_hint: Optional[str] = None) -> RetrievalResult:
        """Encuentra los arquetipos estructurales óptimos según palabras clave y semántica."""
        q = query_or_content.lower()
        words = set(re.findall(r"\w+", q))

        scored_candidates = []
        for ref in REFERENCE_COMPOSITIONS:
            score = 0
            # 1. Coincidencia estricta de dominio
            if domain_hint and ref.domain == domain_hint.lower():
                score += 35
            elif ref.domain in words:
                score += 15

            # 2. Coincidencia de palabras clave y términos técnicos
            for kw in ref.keywords:
                if kw in q:
                    score += 25
                elif any(w in kw for w in words):
                    score += 10

            scored_candidates.append((score, ref))

        scored_candidates.sort(key=lambda x: x[0], reverse=True)
        top_matches = [ref for score, ref in scored_candidates[:3]]

        if not top_matches:
            # Fallback a composición por defecto
            top_matches = [REFERENCE_COMPOSITIONS[0]]

        best_ref = top_matches[0]
        try:
            rec_pattern = CompositionPattern(best_ref.pattern)
        except ValueError:
            rec_pattern = CompositionPattern.LAYERED_ARCHITECTURE

        primitives = list(set(best_ref.sample_nodes))
        connectors = list(set(best_ref.sample_connectors))

        return RetrievalResult(
            matched_references=top_matches,
            recommended_pattern=rec_pattern,
            recommended_layout=best_ref.layout_type,
            suggested_primitives=primitives,
            suggested_connectors=connectors,
            complexity=best_ref.complexity
        )
