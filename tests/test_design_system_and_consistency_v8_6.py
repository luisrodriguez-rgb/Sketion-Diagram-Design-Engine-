"""
Sketion 8.6 — Design System Intelligence & Visual Consistency Test Suite
Evalúa el Design System (v8.5) y el Motor de Consistencia Visual (v8.6)
certificando el Visual Consistency Score (VCS >= 95/100).
"""

import os
import sys
import json

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from design import (
    ComponentRegistry,
    ImportanceLevel,
    AudienceProfile,
    VisualConsistencyEngine
)
import sketion

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V7")
os.makedirs(OUT_DIR, exist_ok=True)


def test_design_system_and_consistency():
    print("=" * 115)
    print("🧪 SKETION 8.6 — DESIGN SYSTEM INTELLIGENCE & VISUAL CONSISTENCY CERTIFICATION")
    print("=" * 115)

    # 1. Probar Selección Contextual Multidimensional
    print(" • [1/3] Probando ComponentRegistry con selección contextual multidimensional...")
    
    spec_hero = ComponentRegistry.resolve(
        label="Payment Saga Orchestrator",
        role="service",
        importance=ImportanceLevel.HERO,
        audience=AudienceProfile.ENGINEER,
        description="Distributed State Machine & Atomicity"
    )
    assert spec_hero.is_hero is True, "Fallo: Hero no marcado correctamente"
    assert spec_hero.badge == "HERO CORE", "Fallo: Badge de hero incorrecto"

    spec_db = ComponentRegistry.resolve(
        label="PostgreSQL Database",
        role="database",
        importance=ImportanceLevel.PRIMARY,
        audience=AudienceProfile.EXECUTIVE,
        description="Primary Relational ACID Store"
    )
    assert spec_db.icon == "database", "Fallo: Ícono de base de datos no resuelto"
    print("   ✅ ComponentRegistry superó todas las pruebas de selección contextual.")

    # 2. Generar Diagrama de Producción con el Design System
    print(" • [2/3] Renderizando diagrama multidominio con Tokens y Design System...")
    payload = {
        "title": "Enterprise Cloud Fintech Ecosystem",
        "layers": [
            {
                "name": "1. Zero-Trust Perimeter",
                "entities": [
                    {"label": "Cloudflare Global WAF", "role": "security", "description": "DDoS Shield & Edge Inspection"},
                    {"label": "React.js Web Portal", "role": "actor", "description": "PCI iFrame Client"}
                ]
            },
            {
                "name": "2. High-Throughput Processing",
                "entities": [
                    {"label": "Payment Saga Orchestrator", "role": "service", "is_hero": True, "description": "Distributed State Machine (Saga Pattern)"},
                    {"label": "PCI Tokenizer Vault", "role": "security", "description": "HSM Irreversible Encryption"}
                ]
            },
            {
                "name": "3. Streaming & Storage",
                "entities": [
                    {"label": "Apache Kafka Event Bus", "role": "stream", "description": "High Throughput Partitioning", "topics": ["tx.init", "tx.done"]},
                    {"label": "Aurora PostgreSQL", "role": "database", "description": "ACID Ledger Persistence"},
                    {"label": "Redis Cache", "role": "cache", "description": "Distributed Locks SETNX"}
                ]
            }
        ]
    }

    out_file = os.path.join(OUT_DIR, "design_system_consistency_v8_6.excalidraw")
    scene = sketion.render(payload=payload, archetype="layered", aspect_ratio="16:9", output=out_file)

    # 3. Evaluar Visual Consistency Score (VCS)
    print(" • [3/3] Evaluando Visual Consistency Score (VCS) en el lienzo generado...")
    with open(out_file, "r", encoding="utf-8") as f:
        scene_dict = json.load(f)

    rep = VisualConsistencyEngine.evaluate_scene(scene_dict)

    print("\n" + "=" * 115)
    print("📊 RESULTADOS DE LA EVALUACIÓN DE CONSISTENCIA VISUAL (VCS)")
    print("=" * 115)
    print(f" • Visual Consistency Score (VCS) : {rep.vcs_score} / 100 [{('✅ CERTIFIED' if rep.passed else '❌ FAIL')}]")
    print(f" • Typography Consistency Scale   : {rep.typography_consistency} / 100")
    print(f" • Spacing & Grid Consistency      : {rep.spacing_consistency} / 100")
    print(f" • Icon Semantic Consistency       : {rep.icon_consistency} / 100")
    print(f" • Brand Treatment Consistency     : {rep.brand_consistency} / 100")
    print(f" • Connector Style Consistency     : {rep.connector_consistency} / 100")
    print(f" • Elementos Totales Evaluados     : {len(scene.elements)}")
    print("=" * 115)

    assert rep.passed, f"VCS falló con puntuación {rep.vcs_score}"


if __name__ == "__main__":
    test_design_system_and_consistency()
