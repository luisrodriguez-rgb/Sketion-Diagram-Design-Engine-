"""
Sketion Master Generator — Showcase de Arquetipos Visuales Miro en Excalidraw Nativo
Genera demostraciones en .excalidraw de:
1. Miro D: El Duelo (Antes vs Después con Espina de Stickies Amarillos)
2. Miro B: Las Fases (Roadmap con Numerales Gigantes y Entregables)
3. Miro A: El Cerebro (Hub Central con Ramas, Métricas y Banner de Remate)
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place, compute_card_dimensions
from validation.validator import validate_scene

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V3")
os.makedirs(OUT_DIR, exist_ok=True)

MIRO_PALETTE = {
    "CANVAS": "#F4F4F4",
    "CARD": "#FFFFFF",
    "CARD_BORDER": "#BDBDBD",
    "INK": "#0C0C0C",
    "MUTED": "#9A9A9A",
    "STICKY": "#FFE95C",
    "PAIN_RED": "#E03A2F",
    "PAIN_BG": "#FDEFEF",
    "PAIN_BORDER": "#F05A5A",
    "BANNER_PINK": "#F5BEC0",
    "PASTEL_BLUE": "#9BC7E4",
    "PASTEL_GREEN": "#C2E5D3"
}


def build_duelo_excalidraw():
    """Genera la composición Arquetipo D · EL DUELO (Before vs After)."""
    place_reset(max_row_w=4000, gap=150)
    scene = ExcalidrawScene(roughness=0, bg_color=MIRO_PALETTE["CANVAS"])
    
    w, h = 2600, 1100
    fx, fy = place(w, h)
    fid = scene.add_frame("EL DUELO: Arquitectura Tradicional vs Sistema Moderno", fx, fy, w, h)

    # 1. Cabecera Masiva
    scene.add_text(fx + 60, fy + 40, "LA ARQUITECTURA DEL QUE IMPROVISA", font_size=15, font_family=2, color="#8B8B8B", frame_id=fid)
    scene.add_text(fx + 60, fy + 65, "LEGACY MONOLITH", font_size=42, font_family=2, color="#666666", frame_id=fid)

    scene.add_text(fx + w * 0.5 - 40, fy + 60, "VS", font_size=48, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid)

    scene.add_text(fx + w * 0.5 + 140, fy + 40, "LA ARQUITECTURA DEL QUE TIENE", font_size=15, font_family=2, color="#8B8B8B", frame_id=fid)
    scene.add_text(fx + w * 0.5 + 140, fy + 65, "SISTEMA DISTRIBUIDO", font_size=42, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid)

    # Sub-banner negro central
    scene.add_banner(fx + 100, fy + 145, w - 200, 44,
                     "los dos procesan pedidos. los dos cobran. solo uno puede escalar 100x sin caerse.",
                     bg=MIRO_PALETTE["INK"], text_color="#FFFFFF", font_size=15, frame_id=fid)

    # 2. Espina Central con Stickies Amarillos y Filas Enfrentadas
    categories = [
        ("DE QUÉ HABLO / GESTIÓN", "DEPLOYMENTS", "Despliegues manuales los viernes con 3 horas de downtime", "CI/CD automatizado en segundos con zero-downtime canary"),
        ("CUÁNDO ESCALO / CARGA", "CONCURRENCIA", "Bloqueo de tabla entera en SQL; cuelgue con 50 usuarios", "Locks distribuidos en Redis (120s TTL) y RLS atómico"),
        ("DÓNDE GUARDO / DATOS", "ALMACENAMIENTO", "Todo en una sola BD; si cae la BD, cae el negocio entero", "Microservicios aislados con Event Sourcing en Kafka"),
        ("CÓMO ME ENTERO / LOGS", "MONITORIZACIÓN", "Nos enteramos de los errores cuando el cliente llama gritando", "Alertas en tiempo real con OpenTelemetry, Datadog y APM"),
        ("CUÁNTO CUESTA / COSTES", "INFRAESTRUCTURA", "Servidores dedicados pagados 24/7 al 100% de capacidad", "Auto-scaling serverless pagando solo por milisegundo de uso")
    ]

    spine_x = fx + w * 0.5 - 120
    card_w = 850
    card_h = 75
    start_y = fy + 220
    row_gap = 20

    for i, (cat_label, tag, left_text, right_text) in enumerate(categories):
        cy = start_y + i * (card_h + row_gap)
        
        # Tarjeta Izquierda (Gris / Dolor)
        lx = spine_x - card_w - 30
        scene.add_bound_card(lx, cy, card_w, card_h, left_text,
                             bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"],
                             text_color="#666666", font_size=14, align="right", frame_id=fid)
        
        # Sticky Central Amarillo (-1.5 a +1.5 deg)
        rot = -1.5 if i % 2 == 0 else 1.5
        scene.add_sticky_note(spine_x, cy + 10, 240, 55, tag,
                              bg=MIRO_PALETTE["STICKY"], stroke=MIRO_PALETTE["INK"],
                              font_size=13, angle_deg=rot, frame_id=fid)
        
        # Tarjeta Derecha (Coral / Solución)
        rx = spine_x + 240 + 30
        scene.add_bound_card(rx, cy, card_w, card_h, right_text,
                             bg=MIRO_PALETTE["PAIN_BG"], stroke=MIRO_PALETTE["PAIN_BORDER"],
                             text_color=MIRO_PALETTE["INK"], font_size=14, align="left", frame_id=fid)

    # 3. Métricas de Comparación al Pie
    stats_y = start_y + len(categories) * (card_h + row_gap) + 30
    
    # Métricas Izquierda
    scene.add_chip(fx + 250, stats_y, 160, 95, "31 h", "Downtime / Año", bg="#FFFFFF", text_color="#666666", frame_id=fid)
    scene.add_chip(fx + 440, stats_y, 160, 95, "5 min", "Latencia P99", bg="#FFFFFF", text_color="#666666", frame_id=fid)
    scene.add_chip(fx + 630, stats_y, 160, 95, "4.2%", "Tasa Errores", bg="#FFFFFF", text_color="#666666", frame_id=fid)

    # Métricas Derecha
    scene.add_chip(fx + w - 790, stats_y, 160, 95, "99.99%", "Disponibilidad", bg=MIRO_PALETTE["PAIN_BG"], text_color=MIRO_PALETTE["PAIN_RED"], frame_id=fid)
    scene.add_chip(fx + w - 600, stats_y, 160, 95, "12 ms", "Latencia P99", bg=MIRO_PALETTE["PAIN_BG"], text_color=MIRO_PALETTE["PAIN_RED"], frame_id=fid)
    scene.add_chip(fx + w - 410, stats_y, 160, 95, "0.01%", "Tasa Errores", bg=MIRO_PALETTE["PAIN_BG"], text_color=MIRO_PALETTE["PAIN_RED"], frame_id=fid)

    # 4. Slots de Captura de Evidencia al Fondo
    slots_y = stats_y + 130
    scene.add_capture_slot(fx + 100, slots_y, 700, 160, label="Captura de Logs de Error en Monolito (Antes)", frame_id=fid)
    scene.add_capture_slot(fx + w - 800, slots_y, 700, 160, label="Dashboard de Datadog en Microservicios (Después)", frame_id=fid)

    scene.auto_fit_frame(fid, padding=60.0)
    
    out_path = os.path.join(OUT_DIR, "arquetipo_duelo_before_after.excalidraw")
    scene.save(out_path)
    return out_path


def build_cerebro_excalidraw():
    """Genera la composición Arquetipo A · EL CEREBRO."""
    place_reset(max_row_w=4000, gap=150)
    scene = ExcalidrawScene(roughness=0, bg_color=MIRO_PALETTE["CANVAS"])
    
    w, h = 2600, 1200
    fx, fy = place(w, h)
    fid = scene.add_frame("EL CEREBRO: Toda la Plataforma en un Solo Hub Central", fx, fy, w, h)

    # Cabecera
    scene.add_text(fx + 60, fy + 40, "TU PLATAFORMA ENTERA DENTRO DEL CORE", font_size=38, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid)
    scene.add_text(fx + 60, fy + 90, "un solo motor central, cuatro salidas operativas, cero cuellos de botella", font_size=20, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid)

    # Top Metric Pills
    scene.add_metric_pill(fx + w - 500, fy + 40, "DISPONIBILIDAD", "99.99%", bg=MIRO_PALETTE["INK"], frame_id=fid)
    scene.add_metric_pill(fx + w - 280, fy + 40, "TENANTS", "1,400+", bg=MIRO_PALETTE["INK"], frame_id=fid)

    # Hub Central Negro
    hub_x = fx + w * 0.5 - 120
    hub_y = fy + 160
    scene.add_ellipse(hub_x, hub_y, 240, 140, bg=MIRO_PALETTE["INK"], stroke=MIRO_PALETTE["INK"], frame_id=fid)
    scene.add_text(hub_x + 30, hub_y + 40, "CORE ENGINE\nMulti-Tenant Kernel", font_size=18, font_family=2, color="#FFFFFF", frame_id=fid)

    # 4 Ramas Temáticas
    branches = [
        ("1. RESERVAS & SLOTS", ["Hold atómico 120s en Redis", "Bloqueo por mesa y turno", "Capacidad y aforos dinámicos"], "+35% Ocupación", fx + 80),
        ("2. PAGOS & STRIPE", ["Tokenización de tarjeta PCI", "Depósito no reembolsable", "Facturación B2B automática"], "99.8% Cobro", fx + 680),
        ("3. MENSAJERÍA ASYNC", ["Confirmación por WhatsApp", "Recordatorio SMS 2h antes", "Email con enlace de cancelación"], "0.2% No-Show", fx + 1280),
        ("4. ANALÍTICA OLAP", ["Cálculo de rotación de mesas", "Ticket medio por canal", "Detección de horas valle"], "+24% Margen", fx + 1880)
    ]

    branch_y = fy + 380
    for title, items, stat_text, bx in branches:
        # Línea conectora desde el Hub
        scene.add_line(hub_x + 120, hub_y + 140, bx + 220, branch_y - 30, stroke=MIRO_PALETTE["MUTED"], dashed=True, frame_id=fid)
        
        # Cabecera de Categoría (Círculo/Pastilla)
        scene.add_bound_card(bx, branch_y - 20, 440, 45, title,
                             bg=MIRO_PALETTE["PASTEL_BLUE"], stroke=MIRO_PALETTE["INK"],
                             text_color=MIRO_PALETTE["INK"], font_size=14, frame_id=fid)
        
        # Tarjetas de acción apiladas
        for j, itm in enumerate(items):
            iy = branch_y + 40 + j * 60
            scene.add_bound_card(bx, iy, 440, 50, itm,
                                 bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"],
                                 text_color=MIRO_PALETTE["INK"], font_size=13, align="left", frame_id=fid)
        
        # Chip de estadística al pie de la rama
        stat_y = branch_y + 40 + len(items) * 60 + 15
        scene.add_bound_card(bx + 70, stat_y, 300, 45, stat_text,
                             bg=MIRO_PALETTE["INK"], stroke=MIRO_PALETTE["INK"],
                             text_color="#FFFFFF", font_size=15, frame_id=fid)

    # Banner inferior de Remate (Pink Punchline)
    banner_y = fy + 720
    scene.add_banner(fx + 100, banner_y, w - 200, 55,
                     "no son cuatro herramientas aisladas. es un cerebro unificado que sincroniza el restaurante en tiempo real.",
                     bg=MIRO_PALETTE["BANNER_PINK"], text_color=MIRO_PALETTE["INK"], font_size=16, frame_id=fid)

    # Cadena de Prueba al fondo (3 slots de captura)
    slots_y = banner_y + 85
    scene.add_text(fx + 100, slots_y, "CADENA DE PRUEBA Y EVIDENCIA VISUAL", font_size=13, font_family=3, color=MIRO_PALETTE["MUTED"], frame_id=fid)
    scene.add_capture_slot(fx + 100, slots_y + 25, 750, 160, label="Captura de Pantalla: El Dashboard en Vivo", frame_id=fid)
    scene.add_capture_slot(fx + 920, slots_y + 25, 750, 160, label="Captura de Pantalla: Notificación en WhatsApp", frame_id=fid)
    scene.add_capture_slot(fx + 1740, slots_y + 25, 750, 160, label="Captura de Pantalla: Informe de Conversión", frame_id=fid)

    scene.auto_fit_frame(fid, padding=60.0)

    out_path = os.path.join(OUT_DIR, "arquetipo_cerebro_hub_central.excalidraw")
    scene.save(out_path)
    return out_path


def build_fases_excalidraw():
    """Genera la composición Arquetipo B · LAS FASES (Roadmap con Numerales Gigantes)."""
    place_reset(max_row_w=4000, gap=150)
    scene = ExcalidrawScene(roughness=0, bg_color=MIRO_PALETTE["CANVAS"])
    
    w, h = 2600, 1300
    fx, fy = place(w, h)
    fid = scene.add_frame("LAS FASES: Roadmap de 90 Días con Entregables", fx, fy, w, h)

    # Cabecera
    scene.add_text(fx + 60, fy + 40, "ROADMAP 90 DÍAS: DE 0 A TU PRIMER SISTEMA", font_size=38, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid)
    scene.add_text(fx + 60, fy + 90, "seis fases, una por quincena, con entregables obligatorios sin saltarte ninguna", font_size=20, font_family=2, color=MIRO_PALETTE["PAIN_RED"], frame_id=fid)

    # Top Metric Pills
    scene.add_metric_pill(fx + w - 520, fy + 40, "DURACIÓN", "90 días", bg=MIRO_PALETTE["INK"], frame_id=fid)
    scene.add_metric_pill(fx + w - 320, fy + 40, "HORAS/SEM", "6 h", bg=MIRO_PALETTE["INK"], frame_id=fid)

    # Grilla 2 Columnas x 3 Filas
    fases = [
        ("1", "FUNDAMENTOS Y CONTEXTO", "días 1-15", ["Escribir context.md con qué vendo y a quién", "Subir 10 llamadas reales de clientes", "Configurar RBAC y multi-tenancy base"], "ENTREGABLE: Contexto estructurado que funciona en cualquier chat", 0, 0),
        ("2", "VISIBILIDAD Y AUTORIDAD", "días 16-30", ["Definir 6 bloques de contenido temático", "7 piezas/semana con el mismo mensaje", "Grabar 1 video largo por quincena"], "ENTREGABLE: 30 piezas programadas que se entienden como una sola idea", 1, 0),
        ("3", "VALIDACIÓN CON CLIENTES", "días 31-45", ["10 conversaciones con clientes reales", "Identificar los 3 dolores más repetidos", "Escribir la promesa en 15 palabras"], "ENTREGABLE: Oferta validada con frase de promesa que la gente asiente", 0, 1),
        ("4", "PRIMERAS VENTAS & COBRO", "días 46-60", ["Lanzar beta cerrada a precio de validación", "Grabar llamadas para feedback directo", "Ajustar onboarding según errores"], "ENTREGABLE: Dinero cobrado y primeras 5 personas usando el sistema", 1, 1),
        ("5", "ESCALADO DE OPERACIÓN", "días 61-75", ["Automatizar facturación con Stripe", "Workers asíncronos para notificaciones", "Monitoreo de latencia y logs con APM"], "ENTREGABLE: Sistema procesando pedidos en automático sin intervención", 0, 2),
        ("6", "DELEGACIÓN Y AUTONOMÍA", "días 76-90", ["Cada tarea repetida se convierte en skill", "Dashboard de métricas en tiempo real", "Guardias de soporte y alertas P0"], "ENTREGABLE: Negocio funcionando el día que el fundador no trabaja", 1, 2)
    ]

    grid_start_y = fy + 160
    col_w = 1180
    row_h = 240
    gap_x = 80
    gap_y = 35

    for num, title, subtitle, bullets, deliverable, col_idx, row_idx in fases:
        bx = fx + 60 + col_idx * (col_w + gap_x)
        by = grid_start_y + row_idx * (row_h + gap_y)

        # Numeral Gigante
        num_x = bx + 20
        scene.add_text(num_x, by + 20, "FASE", font_size=13, font_family=2, color=MIRO_PALETTE["MUTED"], frame_id=fid)
        scene.add_text(num_x - 5, by + 45, num, font_size=72, font_family=2, color=MIRO_PALETTE["INK"], frame_id=fid)

        # Contenedor de la Fase (Dashed Box)
        box_x = num_x + 90
        box_w = col_w - 110
        scene.add_rect(box_x, by, box_w, row_h, bg="#FFFFFF", stroke=MIRO_PALETTE["CARD_BORDER"], stroke_w=1.5, stroke_style="dashed", roundness_type=3, frame_id=fid)

        # Badge de Título Pastel
        scene.add_bound_card(box_x + 15, by + 15, 340, 36, title,
                             bg=MIRO_PALETTE["PASTEL_BLUE"], stroke=MIRO_PALETTE["INK"],
                             text_color=MIRO_PALETTE["INK"], font_size=12, frame_id=fid)
        scene.add_text(box_x + 370, by + 24, subtitle, font_size=12, font_family=2, color=MIRO_PALETTE["MUTED"], frame_id=fid)

        # Bullets de Acción
        for bi, bullet in enumerate(bullets):
            scene.add_text(box_x + 20, by + 65 + bi * 28, f"• {bullet}", font_size=13, font_family=2, color="#333333", frame_id=fid)

        # Barra de Entregable Rojo al Pie
        scene.add_banner(box_x + 15, by + row_h - 48, box_w - 30, 34, deliverable,
                         bg=MIRO_PALETTE["PAIN_BG"], text_color=MIRO_PALETTE["PAIN_RED"], font_size=12, frame_id=fid)

    scene.auto_fit_frame(fid, padding=60.0)

    out_path = os.path.join(OUT_DIR, "arquetipo_fases_roadmap_90dias.excalidraw")
    scene.save(out_path)
    return out_path


if __name__ == "__main__":
    p1 = build_duelo_excalidraw()
    p2 = build_cerebro_excalidraw()
    p3 = build_fases_excalidraw()
    print("==================================================")
    print("DEMOS DE ARQUETIPOS EDITORIALES MIRO GENERADAS:")
    print(f"1. {p1}")
    print(f"2. {p2}")
    print(f"3. {p3}")
    print("==================================================")
