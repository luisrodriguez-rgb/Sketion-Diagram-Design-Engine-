import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

import sketion
from sketion import ExcalidrawScene

def build_non_technical_diagram():
    scene = ExcalidrawScene()
    fid = scene.add_frame("Sketion — ¿Cómo funciona la fábrica de diagramas inteligentes?", 40, 20, 1840, 1180)

    # ═════════════════════════════════════════════════════════════════════════
    # CABECERA PRINCIPAL (CLARA, MODERNA Y AMIGABLE)
    # ═════════════════════════════════════════════════════════════════════════
    scene.add_rect(60, 35, 1800, 60, bg="#0F172A", stroke="#0F172A", roundness_type=3, frame_id=fid)
    scene.add_text(85, 46, "SKETION: TU ARQUITECTO Y DISEÑADOR VISUAL INTELIGENTE", font_size=14, font_family=2, color="#38BDF8", frame_id=fid)
    scene.add_text(85, 70, "¿Cómo convierte tus ideas, explicaciones y problemas en diagramas visuales profesionales y fáciles de entender?", font_size=10, font_family=1, color="#CBD5E1", frame_id=fid)

    # ═════════════════════════════════════════════════════════════════════════
    # SECCIÓN 1: EL VIAJE DE TU IDEA EN 4 PASOS (FLUJO SUPERIOR COMPACTO)
    # ═════════════════════════════════════════════════════════════════════════
    scene.add_rect(60, 110, 1800, 260, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    scene.add_text(85, 126, "EL VIAJE DE TU IDEA: DE UN TEXTO COMÚN A UN DIAGRAMA PROFESIONAL EN 4 PASOS", font_size=11, font_family=2, color="#0F172A", frame_id=fid)

    steps = [
        ("PASO 1: TE ESCUCHA Y ENTIENDE", "El Lector Inteligente", 
         "Le cuentas tu idea con palabras normales.\n\nSketion identifica quiénes participan, qué pasos hay y qué es lo más importante a comunicar.",
         "#0284C7", "#EFF6FF", 85),
        
        ("PASO 2: ELIGE EL MEJOR DIBUJO", "El Arquitecto de Ideas", 
         "No hace siempre el mismo dibujo aburrido.\n\nSabe si necesitas un mapa paso a paso, un círculo de relaciones o un tablero de control.",
         "#D93829", "#FFF5F2", 525),
        
        ("PASO 3: ORDENA SIN ENREDOS", "El Urbanista del Lienzo", 
         "Acomoda cada tarjeta en su lugar exacto.\n\nDibuja flechas por caminos limpios para que ninguna línea cruce encima de las letras.",
         "#059669", "#F0FDF4", 965),
        
        ("PASO 4: PULE Y TE ENTREGA", "El Diseñador Ejecutivo", 
         "Aplica colores profesionales y tipografías.\n\nTe entrega un archivo que puedes abrir, mover, editar o proyectar en tu reunión.",
         "#7C3AED", "#F5F3FF", 1405)
    ]

    for stitle, ssub, sdesc, scol, sbg, sx in steps:
        scene.add_rect(sx, 150, 390, 195, bg=sbg, stroke=scol, stroke_w=1.5, roundness_type=3, frame_id=fid)
        
        # Badge
        scene.add_rect(sx + 14, 162, 200, 22, bg=scol, stroke=scol, roundness_type=3, frame_id=fid)
        scene.add_text(sx + 20, 167, stitle, font_size=8, font_family=2, color="#FFFFFF", frame_id=fid)
        
        # Subtítulo amigable
        scene.add_text(sx + 14, 195, ssub, font_size=12, font_family=2, color="#0F172A", frame_id=fid)
        scene.add_line(sx + 14, 212, sx + 375, 212, stroke=scol, stroke_w=1.0, frame_id=fid)
        
        # Descripción clara
        scene.add_text(sx + 14, 224, sdesc, font_size=9, font_family=1, color="#334155", frame_id=fid)

    # Flechas conectores entre pasos (perfectamente centradas en y=245)
    scene.add_arrow(475, 245, 525, 245, stroke="#0284C7", stroke_w=2.2, frame_id=fid)
    scene.add_arrow(915, 245, 965, 245, stroke="#D93829", stroke_w=2.2, frame_id=fid)
    scene.add_arrow(1355, 245, 1405, 245, stroke="#059669", stroke_w=2.2, frame_id=fid)

    # ═════════════════════════════════════════════════════════════════════════
    # SECCIÓN 2: ANTES VS DESPUÉS (DUELO COMPARATIVO, COLUMNA IZQUIERDA w=875)
    # ═════════════════════════════════════════════════════════════════════════
    scene.add_rect(60, 390, 875, 760, bg="#FFFFFF", stroke="#0284C7", stroke_w=1.5, roundness_type=3, frame_id=fid)
    scene.add_text(85, 410, "¿POR QUÉ SKETION CAMBIA LAS REGLAS DEL JUEGO? (COMPARATIVA)", font_size=11, font_family=2, color="#0284C7", frame_id=fid)

    # Bloque 1: El Problema Tradicional (Rojo / Gris)
    scene.add_rect(80, 435, 835, 240, bg="#FEF2F2", stroke="#DC2626", stroke_w=1.2, roundness_type=3, frame_id=fid)
    scene.add_rect(80, 435, 835, 36, bg="#FEE2E2", stroke="#DC2626", stroke_w=1.0, roundness_type=3, frame_id=fid)
    scene.add_text(100, 446, "[-] EL PROBLEMA HABITUAL (DIAGRAMAS MANUALES Y HERRAMIENTAS COMUNES)", font_size=10, font_family=2, color="#991B1B", frame_id=fid)
    
    bad_points = [
        "Monotonía Aburrida: Siempre dibujan los mismos rectángulos apilados en fila sin importar el tema.",
        "Flechas Cruzadas: Líneas desordenadas que pasan por encima de las letras y tapan los títulos.",
        "Horas Perdidas: Mover cajitas una por una intentando que no se descuadren los márgenes.",
        "Imágenes Muertas: Te entregan una foto fija (.png) que no puedes editar cuando algo cambia."
    ]
    for b_i, b_pt in enumerate(bad_points):
        scene.add_text(100, 485 + b_i * 44, f"• {b_pt}", font_size=9, font_family=1, color="#7F1D1D", frame_id=fid)

    # Conector VS
    scene.add_ellipse(465, 685, 45, 45, bg="#0F172A", stroke="#0F172A", stroke_w=1.5, frame_id=fid)
    scene.add_text(475, 698, "VS", font_size=12, font_family=2, color="#FFFFFF", frame_id=fid)

    # Bloque 2: La Solución con Sketion (Verde / Éxito - 0 Emojis, Estilo Puro)
    scene.add_rect(80, 740, 835, 385, bg="#F0FDF4", stroke="#16A34A", stroke_w=1.5, roundness_type=3, frame_id=fid)
    scene.add_rect(80, 740, 835, 36, bg="#DCFCE7", stroke="#16A34A", stroke_w=1.0, roundness_type=3, frame_id=fid)
    scene.add_text(100, 751, "[+] LA EXPERIENCIA SKETION (DISEÑO PROFESIONAL AUTÓNOMO)", font_size=10, font_family=2, color="#166534", frame_id=fid)

    good_points = [
        ("✦ Más de 20 Formas Inteligentes:", "Escoge el formato perfecto: mapas de valor, círculos de relaciones, árboles o tableros A3."),
        ("✦ Flechas sin Enredos:", "Ruteo limpio por canales despejados; nunca tapa letras ni deja líneas torpes."),
        ("✦ Calidad Ejecutiva:", "Tipografía moderna y paletas armónicas listas para proyectar en la junta directiva."),
        ("✦ 100% Editable en Excalidraw:", "Puedes mover cualquier elemento, cambiar textos y ajustar colores cuando lo necesites.")
    ]
    for g_i, (g_tit, g_desc) in enumerate(good_points):
        gy = 790 + g_i * 75
        scene.add_text(100, gy, g_tit, font_size=10, font_family=2, color="#15803D", frame_id=fid)
        scene.add_text(100, gy + 22, g_desc, font_size=9, font_family=1, color="#14532D", frame_id=fid)

    # ═════════════════════════════════════════════════════════════════════════
    # SECCIÓN 3: CASOS DE USO REALES (MOSAICO DE 4 TARJETAS, COLUMNA DERECHA w=905)
    # ═════════════════════════════════════════════════════════════════════════
    scene.add_rect(955, 390, 905, 760, bg="#FFFFFF", stroke="#D93829", stroke_w=1.5, roundness_type=3, frame_id=fid)
    scene.add_text(980, 410, "SKETION EN ACCIÓN: EJEMPLOS REALES DE LO QUE PUEDES CREAR", font_size=11, font_family=2, color="#D93829", frame_id=fid)

    cases = [
        ("1. Ventas & Comercio Online", "Tu Pedido: 'Explica cómo un cliente compra y recibe su pedido.'\nResultado Sketion: Mapa de experiencia cliente ➔ pago ➔ despacho.", "VENTAS", "browser", "#2563EB", "#EFF6FF", 435),
        ("2. Fábricas & Operaciones", "Tu Pedido: 'Tengo 5 máquinas y se acumula inventario en la 3.'\nResultado Sketion: Tablero A3 con cuello de botella y 4 soluciones.", "OPERACIONES", "server", "#DC2626", "#FEF2F2", 610),
        ("3. Equipos & Estrategia", "Tu Pedido: 'Aclara qué le toca hacer a Ventas, Soporte y Finanzas.'\nResultado Sketion: Carriles de responsabilidad con roles claros.", "ESTRATEGIA", "user", "#059669", "#F0FDF4", 785),
        ("4. Tecnología & Asistentes IA", "Tu Pedido: 'Presenta el nuevo asistente virtual a los directivos.'\nResultado Sketion: Ecosistema con seguridad, datos y trazabilidad.", "INNOVACIÓN", "shield", "#7C3AED", "#F5F3FF", 960)
    ]

    for ctitle, cdesc, cbadge, cicon, ccol, cbg, cy in cases:
        scene.add_quad_card(975, cy, 865, 145, ctitle, cdesc, badge=cbadge, icon=cicon, font_size=13, frame_id=fid)

    # Exportación
    output_dir = os.path.join(workspace_dir, "docs")
    os.makedirs(output_dir, exist_ok=True)

    excalidraw_file = os.path.join(output_dir, "sketion_guia_no_tecnica.excalidraw")
    scene.save(excalidraw_file)
    print(f"Saved Excalidraw: {excalidraw_file}")

    svg_file = os.path.join(output_dir, "sketion_guia_no_tecnica.svg")
    sketion.export(scene, svg_file, format="svg")
    print(f"Saved SVG: {svg_file}")

if __name__ == "__main__":
    build_non_technical_diagram()
