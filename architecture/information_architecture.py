"""
Sketion 8.0 — Information Architecture Engine (Auditable, Dynamic & Audience-Aware)
Gestiona la carga cognitiva masiva en problemas con 50+ entidades, 20+ relaciones y métricas mixtas.

Capacidades Centrales:
1. 6 Tiers Formales: HERO, PRIMARY, SECONDARY, METADATA, APPENDIX, SUPPRESSED.
2. 4 Estados de Visibilidad: VISIBLE, COLLAPSED, APPENDIX, SUPPRESSED.
3. Hero Mutation Dinámico: El protagonista muta según la conjunción (Audiencia x Objetivo).
4. InformationRole Auditado:
   - semantic_importance, audience_relevance, narrative_relevance
   - priority_score, detail_cost, visibility, reason: List[str]
5. Métricas Matemáticas:
   - Semantic Retention Rate (100.0%)
   - Primary Flow Reduction (PFR) = 1.0 - (Main Flow Cards / Total Entities)
   - Cognitive Load Index (CLI)
   - Audience Transformation Score (ATS)
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple, Optional


class EntityTier:
    HERO = "HERO"                  # Protagonista de la historia (Acento coral exclusivo)
    PRIMARY = "PRIMARY"            # Componentes centrales del flujo narrativo (3-6 tarjetas)
    SECONDARY = "SECONDARY"        # Elementos de soporte y conectividad
    METADATA = "METADATA"          # Badges y métricas numéricas convertidas en pills superiores
    APPENDIX_CALLOUT = "APPENDIX"  # Circuit breakers, fallbacks, warnings en notas laterales
    SUPPRESSED = "SUPPRESSED"      # Ocultado en la vista actual para evitar sobrecarga


class VisibilityState:
    VISIBLE = "VISIBLE"            # Presente físicamente en el flujo central
    COLLAPSED = "COLLAPSED"        # Agrupado indirectamente en pastillas de soporte
    APPENDIX = "APPENDIX"          # Visible en notas y callouts laterales
    SUPPRESSED = "SUPPRESSED"      # Conservado en el modelo semántico pero oculto en esta vista


@dataclass
class InformationRole:
    tier: str
    semantic_importance: float   # 0.0 - 1.0
    audience_relevance: float    # 0.0 - 1.0
    narrative_relevance: float   # 0.0 - 1.0
    priority_score: float        # Ponderación compuesta
    detail_cost: float           # Carga de ruido visual (0.0 - 1.0)
    visibility: str              # VISIBLE, COLLAPSED, APPENDIX, SUPPRESSED
    target_frame: int = 1
    visual_representation: str = "card"
    reasons: List[str] = field(default_factory=list)


@dataclass
class StructuredEntity:
    id: str
    label: str
    domain_group: str
    role: InformationRole
    is_hero: bool = False


@dataclass
class InformationArchitecturePlan:
    total_raw_entities: int
    visible_count: int
    collapsed_count: int
    appendix_count: int
    suppressed_count: int
    semantic_retention_rate: float        # 100.0%
    primary_flow_reduction: float         # e.g., 0.89 (89% de reducción de tarjetas)
    cognitive_load_index: float           # Índice de carga cognitiva
    hero_entity_label: str
    selected_archetype: str
    domain_groups: Dict[str, List[StructuredEntity]]
    entity_traceability: List[Dict[str, Any]]
    target_audience: str
    target_objective: str
    progressive_disclosure_strategy: str
    rationale: str


class InformationArchitectureEngine:
    """Motor de arquitectura de información y gestión de carga cognitiva."""

    @classmethod
    def structure_payload(cls,
                          raw_entities: List[Dict[str, Any]],
                          target_audience: str = "OPERACIONES",
                          target_objective: str = "Flujo Operacional General",
                          max_primary_per_frame: int = 6) -> InformationArchitecturePlan:
        structured_list = []
        domain_groups = {}
        traceability = []

        aud_up = target_audience.upper()
        obj_low = target_objective.lower()

        # 1. Determinar el arquetipo óptimo y los sesgos del Hero según (Audiencia x Objetivo)
        if "CEO" in aud_up or "FINANCIERO" in obj_low:
            hero_keywords = ["volumen", "plataforma", "checkout", "revenue", "mrr", "settlement"]
            selected_archetype = "P (Cadena de Valor & Retorno)"
        elif "AUDITOR" in aud_up or "SOC2" in aud_up or "COMPLIANCE" in aud_up or "CONTROL" in obj_low:
            hero_keywords = ["tokenizer", "vault", "pci", "soc2", "audit", "aml"]
            selected_archetype = "J (Cebolla de Seguridad & Gobernanza)"
        elif "OPERACIONES" in aud_up or "DISPUTE" in obj_low or "CUELLO" in obj_low:
            hero_keywords = ["reconciliation", "support", "pos", "dispute", "kds"]
            selected_archetype = "E (Swimlanes de Coordinación Operativa)"
        else:  # TECH / ENGINEER / RESILIENCIA
            hero_keywords = ["orchestrator", "kafka", "idempotency", "jwt", "flink"]
            selected_archetype = "C (Flow Pipeline con Bucle de Feedback)"

        # 2. Ponderar importancia entidad por entidad
        candidate_heroes = []

        for idx, ent in enumerate(raw_entities):
            lbl = ent.get("label", f"Entidad {idx+1}")
            domain = ent.get("domain", "CORE")
            lbl_low = lbl.lower()
            reasons = []

            # Relevancia por Audiencia
            if "CEO" in aud_up:
                aud_rel = 0.95 if any(k in lbl_low for k in ["volumen", "mrr", "sla", "negocio", "checkout", "pago", "risk", "settlement"]) else 0.15
            elif "AUDITOR" in aud_up or "SOC2" in aud_up or "COMPLIANCE" in aud_up:
                aud_rel = 0.95 if any(k in lbl_low for k in ["soc2", "pci", "aml", "tax", "dian", "audit", "vault", "tokenizer", "mtls"]) else 0.20
            elif "OPERACIONES" in aud_up:
                aud_rel = 0.95 if any(k in lbl_low for k in ["pos", "whatsapp", "kds", "orden", "support", "dispute", "reconciliation", "worker"]) else 0.35
            else:  # TECH / ENGINEER
                aud_rel = 0.95 if any(k in lbl_low for k in ["jwt", "orchestrator", "kafka", "redis", "flink", "grpc", "s3", "circuit", "idempotency", "aurora"]) else 0.40

            # Relevancia Narrativa por Objetivo
            if any(k in obj_low for k in ["riesgo", "falla", "dispute"]):
                narr_rel = 0.95 if any(k in lbl_low for k in ["warning", "fallback", "circuit", "fraud", "dispute", "chargeback", "timeout"]) else 0.35
            elif any(k in obj_low for k in ["control", "evidencia", "compliance"]):
                narr_rel = 0.95 if any(k in lbl_low for k in ["soc2", "pci", "audit", "immutable", "aml", "dian", "mtls"]) else 0.35
            elif any(k in obj_low for k in ["resiliencia", "sla", "idempotencia"]):
                narr_rel = 0.95 if any(k in lbl_low for k in ["sla", "latency", "aurora", "replica", "idempotency", "redlock", "dr"]) else 0.40
            else:  # Flujo general
                narr_rel = 0.90 if any(k in lbl_low for k in ["checkout", "gateway", "orchestrator", "switch", "worker", "auth"]) else 0.50

            # Semantic Importance Base
            sem_imp = (aud_rel * 0.5 + narr_rel * 0.5)

            # Check if this matches Hero profile
            is_hero_match = any(k in lbl_low for k in hero_keywords)
            if is_hero_match:
                candidate_heroes.append((idx, lbl, sem_imp + 0.3))

        # Seleccionar el Hero con mayor afinidad para esta conjunción
        candidate_heroes.sort(key=lambda x: x[2], reverse=True)
        chosen_hero_idx = candidate_heroes[0][0] if candidate_heroes else 0
        chosen_hero_lbl = raw_entities[chosen_hero_idx].get("label", "")

        # 3. Clasificación definitiva en Tiers y Visibilidad
        for idx, ent in enumerate(raw_entities):
            lbl = ent.get("label", f"Entidad {idx+1}")
            domain = ent.get("domain", "CORE")
            lbl_low = lbl.lower()
            reasons = []

            # Recalcular score
            if "CEO" in aud_up:
                aud_rel = 0.95 if any(k in lbl_low for k in ["volumen", "mrr", "sla", "negocio", "checkout", "pago", "risk", "settlement"]) else 0.15
            elif "AUDITOR" in aud_up or "SOC2" in aud_up or "COMPLIANCE" in aud_up:
                aud_rel = 0.95 if any(k in lbl_low for k in ["soc2", "pci", "aml", "tax", "dian", "audit", "vault", "tokenizer", "mtls"]) else 0.20
            elif "OPERACIONES" in aud_up:
                aud_rel = 0.95 if any(k in lbl_low for k in ["pos", "whatsapp", "kds", "orden", "support", "dispute", "reconciliation", "worker"]) else 0.35
            else:
                aud_rel = 0.95 if any(k in lbl_low for k in ["jwt", "orchestrator", "kafka", "redis", "flink", "grpc", "s3", "circuit", "idempotency", "aurora"]) else 0.40

            if any(k in obj_low for k in ["riesgo", "falla", "dispute"]):
                narr_rel = 0.95 if any(k in lbl_low for k in ["warning", "fallback", "circuit", "fraud", "dispute", "chargeback", "timeout"]) else 0.35
            elif any(k in obj_low for k in ["control", "evidencia", "compliance"]):
                narr_rel = 0.95 if any(k in lbl_low for k in ["soc2", "pci", "audit", "immutable", "aml", "dian", "mtls"]) else 0.35
            elif any(k in obj_low for k in ["resiliencia", "sla", "idempotencia"]):
                narr_rel = 0.95 if any(k in lbl_low for k in ["sla", "latency", "aurora", "replica", "idempotency", "redlock", "dr"]) else 0.40
            else:
                narr_rel = 0.90 if any(k in lbl_low for k in ["checkout", "gateway", "orchestrator", "switch", "worker", "auth"]) else 0.50

            priority_score = round(aud_rel * 0.55 + narr_rel * 0.45, 2)

            # Clasificación de Tiers
            if idx == chosen_hero_idx:
                tier = EntityTier.HERO
                vis = VisibilityState.VISIBLE
                rep = "hero_card_accent"
                frame = 1
                reasons.append("Protagonista focal por afinidad máxima de audiencia y objetivo.")
            elif any(k in lbl_low for k in ["sla", "ms", "%", "$", "tps", "uptime"]):
                tier = EntityTier.METADATA
                vis = VisibilityState.COLLAPSED
                rep = "top_metadata_pill"
                frame = 1
                reasons.append("Métrica cuantitativa convertida en badge superior sin ocupar tarjeta completa.")
            elif any(k in lbl_low for k in ["warning", "fallback", "circuit", "dr", "timeout", "retry"]):
                tier = EntityTier.APPENDIX_CALLOUT
                vis = VisibilityState.APPENDIX
                rep = "side_callout_box"
                frame = 3
                reasons.append("Política de excepción / fallo aislada en callout lateral.")
            elif aud_rel < 0.25 and narr_rel < 0.40:
                tier = EntityTier.SUPPRESSED
                vis = VisibilityState.SUPPRESSED
                rep = "suppressed_view"
                frame = 0
                reasons.append("Detalle técnico secundario ocultado en esta vista para proteger el foco visual.")
            elif priority_score >= 0.65:
                tier = EntityTier.PRIMARY
                vis = VisibilityState.VISIBLE
                rep = "quad_corner_card"
                frame = 1
                reasons.append("Componente primario del flujo central por alta relevancia.")
            else:
                tier = EntityTier.SECONDARY
                vis = VisibilityState.VISIBLE
                rep = "support_node"
                frame = 2
                reasons.append("Componente de soporte interconectado.")

            role = InformationRole(
                tier=tier,
                semantic_importance=round(aud_rel * 0.5 + narr_rel * 0.5, 2),
                audience_relevance=round(aud_rel, 2),
                narrative_relevance=round(narr_rel, 2),
                priority_score=priority_score,
                detail_cost=0.2 if tier in [EntityTier.METADATA, EntityTier.APPENDIX_CALLOUT] else 0.8,
                visibility=vis,
                target_frame=frame,
                visual_representation=rep,
                reasons=reasons
            )

            struct_ent = StructuredEntity(
                id=ent.get("id", f"ent_{idx+1}"),
                label=lbl,
                domain_group=domain,
                role=role,
                is_hero=(tier == EntityTier.HERO)
            )
            structured_list.append(struct_ent)

            if tier != EntityTier.SUPPRESSED:
                domain_groups.setdefault(domain, []).append(struct_ent)

            traceability.append({
                "id": struct_ent.id,
                "label": struct_ent.label,
                "domain": domain,
                "tier": tier,
                "visibility": vis,
                "frame": frame,
                "representation": rep,
                "priority_score": priority_score,
                "reason": reasons[0] if reasons else ""
            })

        # Conteos de visibilidad
        visible_cnt = sum(1 for e in structured_list if e.role.visibility == VisibilityState.VISIBLE)
        collapsed_cnt = sum(1 for e in structured_list if e.role.visibility == VisibilityState.COLLAPSED)
        appendix_cnt = sum(1 for e in structured_list if e.role.visibility == VisibilityState.APPENDIX)
        suppressed_cnt = sum(1 for e in structured_list if e.role.visibility == VisibilityState.SUPPRESSED)

        total_raw = len(raw_entities)
        heroes = [e for e in structured_list if e.role.tier == EntityTier.HERO]
        primaries = [e for e in structured_list if e.role.tier == EntityTier.PRIMARY]

        # Semantic Retention Rate = 100.0% (El 100% de la semántica está modelada y clasificada)
        sem_retention = 100.0

        # Primary Flow Reduction (PFR) = 1.0 - (Tarjetas Principales / Entidades Totales)
        main_flow_cards = len(heroes) + min(max_primary_per_frame, len(primaries))
        pfr = round(1.0 - (float(main_flow_cards) / float(total_raw)), 2)

        # Cognitive Load Index = (Tarjetas Visibles * 1.0 + Pills * 0.2 + Callouts * 0.3)
        cli = round(visible_cnt * 1.0 + collapsed_cnt * 0.2 + appendix_cnt * 0.3, 1)

        strat = f"Progressive Disclosure ({aud_up}): Hero '{chosen_hero_lbl}', {len(primaries)} Primarias, {collapsed_cnt} Pills, {appendix_cnt} Callouts, {suppressed_cnt} Suprimidas (PFR: {int(pfr*100)}%, CLI: {cli})."

        return InformationArchitecturePlan(
            total_raw_entities=total_raw,
            visible_count=visible_cnt,
            collapsed_count=collapsed_cnt,
            appendix_count=appendix_cnt,
            suppressed_count=suppressed_cnt,
            semantic_retention_rate=sem_retention,
            primary_flow_reduction=pfr,
            cognitive_load_index=cli,
            hero_entity_label=chosen_hero_lbl,
            selected_archetype=selected_archetype,
            domain_groups=domain_groups,
            entity_traceability=traceability,
            target_audience=target_audience,
            target_objective=target_objective,
            progressive_disclosure_strategy=strat,
            rationale=f"Adaptación a '{target_audience}' con foco en '{target_objective}' -> Arquetipo '{selected_archetype}', Retención 100% y Alivio de Flujo Principal del {int(pfr*100)}%."
        )
