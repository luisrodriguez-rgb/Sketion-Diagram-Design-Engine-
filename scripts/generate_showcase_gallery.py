"""
Sketion Showcase Gallery Generator (v10.0 GA)
Genera la galería visual completa de demostración:
- 20 Arquetipos Narrativos de Negocio (A - T)
- 12+ Formas Semánticas Especializadas
Exporta cada caso en formato editable .excalidraw y gráfico vectorial puro .svg.
"""

import os
import sys
import json
import math

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

import sketion
from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from visual_intelligence.visual_matrix import VisualMatrixEngine, SpatialArchetype
from visual_intelligence.visual_composition import VisualCompositionEngine
from visual_intelligence.data_viz import LightDataVizEngine, KPICardSpec, FunnelStepSpec
from export.svg_exporter import SVGExporter

GALLERY_DIR = os.path.join(workspace_dir, "docs", "gallery")
ARCHETYPES_DIR = os.path.join(GALLERY_DIR, "archetypes")
SHAPES_DIR = os.path.join(GALLERY_DIR, "shapes")

os.makedirs(ARCHETYPES_DIR, exist_ok=True)
os.makedirs(SHAPES_DIR, exist_ok=True)


# ===================================================================================================
# 1. GENERADOR DE LOS 20 ARQUETIPOS DE NEGOCIO (A - T)
# ===================================================================================================

