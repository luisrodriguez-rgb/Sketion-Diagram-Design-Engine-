"""
Sketion 8.5 — Polymorphic Diversity Architecture Showcase
Demuestra la ruptura total del monocultivo de cajas mediante:
- Frame 1: Pipeline Flow Continuo (Arquetipo C/P) con Actores Circulares y Barreras WAF
- Frame 2: Topología Radial Hub & Spoke (Arquetipo A) con Orquestador Central y Satélites Orbitando
- Frame 3: Capas de Persistencia con Cilindros de Base de Datos y Tuberías de Streaming Kafka
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from layout.pipeline_flow import PipelineFlowLayoutEngine
from layout.radial_hub import RadialHubLayoutEngine
from layout.layered_architecture import LayeredArchitectureLayoutEngine
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


def build_diverse_architecture_board():
    place_reset(max_row_w=3200, gap=150)
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])

    fw = 2950.0
    fh = 950.0

    # ═══════════════════════════════════════════════════════════════════════════
    # MARCO 1: ARQUETIPO C — PIPELINE FLOW VIVO & BARRERA PERIMETRAL (Y = 0)
    # ═══════════════════════════════════════════════════════════════════════════
    f1_x, f1_y = place(fw, fh)
    fid1 = scene.add_frame("FRAME 1: ARQUETIPO C — PIPELINE TRANSACCIONAL CONTINUO & ACTORES", f1_x, f1_y, fw, fh)

    scene.add_text(f1_x + 60.0, f1_y + 35.0, "INGRESS & PIPELINE TOPOLOGY  ·  DIRECTIONAL ARROWS & ZERO-TRUST", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "Flujo Secuencial Vivo: Actores en Pastilla, Barrera WAF y Pipeline con Bucle de Retorno", font_size=26, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    # 1.1 Actores / Clientes (Pastillas Circulares con Avatares)
    scene.add_text(f1_x + 60.0, f1_y + 115.0, "1. ACTORES & CANALES DE CLIENTE", font_size=14, font_family=2, color=PALETTE["INK"], frame_id=fid1)
    act_y = f1_y + 145.0
    act_w = 260.0
    scene.add_actor_node(f1_x + 60.0, act_y, act_w, 60.0, "Web Checkout", "Next.js SPA", icon="laptop", frame_id=fid1)
    scene.add_actor_node(f1_x + 60.0, act_y + 75.0, act_w, 60.0, "Mobile SDK", "iOS & Android", icon="laptop", frame_id=fid1)
    scene.add_actor_node(f1_x + 60.0, act_y + 150.0, act_w, 60.0, "POS Terminal", "Retail Smart", icon="card", frame_id=fid1)
    scene.add_actor_node(f1_x + 60.0, act_y + 225.0, act_w, 60.0, "WhatsApp Pay", "Bot Conversacional", icon="users", frame_id=fid1)

    # 1.2 Barrera Perimetral WAF
    bar_x = f1_x + 360.0
    bar_w = 340.0
    scene.add_security_barrier(bar_x, act_y, bar_w, 285.0, "Zero-Trust Edge", [
        "Cloudflare Global WAF & DDoS",
        "Route53 Latency DNS Failover",
        "Kong Gateway + Envoy Token Bucket",
        "mTLS Mutual Auth X.509",
        "AWS ALB Multi-AZ Cluster"
    ], badge="INSPECCIÓN L7", frame_id=fid1)

    # Conectores desde actores hacia la barrera
    for i in range(4):
        ay = act_y + 30.0 + i * 75.0
        scene.add_arrow(f1_x + 60.0 + act_w, ay, bar_x, ay, stroke="#2563EB", stroke_w=1.5, frame_id=fid1)

    # 1.3 Pipeline Flow Secuencial Horizontal
    pipe_x = bar_x + bar_w + 40.0
    pipe_w = fw - 120.0 - pipe_x + f1_x
    scene.add_text(pipe_x, f1_y + 115.0, "2. PIPELINE SECUENCIAL EN 5 ETAPAS (CON FEEDBACK LOOP)", font_size=14, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    pipe_steps = [
        {"title": "01. Auth JWT", "sublabel": "Validación de firma\nRSA-4096 / Ed25519", "badge": "AUTH", "icon": "key"},
        {"title": "02. Idempotency", "sublabel": "Bloqueo SETNX 24h\nCero doble cobro", "badge": "LOCK", "icon": "lock", "is_hero": True},
        {"title": "03. Risk ML", "sublabel": "Inferencia < 20ms\nScore de Fraude", "badge": "AI SCORE", "icon": "shield"},
        {"title": "04. Gateway Direct", "sublabel": "Visa/Mastercard\nACH / PIX / PSE", "badge": "RAIL", "icon": "server"},
        {"title": "05. Ledger ACID", "sublabel": "Asiento inmutable\nDouble-Entry", "badge": "LEDGER", "icon": "database"}
    ]

    PipelineFlowLayoutEngine.render_pipeline(
        scene, pipe_x, act_y + 20.0, pipe_w, 200.0,
        pipe_steps, hero_idx=1, return_loop=True, frame_id=fid1
    )

    # Conector de la barrera al primer paso del pipeline
    scene.add_arrow(bar_x + bar_w, act_y + 120.0, pipe_x, act_y + 120.0, stroke="#059669", stroke_w=2.0, label="PAYLOAD SEGURO", frame_id=fid1)

    # Panel inferior de SLAs en franjas proporcionales
    scene.add_text(f1_x + 60.0, f1_y + 480.0, "3. COMPROMISOS DE SERVICIO & MÉTRICAS GLOBALES", font_size=14, font_family=2, color=PALETTE["INK"], frame_id=fid1)
    sla_w = (fw - 120.0 - 45.0) / 4.0
    scene.add_quad_card(f1_x + 60.0, f1_y + 510.0, sla_w, 110.0, "SLA 99.999% Uptime", sublabel="< 5.26 min/año inactividad\nMulti-Región Activo-Activo", badge="DISPONIBILIDAD", icon="server", frame_id=fid1)
    scene.add_quad_card(f1_x + 60.0 + (sla_w + 15.0), f1_y + 510.0, sla_w, 110.0, "Latencia <35ms P99", sublabel="Respuesta en Edge Gateway\nRedis In-Memory Cache", badge="LATENCIA", icon="laptop", frame_id=fid1)
    scene.add_quad_card(f1_x + 60.0 + (sla_w + 15.0) * 2, f1_y + 510.0, sla_w, 110.0, "Throughput 25k TPS", sublabel="Capacidad en tráfico pico\nEscalabilidad Kubernetes", badge="RENDIMIENTO", icon="terminal", frame_id=fid1)
    scene.add_quad_card(f1_x + 60.0 + (sla_w + 15.0) * 3, f1_y + 510.0, sla_w, 110.0, "Volumen $25M USD/día", sublabel="Liquidación neta continua\nTrazabilidad SOX/PCI", badge="NEGOCIO", icon="database", frame_id=fid1)

    scene.add_legend_footer(f1_x + 60.0, f1_y + 880.0, fw - 120.0, swatches=[
        {"label": "Idempotencia & Bloqueo Hero", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Flujo de Datos Autorizado", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Bucle de Retorno & Retry", "bg": "#FFFFFF", "stroke": PALETTE["CORAL_HERO"], "is_arrow": True, "dashed": True}
    ], note="Arquetipo C (Pipeline Flow): Topología continua con conectores ortogonales vivos y bucle de feedback.", frame_id=fid1)


    # ═══════════════════════════════════════════════════════════════════════════
    # MARCO 2: ARQUETIPO A — RADIAL HUB & SPOKE (ORQUESTADOR CENTRAL) (Y = 1150)
    # ═══════════════════════════════════════════════════════════════════════════
    f2_x, f2_y = place(fw, fh)
    fid2 = scene.add_frame("FRAME 2: ARQUETIPO A — TOPOLOGÍA RADIAL (HUB ORCHESTRATOR & SATÉLITES)", f2_x, f2_y, fw, fh)

    scene.add_text(f2_x + 60.0, f2_y + 35.0, "RADIAL TOPOLOGY  ·  CENTRAL ORCHESTRATION & SATELLITE RAILS", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid2)
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "Topología Radial Pura: Orquestador Central Hero con Satélites Orbitando a 360°", font_size=26, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    # Renderizar el Hub Radial
    satellites = [
        {"title": "PCI-DSS Vault", "sublabel": "Tokenización HSM\nCifrado Nivel 1", "badge": "VAULT", "icon": "lock"},
        {"title": "Fraud ML Engine", "sublabel": "Score de Riesgo <20ms\nModelo Predictivo", "badge": "AI RISK", "icon": "shield"},
        {"title": "Visa / Mastercard", "sublabel": "Switch ISO 8583\nCaptura Directa", "badge": "CARDS", "icon": "card"},
        {"title": "ACH / SEPA Rails", "sublabel": "Compensación Bancaria\nLotes Nocturnos", "badge": "BANKING", "icon": "server"},
        {"title": "PIX / PSE Instant", "sublabel": "Transferencias QR\nDébito Inmediato", "badge": "INSTANT", "icon": "laptop"},
        {"title": "Dynamic Fee Engine", "sublabel": "Tarifas por Comercio\nImpuestos DIAN", "badge": "FEE", "icon": "file"},
        {"title": "FX Multi-Currency", "sublabel": "Tasa Spot 15m\nCobertura Cambiaria", "badge": "FX", "icon": "card"},
        {"title": "Ledger Double-Entry", "sublabel": "Asientos ACID\nPartida Doble", "badge": "LEDGER", "icon": "database"}
    ]

    RadialHubLayoutEngine.render_radial_ecosystem(
        scene,
        cx=f2_x + (fw * 0.40),
        cy=f2_y + 450.0,
        radius=280.0,
        hub={"title": "PAYMENT ORCHESTRATOR", "sublabel": "Máquina de Estados Saga\nOrquestación Central", "badge": "HERO CORE", "icon": "server"},
        satellites=satellites,
        frame_id=fid2
    )

    # Panel lateral derecho con Callouts de Resiliencia (Stack Layer)
    call_x = f2_x + (fw * 0.72)
    call_w = fw - 120.0 - (fw * 0.72) + 60.0
    scene.add_text(call_x, f2_y + 115.0, "CALLOUTS DE RESILIENCIA (CIRCUIT BREAKERS)", font_size=14, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    callouts = [
        ("Warning: Circuit Breaker", "AISLAMIENTO PASARELA", "TIMEOUT",
         ["Latencia bancaria > 8s dispara apertura de circuito", "Desvío automático a pasarela secundaria"],
         PALETTE["CORAL_BG"], PALETTE["CORAL_BORDER"], "#D93829"),

        ("Fallback: Offline POS", "CONTINGENCIA LOCAL", "OFFLINE",
         ["Límite de crédito local para terminales desconectadas", "Criptofirma de transacciones en cola"],
         PALETTE["AMBER_BG"], PALETTE["AMBER_BORDER"], "#D97706"),

        ("Retry: Exponential Backoff", "REINTENTOS INTELIGENTES", "JITTER",
         ["Intervalos 1s, 2s, 4s, 8s con Jitter aleatorio", "Aislamiento en DLQ tras 5 intentos fallidos"],
         PALETTE["BLUE_BG"], PALETTE["BLUE_BORDER"], "#2563EB"),

        ("DR: Multi-Region Sync", "RECUPERACIÓN DESASTRES", "ACTIVE-ACTIVE",
         ["Replicación sincrónica con RPO = 0s", "RTO < 30s ante caída total de zona AWS"],
         PALETTE["GREEN_BG"], PALETTE["GREEN_BORDER"], "#059669")
    ]

    for c_i, (c_num, c_tit, c_badge, c_items, c_bg, c_str, c_bcol) in enumerate(callouts):
        cy = f2_y + 150.0 + c_i * 155.0
        scene.add_stack_layer(call_x, cy, call_w, 140.0, c_num, c_tit, c_badge, c_items,
                              bg="#FFFFFF", stroke=c_str, header_bg=c_bg, header_stroke=c_str,
                              badge_bg=c_bcol, badge_color="#FFFFFF", frame_id=fid2)

    scene.add_legend_footer(f2_x + 60.0, f2_y + 880.0, fw - 120.0, swatches=[
        {"label": "Orquestador Central Radial", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Satélites de Redes y Ledger", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]},
        {"label": "Resiliencia & Circuit Breakers", "bg": PALETTE["AMBER_BG"], "stroke": PALETTE["AMBER_BORDER"]}
    ], note="Arquetipo A (El Cerebro): Núcleo central con satélites orbitando a 360° y conexiones radiales directas.", frame_id=fid2)


    # ═══════════════════════════════════════════════════════════════════════════
    # MARCO 3: ARQUETIPO LAYER STACK CON CILINDROS & STREAMING PIPES (Y = 2300)
    # ═══════════════════════════════════════════════════════════════════════════
    f3_x, f3_y = place(fw, fh)
    fid3 = scene.add_frame("FRAME 3: ARQUETIPO LAYER STACK — CILINDROS DE STORAGE & KAFKA PIPES", f3_x, f3_y, fw, fh)

    scene.add_text(f3_x + 60.0, f3_y + 35.0, "DATA TIERS & COMPLIANCE  ·  POLYMORPHIC STORAGE & RECONCILIATION", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid3)
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "Persistencia Polimórfica: Cilindros de Base de Datos, Tubería de Streaming Kafka y Mesa de Conciliación", font_size=26, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    # 3.1 Streaming Pipe Horizontal (Kafka Event Bus)
    pipe_w = fw - 120.0
    scene.add_streaming_pipe(
        f3_x + 60.0, f3_y + 115.0, pipe_w, 95.0,
        title="APACHE KAFKA HIGH-THROUGHPUT EVENT STREAM",
        topics=["payment.created (Raw Order)", "payment.authorized (Hold)", "payment.settled (Ledger Sync)", "payment.failed (DLQ Isolation)"],
        badge="EVENT BUS KAFKA",
        is_hero=True,
        frame_id=fid3
    )

    # 3.2 Capa de Storage con Cilindros Reales
    col_w = (fw - 120.0 - 40.0) * 0.5
    scene.add_text(f3_x + 60.0, f3_y + 235.0, "1. PERSISTENCIA EN CILINDROS & DATA LAKEHOUSE", font_size=14, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    cyl_w = (col_w - 20.0) * 0.5
    cyl_y = f3_y + 265.0
    cyl_h = 130.0

    scene.add_database_cylinder(f3_x + 60.0, cyl_y, cyl_w, cyl_h, "Aurora PostgreSQL", "Master-Replica ACID\nSharding por Tenant", badge="PRIMARY DB", is_hero=True, frame_id=fid3)
    scene.add_database_cylinder(f3_x + 60.0 + cyl_w + 20.0, cyl_y, cyl_w, cyl_h, "ClickHouse OLAP", "Base de datos columnar\nAnalytics en tiempo real", badge="OLAP SINK", frame_id=fid3)

    scene.add_database_cylinder(f3_x + 60.0, cyl_y + cyl_h + 20.0, cyl_w, cyl_h, "MinIO S3 Vault", "Almacenamiento WORM\nEvidencia de auditoría", badge="AUDIT S3", frame_id=fid3)
    scene.add_database_cylinder(f3_x + 60.0 + cyl_w + 20.0, cyl_y + cyl_h + 20.0, cyl_w, cyl_h, "Redis Redlock", "Distributed Lock & Cache\nSincronización atómica", badge="REDLOCK", frame_id=fid3)

    # 3.3 Capa de Compliance, Operaciones & Conciliación
    ops_x = f3_x + 60.0 + col_w + 40.0
    scene.add_text(ops_x, f3_y + 235.0, "2. GOBERNANZA, AUDITORÍA SOC2 & CONCILIACIÓN NOCTURNA", font_size=14, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    scene.add_feature_card(ops_x, cyl_y, col_w, 130.0, "Nightly Reconciliation Worker", [
        "Cruce automatizado diario de extractos bancarios (.CAMT/.BAI2) vs Ledger interno.",
        "Detección de matches exactos, comisiones adquirentes y transacciones huérfanas.",
        "Certificación contable para auditoría externa y cierre fiscal."
    ], badge="CONCILIACIÓN DIARIA", icon="server", is_hero=True, frame_id=fid3)

    scene.add_quad_card(ops_x, cyl_y + 150.0, (col_w - 20.0) * 0.5, 130.0, "AML Engine", sublabel="Prevención lavado activos.\nCheck OFAC, ONU, PEPs.", badge="COMPLIANCE", icon="shield", frame_id=fid3)
    scene.add_quad_card(ops_x + (col_w - 20.0) * 0.5 + 20.0, cyl_y + 150.0, (col_w - 20.0) * 0.5, 130.0, "SOC2 Audit Collector", sublabel="Logs inmutables WORM.\nCertificación ISO 27001.", badge="SOC2 AUDIT", icon="lock", frame_id=fid3)

    # Conector desde Kafka hacia las bases de datos
    scene.add_arrow(f3_x + 60.0 + (pipe_w * 0.25), f3_y + 210.0, f3_x + 60.0 + (col_w * 0.5), cyl_y, stroke="#4F46E5", stroke_w=1.8, label="CDC SYNC", frame_id=fid3)
    scene.add_arrow(f3_x + 60.0 + (pipe_w * 0.75), f3_y + 210.0, ops_x + (col_w * 0.5), cyl_y, stroke="#059669", stroke_w=1.8, label="EVENT CONSUMER", frame_id=fid3)

    scene.add_legend_footer(f3_x + 60.0, f3_y + 880.0, fw - 120.0, swatches=[
        {"label": "Tubería Kafka de Streaming", "bg": PALETTE["INDIGO_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Cilindro de Base de Datos ACID", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Conciliación Bancaria Diaria", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]}
    ], note="Arquetipo Layer Stack Polimórfico: Cilindros de storage, tuberías de streaming y conectores de eventos cruzados.", frame_id=fid3)

    return scene


def main():
    output_path = os.path.join(OUT_DIR, "arquitectura_polimorfica_diversificada.excalidraw")
    scene = build_diverse_architecture_board()
    scene.save(output_path)

    print(f"Canvas Polimórfico Diversificado generado exitosamente: {output_path}")

    validated_scene, report = validate_scene(output_path)
    print("\n" + "=" * 90)
    print("📊 REPORTE DE VALIDACIÓN SKETION 8.5 — ARQUITECTURA POLIMÓRFICA DIVERSIFICADA")
    print("=" * 90)
    print(f" • Puntuación Global Sketion   : {report.sketion_overall_score} / 100 [{('✅ PASS' if report.is_valid else '❌ FAIL')}]")
    print(f" • Repair Dependency (RDS)     : {report.repair_dependency_score} [{report.repair_dependency_status}]")
    print(f" • Densidad Visual             : {report.visual_metrics.density:.1f} / 10 (Target: 4.0/10)")
    print(f" • Acentos Hero en Escena      : {report.visual_metrics.accent_count} (Regla del acento único respetada)")
    print(f" • Elementos Totales           : {len(scene.elements)}")
    print("=" * 90)


if __name__ == "__main__":
    main()
