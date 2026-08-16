"""
Sketion 4.0 — Generador del Tablero Consultivo: Primera Reunión de Discovery Web
Rediseñado con 3 Arquetipos Visuales Auténticos y Diversos:
- Frame 1: Arquetipo B (Fases Consultivas con Gates de Aprobación)
- Frame 2: Arquetipo Workshop Canvas (Miro-Style Discovery con Post-its libres, Slots de Evidencia y Matriz de Preguntas)
- Frame 3: Arquetipo F (Embudo de Conversión Escalonado con Tasas de Retención y Puntos de Fricción)
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from validation.validator import validate_scene
from validation.fitness_score import calculate_archetype_fitness

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V6")
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
    "CORAL_HERO": "#D93829",
    "CORAL_BG": "#FFF5F2",
    "CORAL_BORDER": "#FCA5A5",
    "DARK_SLATE": "#1E293B",
    "STICKY": "#FFE95C"
}


def build_discovery_client_meeting():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])

    # =========================================================================
    # FRAME 1: ARQUETIPO B (FASES CONSULTIVAS CON GATES DE APROBACIÓN)
    # =========================================================================
    w1, h1 = 2800.0, 960.0
    f1_x, f1_y = place(w1, h1)
    fid1 = scene.add_frame("FRAME 1: FRAMEWORK CONSULTIVO — FASES DE INDAGACIÓN & GATES", f1_x, f1_y, w1, h1)

    scene.add_text(f1_x + 60.0, f1_y + 35.0, "CONSULTING WORKSHOP  ·  DISCOVERY & BRIEFING FRAMEWORK", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "Guía Estratégica: Primera Reunión con Cliente para Creación de Sitio Web", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    stages_f1 = ["FASE 1: MODELO & OFERTA", "FASE 2: OBJETIVOS & KPIS", "FASE 3: ICP & COMPETENCIA", "FASE 4: MÓDULOS & TECH", "FASE 5: SCOPE & CIERRE"]
    scene.add_chevron_ribbon(f1_x + 60.0, f1_y + 115.0, w1 - 220.0, h=38.0, stages=stages_f1, bg=PALETTE["DARK_SLATE"], text_color="#FFFFFF", frame_id=fid1)

    scene.add_vertical_rails(f1_x + w1 - 130.0, f1_y + 115.0, 70.0, 720.0, rails=[
        {"title": "80% ESCUCHAR", "bg": PALETTE["BLUE_HERO"], "text_color": "#FFFFFF"},
        {"title": "20% PREGUNTAR", "bg": PALETTE["DARK_SLATE"], "text_color": "#FFFFFF"},
        {"title": "ENFOQUE EN ROI", "bg": PALETTE["DARK_SLATE"], "text_color": "#FFFFFF"}
    ], frame_id=fid1)

    scope_y = f1_y + 175.0
    scope_h = 660.0
    sc_w = (w1 - 220.0 - 4 * 35.0) / 5.0

    # 5 FASES
    phases = [
        {"num": "1. NEGOCIO & OFERTA", "t1": "Nombre & Propuesta", "s1": "Problema que resuelve · Diferenciador", "t2": "Productos 80/20", "s2": "Oferta más rentable y margen", "t3": "Historia de la Idea", "s3": "Origen y tono de marca", "hero": False},
        {"num": "2. OBJETIVOS & KPIS", "t1": "Propósito de la Web", "s1": "Leads · Venta online · Reservas", "t2": "Métrica de Éxito (KPI)", "s2": "¿Cómo medimos retorno en 90d?", "t3": "Autoridad de Marca", "s3": "Prueba social y confianza", "hero": True},
        {"num": "3. ICP & MERCADO", "t1": "Cliente Ideal (ICP)", "s1": "Edad · Ubicación · B2B vs B2C", "t2": "Canal Actual", "s2": "¿Cómo llegan hoy? (WhatsApp/Pauta)", "t3": "3-5 Referencias", "s3": "Competidores directos de la zona", "hero": False},
        {"num": "4. CONTENIDO & TECH", "t1": "Inventario de Marca", "s1": "Logo · Fotos · Videos · Textos", "t2": "Módulos Requeridos", "s2": "WhatsApp · Formulario · Tienda", "t3": "Infraestructura", "s3": "Dominio · Hosting · Correo", "hero": False},
        {"num": "5. CIERRE & PROPUESTA", "t1": "Funnel Post-Contacto", "s1": "¿Qué pasa tras el interés inicial?", "t2": "Tiempos & Inversión", "s2": "Fecha límite y presupuesto estimado", "t3": "Propuesta Formal", "s3": "Resumen y fecha de cotización", "hero": True}
    ]

    for i, ph in enumerate(phases):
        px = f1_x + 60.0 + i * (sc_w + 35.0)
        bg_col = PALETTE["BLUE_BG"] if ph["hero"] and i == 1 else (PALETTE["CORAL_BG"] if i == 4 else "#FFFFFF")
        stroke_col = PALETTE["BLUE_BORDER"] if ph["hero"] and i == 1 else (PALETTE["CORAL_BORDER"] if i == 4 else PALETTE["CARD_BORDER"])
        scene.add_scope_container(px, scope_y, sc_w, scope_h, label=ph["num"], stroke=stroke_col, bg=bg_col, frame_id=fid1)
        scene.add_quad_card(px + 20.0, scope_y + 65.0, sc_w - 40.0, 125.0, ph["t1"], sublabel=ph["s1"], badge="DISCOVERY", icon="laptop", is_hero=ph["hero"] and i == 1, font_size=18, frame_id=fid1)
        scene.add_quad_card(px + 20.0, scope_y + 225.0, sc_w - 40.0, 125.0, ph["t2"], sublabel=ph["s2"], badge="METRICS" if i == 1 else "MODULES", icon="database" if i == 0 else "monitoring", font_size=18, frame_id=fid1)
        scene.add_quad_card(px + 20.0, scope_y + 385.0, sc_w - 40.0, 125.0, ph["t3"], sublabel=ph["s3"], badge="NEXT" if i == 4 else "TECH", icon="key" if i == 4 else "file", is_hero=ph["hero"] and i == 4, font_size=18, frame_id=fid1)
        if i < 4:
            scene.add_arrow(px + sc_w, scope_y + 125.0, px + sc_w + 35.0, scope_y + 125.0, stroke=PALETTE["BLUE_HERO"] if i == 0 else PALETTE["INK"], stroke_w=2.0, frame_id=fid1)

    scene.add_legend_footer(f1_x + 60.0, f1_y + 865.0, w1 - 220.0, swatches=[
        {"label": "Objetivo & KPIs (Foco)", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Cierre & Propuesta (Hero)", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Flujo de Fases Consultivas", "is_arrow": True, "stroke": PALETTE["BLUE_HERO"]}
    ], note="No hables de colores al inicio · Entiende cómo el negocio gana dinero", frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=50.0)

    # =========================================================================
    # FRAME 2: ARQUETIPO WORKSHOP CANVAS (ESTILO MIRO / NOTAS INTERACTIVAS)
    # =========================================================================
    w2, h2 = 2800.0, 960.0
    f2_x, f2_y = place(w2, h2)
    fid2 = scene.add_frame("FRAME 2: DISCOVERY WORKSHOP — TABLERO DE TRABAJO & NOTAS EN VIVO", f2_x, f2_y, w2, h2)

    scene.add_text(f2_x + 60.0, f2_y + 35.0, "DISCOVERY CANVAS  ·  LIVE CLIENT WORKSHOP", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid2)
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "Tablero de Trabajo en Vivo: Post-its de Diagnóstico, Checklists & Acuerdos", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    # ZONA 1: POST-ITS DE DIAGNÓSTICO DEL NEGOCIO (Izquierda)
    z1_x, z1_y = f2_x + 60.0, f2_y + 120.0
    z1_w = 850.0
    scene.add_scope_container(z1_x, z1_y, z1_w, 770.0, label="1. RADIOGRAFÍA DEL NEGOCIO (POST-ITS EN VIVO)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)

    scene.add_sticky_note(z1_x + 35.0, z1_y + 60.0, 360.0, 160.0,
                          "NOMBRE & SECTOR:\n\n• Nombre del negocio:\n• ¿A qué se dedican exactamente?\n• Antigüedad en el mercado:",
                          angle_deg=-1.5, font_size=15, frame_id=fid2)

    scene.add_sticky_note(z1_x + 440.0, z1_y + 60.0, 360.0, 160.0,
                          "PROPUESTA DE VALOR:\n\n• ¿Por qué les compran a ellos?\n• ¿Qué hacen mejor que los demás?\n• Diferenciador clave:",
                          angle_deg=1.2, font_size=15, frame_id=fid2)

    scene.add_sticky_note(z1_x + 35.0, z1_y + 250.0, 360.0, 160.0,
                          "CLIENTE IDEAL (ICP):\n\n• ¿Quién es el comprador?\n• Edad / Ubicación:\n• ¿B2B (Empresas) o B2C (Personas)?",
                          angle_deg=1.0, font_size=15, frame_id=fid2)

    scene.add_sticky_note(z1_x + 440.0, z1_y + 250.0, 360.0, 160.0,
                          "OFERTA 80/20 (MÁS RENTABLE):\n\n• ¿Cuál es el producto/servicio estrella?\n• ¿Cuál deja mayor margen de ganancia?",
                          angle_deg=-1.0, font_size=15, frame_id=fid2)

    scene.add_capture_slot(z1_x + 35.0, z1_y + 440.0, 770.0, 260.0, label="3 a 5 Sitios Web de Referencia (Pegar enlaces y capturas de lo que les gusta vs no gusta)", bg="#F8FAFC", stroke=PALETTE["BLUE_HERO"], frame_id=fid2)

    # ZONA 2: MATRIZ DE REQUERIMIENTOS & CHECKLIST (Centro)
    z2_x = z1_x + z1_w + 45.0
    z2_w = 900.0
    scene.add_scope_container(z2_x, z1_y, z2_w, 770.0, label="2. CHECKLISTS DE ALCANCE FUNCIONAL & MATERIAL", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid2)

    scene.add_bound_card(z2_x + 30.0, z1_y + 60.0, z2_w - 60.0, 310.0,
                         "CHECKLIST DE FUNCIONALIDADES NECESARIAS:\n\n" +
                         "☑ Botón flotante de WhatsApp directo (con mensaje preconfigurado)\n" +
                         "☑ Formulario de cotización / captura de leads\n" +
                         "☑ Catálogo interactivo de servicios o productos\n" +
                         "☑ Motor de reservas online en tiempo real (Google Calendar)\n" +
                         "☑ Pasarelas de pago (E-commerce local: Wompi / Bold / MercadoPago)\n" +
                         "☑ Blog corporativo y testimonios con fotos reales",
                         bg="#FFFFFF", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                         font_size=15, roundness_type=3, frame_id=fid2)

    scene.add_bound_card(z2_x + 30.0, z1_y + 400.0, z2_w - 60.0, 310.0,
                         "INVENTARIO DE MATERIAL DISPONIBLE (CLIENTE):\n\n" +
                         "☐ Logo en alta resolución (SVG / PNG transparente / AI)\n" +
                         "☐ Manual de marca y colores corporativos oficiales\n" +
                         "☐ Fotografías profesionales de productos / local físico\n" +
                         "☐ Textos de ventas redactados (o requiere redacción)\n" +
                         "☐ Dominio comprado y accesos a DNS\n" +
                         "☐ Correo empresarial corporativo activo",
                         bg="#FFFFFF", stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=15, roundness_type=3, frame_id=fid2)

    # ZONA 3: CIERRE, INVERSIÓN & ACUERDOS (Derecha)
    z3_x = z2_x + z2_w + 45.0
    z3_w = w2 - z3_x - 60.0
    scene.add_scope_container(z3_x, z1_y, z3_w, 770.0, label="3. TIEMPOS, PRESUPUESTO & CIERRE", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid2)

    scene.add_sticky_note(z3_x + 30.0, z1_y + 60.0, z3_w - 60.0, 160.0,
                          "PRESUPUESTO ESTIMADO:\n$ ________________ COP / USD\n\nFECHA DESEADA DE LANZAMIENTO:\n___ / ___ / ______ (Campaña / Evento)",
                          angle_deg=-1.5, font_size=16, frame_id=fid2)

    scene.add_quad_card(z3_x + 30.0, z1_y + 250.0, z3_w - 60.0, 140.0,
                        "Proceso Comercial Interno", sublabel="Al recibir un interesado: ¿Respuesta por WhatsApp, llamada en <15 min o correo?", badge="FUNNEL", icon="sync", font_size=18, frame_id=fid2)

    scene.add_quad_card(z3_x + 30.0, z1_y + 420.0, z3_w - 60.0, 140.0,
                        "Materiales que Enviará el Cliente", sublabel="Lista de accesos y archivos pendientes para esta semana", badge="PENDING", icon="file", font_size=18, frame_id=fid2)

    scene.add_quad_card(z3_x + 30.0, z1_y + 590.0, z3_w - 60.0, 140.0,
                        "Fecha de Entrega de Propuesta", sublabel="Día y hora de la reunión para presentar propuesta formal y cotización", badge="NEXT MEETING", icon="key", is_hero=True, font_size=18, frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=50.0)

    # =========================================================================
    # FRAME 3: ARQUETIPO F (EMBUDO DE CONVERSIÓN COMERCIAL ESCALONADO)
    # =========================================================================
    w3, h3 = 2800.0, 960.0
    f3_x, f3_y = place(w3, h3)
    fid3 = scene.add_frame("FRAME 3: ARQUETIPO F — EMBUDO DE CONVERSIÓN COMERCIAL DEL SITIO WEB", f3_x, f3_y, w3, h3)

    scene.add_text(f3_x + 60.0, f3_y + 35.0, "SALES FUNNEL ARCHITECTURE  ·  CONVERSION & CLOSING ENGINE", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid3)
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "Arquitectura del Embudo: De la Visita al Cierre Comercial y Recompra", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    # 4 CAPAS DEL EMBUDO ESCALONADO (DE ANCHO A ESTRECHO)
    funnel_levels = [
        {"lvl": "1. CAPTACIÓN DE TRÁFICO (100%)", "w": 2400.0, "t": "Redes Sociales (Instagram/TikTok) · Google Search (SEO) · Meta Ads Segmentados", "icon": "laptop", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"], "hero": False},
        {"lvl": "2. LANDING PAGE & PROPUESTA CLARA (40%)", "w": 1900.0, "t": "Hero con Titular de 5 Segundos · Oferta Estrella 80/20 · Prueba Social y Testimonios", "icon": "file", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"], "hero": False},
        {"lvl": "3. PUNTO DE CONTACTO & LEAD (15%)", "w": 1400.0, "t": "Clic en Botón Flotante de WhatsApp · Formulario Cualificado · Motor de Reservas 24/7", "icon": "user", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_BORDER"], "hero": True},
        {"lvl": "4. ATENCIÓN & CIERRE COMERCIAL (5%)", "w": 950.0, "t": "Respuesta en <5 mins · Asesoría Personalizada · Cotización y Venta", "icon": "key", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"], "hero": False}
    ]

    curr_y = f3_y + 130.0
    for fn in funnel_levels:
        fn_x = f3_x + 60.0 + (w3 - 120.0 - fn["w"]) * 0.5
        scene.add_quad_card(fn_x, curr_y, fn["w"], 125.0, fn["lvl"], sublabel=fn["t"], badge="FUNNEL STAGE", icon=fn["icon"], is_hero=fn["hero"], font_size=18, frame_id=fid3)
        if fn != funnel_levels[-1]:
            scene.add_arrow(f3_x + w3 * 0.5, curr_y + 125.0, f3_x + w3 * 0.5, curr_y + 175.0, stroke=PALETTE["BLUE_HERO"], stroke_w=2.5, label="CONVERSIÓN", frame_id=fid3)
        curr_y += 175.0

    # Retención / CRM al pie
    crm_w = 950.0
    crm_x = f3_x + 60.0 + (w3 - 120.0 - crm_w) * 0.5
    scene.add_quad_card(crm_x, curr_y + 10.0, crm_w, 105.0, "5. CRM & RECOMPRA DE CLIENTES", sublabel="Base de datos 100% propia del negocio · Recompra · Referidos", badge="LTV & RETENTION", icon="database", is_hero=True, font_size=18, frame_id=fid3)
    scene.add_arrow(f3_x + w3 * 0.5, curr_y - 50.0 + 125.0, f3_x + w3 * 0.5, curr_y + 10.0, stroke=PALETTE["CORAL_HERO"], stroke_w=2.5, label="CLIENTE CERRADO", frame_id=fid3)

    scene.add_legend_footer(f3_x + 60.0, f3_y + 885.0, w3 - 120.0, swatches=[
        {"label": "Puntos Críticos de Conversión", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Cierre de Venta y Retención", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Flujo de Embudo de Ventas", "is_arrow": True, "stroke": PALETTE["BLUE_HERO"]}
    ], note="La página web debe adaptarse al proceso comercial del negocio, no al revés", frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)

    # Guardar archivo
    out_file = os.path.join(OUT_DIR, "discovery_reunion_cliente_web.excalidraw")
    scene.save(out_file)
    print(f"\n[+] Tablero Discovery Reunión Cliente (Arquetipos Diversificados) guardado exitosamente en:\n    {out_file}")

    # Validaciones
    is_valid, report = validate_scene(out_file)
    print("\n" + report.summary())

    fit_score, fit_details = calculate_archetype_fitness(
        problem_domain="CLIENT_DISCOVERY_WORKSHOP",
        chosen_structures=["CONSULTING_PHASES_GATES", "LIVE_WORKSHOP_STICKY_CANVAS", "STEPPED_CONVERSION_FUNNEL"],
        covered_dimensions=["Entender el Negocio", "Objetivos & KPIs", "Público Objetivo ICP", "Competencia & Referencias", "Contenido & Módulos", "Funnel Comercial", "Cierre & Propuesta"],
        has_physical_space=False,
        has_user_journey=True,
        has_supply_chain=False,
        has_restrictions_matrix=True
    )
    print(f"\nARCHETYPE FITNESS SCORE: {fit_score}/100")
    for d in fit_details:
        print(f"  {d}")

    return out_file


if __name__ == "__main__":
    build_discovery_client_meeting()
