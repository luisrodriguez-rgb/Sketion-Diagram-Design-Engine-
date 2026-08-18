"""
Generador de Categoría 07: UX & Design Research (15 Plantillas)
"""

from .common import create_base_scene, save_and_export

def generate():
    print("\n--- Generando 07: UX & Design Research (15 plantillas) ---")
    cat = "07_ux_research"

    # 106. Research Affinity Cluster
    s, fid, tw, th = create_base_scene("UX Research Affinity Clustering & Pattern Synthesis", "DISEÑO & UX")
    r_stages = [("1. OBSERVACIONES RAW", ["'Me cuesta alinear cajas a mano.'", "'Pierdo tiempo buscando iconos.'"], 40, False),
                ("2. CLUSTERS TEMATICOS", ["Friccion de layout visual", "Carencia de arquetipos listos"], 390, False),
                ("3. PATRONES CONDUCTUALES", ["Los usuarios abandonan si el setup toma > 5 min", "Prefieren exportar SVG antes que PNG"], 740, False),
                ("4. INSIGHTS ACCIONABLES", ["La velocidad de inicio define la retencion", "Cero emojis = mayor percepcion profesional"], 1090, True)]
    for rtitle, ritems, rx, is_h in r_stages:
        s.add_rect(rx, 80, 310, 350, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(rx + 15, 105, rtitle, font_size=11, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        for ii, itxt in enumerate(ritems):
            s.add_rect(rx + 12, 145 + ii * 85, 285, 70, bg="#FFFFFF" if is_h else "#F8FAFC", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=fid)
            s.add_text(rx + 20, 165 + ii * 85, itxt, font_size=10, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 106, "106_research_affinity_cluster", "Research Affinity Cluster", "high", "affinity_clusters", ["raw_data", "clusters", "insights"])

    # 107. Service Blueprint (4 Functional Lanes)
    s, fid, tw, th = create_base_scene("Service Blueprint (Evidence, Customer, Frontstage, Backstage)", "DISEÑO & UX")
    s_lanes = [
        ("1. EVIDENCIA FISICA", "Landing Page Web · Editor SVG · Notificacion Email", 80, "#64748B"),
        ("2. ACCIONES DEL CLIENTE", "Selecciona plantilla -> Personaliza textos -> Descarga SVG", 165, "#0F172A"),
        ("3. FRONTSTAGE (INTERACCION)", "Renderizado en canvas -> Calculo de colisiones -> Auto-fit", 250, "#D93829"),
        ("4. BACKSTAGE & SOPORTE", "Compilador Python SDK -> Validacion CI -> CDN de activos", 335, "#0284C7")
    ]
    for stitle, sdesc, sy, scol in s_lanes:
        s.add_rect(40, sy, tw - 80, 70, bg="#FFFFFF", stroke=scol, stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(60, sy + 12, stitle, font_size=11, font_family=3, color=scol, frame_id=fid)
        s.add_text(60, sy + 38, sdesc, font_size=11, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 107, "107_service_blueprint", "Service Blueprint", "extreme", "service_blueprint", ["physical_evidence", "frontstage", "backstage", "support"])

    # 108. Experience Map
    s, fid, tw, th = create_base_scene("Holistic Customer Experience Map", "DISEÑO & UX")
    e_steps = [("1. Descubrimiento", "Busqueda de plantillas en GitHub", 40, False),
               ("2. Evaluacion", "Inspeccion visual del catalogo", 390, False),
               ("3. Uso Activo", "Generacion con un solo comando", 740, True),
               ("4. Fidelizacion", "Integracion en el flujo de trabajo", 1090, False)]
    for ename, edesc, ex, is_h in e_steps:
        s.add_rect(ex, 140, 310, 150, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(ex + 15, 165, ename, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(ex + 15, 205, edesc, font_size=10, font_family=3, color="#475569", frame_id=fid)
        if ex < 1090:
            s.add_arrow(ex + 310, 215, ex + 350, 215, stroke="#D93829" if is_h else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 108, "108_experience_map", "Experience Map", "high", "experience_map", ["phases", "touchpoints", "emotional_curve"])

    # 109. Touchpoint Map
    s, fid, tw, th = create_base_scene("Multichannel Customer Touchpoint Matrix", "DISEÑO & UX")
    t_heads = ["CANAL / ETAPA", "DESCUBRIMIENTO", "ONBOARDING", "USO CORE", "SOPORTE"]
    t_xs = [40, 320, 580, 840, 1100]
    for th_txt, tx in zip(t_heads, t_xs):
        s.add_text(tx, 85, th_txt, font_size=11, font_family=3, color="#64748B", frame_id=fid)
    t_rows = [
        ("Web / Documentacion", "Landing Page", "Guia Universal", "Visor SVG", "FAQ Tecnico"),
        ("CLI / IDE Extension", "Comando help", "Auto-completado", "Render local", "Logs de depuracion"),
        ("Repositorio GitHub", "README con badges", "Templates folder", "Issues de soporte", "Discusiones")
    ]
    for idx, r in enumerate(t_rows):
        ry = 130 + idx * 85
        s.add_rect(30, ry, tw - 60, 70, bg="#FFF5F2" if idx==0 else "#FFFFFF", stroke="#D93829" if idx==0 else "#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        for val, tx in zip(r, t_xs):
            s.add_text(tx, ry + 25, val, font_size=11, font_family=3, color="#D93829" if idx==0 and tx==t_xs[0] else "#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 109, "109_touchpoint_map", "Touchpoint Map", "medium", "touchpoint_grid", ["channels", "stages"])

    # 110. UX Research Synthesis
    s, fid, tw, th = create_base_scene("Executive UX Research Findings Synthesis", "DISEÑO & UX")
    syn_tiers = [
        ("1. RESUMEN EJECUTIVO (KEY TAKEAWAY)", "Los diagramas vectoriales generados por codigo reducen el tiempo de documentacion un 75%.", 80, "#D93829"),
        ("2. TRES HALLAZGOS PRINCIPALES", "• Cero emojis es mandatorio para reportes de direccion.\n• Inter es la tipografia con mejor legibilidad vectorial.", 165, "#0284C7"),
        ("3. DIRECTRICES DE DISENO PARA EL MOTOR", "Mantener padding >= 35px en frames y ruteo a 90 grados en todos los conectores.", 285, "#059669")
    ]
    for stitle, sdesc, sy, scol in syn_tiers:
        s.add_rect(40, sy, tw - 80, 75 if sy!=165 else 105, bg="#FFFFFF", stroke=scol, stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(60, sy + 12, stitle, font_size=11, font_family=3, color=scol, frame_id=fid)
        s.add_text(60, sy + 38, sdesc, font_size=11, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 110, "110_ux_research_synthesis", "UX Research Synthesis", "medium", "synthesis_layers", ["executive_summary", "key_findings", "recommendations"])

    # 111. Research Findings Board
    s, fid, tw, th = create_base_scene("Qualitative & Quantitative UX Findings Board", "DISEÑO & UX")
    f_cards = [
        ("CITA DE USUARIO 1", "'Poder exportar a SVG e insertarlo en Notion sin dependencias es increible.'", 40, 80, 440, 160, True),
        ("CITA DE USUARIO 2", "'El diseno oscuro y la ausencia de emojis hacen que mis diagramas se vean ejecutivos.'", 500, 80, 440, 160, False),
        ("METRICA DE IMPACTO", "Reduccion del tiempo medio de diagramacion: de 45 min a 2.5 min.", 960, 80, 440, 160, True),
        ("OPORTUNIDAD DE MEJORA", "Agregar mas plantillas especializadas para pipelines de Inteligencia Artificial.", 40, 260, 660, 160, False),
        ("RECOMENDACION TECNICA", "Mantener la suite de regresion CI con 27 pruebas obligatorias antes de cada release.", 720, 260, 680, 160, False)
    ]
    for ft, fd, fx, fy, fw, fh, is_h in f_cards:
        s.add_rect(fx, fy, fw, fh, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(fx + 20, fy + 20, ft, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(fx + 20, fy + 60, fd, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 111, "111_research_findings_board", "Research Findings Board", "medium", "findings_board", ["verbatims", "metrics", "heuristics"])

    # 112. Usability Testing Board
    s, fid, tw, th = create_base_scene("Usability Testing Results & Task Success Board", "DISEÑO & UX")
    u_headers = ["TAREA EVALUADA", "TASA DE EXITO", "TIEMPO PROMEDIO", "SEVERIDAD DE FRICCION", "OBSERVACION"]
    u_xs = [40, 360, 560, 780, 1020]
    for uh, ux_pos in zip(u_headers, u_xs):
        s.add_text(ux_pos, 85, uh, font_size=11, font_family=3, color="#64748B", frame_id=fid)
    u_rows = [
        ("1. Seleccionar plantilla de catalogo", "100%", "4.2 s", "NULA", "Descubrimiento fluido"),
        ("2. Exportar a SVG vectorial", "98%", "2.1 s", "NULA", "Excelente rendimiento"),
        ("3. Personalizar colores de capa", "92%", "12.5 s", "LEVE", "Facil adaptacion visual")
    ]
    for idx, r in enumerate(u_rows):
        ry = 130 + idx * 85
        s.add_rect(30, ry, tw - 60, 70, bg="#FFF5F2" if idx==0 else "#FFFFFF", stroke="#D93829" if idx==0 else "#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        for val, ux_pos in zip(r, u_xs):
            s.add_text(ux_pos, ry + 25, val, font_size=11, font_family=3, color="#D93829" if val in ["100%", "NULA"] else "#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 112, "112_usability_testing_board", "Usability Testing Board", "high", "usability_table", ["task_success", "time_on_task"])

    # 113. User Interview Canvas
    s, fid, tw, th = create_base_scene("User Interview Guide & Structured Transcript Canvas", "DISEÑO & UX")
    i_panels = [
        ("1. PERFIL DEL ENTREVISTADO", "Ingeniero Cloud Senior · 8 anos de experiencia · Lider de arquitectura", 40, 80, 440, 160, False),
        ("2. DOLORES PRINCIPALES", "• Pasar horas alineando flechas\n• Herramientas web que exigen suscripcion cara", 500, 80, 440, 160, True),
        ("3. MOMENTOS DE FRUSTRACION", "Cuando un diagrama desalineado es presentado en una revision tecnica de C-Level.", 960, 80, 440, 160, False),
        ("4. DESEOS & EXPECTATIVAS", "Generar diagramas limpios desde terminal o VS Code con tipografia moderna.", 40, 260, 660, 160, False),
        ("5. PROXIMOS PASOS", "Incluir el flujo en el onboarding de la empresa como herramienta estandar.", 720, 260, 680, 160, False)
    ]
    for it, idesc, ix, iy, iw, ih, is_h in i_panels:
        s.add_rect(ix, iy, iw, ih, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(ix + 20, iy + 20, it, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(ix + 20, iy + 60, idesc, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 113, "113_user_interview_canvas", "User Interview Canvas", "medium", "interview_blocks", ["questions", "quotes", "body_language"])

    # 114. Research Plan
    s, fid, tw, th = create_base_scene("UX Research Plan (Objectives, Hypothesis, Methods, Timeline)", "DISEÑO & UX")
    r_plan = [
        ("1. OBJETIVO DEL ESTUDIO", "Evaluar la usabilidad y adopcion de la biblioteca de 212 plantillas.", 80, "#D93829"),
        ("2. HIPOTESIS DE INVESTIGACION", "Los ingenieros prefieren plantillas con semantica real antes que rectangulos dummy.", 165, "#0284C7"),
        ("3. METODOLOGIA & MUESTRA", "12 entrevistas en profundidad con arquitectos y pruebas de usabilidad moderadas.", 250, "#059669"),
        ("4. CRONOGRAMA & HITOS", "Semanas 1-2: Reclutamiento · Semana 3: Entrevistas · Semana 4: Reporte final.", 335, "#64748B")
    ]
    for rtitle, rdesc, ry, rcol in r_plan:
        s.add_rect(40, ry, tw - 80, 70, bg="#FFFFFF", stroke=rcol, stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(60, ry + 12, rtitle, font_size=11, font_family=3, color=rcol, frame_id=fid)
        s.add_text(60, ry + 38, rdesc, font_size=11, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 114, "114_research_plan", "Research Plan", "medium", "research_plan", ["goals", "methodology", "recruiting"])

    # 115. Research Question Map
    s, fid, tw, th = create_base_scene("Research Question Decomposition Tree", "DISEÑO & UX")
    s.add_quad_card(580, 70, 280, 80, "PREGUNTA CENTRAL", "¿Como mejorar la diagramacion tecnica?", is_hero=True, frame_id=fid)
    s.add_arrow(720, 150, 320, 230, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(720, 150, 720, 230, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(720, 150, 1120, 230, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(200, 230, 250, 110, "Q1: Velocidad", "¿Cuanto tiempo toma crear un diagrama?", badge="TIME", frame_id=fid)
    s.add_quad_card(600, 230, 250, 110, "Q2: Calidad Visual", "¿Cumple los estandares para reviews?", badge="QUALITY", frame_id=fid)
    s.add_quad_card(1000, 230, 250, 110, "Q3: Autonomia", "¿Funciona 100% en local sin internet?", badge="AUTONOMY", frame_id=fid)
    save_and_export(s, fid, cat, 115, "115_research_question_map", "Research Question Map", "medium", "question_tree", ["core_question", "subquestions"])

    # 116. Insight to Opportunity Map
    s, fid, tw, th = create_base_scene("Research Insight to Design Opportunity Translation Map", "DISEÑO & UX")
    i_cols = ["1. HALLAZGO RAW", "2. INSIGHT PROFUNDO", "3. OPORTUNIDAD DE DISENO", "4. SOLUCION PROPUESTA"]
    for i, ic in enumerate(i_cols):
        ix = 40 + i * 345
        s.add_quad_card(ix, 140, 330, 150, ic, f"Traduccion fase #{i+1}", badge=f"FASE {i+1}", is_hero=(i==2), frame_id=fid)
        if i < len(i_cols) - 1:
            s.add_arrow(ix + 330, 215, ix + 345, 215, stroke="#D93829" if i==2 else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 116, "116_insight_to_opportunity", "Insight to Opportunity Map", "high", "translation_flow", ["findings", "insights", "opportunities"])

    # 117. Problem Statement Canvas
    s, fid, tw, th = create_base_scene("Problem Statement Formulation Canvas", "DISEÑO & UX")
    s.add_rect(40, 80, 1360, 100, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "DECLARACION DE PROBLEMA (PROBLEM STATEMENT)", font_size=13, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 140, "Nuestros usuarios necesitan una forma de diagramar arquitecturas limpias porque pierden 4h semanales alineando cajas a mano.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    p_quads = [("¿QUIEN LO SUFRE?", "Arquitectos de software e ingenieros cloud", 40), ("¿DONDE OCURRE?", "En reuniones de diseno de sistemas y documentacion", 500), ("¿CUAL ES EL IMPACTO?", "Retrasos en reviews y diagramas desactualizados", 960)]
    for pt, pd, px in p_quads:
        s.add_rect(px, 200, 440, 220, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(px + 20, 230, pt, font_size=12, font_family=3, color="#0F172A", frame_id=fid)
        s.add_text(px + 20, 275, pd, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 117, "117_problem_statement_canvas", "Problem Statement Canvas", "medium", "problem_canvas", ["who", "where", "impact"])

    # 118. Design Opportunity Map
    s, fid, tw, th = create_base_scene("Strategic Design Opportunity & Value Map", "DISEÑO & UX")
    s.add_rect(40, 80, 660, 165, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "ALTO IMPACTO / ALTA FACTIBILIDAD (PRIORIDAD 1)", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 135, "• Exportador SVG vectorial directo e integracion en Markdown.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 165, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "ALTO IMPACTO / BAJA FACTIBILIDAD (APUESTAS FUTURAS)", font_size=12, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_text(760, 135, "• Reconocimiento optico de diagramas dibujados en pizarra blanca.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(40, 265, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 290, "BAJO IMPACTO / ALTA FACTIBILIDAD (MEJORAS MENORES)", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(60, 320, "• Ajuste de paleta de colores personalizada en config.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(740, 265, 660, 165, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 290, "BAJO IMPACTO / BAJA FACTIBILIDAD (IGNORAR)", font_size=12, font_family=3, color="#64748B", frame_id=fid)
    s.add_text(760, 320, "• Soporte para formatos rasterizados obsoletos.", font_size=11, font_family=3, color="#64748B", frame_id=fid)
    save_and_export(s, fid, cat, 118, "118_design_opportunity_map", "Design Opportunity Map", "medium", "quadrant", ["high_impact", "high_feasibility"])

    # 119. UX Benchmark Matrix
    s, fid, tw, th = create_base_scene("UX Heuristic & Usability Benchmark Matrix", "DISEÑO & UX")
    b_heads = ["PRINCIPIO HEURISTICO", "SKETION V10", "EXCALIDRAW", "LUCIDCHART", "MIRO"]
    b_xs = [40, 320, 580, 840, 1100]
    for bh, bx in zip(b_heads, b_xs):
        s.add_text(bx, 85, bh, font_size=11, font_family=3, color="#64748B", frame_id=fid)
    b_rows = [
        ("Visibilidad del Estado", "Excelente (100% Local)", "Buena", "Buena", "Buena"),
        ("Control y Libertad del Usuario", "Total (Archivos planos)", "Buena", "Restringida", "Restringida"),
        ("Consistencia y Estandares", "Estricto (Cero Emojis)", "Variable", "Media", "Media"),
        ("Flexibilidad y Eficiencia", "CLI + Python SDK", "Manual Web", "Manual Web", "Manual Web")
    ]
    for idx, r in enumerate(b_rows):
        ry = 130 + idx * 85
        s.add_rect(30, ry, tw - 60, 70, bg="#FFF5F2" if idx==0 else "#FFFFFF", stroke="#D93829" if idx==0 else "#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        for val, bx in zip(r, b_xs):
            s.add_text(bx, ry + 25, val, font_size=11, font_family=3, color="#D93829" if idx==0 and bx==b_xs[0] else "#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 119, "119_ux_benchmark_matrix", "UX Benchmark Matrix", "high", "benchmark_table", ["heuristics", "scores"])

    # 120. User Mental Model (Venn)
    s, fid, tw, th = create_base_scene("User Mental Model vs System Conceptual Model", "DISEÑO & UX")
    s.add_ellipse(380, 120, 380, 260, bg="#FFF5F2", stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_text(420, 180, "MODELO MENTAL DEL USUARIO\n\n• Espera comandos simples\n• Quiere diagramas limpios\n• Desea archivos SVG listos", font_size=11, font_family=3, color="#D93829", frame_id=fid)
    s.add_ellipse(680, 120, 380, 260, bg="#EFF6FF", stroke="#3B82F6", stroke_w=2.0, frame_id=fid)
    s.add_text(850, 180, "MODELO REAL DEL SISTEMA\n\n• Parser determinista a 90°\n• Auto-fit con padding >= 35px\n• 0 dependencias de red", font_size=11, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_text(660, 240, "ZONA DE\nALINEACION", font_size=10, font_family=3, color="#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 120, "120_user_mental_model", "User Mental Model", "high", "mental_model_venn", ["user_mental_model", "system_model"])
