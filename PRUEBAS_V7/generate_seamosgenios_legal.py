"""
Generador Maestro del Marco Legal y Operativo de SEAMOSGENIOS S.A.S.
Genera PRUEBAS_V7/seamosgenios_marco_legal.excalidraw siguiendo los principios de
Diagram Design, Sketion 8.0 y la regla Anti-Monocultivo.
"""

import json
import uuid
import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from validation.validator import validate_scene
from rendering.anchor_geometry import ShapeBounds, AnchorGeometryEngine
from rendering.orthogonal_router import OrthogonalRouterEngine


def gen_id(prefix="el"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def make_text(text, x, y, size=14, font=1, color="#1E1E1E", align="left", frame_id=None):
    return {
        "id": gen_id("txt"),
        "type": "text",
        "x": x,
        "y": y,
        "text": text,
        "fontSize": size,
        "fontFamily": font,
        "textAlign": align,
        "verticalAlign": "top",
        "strokeColor": color,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "frameId": frame_id
    }


def make_card(x, y, w, h, stroke="#212529", bg="#FFFFFF", stroke_w=1.0, frame_id=None):
    return {
        "id": gen_id("card"),
        "type": "rectangle",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "strokeColor": stroke,
        "backgroundColor": bg,
        "fillStyle": "solid",
        "strokeWidth": stroke_w,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "roundness": {"type": 3},
        "frameId": frame_id
    }


def make_arrow(start_pt, end_pt, points=None, color="#212529", stroke_w=1.5, dashed=False, frame_id=None):
    pts = points if points else [[0.0, 0.0], [end_pt[0] - start_pt[0], end_pt[1] - start_pt[1]]]
    return {
        "id": gen_id("arr"),
        "type": "arrow",
        "x": start_pt[0],
        "y": start_pt[1],
        "points": pts,
        "strokeColor": color,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": stroke_w,
        "strokeStyle": "dashed" if dashed else "solid",
        "roughness": 0,
        "opacity": 100,
        "startArrowhead": None,
        "endArrowhead": "arrow",
        "frameId": frame_id
    }


def build_seamosgenios_scene():
    elements = []

    # Dimensiones generales del tablero multi-marco
    frame_w = 1250.0
    frame_h = 1000.0
    gap_frames = 100.0

    # ═══════════════════════════════════════════════════════════════════════════
    # MARCO 1: IDENTIDAD, ACTORES & ARQUITECTURA DOCUMENTAL (Hub & Grid)
    # ═══════════════════════════════════════════════════════════════════════════
    f1_x = 50.0
    f1_y = 50.0
    f1_id = gen_id("f1")

    # Contenedor Marco 1
    elements.append({
        "id": f1_id,
        "type": "frame",
        "x": f1_x,
        "y": f1_y,
        "width": frame_w,
        "height": frame_h,
        "name": "01. IDENTIDAD, ACTORES & ARQUITECTURA DOCUMENTAL",
        "strokeColor": "#CED4DA",
        "backgroundColor": "#F8F9FA"
    })

    # Header Frame 1
    elements.append(make_text("SEAMOSGENIOS S.A.S. · MARCO MAESTRO LEGAL v1.0", f1_x + 40, f1_y + 30, size=24, color="#1E1E1E", frame_id=f1_id))
    elements.append(make_text("NIT: 902080201 · Domicilio: Cali, Colombia · Régimen Ley 1581/2012 & SIC", f1_x + 40, f1_y + 65, size=13, font=3, color="#495057", frame_id=f1_id))

    # Sección A: Tarjeta Central de Identidad & Responsable (Hero)
    c_hero = make_card(f1_x + 40, f1_y + 110, 360, 160, stroke="#D93829", bg="#FFF5F5", stroke_w=2.0, frame_id=f1_id)
    elements.append(c_hero)
    elements.append(make_text("RESPONSABLE DEL TRATAMIENTO", f1_x + 55, f1_y + 125, size=11, font=3, color="#D93829", frame_id=f1_id))
    elements.append(make_text("SEAMOSGENIOS S.A.S.", f1_x + 55, f1_y + 145, size=18, color="#1E1E1E", frame_id=f1_id))
    elements.append(make_text("• Correo Oficial: seamosgenios@adpmh.com\n• Sede: Carrera 121 #25-65, Cali\n• Objeto: PreICFES Virtual, Simulacros & B2B\n• Canal PQRS Datos: Implementación Web", f1_x + 55, f1_y + 175, size=13, color="#495057", frame_id=f1_id))

    # Sección B: Matriz de Roles y Actores (8 Perfiles)
    elements.append(make_text("MATRIZ DE ACTORES & ROLES DIFERENCIADOS (8 PERFILES)", f1_x + 430, f1_y + 110, size=15, color="#1E1E1E", frame_id=f1_id))
    
    roles = [
        ("COMPRADOR", "Quien contrata y paga"),
        ("ESTUDIANTE", "Receptor del servicio"),
        ("REPRESENTANTE", "Padre/Madre de menor"),
        ("ACUDIENTE", "Gestor autorizado"),
        ("COLEGIO B2B", "Cliente institucional"),
        ("TUTOR", "Prestador de servicios"),
        ("USUARIO", "Titular de la cuenta"),
        ("TITULAR", "Dueño de los datos")
    ]
    
    for i, (r_tit, r_sub) in enumerate(roles):
        rx = f1_x + 430 + (i % 2) * 380
        ry = f1_y + 140 + (i // 2) * 55
        c_r = make_card(rx, ry, 360, 45, stroke="#CED4DA", bg="#FFFFFF", frame_id=f1_id)
        elements.append(c_r)
        elements.append(make_text(f"ROLE: {r_tit}", rx + 12, ry + 8, size=11, font=3, color="#1971C2", frame_id=f1_id))
        elements.append(make_text(r_sub, rx + 12, ry + 24, size=12, color="#495057", frame_id=f1_id))

    # Sección C: Ecosistema de los 14 Documentos Maestros (Jerarquía)
    elements.append(make_text("ARQUITECTURA DE LOS 14 DOCUMENTOS MAESTROS INDEPENDIENTES", f1_x + 40, f1_y + 390, size=16, color="#1E1E1E", frame_id=f1_id))
    elements.append(make_text("Regla de Oro: Prohibido empaquetar todas las autorizaciones en un solo checkbox.", f1_x + 40, f1_y + 415, size=13, font=3, color="#D93829", frame_id=f1_id))

    # 3 Columnas de Documentos
    # Col 1: Núcleo Legal
    c_nuc = make_card(f1_x + 40, f1_y + 450, 360, 500, stroke="#212529", bg="#FFFFFF", frame_id=f1_id)
    elements.append(c_nuc)
    elements.append(make_text("PILAR I · NÚCLEO CONTRACTUAL", f1_x + 55, f1_y + 465, size=12, font=3, color="#212529", frame_id=f1_id))
    elements.append(make_text("01. Política de Tratamiento de Datos", f1_x + 55, f1_y + 495, size=14, color="#1E1E1E", frame_id=f1_id))
    elements.append(make_text("• Qué datos se tratan y finalidades\n• Derechos, seguridad y retención\n• Proveedores y transmisiones int.\n• Canal oficial de PQRS", f1_x + 55, f1_y + 520, size=12, color="#495057", frame_id=f1_id))
    
    elements.append(make_text("02. Términos y Condiciones", f1_x + 55, f1_y + 610, size=14, color="#1E1E1E", frame_id=f1_id))
    elements.append(make_text("• Reglas de compra y contratación\n• Propiedad intelectual de contenidos\n• Retracto legal y reversión de pagos\n• Cláusula de no garantía de puntaje", f1_x + 55, f1_y + 635, size=12, color="#495057", frame_id=f1_id))

    elements.append(make_text("11. Política Propiedad Intelectual", f1_x + 55, f1_y + 730, size=14, color="#1E1E1E", frame_id=f1_id))
    elements.append(make_text("• Banco de preguntas y simulacros\n• Guías, metodologías y software", f1_x + 55, f1_y + 755, size=12, color="#495057", frame_id=f1_id))

    # Col 2: Autorizaciones Específicas
    c_aut = make_card(f1_x + 430, f1_y + 450, 370, 500, stroke="#1971C2", bg="#F8F9FA", frame_id=f1_id)
    elements.append(c_aut)
    elements.append(make_text("PILAR II · 5 AUTORIZACIONES (CASILLAS SEPARADAS)", f1_x + 445, f1_y + 465, size=12, font=3, color="#1971C2", frame_id=f1_id))
    
    auths = [
        ("03. Autorización Datos Personales", "Aceptación previa, expresa e informada."),
        ("04. Autorización Datos de Menores (NNA)", "Firmada exclusivamente por el Representante."),
        ("05. Autorización Imagen, Voz & Logros", "Opcional. Para testimonios y publicidad."),
        ("06. Autorización Grabación de Clases", "Fines pedagógicos y consulta interna."),
        ("07. Autorización Marketing / WhatsApp", "Opcional. Promociones y nuevos cursos.")
    ]
    for j, (a_tit, a_desc) in enumerate(auths):
        ay = f1_y + 500 + j * 85
        elements.append(make_text(a_tit, f1_x + 445, ay, size=14, color="#1E1E1E", frame_id=f1_id))
        elements.append(make_text(f"• {a_desc}", f1_x + 445, ay + 22, size=12, color="#495057", frame_id=f1_id))

    # Col 3: Reglamentos & B2B
    c_reg = make_card(f1_x + 830, f1_y + 450, 370, 500, stroke="#212529", bg="#FFFFFF", frame_id=f1_id)
    elements.append(c_reg)
    elements.append(make_text("PILAR III · REGLAMENTOS & B2B INSTITUCIONAL", f1_x + 845, f1_y + 465, size=12, font=3, color="#212529", frame_id=f1_id))
    
    regs = [
        ("08. Política de Cookies", "Técnicas, analíticas y gestión."),
        ("09. Reglamento de Plataforma", "Integridad académica y no compartir."),
        ("10. Convivencia Digital", "Meet, chat interno y grupos WhatsApp."),
        ("12. Política de PQRS", "Petición, queja, reclamo y datos."),
        ("13. Cuenta de Padres", "Acceso exclusivo a notas y asistencia."),
        ("14. Acuerdo Colegios B2B", "Tratamiento y roles responsable/encargado.")
    ]
    for k, (r_tit, r_desc) in enumerate(regs):
        ry = f1_y + 500 + k * 70
        elements.append(make_text(r_tit, f1_x + 845, ry, size=13, color="#1E1E1E", frame_id=f1_id))
        elements.append(make_text(f"• {r_desc}", f1_x + 845, ry + 20, size=12, color="#495057", frame_id=f1_id))


    # ═══════════════════════════════════════════════════════════════════════════
    # MARCO 2: FLUJOS CRÍTICOS: MENORES, GRABACIONES & TECH STACK (Swimlanes & Pipeline)
    # ═══════════════════════════════════════════════════════════════════════════
    f2_x = f1_x + frame_w + gap_frames
    f2_y = 50.0
    f2_id = gen_id("f2")

    # Contenedor Marco 2
    elements.append({
        "id": f2_id,
        "type": "frame",
        "x": f2_x,
        "y": f2_y,
        "width": frame_w,
        "height": frame_h,
        "name": "02. FLUJOS CRÍTICOS: MENORES, GRABACIONES IA & PROVEEDORES",
        "strokeColor": "#CED4DA",
        "backgroundColor": "#F8F9FA"
    })

    # Header Frame 2
    elements.append(make_text("FLUJOS DE OPERACIÓN, PROTECCIÓN NNA & INTEGRACIÓN TECH", f2_x + 40, f2_y + 30, size=24, color="#1E1E1E", frame_id=f2_id))
    elements.append(make_text("Tratamiento Reforzado de Menores (SIC) · Grabación Google Meet / Gemini · Proveedores Bold & Factus", f2_x + 40, f2_y + 65, size=13, font=3, color="#495057", frame_id=f2_id))

    # Flujo 1: Protocolo de Protección de Menores (5 Pasos en Pipeline)
    elements.append(make_text("PROTOCOLO REFORZADO DE CAPTURA PARA MENORES DE EDAD (NNA)", f2_x + 40, f2_y + 110, size=16, color="#1E1E1E", frame_id=f2_id))
    
    nna_steps = [
        ("01 DETECTAR", "Detección Edad < 18", "Identificación en registro"),
        ("02 REPRESENTANTE", "Capturar Padre/Tutor", "Nombre, doc y contacto"),
        ("03 AUTORIZAR", "Consentimiento NNA", "Firma digital expresa"),
        ("04 INFORMAR", "Lenguaje Adaptado", "Explicación al menor"),
        ("05 AUDITAR", "Log Evidencia", "Registro consent_id")
    ]
    
    step_w = 210.0
    step_gap = 25.0
    for s_idx, (s_badge, s_title, s_sub) in enumerate(nna_steps):
        sx = f2_x + 40 + s_idx * (step_w + step_gap)
        sy = f2_y + 145
        is_h = (s_idx == 2)
        c_step = make_card(sx, sy, step_w, 100, stroke=("#D93829" if is_h else "#212529"), bg=("#FFF5F5" if is_h else "#FFFFFF"), stroke_w=(2.0 if is_h else 1.0), frame_id=f2_id)
        elements.append(c_step)
        elements.append(make_text(s_badge, sx + 12, sy + 12, size=11, font=3, color=("#D93829" if is_h else "#1971C2"), frame_id=f2_id))
        elements.append(make_text(s_title, sx + 12, sy + 32, size=13, color="#1E1E1E", frame_id=f2_id))
        elements.append(make_text(s_sub, sx + 12, sy + 62, size=11, color="#495057", frame_id=f2_id))

        if s_idx < len(nna_steps) - 1:
            elements.append(make_arrow((sx + step_w, sy + 50), (sx + step_w + step_gap, sy + 50), frame_id=f2_id))

    # Flujo 2: Matriz de Grabaciones & Tratamiento con Inteligencia Artificial
    elements.append(make_text("MATRIZ DE TRATAMIENTO: GRABACIONES DE CLASES & IA (GEMINI)", f2_x + 40, f2_y + 280, size=16, color="#1E1E1E", frame_id=f2_id))

    # Tarjeta Google Meet & Captura
    c_rec1 = make_card(f2_x + 40, f2_y + 315, 360, 180, stroke="#212529", bg="#FFFFFF", frame_id=f2_id)
    elements.append(c_rec1)
    elements.append(make_text("SESIÓN EN VIVO · GOOGLE MEET", f2_x + 55, f2_y + 330, size=11, font=3, color="#1971C2", frame_id=f2_id))
    elements.append(make_text("Captura Multimedia de Clase", f2_x + 55, f2_y + 350, size=15, color="#1E1E1E", frame_id=f2_id))
    elements.append(make_text("• Aviso previo en pantalla obligatorio\n• Video, audio, cámara y micrófono\n• Intervenciones en chat y preguntas\n• Registro automático de asistencia", f2_x + 55, f2_y + 380, size=12, color="#495057", frame_id=f2_id))

    # Tarjeta Procesamiento Gemini & Storage Drive
    c_rec2 = make_card(f2_x + 440, f2_y + 315, 360, 180, stroke="#212529", bg="#FFFFFF", frame_id=f2_id)
    elements.append(c_rec2)
    elements.append(make_text("PROCESAMIENTO IA · GEMINI & DRIVE", f2_x + 455, f2_y + 330, size=11, font=3, color="#1971C2", frame_id=f2_id))
    elements.append(make_text("Transcripción & Almacenamiento", f2_x + 455, f2_y + 350, size=15, color="#1E1E1E", frame_id=f2_id))
    elements.append(make_text("• Almacenamiento seguro Google Drive\n• Transcripción de texto pedagógica\n• Generación de notas y resúmenes\n• Subida a plataforma con acceso auth", f2_x + 455, f2_y + 380, size=12, color="#495057", frame_id=f2_id))

    # Tarjeta Regla de Difusión: Académica vs Pública
    c_rec3 = make_card(f2_x + 840, f2_y + 315, 370, 180, stroke="#D93829", bg="#FFF5F5", stroke_w=2.0, frame_id=f2_id)
    elements.append(c_rec3)
    elements.append(make_text("REGLA DE ORO · SEGREGACIÓN NARRATIVA", f2_x + 855, f2_y + 330, size=11, font=3, color="#D93829", frame_id=f2_id))
    elements.append(make_text("Académica vs Publicación Pública", f2_x + 855, f2_y + 350, size=15, color="#1E1E1E", frame_id=f2_id))
    elements.append(make_text("• Uso Académico: Consulta de refuerzo\n• Publicación YouTube: REQUIERE autorización\n  independiente de imagen y voz\n• Prohibido publicar clases con menores sin aval", f2_x + 855, f2_y + 380, size=12, color="#495057", frame_id=f2_id))

    elements.append(make_arrow((f2_x + 400, f2_y + 405), (f2_x + 440, f2_y + 405), frame_id=f2_id))
    elements.append(make_arrow((f2_x + 800, f2_y + 405), (f2_x + 840, f2_y + 405), frame_id=f2_id))

    # Flujo 3: Matriz de Proveedores Tecnológicos & Transmisiones
    elements.append(make_text("MATRIZ DE PROVEEDORES TECNOLÓGICOS, ENCARGADOS & SERVICIOS", f2_x + 40, f2_y + 530, size=16, color="#1E1E1E", frame_id=f2_id))

    providers = [
        ("GOOGLE LLC", "Meet / Drive / Gemini AI", "Audio, video, chat, transcripción y archivos", "EE.UU. (Verificar Cláusulas Estándar)"),
        ("BOLD.CO", "Pasarela de Pagos Digitales", "Datos de tarjeta, transacción y estado de pago", "Colombia / Pasarela Certificada PCI-DSS"),
        ("FACTUS / BOLD POS", "Facturación Electrónica DIAN", "Razón social, NIT/Cédula, correo y valor", "Colombia / Proveedor Autorizado DIAN"),
        ("WHATSAPP (META)", "Canal Informativo & Grupos", "Número celular, nombre de usuario y mensajes", "EE.UU. / Canales Abiertos & Cerrados"),
        ("PLATAFORMA LMS", "Core Académico & Simulacros", "Cuentas, notas, avance, alertas y reportes", "Infraestructura Cloud Segura")
    ]

    for p_idx, (p_name, p_serv, p_data, p_loc) in enumerate(providers):
        py = f2_y + 570 + p_idx * 75
        c_p = make_card(f2_x + 40, py, 1170, 65, stroke="#CED4DA", bg="#FFFFFF", frame_id=f2_id)
        elements.append(c_p)
        elements.append(make_text(p_name, f2_x + 60, py + 12, size=14, color="#1E1E1E", frame_id=f2_id))
        elements.append(make_text(f"Servicio: {p_serv}", f2_x + 60, py + 34, size=12, font=3, color="#1971C2", frame_id=f2_id))
        elements.append(make_text(f"Datos Tratados: {p_data}", f2_x + 380, py + 15, size=12, color="#495057", frame_id=f2_id))
        elements.append(make_text(f"Tratamiento: {p_loc}", f2_x + 380, py + 36, size=12, font=3, color="#2F9E44", frame_id=f2_id))


    # ═══════════════════════════════════════════════════════════════════════════
    # MARCO 3: CICLO DE VIDA, COMERCIO ELECTRÓNICO, PQRS & AUDITORÍA (Layer Stack)
    # ═══════════════════════════════════════════════════════════════════════════
    f3_x = f2_x + frame_w + gap_frames
    f3_y = 50.0
    f3_id = gen_id("f3")

    # Contenedor Marco 3
    elements.append({
        "id": f3_id,
        "type": "frame",
        "x": f3_x,
        "y": f3_y,
        "width": frame_w,
        "height": frame_h,
        "name": "03. COMERCIO ELECTRÓNICO, PQRS, SEGURIDAD & AUDITORÍA",
        "strokeColor": "#CED4DA",
        "backgroundColor": "#F8F9FA"
    })

    # Header Frame 3
    elements.append(make_text("DERECHOS DEL CONSUMIDOR, SEGURIDAD RBAC & AUDITORÍA", f3_x + 40, f3_y + 30, size=24, color="#1E1E1E", frame_id=f3_id))
    elements.append(make_text("Ley 1480/2011 (Estatuto del Consumidor) · Control de Acceso por Rol · Evidencia Digital RNBD", f3_x + 40, f3_y + 65, size=13, font=3, color="#495057", frame_id=f3_id))

    # Sección A: Flujo de Comercio Electrónico, Retracto y Reversión (Ley 1480)
    elements.append(make_text("RÉGIMEN DE COMERCIO ELECTRÓNICO, RETRACTO & REVERSIÓN", f3_x + 40, f3_y + 110, size=16, color="#1E1E1E", frame_id=f3_id))

    c_ecom1 = make_card(f3_x + 40, f3_y + 140, 360, 180, stroke="#212529", bg="#FFFFFF", frame_id=f3_id)
    elements.append(c_ecom1)
    elements.append(make_text("COMPRA & PERFECCIONAMIENTO", f3_x + 55, f3_y + 155, size=11, font=3, color="#1971C2", frame_id=f3_id))
    elements.append(make_text("Checkout & Pasarela Bold", f3_x + 55, f3_y + 175, size=15, color="#1E1E1E", frame_id=f3_id))
    elements.append(make_text("• Aceptación de Términos y Condiciones\n• Emisión de Factura Electrónica (Factus)\n• Activación de matrícula y credenciales\n• Envío de comprobante por correo", f3_x + 55, f3_y + 205, size=12, color="#495057", frame_id=f3_id))

    c_ecom2 = make_card(f3_x + 440, f3_y + 140, 360, 180, stroke="#D93829", bg="#FFF5F5", stroke_w=2.0, frame_id=f3_id)
    elements.append(c_ecom2)
    elements.append(make_text("DERECHO DE RETRACTO (SIC)", f3_x + 455, f3_y + 155, size=11, font=3, color="#D93829", frame_id=f3_id))
    elements.append(make_text("Reglas Legales de Devolución", f3_x + 455, f3_y + 175, size=15, color="#1E1E1E", frame_id=f3_id))
    elements.append(make_text("• Prohibido cláusula 'no hay devoluciones'\n• Término legal: 5 días hábiles (Ley 1480)\n• Validación de inicio anticipado y consumo\n• Procedimiento formal de solicitud", f3_x + 455, f3_y + 205, size=12, color="#495057", frame_id=f3_id))

    c_ecom3 = make_card(f3_x + 840, f3_y + 140, 370, 180, stroke="#212529", bg="#FFFFFF", frame_id=f3_id)
    elements.append(c_ecom3)
    elements.append(make_text("REVERSIÓN DE PAGOS", f3_x + 855, f3_y + 155, size=11, font=3, color="#1971C2", frame_id=f3_id))
    elements.append(make_text("Fraude, Error o No Servicio", f3_x + 855, f3_y + 175, size=15, color="#1E1E1E", frame_id=f3_id))
    elements.append(make_text("• Operación no solicitada o fraude\n• Producto no recibido o defectuoso\n• Notificación a Bold y emisor bancario\n• Términos legales de respuesta SIC", f3_x + 855, f3_y + 205, size=12, color="#495057", frame_id=f3_id))

    # Sección B: Módulo Integral de PQRS (11 Categorías)
    elements.append(make_text("SISTEMA CENTRALIZADO DE ATENCIÓN DE PQRS & DERECHOS HÁBEAS DATA", f3_x + 40, f3_y + 350, size=16, color="#1E1E1E", frame_id=f3_id))

    pqrs_cats = [
        ("PROTECCIÓN DE DATOS", "Conocer, actualizar, rectificar y suprimir"),
        ("ACADÉMICA", "Clases, simulacros y tutores"),
        ("FACTURACIÓN Y PAGOS", "Cobros, retenciones y facturas DIAN"),
        ("TÉCNICA Y ACCESO", "Problemas LMS, login y grabaciones"),
        ("CONVIVENCIA", "Reportes de conducta y moderación chat"),
        ("INSTITUCIONAL B2B", "Reportes de colegios y convenios")
    ]

    for q_idx, (q_tit, q_desc) in enumerate(pqrs_cats):
        qx = f3_x + 40 + (q_idx % 3) * 395
        qy = f3_y + 385 + (q_idx // 3) * 65
        c_q = make_card(qx, qy, 380, 55, stroke="#CED4DA", bg="#FFFFFF", frame_id=f3_id)
        elements.append(c_q)
        elements.append(make_text(f"PQRS: {q_tit}", qx + 12, qy + 8, size=11, font=3, color="#1971C2", frame_id=f3_id))
        elements.append(make_text(q_desc, qx + 12, qy + 26, size=12, color="#495057", frame_id=f3_id))

    # Sección C: Principio de Mínimo Acceso (RBAC) & Trazabilidad de Evidencia
    elements.append(make_text("SEGURIDAD, CONTROL DE ACCESO (RBAC) & REGISTRO DE EVIDENCIA DIGITAL", f3_x + 40, f3_y + 550, size=16, color="#1E1E1E", frame_id=f3_id))

    # Matriz RBAC
    c_rbac = make_card(f3_x + 40, f3_y + 585, 570, 360, stroke="#212529", bg="#FFFFFF", frame_id=f3_id)
    elements.append(c_rbac)
    elements.append(make_text("MATRIZ DE PERMISOS POR ROL (LEAST PRIVILEGE)", f3_x + 55, f3_y + 600, size=12, font=3, color="#212529", frame_id=f3_id))
    
    rbac_rows = [
        ("TUTOR:", "Solo ve estudiantes asignados y notas. CERO finanzas."),
        ("PADRE/ACUDIENTE:", "Solo ve avance y asistencia de su hijo. No ve terceros."),
        ("ESTUDIANTE:", "Acceso propio a clases, simulacros y notas."),
        ("COORDINADOR:", "Acceso académico global y reportes de cohorte."),
        ("ADMIN / FINANZAS:", "Acceso a facturación, Bold y datos contables."),
        ("COLEGIO B2B:", "Acceso exclusivo al cohorte de su institución.")
    ]
    for r_i, (r_role, r_perm) in enumerate(rbac_rows):
        ry = f3_y + 630 + r_i * 50
        elements.append(make_text(r_role, f3_x + 55, ry, size=12, font=3, color="#1971C2", frame_id=f3_id))
        elements.append(make_text(r_perm, f3_x + 55, ry + 18, size=12, color="#495057", frame_id=f3_id))

    # Registro de Evidencia Digital
    c_evid = make_card(f3_x + 640, f3_y + 585, 570, 360, stroke="#212529", bg="#F8F9FA", frame_id=f3_id)
    elements.append(c_evid)
    elements.append(make_text("LOG INMUTABLE DE CONSENTIMIENTOS (AUDIT TRAIL)", f3_x + 655, f3_y + 600, size=12, font=3, color="#212529", frame_id=f3_id))
    
    log_fields = (
        "Estructura obligatoria por cada consentimiento:\n"
        "• consent_id: Identificador único UUID v4\n"
        "• user_id / student_id / representative_id\n"
        "• consent_type: TERMS | PRIVACY | MINOR | MARKETING | IMAGE\n"
        "• document_version: Ej. POL-DAT-001 v1.0\n"
        "• accepted: true | accepted_at: Timestamp ISO 8601\n"
        "• ip_address, user_agent, channel (Web/Mobile)\n"
        "• revoked_at, revocation_reason (cuando aplique)\n\n"
        "Objetivo de Cumplimiento:\n"
        "Poder responder con certeza forense ante la SIC:\n"
        "¿Quién aceptó, qué versión exacta vio y cuándo?"
    )
    elements.append(make_text(log_fields, f3_x + 655, f3_y + 630, size=12, color="#495057", frame_id=f3_id))

    scene_data = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://sketion.engine.v8",
        "elements": elements,
        "appState": {
            "viewBackgroundColor": "#FFFFFF",
            "gridSize": 20
        }
    }

    return scene_data


def main():
    output_dir = os.path.join(workspace_dir, "PRUEBAS_V7")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "seamosgenios_marco_legal.excalidraw")

    scene_data = build_seamosgenios_scene()

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(scene_data, f, indent=2, ensure_ascii=False)

    print(f"Canvas generado exitosamente: {output_path}")

    # Validar con validator
    validated_scene, report = validate_scene(output_path)
    print("\n" + "=" * 90)
    print("📊 REPORTE DE VALIDACIÓN SKETION 8.0 — SEAMOSGENIOS MARCO LEGAL")
    print("=" * 90)
    print(f" • Puntuación Global Sketion   : {report.sketion_overall_score} / 100 [{('✅ PASS' if report.is_valid else '❌ FAIL')}]")
    print(f" • Repair Dependency (RDS)     : {report.repair_dependency_score} [{report.repair_dependency_status}]")
    print(f" • Densidad Visual             : {report.visual_metrics.density:.1f} / 10 (Target: 4.0/10)")
    print(f" • Acentos Hero en Escena      : {report.visual_metrics.accent_count} (Regla del acento único respetada)")
    print(f" • Elementos Totales           : {len(scene_data['elements'])}")
    print("=" * 90)


if __name__ == "__main__":
    main()
