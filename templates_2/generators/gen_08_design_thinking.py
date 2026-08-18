"""
Generador de Categoría 08: Design Thinking & Ideation (10 Plantillas)
"""

from .common import create_base_scene, save_and_export

def generate():
    print("\n--- Generando 08: Design Thinking & Ideation (10 plantillas) ---")
    cat = "08_design_thinking_ideation"

    # 121. Brainstorming Board
    s, fid, tw, th = create_base_scene("Freeform & Structured Brainstorming Board", "DESIGN THINKING")
    clusters = [
        ("CLUSTER 1: RENDIMIENTO", ["Parser en WebAssembly", "Renderizado paralelo multihilo", "Cache LRU en memoria"], 40, "#D93829"),
        ("CLUSTER 2: EXPERIENCIA", ["Autocompletado en VS Code", "Preview SVG en vivo", "Comando CLI simplificado"], 390, "#0284C7"),
        ("CLUSTER 3: CALIDAD VISUAL", ["Tipografia Inter nativa", "Ruteo ortogonal a 90 grados", "Cero emojis obligatorio"], 740, "#059669"),
        ("CLUSTER 4: ECOSISTEMA", ["212 plantillas de catalogo", "Integracion con Claude / GPT", "Soporte para Antigravity IDE"], 1090, "#D97706")
    ]
    for ctitle, cnotes, cx, ccol in clusters:
        s.add_rect(cx, 80, 310, 350, bg="#FFFFFF", stroke=ccol, stroke_w=1.5, roundness_type=3, frame_id=fid)
        s.add_text(cx + 15, 105, ctitle, font_size=11, font_family=3, color=ccol, frame_id=fid)
        for ni, ntxt in enumerate(cnotes):
            s.add_rect(cx + 12, 140 + ni * 85, 285, 70, bg="#FFF5F2" if ccol=="#D93829" else "#F8FAFC", stroke="#CBD5E1", stroke_w=1.0, roundness_type=3, frame_id=fid)
            s.add_text(cx + 20, 165 + ni * 85, ntxt, font_size=10, font_family=3, color="#0F172A", frame_id=fid)
    save_and_export(s, fid, cat, 121, "121_brainstorming_board", "Brainstorming Board", "low", "sticky_notes", ["idea_cards", "color_clusters"])

    # 122. SCAMPER (7 Columns)
    s, fid, tw, th = create_base_scene("SCAMPER Creative Transformation Framework", "DESIGN THINKING")
    sc_items = [("S: Sustituir", "Reemplazar emojis por iconos vectoriales"),
                ("C: Combinar", "Unir CLI y visualizador web"),
                ("A: Adaptar", "Ajustar sintaxis para Antigravity"),
                ("M: Modificar", "Auto-fit frame con padding >= 35px"),
                ("P: Proponer uso", "Usar como evaluador de diagramas"),
                ("E: Eliminar", "Eliminar dependencias de internet"),
                ("R: Reordenar", "Compilar antes de renderizar")]
    for i, (sclab, scdesc) in enumerate(sc_items):
        sx = 40 + i * 195
        is_hero = i == 3
        s.add_rect(sx, 80, 185, 350, bg="#FFF5F2" if is_hero else "#FFFFFF", stroke="#D93829" if is_hero else "#CBD5E1", stroke_w=1.8 if is_hero else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(sx + 10, 105, sclab, font_size=10, font_family=3, color="#D93829" if is_hero else "#0F172A", frame_id=fid)
        s.add_text(sx + 10, 150, scdesc, font_size=10, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 122, "122_scamper", "SCAMPER", "medium", "scamper_columns", ["scamper_prompts", "cards"])

    # 123. Six Thinking Hats (6 Perspectives)
    s, fid, tw, th = create_base_scene("Edward de Bono's Six Thinking Hats Perspective Board", "DESIGN THINKING")
    hats = [("Sombrero Blanco: Datos", "212 plantillas · VCS: 99.5 · 0 emojis", 40, "#64748B"),
            ("Sombrero Rojo: Emocion", "Sensacion de orden, profesionalismo y confianza", 270, "#D93829"),
            ("Sombrero Negro: Riesgos", "Curvas complejas de Bezier en SVG", 500, "#0F172A"),
            ("Sombrero Amarillo: Beneficios", "Ahorro de 4h/semana en documentacion tecnica", 730, "#D97706"),
            ("Sombrero Verde: Creatividad", "Generador contextual asistido por LLM", 960, "#059669"),
            ("Sombrero Azul: Control", "Suite CI de regresion con 27 tests", 1190, "#0284C7")]
    for hname, hdesc, hx, hcol in hats:
        s.add_rect(hx, 80, 215, 350, bg="#FFFFFF", stroke=hcol, stroke_w=1.8, roundness_type=3, frame_id=fid)
        s.add_text(hx + 12, 105, hname, font_size=10, font_family=3, color=hcol, frame_id=fid)
        s.add_text(hx + 12, 150, hdesc, font_size=10, font_family=3, color="#334155", frame_id=fid)
    save_and_export(s, fid, cat, 123, "123_six_thinking_hats", "Six Thinking Hats", "medium", "perspective_hats", ["hats", "reflections"])

    # 124. Crazy 8s (8 Sketch Grid)
    s, fid, tw, th = create_base_scene("Crazy 8s Rapid Sketching Board (8 Ideas in 8 Minutes)", "DESIGN THINKING")
    for i in range(8):
        col = i % 4
        row = i // 4
        cx = 40 + col * 350
        cy = 90 + row * 170
        is_h = i == 2
        s.add_rect(cx, cy, 325, 150, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#0F172A", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(cx + 15, cy + 15, f"IDEA #{i+1}", font_size=11, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(cx + 15, cy + 45, f"Boceto rapido y descripcion #{i+1}", font_size=10, font_family=3, color="#64748B", frame_id=fid)
    save_and_export(s, fid, cat, 124, "124_crazy_8s", "Crazy 8s", "low", "crazy_8_grid", ["8_cells", "sketch_zones"])

    # 125. How Might We Board
    s, fid, tw, th = create_base_scene("How Might We (HMW) Design Opportunity Board", "DESIGN THINKING")
    hmw_cards = [
        ("HMW 1: VELOCIDAD", "¿Como podriamos generar un diagrama completo en menos de 10 segundos?", 40, 80, 440, 160, True),
        ("HMW 2: CALIDAD", "¿Como podriamos asegurar que ningun diagrama tenga errores de solapamiento?", 500, 80, 440, 160, False),
        ("HMW 3: DISTRIBUCION", "¿Como podriamos permitir que cualquier LLM use Sketion sin instalar nada?", 960, 80, 440, 160, False),
        ("HMW 4: ESTILO", "¿Como podriamos aplicar la identidad editorial Inter en todas las exportaciones?", 40, 260, 660, 160, False),
        ("HMW 5: EXTENSIBILIDAD", "¿Como podriamos facilitar que los usuarios creen sus propios arquetipos?", 720, 260, 680, 160, False)
    ]
    for ht, hd, hx, hy, hw, hh, is_h in hmw_cards:
        s.add_rect(hx, hy, hw, hh, bg="#FFF5F2" if is_h else "#FFFFFF", stroke="#D93829" if is_h else "#CBD5E1", stroke_w=1.8 if is_h else 1.5, roundness_type=3, frame_id=fid)
        s.add_text(hx + 20, hy + 20, ht, font_size=12, font_family=3, color="#D93829" if is_h else "#0F172A", frame_id=fid)
        s.add_text(hx + 20, hy + 60, hd, font_size=11, font_family=3, color="#475569", frame_id=fid)
    save_and_export(s, fid, cat, 125, "125_how_might_we_board", "How Might We Board", "medium", "hmw_matrix", ["hmw_prompts", "vote_chips"])

    # 126. Reverse Brainstorming
    s, fid, tw, th = create_base_scene("Reverse Brainstorming ('How could we cause the problem?')", "DESIGN THINKING")
    s.add_split_duel(40, 80, tw - 80, 350, "Causa del Problema", ["Omitir indices en BD", "Sin timeout de conexion", "Ignorar alertas de CPU"], "Solucion Estructurada", ["Indices B-Tree compuestos", "Configurar connection pool", "Alertas en P99 Latency"], "COMO PROVOCAR EL PROBLEMA", "COMO RESOLVERLO", frame_id=fid)
    save_and_export(s, fid, cat, 126, "126_reverse_brainstorming", "Reverse Brainstorming", "medium", "split_duel", ["how_to_break", "how_to_fix"])

    # 127. Lotus Blossom Diagram (3x3 Grid)
    s, fid, tw, th = create_base_scene("Lotus Blossom 3x3 Creative Idea Expansion Diagram", "DESIGN THINKING")
    for r in range(3):
        for c in range(3):
            lx = 380 + c * 230
            ly = 80 + r * 115
            is_center = r==1 and c==1
            s.add_rect(lx, ly, 215, 100, bg="#FFF5F2" if is_center else "#FFFFFF", stroke="#D93829" if is_center else "#0F172A", stroke_w=2.0 if is_center else 1.2, roundness_type=3, frame_id=fid)
            if is_center:
                s.add_text(lx + 20, ly + 35, "TEMA CENTRAL: SKETION", font_size=11, font_family=3, color="#D93829", frame_id=fid)
            else:
                s.add_text(lx + 15, ly + 25, f"PETALO {chr(65 + r*3 + c)}", font_size=10, font_family=3, color="#0F172A", frame_id=fid)
                s.add_text(lx + 15, ly + 50, "Idea derivada de expansion", font_size=9, font_family=3, color="#64748B", frame_id=fid)
    save_and_export(s, fid, cat, 127, "127_lotus_diagram", "Lotus Diagram", "high", "lotus_matrix", ["central_theme", "subthemes"])

    # 128. How Now Wow Matrix
    s, fid, tw, th = create_base_scene("How-Now-Wow Originality vs Feasibility Matrix", "DESIGN THINKING")
    s.add_rect(40, 80, 660, 165, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "NOW (NORMAL / FACIL DE IMPLEMENTAR)", font_size=12, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_text(60, 135, "• Exportador SVG vectorial con tipografia Inter integrada.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 165, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "WOW (INNOVACION / RUPTURISTA HERO)", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(760, 135, "• Catalogo de 212 plantillas autogeneradas sin dependencias.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(40, 265, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 290, "HOW (FUTURO / DIFICIL DE IMPLEMENTAR)", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(60, 320, "• Editor colaborativo en tiempo real multi-usuario.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(740, 265, 660, 165, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 290, "DESCARTAR (BAJO IMPACTO / DIFICIL)", font_size=12, font_family=3, color="#64748B", frame_id=fid)
    s.add_text(760, 320, "• Soporte para formatos rasterizados pesados.", font_size=11, font_family=3, color="#64748B", frame_id=fid)
    save_and_export(s, fid, cat, 128, "128_how_now_wow_matrix", "How Now Wow Matrix", "medium", "quadrant", ["now_normal", "how_future", "wow_breakthrough"])

    # 129. Idea Prioritization Matrix
    s, fid, tw, th = create_base_scene("Idea Prioritization & Dot Voting Matrix", "DESIGN THINKING")
    s.add_rect(40, 80, 660, 165, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(60, 105, "ALTO IMPACTO / BAJO ESFUERZO (12 VOTOS)", font_size=12, font_family=3, color="#D93829", frame_id=fid)
    s.add_text(60, 135, "• Suite de 212 plantillas vectoriales completas.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(740, 80, 660, 165, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.8, roundness_type=3, frame_id=fid)
    s.add_text(760, 105, "ALTO IMPACTO / ALTO ESFUERZO (8 VOTOS)", font_size=12, font_family=3, color="#1D4ED8", frame_id=fid)
    s.add_text(760, 135, "• Extension nativa para VS Code y JetBrains.", font_size=11, font_family=3, color="#334155", frame_id=fid)
    s.add_rect(40, 265, 660, 165, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(60, 290, "BAJO IMPACTO / BAJO ESFUERZO (3 VOTOS)", font_size=12, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(60, 320, "• Ajuste de paletas de color en modo oscuro.", font_size=11, font_family=3, color="#475569", frame_id=fid)
    s.add_rect(740, 265, 660, 165, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    s.add_text(760, 290, "BAJO IMPACTO / ALTO ESFUERZO (0 VOTOS)", font_size=12, font_family=3, color="#64748B", frame_id=fid)
    s.add_text(760, 320, "• Parser de archivos binarios propietarios antiguos.", font_size=11, font_family=3, color="#64748B", frame_id=fid)
    save_and_export(s, fid, cat, 129, "129_idea_prioritization_matrix", "Idea Prioritization Matrix", "medium", "quadrant", ["impact", "effort", "votes"])

    # 130. Idea Evaluation Canvas (Triple Venn)
    s, fid, tw, th = create_base_scene("Idea Viability, Feasibility & Desirability Canvas", "DESIGN THINKING")
    s.add_ellipse(350, 100, 340, 340, bg="#FFF5F2", stroke="#D93829", stroke_w=1.8, frame_id=fid)
    s.add_text(370, 160, "DESEABILIDAD\n(Usuario lo necesita)", font_size=11, font_family=3, color="#D93829", frame_id=fid)
    s.add_ellipse(650, 100, 340, 340, bg="#EFF6FF", stroke="#3B82F6", stroke_w=1.8, frame_id=fid)
    s.add_text(850, 160, "FACTIBILIDAD\n(Tecnicamente posible)", font_size=11, font_family=3, color="#2563EB", frame_id=fid)
    s.add_ellipse(500, 220, 340, 240, bg="#F8FAFC", stroke="#0F172A", stroke_w=1.8, frame_id=fid)
    s.add_text(600, 370, "VIABILIDAD (Negocio rentable)", font_size=11, font_family=3, color="#0F172A", frame_id=fid)
    s.add_text(620, 250, "ZONA DE INNOVACION", font_size=10, font_family=3, color="#D93829", frame_id=fid)
    save_and_export(s, fid, cat, 130, "130_idea_evaluation_canvas", "Idea Evaluation Canvas", "high", "venn_3_sets", ["viability", "feasibility", "desirability"])
