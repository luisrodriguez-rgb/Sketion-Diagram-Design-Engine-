"""
Sketion 8.4 — Visual Matrix Benchmark (4x4x4 Multi-Archetype / Multi-Domain / Multi-Audience)
Ejecuta la evaluación masiva del motor matricial en los 4 Arquetipos Espaciales:
1. LAYERED: Arquitectura Estratificada por Capas
2. PIPELINE: Flujo Lineal Continuo con Chevrons y Fallback Loops
3. RADIAL_HUB: Topología en Estrella / El Cerebro Transaccional 360°
4. SPLIT_DUEL: Duelo Comparativo de Migración (Legacy vs Target Hero)
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from visual_intelligence.visual_matrix import VisualMatrixEngine, SpatialArchetype
from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from validation.validator import validate_scene

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V7")
os.makedirs(OUT_DIR, exist_ok=True)


# 1. PAYLOAD ARQUETIPO 1: LAYERED (Global E-Commerce Logistics)
PAYLOAD_LAYERED = {
    "layers": [
        {
            "name": "1. Canales de Venta & Clientes",
            "entities": [
                {"id": "e1", "label": "Shopify Storefront", "role": "actor", "tier": "client", "description": "Web SPA & Mobile Checkout"},
                {"id": "e2", "label": "Fleet Driver Mobile App", "role": "actor", "tier": "client", "description": "GPS Tracking & Proof of Delivery"},
                {"id": "e3", "label": "Warehouse POS Scanner", "role": "actor", "tier": "iot", "description": "RFID & Barcode Ingest"}
            ]
        },
        {
            "name": "2. Ruteo & Orquestación de Envíos",
            "entities": [
                {"id": "e4", "label": "Kong API Gateway", "role": "gateway", "tier": "core", "description": "JWT Auth & Rate Limiting"},
                {"id": "e5", "label": "Dispatch Optimizer Core", "role": "service", "tier": "hero", "description": "Heuristic Vehicle Routing & SLA Engine", "is_hero": True},
                {"id": "e6", "label": "Notification Hub", "role": "service", "tier": "core", "description": "WhatsApp & SMS Real-time Alerts"}
            ]
        },
        {
            "name": "3. Streaming & Bases de Datos",
            "entities": [
                {"id": "e7", "label": "Apache Kafka Fleet Stream", "role": "stream", "tier": "core", "description": "Topics: gps.ping · package.scanned · delivered", "topics": ["gps.ping", "pkg.scan", "pkg.deliver"]},
                {"id": "e8", "label": "PostgreSQL Order Ledger", "role": "database", "tier": "storage", "description": "Primary Orders DB SERIALIZABLE"},
                {"id": "e9", "label": "Redis Geo-Cache", "role": "cache", "tier": "storage", "description": "Driver Coordinates TTL 30s"}
            ]
        }
    ]
}


# 2. PAYLOAD ARQUETIPO 2: PIPELINE (Fintech Payment Processing)
PAYLOAD_PIPELINE = {
    "stages": ["1. CHECKOUT AUTH", "2. TOKENIZATION", "3. SAGA ENGINE", "4. SETTLEMENT", "5. AUDIT WORM"],
    "has_return_loop": True,
    "steps": [
        {"id": "p1", "label": "Card Checkout Gateway", "role": "gateway", "tier": "edge", "description": "mTLS & Risk Scoring", "edge_label": "Encrypted Payload"},
        {"id": "p2", "label": "PCI HSM Tokenizer", "role": "security", "tier": "core", "description": "Irreversible Token Vault", "edge_label": "Tokenized PAN"},
        {"id": "p3", "label": "Payment Saga Core", "role": "service", "tier": "hero", "description": "Distributed State Machine", "is_hero": True, "edge_label": "Auth Confirmed"},
        {"id": "p4", "label": "Aurora PostgreSQL", "role": "database", "tier": "storage", "description": "ACID Ledger & Balance", "edge_label": "Event Emitted"},
        {"id": "p5", "label": "MinIO S3 Immutable", "role": "database", "tier": "compliance", "description": "WORM Fiscal Evidence"}
    ]
}


# 3. PAYLOAD ARQUETIPO 3: RADIAL HUB (Microservices Brain)
PAYLOAD_RADIAL = {
    "hub": {
        "id": "hub1",
        "label": "Master Payment Orchestrator",
        "role": "service",
        "tier": "hero",
        "description": "Núcleo de orquestación Saga, idempotencia distribuida y ruteo dinámico.",
        "is_hero": True
    },
    "satellites": [
        {"id": "s1", "label": "Stripe Gateway", "role": "card", "tier": "ext", "description": "International Cards"},
        {"id": "s2", "label": "Visa Direct Switch", "role": "card", "tier": "ext", "description": "Direct Clearing"},
        {"id": "s3", "label": "PIX Instant Rail", "role": "card", "tier": "ext", "description": "Banco Central 24/7"},
        {"id": "s4", "label": "Aurora PostgreSQL", "role": "database", "tier": "storage", "description": "ACID Persistence"},
        {"id": "s5", "label": "Redis Cache", "role": "cache", "tier": "storage", "description": "Locking SETNX"},
        {"id": "s6", "label": "Kafka Event Bus", "role": "stream", "tier": "core", "description": "Event Streaming"}
    ]
}


# 4. PAYLOAD ARQUETIPO 4: SPLIT DUEL (Legacy vs Cloud-Native Target)
PAYLOAD_DUEL = {
    "left": {
        "title": "Arquitectura Monolítica Legacy (2020)",
        "items": [
            "Monolito PHP/MySQL monolítico con acoplamiento severo.",
            "Bloqueos de tabla (table locks) que colapsan transacciones concurrentes.",
            "Despliegues coordinados con ventana de mantenimiento y downtime.",
            "Cero trazabilidad distribuida ante caídas de pasarelas bancarias."
        ]
    },
    "right": {
        "title": "Cloud-Native Event-Driven Target (2026)",
        "items": [
            "Microservicios autónomos en contenedores Kubernetes (EKS).",
            "Persistencia ACID en Aurora PostgreSQL + Cache Redis <15ms.",
            "Despliegues continuos con Canary Releases y Zero-Downtime.",
            "Resiliencia activa con Circuit Breakers y fallback multi-pasarela."
        ]
    }
}


def run_visual_matrix_benchmark():
    print("=" * 115)
    print("🧪 SKETION 8.4 — VISUAL MATRIX BENCHMARK (4 ARQUETIPOS ESPACIALES)")
    print("=" * 115)

    place_reset(max_row_w=3800, gap=140)
    scene = ExcalidrawScene(roughness=0, bg_color="#F8FAFC")

    benchmarks = [
        (SpatialArchetype.LAYERED, "FRAME 1: E-COMMERCE LOGISTICS (LAYERED ARCHITECTURE)", PAYLOAD_LAYERED, 1600.0, 750.0),
        (SpatialArchetype.PIPELINE, "FRAME 2: PAYMENT PROCESSING PIPELINE (CHEVRON FLOW)", PAYLOAD_PIPELINE, 1600.0, 520.0),
        (SpatialArchetype.RADIAL_HUB, "FRAME 3: TRANSACTIONS HUB & SPOKE (THE BRAIN)", PAYLOAD_RADIAL, 1600.0, 680.0),
        (SpatialArchetype.SPLIT_DUEL, "FRAME 4: LEGACY TO TARGET MODERNIZATION (SPLIT DUEL)", PAYLOAD_DUEL, 1600.0, 560.0)
    ]

    for arch, title, payload, tw, th in benchmarks:
        print(f" • Evaluando Arquetipo [{arch.value}]: {title}...")
        fx, fy = place(tw, th)
        VisualMatrixEngine.render_archetype(scene, arch, title, payload, fx, fy, target_w=tw, target_h=th)

    output_path = os.path.join(OUT_DIR, "visual_matrix_4_archetypes_v8_4.excalidraw")
    scene.save(output_path)
    print(f"\nCanvas Matricial v8.4 generado: {output_path}")

    val_scene, val_rep = validate_scene(output_path)
    print("\n" + "=" * 115)
    print("📊 RESULTADOS DEL BENCHMARK VISUAL MATRIX SKETION 8.4")
    print("=" * 115)
    print(f" • Global Sketion Quality Score : {val_rep.sketion_overall_score} / 100 [{('✅ PASS' if val_rep.is_valid else '❌ FAIL')}]")
    print(f" • Repair Dependency Score (RDS): {val_rep.repair_dependency_score} [{val_rep.repair_dependency_status}]")
    print(f" • Elementos Totales Renderizados: {len(scene.elements)}")
    print(f" • Arquetipos Espaciales Probados: 4 (LAYERED, PIPELINE, RADIAL_HUB, SPLIT_DUEL)")
    print(f" • Dimensiones de Frames Ajustados Ceñidos:")
    for f in [e for e in scene.elements if e.get("type") == "frame"]:
        print(f"   - {f.get('name')}: {int(f.get('width', 0))} x {int(f.get('height', 0))} px")
    print("=" * 115)


if __name__ == "__main__":
    run_visual_matrix_benchmark()
