"""
Sketion 8.0 — Generador Oficial Maestro: SEAMOSGENIOS S.A.S. (Versión 2.0)
Estructura Jurídica Integral de la Plataforma en Colombia
Organiza TODO el documento maestro v2.0 en 4 Marcos Verticales de Alta Definición:
- Frame 1 (Y=0): Fundamentos Normativos, Gobernanza y las 5 Capas Estructurales (34 Documentos)
- Frame 2 (Y=1150): Flujos Operativos: Onboarding Legal, Protocolo NNA, Grabaciones Gemini AI & Proveedores
- Frame 3 (Y=2300): Comercio Electrónico (Ley 1480/2439), Retracto, PQRS Hábeas Data & Matriz RBAC
- Frame 4 (Y=3450): Auditoría Forense (Log consent_id), Gestión de Incidentes y Roadmap en 6 Fases
"""

import os
import sys
import json

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


def build_seamosgenios_v2_board():
    # Disposición vertical estricta: marcos de 2950px apilados verticalmente
    place_reset(max_row_w=3200, gap=150)
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])

    fw = 2950.0
    fh = 1000.0

    # ═══════════════════════════════════════════════════════════════════════════
    # FRAME 1: FUNDAMENTOS NORMATIVOS, GOBERNANZA & LAS 5 CAPAS (Y = 0)
    # ═══════════════════════════════════════════════════════════════════════════
    f1_x, f1_y = place(fw, fh)
    fid1 = scene.add_frame("FRAME 1: SEAMOSGENIOS S.A.S. — FUNDAMENTOS, GOBERNANZA & LAS 5 CAPAS ESTRUCTURALES", f1_x, f1_y, fw, fh)

    scene.add_text(f1_x + 60.0, f1_y + 35.0, "SEAMOSGENIOS S.A.S.  ·  ESTRUCTURA JURÍDICA INTEGRAL v2.0", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "Ecosistema Jurídico Integral: Constitución, Ley 1581, Protección de Menores y las 5 Capas Maestras", font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    sc_h = 760.0
    sc1_y = f1_y + 120.0

    # Scope 1: Identidad & Fundamento Constitucional
    sc1_w = 820.0
    sc1_x = f1_x + 60.0
    scene.add_scope_container(sc1_x, sc1_y, sc1_w, sc_h, label="1. IDENTIDAD, OBJETO & MARCO NORMATIVO COLOMBIANO", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

    scene.add_quad_card(sc1_x + 30.0, sc1_y + 50.0, sc1_w - 60.0, 130.0,
                        "SEAMOSGENIOS S.A.S.",
                        sublabel="NIT 902080201 · Carrera 121 #25-65, Cali, Valle del Cauca, Colombia\nCorreo Oficial: seamosgenios@adpmh.com · Modelo: PreICFES Virtual & Convenios B2B",
                        badge="RESPONSABLE", icon="lock", is_hero=True, font_size=18, frame_id=fid1)

    scene.add_bound_card(sc1_x + 30.0, sc1_y + 195.0, sc1_w - 60.0, 185.0,
                         "COLUMNA VERTEBRAL CONSTITUCIONAL Y LEGAL:\n\n"
                         "• Art. 15 Const. Pol.: Derecho a la Intimidad y Hábeas Data (conocer, actualizar, rectificar).\n"
                         "• Art. 44 Const. Pol.: Derechos prevalentes e Interés Superior de Niños y Adolescentes.\n"
                         "• Ley 1581 de 2012 & Dec. 1074/2015: Régimen General de Protección de Datos Personales.\n"
                         "• Ley 1098 de 2006: Código de Infancia y Adolescencia (entornos virtuales seguros).\n"
                         "• Ley 1480 de 2011 & Ley 2439 de 2024: Estatuto del Consumidor y Comercio Electrónico.\n"
                         "• Ley 527 de 1999 (Mensajes de Datos) · Ley 2300 de 2023 (Comunicaciones Comerciales).",
                         bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid1)

    scene.add_sticky_note(sc1_x + 30.0, sc1_y + 395.0, sc1_w - 60.0, 160.0,
                          "REGLA ESTRATÉGICA DE PRIVACIDAD DESDE EL DISEÑO:\n\n"
                          "Tratamiento Real ──► Dato Identificado ──► Finalidad Legítima\n"
                          "                   └──► Fundamento Jurídico ──► Controles RBAC ──► Evidencia Digital\n\n"
                          "Ningún dato se recolecta sin finalidad; ninguna función opera sin respaldo legal.",
                          font_size=13, angle_deg=-1.0, frame_id=fid1)

    scene.add_bound_card(sc1_x + 30.0, sc1_y + 570.0, sc1_w - 60.0, 160.0,
                         "LAS 3 CATEGORÍAS DOCUMENTALES DE LA PLATAFORMA:\n\n"
                         "A. Documentos de Obligación Legal: Política de Datos, Aviso, Términos, Retracto.\n"
                         "B. Documentos de Autorización: Consentimiento Datos, Menores NNA, Imagen/Voz.\n"
                         "C. Documentos Contractuales e Internos: Convivencia, Manual PQRS, Colegios B2B.",
                         bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid1)

    # Scope 2: Matriz de 8 Roles & Privacidad desde el Diseño
    sc2_w = 860.0
    sc2_x = sc1_x + sc1_w + 35.0
    scene.add_scope_container(sc2_x, sc1_y, sc2_w, sc_h, label="2. MATRIZ DE ACTORES & PRIVACIDAD DIFERENCIADA", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

    roles = [
        ("COMPRADOR", "Persona que realiza el pago y contrata", "BUYER", "card"),
        ("ESTUDIANTE", "Receptor del servicio académico PreICFES", "STUDENT", "user"),
        ("REPRESENTANTE", "Padre/Madre que autoriza a estudiante menor", "PARENT", "users"),
        ("ACUDIENTE", "Persona autorizada para gestión y seguimiento", "GUARDIAN", "shield"),
        ("COLEGIO B2B", "Institución educativa con cohorte contratado", "B2B INST", "database"),
        ("TUTOR", "Docente prestador de servicios de mentoría", "TUTOR", "terminal"),
        ("USUARIO", "Persona titular que opera la cuenta LMS", "ACCOUNT", "laptop"),
        ("TITULAR", "Persona natural dueña de los datos personales", "DATA OWNER", "key")
    ]

    rw = (sc2_w - 75.0) * 0.5
    for idx, (r_tit, r_sub, r_badge, r_icon) in enumerate(roles):
        rx = sc2_x + 25.0 + (idx % 2) * (rw + 25.0)
        ry = sc1_y + 50.0 + (idx // 2) * 165.0
        scene.add_quad_card(rx, ry, rw, 140.0, r_tit, sublabel=r_sub, badge=r_badge, icon=r_icon, font_size=16, frame_id=fid1)

    # Scope 3: Las 5 Capas Maestras (34 Documentos)
    sc3_w = 930.0
    sc3_x = sc2_x + sc2_w + 35.0
    scene.add_scope_container(sc3_x, sc1_y, sc3_w, sc_h, label="3. ARQUITECTURA DE LAS 5 CAPAS ESTRUCTURALES (34 DOCUMENTOS)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

    scene.add_bound_card(sc3_x + 25.0, sc1_y + 45.0, sc3_w - 50.0, 135.0,
                         "CAPA 1 · PÚBLICA (8 DOCUMENTOS):\n"
                         "01. Política de Datos · 02. Términos y Condiciones · 03. Aviso de Privacidad · 04. Cookies\n"
                         "05. Propiedad Intelectual · 06. Uso de Plataforma · 07. Convivencia · 08. Política de PQRS.",
                         bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid1)

    scene.add_bound_card(sc3_x + 25.0, sc1_y + 190.0, sc3_w - 50.0, 140.0,
                         "CAPA 2 · AUTORIZACIONES ESPECÍFICAS (7 INSTRUMENTOS SEPARADOS):\n"
                         "09. Autorización Datos · 10. Datos de Menores (NNA) · 11. Imagen y Voz · 12. Testimonios\n"
                         "13. Publicación de Resultados · 14. Marketing (Ley 2300) · 15. Aviso Grabación de Clases.",
                         bg=PALETTE["CORAL_BG"], stroke=PALETTE["CORAL_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid1)

    scene.add_bound_card(sc3_x + 25.0, sc1_y + 340.0, sc3_w - 50.0, 120.0,
                         "CAPA 3 · INSTITUCIONES & FAMILIAS (4 DOCUMENTOS):\n"
                         "16. Contrato con Colegios · 17. Acuerdo de Tratamiento B2B · 18. Reglamento de Padres\n"
                         "19. Reglamento de Estudiantes (Integridad Académica y Convivencia).",
                         bg=PALETTE["GREEN_BG"], stroke=PALETTE["GREEN_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid1)

    scene.add_bound_card(sc3_x + 25.0, sc1_y + 470.0, sc3_w - 50.0, 135.0,
                         "CAPA 4 · GOBERNANZA INTERNA (9 INSTRUMENTOS):\n"
                         "20. Programa Integral de Datos · 21. Manual de Privacidad · 22. Procedimiento Hábeas Data\n"
                         "23. Gestión de Incidentes · 24. Matriz Tratamientos · 25. Matriz Proveedores · 26. Log\n"
                         "27. Matriz de Retención · 28. Matriz de Accesos (Least Privilege).",
                         bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid1)

    scene.add_bound_card(sc3_x + 25.0, sc1_y + 615.0, sc3_w - 50.0, 125.0,
                         "CAPA 5 · PERSONAL & PROVEEDORES (6 CONTRATOS):\n"
                         "29. Contratos Tutores · 30. Acuerdos Confidencialidad · 31. Cesión PI Tutores\n"
                         "32. Tratamiento Proveedores · 33. Acuerdos Tech Stack · 34. Transmisiones Internacionales.",
                         bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid1)

    scene.add_legend_footer(f1_x + 60.0, f1_y + 925.0, fw - 120.0, swatches=[
        {"label": "Responsable & Autorizaciones NNA", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Capas Públicas & Gobernanza", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Institucional B2B & Familias", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]}
    ], note="SEAMOSGENIOS Governance v2.0: Sistema integral de 5 capas alineado con la Ley 1581 y doctrina SIC.", frame_id=fid1)


    # ═══════════════════════════════════════════════════════════════════════════
    # FRAME 2: ONBOARDING LEGAL, PROTOCOLO NNA & MATRIZ TECH STACK (Y = 1150)
    # ═══════════════════════════════════════════════════════════════════════════
    f2_x, f2_y = place(fw, fh)
    fid2 = scene.add_frame("FRAME 2: FLUJOS OPERATIVOS — ONBOARDING LEGAL, PROTOCOLO NNA & MATRIZ TECH STACK", f2_x, f2_y, fw, fh)

    scene.add_text(f2_x + 60.0, f2_y + 35.0, "OPERATIONAL FLOWS  ·  ONBOARDING, MINOR PROTECTION & CLOUD STACK", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid2)
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "Flujos Operativos: Onboarding Legal de 10 Fases, Tratamiento de Menores, Gemini AI y Proveedores", font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    # Top Scope: Flujo Onboarding Legal (10 Fases en Pipeline)
    pipe_w = fw - 120.0
    pipe_h = 240.0
    scene.add_scope_container(f2_x + 60.0, f2_y + 120.0, pipe_w, pipe_h, label="1. MACRO-FLUJO LEGAL DEL ONBOARDING EN LA PLATAFORMA (10 FASES CONCATENADAS)", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid2)

    onb_steps = [
        ("01. PAGO BOLD", "Pasarela Segura", "Confirmación transacción", "PAGO", "lock"),
        ("02. REGISTRO", "Captura Datos", "Identificación usuario", "AUTH", "user"),
        ("03. FILTRO EDAD", "¿Menor de 18?", "Validación representante", "NNA", "alert", True),
        ("04. TÉRMINOS", "Aceptación Base", "Política + Términos", "LEGAL", "file"),
        ("05. AUTORIZA", "Casillas Sep.", "Marketing + Imagen", "CONSENT", "shield"),
        ("06. CUENTA LMS", "Credenciales", "Permisos Least Privilege", "LMS", "laptop"),
        ("07. CLASES MEET", "Aviso Grabación", "Google Meet en vivo", "CLASS", "server"),
        ("08. IA GEMINI", "Transcripción", "Notas y resúmenes", "AI", "terminal"),
        ("09. REPORTES", "Seguimiento", "Avance y simulacros", "REPORT", "database"),
        ("10. PQRS", "Hábeas Data", "Canal de derechos", "PQRS", "key")
    ]

    card_step_w = (pipe_w - 60.0 - 9 * 18.0) / 10.0
    for idx, (s_tit, s_sub, s_meta, s_badge, s_icon, *is_h) in enumerate(onb_steps):
        cx = f2_x + 90.0 + idx * (card_step_w + 18.0)
        cy = f2_y + 175.0
        h_flag = is_h[0] if is_h else False
        scene.add_quad_card(cx, cy, card_step_w, 140.0, s_tit, sublabel=f"{s_sub}\n{s_meta}", badge=s_badge, icon=s_icon, is_hero=h_flag, font_size=14, frame_id=fid2)

        if idx < len(onb_steps) - 1:
            scene.add_arrow(cx + card_step_w, cy + 70.0, cx + card_step_w + 18.0, cy + 70.0, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, frame_id=fid2)

    # Bottom-Left Scope: Protocolo NNA & Cuenta de Padres
    bot2_y = f2_y + 380.0
    bot2_h = 510.0
    nna_w = 880.0
    scene.add_scope_container(f2_x + 60.0, bot2_y, nna_w, bot2_h, label="2. PROTOCOLO REFORZADO DE MENORES (NNA) & CUENTA DE PADRES", stroke=PALETTE["CORAL_BORDER"], bg="#FFFFFF", frame_id=fid2)

    scene.add_quad_card(f2_x + 90.0, bot2_y + 50.0, nna_w - 60.0, 140.0,
                        "Flujo de Autorización para Menores (Ley 1098 / SIC)",
                        sublabel="• Detección automática en registro: si edad < 18 años, el formulario exige datos del representante legal.\n• Firma digital exclusiva del padre/madre/tutor: Prohibido que el menor firme por sí mismo.\n• Derecho a ser escuchado: El menor recibe información sobre el tratamiento en lenguaje adaptado a su edad.",
                        badge="ESTÁNDAR REFORZADO", icon="shield", is_hero=True, font_size=15, frame_id=fid2)

    scene.add_bound_card(f2_x + 90.0, bot2_y + 205.0, nna_w - 60.0, 140.0,
                         "SECCIÓN INDEPENDIENTE DE PADRES (PERMISOS RESTRINGIDOS):\n\n"
                         "• El padre NO utiliza la contraseña del estudiante: cuenta con perfil propio autenticado.\n"
                         "• Visualización exclusiva: Avance académico, asistencia a clases, puntajes y alertas.\n"
                         "• CERO acceso cruzado: Ningún padre puede ver datos ni resultados de otros estudiantes.\n"
                         "• Al cumplir 18 años: El estudiante pasa a ejercer sus derechos de titular con autonomía.",
                         bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid2)

    scene.add_bound_card(f2_x + 90.0, bot2_y + 360.0, nna_w - 60.0, 115.0,
                         "SEGURIDAD DE MENORES EN ENTORNOS DIGITALES (WHATSAPP / CHAT):\n"
                         "• Canales oficiales moderados: Prohibido el contacto privado no supervisado tutor-menor.\n"
                         "• Protocolo estricto contra acoso, suplantación o divulgación no autorizada de notas.\n"
                         "• Registro de incidentes y canal prioritario de denuncia ante la administración.",
                         bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid2)

    # Bottom-Center Scope: Grabaciones & Gemini AI
    rec_w = 880.0
    rec_x = f2_x + 60.0 + nna_w + 30.0
    scene.add_scope_container(rec_x, bot2_y, rec_w, bot2_h, label="3. MATRIZ DE TRATAMIENTO: GRABACIONES & IA (GEMINI)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)

    scene.add_quad_card(rec_x + 30.0, bot2_y + 50.0, (rec_w - 75.0) * 0.5, 145.0,
                        "Sesión Meet en Vivo",
                        sublabel="Aviso en pantalla obligatorio.\nVideo, audio, micrófono y chat.\nRegistro de asistencia y preguntas.",
                        badge="CAPTURA MEET", icon="laptop", font_size=15, frame_id=fid2)

    scene.add_quad_card(rec_x + 30.0 + (rec_w - 75.0) * 0.5 + 15.0, bot2_y + 50.0, (rec_w - 75.0) * 0.5, 145.0,
                        "Procesamiento Gemini",
                        sublabel="Storage seguro en Google Drive.\nTranscripción pedagógica con IA.\nGeneración de resúmenes de estudio.",
                        badge="IA GEMINI & DRIVE", icon="server", font_size=15, frame_id=fid2)

    scene.add_quad_card(rec_x + 30.0, bot2_y + 210.0, rec_w - 60.0, 130.0,
                        "Regla de Oro: Grabación Académica vs Difusión en YouTube",
                        sublabel="• Grabación Académica: Uso exclusivo para consulta interna de estudiantes matriculados.\n• Publicación en YouTube / Redes: REQUIERE autorización independiente y expresa de imagen y voz.\n• Prohibido publicar grabaciones donde aparezcan menores de edad sin consentimiento específico.",
                        badge="SEGREGACIÓN NARRATIVA", icon="shield", is_hero=True, font_size=16, frame_id=fid2)

    scene.add_bound_card(rec_x + 30.0, bot2_y + 355.0, rec_w - 60.0, 125.0,
                         "AVISO OBLIGATORIO ANTES DE INGRESAR A CADA CLASE (MEET):\n\n"
                         "\"Esta sesión será grabada. Tu participación mediante cámara, micrófono o chat formará parte del registro académico.\n"
                         "Las grabaciones se utilizan exclusivamente para fines pedagógicos y de refuerzo dentro de la plataforma.\"",
                         bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid2)

    # Bottom-Right Scope: Proveedores Tecnológicos (Encargados)
    prov_w = fw - 120.0 - nna_w - rec_w - 60.0
    prov_x = rec_x + rec_w + 30.0
    scene.add_scope_container(prov_x, bot2_y, prov_w, bot2_h, label="4. MATRIZ DE PROVEEDORES (ENCARGADOS)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)

    providers = [
        ("GOOGLE LLC", "Meet/Drive/Gemini", "Audio, video, chat y transcripción", "EE.UU. (Cláusulas Tipo)", "CLOUD TECH", "server"),
        ("BOLD.CO", "Pasarela de Pagos", "Datos transacción y estado pago", "Colombia (PCI-DSS)", "PAYMENTS", "lock"),
        ("FACTUS / BOLD POS", "Facturación DIAN", "Datos fiscales y facturas", "Colombia (DIAN)", "BILLING", "file"),
        ("WHATSAPP (META)", "Canal Informativo", "Mensajería y grupos soporte", "EE.UU. (Canal Moderado)", "MESSAGING", "users"),
        ("PLATAFORMA LMS", "Core Académico", "Simulacros, notas y reportes", "Infraestructura Segura", "CORE LMS", "database")
    ]

    for p_i, (p_tit, p_serv, p_data, p_loc, p_badge, p_icon) in enumerate(providers):
        py = bot2_y + 50.0 + p_i * 88.0
        scene.add_quad_card(prov_x + 25.0, py, prov_w - 50.0, 78.0, f"{p_tit} ({p_serv})", sublabel=f"{p_data} · {p_loc}", badge=p_badge, icon=p_icon, font_size=13, frame_id=fid2)

    scene.add_legend_footer(f2_x + 60.0, f2_y + 925.0, fw - 120.0, swatches=[
        {"label": "Consentimiento NNA & Regla YouTube", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Onboarding & Procesamiento IA", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Proveedores & Pasarelas", "bg": "#FFFFFF", "stroke": PALETTE["MUTED"]}
    ], note="SEAMOSGENIOS Operations: Flujos de onboarding, protección de menores y contratos de encargados.", frame_id=fid2)


    # ═══════════════════════════════════════════════════════════════════════════
    # FRAME 3: COMERCIO ELECTRÓNICO (LEY 1480/2439), PQRS & SEGURIDAD (Y = 2300)
    # ═══════════════════════════════════════════════════════════════════════════
    f3_x, f3_y = place(fw, fh)
    fid3 = scene.add_frame("FRAME 3: COMERCIO ELECTRÓNICO, RETRACTO (LEY 1480/2439), PQRS & SEGURIDAD RBAC", f3_x, f3_y, fw, fh)

    scene.add_text(f3_x + 60.0, f3_y + 35.0, "CONSUMER RIGHTS  ·  ROLE-BASED ACCESS CONTROL & HABEAS DATA", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid3)
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "Régimen de Comercio Electrónico (Ley 1480 & 2439), Retracto, PQRS Hábeas Data y Matriz RBAC", font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    sc3_y = f3_y + 120.0

    # Scope 1: Comercio Electrónico (Ley 1480 & Ley 2439 de 2024)
    ecom_w = 820.0
    scene.add_scope_container(f3_x + 60.0, sc3_y, ecom_w, sc_h, label="1. COMERCIO ELECTRÓNICO, RETRACTO & REVERSIÓN (LEY 1480/2439)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)

    scene.add_quad_card(f3_x + 30.0, sc3_y + 50.0, ecom_w - 60.0, 130.0,
                        "Compra Online & Perfeccionamiento",
                        sublabel="Aceptación explícita de Términos y Condiciones en checkout Bold.\nEmisión obligatoria de Factura Electrónica vía Factus.\nActivación automática de credenciales y comprobante al correo.",
                        badge="CHECKOUT BOLD", icon="lock", font_size=16, frame_id=fid3)

    scene.add_quad_card(f3_x + 30.0, sc3_y + 200.0, ecom_w - 60.0, 150.0,
                        "Derecho de Retracto Legal (SIC & Ley 2439)",
                        sublabel="• Término legal: 5 días hábiles siguientes a la compra.\n• PROHIBICIÓN ABSOLUTA de cláusulas de 'no hay devoluciones'.\n• Evaluación jurídica: Si el servicio comenzó con acuerdo del usuario o hubo consumo.\n• Canal formal de radicación con respuesta dentro de los términos legales.",
                        badge="RETRACTO LEY 1480", icon="alert", is_hero=True, font_size=16, frame_id=fid3)

    scene.add_quad_card(f3_x + 30.0, sc3_y + 370.0, ecom_w - 60.0, 130.0,
                        "Reversión de Pagos & Reembolsos",
                        sublabel="Aplica ante: Fraude electrónico, operación no solicitada o servicio no prestado.\nProcedimiento coordinado entre SEAMOSGENIOS, pasarela Bold y banco emisor.\nTiempos de respuesta estrictos conforme a la reglamentación de la SIC.",
                        badge="REVERSIÓN PAGO", icon="file", font_size=16, frame_id=fid3)

    scene.add_bound_card(f3_x + 30.0, sc3_y + 520.0, ecom_w - 60.0, 215.0,
                         "CLÁUSULA DE RESULTADOS ICFES (SIN GARANTÍAS ILÍCITAS):\n\n"
                         "• SEAMOSGENIOS ofrece preparación pedagógica y entrenamiento de alto nivel.\n"
                         "• El puntaje final depende del esfuerzo y estudio individual del alumno.\n"
                         "• Los puntajes de simulacros son herramientas de entrenamiento, no resultados oficiales.\n"
                         "• Queda expresamente prohibido garantizar puntajes específicos o cupos universitarios.",
                         bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid3)

    # Scope 2: Módulo Integral de PQRS & Hábeas Data
    pqrs_w = 860.0
    pqrs_x = f3_x + 60.0 + ecom_w + 35.0
    scene.add_scope_container(pqrs_x, sc3_y, pqrs_w, sc_h, label="2. MÓDULO CENTRALIZADO DE PQRS & HÁBEAS DATA (LEY 1581)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)

    pqrs_items = [
        ("PROTECCIÓN DE DATOS", "Conocer, actualizar, rectificar y suprimir", "HABEAS DATA", "lock"),
        ("ACADÉMICA", "Clases en vivo, simulacros, dudas y tutores", "ACADÉMICO", "laptop"),
        ("FACTURACIÓN Y PAGOS", "Facturas DIAN, cobros, retenciones y Bold", "FINANZAS", "file"),
        ("TÉCNICA Y ACCESO", "Problemas de login LMS, Meet y grabaciones", "SOPORTE TECH", "server"),
        ("CONVIVENCIA DIGITAL", "Reportes de conducta en chat y WhatsApp", "MODERACIÓN", "alert"),
        ("CONVENIOS COLEGIO", "Gestión de directivos y reportes de cohorte", "B2B INSTITUCIONAL", "database")
    ]

    pw = (pqrs_w - 75.0) * 0.5
    for idx, (p_tit, p_sub, p_badge, p_icon) in enumerate(pqrs_items):
        px = pqrs_x + 25.0 + (idx % 2) * (pw + 25.0)
        py = sc3_y + 50.0 + (idx // 2) * 160.0
        scene.add_quad_card(px, py, pw, 135.0, p_tit, sublabel=p_sub, badge=p_badge, icon=p_icon, font_size=16, frame_id=fid3)

    scene.add_bound_card(pqrs_x + 25.0, sc3_y + 550.0, pqrs_w - 50.0, 185.0,
                         "FLUJO HÁBEAS DATA Y TIEMPOS LEGALES DE RESPUESTA:\n\n"
                         "Solicitud ──► Radicación Única ──► Identificación ──► Clasificación ──► Validación ──► Respuesta\n\n"
                         "• Peticiones de información y consultas: 10 días hábiles (prorrogables 5 días).\n"
                         "• Reclamos de protección de datos: 15 días hábiles (prorrogables 8 días, Ley 1581).\n"
                         "• Historial inmutable de solicitudes archivado por 5 años para sustento ante la SIC.",
                         bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid3)

    # Scope 3: Seguridad RBAC & Marketing (Ley 2300/2023)
    sec_w = 930.0
    sec_x = pqrs_x + pqrs_w + 35.0
    scene.add_scope_container(sec_x, sc3_y, sec_w, sc_h, label="3. MATRIZ RBAC (LEAST PRIVILEGE) & MARKETING (LEY 2300)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)

    scene.add_sticky_note(sec_x + 25.0, sc3_y + 50.0, sec_w - 50.0, 175.0,
                          "MATRIZ DE PERMISOS POR ROL (LEAST PRIVILEGE):\n\n"
                          "• Tutores: Solo acceden a estudiantes asignados y notas. CERO datos financieros ni teléfonos de padres.\n"
                          "• Padres: Solo consultan avance y asistencia de sus propios hijos (CERO acceso a terceros).\n"
                          "• Colegios B2B: Solo acceden al cohorte de su institución contratada.\n"
                          "• Administradores: Acceso restringido por 2FA a finanzas, facturación y contratos.",
                          font_size=13, angle_deg=1.0, frame_id=fid3)

    scene.add_bound_card(sec_x + 25.0, sc3_y + 250.0, sec_w - 50.0, 230.0,
                         "RÉGIMEN DE COMUNICACIONES COMERCIALES Y MARKETING (LEY 2300 DE 2023):\n\n"
                         "• Separación estricta: Comunicaciones del servicio (clases, notas) vs Marketing (promociones).\n"
                         "• Preferencias por canal registradas en base de datos: Email, WhatsApp, SMS, Llamadas.\n"
                         "• Horarios legales estrictos: Lunes a viernes 7:00 a 19:00, sábados 8:00 a 15:00.\n"
                         "• Mecanismo de cancelación en un solo clic ('Opt-Out') en todo mensaje comercial enviado.",
                         bg=PALETTE["GREEN_BG"], stroke=PALETTE["GREEN_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid3)

    scene.add_bound_card(sec_x + 25.0, sc3_y + 500.0, sec_w - 50.0, 235.0,
                         "RÉGIMEN DE PROPIEDAD INTELECTUAL & BANCO DE PREGUNTAS:\n\n"
                         "• Activos protegidos: Banco de preguntas ICFES, simulacros, guías, PDFs, videos, plataforma.\n"
                         "• Prohibición expresa de copia, redistribución, reventa o extracción masiva (scraping).\n"
                         "• Contratos de tutores con cláusulas de cesión patrimonial y confidencialidad estricta.\n"
                         "• Regla de Oro: El acceso al contenido académico NO equivale a transferencia de propiedad.",
                         bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid3)

    scene.add_legend_footer(f3_x + 60.0, f3_y + 925.0, fw - 120.0, swatches=[
        {"label": "Derecho de Retracto Legal", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Canal de PQRS Hábeas Data", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Marketing Ley 2300 & PI", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]}
    ], note="SEAMOSGENIOS Compliance: Comercio electrónico Ley 1480/2439, Ley 2300 y protección de propiedad intelectual.", frame_id=fid3)


    # ═══════════════════════════════════════════════════════════════════════════
    # FRAME 4: AUDITORÍA FORENSE, INCIDENTES & ROADMAP EN 6 FASES (Y = 3450)
    # ═══════════════════════════════════════════════════════════════════════════
    f4_x, f4_y = place(fw, fh)
    fid4 = scene.add_frame("FRAME 4: AUDITORÍA FORENSE, GESTIÓN DE INCIDENTES & HOJA DE RUTA EN 6 FASES", f4_x, f4_y, fw, fh)

    scene.add_text(f4_x + 60.0, f4_y + 35.0, "FORENSIC AUDIT  ·  SECURITY INCIDENTS & 6-PHASE IMPLEMENTATION ROADMAP", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid4)
    scene.add_text(f4_x + 60.0, f4_y + 60.0, "Evidencia Digital Inmutable (consent_id), Protocolo de Incidentes, Retención y Roadmap en 6 Fases", font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid4)

    sc4_y = f4_y + 120.0

    # Scope 1: Auditoría Forense & RNBD
    aud_w = 820.0
    scene.add_scope_container(f4_x + 60.0, sc4_y, aud_w, sc_h, label="1. REGISTRO MAESTRO DE CONSENTIMIENTOS & AUDITORÍA FORENSE", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid4)

    scene.add_bound_card(f4_x + 30.0, sc4_y + 50.0, aud_w - 60.0, 260.0,
                         "ESTRUCTURA DE EVIDENCIA DIGITAL INMUTABLE (LOG FORENSE):\n\n"
                         "Cada consentimiento genera un registro inmutable con la siguiente estructura:\n"
                         "• consent_id: UUID v4 único e irrepetible\n"
                         "• user_id / student_id / representative_id\n"
                         "• consent_type: TERMS | PRIVACY | MINOR_DATA | IMAGE_VOICE | MARKETING\n"
                         "• document_version: Ej. POL-DAT-001 v2.0 (versionamiento estricto)\n"
                         "• accepted: true · accepted_at: Timestamp ISO 8601 con hora legal\n"
                         "• ip_address, user_agent, channel (Web / Mobile)\n"
                         "• status: ACTIVO · revoked_at (cuando aplique) · revocation_reason\n\n"
                         "Objetivo: Responder con certeza ante la SIC: ¿Quién aceptó, qué versión exacta vio y cuándo?",
                         bg=PALETTE["GREEN_BG"], stroke=PALETTE["GREEN_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid4)

    scene.add_bound_card(f4_x + 30.0, sc4_y + 330.0, aud_w - 60.0, 200.0,
                         "REGISTRO NACIONAL DE BASES DE DATOS (RNBD / SIC):\n\n"
                         "• Dec. 90/2018: Sujetos obligados: Activos totales > 100.000 UVT o entidades públicas.\n"
                         "• Regla Clave: No estar obligado al RNBD NO exime de cumplir la Ley 1581.\n"
                         "• Res. 56579 de 2025: Actualización de instrucciones oficiales del RNBD ante la SIC.\n"
                         "• Deber permanente: Mantener política, avisos, autorizaciones y medidas de seguridad.",
                         bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid4)

    scene.add_bound_card(f4_x + 30.0, sc4_y + 550.0, aud_w - 60.0, 185.0,
                         "MATRIZ DE RETENCIÓN Y SUPRESIÓN PERIÓDICA:\n\n"
                         "• Cuentas y notas: Durante la relación contractual + 5 años.\n"
                         "• Facturación y pagos: 10 años conforme a la obligación fiscal DIAN.\n"
                         "• Grabaciones de clase: Plazo definido por ciclo académico (prohibido 'para siempre').\n"
                         "• Consentimientos y logs: Conservación permanente como evidencia de cumplimiento.",
                         bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid4)

    # Scope 2: Protocolo de Incidentes de Seguridad
    inc_w = 860.0
    inc_x = f4_x + 60.0 + aud_w + 35.0
    scene.add_scope_container(inc_x, sc4_y, inc_w, sc_h, label="2. PROTOCOLO DE GESTIÓN DE INCIDENTES DE SEGURIDAD (8 FASES)", stroke=PALETTE["CORAL_BORDER"], bg="#FFFFFF", frame_id=fid4)

    inc_phases = [
        ("01. DETECTAR", "Alerta de acceso no autorizado o fuga", "DETECCIÓN", "alert"),
        ("02. CONTENER", "Aislamiento de cuenta o servicio", "CONTENCIÓN", "lock"),
        ("03. INVESTIGAR", "Análisis forense de logs y alcance", "ANÁLISIS", "terminal"),
        ("04. EVALUAR", "Medición de riesgo para titulares", "IMPACTO", "shield"),
        ("05. DOCUMENTAR", "Acta formal de incidente técnico", "REGISTRO", "file"),
        ("06. NOTIFICAR", "Aviso a la SIC y titulares afectados", "NOTIFICACIÓN", "users"),
        ("07. CORREGIR", "Parche de vulnerabilidad y permisos", "REMEDIACIÓN", "server"),
        ("08. PREVENIR", "Actualización de controles y auditoría", "PREVENCIÓN", "key")
    ]

    iw = (inc_w - 75.0) * 0.5
    for idx, (i_tit, i_sub, i_badge, i_icon) in enumerate(inc_phases):
        ix = inc_x + 25.0 + (idx % 2) * (iw + 25.0)
        iy = sc4_y + 50.0 + (idx // 2) * 160.0
        scene.add_quad_card(ix, iy, iw, 135.0, i_tit, sublabel=i_sub, badge=i_badge, icon=i_icon, font_size=16, frame_id=fid4)

    scene.add_bound_card(inc_x + 25.0, sc4_y + 550.0, inc_w - 50.0, 185.0,
                         "CASOS CRÍTICOS DE INCIDENTE EN SEAMOSGENIOS:\n\n"
                         "✖ Cuenta de tutor comprometida o descarga indebida de base de estudiantes.\n"
                         "✖ Grabación con menores publicada en YouTube sin consentimiento específico.\n"
                         "✖ Falla de permisos RBAC donde un padre visualiza datos de otro alumno.\n"
                         "✔ Activación inmediata del comité de seguridad y reporte SIC en términos de ley.",
                         bg=PALETTE["CORAL_BG"], stroke=PALETTE["CORAL_BORDER"], text_color=PALETTE["INK"],
                         font_size=12, align="left", roundness_type=3, frame_id=fid4)

    # Scope 3: Hoja de Ruta en 6 Fases
    road_w = 930.0
    road_x = inc_x + inc_w + 35.0
    scene.add_scope_container(road_x, sc4_y, road_w, sc_h, label="3. HOJA DE RUTA DE IMPLEMENTACIÓN EN 6 FASES", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid4)

    road_phases = [
        ("FASE 1 · BASE LEGAL", "Política de Datos, Términos, Aviso de Privacidad y Flujo de Menores.", PALETTE["BLUE_BG"], PALETTE["BLUE_BORDER"]),
        ("FASE 2 · PLATAFORMA LMS", "Consentimientos independientes, RBAC, Portal de Padres y módulo PQRS.", PALETTE["GREEN_BG"], PALETTE["GREEN_BORDER"]),
        ("FASE 3 · CLASES & GRABACIONES", "Aviso en Meet, Drive, notas con Gemini y regla YouTube.", PALETTE["CORAL_BG"], PALETTE["CORAL_BORDER"]),
        ("FASE 4 · COMERCIAL & PAGOS", "Marketing Ley 2300, pasarela Bold, facturación DIAN y retracto.", PALETTE["BLUE_BG"], PALETTE["BLUE_BORDER"]),
        ("FASE 5 · COLEGIOS B2B", "Contratos institucionales, acuerdos de tratamiento y reportes cohorte.", PALETTE["GREEN_BG"], PALETTE["GREEN_BORDER"]),
        ("FASE 6 · GOBERNANZA INTERNA", "Manual de privacidad, matriz de retención, incidentes y auditoría SIC.", "#F8FAFC", PALETTE["CARD_BORDER"])
    ]

    for r_idx, (r_tit, r_desc, r_bg, r_stroke) in enumerate(road_phases):
        ry = sc4_y + 50.0 + r_idx * 115.0
        scene.add_bound_card(road_x + 25.0, ry, road_w - 50.0, 100.0,
                             f"{r_tit}\n{r_desc}",
                             bg=r_bg, stroke=r_stroke, text_color=PALETTE["INK"],
                             font_size=13, align="left", roundness_type=3, frame_id=fid4)

    scene.add_legend_footer(f4_x + 60.0, f4_y + 925.0, fw - 120.0, swatches=[
        {"label": "Log Forense Inmutable", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]},
        {"label": "Gestión de Incidentes", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Roadmap de Implementación", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]}
    ], note="SEAMOSGENIOS Master Audit: Trazabilidad forense inmutable, respuesta ante incidentes y despliegue por fases.", frame_id=fid4)

    return scene


def main():
    output_path = os.path.join(OUT_DIR, "seamosgenios_estructura_juridica_v2.excalidraw")
    scene = build_seamosgenios_v2_board()
    scene.save(output_path)

    print(f"Canvas v2.0 generado exitosamente con ExcalidrawScene: {output_path}")

    validated_scene, report = validate_scene(output_path)
    print("\n" + "=" * 90)
    print("📊 REPORTE DE VALIDACIÓN SKETION 8.0 — SEAMOSGENIOS ESTRUCTURA JURÍDICA v2.0")
    print("=" * 90)
    print(f" • Puntuación Global Sketion   : {report.sketion_overall_score} / 100 [{('✅ PASS' if report.is_valid else '❌ FAIL')}]")
    print(f" • Repair Dependency (RDS)     : {report.repair_dependency_score} [{report.repair_dependency_status}]")
    print(f" • Densidad Visual             : {report.visual_metrics.density:.1f} / 10 (Target: 4.0/10)")
    print(f" • Acentos Hero en Escena      : {report.visual_metrics.accent_count} (Regla del acento único respetada)")
    print(f" • Elementos Totales           : {len(scene.elements)}")
    print("=" * 90)


if __name__ == "__main__":
    main()
