"""
Sketion 4.0 — Generador del Ecosistema Centralizado SEAMOS GENIOS
Paleta Editorial Calibrada:
- Acento Coral Suave / Ladrillo Editorial: #D93829
- Fondo suave de acento focal: #FFF5F2
- Fondo neutro tarjetas: #FFFFFF
- Bordes neutros: #E2E8F0
- Tinta negra pura: #0F172A
- Tipografía consistente: fontFamily=2 (Monospace / Clean Sans)
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
    "RED_HERO": "#D93829",       # Rojo suave / coral editorial
    "RED_BG": "#FFF5F2",         # Fondo suave editorial
    "RED_BORDER": "#FCA5A5",     # Borde suave
    "DARK_SLATE": "#1E293B",
    "LIGHT_PILL": "#F1F5F9"
}


def build_seamos_genios_ecosystem():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])
    
    # =========================================================================
    # FRAME 1: TOPOLOGÍA MACRO & TRANSICIÓN HACIA EL ECOSISTEMA UNIFICADO
    # =========================================================================
    w1, h1 = 2800.0, 960.0
    f1_x, f1_y = place(w1, h1)
    fid1 = scene.add_frame("FRAME 1: ECOSISTEMA CENTRALIZADO SEAMOS GENIOS — TOPOLOGÍA GENERAL", f1_x, f1_y, w1, h1)

    # Header Editorial (Sans/Mono fontFamily=2)
    scene.add_text(f1_x + 60.0, f1_y + 35.0, "SEAMOS GENIOS  ·  ARQUITECTURA DE ECOSISTEMA UNIFICADO", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "Ecosistema Centralizado: Web Pública · Supabase Auth · App Multi-Rol", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    # Chevron Ribbon Superior
    stages_f1 = ["1. CAPTACIÓN & WEB", "2. AUTENTICACIÓN CENTRAL", "3. BASE DE DATOS & RBAC", "4. PORTALES POR ROL", "5. FINANZAS & EXAMBUILDER"]
    scene.add_chevron_ribbon(f1_x + 60.0, f1_y + 115.0, w1 - 220.0, h=38.0, stages=stages_f1, bg=PALETTE["DARK_SLATE"], text_color="#FFFFFF", frame_id=fid1)

    # Rieles Verticales Laterales
    scene.add_vertical_rails(f1_x + w1 - 130.0, f1_y + 115.0, 70.0, 720.0, rails=[
        {"title": "SUPABASE CORE", "bg": PALETTE["RED_HERO"], "text_color": "#FFFFFF"},
        {"title": "ICFES ENGINE", "bg": PALETTE["DARK_SLATE"], "text_color": "#FFFFFF"},
        {"title": "SEGURIDAD RBAC", "bg": PALETTE["DARK_SLATE"], "text_color": "#FFFFFF"}
    ], frame_id=fid1)

    scope_y = f1_y + 175.0
    scope_h = 660.0

    # SCOPE 1.1: SITIO WEB CORPORATIVO (seamosgenios.org)
    sc1_w = 600.0
    sc1_x = f1_x + 60.0
    scene.add_scope_container(sc1_x, scope_y, sc1_w, scope_h, label="1. WEB CORPORATIVA (seamosgenios.org)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)
    
    c_web1, _ = scene.add_quad_card(sc1_x + 25.0, scope_y + 60.0, 260.0, 115.0, "Home & Hero", sublabel="Qué es · CTA · Login", badge="PUBLIC", icon="laptop", frame_id=fid1)
    c_web2, _ = scene.add_quad_card(sc1_x + 315.0, scope_y + 60.0, 260.0, 115.0, "Programas & Cursos", sublabel="Modalidad · Horarios", badge="PUBLIC", icon="file", frame_id=fid1)
    c_web3, _ = scene.add_quad_card(sc1_x + 25.0, scope_y + 195.0, 260.0, 115.0, "Resultados & Éxito", sublabel="Puntajes ICFES destacados", badge="PUBLIC", icon="monitoring", frame_id=fid1)
    c_web4, _ = scene.add_quad_card(sc1_x + 315.0, scope_y + 195.0, 260.0, 115.0, "Docentes & Alianzas", sublabel="Equipo · Colegios aliados", badge="PUBLIC", icon="users", frame_id=fid1)
    c_web5, _ = scene.add_quad_card(sc1_x + 25.0, scope_y + 330.0, 260.0, 115.0, "Planes y Precios", sublabel="Comparativas de planes", badge="SALES", icon="alert", frame_id=fid1)
    c_web6, _ = scene.add_quad_card(sc1_x + 315.0, scope_y + 330.0, 260.0, 115.0, "Pasarelas de Pago", sublabel="Wompi · ePayco · Bold", badge="PAY", icon="lock", frame_id=fid1)
    c_web7, _ = scene.add_quad_card(sc1_x + 25.0, scope_y + 465.0, 550.0, 95.0, "FAQ · Contacto · Legal", sublabel="Tratamiento de datos · Términos", badge="LEGAL", icon="file", frame_id=fid1)

    # SCOPE 1.2: AUTENTICACIÓN & CAPA CENTRAL (Supabase)
    sc2_w = 650.0
    sc2_x = sc1_x + sc1_w + 45.0
    scene.add_scope_container(sc2_x, scope_y, sc2_w, scope_h, label="2. AUTH & CAPA CENTRAL (SUPABASE)", stroke=PALETTE["RED_BORDER"], bg=PALETTE["RED_BG"], frame_id=fid1)

    c_auth, _ = scene.add_quad_card(sc2_x + 30.0, scope_y + 65.0, sc2_w - 60.0, 125.0, "Supabase Auth (/login)", sublabel="OAuth Google · Microsoft · Email / Pass", badge="AUTH", icon="key", is_hero=True, frame_id=fid1)
    c_db, _ = scene.add_quad_card(sc2_x + 30.0, scope_y + 215.0, sc2_w - 60.0, 125.0, "PostgreSQL Unificado", sublabel="Misma DB · Esquemas Segregados · RLS", badge="CORE DB", icon="postgres", is_hero=False, frame_id=fid1)
    c_storage, _ = scene.add_quad_card(sc2_x + 30.0, scope_y + 365.0, sc2_w - 60.0, 115.0, "Storage & Media Hub", sublabel="Grabaciones Meet · PDFs · Material", badge="STORAGE", icon="bucket", frame_id=fid1)
    c_gw, _ = scene.add_quad_card(sc2_x + 30.0, scope_y + 505.0, sc2_w - 60.0, 115.0, "Role Dispatcher (app.seamosgenios.org)", sublabel="Enrutamiento RBAC por perfil de usuario", badge="GATEWAY", icon="gateway", frame_id=fid1)

    # SCOPE 1.3: APP UNIFICADA POR ROLES (app.seamosgenios.org)
    sc3_w = 1200.0
    sc3_x = sc2_x + sc2_w + 45.0
    scene.add_scope_container(sc3_x, scope_y, sc3_w, scope_h, label="3. PLATAFORMA UNIFICADA (app.seamosgenios.org)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid1)

    c_r1, _ = scene.add_quad_card(sc3_x + 30.0, scope_y + 65.0, 540.0, 125.0, "Panel Estudiante (/app/student)", sublabel="Gamificación (XP/Rachas) · Desafíos · Simulacros", badge="ROL 1", icon="user", pills=["ICFES", "XP"], frame_id=fid1)
    c_r2, _ = scene.add_quad_card(sc3_x + 630.0, scope_y + 65.0, 540.0, 125.0, "Panel Padre de Familia (/app/parent)", sublabel="Seguimiento en vivo · Progreso · Recompensas", badge="ROL 2", icon="users", pills=["TRACK", "ALERT"], frame_id=fid1)
    c_r3, _ = scene.add_quad_card(sc3_x + 30.0, scope_y + 225.0, 540.0, 125.0, "Panel Directivo / Docente (/app/institution)", sublabel="KPIs · Top Estudiantes · Benchmark Nacional", badge="ROL 3", icon="monitoring", pills=["KPI", "DATA"], frame_id=fid1)
    c_r4, _ = scene.add_quad_card(sc3_x + 630.0, scope_y + 225.0, 540.0, 125.0, "Panel Administrador (/app/admin)", sublabel="ExamBuilder IA · Usuarios · Finanzas & Nómina", badge="ROL 4", icon="server", is_hero=False, pills=["EXAM", "ADMIN"], frame_id=fid1)

    # Módulos Estratégicos Inferiores
    c_emb, _ = scene.add_quad_card(sc3_x + 30.0, scope_y + 385.0, 540.0, 125.0, "ExamBuilder Estratégico", sublabel="Banco de Preguntas · Generador IA · Versionado", badge="INTERNAL", icon="terminal", is_hero=True, frame_id=fid1)
    c_fin, _ = scene.add_quad_card(sc3_x + 630.0, scope_y + 385.0, 540.0, 125.0, "Módulo de Finanzas & Facturación", sublabel="Facturación Electrónica · Liquidación Tutores", badge="FIN", icon="database", frame_id=fid1)
    c_pqrs, _ = scene.add_quad_card(sc3_x + 30.0, scope_y + 530.0, 1140.0, 95.0, "Sistema PQRS Centralizado & Asistencia Meet Automatizada", sublabel="Trazabilidad multi-rol de solicitudes y registro automático de asistencia en clases", badge="SHARED", icon="sync", frame_id=fid1)

    # Conexiones Ortogonales
    scene.add_arrow(c_web6["x"] + c_web6["width"], c_web6["y"] + c_web6["height"]*0.5, c_auth["x"], c_auth["y"] + 45.0, stroke=PALETTE["INK"], stroke_w=1.5, label="COMPRA / LOGIN", orthogonal=True, frame_id=fid1)
    scene.add_arrow(c_auth["x"] + c_auth["width"]*0.5, c_auth["y"] + c_auth["height"], c_db["x"] + c_db["width"]*0.5, c_db["y"], stroke=PALETTE["RED_HERO"], stroke_w=2.0, orthogonal=True, frame_id=fid1)
    scene.add_arrow(c_db["x"] + c_db["width"]*0.5, c_db["y"] + c_db["height"], c_gw["x"] + c_gw["width"]*0.5, c_gw["y"], stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid1)
    scene.add_arrow(c_gw["x"] + c_gw["width"], c_gw["y"] + 45.0, c_r1["x"], c_r1["y"] + c_r1["height"]*0.5, stroke=PALETTE["RED_HERO"], stroke_w=2.0, label="RBAC ROUTING", orthogonal=True, frame_id=fid1)

    # Leyenda Inferior
    scene.add_legend_footer(f1_x + 60.0, f1_y + 865.0, w1 - 220.0, swatches=[
        {"label": "Supabase Core & ExamBuilder (Hero)", "bg": PALETTE["RED_BG"], "stroke": PALETTE["RED_HERO"]},
        {"label": "Módulos de Negocio & Paneles", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]},
        {"label": "Flujo de Datos Autenticado", "is_arrow": True, "stroke": PALETTE["RED_HERO"]},
        {"label": "Enrutamiento RBAC", "is_arrow": True, "stroke": PALETTE["INK"]}
    ], note="Un único ecosistema · Una sola base de datos · ExamBuilder integrado en el Admin", frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=50.0)

    # =========================================================================
    # FRAME 2: DESGLOSE DETALLADO DE LOS 4 PANELES DE ROL
    # =========================================================================
    w2, h2 = 2800.0, 960.0
    f2_x, f2_y = place(w2, h2)
    fid2 = scene.add_frame("FRAME 2: ARQUITECTURA DETALLADA DE LOS 4 PANELES (/app/*)", f2_x, f2_y, w2, h2)

    scene.add_text(f2_x + 60.0, f2_y + 35.0, "SEAMOS GENIOS  ·  MATRIZ DE CAPACIDADES POR ROL", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid2)
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "Capacidades y Vistas: Estudiante · Padre · Directivo · Administrador", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    col_w = (w2 - 120.0 - 3 * 35.0) / 4.0
    col_y = f2_y + 120.0
    col_h = 770.0

    # COLUMNA 1: PANEL ESTUDIANTE
    c1_x = f2_x + 60.0
    scene.add_scope_container(c1_x, col_y, col_w, col_h, label="1. ESTUDIANTE (/app/student)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    scene.add_quad_card(c1_x + 20.0, col_y + 55.0, col_w - 40.0, 95.0, "Dashboard & Racha", sublabel="Progreso · Asistencia Meet · XP", badge="STUDENT", icon="user", frame_id=fid2)
    scene.add_quad_card(c1_x + 20.0, col_y + 165.0, col_w - 40.0, 95.0, "Calendario & Clases", sublabel="Enlace Meet · Tutor · Material", badge="CLASS", icon="file", frame_id=fid2)
    scene.add_quad_card(c1_x + 20.0, col_y + 275.0, col_w - 40.0, 95.0, "Grabaciones & Archivo", sublabel="PDF · Videos · Por área y tema", badge="MEDIA", icon="bucket", frame_id=fid2)
    scene.add_quad_card(c1_x + 20.0, col_y + 385.0, col_w - 40.0, 95.0, "Desafíos Gamificados", sublabel="Quizizz/Kahoot · Retos rápidos", badge="GAME", icon="alert", frame_id=fid2)
    scene.add_quad_card(c1_x + 20.0, col_y + 495.0, col_w - 40.0, 95.0, "Simulacros ICFES", sublabel="Mini · Completos · Diagnósticos", badge="EXAM", icon="monitoring", is_hero=True, frame_id=fid2)
    scene.add_quad_card(c1_x + 20.0, col_y + 605.0, col_w - 40.0, 115.0, "Recompensas & XP", sublabel="Spotify · Becas · Ranking escolar", badge="REWARD", icon="key", frame_id=fid2)

    # COLUMNA 2: PANEL PADRE DE FAMILIA
    c2_x = c1_x + col_w + 35.0
    scene.add_scope_container(c2_x, col_y, col_w, col_h, label="2. PADRE DE FAMILIA (/app/parent)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    scene.add_quad_card(c2_x + 20.0, col_y + 55.0, col_w - 40.0, 105.0, "Dashboard de Resumen", sublabel="Vista ejecutiva del estudiante", badge="PARENT", icon="users", frame_id=fid2)
    scene.add_quad_card(c2_x + 20.0, col_y + 175.0, col_w - 40.0, 105.0, "Seguimiento Integral", sublabel="Asistencia Meet · Tareas · Racha", badge="TRACK", icon="monitoring", frame_id=fid2)
    scene.add_quad_card(c2_x + 20.0, col_y + 295.0, col_w - 40.0, 105.0, "Resultados Simplificados", sublabel="Puntajes ICFES claros y gráficos", badge="METRIC", icon="file", frame_id=fid2)
    scene.add_quad_card(c2_x + 20.0, col_y + 415.0, col_w - 40.0, 105.0, "Calendario & Horarios", sublabel="Próximas clases y eventos", badge="AGENDA", icon="laptop", frame_id=fid2)
    scene.add_quad_card(c2_x + 20.0, col_y + 535.0, col_w - 40.0, 105.0, "Puntos & Recompensas", sublabel="Consulta de logros del hijo", badge="POINTS", icon="key", frame_id=fid2)
    scene.add_quad_card(c2_x + 20.0, col_y + 655.0, col_w - 40.0, 85.0, "PQRS Directo", sublabel="Atención y soporte familiar", badge="SUPPORT", icon="sync", frame_id=fid2)

    # COLUMNA 3: PANEL DIRECTIVO / DOCENTE
    c3_x = c2_x + col_w + 35.0
    scene.add_scope_container(c3_x, col_y, col_w, col_h, label="3. DIRECTIVO / DOCENTE (/app/institution)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    scene.add_quad_card(c3_x + 20.0, col_y + 55.0, col_w - 40.0, 105.0, "KPIs Institucionales", sublabel="Promedio general · Participación", badge="INSTITUTION", icon="monitoring", frame_id=fid2)
    scene.add_quad_card(c3_x + 20.0, col_y + 175.0, col_w - 40.0, 105.0, "Analítica de Simulacros", sublabel="Top alumnos · Áreas débiles", badge="ANALYTICS", icon="database", frame_id=fid2)
    scene.add_quad_card(c3_x + 20.0, col_y + 295.0, col_w - 40.0, 105.0, "Benchmark Nacional", sublabel="Comparativa colegios país / ICFES", badge="BENCHMARK", icon="server", is_hero=True, frame_id=fid2)
    scene.add_quad_card(c3_x + 20.0, col_y + 415.0, col_w - 40.0, 105.0, "Alertas Tempranas", sublabel="Estudiantes en riesgo académico", badge="ALERT", icon="alert", frame_id=fid2)
    scene.add_quad_card(c3_x + 20.0, col_y + 535.0, col_w - 40.0, 105.0, "Preguntas Críticas", sublabel="Análisis de preguntas de alto fallo", badge="DIAG", icon="file", frame_id=fid2)
    scene.add_quad_card(c3_x + 20.0, col_y + 655.0, col_w - 40.0, 85.0, "Asistencia por Grupos", sublabel="Filtro por área y curso", badge="REPORT", icon="users", frame_id=fid2)

    # COLUMNA 4: PANEL ADMINISTRADOR & EXAMBUILDER
    c4_x = c3_x + col_w + 35.0
    scene.add_scope_container(c4_x, col_y, col_w, col_h, label="4. ADMINISTRADOR (/app/admin)", stroke=PALETTE["RED_BORDER"], bg=PALETTE["RED_BG"], frame_id=fid2)
    scene.add_quad_card(c4_x + 20.0, col_y + 55.0, col_w - 40.0, 105.0, "Dashboard Ejecutivo", sublabel="KPIs globales de negocio e ingresos", badge="ADMIN", icon="monitoring", frame_id=fid2)
    scene.add_quad_card(c4_x + 20.0, col_y + 175.0, col_w - 40.0, 105.0, "EXAMBUILDER IA", sublabel="Banco de preguntas · Generador IA", badge="CORE TOOL", icon="terminal", is_hero=True, frame_id=fid2)
    scene.add_quad_card(c4_x + 20.0, col_y + 295.0, col_w - 40.0, 105.0, "Constructor de Pruebas", sublabel="Simulacros · Diagnósticos · Plantillas", badge="BUILDER", icon="file", frame_id=fid2)
    scene.add_quad_card(c4_x + 20.0, col_y + 415.0, col_w - 40.0, 105.0, "Gestión de Usuarios & Colegios", sublabel="CRUD Roles · Alianzas educativas", badge="RBAC", icon="users", frame_id=fid2)
    scene.add_quad_card(c4_x + 20.0, col_y + 535.0, col_w - 40.0, 105.0, "Módulo de Finanzas", sublabel="Facturación electrónica · Ingresos", badge="FINANCE", icon="lock", frame_id=fid2)
    scene.add_quad_card(c4_x + 20.0, col_y + 655.0, col_w - 40.0, 85.0, "Liquidación de Tutores", sublabel="Cálculo automático por horas Meet", badge="PAYROLL", icon="sync", frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=50.0)

    # =========================================================================
    # FRAME 3: MOTOR ESTRATÉGICO EXAMBUILDER & PIPELINE ICFES END-TO-END
    # =========================================================================
    w3, h3 = 2800.0, 960.0
    f3_x, f3_y = place(w3, h3)
    fid3 = scene.add_frame("FRAME 3: MOTOR EXAMBUILDER & FLUJO INTEGRAL DE EVALUACIÓN ICFES", f3_x, f3_y, w3, h3)

    scene.add_text(f3_x + 60.0, f3_y + 35.0, "SEAMOS GENIOS  ·  PIPELINE DE EVALUACIÓN Y ANALÍTICA", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid3)
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "Ciclo de Vida: Creación IA -> Presentación Estudiante -> Analítica Multi-Rol", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    # Ribbon Superior
    pipeline_stages = ["1. BANCO & IA", "2. ENSAMBLE & VERSIONADO", "3. RENDICIÓN ESTUDIANTE", "4. CALIFICACIÓN & ICFES", "5. REPORTES & BENCHMARK"]
    scene.add_chevron_ribbon(f3_x + 60.0, f3_y + 115.0, w3 - 120.0, h=38.0, stages=pipeline_stages, bg=PALETTE["DARK_SLATE"], text_color="#FFFFFF", frame_id=fid3)

    st_w = (w3 - 120.0 - 4 * 40.0) / 5.0
    st_y = f3_y + 175.0
    st_h = 680.0

    # ETAPA 1: BANCO & GENERADOR IA (ADMIN)
    x_e1 = f3_x + 60.0
    scene.add_scope_container(x_e1, st_y, st_w, st_h, label="1. CREACIÓN IA & BANCO", stroke=PALETTE["RED_BORDER"], bg=PALETTE["RED_BG"], frame_id=fid3)
    e1_c1, _ = scene.add_quad_card(x_e1 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Generador Asistido IA", sublabel="Creación · Validación · Corrección", badge="AI", icon="terminal", is_hero=True, frame_id=fid3)
    e1_c2, _ = scene.add_quad_card(x_e1 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Banco de Preguntas", sublabel="Áreas · Competencias · Dificultad", badge="DB", icon="database", is_hero=False, frame_id=fid3)
    e1_c3, _ = scene.add_quad_card(x_e1 + 20.0, st_y + 365.0, st_w - 40.0, 115.0, "Taxonomía ICFES", sublabel="Componentes y estándares MEN", badge="TAX", icon="file", frame_id=fid3)

    # ETAPA 2: CONSTRUCTOR & PUBLICACIÓN
    x_e2 = x_e1 + st_w + 40.0
    scene.add_scope_container(x_e2, st_y, st_w, st_h, label="2. CONSTRUCTOR DE PRUEBAS", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    e2_c1, _ = scene.add_quad_card(x_e2 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Constructor de Simulacros", sublabel="Completos · Mini · Diagnósticos", badge="BUILD", icon="server", frame_id=fid3)
    e2_c2, _ = scene.add_quad_card(x_e2 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Plantillas & Versionado", sublabel="Control de cambios y versiones", badge="VER", icon="container", frame_id=fid3)
    e2_c3, _ = scene.add_quad_card(x_e2 + 20.0, st_y + 365.0, st_w - 40.0, 115.0, "Asignación Institucional", sublabel="Colegios · Cursos · Fechas", badge="ASSIGN", icon="users", frame_id=fid3)

    # ETAPA 3: EJECUCIÓN ESTUDIANTE
    x_e3 = x_e2 + st_w + 40.0
    scene.add_scope_container(x_e3, st_y, st_w, st_h, label="3. RENDICIÓN EN VIVO", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    e3_c1, _ = scene.add_quad_card(x_e3 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Player de Simulacros", sublabel="Interfaz cronometrada ICFES", badge="PLAYER", icon="laptop", frame_id=fid3)
    e3_c2, _ = scene.add_quad_card(x_e3 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Guardado en Tiempo Real", sublabel="Autosave continuo en Supabase", badge="SAVE", icon="postgres", frame_id=fid3)
    e3_c3, _ = scene.add_quad_card(x_e3 + 20.0, st_y + 365.0, st_w - 40.0, 115.0, "Entrega & Sellado", sublabel="Cierre y registro de tiempo", badge="SUBMIT", icon="lock", frame_id=fid3)

    # ETAPA 4: CALIFICACIÓN & MOTOR ANALÍTICO
    x_e4 = x_e3 + st_w + 40.0
    scene.add_scope_container(x_e4, st_y, st_w, st_h, label="4. MOTOR DE CALIFICACIÓN", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    e4_c1, _ = scene.add_quad_card(x_e4 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Algoritmo de Ponderación", sublabel="Cálculo TRI y baremos ICFES", badge="TRI", icon="monitoring", frame_id=fid3)
    e4_c2, _ = scene.add_quad_card(x_e4 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Clasificación de Errores", sublabel="Detección de preguntas críticas", badge="DIAG", icon="alert", frame_id=fid3)
    e4_c3, _ = scene.add_quad_card(x_e4 + 20.0, st_y + 365.0, st_w - 40.0, 115.0, "Generador de XP & Puntos", sublabel="Abono de experiencia al perfil", badge="XP", icon="key", frame_id=fid3)

    # ETAPA 5: CONSUMO MULTI-ROL
    x_e5 = x_e4 + st_w + 40.0
    scene.add_scope_container(x_e5, st_y, st_w, st_h, label="5. DISTRIBUCIÓN POR ROL", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    e5_c1, _ = scene.add_quad_card(x_e5 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Estudiante & Padres", sublabel="Puntaje global · Desempeño", badge="VIEW 1", icon="user", frame_id=fid3)
    e5_c2, _ = scene.add_quad_card(x_e5 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Colegio & Docentes", sublabel="Benchmark · Alertas · Ranking", badge="VIEW 2", icon="users", is_hero=True, frame_id=fid3)
    e5_c3, _ = scene.add_quad_card(x_e5 + 20.0, st_y + 365.0, st_w - 40.0, 115.0, "Dirección Académica", sublabel="Reporte macro y mejora continua", badge="VIEW 3", icon="server", frame_id=fid3)

    # Flechas Inter-Etapa
    scene.add_arrow(e1_c2["x"] + e1_c2["width"], e1_c2["y"] + e1_c2["height"]*0.5, e2_c1["x"], e2_c1["y"] + e2_c1["height"]*0.5, stroke=PALETTE["RED_HERO"], stroke_w=2.0, orthogonal=True, frame_id=fid3)
    scene.add_arrow(e2_c3["x"] + e2_c3["width"], e2_c3["y"] + e2_c3["height"]*0.5, e3_c1["x"], e3_c1["y"] + e3_c1["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid3)
    scene.add_arrow(e3_c3["x"] + e3_c3["width"], e3_c3["y"] + e3_c3["height"]*0.5, e4_c1["x"], e4_c1["y"] + e4_c1["height"]*0.5, stroke=PALETTE["RED_HERO"], stroke_w=2.0, orthogonal=True, frame_id=fid3)
    scene.add_arrow(e4_c2["x"] + e4_c2["width"], e4_c2["y"] + e4_c2["height"]*0.5, e5_c2["x"], e5_c2["y"] + e5_c2["height"]*0.5, stroke=PALETTE["INK"], stroke_w=1.5, orthogonal=True, frame_id=fid3)

    # Leyenda Inferior Frame 3
    scene.add_legend_footer(f3_x + 60.0, f3_y + 865.0, w3 - 120.0, swatches=[
        {"label": "Creación IA / Módulos Focales", "bg": PALETTE["RED_BG"], "stroke": PALETTE["RED_HERO"]},
        {"label": "Etapas Estándar de Ejecución", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]},
        {"label": "Flujo Crítico de Evaluación", "is_arrow": True, "stroke": PALETTE["RED_HERO"]}
    ], note="ExamBuilder alimenta el motor de simulación · Supabase unifica la analítica multi-rol", frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)

    # Guardar archivo
    out_file = os.path.join(OUT_DIR, "seamos_genios_ecosistema_centralizado.excalidraw")
    scene.save(out_file)
    print(f"\n[+] Tablero Seamos Genios guardado exitosamente en:\n    {out_file}")
    
    # Validaciones
    is_valid, report = validate_scene(out_file)
    print("\n" + report.summary())

    fit_score, fit_details = calculate_archetype_fitness(
        problem_domain="EDTECH_ECOSYSTEM",
        chosen_structures=["ARCHITECTURE_ECOSYSTEM", "ROLE_PANEL_MATRIX", "PIPELINE_EXAMBUILDER"],
        covered_dimensions=["Web Corporativa", "Supabase Auth", "Roles 4 Paneles", "ExamBuilder IA", "Finanzas"],
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
    build_seamos_genios_ecosystem()
