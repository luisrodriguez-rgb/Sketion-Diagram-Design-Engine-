"""
Sketion 10.0 — Unified Python SDK Test Suite
Verifica la API unificada de alto nivel `import sketion; sketion.render(...)`.
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

import sketion

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V7")
os.makedirs(OUT_DIR, exist_ok=True)


def test_sdk():
    print("=" * 115)
    print(f"🧪 SKETION {sketion.__version__} — UNIFIED PRODUCTION SDK TEST")
    print("=" * 115)

    test_payload = {
        "title": "Global Fintech Core Settlement",
        "layers": [
            {
                "name": "1. Perímetro Zero-Trust",
                "entities": [
                    {"label": "Cloudflare Global WAF", "role": "security", "description": "DDoS Shield"},
                    {"label": "Web Checkout SPA", "role": "actor", "description": "React.js Client"}
                ]
            },
            {
                "name": "2. Orquestación Transaccional Hero",
                "entities": [
                    {"label": "Payment Saga Orchestrator", "role": "service", "is_hero": True, "description": "Distributed State Machine & Atomicity"},
                    {"label": "PCI Tokenizer Vault", "role": "security", "description": "HSM Token Vault"}
                ]
            },
            {
                "name": "3. Persistencia & Event Stream",
                "entities": [
                    {"label": "Apache Kafka Cluster", "role": "stream", "description": "Payment Events"},
                    {"label": "Aurora PostgreSQL", "role": "database", "description": "Primary ACID DB"}
                ]
            }
        ]
    }

    out_file = os.path.join(OUT_DIR, "sketion_sdk_v10_verification.excalidraw")

    print(" • Ejecutando sketion.render(..., archetype='layered', aspect_ratio='16:9')...")
    scene = sketion.render(
        payload=test_payload,
        archetype="layered",
        aspect_ratio="16:9",
        output=out_file
    )

    print(f" • Diagrama generado exitosamente con el SDK: {out_file}")
    val_scene, val_rep = sketion.validate(out_file)

    print("\n" + "=" * 115)
    print("📊 RESULTADOS DE LA CERTIFICACIÓN DEL SDK SKETION 10.0")
    print("=" * 115)
    print(f" • Global Quality Score : {val_rep.sketion_overall_score} / 100 [{('✅ PASS' if val_rep.is_valid else '❌ FAIL')}]")
    print(f" • Repair Dependency (RDS): {val_rep.repair_dependency_score} [{val_rep.repair_dependency_status}]")
    print(f" • Total de Elementos  : {len(scene.elements)}")
    print("=" * 115)


if __name__ == "__main__":
    test_sdk()
