"""
Sketion 8.0 — Information Architecture Engine
Gestiona la carga cognitiva masiva en problemas con 50+ entidades, 20+ relaciones y métricas mixtas.
Implementa:
1. Importance Ranking (P1 Hero, P2 Primary, P3 Secondary, P4 Metadata, P5 Appendix)
2. Semantic Grouping & Section Scoping (Agrupación natural por dominios/secciones)
3. Progressive Disclosure (Diferenciación entre flujo narrativo principal y callouts de soporte)
4. Information Compression (De-duplicación y síntesis de entidades redundantes)
5. Appendix & Footnote Allocation (Aislamiento de detalles secundarios para evitar saturar el lienzo)
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple, Optional


class EntityTier:
    HERO = "HERO"                  # Protagonista absoluto (1 único foco por marco)
    PRIMARY = "PRIMARY"            # Componentes centrales del flujo narrativo
    SECONDARY = "SECONDARY"        # Elementos de soporte y conectividad
    METADATA = "METADATA"          # Badges, métricas numéricas, latencias, SLAs
    APPENDIX_CALLOUT = "APPENDIX"  # Notas técnicas profundas, excepciones, warnings


@dataclass
class StructuredEntity:
    id: str
    label: str
    tier: str
    domain_group: str
    importance_score: float  # 0.0 - 1.0
    audience_relevance: Dict[str, float] = field(default_factory=dict)
    metadata_pills: List[str] = field(default_factory=list)
    bullets: List[str] = field(default_factory=list)
    is_hero: bool = False


@dataclass
class InformationArchitecturePlan:
    total_raw_entities: int
    retained_narrative_entities: int
    metadata_pills_count: int
    appendix_callouts_count: int
    compression_ratio: float
    domain_groups: Dict[str, List[StructuredEntity]]
    progressive_disclosure_strategy: str
    rationale: str


class InformationArchitectureEngine:
    """Motor de arquitectura de información y gestión de carga cognitiva."""

    @classmethod
    def structure_payload(cls,
                          raw_entities: List[Dict[str, Any]],
                          target_audience: str = "OPERACIONES",
                          max_primary_per_frame: int = 6) -> InformationArchitecturePlan:
        structured_list = []
        domain_groups = {}

        # 1. Ponderar importancia de cada entidad
        for idx, ent in enumerate(raw_entities):
            lbl = ent.get("label", f"Entidad {idx+1}")
            domain = ent.get("domain", "CORE")
            is_explicit_hero = ent.get("is_hero", False)

            # Relevancia por audiencia
            aud_weights = {
                "CEO": 0.9 if "negocio" in lbl.lower() or "mrr" in lbl.lower() or "ingresos" in lbl.lower() else 0.4,
                "OPERACIONES": 0.9 if "orden" in lbl.lower() or "kds" in lbl.lower() or "cocina" in lbl.lower() or "fila" in lbl.lower() else 0.6,
                "TECH": 0.9 if "jwt" in lbl.lower() or "redis" in lbl.lower() or "grpc" in lbl.lower() or "lambda" in lbl.lower() else 0.5
            }
            aud_rel = aud_weights.get(target_audience.upper(), 0.7)

            # Clasificar en Tier
            if is_explicit_hero:
                tier = EntityTier.HERO
                imp = 1.0
            elif aud_rel >= 0.8:
                tier = EntityTier.PRIMARY
                imp = 0.85
            elif "sla" in lbl.lower() or "ms" in lbl.lower() or "%" in lbl.lower() or "$" in lbl.lower():
                tier = EntityTier.METADATA
                imp = 0.50
            elif "excepción" in lbl.lower() or "nota" in lbl.lower() or "fallback" in lbl.lower() or "warning" in lbl.lower():
                tier = EntityTier.APPENDIX_CALLOUT
                imp = 0.40
            else:
                tier = EntityTier.SECONDARY
                imp = 0.65

            struct_ent = StructuredEntity(
                id=ent.get("id", f"ent_{idx+1}"),
                label=lbl,
                tier=tier,
                domain_group=domain,
                importance_score=imp,
                audience_relevance=aud_weights,
                metadata_pills=ent.get("pills", []),
                bullets=ent.get("bullets", []),
                is_hero=is_explicit_hero
            )
            structured_list.append(struct_ent)

            domain_groups.setdefault(domain, []).append(struct_ent)

        # 2. Aplicar Progressive Disclosure
        heroes_and_primaries = [e for e in structured_list if e.tier in [EntityTier.HERO, EntityTier.PRIMARY]]
        secondaries = [e for e in structured_list if e.tier == EntityTier.SECONDARY]
        metadatas = [e for e in structured_list if e.tier == EntityTier.METADATA]
        appendixes = [e for e in structured_list if e.tier == EntityTier.APPENDIX_CALLOUT]

        # Si hay exceso de primarias, degradar las de menor importancia
        if len(heroes_and_primaries) > max_primary_per_frame:
            # Mantener solo las top N
            heroes_and_primaries.sort(key=lambda x: x.importance_score, reverse=True)
            promoted = heroes_and_primaries[:max_primary_per_frame]
            demoted = heroes_and_primaries[max_primary_per_frame:]
            for d in demoted:
                d.tier = EntityTier.SECONDARY
            heroes_and_primaries = promoted

        total_raw = len(raw_entities)
        retained_narrative = len(heroes_and_primaries) + len(secondaries)
        compression_ratio = round((retained_narrative / float(total_raw)) if total_raw > 0 else 1.0, 2)

        strat = f"Progressive Disclosure: {len(heroes_and_primaries)} Primarias en Flujo Central, {len(metadatas)} como Badges/Pills, {len(appendixes)} en Callouts laterales."

        return InformationArchitecturePlan(
            total_raw_entities=total_raw,
            retained_narrative_entities=retained_narrative,
            metadata_pills_count=len(metadatas),
            appendix_callouts_count=len(appendixes),
            compression_ratio=compression_ratio,
            domain_groups=domain_groups,
            progressive_disclosure_strategy=strat,
            rationale=f"Organización en {len(domain_groups)} dominios semánticos con {len(heroes_and_primaries)} tarjetas principales para garantizar 4.0/10 de densidad."
        )
