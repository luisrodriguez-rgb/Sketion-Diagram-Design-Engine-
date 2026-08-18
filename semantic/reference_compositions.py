"""
Sketion 30 Archetypal Reference Compositions (v11.0)
Selección curada de 30 composiciones arquetípicas extraídas del ecosistema de 212 plantillas.
Sirve como base de conocimiento estructural para el recuperador semántico de Sketion.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class ReferenceComposition:
    id: str
    name: str
    domain: str
    pattern: str
    layout_type: str
    complexity: str
    keywords: List[str]
    description: str
    sample_nodes: List[str]
    sample_connectors: List[str]


REFERENCE_COMPOSITIONS: List[ReferenceComposition] = [
    # ── 1. SOFTWARE & CLOUD ARCHITECTURE (6) ──────────────────────────────────
    ReferenceComposition(
        "50_security_architecture", "Defense-in-Depth Zero-Trust", "software",
        "security_barrier", "hierarchical", "extreme",
        ["security", "waf", "zero-trust", "mtls", "firewall", "seguridad", "cifrado"],
        "Perímetro defensivo con WAF, Envoy mTLS Gateway, RBAC y DB cifrada.",
        ["User", "Cloudflare WAF", "Envoy Gateway", "Core Service", "Encrypted DB"],
        ["HTTPS/TLS 1.3", "mTLS Mesh", "Zero-Trust", "AES-256"]
    ),
    ReferenceComposition(
        "59_kubernetes_architecture", "Kubernetes Cluster Topology", "software",
        "k8s_topology", "layered", "extreme",
        ["k8s", "kubernetes", "cluster", "pods", "master", "worker", "etcd"],
        "Control Plane con apiserver, scheduler y etcd coordinando Worker Nodes con Pods.",
        ["Control Plane", "etcd", "worker-01 (Pods)", "worker-02 (Pods)"],
        ["gRPC / REST", "Kubelet Agent", "Cluster State"]
    ),
    ReferenceComposition(
        "41_c4_system_context", "C4 System Context Diagram", "software",
        "layered_architecture", "hierarchical", "high",
        ["c4", "context", "banco", "sistema", "usuarios", "externos"],
        "Delimitación de frontera de sistema principal con actores y servicios de terceros.",
        ["Cliente", "Sistema Bancario Core", "Mainframe Legacy", "Notificaciones"],
        ["HTTPS Request", "SNA Link", "REST Webhook"]
    ),
    ReferenceComposition(
        "45_component_architecture", "Hexagonal Ports & Adapters", "software",
        "hexagonal_ports", "hierarchical", "high",
        ["hexagonal", "ports", "adapters", "domain", "clean architecture"],
        "Core de dominio aislado con Inbound Ports y Outbound Adapters para base de datos.",
        ["REST Controller", "Inbound Port", "Domain Core", "Outbound Port", "Hibernate DAO"],
        ["Method Call", "Interface Implementation", "SQL Driver"]
    ),
    ReferenceComposition(
        "46_class_diagram", "UML Class Model with Inheritance", "software",
        "uml_class_model", "hierarchical", "high",
        ["uml", "class", "oop", "herencia", "metodos", "atributos"],
        "Clases de 3 compartimentos con tipado de datos y métodos orientados a objetos.",
        ["UserAccount", "Order", "PaymentTransaction"],
        ["Association 1..*", "Inheritance"]
    ),
    ReferenceComposition(
        "54_cloud_architecture", "Cloud Native Multi-AZ High Availability", "software",
        "layered_architecture", "layered", "high",
        ["cloud", "aws", "multi-az", "availability", "ecs", "aurora", "alb"],
        "DNS Route 53 distribuyendo carga entre AZ-A y AZ-B con réplicas Aurora.",
        ["Route 53", "ALB", "ECS AZ-A", "ECS AZ-B", "Aurora Multi-AZ"],
        ["SSL Termination", "Health Check", "SQL Replication"]
    ),

    # ── 2. DATA, APIS & AI PIPELINES (5) ───────────────────────────────────────
    ReferenceComposition(
        "63_data_pipeline_architecture", "Modern Batch & Streaming Data Pipeline", "data",
        "pipeline_flow", "timeline", "high",
        ["data", "pipeline", "streaming", "kafka", "spark", "lakehouse", "iceberg"],
        "Ingesta de eventos en Kafka con procesamiento Flink/Spark y almacenamiento Iceberg.",
        ["Fuentes IoT", "Kafka Broker", "Spark Streaming", "Iceberg S3 Lakehouse"],
        ["Event Stream", "Avro Schema", "Parquet Ingestion"]
    ),
    ReferenceComposition(
        "65_data_lake_architecture", "Data Lakehouse Medallion Architecture", "data",
        "data_lakehouse", "timeline", "high",
        ["lakehouse", "medallion", "bronze", "silver", "gold", "etl", "dbt"],
        "Flujo en 3 niveles de pureza: Bronze (Raw), Silver (Cleaned) y Gold (Aggregated).",
        ["Bronze Raw JSON", "Silver Cleansed", "Gold Dimensional Mart"],
        ["Raw Ingestion", "Schema Enforcement", "BI Aggregations"]
    ),
    ReferenceComposition(
        "72_multi_agent_system", "Autonomous Multi-Agent Collaborative Hub", "data",
        "radial_hub", "radial", "extreme",
        ["multi-agent", "agents", "ia", "ai", "orchestrator", "researcher", "coder"],
        "Orquestador líder delegando tareas a especialistas (Investigador, Programador, Crítico).",
        ["Lead Orchestrator", "Researcher Agent", "Coder Agent", "Critic Agent"],
        ["Task Delegation", "Result Verification", "Final Synthesis"]
    ),
    ReferenceComposition(
        "74_vector_db_architecture", "Vector Database HNSW Graph Architecture", "data",
        "hierarchical_tree", "hierarchical", "high",
        ["vector", "embeddings", "hnsw", "rag", "similarity", "rocksdb"],
        "Pipeline de embeddings pasando por grafo multicapa HNSW y almacenamiento RocksDB.",
        ["Embedding Engine", "HNSW Layer 2", "HNSW Layer 0", "RocksDB NVMe"],
        ["Dense Vector", "Cosine Traversal", "Storage Write"]
    ),
    ReferenceComposition(
        "69_webhook_architecture", "Resilient Webhook Ingestion with DLQ", "data",
        "pipeline_flow", "timeline", "high",
        ["webhook", "sqs", "dlq", "retry", "idempotency", "resilience"],
        "Receptor con verificación HMAC, cola SQS FIFO, reintentos con DLQ y worker asíncrono.",
        ["Publisher", "Webhook Receiver", "SQS Queue", "Async Worker"],
        ["HMAC Signed HTTP", "Enqueue", "Process Event"]
    ),

    # ── 3. INGENIERÍA & PROCESOS INDUSTRIALES (4) ──────────────────────────────
    ReferenceComposition(
        "22_swimlane_process_map", "Operational Multi-Role Swimlane Map", "engineering",
        "swimlane_process", "swimlane", "high",
        ["swimlane", "procesos", "operaciones", "carriles", "fabricacion", "calidad"],
        "4 carriles funcionales: Planificación, Fabricación, Ensamble y Control de Calidad.",
        ["Planificación", "Fabricación CNC", "Ensamble", "Control Calidad"],
        ["Handover Operativo", "Liberación de Lote"]
    ),
    ReferenceComposition(
        "36_failure_tree_analysis_fta", "Fault Tree Analysis with Logic Gates", "engineering",
        "hierarchical_tree", "tree", "high",
        ["fta", "fault tree", "fallos", "compuertas", "or", "and", "riesgos"],
        "Evento tope superior conectado mediante compuertas booleanas OR/AND a causas raíz.",
        ["Evento Tope", "Compuerta OR", "Fallo Bomba", "Rotura Válvula"],
        ["Propagación de Fallo", "Causa Raíz"]
    ),
    ReferenceComposition(
        "38_a3_problem_solving", "Toyota A3 Continuous Problem Solving Report", "engineering",
        "a3_report", "matrix", "high",
        ["a3", "toyota", "pdca", "problemas", "contramedidas", "kaizen"],
        "Estructura formal de 7 cuadrantes de resolución de problemas según metodología Lean.",
        ["Antecedentes", "Situación Actual", "Causa Raíz", "Contramedidas", "Plan"],
        ["PDCA Flow"]
    ),
    ReferenceComposition(
        "32_control_chart", "Statistical Process Control (SPC X-bar Chart)", "engineering",
        "timeline_roadmap", "timeline", "high",
        ["spc", "control chart", "seis sigma", "lcs", "lci", "variabilidad"],
        "Gráfico con límites estadísticos superior e inferior y muestras de dispersión.",
        ["LCS (+3s)", "Media (mu)", "LCI (-3s)", "Muestras 1..10"],
        ["Tendencia de Control"]
    ),

    # ── 4. NEGOCIOS & ESTRATEGIA (5) ───────────────────────────────────────────
    ReferenceComposition(
        "77_porters_five_forces", "Porter's Five Forces Industry Competitiveness", "business",
        "radial_hub", "radial", "high",
        ["porter", "fuerzas", "competitividad", "estrategia", "mercado"],
        "Rivalidad central rodeada por Entrantes, Proveedores, Compradores y Sustitutos.",
        ["Rivalidad Central", "Entrantes", "Proveedores", "Compradores", "Sustitutos"],
        ["Amenaza Competitiva", "Poder de Negociación"]
    ),
    ReferenceComposition(
        "81_business_strategy_map", "Kaplan-Norton Balanced Scorecard Strategy Map", "business",
        "layered_architecture", "layered", "high",
        ["strategy map", "kaplan", "bsc", "financiera", "clientes", "procesos", "aprendizaje"],
        "4 perspectivas estratégicas enlazadas: Financiera -> Clientes -> Procesos -> Aprendizaje.",
        ["Perspectiva Financiera", "Clientes", "Procesos Internos", "Aprendizaje"],
        ["Causa-Efecto Estratégico"]
    ),
    ReferenceComposition(
        "86_business_ecosystem_map", "Enterprise Multi-Stakeholder Value Network", "business",
        "radial_hub", "radial", "high",
        ["ecosystem", "ecosistema", "partners", "reguladores", "clientes", "empresa"],
        "Empresa Core en el centro conectada con socios, reguladores, nubes y clientes.",
        ["Empresa Core", "Proveedores Cloud", "Partners", "Reguladores", "Clientes"],
        ["Intercambio de Valor", "Cumplimiento"]
    ),
    ReferenceComposition(
        "78_bcg_matrix", "BCG Growth-Share Matrix", "business",
        "matrix_2x2", "matrix", "medium",
        ["bcg", "matriz", "estrellas", "vacas", "interrogantes", "perros"],
        "4 cuadrantes de cartera evaluando crecimiento de mercado vs cuota relativa.",
        ["Estrellas", "Interrogantes", "Vacas Lecheras", "Perros"],
        ["Asignación de Capital"]
    ),
    ReferenceComposition(
        "83_strategy_to_execution_map", "Strategy-to-Execution Cascading Framework", "business",
        "pipeline_flow", "timeline", "high",
        ["ejecucion", "cascada", "vision", "objetivos", "iniciativas", "proyectos", "kpis"],
        "5 niveles de cascada: Visión -> Objetivos -> Iniciativas -> Proyectos -> KPIs.",
        ["Visión", "Objetivos", "Iniciativas", "Proyectos", "KPIs"],
        ["Alineación Estratégica"]
    ),

    # ── 5. PRODUCTO & UX RESEARCH (5) ──────────────────────────────────────────
    ReferenceComposition(
        "107_service_blueprint", "Multilayered Service Blueprint", "ux",
        "service_blueprint", "swimlane", "extreme",
        ["service blueprint", "blueprint", "frontstage", "backstage", "touchpoints"],
        "4 niveles de interacción: Evidencia Física -> Cliente -> Frontstage -> Backstage.",
        ["Evidencia Física", "Acciones Cliente", "Frontstage", "Backstage Soporte"],
        ["Línea de Interacción", "Línea de Visibilidad", "Línea de Soporte"]
    ),
    ReferenceComposition(
        "94_user_story_map", "User Story Mapping by Backbone & Releases", "ux",
        "layered_architecture", "layered", "high",
        ["story map", "backbone", "releases", "mvp", "historias", "epicas"],
        "Backbone horizontal superior con desglose en Release 1 (MVP) y Release 2.",
        ["Backbone Activities", "Release 1 (MVP)", "Release 2 (Enhancements)"],
        ["Priorización de Entrega"]
    ),
    ReferenceComposition(
        "105_north_star_metric", "North Star Metric & Value Drivers Framework", "ux",
        "hierarchical_tree", "tree", "high",
        ["north star", "nsm", "metrica guia", "drivers", "palancas", "retencion"],
        "Métrica estrella superior soportada por palancas de Amplitud, Profundidad y Frecuencia.",
        ["North Star Metric", "Palanca 1: Cobertura", "Palanca 2: Calidad", "Palanca 3: Retención"],
        ["Impacto en Métrica"]
    ),
    ReferenceComposition(
        "108_experience_map", "Holistic Customer Journey & Experience Map", "ux",
        "pipeline_flow", "timeline", "high",
        ["experience map", "journey", "touchpoints", "emocion", "fases"],
        "Fases secuenciales de viaje del usuario con puntos de contacto y curva emocional.",
        ["Descubrimiento", "Evaluación", "Uso Activo", "Fidelización"],
        ["Transición de Experiencia"]
    ),
    ReferenceComposition(
        "120_user_mental_model", "User Mental Model vs System Conceptual Model", "ux",
        "dual_split", "hierarchical", "high",
        ["mental model", "modelo mental", "sistema", "venn", "desalineacion"],
        "Diagrama de Venn bilateral comparando expectativas del usuario vs arquitectura real.",
        ["Modelo Mental Usuario", "Modelo Real Sistema", "Zona de Alineación"],
        ["Intersección Conceptual"]
    ),

    # ── 6. ESTUDIO & PRODUCTIVIDAD (5) ─────────────────────────────────────────
    ReferenceComposition(
        "08_argument_map", "Hierarchical Argumentation & Premise Tree", "education",
        "hierarchical_tree", "tree", "medium",
        ["argumento", "tesis", "premisas", "evidencias", "debate"],
        "Tesis principal superior sustentada por premisas lógicas y datos probatorios.",
        ["Conclusión Principal", "Premisa 1 (Evidencia)", "Premisa 2 (Estudio)"],
        ["Sustentación Lógica"]
    ),
    ReferenceComposition(
        "17_learning_progress_tracker", "Competency & Skill Radar Spider", "education",
        "radar_spider", "radial", "high",
        ["radar", "spider", "competencias", "evaluacion", "progreso"],
        "Radar polar con 6 ejes de maestría técnica y polígono de evaluación.",
        ["Algoritmos", "Sistemas", "Bases de Datos", "Redes", "Seguridad", "DevOps"],
        ["Nivel de Dominio"]
    ),
    ReferenceComposition(
        "131_agile_release_train", "SAFe Agile Release Train & PI Cadence", "agile",
        "timeline_roadmap", "timeline", "high",
        ["safe", "art", "release train", "pi", "sprints", "cadencia"],
        "Cadencia de Program Increment (PI) dividida en 4 Sprints con demo y retrospectiva.",
        ["PI Objective", "Sprint 1", "Sprint 2", "Sprint 3", "Sprint 4 (Demo)"],
        ["Cadencia de Entrega"]
    ),
    ReferenceComposition(
        "140_raci_matrix", "RACI Responsibility Assignment Matrix", "agile",
        "matrix_2x2", "matrix", "high",
        ["raci", "roles", "responsabilidad", "accountable", "consulted", "informed"],
        "Matriz tabular relacionando entregables de proyecto con roles clave.",
        ["Tareas / Entregables", "Product Manager", "Lead Architect", "Engineer", "QA"],
        ["Código R/A/C/I"]
    ),
    ReferenceComposition(
        "150_personal_dashboard", "Executive 4-Quadrant Focus Dashboard", "education",
        "matrix_2x2", "matrix", "high",
        ["dashboard", "productividad", "habitos", "foco", "metricas"],
        "4 cuadrantes de gestión ejecutiva: Foco Diario, Hábitos, Proyectos y Métricas.",
        ["Foco Diario", "Hábitos & Disciplina", "Proyectos Activos", "Métricas"],
        ["Seguimiento de Alto Rendimiento"]
    )
]
