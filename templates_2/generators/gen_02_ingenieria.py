"""
Generador de Categoría 02: Ingeniería Industrial y Procesos (20 Plantillas)
"""

from .common import create_base_scene, save_and_export

def generate():
    print("\n--- Generando 02: Ingeniería Industrial y Procesos (20 plantillas) ---")
    cat = "02_ingenieria_procesos"

    # 21. Value Added Flow Analysis
    s, fid, tw, th = create_base_scene("Value Added vs Waste (VA / NNVA / NVA) Analysis", "INGENIERÍA")
    v_cols = [
        ("VALOR ANADIDO (VA)", "Actividades que transforman el producto y el cliente paga por ellas:\n• Mecanizado CNC\n• Soldadura robotizada\n• Ensamble final", 40, "#059669"),
        ("NO VALOR NECESARIO (NNVA)", "Inspecciones regulatorias y calibracion obligatoria:\n• Calibracion de torquimetros\n• Auditoria ISO 9001\n• Ensayos no destructivos", 500, "#D97706"),
        ("DESPERDICIO PURO (NVA)", "Muda / Perdidas que deben ser eliminadas:\n• Esperas por material\n• Sobreproduccion en lote\n• Retrabajo por defectos", 960, "#D93829")
    ]
    for vt, vd, vx, vc in v_cols:
        s.add_rect(vx, 80, 440, 350, bg="#FFFFFF", stroke=vc, stroke_w=1.8, roundness_type=3, frame_id=fid)
        s.add_text(vx + 20, 105, vt, font_size=12, font_family=3, color=vc, frame_id=fid)
        s.add_text(vx + 20, 150, vd, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 21, "21_value_added_flow_analysis", "Value Added Flow Analysis", "high", "columns", ["value_stream", "waste"])

    # 22. Swimlane Process Map (4 Functional Lanes)
    s, fid, tw, th = create_base_scene("Multi-Role Swimlane Operational Process Map", "INGENIERÍA")
    lanes = ["1. Planificacion", "2. Fabricacion", "3. Ensamble", "4. Control Calidad"]
    for i, lane_title in enumerate(lanes):
        ly = 80 + i * 85
        s.add_rect(40, ly, tw - 80, 75, bg="#F8FAFC" if i%2==0 else "#FFFFFF", stroke="#CBD5E1", stroke_w=1.2, roundness_type=3, frame_id=fid)
        s.add_text(55, ly + 28, lane_title.upper(), font_size=10, font_family=3, color="#64748B", frame_id=fid)
        s.add_quad_card(240 + i * 260, ly + 8, 230, 58, f"Operacion #{i+1}", f"Paso clave en {lane_title}", is_hero=(i==1), frame_id=fid)
        if i < 3:
            s.add_arrow(470 + i * 260, ly + 37, 500 + i * 260, ly + 115, stroke="#D93829" if i==1 else "#94A3B8", stroke_w=1.5, frame_id=fid)
    save_and_export(s, fid, cat, 22, "22_swimlane_process_map", "Swimlane Process Map", "high", "swimlane_4", ["lanes", "flow_nodes"])

    # 23. Decision Analysis Tree
    s, fid, tw, th = create_base_scene("Decision Analysis Tree (Outcomes, Payoffs & Risks)", "INGENIERÍA")
    s.add_quad_card(40, 180, 220, 100, "DECISION RAIZ", "Elegir Proveedor", is_hero=True, frame_id=fid)
    s.add_arrow(260, 230, 360, 130, stroke="#D93829", frame_id=fid)
    s.add_arrow(260, 230, 360, 330, stroke="#94A3B8", frame_id=fid)
    s.add_quad_card(360, 80, 280, 100, "Opcion A: Local", "Costo Alto, Riesgo Bajo", frame_id=fid)
    s.add_quad_card(360, 280, 280, 100, "Opcion B: Internacional", "Costo Bajo, Riesgo Alto", frame_id=fid)
    s.add_arrow(640, 130, 740, 130, stroke="#94A3B8", frame_id=fid)
    s.add_arrow(640, 330, 740, 330, stroke="#94A3B8", frame_id=fid)
    s.add_quad_card(740, 80, 300, 100, "Resultado: Margen 22%", "Lead Time: 2 dias", frame_id=fid)
    s.add_quad_card(740, 280, 300, 100, "Resultado: Margen 38%", "Lead Time: 24 dias", frame_id=fid)
    save_and_export(s, fid, cat, 23, "23_decision_analysis_tree", "Decision Analysis Tree", "high", "decision_tree", ["nodes", "branches"])

    # 24. Process Analysis Matrix
    s, fid, tw, th = create_base_scene("Operational Process Parameter & KPI Matrix", "INGENIERÍA")
    p_heads = ["OPERACION", "CYCLE TIME", "SETUP TIME", "DEFECTOS (PPM)", "CAPACIDAD (CPK)"]
    p_xs = [40, 340, 600, 860, 1120]
    for ph, px in zip(p_heads, p_xs):
        s.add_text(px, 85, ph, font_size=11, font_family=3, color="#64748B", frame_id=fid)
    p_rows = [
        ("Corte Laser Chapa", "14.2 s", "8.0 min", "45 PPM", "1.65 (Excelente)"),
        ("Plegado CNC", "28.5 s", "15.0 min", "120 PPM", "1.33 (Aceptable)"),
        ("Soldadura Robotica", "45.0 s", "22.0 min", "80 PPM", "1.42 (Optimo)"),
        ("Pintura Electrostatica", "60.0 s", "35.0 min", "210 PPM", "1.18 (Alerta)")
    ]
    for idx, r in enumerate(p_rows):
        ry = 130 + idx * 75
        s.add_rect(30, ry, tw - 60, 65, bg="#FFF5F2" if idx==2 else "#FFFFFF", stroke="#D93829" if idx==2 else "#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        for val, px in zip(r, p_xs):
            s.add_text(px, ry + 22, val, font_size=11, font_family=3, color="#D93829" if idx==2 and px==p_xs[0] else "#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 24, "24_process_analysis_matrix", "Process Analysis Matrix", "medium", "matrix_table", ["table", "cells"])

    # 25. Spaghetti Diagram (Plant Layout)
    s, fid, tw, th = create_base_scene("Plant Floor Layout & Spaghetti Movement Diagram", "INGENIERÍA")
    stations = [("Almacen MP", 60, 100), ("Corte Laser", 360, 100), ("Plegado CNC", 700, 100), ("Soldadura", 1040, 100),
                ("Pintura", 1040, 280), ("Ensamble", 700, 280), ("Inspeccion", 360, 280), ("Almacen PT", 60, 280)]
    for s_name, sx, sy in stations:
        s.add_rect(sx, sy, 220, 90, bg="#FFFFFF", stroke="#0F172A", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(sx + 15, sy + 35, s_name, font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    # Spaghetti trajectories
    traj = [(280, 145, 360, 145), (580, 145, 700, 145), (920, 145, 1040, 145), (1150, 190, 1150, 280), (1040, 325, 920, 325), (700, 325, 580, 325), (360, 325, 280, 325)]
    for x1, y1, x2, y2 in traj:
        s.add_arrow(x1, y1, x2, y2, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    save_and_export(s, fid, cat, 25, "25_spaghetti_diagram", "Spaghetti Diagram", "high", "layout_map", ["zones", "trajectories"])

    # 26. Takt Time Analysis
    s, fid, tw, th = create_base_scene("Takt Time vs Available Production Time Analysis", "INGENIERÍA")
    s.add_rect(40, 80, 1360, 100, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "FORMULA DE TAKT TIME = Tiempo Disponible de Trabajo / Demanda del Cliente", font_size=13, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 140, "Tiempo Disponible: 28.800 s/turno (8h) · Demanda: 480 unidades/turno · TAKT TIME: 60.0 SEGUNDOS / UNIDAD", font_size=11, font_family=3, color="#334155", frame_id=fid)
    t_stations = [("Estacion 1 (Corte)", 48, False), ("Estacion 2 (Plegado)", 62, True), ("Estacion 3 (Soldadura)", 55, False), ("Estacion 4 (Ensamble)", 42, False)]
    for i, (st, sec, is_ov) in enumerate(t_stations):
        sx = 40 + i * 345
        s.add_quad_card(sx, 200, 330, 180, st, f"Cycle Time: {sec} s\nTakt Target: 60 s\nEstado: {'EXCEDE TAKT TIME' if is_ov else 'BALANCEADO'}", badge="ESTACION", is_hero=is_ov, frame_id=fid)
    save_and_export(s, fid, cat, 26, "26_takt_time_analysis", "Takt Time Analysis", "medium", "cards_metrics", ["metrics", "thresholds"])

    # 27. Cycle Time Analysis
    s, fid, tw, th = create_base_scene("Cycle Time Breakdown & Variance Analysis", "INGENIERÍA")
    s.add_rect(40, 80, 1360, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_line(80, 360, 1340, 360, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    s.add_line(80, 120, 80, 360, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    s.add_line(80, 200, 1340, 200, stroke="#D93829", stroke_w=1.5, dashed=True, frame_id=fid)
    s.add_text(1200, 180, "LCS = 65s", font_size=11, font_family=3, color="#D93829", frame_id=fid)
    stations_ct = [("Op 10", 45, 140), ("Op 20", 52, 340), ("Op 30", 68, 540), ("Op 40", 41, 740), ("Op 50", 58, 940), ("Op 60", 49, 1140)]
    for st_name, ct_val, bar_x in stations_ct:
        bar_h = ct_val * 3.0
        bar_y = 360 - bar_h
        is_over = ct_val > 60
        s.add_rect(bar_x, bar_y, 80, bar_h, bg="#FFF5F2" if is_over else "#EFF6FF", stroke="#D93829" if is_over else "#3B82F6", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(bar_x + 15, bar_y - 20, f"{ct_val}s", font_size=10, font_family=3, color="#D93829" if is_over else "#1D4ED8", frame_id=fid)
        s.add_text(bar_x + 15, 375, st_name, font_size=10, font_family=3, color="#64748B", frame_id=fid)
    save_and_export(s, fid, cat, 27, "27_cycle_time_analysis", "Cycle Time Analysis", "high", "barchart_ct", ["bars", "limits"])

    # 28. Line Balancing
    s, fid, tw, th = create_base_scene("Assembly Line Balancing & Workstation Allocation", "INGENIERÍA")
    s.add_rect(40, 80, 660, 350, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "METRICAS DE BALANCEO DE LINEA", font_size=13, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 145, "• Eficiencia de Linea: 91.4%\n• Tiempo de Ciclo Objetivo: 55.0 segundos\n• Desbalance (Smoothness Index): 4.2%\n• Numero de Operarios Asignados: 6", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "DISTRIBUCION DE CARGA POR ESTACION", font_size=13, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(760, 145, "1. Estacion Chapa: 51s (92% utilizacion)\n2. Estacion CNC: 54s (98% utilizacion)\n3. Estacion Ensamble: 52s (94% utilizacion)\n4. Estacion Test: 48s (87% utilizacion)", font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 28, "28_line_balancing", "Line Balancing", "high", "split_balance", ["efficiency", "workstations"])

    # 29. Bottleneck TOC
    s, fid, tw, th = create_base_scene("Bottleneck Identification (Theory of Constraints)", "INGENIERÍA")
    toc_steps = [("Paso 1: Corte", "40 u/h", False), ("Paso 2: Mecanizado", "25 u/h (CUELLO)", True), ("Paso 3: Pulido", "45 u/h", False), ("Paso 4: Ensamble", "50 u/h", False)]
    for i, (tname, tcap, is_bn) in enumerate(toc_steps):
        tx = 40 + i * 345
        s.add_quad_card(tx, 140, 330, 150, tname, f"Capacidad: {tcap}\nEstado: {'LIMITANTE DEL FLUJO' if is_bn else 'CAPACIDAD EXCEDENTE'}", badge="TOC", is_hero=is_bn, frame_id=fid)
        if i < 3:
            s.add_arrow(tx + 330, 215, tx + 345, 215, stroke="#D93829" if is_bn else "#94A3B8", stroke_w=1.8, frame_id=fid)
    save_and_export(s, fid, cat, 29, "29_bottleneck_analysis", "Bottleneck Analysis", "medium", "horizontal_flow", ["toc_nodes", "constraint"])

    # 30. OEE Dashboard
    s, fid, tw, th = create_base_scene("Overall Equipment Effectiveness (OEE) Dashboard", "INGENIERÍA")
    oee_kpis = [
        ("DISPONIBILIDAD (A)", "92.4%", "Tiempo Operativo / Tiempo Planificado", False),
        ("RENDIMIENTO (P)", "88.1%", "Velocidad Real / Velocidad Estandar", False),
        ("CALIDAD (Q)", "98.7%", "Piezas Buenas / Total Producido", False),
        ("OEE GLOBAL (A x P x Q)", "80.3%", "World Class Benchmark: >= 85%", True)
    ]
    for i, (kt, kv, kd, is_h) in enumerate(oee_kpis):
        kx = 40 + i * 345
        s.add_rect(kx, 100, 330, 280, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8, roundness_type=3, frame_id=fid)
        s.add_text(kx + 20, 130, kt, font_size=11, font_family=3, color="#D93829" if is_h else "#64748B", frame_id=fid)
        s.add_text(kx + 20, 180, kv, font_size=32, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(kx + 20, 260, kd, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 30, "30_oee_dashboard", "OEE Dashboard", "medium", "kpi_cards", ["kpi", "gauges"])

    # 31. Quality Control Plan
    s, fid, tw, th = create_base_scene("Operational Quality Control Plan (QCP)", "INGENIERÍA")
    q_heads = ["PUNTO INSPECCION", "CARACTERISTICA", "ESPECIFICACION", "HERRAMIENTA", "FRECUENCIA"]
    q_xs = [40, 320, 580, 840, 1100]
    for qh, qx in zip(q_heads, q_xs):
        s.add_text(qx, 85, qh, font_size=11, font_family=3, color="#64748B", frame_id=fid)
    q_rows = [
        ("Entrada Chapa", "Espesor de material", "2.0 mm +/- 0.05", "Micrometro digital", "1 por bobina"),
        ("Post Plegado", "Angulo de doblado", "90 deg +/- 0.5 deg", "Goniometro optico", "5 piezas/hora"),
        ("Post Soldadura", "Penetracion cordon", "Min 1.8 mm", "Ultrasonido NDT", "1 pieza/turno")
    ]
    for idx, r in enumerate(q_rows):
        ry = 130 + idx * 85
        s.add_rect(30, ry, tw - 60, 70, bg="#FFF5F2" if idx==1 else "#FFFFFF", stroke="#D93829" if idx==1 else "#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
        for val, qx in zip(r, q_xs):
            s.add_text(qx, ry + 25, val, font_size=11, font_family=3, color="#D93829" if idx==1 and qx==q_xs[0] else "#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 31, "31_quality_control_plan", "Quality Control Plan", "medium", "matrix_table", ["table", "controls"])

    # 32. Control Chart (SPC)
    s, fid, tw, th = create_base_scene("Statistical Process Control (SPC X-bar Chart)", "INGENIERÍA")
    s.add_line(80, 120, 1360, 120, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_text(1380, 115, "LCS (+3 sigma)", font_size=10, font_family=3, color="#D93829", frame_id=fid)
    s.add_line(80, 240, 1360, 240, stroke="#0F172A", stroke_w=2.0, frame_id=fid)
    s.add_text(1380, 235, "Media (mu)", font_size=10, font_family=3, color="#0F172A", frame_id=fid)
    s.add_line(80, 360, 1360, 360, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    s.add_text(1380, 355, "LCI (-3 sigma)", font_size=10, font_family=3, color="#D93829", frame_id=fid)
    pts = [230, 210, 260, 245, 190, 250, 235, 270, 220, 240]
    for idx in range(len(pts)-1):
        x1 = 120 + idx * 120
        y1 = pts[idx]
        x2 = 120 + (idx+1) * 120
        y2 = pts[idx+1]
        s.add_line(x1, y1, x2, y2, stroke="#2563EB", stroke_w=2.0, frame_id=fid)
        s.add_rect(x1-4, y1-4, 8, 8, bg="#2563EB", stroke="#2563EB", frame_id=fid)
    save_and_export(s, fid, cat, 32, "32_control_chart", "Control Chart", "high", "spc_chart", ["axes", "control_limits", "points"])

    # 33. Histogram Analysis
    s, fid, tw, th = create_base_scene("Frequency Histogram & Capability Distribution", "INGENIERÍA")
    s.add_rect(40, 80, 1360, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_line(100, 380, 1300, 380, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    bars = [("19.85", 40), ("19.90", 90), ("19.95", 180), ("20.00", 260), ("20.05", 190), ("20.10", 85), ("20.15", 35)]
    for b_idx, (blab, b_height) in enumerate(bars):
        bx = 200 + b_idx * 140
        by = 380 - b_height
        is_center = b_idx == 3
        s.add_rect(bx, by, 110, b_height, bg="#FFF5F2" if is_center else "#EFF6FF", stroke="#D93829" if is_center else "#3B82F6", stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(bx + 35, by - 20, f"n={b_height}", font_size=10, font_family=3, color="#D93829" if is_center else "#1D4ED8", frame_id=fid)
        s.add_text(bx + 25, 395, blab, font_size=10, font_family=3, color="#64748B", frame_id=fid)
    save_and_export(s, fid, cat, 33, "33_histogram_analysis", "Histogram Analysis", "medium", "histogram", ["bars", "distribution"])

    # 34. Scatter Diagram
    s, fid, tw, th = create_base_scene("Scatter Correlation Diagram (Temperature vs Viscosity)", "INGENIERÍA")
    s.add_rect(40, 80, 1360, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_line(120, 380, 1300, 380, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    s.add_text(650, 400, "Temperatura de Proceso (°C)", font_size=11, font_family=3, color="#64748B", frame_id=fid)
    s.add_line(120, 120, 120, 380, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    s.add_line(180, 340, 1240, 140, stroke="#D93829", stroke_w=2.0, dashed=True, frame_id=fid)
    s.add_text(1180, 125, "R = -0.92 (Fuerte Correlacion)", font_size=11, font_family=3, color="#D93829", frame_id=fid)
    scatter_pts = [(220, 320), (340, 305), (460, 270), (580, 250), (700, 220), (820, 205), (940, 180), (1060, 160), (1180, 145)]
    for px, py in scatter_pts:
        s.add_ellipse(px-5, py-5, 10, 10, bg="#2563EB", stroke="#1D4ED8", stroke_w=1.5, frame_id=fid)
    save_and_export(s, fid, cat, 34, "34_scatter_diagram", "Scatter Diagram", "medium", "scatter", ["points", "correlation"])

    # 35. Process Capability
    s, fid, tw, th = create_base_scene("Process Capability Analysis (Cp & Cpk Metrics)", "INGENIERÍA")
    s.add_rect(40, 80, 660, 350, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "INDICES DE CAPACIDAD DEL PROCESO", font_size=13, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 145, "• Limite Superior (USL): 20.15 mm\n• Limite Inferior (LSL): 19.85 mm\n• Desviacion Estandar (sigma): 0.035 mm\n• Cp = (USL - LSL) / 6*sigma = 1.43 (Capaz)\n• Cpk = min(CPU, CPL) = 1.36 (Centrado)", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "EVALUACION DE SEIS SIGMA", font_size=13, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(760, 145, "• Rendimiento Estimado: 99.996% libres de defectos\n• Nivel Sigma: 4.8 Sigma\n• Accion Recomendada: Mantener control estadistico y reducir variabilidad en turno nocturno.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 35, "35_process_capability", "Process Capability", "medium", "split_capability", ["indices", "six_sigma"])

    # 36. Failure Tree Analysis / FTA
    s, fid, tw, th = create_base_scene("Fault Tree Analysis (FTA Logical Gates)", "INGENIERÍA")
    s.add_quad_card(600, 70, 260, 80, "EVENTO TOPE (FALLO)", "Perdida de Presion de Linea", is_hero=True, frame_id=fid)
    s.add_diamond(690, 180, 80, 80, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_text(710, 210, "OR", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_arrow(730, 150, 730, 180, stroke="#D93829", frame_id=fid)
    s.add_quad_card(350, 300, 260, 80, "Fallo Bomba Primaria", "Cavitacion Mecanica", frame_id=fid)
    s.add_quad_card(850, 300, 260, 80, "Rotura de Valvula", "Fatiga de Material", frame_id=fid)
    s.add_arrow(730, 260, 480, 300, stroke="#94A3B8", frame_id=fid)
    s.add_arrow(730, 260, 980, 300, stroke="#94A3B8", frame_id=fid)
    save_and_export(s, fid, cat, 36, "36_failure_tree_analysis_fta", "Failure Tree Analysis (FTA)", "high", "tree_logic", ["gates", "root_events"])

    # 37. 8D Problem Solving
    s, fid, tw, th = create_base_scene("8D Problem Solving Quality Methodology", "INGENIERÍA")
    d_steps = ["D1: Formar Equipo", "D2: Describir Problema", "D3: Contencion", "D4: Causa Raiz", "D5: Accion Correctiva", "D6: Validar Solucion", "D7: Prevenir Recurrencia", "D8: Reconocimiento"]
    for i, ds in enumerate(d_steps):
        col = i % 4
        row = i // 4
        s.add_quad_card(40 + col * 350, 100 + row * 160, 320, 130, ds, "Acciones documentadas y estado", is_hero=(i==3), frame_id=fid)
    save_and_export(s, fid, cat, 37, "37_8d_problem_solving", "8D Problem Solving", "medium", "grid_steps", ["8d_blocks", "cards"])

    # 38. A3 Problem Solving (Toyota A3)
    s, fid, tw, th = create_base_scene("A3 Continuous Problem Solving Report", "INGENIERÍA")
    s.add_a3_report(40, 80, 1360, 350, "Reduccion de Retrabajos en Linea 4", [], frame_id=fid)
    save_and_export(s, fid, cat, 38, "38_a3_problem_solving", "A3 Problem Solving", "medium", "a3_report", ["a3_sections", "pdca"])

    # 39. Kaizen Board
    s, fid, tw, th = create_base_scene("Kaizen Continuous Improvement Suggestion Board", "INGENIERÍA")
    k_cols = [
        {"title": "1. Sugerencias", "cards": [{"title": "Guia de corte rapido", "desc": "Operario: J. Perez", "tag": "PROPUESTA"}]},
        {"title": "2. En Evaluacion", "cards": [{"title": "Sensor optico parada", "desc": "Ingeniero: M. Gomez", "tag": "STUDY"}], "is_hero": True},
        {"title": "3. En Implementacion", "cards": [{"title": "Carro ergonomico", "desc": "Mantenimiento", "tag": "WIP"}]},
        {"title": "4. Estandarizado", "cards": [{"title": "Poka-Yoke de conector", "desc": "Impacto: 0 defectos", "tag": "DONE"}]}
    ]
    s.add_kanban_board(40, 80, 1360, 350, "Kaizen Floor Board", k_cols, frame_id=fid)
    save_and_export(s, fid, cat, 39, "39_kaizen_board", "Kaizen Board", "medium", "kanban", ["suggestions", "impact"])

    # 40. Standard Work Combination Sheet
    s, fid, tw, th = create_base_scene("Standard Work Combination Sheet (Manual vs Machine vs Walk)", "INGENIERÍA")
    s.add_rect(40, 80, 1360, 350, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_line(80, 130, 1320, 130, stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    ops = [
        ("1. Cargar pieza en CNC", 12, "Manual"),
        ("2. Ciclo mecanizado automatico", 35, "Maquina"),
        ("3. Desbarbado manual e inspeccion", 15, "Manual"),
        ("4. Caminar a Estacion de Ensamble", 6, "Caminata")
    ]
    for idx, (op_name, duration, op_type) in enumerate(ops):
        oy = 150 + idx * 60
        s.add_text(80, oy + 10, op_name, font_size=11, font_family=3, color="#0F172A", frame_id=fid)
        s.add_rect(420, oy, duration * 22.0, 34.0, bg="#FFF5F2" if op_type=="Manual" else "#EFF6FF" if op_type=="Maquina" else "#F1F5F9", stroke="#D93829" if op_type=="Manual" else "#3B82F6" if op_type=="Maquina" else "#94A3B8", stroke_w=1.2, roundness_type=3, frame_id=fid)
        s.add_text(430, oy + 8, f"{duration}s ({op_type})", font_size=10, font_family=3, color="#D93829" if op_type=="Manual" else "#1D4ED8" if op_type=="Maquina" else "#475569", frame_id=fid)
    save_and_export(s, fid, cat, 40, "40_standard_work_combination", "Standard Work Combination Sheet", "high", "timeline_bars", ["manual_time", "auto_time"])
