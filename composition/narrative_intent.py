"""
Sketion 5.0 — Narrative Intent Engine & Implicit Question Resolver
Antes de seleccionar primitivas o arquetipos, infiere:
1. La Intención Narrativa Dominante (¿Qué historia visual debe contar el diagrama?)
2. La Pregunta Implícita (¿Qué pregunta central debe responder a primera vista?)
3. El Arquetipo Candidato Óptimo basado en narrativa, no solo en palabras clave aisladas.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple


class NarrativeIntentType:
    COMPARISON = "COMPARISON"                 # Comparar opciones A vs B, Legacy vs Modern
    TRANSFORMATION = "TRANSFORMATION"         # De estado actual caótico (As-Is) a estado optimizado (To-Be)
    CAUSAL_ANALYSIS = "CAUSAL_ANALYSIS"       # ¿Por qué ocurre este problema/falla? (Root cause, post-mortem)
    OPERATIONAL_FLOW = "OPERATIONAL_FLOW"     # ¿Cómo interactúan múltiples actores en el tiempo? (Swimlanes)
    DECISION_TRIAGE = "DECISION_TRIAGE"       # ¿Qué camino tomar según condiciones? (Árbol if/else)
    ECOSYSTEM_HUB = "ECOSYSTEM_HUB"           # ¿Cómo se integran múltiples módulos alrededor de un núcleo?
    VALUE_CHAIN = "VALUE_CHAIN"               # ¿Cómo viaja el valor/producto a través de la cadena física/lógica?
    MATURITY_ROADMAP = "MATURITY_ROADMAP"     # ¿Cómo evoluciona el sistema en el tiempo/fases?
    BENCHMARK_MATRIX = "BENCHMARK_MATRIX"     # Matriz estructurada de capacidades y precios


@dataclass
class NarrativeAnalysis:
    dominant_intent: str
    primary_question: str
    target_archetypes: List[str]
    intent_confidence: int
    intent_signals: Dict[str, float]
    narrative_rationale: str


class NarrativeIntentEngine:
    """Motor de análisis de narrativa e intención comunicativa para Sketion."""

    INTENT_DEFINITIONS = [
        {
            "intent": NarrativeIntentType.TRANSFORMATION,
            "question": "¿Cómo transformar el problema actual en una solución estructurada?",
            "archetypes": ["D", "E", "C"],
            "triggers": ["actual", "problema", "cuello de botella", "queremos implementar", "antes", "solución", "optimizar", "reducir filas", "cola", "fricción", "startup que ayuda"],
            "weight": 1.2
        },
        {
            "intent": NarrativeIntentType.COMPARISON,
            "question": "¿Cuáles son las diferencias críticas entre las opciones y cuál es superior?",
            "archetypes": ["D", "S", "Q"],
            "triggers": [" vs ", "versus", "frente a", "comparar", "diferencias", "monolito vs", "alternativas", "comparativa"],
            "weight": 1.3
        },
        {
            "intent": NarrativeIntentType.CAUSAL_ANALYSIS,
            "question": "¿Cuál es la causa raíz de esta degradación o pérdida?",
            "archetypes": ["M", "C"],
            "triggers": ["por qué", "causa", "pérdida", "perdió clientes", "churn", "bugs", "latencia", "fallo", "incidente", "diagnóstico", "raíz", "crisis"],
            "weight": 1.4
        },
        {
            "intent": NarrativeIntentType.OPERATIONAL_FLOW,
            "question": "¿Cómo se coordinan los diferentes roles y sistemas durante la ejecución?",
            "archetypes": ["E", "C", "T"],
            "triggers": ["cocina", "caja", "mesas", "salón", "cliente", "backend", "transferencia", "sistemas intervienen", "interacción", "roles", "hospital", "urgencias", "triaje", "quirófano"],
            "weight": 1.1
        },
        {
            "intent": NarrativeIntentType.DECISION_TRIAGE,
            "question": "¿Qué protocolo o camino debe ejecutarse según las condiciones de entrada?",
            "archetypes": ["O", "C"],
            "triggers": ["si es", "entonces", "condicional", "triaje", "escalado", "p1", "p2", "p3", "reglas", "despertar", "notificar", "urgencias"],
            "weight": 1.5
        },
        {
            "intent": NarrativeIntentType.ECOSYSTEM_HUB,
            "question": "¿Cómo se integran todos los módulos y servicios en torno a un núcleo unificado?",
            "archetypes": ["A", "N"],
            "triggers": ["ecosistema", "central", "hub", "plataforma", "unificado", "portal central", "todo en uno", "suite", "workspace"],
            "weight": 1.2
        },
        {
            "intent": NarrativeIntentType.VALUE_CHAIN,
            "question": "¿Cómo fluye el producto o valor desde el origen hasta el consumidor final?",
            "archetypes": ["P", "E", "C"],
            "triggers": ["suministro", "cadena de frío", "aduana", "transporte", "almacén", "distribución", "farmacias", "trazabilidad", "logística", "dropshipping"],
            "weight": 1.3
        },
        {
            "intent": NarrativeIntentType.MATURITY_ROADMAP,
            "question": "¿Cómo madura y se despliega la estrategia en fases temporales y gates?",
            "archetypes": ["G", "B", "R"],
            "triggers": ["roadmap", "madurez", "trimestres", "q1", "q2", "q3", "q4", "fases", "lanzamiento", "gate", "inducción", "onboarding"],
            "weight": 1.3
        },
        {
            "intent": NarrativeIntentType.BENCHMARK_MATRIX,
            "question": "¿Cómo se compara cada característica técnica y de precio frente a competidores?",
            "archetypes": ["S", "Q"],
            "triggers": ["tabla", "matriz", "características", "competencia", "planes", "precios", "evaluando", "saas de facturación"],
            "weight": 1.3
        }
    ]

    @classmethod
    def analyze_intent(cls, prompt: str) -> NarrativeAnalysis:
        p_low = prompt.lower()
        scored_intents = []

        for item in cls.INTENT_DEFINITIONS:
            matches = [t for t in item["triggers"] if t in p_low]
            raw_score = len(matches) * item["weight"]
            scored_intents.append((item, raw_score, matches))

        scored_intents.sort(key=lambda x: x[1], reverse=True)
        top_intent_def, top_score, top_matches = scored_intents[0]

        # Normalizar confianza entre 25% y 98%
        confidence = min(98, max(30, int((top_score / 3.5) * 100))) if top_score > 0 else 25

        signals_dict = {
            item["intent"]: round(score, 2)
            for item, score, _ in scored_intents[:4] if score > 0
        }

        rationale = (f"Intención '{top_intent_def['intent']}' detectada por señales: "
                     f"{', '.join(top_matches[:4])}. Responde a la pregunta: '{top_intent_def['question']}'")

        return NarrativeAnalysis(
            dominant_intent=top_intent_def["intent"],
            primary_question=top_intent_def["question"],
            target_archetypes=top_intent_def["archetypes"],
            intent_confidence=confidence,
            intent_signals=signals_dict,
            narrative_rationale=rationale
        )
