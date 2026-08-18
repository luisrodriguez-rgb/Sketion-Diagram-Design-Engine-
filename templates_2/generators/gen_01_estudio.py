"""
Generador de Categoría 01: Estudio y Educación (20 Plantillas)
"""

from .common import create_base_scene, save_and_export

def generate():
    print("\n--- Generando 01: Estudio y Educación (20 plantillas) ---")
    cat = "01_estudio_educacion"

    # 01. Study Planner
    s, fid, tw, th = create_base_scene("Study Planner & Goal Timeboxing", "ESTUDIO")
    days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
    for i, d in enumerate(days):
        dx = 40 + i * 230
        s.add_rect(dx, 80, 215, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(dx + 15, 105, d.upper(), font_size=12, font_family=3, color="#D93829" if i==0 else "#0F172A", frame_id=fid)
        s.add_quad_card(dx + 10, 140, 195, 75, "Bloque 1 (2h)", "Matematicas / Calculo", is_hero=(i==0), frame_id=fid)
        s.add_quad_card(dx + 10, 230, 195, 75, "Bloque 2 (1.5h)", "Estructuras de Datos", frame_id=fid)
    save_and_export(s, fid, cat, 1, "01_study_planner", "Study Planner", "medium", "columns", ["cards", "timebox"])

    # 02. Subject Dashboard
    s, fid, tw, th = create_base_scene("Subject Academic Dashboard", "ESTUDIO")
    s.add_rect(40, 80, 420, 350, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "ASIGNATURA: SISTEMAS DISTRIBUIDOS", font_size=13, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 145, "Profesor: Dr. Arboleda\nCreditos: 4 · Calificacion: 4.8/5.0\nHorario: Mar / Jue 14:00 - 16:00\nAula: Lab 302 / Virtual", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(480, 80, 440, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(500, 105, "HITOS & EVALUACIONES", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(500, 145, "* Parcial 1 (25%): 15 de Septiembre\n* Taller Raft / Paxos (20%): 02 de Octubre\n* Parcial 2 (25%): 28 de Octubre\n* Proyecto Final (30%): 20 de Noviembre", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(940, 80, 460, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(960, 105, "BIBLIOGRAFIA & RECURSOS", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(960, 145, "1. Designing Data-Intensive Applications\n2. Distributed Systems: Principles & Paradigms\n3. Papers: Google Spanner, Raft Consensus", font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 2, "02_subject_dashboard", "Subject Dashboard", "low", "grid", ["cards", "kpi"])

    # 03. Course Map
    s, fid, tw, th = create_base_scene("Course Syllabus & Module Progression Map", "ESTUDIO")
    modules = ["Mod 1: Concurrencia", "Mod 2: Consenso", "Mod 3: Replicacion", "Mod 4: Transacciones", "Mod 5: Particion"]
    for i, m in enumerate(modules):
        mx = 40 + i * 275
        s.add_quad_card(mx, 160, 260, 120, m, f"Semanas {i*3+1}-{i*3+3}\n3 Laboratorios", badge=f"NIVEL {i+1}", is_hero=(i==1), frame_id=fid)
        if i < len(modules) - 1:
            s.add_arrow(mx + 260, 220, mx + 275, 220, stroke="#D93829" if i==1 else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 3, "03_course_map", "Course Map", "medium", "horizontal_flow", ["nodes", "connectors"])

    # 04. Chapter Summary
    s, fid, tw, th = create_base_scene("Structured Chapter Summary", "ESTUDIO")
    s.add_rect(40, 80, 420, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "CONCEPTOS CLAVE DEL CAPITULO", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 145, "Capitulo 5: Replicacion Lider-Seguidor\n* Replicacion sincronica vs asincronica\n* Manejo de fallos de nodos (Failover)\n* Problemas de retardo de replicacion\n* Lectura de escrituras propias", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(480, 80, 440, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(500, 105, "ECUACIONES & MODELOS", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(500, 145, "Quorum: w + r > n\nDonde:\n n = numero de replicas\n w = nodos necesarios para confirmar escritura\n r = nodos necesarios para confirmar lectura", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(940, 80, 460, 350, bg="#FFF5F2", stroke="#D93829", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(960, 105, "PREGUNTAS DE AUTOEVALUACION", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(960, 145, "1. Que ocurre si el lider falla durante un failover?\n2. Como se previene el problema de Split-Brain?\n3. Cual es el trade-off entre w=1 y w=all?", font_size=11, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 4, "04_chapter_summary", "Chapter Summary", "low", "grid", ["cards", "text"])

    # 05. Book Analysis (Custom 4-Panel Literary Map)
    s, fid, tw, th = create_base_scene("Critical Literature & Book Analysis Matrix", "ESTUDIO")
    s.add_rect(40, 80, 320, 350, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "FICHA TECNICA & SINOPSIS", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 145, "Obra: El Principito\nAutor: Antoine de Saint-Exupéry\nPublicacion: 1943\nGenero: Novela filosofica\n\nTesis: Lo esencial es invisible a los ojos.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(380, 80, 340, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(400, 105, "MAPA DE PERSONAJES", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(400, 145, "* Protagonista: El Principito\n* Mentor: El Zorro (domesticacion)\n* Conflicto: La Rosa (ego y cuidado)\n* Espejo Adulto: El Rey, El Vanidoso", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(740, 80, 340, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "ARCO NARRATIVO & TENSION", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(760, 145, "1. Inicio: Caida en el Sahara\n2. Desarrollo: Viaje interplanetario\n3. Climax: Encuentro con el zorro\n4. Desenlace: Despedida en el desierto", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(1100, 80, 310, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(1120, 105, "TEMAS & CITAS CRITICAS", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(1120, 145, "'Eres responsable para siempre de lo que has domesticado.'\n\nTemas: La soledad, la amistad, el absurdo del mundo adulto.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 5, "05_book_analysis", "Book Analysis", "medium", "panels_4", ["literary_metadata", "character_map", "themes"])

    # 06. Article Analysis
    s, fid, tw, th = create_base_scene("Academic Research Paper Analysis", "ESTUDIO")
    a_panels = [
        ("1. OBJETIVO & HIPOTESIS", "Evaluar el impacto de la indexacion HNSW en bases de datos vectoriales a gran escala.", 40, False),
        ("2. METODOLOGIA", "Pruebas de carga sobre 1M de vectores con metricas de recall@10 y latencia P99.", 390, False),
        ("3. RESULTADOS CLAVE", "Recall del 98.4% con latencia inferior a 4.2ms en clusters distribuidos.", 740, True),
        ("4. LIMITACIONES & CONCLUSIONES", "Alto consumo de memoria RAM; se recomienda cuantizacion escalar PQ.", 1090, False)
    ]
    for pt, pd, px, is_h in a_panels:
        s.add_rect(px, 100, 320, 320, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(px + 15, 125, pt, font_size=11, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(px + 15, 175, pd, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 6, "06_article_analysis", "Article Analysis", "medium", "columns_4", ["abstract", "methodology", "findings"])

    # 07. Thesis Statement Builder
    s, fid, tw, th = create_base_scene("Thesis Statement & Argument Formulation Builder", "ESTUDIO")
    t_blocks = [
        ("1. TEMA GENERAL", "Sistemas de almacenamiento distribuido", 40, False),
        ("2. PREGUNTA CLAVE", "¿Como garantizar consistencia con minima latencia?", 390, False),
        ("3. POSTURA / TESIS", "El uso de quorums dinamicos reduce la latencia P99 un 35%.", 740, True),
        ("4. EVIDENCIA / JUSTIFICACION", "Benchmarks experimentales sobre redes WAN.", 1090, False)
    ]
    for bt, bd, bx, is_h in t_blocks:
        s.add_quad_card(bx, 140, 310, 150, bt, bd, badge="TESIS", is_hero=is_h, frame_id=fid)
        if bx < 1090:
            s.add_arrow(bx + 310, 215, bx + 350, 215, stroke="#D93829" if is_h else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 7, "07_thesis_statement_builder", "Thesis Statement Builder", "medium", "horizontal_flow", ["nodes", "connectors"])

    # 08. Argument Map
    s, fid, tw, th = create_base_scene("Argument Structure Map (Premises -> Conclusion)", "ESTUDIO")
    s.add_quad_card(600, 70, 260, 80, "CONCLUSION PRINCIPAL", "La arquitectura Hexagonal es superior", is_hero=True, frame_id=fid)
    s.add_quad_card(250, 230, 260, 90, "Premisa 1 (Testabilidad)", "Permite mockear DB sin esfuerzo", frame_id=fid)
    s.add_quad_card(600, 230, 260, 90, "Premisa 2 (Mantenibilidad)", "Aisla reglas de negocio de frameworks", frame_id=fid)
    s.add_quad_card(950, 230, 260, 90, "Premisa 3 (Longevidad)", "Facilita migraciones tecnologicas", frame_id=fid)
    s.add_arrow(380, 230, 680, 150, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(730, 230, 730, 150, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    s.add_arrow(1080, 230, 780, 150, stroke="#D93829", stroke_w=1.5, frame_id=fid)
    save_and_export(s, fid, cat, 8, "08_argument_map", "Argument Map", "medium", "hierarchical_tree", ["nodes", "connectors"])

    # 09. Debate Map
    s, fid, tw, th = create_base_scene("Debate & Controversy Map (Pros vs Cons)", "ESTUDIO")
    s.add_rect(40, 80, 660, 350, bg="#F0FDF4", stroke="#86EFAC", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "ARGUMENTOS A FAVOR (PROS)", font_size=13, font_family=3, color="#166534", frame_id=fid)
    s.add_text(60, 145, "[+] Alta velocidad de iteracion y despliegue continuo.\n[+] Menor acoplamiento entre equipos de ingenieria.\n[+] Escalabilidad horizontal independiente por servicio.\n[+] Resiliencia ante fallos parciales del sistema.", font_size=11, font_family=3, color="#15803D", frame_id=fid)
    s.add_rect(740, 80, 660, 350, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "ARGUMENTOS EN CONTRA (CONTRAS)", font_size=13, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(760, 145, "[-] Mayor complejidad operativa en observabilidad y trazas.\n[-] Overhead de red y latencia de serializacion.\n[-] Dificultad para mantener consistencia transaccional (Saga).\n[-] Costos de infraestructura elevados en fases tempranas.", font_size=11, font_family=3, color="#991B1B", frame_id=fid)
    save_and_export(s, fid, cat, 9, "09_debate_map", "Debate Map", "medium", "split_debate", ["pros", "cons"])

    # 10. Comparison Study (Triple Venn)
    s, fid, tw, th = create_base_scene("Comparative Concept Analysis (Triple Intersection)", "ESTUDIO")
    s.add_ellipse(350, 100, 340, 340, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_text(370, 160, "CONCEPTO A\n(Consistencia CP)", font_size=11, font_family=3, color="#D93829", frame_id=fid)
    s.add_ellipse(650, 100, 340, 340, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.8, frame_id=fid)
    s.add_text(850, 160, "CONCEPTO B\n(Disponibilidad AP)", font_size=11, font_family=3, color="#2563EB", frame_id=fid)
    s.add_ellipse(500, 220, 340, 240, bg="#F8FAFC", stroke="#0F172A", stroke_w=1.8, frame_id=fid)
    s.add_text(600, 370, "CONCEPTO C (Tolerancia a Particion)", font_size=11, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(620, 250, "ZONA DE EQUILIBRIO", font_size=10, font_family=3, color="#D93829", frame_id=fid)
    save_and_export(s, fid, cat, 10, "10_comparison_study", "Comparison Study", "high", "venn_triple", ["circles", "intersections"])

    # 11. Timeline Study
    s, fid, tw, th = create_base_scene("Historical & Sequential Timeline Study", "ESTUDIO")
    s.add_line(80, 240, 1360, 240, stroke="#0F172A", stroke_w=2.5, frame_id=fid)
    t_milestones = [("1970", "Modelo Relacional", "Codd publica paper formal", 120, True), ("1989", "World Wide Web", "Berners-Lee crea HTTP", 420, False), ("2006", "Cloud Computing", "Lanzamiento de AWS EC2/S3", 720, True), ("2017", "Transformers", "Attention is All You Need", 1020, False)]
    for myear, mtitle, mdesc, mx, is_top in t_milestones:
        my = 120 if is_top else 260
        s.add_ellipse(mx + 100, 235, 12, 12, bg="#D93829", stroke="#D93829", frame_id=fid)
        s.add_line(mx + 106, 240, mx + 106, my + (70 if is_top else 0), stroke="#D93829", stroke_w=1.5, frame_id=fid)
        s.add_rect(mx, my, 220, 75, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(mx + 12, my + 10, f"{myear} · {mtitle}", font_size=10, font_family=3, color="#D93829", frame_id=fid)
        s.add_text(mx + 12, my + 32, mdesc, font_size=9, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 11, "11_timeline_study", "Timeline Study", "medium", "timeline_axis", ["axis", "milestones"])

    # 12. Formula Sheet
    s, fid, tw, th = create_base_scene("Mathematical Formula & Theorem Reference", "ESTUDIO")
    f_cards = [
        ("LEY DE LITTLE", "L = lambda * W\nL: Clientes en sistema\nlambda: Tasa de llegada\nW: Tiempo promedio", 40, 80, 420, 160, True),
        ("LEY DE AMDAHL", "S_latency(s) = 1 / ((1 - p) + p / s)\np: Proporcion paralelizable\ns: Factor de aceleracion", 480, 80, 440, 160, False),
        ("TEOREMA DE BAYES", "P(A|B) = [P(B|A) * P(A)] / P(B)\nProbabilidad a posteriori dada\nnueva evidencia.", 940, 80, 460, 160, False),
        ("COMPLEJIDAD BIG-O", "O(1) < O(log n) < O(n) < O(n log n)\n< O(n^2) < O(2^n) < O(n!)", 40, 260, 660, 160, False),
        ("ENTROPIA DE SHANNON", "H(X) = - SUM [ P(x_i) * log_2 P(x_i) ]\nMedida de incertidumbre de datos.", 720, 260, 680, 160, False)
    ]
    for ft, fd, fx, fy, fw, fh, is_h in f_cards:
        s.add_rect(fx, fy, fw, fh, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(fx + 20, fy + 20, ft, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(fx + 20, fy + 60, fd, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 12, "12_formula_sheet", "Formula Sheet", "medium", "grid", ["cards", "math"])

    # 13. Problem Solving Board
    s, fid, tw, th = create_base_scene("Step-by-Step Problem Solving Board", "ESTUDIO")
    p_steps = ["1. Comprender el Enunciado", "2. Identificar Restricciones", "3. Proponer Algoritmo", "4. Implementar & Verificar", "5. Calcular Complejidad"]
    for i, ps in enumerate(p_steps):
        px = 40 + i * 275
        s.add_quad_card(px, 140, 260, 150, ps, "Notas de resolucion y pruebas", badge=f"PASO {i+1}", is_hero=(i==2), frame_id=fid)
        if i < len(p_steps) - 1:
            s.add_arrow(px + 260, 215, px + 275, 215, stroke="#D93829" if i==2 else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 13, "13_problem_solving_board", "Problem Solving Board", "medium", "horizontal_flow", ["nodes", "connectors"])

    # 14. Question Bank (Stratified Shelves)
    s, fid, tw, th = create_base_scene("Stratified Academic Question Bank", "ESTUDIO")
    tiers = [("NIVEL 1: CONCEPTUAL (FACIL)", ["Definir consistencia eventual.", "Explicar el modelo ACID vs BASE."], 40, False),
             ("NIVEL 2: APLICADO (MEDIO)", ["Calcular quorum con n=5 replicas.", "Diseñar particionamiento por hash."], 500, True),
             ("NIVEL 3: ARQUITECTURA (AVANZADO)", ["Mitigar problemas de split-brain en Raft.", "Optimizar garbage collection en RocksDB."], 960, False)]
    for tt, tqs, tx, is_h in tiers:
        s.add_rect(tx, 80, 440, 350, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(tx + 20, 105, tt, font_size=11, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        for qi, qtxt in enumerate(tqs):
            s.add_rect(tx + 15, 145 + qi * 85, 410, 70, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=fid)
            s.add_text(tx + 25, 165 + qi * 85, f"Q{qi+1}: {qtxt}", font_size=10, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 14, "14_question_bank", "Question Bank", "medium", "columns_3", ["shelves", "questions"])

    # 15. Exam Question Matrix
    s, fid, tw, th = create_base_scene("Exam Question & Taxonomy Matrix (Bloom Level vs Topic)", "ESTUDIO")
    headers = ["TEMA / BLOQUE", "RECORDAR (L1)", "COMPRENDER (L2)", "APLICAR (L3)", "ANALIZAR (L4)"]
    h_xs = [40, 320, 580, 840, 1100]
    for h_txt, hx in zip(headers, h_xs):
        s.add_text(hx, 85, h_txt, font_size=11, font_family=3, color="#64748B", frame_id=fid)
    rows = [
        ("Sistemas Distribuidos", "Definir RPC", "Explicar Paxos", "Implementar Raft", "Depurar Redes WAN"),
        ("Bases de Datos", "Listar indices", "Diferenciar B-Tree", "Optimizar queries", "Analizar Lock Contention"),
        ("Seguridad Cloud", "Conocer TLS", "Flujo OAuth 2.0", "Configurar mTLS", "Modelar Amenazas STRIDE")
    ]
    for r_idx, r_data in enumerate(rows):
        ry = 130 + r_idx * 85
        s.add_rect(30, ry, tw - 60, 70, bg="#FFF5F2" if r_idx==0 else "#FFFFFF", stroke="#D93829" if r_idx==0 else "#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        for c_val, hx in zip(r_data, h_xs):
            s.add_text(hx, ry + 25, c_val, font_size=11, font_family=3, color="#D93829" if r_idx==0 and hx==h_xs[0] else "#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 15, "15_exam_question_matrix", "Exam Question Matrix", "high", "matrix_table", ["table", "taxonomy"])

    # 16. Spaced Repetition Board
    s, fid, tw, th = create_base_scene("Spaced Repetition (Leitner Interval Boxes)", "ESTUDIO")
    boxes = ["Caja 1: Diario", "Caja 2: Cada 3 Dias", "Caja 3: Semanal", "Caja 4: Quincenal", "Caja 5: Mensual (Dominado)"]
    for i, b in enumerate(boxes):
        bx = 40 + i * 275
        s.add_quad_card(bx, 140, 260, 150, b, f"Capacidad: {20*(5-i)} Tarjetas\nRetencion: {60 + i*8}%", badge=f"BOX {i+1}", is_hero=(i==4), frame_id=fid)
    save_and_export(s, fid, cat, 16, "16_spaced_repetition_board", "Spaced Repetition Board", "medium", "columns", ["cards", "intervals"])

    # 17. Learning Progress Tracker (Radar Spider)
    s, fid, tw, th = create_base_scene("Skill Mastery & Learning Progress Tracker", "ESTUDIO")
    s.add_radar_chart(725, 240, 140.0, ["Algoritmos", "Sistemas", "Bases de Datos", "Redes", "Seguridad", "DevOps"], [0.90, 0.85, 0.75, 0.65, 0.80, 0.70], frame_id=fid)
    save_and_export(s, fid, cat, 17, "17_learning_progress_tracker", "Learning Progress Tracker", "high", "radar_spider", ["polar_polygon", "axes"])

    # 18. Concept Dependency Map (DAG Graph)
    s, fid, tw, th = create_base_scene("Concept Dependency & Prerequisite Graph", "ESTUDIO")
    s.add_quad_card(40, 180, 220, 80, "Calculo Diferencial", "Prerrequisito Base", is_hero=True, frame_id=fid)
    s.add_arrow(260, 220, 360, 140, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(260, 220, 360, 300, stroke="#94A3B8", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(360, 100, 240, 80, "Calculo Multivariable", "Derivadas Parciales", frame_id=fid)
    s.add_quad_card(360, 260, 240, 80, "Algebra Lineal", "Matrices y Vectores", frame_id=fid)
    s.add_arrow(600, 140, 700, 220, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_arrow(600, 300, 700, 220, stroke="#94A3B8", stroke_w=1.5, frame_id=fid)
    s.add_quad_card(700, 180, 260, 80, "Machine Learning", "Descenso de Gradiente", is_hero=True, frame_id=fid)
    s.add_arrow(960, 220, 1060, 220, stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_quad_card(1060, 180, 260, 80, "Deep Learning & LLMs", "Redes Neuronales", is_hero=True, frame_id=fid)
    save_and_export(s, fid, cat, 18, "18_concept_dependency_map", "Concept Dependency Map", "high", "dag_graph", ["nodes", "dependencies"])

    # 19. Lab Report Canvas
    s, fid, tw, th = create_base_scene("Standard Laboratory Report Canvas", "ESTUDIO")
    l_sec = [
        ("1. OBJETIVO DEL EXPERIMENTO", "Validar el comportamiento termico del disipador.", 40, 80, 420, 160, False),
        ("2. EQUIPOS & MATERIALES", "Termocupla tipo K, osciloscopio, carga electronica.", 480, 80, 440, 160, False),
        ("3. DATOS RECOLECTADOS", "Tabla de temperatura vs corriente (0 a 10A).", 940, 80, 460, 160, True),
        ("4. ANALISIS & DISCUSION", "La resistencia termica concuerda con el modelo FEM (error < 4%).", 40, 260, 660, 160, False),
        ("5. CONCLUSIONES", "El disipador cumple los estandares de seguridad para 85°C maximo.", 720, 260, 680, 160, False)
    ]
    for lt, ld, lx, ly, lw, lh, is_h in l_sec:
        s.add_rect(lx, ly, lw, lh, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(lx + 20, ly + 20, lt, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(lx + 20, ly + 60, ld, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 19, "19_lab_report_canvas", "Lab Report Canvas", "medium", "grid", ["canvas_blocks", "text"])

    # 20. Academic Project Canvas (Custom 6-Block Capstone Canvas)
    s, fid, tw, th = create_base_scene("Academic Capstone & Project Canvas", "ESTUDIO")
    c_blocks = [
        ("1. PREGUNTA DE INVESTIGACION", "¿Como optimizar la recuperacion ante desastres en bases distribuidas?", 40, 80, 440, 160, True),
        ("2. METODOLOGIA PROPUESTA", "Pruebas de inyeccion de fallos (Chaos Engineering) sobre clusters Kubernetes.", 500, 80, 440, 160, False),
        ("3. IMPACTO & RELEVANCIA", "Reduccion del RTO (Recovery Time Objective) de 12 minutos a menos de 45 segundos.", 960, 80, 440, 160, False),
        ("4. HITOS & ENTREGABLES", "• Paper formal IEEE\n• Repositorio con benchmarks reproducibles\n• Defensa de tesis ante jurado", 40, 260, 660, 160, False),
        ("5. RECURSOS & TUTORES", "Director: Dr. Martinez · Laboratorio de Computacion de Alto Rendimiento · Becas de computo cloud", 720, 260, 680, 160, False)
    ]
    for ct, cd, cx, cy, cw, ch, is_h in c_blocks:
        s.add_rect(cx, cy, cw, ch, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(cx + 20, cy + 20, ct, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(cx + 20, cy + 60, cd, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 20, "20_academic_project_canvas", "Academic Project Canvas", "medium", "capstone_grid", ["research_question", "deliverables"])
