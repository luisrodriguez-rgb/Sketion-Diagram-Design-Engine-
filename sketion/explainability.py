"""
Sketion Explainability Engine (v9.3)
Genera la traza estructurada y explicable de las decisiones de diseño arquitectónico
tomadas por el motor de Sketion para cualquier diagrama renderizado (`result.explain()`).
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional


@dataclass
class DesignDecisionTrace:
    title: str
    target_audience: str
    primary_objective: str
    selected_archetype: str
    archetype_rationale: str
    hero_component: str
    hero_rationale: str
    visual_language: str
    aspect_ratio: str
    entity_count: int
    recognized_brands: List[str]
    vcs_score: float
    repair_dependency: float = 0.0

    def to_markdown(self) -> str:
        """Formatea la traza de decisión como un reporte de explicabilidad legible en Markdown."""
        brands_str = ", ".join(self.recognized_brands) if self.recognized_brands else "Entidades genéricas estandarizadas"
        return f"""
# 🧠 SKETION DESIGN DECISION TRACE

* **Diagram Title:** {self.title}
* **Target Audience:** `{self.target_audience}`
* **Primary Objective:** {self.primary_objective}

---

### 🏛️ Spatial Architecture & Composition
* **Selected Archetype:** `{self.selected_archetype}`
* **Archetype Rationale:** {self.archetype_rationale}
* **Aspect Ratio:** `{self.aspect_ratio}`
* **Visual Language Dialect:** `{self.visual_language}`

---

### 🌟 Hero Focus & Semantic Hierarchy
* **Hero Entity:** `{self.hero_component}`
* **Hero Rationale:** {self.hero_rationale}
* **Total Entities Rendered:** {self.entity_count}
* **Recognized Brand Technologies:** {brands_str}

---

### 📊 Quality & Consistency Metrics
* **Visual Consistency Score (VCS):** `{self.vcs_score:.1f} / 100`
* **Repair Dependency Score (RDS):** `{self.repair_dependency:.2f}` (100% Autonomía — Zero Human Interventions)
""".strip()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "target_audience": self.target_audience,
            "primary_objective": self.primary_objective,
            "selected_archetype": self.selected_archetype,
            "archetype_rationale": self.archetype_rationale,
            "hero_component": self.hero_component,
            "hero_rationale": self.hero_rationale,
            "visual_language": self.visual_language,
            "aspect_ratio": self.aspect_ratio,
            "entity_count": self.entity_count,
            "recognized_brands": self.recognized_brands,
            "vcs_score": self.vcs_score,
            "repair_dependency": self.repair_dependency
        }
