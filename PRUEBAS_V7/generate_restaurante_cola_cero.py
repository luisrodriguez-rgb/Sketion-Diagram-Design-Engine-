"""
Sketion 4.0 — Generador del Tablero Estratégico: Startup Cola Cero para Restaurantes
Suite PRUEBAS_V7:
- Frame 1: Arquetipo D (El Duelo VS: El Caos Tradicional de Hora Pico vs Ecosistema Cola Cero)
- Frame 2: Arquetipo E (Swimlanes Operativos: Cliente Móvil, Smart Dispatcher, KDS Cocina, Salón & Mesas)
- Frame 3: Arquetipo C (Flow Pipeline con Bucle Autónomo de Control de Capacidad & Saturación de Cocina)
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from validation.validator import validate_scene
from validation.fitness_score import calculate_archetype_fitness

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V7")
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
    "CORAL_BG": "#FFF5F2",
    "CORAL_BORDER": "#FCA5A5",
    "DARK_SLATE": "#1E293B",
    "STICKY": "#FFE95C"
}


def build_restaurante_cola_cero():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])

    # =========================================================================
    # FRAME 1: ARQUETIPO D — EL DUELO VS (CAOS TRADICIONAL VS COLA CERO)
    # =========================================================================
    w1, h1 = 2800.0, 960.0
    f1_x, f1_y = place(w1, h1)
    fid1 = scene.add_frame("FRAME 1: EL DUELO — DIAGNÓSTICO DEL DOLOR VS SOLUCIÓN COLA CERO", f1_x, f1_y, w1, h1)

    scene.add_text(f1_x + 60.0, f1_y + 35.0, "RESTAURANT QUEUE OPTIMIZATION  ·  THE DUEL (VS) ARCHETYPE", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid1)
    scene.add_text(f1_x + 60.0, f1_y + 60.0, "De Filas de 35 Minutos y Caos en Cocina a Flujo Continuo con Pedidos Anticipados", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid1)

    duel_y = f1_y + 120.0
    duel_h = 740.0
    half_w = (w1 - 120.0 - 50.0) * 0.5

    # LADO IZQUIERDO: EL DOLOR ACTUAL (STACK FRAGMENTADO & FILA FÍSICA)
    dx1 = f1_x + 60.0
    scene.add_scope_container(dx1, duel_y, half_w, duel_h, label="1. MODELO TRADICIONAL (FILA FÍSICA & HORAS PICO EN ROJO)", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid1)

    c_f1 = (half_w - 70.0) * 0.5
    scene.add_quad_card(dx1 + 25.0, duel_y + 55.0, c_f1, 105.0, "Fila Lenta en Caja", sublabel="15-25 mins de espera física", badge="BOTTLENECK 1", icon="user", font_size=18, frame_id=fid1)
    scene.add_quad_card(dx1 + 25.0 + c_f1 + 20.0, duel_y + 55.0, c_f1, 105.0, "Abandono de Clientes", sublabel="35% de comensales se van", badge="CHURN", icon="alert", is_hero=True, font_size=18, frame_id=fid1)

    scene.add_quad_card(dx1 + 25.0, duel_y + 180.0, c_f1, 105.0, "Comandas en Papel / Gritos", sublabel="12% de errores en platos", badge="BOTTLENECK 2", icon="file", font_size=18, frame_id=fid1)
    scene.add_quad_card(dx1 + 25.0 + c_f1 + 20.0, duel_y + 180.0, c_f1, 105.0, "Espera de Pie en Pasillos", sublabel="Aglomeración y roce físico", badge="FRICTION", icon="users", font_size=18, frame_id=fid1)

    scene.add_quad_card(dx1 + 25.0, duel_y + 305.0, half_w - 50.0, 105.0, "Caos y Desorden en Mesas", sublabel="Mesas de 4 ocupadas por 1 persona · Clientes con bandejas buscando dónde sentarse", badge="BOTTLENECK 3", icon="container", font_size=18, frame_id=fid1)

    scene.add_sticky_note(dx1 + 25.0, duel_y + 440.0, half_w - 50.0, 120.0,
                          "DIAGNÓSTICO DEL IMPACTO EN HORA PICO:\n• Pérdida de hasta $4.5M COP / mes por clientes que abandonan la fila.\n• Rotación lenta: cada mesa tarda 50 minutos (35 mins esperando comida + 15 comiendo).\n• Estrés extremo en personal de cocina y quejas constantes.",
                          angle_deg=-1.0, font_size=14, frame_id=fid1)

    # LADO DERECHO: LA SOLUCIÓN COLA CERO (VERDE ESMERALDA)
    dx2 = dx1 + half_w + 50.0
    scene.add_scope_container(dx2, duel_y, half_w, duel_h, label="2. SOLUCIÓN COLA CERO (PRE-ORDEN, KDS & MESAS SINCRONIZADAS)", stroke=PALETTE["GREEN_BORDER"], bg=PALETTE["GREEN_BG"], frame_id=fid1)

    scene.add_quad_card(dx2 + 25.0, duel_y + 55.0, c_f1, 105.0, "Pre-Orden por WhatsApp", sublabel="Menú interactivo antes de llegar", badge="WHATSAPP BOT", icon="laptop", font_size=18, frame_id=fid1)
    scene.add_quad_card(dx2 + 25.0 + c_f1 + 20.0, duel_y + 55.0, c_f1, 105.0, "Pago Digital Instantáneo", sublabel="Wompi / Bold / PSE anticipado", badge="PAYMENT", icon="lock", font_size=18, frame_id=fid1)

    scene.add_quad_card(dx2 + 25.0, duel_y + 180.0, c_f1, 105.0, "KDS Cocina Sincronizado", sublabel="Cocción programada por ETA", badge="KDS DISPLAY", icon="server", font_size=18, frame_id=fid1)
    scene.add_quad_card(dx2 + 25.0 + c_f1 + 20.0, duel_y + 180.0, c_f1, 105.0, "Asignación Inteligente de Mesa", sublabel="Bloqueo automático de mesa", badge="TABLE DISPATCH", icon="database", font_size=18, frame_id=fid1)

    scene.add_quad_card(dx2 + 25.0, duel_y + 305.0, half_w - 50.0, 105.0, "Llegada Express: Cero Espera de Pie", sublabel="El cliente se sienta directamente en su mesa asignada con su plato servido en <3 mins", badge="ZERO QUEUE", icon="key", is_hero=True, font_size=18, frame_id=fid1)

    scene.add_bound_card(dx2 + 25.0, duel_y + 440.0, half_w - 50.0, 120.0,
                         "RESULTADOS ESPERADOS CON COLA CERO:\n" +
                         "✔ Rotación de mesa acelerada: de 50 min a 20 min (+150% capacidad real).\n" +
                         "✔ Abandono de fila reducido a 0% (todos pagan antes de llegar).\n" +
                         "✔ Cero errores de comanda: transmisión 100% digital al KDS de cocina.",
                         bg="#FFFFFF", stroke=PALETTE["GREEN_BORDER"], text_color=PALETTE["INK"],
                         font_size=14, roundness_type=3, frame_id=fid1)

    # Flecha central de transición
    scene.add_arrow(dx1 + half_w, duel_y + 200.0, dx2, duel_y + 200.0, stroke=PALETTE["GREEN_HERO"], stroke_w=3.0, label="TRANSICIÓN DIGITAL", frame_id=fid1)

    scene.add_legend_footer(f1_x + 60.0, f1_y + 885.0, w1 - 120.0, swatches=[
        {"label": "Cuellos de Botella & Abandono (Dolor)", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Solución Cola Cero (Hero)", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]},
        {"label": "Componentes de Transición", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]}
    ], note="No compitas por metros cuadrados · Optimiza los minutos de rotación de cada mesa", frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=50.0)

    # =========================================================================
    # FRAME 2: ARQUETIPO E — SWIMLANES OPERATIVOS DE PLANTA (4 CARRILES)
    # =========================================================================
    w2, h2 = 2800.0, 960.0
    f2_x, f2_y = place(w2, h2)
    fid2 = scene.add_frame("FRAME 2: ARQUETIPO E — SWIMLANES OPERATIVOS END-TO-END", f2_x, f2_y, w2, h2)

    scene.add_text(f2_x + 60.0, f2_y + 35.0, "OPERATIONAL SWIMLANES  ·  MULTI-ACTOR SYNCHRONIZATION", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid2)
    scene.add_text(f2_x + 60.0, f2_y + 60.0, "Sincronización Operativa: Del Pedido en WhatsApp a la Mesa Servida", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid2)

    swim_w = w1 - 120.0
    swim_x = f2_x + 60.0
    swim_start_y = f2_y + 115.0
    swim_h = 170.0
    swim_gap = 20.0

    # 4 SWIMLANES HORIZONTALES
    # CARRIL 1: CLIENTE (MÓVIL / WHATSAPP)
    s1_y = swim_start_y
    scene.add_scope_container(swim_x, s1_y, swim_w, swim_h, label="1. CLIENTE (DESDE OFICINA / EN CAMINO VÍA WHATSAPP)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    c_sw = (swim_w - 40.0 - 3 * 30.0) / 4.0
    scene.add_quad_card(swim_x + 20.0, s1_y + 40.0, c_sw, 110.0, "1. Abre WhatsApp Bot", sublabel="Explora menú digital interactivo", badge="DISCOVERY", icon="laptop", font_size=18, frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0 + c_sw + 30.0, s1_y + 40.0, c_sw, 110.0, "2. Personaliza & Paga", sublabel="Pago digital y selección de hora ETA", badge="CHECKOUT", icon="lock", font_size=18, frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0 + 2*(c_sw + 30.0), s1_y + 40.0, c_sw, 110.0, "3. Recibe Confirmación", sublabel="WhatsApp: 'Orden aceptada · Mesa #4'", badge="NOTIF", icon="sync", font_size=18, frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0 + 3*(c_sw + 30.0), s1_y + 40.0, c_sw, 110.0, "4. Llega y se Sienta", sublabel="Check-in con QR y comida servida", badge="ZERO WAIT", icon="key", is_hero=True, font_size=18, frame_id=fid2)

    # CARRIL 2: SMART DISPATCHER (MOTOR CLOUD DE CAPACIDAD)
    s2_y = s1_y + swim_h + swim_gap
    scene.add_scope_container(swim_x, s2_y, swim_w, swim_h, label="2. SMART DISPATCHER (MOTOR INTELIGENTE DE CAPACIDAD & COLAS)", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0, s2_y + 40.0, c_sw, 110.0, "Validador de Capacidad", sublabel="Calcula saturación actual de cocina", badge="LOAD BALANCER", icon="monitoring", font_size=18, frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0 + c_sw + 30.0, s2_y + 40.0, c_sw, 110.0, "Calculador de ETA", sublabel="Sincroniza tiempo de cocción vs llegada", badge="ETA ENGINE", icon="server", font_size=18, frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0 + 2*(c_sw + 30.0), s2_y + 40.0, c_sw, 110.0, "Asignador de Mesa", sublabel="Bloquea mesa según número de puestos", badge="TABLE ALLOC", icon="database", font_size=18, frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0 + 3*(c_sw + 30.0), s2_y + 40.0, c_sw, 110.0, "Disparador de Alertas", sublabel="Push a WhatsApp cuando plato sale", badge="WEBHOOK", icon="sync", font_size=18, frame_id=fid2)

    # CARRIL 3: COCINA & KDS (PREPARACIÓN SINCRONIZADA)
    s3_y = s2_y + swim_h + swim_gap
    scene.add_scope_container(swim_x, s3_y, swim_w, swim_h, label="3. COCINA & KDS (PREPARACIÓN JUST-IN-TIME)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0, s3_y + 40.0, c_sw, 110.0, "Recepción en Pantalla", sublabel="Orden aparece con cronómetro ETA", badge="KDS SCREEN", icon="laptop", font_size=18, frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0 + c_sw + 30.0, s3_y + 40.0, c_sw, 110.0, "Batching Inteligente", sublabel="Agrupa platos similares para ahorrar gas/tiempo", badge="BATCHING", icon="container", font_size=18, frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0 + 2*(c_sw + 30.0), s3_y + 40.0, c_sw, 110.0, "Cocción Just-In-Time", sublabel="El plato sale caliente en el minuto exacto", badge="COOKING", icon="file", font_size=18, frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0 + 3*(c_sw + 30.0), s3_y + 40.0, c_sw, 110.0, "Marcado 'Listo para Servir'", sublabel="Notifica a salón y actualiza estado", badge="DONE", icon="key", font_size=18, frame_id=fid2)

    # CARRIL 4: SALÓN & MESAS (PUNTO FÍSICO)
    s4_y = s3_y + swim_h + swim_gap
    scene.add_scope_container(swim_x, s4_y, swim_w, swim_h, label="4. SALÓN, MESAS & RETIRO EXPRESS (EXPERIENCIA FÍSICA)", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0, s4_y + 40.0, c_sw, 110.0, "Sensor / Estado de Mesas", sublabel="Monitorea mesas libres vs ocupadas", badge="FLOOR MAP", icon="container", font_size=18, frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0 + c_sw + 30.0, s4_y + 40.0, c_sw, 110.0, "Preparación de Mesa", sublabel="Limpieza y servilletero listo 5 min antes", badge="SETUP", icon="users", font_size=18, frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0 + 2*(c_sw + 30.0), s4_y + 40.0, c_sw, 110.0, "Entrega a Mesa / Pick-Up", sublabel="Servido inmediato al sentarse el cliente", badge="SERVICE", icon="file", font_size=18, frame_id=fid2)
    scene.add_quad_card(swim_x + 20.0 + 3*(c_sw + 30.0), s4_y + 40.0, c_sw, 110.0, "Liberación Rápida", sublabel="Mesa libre en 20 mins lista para otro comensal", badge="ROTATION 2.5X", icon="sync", is_hero=True, font_size=18, frame_id=fid2)

    # Flechas Inter-Carril
    scene.add_arrow(swim_x + 20.0 + c_sw * 0.5, s1_y + swim_h, swim_x + 20.0 + c_sw * 0.5, s2_y, stroke=PALETTE["BLUE_HERO"], stroke_w=2.0, frame_id=fid2)
    scene.add_arrow(swim_x + 20.0 + c_sw + 30.0 + c_sw * 0.5, s2_y + swim_h, swim_x + 20.0 + c_sw + 30.0 + c_sw * 0.5, s3_y, stroke=PALETTE["GREEN_HERO"], stroke_w=2.0, frame_id=fid2)
    scene.add_arrow(swim_x + 20.0 + 3*(c_sw + 30.0) + c_sw * 0.5, s3_y + swim_h, swim_x + 20.0 + 3*(c_sw + 30.0) + c_sw * 0.5, s4_y, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=50.0)

    # =========================================================================
    # FRAME 3: ARQUETIPO C — FLOW PIPELINE CON BUCLE DE CONTROL DE SATURACIÓN
    # =========================================================================
    w3, h3 = 2800.0, 960.0
    f3_x, f3_y = place(w3, h3)
    fid3 = scene.add_frame("FRAME 3: ARQUETIPO C — PIPELINE DE CAPACIDAD & BUCLE DE GESTIÓN DE ESPERA", f3_x, f3_y, w3, h3)

    scene.add_text(f3_x + 60.0, f3_y + 35.0, "DYNAMIC LOAD BALANCING PIPELINE  ·  CAPACITY CONTROL ENGINE", font_size=13, font_family=2, color=PALETTE["MUTED"], frame_id=fid3)
    scene.add_text(f3_x + 60.0, f3_y + 60.0, "Control de Capacidad en Tiempo Real: ¿Qué Pasa Cuando la Cocina Está al 100%?", font_size=30, font_family=2, color=PALETTE["INK"], frame_id=fid3)

    # Ribbon Superior
    stages_f3 = ["1. INGESTA PEDIDO", "2. EVALUACIÓN DE CARGA", "3. KDS COCINA", "4. ASIGNACIÓN MESA", "5. RETIRO / SERVICIO"]
    scene.add_chevron_ribbon(f3_x + 60.0, f3_y + 115.0, w3 - 120.0, h=38.0, stages=stages_f3, bg=PALETTE["DARK_SLATE"], text_color="#FFFFFF", frame_id=fid3)

    st_w = (w3 - 120.0 - 4 * 40.0) / 5.0
    st_y = f3_y + 380.0
    st_h = 420.0

    # PASO 1: INGESTA WHATSAPP
    x_p1 = f3_x + 60.0
    scene.add_scope_container(x_p1, st_y, st_w, st_h, label="1. INGESTA WHATSAPP", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    scene.add_quad_card(x_p1 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Captura de Pedido", sublabel="Platos · Modificaciones · Bebidas", badge="INPUT", icon="laptop", font_size=18, frame_id=fid3)
    scene.add_quad_card(x_p1 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Validación de Pago", sublabel="Cobro en línea exitoso", badge="CONFIRMED", icon="lock", font_size=18, frame_id=fid3)

    # PASO 2: EVALUADOR DE CARGA (LOAD BALANCER)
    x_p2 = x_p1 + st_w + 40.0
    scene.add_scope_container(x_p2, st_y, st_w, st_h, label="2. AUDITOR DE CAPACIDAD", stroke=PALETTE["BLUE_BORDER"], bg=PALETTE["BLUE_BG"], frame_id=fid3)
    scene.add_quad_card(x_p2 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Cálculo de Takt Time", sublabel="Órdenes activas en cocina vs tiempo", badge="EVAL", icon="monitoring", is_hero=True, font_size=18, frame_id=fid3)
    scene.add_quad_card(x_p2 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "¿Capacidad Disponible?", sublabel="Verificación de umbral <20 mins", badge="DECISION", icon="database", font_size=18, frame_id=fid3)

    # BUCLE SUPERIOR DE SATURACIÓN (AUTÓNOMO)
    bucle_y = f3_y + 175.0
    bucle_h = 160.0
    bucle_w = st_w * 2.0 + 40.0
    scene.add_scope_container(x_p2, bucle_y, bucle_w, bucle_h, label="BUCLE DE CONTROL DE SATURACIÓN (SI TIEMPO ESPERA > 20 MINS)", stroke=PALETTE["CORAL_BORDER"], bg=PALETTE["CORAL_BG"], frame_id=fid3)
    scene.add_quad_card(x_p2 + 20.0, bucle_y + 40.0, bucle_w - 40.0, 95.0, "Gestor de Demora & Turno Diferido", sublabel="Ofrece al cliente slot 15 min más tarde con bebida de cortesía o modalidad Express", badge="THROTTLE & RETAIN", icon="sync", is_hero=True, font_size=18, frame_id=fid3)

    # Flechas del bucle
    scene.add_arrow(x_p2 + st_w * 0.5, st_y + 65.0, x_p2 + st_w * 0.5, bucle_y + bucle_h, stroke=PALETTE["CORAL_HERO"], stroke_w=2.0, label="SATURADO (>20m)", frame_id=fid3)
    scene.add_arrow(x_p2 + bucle_w - 50.0, bucle_y + bucle_h, x_p1 + st_w * 0.5, st_y, stroke=PALETTE["CORAL_HERO"], stroke_w=2.0, dashed=True, label="SLOT REAGENDADO", frame_id=fid3)

    # PASO 3: COCINA KDS
    x_p3 = x_p2 + st_w + 40.0
    scene.add_scope_container(x_p3, st_y, st_w, st_h, label="3. KDS COCINA", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    scene.add_quad_card(x_p3 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Cola de Preparación", sublabel="Priorización cronométrica", badge="QUEUED", icon="server", font_size=18, frame_id=fid3)
    scene.add_quad_card(x_p3 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Sellado de Cocción", sublabel="Notificación de plato terminado", badge="COOKED", icon="file", font_size=18, frame_id=fid3)

    # PASO 4: ASIGNACIÓN DE MESAS
    x_p4 = x_p3 + st_w + 40.0
    scene.add_scope_container(x_p4, st_y, st_w, st_h, label="4. SALÓN & MESAS", stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    scene.add_quad_card(x_p4 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Reserva Automática", sublabel="Mesa bloqueada 5 min antes", badge="BLOCKED", icon="container", font_size=18, frame_id=fid3)
    scene.add_quad_card(x_p4 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "QR de Check-in", sublabel="Confirmación de llegada del cliente", badge="ARRIVED", icon="laptop", font_size=18, frame_id=fid3)

    # PASO 5: RETIRO / CONSUMO EXPRESS
    x_p5 = x_p4 + st_w + 40.0
    scene.add_scope_container(x_p5, st_y, st_w, st_h, label="5. ENTREGA & ROTACIÓN", stroke=PALETTE["GREEN_BORDER"], bg=PALETTE["GREEN_BG"], frame_id=fid3)
    scene.add_quad_card(x_p5 + 20.0, st_y + 65.0, st_w - 40.0, 115.0, "Servicio a Mesa Inmediato", sublabel="Comida servida en <3 mins", badge="EXPERIENCE", icon="key", is_hero=True, font_size=18, frame_id=fid3)
    scene.add_quad_card(x_p5 + 20.0, st_y + 215.0, st_w - 40.0, 115.0, "Mesa Liberada en 20m", sublabel="Rotación optimizada en hora pico", badge="ROTATION", icon="sync", font_size=18, frame_id=fid3)

    # Conectores de flujo normal
    scene.add_arrow(x_p1 + st_w, st_y + 120.0, x_p2, st_y + 120.0, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid3)
    scene.add_arrow(x_p2 + st_w, st_y + 120.0, x_p3, st_y + 120.0, stroke=PALETTE["GREEN_HERO"], stroke_w=2.5, label="CAPACIDAD OK", frame_id=fid3)
    scene.add_arrow(x_p3 + st_w, st_y + 120.0, x_p4, st_y + 120.0, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid3)
    scene.add_arrow(x_p4 + st_w, st_y + 120.0, x_p5, st_y + 120.0, stroke=PALETTE["GREEN_HERO"], stroke_w=2.5, label="MESA LISTA", frame_id=fid3)

    scene.add_legend_footer(f3_x + 60.0, f3_y + 885.0, w3 - 120.0, swatches=[
        {"label": "Flujo de Capacidad Disponible (Verde)", "bg": PALETTE["GREEN_BG"], "stroke": PALETTE["GREEN_HERO"]},
        {"label": "Bucle de Retención por Saturación (Rojo)", "bg": PALETTE["CORAL_BG"], "stroke": PALETTE["CORAL_HERO"]},
        {"label": "Fases de Procesamiento", "bg": "#FFFFFF", "stroke": PALETTE["CARD_BORDER"]}
    ], note="Control de carga inteligente: nunca prometas un plato si la cocina no puede cumplir", frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)

    # Guardar archivo
    out_file = os.path.join(OUT_DIR, "restaurante_cola_cero_optimizacion.excalidraw")
    scene.save(out_file)
    print(f"\n[+] Tablero Restaurante Cola Cero guardado exitosamente en:\n    {out_file}")

    # Validaciones
    is_valid, report = validate_scene(out_file)
    print("\n" + report.summary())

    fit_score, fit_details = calculate_archetype_fitness(
        problem_domain="RESTAURANT_QUEUE_OPTIMIZATION",
        chosen_structures=["THE_DUEL_VS_FRICTION", "OPERATIONAL_SWIMLANES_4ACTORS", "CAPACITY_CONTROL_FLOW_PIPELINE"],
        covered_dimensions=["Fila en Caja", "Abandono de Clientes", "KDS Cocina", "Asignación de Mesas", "Pre-orden WhatsApp", "Pagos Digitales", "Control de Saturación"],
        has_physical_space=True,
        has_user_journey=True,
        has_supply_chain=True,
        has_restrictions_matrix=True
    )
    print(f"\nARCHETYPE FITNESS SCORE: {fit_score}/100")
    for d in fit_details:
        print(f"  {d}")

    return out_file


if __name__ == "__main__":
    build_restaurante_cola_cero()
