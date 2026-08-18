import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

import sketion
from sketion import ExcalidrawScene

def build_architecture_diagram():
    scene = ExcalidrawScene()
    fid = scene.add_frame("Sketion v11.0 GA — Arquitectura Técnica del Motor", 40, 20, 1920, 1340)

    # ═════════════════════════════════════════════════════════════════════════
    # HEADER PRINCIPAL
    # ═════════════════════════════════════════════════════════════════════════
    scene.add_rect(60, 35, 1880, 50, bg="#0F172A", stroke="#0F172A", roundness_type=3, frame_id=fid)
    scene.add_text(85, 48, "SKETION VISUAL COMPOSITION ENGINE (v11.0 GA) — ARQUITECTURA TÉCNICA & FUNCIONAMIENTO INTEGRAL", font_size=13, font_family=2, color="#38BDF8", frame_id=fid)
    scene.add_text(85, 66, "Motor autónomo de composición visual, inferencia semántica, ruteo ortogonal Manhattan A*, 20 patrones, 27 tipos visuales y exportación dual (.excalidraw / .svg)", font_size=9, font_family=1, color="#94A3B8", frame_id=fid)

    # ═════════════════════════════════════════════════════════════════════════
    # SECCIÓN 1: PIPELINE END-TO-END DE GENERACIÓN (FLUJO DE DATOS)
    # ═════════════════════════════════════════════════════════════════════════
    scene.add_rect(60, 95, 1880, 310, bg="#F8FAFC", stroke="#CBD5E1", stroke_w=1.5, roundness_type=3, frame_id=fid)
    scene.add_text(85, 112, "1. PIPELINE DE TRANSFORMACIÓN END-TO-END (DEL PROMPT EN LENGUAJE NATURAL A FORMATOS VECTORIALES)", font_size=11, font_family=2, color="#0F172A", frame_id=fid)

    # 6 Cajas del Pipeline con alturas compactas y sin espacio muerto
    stages = [
        ("P1: SEMANTIC INTAKE & IR", "Módulo: semantic/content_model.py\n• Parsing de Prompt / Payload JSON\n• Extracción de Entidades & Roles\n• Inferencia de Relaciones y SLA\n• Construye ContentModel tipado", "SEMANTIC", "#0284C7", "#EFF6FF", 80),
        ("P2: VISUAL INTELLIGENCE", "Módulo: visual_intelligence/ & composition/\n• Selección de Patrón (20 patrones)\n• Matriz de 27 Tipos Visuales\n• DiversityJudge: Score VDS\n• Previene monocultura de capas", "INTELLIGENCE", "#D93829", "#FFF5F2", 390),
        ("P3: MULTI-ALGO LAYOUT", "Módulo: layout/layout_solver.py\n• Algoritmos: Sugiyama (LR/TB),\n  Radial, Swimlane, Tree, Matrix\n• Asignación de Capas jerárquicas\n• Calcula posiciones (x, y, w, h)", "LAYOUT", "#2563EB", "#EFF6FF", 700),
        ("P4: PORTS & MANHATTAN A*", "Módulo: layout/ports.py & router.py\n• Puertos Magnéticos (Top, Bot, L, R)\n• Ruteo Ortogonal Manhattan A*\n• Minimización de cruces de líneas\n• 0 colisiones en cajas o texto", "ROUTER", "#059669", "#F0FDF4", 1010),
        ("P5: THEME & STYLE LOCK", "Módulo: design/theme_engine.py\n• 8 Temas: Editorial, Technical, etc.\n• Paletas HSL de alto contraste\n• Iconografía técnica (0 emojis)\n• Tipografía Inter con jerarquía", "DESIGN", "#D97706", "#FFFBEB", 1320),
        ("P6: VALIDATION & EXPORT", "Módulo: validation/, repair/ & export/\n• Closed-Loop Repair (VCS >= 99)\n• Serializador Excalidraw JSON\n• Generador SVG 1.1 Vectorial Puro\n• Salida dual para edición y preview", "EXPORT", "#7C3AED", "#F5F3FF", 1630)
    ]

    for stitle, sdesc, sbadge, scol, sbg, sx in stages:
        scene.add_rect(sx, 135, 290, 180, bg=sbg, stroke=scol, stroke_w=1.5, roundness_type=3, frame_id=fid)
        # Badge
        scene.add_rect(sx + 12, 147, 120, 20, bg=scol, stroke=scol, roundness_type=3, frame_id=fid)
        scene.add_text(sx + 18, 152, sbadge, font_size=8, font_family=2, color="#FFFFFF", frame_id=fid)
        
        # Título
        scene.add_text(sx + 12, 174, stitle, font_size=10, font_family=2, color="#0F172A", frame_id=fid)
        scene.add_line(sx + 12, 188, sx + 278, 188, stroke=scol, stroke_w=1.0, frame_id=fid)
        
        # Descripción
        scene.add_text(sx + 12, 196, sdesc, font_size=8, font_family=1, color="#334155", frame_id=fid)

    # Flechas conectores entre etapas del pipeline (perfectamente centradas en y=225)
    scene.add_arrow(370, 225, 390, 225, stroke="#0284C7", stroke_w=2.0, frame_id=fid)
    scene.add_arrow(680, 225, 700, 225, stroke="#D93829", stroke_w=2.0, frame_id=fid)
    scene.add_arrow(990, 225, 1010, 225, stroke="#2563EB", stroke_w=2.0, frame_id=fid)
    scene.add_arrow(1300, 225, 1320, 225, stroke="#059669", stroke_w=2.0, frame_id=fid)
    scene.add_arrow(1610, 225, 1630, 225, stroke="#D97706", stroke_w=2.0, frame_id=fid)

    # Barra inferior de garantías inmutables
    scene.add_rect(80, 330, 1840, 60, bg="#FFFFFF", stroke="#CBD5E1", stroke_w=1.2, roundness_type=3, frame_id=fid)
    scene.add_text(95, 342, "GARANTÍAS INMUTABLES DEL PIPELINE:", font_size=9, font_family=2, color="#0F172A", frame_id=fid)
    scene.add_text(95, 362, "✓ 0 Emojis (Iconografía nativa)   ·   ✓ 0 Colisiones Texto/Cajas   ·   ✓ Ruteo ortogonal borde a borde   ·   ✓ Cilindros proporcionados (14% cap)   ·   ✓ Score VCS >= 99/100", font_size=8, font_family=1, color="#475569", frame_id=fid)

    # ═════════════════════════════════════════════════════════════════════════
    # SECCIÓN 2: SUBSISTEMAS INTERNOS (COLUMNA IZQUIERDA, w=925)
    # ═════════════════════════════════════════════════════════════════════════
    scene.add_rect(60, 420, 925, 900, bg="#FFFFFF", stroke="#0284C7", stroke_w=1.5, roundness_type=3, frame_id=fid)
    scene.add_text(85, 438, "2. SUBSISTEMAS Y MODELOS INTERNOS DEL MOTOR", font_size=11, font_family=2, color="#0284C7", frame_id=fid)

    # Sub-bloque 2.1: ContentModel
    scene.add_rect(80, 460, 885, 200, bg="#EFF6FF", stroke="#93C5FD", stroke_w=1.2, roundness_type=3, frame_id=fid)
    scene.add_text(95, 474, "A. MODELO DE CONTENIDO INTERMEDIO (ContentModel / semantic/)", font_size=10, font_family=2, color="#1E40AF", frame_id=fid)
    scene.add_text(95, 498, "• SystemNodeSpec: Nodos de sistema con { id, label, role, is_hero, shape, layer_index, metadata }.\n• ActorSpec: Usuarios, clientes o sistemas externos con iconografía asociada.\n• RelationshipSpec: Conexiones con { source, target, label, relation_type (sync, async, critical, veto) }.\n• MetricSpec: Indicadores cuantitativos y KPIs integrados (e.g. latencias < 50ms, throughput, SLA ≤ 5d).\n• Desacopla completamente la lógica del dominio de la representación gráfica final.", font_size=8, font_family=1, color="#1E3A8A", frame_id=fid)
    
    # Mini-visual demostrativo de entidades
    scene.add_actor_node(100, 580, 260, 60, "Cliente Móvil (mTLS)", "Actor Externo", icon="mobile", frame_id=fid)
    scene.add_quad_card(400, 580, 260, 60, "Payment Saga Core", "Servicio Transaccional", badge="HERO CORE", is_hero=True, icon="server", frame_id=fid)
    scene.add_arrow(360, 610, 400, 610, stroke="#0284C7", stroke_w=1.5, frame_id=fid)
    scene.add_text(680, 600, "◄ Entidades tipadas en memoria\n  antes de calcular geometría", font_size=8, font_family=3, color="#1E40AF", frame_id=fid)

    # Sub-bloque 2.2: Ruteo Manhattan & Puertos (CORREGIDO DE R長TEO A RUTEO)
    scene.add_rect(80, 675, 885, 200, bg="#F0FDF4", stroke="#86EFAC", stroke_w=1.2, roundness_type=3, frame_id=fid)
    scene.add_text(95, 688, "B. RUTEO MANHATTAN A* & PUERTOS MAGNÉTICOS (layout/)", font_size=10, font_family=2, color="#166534", frame_id=fid)
    scene.add_text(95, 710, "• PortManager: Calcula 4 puertos magnéticos por nodo (TOP, BOTTOM, LEFT, RIGHT) con offsets perimetrales.\n• ManhattanRouter: Búsqueda de caminos ortogonales en cuadrícula discreta (Grid de 10px).\n• Función de Costo A*: Penaliza giros (+15), cruce con cajas (+500) y solapamiento de líneas (+80).\n• Garantía: Los conectores siempre nacen y mueren en el borde del contenedor sin invadir texto.", font_size=8, font_family=1, color="#14532D", frame_id=fid)

    # Mini-visual demostrativo de puertos
    scene.add_rect(100, 790, 220, 65, bg="#FFFFFF", stroke="#059669", stroke_w=1.5, roundness_type=3, frame_id=fid)
    scene.add_text(115, 815, "Nodo Origen (Port R)", font_size=9, font_family=2, color="#065F46", frame_id=fid)
    # 4 Puertos dibujados
    scene.add_ellipse(316, 818, 8, 8, bg="#059669", stroke="#059669", frame_id=fid) # R
    scene.add_ellipse(206, 786, 8, 8, bg="#059669", stroke="#059669", frame_id=fid) # T
    scene.add_ellipse(206, 851, 8, 8, bg="#059669", stroke="#059669", frame_id=fid) # B
    scene.add_ellipse(96, 818, 8, 8, bg="#059669", stroke="#059669", frame_id=fid) # L
    
    scene.add_rect(480, 790, 220, 65, bg="#FFFFFF", stroke="#059669", stroke_w=1.5, roundness_type=3, frame_id=fid)
    scene.add_text(495, 815, "Nodo Destino (Port L)", font_size=9, font_family=2, color="#065F46", frame_id=fid)
    scene.add_ellipse(476, 818, 8, 8, bg="#059669", stroke="#059669", frame_id=fid) # L
    
    scene.add_arrow(320, 822, 476, 822, stroke="#059669", stroke_w=2.0, frame_id=fid)
    scene.add_text(340, 805, "Manhattan A*", font_size=8, font_family=3, color="#059669", frame_id=fid)
    scene.add_text(720, 815, "◄ Puertos de anclaje magnético\n  y ruteo ortogonal libre de cruces", font_size=8, font_family=3, color="#166534", frame_id=fid)

    # Sub-bloque 2.3: Catálogo de 20 Patrones y 27 Tipos Visuales
    scene.add_rect(80, 890, 885, 215, bg="#FFFBEB", stroke="#FCD34D", stroke_w=1.2, roundness_type=3, frame_id=fid)
    scene.add_text(95, 904, "C. DIVERSIDAD TOPOLÓGICA & CATÁLOGO VISUAL (visual_intelligence/)", font_size=10, font_family=2, color="#92400E", frame_id=fid)
    scene.add_text(95, 926, "• 20 Patrones: Layered, Radial Hub, Swimlane, Tree, Matrix 2x2, A3 Lean Report, Cornell Notes, Roadmap,\n  Service Blueprint, Decoupled Fabric, Agentic Flywheel, Data Lakehouse, Security Barrier, etc.\n• 27 Tipos Nativos: Tarjetas Quad, Cilindros 3D BD, Pipes Streaming, Barreras WAF, Actores, Tablas y Matrices.\n• DiversityJudge: Evalúa la distribución espacial para impedir la monocultura de capas horizontales.", font_size=8, font_family=1, color="#78350F", frame_id=fid)

    # Mini-visual demostrativo de tipos nativos (Cilindro + Barrera)
    scene.add_database_cylinder(100, 995, 230, 90, "PostgreSQL Aurora", "Sync Multi-AZ ACID", badge="DATABASE", frame_id=fid)
    scene.add_security_barrier(360, 995, 260, 90, "Cloudflare Edge WAF", ["DDoS Shield L7", "TLS 1.3", "Rate Limit"], frame_id=fid)
    scene.add_text(640, 1030, "◄ Morfologías nativas especializadas\n  (cilindros proporcionales y barreras de seguridad)", font_size=8, font_family=3, color="#92400E", frame_id=fid)

    # Sub-bloque 2.4: Sistema de Validación y Reparación
    scene.add_rect(80, 1120, 885, 185, bg="#FFF5F2", stroke="#FCA5A5", stroke_w=1.2, roundness_type=3, frame_id=fid)
    scene.add_text(95, 1134, "D. VALIDACIÓN Y REPARACIÓN EN BUCLE CERRADO (validation/ & repair/)", font_size=10, font_family=2, color="#991B1B", frame_id=fid)
    scene.add_text(95, 1156, "• Visual Consistency Score (VCS): Métrica continua de calidad que audita:\n  1. Cero colisiones geométricas (cajas sobre cajas o flechas sobre texto).\n  2. Proporciones visuales armónicas (tapas dinámicas de cilindros, paddings seguros).\n  3. Jerarquía tipográfica e identificación clara del nodo Hero.\n• ClosedLoopRepairEngine: Si VCS < 95, reajusta automáticamente coordenadas antes de exportar.", font_size=8, font_family=1, color="#7F1D1D", frame_id=fid)

    # ═════════════════════════════════════════════════════════════════════════
    # SECCIÓN 3: GUÍA PARA DESARROLLADORES & SDK (COLUMNA DERECHA, w=925)
    # ═════════════════════════════════════════════════════════════════════════
    scene.add_rect(1015, 420, 925, 900, bg="#FFFFFF", stroke="#D93829", stroke_w=1.5, roundness_type=3, frame_id=fid)
    scene.add_text(1040, 438, "3. GUÍA PARA DESARROLLADORES: APIS, SDK Y EJEMPLOS DE CÓDIGO", font_size=11, font_family=2, color="#D93829", frame_id=fid)

    # Modo 1: API de Alto Nivel
    code_m1 = [
        "import sketion",
        "result = sketion.render(",
        "    payload={\"title\": \"Fintech Core\", \"layers\": [",
        "        {\"name\": \"Ingress\", \"entities\": [{\"label\": \"Kong WAF\", \"role\": \"security\"}]},",
        "        {\"name\": \"Core\", \"entities\": [{\"label\": \"Payment Saga\", \"role\": \"service\", \"is_hero\": True}]}",
        "    ]},",
        "    audience=\"engineer\", archetype=\"layered\", aspect_ratio=\"16:9\"",
        ")",
        "result.export(\"architecture.excalidraw\")",
        "result.export(\"architecture.svg\", format=\"svg\")"
    ]
    scene.add_code_block(1035, 460, 885, 195, "MODO 1: API UNIFICADA DE ALTO NIVEL (sketion.render)", code_m1, lang="PYTHON", is_dark=True, frame_id=fid)

    # Modo 2: LayoutSolver Declarativo
    code_m2 = [
        "from sketion import LayoutSolver, LayoutAlgorithm, ExcalidrawScene",
        "solver = LayoutSolver(algorithm=LayoutAlgorithm.HIERARCHICAL, direction=\"LR\")",
        "solver.add_node(\"client\", \"Web Client\", role=\"actor\", shape=\"actor\", layer_index=0)",
        "solver.add_node(\"core\", \"Payment Saga\", role=\"service\", shape=\"card\", layer_index=1, is_hero=True)",
        "solver.add_node(\"db\", \"PostgreSQL Aurora\", role=\"database\", shape=\"database\", layer_index=2)",
        "solver.connect(\"client\", \"core\", label=\"HTTPS / mTLS\")",
        "solver.connect(\"core\", \"db\", label=\"SQL ACID\", relation_type=\"critical\")",
        "scene = ExcalidrawScene()",
        "fid = scene.add_frame(\"Core Architecture\", 0, 0, 1440, 900)",
        "solver.render_to_scene(scene, frame_id=fid)"
    ]
    scene.add_code_block(1035, 670, 885, 205, "MODO 2: LAYOUT SOLVER DECLARATIVO (layout/layout_solver.py)", code_m2, lang="PYTHON", is_dark=True, frame_id=fid)

    # Modo 3: Builder de Escenas de Bajo Nivel
    code_m3 = [
        "from sketion import ExcalidrawScene",
        "scene = ExcalidrawScene()",
        "fid = scene.add_frame(\"Ecosistema Custom\", 40, 30, 1440, 850)",
        "scene.add_quad_card(80, 120, 280, 110, \"Payment Service\", \"Saga ACID\", badge=\"CORE\", is_hero=True, frame_id=fid)",
        "scene.add_database_cylinder(80, 270, 240, 110, \"PostgreSQL Aurora\", \"Sync Multi-AZ\", badge=\"DB\", frame_id=fid)",
        "scene.add_arrow(220, 230, 220, 270, stroke=\"#2563EB\", stroke_w=2.0, frame_id=fid)",
        "scene.save(\"custom.excalidraw\")",
        "sketion.export(scene, \"custom.svg\", format=\"svg\")"
    ]
    scene.add_code_block(1035, 890, 885, 185, "MODO 3: BUILDER DE ESCENAS DE BAJO NIVEL (render/excalidraw_builder.py)", code_m3, lang="PYTHON", is_dark=True, frame_id=fid)

    # Estructura del Archivo .excalidraw (JSON con saltos de línea limpios sin desbordamiento)
    code_json = [
        "{",
        "  \"type\": \"excalidraw\", \"version\": 2, \"source\": \"sketion-v11.0-ga\",",
        "  \"elements\": [",
        "    { \"type\": \"rectangle\", \"id\": \"elem_1\", \"x\": 80, \"y\": 120, \"width\": 280, \"height\": 110,",
        "      \"strokeColor\": \"#0284C7\", \"backgroundColor\": \"#FFFFFF\", \"roundness\": { \"type\": 3 }, \"frameId\": \"f_1\" },",
        "    { \"type\": \"arrow\", \"id\": \"arr_1\", \"points\": [[0, 0], [0, 40]], \"strokeColor\": \"#2563EB\", \"strokeWidth\": 2 }",
        "  ],",
        "  \"appState\": { \"viewBackgroundColor\": \"#FFFFFF\", \"gridSize\": null }",
        "}"
    ]
    scene.add_code_block(1035, 1090, 885, 215, "ESTRUCTURA DEL ARCHIVO .EXCALIDRAW (JSON NATIVO)", code_json, lang="JSON", is_dark=False, frame_id=fid)

    # Exportación
    output_dir = os.path.join(workspace_dir, "docs")
    os.makedirs(output_dir, exist_ok=True)
    
    excalidraw_file = os.path.join(output_dir, "sketion_engine_architecture.excalidraw")
    scene.save(excalidraw_file)
    print(f"Saved Excalidraw: {excalidraw_file}")
    
    svg_file = os.path.join(output_dir, "sketion_engine_architecture.svg")
    sketion.export(scene, svg_file, format="svg")
    print(f"Saved SVG: {svg_file}")

if __name__ == "__main__":
    build_architecture_diagram()
