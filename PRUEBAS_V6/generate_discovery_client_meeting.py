"""
Sketion 4.0 — Generador del Tablero Consultivo: Primera Reunión de Discovery Web
Paleta: Azul Cobalto Editorial (#2563EB), Blanco (#FFFFFF), Negro Tinta (#0F172A), Slate (#64748B), Acento Coral (#D93829).
Frames:
- Frame 1: Framework Consultivo de los 10 Bloques Estratégicos (Pipeline de Discovery)
- Frame 2: Live Discovery Canvas (Plantilla de Trabajo para Tomar Notas en Vivo)
- Frame 3: Embudo Comercial y Proceso de Conversión del Sitio Web
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
    # FRAME 1: FRAMEWORK CONSULTIVO DE 10 BLOQUES (PIPELINE DE DISCOVERY)
    # =========================================================================
    w1, h1 = 2800.0, 960.0
    f1_x, f1_y = place(w1, h1)
    fid1 = scene.add_frame("FRAME 1: FRAMEWORK CONSULTIVO — LOS 10 BLOQUES DE DISCOVERY WEB", f1_x, f1_y, w1, h1)

    # Header Editorial
    scene.add_text(f1_x + 60.0, f1_y + 35.0, "CONSULTING WORKSHOP  ·  DISCOVERY & BRIEFING FRAMEWORK", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "Guía Estratégica: Primera Reunión con Cliente para Creación de Sitio Web", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    # Chevron Ribbon Superior
    stages_f1 = ["1. NEGOCIO & PROPUESTA", "2. OBJETIVOS & KPIS", "3. PÚBLICO & BENCHMARK", "4. FUNNEL & CONTENIDO", "5. CIERRE & PROPUESTA"]
    scene.add_chevron_ribbon(f1_x + 60.0, f1_y + 115.0, w1 - 220.0, h=38.0, stages=stages_f1, bg=PALETTE["DARK_SLATE"], text_color="#FFFFFF", frame_id=fid1)

    # Rieles Verticales Laterales (Reglas de Consultoría)
    scene.add_vertical_rails(f1_x + w1 - 130.0, f1_y + 115.0, 70.0, 720.0, rails=[
        {"title": "80% ESCUCHAR", "bg": PALETTE["BLUE_HERO"], "text_color": "#FFFFFF"},
        {"title": "20% PREGUNTAR", "bg": PALETTE["DARK_SLATE"], "text_color": "#FFFFFF"},
        {"title": "ENFOQUE EN ROI", "bg": PALETTE["DARK_SLATE"], "text_color": "#FFFFFF"}
    ], frame_id=fid1)

    scope_y = f1_y + 175.0
    scope_h = 660.0
    sc_w = (w1 - 220.0 - 4 * 35.0) / 5.0

    # SCOPE 1: ENTENDER EL NEGOCIO (Bloques 1 y 7)
    sc1_x = f1_x + 60.0
    scene.add_scope_container(sc1_x, scope_y, sc_w, scope_h, label="1. EL NEGOCIO & OFERTA", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)
    scene.add_quad_card(sc1_x + 20.0, scope_y + 65.0, sc_w - 40.0, 125.0, "Nombre & Propuesta", sublabel="Problema que resuelve · Diferenciador", badge="BIZ", icon="laptop", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc1_x + 20.0, scope_y + 225.0, sc_w - 40.0, 125.0, "Productos & Servicios", sublabel="Oferta más rentable · Margen 80/20", badge="OFFER", icon="database", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc1_x + 20.0, scope_y + 385.0, sc_w - 40.0, 125.0, "Origen & Tono de Marca", sublabel="Historia de la idea · Valores clave", badge="STORY", icon="file", font_size=18, frame_id=fid1)

    # SCOPE 2: OBJETIVOS DE LA WEB (Bloque 2)
    sc2_x = sc1_x + sc_w + 35.0
    scene.add_scope_container(sc2_x, scope_y, sc_w, scope_h, label="2. OBJETIVOS & MÉTRICAS", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid1)
    scene.add_quad_card(sc2_x + 20.0, scope_y + 65.0, sc_w - 40.0, 125.0, "Propósito de la Web", sublabel="Leads · Venta online · Reservas · Portafolio", badge="GOAL", icon="laptop", is_hero=True, font_size=18, frame_id=fid1)
    scene.add_quad_card(sc2_x + 20.0, scope_y + 225.0, sc_w - 40.0, 125.0, "Métrica de Éxito (KPI)", sublabel="¿Cómo sabremos en 90 días que funciona?", badge="KPI", icon="monitoring", is_hero=True, font_size=18, frame_id=fid1)
    scene.add_quad_card(sc2_x + 20.0, scope_y + 385.0, sc_w - 40.0, 125.0, "Generación de Confianza", sublabel="Autoridad institucional y prueba social", badge="TRUST", icon="key", font_size=18, frame_id=fid1)

    # SCOPE 3: PÚBLICO & COMPETENCIA (Bloques 3 y 4)
    sc3_x = sc2_x + sc_w + 35.0
    scene.add_scope_container(sc3_x, scope_y, sc_w, scope_h, label="3. ICP & COMPETENCIA", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)
    scene.add_quad_card(sc3_x + 20.0, scope_y + 65.0, sc_w - 40.0, 125.0, "Cliente Ideal (ICP)", sublabel="Edad · Ubicación · B2B vs B2C", badge="USER", icon="user", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc3_x + 20.0, scope_y + 225.0, sc_w - 40.0, 125.0, "Canal de Captación Actual", sublabel="¿Cómo llegan hoy? (WhatsApp / Pauta)", badge="FLOW", icon="sync", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc3_x + 20.0, scope_y + 385.0, sc_w - 40.0, 125.0, "3-5 Sitios de Referencia", sublabel="Competidores · Qué gusta vs qué no", badge="BENCH", icon="monitoring", font_size=18, frame_id=fid1)

    # SCOPE 4: CONTENIDO & ALCANCE TÉCNICO (Bloques 5, 6 y 8)
    sc4_x = sc3_x + sc_w + 35.0
    scene.add_scope_container(sc4_x, scope_y, sc_w, scope_h, label="4. CONTENIDO & MÓDULOS", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)
    scene.add_quad_card(sc4_x + 20.0, scope_y + 65.0, sc_w - 40.0, 125.0, "Inventario de Marca", sublabel="Logo · Fotos profesionales · Videos · Copy", badge="ASSETS", icon="file", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc4_x + 20.0, scope_y + 225.0, sc_w - 40.0, 125.0, "Módulos Requeridos", sublabel="WhatsApp · Formulario · Tienda · Blog", badge="MODULES", icon="container", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc4_x + 20.0, scope_y + 385.0, sc_w - 40.0, 125.0, "Infraestructura Técnica", sublabel="Dominio · Hosting · Correo corporativo", badge="TECH", icon="server", font_size=18, frame_id=fid1)

    # SCOPE 5: PROCESO COMERCIAL & CIERRE (Bloques 7, 9 y 10)
    sc5_x = sc4_x + sc_w + 35.0
    scene.add_scope_container(sc5_x, scope_y, sc_w, scope_h, label="5. FUNNEL & PRÓXIMOS PASOS", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid1)
    scene.add_quad_card(sc5_x + 20.0, scope_y + 65.0, sc_w - 40.0, 125.0, "Proceso Post-Contacto", sublabel="¿Qué pasa tras el interés? (WhatsApp/Llamada)", badge="SALES", icon="alert", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc5_x + 20.0, scope_y + 225.0, sc_w - 40.0, 125.0, "Tiempos & Presupuesto", sublabel="Fecha límite deseada · Inversión estimada", badge="BUDGET", icon="lock", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc5_x + 20.0, scope_y + 385.0, sc_w - 40.0, 125.0, "Cierre & Propuesta Formal", sublabel="Resumen de acuerdos · Fecha de cotización", badge="NEXT", icon="key", is_hero=True, font_size=18, frame_id=fid1)

    # Conexiones de Pipeline
    scene.add_arrow(sc1_x + sc_w, scope_y + 125.0, sc2_x, scope_y + 125.0, stroke=PALETTE["INK"], stroke_w=1.5, frame_id=fid1)
    scene.add_arrow(sc2_x + sc_w, scope_y + 125.0, sc3_x, scope_y + 125.0, stroke=PALETTE["INK"], stroke_w=1.5, frame_id=fid1)
    scene.add_arrow(sc3_x + sc_w, scope_y + 125.0, sc4_x, scope_y + 125.0, stroke=PALETTE["INK"], stroke_w=1.5, frame_id=fid1)
    scene.add_arrow(sc4_x + sc_w, scope_y + 125.0, sc5_x, scope_y + 125.0, stroke=PALETTE["CORAL_HERO"], stroke_w=2.0, frame_id=fid1)

    # Leyenda Inferior
    scene.add_legend_footer(f1_x + 60.0, f1_y + 865.0, w1 - 220.0, swatches=[
        {"label": "Objetivo & KPIs (Foco)", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Cierre & Propuesta (Hero)", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Bloques de Indagación", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]}
    ], note="No hables de colores al inicio · Entiende cómo el negocio gana dinero", frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=50.0)

    # =========================================================================
    # FRAME 2: LIVE DISCOVERY CANVAS (PLANTILLA PARA TOMAR NOTAS EN VIVO)
    # =========================================================================
    w2, h2 = 2800.0, 960.0
    f2_x, f2_y = place(w2, h2)
    fid2 = scene.add_frame("FRAME 2: LIVE DISCOVERY CANVAS — PLANTILLA DE NOTAS EN REUNIÓN", f2_x, f2_y, w2, h2)

    scene.add_text(f2_x + 60.0, f2_y + 35.0, "DISCOVERY CANVAS  ·  PLANTILLA INTERACTIVA DE TOMA DE REQUERIMIENTOS", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid2)
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "Plantilla de Trabajo en Vivo: Resumen Ejecutivo · Checklist de Módulos · Acuerdos", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    # 3 Columnas de Trabajo
    canvas_col_w = (w2 - 120.0 - 2 * 45.0) / 3.0
    canvas_col_y = f2_y + 120.0
    canvas_col_h = 770.0

    # COLUMNA 1: PERFIL DEL NEGOCIO & CLIENTE
    can1_x = f2_x + 60.0
    scene.add_scope_container(can1_x, canvas_col_y, canvas_col_w, canvas_col_h, label="1. PERFIL DEL NEGOCIO & ICP", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    scene.add_quad_card(can1_x + 25.0, canvas_col_y + 55.0, canvas_col_w - 50.0, 115.0, "Nombre del Negocio & Sector", sublabel="Escribir nombre, antigüedad y propuesta de valor", badge="INFO", icon="laptop", font_size=18, frame_id=fid2)
    scene.add_quad_card(can1_x + 25.0, canvas_col_y + 195.0, canvas_col_w - 50.0, 115.0, "Objetivo Principal del Sitio", sublabel="[ ] Leads   [ ] Venta   [ ] Reservas   [ ] Marca", badge="TARGET", icon="monitoring", is_hero=True, font_size=18, frame_id=fid2)
    scene.add_quad_card(can1_x + 25.0, canvas_col_y + 335.0, canvas_col_w - 50.0, 115.0, "Cliente Ideal (ICP)", sublabel="Edad, ubicación, perfil B2B/B2C y objeciones comunes", badge="ICP", icon="users", font_size=18, frame_id=fid2)
    scene.add_quad_card(can1_x + 25.0, canvas_col_y + 475.0, canvas_col_w - 50.0, 115.0, "3-5 Sitios Web de Referencia", sublabel="1. ____________  2. ____________  3. ____________", badge="REFS", icon="file", font_size=18, frame_id=fid2)
    scene.add_quad_card(can1_x + 25.0, canvas_col_y + 615.0, canvas_col_w - 50.0, 115.0, "Oferta Estrella (80/20)", sublabel="Servicio o producto con mayor margen de ganancia", badge="MARGIN", icon="database", font_size=18, frame_id=fid2)

    # COLUMNA 2: CHECKLIST DE FUNCIONALIDADES & MATERIAL
    can2_x = can1_x + canvas_col_w + 45.0
    scene.add_scope_container(can2_x, canvas_col_y, canvas_col_w, canvas_col_h, label="2. MÓDULOS & INVENTARIO DE MARCA", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    
    # Checklist Funcional
    scene.add_bound_card(can2_x + 25.0, canvas_col_y + 55.0, canvas_col_w - 50.0, 310.0,
                         "CHECKLIST DE FUNCIONALIDADES:\n\n" +
                         "☑ Botón flotante de WhatsApp directo\n" +
                         "☑ Formulario de cotización / contacto\n" +
                         "☑ Catálogo interactivo de servicios/productos\n" +
                         "☑ Motor de reservas online en tiempo real\n" +
                         "☑ Pasarelas de pago (E-commerce local)\n" +
                         "☑ Blog corporativo y testimonios con fotos",
                         bg="#FFFFFF", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"],
                         font_size=15, roundness_type=3, frame_id=fid2)

    # Checklist Material Disponible
    scene.add_bound_card(can2_x + 25.0, canvas_col_y + 395.0, canvas_col_w - 50.0, 335.0,
                         "INVENTARIO DE MATERIAL DISPONIBLE:\n\n" +
                         "☐ Logo en alta resolución (SVG / PNG / AI)\n" +
                         "☐ Manual de marca y colores corporativos\n" +
                         "☐ Fotografías profesionales de producto/local\n" +
                         "☐ Textos y estructura de contenido redactados\n" +
                         "☐ Dominio comprado y acceso a DNS\n" +
                         "☐ Correo empresarial configurado",
                         bg=PALETTE["BLUE_BG"], stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"],
                         font_size=15, roundness_type=3, frame_id=fid2)

    # COLUMNA 3: TIEMPOS, INVERSIÓN & PRÓXIMOS PASOS
    can3_x = can2_x + canvas_col_w + 45.0
    scene.add_scope_container(can3_x, canvas_col_y, canvas_col_w, canvas_col_h, label="3. TIEMPOS, PRESUPUESTO & ACUERDOS", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid2)

    scene.add_sticky_note(can3_x + 25.0, canvas_col_y + 55.0, canvas_col_w - 50.0, 140.0,
                          "PRESUPUESTO ESTIMADO:\n$ ________________ COP / USD\n\nFECHA OBJETIVO DE LANZAMIENTO:\n___ / ___ / ______ (Evento o campaña)",
                          angle_deg=-1.0, font_size=15, frame_id=fid2)

    scene.add_quad_card(can3_x + 25.0, canvas_col_y + 225.0, canvas_col_w - 50.0, 140.0,
                        "Proceso Comercial Interno", sublabel="Al recibir un lead: ¿WhatsApp directo, llamada en <15m o correo automatizado?",
                        badge="SALES FUNNEL", icon="sync", font_size=18, frame_id=fid2)

    scene.add_quad_card(can3_x + 25.0, canvas_col_y + 395.0, canvas_col_w - 50.0, 140.0,
                        "Materiales Pendientes del Cliente", sublabel="Lista de accesos y archivos que el cliente debe entregar esta semana",
                        badge="PENDING", icon="file", font_size=18, frame_id=fid2)

    scene.add_quad_card(can3_x + 25.0, canvas_col_y + 565.0, canvas_col_w - 50.0, 165.0,
                        "Fecha de Entrega de Propuesta", sublabel="Día y hora de la reunión para presentar propuesta formal, cotización y alcance detallado",
                        badge="NEXT STEP", icon="key", is_hero=True, font_size=18, frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=50.0)

    # =========================================================================
    # FRAME 3: EMBUDO COMERCIAL DEL SITIO WEB (MÁQUINA DE VENTAS)
    # =========================================================================
    w3, h3 = 2800.0, 960.0
    f3_x, f3_y = place(w3, h3)
    fid3 = scene.add_frame("FRAME 3: EMBUDO COMERCIAL — LA WEB COMO MÁQUINA DE CAPTACIÓN", f3_x, f3_y, w3, h3)

    scene.add_text(f3_x + 60.0, f3_y + 35.0, "SALES FUNNEL ARCHITECTURE  ·  PROCESO DE CONVERSIÓN", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid3)
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "Arquitectura de Conversión: De la Visita al Cierre Comercial", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    pipeline_stages_f3 = ["1. TRÁFICO & CANALES", "2. EXPERIENCIA WEB", "3. PUNTO DE CONTACTO", "4. ATENCIÓN COMERCIAL", "5. VENTA & FIDELIZACIÓN"]
    scene.add_chevron_ribbon(f3_x + 60.0, f3_y + 115.0, w3 - 120.0, h=38.0, stages=pipeline_stages_f3, bg=PALETTE["DARK_SLATE"], text_color="#FFFFFF", frame_id=fid3)

    st3_w = (w3 - 120.0 - 4 * 40.0) / 5.0
    st3_y = f3_y + 175.0
    st3_h = 680.0

    # ETAPA 1: TRÁFICO
    x3_1 = f3_x + 60.0
    scene.add_scope_container(x3_1, st3_y, st3_w, st3_h, label="1. FUENTES DE TRÁFICO", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c3_1, _ = scene.add_quad_card(x3_1 + 20.0, st3_y + 65.0, st3_w - 40.0, 120.0, "Instagram & TikTok", sublabel="Enlace en bio · Reels orgánicos", badge="SOCIAL", icon="laptop", font_size=18, frame_id=fid3)
    c3_2, _ = scene.add_quad_card(x3_1 + 20.0, st3_y + 225.0, st3_w - 40.0, 120.0, "Google Search (SEO)", sublabel="Búsqueda local y Google Maps", badge="SEARCH", icon="server", font_size=18, frame_id=fid3)
    c3_3, _ = scene.add_quad_card(x3_1 + 20.0, st3_y + 385.0, st3_w - 40.0, 120.0, "Pauta / Meta Ads", sublabel="Campañas pagadas segmentadas", badge="ADS", icon="alert", font_size=18, frame_id=fid3)

    # ETAPA 2: LANDING PAGE
    x3_2 = x3_1 + st3_w + 40.0
    scene.add_scope_container(x3_2, st3_y, st3_w, st3_h, label="2. SITIO WEB (CONVERSIÓN)", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid3)
    c3_4, _ = scene.add_quad_card(x3_2 + 20.0, st3_y + 65.0, st3_w - 40.0, 120.0, "Hero & Propuesta Clara", sublabel="Titular magnético en 5 segundos", badge="HERO", icon="laptop", is_hero=True, font_size=18, frame_id=fid3)
    c3_5, _ = scene.add_quad_card(x3_2 + 20.0, st3_y + 225.0, st3_w - 40.0, 120.0, "Catálogo / Oferta 80/20", sublabel="Beneficios claros y diferenciales", badge="OFFER", icon="file", font_size=18, frame_id=fid3)
    c3_6, _ = scene.add_quad_card(x3_2 + 20.0, st3_y + 385.0, st3_w - 40.0, 120.0, "Prueba Social & Casos", sublabel="Testimonios y reseñas verificadas", badge="SOCIAL PROOF", icon="users", font_size=18, frame_id=fid3)

    # ETAPA 3: CONVERSIÓN
    x3_3 = x3_2 + st3_w + 40.0
    scene.add_scope_container(x3_3, st3_y, st3_w, st3_h, label="3. ACCIÓN DEL CLIENTE", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c3_7, _ = scene.add_quad_card(x3_3 + 20.0, st3_y + 65.0, st3_w - 40.0, 120.0, "Clic en WhatsApp", sublabel="Mensaje predeterminado listo", badge="WHATSAPP", icon="user", is_hero=True, font_size=18, frame_id=fid3)
    c3_8, _ = scene.add_quad_card(x3_3 + 20.0, st3_y + 225.0, st3_w - 40.0, 120.0, "Formulario / Lead", sublabel="Captura de nombre, correo y necesidad", badge="LEAD FORM", icon="file", font_size=18, frame_id=fid3)
    c3_9, _ = scene.add_quad_card(x3_3 + 20.0, st3_y + 385.0, st3_w - 40.0, 120.0, "Reserva / Pago Online", sublabel="Autoservicio 24/7 sin fricción", badge="CHECKOUT", icon="lock", font_size=18, frame_id=fid3)

    # ETAPA 4: ATENCIÓN
    x3_4 = x3_3 + st3_w + 40.0
    scene.add_scope_container(x3_4, st3_y, st3_w, st3_h, label="4. PROCESO COMERCIAL", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c3_10, _ = scene.add_quad_card(x3_4 + 20.0, st3_y + 65.0, st3_w - 40.0, 120.0, "Respuesta Inmediata", sublabel="Atención humana o bot en <5 mins", badge="RESPONSE", icon="sync", font_size=18, frame_id=fid3)
    c3_11, _ = scene.add_quad_card(x3_4 + 20.0, st3_y + 225.0, st3_w - 40.0, 120.0, "Calificación & Asesoría", sublabel="Descubrimiento de necesidades", badge="QUALIFY", icon="monitoring", font_size=18, frame_id=fid3)
    c3_12, _ = scene.add_quad_card(x3_4 + 20.0, st3_y + 385.0, st3_w - 40.0, 120.0, "Cotización / Cierre", sublabel="Envío de propuesta personalizada", badge="CLOSING", icon="key", font_size=18, frame_id=fid3)

    # ETAPA 5: FIDELIZACIÓN
    x3_5 = x3_4 + st3_w + 40.0
    scene.add_scope_container(x3_5, st3_y, st3_w, st3_h, label="5. CLIENTE & RETENCIÓN", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid3)
    c3_13, _ = scene.add_quad_card(x3_5 + 20.0, st3_y + 65.0, st3_w - 40.0, 120.0, "Entrega de Servicio", sublabel="Experiencia de compra impecable", badge="DELIVERY", icon="container", font_size=18, frame_id=fid3)
    c3_14, _ = scene.add_quad_card(x3_5 + 20.0, st3_y + 225.0, st3_w - 40.0, 120.0, "Base de Datos en CRM", sublabel="Historial de compra del cliente", badge="CRM", icon="database", font_size=18, frame_id=fid3)
    c3_15, _ = scene.add_quad_card(x3_5 + 20.0, st3_y + 385.0, st3_w - 40.0, 120.0, "Recompra & Referidos", sublabel="Clientes recurrentes y embajadores", badge="LTV", icon="users", is_hero=True, font_size=18, frame_id=fid3)

    # Conexiones Ortogonales del Funnel
    scene.add_arrow(c3_1["x"] + c3_1["width"], c3_1["y"] + c3_1["height"]*0.5, c3_4["x"], c3_4["y"] + c3_4["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid3)
    scene.add_arrow(c3_4["x"] + c3_4["width"], c3_4["y"] + c3_4["height"]*0.5, c3_7["x"], c3_7["y"] + c3_7["height"]*0.5, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, label="CTA CLICK", orthogonal=True, frame_id=fid3)
    scene.add_arrow(c3_7["x"] + c3_7["width"], c3_7["y"] + c3_7["height"]*0.5, c3_10["x"], c3_10["y"] + c3_10["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, label="LEAD ENTRANTE", orthogonal=True, frame_id=fid3)
    scene.add_arrow(c3_12["x"] + c3_12["width"], c3_12["y"] + c3_12["height"]*0.5, c3_13["x"], c3_13["y"] + c3_13["height"]*0.5, stroke=PALETTE["CORAL_HERO"], stroke_w=2.0, label="CIERRE DE VENTA", orthogonal=True, frame_id=fid3)

    # Leyenda Inferior Frame 3
    scene.add_legend_footer(f3_x + 60.0, f3_y + 865.0, w3 - 120.0, swatches=[
        {"label": "Puntos Críticos de Conversión", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Cierre Comercial & Retención", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Flujo de Conversión End-to-End", "is_arrow": True, "stroke": PALETTE["BLUE_HERO"]}
    ], note="La página web debe adaptarse al proceso comercial del cliente, no al revés", frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)

    # Guardar archivo
    out_file = os.path.join(OUT_DIR, "discovery_reunion_cliente_web.excalidraw")
    scene.save(out_file)
    print(f"\n[+] Tablero Discovery Reunión Cliente guardado exitosamente en:\n    {out_file}")

    # Validaciones
    is_valid, report = validate_scene(out_file)
    print("\n" + report.summary())

    fit_score, fit_details = calculate_archetype_fitness(
        problem_domain="CLIENT_DISCOVERY_WORKSHOP",
        chosen_structures=["PIPELINE_DISCOVERY_10_BLOCKS", "LIVE_DISCOVERY_CANVAS", "SALES_FUNNEL_ARCHITECTURE"],
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
