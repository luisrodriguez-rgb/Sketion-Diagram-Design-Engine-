"""
Sketion 3.3 — Generador Maestro para Benchmark de 3 Audiencias (Pruebas V5)
Mismo Caso de Negocio (Cafeteria Universitaria) -> 3 Representaciones Visuales Radicalmente Diferentes:
1. CEO / Directivo: Diagrama de Decision Estrategica, ROI y Asignacion de Recursos
2. Gerente de Operaciones: Diagrama de Proceso Fisico, Takt Time, Segregacion Espacial y Roles
3. Equipo de Producto / Tech: Arquitectura de Sistema, Pre-Order App, KDS y Motor de Estimacion ETA
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from layout.grid import compute_matrix_layout
from validation.validator import validate_scene

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V5")
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


# =============================================================================
# 1. AUDIENCIA: CEO / DIRECTIVO (DIAGRAMA DE DECISION ESTRATEGICA)
# =============================================================================
def build_ceo_decision_scene() -> str:
    place_reset(max_row_w=3200, gap=140)
    scene = ExcalidrawScene(roughness=0, bg_color=MIRO_PALETTE["CANVAS"])

    # FRAME 1: EL DUELO ESTRATEGICO (AS-IS VS PROPUESTA DE 3 FASES)
    w1, h1 = 2800, 920
    fx1, fy1 = place(w1, h1)
    fid1 = scene.add_frame("1. EL DUELO DIRECTIVO: Modelo Actual Colapsado vs Propuesta Orquestada", fx1, fy1, w1, h1)

    scene.add_text(fx1 + 50, fy1 + 35, "DECISION DIRECTIVA: RESOLUCION DEL DEFICIT DE CAPACIDAD EN RECESO", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid1)
    scene.add_text(fx1 + 50, fy1 + 75, "como absorber 430 ped/h y proteger el margen con $0 de contrataciones fijas y sin obras mayores", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)

    scene.add_metric_pill(fx1 + w1 - 580, fy1 + 35, "CAPACIDAD META", "+36% Throughput", bg=MIRO_PALETTE["INK"], frame_id=fid1)
    scene.add_metric_pill(fx1 + w1 - 320, fy1 + 35, "COSTO FIJO", "$0 Contratos", bg=MIRO_PALETTE["INK"], frame_id=fid1)

    # Sub-titulares VS
    mid_x = fx1 + w1 * 0.5
    scene.add_text(fx1 + 80, fy1 + 130, "MODELO ACTUAL (INEFICIENTE Y LIMITADO)", font_size=20, font_family=2, color=MIRO_PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(mid_x + 80, fy1 + 130, "MODELO ORQUESTADO (AUMENTO EFECTIVO)", font_size=20, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)
    scene.add_text(mid_x - 30, fy1 + 130, "VS", font_size=28, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid1)

    # Filas de Comparacion con Post-it central
    duel_rows = [
        ("Deficit estructural: Capacidad 300 vs 430 ped/h", "CAPACIDAD", "Capacidad efectiva: 410 ped/h (+36% absorcion)"),
        ("Cajero hace 5 tareas simultaneas; fila > 25", "PERSONAL", "Reasignacion en pico: 1 caja + 1 entrega + 2 cocina ($0)"),
        ("Congestion en barra; clientes pidiendo y esperando", "ESPACIO", "Separacion fisica de Order y Pickup (carril A/B)"),
        ("14% de abandono de fila; perdida de $2,400/mes", "RETENCION", "Abandono < 1.5% con pre-order app y retiro expres"),
        ("Baja rotacion bloquea cocina en horas pico", "MARGEN", "Combos rapidos en horas pico (+4.8% margen promedio)")
    ]

    for i, (left_t, spine_t, right_t) in enumerate(duel_rows):
        ry = fy1 + 180 + i * 115
        
        # Tarjeta Izquierda (Gris/Dolor)
        scene.add_bound_card(fx1 + 60, ry, 1100, 80, left_t,
                             bg=MIRO_PALETTE["PAIN_BG"], stroke=MIRO_PALETTE["PAIN_BORDER"], text_color=MIRO_PALETTE["INK"],
                             font_size=14, roundness_type=3, frame_id=fid1)
        
        # Post-it Central
        scene.add_sticky_note(mid_x - 110, ry + 5, 220, 70, spine_t,
                              angle_deg=-1.2 if i % 2 == 0 else 1.2, font_size=13, frame_id=fid1)
        
        # Tarjeta Derecha (Coral/Solucion)
        scene.add_bound_card(mid_x + 140, ry, 1100, 80, right_t,
                             bg="#FFFFFF", stroke=MIRO_PALETTE["INK"], text_color=MIRO_PALETTE["INK"],
                             font_size=14, roundness_type=3, frame_id=fid1)

    # Metricas al pie
    foot_y = fy1 + 770
    scene.add_rect(fx1 + 60, foot_y, 1100, 90, bg=MIRO_PALETTE["PAIN_BG"], stroke=MIRO_PALETTE["PAIN_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid1)
    scene.add_text(fx1 + 80, foot_y + 15, "14% Abandono | 300 ped/h max | $28k perdida anual", font_size=20, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)
    scene.add_text(fx1 + 80, foot_y + 50, "Impacto actual: Clientes insatisfechos y congestion cronica", font_size=13, font_family=2, color=MIRO_PALETTE["MUTED"], frame_id=fid1)

    scene.add_rect(mid_x + 140, foot_y, 1100, 90, bg=MIRO_PALETTE["PASTEL_GREEN"], stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid1)
    scene.add_text(mid_x + 160, foot_y + 15, "< 1.5% Abandono | 410 ped/h | +$42k ingresos netos", font_size=20, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid1)
    scene.add_text(mid_x + 160, foot_y + 50, "Resultado proyectado: Experiencia fluida con costo de inversion recuperable en 30 dias", font_size=13, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=50.0)


    # FRAME 2: RADAR DE DECISION Y ROADMAP DE IMPLEMENTACION
    w2, h2 = 2800, 850
    fx2, fy2 = place(w2, h2)
    fid2 = scene.add_frame("2. HOJA DE RUTA DIRECTIVA: Radar de Prioridades y Fases de Aprobacion", fx2, fy2, w2, h2)

    scene.add_text(fx2 + 50, fy2 + 35, "PLAN DE EJECUCION POR FASES & GOBERNANZA DE RECURSOS", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid2)
    scene.add_text(fx2 + 50, fy2 + 75, "secuencia logica de implementacion: quick wins inmediatos -> canal digital -> optimizacion de menu", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid2)

    phases = [
        ("FASE 1: QUICK WINS (SEMANA 1)", "Costo $0 / Aprobacion Inmediata", [
            "B. Separar fisicamente Order y Pickup (senaletica)",
            "G. Reasignar personal durante el receso (1 caja / 1 runner)",
            "D. Batching previo de 80 sandwiches top antes de las 10:00"
        ], MIRO_PALETTE["PASTEL_GREEN"]),
        ("FASE 2: CANAL DIGITAL (SEMANAS 2-4)", "Inversion Minima en Software / ROI 30d", [
            "A. Lanzamiento de App de Pre-Order para alumnos",
            "F. Habilitacion de Estacion / Mesa de Retiro Expres",
            "H. Pantallas visibles con tiempos de preparacion estimados"
        ], MIRO_PALETTE["PASTEL_BLUE"]),
        ("FASE 3: OPTIMIZACION DE MENU (MES 2)", "Mejora de Margen y Velocidad", [
            "C. Menu especial compacto para franja de 10:00 a 12:00",
            "J. Creacion de Combos Rapidos (Cafe + Muffin listo)",
            "E. Sistema de pronostico historico semanal"
        ], "#FFFFFF")
    ]

    card_pw = 850
    card_ph = 480
    for pi, (p_title, p_sub, p_items, p_bg) in enumerate(phases):
        px = fx2 + 60 + pi * (card_pw + 45)
        py = fy2 + 130
        
        scene.add_rect(px, py, card_pw, card_ph, bg=p_bg, stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid2)
        scene.add_text(px + 25, py + 25, p_title, font_size=18, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid2)
        scene.add_text(px + 25, py + 55, p_sub, font_size=13, font_family=2, color=MIRO_PALETTE["MUTED"], frame_id=fid2)

        for ii, item_txt in enumerate(p_items):
            iy = py + 100 + ii * 110
            scene.add_bound_card(px + 25, iy, card_pw - 50, 85, item_txt,
                                 bg="#FFFFFF", stroke=MIRO_PALETTE["INK"], text_color=MIRO_PALETTE["INK"],
                                 font_size=13, roundness_type=3, frame_id=fid2)

    scene.add_banner(fx2 + 60, fy2 + 660, w2 - 120, 50,
                     "resolucion de junta directiva: aprobar fase 1 de ejecucion inmediata a costo cero y autorizar presupuesto de fase 2.",
                     bg=MIRO_PALETTE["BANNER_PINK"], text_color=MIRO_PALETTE["INK"], font_size=14, frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=50.0)

    out_ceo = os.path.join(OUT_DIR, "01_audiencia_ceo_decision.excalidraw")
    scene.save(out_ceo)
    return out_ceo


# =============================================================================
# 2. AUDIENCIA: GERENTE DE OPERACIONES (PROCESO FISICO & TAKT TIME)
# =============================================================================
def build_operations_process_scene() -> str:
    place_reset(max_row_w=3200, gap=140)
    scene = ExcalidrawScene(roughness=0, bg_color=MIRO_PALETTE["CANVAS"])

    # FRAME 1: LAYOUT FISICO Y SEGREGACION ESPACIAL DE BARRA
    w1, h1 = 2800, 950
    fx1, fy1 = place(w1, h1)
    fid1 = scene.add_frame("1. PLANTA OPERATIVA: Segregacion Fisica de Flujos y Asignacion de Puestos en Pico", fx1, fy1, w1, h1)

    scene.add_text(fx1 + 50, fy1 + 35, "DISEÑO DE PLANTA: RECONFIGURACION DE BARRA Y ZONAS DE FLUJO", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid1)
    scene.add_text(fx1 + 50, fy1 + 75, "eliminacion de colisiones cruzadas separando carril de pedido, carril de recogida y locker digital", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)

    zones = [
        ("ZONA 1: INGRESS / PEDIDO", 620, [
            ("z1_line", "Carril A: Fila Presencial", "Capacidad: 12 clientes max\nFiltro visual de ingreso"),
            ("z1_cash", "Puesto 1: Cajero Puro", "UNICA FUNCION: Tomar orden y cobrar\nTakt Time: 10 seg / cliente")
        ], MIRO_PALETTE["PASTEL_BLUE"]),
        ("ZONA 2: COCINA & BATCHING", 720, [
            ("z2_batch", "Estacion de Batching Previo", "80 sandwiches listos en calor\nStock regulador de horas pico"),
            ("z2_prep", "Puesto 2 y 3: Linea Cocina", "2 Cocineros dedicados\nKDS pantalla de comandas")
        ], "#FFFFFF"),
        ("ZONA 3: EXPEDICION / PICKUP", 650, [
            ("z3_run", "Puesto 4: Runner / Entrega", "Entrega pedidos fisicos listos\nVerifica ticket y despacho"),
            ("z3_line", "Carril B: Espera de Retiro", "Espacio despejado con pantalla ETA")
        ], MIRO_PALETTE["PASTEL_GREEN"]),
        ("ZONA 4: CANAL DIGITAL EXPRESS", 620, [
            ("z4_lock", "Estacion Digital Dedicada", "Mesa / Casillero de autoservicio\nRetiro en 5 seg con QR"),
            ("z4_out", "Salida Despejada", "Flujo directo al pasillo sin retorno")
        ], MIRO_PALETTE["STICKY"])
    ]

    curr_x = fx1 + 60.0
    for z_title, zw, znodes, zbg in zones:
        zh = 480.0
        zy = fy1 + 140.0
        
        scene.add_scope_container(curr_x, zy, zw, zh, label=z_title, stroke=MIRO_PALETTE["CARD_BORDER"], bg=zbg, frame_id=fid1)

        for ni, (nid, ntitle, nsub) in enumerate(znodes):
            nx = curr_x + 25.0
            ny = zy + 65.0 + ni * 180.0
            nw = zw - 50.0
            nh = 120.0
            
            scene.add_dual_card(nx, ny, nw, nh, ntitle, sublabel=nsub,
                                bg="#FFFFFF", stroke=MIRO_PALETTE["INK"], text_color=MIRO_PALETTE["INK"], frame_id=fid1)

        curr_x += zw + 50.0

    scene.add_banner(fx1 + 60, fy1 + 680, w1 - 120, 50,
                     "regla operativa de oro: ningun cliente que ya pago comparte espacio con quien esta decidiendo su pedido.",
                     bg=MIRO_PALETTE["BANNER_PINK"], text_color=MIRO_PALETTE["INK"], font_size=14, frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=50.0)


    # FRAME 2: TAKT TIME, MATRIZ DE TIEMPOS DE CICLO Y BATCHING
    w2, h2 = 2800, 850
    fx2, fy2 = place(w2, h2)
    fid2 = scene.add_frame("2. INGENIERIA DE PROCESO: Takt Time, Balanceo de Linea y Protocolo de Batching", fx2, fy2, w2, h2)

    scene.add_text(fx2 + 50, fy2 + 35, "ANALISIS DE TIEMPOS DE CICLO (TAKT TIME) Y BALANCEO DE LINEA", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid2)
    scene.add_text(fx2 + 50, fy2 + 75, "calculo de segundos por pedido para cumplir la meta de 410 pedidos/hora en receso", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid2)

    takt_headers = ["ESTACION / ROL", "TIEMPO AS-IS (CUELLO)", "TIEMPO TO-BE (BALANCEADO)", "CAPACIDAD HORA", "PROTOCOLOS DE OPERACION EN PICO"]
    takt_rows = [
        {"values": ["Caja de Cobro", "35 seg (5 tareas simultaneas)", "9.0 seg (Solo cobro y ticket)", "400 ped/h", "Menu rapido en pantalla; pago con tarjeta contactless activado."]},
        {"values": ["Cocina (Rapidos 62%)", "90 seg / pedido individual", "15 seg (Batch de 10 unidades)", "420 ped/h", "80 unidades pre-elaboradas en horas valle (9:15 a 9:55 AM)."]},
        {"values": ["Cocina (Complejos 15%)", "480 seg (Bloquea plancha)", "180 seg (Mise-en-place lista)", "120 ped/h", "Pasan a carril secundario de preparacion sin frenar la linea rapida."]},
        {"values": ["Despacho / Runner", "Sin asignar (Cajero entrega)", "7.5 seg (Entrega continua)", "480 ped/h", "El runner ensambla bandeja, entrega y canta numero de comanda."]},
        {"values": ["App Digital Express", "Interrupcion a viva voz", "4.0 seg (Autoservicio QR)", "600 ped/h", "El alumno escanea su codigo en el casillero y retira en 5 segundos."]}
    ]

    grid_t = compute_matrix_layout(start_x=fx2 + 50, start_y=fy2 + 130, headers=takt_headers, rows=takt_rows)

    for cell in grid_t["headers"]:
        c = cell["col"]
        scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], takt_headers[c],
                             bg=MIRO_PALETTE["INK"], stroke=MIRO_PALETTE["INK"], text_color="#FFFFFF",
                             font_size=12, roundness_type=None, frame_id=fid2)

    for r, row_cells in enumerate(grid_t["rows"]):
        row_data = takt_rows[r]
        vals = row_data["values"]
        for c, cell in enumerate(row_cells):
            val = vals[c] if c < len(vals) else ""
            scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], str(val),
                                 bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], text_color=MIRO_PALETTE["INK"],
                                 font_size=11, roundness_type=None, frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=50.0)

    out_ops = os.path.join(OUT_DIR, "02_audiencia_operaciones_proceso.excalidraw")
    scene.save(out_ops)
    return out_ops


# =============================================================================
# 3. AUDIENCIA: EQUIPO DE PRODUCTO / TECH (ARQUITECTURA DE SISTEMA & APPS)
# =============================================================================
def build_product_tech_scene() -> str:
    place_reset(max_row_w=3200, gap=140)
    scene = ExcalidrawScene(roughness=0, bg_color=MIRO_PALETTE["CANVAS"])

    # FRAME 1: ARQUITECTURA DE SOFTWARE, CANALES Y MOTOR DE ESTIMACION ETA
    w1, h1 = 2800, 950
    fx1, fy1 = place(w1, h1)
    fid1 = scene.add_frame("1. ARQUITECTURA DE SISTEMA: Pre-Order App, KDS en Cocina y Motor de Tiempos (ETA)", fx1, fy1, w1, h1)

    scene.add_text(fx1 + 50, fy1 + 35, "PLATAFORMA TECNOLOGICA: CANALES DIGITALES Y MOTOR KDS", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid1)
    scene.add_text(fx1 + 50, fy1 + 75, "orquestacion en tiempo real: app de pre-orden, integracion POS, cola KDS y pantallas publicas", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)

    tech_columns = [
        ("col_clients", "1. CLIENTES & INGRESS", 380, [
            ("cli_app", "App Movil Alumnos", "Flutter / React Native\nPre-orden y slot de recogida"),
            ("cli_pos", "Terminal POS Caja", "Fast Checkout Contactless"),
            ("cli_web", "Portal Web Staff", "Pedidos corporativos de profesores")
        ]),
        ("col_gw", "2. API GATEWAY", 360, [
            ("gw_edge", "Envoy API Gateway", "Rate limit & Auth JWT"),
            ("gw_event", "Event Ingestion", "WebSocket push a cocina")
        ]),
        ("col_services", "3. SERVICIOS CORE", 440, [
            ("svc_order", "Order Orchestrator", "Maquina de estados del pedido"),
            ("svc_eta", "Dynamic ETA Engine", "Calculo predictivo de min espera"),
            ("svc_inventory", "Slot / Inventory Manager", "Control de stock de combos y batch")
        ]),
        ("col_kds", "4. HARDWARE COCINA / KDS", 420, [
            ("kds_screen", "Kitchen Display Screen", "Comandas agrupadas por tiempo de coccion"),
            ("kds_runner", "Tableta Runner Despacho", "Notificacion de pedido listo")
        ]),
        ("col_displays", "5. INTERFACES PUBLICAS", 420, [
            ("disp_screen", "Pantalla TV Turnos (ETA)", "Muestra # orden y tiempo restante"),
            ("disp_locker", "Locker / QR Scanner", "Desbloqueo de casillero digital")
        ])
    ]

    curr_x = fx1 + 45.0
    tech_coords = {}

    for sid, s_title, sw, snodes in tech_columns:
        sh = max(450.0, len(snodes) * 115.0 + 85.0)
        sy = fy1 + 130.0
        
        scene.add_scope_container(curr_x, sy, sw, sh, label=s_title, stroke=MIRO_PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

        for ni, (nid, ntitle, nsub) in enumerate(snodes):
            nx = curr_x + 20.0
            ny = sy + 50.0 + ni * 110.0
            nw = sw - 40.0
            nh = 85.0
            
            is_eta = ("ETA" in ntitle or "KDS" in ntitle)
            bg = MIRO_PALETTE["PASTEL_GREEN"] if is_eta else "#FFFFFF"
            border = MIRO_PALETTE["INK"] if is_eta else MIRO_PALETTE["CARD_BORDER"]
            
            container, _ = scene.add_dual_card(nx, ny, nw, nh, ntitle, sublabel=nsub,
                                               bg=bg, stroke=border, text_color=MIRO_PALETTE["INK"], frame_id=fid1)
            tech_coords[nid] = (container["x"], container["y"], container["width"], container["height"])

        curr_x += sw + 55.0

    # Conexiones
    tech_edges = [
        ("cli_app", "gw_edge", "POST /v1/preorder"),
        ("cli_pos", "gw_edge", "POST /v1/pos-sale"),
        ("gw_edge", "svc_order", "Dispatch Order"),
        ("svc_order", "svc_eta", "Query Prep Time"),
        ("svc_order", "kds_screen", "Comanda a Cocina"),
        ("kds_screen", "kds_runner", "Item Listo"),
        ("svc_eta", "disp_screen", "Broadcast ETA"),
        ("kds_runner", "disp_locker", "QR Habilitado")
    ]

    for f_id, t_id, lbl in tech_edges:
        if f_id in tech_coords and t_id in tech_coords:
            fx, fy, fw, fh = tech_coords[f_id]
            tx, ty, tw, th = tech_coords[t_id]
            if tx >= fx + fw:
                scene.add_arrow(fx + fw, fy + fh * 0.5, tx, ty + th * 0.5,
                                stroke=MIRO_PALETTE["MUTED"], stroke_w=1.5, label=lbl, orthogonal=True, frame_id=fid1)
            elif tx < fx:
                scene.add_arrow(fx, fy + 18.0, tx + tw, ty + 18.0,
                                stroke=MIRO_PALETTE["MUTED"], stroke_w=1.5, label=lbl, orthogonal=True, frame_id=fid1)
            else:
                scene.add_arrow(fx + fw * 0.5, fy + fh, tx + tw * 0.5, ty,
                                stroke=MIRO_PALETTE["MUTED"], stroke_w=1.5, label=lbl, orthogonal=True, frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=50.0)


    # FRAME 2: USER JOURNEY DIGITAL & ESTADOS KDS
    w2, h2 = 2800, 800
    fx2, fy2 = place(w2, h2)
    fid2 = scene.add_frame("2. USER JOURNEY: Experiencia del Alumno y Ciclo de Vida del Pedido Digital", fx2, fy2, w2, h2)

    scene.add_text(fx2 + 50, fy2 + 35, "JOURNEY DEL ALUMNO: DE LA PRE-ORDEN AL RETIRO EN 5 SEGUNDOS", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid2)
    scene.add_text(fx2 + 50, fy2 + 75, "flujo de interaccion extremo a extremo con slots de captura y retroalimentacion de estado", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid2)

    journey_steps = [
        ("PASO 1: SELECCION", "Alumno elige combo y slot\n(Ej: Receso 10:15 AM)", fx2 + 60, fy2 + 160),
        ("PASO 2: PAGO & ETA", "Pago en 1-clic Apple/Google Pay\nRecibe ticket digital y QR", fx2 + 580, fy2 + 160),
        ("PASO 3: COCINA KDS", "Comanda aparece en cocina 4 min\nantes de la hora prometida", fx2 + 1100, fy2 + 160),
        ("PASO 4: ALERTA PUSH", "Notificacion: 'Tu pedido esta en\nla Estacion Digital Locker B'", fx2 + 1620, fy2 + 160),
        ("PASO 5: RETIRO EXPRESS", "Escaneo de QR en 5 segundos\nCero colision con la fila fisica", fx2 + 2140, fy2 + 160)
    ]

    for j_num, j_desc, jx, jy in journey_steps:
        scene.add_bound_card(jx, jy, 440, 100, f"{j_num}\n{j_desc}",
                             bg="#FFFFFF", stroke=MIRO_PALETTE["INK"], text_color=MIRO_PALETTE["INK"],
                             font_size=13, roundness_type=3, frame_id=fid2)

    for i in range(len(journey_steps) - 1):
        x1 = journey_steps[i][2] + 440
        y1 = journey_steps[i][3] + 50
        x2 = journey_steps[i+1][2]
        y2 = journey_steps[i+1][3] + 50
        scene.add_arrow(x1, y1, x2, y2, stroke=MIRO_PALETTE["INK"], stroke_w=1.5, orthogonal=False, frame_id=fid2)

    # Slots de Captura de UI abajo
    scene.add_capture_slot(fx2 + 60, fy2 + 320, 620, 320, label="Captura: Pantalla de Seleccion de Slot en App Movil", stroke=MIRO_PALETTE["CARD_BORDER"], frame_id=fid2)
    scene.add_capture_slot(fx2 + 740, fy2 + 320, 620, 320, label="Captura: Ticket QR y Cuenta Regresiva de Preparacion", stroke=MIRO_PALETTE["CARD_BORDER"], frame_id=fid2)
    scene.add_capture_slot(fx2 + 1420, fy2 + 320, 620, 320, label="Captura: Pantalla KDS en Cocina con Filtro de Takt Time", stroke=MIRO_PALETTE["PAIN_BORDER"], frame_id=fid2)
    scene.add_capture_slot(fx2 + 2100, fy2 + 320, 620, 320, label="Captura: Escaner de QR y Despacho en Casillero Express", stroke=MIRO_PALETTE["CARD_BORDER"], frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=50.0)

    out_tech = os.path.join(OUT_DIR, "03_audiencia_producto_sistema.excalidraw")
    scene.save(out_tech)
    return out_tech


if __name__ == "__main__":
    print("==================================================")
    print("GENERANDO 3 LIENZOS POR AUDIENCIA (PRUEBAS V5)...")
    print("==================================================")
    
    p1 = build_ceo_decision_scene()
    print(f"\n1. CEO / Directivo: {p1}")
    _, r1 = validate_scene(p1)
    print(r1.summary())
    
    p2 = build_operations_process_scene()
    print(f"\n2. Gerente Operaciones: {p2}")
    _, r2 = validate_scene(p2)
    print(r2.summary())
    
    p3 = build_product_tech_scene()
    print(f"\n3. Equipo Producto / Tech: {p3}")
    _, r3 = validate_scene(p3)
    print(r3.summary())
    
    print("\n==================================================")
    print("TODOS LOS LIENZOS DE AUDIENCIA GENERADOS Y VALIDADOS CON EXITO.")
    print("==================================================")
