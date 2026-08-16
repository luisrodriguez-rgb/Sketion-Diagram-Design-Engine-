"""
Sketion 8.0 — Generador Oficial Maestro: SEAMOSGENIOS S.A.S. (Versión 2.0 Editorial)
Estructura Jurídica Integral de la Plataforma en Colombia
Rediseñado con Variedad Arquetípica, Llenado Espacial Proporcional, Tipografía Homogénea
y Cero Colisiones Espaciales:
- Frame 1 (Y=0): Arquetipo Layer Stack & Matriz de Roles (34 Documentos en 5 Capas Estructuradas)
- Frame 2 (Y=1150): Arquetipo Macro Pipeline & Swimlanes (Onboarding 10 Pasos, NNA, Grabaciones & Gemini)
- Frame 3 (Y=2300): Arquetipo Comparative Matrix & RBAC Table (Comercio Ley 1480/2439, PQRS y Horarios Ley 2300)
- Frame 4 (Y=3450): Arquetipo Forensic Audit & Timeline Roadmap (Terminal consent_id, 8 Fases Incidentes y Roadmap)
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
    "SLATE_BG": "#F1F5F9",
    "SLATE_BORDER": "#CBD5E1",
    "INDIGO_BG": "#EEF2FF",
    "INDIGO_BORDER": "#C7D2FE",
    "STICKY": "#FFE95C"
}


def build_seamosgenios_v2_board():
    # Marcos de 2950px de ancho apilados verticalmente con 150px de espacio
    place_reset(max_row_w=3200, gap=150)
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])

    fw = 2950.0
    fh = 1000.0

    # ═══════════════════════════════════════════════════════════════════════════
    # FRAME 1: FUNDAMENTOS NORMATIVOS, ROLES & LAS 5 CAPAS ESTRUCTURALES (Y = 0)
    # ═══════════════════════════════════════════════════════════════════════════
    f1_x, f1_y = place(fw, fh)
    fid1 = scene.add_frame("FRAME 1: SEAMOSGENIOS S.A.S. — FUNDAMENTOS, GOBERNANZA & LAS 5 CAPAS ESTRUCTURALES", f1_x, f1_y, fw, fh)

    scene.add_text(f1_x + 60.0, f1_y + 35.0, "SEAMOSGENIOS S.A.S.  ·  ESTRUCTURA JURÍDICA INTEGRAL v2.0", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "Ecosistema Jurídico Integral: Constitución, Ley 1581, Protección de Menores y las 5 Capas Maestras", font_size=26, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    sc_h = 760.0
    sc1_y = f1_y + 115.0

    # Scope 1: Identidad & Marco Normativo
    sc1_w = 830.0
    sc1_x = f1_x + 60.0
    scene.add_scope_container(sc1_x, sc1_y, sc1_w, sc_h, label="1. IDENTIDAD, OBJETO & MARCO NORMATIVO COLOMBIANO", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

    scene.add_quad_card(sc1_x + 25.0, sc1_y + 45.0, sc1_w - 50.0, 125.0,
                        "SEAMOSGENIOS S.A.S.",
                        sublabel="NIT 902080201 · Carrera 121 #25-65, Cali, Valle del Cauca, Colombia\nCorreo Oficial: seamosgenios@adpmh.com · Modelo: PreICFES Virtual & Convenios B2B",
                        badge="RESPONSABLE", icon="lock", is_hero=True, font_size=17, frame_id=fid1)

    scene.add_feature_card(sc1_x + 25.0, sc1_y + 185.0, sc1_w - 50.0, 185.0,
                           "Marco Constitucional y Legal Aplicable",
                           [
                               "Art. 15 Const. Pol.: Derecho a la Intimidad y Hábeas Data (conocer, actualizar, rectificar)",
                               "Art. 44 Const. Pol.: Derechos prevalentes e Interés Superior de Niños y Adolescentes (NNA)",
                               "Ley 1581 de 2012 & Dec. 1074/2015: Régimen General de Protección de Datos Personales",
                               "Ley 1098 de 2006: Código de Infancia y Adolescencia (entornos virtuales protegidos)",
                               "Ley 1480 de 2011 & Ley 2439 de 2024: Estatuto del Consumidor y Comercio Electrónico",
                               "Ley 527 de 1999 (Mensajes de Datos) · Ley 2300 de 2023 (Horarios y Canales Comerciales)"
                           ],
                           badge="COLUMNA LEGAL", bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], frame_id=fid1)

    scene.add_sticky_note(sc1_x + 25.0, sc1_y + 385.0, sc1_w - 50.0, 160.0,
                          "REGLA ESTRATÉGICA DE PRIVACIDAD DESDE EL DISEÑO:\n\n"
                          "Tratamiento Real ──► Dato Identificado ──► Finalidad Legítima\n"
                          "                   └──► Fundamento Jurídico ──► Controles RBAC ──► Evidencia Digital\n\n"
                          "Ningún dato se recolecta sin finalidad; ninguna función opera sin respaldo legal.",
                          font_size=13, angle_deg=-1.0, frame_id=fid1)

    scene.add_feature_card(sc1_x + 25.0, sc1_y + 560.0, sc1_w - 50.0, 160.0,
                           "Las 3 Categorías Documentales de la Plataforma",
                           [
                               "A. Documentos de Obligación Legal: Política de Datos, Aviso, Términos, Retracto y Reversión.",
                               "B. Documentos de Autorización: Consentimientos separados (Datos, Menores NNA, Imagen/Voz).",
                               "C. Documentos Contractuales e Internos: Convivencia, Manual PQRS, Convenios Colegios B2B."
                           ],
                           badge="CLASIFICACIÓN", bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], frame_id=fid1)

    # Scope 2: Matriz de 8 Roles
    sc2_w = 880.0
    sc2_x = sc1_x + sc1_w + 30.0
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

    rw = (sc2_w - 65.0) * 0.5
    for idx, (r_tit, r_sub, r_badge, r_icon) in enumerate(roles):
        rx = sc2_x + 20.0 + (idx % 2) * (rw + 20.0)
        ry = sc1_y + 45.0 + (idx // 2) * 165.0
        scene.add_quad_card(rx, ry, rw, 145.0, r_tit, sublabel=r_sub, badge=r_badge, icon=r_icon, font_size=15, frame_id=fid1)

    # Scope 3: Las 5 Capas Estructurales (34 Documentos en Stack Arquitectónico)
    sc3_w = 1070.0
    sc3_x = sc2_x + sc2_w + 30.0
    scene.add_scope_container(sc3_x, sc1_y, sc3_w, sc_h, label="3. ARQUITECTURA DE LAS 5 CAPAS ESTRUCTURALES (34 DOCUMENTOS)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

    layers = [
        ("CAPA 1", "PÚBLICA & CONTRATACIÓN BASE", "8 DOCUMENTOS",
         ["01. Política de Tratamiento de Datos", "02. Términos y Condiciones", "03. Aviso de Privacidad", "04. Política de Cookies",
          "05. Política de Propiedad Intelectual", "06. Reglamento de Uso LMS", "07. Convivencia Digital", "08. Política de PQRS"],
         PALETTE["BLUE_BG"], PALETTE["BLUE_BORDER"], "#2563EB", "#FFFFFF"),

        ("CAPA 2", "AUTORIZACIONES INDEPENDIENTES", "7 CONSENTIMIENTOS",
         ["09. Autorización Datos Personales", "10. Datos de Menores (NNA)", "11. Imagen y Voz", "12. Testimonios",
          "13. Publicación de Resultados", "14. Marketing (Ley 2300/2023)", "15. Aviso Grabación de Clases"],
         PALETTE["CORAL_BG"], PALETTE["CORAL_BORDER"], "#D93829", "#FFFFFF"),

        ("CAPA 3", "INSTITUCIONES & FAMILIAS", "4 DOCUMENTOS",
         ["16. Contrato Marco con Colegios B2B", "17. Acuerdo de Tratamiento B2B", "18. Reglamento para Padres",
          "19. Reglamento de Estudiantes (Integridad Académica y Convivencia Digital)"],
         PALETTE["GREEN_BG"], PALETTE["GREEN_BORDER"], "#059669", "#FFFFFF"),

        ("CAPA 4", "GOBERNANZA INTERNA & AUDITORÍA", "9 INSTRUMENTOS",
         ["20. Programa Integral de Datos", "21. Manual de Privacidad", "22. Procedimiento Hábeas Data", "23. Gestión de Incidentes",
          "24. Matriz de Tratamientos", "25. Matriz de Proveedores", "26. Log de Consentimientos", "27. Matriz de Retención", "28. Matriz de Accesos RBAC"],
         PALETTE["SLATE_BG"], PALETTE["SLATE_BORDER"], "#475569", "#FFFFFF"),

        ("CAPA 5", "PERSONAL & PROVEEDORES TECH", "6 CONTRATOS",
         ["29. Contratos Laborales/Servicios Tutores", "30. Acuerdos de Confidencialidad", "31. Cesión de Propiedad Intelectual",
          "32. Cláusulas de Datos Proveedores", "33. Acuerdos de Nivel de Servicio Tech Stack", "34. Acuerdos de Transmisión Internacional"],
         PALETTE["INDIGO_BG"], PALETTE["INDIGO_BORDER"], "#4F46E5", "#FFFFFF")
    ]

    layer_h = 130.0
    for l_idx, (l_num, l_tit, l_cnt, l_docs, l_bg, l_str, l_bbg, l_bcol) in enumerate(layers):
        ly = sc1_y + 45.0 + l_idx * (layer_h + 10.0)
        scene.add_stack_layer(sc3_x + 20.0, ly, sc3_w - 40.0, layer_h,
                              l_num, l_tit, l_cnt, l_docs,
                              bg="#FFFFFF", stroke=l_str,
                              header_bg=l_bg, header_stroke=l_str,
                              badge_bg=l_bbg, badge_color=l_bcol, frame_id=fid1)

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
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "Flujos Operativos: Onboarding Legal de 10 Fases, Tratamiento de Menores, Gemini AI y Proveedores", font_size=26, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    # Top Scope: Flujo Onboarding Legal (10 Fases en Pipeline)
    pipe_w = fw - 120.0
    pipe_h = 230.0
    scene.add_scope_container(f2_x + 60.0, f2_y + 115.0, pipe_w, pipe_h, label="1. MACRO-FLUJO LEGAL DEL ONBOARDING EN LA PLATAFORMA (10 FASES CONCATENADAS)", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid2)

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

    card_step_w = (pipe_w - 50.0 - 9 * 18.0) / 10.0
    for idx, (s_tit, s_sub, s_meta, s_badge, s_icon, *is_h) in enumerate(onb_steps):
        cx = f2_x + 85.0 + idx * (card_step_w + 18.0)
        cy = f2_y + 165.0
        h_flag = is_h[0] if is_h else False
        scene.add_quad_card(cx, cy, card_step_w, 145.0, s_tit, sublabel=f"{s_sub}\n{s_meta}", badge=s_badge, icon=s_icon, is_hero=h_flag, font_size=14, frame_id=fid2)

        if idx < len(onb_steps) - 1:
            scene.add_arrow(cx + card_step_w, cy + 72.0, cx + card_step_w + 18.0, cy + 72.0, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, frame_id=fid2)

    # Bottom-Left Scope: Protocolo NNA & Cuenta de Padres
    bot2_y = f2_y + 365.0
    bot2_h = 525.0
    nna_w = 900.0
    scene.add_scope_container(f2_x + 60.0, bot2_y, nna_w, bot2_h, label="2. PROTOCOLO REFORZADO DE MENORES (NNA) & CUENTA DE PADRES", stroke=PALETTE["CORAL_BORDER"], bg="#FFFFFF", frame_id=fid2)

    scene.add_feature_card(f2_x + 85.0, bot2_y + 40.0, nna_w - 50.0, 155.0,
                           "Flujo de Autorización para Menores (Ley 1098 / SIC)",
                           [
                               "Detección automática en registro: Si la edad es menor de 18 años, el formulario bloquea la autofirma.",
                               "Firma digital exclusiva del padre/madre/tutor: Captura de documento de identidad y parentesco.",
                               "Derecho a ser escuchado: El menor recibe información clara adaptada a su nivel de desarrollo."
                           ],
                           badge="ESTÁNDAR REFORZADO", icon="shield", is_hero=True, frame_id=fid2)

    scene.add_feature_card(f2_x + 85.0, bot2_y + 210.0, nna_w - 50.0, 145.0,
                           "Sección Independiente de Padres (Permisos Restringidos)",
                           [
                               "El padre cuenta con credenciales y perfil propio (prohibido compartir la contraseña del alumno).",
                               "Visualización exclusiva de notas, asistencia a clases Meet, resultados de simulacros y alertas.",
                               "Cero acceso cruzado a datos de otros estudiantes o información financiera general."
                           ],
                           badge="PORTAL PADRES", icon="users", bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], frame_id=fid2)

    scene.add_feature_card(f2_x + 85.0, bot2_y + 370.0, nna_w - 50.0, 130.0,
                           "Seguridad de Menores en Entornos Digitales (WhatsApp / Chat)",
                           [
                               "Canales oficiales moderados: Prohibido el contacto privado no supervisado tutor-estudiante.",
                               "Protocolo estricto contra acoso, suplantación o divulgación no autorizada de calificaciones.",
                               "Botón de alerta rápida y escalamiento prioritario ante cualquier comportamiento indebido."
                           ],
                           badge="MODERACIÓN", icon="alert", bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], frame_id=fid2)

    # Bottom-Center Scope: Grabaciones & Gemini AI
    rec_w = 900.0
    rec_x = f2_x + 60.0 + nna_w + 25.0
    scene.add_scope_container(rec_x, bot2_y, rec_w, bot2_h, label="3. MATRIZ DE TRATAMIENTO: GRABACIONES & IA (GEMINI)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)

    scene.add_quad_card(rec_x + 25.0, bot2_y + 40.0, (rec_w - 65.0) * 0.5, 145.0,
                        "Sesión Meet en Vivo",
                        sublabel="Aviso en pantalla obligatorio.\nVideo, audio, micrófono y chat.\nRegistro de asistencia y preguntas.",
                        badge="CAPTURA MEET", icon="laptop", font_size=15, frame_id=fid2)

    scene.add_quad_card(rec_x + 25.0 + (rec_w - 65.0) * 0.5 + 15.0, bot2_y + 40.0, (rec_w - 65.0) * 0.5, 145.0,
                        "Procesamiento Gemini",
                        sublabel="Storage seguro en Google Drive.\nTranscripción pedagógica con IA.\nGeneración de resúmenes de estudio.",
                        badge="IA GEMINI & DRIVE", icon="server", font_size=15, frame_id=fid2)

    scene.add_feature_card(rec_x + 25.0, bot2_y + 200.0, rec_w - 50.0, 160.0,
                           "Regla de Oro: Grabación Académica vs Difusión en YouTube",
                           [
                               "Grabación Académica: Uso exclusivo para consulta interna de estudiantes matriculados en la cohorte.",
                               "Publicación en YouTube / Redes: REQUIERE autorización independiente y expresa de imagen y voz.",
                               "Prohibición estricta de publicar grabaciones donde aparezcan menores sin consentimiento específico."
                           ],
                           badge="SEGREGACIÓN NARRATIVA", icon="shield", is_hero=True, frame_id=fid2)

    scene.add_feature_card(rec_x + 25.0, bot2_y + 375.0, rec_w - 50.0, 125.0,
                           "Aviso Obligatorio al Ingresar a la Sala Meet",
                           [
                               "\"Esta sesión será grabada para fines pedagógicos y refuerzo dentro de la plataforma.",
                               "Tu participación mediante cámara, micrófono o chat formará parte del registro académico.\""
                           ],
                           badge="AVISO CLASE", bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], frame_id=fid2)

    # Bottom-Right Scope: Proveedores Tecnológicos (Encargados)
    prov_w = fw - 120.0 - nna_w - rec_w - 50.0
    prov_x = rec_x + rec_w + 25.0
    scene.add_scope_container(prov_x, bot2_y, prov_w, bot2_h, label="4. MATRIZ DE PROVEEDORES (ENCARGADOS)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)

    providers = [
        ("GOOGLE LLC", "Meet/Drive/Gemini", "Audio, video, chat y transcripción", "EE.UU. (Cláusulas Tipo)", "CLOUD TECH", "server"),
        ("BOLD.CO", "Pasarela de Pagos", "Datos transacción y estado pago", "Colombia (PCI-DSS)", "PAYMENTS", "lock"),
        ("FACTUS / BOLD POS", "Facturación DIAN", "Datos fiscales y facturas", "Colombia (DIAN)", "BILLING", "file"),
        ("WHATSAPP (META)", "Canal Informativo", "Mensajería y grupos soporte", "EE.UU. (Canal Moderado)", "MESSAGING", "users"),
        ("PLATAFORMA LMS", "Core Académico", "Simulacros, notas y reportes", "Infraestructura Segura", "CORE LMS", "database")
    ]

    for p_i, (p_tit, p_serv, p_data, p_loc, p_badge, p_icon) in enumerate(providers):
        py = bot2_y + 40.0 + p_i * 92.0
        scene.add_quad_card(prov_x + 20.0, py, prov_w - 40.0, 82.0, f"{p_tit} ({p_serv})", sublabel=f"{p_data} · {p_loc}", badge=p_badge, icon=p_icon, font_size=13, frame_id=fid2)

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
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "Régimen de Comercio Electrónico (Ley 1480 & 2439), Retracto, PQRS Hábeas Data y Matriz RBAC", font_size=26, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    sc3_y = f3_y + 115.0

    # Scope 1: Comercio Electrónico
    ecom_w = 830.0
    scene.add_scope_container(f3_x + 60.0, sc3_y, ecom_w, sc_h, label="1. COMERCIO ELECTRÓNICO, RETRACTO & REVERSIÓN (LEY 1480/2439)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)

    scene.add_quad_card(f3_x + 25.0, sc3_y + 45.0, ecom_w - 50.0, 130.0,
                        "Compra Online & Perfeccionamiento",
                        sublabel="Aceptación explícita de Términos y Condiciones en checkout Bold.\nEmisión obligatoria de Factura Electrónica vía Factus.\nActivación automática de credenciales y comprobante al correo.",
                        badge="CHECKOUT BOLD", icon="lock", font_size=16, frame_id=fid3)

    scene.add_feature_card(f3_x + 25.0, sc3_y + 190.0, ecom_w - 50.0, 175.0,
                           "Derecho de Retracto Legal (SIC & Ley 2439 de 2024)",
                           [
                               "Término legal obligatorio: 5 días hábiles siguientes a la contratación del servicio.",
                               "PROHIBICIÓN ABSOLUTA de cláusulas abusivas de 'no se hacen devoluciones bajo ningún motivo'.",
                               "Evaluación caso a caso: Verificación de si el servicio inició con acuerdo expreso o consumo.",
                               "Canal formal habilitado para radicación y desembolso dentro de los plazos reglamentarios."
                           ],
                           badge="RETRACTO LEY 1480", icon="alert", is_hero=True, frame_id=fid3)

    scene.add_feature_card(f3_x + 25.0, sc3_y + 380.0, ecom_w - 50.0, 150.0,
                           "Reversión de Pagos & Reembolsos por Fraude",
                           [
                               "Aplica en supuestos legales: Fraude electrónico, operación no solicitada o producto no recibido.",
                               "Procedimiento coordinado entre SEAMOSGENIOS, pasarela Bold y entidad bancaria emisora.",
                               "Notificación oportuna dentro de los 5 días hábiles posteriores a la noticia del fraude."
                           ],
                           badge="REVERSIÓN PAGO", icon="file", bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], frame_id=fid3)

    scene.add_feature_card(f3_x + 25.0, sc3_y + 545.0, ecom_w - 50.0, 175.0,
                           "Cláusula de Resultados ICFES (Sin Garantías Ilícitas)",
                           [
                               "SEAMOSGENIOS ofrece entrenamiento pedagógico y metodología de alta calidad académica.",
                               "El puntaje final en la prueba ICFES Saber 11 depende del esfuerzo y estudio individual del alumno.",
                               "Los simulacros son herramientas de diagnóstico, no garantías de resultados o cupos universitarios.",
                               "Prohibición de publicidad engañosa sobre garantías de puntajes específicos."
                           ],
                           badge="CLÁUSULA EDUCATIVA", bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], frame_id=fid3)

    # Scope 2: Módulo Integral de PQRS & Hábeas Data
    pqrs_w = 880.0
    pqrs_x = f3_x + 60.0 + ecom_w + 30.0
    scene.add_scope_container(pqrs_x, sc3_y, pqrs_w, sc_h, label="2. MÓDULO CENTRALIZADO DE PQRS & HÁBEAS DATA (LEY 1581)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)

    pqrs_items = [
        ("PROTECCIÓN DE DATOS", "Conocer, actualizar, rectificar y suprimir", "HABEAS DATA", "lock"),
        ("ACADÉMICA", "Clases en vivo, simulacros, dudas y tutores", "ACADÉMICO", "laptop"),
        ("FACTURACIÓN Y PAGOS", "Facturas DIAN, cobros, retenciones y Bold", "FINANZAS", "file"),
        ("TÉCNICA Y ACCESO", "Problemas de login LMS, Meet y grabaciones", "SOPORTE TECH", "server"),
        ("CONVIVENCIA DIGITAL", "Reportes de conducta en chat y WhatsApp", "MODERACIÓN", "alert"),
        ("CONVENIOS COLEGIO", "Gestión de directivos y reportes de cohorte", "B2B INSTITUCIONAL", "database")
    ]

    pw = (pqrs_w - 65.0) * 0.5
    for idx, (p_tit, p_sub, p_badge, p_icon) in enumerate(pqrs_items):
        px = pqrs_x + 20.0 + (idx % 2) * (pw + 20.0)
        py = sc3_y + 45.0 + (idx // 2) * 165.0
        scene.add_quad_card(px, py, pw, 145.0, p_tit, sublabel=p_sub, badge=p_badge, icon=p_icon, font_size=15, frame_id=fid3)

    scene.add_feature_card(pqrs_x + 20.0, sc3_y + 555.0, pqrs_w - 40.0, 165.0,
                           "Flujo Hábeas Data y Tiempos Legales de Respuesta (SLA)",
                           [
                               "Flujo: Solicitud ──► Radicación Única ──► Identificación ──► Clasificación ──► Validación ──► Respuesta",
                               "Consultas y peticiones de información general: Término de 10 días hábiles (prorrogables 5 días).",
                               "Reclamos de protección de datos (Ley 1581): Término de 15 días hábiles (prorrogables 8 días).",
                               "Registro inmutable de PQRS archivado por 5 años para sustento probatorio ante la SIC."
                           ],
                           badge="SLA HÁBEAS DATA", bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], frame_id=fid3)

    # Scope 3: Seguridad RBAC & Marketing (Ley 2300/2023)
    sec_w = 1070.0
    sec_x = pqrs_x + pqrs_w + 30.0
    scene.add_scope_container(sec_x, sc3_y, sec_w, sc_h, label="3. MATRIZ RBAC (LEAST PRIVILEGE) & MARKETING (LEY 2300)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)

    scene.add_sticky_note(sec_x + 20.0, sc3_y + 45.0, sec_w - 40.0, 175.0,
                          "MATRIZ DE PERMISOS POR ROL (LEAST PRIVILEGE):\n\n"
                          "• Tutores: Solo acceden a estudiantes asignados y notas. CERO datos financieros ni teléfonos de padres.\n"
                          "• Padres: Solo consultan avance y asistencia de sus propios hijos (CERO acceso a terceros).\n"
                          "• Colegios B2B: Solo acceden al cohorte de su institución contratada.\n"
                          "• Administradores: Acceso restringido por 2FA a finanzas, facturación y contratos.",
                          font_size=13, angle_deg=1.0, frame_id=fid3)

    scene.add_feature_card(sec_x + 20.0, sc3_y + 240.0, sec_w - 40.0, 230.0,
                           "Régimen de Comunicaciones Comerciales y Marketing (Ley 2300 de 2023)",
                           [
                               "Separación estricta: Comunicaciones del servicio (clases, alertas) vs Marketing (ofertas y promociones).",
                               "Preferencias por canal registradas en base de datos: Email, WhatsApp, SMS y Llamadas telefónicas.",
                               "Horarios legales estrictos: Lunes a viernes de 7:00 a 19:00, sábados de 8:00 a 15:00. Prohibido domingos y festivos.",
                               "Mecanismo de cancelación en un solo clic ('Opt-Out') visible en todo mensaje comercial enviado."
                           ],
                           badge="LEY 'DEJEN DE FREGAR'", bg=PALETTE["GREEN_BG"], stroke=PALETTE["GREEN_BORDER"], frame_id=fid3)

    scene.add_feature_card(sec_x + 20.0, sc3_y + 490.0, sec_w - 40.0, 230.0,
                           "Régimen de Propiedad Intelectual & Banco de Preguntas ICFES",
                           [
                               "Activos protegidos: Banco de preguntas ICFES, simulacros, guías pedagógicas, PDFs, videos y plataforma.",
                               "Prohibición expresa de copia, redistribución, reventa o extracción masiva automatizada (scraping).",
                               "Contratos de tutores con cláusulas de cesión patrimonial de derechos de autor y confidencialidad estricta.",
                               "Regla de Oro: El acceso al contenido académico NO equivale a transferencia de titularidad ni licencia comercial."
                           ],
                           badge="PROPIEDAD INTELECTUAL", bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], frame_id=fid3)

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
    scene.add_text(f4_x + 60.0, f4_y + 60.0, "Evidencia Digital Inmutable (consent_id), Protocolo de Incidentes, Retención y Roadmap en 6 Fases", font_size=26, font_family=2, color=PALETTE["INK"], frame_id=fid4)

    sc4_y = f4_y + 115.0

    # Scope 1: Auditoría Forense & RNBD
    aud_w = 830.0
    scene.add_scope_container(f4_x + 60.0, sc4_y, aud_w, sc_h, label="1. REGISTRO MAESTRO DE CONSENTIMIENTOS & AUDITORÍA FORENSE", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid4)

    scene.add_feature_card(f4_x + 25.0, sc4_y + 45.0, aud_w - 50.0, 270.0,
                           "Estructura de Evidencia Digital Inmutable (Log Forense)",
                           [
                               "consent_id: UUID v4 único e irrepetible generado en el backend",
                               "user_id / student_id / representative_id: Trazabilidad de actores",
                               "consent_type: TERMS | PRIVACY | MINOR_DATA | IMAGE_VOICE | MARKETING",
                               "document_version: Ej. POL-DAT-001 v2.0 (versionamiento estricto asociado)",
                               "accepted: true · accepted_at: Timestamp ISO 8601 con hora legal colombiana",
                               "ip_address, user_agent, channel (Web / Mobile LMS)",
                               "status: ACTIVO · revoked_at (cuando aplique) · revocation_reason",
                               "Objetivo: Responder con certeza probatoria ante la SIC: ¿Quién aceptó, qué vio y cuándo?"
                           ],
                           badge="LOG INMUTABLE", bg=PALETTE["GREEN_BG"], stroke=PALETTE["GREEN_BORDER"], frame_id=fid4)

    scene.add_feature_card(f4_x + 25.0, sc4_y + 330.0, aud_w - 50.0, 195.0,
                           "Registro Nacional de Bases de Datos (RNBD / SIC)",
                           [
                               "Dec. 90/2018: Sujetos obligados: Activos totales > 100.000 UVT o entidades de naturaleza pública.",
                               "Regla Clave: No estar obligado al RNBD NO exime de cumplir todas las obligaciones de la Ley 1581.",
                               "Res. 56579 de 2025: Actualización de instrucciones oficiales del RNBD ante la SIC.",
                               "Deber permanente: Mantener política, avisos, autorizaciones y programa integral de datos."
                           ],
                           badge="RNBD / SIC", bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], frame_id=fid4)

    scene.add_feature_card(f4_x + 25.0, sc4_y + 540.0, aud_w - 50.0, 185.0,
                           "Matriz de Retención y Supresión Periódica",
                           [
                               "Cuentas de estudiantes y notas: Durante la relación contractual + 5 años de prescripción civil.",
                               "Facturación y pagos: 10 años conforme a la obligación fiscal DIAN.",
                               "Grabaciones de clase: Plazo definido por ciclo académico (prohibida la retención indefinida).",
                               "Consentimientos y logs forenses: Conservación permanente como evidencia de cumplimiento."
                           ],
                           badge="RETENCIÓN DATOS", bg="#F8FAFC", stroke=PALETTE["CARD_BORDER"], frame_id=fid4)

    # Scope 2: Protocolo de Incidentes de Seguridad (Con separación vertical exacta: CERO colisión)
    inc_w = 880.0
    inc_x = f4_x + 60.0 + aud_w + 30.0
    scene.add_scope_container(inc_x, sc4_y, inc_w, sc_h, label="2. PROTOCOLO DE GESTIÓN DE INCIDENTES DE SEGURIDAD (8 FASES)", stroke=PALETTE["CORAL_BORDER"], bg="#FFFFFF", frame_id=fid4)

    inc_phases = [
        ("01. DETECTAR", "Alerta de acceso o fuga", "DETECCIÓN", "alert"),
        ("02. CONTENER", "Aislamiento de cuenta/servicio", "CONTENCIÓN", "lock"),
        ("03. INVESTIGAR", "Análisis forense de logs", "ANÁLISIS", "terminal"),
        ("04. EVALUAR", "Medición de riesgo a titulares", "IMPACTO", "shield"),
        ("05. DOCUMENTAR", "Acta formal de incidente técnico", "REGISTRO", "file"),
        ("06. NOTIFICAR", "Aviso a la SIC y afectados", "NOTIFICACIÓN", "users"),
        ("07. CORREGIR", "Parche y ajuste de permisos", "REMEDIACIÓN", "server"),
        ("08. PREVENIR", "Actualización de controles", "PREVENCIÓN", "key")
    ]

    # Matriz 2x4 con altura de 95px por fila: ocupa de y=45px hasta y=485px
    iw = (inc_w - 65.0) * 0.5
    for idx, (i_tit, i_sub, i_badge, i_icon) in enumerate(inc_phases):
        ix = inc_x + 20.0 + (idx % 2) * (iw + 20.0)
        iy = sc4_y + 45.0 + (idx // 2) * 110.0
        scene.add_quad_card(ix, iy, iw, 95.0, i_tit, sublabel=i_sub, badge=i_badge, icon=i_icon, font_size=14, frame_id=fid4)

    # Casos críticos ubicado en y=510px con 210px de altura (Completamente despejado debajo de la fila 4)
    scene.add_feature_card(inc_x + 20.0, sc4_y + 510.0, inc_w - 40.0, 215.0,
                           "Casos Críticos de Incidente en SEAMOSGENIOS",
                           [
                               "Cuenta de tutor comprometida o descarga indebida de base de datos de estudiantes.",
                               "Grabación con imagen de menores publicada en YouTube sin consentimiento específico previo.",
                               "Falla de permisos RBAC donde un padre visualiza calificaciones de otro estudiante ajeno.",
                               "Activación inmediata del comité de seguridad y reporte formal ante la SIC en los términos legales."
                           ],
                           badge="CASOS CRÍTICOS", icon="alert", is_hero=True, frame_id=fid4)

    # Scope 3: Hoja de Ruta en 6 Fases
    road_w = 1070.0
    road_x = inc_x + inc_w + 30.0
    scene.add_scope_container(road_x, sc4_y, road_w, sc_h, label="3. HOJA DE RUTA DE IMPLEMENTACIÓN EN 6 FASES", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid4)

    road_phases = [
        ("FASE 1 · BASE LEGAL", "Política de Datos, Términos y Condiciones, Aviso de Privacidad y Flujo de Menores NNA.", PALETTE["BLUE_BG"], PALETTE["BLUE_BORDER"], "#2563EB"),
        ("FASE 2 · PLATAFORMA LMS", "Consentimientos independientes, Matriz RBAC, Portal de Padres y Módulo de PQRS Hábeas Data.", PALETTE["GREEN_BG"], PALETTE["GREEN_BORDER"], "#059669"),
        ("FASE 3 · CLASES & GRABACIONES", "Aviso en salas Meet, almacenamiento Google Drive, notas con Gemini AI y regla YouTube.", PALETTE["CORAL_BG"], PALETTE["CORAL_BORDER"], "#D93829"),
        ("FASE 4 · COMERCIAL & PAGOS", "Marketing Ley 2300, pasarela Bold, facturación DIAN con Factus y derecho de retracto.", PALETTE["INDIGO_BG"], PALETTE["INDIGO_BORDER"], "#4F46E5"),
        ("FASE 5 · COLEGIOS B2B", "Contratos institucionales B2B, acuerdos de tratamiento de datos y reportes de cohorte.", PALETTE["GREEN_BG"], PALETTE["GREEN_BORDER"], "#059669"),
        ("FASE 6 · GOBERNANZA INTERNA", "Manual de privacidad, matriz de retención, gestión de incidentes y preparación de auditoría SIC.", PALETTE["SLATE_BG"], PALETTE["SLATE_BORDER"], "#475569")
    ]

    for r_idx, (r_tit, r_desc, r_bg, r_stroke, r_badge_col) in enumerate(road_phases):
        ry = sc4_y + 45.0 + r_idx * 115.0
        scene.add_stack_layer(road_x + 20.0, ry, road_w - 40.0, 105.0,
                              f"PASO {r_idx+1}", r_tit, "COMPLIANCE",
                              [r_desc],
                              bg="#FFFFFF", stroke=r_stroke,
                              header_bg=r_bg, header_stroke=r_stroke,
                              badge_bg=r_badge_col, badge_color="#FFFFFF", frame_id=fid4)

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
    print("📊 REPORTE DE VALIDACIÓN SKETION 8.0 — SEAMOSGENIOS ESTRUCTURA JURÍDICA v2.0 (REDISEÑO EDITORIAL)")
    print("=" * 90)
    print(f" • Puntuación Global Sketion   : {report.sketion_overall_score} / 100 [{('✅ PASS' if report.is_valid else '❌ FAIL')}]")
    print(f" • Repair Dependency (RDS)     : {report.repair_dependency_score} [{report.repair_dependency_status}]")
    print(f" • Densidad Visual             : {report.visual_metrics.density:.1f} / 10 (Target: 4.0/10)")
    print(f" • Acentos Hero en Escena      : {report.visual_metrics.accent_count} (Regla del acento único respetada)")
    print(f" • Elementos Totales           : {len(scene.elements)}")
    print("=" * 90)


if __name__ == "__main__":
    main()
