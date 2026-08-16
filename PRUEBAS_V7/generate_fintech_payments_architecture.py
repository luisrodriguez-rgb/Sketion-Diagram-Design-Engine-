"""
Sketion 8.0 — Generador Oficial: Arquitectura Visual de Plataforma de Pagos Fintech
Diseñado para equipo mixto: Producto, Ingeniería y Dirección.
Multi-Frame de 3 Capas Especializadas con Arquetipos Diversificados:
- Marco 1 (Y = 0): Arquetipo P (Pipeline de Valor & Macro-Flow Ejecutivo para Dirección y Producto)
- Marco 2 (Y = 1150): Arquetipo Layer Stack & Topology (Microservicios, Kafka, Redis y PostgreSQL para Ingeniería)
- Marco 3 (Y = 2300): Arquetipo E (Swimlanes de Resiliencia, Tokenizer PCI-DSS, DLQ y Conciliación Nocturna)
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from validation.validator import validate_scene

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V7")
os.makedirs(OUT_DIR, exist_ok=True)

PALETTE = {
    "CANVAS": "#F8FAFC",
    "CARD": "#FFFFFF",
    "CARD_BORDER": "#CBD5E1",
    "INK": "#0F172A",
    "MUTED": "#64748B",
    "BLUE_HERO": "#2563EB",
    "BLUE_BG": "#EFF6FF",
    "BLUE_BORDER": "#93C5FD",
    "GREEN_HERO": "#059669",
    "GREEN_BG": "#F0FDF4",
    "GREEN_BORDER": "#86EFAC",
    "CORAL_HERO": "#D93829",
    "CORAL_BG": "#FFF5F2",
    "CORAL_BORDER": "#FCA5A5",
    "SLATE_BG": "#F1F5F9",
    "SLATE_BORDER": "#CBD5E1",
    "INDIGO_BG": "#EEF2FF",
    "INDIGO_BORDER": "#C7D2FE",
    "AMBER_BG": "#FEF3C7",
    "AMBER_BORDER": "#FCD34D",
    "STICKY": "#FFE95C"
}


def build_fintech_payments_board():
    # 3 Marcos de 2950px de ancho apilados verticalmente con 150px de separación
    place_reset(max_row_w=3200, gap=150)
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])

    fw = 2950.0
    fh = 1000.0
    sc_h = 760.0

    # ═══════════════════════════════════════════════════════════════════════════
    # MARCO 1: VISTA EJECUTIVA & MACRO-PIPELINE (DIRECCIÓN & PRODUCTO) (Y = 0)
    # ═══════════════════════════════════════════════════════════════════════════
    f1_x, f1_y = place(fw, fh)
    fid1 = scene.add_frame("FRAME 1: VISTA EJECUTIVA — PIPELINE DE CONVERSIÓN, CANALES & GOBERNANZA", f1_x, f1_y, fw, fh)

    scene.add_text(f1_x + 60.0, f1_y + 35.0, "FINTECH PAYMENT PLATFORM  ·  EXECUTIVE & PRODUCT ARCHITECTURE", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "Flujo de Conversión End-to-End: Canales, Orquestación de Pagos y SLAs de Alta Disponibilidad", font_size=26, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    sc1_y = f1_y + 115.0

    # Scope 1: Canales & Ingress de Clientes
    sc1_w = 830.0
    sc1_x = f1_x + 60.0
    scene.add_scope_container(sc1_x, sc1_y, sc1_w, sc_h, label="1. CANALES DE ADQUISICIÓN & EXPERIENCIA DE CHECKOUT", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

    scene.add_quad_card(sc1_x + 25.0, sc1_y + 45.0, (sc1_w - 65.0) * 0.5, 145.0,
                        "Web Checkout Client",
                        sublabel="React / Next.js SPA.\nTokenización en browser.\nSoporte 3D Secure 2.0.",
                        badge="CANAL WEB", icon="laptop", font_size=15, frame_id=fid1)

    scene.add_quad_card(sc1_x + 25.0 + (sc1_w - 65.0) * 0.5 + 15.0, sc1_y + 45.0, (sc1_w - 65.0) * 0.5, 145.0,
                        "Mobile App & SDK",
                        sublabel="iOS / Android nativo.\nBiometría FaceID / TouchID.\nApple Pay & Google Pay.",
                        badge="MOBILE SDK", icon="laptop", font_size=15, frame_id=fid1)

    scene.add_feature_card(sc1_x + 25.0, sc1_y + 205.0, sc1_w - 50.0, 180.0,
                           "Métricas de Experiencia y Conversión de Producto",
                           [
                               "Latencia objetivo P99: < 450ms desde clic hasta confirmación en pantalla.",
                               "One-Click Checkout: Bóveda de tarjetas seguras con tokenización PCI-DSS Nivel 1.",
                               "Smart Routing Transaccional: Derivación dinámica al adquirente con menor tasa de rechazo.",
                               "Tasa de Aprobación Global: > 94.2% con reintento silencioso en pasarelas secundarias."
                           ],
                           badge="EXPERIENCIA UX", icon="card", bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], frame_id=fid1)

    scene.add_sticky_note(sc1_x + 25.0, sc1_y + 400.0, sc1_w - 50.0, 150.0,
                          "REGLA DE ORO DE PRODUCTO FINTECH:\n\n"
                          "Cero Fricción en UI ──► Seguridad Invisible ──► Idempotencia Garantizada\n\n"
                          "Si el usuario pierde conexión a mitad del pago, NUNCA se cobra dos veces.",
                          font_size=13, angle_deg=-1.0, frame_id=fid1)

    scene.add_feature_card(sc1_x + 25.0, sc1_y + 565.0, sc1_w - 50.0, 155.0,
                           "Integraciones B2B & Webhooks para Comercios",
                           [
                               "API REST / GraphQL pública con autenticación mediante API Keys y mTLS.",
                               "Notificaciones Webhook en tiempo real con firma criptográfica HMAC-SHA256.",
                               "Panel de comercios en tiempo real con analytics de conversión y liquidaciones."
                           ],
                           badge="INTEGRACIÓN B2B", bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], frame_id=fid1)

    # Scope 2: Macro-Flujo de Transacción en 8 Pasos (Pipeline Ribbon)
    sc2_w = 1050.0
    sc2_x = sc1_x + sc1_w + 30.0
    scene.add_scope_container(sc2_x, sc1_y, sc2_w, sc_h, label="2. MACRO-PIPELINE DE PROCESAMIENTO TRANSACCIONAL (8 ETAPAS)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

    pipe_steps = [
        ("01. INICIAR", "Generación orden", "ID Transacción", "INGRESS", "card"),
        ("02. IDEMPOTENCIA", "Verificación Key", "Bloqueo duplicados", "CORE LOCK", "lock", True),
        ("03. ANTI-FRAUDE", "Score de Riesgo", "ML en tiempo real", "RISK ENGINE", "shield"),
        ("04. TOKENIZAR", "Cifrado PCI-DSS", "Bóveda HSM segura", "PCI VAULT", "key"),
        ("05. GATEWAY", "Envío al Adquirente", "Visa/Mastercard/PSE", "ROUTING", "server"),
        ("06. LEDGER", "Registro ACID", "Asiento de saldo", "DATABASE", "database"),
        ("07. EVENTO ASYNC", "Publicación Kafka", "Tópico payment.settled", "STREAMING", "terminal"),
        ("08. NOTIFICAR", "Push / Webhook", "Comprobante formal", "DELIVERY", "file")
    ]

    p_card_w = (sc2_w - 65.0) * 0.5
    for idx, (p_tit, p_sub, p_meta, p_badge, p_icon, *is_h) in enumerate(pipe_steps):
        px = sc2_x + 20.0 + (idx % 2) * (p_card_w + 25.0)
        py = sc1_y + 45.0 + (idx // 2) * 165.0
        h_flag = is_h[0] if is_h else False
        scene.add_quad_card(px, py, p_card_w, 145.0, p_tit, sublabel=f"{p_sub}\n{p_meta}", badge=p_badge, icon=p_icon, is_hero=h_flag, font_size=15, frame_id=fid1)

    # Scope 3: Gobernanza de Negocio & SLAs
    sc3_w = fw - 120.0 - sc1_w - sc2_w - 60.0
    sc3_x = sc2_x + sc2_w + 30.0
    scene.add_scope_container(sc3_x, sc1_y, sc3_w, sc_h, label="3. GOBERNANZA, SLAS & CAPACIDAD", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

    sla_layers = [
        ("SLA 99.999%", "DISPONIBILIDAD CINCO NUEVES", "TIEMPO ACTIVO",
         ["< 5.26 minutos de inactividad anual permitida", "Multi-Región Activo-Activo en AWS / GCP", "Zero Downtime Deployments (Canary Releases)"],
         PALETTE["GREEN_BG"], PALETTE["GREEN_BORDER"], "#059669"),

        ("5.000 TPS", "CAPACIDAD Y THROUGHPUT PICO", "RENDIMIENTO",
         ["Procesamiento escalable horizontalmente en EKS", "Autoscaling reactivo ante eventos Black Friday", "Latencia p50 < 180ms / p99 < 450ms"],
         PALETTE["BLUE_BG"], PALETTE["BLUE_BORDER"], "#2563EB"),

        ("PCI-DSS", "CUMPLIMIENTO & AUDITORÍA REGULATORIA", "NORMATIVA",
         ["Certificación PCI-DSS Nivel 1 para tarjetas", "Cifrado de datos en tránsito (TLS 1.3) y reposo (AES-256)", "Trazabilidad forense inmutable ante entidades bancarias"],
         PALETTE["SLATE_BG"], PALETTE["SLATE_BORDER"], "#475569")
    ]

    for l_i, (l_num, l_tit, l_badge, l_items, l_bg, l_str, l_bcol) in enumerate(sla_layers):
        ly = sc1_y + 45.0 + l_i * 225.0
        scene.add_stack_layer(sc3_x + 20.0, ly, sc3_w - 40.0, 205.0,
                              l_num, l_tit, l_badge, l_items,
                              bg="#FFFFFF", stroke=l_str,
                              header_bg=l_bg, header_stroke=l_str,
                              badge_bg=l_bcol, badge_color="#FFFFFF", frame_id=fid1)

    scene.add_legend_footer(f1_x + 60.0, f1_y + 925.0, fw - 120.0, swatches=[
        {"label": "Idempotencia & Bloqueo Transaccional", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Canales & Experiencia UX", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Disponibilidad 99.999% & SLAs", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]}
    ], note="Fintech Executive Architecture: Visión estratégica de canales, pipeline transaccional y compromisos de servicio.", frame_id=fid1)


    # ═══════════════════════════════════════════════════════════════════════════
    # MARCO 2: ARQUITECTURA TÉCNICA DE MICROSERVICIOS (INGENIERÍA) (Y = 1150)
    # ═══════════════════════════════════════════════════════════════════════════
    f2_x, f2_y = place(fw, fh)
    fid2 = scene.add_frame("FRAME 2: ARQUITECTURA TÉCNICA — MICROSERVICIOS, EVENT STREAMING & PERSISTENCIA", f2_x, f2_y, fw, fh)

    scene.add_text(f2_x + 60.0, f2_y + 35.0, "SYSTEM TOPOLOGY  ·  MICROSERVICES, ASYNCHRONOUS PIPELINE & DATA TIERS", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid2)
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "Topología de Servicios: Gateway, Autenticación, Kafka, Redis Cluster y PostgreSQL Sharded", font_size=26, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    sc2_y = f2_y + 115.0

    # Scope 1: Ingress, Auth & Edge Security
    sec1_w = 830.0
    scene.add_scope_container(f2_x + 60.0, sc2_y, sec1_w, sc_h, label="1. EDGE INGRESS, API GATEWAY & AUTENTICACIÓN (OAUTH2)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)

    scene.add_quad_card(f2_x + 85.0, sc2_y + 45.0, sec1_w - 50.0, 140.0,
                        "Cloudflare WAF & DDoS Shield",
                        sublabel="Filtrado perimetral de ataques Layer 7.\nTerminación TLS 1.3 y verificación mTLS.\nInspección de anomalías de tráfico malicioso.",
                        badge="EDGE SECURITY", icon="shield", font_size=16, frame_id=fid2)

    scene.add_quad_card(f2_x + 85.0, sc2_y + 205.0, sec1_w - 50.0, 140.0,
                        "Kong API Gateway Cluster",
                        sublabel="Enrutamiento dinámico a microservicios backend.\nRate Limiting distribuido con algoritmo Token Bucket.\nInyección de Correlation ID para trazabilidad distribuida.",
                        badge="API GATEWAY", icon="server", font_size=16, frame_id=fid2)

    scene.add_feature_card(f2_x + 85.0, sc2_y + 365.0, sec1_w - 50.0, 175.0,
                           "Servicio de Autenticación & Tokens (OAuth2 / OIDC)",
                           [
                               "Emisión y validación de tokens JWT asimétricos (claves RSA-4096 / Ed25519).",
                               "Almacenamiento de sesiones activas y listas de revocación en Redis Caché.",
                               "Soporte de API Keys seguras para clientes B2B con rotación automática de secretos.",
                               "Políticas RBAC estrictas: Roles de Comercio, Auditor, Cajero y SuperAdmin."
                           ],
                           badge="AUTH SERVICE", icon="key", bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], frame_id=fid2)

    scene.add_feature_card(f2_x + 85.0, sc2_y + 555.0, sec1_w - 50.0, 165.0,
                           "Capa de Resiliencia Perimetral (Circuit Breaker)",
                           [
                               "Implementación de patrón Circuit Breaker con Netflix Resilience4j / Envoy.",
                               "Degradación elegante ante caídas temporales de proveedores bancarios.",
                               "Fallback automático a pasarelas alternativas de contingencia."
                           ],
                           badge="RESILIENCIA", bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], frame_id=fid2)

    # Scope 2: Core Processing Microservices
    core2_w = 950.0
    core2_x = f2_x + 60.0 + sec1_w + 30.0
    scene.add_scope_container(core2_x, sc2_y, core2_w, sc_h, label="2. CORE DE PROCESAMIENTO DE PAGOS & MÁQUINA DE ESTADOS", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)

    scene.add_quad_card(core2_x + 25.0, sc2_y + 45.0, core2_w - 50.0, 140.0,
                        "Payment Orchestrator Engine",
                        sublabel="Máquina de estados finitos transaccionales (Saga Pattern).\nCoordinación de compensaciones ante rechazos bancarios.\nGestión del ciclo de vida: PENDING -> AUTHORIZED -> SETTLED -> REFUNDED.",
                        badge="ORQUESTADOR", icon="server", font_size=16, frame_id=fid2)

    p_services = [
        ("Card Payment Service", "Procesamiento de tarjetas crédito/débito.\nConexión directa Visa/Mastercard.\n3D Secure 2.0 y soporte EMV.", "CARDS", "card"),
        ("ACH & PSE Instant Transfer", "Transferencias bancarias en tiempo real.\nProtocolos ACH, FedNow y redes locales PSE.\nConciliación de referencias de pago.", "ACH / BANK", "server"),
        ("Crypto & Digital Wallets", "Integración con Apple Pay, Google Wallet.\nCobros instantáneos en stablecoins (USDC).\nLiquidación a moneda fiduciaria.", "WALLETS", "laptop"),
        ("Payout & Dispersion Engine", "Dispersión masiva de fondos a comercios.\nTransferencias nocturnas programadas.\nCálculo automático de retenciones fiscales.", "DISPERSION", "database")
    ]

    ps_w = (core2_w - 65.0) * 0.5
    for idx, (ps_tit, ps_sub, ps_badge, ps_icon) in enumerate(p_services):
        px = core2_x + 20.0 + (idx % 2) * (ps_w + 25.0)
        py = sc2_y + 205.0 + (idx // 2) * 165.0
        scene.add_quad_card(px, py, ps_w, 145.0, ps_tit, sublabel=ps_sub, badge=ps_badge, icon=ps_icon, font_size=14, frame_id=fid2)

    scene.add_feature_card(core2_x + 20.0, sc2_y + 550.0, core2_w - 40.0, 170.0,
                           "Verificador de Claves de Idempotencia (Idempotency Key)",
                           [
                               "Header obligatorio `X-Idempotency-Key` (UUID v4) en cada petición de cobro.",
                               "Bloqueo atómico distribuido en Redis (SETNX con TTL de 24 horas) para evitar doble cobro.",
                               "Si la petición se repite en vuelo, devuelve la respuesta exacta cacheada sin reprocesar.",
                               "Garantía estricta Exactly-Once Processing en todo el pipeline financiero."
                           ],
                           badge="IDEMPOTENCY VERIFIER", icon="lock", is_hero=True, frame_id=fid2)

    # Scope 3: Storage Layer, Cache & Event Bus
    data2_w = fw - 120.0 - sec1_w - core2_w - 60.0
    data2_x = core2_x + core2_w + 30.0
    scene.add_scope_container(data2_x, sc2_y, data2_w, sc_h, label="3. CAPA DE DATOS, CACHÉ & EVENT STREAMING", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)

    data_stacks = [
        ("POSTGRESQL", "BASE DE DATOS RELACIONAL ACID", "LEDGER FINANCIERO",
         ["Master-Replica con Sharding por Tenant y partición por fecha", "Nivel de aislamiento SERIALIZABLE para transferencias", "Tablas inmutables de asientos contables (Double-Entry Ledger)"],
         PALETTE["BLUE_BG"], PALETTE["BLUE_BORDER"], "#2563EB"),

        ("REDIS CLUSTER", "CACHÉ EN MEMORIA & LOCK DISTRIBUIDO", "TOKEN & LOCKS",
         ["Almacenamiento de claves de idempotencia con expiración TTL", "Distributed Locks con algoritmo Redlock para concurrencia", "Caché de rutas de adquirentes y catálogo de comisiones"],
         PALETTE["AMBER_BG"], PALETTE["AMBER_BORDER"], "#D97706"),

        ("APACHE KAFKA", "BUS DE EVENTOS ASÍNCRONOS", "EVENT STREAMING",
         ["Tópicos particionados: payment.created, payment.settled, payment.failed", "Procesamiento con Kafka Streams para detección de patrones", "Garantía de orden secuencial por Tenant ID"],
         PALETTE["INDIGO_BG"], PALETTE["INDIGO_BORDER"], "#4F46E5"),

        ("ANALYTICS SINK", "LAKEHOUSE & MOTOR DE MÉTRICAS", "CLICKHOUSE / OLAP",
         ["Sink en tiempo real para dashboards de volumen transaccional", "Cálculo continuo de tasas de aprobación y comisiones", "Exportación automatizada a Data Lake para modelos de ML"],
         PALETTE["GREEN_BG"], PALETTE["GREEN_BORDER"], "#059669")
    ]

    for d_i, (d_num, d_tit, d_badge, d_items, d_bg, d_str, d_bcol) in enumerate(data_stacks):
        dy = sc2_y + 45.0 + d_i * 168.0
        scene.add_stack_layer(data2_x + 20.0, dy, data2_w - 40.0, 155.0,
                              d_num, d_tit, d_badge, d_items,
                              bg="#FFFFFF", stroke=d_str,
                              header_bg=d_bg, header_stroke=d_str,
                              badge_bg=d_bcol, badge_color="#FFFFFF", frame_id=fid2)

    scene.add_legend_footer(f2_x + 60.0, f2_y + 925.0, fw - 120.0, swatches=[
        {"label": "Verificador de Idempotencia (Exactly-Once)", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Ingress & Microservicios de Pago", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Persistencia ACID & Kafka Streaming", "bg": PALETTE["INDIGO_BG"], "stroke": PALETTE["GREEN_HERO"]}
    ], note="Fintech Engineering Topology: Microservicios desacoplados con contratos de idempotencia, streaming Kafka y ledger inmutable.", frame_id=fid2)


    # ═══════════════════════════════════════════════════════════════════════════
    # MARCO 3: RESILIENCIA, PCI-DSS & CONCILIACIÓN (OPERACIONES) (Y = 2300)
    # ═══════════════════════════════════════════════════════════════════════════
    f3_x, f3_y = place(fw, fh)
    fid3 = scene.add_frame("FRAME 3: RESILIENCIA & CONTROL — SEGURIDAD PCI-DSS, DEAD LETTER QUEUE & CONCILIACIÓN", f3_x, f3_y, fw, fh)

    scene.add_text(f3_x + 60.0, f3_y + 35.0, "OPERATIONAL RESILIENCE  ·  PCI COMPLIANCE, DLQ RECOVERY & RECONCILIATION", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid3)
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "Resiliencia Operativa: Tokenizador PCI-DSS HSM, Reintentos con Jitter, DLQ y Conciliación Bancaria", font_size=26, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    sc3_y = f3_y + 115.0

    # Scope 1: Seguridad, Bóveda PCI-DSS & Anti-Fraude
    sec3_w = 830.0
    scene.add_scope_container(f3_x + 60.0, sc3_y, sec3_w, sc_h, label="1. SEGURIDAD REFORZADA, BÓVEDA PCI-DSS & MOTOR ANTI-FRAUDE", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)

    scene.add_feature_card(f3_x + 85.0, sc3_y + 45.0, sec3_w - 50.0, 200.0,
                           "Bóveda de Tokenización Aislada (PCI-DSS Vault)",
                           [
                               "Los datos de tarjetas (PAN, CVV, Fecha) NUNCA tocan la base de datos principal.",
                               "Cifrado por Hardware Security Module (HSM) con claves maestras rotativas.",
                               "Generación de tokens opacos irreversibles para uso en transacciones recurrentes.",
                               "Cumplimiento formal de los 12 requerimientos estándar de PCI-DSS Nivel 1."
                           ],
                           badge="PCI TOKENIZER", icon="lock", is_hero=True, frame_id=fid3)

    scene.add_feature_card(f3_x + 85.0, sc3_y + 260.0, sec3_w - 50.0, 190.0,
                           "Motor de Prevención de Fraude con Machine Learning",
                           [
                               "Evaluación de riesgo en menos de 50ms por transacción.",
                               "Detección de patrones anómalos: Georreferenciación, velocidad de gasto y Device Fingerprint.",
                               "Reglas de bloqueo automático, desafío 3D Secure forzado o pase limpio.",
                               "Integración con listas negras globales y consorcios de fraude bancario."
                           ],
                           badge="ANTI-FRAUD AI", icon="shield", bg=PALETTE["CORAL_BG"], stroke=PALETTE["CORAL_BORDER"], frame_id=fid3)

    scene.add_feature_card(f3_x + 85.0, sc3_y + 465.0, sec3_w - 50.0, 160.0,
                           "Auditoría Forense & Logs Inmutables",
                           [
                               "Registro de cada intento de pago con firma criptográfica de evento.",
                               "Almacenamiento WORM (Write Once, Read Many) en Amazon S3 Glacier.",
                               "Imposibilidad de alteración de registros por administradores internos."
                           ],
                           badge="AUDIT LOG", bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], frame_id=fid3)

    # Scope 2: Máquina de Reintentos, Circuit Breaker & Dead Letter Queue (DLQ)
    retry_w = 950.0
    retry_x = f3_x + 60.0 + sec3_w + 30.0
    scene.add_scope_container(retry_x, sc3_y, retry_w, sc_h, label="2. MÁQUINA DE REINTENTOS, CIRCUIT BREAKER & DEAD LETTER QUEUE (DLQ)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)

    scene.add_quad_card(retry_x + 25.0, sc3_y + 45.0, (retry_w - 65.0) * 0.5, 140.0,
                        "Exponential Backoff con Jitter",
                        sublabel="Intervalos: 1s -> 2s -> 4s -> 8s + variación aleatoria.\nEvita el efecto estampida (Thundering Herd).\nMáximo 3 intentos por transacción transitoria.",
                        badge="REINTENTO", icon="terminal", font_size=14, frame_id=fid3)

    scene.add_quad_card(retry_x + 25.0 + (retry_w - 65.0) * 0.5 + 15.0, sc3_y + 45.0, (retry_w - 65.0) * 0.5, 140.0,
                        "Dead Letter Queue (DLQ)",
                        sublabel="Aislamiento de mensajes fallidos no recuperables.\nAlerta inmediata a canal de guardia en PagerDuty.\nRe-inyección manual tras corrección del proveedor.",
                        badge="COLA DLQ", icon="alert", font_size=14, frame_id=fid3)

    scene.add_feature_card(retry_x + 25.0, sc3_y + 200.0, retry_w - 50.0, 165.0,
                           "Protocolo de Resolución de Timeouts Bancarios (Status Unknown)",
                           [
                               "Si el banco no responde en 8 segundos, la transacción pasa a estado `PENDING_CONFIRMATION`.",
                               "Worker en segundo plano consulta el estado del cobro mediante sondeo idempotente.",
                               "Evita rechazar transacciones que el banco ya debitó o duplicar cobros no confirmados.",
                               "Actualización asíncrona al comercio mediante Webhook una vez resuelto el estado."
                           ],
                           badge="TIMEOUT RECOVERY", icon="server", bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], frame_id=fid3)

    scene.add_feature_card(retry_x + 25.0, sc3_y + 380.0, retry_w - 50.0, 150.0,
                           "Degradación Elegante & Ruteo Alternativo de Redes",
                           [
                               "Monitoreo continuo de latencia por adquirente (Stripe, Adyen, Bancos Locales).",
                               "Si la tasa de error de un canal supera el 5%, el tráfico migra automáticamente al secundario.",
                               "Restablecimiento automático una vez estabilizado el proveedor principal."
                           ],
                           badge="SMART FAILOVER", icon="card", bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], frame_id=fid3)

    scene.add_sticky_note(retry_x + 25.0, sc3_y + 545.0, retry_w - 50.0, 175.0,
                          "POLÍTICA DE RESILIENCIA OPERATIVA:\n\n"
                          "1. Todo fallo transitorio se reintenta con Exponential Backoff y Jitter.\n"
                          "2. Todo fallo definitivo se aísla en la Dead Letter Queue (DLQ).\n"
                          "3. Ningún centavo se pierde en tránsito entre el cliente y el banco.",
                          font_size=13, angle_deg=1.0, frame_id=fid3)

    # Scope 3: Conciliación Nocturna & Observabilidad
    rec3_w = fw - 120.0 - sec3_w - retry_w - 60.0
    rec3_x = retry_x + retry_w + 30.0
    scene.add_scope_container(rec3_x, sc3_y, rec3_w, sc_h, label="3. CONCILIACIÓN BANCARIA NOCTURNA & OBSERVABILIDAD 24/7", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)

    scene.add_feature_card(rec3_x + 20.0, sc3_y + 45.0, rec3_w - 40.0, 240.0,
                           "Nightly Reconciliation Worker (Conciliación Diaria)",
                           [
                               "Cruce automatizado diario de archivos de liquidación bancaria (.CAMT / .BAI2) vs Ledger interno.",
                               "Identificación automática de 3 estados de conciliación:",
                               "  • Match Exacto: Monto, fecha y referencia coinciden (99.8% de operaciones).",
                               "  • Diferencia de Comisión: Ajuste contable por tarifas de adquirente.",
                               "  • Transacción Huérfana: Alerta prioritaria para conciliación manual por equipo financiero.",
                               "Generación de reportes de balance y certificación de fondos para auditoría externa."
                           ],
                           badge="CONCILIACIÓN NOCTURNA", icon="file", bg=PALETTE["GREEN_BG"], stroke=PALETTE["GREEN_BORDER"], frame_id=fid3)

    scene.add_feature_card(rec3_x + 20.0, sc3_y + 300.0, rec3_w - 40.0, 240.0,
                           "Observabilidad Full-Stack & Telemetría Distribuida",
                           [
                               "Trazabilidad distribuida con OpenTelemetry e inyección de `trace_id` en headers.",
                               "Métricas en tiempo real con Prometheus: TPS por canal, latencia p50/p95/p99 y error rate.",
                               "Dashboards operacionales en Grafana para monitoreo visual del equipo de SRE.",
                               "Alertas automáticas vía PagerDuty y Slack ante desvíos de SLA o anomalías en colas Kafka."
                           ],
                           badge="TELEMETRÍA 24/7", icon="database", bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], frame_id=fid3)

    scene.add_quad_card(rec3_x + 20.0, sc3_y + 555.0, rec3_w - 40.0, 165.0,
                        "Soporte & Mesa de Operaciones",
                        sublabel="Consola unificada para operaciones y servicio al cliente.\nBúsqueda instantánea por UUID, tarjeta enmascarada o comercio.\nHerramientas de reembolso (refund) con autorización de 2 firmas.",
                        badge="OPERACIONES", icon="users", font_size=15, frame_id=fid3)

    scene.add_legend_footer(f3_x + 60.0, f3_y + 925.0, fw - 120.0, swatches=[
        {"label": "Bóveda PCI-DSS HSM & Anti-Fraude", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Dead Letter Queue & Backoff", "bg": PALETTE["AMBER_BG"], "stroke": PALETTE["AMBER_BORDER"]},
        {"label": "Conciliación Bancaria & Telemetría", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]}
    ], note="Fintech Operations Architecture: Bóveda PCI-DSS, tolerancia a fallos con DLQ y conciliación nocturna automatizada.", frame_id=fid3)

    return scene


def main():
    output_path = os.path.join(OUT_DIR, "arquitectura_pagos_fintech.excalidraw")
    scene = build_fintech_payments_board()
    scene.save(output_path)

    print(f"Canvas Fintech generado exitosamente: {output_path}")

    validated_scene, report = validate_scene(output_path)
    print("\n" + "=" * 90)
    print("📊 REPORTE DE VALIDACIÓN SKETION 8.0 — ARQUITECTURA VISUAL DE PAGOS FINTECH")
    print("=" * 90)
    print(f" • Puntuación Global Sketion   : {report.sketion_overall_score} / 100 [{('✅ PASS' if report.is_valid else '❌ FAIL')}]")
    print(f" • Repair Dependency (RDS)     : {report.repair_dependency_score} [{report.repair_dependency_status}]")
    print(f" • Densidad Visual             : {report.visual_metrics.density:.1f} / 10 (Target: 4.0/10)")
    print(f" • Acentos Hero en Escena      : {report.visual_metrics.accent_count} (Regla del acento único respetada)")
    print(f" • Elementos Totales           : {len(scene.elements)}")
    print("=" * 90)


if __name__ == "__main__":
    main()
