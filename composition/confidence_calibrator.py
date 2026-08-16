"""
Sketion 5.0 — Confidence Calibration & Uncertainty Tiers
Calibra formalmente la certidumbre de decisión compositiva y activa acciones proporcionales:
- 90–100% -> HIGH_CONFIDENCE (Render directo con arquetipo primario)
- 75–89%  -> CONFIDENT (Render con validación de señales secundarias)
- 60–74%  -> MODERATE (Búsqueda entre Top-2 candidatos)
- 40–59%  -> AMBIGUOUS (Generación y evaluación de Top-3 candidatos)
- 20–39%  -> UNCERTAIN (Generación de Top-5 candidatos con Composition Judge)
- 0–19%   -> COMPOSITION_UNKNOWN (Deep Search + advertencia explícita)
"""

from dataclasses import dataclass
from typing import Dict, Any, List


class UncertaintyTier:
    HIGH_CONFIDENCE = "HIGH_CONFIDENCE"
    CONFIDENT = "CONFIDENT"
    MODERATE = "MODERATE"
    AMBIGUOUS = "AMBIGUOUS"
    UNCERTAIN = "UNCERTAIN"
    UNKNOWN = "COMPOSITION_UNKNOWN"


@dataclass
class CalibratedConfidence:
    raw_confidence: int
    calibrated_confidence: int
    tier: str
    recommended_action: str
    candidates_to_evaluate: int
    requires_composition_judge: bool


class ConfidenceCalibrator:
    """Calibra la certidumbre del motor y determina la estrategia de búsqueda requerida."""

    @classmethod
    def calibrate(cls, raw_confidence: int, margin_to_runner_up: int) -> CalibratedConfidence:
        # Ponderar la confianza cruda con la distancia al segundo lugar
        calibrated = int(raw_confidence * 0.7 + min(30, margin_to_runner_up) * 1.0)
        calibrated = min(98, max(5, calibrated))

        if calibrated >= 90:
            tier = UncertaintyTier.HIGH_CONFIDENCE
            action = "Renderizado directo: La intención semántica es inequívoca."
            cand_count = 1
            need_judge = False
        elif calibrated >= 75:
            tier = UncertaintyTier.CONFIDENT
            action = "Renderizado seguro con verificación de coherencia de conectores."
            cand_count = 1
            need_judge = False
        elif calibrated >= 60:
            tier = UncertaintyTier.MODERATE
            action = "Evaluar Top-2 candidatos en memoria antes de comprometer el layout."
            cand_count = 2
            need_judge = True
        elif calibrated >= 40:
            tier = UncertaintyTier.AMBIGUOUS
            action = "Evaluar Top-3 candidatos con el Composition Judge (Fidelidad Narrativa)."
            cand_count = 3
            need_judge = True
        elif calibrated >= 20:
            tier = UncertaintyTier.UNCERTAIN
            action = "Incertidumbre alta: Búsqueda compositiva exhaustiva (Top-5 candidatos)."
            cand_count = 5
            need_judge = True
        else:
            tier = UncertaintyTier.UNKNOWN
            action = "Composición Desconocida: Deep Composition Search con alerta explícita en reporte."
            cand_count = 5
            need_judge = True

        return CalibratedConfidence(
            raw_confidence=raw_confidence,
            calibrated_confidence=calibrated,
            tier=tier,
            recommended_action=action,
            candidates_to_evaluate=cand_count,
            requires_composition_judge=need_judge
        )
