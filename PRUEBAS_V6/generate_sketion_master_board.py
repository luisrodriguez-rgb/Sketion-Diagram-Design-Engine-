"""
Sketion 4.0 — Generador del Tablero Maestro de Visión y Arquitectura SKETION
Paleta: Azul Sketion (#2563EB), Azul Profundo (#1D4ED8), Blanco (#FFFFFF), Negro Tinta (#0F172A), Slate (#64748B), Verde (#059669), Coral (#D93829).
Frames:
- Frame 1: Identidad, Misión & El Gran Problema (Fragmentación vs. Sketion Workspace)
- Frame 2: Arquitectura del Sistema (Local-First, Canvas Engines & Cloud Backend)
- Frame 3: Sketion Intelligence — Pipeline Semántico y Motor de IA Estructurado
- Frame 4: Estado del Producto, Roadmap Oficial y los 5 Niveles de Evolución
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
    # FRAME 1: IDENTIDAD, POSICIONAMIENTO & EL DUELO DE LA FRAGMENTACIÓN
    # =========================================================================
    w1, h1 = 2800.0, 960.0
    f1_x, f1_y = place(w1, h1)
    fid1 = scene.add_frame("FRAME 1: SKETION MASTER — IDENTIDAD, POSICIONAMIENTO & EL GRAN PROBLEMA", f1_x, f1_y, w1, h1)

    scene.add_text(f1_x + 60.0, f1_y + 35.0, "SKETION MASTER PROJECT  ·  THINK. STRUCTURE. BUILD.", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "Sketion: The Visual Knowledge Workspace (Everything Connected. Everything Visual.)", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    stages_f1 = ["1. PROBLEMA: 10 APPS", "2. FRICCIÓN COGNITIVA", "3. CANVAS UNIFICADO", "4. KNOWLEDGE GRAPH", "5. CONTROL HUMANO"]
    scene.add_chevron_ribbon(f1_x + 60.0, f1_y + 115.0, w1 - 220.0, h=38.0, stages=stages_f1, bg=PALETTE["DARK_SLATE"], text_color="#FFFFFF", frame_id=fid1)

    scene.add_vertical_rails(f1_x + w1 - 130.0, f1_y + 115.0, 70.0, 720.0, rails=[
        {"title": "LOCAL-FIRST", "bg": PALETTE["BLUE_HERO"], "text_color": "#FFFFFF"},
        {"title": "KNOWLEDGE OS", "bg": PALETTE["DARK_SLATE"], "text_color": "#FFFFFF"},
        {"title": "AI STRUCTURE", "bg": PALETTE["DARK_SLATE"], "text_color": "#FFFFFF"}
    ], frame_id=fid1)

    scope_y = f1_y + 175.0
    scope_h = 660.0

    # SCOPE 1.1: REALIDAD ACTUAL (FRAGMENTACIÓN DE 6+ APPS)
    sc1_w = 1100.0
    sc1_x = f1_x + 60.0
    scene.add_scope_container(sc1_x, scope_y, sc1_w, scope_h, label="1. EL PROBLEMA ACTUAL: FRAGMENTACIÓN DE HERRAMIENTAS", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid1)

    card_w1 = 490.0
    scene.add_quad_card(sc1_x + 35.0, scope_y + 60.0, card_w1, 115.0, "PDFs en Adobe / Preview", sublabel="Texto muerto · Sin conexión a notas", badge="DOCS", icon="file", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc1_x + 565.0, scope_y + 60.0, card_w1, 115.0, "Notas en Notion / Docs", sublabel="Listas lineales · Sin espacialidad", badge="NOTES", icon="laptop", font_size=18, frame_id=fid1)
    
    scene.add_quad_card(sc1_x + 35.0, scope_y + 195.0, card_w1, 115.0, "Fórmulas en Overleaf / LaTeX", sublabel="Aislado de explicaciones visuales", badge="MATH", icon="server", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc1_x + 565.0, scope_y + 195.0, card_w1, 115.0, "Diagramas en Excalidraw", sublabel="Solo dibujo · Sin datos ni documentos", badge="DRAW", icon="container", font_size=18, frame_id=fid1)

    scene.add_quad_card(sc1_x + 35.0, scope_y + 330.0, card_w1, 115.0, "Datos en Excel / Sheets", sublabel="Tablas frías desconectadas de notas", badge="DATA", icon="database", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc1_x + 565.0, scope_y + 330.0, card_w1, 115.0, "Flashcards en Anki", sublabel="Preguntas aisladas del material original", badge="CARDS", icon="users", font_size=18, frame_id=fid1)

    scene.add_sticky_note(sc1_x + 35.0, scope_y + 465.0, 1020.0, 95.0, "CICLO DE FRICCIÓN CONSTANTE:\nOpen -> Switch -> Copy -> Paste -> Reorganize -> Switch Again (Pérdida del 40% del tiempo de estudio y desarrollo).", angle_deg=-0.5, font_size=14, frame_id=fid1)

    # SCOPE 1.2: SKETION UNIFIED WORKSPACE
    sc2_w = 1350.0
    sc2_x = sc1_x + sc1_w + 45.0
    scene.add_scope_container(sc2_x, scope_y, sc2_w, scope_h, label="2. SOLUCIÓN SKETION: VISUAL KNOWLEDGE WORKSPACE UNIFICADO", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid1)

    card_w2 = 615.0
    scene.add_quad_card(sc2_x + 35.0, scope_y + 60.0, card_w2, 115.0, "PDFs Interactivos con Overlays", sublabel="Capas de texto vivo sobre el lienzo", badge="PDF ENGINE", icon="file", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc2_x + 685.0, scope_y + 60.0, card_w2, 115.0, "Notas Conectadas Espaciales", sublabel="Nodos de conocimiento interrelacionados", badge="KNOWLEDGE GRAPH", icon="laptop", is_hero=True, font_size=18, frame_id=fid1)

    scene.add_quad_card(sc2_x + 35.0, scope_y + 195.0, card_w2, 115.0, "Renderizado Nativo de LaTeX", sublabel="Fórmulas vivas integradas al diagrama", badge="KATEX", icon="server", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc2_x + 685.0, scope_y + 195.0, card_w2, 115.0, "Mermaid & Diagramación Técnica", sublabel="Arquitectura de software y flujos lógicos", badge="MERMAID", icon="container", font_size=18, frame_id=fid1)

    scene.add_quad_card(sc2_x + 35.0, scope_y + 330.0, card_w2, 115.0, "Datasets & Gráficos en Vivo", sublabel="Importación CSV y Google Sheets en canvas", badge="DATA VIS", icon="database", font_size=18, frame_id=fid1)
    scene.add_quad_card(sc2_x + 685.0, scope_y + 330.0, card_w2, 115.0, "Study Mode & Flashcards Vivas", sublabel="Active recall nacido del propio canvas", badge="ACTIVE RECALL", icon="users", is_hero=True, font_size=18, frame_id=fid1)

    scene.add_quad_card(sc2_x + 35.0, scope_y + 465.0, 1265.0, 95.0, "Filosofía Central de IA", sublabel="AI should organize your thinking, not replace it · Generación estructurada de artefactos editables", badge="AI PHILOSOPHY", icon="key", font_size=18, frame_id=fid1)

    scene.add_arrow(sc1_x + sc1_w, scope_y + 250.0, sc2_x, scope_y + 250.0, stroke=PALETTE["BLUE_HERO"], stroke_w=2.5, label="UNIFICACIÓN ESPACIAL", orthogonal=True, frame_id=fid1)

    scene.add_legend_footer(f1_x + 60.0, f1_y + 865.0, w1 - 220.0, swatches=[
        {"label": "Sketion Knowledge Core", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Stack Legado / Fragmentación", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Conexión Unificada", "is_arrow": True, "stroke": PALETTE["BLUE_HERO"]}
    ], note="Knowledge shouldn't have to live in ten disconnected apps · Everything connected · Everything visual", frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=50.0)

    # =========================================================================
    # FRAME 2: ARQUITECTURA TÉCNICA (LOCAL-FIRST, CANVAS & CLOUD)
    # =========================================================================
    w2, h2 = 2800.0, 960.0
    f2_x, f2_y = place(w2, h2)
    fid2 = scene.add_frame("FRAME 2: ARQUITECTURA TÉCNICA — LOCAL-FIRST STACK & CLOUD SYNC", f2_x, f2_y, w2, h2)

    scene.add_text(f2_x + 60.0, f2_y + 35.0, "SKETION ARCHITECTURE  ·  LOCAL-FIRST & EDGE COMPUTING", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid2)
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "Arquitectura de la Aplicación: React 18 · Excalidraw Engine · IndexedDB · Supabase", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    stages_f2 = ["1. FRONTEND CORE", "2. CANVAS ENGINES", "3. LOCAL PERSISTENCE", "4. SUPABASE CLOUD", "5. REALTIME COLLAB"]
    scene.add_chevron_ribbon(f2_x + 60.0, f2_y + 115.0, w2 - 120.0, h=38.0, stages=stages_f2, bg=PALETTE["DARK_SLATE"], text_color="#FFFFFF", frame_id=fid2)

    st2_w = (w2 - 120.0 - 4 * 40.0) / 5.0
    st2_y = f2_y + 175.0
    st2_h = 680.0

    # COLUMNA 1: FRONTEND CORE
    x2_1 = f2_x + 60.0
    scene.add_scope_container(x2_1, st2_y, st2_w, st2_h, label="1. FRONTEND CORE", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    c2_1, _ = scene.add_quad_card(x2_1 + 20.0, st2_y + 65.0, st2_w - 40.0, 115.0, "React 18 & Vite", sublabel="Arquitectura modular rápida", badge="FRAMEWORK", icon="laptop", font_size=18, frame_id=fid2)
    c2_2, _ = scene.add_quad_card(x2_1 + 20.0, st2_y + 215.0, st2_w - 40.0, 115.0, "TypeScript Strict", sublabel="Tipado robusto end-to-end", badge="LANG", icon="server", font_size=18, frame_id=fid2)
    c2_3, _ = scene.add_quad_card(x2_1 + 20.0, st2_y + 365.0, st2_w - 40.0, 115.0, "Tailwind & Typography", sublabel="Outfit headings + Inter body", badge="UI", icon="file", font_size=18, frame_id=fid2)

    # COLUMNA 2: CANVAS ENGINES
    x2_2 = x2_1 + st2_w + 40.0
    scene.add_scope_container(x2_2, st2_y, st2_w, st2_h, label="2. CANVAS ENGINES", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid2)
    c2_4, _ = scene.add_quad_card(x2_2 + 20.0, st2_y + 65.0, st2_w - 40.0, 115.0, "Excalidraw Engine", sublabel="Lienzo infinito, zoom & pan", badge="CANVAS CORE", icon="container", is_hero=True, font_size=18, frame_id=fid2)
    c2_5, _ = scene.add_quad_card(x2_2 + 20.0, st2_y + 215.0, st2_w - 40.0, 115.0, "PDF.js Text Layer", sublabel="Renderizado de blobs y overlays", badge="PDF ENGINE", icon="file", font_size=18, frame_id=fid2)
    c2_6, _ = scene.add_quad_card(x2_2 + 20.0, st2_y + 365.0, st2_w - 40.0, 115.0, "KaTeX & Mermaid", sublabel="Ecuaciones y flujos en código", badge="MATH/FLOW", icon="database", font_size=18, frame_id=fid2)

    # COLUMNA 3: LOCAL PERSISTENCE (LOCAL-FIRST)
    x2_3 = x2_2 + st2_w + 40.0
    scene.add_scope_container(x2_3, st2_y, st2_w, st2_h, label="3. LOCAL-FIRST ENGINE", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    c2_7, _ = scene.add_quad_card(x2_3 + 20.0, st2_y + 65.0, st2_w - 40.0, 115.0, "IndexedDB (Dexie.js)", sublabel="Persistencia local sin latencia", badge="STORAGE", icon="database", is_hero=True, font_size=18, frame_id=fid2)
    c2_8, _ = scene.add_quad_card(x2_3 + 20.0, st2_y + 215.0, st2_w - 40.0, 115.0, "Offline Resilience", sublabel="Funciona 100% sin internet", badge="OFFLINE", icon="lock", font_size=18, frame_id=fid2)
    c2_9, _ = scene.add_quad_card(x2_3 + 20.0, st2_y + 365.0, st2_w - 40.0, 115.0, "State Rehydration", sublabel="Recuperación instantánea de sesión", badge="STATE", icon="sync", font_size=18, frame_id=fid2)

    # COLUMNA 4: CLOUD & SYNC BACKEND
    x2_4 = x2_3 + st2_w + 40.0
    scene.add_scope_container(x2_4, st2_y, st2_w, st2_h, label="4. SUPABASE BACKEND", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    c2_10, _ = scene.add_quad_card(x2_4 + 20.0, st2_y + 65.0, st2_w - 40.0, 115.0, "Supabase Auth & RLS", sublabel="Seguridad por fila y roles", badge="AUTH", icon="key", font_size=18, frame_id=fid2)
    c2_11, _ = scene.add_quad_card(x2_4 + 20.0, st2_y + 215.0, st2_w - 40.0, 115.0, "PostgreSQL Database", sublabel="Almacén de proyectos y boards", badge="POSTGRES", icon="database", font_size=18, frame_id=fid2)
    c2_12, _ = scene.add_quad_card(x2_4 + 20.0, st2_y + 365.0, st2_w - 40.0, 115.0, "Supabase Storage", sublabel="Gestión de PDFs y activos binarios", badge="STORAGE", icon="server", font_size=18, frame_id=fid2)

    # COLUMNA 5: REALTIME & DEPLOY
    x2_5 = x2_4 + st2_w + 40.0
    scene.add_scope_container(x2_5, st2_y, st2_w, st2_h, label="5. REALTIME & INFRA", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    c2_13, _ = scene.add_quad_card(x2_5 + 20.0, st2_y + 65.0, st2_w - 40.0, 115.0, "Socket.IO Collab", sublabel="Colaboración multiusuario en vivo", badge="REALTIME", icon="sync", font_size=18, frame_id=fid2)
    c2_14, _ = scene.add_quad_card(x2_5 + 20.0, st2_y + 215.0, st2_w - 40.0, 115.0, "Vercel Edge Network", sublabel="Despliegue global de baja latencia", badge="HOSTING", icon="server", font_size=18, frame_id=fid2)
    c2_15, _ = scene.add_quad_card(x2_5 + 20.0, st2_y + 365.0, st2_w - 40.0, 115.0, "VitePress Docs", sublabel="Documentación viva indexada", badge="DOCS", icon="file", font_size=18, frame_id=fid2)

    # Conexiones Ortogonales
    scene.add_arrow(c2_1["x"] + c2_1["width"], c2_1["y"] + c2_1["height"]*0.5, c2_4["x"], c2_4["y"] + c2_4["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid2)
    scene.add_arrow(c2_4["x"] + c2_4["width"], c2_4["y"] + c2_4["height"]*0.5, c2_7["x"], c2_7["y"] + c2_7["height"]*0.5, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, label="LOCAL WRITE", orthogonal=True, frame_id=fid2)
    scene.add_arrow(c2_7["x"] + c2_7["width"], c2_7["y"] + c2_7["height"]*0.5, c2_11["x"], c2_11["y"] + c2_11["height"]*0.5, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, label="ASYNC SYNC", orthogonal=True, frame_id=fid2)
    scene.add_arrow(c2_11["x"] + c2_11["width"], c2_11["y"] + c2_11["height"]*0.5, c2_13["x"], c2_13["y"] + c2_13["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid2)

    scene.add_legend_footer(f2_x + 60.0, f2_y + 865.0, w2 - 120.0, swatches=[
        {"label": "Núcleo de Ejecución Local", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Módulos de Infraestructura", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]},
        {"label": "Sincronización Local-to-Cloud", "is_arrow": True, "stroke": PALETTE["BLUE_HERO"]}
    ], note="Your workspace should remain useful even when the network doesn't · Local-First Architecture", frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=50.0)

    # =========================================================================
    # FRAME 3: SKETION INTELLIGENCE — EL PIPELINE SEMÁNTICO DE IA
    # =========================================================================
    w3, h3 = 2800.0, 960.0
    f3_x, f3_y = place(w3, h3)
    fid3 = scene.add_frame("FRAME 3: SKETION INTELLIGENCE — PIPELINE SEMÁNTICO & AUTO-REPAIR", f3_x, f3_y, w3, h3)

    scene.add_text(f3_x + 60.0, f3_y + 35.0, "SKETION INTELLIGENCE  ·  STRUCTURED AI DIAGRAMMING ENGINE", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid3)
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "De Lenguaje Natural a Artefactos Nativos Editables (.excalidraw)", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    stages_f3 = ["1. PROMPT USUARIO", "2. ANÁLISIS SEMÁNTICO", "3. SELECCIÓN ARQUETIPO", "4. GEOMETRÍA & LAYOUT", "5. AUTO-REPAIR & RENDER"]
    scene.add_chevron_ribbon(f3_x + 60.0, f3_y + 115.0, w3 - 120.0, h=38.0, stages=stages_f3, bg=PALETTE["DARK_SLATE"], text_color="#FFFFFF", frame_id=fid3)

    st3_w = (w3 - 120.0 - 4 * 40.0) / 5.0
    st3_y = f3_y + 175.0
    st3_h = 680.0

    # PASO 1: ENTRADA
    x3_1 = f3_x + 60.0
    scene.add_scope_container(x3_1, st3_y, st3_w, st3_h, label="1. INPUT BRUTO", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c3_1, _ = scene.add_quad_card(x3_1 + 20.0, st3_y + 65.0, st3_w - 40.0, 120.0, "Prompt Desestructurado", sublabel="Texto en lenguaje natural o brief", badge="INPUT", icon="laptop", font_size=18, frame_id=fid3)
    c3_2, _ = scene.add_quad_card(x3_1 + 20.0, st3_y + 225.0, st3_w - 40.0, 120.0, "Documentos / PDFs", sublabel="Contenido técnico o requerimientos", badge="CONTEXT", icon="file", font_size=18, frame_id=fid3)
    c3_3, _ = scene.add_quad_card(x3_1 + 20.0, st3_y + 385.0, st3_w - 40.0, 120.0, "Perfil de Audiencia", sublabel="CEO · Ops · Tech · Data · Pitch", badge="AUDIENCE", icon="users", font_size=18, frame_id=fid3)

    # PASO 2: SEMANTIC ENGINE
    x3_2 = x3_1 + st3_w + 40.0
    scene.add_scope_container(x3_2, st3_y, st3_w, st3_h, label="2. MOTOR SEMÁNTICO", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid3)
    c3_4, _ = scene.add_quad_card(x3_2 + 20.0, st3_y + 65.0, st3_w - 40.0, 120.0, "Extracción de Entidades", sublabel="Nodos, relaciones y dependencias", badge="ENTITIES", icon="database", is_hero=True, font_size=18, frame_id=fid3)
    c3_5, _ = scene.add_quad_card(x3_2 + 20.0, st3_y + 225.0, st3_w - 40.0, 120.0, "Hard Constraints", sublabel="Restricciones lógicas innegociables", badge="RULES", icon="lock", font_size=18, frame_id=fid3)
    c3_6, _ = scene.add_quad_card(x3_2 + 20.0, st3_y + 385.0, st3_w - 40.0, 120.0, "Intermediate Rep (IR)", sublabel="Esquema JSON desacoplado", badge="SCHEMA", icon="server", font_size=18, frame_id=fid3)

    # PASO 3: SELECCIÓN DE ARQUETIPO
    x3_3 = x3_2 + st3_w + 40.0
    scene.add_scope_container(x3_3, st3_y, st3_w, st3_h, label="3. CATÁLOGO ARQUETIPOS", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c3_7, _ = scene.add_quad_card(x3_3 + 20.0, st3_y + 65.0, st3_w - 40.0, 120.0, "20 Arquetipos (A - T)", sublabel="Cerebro · Fases · Duelo · Planta", badge="ARCHETYPES", icon="container", font_size=18, frame_id=fid3)
    c3_8, _ = scene.add_quad_card(x3_3 + 20.0, st3_y + 225.0, st3_w - 40.0, 120.0, "27 Tipos Visuales", sublabel="Medallion · 2x2 · Sequence · Swimlane", badge="TYPES", icon="file", font_size=18, frame_id=fid3)
    c3_9, _ = scene.add_quad_card(x3_3 + 20.0, st3_y + 385.0, st3_w - 40.0, 120.0, "Archetype Fitness Test", sublabel="Evaluación de adecuación estructural", badge="FITNESS", icon="monitoring", is_hero=True, font_size=18, frame_id=fid3)

    # PASO 4: LAYOUT & DESIGN TOKENS
    x3_4 = x3_3 + st3_w + 40.0
    scene.add_scope_container(x3_4, st3_y, st3_w, st3_h, label="4. MOTOR DE LAYOUT", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    c3_10, _ = scene.add_quad_card(x3_4 + 20.0, st3_y + 65.0, st3_w - 40.0, 120.0, "Gaps & Gutters (95/65px)", sublabel="Espaciado editorial anti-amontonamiento", badge="GRID", icon="container", font_size=18, frame_id=fid3)
    c3_11, _ = scene.add_quad_card(x3_4 + 20.0, st3_y + 225.0, st3_w - 40.0, 120.0, "Tipografía Proporcional", sublabel="18-20px en tarjetas · 14px en tablas", badge="FONTS", icon="file", font_size=18, frame_id=fid3)
    c3_12, _ = scene.add_quad_card(x3_4 + 20.0, st3_y + 385.0, st3_w - 40.0, 120.0, "1 Accent Rule (Focal)", sublabel="Exactamente 1 héroe con acento", badge="PALETTE", icon="key", font_size=18, frame_id=fid3)

    # PASO 5: VALIDACIÓN & REPARACIÓN
    x3_5 = x3_4 + st3_w + 40.0
    scene.add_scope_container(x3_5, st3_y, st3_w, st3_h, label="5. VALIDACIÓN 6D", stroke=PALETTE["GREEN_BORDER"], bg=PALETTE["GREEN_BG"], frame_id=fid3)
    c3_13, _ = scene.add_quad_card(x3_5 + 20.0, st3_y + 65.0, st3_w - 40.0, 120.0, "Quality Score (0-100)", sublabel="Estructura · Layout · Jerarquía · Ruido", badge="QUALITY", icon="monitoring", is_hero=True, font_size=18, frame_id=fid3)
    c3_14, _ = scene.add_quad_card(x3_5 + 20.0, st3_y + 225.0, st3_w - 40.0, 120.0, "Bucle de Auto-Repair", sublabel="Corrección autónoma sin intervención", badge="REPAIR", icon="sync", font_size=18, frame_id=fid3)
    c3_15, _ = scene.add_quad_card(x3_5 + 20.0, st3_y + 385.0, st3_w - 40.0, 120.0, "Artefacto .excalidraw", sublabel="100% nativo y editable por el usuario", badge="OUTPUT", icon="laptop", font_size=18, frame_id=fid3)

    # Conexiones Ortogonales
    scene.add_arrow(c3_1["x"] + c3_1["width"], c3_1["y"] + c3_1["height"]*0.5, c3_4["x"], c3_4["y"] + c3_4["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid3)
    scene.add_arrow(c3_6["x"] + c3_6["width"], c3_6["y"] + c3_6["height"]*0.5, c3_7["x"], c3_7["y"] + c3_7["height"]*0.5, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, label="MAP ARQUETIPO", orthogonal=True, frame_id=fid3)
    scene.add_arrow(c3_9["x"] + c3_9["width"], c3_9["y"] + c3_9["height"]*0.5, c3_10["x"], c3_10["y"] + c3_10["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, label="CALC GEOMETRÍA", orthogonal=True, frame_id=fid3)
    scene.add_arrow(c3_12["x"] + c3_12["width"], c3_12["y"] + c3_12["height"]*0.5, c3_13["x"], c3_13["y"] + c3_13["height"]*0.5, stroke=PALETTE["GREEN_HERO"], stroke_w=2.0, label="VALIDATE & PASS", orthogonal=True, frame_id=fid3)

    scene.add_legend_footer(f3_x + 60.0, f3_y + 865.0, w3 - 120.0, swatches=[
        {"label": "Motor Semántico & Extracción", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Validador 6D & Auto-Repair", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]},
        {"label": "Flujo de Síntesis Inteligente", "is_arrow": True, "stroke": PALETTE["BLUE_HERO"]}
    ], note="AI doesn't design from scratch · AI completes structured visual systems", frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)

    # =========================================================================
    # FRAME 4: ESTADO DEL PRODUCTO, ROADMAP Y LOS 5 NIVELES DE EVOLUCIÓN
    # =========================================================================
    w4, h4 = 2800.0, 960.0
    f4_x, f4_y = place(w4, h4)
    fid4 = scene.add_frame("FRAME 4: SKETION EVOLUTION — ESTADO ACTUAL, ROADMAP & 5 NIVELES", f4_x, f4_y, w4, h4)

    scene.add_text(f4_x + 60.0, f4_y + 35.0, "SKETION ROADMAP  ·  PRODUCT HORIZONS & MATURITY LEVELS", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid4)
    scene.add_text(f4_x + 60.0, f4_y + 60.0, "Horizontes de Producto: De un Canvas Extendido a la Plataforma de Inteligencia Visual", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid4)

    stages_f4 = ["NIVEL 1: CANVAS (DRAW)", "NIVEL 2: WORKSPACE (DOCS)", "NIVEL 3: KNOWLEDGE (CONNECTED)", "NIVEL 4: AI WORKSPACE (ASSIST)", "NIVEL 5: VISUAL INTELLIGENCE"]
    scene.add_chevron_ribbon(f4_x + 60.0, f4_y + 115.0, w4 - 120.0, h=38.0, stages=stages_f4, bg=PALETTE["DARK_SLATE"], text_color="#FFFFFF", frame_id=fid4)

    col4_w = (w4 - 120.0 - 2 * 45.0) / 3.0
    col4_y = f4_y + 175.0
    col4_h = 680.0

    # COLUMNA 1: DISPONIBLE HOY (LIVE)
    x4_1 = f4_x + 60.0
    scene.add_scope_container(x4_1, col4_y, col4_w, col4_h, label="🟢 1. DISPONIBLE HOY (LIVE PRODUCTION)", stroke=PALETTE["GREEN_BORDER"], bg=PALETTE["GREEN_BG"], frame_id=fid4)
    scene.add_quad_card(x4_1 + 25.0, col4_y + 55.0, col4_w - 50.0, 105.0, "Infinite Canvas & Drawing Core", sublabel="Bocetos, formas, conectores y zoom fluido", badge="CANVAS", icon="laptop", font_size=18, frame_id=fid4)
    scene.add_quad_card(x4_1 + 25.0, col4_y + 175.0, col4_w - 50.0, 105.0, "Local-First Persistence", sublabel="IndexedDB con soporte offline completo", badge="LOCAL", icon="database", is_hero=True, font_size=18, frame_id=fid4)
    scene.add_quad_card(x4_1 + 25.0, col4_y + 295.0, col4_w - 50.0, 105.0, "PDF Workspace & Text Overlays", sublabel="Importación y anotación espacial", badge="PDFS", icon="file", font_size=18, frame_id=fid4)
    scene.add_quad_card(x4_1 + 25.0, col4_y + 415.0, col4_w - 50.0, 105.0, "LaTeX Math & KaTeX Nativo", sublabel="Fórmulas matemáticas integradas", badge="MATH", icon="server", font_size=18, frame_id=fid4)
    scene.add_quad_card(x4_1 + 25.0, col4_y + 535.0, col4_w - 50.0, 105.0, "Study Mode & Flashcards Vivas", sublabel="Active recall ligado al canvas", badge="STUDY", icon="users", is_hero=True, font_size=18, frame_id=fid4)

    # COLUMNA 2: EN CONSTRUCCIÓN (BUILDING)
    x4_2 = x4_1 + col4_w + 45.0
    scene.add_scope_container(x4_2, col4_y, col4_w, col4_h, label="🟡 2. EN CONSTRUCCIÓN (ROADMAP Q3-Q4)", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid4)
    scene.add_quad_card(x4_2 + 25.0, col4_y + 55.0, col4_w - 50.0, 105.0, "Premium Template Library", sublabel="Plantillas universitarias y de arquitectura", badge="TEMPLATES", icon="container", font_size=18, frame_id=fid4)
    scene.add_quad_card(x4_2 + 25.0, col4_y + 175.0, col4_w - 50.0, 105.0, "Mermaid Workflows Interactivos", sublabel="Edición bidireccional código <-> visual", badge="MERMAID", icon="server", is_hero=True, font_size=18, frame_id=fid4)
    scene.add_quad_card(x4_2 + 25.0, col4_y + 295.0, col4_w - 50.0, 105.0, "Google Colab & Code Sandbox", sublabel="Ejecución de snippets en vivo en canvas", badge="CODE", icon="laptop", font_size=18, frame_id=fid4)
    scene.add_quad_card(x4_2 + 25.0, col4_y + 415.0, col4_w - 50.0, 105.0, "Presenter Mode & PPTX Export", sublabel="De frames a presentaciones ejecutivas", badge="PRESENT", icon="file", font_size=18, frame_id=fid4)
    scene.add_quad_card(x4_2 + 25.0, col4_y + 535.0, col4_w - 50.0, 105.0, "Spatial Comments & Inbox", sublabel="Comentarios anclados a coordenadas", badge="COLLAB", icon="users", font_size=18, frame_id=fid4)

    # COLUMNA 3: EN INVESTIGACIÓN (R&D / IA)
    x4_3 = x4_2 + col4_w + 45.0
    scene.add_scope_container(x4_3, col4_y, col4_w, col4_h, label="🔵 3. EN INVESTIGACIÓN (AI ENGINE & R&D)", stroke=PALETTE["DARK_SLATE"], bg="#FFFFFF", frame_id=fid4)
    scene.add_quad_card(x4_3 + 25.0, col4_y + 55.0, col4_w - 50.0, 105.0, "AI Skill Engine (Sketion 4.0)", sublabel="Comprensión semántica y auto-repair", badge="AI CORE", icon="key", is_hero=True, font_size=18, frame_id=fid4)
    scene.add_quad_card(x4_3 + 25.0, col4_y + 175.0, col4_w - 50.0, 105.0, "AI-Assisted PDF Workflows", sublabel="Extracción automática de fórmulas y gráficos", badge="AI DOCS", icon="file", font_size=18, frame_id=fid4)
    scene.add_quad_card(x4_3 + 25.0, col4_y + 295.0, col4_w - 50.0, 105.0, "Knowledge Graph Automatizado", sublabel="Descubrimiento de conexiones semánticas", badge="GRAPH", icon="database", font_size=18, frame_id=fid4)
    scene.add_quad_card(x4_3 + 25.0, col4_y + 415.0, col4_w - 50.0, 105.0, "Plugin Ecosystem & SDK", sublabel="Extensiones de terceros sobre el canvas", badge="PLUGINS", icon="server", font_size=18, frame_id=fid4)
    scene.add_quad_card(x4_3 + 25.0, col4_y + 535.0, col4_w - 50.0, 105.0, "Visual Intelligence Platform", sublabel="Nivel 5: Prompt -> Sistema Visual Vivo", badge="LEVEL 5", icon="monitoring", is_hero=True, font_size=18, frame_id=fid4)

    scene.add_legend_footer(f4_x + 60.0, f4_y + 865.0, w4 - 120.0, swatches=[
        {"label": "Disponible Hoy (Producción)", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]},
        {"label": "En Construcción Activa", "bg": PALETTE["BLUE_BG"], "stroke": PALETTE["BLUE_HERO"]},
        {"label": "Investigación & Plataforma IA", "bg": "#FFFFFF", "stroke": PALETTE["DARK_SLATE"]}
    ], note="No confundir lo que ya existe con lo que se está construyendo · Honestidad de Producto Radical", frame_id=fid4)

    scene.auto_fit_frame(fid4, padding=50.0)

    # Guardar archivo
    out_file = os.path.join(OUT_DIR, "sketion_master_project.excalidraw")
    scene.save(out_file)
    print(f"\n[+] Tablero Sketion Master Project guardado exitosamente en:\n    {out_file}")

    # Validaciones
    is_valid, report = validate_scene(out_file)
    print("\n" + report.summary())

    fit_score, fit_details = calculate_archetype_fitness(
        problem_domain="SKETION_MASTER_KNOWLEDGE_WORKSPACE",
        chosen_structures=["DUEL_VS_FRAGMENTATION", "LOCAL_FIRST_STACK_ARCHITECTURE", "STRUCTURED_AI_PIPELINE", "PRODUCT_HORIZONS_ROADMAP"],
        covered_dimensions=["Identidad & Posicionamiento", "El Problema de Fragmentación", "Arquitectura Local-First", "Sketion Intelligence Engine", "Estado del Producto & Roadmap 5 Niveles"],
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
