"""
Script para generar la explicación visual accesible de SaaS usando Sketion Engine
"""
import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset
from engines.recipes import engine_red, DEFAULT_PALETTE
from semantic.models import SemanticDiagram, SemanticNode, SemanticEdge, Scope, DetailLevel, OutputPreset
from validation.validator import validate_scene

def generate():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color="#ffffff")

    title = "Cómo Funciona un SaaS B2B (Explicado Simple)"

    # 1. Scopes con analogías claras
    scopes = [
        {
            "id": "scope_front",
            "label": "1. LA ENTRADA (PANTALLA Y SEGURIDAD)",
            "rel_x": 30,
            "rel_y": 80,
            "w": 300,
            "h": 580
        },
        {
            "id": "scope_core",
            "label": "2. EL CEREBRO CENTRAL (COORDINACIÓN)",
            "rel_x": 360,
            "rel_y": 80,
            "w": 380,
            "h": 580
        },
        {
            "id": "scope_back",
            "label": "3. LA COCINA Y ARCHIVO (TRABAJO)",
            "rel_x": 770,
            "rel_y": 80,
            "w": 360,
            "h": 580
        },
        {
            "id": "scope_ext",
            "label": "4. PROVEEDORES Y SOCIOS",
            "rel_x": 1160,
            "rel_y": 80,
            "w": 260,
            "h": 580
        }
    ]

    # 2. Nodos con analogías intuitivas
    nodes = [
        {
            "id": "ui_screen",
            "label": "La Pantalla de tu App",
            "sublabel": "Donde haces clic y trabajas",
            "metadata": "Frontend",
            "rel_x": 50,
            "rel_y": 140
        },
        {
            "id": "security_guard",
            "label": "El Guardia de Seguridad",
            "sublabel": "Bloquea ataques y tráfico falso",
            "metadata": "WAF / Firewall",
            "rel_x": 50,
            "rel_y": 340
        },
        {
            "id": "manager_gateway",
            "label": "El Gerente de Tráfico",
            "sublabel": "Recibe pedidos y reparte tareas",
            "metadata": "API Gateway",
            "is_hero": True,  # Nodo focal
            "rel_x": 390,
            "rel_y": 140
        },
        {
            "id": "auth_keys",
            "label": "Control de Llaves y Roles",
            "sublabel": "¿Quién eres y qué puedes ver?",
            "metadata": "Auth / Permisos",
            "rel_x": 390,
            "rel_y": 340
        },
        {
            "id": "workers_kitchen",
            "label": "Cocineros en Segundo Plano",
            "sublabel": "Hacen tareas pesadas sin trabarte",
            "metadata": "Async Workers",
            "rel_x": 800,
            "rel_y": 140
        },
        {
            "id": "database_vault",
            "label": "La Caja Fuerte de Datos",
            "sublabel": "Guarda clientes, precios y ventas",
            "metadata": "Base de Datos SQL",
            "rel_x": 800,
            "rel_y": 340
        },
        {
            "id": "ext_bank",
            "label": "El Banco (Cobros)",
            "sublabel": "Cobra tarjetas y suscripciones",
            "metadata": "Stripe",
            "rel_x": 1180,
            "rel_y": 140
        },
        {
            "id": "ext_postman",
            "label": "El Cartero (Correos)",
            "sublabel": "Envía facturas y alertas",
            "metadata": "Email Service",
            "rel_x": 1180,
            "rel_y": 340
        }
    ]

    # 3. Conexiones explicativas
    edges = [
        { "from": "ui_screen", "to": "security_guard", "label": "Envía clic" },
        { "from": "security_guard", "to": "manager_gateway", "label": "Paso limpio" },
        { "from": "manager_gateway", "to": "auth_keys", "label": "¿Permiso?" },
        { "from": "manager_gateway", "to": "database_vault", "label": "Buscar dato" },
        { "from": "manager_gateway", "to": "workers_kitchen", "label": "Tarea pesada" },
        { "from": "workers_kitchen", "to": "ext_postman", "label": "Mandar email" },
        { "from": "manager_gateway", "to": "ext_bank", "label": "Cobrar mes" }
    ]

    # 4. Render
    engine_red(scene, title, nodes, edges, scopes=scopes, palette=DEFAULT_PALETTE, w=1480, h=700)

    # 5. Validación y Quality Score
    sem_diagram = SemanticDiagram(
        title=title,
        semantic_type="architecture",
        detail_level=DetailLevel.BALANCED,
        output_preset=OutputPreset.DOCS,
        engine="red",
        scopes=[Scope(id=s["id"], label=s["label"]) for s in scopes],
        nodes=[SemanticNode(id=n["id"], label=n["label"], sublabel=n.get("sublabel"), is_hero=n.get("is_hero", False)) for n in nodes],
        edges=[SemanticEdge(from_node=e["from"], to_node=e["to"], label=e.get("label")) for e in edges]
    )

    scene_data, report = validate_scene(scene.to_dict(), diagram=sem_diagram, auto_repair=True)
    print(report.summary())

    output_path = os.path.join(workspace_dir, "arquitectura_saas_explicacion_simple.excalidraw")
    scene.save(output_path)
    print(f"\nArchivo guardado con éxito en: {output_path}")

if __name__ == "__main__":
    generate()
