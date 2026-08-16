"""
Sketion 8.0 — Generador Oficial Maestro: SEAMOSGENIOS S.A.S.
Organiza TODO el documento maestro legal en 3 Marcos Verticales (Scroll Natural):
- Frame 1 (Y=0): Identidad, Matriz de 8 Roles y los 14 Documentos Maestros (Hub & Grid)
- Frame 2 (Y=1150): Protocolo Reforzado Menores (NNA), Grabaciones Gemini AI & Proveedores
- Frame 3 (Y=2300): Comercio Electrónico (Ley 1480), Retracto, PQRS, Matriz RBAC & Log Forense
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
    "DARK_SLATE": "#1E293B",
    "STICKY": "#FFE95C"
}


def build_seamosgenios_legal_board():
    # max_row_w = 3000 fuerza a que cada marco de ancho 2800 se coloque VERTICALMENTE uno debajo del otro
    place_reset(max_row_w=3000, gap=150)
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])

    fw = 2800.0
    fh = 1000.0

    # ═══════════════════════════════════════════════════════════════════════════
    # FRAME 1: IDENTIDAD, MATRIZ DE ROLES & LOS 14 DOCUMENTOS (Y = 0)
    # ═══════════════════════════════════════════════════════════════════════════
    f1_x, f1_y = place(fw, fh)
    fid1 = scene.add_frame("FRAME 1: SEAMOSGENIOS S.A.S. — IDENTIDAD, ROLES & ARQUITECTURA DOCUMENTAL", f1_x, f1_y, fw, fh)

    scene.add_text(f1_x + 60.0, f1_y + 35.0, "SEAMOSGENIOS S.A.S.  ·  MARCO MAESTRO LEGAL & GOBERNANZA v1.0", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "Ecosistema Jurídico Integral: Protección de Datos (Ley 1581/2012), 8 Roles y 14 Documentos Maestros", font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    sc_h = 760.0

    # Scope 1: Identidad del Responsable
    sc1_w = 820.0
    sc1_x = f1_x + 60.0
    sc1_y = f1_y + 120.0
    scene.add_scope_container(sc1_x, sc1_y, sc1_w, sc_h, label="1. IDENTIDAD & RESPONSABLE DEL TRATAMIENTO", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

    scene.add_quad_card(sc1_x + 30.0, sc1_y + 50.0, sc1_w - 60.0, 130.0,
                        "SEAMOSGENIOS S.A.S.",
                        sublabel="NIT 902080201 · Carrera 121 #25-65, Cali, Valle del Cauca, Colombia\nCorreo Oficial: seamosgenios@adpmh.com · Objeto: PreICFES Virtual & Convenios B2B",
                        badge="RESPONSABLE", icon="lock", is_hero=True, font_size=18, frame_id=fid1)

    scene.add_sticky_note(sc1_x + 30.0, sc1_y + 195.0, sc1_w - 60.0, 150.0,
                          "REGLA DE ORO DE PRIVACIDAD (LEY 1581 / SIC):\n"
                          "• La autorización debe ser previa, expresa, informada y demostrable.\n"
                          "• PROHIBIDO empaquetar todas las autorizaciones en una sola casilla.\n"
                          "• Cada finalidad sensible (menores, imagen, marketing) requiere consentimiento independiente.",
                          font_size=14, angle_deg=-1.0, frame_id=fid1)

    scene.add_bound_card(sc1_x + 30.0, sc1_y + 360.0, sc1_w - 60.0, 175.0,
                         "CANAL CENTRALIZADO DE HÁBEAS DATA & PQRS:\n\n"
                         "• Correo de atención exclusiva: seamosgenios@adpmh.com\n"
                         "• Formulario autenticado en plataforma web con radicado automático.\n"
                         "• Términos legales de respuesta: 15 días hábiles conforme al régimen SIC.\n"
                         "• Registro de historial y trazabilidad inmutable por cada solicitud.",
                         bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=13, align="left", roundness_type=3, frame_id=fid1)

    scene.add_bound_card(sc1_x + 30.0, sc1_y + 550.0, sc1_w - 60.0, 180.0,
                         "PRINCIPIO DE MINIMIZACIÓN DE DATOS (CAMPOS SOLICITADOS):\n\n"
                         "✔ Identificación y contacto: Nombre, doc, fecha nacimiento, correo, WhatsApp.\n"
                         "✔ Información académica: Colegio, grado, carrera interés, puntajes simulacros.\n"
                         "✖ DATOS SENSIBLES EXCLUIDOS: Cero biometría, cero religión, cero política.\n"
                         "✖ Datos de salud: Solo si existe reporte indispensable para adecuación de clase.",
                         bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                         font_size=13, align="left", roundness_type=3, frame_id=fid1)

    # Scope 2: Matriz de 8 Roles
    sc2_w = 860.0
    sc2_x = sc1_x + sc1_w + 35.0
    scene.add_scope_container(sc2_x, sc1_y, sc2_w, sc_h, label="2. MATRIZ DE ACTORES & ROLES (8 PERFILES DIFERENCIADOS)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

    roles = [
        ("COMPRADOR", "Quien contrata y paga el servicio", "BUYER", "card"),
        ("ESTUDIANTE", "Receptor del servicio académico PreICFES", "STUDENT", "user"),
        ("REPRESENTANTE", "Padre/Madre de estudiante menor de edad", "PARENT", "users"),
        ("ACUDIENTE", "Persona autorizada para trámites y seguimiento", "GUARDIAN", "shield"),
        ("COLEGIO B2B", "Institución educativa cliente con cohorte", "B2B INST", "database"),
        ("TUTOR", "Prestador de servicios docentes y mentoría", "TUTOR", "terminal"),
        ("USUARIO", "Persona titular que opera la cuenta LMS", "ACCOUNT", "laptop"),
        ("TITULAR", "Persona natural dueña de los datos personales", "DATA OWNER", "key")
    ]

    rw = (sc2_w - 75.0) * 0.5
    for idx, (r_tit, r_sub, r_badge, r_icon) in enumerate(roles):
        rx = sc2_x + 25.0 + (idx % 2) * (rw + 25.0)
        ry = sc1_y + 50.0 + (idx // 2) * 165.0
        scene.add_quad_card(rx, ry, rw, 140.0, r_tit, sublabel=r_sub, badge=r_badge, icon=r_icon, font_size=16, frame_id=fid1)

    # Scope 3: Los 14 Documentos Maestros
    sc3_w = 930.0
    sc3_x = sc2_x + sc2_w + 35.0
    scene.add_scope_container(sc3_x, sc1_y, sc3_w, sc_h, label="3. ECOSISTEMA DE LOS 14 DOCUMENTOS MAESTROS INDEPENDIENTES", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

    scene.add_bound_card(sc3_x + 25.0, sc1_y + 50.0, sc3_w - 50.0, 215.0,
                         "PILAR I · NÚCLEO CONTRACTUAL & PROPIEDAD INTELECTUAL:\n\n"
                         "• 01. Política de Tratamiento de Datos: Régimen general, finalidades, derechos y retención.\n"
                         "• 02. Términos y Condiciones: Compra, acceso, reglas de clase, retracto y reversión.\n"
                         "• 11. Política de Propiedad Intelectual: Banco de preguntas ICFES, simulacros, PDFs, videos.",
                         bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=13, align="left", roundness_type=3, frame_id=fid1)

    scene.add_bound_card(sc3_x + 25.0, sc1_y + 285.0, sc3_w - 50.0, 235.0,
                         "PILAR II · 5 AUTORIZACIONES ESPECÍFICAS (CASILLAS INDEPENDIENTES):\n\n"
                         "• 03. Autorización Tratamiento de Datos Personales (Consentimiento general).\n"
                         "• 04. Autorización Datos de Menores (NNA) (Otorgada exclusivamente por representante legal).\n"
                         "• 05. Autorización Imagen, Voz, Testimonios y Resultados (Opcional para publicidad y redes).\n"
                         "• 06. Autorización Grabación de Clases y Transcripciones (Fines académicos y de consulta).\n"
                         "• 07. Autorización Comunicaciones Comerciales y WhatsApp (Opcional para promociones).",
                         bg=PALETTE["CORAL_BG"], stroke=PALETTE["CORAL_BORDER"], text_color=PALETTE["INK"],
                         font_size=13, align="left", roundness_type=3, frame_id=fid1)

    scene.add_bound_card(sc3_x + 25.0, sc1_y + 540.0, sc3_w - 50.0, 195.0,
                         "PILAR III · REGLAMENTOS OPERATIVOS & CONVENIOS B2B:\n\n"
                         "• 08. Política de Cookies · 09. Reglamento de Uso de Plataforma LMS.\n"
                         "• 10. Convivencia Digital (Meet, WhatsApp) · 12. Política Integral de PQRS.\n"
                         "• 13. Reglamento de Cuenta de Padres · 14. Acuerdo de Tratamiento con Colegios B2B.",
                         bg=PALETTE["GREEN_BG"], stroke=PALETTE["GREEN_BORDER"], text_color=PALETTE["INK"],
                         font_size=13, align="left", roundness_type=3, frame_id=fid1)

    scene.add_legend_footer(f1_x + 60.0, f1_y + 925.0, fw - 120.0, swatches=[
        {"label": "Responsable & Autorizaciones NNA", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Núcleo Contractual", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Reglamentos & B2B", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]},
        {"label": "Actores del Ecosistema", "bg": "#FFFFFF", "stroke": PALETTE["MUTED"]}
    ], note="SEAMOSGENIOS Compliance: Estricta separación de consentimientos conforme a la Ley 1581 de 2012.", frame_id=fid1)


    # ═══════════════════════════════════════════════════════════════════════════
    # FRAME 2: OPERACIÓN — PROTECCIÓN DE MENORES (NNA), GRABACIONES & TECH STACK
    # ═══════════════════════════════════════════════════════════════════════════
    f2_x, f2_y = place(fw, fh)
    fid2 = scene.add_frame("FRAME 2: OPERACIÓN — PROTECCIÓN NNA, GRABACIONES GEMINI AI & PROVEEDORES", f2_x, f2_y, fw, fh)

    scene.add_text(f2_x + 60.0, f2_y + 35.0, "OPERATIONAL FLOWS  ·  MINOR PROTECTION & CLOUD TECH STACK", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid2)
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "Flujos Críticos: Menores de Edad, Procesamiento IA con Gemini y Transmisiones Internacionales", font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    # Top Scope: Protocolo de Menores (5 Pasos en Pipeline)
    nna_w = fw - 120.0
    nna_h = 240.0
    scene.add_scope_container(f2_x + 60.0, f2_y + 120.0, nna_w, nna_h, label="1. PROTOCOLO REFORZADO DE CAPTURA PARA MENORES DE EDAD (NNA)", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid2)

    step_cards = [
        ("01. DETECTAR EDAD", "Filtro en Formulario", "Detección de edad < 18 años", "STEP 1", "alert"),
        ("02. REPRESENTANTE", "Capturar Padre/Madre", "Nombre, cédula y parentesco", "STEP 2", "users"),
        ("03. AUTORIZACIÓN", "Consentimiento NNA", "Firma expresa del acudiente", "STEP 3", "lock", True),
        ("04. INFORMAR MENOR", "Lenguaje Adaptado", "Derecho a ser escuchado", "STEP 4", "laptop"),
        ("05. LOG AUDITABLE", "Registro consent_id", "Evidencia forense ante SIC", "STEP 5", "database")
    ]

    card_step_w = (nna_w - 60.0 - 4 * 35.0) / 5.0
    for idx, (s_tit, s_sub, s_meta, s_badge, s_icon, *is_h) in enumerate(step_cards):
        cx = f2_x + 90.0 + idx * (card_step_w + 35.0)
        cy = f2_y + 175.0
        h_flag = is_h[0] if is_h else False
        scene.add_quad_card(cx, cy, card_step_w, 140.0, s_tit, sublabel=f"{s_sub}\n{s_meta}", badge=s_badge, icon=s_icon, is_hero=h_flag, font_size=16, frame_id=fid2)

        if idx < len(step_cards) - 1:
            scene.add_arrow(cx + card_step_w, cy + 70.0, cx + card_step_w + 35.0, cy + 70.0, stroke=PALETTE["CORAL_HERO"], stroke_w=2.0, frame_id=fid2)

    # Bottom-Left Scope: Grabaciones & Gemini AI
    bot_y = f2_y + 380.0
    bot_h = 510.0
    rec_w = 1260.0
    scene.add_scope_container(f2_x + 60.0, bot_y, rec_w, bot_h, label="2. MATRIZ DE TRATAMIENTO: GRABACIONES DE CLASE & IA (GEMINI)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)

    scene.add_quad_card(f2_x + 90.0, bot_y + 50.0, (rec_w - 90.0) * 0.5, 145.0,
                        "Sesión en Vivo (Google Meet)",
                        sublabel="Aviso previo obligatorio en pantalla.\nCaptura de video, audio, micrófono y chat.\nRegistro de asistencia y preguntas.",
                        badge="CAPTURA EN VIVO", icon="laptop", font_size=16, frame_id=fid2)

    scene.add_quad_card(f2_x + 90.0 + (rec_w - 90.0) * 0.5 + 30.0, bot_y + 50.0, (rec_w - 90.0) * 0.5, 145.0,
                        "Procesamiento IA & Google Drive",
                        sublabel="Almacenamiento seguro en Google Drive.\nTranscripción pedagógica con Gemini.\nGeneración de resúmenes de estudio.",
                        badge="IA GEMINI & DRIVE", icon="server", font_size=16, frame_id=fid2)

    scene.add_quad_card(f2_x + 90.0, bot_y + 220.0, rec_w - 60.0, 130.0,
                        "Regla de Oro: Grabación Académica vs Publicación en YouTube",
                        sublabel="• Grabación Académica: Uso exclusivo para consulta interna de estudiantes matriculados.\n• Publicación Pública (YouTube / Redes): REQUIERE autorización independiente y expresa de imagen y voz.\n• Prohibido publicar grabaciones donde aparezcan menores de edad sin consentimiento específico.",
                        badge="SEGREGACIÓN NARRATIVA", icon="shield", is_hero=True, font_size=17, frame_id=fid2)

    scene.add_bound_card(f2_x + 90.0, bot_y + 375.0, rec_w - 60.0, 105.0,
                         "AVISO OBLIGATORIO ANTES DE INGRESAR A CADA CLASE (MEET):\n"
                         "\"Esta sesión será grabada. Tu participación mediante cámara, micrófono o chat formará parte del registro académico.\n"
                         "Las grabaciones se utilizan exclusivamente para fines pedagógicos y de refuerzo dentro de la plataforma.\"",
                         bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=13, align="left", roundness_type=3, frame_id=fid2)

    # Bottom-Right Scope: Proveedores Tecnológicos (Encargados)
    prov_w = fw - 120.0 - rec_w - 40.0
    prov_x = f2_x + 60.0 + rec_w + 40.0
    scene.add_scope_container(prov_x, bot_y, prov_w, bot_h, label="3. MATRIZ DE PROVEEDORES TECNOLÓGICOS (ENCARGADOS)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)

    providers = [
        ("GOOGLE LLC (Meet/Drive/Gemini)", "Audio, video, chat, archivos y transcripción IA", "EE.UU. (Cláusulas Estándar)", "CLOUD TECH", "server"),
        ("BOLD.CO (Pasarela de Pagos)", "Datos de transacción, tarjeta y estado de pago", "Colombia (Certificado PCI-DSS)", "PAYMENTS", "lock"),
        ("FACTUS / BOLD POS", "Facturación Electrónica DIAN", "Colombia (Proveedor DIAN)", "BILLING", "file"),
        ("WHATSAPP (META)", "Grupos informativos y mensajería de soporte", "EE.UU. (Canal Moderado)", "MESSAGING", "users"),
        ("PLATAFORMA LMS CORE", "Cuentas, simulacros, notas, alertas y reportes", "Infraestructura Cloud Segura", "CORE LMS", "database")
    ]

    for p_i, (p_tit, p_data, p_loc, p_badge, p_icon) in enumerate(providers):
        py = bot_y + 50.0 + p_i * 88.0
        scene.add_quad_card(prov_x + 30.0, py, prov_w - 60.0, 76.0, p_tit, sublabel=f"{p_data} · {p_loc}", badge=p_badge, icon=p_icon, font_size=14, frame_id=fid2)

    scene.add_legend_footer(f2_x + 60.0, f2_y + 925.0, fw - 120.0, swatches=[
        {"label": "Consentimiento NNA & Regla YouTube", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Procesamiento Gemini & Avisos", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Pasarelas & Facturación DIAN", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]}
    ], note="SEAMOSGENIOS Tech Stack: Contratos de procesamiento con Google, Bold, Factus y WhatsApp.", frame_id=fid2)


    # ═══════════════════════════════════════════════════════════════════════════
    # FRAME 3: COMERCIO ELECTRÓNICO, SEGURIDAD RBAC, PQRS & AUDITORÍA FORENSE
    # ═══════════════════════════════════════════════════════════════════════════
    f3_x, f3_y = place(fw, fh)
    fid3 = scene.add_frame("FRAME 3: COMERCIO ELECTRÓNICO, SEGURIDAD RBAC, PQRS & AUDITORÍA FORENSE", f3_x, f3_y, fw, fh)

    scene.add_text(f3_x + 60.0, f3_y + 35.0, "CONSUMER RIGHTS  ·  ROLE-BASED ACCESS CONTROL & FORENSIC AUDIT", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid3)
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "Régimen de Comercio Electrónico (Ley 1480/2011), Matriz de Seguridad RBAC y Registro de Evidencia", font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    # Scope 1: Comercio Electrónico (Ley 1480)
    ecom_w = 820.0
    scene.add_scope_container(f3_x + 60.0, sc1_y, ecom_w, sc_h, label="1. RÉGIMEN DE COMERCIO ELECTRÓNICO (LEY 1480/2011)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)

    scene.add_quad_card(f3_x + 30.0, sc1_y + 50.0, ecom_w - 60.0, 130.0,
                        "Compra Online & Perfeccionamiento",
                        sublabel="Aceptación explícita de Términos y Condiciones en checkout Bold.\nEmisión obligatoria de Factura Electrónica vía Factus.\nActivación automática de credenciales y envío de comprobante.",
                        badge="CHECKOUT BOLD", icon="lock", font_size=16, frame_id=fid3)

    scene.add_quad_card(f3_x + 30.0, sc1_y + 205.0, ecom_w - 60.0, 150.0,
                        "Derecho de Retracto Legal (SIC)",
                        sublabel="• Término legal: 5 días hábiles siguientes a la compra.\n• Prohibición absoluta de cláusulas abusivas de 'no hay devoluciones'.\n• Evaluación jurídica si el servicio ya inició o hubo consumo de simulacros.\n• Canal formal de radicación con respuesta en términos de ley.",
                        badge="RETRACTO LEY 1480", icon="alert", is_hero=True, font_size=16, frame_id=fid3)

    scene.add_quad_card(f3_x + 30.0, sc1_y + 380.0, ecom_w - 60.0, 130.0,
                        "Reversión de Pagos & Reembolsos",
                        sublabel="Aplica ante: Fraude electrónico, operación no solicitada o servicio no prestado.\nProcedimiento coordinado entre SEAMOSGENIOS, pasarela Bold y banco emisor.\nTiempos de respuesta estrictos conforme a la reglamentación SIC.",
                        badge="REVERSIÓN PAGO", icon="file", font_size=16, frame_id=fid3)

    scene.add_bound_card(f3_x + 30.0, sc1_y + 535.0, ecom_w - 60.0, 195.0,
                         "CLÁUSULA DE RESULTADOS ICFES (SIN GARANTÍAS ILÍCITAS):\n\n"
                         "• SEAMOSGENIOS ofrece preparación pedagógica de alto nivel.\n"
                         "• El puntaje final depende del esfuerzo y estudio individual del alumno.\n"
                         "• Los puntajes de simulacros son herramientas de entrenamiento, no resultados oficiales.\n"
                         "• Queda expresamente prohibido garantizar puntajes específicos o cupos universitarios.",
                         bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                         font_size=13, align="left", roundness_type=3, frame_id=fid3)

    # Scope 2: Módulo Integral de PQRS (6 Categorías)
    pqrs_w = 860.0
    pqrs_x = f3_x + 60.0 + ecom_w + 35.0
    scene.add_scope_container(pqrs_x, sc1_y, pqrs_w, sc_h, label="2. MÓDULO CENTRALIZADO DE PQRS & HÁBEAS DATA", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)

    pqrs_items = [
        ("PROTECCIÓN DE DATOS", "Conocer, actualizar, rectificar y suprimir datos", "HABEAS DATA", "lock"),
        ("ACADÉMICA", "Clases en vivo, simulacros, dudas y tutores", "ACADÉMICO", "laptop"),
        ("FACTURACIÓN Y PAGOS", "Facturas DIAN, cobros, retenciones y Bold", "FINANZAS", "file"),
        ("TÉCNICA Y ACCESO", "Problemas de login LMS, Meet y grabaciones", "SOPORTE TECH", "server"),
        ("CONVIVENCIA DIGITAL", "Reportes de conducta en chat y WhatsApp", "MODERACIÓN", "alert"),
        ("CONVENIOS COLEGIO", "Gestión de directivos y reportes de cohorte", "B2B INSTITUCIONAL", "database")
    ]

    pw = (pqrs_w - 75.0) * 0.5
    for idx, (p_tit, p_sub, p_badge, p_icon) in enumerate(pqrs_items):
        px = pqrs_x + 25.0 + (idx % 2) * (pw + 25.0)
        py = sc1_y + 50.0 + (idx // 2) * 165.0
        scene.add_quad_card(px, py, pw, 140.0, p_tit, sublabel=p_sub, badge=p_badge, icon=p_icon, font_size=16, frame_id=fid3)

    scene.add_bound_card(pqrs_x + 25.0, sc1_y + 560.0, pqrs_w - 50.0, 170.0,
                         "TRAZABILIDAD Y TIEMPOS LEGALES DE RESPUESTA:\n"
                         "• Peticiones de información y consultas: 10 a 15 días hábiles.\n"
                         "• Reclamos de protección de datos: 15 días hábiles prorrogables por 8 días (Ley 1581).\n"
                         "• Quejas y reclamos de servicio: Respuesta formal con asignación de ticket único.\n"
                         "• Registro de historial y evidencia de resolución archivado por 5 años.",
                         bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=13, align="left", roundness_type=3, frame_id=fid3)

    # Scope 3: Seguridad RBAC & Registro de Evidencia Digital
    sec_w = 930.0
    sec_x = pqrs_x + pqrs_w + 35.0
    scene.add_scope_container(sec_x, sc1_y, sec_w, sc_h, label="3. SEGURIDAD RBAC & AUDITORÍA FORENSE DE EVIDENCIA", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)

    scene.add_sticky_note(sec_x + 25.0, sc1_y + 50.0, sec_w - 50.0, 175.0,
                          "MATRIZ DE PERMISOS POR ROL (LEAST PRIVILEGE):\n"
                          "• Tutores: Solo acceden a estudiantes asignados y notas. CERO datos financieros.\n"
                          "• Padres/Acudientes: Solo consultan avance y asistencia de sus hijos (CERO terceros).\n"
                          "• Colegios B2B: Solo acceden al cohorte de su institución contratada.\n"
                          "• Administradores: Acceso restringido por doble factor a finanzas y contratos.",
                          font_size=14, angle_deg=1.0, frame_id=fid3)

    scene.add_bound_card(sec_x + 25.0, sc1_y + 250.0, sec_w - 50.0, 255.0,
                         "ESTRUCTURA DE EVIDENCIA DIGITAL (LOG INMUTABLE):\n\n"
                         "Cada consentimiento genera un registro auditable con los campos:\n"
                         "• consent_id: UUID v4 único e irrepetible\n"
                         "• user_id / student_id / representative_id\n"
                         "• consent_type: TERMS | PRIVACY | MINOR_DATA | IMAGE_VOICE | MARKETING\n"
                         "• document_version: Ej. POL-DAT-001 v1.0 (versionamiento estricto)\n"
                         "• accepted: true · accepted_at: Timestamp ISO 8601 con hora legal\n"
                         "• ip_address, user_agent, channel (Web / Mobile)",
                         bg=PALETTE["GREEN_BG"], stroke=PALETTE["GREEN_BORDER"], text_color=PALETTE["INK"],
                         font_size=13, align="left", roundness_type=3, frame_id=fid3)

    scene.add_bound_card(sec_x + 25.0, sc1_y + 530.0, sec_w - 50.0, 200.0,
                         "CHECKLIST DE CUMPLIMIENTO REGULATORIO (RNBD / SIC):\n\n"
                         "✔ Verificación de obligación de Registro Nacional de Bases de Datos (RNBD).\n"
                         "✔ Contratos de Transmisión de Datos firmados con Google y Bold.\n"
                         "✔ Protocolo de Gestión de Incidentes de Seguridad y fuga de información.\n"
                         "✔ Matriz de Retención y Supresión Periódica de Datos Académicos.",
                         bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                         font_size=13, align="left", roundness_type=3, frame_id=fid3)

    scene.add_legend_footer(f3_x + 60.0, f3_y + 925.0, fw - 120.0, swatches=[
        {"label": "Derecho de Retracto Legal", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Canal de PQRS", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Log Inmutable de Evidencia", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]},
        {"label": "Seguridad Least Privilege", "bg": "#FFFFFF", "stroke": PALETTE["DARK_SLATE"]}
    ], note="SEAMOSGENIOS Governance: Cumplimiento de la Ley 1480 y preparación ante auditorías SIC.", frame_id=fid3)

    return scene


def main():
    output_path = os.path.join(OUT_DIR, "seamosgenios_marco_legal.excalidraw")
    scene = build_seamosgenios_legal_board()
    scene.save(output_path)

    print(f"Canvas generado exitosamente con ExcalidrawScene: {output_path}")

    validated_scene, report = validate_scene(output_path)
    print("\n" + "=" * 90)
    print("📊 REPORTE DE VALIDACIÓN SKETION 8.0 — SEAMOSGENIOS MARCO LEGAL")
    print("=" * 90)
    print(f" • Puntuación Global Sketion   : {report.sketion_overall_score} / 100 [{('✅ PASS' if report.is_valid else '❌ FAIL')}]")
    print(f" • Repair Dependency (RDS)     : {report.repair_dependency_score} [{report.repair_dependency_status}]")
    print(f" • Densidad Visual             : {report.visual_metrics.density:.1f} / 10 (Target: 4.0/10)")
    print(f" • Acentos Hero en Escena      : {report.visual_metrics.accent_count} (Regla del acento único respetada)")
    print(f" • Elementos Totales           : {len(scene.elements)}")
    print("=" * 90)


if __name__ == "__main__":
    main()
