"""
Script para generar la Arquitectura SaaS B2B Moderna usando Sketion Engine
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

    title = "Arquitectura SaaS B2B Moderna"

    # 1. Definición de Scopes / Zonas de Infraestructura
    scopes = [
        {
            "id": "scope_edge",
            "label": "EDGE & INGRESS LAYER",
            "rel_x": 30,
            "rel_y": 80,
            "w": 280,
            "h": 620
        },
        {
            "id": "scope_core",
            "label": "GATEWAY & MICROSERVICES",
            "rel_x": 340,
            "rel_y": 80,
            "w": 380,
            "h": 620
        },
        {
            "id": "scope_async",
            "label": "ASYNC PROCESSING & DATA",
            "rel_x": 750,
            "rel_y": 80,
            "w": 380,
            "h": 620
        },
        {
            "id": "scope_external",
            "label": "THIRD-PARTY SERVICES",
            "rel_x": 1160,
            "rel_y": 80,
            "w": 260,
            "h": 620
        }
    ]

    # 2. Nodos con Doble Jerarquía
    nodes = [
        # Edge
        {
            "id": "web_app",
            "label": "Web Dashboard (Next.js)",
            "sublabel": "B2B Admin Panel",
            "metadata": ":3000",
            "rel_x": 50,
            "rel_y": 140
        },
        {
            "id": "cdn_waf",
            "label": "Cloudflare Edge",
            "sublabel": "WAF & DDoS Shield",
            "metadata": ":443",
            "rel_x": 50,
            "rel_y": 300
        },
        # Core
        {
            "id": "api_gateway",
            "label": "API Gateway (FastAPI)",
            "sublabel": "Rate Limit & Routing",
            "metadata": ":8000",
            "is_hero": True,  # Nodo focal de acento
            "rel_x": 380,
            "rel_y": 140
        },
        {
            "id": "auth_service",
            "label": "Auth & RBAC Service",
            "sublabel": "SAML / OIDC / JWT",
            "metadata": ":8081",
            "rel_x": 380,
            "rel_y": 300
        },
        {
            "id": "tenant_service",
            "label": "Tenant Service",
            "sublabel": "Multi-Tenant Isolation",
            "metadata": ":8082",
            "rel_x": 380,
            "rel_y": 460
        },
        # Async & Data
        {
            "id": "event_bus",
            "label": "Event Bus (Kafka / Redis)",
            "sublabel": "Event Streaming",
            "metadata": ":9092",
            "rel_x": 790,
            "rel_y": 140
        },
        {
            "id": "background_worker",
            "label": "Async Workers",
            "sublabel": "Reportes & Webhooks",
            "metadata": "Celery Pool",
            "rel_x": 790,
            "rel_y": 300
        },
        {
            "id": "db_postgres",
            "label": "PostgreSQL Multi-Tenant",
            "sublabel": "Schemas aislados por cliente",
            "metadata": ":5432",
            "rel_x": 790,
            "rel_y": 460
        },
        # External
        {
            "id": "stripe",
            "label": "Stripe Billing",
            "sublabel": "Suscripciones B2B",
            "metadata": "API v1",
            "rel_x": 1180,
            "rel_y": 140
        },
        {
            "id": "s3_storage",
            "label": "AWS S3 / R2",
            "sublabel": "Facturas & Documentos",
            "metadata": "Blob Store",
            "rel_x": 1180,
            "rel_y": 300
        },
        {
            "id": "email_service",
            "label": "Resend / SendGrid",
            "sublabel": "Emails Transaccionales",
            "metadata": "SMTP/API",
            "rel_x": 1180,
            "rel_y": 460
        }
    ]

    # 3. Conexiones ortogonales
    edges = [
        { "from": "web_app", "to": "cdn_waf", "label": "HTTPS" },
        { "from": "cdn_waf", "to": "api_gateway", "label": "Origin Route" },
        { "from": "api_gateway", "to": "auth_service", "label": "Verify SAML/JWT" },
        { "from": "api_gateway", "to": "tenant_service", "label": "Tenant Context" },
        { "from": "tenant_service", "to": "event_bus", "label": "Emit Event" },
        { "from": "event_bus", "to": "background_worker", "label": "Consume" },
        { "from": "tenant_service", "to": "db_postgres", "label": "SQL CRUD" },
        { "from": "background_worker", "to": "s3_storage", "label": "Generate PDF" },
        { "from": "background_worker", "to": "email_service", "label": "Send Email" },
        { "from": "tenant_service", "to": "stripe", "label": "Usage Metering" }
    ]

    # 4. Render con el motor RED
    engine_red(scene, title, nodes, edges, scopes=scopes, palette=DEFAULT_PALETTE, w=1480, h=750)

    # 5. Validación integral y Quality Score
    sem_diagram = SemanticDiagram(
        title=title,
        semantic_type="architecture",
        detail_level=DetailLevel.DETAILED,
        output_preset=OutputPreset.DEEP_DIVE,
        engine="red",
        scopes=[Scope(id=s["id"], label=s["label"]) for s in scopes],
        nodes=[SemanticNode(id=n["id"], label=n["label"], sublabel=n.get("sublabel"), is_hero=n.get("is_hero", False)) for n in nodes],
        edges=[SemanticEdge(from_node=e["from"], to_node=e["to"], label=e.get("label")) for e in edges]
    )

    scene_data, report = validate_scene(scene.to_dict(), diagram=sem_diagram, auto_repair=True)
    print(report.summary())

    output_path = os.path.join(workspace_dir, "arquitectura_saas_b2b.excalidraw")
    scene.save(output_path)
    print(f"\nArchivo guardado con éxito en: {output_path}")

if __name__ == "__main__":
    generate()
