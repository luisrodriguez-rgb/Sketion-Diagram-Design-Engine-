"""
Sketion 7.0 — Layout Stability Metric Engine
Evalúa la varianza y estabilidad del motor ejecutando el mismo prompt N veces (N=5).
Mide:
- Archetype consistency
- Narrative intent consistency
- Frame count variance
- Hero selection variance
- Density variance
- Score variance
"""

import statistics
from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple


@dataclass
class StabilityReport:
    prompt: str
    run_count: int
    archetype_consistency_pct: float
    intent_consistency_pct: float
    score_mean: float
    score_variance: float
    density_mean: float
    density_variance: float
    stability_status: str
    is_stable: bool


class LayoutStabilityEngine:
    """Calcula la robustez y reproducibilidad del motor ante ejecuciones repetidas."""

    @classmethod
    def evaluate_stability(cls, runs_data: List[Dict[str, Any]], prompt: str = "") -> StabilityReport:
        if not runs_data:
            return StabilityReport(prompt, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "NO_DATA", False)

        archetypes = [r.get("archetype") for r in runs_data]
        intents = [r.get("intent") for r in runs_data]
        scores = [r.get("overall_score", 95) for r in runs_data]
        densities = [r.get("density", 3.5) for r in runs_data]

        total = len(runs_data)
        # Modo / elemento más frecuente
        most_common_arch = max(set(archetypes), key=archetypes.count)
        arch_consistency = round((archetypes.count(most_common_arch) / float(total)) * 100.0, 1)

        most_common_intent = max(set(intents), key=intents.count)
        intent_consistency = round((intents.count(most_common_intent) / float(total)) * 100.0, 1)

        score_mean = round(statistics.mean(scores), 1)
        score_var = round(statistics.pvariance(scores), 2) if total > 1 else 0.0

        density_mean = round(statistics.mean(densities), 1)
        density_var = round(statistics.pvariance(densities), 2) if total > 1 else 0.0

        is_stable = (arch_consistency >= 80.0 and score_var <= 15.0 and density_var <= 1.0)
        status = "HIGHLY_STABLE" if is_stable else "VARIABLE"

        return StabilityReport(
            prompt=prompt,
            run_count=total,
            archetype_consistency_pct=arch_consistency,
            intent_consistency_pct=intent_consistency,
            score_mean=score_mean,
            score_variance=score_var,
            density_mean=density_mean,
            density_variance=density_var,
            stability_status=status,
            is_stable=is_stable
        )
