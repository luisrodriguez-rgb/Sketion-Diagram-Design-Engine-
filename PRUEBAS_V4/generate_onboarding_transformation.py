"""
Sketion 3.3 — Generador Maestro para Prueba V4:
Transformación del Proceso de Onboarding e Incorporación de Empleados
Composición Multi-Frame Editorial de Alto Impacto:
- Frame 1: Arquetipo D · El Duelo (Before vs After / Proceso Manual vs Orquestado)
- Frame 2: Arquetipo E · La Cadena de Actores y Gobernanza (Swimlanes de Flujo)
- Frame 3: Matriz de Gobernanza y Matriz de Acceso Privilegiado vs Automático
- Frame 4: Dashboard de Observabilidad y KPIs de Eficiencia (< 4h Target)
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


def build_onboarding_transformation_scene() -> str:
    place_reset(max_row_w=3400, gap=120)
    scene = ExcalidrawScene(roughness=0, bg_color=MIRO_PALETTE["CANVAS"])

    # =========================================================================
    # FRAME 1: EL DUELO (BEFORE VS AFTER / ONBOARDING ENFRENTADO)
    # =========================================================================
    w1, h1 = 2800, 1150
    fx1, fy1 = place(w1, h1)
    fid1 = scene.add_frame("1. EL DUELO: Proceso Manual Caótico (3-7 Días) vs Orquestación Automatizada (< 4 Horas)", fx1, fy1, w1, h1)

    # Cabecera Masiva
    scene.add_text(fx1 + 60, fy1 + 35, "EL ONBOARDING DEL QUE IMPROVISA", font_size=15, font_family=2, color="#8B8B8B", frame_id=fid1)
    scene.add_text(fx1 + 60, fy1 + 60, "MANUAL & SILOS (3-7 DÍAS)", font_size=38, font_family=2, color="#666666", frame_id=fid1)

    scene.add_text(fx1 + w1 * 0.5 - 40, fy1 + 55, "VS", font_size=46, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid1)

    scene.add_text(fx1 + w1 * 0.5 + 160, fy1 + 35, "EL ONBOARDING DEL QUE TIENE", font_size=15, font_family=2, color="#8B8B8B", frame_id=fid1)
    scene.add_text(fx1 + w1 * 0.5 + 160, fy1 + 60, "SISTEMA ORQUESTADO (< 4 H)", font_size=38, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)

    # Top Metric Pills
    scene.add_metric_pill(fx1 + w1 - 540, fy1 + 35, "OBJETIVO", "< 4 horas", bg=MIRO_PALETTE["INK"], frame_id=fid1)
    scene.add_metric_pill(fx1 + w1 - 320, fy1 + 35, "GOBERNANZA", "100% Auditada", bg=MIRO_PALETTE["INK"], frame_id=fid1)

    # Sub-banner negro central
    scene.add_banner(fx1 + 80, fy1 + 130, w1 - 160, 44,
                     "los dos incorporan al empleado. solo uno elimina los errores de digitación y garantiza auditoría total de seguridad.",
                     bg=MIRO_PALETTE["INK"], text_color="#FFFFFF", font_size=15, frame_id=fid1)

    # Filas Enfrentadas con Espina Central de Stickies Amarillos
    duelo_rows = [
        ("DOCUMENTACIÓN", "El empleado llena 5 formularios y envía PDFs por correo suelto", "Portal web self-service unificado con validación y OCR en tiempo real"),
        ("VALIDACIÓN RRHH", "RRHH revisa manualmente; si falta un dato, devuelve correo y se frena todo", "Motor de validación automática de campos con checklist instantáneo"),
        ("PROVISIONING 5 SISTEMAS", "RRHH digita manualmente al empleado en 5 plataformas aisladas", "Event Broker sincroniza en paralelo HRIS, IdP, Slack, Jira y ERP"),
        ("APROBACIONES", "Cadena de correos y llamadas buscando la firma del gerente", "Notificación interactiva 1-clic en Slack/Email con SLA de respuesta"),
        ("SEGURIDAD & PRIVILEGIOS", "Accesos críticos otorgados sin control o esperando 4 días al CISO", "RBAC automatizado para roles base + Puerta manual obligatoria para accesos root"),
        ("PRIMER DÍA", "Empleado esperando 3 días con la pantalla bloqueada sin accesos", "Primer día 100% operativo desde las 9:00 AM con cuentas listas")
    ]

    spine_x = fx1 + w1 * 0.5 - 120
    card_w = 950
    card_h = 75
    start_y = fy1 + 200
    row_gap = 18

    for i, (tag, left_text, right_text) in enumerate(duelo_rows):
        cy = start_y + i * (card_h + row_gap)
        
        # Tarjeta Izquierda (Gris / Dolor)
        lx = spine_x - card_w - 30
        scene.add_bound_card(lx, cy, card_w, card_h, left_text,
                             bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"],
                             text_color="#666666", font_size=14, align="right", frame_id=fid1)
        
        # Sticky Central Amarillo (-1.5 a +1.5 deg)
        rot = -1.5 if i % 2 == 0 else 1.5
        scene.add_sticky_note(spine_x, cy + 10, 240, 55, tag,
                              bg=MIRO_PALETTE["STICKY"], stroke=MIRO_PALETTE["INK"],
                              font_size=12, angle_deg=rot, frame_id=fid1)
        
        # Tarjeta Derecha (Coral / Solución)
        rx = spine_x + 240 + 30
        scene.add_bound_card(rx, cy, card_w, card_h, right_text,
                             bg=MIRO_PALETTE["PAIN_BG"], stroke=MIRO_PALETTE["PAIN_BORDER"],
                             text_color=MIRO_PALETTE["INK"], font_size=14, align="left", frame_id=fid1)

    # Comparativa de Cifras al Pie
    stats_y = start_y + len(duelo_rows) * (card_h + row_gap) + 25
    scene.add_chip(fx1 + 350, stats_y, 180, 90, "3-7 días", "Tiempo Onboarding", bg="#FFFFFF", text_color="#666666", frame_id=fid1)
    scene.add_chip(fx1 + 560, stats_y, 180, 90, "8+", "Handoffs Manuales", bg="#FFFFFF", text_color="#666666", frame_id=fid1)
    scene.add_chip(fx1 + 770, stats_y, 180, 90, "18%", "Tasa de Errores", bg="#FFFFFF", text_color="#666666", frame_id=fid1)

    scene.add_chip(fx1 + w1 - 950, stats_y, 180, 90, "3.8 h", "Tiempo Total", bg=MIRO_PALETTE["PAIN_BG"], text_color=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)
    scene.add_chip(fx1 + w1 - 740, stats_y, 180, 90, "2", "Intervenciones", bg=MIRO_PALETTE["PAIN_BG"], text_color=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)
    scene.add_chip(fx1 + w1 - 530, stats_y, 180, 90, "0.2%", "Tasa de Errores", bg=MIRO_PALETTE["PAIN_BG"], text_color=MIRO_PALETTE["PAIN_RED"], frame_id=fid1)

    # Banner de Remate Inferior
    scene.add_banner(fx1 + 80, stats_y + 115, w1 - 160, 50,
                     "la automatización no elimina a RRHH ni a Seguridad: elimina la burocracia ciega para centrarse en la gobernanza y la experiencia humana.",
                     bg=MIRO_PALETTE["BANNER_PINK"], text_color=MIRO_PALETTE["INK"], font_size=15, frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=60.0)


    # =========================================================================
    # FRAME 2: ARQUETIPO E · LA CADENA DE ACTORES Y GOBERNANZA (SWIMLANES)
    # =========================================================================
    w2, h2 = 2800, 1050
    fx2, fy2 = place(w2, h2)
    fid2 = scene.add_frame("2. ARQUITECTURA DE ORQUESTACIÓN: Swimlanes por Actor y Handoffs de Seguridad", fx2, fy2, w2, h2)

    scene.add_text(fx2 + 60, fy2 + 35, "CADENA OPERATIVA DE ONBOARDING MULTI-ACTOR", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid2)
    scene.add_text(fx2 + 60, fy2 + 75, "flujo coordinado en 5 carriles: empleado, orquestador, gerente, seguridad ciso y sistemas destino", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid2)

    # Definir Swimlanes
    lanes = [
        ("1. EMPLEADO", "Portal Self-Service", MIRO_PALETTE["PASTEL_BLUE"]),
        ("2. ORQUESTADOR", "Workflow Core Engine", MIRO_PALETTE["INK"]),
        ("3. GERENTE", "Aprobador Operativo", MIRO_PALETTE["STICKY"]),
        ("4. CISO / SEGURIDAD", "Guardián de Privilegios", MIRO_PALETTE["PAIN_BG"]),
        ("5. SISTEMAS DESTINO", "5 Plataformas Core", MIRO_PALETTE["PASTEL_GREEN"])
    ]

    time_cols = ["01. REGISTRO", "02. VALIDACIÓN", "03. CUENTAS BASE", "04. APROBACIONES", "05. PROVISIONING", "06. BIENVENIDA"]

    lane_h = 135
    start_lane_y = fy2 + 130
    lane_w = w2 - 120
    time_col_w = (lane_w - 260) / len(time_cols)

    # Cabeceras de Tiempo Arriba
    for ti, tname in enumerate(time_cols):
        tx = fx2 + 320 + ti * time_col_w
        scene.add_text(tx + 20, start_lane_y - 28, tname, font_size=13, font_family=3, color=MIRO_PALETTE["MUTED"], frame_id=fid2)

    # Render de Swimlanes
    lane_cards = {}
    for li, (lane_name, lane_sub, lane_color) in enumerate(lanes):
        ly = start_lane_y + li * lane_h
        # Contenedor de carril
        scene.add_rect(fx2 + 60, ly, lane_w, lane_h - 10, bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.0, roundness_type=3, frame_id=fid2)
        
        # Cabecera Lateral del Actor
        head_bg = lane_color if lane_color != MIRO_PALETTE["INK"] else "#0C0C0C"
        head_text_color = "#FFFFFF" if lane_color == MIRO_PALETTE["INK"] else MIRO_PALETTE["INK"]
        scene.add_bound_card(fx2 + 70, ly + 15, 220, 85, f"{lane_name}\n{lane_sub}",
                             bg=head_bg, stroke=MIRO_PALETTE["INK"],
                             text_color=head_text_color, font_size=13, frame_id=fid2)

    # Tarjetas en la Grilla
    cards_data = [
        # (lane_idx, col_idx, id, title, sublabel)
        (0, 0, "emp_reg", "Sube Documentos", "DNI, cuenta bancaria, firma"),
        (1, 1, "orq_val", "OCR & Validación", "Checklist atómico en 60s"),
        (1, 2, "orq_base", "Crea Cuentas Base", "Email corporativo + Slack"),
        (2, 3, "ger_apr", "Aprueba Permisos Rol", "1-clic en Slack (SLA < 2h)"),
        (3, 3, "ciso_apr", "Aprueba Privilegiados", "MFA + Just-in-Time Access"),
        (4, 4, "sis_sync", "Sincroniza 5 Sistemas", "HRIS, IdP, ERP, AWS, Jira"),
        (0, 5, "emp_ready", "Acceso Total Listo", "Primer login a las 9:00 AM")
    ]

    for li, ci, cid, title, sub in cards_data:
        cx = fx2 + 320 + ci * time_col_w
        cy = start_lane_y + li * lane_h + 15
        cw = time_col_w - 30
        ch = 75
        is_security = (li == 3)
        bg = MIRO_PALETTE["PAIN_BG"] if is_security else "#FFFFFF"
        border = MIRO_PALETTE["PAIN_BORDER"] if is_security else MIRO_PALETTE["CARD_BORDER"]
        
        container, _ = scene.add_dual_card(cx, cy, cw, ch, title, sublabel=sub,
                                           bg=bg, stroke=border, text_color=MIRO_PALETTE["INK"], frame_id=fid2)
        lane_cards[cid] = (container["x"], container["y"], container["width"], container["height"])

    # Conexiones y Saltos entre Carriles (Handoffs)
    handoffs = [
        ("emp_reg", "orq_val", "Webhook"),
        ("orq_val", "orq_base", "Auto-Provision"),
        ("orq_base", "ger_apr", "Solicitud Rol"),
        ("orq_base", "ciso_apr", "Alerta Privilegio"),
        ("ger_apr", "sis_sync", "Aprobado"),
        ("ciso_apr", "sis_sync", "Certificado CISO"),
        ("sis_sync", "emp_ready", "Notificación Final")
    ]

    for f_id, t_id, lbl in handoffs:
        if f_id in lane_cards and t_id in lane_cards:
            fx, fy, fw, fh = lane_cards[f_id]
            tx, ty, tw, th = lane_cards[t_id]
            scene.add_arrow(fx + fw, fy + fh * 0.5, tx, ty + th * 0.5,
                            stroke=MIRO_PALETTE["INK"], stroke_w=1.5, label=lbl, orthogonal=True, frame_id=fid2)

    # Bloque de Cadena de Evidencia al Pie
    ev_y = start_lane_y + len(lanes) * lane_h + 20
    scene.add_capture_slot(fx2 + 80, ev_y, 750, 150, label="Captura: Portal de Subida de Documentos del Empleado", frame_id=fid2)
    scene.add_capture_slot(fx2 + 980, ev_y, 750, 150, label="Captura: Notificación de Aprobación 1-Clic en Slack", frame_id=fid2)
    scene.add_capture_slot(fx2 + 1880, ev_y, 750, 150, label="Captura: Auditoría de Accesos en Tiempo Real (SIEM)", frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=60.0)


    # =========================================================================
    # FRAME 3: MATRIZ DE GOBERNANZA Y POLÍTICAS DE ACCESO
    # =========================================================================
    w3, h3 = 2800, 750
    fx3, fy3 = place(w3, h3)
    fid3 = scene.add_frame("3. MATRIZ DE GOBERNANZA: Tipos de Acceso, Aprobadores y Mecanismos de Fallback", fx3, fy3, w3, h3)

    scene.add_text(fx3 + 50, fy3 + 35, "MATRIZ DE ASIGNACIÓN DE ACCESOS Y REGLAS DE SEGURIDAD", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid3)
    scene.add_text(fx3 + 50, fy3 + 75, "distinción estricta entre provisionamiento automático y puertas de aprobación humana obligatorias", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid3)

    matrix_headers = ["CATEGORÍA DE ACCESO", "SISTEMAS INVOLUCRADOS", "TIPO DE APROBACIÓN", "SLA OBJETIVO", "POLÍTICA DE SEGURIDAD Y REGLA DE AUDITORÍA"]
    matrix_rows = [
        {"values": ["Identidad y Colaboración Base", "Google Workspace, Slack, HRIS", "100% Automatizado", "< 5 minutos", "Asignación estándar por rol y departamento sin intervención manual."]},
        {"values": ["Herramientas de Productividad", "Figma, Notion, Jira, GitHub Reader", "Aprobación Gerente (1-Clic)", "< 2 horas", "El gerente valida necesidad funcional; si no responde en 4h, escala a Director."]},
        {"values": ["Accesos Financieros / ERP", "SAP, Stripe Dashboard, Facturación", "Aprobación Gerente + Finanzas", "< 3 horas", "Requiere doble visto bueno; nunca se auto-aprueba. Bloqueo en fines de semana."]},
        {"values": ["Accesos Privilegiados & Producción", "AWS Root, Bastion Host, BD Clientes", "Aprobación CISO / Seguridad (OBLIGATORIO)", "< 4 horas", "Estrictamente manual con Just-in-Time (JIT) TTL 8h, MFA FIDO2 y registro en SIEM."]},
        {"values": ["Offboarding / Revocación Inmediata", "Todos los 5 Sistemas Conectados", "Automático por Trigger de Salida", "< 60 segundos", "Revocación global síncrona ante terminación de contrato para evitar accesos huérfanos."]}
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
        is_priv = ("Privilegiados" in vals[0] or "Offboarding" in vals[0])
        for c, cell in enumerate(row_cells):
            val = vals[c] if c < len(vals) else ""
            bg = MIRO_PALETTE["PAIN_BG"] if (is_priv and c == 2) else "#FFFFFF"
            text_col = MIRO_PALETTE["PAIN_RED"] if (is_priv and c == 2) else MIRO_PALETTE["INK"]
            scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], str(val),
                                 bg=bg, stroke=MIRO_PALETTE["CARD_BORDER"], text_color=text_col,
                                 font_size=12, roundness_type=None, frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)


    # =========================================================================
    # FRAME 4: DASHBOARD DE KPIS Y OBSERVABILIDAD DEL ONBOARDING
    # =========================================================================
    w4, h4 = 2800, 650
    fx4, fy4 = place(w4, h4)
    fid4 = scene.add_frame("4. DASHBOARD DE MÉTRICAS: Los 6 KPIs de Eficiencia y Éxito del Onboarding", fx4, fy4, w4, h4)

    scene.add_text(fx4 + 50, fy4 + 35, "PANEL DE CONTROL Y SLA DE INCORPORACIÓN DE EMPLEADOS", font_size=32, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
    scene.add_text(fx4 + 50, fy4 + 75, "medición continua de velocidad, calidad de datos y reducción de carga operativa", font_size=18, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid4)

    kpis = [
        ("3.8 h", "TIEMPO TOTAL ONBOARDING", "Meta: < 4 h (Antes: 3-7 días)", MIRO_PALETTE["PAIN_BG"], MIRO_PALETTE["PAIN_RED"]),
        ("45 min", "TIEMPO ESPERANDO APROBACIÓN", "SLA Gerencial en Slack (Antes: 48h)", "#FFFFFF", MIRO_PALETTE["INK"]),
        ("2", "INTERVENCIONES HUMANAS MÁX.", "Solo Gerente y CISO (Antes: 8+)", "#FFFFFF", MIRO_PALETTE["INK"]),
        ("0.2%", "TASA DE ERRORES DE DIGITACIÓN", "Validación con OCR (Antes: 18%)", MIRO_PALETTE["PAIN_BG"], MIRO_PALETTE["PAIN_RED"]),
        ("82%", "PORCENTAJE AUTOMATIZADO", "Cuentas y formularios sin fricción", "#FFFFFF", MIRO_PALETTE["INK"]),
        ("15 min", "TIEMPO HASTA PRIMER ACCESO", "Email y Slack listos al iniciar", MIRO_PALETTE["PAIN_BG"], MIRO_PALETTE["PAIN_RED"])
    ]

    chip_w = 420
    chip_h = 150
    gap_x = 35
    start_kpi_y = fy4 + 140

    for i, (val, title, subtitle, bg_col, text_col) in enumerate(kpis):
        cx = fx4 + 50 + (i % 3) * (chip_w + gap_x)
        cy = start_kpi_y + (i // 3) * (chip_h + 30)
        
        card = scene.add_rect(cx, cy, chip_w, chip_h, bg=bg_col, stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.5, roundness_type=3, frame_id=fid4)
        scene.add_text(cx + 25, cy + 20, val, font_size=42, font_family=2, color=text_col, frame_id=fid4)
        scene.add_text(cx + 25, cy + 80, title, font_size=13, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
        scene.add_text(cx + 25, cy + 105, subtitle, font_size=12, font_family=2, color=MIRO_PALETTE["MUTED"], frame_id=fid4)

    # Lead Magnet / Action Box a la derecha del Dashboard
    box_x = fx4 + 50 + 3 * (chip_w + gap_x) + 30
    box_w = w4 - (box_x - fx4) - 60
    scene.add_rect(box_x, start_kpi_y, box_w, chip_h * 2 + 30, bg="#FFFFFF", stroke=MIRO_PALETTE["PAIN_BORDER"], stroke_w=1.5, stroke_style="dashed", roundness_type=3, frame_id=fid4)
    scene.add_text(box_x + 30, start_kpi_y + 30, "CHECKLIST DE DESPLIEGUE DEL SISTEMA", font_size=16, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid4)
    scene.add_text(box_x + 30, start_kpi_y + 70, "1. [✓] Integración Webhook Portal -> Workflow Engine\n2. [✓] Conector SCIM con Google Workspace y Slack\n3. [✓] Flujo de Aprobación 1-Clic en Slack API\n4. [✓] Gate de Seguridad FIDO2 / CISO para Privilegiados\n5. [✓] Exportación de Logs de Auditoría a SIEM",
                   font_size=13, font_family=2, color="#333333", frame_id=fid4)
    
    scene.add_banner(box_x + 20, start_kpi_y + 260, box_w - 40, 45,
                     "resultado: 100% de empleados operativos el día 1 en < 4 horas.",
                     bg=MIRO_PALETTE["BANNER_PINK"], text_color=MIRO_PALETTE["INK"], font_size=13, frame_id=fid4)

    scene.auto_fit_frame(fid4, padding=50.0)

    out_path = os.path.join(OUT_DIR, "incorporacion_empleados_onboarding.excalidraw")
    scene.save(out_path)
    return out_path


if __name__ == "__main__":
    path = build_onboarding_transformation_scene()
    print("==================================================")
    print("ESCENA DE ONBOARDING GENERADA:")
    print(f"Ruta: {path}")
    print("==================================================")
    scene_data, report = validate_scene(path)
    print(report.get_summary())
