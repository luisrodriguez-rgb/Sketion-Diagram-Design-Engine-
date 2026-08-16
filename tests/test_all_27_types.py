"""
Sketion 4.0 — Master Test Suite: Verificación Exhaustiva de los 27 Tipos Visuales
Genera y audita automáticamente un diagrama de prueba para cada uno de los 27 tipos visuales
en la carpeta PRUEBAS_27_TYPES/
"""

import os
import sys
import json

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from validation.validator import validate_scene
from engines.catalog import VISUAL_TYPES_CATALOG, list_all_visual_types

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_27_TYPES")
os.makedirs(OUT_DIR, exist_ok=True)


def build_all_27_scenes() -> list:
    results = []
    
    # 1. Medallion
    place_reset()
    s1 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    stages = [
        {"name": "1. RAW / INGEST", "desc": "Landing Zone (JSON/CSV)", "items": ["POS Stream (Kafka)", "Webhooks Pagos", "Logs Servidor"]},
        {"name": "2. BRONZE / DEDUPE", "desc": "Delta Lake Inmutable", "items": ["Schema Validation", "Deduplicacion", "Particion por Fecha"]},
        {"name": "3. SILVER / CLEAN", "desc": "Marts Normalizados", "items": ["Limpieza de Nulos", "Enriquecimiento", "Joins Transaccionales"]},
        {"name": "4. GOLD / AGGREGATE", "desc": "Feature Store & BI", "items": ["Metricas Financieras", "Customer Lifetime Value", "Modelos ML"], "is_gold": True}
    ]
    fn1 = VISUAL_TYPES_CATALOG["medallion"]["render_fn"]
    fn1(s1, "Arquitectura Lakehouse E-Commerce", stages, x, y)
    p1 = os.path.join(OUT_DIR, "01_medallion.excalidraw")
    s1.save(p1)
    _, r1 = validate_scene(p1)
    results.append({"type": "medallion", "file": p1, "score": r1.sketion_overall_score})

    # 2. Data Flow
    place_reset()
    s2 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    roles = ["Data Engineer", "Data Scientist", "BI Analyst"]
    stages_df = ["1. Ingest", "2. Store", "3. Transform", "4. Model & Predict", "5. Publish"]
    tasks_df = [
        {"role_idx": 0, "stage_idx": 0, "label": "Kafka Event Pipeline"},
        {"role_idx": 0, "stage_idx": 1, "label": "Parquet S3 Raw Storage"},
        {"role_idx": 0, "stage_idx": 2, "label": "dbt Silver Clean Transformations"},
        {"role_idx": 1, "stage_idx": 3, "label": "MLflow Feature Training", "is_hero": True},
        {"role_idx": 2, "stage_idx": 4, "label": "Tableau / Looker KPI Dashboard"}
    ]
    fn2 = VISUAL_TYPES_CATALOG["data_flow"]["render_fn"]
    fn2(s2, "Pipeline Analitico por Roles de Datos", roles, stages_df, tasks_df, x, y)
    p2 = os.path.join(OUT_DIR, "02_data_flow.excalidraw")
    s2.save(p2)
    _, r2 = validate_scene(p2)
    results.append({"type": "data_flow", "file": p2, "score": r2.sketion_overall_score})

    # 3. DP Integration
    place_reset()
    s3 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    sources = ["POS Database (Postgres)", "Clickstream (Kafka)", "CRM API (Salesforce)"]
    core = ["Apache Iceberg Storage", "Trino Query Engine", "Airflow Orchestrator"]
    consumers = ["BI Dashboards", "Data Science Notebooks", "Reverse ETL to Marketing"]
    fn3 = VISUAL_TYPES_CATALOG["dp_integration"]["render_fn"]
    fn3(s3, "Topologia de Integracion de Plataforma de Datos", sources, core, consumers, x, y)
    p3 = os.path.join(OUT_DIR, "03_dp_integration.excalidraw")
    s3.save(p3)
    _, r3 = validate_scene(p3)
    results.append({"type": "dp_integration", "file": p3, "score": r3.sketion_overall_score})

    # 4. DP Security Matrix
    place_reset()
    s4 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    sec_roles = ["Data Engineer", "Data Scientist", "Business Analyst", "Admin", "Partner"]
    comps = ["Object Storage S3", "Query Engine (SQL)", "Jupyter Hub", "BI Reporting", "Airflow DAGs"]
    mat_data = [
        ["Write", "Read", "None", "Admin", "None"],
        ["Write", "Read", "Read", "Admin", "Read"],
        ["Write", "Write", "None", "Admin", "None"],
        ["Write", "Read", "Write", "Admin", "Read"],
        ["Write", "Read", "None", "Admin", "None"]
    ]
    fn4 = VISUAL_TYPES_CATALOG["dp_security_matrix"]["render_fn"]
    fn4(s4, "Matriz de Permisos y Control de Acceso RBAC", sec_roles, comps, mat_data, x, y)
    p4 = os.path.join(OUT_DIR, "04_dp_security_matrix.excalidraw")
    s4.save(p4)
    _, r4 = validate_scene(p4)
    results.append({"type": "dp_security_matrix", "file": p4, "score": r4.sketion_overall_score})

    # 5. ER Model
    place_reset()
    s5 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    entities = [
        {"id": "users", "name": "Users", "fields": ["PK id: uuid", "name: varchar", "email: varchar", "created_at: timestamp"]},
        {"id": "orders", "name": "Orders", "fields": ["PK id: uuid", "FK user_id: uuid", "amount: decimal", "status: varchar"]},
        {"id": "items", "name": "OrderItems", "fields": ["PK id: uuid", "FK order_id: uuid", "product_id: uuid", "qty: int"]},
        {"id": "payments", "name": "Payments", "fields": ["PK id: uuid", "FK order_id: uuid", "provider: varchar", "status: varchar"]}
    ]
    relations = [
        ("users", "orders", "1 : N"),
        ("orders", "items", "1 : N"),
        ("orders", "payments", "1 : 1")
    ]
    fn5 = VISUAL_TYPES_CATALOG["er_model"]["render_fn"]
    fn5(s5, "Modelo de Datos Relacional de E-Commerce", entities, relations, x, y)
    p5 = os.path.join(OUT_DIR, "05_er_model.excalidraw")
    s5.save(p5)
    _, r5 = validate_scene(p5)
    results.append({"type": "er_model", "file": p5, "score": r5.sketion_overall_score})

    # 6. Consultant 2x2
    place_reset()
    s6 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    quads = [
        {"name": "Quick Wins (Bajo Esfuerzo / Alto Impacto)", "desc": "Ejecucion Inmediata", "items": ["Separar Order/Pickup", "Batching previo de 80 sandwiches"], "is_hero": True},
        {"name": "Major Projects (Alto Esfuerzo / Alto Impacto)", "desc": "Planificacion Estrategica", "items": ["App Pre-Order con Casilleros QR", "Migracion Cloud"]},
        {"name": "Fill-ins (Bajo Esfuerzo / Bajo Impacto)", "desc": "Tareas Secundarias", "items": ["Actualizar logo en menu", "Cambio de uniformes"]},
        {"name": "Thankless Tasks (Alto Esfuerzo / Bajo Impacto)", "desc": "Evitar o Descartar", "items": ["Ampliacion de cocina con obra mayor"]}
    ]
    fn6 = VISUAL_TYPES_CATALOG["consultant_2x2"]["render_fn"]
    fn6(s6, "Matriz de Priorizacion Estrategica de Iniciativas", "Esfuerzo de Implementacion", "Impacto en Negocio", quads, x, y)
    p6 = os.path.join(OUT_DIR, "06_consultant_2x2.excalidraw")
    s6.save(p6)
    _, r6 = validate_scene(p6)
    results.append({"type": "consultant_2x2", "file": p6, "score": r6.sketion_overall_score})

    # 7. Quadrant
    place_reset()
    s7 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    pts_q = [
        {"x_val": 0.2, "y_val": 0.8, "label": "Quick Win A", "is_hero": True},
        {"x_val": 0.8, "y_val": 0.85, "label": "Major Strategic Core"},
        {"x_val": 0.15, "y_val": 0.2, "label": "Low-Priority Task"},
        {"x_val": 0.75, "y_val": 0.3, "label": "High-Effort Burden"}
    ]
    fn7 = VISUAL_TYPES_CATALOG["quadrant"]["render_fn"]
    fn7(s7, "Posicionamiento de Iniciativas en Cuadrante", "Esfuerzo", "Impacto", pts_q, x, y)
    p7 = os.path.join(OUT_DIR, "07_quadrant.excalidraw")
    s7.save(p7)
    _, r7 = validate_scene(p7)
    results.append({"type": "quadrant", "file": p7, "score": r7.sketion_overall_score})

    # 8. Loop Flywheel
    place_reset()
    s8 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    stations = [
        {"title": "1. Captura de Datos", "sub": "Interacciones en App"},
        {"title": "2. Entrenamiento ML", "sub": "Optimizacion Continua", "is_hero": True},
        {"title": "3. Recomendacion", "sub": "Personalizacion en UI"},
        {"title": "4. Conversion & Retencion", "sub": "Mayor LTV"}
    ]
    fn8 = VISUAL_TYPES_CATALOG["loop_flywheel"]["render_fn"]
    fn8(s8, "Flywheel de Personalizacion Continua con IA", "Shared Memory Core", stations, x, y)
    p8 = os.path.join(OUT_DIR, "08_loop_flywheel.excalidraw")
    s8.save(p8)
    _, r8 = validate_scene(p8)
    results.append({"type": "loop_flywheel", "file": p8, "score": r8.sketion_overall_score})

    # 9. IT Current-State
    place_reset()
    s9 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    fn9 = VISUAL_TYPES_CATALOG["it_current_state"]["render_fn"]
    fn9(s9, "Modernizacion de Arquitectura Retail Legacy",
        ["Servidores On-Premise 2012", "Hojas Excel Compartidas", "Scripts Nocturnos Batch"],
        ["Silos de datos sin sincronizacion", "Caidas en picos de venta", "Costos de mantenimiento altos"],
        ["Plataforma Cloud Nativa", "Streaming Kafka en Tiempo Real", "Base de Datos Distribuida"],
        x, y)
    p9 = os.path.join(OUT_DIR, "09_it_current_state.excalidraw")
    s9.save(p9)
    _, r9 = validate_scene(p9)
    results.append({"type": "it_current_state", "file": p9, "score": r9.sketion_overall_score})

    # 10. Venn
    place_reset()
    s10 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    fn10 = VISUAL_TYPES_CATALOG["venn"]["render_fn"]
    fn10(s10, "Diseno de Producto: Deseable x Factible x Viable",
         [{"name": "Deseable (Usuarios)"}, {"name": "Factible (Tecnologia)"}, {"name": "Viable (Negocio)"}],
         "SWEET SPOT DE PRODUCTO", x, y)
    p10 = os.path.join(OUT_DIR, "10_venn.excalidraw")
    s10.save(p10)
    _, r10 = validate_scene(p10)
    results.append({"type": "venn", "file": p10, "score": r10.sketion_overall_score})

    # 11. Pyramid / Funnel
    place_reset()
    s11 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    tiers = [
        {"name": "1. Visitantes Web (Top of Funnel)", "stat": "100,000 usuarios / mes (100%)"},
        {"name": "2. Usuarios Registrados", "stat": "25,000 usuarios (25%)"},
        {"name": "3. Checkout Iniciado", "stat": "8,500 carritos (8.5%)"},
        {"name": "4. Clientes Pagos (Retencion)", "stat": "3,400 clientes (3.4% Conversion)"}
    ]
    fn11 = VISUAL_TYPES_CATALOG["pyramid_funnel"]["render_fn"]
    fn11(s11, "Embudo de Conversion E-Commerce", tiers, x, y)
    p11 = os.path.join(OUT_DIR, "11_pyramid_funnel.excalidraw")
    s11.save(p11)
    _, r11 = validate_scene(p11)
    results.append({"type": "pyramid_funnel", "file": p11, "score": r11.sketion_overall_score})

    # 12. Architecture
    place_reset()
    s12 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    scopes_arch = [
        {"title": "1. Ingress Edge", "nodes": [{"id": "gw", "title": "Envoy Gateway", "sub": "TLS & Auth"}, {"id": "waf", "title": "Cloudflare WAF", "sub": "DDoS Shield"}]},
        {"title": "2. Microservicios Core", "nodes": [{"id": "order", "title": "Order Service", "sub": "gRPC API", "is_hero": True}, {"id": "pay", "title": "Payment Service", "sub": "Idempotency"}]},
        {"title": "3. Persistencia", "nodes": [{"id": "db", "title": "PostgreSQL Cluster", "sub": "Multi-AZ"}, {"id": "cache", "title": "Redis Cache", "sub": "Sub-ms Latency"}]}
    ]
    conns_arch = [("gw", "order", "Dispatch"), ("order", "pay", "Process"), ("order", "db", "SQL Store")]
    fn12 = VISUAL_TYPES_CATALOG["architecture"]["render_fn"]
    fn12(s12, "Arquitectura de Microservicios en Kubernetes", scopes_arch, conns_arch, x, y)
    p12 = os.path.join(OUT_DIR, "12_architecture.excalidraw")
    s12.save(p12)
    _, r12 = validate_scene(p12)
    results.append({"type": "architecture", "file": p12, "score": r12.sketion_overall_score})

    # 13. High-Level
    place_reset()
    s13 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    cluster_l = [
        {"title": "Presentation Layer", "items": ["Next.js SSR App", "Mobile Flutter", "Admin Portal"]},
        {"title": "Application Core", "items": ["GraphQL Gateway", "Event Broker Kafka", "Auth Server"]},
        {"title": "Data Storage", "items": ["MongoDB Atlas", "Elasticsearch Cluster", "S3 Storage"]}
    ]
    fn13 = VISUAL_TYPES_CATALOG["high_level"]["render_fn"]
    fn13(s13, "Topologia Global de Aplicacion Empresarial", "Kubernetes Multi-Region Cluster Orchestrator", cluster_l, x, y)
    p13 = os.path.join(OUT_DIR, "13_high_level.excalidraw")
    s13.save(p13)
    _, r13 = validate_scene(p13)
    results.append({"type": "high_level", "file": p13, "score": r13.sketion_overall_score})

    # 14. Sequence
    place_reset()
    s14 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    seq_actors = ["Cliente Web", "API Gateway", "Auth Service", "Order Service", "Payment Gateway"]
    seq_msgs = [
        (0, 1, "POST /orders", False),
        (1, 2, "Verify JWT Token", False),
        (2, 1, "Token Valid 200", True),
        (1, 3, "Create Order", False),
        (3, 4, "Charge Credit Card", False),
        (4, 3, "Payment Approved", True),
        (3, 0, "Order Confirmed 201", True)
    ]
    fn14 = VISUAL_TYPES_CATALOG["sequence"]["render_fn"]
    fn14(s14, "Secuencia Temporal de Checkout y Pago", seq_actors, seq_msgs, x, y)
    p14 = os.path.join(OUT_DIR, "14_sequence.excalidraw")
    s14.save(p14)
    _, r14 = validate_scene(p14)
    results.append({"type": "sequence", "file": p14, "score": r14.sketion_overall_score})

    # 15. State Machine
    place_reset()
    s15 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    states_sm = [
        {"id": "draft", "name": "Draft", "desc": "Edicion inicial"},
        {"id": "review", "name": "In Review", "desc": "Revision editorial"},
        {"id": "published", "name": "Published", "desc": "Visible en produccion", "is_hero": True},
        {"id": "archived", "name": "Archived", "desc": "Solo lectura", "is_final": True}
    ]
    trans_sm = [
        ("draft", "review", "Submit PR"),
        ("review", "published", "Approve & Merge"),
        ("published", "archived", "Deprecate")
    ]
    fn15 = VISUAL_TYPES_CATALOG["state_machine"]["render_fn"]
    fn15(s15, "Ciclo de Vida de Publicacion de Contenido", states_sm, trans_sm, x, y)
    p15 = os.path.join(OUT_DIR, "15_state_machine.excalidraw")
    s15.save(p15)
    _, r15 = validate_scene(p15)
    results.append({"type": "state_machine", "file": p15, "score": r15.sketion_overall_score})

    # 16. Layer Stack
    place_reset()
    s16 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    layers_s = [
        {"name": "UI Surface & Components", "sub": "React, Tailwind, Web Components"},
        {"name": "Agent Harness & Orchestrator", "sub": "Antigravity Runtime & Tools", "is_hero": True},
        {"name": "Prompt & Semantic Layer", "sub": "Templates, Constraints, Memory"},
        {"name": "SDK & Transport Client", "sub": "gRPC, REST, WebSocket"},
        {"name": "Model Weights & Inference", "sub": "Foundation LLM Engine"}
    ]
    fn16 = VISUAL_TYPES_CATALOG["layer_stack"]["render_fn"]
    fn16(s16, "Stack Tecnologico de Aplicacion de IA Agente", layers_s, x, y)
    p16 = os.path.join(OUT_DIR, "16_layer_stack.excalidraw")
    s16.save(p16)
    _, r16 = validate_scene(p16)
    results.append({"type": "layer_stack", "file": p16, "score": r16.sketion_overall_score})

    # 17. Nested
    place_reset()
    s17 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    fn17 = VISUAL_TYPES_CATALOG["nested"]["render_fn"]
    fn17(s17, "Jerarquia de Configuracion de Reglas y Skills",
         "1. Global Workspace Boundary", "2. Project Specific Skill Directory", "3. Core Agent Context (SKILL.md)",
         x, y)
    p17 = os.path.join(OUT_DIR, "17_nested.excalidraw")
    s17.save(p17)
    _, r17 = validate_scene(p17)
    results.append({"type": "nested", "file": p17, "score": r17.sketion_overall_score})

    # 18. Flowchart
    place_reset()
    s18 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    nodes_fc = [
        {"text": "1. Identificar Flujo Repetitivo"},
        {"text": "2. ¿Se ejecuta > 3 veces?", "is_decision": True},
        {"text": "3. Crear Skill Estandarizada"},
        {"text": "4. Documentar en README"}
    ]
    branches_fc = [(0, 1, "Evaluar"), (1, 2, "SI"), (2, 3, "Finalizar")]
    fn18 = VISUAL_TYPES_CATALOG["flowchart"]["render_fn"]
    fn18(s18, "Arbol de Decision para Creacion de Skills", nodes_fc, branches_fc, x, y)
    p18 = os.path.join(OUT_DIR, "18_flowchart.excalidraw")
    s18.save(p18)
    _, r18 = validate_scene(p18)
    results.append({"type": "flowchart", "file": p18, "score": r18.sketion_overall_score})

    # 19. Swimlane
    place_reset()
    s19 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    lanes_sw = [
        {"name": "Customer", "steps": ["Selecciona Productos en App", "Realiza Pago Online", "Recibe Notificacion Push"]},
        {"name": "Kitchen", "steps": ["Recibe Comanda KDS", "Prepara Pedido en 4 min", "Marca Pedido Listo"]},
        {"name": "Runner", "steps": ["Recoge Plato de Cocina", "Carga Locker Express", "Verifica Entrega"]}
    ]
    fn19 = VISUAL_TYPES_CATALOG["swimlane"]["render_fn"]
    fn19(s19, "Flujo Operativo de Cafeteria por Roles", lanes_sw, x, y)
    p19 = os.path.join(OUT_DIR, "19_swimlane.excalidraw")
    s19.save(p19)
    _, r19 = validate_scene(p19)
    results.append({"type": "swimlane", "file": p19, "score": r19.sketion_overall_score})

    # 20. Process
    place_reset()
    s20 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    steps_pr = [
        {"num": "01", "title": "Solicitud de Credito", "actor": "Cliente"},
        {"num": "02", "title": "Scoring de Riesgo", "actor": "Motor ML", "is_hero": True},
        {"num": "03", "title": "Revision Compliance", "actor": "Oficial de Riesgos"},
        {"num": "04", "title": "Desembolso Inmediato", "actor": "Core Bancario"}
    ]
    fn20 = VISUAL_TYPES_CATALOG["process"]["render_fn"]
    fn20(s20, "Proceso de Originacion de Credito Digital", steps_pr, x, y)
    p20 = os.path.join(OUT_DIR, "20_process.excalidraw")
    s20.save(p20)
    _, r20 = validate_scene(p20)
    results.append({"type": "process", "file": p20, "score": r20.sketion_overall_score})

    # 21. Gantt
    place_reset()
    s21 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    months = ["Mes 1", "Mes 2", "Mes 3", "Mes 4", "Mes 5", "Mes 6"]
    tasks_g = [
        {"name": "Research & Discovery", "start_month": 0.0, "duration": 1.5},
        {"name": "Arquitectura & MVP", "start_month": 1.0, "duration": 2.0},
        {"name": "Gate de Seguridad SOC2", "start_month": 3.0, "duration": 0.5, "is_gate": True},
        {"name": "Beta Privada Clientes", "start_month": 3.5, "duration": 1.5},
        {"name": "Lanzamiento Global", "start_month": 5.0, "duration": 1.0}
    ]
    fn21 = VISUAL_TYPES_CATALOG["gantt"]["render_fn"]
    fn21(s21, "Cronograma Gantt de Lanzamiento de Plataforma", months, tasks_g, x, y)
    p21 = os.path.join(OUT_DIR, "21_gantt.excalidraw")
    s21.save(p21)
    _, r21 = validate_scene(p21)
    results.append({"type": "gantt", "file": p21, "score": r21.sketion_overall_score})

    # 22. Timeline
    place_reset()
    s22 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    milestones_t = [
        {"date": "Q1 2026", "title": "Lanzamiento Sketion 1.0"},
        {"date": "Q2 2026", "title": "20 Arquetipos de Negocio"},
        {"date": "Q3 2026", "title": "Motor de Audiencia y Auto-Split"},
        {"date": "Q4 2026", "title": "27 Tipos Visuales Completos"}
    ]
    fn22 = VISUAL_TYPES_CATALOG["timeline"]["render_fn"]
    fn22(s22, "Hoja de Ruta de Evolucion del Producto", milestones_t, x, y)
    p22 = os.path.join(OUT_DIR, "22_timeline.excalidraw")
    s22.save(p22)
    _, r22 = validate_scene(p22)
    results.append({"type": "timeline", "file": p22, "score": r22.sketion_overall_score})

    # 23. Org Chart
    place_reset()
    s23 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    leader = {"name": "Chief Technology Officer", "role": "Liderazgo de Ingenieria"}
    deps = [
        {"name": "Data Platform", "members": ["Lead Data Eng", "ML Engineer", "BI Lead"]},
        {"name": "Core Backend", "members": ["Staff Engineer", "Distributed Systems", "Security Specialist"]},
        {"name": "Product & UX", "members": ["Lead Designer", "Frontend Architect", "Product Manager"]}
    ]
    fn23 = VISUAL_TYPES_CATALOG["org_chart"]["render_fn"]
    fn23(s23, "Organigrama de la Division de Tecnologia", leader, deps, x, y)
    p23 = os.path.join(OUT_DIR, "23_org_chart.excalidraw")
    s23.save(p23)
    _, r23 = validate_scene(p23)
    results.append({"type": "org_chart", "file": p23, "score": r23.sketion_overall_score})

    # 24. Tree
    place_reset()
    s24 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    branches_tr = [
        {"name": "Sistemas de Almacenamiento", "subitems": ["Relacional (Postgres)", "Documental (Mongo)", "Vectorial (Pinecone)"]},
        {"name": "Capa de Mensajeria", "subitems": ["Streaming (Kafka)", "Colas FIFO (RabbitMQ)", "PubSub Redis"]},
        {"name": "Capa de Computo", "subitems": ["Kubernetes EKS", "Serverless Lambda", "Edge Cloudflare"]}
    ]
    fn24 = VISUAL_TYPES_CATALOG["tree"]["render_fn"]
    fn24(s24, "Taxonomia de Componentes de Infraestructura Cloud", "Cloud Infrastructure", branches_tr, x, y)
    p24 = os.path.join(OUT_DIR, "24_tree.excalidraw")
    s24.save(p24)
    _, r24 = validate_scene(p24)
    results.append({"type": "tree", "file": p24, "score": r24.sketion_overall_score})

    # 25. Bar Chart
    place_reset()
    s25 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    fn25 = VISUAL_TYPES_CATALOG["bar_chart"]["render_fn"]
    fn25(s25, "Throughput de Transacciones por Segundo (TPS)",
         ["Monolito Legacy", "Microservicios v1", "Sketion v4 Engine", "Async Kafka Buffer"],
         [180.0, 320.0, 850.0, 620.0], hero_idx=2, x=x, y=y)
    p25 = os.path.join(OUT_DIR, "25_bar_chart.excalidraw")
    s25.save(p25)
    _, r25 = validate_scene(p25)
    results.append({"type": "bar_chart", "file": p25, "score": r25.sketion_overall_score})

    # 26. Line Chart
    place_reset()
    s26 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    fn26 = VISUAL_TYPES_CATALOG["line_chart"]["render_fn"]
    fn26(s26, "Evolucion de Latencia P99 (ms) vs Carga de Usuarios",
         ["100 req/s", "500 req/s", "1k req/s", "5k req/s", "10k req/s"],
         [
             {"values": [25.0, 32.0, 45.0, 78.0, 95.0], "color": "#0C0C0C"},
             {"values": [12.0, 14.0, 18.0, 24.0, 28.0], "color": "#E03A2F", "is_hero": True}
         ], x=x, y=y)
    p26 = os.path.join(OUT_DIR, "26_line_chart.excalidraw")
    s26.save(p26)
    _, r26 = validate_scene(p26)
    results.append({"type": "line_chart", "file": p26, "score": r26.sketion_overall_score})

    # 27. Scatter Plot
    place_reset()
    s27 = ExcalidrawScene(roughness=0, bg_color="#F4F4F4")
    x, y = place(2800, 850)
    fn27 = VISUAL_TYPES_CATALOG["scatter_plot"]["render_fn"]
    fn27(s27, "Correlacion entre Tamano de Cache y Tasa de Hits",
         [(0.15, 0.25, "512MB"), (0.35, 0.55, "1GB"), (0.6, 0.78, "2GB"), (0.85, 0.94, "4GB (Optimo)")],
         "Tamano de Memoria Cache", "Hit Rate (%)", x=x, y=y)
    p27 = os.path.join(OUT_DIR, "27_scatter_plot.excalidraw")
    s27.save(p27)
    _, r27 = validate_scene(p27)
    results.append({"type": "scatter_plot", "file": p27, "score": r27.sketion_overall_score})

    return results


def main():
    print("==================================================================")
    print("SKETION 4.0 — VERIFICACIÓN EXHAUSTIVA DE LOS 27 TIPOS VISUALES")
    print("==================================================================")
    
    results = build_all_27_scenes()
    
    print("\n| # | Tipo Visual | Archivo Excalidraw | Calidad Sketion | Estado |")
    print("|---|---|---|---|---|")
    all_passed = True
    for i, res in enumerate(results):
        score = res["score"]
        status = "PASS" if score >= 90 else "FAIL"
        if score < 90:
            all_passed = False
        fname = os.path.basename(res["file"])
        print(f"| {i+1:02d} | `{res['type']}` | `{fname}` | **{score}/100** | {status} |")

    report_path = os.path.join(workspace_dir, "PRUEBAS_27_TYPES", "reporte_27_tipos.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
        
    print("==================================================================")
    if all_passed:
        print(f"LOS 27 TIPOS VISUALES PASARON CON ÉXITO (>=90/100). Reporte: {report_path}")
    else:
        print("ALGUNOS TIPOS REQUIEREN AJUSTE.")
    print("==================================================================")


if __name__ == "__main__":
    main()
