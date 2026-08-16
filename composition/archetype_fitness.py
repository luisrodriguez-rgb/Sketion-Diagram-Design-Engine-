"""
Sketion 4.5 — Composition Intelligence & Archetype Decision Engine
Analiza la intención semántica del problema y clasifica/clasifica autónomamente los 20 arquetipos de negocio (A - T).
Devuelve el Arquetipo Seleccionado, el Score de Confianza (%) y alternativas viables.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional


@dataclass
class ArchetypeRecommendation:
    code: str
    name: str
    confidence: int  # 0 - 100
    rationale: str
    is_primary: bool = False


class CompositionIntelligenceEngine:
    """Motor de decisión de composición visual para Sketion."""

    ARCHETYPE_INTENT_RULES = [
        {
            "code": "D",
            "name": "El Duelo (VS)",
            "keywords": ["problema", "actual", "cuello de botella", "frente a", "vs", "antes", "después", "abandono", "fricción", "solución", "legacy", "caos"],
            "base_score": 30,
            "weight": 15
        },
        {
            "code": "E",
            "name": "La Cadena / Swimlanes Operativos",
            "keywords": ["cocina", "caja", "mesas", "salón", "roles", "operación", "actores", "planta", "cliente", "personal", "kds", "swimlane"],
            "base_score": 25,
            "weight": 14
        },
        {
            "code": "C",
            "name": "Flow Pipeline con Bucle",
            "keywords": ["flujo", "pipeline", "etapas", "capacidad", "saturación", "retraso", "proceso", "ciclo", "cola", "despacho", "bucle", "feedback"],
            "base_score": 25,
            "weight": 14
        },
        {
            "code": "A",
            "name": "El Cerebro (Hub Radial)",
            "keywords": ["ecosistema", "central", "hub", "plataforma", "unificado", "satélites", "módulos", "integración", "núcleo"],
            "base_score": 20,
            "weight": 12
        },
        {
            "code": "G",
            "name": "La Pirámide / Escalera de Madurez",
            "keywords": ["madurez", "roadmap", "niveles", "fases", "evolución", "crecimiento", "trimestre", "largo plazo"],
            "base_score": 15,
            "weight": 10
        },
        {
            "code": "S",
            "name": "Matriz Forense Tabular",
            "keywords": ["tabla", "comparativa", "características", "competencia", "planes", "precios", "matriz"],
            "base_score": 15,
            "weight": 12
        },
        {
            "code": "F",
            "name": "El Embudo (Funnel de Conversión)",
            "keywords": ["conversión", "embudo", "tráfico", "leads", "ventas", "cierre", "retención", "crm", "funnel"],
            "base_score": 15,
            "weight": 12
        }
    ]

    @classmethod
    def rank_archetypes(cls, unstructured_prompt: str) -> List[ArchetypeRecommendation]:
        """Evalúa un prompt arbitrario y clasifica los arquetipos por relevancia y confianza."""
        p_low = unstructured_prompt.lower()
        results = []

        for rule in cls.ARCHETYPE_INTENT_RULES:
            match_count = sum(1 for kw in rule["keywords"] if kw in p_low)
            confidence = min(98, rule["base_score"] + match_count * rule["weight"])
            
            rationale_parts = [kw for kw in rule["keywords"] if kw in p_low]
            rationale = f"Detectado por presencia de: {', '.join(rationale_parts[:4])}" if rationale_parts else "Score base"

            results.append(ArchetypeRecommendation(
                code=rule["code"],
                name=rule["name"],
                confidence=confidence,
                rationale=rationale
            ))

        results.sort(key=lambda r: r.confidence, reverse=True)
        if results:
            results[0].is_primary = True
        return results

    @classmethod
    def plan_multi_frame_composition(cls, unstructured_prompt: str) -> List[Tuple[str, str, int, str]]:
        """
        Deduce si el problema requiere un multi-frame y asigna una narrativa coherente
        respetando la Regla Anti-Monocultivo.
        """
        ranked = cls.rank_archetypes(unstructured_prompt)
        
        # Si el prompt habla de problema + actores + capacidad -> 3 frames narrativos
        p_low = unstructured_prompt.lower()
        has_problem_vs_solution = any(k in p_low for k in ["actual", "problema", "cuello de botella", "solución"])
        has_actors = any(k in p_low for k in ["cliente", "cocina", "caja", "mesas", "roles"])
        has_capacity_or_loop = any(k in p_low for k in ["capacidad", "saturación", "filas", "espera", "tiempo"])

        plan = []
        if has_problem_vs_solution:
            plan.append(("FRAME 1", "D", 95, "El Duelo VS: Diagnóstico de Fricciones As-Is vs Visión To-Be"))
        if has_actors:
            plan.append(("FRAME 2", "E", 92, "Swimlanes Operativos: Coordinación entre Cliente, Backend, Cocina y Salón"))
        if has_capacity_or_loop:
            plan.append(("FRAME 3", "C", 89, "Flow Pipeline: Control de Capacidad y Bucle de Espera/Saturación"))

        if not plan:
            top = ranked[0]
            plan.append(("FRAME 1", top.code, top.confidence, f"Arquetipo Principal: {top.name}"))

        return plan
