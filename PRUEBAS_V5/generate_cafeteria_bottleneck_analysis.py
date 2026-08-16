"""
Sketion 3.3 — Generador Maestro para Analisis de Cuellos de Botella en Cafeteria Universitaria (Pruebas V4)
Composicion Multi-Frame Ejecutiva para Equipo Directivo:
- Frame 1: Diagnostico As-Is (Flujo Operativo, Mezcla de Demanda y Deficit de Capacidad)
- Frame 2: Analisis de Causa Raiz Causal (Arquetipo M: Espina de Ishikawa)
- Frame 3: Matriz de Evaluacion de 10 Alternativas (A-J), Trade-offs y Restricciones
- Frame 4: Plan de Accion Priorizado (Radar 2x2 Impacto vs Esfuerzo) y Dashboard de KPIs de Exito
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place
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


def build_cafeteria_analysis_scene() -> str:
    place_reset(max_row_w=3200, gap=140)
    scene = ExcalidrawScene(roughness=0, bg_color=MIRO_PALETTE["CANVAS"])

    # =========================================================================
    # FRAME 1: DIAGNOSTICO AS-IS (FLUJO OPERATIVO Y DEFICIT ESTRUCTURAL)
    # =========================================================================
    w1, h1 = 3000, 1050
    fx1, fy1 = place(w1, h1)
    fid1 = scene.add_frame("1. DIAGNOSTICO AS-IS: Flujo Operativo, Canales de Entrada y Deficit de Capacidad", fx1, fy1, w1, h1)

    scene.add_text(fx1 + 50, fy1 + 35, "DIAGNOSTICO OPERATIVO: FLUJO AS-IS Y CUELLOS DE BOTELLA", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid1)
    scene.add_text(fx1 + 50, fy1 + 75, "deficit estructural de -130 ped/h en receso, multifuncion en caja y colapso de espacio fisico", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)

    # Top Metric Pills
    scene.add_metric_pill(fx1 + w1 - 620, fy1 + 35, "DEMANDA PICO", "430 Pedidos / Hora", bg=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)
    scene.add_metric_pill(fx1 + w1 - 320, fy1 + 35, "CAPACIDAD", "300 Pedidos / Hora", bg=MIRO_PALETTE["INK"], frame_id=fid1)

    # Scopes / Columnas de Flujo
    scopes_data = [
        ("col_channels", "1. CANALES DE ENTRADA", 380, [
            ("node_phys", "Fila Fisica (71%)", "Llegan directo sin pedido previo\nFila supera 25 personas"),
            ("node_dig", "App Digital (19%)", "Horas de recogida variables\nSe acumulan sin aviso"),
            ("node_intern", "Interno / Staff (10%)", "Profesores y eventos")
        ]),
        ("col_cashier", "2. CUELLO DE BOTELLA: CAJA", 440, [
            ("node_cash_overload", "Cajero (5 Tareas en 1)", "1. Toma pedido | 2. Cobra\n3. Responde dudas | 4. Entrega\n5. Resuelve fallos de pago")
        ]),
        ("col_kitchen", "3. COCINA & PRODUCCION", 460, [
            ("node_deficit", "Deficit de Capacidad (-130/h)", "Capacidad: 300 ped/h\nDemanda: 430 ped/h"),
            ("node_mix", "Mezcla de Preparacion", "62% < 4 min (Rapidos)\n23% 4-8 min | 15% > 8 min (Lentos)")
        ]),
        ("col_pickup", "4. ZONA DE CONGESTION", 420, [
            ("node_space_mix", "Espacio Sin Separacion", "Clientes para pedir, recoger y\nya atendidos colisionan"),
            ("node_blind", "Cero Visibilidad de Tiempos", "Clientes no saben tiempo de espera")
        ]),
        ("col_impact", "5. SINTOMA / IMPACTO", 400, [
            ("node_abandon", "Abandono de Fila", "Clientes se van sin comprar\nPerdida directa de ingresos"),
            ("node_friction", "Tiempos Desproporcionados", "Fila > 25 dispara espera no lineal")
        ])
    ]

    curr_x = fx1 + 45.0
    nodes_coords = {}

    for sid, s_title, sw, snodes in scopes_data:
        sh = max(450.0, len(snodes) * 115.0 + 85.0)
        sy = fy1 + 130.0
        
        scene.add_scope_container(curr_x, sy, sw, sh, label=s_title, stroke=MIRO_PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

        for ni, (nid, ntitle, nsub) in enumerate(snodes):
            nx = curr_x + 20.0
            ny = sy + 50.0 + ni * 110.0
            nw = sw - 40.0
            nh = 85.0
            
            is_pain = ("Deficit" in ntitle or "Cajero" in ntitle or "Abandono" in ntitle or "Sin Separacion" in ntitle)
            bg = MIRO_PALETTE["PAIN_BG"] if is_pain else "#FFFFFF"
            border = MIRO_PALETTE["PAIN_BORDER"] if is_pain else MIRO_PALETTE["CARD_BORDER"]
            text_col = MIRO_PALETTE["PAIN_RED"] if is_pain else MIRO_PALETTE["INK"]
            
            container, _ = scene.add_dual_card(nx, ny, nw, nh, ntitle, sublabel=nsub,
                                               bg=bg, stroke=border, text_color=text_col, frame_id=fid1)
            nodes_coords[nid] = (container["x"], container["y"], container["width"], container["height"])

        curr_x += sw + 55.0

    # Conectores
    edges = [
        ("node_phys", "node_cash_overload", "Fila fisica"),
        ("node_dig", "node_deficit", "Orden digital directa"),
        ("node_intern", "node_deficit", "Ticket interno"),
        ("node_cash_overload", "node_deficit", "Carga a cocina"),
        ("node_deficit", "node_mix", "Encola pedidos"),
        ("node_mix", "node_space_mix", "Platos listos"),
        ("node_space_mix", "node_blind", "Sin avisos"),
        ("node_cash_overload", "node_abandon", "Fila > 25 personas"),
        ("node_space_mix", "node_friction", "Congestion mutua")
    ]

    for f_id, t_id, lbl in edges:
        if f_id in nodes_coords and t_id in nodes_coords:
            fx, fy, fw, fh = nodes_coords[f_id]
            tx, ty, tw, th = nodes_coords[t_id]
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
    # FRAME 2: ANALISIS DE CAUSA RAIZ (ARQUETIPO M: ESPINA DE ISHIKAWA)
    # =========================================================================
    w2, h2 = 3000, 1000
    fx2, fy2 = place(w2, h2)
    fid2 = scene.add_frame("2. ANALISIS DE CAUSA RAIZ: Diagrama de Ishikawa de Congestion y Abandono", fx2, fy2, w2, h2)

    scene.add_text(fx2 + 50, fy2 + 35, "MODELO CAUSAL: ESPINA DE ISHIKAWA DE COLAPSO EN RECESO", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid2)
    scene.add_text(fx2 + 50, fy2 + 75, "descomposicion de causas raiz en personas, procesos, capacidad y espacio fisico", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid2)

    # Eje Central de Ishikawa
    axis_y = fy2 + 480.0
    scene.add_line(fx2 + 100, axis_y, fx2 + 2250, axis_y, stroke=MIRO_PALETTE["INK"], stroke_w=3.0, frame_id=fid2)

    # Cabeza del Pescado (Problema Terminal a la Derecha)
    head_w, head_h = 480, 160
    head_x, head_y = fx2 + 2280, axis_y - head_h * 0.5
    scene.add_rect(head_x, head_y, head_w, head_h, bg=MIRO_PALETTE["PAIN_BG"], stroke=MIRO_PALETTE["PAIN_BORDER"], stroke_w=2.0, roundness_type=3, frame_id=fid2)
    scene.add_text(head_x + 25, head_y + 25, "PROBLEMA TERMINAL:", font_size=14, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid2)
    scene.add_text(head_x + 25, head_y + 55, "COLAPSO EN RECESO,\nFILA > 25 PERSONAS Y\nABANDONO DE CLIENTES", font_size=20, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid2)

    # 4 Ramas Principales (Costillas)
    ribs = [
        # Rama Superior Izquierda: PERSONAS & ROLES
        ("1. PERSONAS & ROLES", fx2 + 250, fy2 + 160, fx2 + 650, axis_y, [
            "Cajero con 5 tareas simultaneas (cobra, entrega, dudas)",
            "Personal de cocina desbordado sin apoyo en horas pico",
            "Cero distribucion flexible de funciones durante receso"
        ], True),
        # Rama Superior Derecha: PROCESOS & PRIORIZACION
        ("2. PROCESOS & CANALES", fx2 + 1200, fy2 + 160, fx2 + 1600, axis_y, [
            "71% llega sin pedido previo por falta de canal digital activo",
            "Prioridad variable entre pedidos digitales y fisicos",
            "Falta de informacion historica para predecir demanda"
        ], True),
        # Rama Inferior Izquierda: PRODUCTO & CAPACIDAD
        ("3. PRODUCTO & CAPACIDAD", fx2 + 250, fy2 + 820, fx2 + 650, axis_y, [
            "Deficit estructural: Capacidad 300 vs Demanda 430 ped/h",
            "15% de productos tardan > 8 min y bloquean cocina",
            "Productos de alto margen requieren preparacion lenta"
        ], False),
        # Rama Inferior Derecha: ESPACIO & VISIBILIDAD
        ("4. ESPACIO & VISIBILIDAD", fx2 + 1200, fy2 + 820, fx2 + 1600, axis_y, [
            "Sin separacion fisica entre 'Pedir' y 'Recoger'",
            "Clientes no tienen visibilidad del tiempo estimado",
            "Aglomeracion cruzada frente a la barra de despacho"
        ], False)
    ]

    for cat_title, box_x, box_y, rib_end_x, rib_end_y, causes, is_top in ribs:
        # Tarjeta de Categoria
        scene.add_bound_card(box_x, box_y, 420, 45, cat_title,
                             bg=MIRO_PALETTE["INK"], stroke=MIRO_PALETTE["INK"], text_color="#FFFFFF",
                             font_size=13, roundness_type=3, frame_id=fid2)
        
        # Linea diagonal de costilla hacia el eje
        start_y = box_y + 45 if is_top else box_y
        scene.add_arrow(box_x + 210, start_y, rib_end_x, rib_end_y,
                        stroke=MIRO_PALETTE["MUTED"], stroke_w=2.0, orthogonal=False, frame_id=fid2)

        # Tarjetas de sub-causas flotantes
        for ci, cause_txt in enumerate(causes):
            cx = box_x + 40
            cy = (box_y + 60 + ci * 65) if is_top else (box_y - 190 + ci * 65)
            scene.add_bound_card(cx, cy, 380, 55, cause_txt,
                                 bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], text_color=MIRO_PALETTE["INK"],
                                 font_size=11, roundness_type=3, frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=60.0)


    # =========================================================================
    # FRAME 3: MATRIZ DE EVALUACION DE 10 ALTERNATIVAS (A - J) Y RESTRICCIONES
    # =========================================================================
    w3, h3 = 3000, 1100
    fx3, fy3 = place(w3, h3)
    fid3 = scene.add_frame("3. MATRIZ DE ALTERNATIVAS: Evaluacion de 10 Opciones frente a 5 Restricciones", fx3, fy3, w3, h3)

    scene.add_text(fx3 + 50, fy3 + 35, "MATRIZ DE ALTERNATIVAS, RESTRICCIONES & TRADE-OFFS (A - J)", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid3)
    scene.add_text(fx3 + 50, fy3 + 75, "evaluacion sistematica de impacto, factibilidad y cumplimiento de restricciones directivas", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid3)

    matrix_headers = [
        "ID & ALTERNATIVA",
        "DESCRIPCION OPERATIVA",
        "IMPACTO EN CAPACIDAD",
        "CUMPLIMIENTO DE RESTRICCIONES",
        "TRADE-OFF / RIESGO ASOCIADO",
        "DICTAMEN"
    ]

    matrix_rows = [
        {"values": ["A. Pedidos Anticipados", "App para pedir antes de receso y asignar slot", "Alto (+25% throughput)", "100% (Sin espacio ni contratacion)", "Requiere adopcion digital del cliente", "PRIORIDAD 1"]},
        {"values": ["B. Separar Order & Pickup", "Reorganizar barra: Carril A (Pide) / Carril B (Recoge)", "Muy Alto (-40% congestions)", "100% (Mismo espacio fisico reconfigurado)", "Costo minimo de senaletica y pintura", "PRIORIDAD 1 (Quick Win)"]},
        {"values": ["C. Menu Especial Pico", "Carta compacta en receso con platos < 4 min", "Alto (+30% velocidad cocina)", "Cumple (Reduccion solo temporal de 10-12h)", "Perdida de variedad por 2 horas", "PRIORIDAD 2"]},
        {"values": ["D. Batching Anticipado", "Pre-armar 80 sandwiches/cafes top antes del pico", "Muy Alto (+35% salida inmediata)", "100% (Usa horas valle previas)", "Riesgo de merma si la demanda no compra", "PRIORIDAD 1"]},
        {"values": ["E. Pronostico Historico", "Ajustar produccion segun datos de dias pasados", "Medio (+15% planificacion)", "100% (Solo software / planilla)", "Requiere disciplina de registro", "PRIORIDAD 2"]},
        {"values": ["F. Estacion Digital Dedicada", "Mesa/locker exclusivo para entrega rapida digital", "Alto (Descongestiona fila 19%)", "Cumple (Ocupa 1.5m de barra actual)", "Ninguno significativo", "PRIORIDAD 1"]},
        {"values": ["G. Reasignacion de Personal", "Durante receso: 1 en caja, 1 apoyo entrega, 2 cocina", "Muy Alto (Elimina cuello de caja)", "100% (Cero contrataciones adicionales)", "Exige capacitacion cruzada del equipo", "PRIORIDAD 1 (Quick Win)"]},
        {"values": ["H. Pantallas de Espera", "Monitor visible con numero de orden y min estimados", "Medio (Reduce ansiedad y abandono)", "100% (Hardware de bajo coste)", "No aumenta velocidad de cocina per se", "PRIORIDAD 2"]},
        {"values": ["I. Eliminar Baja Rotacion", "Borrar permanentemente platos de preparacion > 8m", "Bajo en pico / Alto riesgo", "INCUMPLE (Directiva prohibe reducir menu)", "Dano a satisfaccion de clientes fijos", "DESCARTADA"]},
        {"values": ["J. Combos Rapidos", "Paquetes cerrados (Cafe + Muffin listo)", "Alto (+20% rapidez de eleccion)", "100% (Mejora ticket promedio)", "Requiere stock suficiente de combos", "PRIORIDAD 2"]}
    ]

    grid = compute_matrix_layout(start_x=fx3 + 50, start_y=fy3 + 125, headers=matrix_headers, rows=matrix_rows)

    for cell in grid["headers"]:
        c = cell["col"]
        scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], matrix_headers[c],
                             bg=MIRO_PALETTE["INK"], stroke=MIRO_PALETTE["INK"], text_color="#FFFFFF",
                             font_size=12, roundness_type=None, frame_id=fid3)

    for r, row_cells in enumerate(grid["rows"]):
        row_data = matrix_rows[r]
        vals = row_data["values"]
        is_prio1 = ("PRIORIDAD 1" in vals[5])
        is_discard = ("DESCARTADA" in vals[5])
        
        for c, cell in enumerate(row_cells):
            val = vals[c] if c < len(vals) else ""
            bg = MIRO_PALETTE["PASTEL_GREEN"] if (is_prio1 and c == 5) else (MIRO_PALETTE["PAIN_BG"] if is_discard else "#FFFFFF")
            text_col = MIRO_PALETTE["INK"] if not is_discard else MIRO_PALETTE["PAIN_RED"]
            scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], str(val),
                                 bg=bg, stroke=MIRO_PALETTE["CARD_BORDER"], text_color=text_col,
                                 font_size=11, roundness_type=None, frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)


    # =========================================================================
    # FRAME 4: PLAN DE ACCION PRIORIZADO (RADAR 2X2) Y DASHBOARD DE KPIS
    # =========================================================================
    w4, h4 = 3000, 1000
    fx4, fy4 = place(w4, h4)
    fid4 = scene.add_frame("4. PLAN DE ACCION: Radar 2x2 Impacto vs Esfuerzo y Dashboard de Metricas de Exito", fx4, fy4, w4, h4)

    scene.add_text(fx4 + 50, fy4 + 35, "PLAN DE IMPLEMENTACION DIRECTIVA & METRICAS DE EXITO", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
    scene.add_text(fx4 + 50, fy4 + 75, "fase 1 de quick wins inmediatos a costo cero y validacion cuantitativa de resultados", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid4)

    # Radar 2x2 a la Izquierda
    radar_x = fx4 + 50
    radar_y = fy4 + 130
    radar_w = 1350
    radar_h = 560

    # Fondo del Radar
    scene.add_rect(radar_x, radar_y, radar_w, radar_h, bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid4)
    
    # Ejes Cartesianos
    mid_rx = radar_x + radar_w * 0.5
    mid_ry = radar_y + radar_h * 0.5
    scene.add_line(radar_x + 30, mid_ry, radar_x + radar_w - 30, mid_ry, stroke=MIRO_PALETTE["MUTED"], stroke_w=1.5, dashed=True, frame_id=fid4)
    scene.add_line(mid_rx, radar_y + 30, mid_rx, radar_y + radar_h - 30, stroke=MIRO_PALETTE["MUTED"], stroke_w=1.5, dashed=True, frame_id=fid4)

    # Titulos de Cuadrantes
    # Q1: Alto Impacto / Bajo Esfuerzo (Quick Wins)
    scene.add_rect(radar_x + 20, radar_y + 20, radar_w * 0.5 - 30, radar_h * 0.5 - 30, bg=MIRO_PALETTE["PASTEL_GREEN"], stroke="transparent", frame_id=fid4)
    scene.add_text(radar_x + 35, radar_y + 35, "QUICK WINS (ALTO IMPACTO / BAJO ESFUERZO):", font_size=13, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
    scene.add_bound_card(radar_x + 35, radar_y + 65, 270, 50, "B. Separar Order / Pickup", bg="#FFFFFF", stroke=MIRO_PALETTE["INK"], text_color=MIRO_PALETTE["INK"], font_size=11, frame_id=fid4)
    scene.add_bound_card(radar_x + 320, radar_y + 65, 270, 50, "G. Reasignar Personal en Pico", bg="#FFFFFF", stroke=MIRO_PALETTE["INK"], text_color=MIRO_PALETTE["INK"], font_size=11, frame_id=fid4)
    scene.add_bound_card(radar_x + 35, radar_y + 130, 270, 50, "D. Batching Previo de Top 5", bg="#FFFFFF", stroke=MIRO_PALETTE["INK"], text_color=MIRO_PALETTE["INK"], font_size=11, frame_id=fid4)

    # Q2: Alto Impacto / Alto Esfuerzo (Proyectos Clave)
    scene.add_rect(mid_rx + 10, radar_y + 20, radar_w * 0.5 - 30, radar_h * 0.5 - 30, bg=MIRO_PALETTE["PASTEL_BLUE"], stroke="transparent", frame_id=fid4)
    scene.add_text(mid_rx + 25, radar_y + 35, "PROYECTOS ESTRATEGICOS (ALTO ESFUERZO):", font_size=13, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
    scene.add_bound_card(mid_rx + 25, radar_y + 65, 270, 50, "A. App Pedidos Anticipados", bg="#FFFFFF", stroke=MIRO_PALETTE["INK"], text_color=MIRO_PALETTE["INK"], font_size=11, frame_id=fid4)
    scene.add_bound_card(mid_rx + 310, radar_y + 65, 270, 50, "F. Estacion Digital Dedicada", bg="#FFFFFF", stroke=MIRO_PALETTE["INK"], text_color=MIRO_PALETTE["INK"], font_size=11, frame_id=fid4)

    # Q3: Bajo Impacto / Bajo Esfuerzo (Mejoras Incrementales)
    scene.add_text(radar_x + 35, mid_ry + 20, "MEJORAS INCREMENTALES:", font_size=13, font_family=2, color=MIRO_PALETTE["MUTED"], frame_id=fid4)
    scene.add_bound_card(radar_x + 35, mid_ry + 50, 270, 50, "E. Pronostico Historico", bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], text_color=MIRO_PALETTE["INK"], font_size=11, frame_id=fid4)
    scene.add_bound_card(radar_x + 320, mid_ry + 50, 270, 50, "J. Combos Rapidos", bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], text_color=MIRO_PALETTE["INK"], font_size=11, frame_id=fid4)

    # Q4: Bajo Impacto / Alto Esfuerzo (Descartadas)
    scene.add_rect(mid_rx + 10, mid_ry + 10, radar_w * 0.5 - 30, radar_h * 0.5 - 30, bg=MIRO_PALETTE["PAIN_BG"], stroke="transparent", frame_id=fid4)
    scene.add_text(mid_rx + 25, mid_ry + 20, "DESCARTADAS / ALTO RIESGO:", font_size=13, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid4)
    scene.add_bound_card(mid_rx + 25, mid_ry + 50, 290, 50, "I. Eliminar Baja Rotacion", bg="#FFFFFF", stroke=MIRO_PALETTE["PAIN_BORDER"], text_color=MIRO_PALETTE["PAIN_RED"], font_size=11, frame_id=fid4)

    # Dashboard de KPIs a la Derecha
    dash_x = radar_x + radar_w + 50
    dash_w = w4 - (dash_x - fx4) - 60
    
    kpis_cafeteria = [
        ("410 ped/h", "CAPACIDAD EFECTIVA META", "Aumento de +36% sin contratar personal", MIRO_PALETTE["PASTEL_GREEN"], MIRO_PALETTE["INK"]),
        ("< 1.5%", "TASA DE ABANDONO DE FILA", "Reducida desde el 14% actual con espera < 4m", MIRO_PALETTE["PASTEL_GREEN"], MIRO_PALETTE["INK"]),
        ("3.2 min", "TIEMPO PROMEDIO ESPERA P90", "Fila fluida con maximo 8 personas en espera", MIRO_PALETTE["PASTEL_BLUE"], MIRO_PALETTE["INK"]),
        ("+4.8%", "MARGEN PROMEDIO POR PEDIDO", "Protegido con combos y sin descartar productos", "#FFFFFF", MIRO_PALETTE["INK"]),
        ("42%", "PENETRACION CANAL DIGITAL", "Migracion desde el 19% actual hacia pre-order", "#FFFFFF", MIRO_PALETTE["INK"]),
        ("0 Nuevos", "COSTO FIJO ADICIONAL", "Cero contrataciones fijas ni obras mayores", MIRO_PALETTE["STICKY"], MIRO_PALETTE["INK"])
    ]

    for i, (val, title, subtitle, bg_col, text_col) in enumerate(kpis_cafeteria):
        cx = dash_x + (i % 2) * (dash_w * 0.5)
        cy = radar_y + (i // 2) * 185
        cw = dash_w * 0.5 - 20
        ch = 165
        
        scene.add_rect(cx, cy, cw, ch, bg=bg_col, stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid4)
        scene.add_text(cx + 20, cy + 20, val, font_size=32, font_family=2, color=text_col, frame_id=fid4)
        scene.add_text(cx + 20, cy + 75, title, font_size=12, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
        scene.add_text(cx + 20, cy + 105, subtitle, font_size=11, font_family=2, color=MIRO_PALETTE["MUTED"], frame_id=fid4)

    # Banner inferior de sintesis ejecutiva
    scene.add_banner(fx4 + 50, fy4 + 730, w4 - 100, 50,
                     "conclusion directiva: la solucion no es trabajar mas rapido, sino desacoplar la toma de pedidos, batching previo y canal digital.",
                     bg=MIRO_PALETTE["BANNER_PINK"], text_color=MIRO_PALETTE["INK"], font_size=14, frame_id=fid4)

    scene.auto_fit_frame(fid4, padding=50.0)

    out_path = os.path.join(OUT_DIR, "analisis_operaciones_cafeteria.excalidraw")
    scene.save(out_path)
    return out_path


if __name__ == "__main__":
    path = build_cafeteria_analysis_scene()
    print("==================================================")
    print("ESCENA DE ANALISIS DE CAFETERIA GENERADA:")
    print(f"Ruta: {path}")
    print("==================================================")
    scene_data, report = validate_scene(path)
    print(report.summary())
