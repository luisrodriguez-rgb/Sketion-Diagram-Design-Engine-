"""
Generador de Categoría 04: Data, APIs & AI (15 Plantillas)
"""

from .common import create_base_scene, save_and_export

def generate():
    print("\n--- Generando 04: Data, APIs & AI (15 plantillas) ---")
    cat = "04_data_apis_ai"

    # 61. DFD Level 0 (Context)
    s, fid, tw, th = create_base_scene("Data Flow Diagram (DFD Level 0 Context)", "DATA & AI")
    s.add_actor_node(40, 180, 200, 75, "Usuario Cliente", "Entidad Externa", frame_id=fid)
    s.add_arrow(240, 215, 450, 215, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_ellipse(450, 120, 360, 200, bg="#FFF5F2", stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_text(520, 210, "0.0 SISTEMA DE COMERCIO", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_arrow(810, 215, 1020, 215, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_quad_card(1020, 160, 260, 110, "Pasarela Bancaria", "Entidad Externa 3DS", badge="EXTERNAL", frame_id=fid)
    save_and_export(s, fid, cat, 61, "61_dfd_level_0", "Data Flow Diagram Level 0", "medium", "dfd_context", ["external_entities", "process", "flows"])

    # 62. DFD Level 1
    s, fid, tw, th = create_base_scene("Data Flow Diagram (DFD Level 1 Decomposition)", "DATA & AI")
    dfd_procs = [("1.0 Autenticar", 40), ("2.0 Gestionar Carrito", 390), ("3.0 Procesar Orden", 740), ("4.0 Facturacion", 1090)]
    for pname, px in dfd_procs:
        s.add_ellipse(px, 140, 260, 140, bg="#FFFFFF", stroke="#0F172A", stroke_w=1.8, frame_id=fid)
        s.add_text(px + 45, 200, pname, font_size=12, font_family=3, color="#0F172A", frame_id=fid)
        if px < 1090:
            s.add_arrow(px + 260, 210, px + 350, 210, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 62, "62_dfd_level_1", "Data Flow Diagram Level 1", "high", "dfd_decomp", ["subprocesses", "datastores"])

    # 63. Data Pipeline Architecture
    s, fid, tw, th = create_base_scene("Modern Data Pipeline (Batch & Real-Time Streaming)", "DATA & AI")
    s.add_quad_card(40, 160, 220, 110, "Fuentes de Eventos", "IoT + Webhooks HTTP", badge="SOURCES", frame_id=fid)
    s.add_arrow(260, 215, 340, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_streaming_pipe(340, 140, 300, 140, "Apache Kafka Cluster", ["orders.stream.v1", "telemetry.raw"], badge="BROKER", is_hero=True, frame_id=fid)
    s.add_arrow(640, 215, 720, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(720, 140, 280, 140, "Apache Spark / Flink", "Transformaciones en streaming\nValidacion de esquemas Avro", badge="PROCESSING", frame_id=fid)
    s.add_arrow(1000, 215, 1080, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_database_cylinder(1080, 140, 280, 140, "Apache Iceberg Lakehouse", "Parquet en Amazon S3", frame_id=fid)
    save_and_export(s, fid, cat, 63, "63_data_pipeline_architecture", "Data Pipeline Architecture", "high", "data_pipeline", ["sources", "lakehouse", "analytics"])

    # 64. Data Warehouse Architecture (Star Schema)
    s, fid, tw, th = create_base_scene("Enterprise Data Warehouse (Staging -> Star Schema -> Data Marts)", "DATA & AI")
    s.add_rect(40, 80, 340, 350, bg="#F8FAFC", stroke="#0F172A", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "CAPA 1: STAGING AREA", font_size=11, font_family=3, color="#0F172A", frame_id=fid)
    s.add_quad_card(60, 150, 300, 90, "Raw Staging Tables", "Ingesta directa sin transformar", frame_id=fid)
    s.add_arrow(380, 220, 460, 220, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_rect(460, 80, 480, 350, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(480, 105, "CAPA 2: STAR SCHEMA (CORE DWH)", font_size=11, font_family=3, color="#D93829", frame_id=fid)
    s.add_quad_card(480, 140, 200, 80, "Dim_Customer", "Dimension SCD Tipo 2", frame_id=fid)
    s.add_quad_card(720, 140, 200, 80, "Dim_Product", "Catalogo y Categorias", frame_id=fid)
    s.add_quad_card(600, 260, 220, 100, "Fact_Sales", "Metricas de Venta", is_hero=True, frame_id=fid)
    s.add_arrow(940, 220, 1020, 220, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_rect(1020, 80, 380, 350, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(1040, 105, "CAPA 3: DATA MARTS BI", font_size=11, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_quad_card(1040, 150, 340, 90, "Data Mart Finanzas", "PowerBI / Tableau Dashboards", badge="FINANCE", frame_id=fid)
    save_and_export(s, fid, cat, 64, "64_data_warehouse_architecture", "Data Warehouse Architecture", "high", "dwh_tiers", ["staging", "star_schema", "datamarts"])

    # 65. Data Lake Architecture (Medallion)
    s, fid, tw, th = create_base_scene("Data Lakehouse Medallion Multi-Tier Architecture", "DATA & AI")
    tiers = [("BRONZE (RAW)", "Archivos JSON y CSV brutos\nSin schema enforcement", 40, "#CD7F32", False),
             ("SILVER (CLEANSED)", "Tablas limpias y deduplicadas\nSchema evolution habilitado", 500, "#94A3B8", False),
             ("GOLD (AGGREGATED)", "Modelos dimensionales de negocio\nOptimizados para queries analiticas", 960, "#D97706", True)]
    for tname, tdesc, tx, tcolor, is_h in tiers:
        s.add_rect(tx, 80, 440, 350, bg="#FFF5F2" if is_h else "#FFFFFF", stroke=tcolor, stroke_w=2.0, roundness_type=3, frame_id=fid)
        s.add_text(tx + 20, 105, tname, font_size=12, font_family=3, color=tcolor, frame_id=fid)
        s.add_text(tx + 20, 150, tdesc, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 65, "65_data_lake_architecture", "Data Lake Architecture", "high", "lakehouse", ["raw", "bronze", "silver", "gold"])

    # 66. ETL Pipeline
    s, fid, tw, th = create_base_scene("ETL / ELT Pipeline with Data Quality Validation Gates", "DATA & AI")
    p_steps = ["1. Extract (APIs/DB)", "2. Validate (Great Expectations)", "3. Transform (dbt Core)", "4. Load (Snowflake)"]
    for i, pstep in enumerate(p_steps):
        px = 40 + i * 345
        s.add_quad_card(px, 140, 330, 150, pstep, f"Etapa #{i+1} del pipeline de datos", badge="ETL", is_hero=(i==1), frame_id=fid)
        if i < 3:
            s.add_arrow(px + 330, 215, px + 345, 215, stroke="#D93829" if i==1 else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 66, "66_etl_pipeline", "ETL Pipeline", "medium", "etl_flow", ["extract", "transform", "load", "dq"])

    # 67. API Request Flow
    s, fid, tw, th = create_base_scene("REST API Request-Response Lifecycle Flow", "DATA & AI")
    r_nodes = ["1. Cliente HTTP", "2. API Gateway", "3. Auth / JWT", "4. Service Controller", "5. PostgreSQL DB"]
    for i, rname in enumerate(r_nodes):
        rx = 40 + i * 275
        s.add_quad_card(rx, 140, 260, 150, rname, f"Fase #{i+1} de la peticion", badge="HTTP", is_hero=(i==1), frame_id=fid)
        if i < 4:
            s.add_arrow(rx + 260, 215, rx + 275, 215, stroke="#D93829" if i==1 else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 67, "67_api_request_flow", "API Request Flow", "high", "sequence_flow", ["client", "gateway", "controller", "db"])

    # 68. API Integration Map
    s, fid, tw, th = create_base_scene("Third-Party API Integration & Contract Map", "DATA & AI")
    s.add_quad_card(550, 140, 320, 150, "CORE APP PLATFORM", "Orquestador de Servicios Internos", badge="CORE", is_hero=True, frame_id=fid)
    ext_apis = [("Stripe Payments", 40, 80), ("Twilio SMS", 40, 260), ("SendGrid Email", 1080, 80), ("Google Maps API", 1080, 260)]
    for apiname, ax, ay in ext_apis:
        s.add_quad_card(ax, ay, 280, 110, apiname, "Integracion HTTPS / REST", badge="3RD PARTY", frame_id=fid)
        if ax < 500:
            s.add_arrow(ax + 280, ay + 55, 550, 215, stroke="#D93829", stroke_w=1.5, frame_id=fid)
        else:
            s.add_arrow(870, 215, ax, ay + 55, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    save_and_export(s, fid, cat, 68, "68_api_integration_map", "API Integration Map", "high", "integration_map", ["internal_services", "external_apis"])

    # 69. Webhook Architecture
    s, fid, tw, th = create_base_scene("Resilient Webhook Architecture (Publisher, Queue, Retry DLQ, Worker)", "DATA & AI")
    s.add_quad_card(40, 160, 220, 110, "Stripe Publisher", "Webhook Event Dispatched", badge="PUBLISHER", frame_id=fid)
    s.add_arrow(260, 215, 340, 215, stroke="#94A3B8", frame_id=fid)
    s.add_quad_card(340, 130, 260, 150, "Webhook Receiver", "HMAC Signature Verify\nIdempotency Check", badge="RECEIVER", is_hero=True, frame_id=fid)
    s.add_arrow(600, 215, 680, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_streaming_pipe(680, 140, 320, 140, "SQS Event Queue", ["event.charge.succeeded", "retry.dlq.v1"], badge="QUEUE", frame_id=fid)
    s.add_arrow(1000, 215, 1080, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(1080, 150, 260, 120, "Async Worker", "Database Sync\nEmail Dispatch", badge="WORKER", frame_id=fid)
    save_and_export(s, fid, cat, 69, "69_webhook_architecture", "Webhook Architecture", "high", "webhook_pipeline", ["publisher", "queue", "dlq", "worker"])

    # 70. OAuth Authentication Flow (PKCE)
    s, fid, tw, th = create_base_scene("OAuth 2.0 Authorization Code Flow with PKCE", "DATA & AI")
    o_steps = ["1. Code Challenge", "2. Auth Consent", "3. Auth Code Issued", "4. Code + Verifier Exchange", "5. Access + Refresh Token"]
    for i, ostep in enumerate(o_steps):
        ox = 40 + i * 275
        s.add_quad_card(ox, 140, 260, 150, ostep, f"Paso #{i+1} de autorizacion", badge="PKCE", is_hero=(i==3), frame_id=fid)
        if i < 4:
            s.add_arrow(ox + 260, 215, ox + 275, 215, stroke="#D93829" if i==3 else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 70, "70_oauth_authentication_flow", "OAuth Authentication Flow", "extreme", "oauth_sequence", ["user", "client", "auth_server", "api"])

    # 71. JWT Authentication Flow
    s, fid, tw, th = create_base_scene("JSON Web Token (JWT) Lifecycle: Issue, Verify & Refresh", "DATA & AI")
    jwt_blocks = [("1. Login Request", "Usuario y contrasena", 40, False),
                  ("2. Emision de JWT", "Firma RS256 con clave privada", 390, True),
                  ("3. Validacion Gateway", "Verificacion de clave publica", 740, False),
                  ("4. Token Refresh", "Rotacion de refresh token", 1090, False)]
    for jtitle, jdesc, jx, is_h in jwt_blocks:
        s.add_quad_card(jx, 140, 310, 150, jtitle, jdesc, badge="JWT", is_hero=is_h, frame_id=fid)
        if jx < 1090:
            s.add_arrow(jx + 310, 215, jx + 350, 215, stroke="#D93829" if is_h else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 71, "71_jwt_authentication_flow", "JWT Authentication Flow", "medium", "jwt_flow", ["token_issue", "verify", "refresh"])

    # 72. Multi-Agent System Hub
    s, fid, tw, th = create_base_scene("Multi-Agent Autonomous System (Supervisor, Researcher, Coder, Critic)", "DATA & AI")
    s.add_quad_card(600, 70, 260, 90, "LEAD ORCHESTRATOR", "Task Decomposition & Routing", badge="SUPERVISOR", is_hero=True, frame_id=fid)
    s.add_quad_card(200, 240, 250, 110, "Agent 1: Researcher", "Web Search & Fact Check", badge="SPECIALIST", frame_id=fid)
    s.add_quad_card(600, 240, 250, 110, "Agent 2: Code Engineer", "Synthesis & Unit Testing", badge="SPECIALIST", frame_id=fid)
    s.add_quad_card(1000, 240, 250, 110, "Agent 3: Quality Critic", "Evaluation & Guardrails", badge="SPECIALIST", frame_id=fid)
    s.add_arrow(680, 160, 325, 240, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(730, 160, 725, 240, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(780, 160, 1125, 240, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 72, "72_multi_agent_system", "Multi-Agent System", "extreme", "multi_agent_hub", ["orchestrator", "specialists", "memory"])

    # 73. LLM App Architecture
    s, fid, tw, th = create_base_scene("Production LLM Application (Semantic Cache, Guardrails, Model Fallback)", "DATA & AI")
    s.add_quad_card(40, 160, 240, 110, "User Prompt", "Entrada de consulta", badge="INPUT", frame_id=fid)
    s.add_arrow(280, 215, 360, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(360, 140, 280, 140, "Semantic Cache (Redis)", "Similitud Coseno >= 0.95\nEvita llamadas innecesarias", badge="CACHE", frame_id=fid)
    s.add_arrow(640, 215, 720, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(720, 130, 300, 160, "LLM Router & Guardrails", "NeMo Guardrails + Fallback\nClaude 3.5 -> GPT-4o", badge="ORCHESTRATOR", is_hero=True, frame_id=fid)
    s.add_arrow(1020, 215, 1100, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(1100, 160, 260, 110, "Structured Response", "JSON Schema validado", badge="OUTPUT", frame_id=fid)
    save_and_export(s, fid, cat, 73, "73_llm_app_architecture", "LLM App Architecture", "high", "llm_stack", ["semantic_cache", "guardrails", "routing"])

    # 74. Vector Database Architecture (HNSW Internal)
    s, fid, tw, th = create_base_scene("Vector Database Architecture (Embedding API, HNSW Index, Storage Engine)", "DATA & AI")
    s.add_quad_card(40, 160, 240, 120, "Embedding Engine", "Model: text-embedding-3\nDimension: 1536d", badge="EMBED", frame_id=fid)
    s.add_arrow(280, 220, 380, 220, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_rect(380, 80, 560, 350, bg="#FFF5F2", stroke="#D93829", stroke_w=2.0, roundness_type=3, frame_id=fid)
    s.add_text(400, 105, "INDICE VECTORIAL HNSW (GRAFO MULTICAPA)", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_quad_card(400, 140, 240, 110, "Layer 2 (Coarse)", "Saltos largos de exploracion", badge="TOP LAYER", frame_id=fid)
    s.add_quad_card(680, 140, 240, 110, "Layer 0 (Dense)", "Grafo completo de vecinos", badge="BASE LAYER", frame_id=fid)
    s.add_arrow(640, 195, 680, 195, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(940, 220, 1040, 220, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_database_cylinder(1040, 130, 320, 170, "RocksDB Storage Engine", "Vectores + Metadata JSON en NVMe", frame_id=fid)
    save_and_export(s, fid, cat, 74, "74_vector_db_architecture", "Vector Database Architecture", "high", "vector_index", ["hnsw_layers", "scalar_quantization"])

    # 75. AI Evaluation Pipeline
    s, fid, tw, th = create_base_scene("LLM Evaluation Pipeline (Ragas, Faithfulness, Groundedness & Evals)", "DATA & AI")
    eval_stages = ["1. Dataset de Prueba", "2. Generacion LLM", "3. Metricas Ragas (Fidelidad)", "4. Reporte de Evals"]
    for i, estage in enumerate(eval_stages):
        ex = 40 + i * 345
        s.add_quad_card(ex, 140, 330, 150, estage, f"Fase #{i+1} de evaluacion continua", badge="EVALS", is_hero=(i==2), frame_id=fid)
        if i < 3:
            s.add_arrow(ex + 330, 215, ex + 345, 215, stroke="#D93829" if i==2 else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 75, "75_ai_evaluation_pipeline", "AI Evaluation Pipeline", "high", "eval_pipeline", ["test_dataset", "ragas_metrics", "eval_report"])