ARCHETYPE_PAYLOADS = [
    # 01. Radial Hub / The Brain
    ("01_radial_hub_brain", "01. Hub & Spoke: El Cerebro Transaccional", SpatialArchetype.RADIAL_HUB, {
        "title": "Master Payment Gateway Hub",
        "hub": {"label": "Payment Orchestrator Core", "role": "service", "is_hero": True, "description": "Distributed Saga & Idempotency Engine"},
        "satellites": [
            {"label": "Visa Direct Switch", "role": "card", "description": "Interchange Network"},
            {"label": "Stripe Gateway", "role": "card", "description": "International Cards"},
            {"label": "PIX Instant Rail", "role": "card", "description": "Banco Central 24/7"},
            {"label": "Aurora PostgreSQL", "role": "database", "description": "ACID Ledger"},
            {"label": "Redis Cache", "role": "cache", "description": "Distributed Lock"},
            {"label": "Apache Kafka", "role": "stream", "description": "Event Stream"}
        ]
    }),

    # 02. Split Duel (Legacy vs Cloud-Native Target)
    ("02_split_duel_legacy_vs_cloud", "02. El Duelo: Modernización de Monolito a Cloud-Native", SpatialArchetype.SPLIT_DUEL, {
        "title": "Core Banking Modernization Roadmap",
        "left": {
            "title": "Arquitectura Monolítica Legacy (2020)",
            "items": ["Monolito PHP/MySQL con acoplamiento severo", "Bloqueos de tabla globales en alta concurrencia", "Ventanas de mantenimiento con 2h de downtime", "Cero trazabilidad distribuida ante caídas de pasarela"]
        },
        "right": {
            "title": "Cloud-Native Event-Driven Target (2026)",
            "items": ["Microservicios autónomos en Kubernetes EKS", "Persistencia ACID en Aurora PostgreSQL + Cache Redis", "Despliegues continuos con Canary y Zero-Downtime", "Resiliencia activa con Circuit Breaker multi-proveedor"]
        }
    }),

    # 03. Pipeline with Feedback Loop
    ("03_pipeline_feedback_loop", "03. Pipeline de Checkout con Bucle de Reintento", SpatialArchetype.PIPELINE, {
        "title": "Checkout Payment Authorization Pipeline",
        "stages": ["1. INGEST", "2. TOKENIZATION", "3. SAGA ENGINE", "4. SETTLEMENT", "5. AUDIT"],
        "has_return_loop": True,
        "steps": [
            {"label": "Edge API Gateway", "role": "gateway", "description": "mTLS & Risk Filter", "edge_label": "Encrypted Ingest"},
            {"label": "PCI HSM Tokenizer", "role": "security", "description": "PAN Tokenization Vault", "edge_label": "Tokenized ID"},
            {"label": "Payment Saga Core", "role": "service", "is_hero": True, "description": "Distributed State Machine", "edge_label": "Auth Confirmed"},
            {"label": "Aurora PostgreSQL", "role": "database", "description": "ACID Balance Ledger", "edge_label": "Event Emitted"},
            {"label": "MinIO S3 Immutable", "role": "database", "description": "WORM Fiscal Audit"}
        ]
    }),

    # 04. Medallion Lakehouse
    ("04_medallion_lakehouse", "04. Lakehouse Medallion: Ingesta a Analytics", SpatialArchetype.LAYERED, {
        "title": "Enterprise Data Lakehouse Architecture",
        "layers": [
            {"name": "1. Ingesta Raw (Bronze Tier)", "entities": [{"label": "Kafka Ingest Stream", "role": "stream"}, {"label": "Raw S3 Landing Bucket", "role": "database"}]},
            {"name": "2. Enriquecimiento & Limpieza (Silver Tier)", "entities": [{"label": "Apache Spark Batch ETL", "role": "service"}, {"label": "Apache Iceberg Delta Table", "role": "database"}]},
            {"name": "3. Agregaciones de Negocio (Gold Tier)", "entities": [{"label": "ClickHouse Realtime OLAP", "role": "database", "is_hero": True}, {"label": "Superset BI Dashboards", "role": "actor"}]}
        ]
    }),

    # 05. Value Chain (Porter)
    ("05_value_chain_porter", "05. Cadena de Valor Empresarial", SpatialArchetype.PIPELINE, {
        "title": "End-to-End Enterprise Value Chain",
        "stages": ["1. LOGÍSTICA ENTRADA", "2. OPERACIONES", "3. LOGÍSTICA SALIDA", "4. MARKETING & VENTAS", "5. SERVICIO POST-VENTA"],
        "has_return_loop": False,
        "steps": [
            {"label": "Supplier Ingest Portal", "role": "actor", "description": "Raw Material Sourcing"},
            {"label": "Automated Assembly Line", "role": "service", "is_hero": True, "description": "Robotic Manufacturing"},
            {"label": "Fleet Dispatch Hub", "role": "gateway", "description": "Real-time Vehicle Routing"},
            {"label": "Shopify Commerce Engine", "role": "card", "description": "Omnichannel Sales"},
            {"label": "Customer Support Hub", "role": "actor", "description": "24/7 SLA Resolution"}
        ]
    }),

    # 06. Growth Flywheel
    ("06_growth_flywheel", "06. Flywheel de Crecimiento de Producto", SpatialArchetype.RADIAL_HUB, {
        "title": "Product-Led Growth (PLG) Flywheel",
        "hub": {"label": "Core Product Experience", "role": "service", "is_hero": True, "description": "High-Value Feature Platform"},
        "satellites": [
            {"label": "Freemium User Acquisition", "role": "actor", "description": "Viral Inbound Traffic"},
            {"label": "Time-To-Value Activation", "role": "service", "description": "Guided Onboarding Flow"},
            {"label": "Feature Paywall Upgrade", "role": "card", "description": "Stripe Self-Serve Billing"},
            {"label": "Usage Expansion Engine", "role": "stream", "description": "Multi-Seat Collaboration"},
            {"label": "Advocacy & Referral Loop", "role": "actor", "description": "Net Promoter Engine"}
        ]
    }),

    # 07. Maturity Roadmap Staircase
    ("07_maturity_roadmap_staircase", "07. Escalera de Madurez Tecnológica", SpatialArchetype.LAYERED, {
        "title": "Cloud Engineering Maturity Horizons",
        "layers": [
            {"name": "Horizonte 1: Fundaciones Cloud (Mes 1-3)", "entities": [{"label": "Docker Containerization", "role": "service"}, {"label": "GitLab CI/CD Baseline", "role": "service"}]},
            {"name": "Horizonte 2: Orquestación & Resiliencia (Mes 4-6)", "entities": [{"label": "Kubernetes EKS Cluster", "role": "service", "is_hero": True}, {"label": "Prometheus Observability", "role": "service"}]},
            {"name": "Horizonte 3: Autonomía & ML (Mes 7-12)", "entities": [{"label": "Istio Service Mesh", "role": "security"}, {"label": "KEDA Auto-Scaling", "role": "service"}, {"label": "MLOps Feature Store", "role": "database"}]}
        ]
    }),

    # 08. Operational Swimlanes
    ("08_operational_swimlanes", "08. Swimlanes Operativos Multi-Departamento", SpatialArchetype.LAYERED, {
        "title": "Cross-Functional Incident Resolution Swimlane",
        "layers": [
            {"name": "Carril 1: Detección & Monitoreo (SRE NOC)", "entities": [{"label": "Datadog Anomaly Alert", "role": "service"}, {"label": "PagerDuty Escalation", "role": "security"}]},
            {"name": "Carril 2: Mitigación & Código (Engineering)", "entities": [{"label": "War Room Coordinator", "role": "service", "is_hero": True}, {"label": "Canary Rollback Trigger", "role": "gateway"}]},
            {"name": "Carril 3: Comunicación Externa (Customer Ops)", "entities": [{"label": "Public Statuspage Update", "role": "actor"}, {"label": "Post-Mortem Incident Report", "role": "database"}]}
        ]
    }),

    # 09. Conversion Funnel
    ("09_conversion_funnel", "09. Embudo de Conversión de Usuario", SpatialArchetype.PIPELINE, {
        "title": "B2B SaaS Conversion Funnel",
        "stages": ["1. VISITANTES (100k)", "2. SIGNUPS (15k)", "3. ACTIVADOS (4.5k)", "4. DE PAGO (1.2k)", "5. ENTERPRISE (180)"],
        "has_return_loop": False,
        "steps": [
            {"label": "Organic SEO & Ads Ingest", "role": "actor", "description": "100,000 Unique Visitors"},
            {"label": "Magic Link Onboarding", "role": "gateway", "description": "15.0% Signup Rate"},
            {"label": "First Workspace Project", "role": "service", "description": "30.0% Activation Rate"},
            {"label": "Stripe Pro Subscription", "role": "card", "is_hero": True, "description": "26.6% Paid Conversion"},
            {"label": "Enterprise Custom SLA", "role": "security", "description": "15.0% Enterprise Upgrade"}
        ]
    }),

    # 10. Capability & SLA Matrix
    ("10_capability_sla_matrix", "10. Matriz de Capacidades y SLA", SpatialArchetype.LAYERED, {
        "title": "Multi-Tier Infrastructure SLA Matrix",
        "layers": [
            {"name": "Tier 1: Misión Crítica (SLA 99.999% · P99 <10ms)", "entities": [{"label": "Payment Core Cluster", "role": "service", "is_hero": True}, {"label": "Aurora Multi-AZ DB", "role": "database"}]},
            {"name": "Tier 2: Servicios de Negocio (SLA 99.95% · P99 <80ms)", "entities": [{"label": "User Profile Service", "role": "service"}, {"label": "Redis Session Cache", "role": "cache"}]},
            {"name": "Tier 3: Reportes Asíncronos (SLA 99.5% · Batch)", "entities": [{"label": "Nightly Reconciliation Worker", "role": "service"}, {"label": "Snowflake Cold DWH", "role": "database"}]}
        ]
    }),

    # 11. Event-Driven Mesh
    ("11_event_driven_mesh", "11. Malla Desacoplada Basada en Eventos", SpatialArchetype.LAYERED, {
        "title": "Enterprise Event-Driven Architecture",
        "layers": [
            {"name": "1. Publicadores de Eventos", "entities": [{"label": "Order Service", "role": "service"}, {"label": "Inventory Service", "role": "service"}]},
            {"name": "2. Backbone de Eventos (Event Stream Core)", "entities": [{"label": "Apache Kafka Event Mesh", "role": "stream", "is_hero": True}, {"label": "Schema Registry Avro", "role": "security"}]},
            {"name": "3. Consumidores & Persistencia", "entities": [{"label": "Notification Worker", "role": "service"}, {"label": "PostgreSQL Order DB", "role": "database"}]}
        ]
    }),

    # 12. Zero-Trust Security Perimeter
    ("12_zero_trust_security_perimeter", "12. Perímetro de Seguridad Zero-Trust", SpatialArchetype.LAYERED, {
        "title": "Zero-Trust HIPAA/PCI Compliant Architecture",
        "layers": [
            {"name": "1. Borde Perimetral & Anti-DDoS", "entities": [{"label": "Cloudflare Global WAF", "role": "security"}, {"label": "mTLS Envoy Gateway", "role": "security"}]},
            {"name": "2. Bóveda Criptográfica & Auth", "entities": [{"label": "PCI HSM Key Vault", "role": "security", "is_hero": True}, {"label": "OPA Policy Engine", "role": "security"}]},
            {"name": "3. Almacenamiento Cifrado WORM", "entities": [{"label": "MinIO WORM S3 Audit", "role": "database"}, {"label": "PostgreSQL Encrypted PHI", "role": "database"}]}
        ]
    }),

    # 13. Micro-Frontend Shell
    ("13_micro_frontend_shell", "13. Arquitectura Micro-Frontend Modular", SpatialArchetype.LAYERED, {
        "title": "Enterprise Micro-Frontend Application Shell",
        "layers": [
            {"name": "1. Aplicación Shell Contenedora", "entities": [{"label": "Next.js App Shell Host", "role": "actor", "is_hero": True}, {"label": "Auth0 SSO Provider", "role": "security"}]},
            {"name": "2. Micro-Frontends Remotos", "entities": [{"label": "Checkout Remote (React)", "role": "service"}, {"label": "Catalog Remote (Vue.js)", "role": "service"}, {"label": "Account Remote (Svelte)", "role": "service"}]},
            {"name": "3. Backend For Frontend (BFF)", "entities": [{"label": "GraphQL Federation Gateway", "role": "gateway"}]}
        ]
    }),

    # 14. Edge Anycast CDN Mesh
    ("14_edge_anycast_cdn_mesh", "14. Malla Perimetral Anycast & CDN", SpatialArchetype.LAYERED, {
        "title": "Global Edge Computing & Anycast Network",
        "layers": [
            {"name": "1. Red Global Anycast", "entities": [{"label": "Global Anycast IP Mesh", "role": "security"}, {"label": "Cloudflare Edge Workers", "role": "service", "is_hero": True}]},
            {"name": "2. Capa de Caché Perimetral", "entities": [{"label": "Redis Edge KV Store", "role": "cache"}, {"label": "CloudFront CDN Points", "role": "service"}]},
            {"name": "3. Origen Centralizado", "entities": [{"label": "Origin EKS Cluster", "role": "service"}, {"label": "Primary Aurora DB", "role": "database"}]}
        ]
    }),

    # 15. Multi-Tenant SaaS Isolation
    ("15_multi_tenant_saas_isolation", "15. Aislamiento Multi-Inquilino (SaaS)", SpatialArchetype.LAYERED, {
        "title": "Multi-Tenant SaaS Data Isolation",
        "layers": [
            {"name": "1. Ruteo de Inquilinos & Gateway", "entities": [{"label": "Tenant Context Router", "role": "gateway"}, {"label": "Cognito RBAC Auth", "role": "security"}]},
            {"name": "2. Lógica Compartida Stateless", "entities": [{"label": "Tenant-Aware Service Core", "role": "service", "is_hero": True}]},
            {"name": "3. Persistencia Aislada por Esquema", "entities": [{"label": "Postgres (Tenant A Schema)", "role": "database"}, {"label": "Postgres (Tenant B Schema)", "role": "database"}]}
        ]
    }),

    # 16. IoT Device Fleet Telemetry
    ("16_iot_device_fleet_telemetry", "16. Ingesta Masiva de Telemetría IoT", SpatialArchetype.PIPELINE, {
        "title": "High-Volume IoT Telemetry Fleet Ingestion",
        "stages": ["1. SENSORES (MQTT)", "2. BROKER CLOUD", "3. STREAM ENGINE", "4. BASE TIME-SERIES", "5. NOC ALERTS"],
        "has_return_loop": False,
        "steps": [
            {"label": "Edge IoT Sensor Node", "role": "actor", "description": "100k Connected Devices"},
            {"label": "EMQX MQTT Broker", "role": "gateway", "description": "QoS 1 Ingestion"},
            {"label": "Apache Flink CEP", "role": "service", "is_hero": True, "description": "Sliding Window Anomaly"},
            {"label": "TimescaleDB Time-Series", "role": "database", "description": "Sub-Second Sensor Metrics"},
            {"label": "Grafana NOC Wall", "role": "actor", "description": "Real-time Operations"}
        ]
    }),

    # 17. GenAI / RAG MLOps Pipeline
    ("17_genai_rag_mlops_pipeline", "17. Pipeline de IA Generativa & RAG", SpatialArchetype.LAYERED, {
        "title": "Enterprise Retrieval-Augmented Generation (RAG)",
        "layers": [
            {"name": "1. Ingesta Documental & Embeddings", "entities": [{"label": "PDF / OCR Ingestion", "role": "actor"}, {"label": "GPU Embedding Worker", "role": "service"}]},
            {"name": "2. Base Vectorial & Sintetizador RAG", "entities": [{"label": "Milvus Vector Database", "role": "database"}, {"label": "RAG Synthesizer Core", "role": "service", "is_hero": True}]},
            {"name": "3. Inferencia LLM & Guardrails", "entities": [{"label": "vLLM GPU Cluster", "role": "service"}, {"label": "LLM Guardrail WAF", "role": "security"}, {"label": "LangSmith Traces", "role": "service"}]}
        ]
    }),

    # 18. Database Replication & Sharding
    ("18_database_replication_sharding", "18. Replicación y Sharding de Bases de Datos", SpatialArchetype.RADIAL_HUB, {
        "title": "High-Availability Database Cluster Topology",
        "hub": {"label": "Primary Database Master (Read/Write)", "role": "database", "is_hero": True, "description": "SERIALIZABLE ACID Transactions"},
        "satellites": [
            {"label": "Read Replica 1 (Reporting)", "role": "database", "description": "Async WAL Replication"},
            {"label": "Read Replica 2 (Analytics)", "role": "database", "description": "Async WAL Replication"},
            {"label": "PgBouncer Connection Pool", "role": "gateway", "description": "Pooler Proxy"},
            {"label": "Redis Query Cache", "role": "cache", "description": "TTL 60s Cache"},
            {"label": "Backup S3 WORM Store", "role": "database", "description": "Continuous Archiving"}
        ]
    }),

    # 19. Disaster Recovery Multi-Region
    ("19_disaster_recovery_multi_region", "19. Recuperación ante Desastres Multi-Región", SpatialArchetype.LAYERED, {
        "title": "Active-Passive Disaster Recovery Architecture",
        "layers": [
            {"name": "1. Enrutamiento DNS Global", "entities": [{"label": "AWS Route53 Failover", "role": "gateway", "is_hero": True}, {"label": "Health Check Heartbeat", "role": "security"}]},
            {"name": "2. Región Primaria (US-East-1 Active)", "entities": [{"label": "Primary EKS Cluster", "role": "service"}, {"label": "Primary Aurora PostgreSQL", "role": "database"}]},
            {"name": "3. Región Secundaria (US-West-2 Standby)", "entities": [{"label": "Standby EKS Cluster", "role": "service"}, {"label": "Cross-Region Aurora Replica", "role": "database"}]}
        ]
    }),

    # 20. CI/CD Canary Deployment
    ("20_cicd_canary_deployment", "20. Pipeline CI/CD con Despliegues Canary", SpatialArchetype.PIPELINE, {
        "title": "Automated Canary Deployment & Rollback Pipeline",
        "stages": ["1. GIT COMMIT", "2. TEST SUITE", "3. BUILD ARTIFACT", "4. CANARY 10%", "5. PRODUCTION 100%"],
        "has_return_loop": True,
        "steps": [
            {"label": "Developer Git Push", "role": "actor", "description": "Pull Request Sign-off"},
            {"label": "Automated CI Tests", "role": "service", "description": "Unit & Integration Tests"},
            {"label": "Docker Container Registry", "role": "database", "description": "Immutable Image SHA"},
            {"label": "ArgoCD Canary Rollout", "role": "service", "is_hero": True, "description": "10% Traffic Health Metric"},
            {"label": "Full Production Scale", "role": "service", "description": "100% Traffic Zero-Downtime"}
        ]
    })
]


