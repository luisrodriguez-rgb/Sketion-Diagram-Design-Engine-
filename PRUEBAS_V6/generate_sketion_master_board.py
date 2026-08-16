"""
Sketion 4.0 — Generador del Tablero Maestro de Visión y Arquitectura SKETION
Rediseñado con 4 Arquetipos Visuales Distintos y Auténticos:
- Frame 1: Arquetipo D (Duelo de Fragmentación) + Arquetipo A (El Hub Central / Radial Core)
- Frame 2: Arquetipo Layer Stack (Pila Horizontal de 4 Capas Técnicas de Software)
- Frame 3: Arquetipo C (Flow Pipeline) con Bucle Visible de Auto-Repair y Feedback
- Frame 4: Arquetipo G (Escalera de Madurez de 5 Niveles) + Matriz de Horizontes (Live, Building, R&D)
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


def build_sketion_master_project():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])

    # =========================================================================
    # FRAME 1: ARQUETIPO D (DUELO) + ARQUETIPO A (EL CEREBRO / RADIAL HUB)
    # =========================================================================
    w1, h1 = 2800.0, 980.0
    f1_x, f1_y = place(w1, h1)
    fid1 = scene.add_frame("FRAME 1: SKETION MASTER — IDENTIDAD, POSICIONAMIENTO & HUB RADIAL DE CONOCIMIENTO", f1_x, f1_y, w1, h1)

    scene.add_text(f1_x + 60.0, f1_y + 35.0, "SKETION MASTER PROJECT  ·  THINK. STRUCTURE. BUILD.", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "De la Fragmentación de 10 Apps al Hub Central de Conocimiento Visual", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    scope_y = f1_y + 115.0
    scope_h = 740.0

    # PANEL IZQUIERDO: EL DOLOR DE LA FRAGMENTACIÓN (Arquetipo D - Duelo)
    sc1_w = 950.0
    sc1_x = f1_x + 60.0
    scene.add_scope_container(sc1_x, scope_y, sc1_w, scope_h, label="1. EL PROBLEMA: STACK FRAGMENTADO (6+ APPS AISLADAS)", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid1)

    c_f1 = 410.0
    scene.add_quad_card(sc1_x + 35.0, scope_y + 60.0, c_f1, 105.0, "PDFs en Adobe / Reader", sublabel="Texto estático · Sin conexión a notas", badge="DOCS", icon="file", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc1_x + 505.0, scope_y + 60.0, c_f1, 105.0, "Notas en Notion / Docs", sublabel="Listas lineales · Sin espacialidad", badge="NOTES", icon="laptop", font_size=18, frame_id=fid1)

    scene.add_quad_card(sc1_x + 35.0, scope_y + 185.0, c_f1, 105.0, "Fórmulas en Overleaf", sublabel="LaTeX aislado de explicaciones", badge="MATH", icon="server", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc1_x + 505.0, scope_y + 185.0, c_f1, 105.0, "Diagramas en Excalidraw", sublabel="Solo dibujo libre · Sin datos ni docs", badge="DRAW", icon="container", font_size=18, frame_id=fid1)

    scene.add_quad_card(sc1_x + 35.0, scope_y + 310.0, c_f1, 105.0, "Datos en Excel / Sheets", sublabel="Tablas frías desconectadas de notas", badge="DATA", icon="database", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc1_x + 505.0, scope_y + 310.0, c_f1, 105.0, "Flashcards en Anki", sublabel="Preguntas aisladas del material", badge="CARDS", icon="users", font_size=18, frame_id=fid1)

    # Flechas rojas de fricción entre apps
    scene.add_arrow(sc1_x + 240.0, scope_y + 165.0, sc1_x + 240.0, scope_y + 185.0, stroke=PALETTE["CORAL_HERO"], stroke_w=1.5, dashed=True, frame_id=fid1)
    scene.add_arrow(sc1_x + 710.0, scope_y + 165.0, sc1_x + 710.0, scope_y + 185.0, stroke=PALETTE["CORAL_HERO"], stroke_w=1.5, dashed=True, frame_id=fid1)
    scene.add_arrow(sc1_x + 240.0, scope_y + 290.0, sc1_x + 240.0, scope_y + 310.0, stroke=PALETTE["CORAL_HERO"], stroke_w=1.5, dashed=True, frame_id=fid1)

    scene.add_sticky_note(sc1_x + 35.0, scope_y + 440.0, 880.0, 110.0,
                          "CICLO DE FRICCIÓN COGNITIVA:\nOpen -> Switch -> Copy -> Paste -> Reorganize -> Switch Again.\nSe pierde el 40% del tiempo de investigación y estudio cambiando de pestañas.",
                          angle_deg=-1.0, font_size=15, frame_id=fid1)

    # PANEL DERECHO: ARQUETIPO A (EL CEREBRO / RADIAL HUB)
    sc2_w = 1660.0
    sc2_x = sc1_x + sc1_w + 70.0
    scene.add_scope_container(sc2_x, scope_y, sc2_w, scope_h, label="2. SOLUCIÓN SKETION: HUB CENTRAL DE CONOCIMIENTO (ARQUETIPO RADIAL)", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid1)

    # HUB CENTRAL (EL CEREBRO)
    hub_w, hub_h = 560.0, 160.0
    hub_x = sc2_x + (sc2_w - hub_w) * 0.5
    hub_y = scope_y + (scope_h - hub_h) * 0.5 - 30.0
    hub_box, _ = scene.add_quad_card(hub_x, hub_y, hub_w, hub_h,
                                     "SKETION INFINITE CANVAS CORE",
                                     sublabel="Lienzo espacial donde todo el conocimiento converge y se conecta en vivo",
                                     badge="NUCLEUS", icon="laptop", is_hero=True, font_size=20, pills=["LOCAL-FIRST", "INTERACTIVE"], frame_id=fid1)

    # 6 SATÉLITES RADIALES CONECTADOS AL HUB
    sat_w, sat_h = 440.0, 115.0

    # 1. Top-Left: PDFs
    s1_x, s1_y = sc2_x + 45.0, scope_y + 55.0
    c_s1, _ = scene.add_quad_card(s1_x, s1_y, sat_w, sat_h, "PDFs con Text Overlays", sublabel="Anotaciones y capas de texto vivo", badge="DOCS", icon="file", font_size=18, frame_id=fid1)
    scene.add_arrow(c_s1["x"] + sat_w, c_s1["y"] + sat_h * 0.5, hub_x, hub_y + 30.0, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, frame_id=fid1)

    # 2. Top-Right: LaTeX
    s2_x, s2_y = sc2_x + sc2_w - sat_w - 45.0, scope_y + 55.0
    c_s2, _ = scene.add_quad_card(s2_x, s2_y, sat_w, sat_h, "LaTeX & Math (KaTeX)", sublabel="Fórmulas integradas al espacio visual", badge="MATH", icon="server", font_size=18, frame_id=fid1)
    scene.add_arrow(c_s2["x"], c_s2["y"] + sat_h * 0.5, hub_x + hub_w, hub_y + 30.0, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, frame_id=fid1)

    # 3. Mid-Left: Notes
    s3_x, s3_y = sc2_x + 45.0, hub_y + 20.0
    c_s3, _ = scene.add_quad_card(s3_x, s3_y, sat_w, sat_h, "Knowledge Graph Notes", sublabel="Notas espaciales conectadas entre sí", badge="GRAPH", icon="laptop", font_size=18, frame_id=fid1)
    scene.add_arrow(c_s3["x"] + sat_w, c_s3["y"] + sat_h * 0.5, hub_x, hub_y + hub_h * 0.5, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, frame_id=fid1)

    # 4. Mid-Right: Mermaid
    s4_x, s4_y = sc2_x + sc2_w - sat_w - 45.0, hub_y + 20.0
    c_s4, _ = scene.add_quad_card(s4_x, s4_y, sat_w, sat_h, "Mermaid Diagrams", sublabel="Arquitecturas y flujos lógicos", badge="DIAGRAMS", icon="container", font_size=18, frame_id=fid1)
    scene.add_arrow(c_s4["x"], c_s4["y"] + sat_h * 0.5, hub_x + hub_w, hub_y + hub_h * 0.5, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, frame_id=fid1)

    # 5. Bottom-Left: Datasets
    s5_x, s5_y = sc2_x + 45.0, scope_y + scope_h - sat_h - 75.0
    c_s5, _ = scene.add_quad_card(s5_x, s5_y, sat_w, sat_h, "Datasets & Live Charts", sublabel="CSV y Google Sheets en el canvas", badge="DATA", icon="database", font_size=18, frame_id=fid1)
    scene.add_arrow(c_s5["x"] + sat_w, c_s5["y"] + sat_h * 0.5, hub_x, hub_y + hub_h - 30.0, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, frame_id=fid1)

    # 6. Bottom-Right: Flashcards
    s6_x, s6_y = sc2_x + sc2_w - sat_w - 45.0, scope_y + scope_h - sat_h - 75.0
    c_s6, _ = scene.add_quad_card(s6_x, s6_y, sat_w, sat_h, "Study Mode & Flashcards", sublabel="Active recall nacido del propio canvas", badge="RECALL", icon="users", is_hero=True, font_size=18, frame_id=fid1)
    scene.add_arrow(c_s6["x"], c_s6["y"] + sat_h * 0.5, hub_x + hub_w, hub_y + hub_h - 30.0, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, frame_id=fid1)

    # Conexión de Transformación
    scene.add_arrow(sc1_x + sc1_w, scope_y + scope_h * 0.5, sc2_x, scope_y + scope_h * 0.5, stroke=PALETTE["BLUE_HERO"], stroke_w=3.0, label="UNIFICACIÓN TOTAL", orthogonal=True, frame_id=fid1)

    scene.add_legend_footer(f1_x + 60.0, f1_y + 885.0, w1 - 120.0, swatches=[
        {"label": "Núcleo del Canvas Sketion", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Formatos Satelitales Conectados", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]},
        {"label": "Fragmentación Legada", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]}
    ], note="Think. Structure. Build. · Everything connected · Everything visual", frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=50.0)

    # =========================================================================
    # FRAME 2: ARQUETIPO LAYER STACK (PILA HORIZONTAL DE 4 CAPAS TÉCNICAS)
    # =========================================================================
    w2, h2 = 2800.0, 980.0
    f2_x, f2_y = place(w2, h2)
    fid2 = scene.add_frame("FRAME 2: SKETION ARCHITECTURE — LAYER STACK HORIZONTAL & LOCAL-FIRST", f2_x, f2_y, w2, h2)

    scene.add_text(f2_x + 60.0, f2_y + 35.0, "SKETION ARCHITECTURE  ·  LAYERED TIER ARCHITECTURE", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid2)
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "Pila de Arquitectura por Capas: De la Interfaz React al Backend Supabase", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    layer_w = w2 - 120.0
    layer_x = f2_x + 60.0
    layer_start_y = f2_y + 115.0
    layer_h = 165.0
    layer_gap = 25.0

    # CAPA 1: CAPA DE PRESENTACIÓN & UI
    l1_y = layer_start_y
    scene.add_scope_container(layer_x, l1_y, layer_w, layer_h, label="CAPA 1: PRESENTACIÓN & INTERFAZ (BROWSER CLIENT)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    sub_w1 = (layer_w - 40.0 - 2 * 30.0) / 3.0
    scene.add_quad_card(layer_x + 20.0, l1_y + 40.0, sub_w1, 105.0, "React 18 & Vite", sublabel="Arquitectura de componentes modulares y hot-reload", badge="FRONTEND", icon="laptop", font_size=18, frame_id=fid2)
    scene.add_quad_card(layer_x + 20.0 + sub_w1 + 30.0, l1_y + 40.0, sub_w1, 105.0, "TypeScript Strict Mode", sublabel="Tipado estático seguro para modelos y estados de canvas", badge="TYPES", icon="server", font_size=18, frame_id=fid2)
    scene.add_quad_card(layer_x + 20.0 + 2 * (sub_w1 + 30.0), l1_y + 40.0, sub_w1, 105.0, "Tailwind CSS + Outfit / Inter", sublabel="Sistema de diseño sobrio, tokens y micro-animaciones", badge="DESIGN TOKENS", icon="file", font_size=18, frame_id=fid2)

    # CAPA 2: MOTORES DE RENDERIZADO EN EL CANVAS
    l2_y = l1_y + layer_h + layer_gap
    scene.add_scope_container(layer_x, l2_y, layer_w, layer_h, label="CAPA 2: MOTORES DE RENDERIZADO & VISUALIZACIÓN DEL CANVAS", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid2)
    sub_w2 = (layer_w - 40.0 - 3 * 25.0) / 4.0
    scene.add_quad_card(layer_x + 20.0, l2_y + 40.0, sub_w2, 105.0, "Excalidraw Core", sublabel="Lienzo infinito, render por capas y selección espacial", badge="CANVAS ENGINE", icon="container", is_hero=True, font_size=18, frame_id=fid2)
    scene.add_quad_card(layer_x + 20.0 + (sub_w2 + 25.0), l2_y + 40.0, sub_w2, 105.0, "PDF.js Engine", sublabel="Decodificación de blobs, overlays y texto interactivo", badge="PDF ENGINE", icon="file", font_size=18, frame_id=fid2)
    scene.add_quad_card(layer_x + 20.0 + 2 * (sub_w2 + 25.0), l2_y + 40.0, sub_w2, 105.0, "KaTeX Math Parser", sublabel="Renderizado vectorial de fórmulas matemáticas complejas", badge="LATEX PARSER", icon="server", font_size=18, frame_id=fid2)
    scene.add_quad_card(layer_x + 20.0 + 3 * (sub_w2 + 25.0), l2_y + 40.0, sub_w2, 105.0, "Mermaid Runtime", sublabel="Generación de diagramas de secuencia y flujos de código", badge="MERMAID RUNTIME", icon="database", font_size=18, frame_id=fid2)

    # CAPA 3: PERSISTENCIA LOCAL (LOCAL-FIRST TIER) - HÉROE
    l3_y = l2_y + layer_h + layer_gap
    scene.add_scope_container(layer_x, l3_y, layer_w, layer_h, label="CAPA 3: MOTOR DE PERSISTENCIA LOCAL-FIRST (LATENCIA CERO & OFFLINE RESILIENCE)", stroke=PALETTE["GREEN_BORDER"], bg=PALETTE["GREEN_BG"], frame_id=fid2)
    sub_w3 = (layer_w - 40.0 - 2 * 30.0) / 3.0
    scene.add_quad_card(layer_x + 20.0, l3_y + 40.0, sub_w3, 105.0, "IndexedDB (Dexie.js)", sublabel="Persistencia local instantánea de boards, notas y blobs", badge="LOCAL DB", icon="database", is_hero=True, font_size=18, pills=["FAST", "OFFLINE"], frame_id=fid2)
    scene.add_quad_card(layer_x + 20.0 + sub_w3 + 30.0, l3_y + 40.0, sub_w3, 105.0, "Offline State Manager", sublabel="Cola de operaciones locales para sincronización diferida", badge="STATE QUEUE", icon="lock", font_size=18, frame_id=fid2)
    scene.add_quad_card(layer_x + 20.0 + 2 * (sub_w3 + 30.0), l3_y + 40.0, sub_w3, 105.0, "Blob Cache & Rehydration", sublabel="Carga ultrarrápida de documentos sin depender de red", badge="BLOB CACHE", icon="sync", font_size=18, frame_id=fid2)

    # CAPA 4: CLOUD BACKEND & SINCRONIZACIÓN
    l4_y = l3_y + layer_h + layer_gap
    scene.add_scope_container(layer_x, l4_y, layer_w, layer_h, label="CAPA 4: INFRAESTRUCTURA CLOUD, SINCRONIZACIÓN & COLABORACIÓN", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    sub_w4 = (layer_w - 40.0 - 3 * 25.0) / 4.0
    scene.add_quad_card(layer_x + 20.0, l4_y + 40.0, sub_w4, 105.0, "Supabase Auth & RLS", sublabel="Autenticación segura y permisos por proyecto", badge="SECURITY", icon="key", font_size=18, frame_id=fid2)
    scene.add_quad_card(layer_x + 20.0 + (sub_w4 + 25.0), l4_y + 40.0, sub_w4, 105.0, "PostgreSQL Database", sublabel="Almacén relacional de metadatos y workspaces", badge="POSTGRES", icon="database", font_size=18, frame_id=fid2)
    scene.add_quad_card(layer_x + 20.0 + 2 * (sub_w4 + 25.0), l4_y + 40.0, sub_w4, 105.0, "Supabase Storage", sublabel="Buckets seguros para almacenamiento de PDFs", badge="STORAGE", icon="server", font_size=18, frame_id=fid2)
    scene.add_quad_card(layer_x + 20.0 + 3 * (sub_w4 + 25.0), l4_y + 40.0, sub_w4, 105.0, "Socket.IO Collab", sublabel="Comentarios espaciales y presencia en tiempo real", badge="REALTIME", icon="sync", font_size=18, frame_id=fid2)

    # Conectores Verticales entre Capas
    scene.add_arrow(layer_x + layer_w * 0.25, l1_y + layer_h, layer_x + layer_w * 0.25, l2_y, stroke=PALETTE["INK"], stroke_w=1.5, frame_id=fid2)
    scene.add_arrow(layer_x + layer_w * 0.5, l2_y + layer_h, layer_x + layer_w * 0.5, l3_y, stroke=PALETTE["BLUE_HERO"], stroke_w=2.5, label="PERSISTENCIA DIRECTA", frame_id=fid2)
    scene.add_arrow(layer_x + layer_w * 0.75, l3_y + layer_h, layer_x + layer_w * 0.75, l4_y, stroke=PALETTE["GREEN_HERO"], stroke_w=2.5, label="SYNC ASÍNCRONO", frame_id=fid2)

    scene.add_legend_footer(f2_x + 60.0, f2_y + 885.0, w2 - 120.0, swatches=[
        {"label": "Capa Local-First Héroe", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]},
        {"label": "Motores del Canvas", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Servicios de Infraestructura", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]}
    ], note="Your workspace should remain useful even when the network doesn't · Local-First Architecture", frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=50.0)

    # =========================================================================
    # FRAME 3: ARQUETIPO C (FLOW PIPELINE) CON BUCLE VISIBLE DE AUTO-REPAIR
    # =========================================================================
    w3, h3 = 2800.0, 980.0
    f3_x, f3_y = place(w3, h3)
    fid3 = scene.add_frame("FRAME 3: SKETION INTELLIGENCE — PIPELINE SEMÁNTICO & AUTO-REPAIR LOOP", f3_x, f3_y, w3, h3)

    scene.add_text(f3_x + 60.0, f3_y + 35.0, "SKETION INTELLIGENCE  ·  STRUCTURED AI DIAGRAMMING ENGINE", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid3)
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "Pipeline de 4 Capas: Comprensión Semántica, Geometría Determinista & Bucle de Reparación", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    # 5 ETAPAS DEL PIPELINE PRINCIPAL (FLUJO HORIZONTAL)
    pipe_y = f3_y + 360.0
    pipe_w = (w3 - 120.0 - 4 * 60.0) / 5.0
    pipe_h = 240.0

    # PASO 1: INPUT
    p1_x = f3_x + 60.0
    scene.add_scope_container(p1_x, pipe_y, pipe_w, pipe_h, label="1. INPUT BRUTO", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c_p1, _ = scene.add_quad_card(p1_x + 20.0, pipe_y + 50.0, pipe_w - 40.0, 160.0, "Prompt del Usuario", sublabel="Texto desestructurado · Requerimientos técnicos · Audiencia objetivo (CEO/Ops/Tech)", badge="INPUT", icon="laptop", font_size=18, frame_id=fid3)

    # PASO 2: SEMÁNTICA
    p2_x = p1_x + pipe_w + 60.0
    scene.add_scope_container(p2_x, pipe_y, pipe_w, pipe_h, label="2. MOTOR SEMÁNTICO", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid3)
    c_p2, _ = scene.add_quad_card(p2_x + 20.0, pipe_y + 50.0, pipe_w - 40.0, 160.0, "Análisis de Entidades", sublabel="Extracción de nodos, jerarquías y restricciones semánticas duras (IR Schema)", badge="SEMANTICS", icon="database", is_hero=True, font_size=18, frame_id=fid3)

    # PASO 3: SELECCIÓN ARQUETIPO
    p3_x = p2_x + pipe_w + 60.0
    scene.add_scope_container(p3_x, pipe_y, pipe_w, pipe_h, label="3. CATÁLOGO ARQUETIPOS", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c_p3, _ = scene.add_quad_card(p3_x + 20.0, pipe_y + 50.0, pipe_w - 40.0, 160.0, "Mapeo 20 Arquetipos", sublabel="Selección óptima entre A-T y los 27 tipos visuales + Archetype Fitness Score", badge="ARCHETYPE", icon="container", font_size=18, frame_id=fid3)

    # PASO 4: LAYOUT & TOKENS
    p4_x = p3_x + pipe_w + 60.0
    scene.add_scope_container(p4_x, pipe_y, pipe_w, pipe_h, label="4. MOTOR DE LAYOUT", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c_p4, _ = scene.add_quad_card(p4_x + 20.0, pipe_y + 50.0, pipe_w - 40.0, 160.0, "Cálculo Geométrico", sublabel="Gaps de 95px · Fuentes 18-20px · 1 Acento · Conectores ortogonales a 90°", badge="GEOMETRY", icon="server", font_size=18, frame_id=fid3)

    # PASO 5: VALIDADOR
    p5_x = p4_x + pipe_w + 60.0
    scene.add_scope_container(p5_x, pipe_y, pipe_w, pipe_h, label="5. VALIDADOR 6D", stroke=PALETTE["GREEN_BORDER"], bg=PALETTE["GREEN_BG"], frame_id=fid3)
    c_p5, _ = scene.add_quad_card(p5_x + 20.0, pipe_y + 50.0, pipe_w - 40.0, 160.0, "Quality Score (0-100)", sublabel="Inspección de solapamientos, densidad, legibilidad y tokens de marca", badge="VALIDATOR", icon="monitoring", is_hero=True, font_size=18, frame_id=fid3)

    # FLECHAS DEL FLUJO PRINCIPAL
    scene.add_arrow(p1_x + pipe_w, pipe_y + pipe_h * 0.5, p2_x, pipe_y + pipe_h * 0.5, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid3)
    scene.add_arrow(p2_x + pipe_w, pipe_y + pipe_h * 0.5, p3_x, pipe_y + pipe_h * 0.5, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, frame_id=fid3)
    scene.add_arrow(p3_x + pipe_w, pipe_y + pipe_h * 0.5, p4_x, pipe_y + pipe_h * 0.5, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid3)
    scene.add_arrow(p4_x + pipe_w, pipe_y + pipe_h * 0.5, p5_x, pipe_y + pipe_h * 0.5, stroke=PALETTE["GREEN_HERO"], stroke_w=2.5, frame_id=fid3)

    # BUCLE SUPERIOR DE AUTO-REPAIR (RECURSIÓN FINITA)
    repair_x = p4_x - 50.0
    repair_y = f3_y + 140.0
    repair_w = pipe_w + 100.0
    repair_h = 150.0
    scene.add_scope_container(repair_x, repair_y, repair_w, repair_h, label="BUCLE AUTÓNOMO DE AUTO-REPAIR (MÁX 3 CICLOS)", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid3)
    c_repair, _ = scene.add_quad_card(repair_x + 20.0, repair_y + 40.0, repair_w - 40.0, 95.0,
                                      "Algoritmo de Corrección Autónoma",
                                      sublabel="Degrada acentos sobrantes · Reajusta fuentes · Expande containers",
                                      badge="AUTO-REPAIR", icon="sync", is_hero=True, font_size=18, frame_id=fid3)

    # Flecha de Error hacia Auto-Repair (Sube desde el validador)
    scene.add_arrow(p5_x + pipe_w * 0.5, pipe_y, p5_x + pipe_w * 0.5, repair_y + repair_h * 0.5, stroke=PALETTE["CORAL_HERO"], stroke_w=2.0, label="¿Score < 90?", orthogonal=True, frame_id=fid3)
    scene.add_arrow(p5_x + pipe_w * 0.5, repair_y + repair_h * 0.5, repair_x + repair_w, repair_y + repair_h * 0.5, stroke=PALETTE["CORAL_HERO"], stroke_w=2.0, frame_id=fid3)

    # Flecha de Re-inyección desde Auto-Repair hacia Motor de Layout
    scene.add_arrow(repair_x, repair_y + repair_h * 0.5, p4_x + pipe_w * 0.5, repair_y + repair_h * 0.5, stroke=PALETTE["CORAL_HERO"], stroke_w=2.0, label="REAPLICAR REGLAS", orthogonal=True, frame_id=fid3)
    scene.add_arrow(p4_x + pipe_w * 0.5, repair_y + repair_h * 0.5, p4_x + pipe_w * 0.5, pipe_y, stroke=PALETTE["CORAL_HERO"], stroke_w=2.0, frame_id=fid3)

    # SALIDA FINAL INFERIOR (ARTEFACTO NATIVO)
    out_x = p5_x - 80.0
    out_y = pipe_y + pipe_h + 50.0
    out_w = pipe_w + 160.0
    out_h = 110.0
    scene.add_quad_card(out_x, out_y, out_w, out_h,
                        "ARTEFACTO .EXCALIDRAW FINAL",
                        sublabel="JSON nativo válido · 100% editable por el humano en el canvas",
                        badge="EDITABLE OUTPUT", icon="key", is_hero=True, font_size=18, frame_id=fid3)

    scene.add_arrow(p5_x + pipe_w * 0.5, pipe_y + pipe_h, p5_x + pipe_w * 0.5, out_y, stroke=PALETTE["GREEN_HERO"], stroke_w=2.5, label="PASS (>=90/100)", orthogonal=True, frame_id=fid3)

    scene.add_legend_footer(f3_x + 60.0, f3_y + 885.0, w3 - 120.0, swatches=[
        {"label": "Pipeline Principal de Inferencia", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Bucle de Auto-Repair Autónomo", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Artefacto Nativo Aprobado", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]}
    ], note="AI doesn't design from scratch · AI completes structured visual systems", frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)

    # =========================================================================
    # FRAME 4: ARQUETIPO G (ESCALERA 5 NIVELES) + MATRIZ DE HORIZONTES
    # =========================================================================
    w4, h4 = 2800.0, 980.0
    f4_x, f4_y = place(w4, h4)
    fid4 = scene.add_frame("FRAME 4: SKETION ROADMAP — ESCALERA DE 5 NIVELES & MATRIZ DE HORIZONTES", f4_x, f4_y, w4, h4)

    scene.add_text(f4_x + 60.0, f4_y + 35.0, "SKETION ROADMAP  ·  5-LEVEL MATURITY MODEL & HORIZONS", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid4)
    scene.add_text(f4_x + 60.0, f4_y + 60.0, "Modelo de Evolución: De Canvas de Dibujo a Plataforma de Inteligencia Visual", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid4)

    # PARTE SUPERIOR: ESCALERA DE MADUREZ DE 5 NIVELES (ARQUETIPO G / PIRÁMIDE)
    stair_y = f4_y + 115.0
    stair_w = (w4 - 120.0 - 4 * 25.0) / 5.0
    stair_h = 145.0

    levels = [
        {"lvl": "NIVEL 1: CANVAS", "desc": "Dibujo & Bocetado Libre", "badge": "DRAW", "hero": False},
        {"lvl": "NIVEL 2: WORKSPACE", "desc": "Docs + Notas + Fórmulas + Datos", "badge": "DOCS", "hero": False},
        {"lvl": "NIVEL 3: KNOWLEDGE", "desc": "Todo Conectado Espacialmente", "badge": "CONNECTED", "hero": False},
        {"lvl": "NIVEL 4: AI WORKSPACE", "desc": "IA que Estructura sin Reemplazar", "badge": "AI ASSIST", "hero": True},
        {"lvl": "NIVEL 5: VISUAL PLATFORM", "desc": "Prompt -> Sistema Visual Vivo", "badge": "INTELLIGENCE", "hero": True}
    ]

    for i, lv in enumerate(levels):
        lx = f4_x + 60.0 + i * (stair_w + 25.0)
        scene.add_quad_card(lx, stair_y, stair_w, stair_h, lv["lvl"], sublabel=lv["desc"], badge=lv["badge"], icon="laptop" if i < 3 else "key", is_hero=lv["hero"], font_size=18, frame_id=fid4)
        if i < 4:
            scene.add_arrow(lx + stair_w, stair_y + stair_h * 0.5, lx + stair_w + 25.0, stair_y + stair_h * 0.5, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, frame_id=fid4)

    # PARTE INFERIOR: MATRIZ DE 3 HORIZONTES VISUALMENTE CONTRASTADOS
    hz_y = stair_y + stair_h + 35.0
    hz_w = (w4 - 120.0 - 2 * 40.0) / 3.0
    hz_h = 540.0

    # HORIZONTE 1: DISPONIBLE HOY (PRODUCCIÓN LIVE) - VERDE
    hz1_x = f4_x + 60.0
    scene.add_scope_container(hz1_x, hz_y, hz_w, hz_h, label="🟢 HORIZONTE 1: DISPONIBLE HOY (LIVE PRODUCTION)", stroke=PALETTE["GREEN_BORDER"], bg=PALETTE["GREEN_BG"], frame_id=fid4)
    scene.add_quad_card(hz1_x + 25.0, hz_y + 50.0, hz_w - 50.0, 105.0, "Infinite Canvas & Core Tools", sublabel="Bocetos, formas vectoriales, zoom y pan fluido", badge="CANVAS", icon="laptop", font_size=18, frame_id=fid4)
    scene.add_quad_card(hz1_x + 25.0, hz_y + 170.0, hz_w - 50.0, 105.0, "Local-First Persistence", sublabel="IndexedDB con soporte offline y latencia cero", badge="LOCAL-FIRST", icon="database", is_hero=True, font_size=18, frame_id=fid4)
    scene.add_quad_card(hz1_x + 25.0, hz_y + 290.0, hz_w - 50.0, 105.0, "PDFs & KaTeX Math Nativo", sublabel="Texto interactivo y fórmulas matemáticas en canvas", badge="CORE ENGINES", icon="server", font_size=18, frame_id=fid4)
    scene.add_quad_card(hz1_x + 25.0, hz_y + 410.0, hz_w - 50.0, 105.0, "Study Mode & Flashcards Vivas", sublabel="Active recall directamente vinculado a los nodos", badge="STUDY", icon="users", font_size=18, frame_id=fid4)

    # HORIZONTE 2: EN CONSTRUCCIÓN (Q3-Q4) - AZUL
    hz2_x = hz1_x + hz_w + 40.0
    scene.add_scope_container(hz2_x, hz_y, hz_w, hz_h, label="🟡 HORIZONTE 2: EN CONSTRUCCIÓN (ROADMAP Q3-Q4)", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid4)
    scene.add_quad_card(hz2_x + 25.0, hz_y + 50.0, hz_w - 50.0, 105.0, "Premium Template Library", sublabel="Plantillas académicas, software y system design", badge="TEMPLATES", icon="container", font_size=18, frame_id=fid4)
    scene.add_quad_card(hz2_x + 25.0, hz_y + 170.0, hz_w - 50.0, 105.0, "Mermaid Interactivo Bidireccional", sublabel="Edición en vivo de código y representación visual", badge="MERMAID", icon="server", is_hero=True, font_size=18, frame_id=fid4)
    scene.add_quad_card(hz2_x + 25.0, hz_y + 290.0, hz_w - 50.0, 105.0, "Colab Sandbox & Code Runner", sublabel="Ejecución de snippets de código en el canvas", badge="SANDBOX", icon="laptop", font_size=18, frame_id=fid4)
    scene.add_quad_card(hz2_x + 25.0, hz_y + 410.0, hz_w - 50.0, 105.0, "Spatial Comments & Inbox", sublabel="Comentarios fijados a coordenadas y bandeja central", badge="COLLAB", icon="users", font_size=18, frame_id=fid4)

    # HORIZONTE 3: INVESTIGACIÓN & R&D - SLATE
    hz3_x = hz2_x + hz_w + 40.0
    scene.add_scope_container(hz3_x, hz_y, hz_w, hz_h, label="🔵 HORIZONTE 3: INVESTIGACIÓN & R&D (AI PLATFORM)", stroke=PALETTE["DARK_SLATE"], bg="#FFFFFF", frame_id=fid4)
    scene.add_quad_card(hz3_x + 25.0, hz_y + 50.0, hz_w - 50.0, 105.0, "AI Skill Engine (Sketion 4.0)", sublabel="Inferencia semántica, layout determinista y auto-repair", badge="AI CORE", icon="key", is_hero=True, font_size=18, frame_id=fid4)
    scene.add_quad_card(hz3_x + 25.0, hz_y + 170.0, hz_w - 50.0, 105.0, "AI-Assisted PDF Extraction", sublabel="Detección y extracción automática de tablas y fórmulas", badge="AI DOCS", icon="file", font_size=18, frame_id=fid4)
    scene.add_quad_card(hz3_x + 25.0, hz_y + 290.0, hz_w - 50.0, 105.0, "Knowledge Graph Automatizado", sublabel="Inferencia de relaciones conceptuales en el espacio", badge="GRAPH R&D", icon="database", font_size=18, frame_id=fid4)
    scene.add_quad_card(hz3_x + 25.0, hz_y + 410.0, hz_w - 50.0, 105.0, "Visual Intelligence Platform", sublabel="Nivel 5: Del prompt a artefactos visuales vivos", badge="LEVEL 5", icon="monitoring", is_hero=True, font_size=18, frame_id=fid4)

    scene.add_legend_footer(f4_x + 60.0, f4_y + 885.0, w4 - 120.0, swatches=[
        {"label": "Horizonte 1: Producción Live", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]},
        {"label": "Horizonte 2: Construcción Q3-Q4", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Horizonte 3: Investigación IA", "bg": "#FFFFFF", "stroke": PALETTE["DARK_SLATE"]}
    ], note="No confundir lo disponible hoy con la investigación · Honestidad de Producto Radical", frame_id=fid4)

    scene.auto_fit_frame(fid4, padding=50.0)

    # Guardar archivo
    out_file = os.path.join(OUT_DIR, "sketion_master_project.excalidraw")
    scene.save(out_file)
    print(f"\n[+] Tablero Sketion Master Project (Arquetipos Diversificados) guardado exitosamente en:\n    {out_file}")

    # Validaciones
    is_valid, report = validate_scene(out_file)
    print("\n" + report.summary())

    fit_score, fit_details = calculate_archetype_fitness(
        problem_domain="SKETION_MASTER_KNOWLEDGE_WORKSPACE",
        chosen_structures=["DUEL_AND_RADIAL_HUB", "HORIZONTAL_LAYER_STACK", "FLOW_PIPELINE_WITH_AUTO_REPAIR_LOOP", "MATURITY_STAIR_AND_HORIZONS"],
        covered_dimensions=["Identidad & Posicionamiento", "Hub Radial de Conocimiento", "Arquitectura Layer Stack", "Pipeline IA con Auto-Repair Loop", "Escalera 5 Niveles y Horizontes"],
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
    build_sketion_master_project()
