"""
Generador de Categoría 10: Productividad y Organización (10 Plantillas)
"""

from .common import create_base_scene, save_and_export

def generate():
    print("\n--- Generando 10: Productividad y Organización (10 plantillas) ---")
    cat = "10_productividad_personal"

    # 141. Monthly Planner (30 Days Grid)
    s, fid, tw, th = create_base_scene("Monthly Strategic & Operational Planner", "PRODUCTIVIDAD")
    for d in range(1, 31):
        col = (d-1) % 6
        row = (d-1) // 6
        is_h = d == 15
        s.add_rect(40 + col * 230, 80 + row * 68, 215, 60, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.2, roundness_type=3, frame_id=fid)
        s.add_text(55 + col * 230, 95 + row * 68, f"Dia {d}", font_size=10, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 141, "141_monthly_planner", "Monthly Planner", "low", "calendar_grid", ["days_30", "events"])

    # 142. Yearly Planner (4 Quarters)
    s, fid, tw, th = create_base_scene("Yearly Strategic Milestones & Goals Planner", "PRODUCTIVIDAD")
    q_quarters = [("Q1: ENE - MAR", "Lanzamiento Core GA y 62 plantillas", 40, False),
                  ("Q2: ABR - JUN", "Expansion v2 (150 nuevas plantillas)", 390, True),
                  ("Q3: JUL - SEP", "Ecosistema de plugins para IDEs", 740, False),
                  ("Q4: OCT - DIC", "Generador autonomo multimodal", 1090, False)]
    for qtitle, qdesc, qx, is_h in q_quarters:
        s.add_rect(qx, 80, 310, 350, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(qx + 15, 105, qtitle, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(qx + 15, 150, qdesc, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 142, "142_yearly_planner", "Yearly Planner", "medium", "quarters_4", ["quarters", "annual_goals"])

    # 143. Goal Planner (SMART Framework)
    s, fid, tw, th = create_base_scene("SMART Goal Formulation & Execution Planner", "PRODUCTIVIDAD")
    smart_blocks = [
        ("S: ESPECIFICO (SPECIFIC)", "Construir 150 plantillas de diagramacion sin repeticion estructural.", 40, 80, 440, 160, True),
        ("M: MEDIBLE (MEASURABLE)", "Validar 150/150 SVGs y 150/150 Excalidraw con VCS >= 99.0 y 0 emojis.", 500, 80, 440, 160, False),
        ("A: ALCANZABLE (ACHIEVABLE)", "Usar constructores modulares especializados en ExcalidrawScene.", 960, 80, 440, 160, False),
        ("R: RELEVANTE (RELEVANT)", "Elevar el posicionamiento de Sketion como motor de diagramacion definitivo.", 40, 260, 660, 160, False),
        ("T: TEMPORALIZADO (TIME-BOUND)", "Completar la generacion, auditoria y documentacion hoy mismo.", 720, 260, 680, 160, False)
    ]
    for st, sd, sx, sy, sw, sh, is_h in smart_blocks:
        s.add_rect(sx, sy, sw, sh, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(sx + 20, sy + 20, st, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(sx + 20, sy + 60, sd, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 143, "143_goal_planner", "Goal Planner", "medium", "smart_goals", ["specific", "measurable", "achievable", "relevant", "time_bound"])

    # 144. Goal Breakdown (Cascade)
    s, fid, tw, th = create_base_scene("Annual Goal to Daily Habit Decomposition Tree", "PRODUCTIVIDAD")
    s.add_quad_card(580, 70, 280, 80, "META ANUAL: SKETION V10", "Suite Universal de Diagramacion", is_hero=True, frame_id=fid)
    s.add_arrow(720, 150, 320, 230, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(720, 150, 720, 230, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(720, 150, 1120, 230, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(200, 230, 250, 110, "Hito Q1: 62 Core", "Fundamentos y CI", badge="Q1", frame_id=fid)
    s.add_quad_card(600, 230, 250, 110, "Hito Q2: 150 Expansion", "212 plantillas listas", badge="Q2", is_hero=True, frame_id=fid)
    s.add_quad_card(1000, 230, 250, 110, "Habito Diario: 1 Commit", "Revision de calidad constante", badge="HABIT", frame_id=fid)
    save_and_export(s, fid, cat, 144, "144_goal_breakdown", "Goal Breakdown", "medium", "goal_tree", ["annual_goal", "monthly_milestones", "daily_habits"])

    # 145. Personal OKR (3 Objectives & Key Results)
    s, fid, tw, th = create_base_scene("Personal Objectives & Key Results (OKR) Canvas", "PRODUCTIVIDAD")
    okr_tiers = [
        ("OBJETIVO 1: CALIDAD DE INGENIERIA (100% COMPLETADO)", "KR 1: Cero errores de sintaxis en 212 SVGs · KR 2: VCS >= 99.0 · KR 3: Cero emojis", 80, "#059669"),
        ("OBJETIVO 2: VELOCIDAD DE DESARROLLO (EN CURSO)", "KR 1: Compilar 150 plantillas en < 3s · KR 2: Scripts modulares por categoria", 190, "#D93829"),
        ("OBJETIVO 3: IMPACTO PROFESIONAL", "KR 1: Documentacion clara en README · KR 2: Informe diagnostico completo", 300, "#0284C7")
    ]
    for o_title, o_desc, oy, o_col in okr_tiers:
        s.add_rect(40, oy, tw - 80, 95, bg="#FFFFFF", stroke=o_col, stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(60, oy + 15, o_title, font_size=11, font_family=3, color=o_col, frame_id=fid)
        s.add_text(60, oy + 48, o_desc, font_size=11, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 145, "145_personal_okr", "Personal OKR", "medium", "okr_canvas", ["objective", "key_results"])

    # 146. Task Dependency Map
    s, fid, tw, th = create_base_scene("Personal Task Dependency & Priority Graph", "PRODUCTIVIDAD")
    s.add_quad_card(40, 180, 220, 90, "Definir Requisitos", "Paso 1", is_hero=True, frame_id=fid)
    s.add_arrow(260, 225, 360, 225, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(360, 180, 260, 90, "Escribir Generadores", "Paso 2 (Modular)", is_hero=True, frame_id=fid)
    s.add_arrow(620, 225, 720, 225, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(720, 180, 260, 90, "Auditoria y Reporte", "Paso 3", is_hero=True, frame_id=fid)
    s.add_arrow(980, 225, 1080, 225, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_quad_card(1080, 180, 240, 90, "Entrega al Usuario", "Paso 4 (Exito)", is_hero=True, frame_id=fid)
    save_and_export(s, fid, cat, 146, "146_task_dependency_map", "Task Dependency Map", "medium", "task_graph", ["tasks", "dependencies"])

    # 147. Meeting Agenda
    s, fid, tw, th = create_base_scene("Executive Meeting Agenda & Time Allocation", "PRODUCTIVIDAD")
    s.add_rect(40, 80, 1360, 80, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "REUNION EJECUTIVA: Lanzamiento Sketion Expansion Library v2 (212 Templates)", font_size=13, font_family=3, color="#D93829", frame_id=fid)
    s_topics = [("10:00 - 10:15", "Alineacion de Alcance", "Validar las 150 plantillas y diversidad visual."),
                ("10:15 - 10:45", "Auditoria de Calidad", "Revisar VCS >= 99.5 y cero emojis."),
                ("10:45 - 11:00", "Acuerdos & Despliegue", "Sincronizacion en GitHub y documentacion.")]
    for i, (ttime, ttitle, tdesc) in enumerate(s_topics):
        tx = 40 + i * 460
        s.add_rect(tx, 180, 430, 240, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(tx + 20, 210, ttime, font_size=11, font_family=3, color="#D93829", frame_id=fid)
        s.add_text(tx + 20, 245, ttitle, font_size=13, font_family=3, color="#0F172A", frame_id=fid)
        s.add_text(tx + 20, 285, tdesc, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 147, "147_meeting_agenda", "Meeting Agenda", "low", "agenda_blocks", ["time_slots", "topics"])

    # 148. Meeting Retrospective
    s, fid, tw, th = create_base_scene("Meeting Effectiveness & Action Items Retrospective", "PRODUCTIVIDAD")
    r_cols = [
        {"title": "1. Que Salio Bien", "cards": [{"title": "Velocidad de ejecucion", "desc": "Generacion en segundos", "tag": "PLUS"}]},
        {"title": "2. Que Podemos Mejorar", "cards": [{"title": "Diversidad inicial", "desc": "Evitar funciones genericas", "tag": "DELTA"}], "is_hero": True},
        {"title": "3. Acciones Acordadas", "cards": [{"title": "Constructores modulares", "desc": "Implementados en core", "tag": "ACTION"}]}
    ]
    s.add_kanban_board(40, 80, 1360, 350, "Retro Board", r_cols, frame_id=fid)
    save_and_export(s, fid, cat, 148, "148_meeting_retrospective", "Meeting Retrospective", "medium", "swimlane", ["effectiveness", "actions"])

    # 149. Decision Log (ADR Architecture Decision Record)
    s, fid, tw, th = create_base_scene("Architecture Decision Record (ADR) Log", "PRODUCTIVIDAD")
    s.add_rect(40, 80, 1360, 350, bg="#FFFFFF", stroke="#0F172A", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "ADR-0042: REESTRUCTURACION MODULAR DE LA BIBLIOTECA DE 150 PLANTILLAS", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    adr_cols = [
        ("CONTEXTO", "Las primeras 150 plantillas reutilizaban funciones estaticas repetitivas.", 60, False),
        ("DECISION", "Crear generadores dedicados por categoria con constructores modulares propios.", 500, True),
        ("CONSECUENCIAS", "100% de diversidad estructural, 0 emojis, VCS >= 99.5 y arquitectura mantenible.", 940, False)
    ]
    for atitle, adesc, ax, is_h in adr_cols:
        s.add_rect(ax, 140, 400, 250, bg="#FFF5F2" if is_h else "#F8FAFC", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(ax + 15, 165, atitle, font_size=11, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(ax + 15, 205, adesc, font_size=11, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 149, "149_decision_log", "Decision Log", "medium", "timeline_adr", ["decision_id", "context", "consequences"])

    # 150. Personal Dashboard (4-Block Executive Health & Focus)
    s, fid, tw, th = create_base_scene("Personal Executive Productivity & Focus Dashboard", "PRODUCTIVIDAD")
    p_quads = [
        ("FOCO DIARIO PRINCIPAL", "• Finalizar la compilacion de las 212 plantillas\n• Entregar reporte comparativo completo", 40, 80, 660, 165, True),
        ("HABITOS & DISCIPLINA", "• 100% cero emojis en todos los archivos\n• Validar 27 tests CI de regresion", 740, 80, 660, 165, False),
        ("PROYECTOS ACTIVOS", "• Sketion v10 GA Core (Completado)\n• Expansion v2 150 Templates (Completado)", 40, 265, 660, 165, False),
        ("METRICAS DE EFECTIVIDAD", "• Horas de Deep Work: 6.5h\n• Consistencia Visual: 99.50 / 100", 740, 265, 660, 165, True)
    ]
    for pt, pd, px, py, pw, ph, is_h in p_quads:
        s.add_rect(px, py, pw, ph, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(px + 20, py + 20, pt, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(px + 20, py + 60, pd, font_size=11, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 150, "150_personal_dashboard", "Personal Dashboard", "high", "personal_dashboard", ["daily_focus", "metrics", "habits", "projects"])
