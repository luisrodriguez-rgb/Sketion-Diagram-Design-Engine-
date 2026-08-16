"""
Script para generar la Arquitectura Completa de una Plataforma E-Commerce usando Sketion Engine
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

    title = "Arquitectura de Plataforma E-Commerce Global"

    # 1. Scopes / Zonas de la Plataforma
    scopes = [
        {
            "id": "scope_front",
            "label": "1. USUARIOS EXTERNOS & FRONTEND",
            "rel_x": 30,
            "rel_y": 80,
            "w": 280,
            "h": 640
        },
        {
            "id": "scope_gateway",
            "label": "2. INFRAESTRUCTURA DE APLICACIÓN",
            "rel_x": 340,
            "rel_y": 80,
            "w": 360,
            "h": 640
        },
        {
            "id": "scope_internal",
            "label": "3. SERVICIOS INTERNOS (CORE)",
            "rel_x": 730,
            "rel_y": 80,
            "w": 360,
            "h": 640
        },
        {
            "id": "scope_data",
            "label": "4. BASE DE DATOS & EVENTOS",
            "rel_x": 1120,
            "rel_y": 80,
            "w": 320,
            "h": 640
        },
        {
            "id": "scope_ext",
            "label": "5. PROVEEDORES EXTERNOS",
            "rel_x": 1470,
            "rel_y": 80,
            "w": 280,
            "h": 640
        }
    ]

    # 2. Nodos con Doble Jerarquía Tipográfica
    nodes = [
        # Scope 1: Front
        {
            "id": "storefront_web",
            "label": "Web Storefront (Next.js)",
            "sublabel": "Catálogo & Carrito SSR",
            "metadata": ":3000",
            "rel_x": 50,
            "rel_y": 140
        },
        {
            "id": "mobile_app",
            "label": "App Móvil (Flutter)",
            "sublabel": "Compradores iOS / Android",
            "metadata": "Mobile",
            "rel_x": 50,
            "rel_y": 300
        },
        {
            "id": "cdn_edge",
            "label": "Cloudflare CDN / WAF",
            "sublabel": "Imágenes de Producto & Cache",
            "metadata": "Edge",
            "rel_x": 50,
            "rel_y": 460
        },
        # Scope 2: App Infra
        {
            "id": "api_gateway",
            "label": "API Gateway & Router",
            "sublabel": "Rate Limit & Load Balancer",
            "metadata": ":8000",
            "is_hero": True,  # Nodo focal de acento
            "rel_x": 370,
            "rel_y": 140
        },
        {
            "id": "auth_service",
            "label": "Auth & Sesiones",
            "sublabel": "JWT / OAuth2 / Perfiles",
            "metadata": ":8081",
            "rel_x": 370,
            "rel_y": 360
        },
        # Scope 3: Servicios Internos
        {
            "id": "catalog_service",
            "label": "Servicio de Catálogo",
            "sublabel": "Búsqueda & Recomendaciones",
            "metadata": "Elasticsearch",
            "rel_x": 760,
            "rel_y": 140
        },
        {
            "id": "orders_service",
            "label": "Servicio de Pedidos",
            "sublabel": "Checkout & Orquestación Saga",
            "metadata": ":8082",
            "rel_x": 760,
            "rel_y": 300
        },
        {
            "id": "inventory_service",
            "label": "Servicio de Inventario",
            "sublabel": "Bloqueo de Stock en Tiempo Real",
            "metadata": ":8083",
            "rel_x": 760,
            "rel_y": 460
        },
        # Scope 4: Data & Events
        {
            "id": "db_postgres",
            "label": "PostgreSQL Primary/Replica",
            "sublabel": "Órdenes, Clientes & Productos",
            "metadata": ":5432",
            "rel_x": 1150,
            "rel_y": 140
        },
        {
            "id": "cache_redis",
            "label": "Redis Cache Cluster",
            "sublabel": "Carritos Activos & Locks",
            "metadata": ":6379",
            "rel_x": 1150,
            "rel_y": 300
        },
        {
            "id": "kafka_bus",
            "label": "Kafka Event Streaming",
            "sublabel": "OrderPlaced, PaymentApproved",
            "metadata": ":9092",
            "rel_x": 1150,
            "rel_y": 460
        },
        # Scope 5: Proveedores Externos
        {
            "id": "ext_payments",
            "label": "Pasarelas de Pago",
            "sublabel": "Stripe / PayPal / Apple Pay",
            "metadata": "PCI-DSS",
            "rel_x": 1500,
            "rel_y": 140
        },
        {
            "id": "ext_courier",
            "label": "Logística & Courier",
            "sublabel": "FedEx / DHL / ShipStation",
            "metadata": "Tracking API",
            "rel_x": 1500,
            "rel_y": 300
        },
        {
            "id": "ext_comms",
            "label": "Comunicaciones",
            "sublabel": "Twilio (SMS) & Resend (Email)",
            "metadata": "Transactional",
            "rel_x": 1500,
            "rel_y": 460
        }
    ]

    # 3. Conexiones ortogonales
    edges = [
        { "from": "storefront_web", "to": "cdn_edge", "label": "HTTPS" },
        { "from": "mobile_app", "to": "api_gateway", "label": "API Calls" },
        { "from": "cdn_edge", "to": "api_gateway", "label": "Origin Route" },
        { "from": "api_gateway", "to": "auth_service", "label": "Verify Token" },
        { "from": "api_gateway", "to": "catalog_service", "label": "GET /products" },
        { "from": "api_gateway", "to": "orders_service", "label": "POST /checkout" },
        { "from": "orders_service", "to": "inventory_service", "label": "Lock Stock" },
        { "from": "catalog_service", "to": "db_postgres", "label": "Read Replica" },
        { "from": "orders_service", "to": "db_postgres", "label": "Write Primary" },
        { "from": "orders_service", "to": "cache_redis", "label": "Cart State" },
        { "from": "orders_service", "to": "kafka_bus", "label": "Emit OrderCreated" },
        { "from": "orders_service", "to": "ext_payments", "label": "Charge Payment" },
        { "from": "kafka_bus", "to": "ext_courier", "label": "Fulfillment Job" },
        { "from": "kafka_bus", "to": "ext_comms", "label": "Send Confirmation" }
    ]

    # 4. Render
    engine_red(scene, title, nodes, edges, scopes=scopes, palette=DEFAULT_PALETTE, w=1800, h=780)

    # 5. Validación y Quality Score
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

    output_path = os.path.join(workspace_dir, "arquitectura_plataforma_ecommerce.excalidraw")
    scene.save(output_path)
    print(f"\nArchivo guardado con éxito en: {output_path}")

if __name__ == "__main__":
    generate()
