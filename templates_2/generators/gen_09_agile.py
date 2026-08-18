"""
Generador de Categoría 09: Agile y Gestión de Proyectos (10 Plantillas)
"""

from .common import create_base_scene, save_and_export

def generate():
    print("\n--- Generando 09: Agile y Gestión de Proyectos (10 plantillas) ---")
    cat = "09_agile_proyectos"

    # 131. Agile Release Train (SAFe Cadence)
    s, fid, tw, th = create_base_scene("Agile Release Train (ART) Cadence & Sprints", "AGILE & PROYECTOS")
    s.add_rect(40, 80, 1360, 70, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "PROGRAM INCREMENT (PI-Q3): Sistema de Plantillas y Auditoria Continua", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    sprints = ["Sprint 1: Core 62", "Sprint 2: Expansion v2", "Sprint 3: Quality Audit", "Sprint 4: Release GA"]
    for i, sp in enumerate(sprints):
        sx = 40 + i * 345
        s.add_quad_card(sx, 170, 330, 250, sp, f"Objetivos de iteracion #{i+1}\nEntregables cerrados\nDemo & Retrospectiva", badge=f"SPRINT {i+1}", is_hero=(i==1), frame_id=fid)
    save_and_export(s, fid, cat, 131, "131_agile_release_train", "Agile Release Train", "high", "release_train", ["pi_cadence", "sprints"])

    # 132. Sprint Review
    s, fid, tw, th = create_base_scene("Sprint Review & Stakeholder Demo Board", "AGILE & PROYECTOS")
    sr_cols = [
        {"title": "1. Historias Aceptadas", "cards": [{"title": "Exportador SVG", "desc": "100% de tests aprobados", "tag": "DEMO"}]},
        {"title": "2. Feedback Recibido", "cards": [{"title": "Mayor diversidad", "desc": "Requerido por usuarios", "tag": "FEEDBACK"}], "is_hero": True},
        {"title": "3. Ajustes de Backlog", "cards": [{"title": "Generador v2", "desc": "Priorizado para Sprint 2", "tag": "TODO"}]},
        {"title": "4. Metricas de Sprint", "cards": [{"title": "Velocidad: 42 pts", "desc": "VCS: 99.5 / 100", "tag": "METRICS"}]}
    ]
    s.add_kanban_board(40, 80, 1360, 350, "Review Board", sr_cols, frame_id=fid)
    save_and_export(s, fid, cat, 132, "132_sprint_review", "Sprint Review", "medium", "swimlane", ["demo_features", "feedback"])

    # 133. Daily Standup Board
    s, fid, tw, th = create_base_scene("Daily Standup (Yesterday, Today, Blockers)", "AGILE & PROYECTOS")
    d_cols = [
        ("AYER (COMPLETADO)", ["• Generadas categorias 1 a 5", "• Creado informe de diagnostico", "• Actualizado README.md"], 40, False),
        ("HOY (PLANIFICADO)", ["• Generar categorias 6 a 10", "• Auditar 150 plantillas con 0 emojis", "• Ejecutar suite CI de 27 tests"], 500, True),
        ("BLOQUEOS / IMPEDIMENTOS", ["• Ninguno activo actualmente", "• Todos los tests en PASS"], 960, False)
    ]
    for dt, dtasks, dx, is_h in d_cols:
        s.add_rect(dx, 80, 440, 350, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(dx + 20, 105, dt, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        for ti, ttxt in enumerate(dtasks):
            s.add_text(dx + 20, 150 + ti * 32, ttxt, font_size=11, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 133, "133_daily_standup_board", "Daily Standup Board", "low", "columns_3", ["yesterday", "today", "blockers"])

    # 134. Release Planning
    s, fid, tw, th = create_base_scene("Quarterly Release Planning Roadmap", "AGILE & PROYECTOS")
    s.add_rect(40, 80, 1360, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_line(80, 130, 1320, 130, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    q_releases = [
        ("Q1: Core Engine GA (62 Templates)", 140, 300, "#059669"),
        ("Q2: Expansion v2 (150 Templates)", 480, 350, "#D93829"),
        ("Q3: Ecosistema IDEs & Plugins", 860, 240, "#0284C7"),
        ("Q4: Generador Autonomo IA v11", 1120, 180, "#D97706")
    ]
    for idx, (qname, qx, qw, qcol) in enumerate(q_releases):
        qy = 150 + idx * 60
        s.add_text(80, qy + 12, f"Trimestre #{idx+1}", font_size=11, font_family=3, color="#64748B", frame_id=fid)
        s.add_rect(qx, qy, qw, 36.0, bg="#FFF5F2" if qcol=="#D93829" else "#F8FAFC", stroke=qcol, stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(qx + 15, qy + 10, qname, font_size=10, font_family=3, color=qcol, frame_id=fid)
    save_and_export(s, fid, cat, 134, "134_release_planning", "Release Planning", "high", "gantt", ["quarterly_timeline", "releases"])

    # 135. Project Timeline
    s, fid, tw, th = create_base_scene("Executive Project Milestone Timeline", "AGILE & PROYECTOS")
    s.add_line(80, 240, 1360, 240, stroke="#0F172A", stroke_w=2.5, frame_id=fid)
    m_nodes = [("Hito 1 (Ago 01)", "Fase de Diseno", 120, True),
               ("Hito 2 (Ago 10)", "Compilacion Core", 420, False),
               ("Hito 3 (Ago 17)", "Expansion v2 150 Templates", 720, True),
               ("Hito 4 (Ago 25)", "Lanzamiento Produccion", 1020, False)]
    for mdate, mtitle, mx, is_top in m_nodes:
        my = 120 if is_top else 260
        s.add_ellipse(mx + 100, 235, 12, 12, bg="#D93829", stroke="#D93829", frame_id=fid)
        s.add_line(mx + 106, 240, mx + 106, my + (70 if is_top else 0), stroke="#D93829", stroke_w=1.5, frame_id=fid)
        s.add_rect(mx, my, 220, 75, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(mx + 12, my + 10, mdate, font_size=10, font_family=3, color="#D93829", frame_id=fid)
        s.add_text(mx + 12, my + 32, mtitle, font_size=10, font_family=3, color="#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 135, "135_project_timeline", "Project Timeline", "medium", "timeline", ["milestones", "dates"])

    # 136. Gantt Chart
    s, fid, tw, th = create_base_scene("Work Breakdown Gantt Chart with Dependencies", "AGILE & PROYECTOS")
    s.add_rect(40, 80, 1360, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_line(80, 130, 1320, 130, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    tasks = [
        ("1. Diseno de Constructores Modulares", 140, 250, "#059669"),
        ("2. Generacion de 150 Plantillas", 410, 380, "#D93829"),
        ("3. Auditoria de Calidad y Cero Emojis", 810, 220, "#0284C7"),
        ("4. Despliegue en GitHub y CI", 1050, 220, "#D97706")
    ]
    for idx, (tname, tx, tw_b, tcol) in enumerate(tasks):
        ty = 150 + idx * 60
        s.add_text(80, ty + 12, f"Tarea #{idx+1}", font_size=11, font_family=3, color="#64748B", frame_id=fid)
        s.add_rect(tx, ty, tw_b, 36.0, bg="#FFF5F2" if tcol=="#D93829" else "#F8FAFC", stroke=tcol, stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(tx + 15, ty + 10, tname, font_size=10, font_family=3, color=tcol, frame_id=fid)
    save_and_export(s, fid, cat, 136, "136_gantt_chart", "Gantt Chart", "high", "gantt_detailed", ["tasks", "bars", "dependencies"])

    # 137. Project Dependency Map
    s, fid, tw, th = create_base_scene("Critical Path & Task Dependency Graph", "AGILE & PROYECTOS")
    s.add_quad_card(40, 180, 220, 90, "Diseno de Arquitectura", "Paso Inicial", is_hero=True, frame_id=fid)
    s.add_arrow(260, 225, 360, 140, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(260, 225, 360, 310, stroke="#94A3B8", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(360, 100, 260, 90, "Backend API & Engine", "Ruta Critica", is_hero=True, frame_id=fid)
    s.add_quad_card(360, 270, 260, 90, "Frontend UI / Extension", "Desarrollo Paralelo", frame_id=fid)
    s.add_arrow(620, 145, 720, 225, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(620, 315, 720, 225, stroke="#94A3B8", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(720, 180, 260, 90, "Auditoria QA & CI", "Pruebas de Regresion", is_hero=True, frame_id=fid)
    s.add_arrow(980, 225, 1080, 225, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_quad_card(1080, 180, 240, 90, "Despliegue a Prod", "Release Final GA", is_hero=True, frame_id=fid)
    save_and_export(s, fid, cat, 137, "137_project_dependency_map", "Project Dependency Map", "high", "critical_path", ["task_nodes", "dependencies"])

    # 138. Project Status Dashboard (4 RAG Semaphores)
    s, fid, tw, th = create_base_scene("Project Health & Status Dashboard (RAG Semaphore)", "AGILE & PROYECTOS")
    rag_cards = [
        ("PRESUPUESTO (BUDGET)", "EN VERDE (ON TRACK)", "Desviacion: 0% · Consumo: $0", "#059669", False),
        ("CRONOGRAMA (SCHEDULE)", "EN VERDE (ON TRACK)", "150/150 plantillas generadas a tiempo", "#059669", True),
        ("CALIDAD & TESTS (QUALITY)", "EN VERDE (EXCELENTE)", "27/27 PASS · VCS: 99.50 / 100", "#059669", False),
        ("RIESGOS GLOBALES (RISKS)", "BAJO (MITIGADO)", "0 bloqueos activos · Cero emojis", "#059669", False)
    ]
    for i, (rt, rv, rd, rc, is_h) in enumerate(rag_cards):
        rx = 40 + i * 345
        s.add_rect(rx, 100, 330, 280, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8, roundness_type=3, frame_id=fid)
        s.add_text(rx + 20, 130, rt, font_size=11, font_family=3, color="#D93829" if is_h else "#64748B", frame_id=fid)
        s.add_text(rx + 20, 180, rv, font_size=16, font_family=3, color=rc, frame_id=fid)
        s.add_text(rx + 20, 250, rd, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 138, "138_project_status_dashboard", "Project Status Dashboard", "medium", "rag_dashboard", ["budget", "schedule", "quality", "risks"])

    # 139. RAID Log (4 Columns)
    s, fid, tw, th = create_base_scene("RAID Log (Risks, Assumptions, Issues, Dependencies)", "AGILE & PROYECTOS")
    raid_cols = [("1. RISKS (RIESGOS)", ["Curvas Bezier en SVG", "Compatibilidad en navegadores"], 40, False),
                 ("2. ASSUMPTIONS (SUPUESTOS)", ["Usuarios valoran 0 emojis", "Python 3.10+ disponible"], 390, False),
                 ("3. ISSUES (PROBLEMAS)", ["Solapamiento inicial resuelto", "Todos los tests aprobados"], 740, True),
                 ("4. DEPENDENCIES (DEPENDENCIAS)", ["Tipografia Inter disponible", "Modulo ElementTree nativo"], 1090, False)]
    for rtitle, ritems, rx, is_h in raid_cols:
        s.add_rect(rx, 80, 310, 350, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(rx + 15, 105, rtitle, font_size=11, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        for ii, itxt in enumerate(ritems):
            s.add_rect(rx + 12, 145 + ii * 85, 285, 70, bg="#FFFFFF" if is_h else "#F8FAFC", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=fid)
            s.add_text(rx + 20, 165 + ii * 85, itxt, font_size=10, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 139, "139_raid_log", "RAID Log", "medium", "columns_4", ["risks", "assumptions", "issues", "dependencies"])

    # 140. RACI Matrix
    s, fid, tw, th = create_base_scene("RACI Responsibility Assignment Matrix", "AGILE & PROYECTOS")
    r_heads = ["ENTREGABLE / TAREA", "PRODUCT MANAGER", "LEAD ARCHITECT", "DEV ENGINEER", "QA LEAD"]
    r_xs = [40, 360, 620, 880, 1140]
    for rh, rx in zip(r_heads, r_xs):
        s.add_text(rx, 85, rh, font_size=11, font_family=3, color="#64748B", frame_id=fid)
    r_rows = [
        ("Definicion de 212 Plantillas", "A (Accountable)", "R (Responsible)", "C (Consulted)", "I (Informed)"),
        ("Desarrollo de Constructores", "I (Informed)", "A (Accountable)", "R (Responsible)", "C (Consulted)"),
        ("Auditoria de Calidad CI", "I (Informed)", "C (Consulted)", "C (Consulted)", "A / R (Resp/Acc)")
    ]
    for idx, r in enumerate(r_rows):
        ry = 130 + idx * 85
        s.add_rect(30, ry, tw - 60, 70, bg="#FFF5F2" if idx==0 else "#FFFFFF", stroke="#D93829" if idx==0 else "#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        for val, rx in zip(r, r_xs):
            s.add_text(rx, ry + 25, val, font_size=11, font_family=3, color="#D93829" if idx==0 and rx==r_xs[0] else "#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 140, "140_raci_matrix", "RACI Matrix", "high", "matrix_table", ["roles", "raci_codes"])
