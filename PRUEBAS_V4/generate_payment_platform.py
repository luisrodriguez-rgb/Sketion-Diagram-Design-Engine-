"""
Sketion 3.3 — Generador Maestro para Plataforma de Pagos Distribuida (Pruebas V4)
Composición Multi-Frame para Ingeniería de Sistemas:
- Frame 1: Arquitectura Distribuida y Pipeline End-to-End (Comercio -> Gateway -> Fraude -> Orquestador -> Proveedor -> Ledger -> Async)
- Frame 2: Máquina de Estados Financiera, Tratamiento de UNKNOWN y Ciclo Post-Autorización (Captura, Cancelación, Reembolsos)
- Frame 3: Matriz de Resiliencia, Idempotencia, Deduplicación y Fallos Concurrente (7 Escenarios Críticos)
- Frame 4: Contrato de Datos, Estructura del Ledger (Doble Partida) y Principios de Aislamiento
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place, compute_card_dimensions
from layout.grid import compute_matrix_layout
from validation.validator import validate_scene

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V4")
os.makedirs(OUT_DIR, exist_ok=True)

MIRO_PALETTE = {
    "CANVAS": "#F4F4F4",
    "CARD": "#FFFFFF",
    "CARD_BORDER": "#BDBDBD",
    "INK": "#0C0C0C",
    "MUTED": "#8B8B8B",
    "STICKY": "#FFE95C",
    "PAIN_RED": "#E03A2F",
    "PAIN_BG": "#FDEFEF",
    "PAIN_BORDER": "#F05A5A",
    "BANNER_PINK": "#F5BEC0",
    "PASTEL_BLUE": "#9BC7E4",
    "PASTEL_GREEN": "#C2E5D3"
}


def build_payment_platform_scene() -> str:
    place_reset(max_row_w=3400, gap=130)
    scene = ExcalidrawScene(roughness=0, bg_color=MIRO_PALETTE["CANVAS"])

    # =========================================================================
    # FRAME 1: ARQUITECTURA DISTRIBUIDA Y PIPELINE DE PROCESAMIENTO
    # =========================================================================
    w1, h1 = 3000, 1000
    fx1, fy1 = place(w1, h1)
    fid1 = scene.add_frame("1. ARQUITECTURA DE PAGOS: Pipeline Síncrono, Aislamiento de Ledger y Eventos Asíncronos", fx1, fy1, w1, h1)

    scene.add_text(fx1 + 50, fy1 + 35, "PLATAFORMA DISTRIBUIDA DE PROCESAMIENTO DE PAGOS", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid1)
    scene.add_text(fx1 + 50, fy1 + 75, "flujo transaccional síncrono con idempotencia estricta, outbox pattern y proyecciones eventuales", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)

    # Top Metric Pills
    scene.add_metric_pill(fx1 + w1 - 580, fy1 + 35, "LEDGER", "Fuente de Verdad 100%", bg=MIRO_PALETTE["INK"], frame_id=fid1)
    scene.add_metric_pill(fx1 + w1 - 320, fy1 + 35, "IDEMPOTENCIA", "Exact-Once State", bg=MIRO_PALETTE["INK"], frame_id=fid1)

    # Columnas de Infraestructura
    columns = [
        ("col_client", "1. COMERCIO / CLIENTE", 340, [
            ("node_merchant", "Comercio (Merchant)", "POST /v1/charges\nIdempotency-Key: uuid")
        ]),
        ("col_ingress", "2. INGRESS & AUTH", 360, [
            ("node_gw", "API Gateway", "Rate Limit & TLS Term."),
            ("node_auth", "Auth & RBAC", "API Key / HMAC Signature")
        ]),
        ("col_fraud", "3. FRAUD DETECTION", 380, [
            ("node_fraud", "Fraud Engine (ML)", "APPROVED | REVIEW | REJECTED\nSLA < 40ms timeout fallback")
        ]),
        ("col_orch", "4. PAYMENT ORCHESTRATOR", 440, [
            ("node_orch", "Orchestrator Core", "State Machine & Idempotency\nTransactional Outbox Table"),
            ("node_reconcil", "Reconciliation Worker", "Polling ante estado UNKNOWN")
        ]),
        ("col_provider", "5. PAYMENT PROVIDER", 400, [
            ("node_prov", "Acquirer / Provider", "AUTHORIZED | DECLINED\nTIMEOUT | UNKNOWN")
        ]),
        ("col_ledger", "6. FINANCIAL LEDGER", 420, [
            ("node_ledger", "Double-Entry Ledger", "Fuente de Verdad Financiera\nInmutable (Debe = Haber)")
        ]),
        ("col_async", "7. PROYECCIONES EVENTUALES", 440, [
            ("node_bus", "Kafka Event Broker", "Eventos: PaymentAuthorized, etc.\nAt-Least-Once Delivery"),
            ("node_notif", "Notification Service", "Webhooks / Emails a comercios\n(Sin efecto en Ledger)"),
            ("node_analyt", "Analytics OLAP", "ClickHouse / BigQuery\n(Eventual, nunca bloquea)")
        ])
    ]

    curr_x = fx1 + 45.0
    node_map = {}

    for cid, ctitle, cw, cnodes in columns:
        ch = max(450.0, len(cnodes) * 115.0 + 80.0)
        cy = fy1 + 130.0
        
        scene.add_scope_container(curr_x, cy, cw, ch, label=ctitle, stroke=MIRO_PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

        for ni, (nid, ntitle, nsub) in enumerate(cnodes):
            nx = curr_x + 20.0
            ny = cy + 50.0 + ni * 110.0
            nw = cw - 40.0
            nh = 85.0
            
            is_ledger = ("Ledger" in ntitle)
            is_orch = ("Orchestrator" in ntitle)
            bg = MIRO_PALETTE["PASTEL_BLUE"] if is_ledger else (MIRO_PALETTE["PAIN_BG"] if is_orch else "#FFFFFF")
            border = MIRO_PALETTE["INK"] if is_ledger else (MIRO_PALETTE["PAIN_BORDER"] if is_orch else MIRO_PALETTE["CARD_BORDER"])
            
            container, _ = scene.add_dual_card(nx, ny, nw, nh, ntitle, sublabel=nsub,
                                               bg=bg, stroke=border, text_color=MIRO_PALETTE["INK"], frame_id=fid1)
            node_map[nid] = (container["x"], container["y"], container["width"], container["height"])

        curr_x += cw + 55.0

    # Conexiones del Pipeline
    edges = [
        ("node_merchant", "node_gw", "HTTP POST"),
        ("node_gw", "node_auth", "Valida Firma"),
        ("node_auth", "node_fraud", "Risk Check"),
        ("node_fraud", "node_orch", "If APPROVED"),
        ("node_orch", "node_prov", "Authorize Request"),
        ("node_prov", "node_orch", "Provider Result"),
        ("node_orch", "node_ledger", "Commit Asiento"),
        ("node_orch", "node_bus", "Outbox Event"),
        ("node_bus", "node_notif", "Consume: Notif"),
        ("node_bus", "node_analyt", "Consume: Metrics"),
        ("node_reconcil", "node_prov", "Query Status (UNKNOWN)")
    ]

    for f_id, t_id, lbl in edges:
        if f_id in node_map and t_id in node_map:
            fx, fy, fw, fh = node_map[f_id]
            tx, ty, tw, th = node_map[t_id]
            
            if tx >= fx + fw:
                scene.add_arrow(fx + fw, fy + fh * 0.5, tx, ty + th * 0.5,
                                stroke=MIRO_PALETTE["MUTED"], stroke_w=1.5, label=lbl, orthogonal=True, frame_id=fid1)
            elif tx < fx:
                scene.add_arrow(fx, fy + 18.0, tx + tw, ty + 18.0,
                                stroke=MIRO_PALETTE["MUTED"], stroke_w=1.5, label=lbl, orthogonal=True, frame_id=fid1)
            else:
                scene.add_arrow(fx + fw * 0.5, fy + fh, tx + tw * 0.5, ty,
                                stroke=MIRO_PALETTE["MUTED"], stroke_w=1.5, label=lbl, orthogonal=True, frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=60.0)


    # =========================================================================
    # FRAME 2: MÁQUINA DE ESTADOS FINANCIERA Y CICLO DE VIDA POST-AUTORIZACIÓN
    # =========================================================================
    w2, h2 = 3000, 1100
    fx2, fy2 = place(w2, h2)
    fid2 = scene.add_frame("2. MÁQUINA DE ESTADOS: De Fraude a Liquidación, Manejo de UNKNOWN y Reembolsos", fx2, fy2, w2, h2)

    scene.add_text(fx2 + 50, fy2 + 35, "TRANSICIONES DE ESTADO FINANCIERO Y CICLO POST-AUTORIZACIÓN", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid2)
    scene.add_text(fx2 + 50, fy2 + 75, "árbol de decisión de fraude, resolución asíncrona de UNKNOWN y operaciones posteriores", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid2)

    # Sub-banner de regla crítica
    scene.add_banner(fx2 + 60, fy2 + 125, w2 - 120, 44,
                     "regla de oro: ante resultado UNKNOWN/TIMEOUT nunca se asume fallo; se mantiene en PENDING_RECONCILIATION.",
                     bg=MIRO_PALETTE["INK"], text_color="#FFFFFF", font_size=15, frame_id=fid2)

    # Fila 1: Estados de Fraude & Autorización
    f1_states = [
        ("INICIADO", "Payload validado\nIdempotency registrada", fx2 + 60, fy2 + 220, "#FFFFFF"),
        ("FRAUD_REVIEW", "Flag de riesgo sospechoso\nCola manual de analistas", fx2 + 520, fy2 + 340, MIRO_PALETTE["STICKY"]),
        ("FRAUD_REJECTED", "Rechazo definitivo\nSin llamada a pasarela", fx2 + 520, fy2 + 460, MIRO_PALETTE["PAIN_BG"]),
        ("AUTHORIZED", "Fondos retenidos en emisor\nListo para captura (TTL 7d)", fx2 + 980, fy2 + 220, MIRO_PALETTE["PASTEL_GREEN"]),
        ("DECLINED", "Rechazo por banco emisor\nFondos insuficientes/Robo", fx2 + 980, fy2 + 460, MIRO_PALETTE["PAIN_BG"]),
        ("UNKNOWN / TIMEOUT", "Respuesta no recibida\nPasa a reconciliación", fx2 + 980, fy2 + 340, MIRO_PALETTE["STICKY"])
    ]

    for st_title, st_desc, sx, sy, sbg in f1_states:
        is_bad = ("REJECTED" in st_title or "DECLINED" in st_title)
        border = MIRO_PALETTE["PAIN_BORDER"] if is_bad else MIRO_PALETTE["CARD_BORDER"]
        text_col = MIRO_PALETTE["PAIN_RED"] if is_bad else MIRO_PALETTE["INK"]
        scene.add_bound_card(sx, sy, 380, 85, f"{st_title}\n{st_desc}",
                             bg=sbg, stroke=border, text_color=text_col, font_size=13, frame_id=fid2)

    # Conectar Estados de Entrada
    scene.add_arrow(fx2 + 440, fy2 + 262, fx2 + 980, fy2 + 262, stroke=MIRO_PALETTE["INK"], stroke_w=1.5, label="Fraude APPROVED", frame_id=fid2)
    scene.add_arrow(fx2 + 250, fy2 + 305, fx2 + 520, fy2 + 382, stroke=MIRO_PALETTE["MUTED"], stroke_w=1.5, label="REVIEW", orthogonal=True, frame_id=fid2)
    scene.add_arrow(fx2 + 250, fy2 + 305, fx2 + 520, fy2 + 502, stroke=MIRO_PALETTE["PAIN_RED"], stroke_w=1.5, label="REJECTED", orthogonal=True, frame_id=fid2)

    # Conectar a Provider Out
    scene.add_arrow(fx2 + 1360, fy2 + 262, fx2 + 1540, fy2 + 262, stroke=MIRO_PALETTE["INK"], stroke_w=1.5, label="POST /capture", frame_id=fid2)

    # Fila 2: Ciclo de Vida Post-Autorización
    f2_states = [
        ("CAPTURED", "Fondos transferidos a cuenta\nAsiento en Ledger: Liquidado", fx2 + 1540, fy2 + 220, MIRO_PALETTE["PASTEL_BLUE"]),
        ("VOIDED / CANCELLED", "Autorización anulada\nFondos liberados al cliente", fx2 + 1540, fy2 + 360, "#FFFFFF"),
        ("PARTIALLY REFUNDED", "Reembolso parcial ejecutado\nAsiento de ajuste en Ledger", fx2 + 2040, fy2 + 220, MIRO_PALETTE["STICKY"]),
        ("FULLY REFUNDED", "Reembolso 100% completado\nAsiento de contrapartida", fx2 + 2040, fy2 + 360, "#FFFFFF"),
        ("RECONCILED (AUTO)", "Aclaración de UNKNOWN\nSincronizado vía Polling/Reporte", fx2 + 1540, fy2 + 500, MIRO_PALETTE["PASTEL_GREEN"])
    ]

    for st_title, st_desc, sx, sy, sbg in f2_states:
        scene.add_bound_card(sx, sy, 420, 85, f"{st_title}\n{st_desc}",
                             bg=sbg, stroke=MIRO_PALETTE["CARD_BORDER"], text_color=MIRO_PALETTE["INK"],
                             font_size=13, frame_id=fid2)

    scene.add_arrow(fx2 + 1960, fy2 + 262, fx2 + 2040, fy2 + 262, stroke=MIRO_PALETTE["INK"], stroke_w=1.5, label="Refund Parcial", frame_id=fid2)
    scene.add_arrow(fx2 + 1960, fy2 + 262, fx2 + 2040, fy2 + 402, stroke=MIRO_PALETTE["INK"], stroke_w=1.5, label="Refund Total", orthogonal=True, frame_id=fid2)
    scene.add_arrow(fx2 + 1360, fy2 + 382, fx2 + 1540, fy2 + 542, stroke=MIRO_PALETTE["MUTED"], stroke_w=1.5, label="Polling / Batch", orthogonal=True, frame_id=fid2)

    # Bloque de Explicación de Reconciliación al Pie
    rec_y = fy2 + 630.0
    scene.add_rect(fx2 + 60, rec_y, w2 - 120, 160, bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.5, stroke_style="dashed", roundness_type=3, frame_id=fid2)
    scene.add_text(fx2 + 85, rec_y + 20, "PROTOCOLO DE RECONCILIACIÓN Y MANEJO DE ESTADOS DUDOSOS (UNKNOWN / TIMEOUT):", font_size=15, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid2)
    scene.add_text(fx2 + 85, rec_y + 55, "1. [Timeout Inmediato]: El Orchestrator devuelve HTTP 202 ACCEPTED (Pending) al comercio con el order_id.\n2. [Polling Exponencial]: Worker consulta el endpoint /status del proveedor a los 30s, 2m y 10m.\n3. [Reconciliation Batch]: Proceso nocturno compara los extractos de liquidación del procesador contra la base de datos local.\n4. [Resolución]: Si el proveedor cobró -> Transiciona a AUTHORIZED/CAPTURED en Ledger. Si no existe -> Transiciona a DECLINED_TIMEOUT.",
                   font_size=13, font_family=2, color="#333333", frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=60.0)


    # =========================================================================
    # FRAME 3: MATRIZ DE RESILIENCIA DISTRIBUIDA E IDEMPOTENCIA (7 ESCENARIOS)
    # =========================================================================
    w3, h3 = 3000, 850
    fx3, fy3 = place(w3, h3)
    fid3 = scene.add_frame("3. MATRIZ DE RESILIENCIA: Idempotencia, Deduplicación y Tolerancia a Fallos", fx3, fy3, w3, h3)

    scene.add_text(fx3 + 50, fy3 + 35, "MATRIZ DE IDEMPOTENCIA Y TRATAMIENTO DE ESCENARIOS DE FALLO", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid3)
    scene.add_text(fx3 + 50, fy3 + 75, "análisis formal de los 7 escenarios distribuidos, causas de concurrencia y mecanismos de recuperación", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid3)

    matrix_headers = ["ESCENARIO DE FALLO", "DESCRIPCIÓN / CONDICIÓN CONCURRENTE", "MECANISMO DE IDEMPOTENCIA", "IMPACTO EN LEDGER", "GARANTÍA DE CONSISTENCIA"]
    matrix_rows = [
        {"values": ["1. Doble Envío de Solicitud", "El cliente hace doble clic o reintenta por red.", "Redis Key: idempotency:{merchant_id}:{idempotency_key} con TTL 24h. Si ya existe, retorna respuesta en cache.", "Cero duplicación de asientos. Un solo cargo.", "Exact-Once Effect"]},
        {"values": ["2. Timeout del Proveedor", "La pasarela no responde en 5000ms tras procesar.", "El Orchestrator asigna estado PENDING_RECONCILIATION y delega en el Reconciliation Worker.", "No se crea asiento hasta confirmación de cobro.", "Consistencia Eventual"]},
        {"values": ["3. Respuesta Duplicada", "El proveedor envía confirmación doble síncrona.", "Filtro de transición de State Machine: si el estado ya es AUTHORIZED, ignora el segundo payload.", "Ninguno. El Ledger ignora eventos ya aplicados.", "Idempotent State Check"]},
        {"values": ["4. Webhook Duplicado", "El proveedor reintenta el webhook HTTP 5 veces.", "Tabla de deduplicación de webhooks con Unique Constraint sobre webhook_event_id.", "El primer webhook asienta en Ledger; los otros devuelven 200 OK sin procesar.", "Deduplicación Atómica"]},
        {"values": ["5. Webhook Fuera de Orden", "Llega webhook de CAPTURED antes del de AUTHORIZED.", "Verificación de monotonicidad de versiones. Si llega CAPTURED en estado PENDING, transiciona directo aplicando ambos.", "El Ledger genera los asientos de autorización y captura en secuencia lógica.", "Sequencing & Versioning"]},
        {"values": ["6. Caída de Notifications", "El servicio de notificaciones / webhooks se cae.", "Outbox pattern desacoplado en Kafka. Los mensajes quedan encolados en el broker.", "Cero impacto. El Ledger ya está comprometido y cerrado.", "Aislamiento de Dominio"]},
        {"values": ["7. Caída de Analytics", "El motor OLAP ClickHouse está en mantenimiento.", "Consumo asíncrono con Dead Letter Queue (DLQ). Replay automático al restablecer servicio.", "Cero impacto financiero. Analytics es 100% de solo lectura.", "Eventual Consistency"]}
    ]

    grid = compute_matrix_layout(start_x=fx3 + 50, start_y=fy3 + 125, headers=matrix_headers, rows=matrix_rows)

    for cell in grid["headers"]:
        c = cell["col"]
        scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], matrix_headers[c],
                             bg=MIRO_PALETTE["INK"], stroke=MIRO_PALETTE["INK"], text_color="#FFFFFF",
                             font_size=13, roundness_type=None, frame_id=fid3)

    for r, row_cells in enumerate(grid["rows"]):
        row_data = matrix_rows[r]
        vals = row_data["values"]
        is_dlq = ("Caída" in vals[0] or "Timeout" in vals[0])
        for c, cell in enumerate(row_cells):
            val = vals[c] if c < len(vals) else ""
            bg = MIRO_PALETTE["PAIN_BG"] if (is_dlq and c == 0) else "#FFFFFF"
            text_col = MIRO_PALETTE["PAIN_RED"] if (is_dlq and c == 0) else MIRO_PALETTE["INK"]
            scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], str(val),
                                 bg=bg, stroke=MIRO_PALETTE["CARD_BORDER"], text_color=text_col,
                                 font_size=12, roundness_type=None, frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)


    # =========================================================================
    # FRAME 4: CONTRATO DE DATOS, DOBLE PARTIDA EN LEDGER Y REGLAS DE AISLAMIENTO
    # =========================================================================
    w4, h4 = 3000, 750
    fx4, fy4 = place(w4, h4)
    fid4 = scene.add_frame("4. MODELO DE DATOS & LEDGER: Contrato de Solicitud, Doble Partida y Aislamiento", fx4, fy4, w4, h4)

    scene.add_text(fx4 + 50, fy4 + 35, "CONTRATO DE CARGA ÚTIL & MODELO FINANCIERO INMUTABLE", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
    scene.add_text(fx4 + 50, fy4 + 75, "especificación del payload JSON, estructura de asientos de balance y aislamiento de efectos secundarios", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid4)

    # 3 Cajas Principales
    col_w = 900
    col_h = 420
    start_c_y = fy4 + 130

    # Caja 1: Schema de Solicitud
    scene.add_rect(fx4 + 50, start_c_y, col_w, col_h, bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid4)
    scene.add_text(fx4 + 75, start_c_y + 20, "1. CONTRATO DE SOLICITUD (PAYLOAD SCHEMA):", font_size=15, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
    payload_str = """{
  "merchant_id": "mch_994812",
  "customer_id": "usr_440192",
  "amount": 14950,
  "currency": "USD",
  "payment_method": {
    "type": "credit_card",
    "token": "tok_visa_4242"
  },
  "order_id": "ord_88192301",
  "idempotency_key": "idem_a8f9-41bc-9901"
}"""
    scene.add_text(fx4 + 75, start_c_y + 60, payload_str, font_size=13, font_family=3, color="#1E293B", frame_id=fid4)

    # Caja 2: Asientos en Doble Partida del Ledger
    scene.add_rect(fx4 + 1000, start_c_y, col_w, col_h, bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid4)
    scene.add_text(fx4 + 1025, start_c_y + 20, "2. ESTRUCTURA DE ASIENTOS (DOUBLE-ENTRY LEDGER):", font_size=15, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
    ledger_str = """ASIENTO: Liquidación de Cobro (Capture)
