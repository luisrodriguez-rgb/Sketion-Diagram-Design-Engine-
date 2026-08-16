"""
Script para generar el diagrama explicativo de una API REST usando Sketion Engine
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

    title = "Funcionamiento de una API REST"

    # 1. Definición de Zonas / Scopes
    scopes = [
        {
            "id": "client_scope",
            "label": "CLIENT LAYER (CONSUMIDOR)",
            "rel_x": 30,
            "rel_y": 80,
            "w": 300,
            "h": 500
        },
        {
            "id": "api_scope",
            "label": "REST API SERVER (CORE)",
            "rel_x": 360,
            "rel_y": 80,
            "w": 400,
            "h": 500
        },
        {
            "id": "data_scope",
            "label": "PERSISTENCE & EXTERNAL",
            "rel_x": 790,
            "rel_y": 80,
            "w": 320,
            "h": 500
        }
    ]

    # 2. Nodos con Doble Jerarquía
    nodes = [
        {
            "id": "client_web",
            "label": "Cliente Web / Frontend",
            "sublabel": "Browser / React App",
            "metadata": "HTTP Client",
            "rel_x": 50,
            "rel_y": 140
        },
        {
            "id": "client_mobile",
            "label": "App Móvil",
            "sublabel": "iOS / Android App",
            "metadata": "Fetch / Axios",
            "rel_x": 50,
            "rel_y": 300
        },
        {
            "id": "api_router",
            "label": "API Router & Endpoints",
            "sublabel": "/api/v1/users · /orders",
            "metadata": ":8000",
            "is_hero": True,  # Nodo focal acentuado
            "rel_x": 400,
            "rel_y": 140
        },
        {
            "id": "api_middleware",
            "label": "Middleware & Lógica",
            "sublabel": "Auth JWT + Validación JSON",
            "metadata": "Controller",
            "rel_x": 400,
            "rel_y": 300
        },
        {
            "id": "database",
            "label": "Base de Datos",
            "sublabel": "PostgreSQL / MongoDB",
            "metadata": ":5432",
            "rel_x": 820,
            "rel_y": 140
        },
        {
            "id": "external_api",
            "label": "Servicio Externo",
            "sublabel": "Pasarela / Notificaciones",
            "metadata": "OAuth2",
            "rel_x": 820,
            "rel_y": 300
        }
    ]

    # 3. Conexiones con verbos y protocolos REST
    edges = [
        { "from": "client_web", "to": "api_router", "label": "GET/POST HTTP Request" },
        { "from": "client_mobile", "to": "api_router", "label": "PUT/DELETE + Headers" },
        { "from": "api_router", "to": "api_middleware", "label": "Dispatch & Auth" },
        { "from": "api_middleware", "to": "database", "label": "SQL Queries / CRUD" },
        { "from": "api_middleware", "to": "external_api", "label": "Webhook / HTTPS" },
        { "from": "api_router", "to": "client_web", "label": "200 OK + JSON Response" }
    ]

    # 4. Render con el motor RED (Arquitectura estructurada)
    engine_red(scene, title, nodes, edges, scopes=scopes, palette=DEFAULT_PALETTE, w=1200, h=650)

    # 5. Validación y cálculo de Fidelity & Quality
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

    output_path = os.path.join(workspace_dir, "api_rest_explicacion.excalidraw")
    scene.save(output_path)
    print(f"\nArchivo guardado con éxito en: {output_path}")

if __name__ == "__main__":
    generate()