# ===================================================================================================
# 2. GENERADOR DE LAS 12+ FORMAS SEMÁNTICAS ESPECIALIZADAS
# ===================================================================================================

SHAPE_SPECS = [
    ("shape_01_database_cylinder", "Cilindro de Base de Datos", "DATABASE_CYLINDER", lambda s, f: s.add_database_cylinder(50, 70, 260, 130, title="Aurora PostgreSQL", sublabel="ACID Persistent Ledger", badge="ACID DB", is_hero=False, frame_id=f)),
    ("shape_02_streaming_pipe", "Tubería de Streaming", "STREAMING_PIPE", lambda s, f: s.add_streaming_pipe(50, 70, 320, 130, title="Apache Kafka Event Stream", topics=["tx.init", "tx.settled", "tx.dlq"], badge="EVENT STREAM", frame_id=f)),
    ("shape_03_security_barrier_waf", "Barrera Perimetral Zero-Trust", "SECURITY_BARRIER", lambda s, f: s.add_security_barrier(50, 70, 320, 130, title="Cloudflare Global WAF", rules=["DDoS Shield Protection", "mTLS Edge Inspection", "Rate Limit 10k rps"], badge="ZERO-TRUST", frame_id=f)),
    ("shape_04_actor_pill", "Pastilla de Actor / Cliente", "ACTOR_PILL", lambda s, f: s.add_actor_node(50, 90, 260, 60, name="Mobile Client App", role="CONSUMER", icon="laptop", is_hero=False, frame_id=f)),
    ("shape_05_decision_diamond", "Rombo de Decisión Condicional", "DECISION_DIAMOND", lambda s, f: (s.add_diamond(90, 60, 160, 140, bg="#FFFBEB", stroke="#D97706", stroke_w=1.5, frame_id=f), s.add_text(115, 115, "Risk > 85?", font_size=13, font_family=2, color="#92400E", frame_id=f))),
    ("shape_06_hero_card", "Tarjeta Hero Transaccional", "HERO_CARD", lambda s, f: s.add_quad_card(50, 70, 300, 130, title="Payment Saga Orchestrator", sublabel="Distributed State Machine & Atomicity", badge="HERO CORE", icon="server", is_hero=True, frame_id=f)),
    ("shape_07_kpi_metric_card", "Tarjeta de Métrica / KPI", "METRIC_CARD", lambda s, f: LightDataVizEngine.render_kpi_card(s, 50, 70, 260, 130, KPICardSpec(value="99.999%", label="Platform SLA Availability", subtext="P99 Latency < 12ms", status_color="#059669", badge="SLO METRIC"), frame_id=f)),
    ("shape_08_conversion_funnel_step", "Paso de Embudo / Funnel", "FUNNEL_STEP", lambda s, f: LightDataVizEngine.render_funnel(s, 50, 70, 320, 130, [FunnelStepSpec(step_name="1. Inbound Leads", volume_label="50,000", conversion_pct="100%"), FunnelStepSpec(step_name="2. Tokenized Checkout", volume_label="14,250", conversion_pct="28.5%", is_hero=True)], frame_id=f)),
    ("shape_09_action_affordance_button", "Control de Acción / Affordance", "ACTION_AFFORDANCE", lambda s, f: (s.add_rect(50, 90, 240, 50, bg="#EFF6FF", stroke="#2563EB", stroke_w=1.5, roundness_type=3, frame_id=f), s.add_text(65, 105, "POST /v1/payments [EXECUTE]", font_size=11, font_family=3, color="#1D4ED8", frame_id=f))),
    ("shape_10_vpc_container_boundary", "Límite de Contenedor / VPC", "VPC_CONTAINER", lambda s, f: (s.add_rect(50, 70, 320, 130, bg="#F8FAFC", stroke="#94A3B8", stroke_w=1.5, stroke_style="dashed", roundness_type=3, frame_id=f), s.add_text(65, 80, "AWS VPC (us-east-1 Private Subnet)", font_size=11, font_family=2, color="#64748B", frame_id=f))),
    ("shape_11_alert_risk_callout", "Callout de Alerta / Riesgo", "ALERT_CALLOUT", lambda s, f: (s.add_rect(50, 70, 320, 120, bg="#FEF2F2", stroke="#FCA5A5", stroke_w=1.5, roundness_type=3, frame_id=f), s.add_icon("alert", 65, 82, size=18.0, color="#DC2626", frame_id=f), s.add_text(90, 84, "CRITICAL DEPENDENCY", font_size=12, font_family=2, color="#991B1B", frame_id=f), s.add_text(65, 110, "Cualquier fallo en el HSM tokenizador detiene transacciones.", font_size=11, font_family=2, color="#7F1D1D", frame_id=f))),
    ("shape_12_quad_card_standard", "Tarjeta Quad de Servicio Estándar", "QUAD_CARD", lambda s, f: s.add_quad_card(50, 70, 260, 130, title="Notification Worker", sublabel="WhatsApp & SMS Real-time Alerts", badge="MICROSERVICE", icon="server", is_hero=False, frame_id=f))
]


