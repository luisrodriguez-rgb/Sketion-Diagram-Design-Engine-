"""
Sketion 4.0 — Generador del Tablero Estratégico y Comparativo EL SABIO
Paleta: Negro Tinta (#0F172A), Blanco (#FFFFFF), Slate (#64748B), Rojo/Coral (#D93829), Verde Pastel (#059669 / #DCFCE7).
Frames:
- Frame 1: El Duelo VS (Stack Fragmentado de 5 Herramientas vs. El Sabio OS)
- Frame 2: Matriz Forense de Competencia y Mercado Real en Colombia
- Frame 3: Arquitectura de Capacidades (Hub Central & Satélites Operativos)
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from validation.validator import validate_scene
from validation.fitness_score import calculate_archetype_fitness
from layout.grid import compute_matrix_layout

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V6")
os.makedirs(OUT_DIR, exist_ok=True)

PALETTE = {
    "CANVAS": "#F8FAFC",
    "CARD": "#FFFFFF",
    "CARD_BORDER": "#CBD5E1",
    "INK": "#0F172A",
    "MUTED": "#64748B",
    "RED_HERO": "#D93829",
    "RED_BG": "#FEF2F2",
    "RED_BORDER": "#FCA5A5",
    "GREEN_HERO": "#059669",
    "GREEN_BG": "#F0FDF4",
    "GREEN_BORDER": "#86EFAC",
    "DARK_SLATE": "#1E293B",
    "STICKY": "#FFE95C"
}


def build_el_sabio_comparison():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])

    # =========================================================================
    # FRAME 1: EL DUELO VS — STACK FRAGMENTADO VS. EL SABIO SISTEMA OPERATIVO
    # =========================================================================
    w1, h1 = 2800.0, 960.0
    f1_x, f1_y = place(w1, h1)
    fid1 = scene.add_frame("FRAME 1: POSICIONAMIENTO ESTRATÉGICO — EL DUELO (STACK FRAGMENTADO VS. EL SABIO)", f1_x, f1_y, w1, h1)

    scene.add_text(f1_x + 60.0, f1_y + 35.0, "EL SABIO  ·  PROPUESTA DE VALOR & ANÁLISIS DE MERCADO", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "De 5 Herramientas Inconexas al Sistema Operativo Integral del Restaurante", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    stages_f1 = ["1. STACK FRAGMENTADO", "2. FRICCIÓN & ERRORES", "3. PUENTE DIGITAL", "4. EL SABIO OS", "5. CONTROL & RETENCIÓN"]
    scene.add_chevron_ribbon(f1_x + 60.0, f1_y + 115.0, w1 - 220.0, h=38.0, stages=stages_f1, bg=PALETTE["DARK_SLATE"], text_color="#FFFFFF", frame_id=fid1)

    scene.add_vertical_rails(f1_x + w1 - 130.0, f1_y + 115.0, 70.0, 720.0, rails=[
        {"title": "100% PROPIO", "bg": PALETTE["GREEN_HERO"], "text_color": "#FFFFFF"},
        {"title": "0% COMISIÓN", "bg": PALETTE["DARK_SLATE"], "text_color": "#FFFFFF"},
        {"title": "DATA PRIVADA", "bg": PALETTE["DARK_SLATE"], "text_color": "#FFFFFF"}
    ], frame_id=fid1)

    scope_y = f1_y + 175.0
    scope_h = 660.0

    # SCOPE 1.1: REALIDAD ACTUAL (STACK FRAGMENTADO & COSTOS OCULTOS)
    sc1_w = 1100.0
    sc1_x = f1_x + 60.0
    scene.add_scope_container(sc1_x, scope_y, sc1_w, scope_h, label="1. LA REALIDAD ACTUAL: STACK FRAGMENTADO (ALTA FRICCIÓN)", stroke=PALETTE["RED_BORDER"], bg=PALETTE["RED_BG"], frame_id=fid1)

    card_w1 = 490.0
    scene.add_quad_card(sc1_x + 35.0, scope_y + 60.0, card_w1, 115.0, "WhatsApp Business", sublabel="Reservas manuales · 2-4 hrs/día · Errores", badge="CHAT", icon="alert", frame_id=fid1)
    scene.add_quad_card(sc1_x + 565.0, scope_y + 60.0, card_w1, 115.0, "Linktree / Beacons", sublabel="Puente torpe en Instagram · Cero branding", badge="LINK", icon="laptop", frame_id=fid1)
    
    scene.add_quad_card(sc1_x + 35.0, scope_y + 195.0, card_w1, 115.0, "Menú QR Genérico", sublabel="PDF estático o app ajena · $50k/mes", badge="MENU", icon="file", frame_id=fid1)
    scene.add_quad_card(sc1_x + 565.0, scope_y + 195.0, card_w1, 115.0, "Agenda en Papel / Excel", sublabel="Cero plano visual · Riesgo de overbooking", badge="PAPER", icon="file", frame_id=fid1)

    scene.add_quad_card(sc1_x + 35.0, scope_y + 330.0, 1020.0, 105.0, "Landing Tradicional Desconectada", sublabel="Página estática sin integración a reservas, mesas ni base de datos de clientes", badge="WEB", icon="laptop", frame_id=fid1)

    # Post-it de Diagnóstico Económico
    scene.add_sticky_note(sc1_x + 35.0, scope_y + 460.0, 1020.0, 95.0, "DIAGNÓSTICO: Gastan $150k+/mes en suscripciones dispersas + 80 horas/mes de personal respondiendo chats, perdiendo clientes por demoras y desorganización en sala.", angle_deg=-0.5, font_size=12, frame_id=fid1)

    # SCOPE 1.2: EL SABIO (SISTEMA OPERATIVO INTEGRAL)
    sc2_w = 1350.0
    sc2_x = sc1_x + sc1_w + 45.0
    scene.add_scope_container(sc2_x, scope_y, sc2_w, scope_h, label="2. SOLUCIÓN EL SABIO: SISTEMA OPERATIVO GASTRONÓMICO UNIFICADO", stroke=PALETTE["GREEN_BORDER"], bg=PALETTE["GREEN_BG"], frame_id=fid1)

    card_w2 = 615.0
    scene.add_quad_card(sc2_x + 35.0, scope_y + 60.0, card_w2, 115.0, "Sitio Web Corporativo & Dominio", sublabel="Identidad visual premium · Dominio propio", badge="BRAND", icon="laptop", frame_id=fid1)
    scene.add_quad_card(sc2_x + 685.0, scope_y + 60.0, card_w2, 115.0, "Plano Interactivo de Mesas", sublabel="Mapa digital fiel a la distribución real", badge="FLOOR", icon="container", is_hero=True, pills=["MAP", "SEATS"], frame_id=fid1)

    scene.add_quad_card(sc2_x + 35.0, scope_y + 195.0, card_w2, 115.0, "Motor de Reservas 24/7 en Vivo", sublabel="Autoservicio en tiempo real · 0 comisiones", badge="BOOKING", icon="sync", is_hero=True, pills=["24/7", "AUTO"], frame_id=fid1)
    scene.add_quad_card(sc2_x + 685.0, scope_y + 195.0, card_w2, 115.0, "Menú Digital Interactivo", sublabel="Actualización en vivo · Categorías y fotos", badge="MENU", icon="file", frame_id=fid1)

    scene.add_quad_card(sc2_x + 35.0, scope_y + 330.0, card_w2, 115.0, "CRM & Historial de Clientes", sublabel="Base de datos 100% propia del restaurante", badge="CRM", icon="users", frame_id=fid1)
    scene.add_quad_card(sc2_x + 685.0, scope_y + 330.0, card_w2, 115.0, "Dashboard Operativo para Host", sublabel="Métricas de ocupación, rotación y ventas", badge="METRICS", icon="monitoring", frame_id=fid1)

    scene.add_quad_card(sc2_x + 35.0, scope_y + 465.0, 1265.0, 95.0, "Marca Blanca Dedicada (White Label)", sublabel="Cero logos de terceros · Adaptado 100% al local · Propiedad total de la data y operación", badge="WHITE LABEL", icon="key", frame_id=fid1)

    # Conexión de Transformación
    scene.add_arrow(sc1_x + sc1_w, scope_y + 250.0, sc2_x, scope_y + 250.0, stroke=PALETTE["GREEN_HERO"], stroke_w=2.5, label="UNIFICACIÓN TOTAL", orthogonal=True, frame_id=fid1)

    # Leyenda Inferior
    scene.add_legend_footer(f1_x + 60.0, f1_y + 865.0, w1 - 220.0, swatches=[
        {"label": "El Sabio Core Differentiator", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]},
        {"label": "Stack Legado / Fricción Actual", "bg": PALETTE["RED_BG"], "stroke": PALETTE["RED_HERO"]},
        {"label": "Transición Unificada", "is_arrow": True, "stroke": PALETTE["GREEN_HERO"]}
    ], note="No compites por precio de landing · Compites por el control operativo del restaurante", frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=50.0)

    # =========================================================================
    # FRAME 2: MATRIZ FORENSE DE MERCADO & COMPETENCIA EN COLOMBIA
    # =========================================================================
    w2, h2 = 2800.0, 960.0
    f2_x, f2_y = place(w2, h2)
    fid2 = scene.add_frame("FRAME 2: MATRIZ FORENSE DE MERCADO — EL SABIO VS. ALTERNATIVAS REALES", f2_x, f2_y, w2, h2)

    scene.add_text(f2_x + 60.0, f2_y + 35.0, "EL SABIO  ·  MATRIZ COMPARATIVA DE CAPACIDADES OPERATIVAS", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid2)
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "Comparativa: WhatsApp/Linktree · Menú QR · Web Tradicional · SaaS Globales · El Sabio", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    headers = [
        "Capacidad / Variable",
        "WhatsApp + Linktree",
        "Menú QR (MenuApp)",
        "Web Tradicional",
        "OpenTable / TheFork",
        "EL SABIO PLATAFORMA"
    ]

    rows_data = [
        {"name": "Reservas Online", "values": ["Reservas Online 24/7", "Manual (Lento)", "No disponible", "Formulario simple", "Sí (Comisión)", "Sí (En vivo · 0 Comisiones)"]},
        {"name": "Plano de Mesas", "values": ["Plano Interactivo de Mesas", "No existe", "No existe", "No existe", "Solo planes Enterprise", "Sí (Fiel al local físico)"]},
        {"name": "Gestión de Ocupación", "values": ["Control de Aforo y Ocupación", "No (Riesgo overbooking)", "No", "No", "Sí (Rígido)", "Sí (Dinámico por zonas)"]},
        {"name": "Menú Digital", "values": ["Menú Digital Integrado", "PDF pesado", "Sí (Básico)", "PDF estático", "No disponible", "Sí (Interactivo editable)"]},
        {"name": "Dashboard Host", "values": ["Dashboard Operativo en Vivo", "No existe", "Limitado", "No existe", "Sí (Plataforma ajena)", "Sí (Dedicado para el local)"]},
        {"name": "CRM & Historial", "values": ["Base de Datos de Clientes", "Chats perdidos", "No captura", "No captura", "De la plataforma", "100% del Restaurante"]},
        {"name": "Comisiones", "values": ["Cobro por Reserva / Venta", "$0", "$0", "$0", "Comisión por comensal", "$0 Comisión siempre"]},
        {"name": "Branding", "values": ["Marca Blanca (White Label)", "Logo ajeno", "Logo de la app", "Genérico", "Logo OpenTable", "100% Marca del Restaurante"]}
    ]

    grid = compute_matrix_layout(f2_x + 60.0, f2_y + 130.0, headers, rows_data, min_col_w=240.0)

    # Cabecera de Matriz
    for c, cell in enumerate(grid["headers"]):
        is_sabio_col = (c == len(headers) - 1)
        bg_col = PALETTE["GREEN_HERO"] if is_sabio_col else PALETTE["DARK_SLATE"]
        scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], headers[c].upper(),
                             bg=bg_col, stroke=bg_col, text_color="#FFFFFF",
                             font_size=14, roundness_type=None, frame_id=fid2)

    # Celdas
    for r, row_cells in enumerate(grid["rows"]):
        vals = rows_data[r]["values"]
        for c, cell in enumerate(row_cells):
            val = str(vals[c])
            is_sabio_col = (c == len(row_cells) - 1)
            
            if is_sabio_col:
                bg = PALETTE["GREEN_BG"]
                stroke = PALETTE["GREEN_BORDER"]
                text_col = PALETTE["GREEN_HERO"]
            elif "No" in val or "Comisión" in val:
                bg = "#FFFFFF"
                stroke = PALETTE["CARD_BORDER"]
                text_col = PALETTE["MUTED"]
            else:
                bg = "#FFFFFF"
                stroke = PALETTE["CARD_BORDER"]
                text_col = PALETTE["INK"]

            scene.add_bound_card(cell["x"], cell["y"], cell["w"], cell["h"], val,
                                 bg=bg, stroke=stroke, text_color=text_col,
                                 font_size=13 if len(val) > 22 else 14, roundness_type=3 if c > 0 else None, frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=50.0)

    # =========================================================================
    # FRAME 3: ARQUITECTURA OPERATIVA DEL SISTEMA (HUB & SATÉLITES)
    # =========================================================================
    w3, h3 = 2800.0, 960.0
    f3_x, f3_y = place(w3, h3)
    fid3 = scene.add_frame("FRAME 3: ARQUITECTURA OPERATIVA — EL SABIO CORE & SATÉLITES", f3_x, f3_y, w3, h3)

    scene.add_text(f3_x + 60.0, f3_y + 35.0, "EL SABIO  ·  ARQUITECTURA DE INTEGRACIÓN Y NÚCLEO DIGITAL", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid3)
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "Ecosistema Centralizado: Hub Central Operativo y Satélites Funcionales", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    # Ribbon Superior
    pipeline_stages = ["1. CAPTACIÓN DIGITAL", "2. EXPERIENCIA COMENSAL", "3. MOTOR DE MESAS", "4. HOST & SALA", "5. CRM & ANALÍTICA"]
    scene.add_chevron_ribbon(f3_x + 60.0, f3_y + 115.0, w3 - 120.0, h=38.0, stages=pipeline_stages, bg=PALETTE["DARK_SLATE"], text_color="#FFFFFF", frame_id=fid3)

    st_w = (w3 - 120.0 - 4 * 40.0) / 5.0
    st_y = f3_y + 175.0
    st_h = 680.0

    # COLUMNA 1: CANAL PÚBLICO
    x_e1 = f3_x + 60.0
    scene.add_scope_container(x_e1, st_y, st_w, st_h, label="1. PRESENCIA & MARCA", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c_p1, _ = scene.add_quad_card(x_e1 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Web Corporativa", sublabel="Diseño premium a medida", badge="WEB", icon="laptop", frame_id=fid3)
    c_p2, _ = scene.add_quad_card(x_e1 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Dominio Propio", sublabel="tu-restaurante.com", badge="DNS", icon="server", frame_id=fid3)
    c_p3, _ = scene.add_quad_card(x_e1 + 20.0, st_y + 365.0, st_w - 40.0, 115.0, "Acceso Instagram/QR", sublabel="Enlace único directo", badge="LINK", icon="file", frame_id=fid3)

    # COLUMNA 2: COMENSAL
    x_e2 = x_e1 + st_w + 40.0
    scene.add_scope_container(x_e2, st_y, st_w, st_h, label="2. EXPERIENCIA CLIENTE", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c_c1, _ = scene.add_quad_card(x_e2 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Menú Interactivo", sublabel="Platos · Fotos · Precios", badge="MENU", icon="file", frame_id=fid3)
    c_c2, _ = scene.add_quad_card(x_e2 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Reserva Online 24/7", sublabel="Selección de fecha y hora", badge="BOOKING", icon="sync", is_hero=True, frame_id=fid3)
    c_c3, _ = scene.add_quad_card(x_e2 + 20.0, st_y + 365.0, st_w - 40.0, 115.0, "Confirmación Automática", sublabel="Notificación inmediata", badge="NOTIF", icon="key", frame_id=fid3)

    # COLUMNA 3: CORE PLANO DIGITAL
    x_e3 = x_e2 + st_w + 40.0
    scene.add_scope_container(x_e3, st_y, st_w, st_h, label="3. PLANO DIGITAL SALA", stroke=PALETTE["GREEN_BORDER"], bg=PALETTE["GREEN_BG"], frame_id=fid3)
    c_m1, _ = scene.add_quad_card(x_e3 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Mapa de Mesas Digital", sublabel="Fiel al local físico real", badge="MAP", icon="container", is_hero=True, pills=["SVG", "ZONAS"], frame_id=fid3)
    c_m2, _ = scene.add_quad_card(x_e3 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Control de Zonas", sublabel="Terraza · Salón · VIP", badge="ZONES", icon="server", frame_id=fid3)
    c_m3, _ = scene.add_quad_card(x_e3 + 20.0, st_y + 365.0, st_w - 40.0, 115.0, "Bloqueo por Horarios", sublabel="Gestión de rotación", badge="SLOTS", icon="lock", frame_id=fid3)

    # COLUMNA 4: HOST & OPERACIÓN
    x_e4 = x_e3 + st_w + 40.0
    scene.add_scope_container(x_e4, st_y, st_w, st_h, label="4. DASHBOARD OPERATIVO", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c_h1, _ = scene.add_quad_card(x_e4 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Vista Host en Sala", sublabel="Estado de mesas en vivo", badge="HOST", icon="monitoring", is_hero=True, frame_id=fid3)
    c_h2, _ = scene.add_quad_card(x_e4 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Llegadas & Check-in", sublabel="Control de comensales", badge="CHECK", icon="user", frame_id=fid3)
    c_h3, _ = scene.add_quad_card(x_e4 + 20.0, st_y + 365.0, st_w - 40.0, 115.0, "Gestión de No-Shows", sublabel="Liberación automática", badge="ALERTS", icon="alert", frame_id=fid3)

    # COLUMNA 5: DATA & NEGOCIO
    x_e5 = x_e4 + st_w + 40.0
    scene.add_scope_container(x_e5, st_y, st_w, st_h, label="5. CRM & INTELIGENCIA", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c_d1, _ = scene.add_quad_card(x_e5 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "CRM de Comensales", sublabel="Historial · Cumpleaños", badge="CRM", icon="users", frame_id=fid3)
    c_d2, _ = scene.add_quad_card(x_e5 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Analítica de Ocupación", sublabel="Días y horas de mayor venta", badge="DATA", icon="database", is_hero=True, frame_id=fid3)
    c_d3, _ = scene.add_quad_card(x_e5 + 20.0, st_y + 365.0, st_w - 40.0, 115.0, "Exportación de Datos", sublabel="100% propiedad del restaurante", badge="OWN", icon="key", frame_id=fid3)

    # Conexiones Ortogonales
    scene.add_arrow(c_p1["x"] + c_p1["width"], c_p1["y"] + c_p1["height"]*0.5, c_c2["x"], c_c2["y"] + c_c2["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid3)
    scene.add_arrow(c_c2["x"] + c_c2["width"], c_c2["y"] + c_c2["height"]*0.5, c_m1["x"], c_m1["y"] + c_m1["height"]*0.5, stroke=PALETTE["GREEN_HERO"], stroke_w=2.0, label="ASIGNACIÓN", orthogonal=True, frame_id=fid3)
    scene.add_arrow(c_m1["x"] + c_m1["width"], c_m1["y"] + c_m1["height"]*0.5, c_h1["x"], c_h1["y"] + c_h1["height"]*0.5, stroke=PALETTE["GREEN_HERO"], stroke_w=2.0, orthogonal=True, frame_id=fid3)
    scene.add_arrow(c_h1["x"] + c_h1["width"], c_h1["y"] + c_h1["height"]*0.5, c_d1["x"], c_d1["y"] + c_d1["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid3)

    # Leyenda Inferior
    scene.add_legend_footer(f3_x + 60.0, f3_y + 865.0, w3 - 120.0, swatches=[
        {"label": "Núcleo Diferencial El Sabio", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]},
        {"label": "Módulos Operativos Estándar", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]},
        {"label": "Flujo de Reserva y Asignación", "is_arrow": True, "stroke": PALETTE["GREEN_HERO"]}
    ], note="El Sabio es el sistema operativo del restaurante · Cero comisiones · 100% marca blanca", frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)

    # Guardar archivo
    out_file = os.path.join(OUT_DIR, "el_sabio_posicionamiento_estrategico.excalidraw")
    scene.save(out_file)
    print(f"\n[+] Tablero El Sabio guardado exitosamente en:\n    {out_file}")
    
    # Validaciones
    is_valid, report = validate_scene(out_file)
    print("\n" + report.summary())

    fit_score, fit_details = calculate_archetype_fitness(
        problem_domain="RESTAURANT_HOSPITALITY_OS",
        chosen_structures=["DUEL_VS_COMPARISON", "MARKET_FORENSIC_MATRIX", "HUB_SATELLITE_ARCHITECTURE"],
        covered_dimensions=["Stack Fragmentado vs OS", "Matriz Forense de Mercado", "Plano Interactivo de Mesas", "CRM y Propiedad de Datos", "Cero Comisiones"],
        has_physical_space=True,
        has_user_journey=True,
        has_supply_chain=False,
        has_restrictions_matrix=True
    )
    print(f"\nARCHETYPE FITNESS SCORE: {fit_score}/100")
    for d in fit_details:
        print(f"  {d}")

    return out_file


if __name__ == "__main__":
    build_el_sabio_comparison()
