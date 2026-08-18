"""
Generador de Categoría 06: Producto y Product Management (15 Plantillas)
"""

from .common import create_base_scene, save_and_export

def generate():
    print("\n--- Generando 06: Producto y Product Management (15 plantillas) ---")
    cat = "06_producto_pm"

    # 91. Product Discovery Canvas
    s, fid, tw, th = create_base_scene("Product Discovery & Problem Validation Canvas", "PRODUCTO")
    d_panels = [
        ("1. PROBLEMA DEL USUARIO", "Los equipos pierden 4h/semana cuadrando diagramas a mano.", 40, 80, 440, 160, True),
        ("2. USUARIO OBJETIVO", "Arquitectos de software, tech leads y profesores de ingenieria.", 500, 80, 440, 160, False),
        ("3. PROPUESTA DE VALOR", "Generacion instantanea de 212 plantillas vectoriales listas para produccion.", 960, 80, 440, 160, False),
        ("4. HIPOTESIS CLAVE", "Los usuarios prefieren diagramas limpios con 0 emojis sobre bibliotecas genericas.", 40, 260, 660, 160, False),
        ("5. EXPERIMENTO DE VALIDACION", "Lanzar repositorio open source y medir tasa de conversion a descargas SVG.", 720, 260, 680, 160, False)
    ]
    for dt, dd, dx, dy, dw, dh, is_h in d_panels:
        s.add_rect(dx, dy, dw, dh, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(dx + 20, dy + 20, dt, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(dx + 20, dy + 60, dd, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 91, "91_product_discovery_canvas", "Product Discovery Canvas", "medium", "discovery_canvas", ["user_problem", "assumptions", "experiments"])

    # 92. PRD Canvas (1-Pager)
    s, fid, tw, th = create_base_scene("Product Requirements Document (PRD) 1-Pager Canvas", "PRODUCTO")
    prd_sections = [
        ("1. OBJETIVO DEL PRODUCTO", "Proveer un motor de diagramacion con 212 plantillas vectoriales.", 80, "#D93829"),
        ("2. REQUERIMIENTOS FUNCIONALES", "Exportacion a SVG, Excalidraw, cero dependencias y modo offline.", 165, "#0284C7"),
        ("3. REQUERIMIENTOS NO FUNCIONALES", "Tiempo de renderizado < 100ms, VCS >= 99.0, compatibilidad web.", 250, "#059669"),
        ("4. FUERA DE ALCANCE (OUT OF SCOPE)", "Edicion de video, diagramas rasterizados o almacenamiento en nube.", 335, "#64748B")
    ]
    for p_title, p_desc, py, p_col in prd_sections:
        s.add_rect(40, py, tw - 80, 70, bg="#FFFFFF", stroke=p_col, stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(60, py + 12, p_title, font_size=11, font_family=3, color=p_col, frame_id=fid)
        s.add_text(60, py + 38, p_desc, font_size=11, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 92, "92_prd_canvas", "PRD Canvas", "medium", "prd_layers", ["overview", "requirements", "out_of_scope"])

    # 93. Product Backlog Tree
    s, fid, tw, th = create_base_scene("Hierarchical Product Backlog & Theme Tree", "PRODUCTO")
    s.add_quad_card(580, 70, 280, 80, "TEMA: MOTOR SKETION", "Version 10.0 GA", is_hero=True, frame_id=fid)
    s.add_arrow(720, 150, 320, 230, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(720, 150, 720, 230, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(720, 150, 1120, 230, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(200, 230, 250, 110, "Epica 1: Render SVG", "100% Inter nativo", badge="EPIC 1", frame_id=fid)
    s.add_quad_card(600, 230, 250, 110, "Epica 2: 212 Templates", "62 Core + 150 v2", badge="EPIC 2", frame_id=fid)
    s.add_quad_card(1000, 230, 250, 110, "Epica 3: CI/CD Suite", "27 tests automatizados", badge="EPIC 3", frame_id=fid)
    save_and_export(s, fid, cat, 93, "93_product_backlog", "Product Backlog", "medium", "backlog_tree", ["epics", "user_stories", "tasks"])

    # 94. User Story Map
    s, fid, tw, th = create_base_scene("User Story Mapping by Customer Backbone & Releases", "PRODUCTO")
    s.add_rect(40, 80, tw - 80, 70, bg="#F1F5F9", stroke="#CBD5E1", stroke_w=1.2, roundness_type=3, frame_id=fid)
    s.add_text(55, 105, "BACKBONE: 1. Descubrir Plantilla -> 2. Personalizar -> 3. Exportar SVG -> 4. Integrar en Doc", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_rect(40, 170, tw - 80, 110, bg="#FFF5F2", stroke="#D93829", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(55, 185, "RELEASE 1 (MVP CORE): 62 plantillas fundamentales + renderizado determinista", font_size=11, font_family=3, color="#D93829", frame_id=fid)
    s.add_rect(40, 300, tw - 80, 110, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.2, roundness_type=3, frame_id=fid)
    s.add_text(55, 315, "RELEASE 2 (EXPANSION V2): 150 plantillas especializadas + manifest con metricas de complejidad", font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 94, "94_user_story_map", "User Story Map", "high", "story_map", ["backbone_activities", "releases"])

    # 95. Feature Prioritization Matrix
    s, fid, tw, th = create_base_scene("Feature Value vs Complexity Prioritization", "PRODUCTO")
    s.add_rect(40, 80, 660, 165, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "QUICK WINS (ALTO VALOR / BAJA COMPLEJIDAD)", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 135, "• Exportador SVG vectorial directo sin dependencias.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 165, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "PROYECTOS HERO (ALTO VALOR / ALTA COMPLEJIDAD)", font_size=12, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_text(760, 135, "• Generacion automatica de arquitecturas mediante LLM.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(40, 265, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 290, "BAJA PRIORIDAD (BAJO VALOR / BAJA COMPLEJIDAD)", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(60, 320, "• Cambio de tema de color manual en CLI.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(740, 265, 660, 165, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 290, "DESCARTAR (BAJO VALOR / ALTA COMPLEJIDAD)", font_size=12, font_family=3, color="#64748B", frame_id=fid)
    s.add_text(760, 320, "• Editor WYSIWYG pesado en Electron.", font_size=11, font_family=3, color="#64748B", frame_id=fid)
    save_and_export(s, fid, cat, 95, "95_feature_prioritization_matrix", "Feature Prioritization Matrix", "medium", "quadrant", ["quick_wins", "strategic"])

    # 96. Feature Comparison Matrix
    s, fid, tw, th = create_base_scene("Feature Comparison vs Market Alternatives", "PRODUCTO")
    f_heads = ["FUNCIONALIDAD", "SKETION V10", "EXCALIDRAW WEB", "MIRO", "LUCIDCHART"]
    f_xs = [40, 320, 580, 840, 1100]
    for fh, fx in zip(f_heads, f_xs):
        s.add_text(fx, 85, fh, font_size=11, font_family=3, color="#64748B", frame_id=fid)
    f_rows = [
        ("Biblioteca de Plantillas", "212 Vectoriales", "Comunidad (~40)", "150+ (Cloud)", "200+ (Cloud)"),
        ("Renderizado Offline", "Si (100% Local)", "Parcial (Browser)", "No (Requiere Red)", "No (Requiere Red)"),
        ("Politica de Cero Emojis", "Si (Estricto)", "No", "No", "No"),
        ("Integracion CLI / SDK", "Si (Python Native)", "No", "No", "No")
    ]
    for idx, r in enumerate(f_rows):
        ry = 130 + idx * 75
        s.add_rect(30, ry, tw - 60, 65, bg="#FFF5F2" if idx==0 else "#FFFFFF", stroke="#D93829" if idx==0 else "#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        for val, fx in zip(r, f_xs):
            s.add_text(fx, ry + 22, val, font_size=11, font_family=3, color="#D93829" if idx==0 and fx==f_xs[0] else "#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 96, "96_feature_comparison_matrix", "Feature Comparison Matrix", "medium", "matrix_table", ["feature_list", "competitors"])

    # 97. Product Opportunity Canvas
    s, fid, tw, th = create_base_scene("Product Opportunity Assessment Canvas", "PRODUCTO")
    o_panels = [
        ("1. OPORTUNIDAD DE MERCADO", "Demanda masiva de herramientas de diagramacion para IA y desarrollo asistido.", 40, 80, 440, 160, True),
        ("2. POR QUE AHORA?", "La adopcion de Cursor y Antigravity exige generacion de diagramas por codigo.", 500, 80, 440, 160, False),
        ("3. VENTAJA DEFENDIBLE", "Motor determinista con 212 plantillas sin costo recurrente de API.", 960, 80, 440, 160, False),
        ("4. ESTRATEGIA GO-TO-MARKET", "Distribucion como skill oficial y paquete de Python open-source.", 40, 260, 660, 160, False),
        ("5. METRICA DE EXITO (TAM)", "Alcanzar 50,000 diagramas exportados en el primer trimestre.", 720, 260, 680, 160, False)
    ]
    for ot, od, ox, oy, ow, oh, is_h in o_panels:
        s.add_rect(ox, oy, ow, oh, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(ox + 20, oy + 20, ot, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(ox + 20, oy + 60, od, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 97, "97_product_opportunity_canvas", "Product Opportunity Canvas", "medium", "opportunity_canvas", ["market_size", "timing", "risks"])

    # 98. PMF Canvas
    s, fid, tw, th = create_base_scene("Product-Market Fit (PMF) Validation Framework", "PRODUCTO")
    s.add_rect(40, 80, 660, 350, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "EVALUACION DEL MERCADO (DEMANDA)", font_size=13, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 145, "• Audiencia Core: Ingenieros de Software y Arquitectos Cloud\n• Dolor Critico: Tiempo perdido cuadrando cajas a mano\n• Alternativa Actual: Herramientas web lentas y de pago", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "ENCANTO DEL PRODUCTO (RETENCION)", font_size=13, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(760, 145, "• Factor Wow: Exportacion SVG vectorial con tipografia Inter\n• Score Sean Ellis: 68% de usuarios 'muy decepcionados' sin la app\n• Estado: PRODUCT-MARKET FIT ALCANZADO", font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 98, "98_pmf_canvas", "PMF Canvas", "medium", "matrix_2x2", ["market_pull", "retention"])

    # 99. Product Lifecycle Map
    s, fid, tw, th = create_base_scene("Product Lifecycle Stages (Intro -> Growth -> Maturity -> Decline)", "PRODUCTO")
    s.add_line(80, 380, 1360, 380, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    stages = [("1. Introduccion", "Lanzamiento MVP Core 62", 140, False),
              ("2. Crecimiento", "Expansion v2 (212 Templates)", 460, True),
              ("3. Madurez", "Integracion en IDEs y LLMs", 780, False),
              ("4. Renovacion", "Generacion Autonoma AI v11", 1100, False)]
    for sname, sdesc, sx, is_h in stages:
        s.add_rect(sx, 160, 260, 140, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(sx + 15, 185, sname, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(sx + 15, 225, sdesc, font_size=10, font_family=3, color="#475569", frame_id=fid)
        s.add_line(sx + 130, 300, sx + 130, 380, stroke="#D93829" if is_h else "#94A3B8", stroke_w=1.5, frame_id=fid)
    save_and_export(s, fid, cat, 99, "99_product_lifecycle_map", "Product Lifecycle Map", "high", "lifecycle_curve", ["stages", "strategies"])

    # 100. Release Plan (Gantt)
    s, fid, tw, th = create_base_scene("Product Release Plan & Milestone Schedule", "PRODUCTO")
    s.add_rect(40, 80, 1360, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_line(80, 130, 1320, 130, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    releases = [
        ("v10.0 GA Core (62 Plantillas)", 140, 300, "#059669"),
        ("v10.1 Expansion (150 Plantillas)", 480, 350, "#D93829"),
        ("v10.2 Quality Audit (VCS >= 99)", 860, 240, "#0284C7"),
        ("v10.3 IDE Extension Sync", 1120, 180, "#D97706")
    ]
    for idx, (rname, rx, rw, rcol) in enumerate(releases):
        ry = 150 + idx * 60
        s.add_text(80, ry + 12, f"Rel #{idx+1}", font_size=11, font_family=3, color="#64748B", frame_id=fid)
        s.add_rect(rx, ry, rw, 36.0, bg="#FFF5F2" if rcol=="#D93829" else "#F8FAFC", stroke=rcol, stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(rx + 15, ry + 10, rname, font_size=10, font_family=3, color=rcol, frame_id=fid)
    save_and_export(s, fid, cat, 100, "100_release_plan", "Release Plan", "high", "gantt_releases", ["versions", "deadlines", "features"])

    # 101. Sprint Planning Board
    s, fid, tw, th = create_base_scene("Sprint Capacity & Velocity Planning Board", "PRODUCTO")
    s_cols = [
        {"title": "1. Backlog", "cards": [{"title": "Parser WASM", "desc": "Compilacion rapida", "tag": "P2"}]},
        {"title": "2. En Progreso", "cards": [{"title": "Reconstruir templates_2", "desc": "150 plantillas ricas", "tag": "P0"}], "is_hero": True},
        {"title": "3. Code Review", "cards": [{"title": "Auditoria de Cero Emojis", "desc": "Validar regex y XML", "tag": "P1"}]},
        {"title": "4. Completado", "cards": [{"title": "Core 62 Templates", "desc": "Validado en CI", "tag": "DONE"}]}
    ]
    s.add_kanban_board(40, 80, 1360, 350, "Sprint Board", s_cols, frame_id=fid)
    save_and_export(s, fid, cat, 101, "101_sprint_planning_board", "Sprint Planning Board", "medium", "sprint_board", ["capacity", "story_points"])

    # 102. Sprint Goal Canvas
    s, fid, tw, th = create_base_scene("Sprint Goal & Business Outcome Canvas", "PRODUCTO")
    s.add_rect(40, 80, 1360, 90, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "OBJETIVO DEL SPRINT (SP-24): Habilitar exportacion vectorial SVG nativa en produccion", font_size=13, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 140, "Por que es valioso? Permite a los usuarios descargar diagramas listos para web sin dependencias.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s_goals = [("1. CRITERIO DE EXITO", "100% de los 27 tipos exportan SVG valido.", 40), ("2. METRICA DE IMPACTO", "VCS >= 98.0 / 100 en el test suite.", 500), ("3. RIESGOS", "Curvas Bezier en diagramas de Venn.", 960)]
    for gt, gd, gx in s_goals:
        s.add_rect(gx, 190, 440, 230, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(gx + 20, 220, gt, font_size=12, font_family=3, color="#0F172A", frame_id=fid)
        s.add_text(gx + 20, 260, gd, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 102, "102_sprint_goal_canvas", "Sprint Goal Canvas", "medium", "goal_canvas", ["sprint_goal", "success_criteria"])

    # 103. Epic Breakdown
    s, fid, tw, th = create_base_scene("Epic Decomposition into Stories & Technical Tasks", "PRODUCTO")
    s.add_quad_card(40, 160, 280, 120, "EPICA PRINCIPAL", "Motor de Plantillas v2", badge="EPIC", is_hero=True, frame_id=fid)
    s.add_arrow(320, 220, 440, 120, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(320, 220, 440, 220, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(320, 220, 440, 320, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(440, 80, 440, 80, "Story 1: Generador Categorias 1 a 5", "Estudio, Ingenieria, Software, Data", frame_id=fid)
    s.add_quad_card(440, 180, 440, 80, "Story 2: Generador Categorias 6 a 10", "Producto, UX, Agile, Productividad", is_hero=True, frame_id=fid)
    s.add_quad_card(440, 280, 440, 80, "Story 3: Validador de Calidad", "Auditoria de Cero Emojis y VCS >= 99", frame_id=fid)
    save_and_export(s, fid, cat, 103, "103_epic_breakdown", "Epic Breakdown", "medium", "epic_tree", ["epic", "stories", "subtasks"])

    # 104. Product Metrics Tree
    s, fid, tw, th = create_base_scene("Product Metrics Hierarchy Tree (North Star -> Inputs)", "PRODUCTO")
    s.add_quad_card(600, 70, 260, 90, "NORTH STAR METRIC", "Exportaciones Exitosas", badge="NSM", is_hero=True, frame_id=fid)
    s.add_arrow(680, 160, 325, 240, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(730, 160, 725, 240, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(780, 160, 1125, 240, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(200, 240, 250, 110, "Input 1: Amplitud", "212 Plantillas Listas", badge="BREADTH", frame_id=fid)
    s.add_quad_card(600, 240, 250, 110, "Input 2: Calidad Visual", "VCS >= 99.0 y 0 Emojis", badge="QUALITY", frame_id=fid)
    s.add_quad_card(1000, 240, 250, 110, "Input 3: Velocidad", "Renderizado < 100ms", badge="VELOCITY", frame_id=fid)
    save_and_export(s, fid, cat, 104, "104_product_metrics_tree", "Product Metrics Tree", "high", "metric_tree", ["north_star", "input_metrics"])

    # 105. North Star Metric Framework
    s, fid, tw, th = create_base_scene("North Star Metric (NSM) & Strategic Value Levers", "PRODUCTO")
    s.add_quad_card(600, 70, 260, 90, "NORTH STAR METRIC", "Diagramas Exportados con Exito", badge="ESTRELLA GUIA", is_hero=True, frame_id=fid)
    s.add_quad_card(200, 240, 250, 110, "Palanca 1: Cobertura", "62 + 150 Plantillas", badge="BREADTH", frame_id=fid)
    s.add_quad_card(600, 240, 250, 110, "Palanca 2: Fidelidad", "Tipografia Inter Nativa", badge="QUALITY", frame_id=fid)
    s.add_quad_card(1000, 240, 250, 110, "Palanca 3: Retencion", "Uso Semanal Recurrente", badge="RETENTION", frame_id=fid)
    s.add_arrow(680, 160, 325, 240, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(730, 160, 725, 240, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(780, 160, 1125, 240, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 105, "105_north_star_metric", "North Star Metric Framework", "high", "north_star_hub", ["nsm", "drivers", "kpis"])
