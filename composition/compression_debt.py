"""
Sketion 5.0 — Compression Debt Engine
Mide el porcentaje de carga semántica sacrificada entre el input y el renderizado final.
Fórmula: Compression Debt = (Entidades Críticas Input - Entidades Renderizadas) / Entidades Críticas Input * 100%
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Tuple


@dataclass
class CompressionAudit:
    total_input_entities: int
    rendered_entities: int
    compression_debt_pct: float
    status: str  # 'EXCELLENT', 'ACCEPTABLE', 'WARNING', 'CRITICAL'
    omitted_entities: List[str]


class CompressionDebtEngine:
    """Audita si el diagrama retuvo todas las entidades clave o sacrificó información."""

    @classmethod
    def calculate_debt(cls, input_entities: List[str], rendered_elements_labels: List[str]) -> CompressionAudit:
        if not input_entities:
            return CompressionAudit(0, 0, 0.0, "EXCELLENT", [])

        # Normalizar strings para matching
        rendered_corpus = " ".join([str(lbl).lower() for lbl in rendered_elements_labels])
        
        omitted = []
        for ent in input_entities:
            ent_low = ent.lower().strip()
            # Si ninguna palabra clave representativa de la entidad aparece en el render
            ent_words = [w for w in ent_low.split() if len(w) > 3]
            matched = any(w in rendered_corpus for w in ent_words) if ent_words else (ent_low in rendered_corpus)
            if not matched:
                omitted.append(ent)

        total_in = len(input_entities)
        omitted_count = len(omitted)
        rendered_count = total_in - omitted_count
        debt_pct = round((omitted_count / float(total_in)) * 100.0, 1)

        if debt_pct <= 5.0:
            status = "EXCELLENT (0-5% deuda)"
        elif debt_pct <= 12.0:
            status = "ACCEPTABLE (5-12% deuda)"
        elif debt_pct <= 22.0:
            status = "WARNING (12-22% deuda)"
        else:
            status = "CRITICAL (>22% deuda: información clave omitida)"

        return CompressionAudit(
            total_input_entities=total_in,
            rendered_entities=rendered_count,
            compression_debt_pct=debt_pct,
            status=status,
            omitted_entities=omitted
        )
