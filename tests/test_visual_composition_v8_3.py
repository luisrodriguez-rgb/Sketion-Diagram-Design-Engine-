"""
Sketion 8.3 — Visual Composition Intelligence Automated Benchmark
Prueba la composición visual autónoma de Sketion en 3 dominios arquitectónicos complejos:
1. Fintech Global Settlement Platform
2. Enterprise Generative AI & MLOps Pipeline
3. Zero-Trust Healthcare EHR & Compliance Platform
Valida el mapeo autónomo de marcas, íconos vectoriales, formas semánticas y auto-fit de frames.
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from visual_intelligence.visual_composition import VisualCompositionEngine
from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from validation.validator import validate_scene

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V7")
os.makedirs(OUT_DIR, exist_ok=True)


# 1. PAYLOAD DOMINIO 1: FINTECH HIGH-THROUGHPUT
FINTECH_LAYERS = [
    {
        "name": "1. Capa de Adquisición & Edge Security",
        "entities": [
            {"id": "f1", "label": "Cloudflare Global WAF", "role": "security", "tier": "edge", "description": "DDoS Shield & Anycast DNS"},
            {"id": "f2", "label": "Web Checkout SPA", "role": "actor", "tier": "client", "description": "React.js PCI iFrame"},
            {"id": "f3", "label": "Mobile SDK iOS & Android", "role": "actor", "tier": "client", "description": "Swift / Kotlin Native"},
            {"id": "f4", "label": "POS Retail Terminal", "role": "actor", "tier": "client", "description": "EMV Chip & Contactless NFC"}
        ]
    },
    {
        "name": "2. Capa de Orquestación & Core Transaccional",
        "entities": [
            {"id": "f5", "label": "Kong API Gateway", "role": "gateway", "tier": "core", "description": "mTLS Auth & Rate Limiting"},
            {"id": "f6", "label": "Payment Saga Orchestrator", "role": "service", "tier": "hero", "description": "Distributed State Machine & Atomicity", "is_hero": True},
            {"id": "f7", "label": "PCI Tokenizer Vault", "role": "security", "tier": "core", "description": "Irreversible Tokenization HSM"}
        ]
    },
    {
        "name": "3. Streaming & Persistencia ACID",
        "entities": [
            {"id": "f8", "label": "Apache Kafka Cluster", "role": "stream", "tier": "core", "description": "Topics: payment.created · settled · failed", "topics": ["tx.auth", "tx.settle", "tx.fail"]},
            {"id": "f9", "label": "Aurora PostgreSQL", "role": "database", "tier": "storage", "description": "Primary Cluster SERIALIZABLE"},
            {"id": "f10", "label": "Redis In-Memory Cache", "role": "cache", "tier": "storage", "description": "Idempotency Keys & Session TTL"},
            {"id": "f11", "label": "ClickHouse Real-Time OLAP", "role": "database", "tier": "analytics", "description": "Financial Metrics & Auditing"}
        ]
    }
]


# 2. PAYLOAD DOMINIO 2: ENTERPRISE GENERATIVE AI & MLOPS
AI_MLOPS_LAYERS = [
    {
        "name": "1. Ingesta de Documentos & Vectorización",
        "entities": [
            {"id": "ai1", "label": "Enterprise Document Ingestor", "role": "service", "tier": "input", "description": "PDF, Office, Markdown & OCR Scans"},
            {"id": "ai2", "label": "Text Chunking & Tokenizer", "role": "service", "tier": "processing", "description": "Semantic Boundary Splitting (512 tokens)"},
            {"id": "ai3", "label": "Embedding Generator Cluster", "role": "service", "tier": "core", "description": "Text-Embedding-3 Large GPU Workers"}
        ]
    },
    {
        "name": "2. Búsqueda Vectorial Híbrida & RAG",
        "entities": [
            {"id": "ai4", "label": "Milvus Vector Database", "role": "database", "tier": "storage", "description": "HNSW Index & Cosine Distance Search"},
            {"id": "ai5", "label": "RAG Context Synthesizer Core", "role": "service", "tier": "hero", "description": "Prompt Template Assembly & Re-Ranking", "is_hero": True},
            {"id": "ai6", "label": "Snowflake Knowledge Warehouse", "role": "database", "tier": "storage", "description": "Relational Metadata & Audit History"}
        ]
    },
    {
        "name": "3. Inferencia LLM & Guardrails de Seguridad",
        "entities": [
            {"id": "ai7", "label": "LLM Security Guardrail WAF", "role": "security", "tier": "edge", "description": "Prompt Injection & PII Data Redaction"},
            {"id": "ai8", "label": "vLLM High-Throughput Cluster", "role": "service", "tier": "core", "description": "PagedAttention Engine Multi-GPU"},
            {"id": "ai9", "label": "LangSmith Telemetry & Traces", "role": "service", "tier": "observability", "description": "Token Cost, Latency & Hallucination Eval"}
        ]
    }
]


# 3. PAYLOAD DOMINIO 3: HEALTHCARE ZERO-TRUST EHR SAAS
HEALTHCARE_LAYERS = [
    {
        "name": "1. Portales Clínicos & Actores Médicos",
        "entities": [
            {"id": "h1", "label": "Doctor Web Portal", "role": "actor", "tier": "client", "description": "Electronic Health Records (EHR)"},
            {"id": "h2", "label": "Mobile Patient App", "role": "actor", "tier": "client", "description": "Prescriptions & Biometric Sign-in"},
            {"id": "h3", "label": "Hospital IoT Vital Monitor", "role": "actor", "tier": "iot", "description": "Telemetry Tele-Care HL7 / FHIR"}
        ]
    },
    {
        "name": "2. Bóveda HIPAA & Motores de Consentimiento",
        "entities": [
            {"id": "h4", "label": "HIPAA Cryptographic Vault", "role": "security", "tier": "hero", "description": "Hardware Security Module (HSM) AES-256", "is_hero": True},
            {"id": "h5", "label": "Patient Consent Engine", "role": "service", "tier": "core", "description": "Dynamic Granular Access Control (ABAC)"},
            {"id": "h6", "label": "MinIO S3 Immutable Vault", "role": "database", "tier": "compliance", "description": "WORM Audit Logs Retention (10 Years)"}
        ]
    },
    {
        "name": "3. Motores de Interoperabilidad & Base de Datos",
        "entities": [
            {"id": "h7", "label": "FHIR Interoperability API", "role": "gateway", "tier": "core", "description": "Standardized Clinical Data Exchange"},
            {"id": "h8", "label": "PostgreSQL Clinical DB", "role": "database", "tier": "storage", "description": "Encrypted PHI Tables at Rest"}
        ]
    }
]


def run_visual_composition_benchmark():
    print("=" * 115)
    print("🧪 SKETION 8.3 — VISUAL COMPOSITION INTELLIGENCE AUTOMATED BENCHMARK")
    print("=" * 115)

    place_reset(max_row_w=3800, gap=140)
    scene = ExcalidrawScene(roughness=0, bg_color="#F8FAFC")

    domains = [
        ("FRAME 1: FINTECH GLOBAL SETTLEMENT PLATFORM", FINTECH_LAYERS, 1600.0, 600.0),
        ("FRAME 2: ENTERPRISE GENERATIVE AI & MLOPS PIPELINE", AI_MLOPS_LAYERS, 1600.0, 600.0),
        ("FRAME 3: ZERO-TRUST HEALTHCARE EHR & COMPLIANCE", HEALTHCARE_LAYERS, 1600.0, 600.0)
    ]

    for title, layers, w, h in domains:
        print(f" • Componiendo visualmente: {title}...")
        fx, fy = place(w, h)
        VisualCompositionEngine.compose_layered_board(scene, title, layers, fx, fy, w=w)

    output_path = os.path.join(OUT_DIR, "visual_composition_v8_3_multi_domain.excalidraw")
    scene.save(output_path)
    print(f"\nCanvas Multidominio v8.3 generado: {output_path}")

    val_scene, val_rep = validate_scene(output_path)
    print("\n" + "=" * 115)
    print("📊 RESULTADOS DEL BENCHMARK VISUAL COMPOSITION INTELLIGENCE SKETION 8.3")
    print("=" * 115)
    print(f" • Global Sketion Quality Score : {val_rep.sketion_overall_score} / 100 [{('✅ PASS' if val_rep.is_valid else '❌ FAIL')}]")
    print(f" • Repair Dependency Score (RDS): {val_rep.repair_dependency_score} [{val_rep.repair_dependency_status}]")
    print(f" • Elementos Totales Renderizados: {len(scene.elements)}")
    print(f" • Dominios Arquitectónicos     : 3 (Fintech, GenAI/MLOps, Healthcare Zero-Trust)")
    print(f" • Auto-Fit de Frames:")
    for f in [e for e in scene.elements if e.get("type") == "frame"]:
        print(f"   - {f.get('name')}: {int(f.get('width', 0))} x {int(f.get('height', 0))} px")
    print("=" * 115)


if __name__ == "__main__":
    run_visual_composition_benchmark()