--------------------------------------------------
CUENTA DEBITADA (DEBE):
• Activo / Fondos por Cobrar Pasarela: +$149.50

CUENTAS ACREDITADAS (HABER):
• Pasivo / Saldo Comercio (Merchant):  +$145.01
• Ingreso / Comisión Plataforma (Fee):   +$4.49

SUMA DEBE ($149.50) == SUMA HABER ($149.50)
* Regla Inmutable: Ningún asiento puede modificarse o
  borrarse. Las correcciones se asientan como Contrapartida."""
    scene.add_text(fx4 + 1025, start_c_y + 60, ledger_str, font_size=12, font_family=3, color="#1E293B", frame_id=fid4)

    # Caja 3: Reglas de Aislamiento y No-Bloqueo
    scene.add_rect(fx4 + 1950, start_c_y, col_w, col_h, bg=MIRO_PALETTE["PAIN_BG"], stroke=MIRO_PALETTE["PAIN_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid4)
    scene.add_text(fx4 + 1975, start_c_y + 20, "3. PRINCIPIOS DE AISLAMIENTO Y NO-BLOQUEO:", font_size=15, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid4)
    rules_str = """• FUENTE DE VERDAD: El Ledger es la única verdad.
  Si el Ledger dice que se cobró, el dinero existe.

