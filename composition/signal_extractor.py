"""
Sketion 5.0 — Semantic Signal Extractor & Interpretable Scoring
Extrae señales semánticas multidimensionales de un prompt no estructurado
y calcula la afinidad de cada arquetipo con un desglose aditivo 100% explicable.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Tuple


@dataclass
class SemanticSignals:
    contrast_level: float = 0.0          # Presencia de dolor vs solución, antes vs después
    actor_count: float = 0.0             # Múltiples actores, roles o swimlanes
    sequential_flow: float = 0.0         # Procesos lineales paso a paso
    capacity_feedback_loop: float = 0.0  # Cuellos de botella, saturación, bucles de control
    hub_centrality: float = 0.0          # Ecosistema unificado, núcleo central + satélites
    hierarchical_maturity: float = 0.0   # Niveles de madurez, capas, pirámides, roadmaps
    tabular_comparison: float = 0.0      # Comparativa celda por celda, matriz de funciones
    cause_effect_analysis: float = 0.0   # Análisis de causa raíz, bugs, churn, diagnóstico
    decision_triage: float = 0.0         # Reglas condicionales if/else, triaje, escalado
    supply_chain_logistics: float = 0.0  # Cadena física, aduanas, frío, distribución
    raw_detected_signals: Dict[str, List[str]] = field(default_factory=dict)


@dataclass
class InterpretableArchetypeScore:
    code: str
    name: str
    confidence: int
    signal_contributions: Dict[str, float]
    rationale: str
    is_primary: bool = False


class SemanticSignalExtractor:
    """Extrae señales objetivas e interpretables de cualquier prompt de negocio o ingeniería."""

    SIGNAL_KEYWORDS = {
        "contrast": ["frente a", "vs", "antes", "después", "abandono", "fricción", "legacy", "caos", "tradicional", "servidor php"],
        "actors": ["cliente", "cocina", "caja", "mesas", "salón", "roles", "operación", "actores", "personal", "kds", "usuarios", "banco", "servidor", "admin", "hospital", "urgencias", "quirófano", "uci"],
        "sequential": ["flujo", "paso", "proceso", "etapas", "después", "luego", "pipeline", "cadena", "orden", "secuencia", "ingesta", "transformados", "kafka", "flink", "clickhouse", "data lake", "nifi", "airflow", "trino"],
        "capacity_loop": ["capacidad", "saturación", "espera", "filas", "retraso", "demora", "tiempo", "bucle", "reintento", "feedback", "throttle", "cuello de botella"],
        "hub": ["ecosistema", "central", "hub", "plataforma", "unificado", "satélites", "núcleo", "workspace", "todo en uno", "portal central"],
        "maturity": ["madurez", "roadmap", "niveles", "fases", "evolución", "crecimiento", "trimestre", "largo plazo", "pirámide", "capas", "q1", "q2", "q3", "q4"],
        "tabular": ["tabla", "comparativa", "características", "competencia", "planes", "precios", "matriz", "evaluando", "comparar nuestro saas"],
        "cause_effect": ["causa", "por qué", "pérdida", "perdió clientes", "churn", "bugs", "diagnóstico", "raíz", "defectos", "latencia", "post-mortem"],
        "decision": ["si es", "entonces", "condicional", "triaje", "escalado", "p1", "p2", "p3", "reglas", "despertar", "notificar"],
        "supply_chain": ["suministro", "aduana", "transporte", "cadena de frío", "frío", "iot", "almacén", "distribución", "farmacias", "trazabilidad", "logística", "dropshipping"]
    }

    @classmethod
    def extract_signals(cls, prompt: str) -> SemanticSignals:
        p_low = prompt.lower()
        detected = {}
        scores = {}

        for sig_name, kws in cls.SIGNAL_KEYWORDS.items():
            matched = [k for k in kws if k in p_low]
            detected[sig_name] = matched
            # Intensidad normalizada (hasta 1.0)
            scores[sig_name] = min(1.0, len(matched) * 0.35)

        return SemanticSignals(
            contrast_level=scores["contrast"],
            actor_count=scores["actors"],
            sequential_flow=scores["sequential"],
            capacity_feedback_loop=scores["capacity_loop"],
            hub_centrality=scores["hub"],
            hierarchical_maturity=scores["maturity"],
            tabular_comparison=scores["tabular"],
            cause_effect_analysis=scores["cause_effect"],
            decision_triage=scores["decision"],
            supply_chain_logistics=scores["supply_chain"],
            raw_detected_signals=detected
        )

    @classmethod
    def evaluate_archetypes_with_signals(cls, prompt: str) -> List[InterpretableArchetypeScore]:
        signals = cls.extract_signals(prompt)
        archetypes_config = [
            {
                "code": "D",
                "name": "El Duelo (VS)",
                "weights": {"contrast": 0.65, "capacity_loop": 0.20, "sequential": 0.15},
                "base": 0.05
            },
            {
                "code": "E",
                "name": "Swimlanes Operativos",
                "weights": {"actors": 0.60, "sequential": 0.25, "supply_chain": 0.15},
                "base": 0.05
            },
            {
                "code": "C",
                "name": "Flow Pipeline con Bucle",
                "weights": {"sequential": 0.60, "capacity_loop": 0.30, "contrast": 0.10},
                "base": 0.05
            },
            {
                "code": "A",
                "name": "El Cerebro (Hub Radial)",
                "weights": {"hub": 0.70, "actors": 0.15, "sequential": 0.15},
                "base": 0.05
            },
            {
                "code": "G",
                "name": "La Pirámide / Escalera",
                "weights": {"maturity": 0.70, "sequential": 0.20, "contrast": 0.10},
                "base": 0.05
            },
            {
                "code": "S",
                "name": "Matriz Forense Tabular",
                "weights": {"tabular": 0.75, "contrast": 0.15, "actors": 0.10},
                "base": 0.05
            },
            {
                "code": "M",
                "name": "La Espina (Ishikawa Causa-Raíz)",
                "weights": {"cause_effect": 0.75, "contrast": 0.15, "sequential": 0.10},
                "base": 0.05
            },
            {
                "code": "O",
                "name": "Árbol de Decisión / Triaje",
                "weights": {"decision": 0.80, "sequential": 0.10, "actors": 0.10},
                "base": 0.05
            },
            {
                "code": "P",
                "name": "Cadena de Valor & Supply Chain",
                "weights": {"supply_chain": 0.70, "sequential": 0.20, "actors": 0.10},
                "base": 0.05
            }
        ]

        scored_archetypes = []
        for arch in archetypes_config:
            total_score = arch["base"]
            contribs = {}
            for sig, weight in arch["weights"].items():
                sig_val = getattr(signals, f"{sig}_level" if hasattr(signals, f"{sig}_level") else ("actor_count" if sig == "actors" else "sequential_flow" if sig == "sequential" else "capacity_feedback_loop" if sig == "capacity_loop" else "hub_centrality" if sig == "hub" else "hierarchical_maturity" if sig == "maturity" else "tabular_comparison" if sig == "tabular" else "cause_effect_analysis" if sig == "cause_effect" else "decision_triage" if sig == "decision" else "supply_chain_logistics" if sig == "supply_chain" else 0.0), 0.0)
                contribution = sig_val * weight
                contribs[sig] = round(contribution, 3)
                total_score += contribution

            confidence = min(98, max(5, int(total_score * 100)))
            rationale_items = [f"{sig}: +{contrib:.2f}" for sig, contrib in contribs.items() if contrib > 0.02]
            rationale = " | ".join(rationale_items) if rationale_items else "Score base"

            scored_archetypes.append(InterpretableArchetypeScore(
                code=arch["code"],
                name=arch["name"],
                confidence=confidence,
                signal_contributions=contribs,
                rationale=rationale
            ))

        scored_archetypes.sort(key=lambda a: a.confidence, reverse=True)
        if scored_archetypes:
            scored_archetypes[0].is_primary = True

        return scored_archetypes
