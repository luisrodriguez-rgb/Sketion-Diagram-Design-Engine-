"""
Generador de Categoría 05: Negocios y Estrategia (15 Plantillas)
"""

from .common import create_base_scene, save_and_export

def generate():
    print("\n--- Generando 05: Negocios y Estrategia (15 plantillas) ---")
    cat = "05_negocios_estrategia"

    # 76. PESTEL Analysis (6 Vertical Pillars)
    s, fid, tw, th = create_base_scene("PESTEL Macroeconomic Environmental Analysis", "NEGOCIOS")
    p_cols = [("1. Politico", "Regulaciones de IA\nAranceles cloud", False),
              ("2. Economico", "Tasa de interes\nInflacion tech", False),
              ("3. Social", "Trabajo remoto\nAdopcion digital", False),
              ("4. Tecnologico", "Modelos generativos\nEdge computing", True),
              ("5. Ecologico", "Huella de carbono\nGreen Datacenters", False),
              ("6. Legal", "Cumplimiento GDPR\nPropiedad intelectual", False)]
    for i, (pc, pdesc, is_h) in enumerate(p_cols):
        px = 40 + i * 230
        s.add_rect(px, 80, 215, 350, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(px + 15, 105, pc.upper(), font_size=11, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(px + 15, 140, pdesc, font_size=10, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 76, "76_pestel_analysis", "PESTEL Analysis", "medium", "columns_6", ["macro_factors", "trends"])

    # 77. Porter's Five Forces
    s, fid, tw, th = create_base_scene("Porter's Five Forces Industry Competitiveness Model", "NEGOCIOS")
    s.add_quad_card(600, 70, 260, 90, "NUEVOS ENTRANTES", "Barreras de entrada tecnicas", badge="AMENAZA", frame_id=fid)
    s.add_quad_card(150, 200, 260, 90, "PROVEEDORES", "Poder de monopolio cloud", badge="PODER", frame_id=fid)
    s.add_quad_card(600, 200, 260, 90, "RIVALIDAD INDUSTRIA", "Competencia Directa de Motores", badge="CENTRAL", is_hero=True, frame_id=fid)
    s.add_quad_card(1050, 200, 260, 90, "COMPRADORES", "Sensibilidad al precio / SaaS", badge="PODER", frame_id=fid)
    s.add_quad_card(600, 330, 260, 90, "SUBSTITUTOS", "Herramientas no-code web", badge="AMENAZA", frame_id=fid)
    s.add_arrow(730, 160, 730, 200, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(410, 245, 600, 245, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(1050, 245, 860, 245, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(730, 330, 730, 290, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    save_and_export(s, fid, cat, 77, "77_porters_five_forces", "Porter's Five Forces", "high", "five_forces", ["central_rivalry", "forces"])

    # 78. BCG Matrix
    s, fid, tw, th = create_base_scene("BCG Growth-Share Portfolio Matrix", "NEGOCIOS")
    s.add_rect(40, 80, 660, 165, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "ESTRELLAS (ALTO CRECIMIENTO / ALTA CUOTA)", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 135, "• Sketion Pro Generator · Invertir fuertemente para liderar.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "INTERROGANTES (ALTO CRECIMIENTO / BAJA CUOTA)", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(760, 135, "• Extension VS Code · Analizar si duplicar inversion o pivotar.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(40, 265, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 290, "VACAS LECHERAS (BAJO CRECIMIENTO / ALTA CUOTA)", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(60, 320, "• Core Template Engine · Ordeñar caja para financiar Estrellas.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(740, 265, 660, 165, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 290, "PERROS (BAJO CRECIMIENTO / BAJA CUOTA)", font_size=12, font_family=3, color="#64748B", frame_id=fid)
    s.add_text(760, 320, "• Plugin Legacy v1 · Desinvertir o descontinuar.", font_size=11, font_family=3, color="#64748B", frame_id=fid)
    save_and_export(s, fid, cat, 78, "78_bcg_matrix", "BCG Matrix", "medium", "matrix_2x2", ["stars", "cash_cows", "question_marks", "dogs"])

    # 79. Ansoff Matrix
    s, fid, tw, th = create_base_scene("Ansoff Market & Product Growth Strategy Matrix", "NEGOCIOS")
    s.add_rect(40, 80, 660, 165, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "1. PENETRACION DE MERCADO (ACTUAL / ACTUAL)", font_size=12, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_text(60, 135, "• Mas volumen con la biblioteca de 212 plantillas.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 165, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "2. DESARROLLO DE PRODUCTO (NUEVO / ACTUAL)", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(760, 135, "• Exportador nativo WebAssembly y CLI interactivo.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(40, 265, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 290, "3. DESARROLLO DE MERCADO (ACTUAL / NUEVO)", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(60, 320, "• Expansion al sector academico y universidades.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(740, 265, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 290, "4. DIVERSIFICACION (NUEVO / NUEVO)", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(760, 320, "• Consultoria de arquitectura corporativa asistida por IA.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 79, "79_ansoff_matrix", "Ansoff Matrix", "medium", "matrix_2x2", ["penetration", "dev_market", "dev_product", "diversification"])

    # 80. Value Proposition Canvas
    s, fid, tw, th = create_base_scene("Value Proposition Canvas (Customer Profile vs Value Map)", "NEGOCIOS")
    s.add_rect(40, 80, 660, 350, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "MAPA DE VALOR (PRODUCTO)", font_size=13, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 145, "* Creadores de Ganancias: Diagramacion instantanea y 0 emojis.\n* Aliviadores de Dolores: Elimina alineacion manual torpe.\n* Productos & Servicios: Motor Sketion con 212 plantillas.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "PERFIL DEL CLIENTE (SEGMENTO)", font_size=13, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(760, 145, "* Ganancias Esperadas: Documentacion que impresione a directores.\n* Dolores & Frustraciones: Pérdida de 4h/semana cuadrando cajas.\n* Trabajos del Cliente: Diseñar arquitecturas y flujos de proceso.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 80, "80_value_proposition_canvas", "Value Proposition Canvas", "medium", "split_duel", ["value_map", "customer_profile"])

    # 81. Business Strategy Map (Kaplan-Norton 4 Perspectives)
    s, fid, tw, th = create_base_scene("Kaplan-Norton Balanced Scorecard Strategy Map", "NEGOCIOS")
    perspectives = [
        ("1. PERSPECTIVA FINANCIERA", "Maximizar margen operativo (+35%) y LTV de clientes", 80, "#D93829"),
        ("2. PERSPECTIVA DE CLIENTES", "Lograr NPS >= 75 y retencion neta de ingresos >= 120%", 165, "#0284C7"),
        ("3. PERSPECTIVA DE PROCESOS INTERNOS", "Automatizar 100% de la generacion de plantillas y CI", 250, "#059669"),
        ("4. PERSPECTIVA DE APRENDIZAJE & CRECIMIENTO", "Capacitar al equipo en arquitectura cloud y modelos IA", 335, "#D97706")
    ]
    for p_title, p_desc, py, p_color in perspectives:
        s.add_rect(40, py, tw - 80, 70, bg="#FFFFFF", stroke=p_color, stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(60, py + 12, p_title, font_size=11, font_family=3, color=p_color, frame_id=fid)
        s.add_text(60, py + 38, p_desc, font_size=11, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 81, "81_business_strategy_map", "Business Strategy Map", "high", "strategy_layers", ["financial", "customer", "internal", "learning"])

    # 82. Strategic Objectives Map
    s, fid, tw, th = create_base_scene("Strategic Objectives & Alignment Tree", "NEGOCIOS")
    s.add_quad_card(580, 70, 280, 80, "OBJETIVO GENERAL", "Liderar Diagramacion con IA", is_hero=True, frame_id=fid)
    s.add_arrow(720, 150, 320, 230, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(720, 150, 720, 230, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(720, 150, 1120, 230, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(200, 230, 250, 110, "Obj 1: Excelencia Visual", "VCS >= 99.0 en 212 plantillas", badge="CALIDAD", frame_id=fid)
    s.add_quad_card(600, 230, 250, 110, "Obj 2: Adopcion Global", "10,000 usuarios activos", badge="CRECIMIENTO", frame_id=fid)
    s.add_quad_card(1000, 230, 250, 110, "Obj 3: Integraciones", "Extensiones Cursor / Windsurf", badge="ECOSISTEMA", frame_id=fid)
    save_and_export(s, fid, cat, 82, "82_strategic_objectives_map", "Strategic Objectives Map", "medium", "tree", ["strategic_goals", "initiatives"])

    # 83. Strategy to Execution Map (Cascade)
    s, fid, tw, th = create_base_scene("Strategy-to-Execution Cascading Framework", "NEGOCIOS")
    s_levels = ["1. VISION CORPORATIVA", "2. OBJETIVOS ESTRATEGICOS", "3. INICIATIVAS CLAVE", "4. PROYECTOS TACTICOS", "5. METRICAS & KPIS"]
    for i, sl in enumerate(s_levels):
        sx = 40 + i * 275
        s.add_quad_card(sx, 140, 260, 150, sl, f"Nivel {i+1} de ejecucion", badge=f"NIVEL {i+1}", is_hero=(i==1), frame_id=fid)
        if i < len(s_levels) - 1:
            s.add_arrow(sx + 260, 215, sx + 275, 215, stroke="#D93829" if i==1 else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 83, "83_strategy_to_execution_map", "Strategy to Execution Map", "high", "horizontal_flow", ["cascade_levels", "connectors"])

    # 84. Product Portfolio Map
    s, fid, tw, th = create_base_scene("Product Portfolio Map (Growth vs Profitability)", "NEGOCIOS")
    s.add_rect(40, 80, 1360, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_line(100, 255, 1340, 255, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    s.add_line(720, 100, 720, 410, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    s.add_text(1180, 240, "Rentabilidad ->", font_size=11, font_family=3, color="#64748B", frame_id=fid)
    s.add_text(730, 115, "Crecimiento ^", font_size=11, font_family=3, color="#64748B", frame_id=fid)
    prods = [("Sketion Engine", 950, 160, 36, True), ("Templates v2", 820, 180, 28, True), ("Legacy CLI", 350, 340, 22, False)]
    for pname, px, py, prad, is_h in prods:
        s.add_ellipse(px - prad, py - prad, prad*2, prad*2, bg="#FFF5F2" if is_h else "#EFF6FF", stroke="#D93829" if is_h else "#3B82F6", stroke_w=1.8, frame_id=fid)
        s.add_text(px - 35, py - 6, pname, font_size=10, font_family=3, color="#D93829" if is_h else "#1D4ED8", frame_id=fid)
    save_and_export(s, fid, cat, 84, "84_product_portfolio_map", "Product Portfolio Map", "high", "portfolio_matrix", ["growth", "profitability", "bubble_size"])

    # 85. Customer Segmentation Map
    s, fid, tw, th = create_base_scene("Customer Segmentation Value & Potential Matrix", "NEGOCIOS")
    s.add_rect(40, 80, 660, 165, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "CLIENTES VIP / CHAMPIONS (ALTO VALOR / ALTO POTENCIAL)", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 135, "• Arquitectos Corporativos y Lideres Tecnicos · Retener y co-crear.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "POTENCIALES PROSPECTOS (BAJO VALOR / ALTO POTENCIAL)", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(760, 135, "• Estudiantes de ingenieria y autodidactas · Nutrir y fidelizar.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(40, 265, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 290, "TRANSACCIONALES ESTABLES (ALTO VALOR / BAJO POTENCIAL)", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(60, 320, "• Consultores puntuales · Automatizar autoservicio.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(740, 265, 660, 165, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 290, "USUARIOS CASUALES (BAJO VALOR / BAJO POTENCIAL)", font_size=12, font_family=3, color="#64748B", frame_id=fid)
    s.add_text(760, 320, "• Usuarios free esporadicos · Conversion organica.", font_size=11, font_family=3, color="#64748B", frame_id=fid)
    save_and_export(s, fid, cat, 85, "85_customer_segmentation_map", "Customer Segmentation Map", "medium", "quadrant", ["high_value", "growth_potential"])

    # 86. Business Ecosystem Map (Central Hub + Multi-Stakeholders)
    s, fid, tw, th = create_base_scene("Business Ecosystem & Multi-Stakeholder Value Network", "NEGOCIOS")
    s.add_quad_card(550, 140, 340, 150, "EMPRESA CORE (SKETION)", "Motor de Diagramacion & Plataforma", badge="CORE PLATFORM", is_hero=True, frame_id=fid)
    actors = [("Proveedores Cloud (AWS/GCP)", 40, 80), ("Partners Tecnologicos (IDEs)", 40, 260), ("Reguladores ISO/SOC2", 1060, 80), ("Clientes Enterprise", 1060, 260)]
    for aname, ax, ay in actors:
        s.add_quad_card(ax, ay, 300, 110, aname, "Relacion de valor e intercambio", badge="ECOSYSTEM", frame_id=fid)
        if ax < 500:
            s.add_arrow(ax + 300, ay + 55, 550, 215, stroke="#D93829", stroke_w=1.8, frame_id=fid)
        else:
            s.add_arrow(890, 215, ax, ay + 55, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 86, "86_business_ecosystem_map", "Business Ecosystem Map", "high", "ecosystem_network", ["partners", "company", "regulators", "tech"])

    # 87. Cost vs Benefit Matrix
    s, fid, tw, th = create_base_scene("Cost vs Benefit Strategic Decision Matrix", "NEGOCIOS")
    s.add_rect(40, 80, 660, 165, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "QUICK WINS (ALTO BENEFICIO / BAJO COSTO)", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 135, "• Exportador SVG vectorial optimizado · Prioridad Inmediata.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 165, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "PROYECTOS ESTRATEGICOS (ALTO BENEFICIO / ALTO COSTO)", font_size=12, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_text(760, 135, "• Plataforma colaborativa en tiempo real con WebSockets.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(40, 265, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 290, "TAREAS DE RELLENO (BAJO BENEFICIO / BAJO COSTO)", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(60, 320, "• Ajustes menores de documentacion interna.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(740, 265, 660, 165, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 290, "POZOS SIN FONDO (BAJO BENEFICIO / ALTO COSTO)", font_size=12, font_family=3, color="#64748B", frame_id=fid)
    s.add_text(760, 320, "• Reescritura completa del parser sin requerimiento formal.", font_size=11, font_family=3, color="#64748B", frame_id=fid)
    save_and_export(s, fid, cat, 87, "87_cost_vs_benefit_matrix", "Cost vs Benefit Matrix", "medium", "quadrant", ["high_benefit", "low_cost"])

    # 88. Scenario Planning
    s, fid, tw, th = create_base_scene("Strategic Scenario Planning & Uncertainty Matrix", "NEGOCIOS")
    s.add_rect(40, 80, 660, 165, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "ESCENARIO 1: BOOM IA + REGULACION ABIERTA", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 135, "• Crecimiento exponencial; adopcion masiva de motores locales.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "ESCENARIO 2: BOOM IA + REGULACION ESTRICTA", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(760, 135, "• Demanda de soluciones 100% on-premises y zero telemetry.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(40, 265, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 290, "ESCENARIO 3: INVIERNO IA + REGULACION ABIERTA", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(60, 320, "• Competencia por costo y eficiencia extrema de renderizado.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(740, 265, 660, 165, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 290, "ESCENARIO 4: INVIERNO IA + REGULACION ESTRICTA", font_size=12, font_family=3, color="#64748B", frame_id=fid)
    s.add_text(760, 320, "• Consolidacion en clientes corporativos consolidados.", font_size=11, font_family=3, color="#64748B", frame_id=fid)
    save_and_export(s, fid, cat, 88, "88_scenario_planning", "Scenario Planning", "high", "matrix_2x2", ["plausible_futures", "adaptations"])

    # 89. Competitive Analysis
    s, fid, tw, th = create_base_scene("Comprehensive Market Competitive Analysis", "NEGOCIOS")
    c_heads = ["PLATAFORMA", "MODO LOCAL / OFFLINE", "EXPORTACION SVG PURA", "PRECIO BASE", "SCORE GENERAL"]
    c_xs = [40, 320, 580, 840, 1100]
    for ch, cx in zip(c_heads, c_xs):
        s.add_text(cx, 85, ch, font_size=11, font_family=3, color="#64748B", frame_id=fid)
    c_rows = [
        ("Sketion Engine v10", "Si (100% Autonomo)", "Si (Inter Nativo)", "$0 (Open Source)", "99.5 / 100 (Lider)"),
        ("Miro / Lucidchart", "No (Requiere Cloud)", "Si (Con marca de agua)", "$12/usuario/mes", "82.0 / 100"),
        ("Excalidraw Web", "Parcial (Solo Browser)", "Si (Fuente manual)", "Freemium", "88.0 / 100")
    ]
    for idx, r in enumerate(c_rows):
        ry = 130 + idx * 85
        s.add_rect(30, ry, tw - 60, 70, bg="#FFF5F2" if idx==0 else "#FFFFFF", stroke="#D93829" if idx==0 else "#CBD5E1", stroke_w=1.8 if idx==0 else 1.5, roundness_type=3, frame_id=fid)
        for val, cx in zip(r, c_xs):
            s.add_text(cx, ry + 25, val, font_size=11, font_family=3, color="#D93829" if idx==0 and cx==c_xs[0] else "#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 89, "89_competitive_analysis", "Competitive Analysis", "medium", "comparison_table", ["competitors", "features"])

    # 90. Business Capability Architecture
    s, fid, tw, th = create_base_scene("Enterprise Business Capability Architecture", "NEGOCIOS")
    b_cap_tiers = [
        ("1. CAPACIDADES FRONT-OFFICE (ORIENTADAS A CLIENTE)", ["Venta Online", "Soporte Tecnico 24/7", "Portal de Desarrolladores"], 80, "#D93829"),
        ("2. CAPACIDADES CORE (CADENA DE VALOR)", ["Compilacion de Diagramas", "Exportacion Vectorial", "Motor de Inteligencia Visual"], 190, "#0284C7"),
        ("3. CAPACIDADES DE SOPORTE & GOBIERNO", ["Gestion Financiera", "Cumplimiento Legal ISO", "Infraestructura Cloud CI/CD"], 300, "#64748B")
    ]
    for c_title, c_boxes, cy, c_color in b_cap_tiers:
        s.add_rect(40, cy, tw - 80, 95, bg="#FFFFFF", stroke=c_color, stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(55, cy + 12, c_title, font_size=10, font_family=3, color=c_color, frame_id=fid)
        for bi, btxt in enumerate(c_boxes):
            s.add_rect(55 + bi * 440, cy + 35, 420, 48, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=fid)
            s.add_text(70 + bi * 440, cy + 50, btxt, font_size=11, font_family=3, color="#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 90, "90_business_architecture", "Business Architecture", "high", "capability_map", ["core_capabilities", "supporting"])