• NOTIFICACIONES READ-ONLY:
  El Notification Service jamás muta estados en BD.
  Si un webhook falla, se reintenta sin tocar saldo.

• ANALYTICS EVENTUAL:
  El pipeline OLAP es 100% asíncrono. Un fallo en
  ClickHouse jamás rechaza ni retrasa un pago.

• IDEMPOTENCIA EN CONSUMIDORES:
  Todos los workers procesan eventos con 'At-Least-Once'.
  Verifican hash o id de evento antes de ejecutar."""
    scene.add_text(fx4 + 1975, start_c_y + 60, rules_str, font_size=13, font_family=2, color="#0C0C0C", frame_id=fid4)

    # Banner inferior
    scene.add_banner(fx4 + 50, fy4 + 580, w4 - 100, 50,
                     "la consistencia financiera se garantiza mediante inmutabilidad del ledger e idempotencia atómica en cada capa distribuida.",
                     bg=MIRO_PALETTE["BANNER_PINK"], text_color=MIRO_PALETTE["INK"], font_size=14, frame_id=fid4)

    scene.auto_fit_frame(fid4, padding=50.0)

    out_path = os.path.join(OUT_DIR, "plataforma_pagos_distribuida.excalidraw")
    scene.save(out_path)
    return out_path


if __name__ == "__main__":
    path = build_payment_platform_scene()
    print("==================================================")
    print("ESCENA DE PLATAFORMA DE PAGOS GENERADA:")
    print(f"Ruta: {path}")
    print("==================================================")
    scene_data, report = validate_scene(path)
    print(report.summary())
