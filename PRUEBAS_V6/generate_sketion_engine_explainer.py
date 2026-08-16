"""
Sketion 4.0 — Generador del Tablero Explicativo: ¿Cómo Funciona Sketion Engine?
Paleta: Azul Sketion (#2563EB), Azul Profundo (#1D4ED8), Blanco (#FFFFFF), Negro Tinta (#0F172A), Slate (#64748B), Verde (#059669), Coral (#D93829).
Frames:
- Frame 1: La Arquitectura de 4 Capas Desacopladas (De Prompt a Artefacto Nativo)
- Frame 2: El Validador de Calidad 6D y el Bucle Autónomo de Auto-Repair
- Frame 3: La Regla Anti-Monocultivo en Acción (Mapeo Semántica -> Arquetipo)
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
    "GREEN_HERO": "#059669",
    "GREEN_BG": "#F0FDF4",
    "GREEN_BORDER": "#86EFAC",
    "CORAL_HERO": "#D93829",
    "CORAL_BG": "#FEF2F2",
    "CORAL_BORDER": "#FCA5A5",
    "DARK_SLATE": "#1E293B",
    "STICKY": "#FFE95C"
}


def build_sketion_engine_explainer():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])

    # =========================================================================
    # FRAME 1: LA ARQUITECTURA DE 4 CAPAS DESACOPLADAS (LAYER STACK)
    # =========================================================================
    w1, h1 = 2800.0, 980.0
    f1_x, f1_y = place(w1, h1)
    fid1 = scene.add_frame("FRAME 1: ANATOMÍA DE SKETION 4.0 — LA ARQUITECTURA DE 4 CAPAS", f1_x, f1_y, w1, h1)

    scene.add_text(f1_x + 60.0, f1_y + 35.0, "SKETION ENGINE ANATOMY  ·  STRUCTURED VISUAL COMPILER", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "¿Cómo Funciona Sketion?: El Pipeline de Compilación Semántico a Excalidraw Nativo", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    layer_w = w1 - 120.0
    layer_x = f1_x + 60.0
    layer_start_y = f1_y + 115.0
    layer_h = 165.0
    layer_gap = 25.0

    # CAPA 1: MOTOR SEMÁNTICO & INFERENCIA DE AUDIENCIA
    l1_y = layer_start_y
    scene.add_scope_container(layer_x, l1_y, layer_w, layer_h, label="CAPA 1: MOTOR SEMÁNTICO & INFERENCIA DE AUDIENCIA (EL ANALIZADOR COGNITIVO)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)
    sub_w1 = (layer_w - 40.0 - 2 * 30.0) / 3.0
    scene.add_quad_card(layer_x + 20.0, l1_y + 40.0, sub_w1, 105.0, "Inferencia de Audiencia", sublabel="Adapta la densidad y el tono según el receptor (CEO, Ops, Tech, Data)", badge="AUDIENCE", icon="users", font_size=18, frame_id=fid1)
    scene.add_quad_card(layer_x + 20.0 + sub_w1 + 30.0, l1_y + 40.0, sub_w1, 105.0, "Extracción de Entidades", sublabel="Descompone el texto libre en nodos, flujos y dependencias clave", badge="ENTITIES", icon="database", is_hero=True, font_size=18, frame_id=fid1)
    scene.add_quad_card(layer_x + 20.0 + 2 * (sub_w1 + 30.0), l1_y + 40.0, sub_w1, 105.0, "Restricciones Semánticas (IR)", sublabel="Genera el esquema intermedio y detecta dependencias inviolables", badge="IR SCHEMA", icon="lock", font_size=18, frame_id=fid1)

    # CAPA 2: MOTOR DE ARQUETIPOS & ENRUTADOR VISUAL
    l2_y = l1_y + layer_h + layer_gap
    scene.add_scope_container(layer_x, l2_y, layer_w, layer_h, label="CAPA 2: MOTOR DE ARQUETIPOS & ENRUTADOR VISUAL (EL SELECTOR ESTRUCTURAL)", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid1)
    sub_w2 = (layer_w - 40.0 - 2 * 30.0) / 3.0
    scene.add_quad_card(layer_x + 20.0, l2_y + 40.0, sub_w2, 105.0, "Catálogo 20 Arquetipos (A-T)", sublabel="Mapea al patrón geométrico óptimo (Cerebro, Duelo, Flow, Planta)", badge="ARCHETYPES", icon="container", font_size=18, frame_id=fid1)
    scene.add_quad_card(layer_x + 20.0 + (sub_w2 + 30.0), l2_y + 40.0, sub_w2, 105.0, "Suite de 27 Tipos Visuales", sublabel="Motores especializados: Lakehouse, 2x2, Software, Gantt, Swimlanes", badge="27 TYPES", icon="server", is_hero=True, font_size=18, frame_id=fid1)
    scene.add_quad_card(layer_x + 20.0 + 2 * (sub_w2 + 30.0), l2_y + 40.0, sub_w2, 105.0, "Regla Anti-Monocultivo", sublabel="Prohíbe estrictamente repetir la misma disposición en multi-frame", badge="ANTI-MONOCULTURE", icon="key", font_size=18, frame_id=fid1)

    # CAPA 3: MOTOR GEOMÉTRICO, TOKENS & TIPOGRAFÍA
    l3_y = l2_y + layer_h + layer_gap
    scene.add_scope_container(layer_x, l3_y, layer_w, layer_h, label="CAPA 3: MOTOR GEOMÉTRICO, TOKENS & TIPOGRAFÍA (EL CALCULADOR ESPACIAL)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)
    sub_w3 = (layer_w - 40.0 - 2 * 30.0) / 3.0
    scene.add_quad_card(layer_x + 20.0, l3_y + 40.0, sub_w3, 105.0, "Gaps & Gutters (95/65px)", sublabel="Cálculo determinista de distancias para evitar amontonamientos", badge="LAYOUT ENGINE", icon="container", font_size=18, frame_id=fid1)
    scene.add_quad_card(layer_x + 20.0 + sub_w3 + 30.0, l3_y + 40.0, sub_w3, 105.0, "Tipografía Proporcional", sublabel="Fuentes a 18-20px en tarjetas y 14px en tablas (cero letra diminuta)", badge="FONTS (18-20px)", icon="file", font_size=18, frame_id=fid1)
    scene.add_quad_card(layer_x + 20.0 + 2 * (sub_w3 + 30.0), l3_y + 40.0, sub_w3, 105.0, "Conectores Ortogonales & 1 Acento", sublabel="Ruteo a 90° con pastillas protectoras + presupuesto estricto de héroes", badge="ROUTING & ACCENT", icon="sync", font_size=18, frame_id=fid1)

    # CAPA 4: RENDER NATIVO, VALIDADOR 6D & AUTO-REPAIR
    l4_y = l3_y + layer_h + layer_gap
    scene.add_scope_container(layer_x, l4_y, layer_w, layer_h, label="CAPA 4: RENDER NATIVO, VALIDADOR 6D & AUTO-REPAIR (EL COMPILADOR Y CORRECTOR)", stroke=PALETTE["GREEN_BORDER"], bg=PALETTE["GREEN_BG"], frame_id=fid1)
    sub_w4 = (layer_w - 40.0 - 2 * 30.0) / 3.0
    scene.add_quad_card(layer_x + 20.0, l4_y + 40.0, sub_w4, 105.0, "Elementos Nativos Excalidraw", sublabel="JSON válido con boundElements bidireccionales y fontFamily=2", badge="NATIVE JSON", icon="laptop", font_size=18, frame_id=fid1)
    scene.add_quad_card(layer_x + 20.0 + (sub_w4 + 30.0), l4_y + 40.0, sub_w4, 105.0, "Validador 6 Dimensiones", sublabel="Evalúa Estructura, Layout, Legibilidad, Jerarquía, Densidad y Tokens", badge="QUALITY SCORE", icon="monitoring", is_hero=True, font_size=18, frame_id=fid1)
    scene.add_quad_card(layer_x + 20.0 + 2 * (sub_w4 + 30.0), l4_y + 40.0, sub_w4, 105.0, "Bucle Autónomo de Auto-Repair", sublabel="Si Score < 90, corrige y re-inyecta reglas sin intervención humana", badge="AUTO-REPAIR LOOP", icon="sync", font_size=18, frame_id=fid1)

    # Conectores Verticales
    scene.add_arrow(layer_x + layer_w * 0.25, l1_y + layer_h, layer_x + layer_w * 0.25, l2_y, stroke=PALETTE["INK"], stroke_w=1.5, frame_id=fid1)
    scene.add_arrow(layer_x + layer_w * 0.5, l2_y + layer_h, layer_x + layer_w * 0.5, l3_y, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, label="ESQUEMA A GEOMETRÍA", frame_id=fid1)
    scene.add_arrow(layer_x + layer_w * 0.75, l3_y + layer_h, layer_x + layer_w * 0.75, l4_y, stroke=PALETTE["GREEN_HERO"], stroke_w=2.0, label="RENDER & VERIFICACIÓN", frame_id=fid1)

    scene.add_legend_footer(f1_x + 60.0, f1_y + 885.0, w1 - 120.0, swatches=[
        {"label": "Compilación & Auto-Repair Héroe", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]},
        {"label": "Catálogo de Motores y Arquetipos", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Capas Analíticas y Geométricas", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]}
    ], note="Sketion compiles unstructured thinking into structured, editable visual artifacts", frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=50.0)

    # =========================================================================
    # FRAME 2: EL VALIDADOR DE CALIDAD 6D Y EL BUCLE DE AUTO-REPAIR
    # =========================================================================
    w2, h2 = 2800.0, 980.0
    f2_x, f2_y = place(w2, h2)
    fid2 = scene.add_frame("FRAME 2: SKETION QUALITY ENGINE — VALIDADOR 6D & AUTO-REPAIR LOOP", f2_x, f2_y, w2, h2)

    scene.add_text(f2_x + 60.0, f2_y + 35.0, "SKETION QUALITY SYSTEM  ·  6-DIMENSIONAL AUDIT & RECURSIVE HEALING", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid2)
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "El Motor de Calidad 6D: Cómo se Inspecciona y Repara Cada Diagrama", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    # PARTE IZQUIERDA: LAS 6 DIMENSIONES DE CALIDAD
    z1_x = f2_x + 60.0
    z1_y = f2_y + 120.0
    z1_w = 1250.0
    z1_h = 740.0
    scene.add_scope_container(z1_x, z1_y, z1_w, z1_h, label="LAS 6 DIMENSIONES EVALUADAS (QUALITY SCORE 0 - 100)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)

    card_d_w = 560.0
    scene.add_quad_card(z1_x + 35.0, z1_y + 60.0, card_d_w, 105.0, "1. Structure (100 pts)", sublabel="Integridad de IDs, boundElements y textos vinculados", badge="STRUCTURE", icon="laptop", font_size=18, frame_id=fid2)
    scene.add_quad_card(z1_x + 655.0, z1_y + 60.0, card_d_w, 105.0, "2. Layout & Spacing (100 pts)", sublabel="Gaps de 95/65px, ausencia de colisiones y overlaps", badge="LAYOUT", icon="container", font_size=18, frame_id=fid2)

    scene.add_quad_card(z1_x + 35.0, z1_y + 195.0, card_d_w, 105.0, "3. Readability (100 pts)", sublabel="Fuentes proporcionales (18-20px) sin espacios vacíos", badge="READABILITY", icon="file", is_hero=True, font_size=18, frame_id=fid2)
    scene.add_quad_card(z1_x + 655.0, z1_y + 195.0, card_d_w, 105.0, "4. Hierarchy & Accents (100 pts)", sublabel="Exactamente 1-2 héroes con acento focal por marco", badge="HIERARCHY", icon="key", font_size=18, frame_id=fid2)

    scene.add_quad_card(z1_x + 35.0, z1_y + 330.0, card_d_w, 105.0, "5. Visual Noise (100 pts)", sublabel="Densidad calibrada en 4.0/10 (aire visual y respiro)", badge="DENSITY 4/10", icon="monitoring", font_size=18, frame_id=fid2)
    scene.add_quad_card(z1_x + 655.0, z1_y + 330.0, card_d_w, 105.0, "6. Brand Consistency (100 pts)", sublabel="Uso estricto de tokens y paletas editoriales aprobadas", badge="TOKENS", icon="database", font_size=18, frame_id=fid2)

    scene.add_sticky_note(z1_x + 35.0, z1_y + 465.0, 1180.0, 95.0,
                          "CRITERIO DE APROBACIÓN:\nUn diagrama solo es entregado si obtiene Overall Quality Score >= 90/100 y Archetype Fitness = 100/100.\nSi falla, entra inmediatamente en el bucle de reparación autónoma.",
                          angle_deg=-0.5, font_size=14, frame_id=fid2)

    # PARTE DERECHA: EL BUCLE DE AUTO-REPAIR (RECURSIVO)
    z2_x = z1_x + z1_w + 60.0
    z2_y = z1_y
    z2_w = w2 - z2_x - 60.0
    z2_h = 740.0
    scene.add_scope_container(z2_x, z2_y, z2_w, z2_h, label="BUCLE AUTÓNOMO DE AUTO-REPAIR (MÁX 3 ITERACIONES)", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid2)

    scene.add_quad_card(z2_x + 35.0, z2_y + 60.0, z2_w - 70.0, 115.0,
                        "Paso 1: Auditoría y Detección",
                        sublabel="El validador lista incidencias (ej. sobrecarga de acentos o solapamiento)",
                        badge="AUDIT", icon="monitoring", font_size=18, frame_id=fid2)

    scene.add_quad_card(z2_x + 35.0, z2_y + 215.0, z2_w - 70.0, 115.0,
                        "Paso 2: Aplicación de Heurísticas de Reparación",
                        sublabel="Degrada acentos a neutro · Ajusta tamaño de fuente · Expande contenedores",
                        badge="HEAL", icon="sync", is_hero=True, font_size=18, frame_id=fid2)

    scene.add_quad_card(z2_x + 35.0, z2_y + 370.0, z2_w - 70.0, 115.0,
                        "Paso 3: Re-validación del Score",
                        sublabel="Recalcula el índice. Si Score >= 90, aprueba; si no, itera hasta ciclo 3",
                        badge="RE-CHECK", icon="lock", font_size=18, frame_id=fid2)

    scene.add_quad_card(z2_x + 35.0, z2_y + 525.0, z2_w - 70.0, 115.0,
                        "Paso 4: Exportación Nativa Exitosa",
                        sublabel="Entrega el archivo .excalidraw 100% verificado, limpio y legible",
                        badge="DELIVERY", icon="key", font_size=18, frame_id=fid2)

    scene.add_arrow(z2_x + z2_w * 0.5, z2_y + 175.0, z2_x + z2_w * 0.5, z2_y + 215.0, stroke=PALETTE["CORAL_HERO"], stroke_w=2.0, frame_id=fid2)
    scene.add_arrow(z2_x + z2_w * 0.5, z2_y + 330.0, z2_x + z2_w * 0.5, z2_y + 370.0, stroke=PALETTE["CORAL_HERO"], stroke_w=2.0, frame_id=fid2)
    scene.add_arrow(z2_x + z2_w * 0.5, z2_y + 485.0, z2_x + z2_w * 0.5, z2_y + 525.0, stroke=PALETTE["GREEN_HERO"], stroke_w=2.5, label="PASS (>=90)", frame_id=fid2)

    scene.add_arrow(z1_x + z1_w, z1_y + 240.0, z2_x, z2_y + 240.0, stroke=PALETTE["CORAL_HERO"], stroke_w=2.5, label="SI SCORE < 90", orthogonal=True, frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=50.0)

    # =========================================================================
    # FRAME 3: LA REGLA ANTI-MONOCULTIVO EN ACCIÓN (CATÁLOGO DE ARQUETIPOS)
    # =========================================================================
    w3, h3 = 2800.0, 980.0
    f3_x, f3_y = place(w3, h3)
    fid3 = scene.add_frame("FRAME 3: DIVERSIDAD DE ARQUETIPOS — MAPEO SEMÁNTICO A GEOMETRÍA REAL", f3_x, f3_y, w3, h3)

    scene.add_text(f3_x + 60.0, f3_y + 35.0, "ARCHETYPE DIVERSITY ENGINE  ·  ANTI-MONOCULTURE RULE", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid3)
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "Mapeo Semántico Obligatorio: Cada Problema Tiene su Propia Geometría Nativa", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    # 6 CAJAS DE ARQUETIPOS ESPECIALIZADOS
    grid_w = (w3 - 120.0 - 2 * 45.0) / 3.0
    grid_h = 340.0
    gy1 = f3_y + 125.0
    gy2 = gy1 + grid_h + 35.0

    gx1 = f3_x + 60.0
    gx2 = gx1 + grid_w + 45.0
    gx3 = gx2 + grid_w + 45.0

    # 1. ECOSISTEMAS
    scene.add_scope_container(gx1, gy1, grid_w, grid_h, label="1. ECOSISTEMAS & PLATAFORMAS", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid3)
    scene.add_quad_card(gx1 + 25.0, gy1 + 55.0, grid_w - 50.0, 115.0, "Arquetipo A: El Cerebro", sublabel="Hub central interactivo con satélites conectados radialmente", badge="RADIAL HUB", icon="laptop", is_hero=True, font_size=18, frame_id=fid3)
    scene.add_bound_card(gx1 + 25.0, gy1 + 190.0, grid_w - 50.0, 120.0, "Uso: Sistemas multi-módulo, suites de productos, data lakehouse centralizado.", bg="#FFFFFF", stroke=PALETTE["BLUE_BORDER"], text_color=PALETTE["INK"], font_size=14, roundness_type=3, frame_id=fid3)

    # 2. ARQUITECTURA SOFTWARE
    scene.add_scope_container(gx2, gy1, grid_w, grid_h, label="2. ARQUITECTURA SOFTWARE & CLOUD", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    scene.add_quad_card(gx2 + 25.0, gy1 + 55.0, grid_w - 50.0, 115.0, "Arquetipo Layer Stack", sublabel="Pila horizontal de capas técnicas (UI -> Engine -> DB -> Cloud)", badge="LAYER STACK", icon="server", font_size=18, frame_id=fid3)
    scene.add_bound_card(gx2 + 25.0, gy1 + 190.0, grid_w - 50.0, 120.0, "Uso: Infraestructura cloud, microservicios, capas de abstracción y persistencia.", bg="#FFFFFF", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"], font_size=14, roundness_type=3, frame_id=fid3)

    # 3. PIPELINES & PROCESOS
    scene.add_scope_container(gx3, gy1, grid_w, grid_h, label="3. PIPELINES, DATOS & IA", stroke=PALETTE["GREEN_BORDER"], bg=PALETTE["GREEN_BG"], frame_id=fid3)
    scene.add_quad_card(gx3 + 25.0, gy1 + 55.0, grid_w - 50.0, 115.0, "Arquetipo C: Flow con Feedback", sublabel="Flujo secuencial con decisiones lógicas y bucle de auto-reparación", badge="FLOW PIPELINE", icon="sync", is_hero=True, font_size=18, frame_id=fid3)
    scene.add_bound_card(gx3 + 25.0, gy1 + 190.0, grid_w - 50.0, 120.0, "Uso: Pipelines ETL, algoritmos de inferencia IA, ciclos de vida y compilación.", bg="#FFFFFF", stroke=PALETTE["GREEN_BORDER"], text_color=PALETTE["INK"], font_size=14, roundness_type=3, frame_id=fid3)

    # 4. ROADMAPS & MADUREZ
    scene.add_scope_container(gx1, gy2, grid_w, grid_h, label="4. ROADMAPS & ESTRATEGIA", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    scene.add_quad_card(gx1 + 25.0, gy2 + 55.0, grid_w - 50.0, 115.0, "Arquetipo G: Escalera de 5 Niveles", sublabel="Madurez progresiva ascendente combinada con matriz de horizontes", badge="MATURITY STAIR", icon="container", font_size=18, frame_id=fid3)
    scene.add_bound_card(gx1 + 25.0, gy2 + 190.0, grid_w - 50.0, 120.0, "Uso: Planes de lanzamiento a 90 días, evolución tecnológica, niveles de madurez.", bg="#FFFFFF", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"], font_size=14, roundness_type=3, frame_id=fid3)

    # 5. COMPARATIVAS & MERCADO
    scene.add_scope_container(gx2, gy2, grid_w, grid_h, label="5. COMPARATIVAS & ANTES VS DESPUÉS", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid3)
    scene.add_quad_card(gx2 + 25.0, gy2 + 55.0, grid_w - 50.0, 115.0, "Arquetipo D: El Duelo VS", sublabel="Contraste explícito entre el dolor legado (rojo) y la solución moderna (verde)", badge="THE DUEL (VS)", icon="alert", is_hero=True, font_size=18, frame_id=fid3)
    scene.add_bound_card(gx2 + 25.0, gy2 + 190.0, grid_w - 50.0, 120.0, "Uso: Pitch decks, propuestas de valor, migraciones de software y benchmarking.", bg="#FFFFFF", stroke=PALETTE["CORAL_BORDER"], text_color=PALETTE["INK"], font_size=14, roundness_type=3, frame_id=fid3)

    # 6. WORKSHOPS & DISCOVERY
    scene.add_scope_container(gx3, gy2, grid_w, grid_h, label="6. SESIONES DE DISCOVERY & WORKSHOPS", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    scene.add_quad_card(gx3 + 25.0, gy2 + 55.0, grid_w - 50.0, 115.0, "Arquetipo Workshop Canvas", sublabel="Notas adhesivas libres, slots de evidencia y matrices de requerimientos", badge="MIRO CANVAS", icon="file", font_size=18, frame_id=fid3)
    scene.add_bound_card(gx3 + 25.0, gy2 + 190.0, grid_w - 50.0, 120.0, "Uso: Reuniones con clientes, lluvia de ideas, levantamiento de requerimientos en vivo.", bg="#FFFFFF", stroke=PALETTE["CARD_BORDER"], text_color=PALETTE["INK"], font_size=14, roundness_type=3, frame_id=fid3)

    scene.add_legend_footer(f3_x + 60.0, f3_y + 885.0, w3 - 120.0, swatches=[
        {"label": "Arquetipos Centrales & Héroes", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Duelo & Fricción de Mercado", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Pipelines & Validación Autónoma", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]}
    ], note="Cada problema tiene una forma geométrica natural · Cero clonación de plantillas", frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)

    # Guardar archivo
    out_file = os.path.join(OUT_DIR, "como_funciona_sketion_engine.excalidraw")
    scene.save(out_file)
    print(f"\n[+] Tablero Explicativo Sketion Engine guardado exitosamente en:\n    {out_file}")

    # Validaciones
    is_valid, report = validate_scene(out_file)
    print("\n" + report.summary())

    fit_score, fit_details = calculate_archetype_fitness(
        problem_domain="SKETION_ENGINE_EXPLAINER",
        chosen_structures=["LAYER_STACK_ARCHITECTURE", "RECURSIVE_AUTO_REPAIR_LOOP", "ARCHETYPE_DIVERSITY_GALLERY"],
        covered_dimensions=["4 Capas de Compilación", "Inferencia de Audiencia", "Validador 6D", "Bucle de Auto-Repair", "Regla Anti-Monocultivo", "Mapeo Semántico"],
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
    build_sketion_engine_explainer()
