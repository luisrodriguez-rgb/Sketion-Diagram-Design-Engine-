"""
Sketion 3.3 — Generador Maestro para Sistema de Reserva de Espacios Universitarios (Pruebas V4)
Composición Multi-Frame Editorial:
- Frame 1: Arquitectura Distribuida y RBAC por Roles (Estudiantes, Profesores, Coordinación, Mantenimiento, Seguridad)
- Frame 2: Ciclo de Vida de Reserva y Protocolo de Desplazamiento por Prioridad (Preemption Workflow)
- Frame 3: Matriz de Políticas de Acceso, Horarios por Rol y Resolución de Conflictos
- Frame 4: Dashboard de Analítica de Ocupación, Facultades y Detección de Subutilización
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


def build_university_reservation_scene() -> str:
    place_reset(max_row_w=3400, gap=130)
    scene = ExcalidrawScene(roughness=0, bg_color=MIRO_PALETTE["CANVAS"])

    # =========================================================================
    # FRAME 1: ARQUITECTURA DISTRIBUIDA Y RBAC POR ROLES
    # =========================================================================
    w1, h1 = 2800, 950
    fx1, fy1 = place(w1, h1)
    fid1 = scene.add_frame("1. ARQUITECTURA DISTRIBUIDA: Control de Acceso RBAC, Motor de Prioridades y Eventos", fx1, fy1, w1, h1)

    scene.add_text(fx1 + 50, fy1 + 35, "PLATAFORMA UNIFICADA DE RESERVA DE ESPACIOS DE CAMPUS", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid1)
    scene.add_text(fx1 + 50, fy1 + 75, "gestión concurrente de salas, aulas y auditorios con jerarquía estricta de bloqueos y alertas", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)

    # Top Metric Pills
    scene.add_metric_pill(fx1 + w1 - 560, fy1 + 35, "ESPACIOS", "450 Aulas/Salas", bg=MIRO_PALETTE["INK"], frame_id=fid1)
    scene.add_metric_pill(fx1 + w1 - 320, fy1 + 35, "USUARIOS", "32,000+ Activos", bg=MIRO_PALETTE["INK"], frame_id=fid1)

    # Scopes / Columnas
    scopes_data = [
        ("col_actores", "1. ACTORES & ROLES (RBAC)", 380, [
            ("act_est", "Estudiantes", "Salas de estudio e individuales"),
            ("act_prof", "Profesores", "Aulas magistrales y laboratorios"),
            ("act_coord", "Coordinadores", "Bloqueos y actos institucionales"),
            ("act_mant", "Mantenimiento", "Averías y bloqueos de reparación"),
            ("act_sec", "Seguridad", "Restricciones y aforos críticos")
        ]),
        ("col_gateway", "2. GATEWAY & AUTH", 360, [
            ("gw_api", "API Gateway & SSO", "OAuth2 / SAML Institucional"),
            ("gw_policy", "Time-Slot Policy Engine", "Validación franjas según rol")
        ]),
        ("col_core", "3. SERVICIOS CORE", 440, [
            ("svc_booking", "Booking Lifecycle Service", "Máquina de estados de reservas"),
            ("svc_preempt", "Priority & Lock Engine", "Jerarquía de bloqueos y desalojos"),
            ("svc_approval", "Approval Workflow Service", "Aprobación docente/coordinación")
        ]),
        ("col_events", "4. EVENT STREAMING", 380, [
            ("bus_kafka", "Kafka Event Broker", "Eventos asíncronos y alertas"),
            ("worker_notif", "Notification Dispatcher", "Reubicaciones y avisos en tiempo real")
        ]),
        ("col_data", "5. PERSISTENCIA & LOCKS", 420, [
            ("db_pg", "PostgreSQL + tsrange", "Exclusion Constraint (cero solapes)"),
            ("cache_redis", "Redis Cluster (Locks)", "Hold temporal de 5 min")
        ]),
        ("col_channels", "6. CANALES NOTIFICACIÓN", 360, [
            ("ch_app", "App Móvil Universitaria", "Push notifications y QR check-in"),
            ("ch_email", "Email Institucional", "Comprobantes y reubicación")
        ])
    ]

    # Calcular posiciones horizontales con gutter de 65px
    curr_x = fx1 + 45.0
    nodes_coords = {}

    for sid, s_title, sw, snodes in scopes_data:
        # Calcular altura del scope según nodos
        sh = max(420.0, len(snodes) * 95.0 + 90.0)
        sy = fy1 + 130.0
        
        # Contenedor de Scope
        scene.add_scope_container(curr_x, sy, sw, sh, label=s_title, stroke=MIRO_PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)
        
        # Tarjetas dentro del scope
        for ni, (nid, ntitle, nsub) in enumerate(snodes):
            nx = curr_x + 25.0
            ny = sy + 55.0 + ni * 90.0
            nw = sw - 50.0
            nh = 72.0
            
            is_priority = (nid in ["act_coord", "act_mant", "act_sec", "svc_preempt"])
            bg = MIRO_PALETTE["PAIN_BG"] if is_priority else "#FFFFFF"
            border = MIRO_PALETTE["PAIN_BORDER"] if is_priority else MIRO_PALETTE["CARD_BORDER"]
            
            container, _ = scene.add_dual_card(nx, ny, nw, nh, ntitle, sublabel=nsub,
                                               bg=bg, stroke=border, text_color=MIRO_PALETTE["INK"], frame_id=fid1)
            nodes_coords[nid] = (container["x"], container["y"], container["width"], container["height"])

        curr_x += sw + 55.0  # Gutter limpio entre scopes

    # Conexiones clave
    edges = [
        ("act_est", "gw_api", "Reserva Sala"),
        ("act_prof", "gw_api", "Reserva Aula"),
        ("act_coord", "gw_api", "Bloqueo Examen"),
        ("act_mant", "gw_api", "Avería Espacio"),
        ("gw_api", "gw_policy", "Verifica Rol/Horario"),
        ("gw_policy", "svc_booking", "Request Válido"),
        ("svc_booking", "svc_preempt", "Evalúa Prioridad"),
        ("svc_preempt", "cache_redis", "Distributed Lock"),
        ("svc_booking", "db_pg", "Commit Reserva"),
        ("svc_preempt", "bus_kafka", "Evento: SpaceBlocked"),
        ("bus_kafka", "worker_notif", "Consume Evento"),
        ("worker_notif", "ch_app", "Alerta Reubicación"),
        ("worker_notif", "ch_email", "Email Afectados")
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
    # FRAME 2: CICLO DE VIDA DE RESERVA & PROTOCOLO DE DESPLAZAMIENTO (PREEMPTION)
    # =========================================================================
    w2, h2 = 2800, 1100
    fx2, fy2 = place(w2, h2)
    fid2 = scene.add_frame("2. MÁQUINA DE ESTADOS & PROTOCOLO DE PREEMPTION: Del Registro a la Reubicación por Bloqueo", fx2, fy2, w2, h2)

    scene.add_text(fx2 + 50, fy2 + 35, "CICLO DE VIDA DE LA RESERVA & JERARQUÍA DE PREEMPTION", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid2)
    scene.add_text(fx2 + 50, fy2 + 75, "estados operativos, disparadores de cambio y resolución de conflictos ante bloqueos de mantenimiento", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid2)

    # Sub-banner negro superior
    scene.add_banner(fx2 + 60, fy2 + 125, w2 - 120, 44,
                     "un bloqueo de mantenimiento o seguridad desplaza automáticamente las reservas existentes y dispara reubicación inteligente.",
                     bg=MIRO_PALETTE["INK"], text_color="#FFFFFF", font_size=15, frame_id=fid2)

    # Flujo Lineal de 6 Estados Principales
    states_flow = [
        ("01", "1. SOLICITADA", "Registro en portal / app\nVerifica disponibilidad", "#FFFFFF"),
        ("02", "2. EN EVALUACIÓN", "Validación automática o\nAprobación de Coordinador", MIRO_PALETTE["STICKY"]),
        ("03", "3. APROBADA", "Token de acceso generado\nNotificación al solicitante", MIRO_PALETTE["PASTEL_BLUE"]),
        ("04", "4. CONFIRMADA", "Espacio reservado en BD\nLock atómico 'tsrange'", MIRO_PALETTE["PASTEL_GREEN"]),
        ("05", "5. EN CURSO", "Check-in con QR en puerta\nVentana de 15 min no-show", "#FFFFFF"),
        ("06", "6. FINALIZADA", "Liberación del espacio\nMétricas de uso a OLAP", "#FFFFFF")
    ]

    flow_start_x = fx2 + 60.0
    flow_y = fy2 + 220.0
    card_w = 380.0
    card_h = 95.0
    gap_flow = 75.0

    state_coords = []
    for i, (num, st_title, st_sub, st_bg) in enumerate(states_flow):
        sx = flow_start_x + i * (card_w + gap_flow)
        
        scene.add_text(sx, flow_y - 24, f"ESTADO {num}", font_size=12, font_family=3, color=MIRO_PALETTE["MUTED"], frame_id=fid2)
        container, _ = scene.add_dual_card(sx, flow_y, card_w, card_h, st_title, sublabel=st_sub,
                                           bg=st_bg, stroke=MIRO_PALETTE["INK"], text_color=MIRO_PALETTE["INK"], frame_id=fid2)
        state_coords.append((container["x"], container["y"], container["width"], container["height"]))

    # Conectar Estados Principales
    flow_labels = ["Requiere Aprobación", "Visto Bueno", "Commit BD", "Check-in QR", "Tiempo Cumplido"]
    for i in range(len(state_coords) - 1):
        x1 = state_coords[i][0] + state_coords[i][2]
        y1 = state_coords[i][1] + state_coords[i][3] * 0.5
        x2 = state_coords[i+1][0]
        y2 = state_coords[i+1][1] + state_coords[i+1][3] * 0.5
        scene.add_arrow(x1, y1, x2, y2, stroke=MIRO_PALETTE["INK"], stroke_w=1.5, label=flow_labels[i], orthogonal=False, frame_id=fid2)

    # Fila Inferior: Estados de Excepción y Desplazamiento por Bloqueo
    exc_y = flow_y + 190.0
    scene.add_text(fx2 + 60, exc_y - 15, "RAMAS DE EXCEPCIÓN, EXPIRACIÓN & DESPLAZAMIENTO (PREEMPTION)", font_size=16, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid2)

    exceptions = [
        ("RECHAZADA", "Coordinador deniega solicitud\nMotivo y sugerencia", fx2 + 60),
        ("EXPIRADA", "No-show tras 15 min de inicio\nLiberación inmediata de sala", fx2 + 540),
        ("MODIFICADA", "Cambio de horario/capacidad\nRevalida disponibilidad", fx2 + 1020),
        ("CANCELADA", "Usuario anula con > 2h\nSin penalización de uso", fx2 + 1500),
        ("DESPLAZADA (PREEMPTED)", "Mantenimiento/Seguridad bloquea\nReubicación automática inteligente", fx2 + 1980)
    ]

    for ex_title, ex_desc, ex_x in exceptions:
        is_preempt = ("DESPLAZADA" in ex_title)
        bg = MIRO_PALETTE["PAIN_BG"] if is_preempt else "#FFFFFF"
        border = MIRO_PALETTE["PAIN_BORDER"] if is_preempt else MIRO_PALETTE["CARD_BORDER"]
        text_col = MIRO_PALETTE["PAIN_RED"] if is_preempt else MIRO_PALETTE["INK"]
        
        scene.add_bound_card(ex_x, exc_y + 15, 420, 85, f"{ex_title}\n{ex_desc}",
                             bg=bg, stroke=border, text_color=text_col, font_size=13, frame_id=fid2)

    # Conectar Preemption al flujo
    scene.add_arrow(state_coords[3][0] + 190, state_coords[3][1] + state_coords[3][3],
                    fx2 + 1980 + 210, exc_y + 15,
                    stroke=MIRO_PALETTE["PAIN_RED"], stroke_w=1.5, label="Bloqueo Urgente", orthogonal=True, frame_id=fid2)

    # Bloque de Jerarquía de Prioridades a la Izquierda
    prio_y = exc_y + 140.0
    scene.add_rect(fx2 + 60, prio_y, w2 - 120, 180, bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.5, stroke_style="dashed", roundness_type=3, frame_id=fid2)
    scene.add_text(fx2 + 85, prio_y + 20, "TABLA JERÁRQUICA DE PRIORIDAD DE BLOQUEO (PREEMPTION RULES):", font_size=15, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid2)
    
    prio_items = [
        ("NIVEL 1: SEGURIDAD", "Restricción de aforo / Protocolos de emergencia (Prioridad Absoluta)", MIRO_PALETTE["PAIN_BG"]),
        ("NIVEL 2: MANTENIMIENTO", "Averías, roturas o reparaciones técnicas (Desplaza reservas y reubica)", MIRO_PALETTE["STICKY"]),
        ("NIVEL 3: COORDINACIÓN", "Exámenes oficiales, claustros y actos solemnes de rectorado", MIRO_PALETTE["PASTEL_BLUE"]),
        ("NIVEL 4: PROFESORES", "Aulas lectivas para clases magistrales y laboratorios reglados", "#FFFFFF"),
        ("NIVEL 5: ESTUDIANTES", "Salas de estudio grupales e individuales (Sujetas a franja horaria)", "#FFFFFF")
    ]

    for pi, (p_title, p_sub, p_bg) in enumerate(prio_items):
        px = fx2 + 85 + pi * 520
        py = prio_y + 55
        scene.add_bound_card(px, py, 490, 85, f"{p_title}\n{p_sub}",
                             bg=p_bg, stroke=MIRO_PALETTE["CARD_BORDER"], text_color=MIRO_PALETTE["INK"],
                             font_size=12, frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=60.0)


    # =========================================================================
    # FRAME 3: MATRIZ DE POLÍTICAS DE ACCESO, HORARIOS Y GESTIÓN DE CONFLICTOS
    # =========================================================================
    w3, h3 = 2800, 780
    fx3, fy3 = place(w3, h3)
    fid3 = scene.add_frame("3. MATRIZ DE POLÍTICAS: Horarios por Rol, Reglas de Aprobación y Acciones ante Bloqueos", fx3, fy3, w3, h3)

    scene.add_text(fx3 + 50, fy3 + 35, "MATRIZ DE DISPONIBILIDAD HORARIA Y RESOLUCIÓN DE CONFLICTOS", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid3)
    scene.add_text(fx3 + 50, fy3 + 75, "reglas de negocio según tipo de espacio, permisos de rol y protocolo ante incidencias de mantenimiento", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid3)

    matrix_headers = ["TIPO DE ESPACIO", "USUARIOS AUTORIZADOS", "HORARIOS Y REGLAS DE FRANJA", "MODO DE RESERVA", "PROTOCOLO ANTE BLOQUEO / MANTENIMIENTO"]
    matrix_rows = [
        {"values": ["Salas de Estudio Grupal", "Estudiantes (pregrado/posgrado)", "Lunes a Viernes (8:00 a 22:00) | Máx 3h por sesión", "100% Instantáneo", "Notificación Push en < 60s y sugerencia de sala libre en el mismo edificio."]},
        {"values": ["Aulas Magistrales y Seminarios", "Profesores y Departamentos", "Mañanas: Clases regladas | Tardes: Abierto a talleres", "Aprobación Coordinador (< 4h)", "Reubicación automática a aula con igual capacidad y equipamiento proyector."]},
        {"values": ["Laboratorios Especializados", "Profesores e Investigadores", "Sujeto a calendario de investigación y normas de seguridad", "Aprobación Doble (Dpto + Lab)", "Inspección previa de seguridad; aviso urgente de suspensión con 48h."]},
        {"values": ["Auditorios y Paraninfos", "Coordinación y Rectorado", "Eventos solemnes, congresos y graduaciones oficiales", "Aprobación Coordinación Central", "Prioridad jerárquica Nivel 3: Desplaza cualquier reserva docente previa."]},
        {"values": ["Espacios Bloqueados por Avería", "Personal de Mantenimiento", "Bloqueo 24/7 hasta firma de finalización de obra", "Trigger Inmediato Mantenimiento", "Cancelación/reubicación de todas las reservas de la franja y alerta a CISO."]}
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
        is_maint = ("Avería" in vals[0] or "Laboratorios" in vals[0])
        for c, cell in enumerate(row_cells):
            val = vals[c] if c < len(vals) else ""
            bg = MIRO_PALETTE["PAIN_BG"] if (is_maint and c == 4) else "#FFFFFF"
            text_col = MIRO_PALETTE["PAIN_RED"] if (is_maint and c == 4) else MIRO_PALETTE["INK"]
            scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], str(val),
                                 bg=bg, stroke=MIRO_PALETTE["CARD_BORDER"], text_color=text_col,
                                 font_size=12, roundness_type=None, frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)


    # =========================================================================
    # FRAME 4: DASHBOARD DE ANALÍTICA, UTILIZACIÓN Y DETECCIÓN DE ESPACIOS
    # =========================================================================
    w4, h4 = 2800, 700
    fx4, fy4 = place(w4, h4)
    fid4 = scene.add_frame("4. DASHBOARD ANALÍTICO: Utilización por Facultad, Horas Reservadas, No-Shows y Subutilización", fx4, fy4, w4, h4)

    scene.add_text(fx4 + 50, fy4 + 35, "PANEL EJECUTIVO DE OCUPACIÓN Y EFICIENCIA DE ESPACIOS", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
    scene.add_text(fx4 + 50, fy4 + 75, "métricas de demanda horaria, tasa de cancelaciones y optimización de capacidad instalada", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid4)

    kpis_uni = [
        ("88.4%", "UTILIZACIÓN PROMEDIO ESPACIOS", "Pico en semanas de exámenes (Meta: > 80%)", MIRO_PALETTE["PASTEL_GREEN"], MIRO_PALETTE["INK"]),
        ("14,250 h", "HORAS RESERVADAS / SEMESTRE", "+18% vs semestre anterior (450 salas)", "#FFFFFF", MIRO_PALETTE["INK"]),
        ("Ingeniería (94%)", "FACULTAD CON MAYOR DEMANDA", "Seguida por Medicina (89%) y Derecho (76%)", MIRO_PALETTE["PASTEL_BLUE"], MIRO_PALETTE["INK"]),
        ("1.8%", "TASA DE NO-SHOWS (INASISTENCIA)", "Reducida con check-in QR en puerta (Antes: 14%)", MIRO_PALETTE["PAIN_BG"], MIRO_PALETTE["PAIN_RED"]),
        ("3.4%", "TASA DE CANCELACIONES A TIEMPO", "Liberadas con > 2h de antelación para otros", "#FFFFFF", MIRO_PALETTE["INK"]),
        ("10:00 - 13:00", "FRANJA DE DEMANDA PICO", "Aulas magnas al 98% de ocupación", "#FFFFFF", MIRO_PALETTE["INK"]),
        ("6 Salas", "ESPACIOS SUBUTILIZADOS (< 35%)", "Detectados para reasignación como salas estudio", MIRO_PALETTE["PAIN_BG"], MIRO_PALETTE["PAIN_RED"])
    ]

    chip_w = 360
    chip_h = 140
    gap_kpi = 25
    start_kpi_y = fy4 + 130

    for i, (val, title, subtitle, bg_col, text_col) in enumerate(kpis_uni[:6]):
        cx = fx4 + 50 + (i % 3) * (chip_w + gap_kpi)
        cy = start_kpi_y + (i // 3) * (chip_h + 20)
        
        scene.add_rect(cx, cy, chip_w, chip_h, bg=bg_col, stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid4)
        scene.add_text(cx + 20, cy + 18, val, font_size=34, font_family=2, color=text_col, frame_id=fid4)
        scene.add_text(cx + 20, cy + 72, title, font_size=12, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
        scene.add_text(cx + 20, cy + 95, subtitle, font_size=11, font_family=2, color=MIRO_PALETTE["MUTED"], frame_id=fid4)

    # Columna Derecha: Tarjeta de Subutilización + Checklist de Alertas
    right_x = fx4 + 50 + 3 * (chip_w + gap_kpi) + 20
    right_w = w4 - (right_x - fx4) - 60

    # Tarjeta de Subutilización
    scene.add_rect(right_x, start_kpi_y, right_w, 140, bg=MIRO_PALETTE["PAIN_BG"], stroke=MIRO_PALETTE["PAIN_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid4)
    scene.add_text(right_x + 25, start_kpi_y + 18, "6 Salas Subutilizadas (< 35% uso)", font_size=24, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid4)
    scene.add_text(right_x + 25, start_kpi_y + 60, "Edificio B (Aulas 104, 108) y Pabellón Norte (Seminarios 3 y 4).\nPropuesta: Habilitar como salas de estudio libre durante tardes.",
                   font_size=13, font_family=2, color="#333333", frame_id=fid4)

    # Tarjeta de Reglas de Alerta
    scene.add_rect(right_x, start_kpi_y + 160, right_w, 140, bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.5, stroke_style="dashed", roundness_type=3, frame_id=fid4)
    scene.add_text(right_x + 25, start_kpi_y + 180, "SISTEMA DE NOTIFICACIONES AUTOMÁTICAS ACTIVAS:", font_size=14, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
    scene.add_text(right_x + 25, start_kpi_y + 210, "• Aprobación / Rechazo instantáneo por App y Email\n• Alerta de Desalojo por Bloqueo con sugerencia de alternativa\n• Recordatorio 1h antes con botón de check-in QR",
                   font_size=12, font_family=2, color="#555555", frame_id=fid4)

    # Banner inferior de cierre
    scene.add_banner(fx4 + 50, fy4 + 480, w4 - 100, 50,
                     "la gobernanza por prioridades garantiza que la actividad académica nunca se detenga ante averías o actos extraordinarios.",
                     bg=MIRO_PALETTE["BANNER_PINK"], text_color=MIRO_PALETTE["INK"], font_size=14, frame_id=fid4)

    scene.auto_fit_frame(fid4, padding=50.0)

    out_path = os.path.join(OUT_DIR, "sistema_reserva_espacios_universidad.excalidraw")
    scene.save(out_path)
    return out_path


if __name__ == "__main__":
    path = build_university_reservation_scene()
    print("==================================================")
    print("ESCENA DE RESERVA DE ESPACIOS UNIVERSITARIOS GENERADA:")
    print(f"Ruta: {path}")
    print("==================================================")
    scene_data, report = validate_scene(path)
    print(report.summary())
