"""
Sketion 5.5 — Narrative Model Engine
Representación rica de la historia visual que debe contar el diagrama:
- Intención Narrativa (Intent)
- Pregunta Implícita Primaria (Primary Question)
- Arco Narrativo (Story Arc: [estado_inicial, mecanismo, estado_futuro, valor])
- Relación Semántica Dominante (Dominant Relationship: contrast, cause_effect, flow, hub, hierarchy)
- Prioridad de Disposición Visual (Visual Priority: side_by_side, layered_stack, fishbone, radial, swimlane)
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple


@dataclass
class NarrativeModel:
    intent: str
    primary_question: str
    story_arc: List[str]
    dominant_relationship: str
    visual_priority: str
    target_archetypes: List[str]
    confidence: int
    rationale: str


class NarrativeModelEngine:
    """Extrae el modelo narrativo completo para guiar la búsqueda compositiva."""

    NARRATIVE_SCHEMAS = [
        {
            "intent": "CAUSAL_ANALYSIS",
            "question": "¿Cuál es la causa raíz de este problema o degradación?",
            "story_arc": ["síntoma_observable", "categorías_causales", "factores_raíz", "mitigación"],
            "relationship": "cause_effect",
            "visual_priority": "fishbone_causal",
            "archetypes": ["M", "C"],
            "triggers": ["por qué", "causa", "pérdida", "perdió clientes", "churn", "bugs", "latencia", "fallo", "incidente", "diagnóstico", "raíz", "crisis", "post-mortem"],
            "weight": 1.6
        },
        {
            "intent": "COMPARISON",
            "question": "¿Cuáles son las diferencias críticas entre las opciones y cuál es superior?",
            "story_arc": ["opción_a", "opción_b", "criterios_evaluación", "veredicto"],
            "relationship": "contrast",
            "visual_priority": "side_by_side",
            "archetypes": ["D", "S", "Q"],
            "triggers": [" vs ", "versus", "frente a", "comparar", "diferencias", "monolito vs", "alternativas", "comparativa", "monolito modular vs microservicios", "crm vs erp"],
            "weight": 1.5
        },
        {
            "intent": "TRANSFORMATION",
            "question": "¿Cómo transformar el dolor actual en una solución estructurada que genera valor?",
            "story_arc": ["estado_as_is", "fricciones", "mecanismo_tecnológico", "estado_to_be_valor"],
            "relationship": "transformation",
            "visual_priority": "side_by_side",
            "archetypes": ["D", "E", "C", "A"],
            "triggers": ["actual", "problema", "cuello de botella", "queremos implementar", "antes", "solución", "optimizar", "reducir filas", "cola", "fricción", "startup que ayuda", "pitch", "inversores", "convencer a inversores"],
            "weight": 1.4
        },
        {
            "intent": "OPERATIONAL_FLOW",
            "question": "¿Cómo se coordinan los diferentes roles, sistemas y actores durante la operación?",
            "story_arc": ["disparador_inicial", "coordinación_actores", "pasos_sincronizados", "resultado_operativo"],
            "relationship": "temporal_sequence",
            "visual_priority": "swimlane_actors",
            "archetypes": ["E", "C", "T"],
            "triggers": ["cocina", "caja", "mesas", "salón", "cliente", "backend", "transferencia", "transacciones", "flujo de transacciones", "procesamiento de pagos", "sistemas intervienen", "interacción", "roles", "hospital", "urgencias", "triaje", "quirófano", "auditoría soc2", "oficinas físicas"],
            "weight": 1.4
        },
        {
            "intent": "DECISION_TRIAGE",
            "question": "¿Qué protocolo condicional debe ejecutarse según las reglas de entrada?",
            "story_arc": ["evento_alerta", "evaluación_condición", "enrutamiento_responsable", "resolución"],
            "relationship": "conditional_branching",
            "visual_priority": "decision_tree",
            "archetypes": ["O", "C"],
            "triggers": ["si es", "entonces", "condicional", "triaje", "escalado", "p1", "p2", "p3", "reglas", "despertar", "notificar"],
            "weight": 1.7
        },
        {
            "intent": "ECOSYSTEM_HUB",
            "question": "¿Cómo se integran todos los módulos y servicios en torno a un núcleo unificado?",
            "story_arc": ["núcleo_central", "servicios_satélite", "flujos_bidireccionales", "ecosistema_integrado"],
            "relationship": "hub_spoke",
            "visual_priority": "radial_orbit",
            "archetypes": ["A", "N"],
            "triggers": ["ecosistema", "central", "hub", "plataforma", "unificado", "portal central", "todo en uno", "suite", "workspace", "fusión de dos empresas"],
            "weight": 1.3
        },
        {
            "intent": "VALUE_CHAIN",
            "question": "¿Cómo fluye el producto o valor a través de la cadena física y logística?",
            "story_arc": ["origen_proveedor", "transporte_aduanas", "almacenamiento", "distribución_consumidor"],
            "relationship": "supply_flow",
            "visual_priority": "linear_chain",
            "archetypes": ["P", "E", "C"],
            "triggers": ["suministro", "cadena de frío", "aduana", "transporte", "almacén", "distribución", "farmacias", "trazabilidad", "logística", "dropshipping"],
            "weight": 1.4
        },
        {
            "intent": "MATURITY_ROADMAP",
            "question": "¿Cómo evoluciona y madura el sistema a lo largo de fases y gates de aprobación?",
            "story_arc": ["fase_inicial", "hitos_progresivos", "gates_calidad", "madurez_completa"],
            "relationship": "temporal_maturity",
            "visual_priority": "stepped_ladder",
            "archetypes": ["G", "B", "R"],
            "triggers": ["roadmap", "madurez", "trimestres", "q1", "q2", "q3", "q4", "fases", "lanzamiento", "gate", "inducción", "onboarding"],
            "weight": 1.4
        },
        {
            "intent": "BENCHMARK_MATRIX",
            "question": "¿Cómo se compara cada característica técnica y de precio frente al mercado?",
            "story_arc": ["entidades_competidoras", "dimensiones_comparación", "evaluación_celda", "conclusión_liderazgo"],
            "relationship": "matrix_grid",
            "visual_priority": "tabular_grid",
            "archetypes": ["S", "Q"],
            "triggers": ["tabla", "matriz", "características", "competencia", "planes", "precios", "evaluando", "saas de facturación"],
            "weight": 1.4
        }
    ]

    @classmethod
    def infer_narrative_model(cls, prompt: str) -> NarrativeModel:
        p_low = prompt.lower()
        scored = []

        # Caso especial: Si hay 'pitch' o 'convencer a inversores' o 'modelo de negocio' -> TRANSFORMATION
        is_pitch_value = any(k in p_low for k in ["pitch", "inversores", "convencer a inversores", "modelo de negocio"])
        # Caso especial: Causal solo si es un incidente/diagnóstico de latencia explícito
        is_explicit_causal = any(k in p_low for k in ["crisis de latencia", "15 posibles causas", "perdió clientes", "por qué", "causa raíz", "post-mortem"]) and not is_pitch_value

        for schema in cls.NARRATIVE_SCHEMAS:
            matches = [t for t in schema["triggers"] if t in p_low]
            raw_score = len(matches) * schema["weight"]

            if is_pitch_value and schema["intent"] == "TRANSFORMATION":
                raw_score += 25.0
            elif is_explicit_causal and schema["intent"] == "CAUSAL_ANALYSIS":
                raw_score += 20.0
            elif " vs " in p_low and schema["intent"] == "COMPARISON":
                raw_score += 15.0

            scored.append((schema, raw_score, matches))

        scored.sort(key=lambda x: x[1], reverse=True)
        top_schema, top_score, top_matches = scored[0]

        confidence = min(98, max(35, int((top_score / 4.0) * 100)))

        rationale = (f"Intención '{top_schema['intent']}' ({confidence}%) con arco: "
                     f"{' -> '.join(top_schema['story_arc'][:3])}. Responde a: '{top_schema['question']}'")

        return NarrativeModel(
            intent=top_schema["intent"],
            primary_question=top_schema["question"],
            story_arc=top_schema["story_arc"],
            dominant_relationship=top_schema["relationship"],
            visual_priority=top_schema["visual_priority"],
            target_archetypes=top_schema["archetypes"],
            confidence=confidence,
            rationale=rationale
        )