def generate_all_showcase():
    print("=" * 115)
    print("🎨 GENERANDO GALERÍA VISUAL DE DEMOSTRACIÓN (20 ARQUETIPOS + 12 FORMAS)")
    print("=" * 115)

    # 1. Generar 20 Arquetipos
    print("\n • [1/2] Generando 20 Arquetipos Narrativos de Negocio...")
    for file_id, title, archetype, payload in ARCHETYPE_PAYLOADS:
        scene = ExcalidrawScene(roughness=0, bg_color="#F8FAFC")
        place_reset(max_row_w=3800, gap=140)
        
        tw = 1600.0
        th = 650.0 if archetype != SpatialArchetype.PIPELINE else 520.0
        fx, fy = place(tw, th)
        
        VisualMatrixEngine.render_archetype(scene, archetype, title, payload, fx, fy, target_w=tw, target_h=th)
        
        excal_path = os.path.join(ARCHETYPES_DIR, f"{file_id}.excalidraw")
        svg_path = os.path.join(ARCHETYPES_DIR, f"{file_id}.svg")
        
        scene.save(excal_path)
        SVGExporter.export(scene.to_dict(), svg_path)
        print(f"   ✅ Arquetipo generado: {file_id}.svg & .excalidraw")

    # 2. Generar 12 Formas Semánticas
    print("\n • [2/2] Generando Muestrario de las 12+ Formas Semánticas...")
    for file_id, name, shape_code, render_fn in SHAPE_SPECS:
        scene = ExcalidrawScene(roughness=0, bg_color="#FFFFFF")
        fid = scene.add_frame(f"FORMA SEMÁNTICA: {name.upper()}", 10, 10, 420, 240)
        scene.add_text(30, 40, f"SKETION VISUAL PRIMITIVE · {shape_code}", font_size=11, font_family=2, color="#64748B", frame_id=fid)
        
        render_fn(scene, fid)
        scene.auto_fit_frame(fid, padding=30.0)
        
        excal_path = os.path.join(SHAPES_DIR, f"{file_id}.excalidraw")
        svg_path = os.path.join(SHAPES_DIR, f"{file_id}.svg")
        
        scene.save(excal_path)
        SVGExporter.export(scene.to_dict(), svg_path)
        print(f"   ✅ Forma generada: {file_id}.svg & .excalidraw")

    print("\n" + "=" * 115)
    print("🏆 GALERÍA VISUAL GENERADA CON ÉXITO")
    print(f" • Directorio de Salida: {GALLERY_DIR}")
    print(f" • Arquetipos Generados: {len(ARCHETYPE_PAYLOADS)} archivos SVG y .excalidraw")
    print(f" • Formas Generadas    : {len(SHAPE_SPECS)} archivos SVG y .excalidraw")
    print("=" * 115)


if __name__ == "__main__":
    generate_all_showcase()
