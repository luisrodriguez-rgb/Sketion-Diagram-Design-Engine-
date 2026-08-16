"""
Sketion 4.0 — Test de Generalización Radical: Optimización de Cafeterías Universitarias
Demuestra que Sketion NO es un template generator estático de cajas SaaS,
sino un sistema de diseño visual capaz de articular simultáneamente:
Persona -> Proceso -> Espacio Físico -> Tecnología -> Datos -> Restricciones -> Resultado.
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
    "CANVAS": "#F4F4F4",
    "CARD": "#FFFFFF",
    "CARD_BORDER": "#BDBDBD",
    "INK": "#0C0C0C",
    "MUTED": "#8B8B8B",
    "STICKY": "#FFE95C",
    "PAIN_RED": "#E03A2F",
    "PAIN_BG": "#FDEFEF",
    "PAIN_BORDER": "#F05A5A",
    "BANNER_PINK": "#F5BEC0",
    "PASTEL_BLUE": "#9BC7E4",
    "PASTEL_GREEN": "#C2E5D3"
}


def build_campus_cafeteria_multidimensional_canvas():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])
    
    # =========================================================================
    # FRAME 1: EXPERIENCIA DEL ESTUDIANTE (JOURNEY DUAL: AS-IS VS TO-BE)
    # =========================================================================
    w1, h1 = 3200.0, 950.0
    f1_x, f1_y = place(w1, h1)
    fid1 = scene.add_frame("FRAME 1: JOURNEY DUAL — AS-IS MANUAL VS TO-BE PRE-ORDEN DIGITAL", f1_x, f1_y, w1, h1)
    
    scene.add_text(f1_x + 50, f1_y + 35, "EXPERIENCIA DEL ESTUDIANTE: TRANSFORMACIÓN DEL FLUJO DE ESPERA", font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid1)
    scene.add_text(f1_x + 50, f1_y + 75, "comparativa paso a paso del viaje del usuario: eliminacion de cuellos de botella en caja y despacho", font_size=15, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid1)

    # Mini KPIs Frame 1
    scene.add_metric_pill(f1_x + w1 - 700, f1_y + 40, "TIEMPO AS-IS", "18.5 Minutos en Fila", bg=PALETTE["PAIN_RED"], frame_id=fid1)
    scene.add_metric_pill(f1_x + w1 - 380, f1_y + 40, "TIEMPO TO-BE", "45 Segundos Recogida", bg=PALETTE["INK"], frame_id=fid1)

    # Bloque Superior: Flujo As-Is (Fila Caótica)
    scene.add_scope_container(f1_x + 60.0, f1_y + 130.0, w1 - 120.0, 320.0,
                              label="PROCESO ACTUAL (AS-IS): FILA EN SERIE CON ALTO ROZAMIENTO FÍSICO",
                              stroke=PALETTE["PAIN_BORDER"], bg=PALETTE["PAIN_BG"], frame_id=fid1)
    
    as_is_steps = [
        ("1. Llegada Masiva", "Pico simultaneo de 800 estudiantes al sonar campana"),
        ("2. Fila Consulta", "Estudiantes leen menu en pared obstruyendo puerta"),
        ("3. Toma de Orden", "Cajero manual digita pedido en POS antiguo"),
        ("4. Pago Efectivo/Tarj", "Friccion en cobro y entrega de cambio"),
        ("5. Espera en Mostrador", "Aglomeracion desordenada esperando nombre"),
        ("6. Entrega Plato", "Revision manual de ticket de compra")
    ]
    
    step_w1 = (w1 - 200.0 - 5 * 30.0) / 6.0
    for i, (stitle, ssub) in enumerate(as_is_steps):
        sx = f1_x + 90.0 + i * (step_w1 + 30.0)
        sy = f1_y + 200.0
        scene.add_dual_card(sx, sy, step_w1, 110.0, stitle, sublabel=ssub,
                            bg="#FFFFFF", stroke=PALETTE["PAIN_BORDER"], text_color=PALETTE["INK"], frame_id=fid1)
        if i < 5:
            scene.add_arrow(sx + step_w1, sy + 55.0, sx + step_w1 + 30.0, sy + 55.0,
                            stroke=PALETTE["PAIN_RED"], stroke_w=2.0, frame_id=fid1)

    # Bloque Inferior: Flujo To-Be (Pre-Orden Móvil + Lockers)
    scene.add_scope_container(f1_x + 60.0, f1_y + 490.0, w1 - 120.0, 380.0,
                              label="PROCESO DESTINO (TO-BE): PRE-ORDEN ASÍNCRONA Y RETIRO EXPRESS",
                              stroke=PALETTE["INK"], bg=PALETTE["PASTEL_GREEN"], frame_id=fid1)

    to_be_steps = [
        ("1. Pre-Orden en App", "Estudiante ordena 20 min antes desde salon", "phone"),
        ("2. Pago Digital", "Debito express de saldo universitario / tarjeta", "lock"),
        ("3. Batching Cocina", "KDS agrupa ordenes por slot de tiempo", "server"),
        ("4. Carga a Locker", "Staff deposita pedido en casillero termico", "container"),
        ("5. Retiro con QR", "Estudiante escanea QR y retira en 15 seg", "laptop")
    ]
    
    step_w2 = (w1 - 200.0 - 4 * 40.0) / 5.0
    for i, (stitle, ssub, sicon) in enumerate(to_be_steps):
        sx = f1_x + 90.0 + i * (step_w2 + 40.0)
        sy = f1_y + 570.0
        is_hero_step = (i == 4)
        bg_card = PALETTE["INK"] if is_hero_step else "#FFFFFF"
        text_col = "#FFFFFF" if is_hero_step else PALETTE["INK"]
        scene.add_card_with_icon(sx, sy, step_w2, 130.0, stitle, sublabel=ssub, icon=sicon,
                                 bg=bg_card, stroke=PALETTE["INK"], text_color=text_col, frame_id=fid1)
        if i < 4:
            scene.add_arrow(sx + step_w2, sy + 65.0, sx + step_w2 + 40.0, sy + 65.0,
                            stroke=PALETTE["INK"], stroke_w=2.0, label="Paso Digital", frame_id=fid1)

    scene.auto_fit_frame(fid1, padding=50.0)

    # =========================================================================
    # FRAME 2: PLANTA FÍSICA & SEGREGACIÓN OPERATIVA (HUB VS SATÉLITE)
    # =========================================================================
    w2, h2 = 3200.0, 950.0
    f2_x, f2_y = place(w2, h2)
    fid2 = scene.add_frame("FRAME 2: PLANTA OPERATIVA — CAFETERÍA CENTRAL (HUB) VS SATÉLITE (CEDI)", f2_x, f2_y, w2, h2)
    
    scene.add_text(f2_x + 50, f2_y + 35, "DISTRIBUCIÓN FÍSICA DE PLANTA Y LOGÍSTICA DE ABASTECIMIENTO", font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid2)
    scene.add_text(f2_x + 50, f2_y + 75, "segregacion de flujos calientes in-situ y abastecimiento frio desde el centro de distribucion", font_size=15, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid2)

    col2_w = (w2 - 120.0 - 2 * 60.0) / 3.0

    # Zona 1: Centro de Distribución (CEDI)
    scene.add_scope_container(f2_x + 60.0, f2_y + 130.0, col2_w, 720.0,
                              label="1. CENTRO DE DISTRIBUCIÓN (CEDI)",
                              stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    scene.add_card_with_icon(f2_x + 85.0, f2_y + 200.0, col2_w - 50.0, 120.0,
                             "Almacén Central & Stock", "Control de perecederos y lotes", icon="bucket", frame_id=fid2)
    scene.add_card_with_icon(f2_x + 85.0, f2_y + 350.0, col2_w - 50.0, 120.0,
                             "Preparación Fría & Ensamblaje", "Sandwiches, ensaladas y bebidas", icon="container", frame_id=fid2)
    scene.add_card_with_icon(f2_x + 85.0, f2_y + 500.0, col2_w - 50.0, 120.0,
                             "Ruta de Despacho Térmico", "Vehículos refrigerados a satélites", icon="pipeline", frame_id=fid2)

    # Zona 2: Cafetería Central (Hub con Cocina Caliente)
    scene.add_scope_container(f2_x + 120.0 + col2_w, f2_y + 130.0, col2_w, 720.0,
                              label="2. CAFETERÍA CENTRAL (COCINA CALIENTE)",
                              stroke=PALETTE["INK"], bg=PALETTE["PASTEL_BLUE"], frame_id=fid2)
    scene.add_card_with_icon(f2_x + 145.0 + col2_w, f2_y + 200.0, col2_w - 50.0, 120.0,
                             "Cocina de Alto Rendimiento", "Platos calientes y minutas a demanda", icon="server", frame_id=fid2)
    scene.add_card_with_icon(f2_x + 145.0 + col2_w, f2_y + 350.0, col2_w - 50.0, 120.0,
                             "Pantalla KDS de Despacho", "Secuencia de comandas optimizada", icon="terminal", frame_id=fid2)
    scene.add_card_with_icon(f2_x + 145.0 + col2_w, f2_y + 500.0, col2_w - 50.0, 120.0,
                             "Casilleros Térmicos QR", "Lockers express de autoservicio", icon="lock", frame_id=fid2)

    # Zona 3: Cafetería Satélite (Recepción y Despacho Express)
    scene.add_scope_container(f2_x + 180.0 + 2 * col2_w, f2_y + 130.0, col2_w, 720.0,
                              label="3. CAFETERÍAS SATÉLITES (GRAB & GO)",
                              stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid2)
    scene.add_card_with_icon(f2_x + 205.0 + 2 * col2_w, f2_y + 200.0, col2_w - 50.0, 120.0,
                             "Recepción de Lotes CEDI", "Verificación de temperatura y stock", icon="sync", frame_id=fid2)
    scene.add_card_with_icon(f2_x + 205.0 + 2 * col2_w, f2_y + 350.0, col2_w - 50.0, 120.0,
                             "Neveras Inteligentes RFID", "Apertura con credencial universitaria", icon="key", frame_id=fid2)
    scene.add_card_with_icon(f2_x + 205.0 + 2 * col2_w, f2_y + 500.0, col2_w - 50.0, 120.0,
                             "Mostrador Rápido de Café", "Expendio en 20 segundos por cliente", icon="user", frame_id=fid2)

    # Flechas de Suministro Inter-Zona
    scene.add_arrow(f2_x + 60.0 + col2_w, f2_y + 560.0, f2_x + 180.0 + 2 * col2_w, f2_y + 560.0,
                    stroke=PALETTE["INK"], stroke_w=2.0, label="Abastecimiento Diario CEDI", orthogonal=True, frame_id=fid2)

    scene.auto_fit_frame(fid2, padding=50.0)

    # =========================================================================
    # FRAME 3: MOTOR PREDICTIVO & REGLAS DE RESTRICCIÓN (DATOS & REST)
    # =========================================================================
    w3, h3 = 3200.0, 950.0
    f3_x, f3_y = place(w3, h3)
    fid3 = scene.add_frame("FRAME 3: MOTOR DE DEMANDA & ASIGNACIÓN — PREDICCIÓN Y REGLAS DE CAPACIDAD", f3_x, f3_y, w3, h3)
    
    scene.add_text(f3_x + 50, f3_y + 35, "MOTOR DE PREDICCIÓN DE DEMANDA Y ASIGNACIÓN BALANCEADA", font_size=28, font_family=2, color=PALETTE["INK"], frame_id=fid3)
    scene.add_text(f3_x + 50, f3_y + 75, "algoritmo predictivo basado en horarios academicos para evitar saturacion de cocinas", font_size=15, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid3)

    # Variables de Entrada (Izquierda)
    scene.add_scope_container(f3_x + 60.0, f3_y + 130.0, 800.0, 720.0,
                              label="VARIABLES DE ENTRADA (SEÑALES ACADÉMICAS)",
                              stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    scene.add_dual_card(f3_x + 85.0, f3_y + 200.0, 750.0, 110.0, "Horarios de Clase y Aforos", "Cruza 14,000 estudiantes matriculados y salidas por edificio", frame_id=fid3)
    scene.add_dual_card(f3_x + 85.0, f3_y + 340.0, 750.0, 110.0, "Histórico de Ventas y Clima", "Patrones de consumo en dias lluviosos vs soleados", frame_id=fid3)
    scene.add_dual_card(f3_x + 85.0, f3_y + 480.0, 750.0, 110.0, "Stock de Perecederos en Tiempo Real", "Nivel de ingredientes en camara fria del CEDI", frame_id=fid3)

    # Motor Central (Hero)
    scene.add_scope_container(f3_x + 920.0, f3_y + 130.0, 1100.0, 720.0,
                              label="ALGORITMO DE ASIGNACIÓN Y TAKT TIME PREDICTIVO",
                              stroke=PALETTE["INK"], bg=PALETTE["PASTEL_GREEN"], frame_id=fid3)
    scene.add_card_with_icon(f3_x + 950.0, f3_y + 220.0, 1040.0, 140.0,
                             "Optimizador de Carga de Cocina", "Slots de 40 pedidos maximo por ventana de 10 min", icon="server",
                             bg=PALETTE["INK"], stroke=PALETTE["INK"], text_color="#FFFFFF", frame_id=fid3)
    scene.add_card_with_icon(f3_x + 950.0, f3_y + 400.0, 1040.0, 130.0,
                             "Balanceador de Cafeterías Cercanas", "Redirige pedidos frios a satelites cuando central esta al 90%", icon="sync", frame_id=fid3)
    scene.add_dual_card(f3_x + 950.0, f3_y + 570.0, 1040.0, 120.0,
                        "Generador de Alertas de Pre-Cocción", "Envia orden de hornear 60 croissants 15 min antes del receso", frame_id=fid3)

    # Acciones Ejecutables (Derecha)
    scene.add_scope_container(f3_x + 2080.0, f3_y + 130.0, 1060.0, 720.0,
                              label="ACCIONES OPERATIVAS Y RESULTADOS",
                              stroke=PALETTE["CARD_BORDER"], bg="#FFFFFF", frame_id=fid3)
    scene.add_dual_card(f3_x + 2110.0, f3_y + 200.0, 1000.0, 110.0, "Cero Filas en Puerta", "92% de estudiantes retira su pedido en < 1 minuto", frame_id=fid3)
    scene.add_dual_card(f3_x + 2110.0, f3_y + 340.0, 1000.0, 110.0, "Reducción de Merma (-40%)", "Preparacion justa a tiempo segun demanda pronosticada", frame_id=fid3)
    scene.add_dual_card(f3_x + 2110.0, f3_y + 480.0, 1000.0, 110.0, "Costos Fijos Operativos Estables", "Mismo personal de cocina con rendimiento optimizado", frame_id=fid3)

    # Conexiones de Entrada a Motor y a Resultados
    scene.add_arrow(f3_x + 835.0, f3_y + 255.0, f3_x + 920.0, f3_y + 255.0, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid3)
    scene.add_arrow(f3_x + 2020.0, f3_y + 290.0, f3_x + 2080.0, f3_y + 290.0, stroke=PALETTE["INK"], stroke_w=2.0, frame_id=fid3)

    scene.auto_fit_frame(fid3, padding=50.0)

    out_path = os.path.join(OUT_DIR, "optimizacion_cafeterias_campus_radical.excalidraw")
    scene.save(out_path)
    print(f"[+] Archivo Excalidraw Campus guardado en: {out_path}")
    
    _, report = validate_scene(out_path)
    print("\n" + report.summary())

    fitness_score, critiques = calculate_archetype_fitness(
        problem_domain="OPERATIONS_CAMPUS",
        chosen_structures=["DUAL_JOURNEY_TIMELINE", "PHYSICAL_FLOORPLAN_SWIMLANE", "PREDICTIVE_FLOW_ENGINE"],
        covered_dimensions=["PERSONA", "PROCESO", "ESPACIO_FISICO", "TECNOLOGIA", "DATOS", "RESTRICCIONES", "RESULTADO"],
        has_physical_space=True,
        has_user_journey=True,
        has_supply_chain=True,
        has_restrictions_matrix=True
    )
    
    print("\n==================================================")
    print(f"ARCHETYPE FITNESS SCORE: {fitness_score}/100")
    print("==================================================")
    if critiques:
        for c in critiques:
            print(f"  • {c}")
    else:
        print("  ✅ Ajuste estructural óptimo: el diagrama modela espacio físico, journey, datos y abastecimiento sin caer en templates genéricos.")
    print("==================================================")

    return out_path, report, fitness_score


if __name__ == "__main__":
    build_campus_cafeteria_multidimensional_canvas()
