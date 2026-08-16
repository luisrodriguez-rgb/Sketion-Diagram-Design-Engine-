"""
Sketion Dogfooding Benchmark Suite 2.8
Genera las versiones corregidas de todos los diagramas en PRUEBAS_V2/
aplicando:
1. Dynamic Card Dimensions (Cero desbordamientos de texto)
2. Pill Labels en conectores (Cero choques con líneas)
3. Auto-Fit de Frames (Cero espacios blancos muertos)
4. Anclajes laterales limpios
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset
from engines.recipes import engine_red, engine_flujo, DEFAULT_PALETTE
from semantic.models import SemanticDiagram, SemanticNode, SemanticEdge, Scope, DetailLevel, OutputPreset, SemanticFlowStep
from validation.validator import validate_scene

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V2")
os.makedirs(OUT_DIR, exist_ok=True)


def gen_ecommerce_flow():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color="#ffffff")
    title = "Proceso de Compra E-Commerce"
    steps = [
        {"step_num": "01", "label": "Catálogo y Carrito\nSelección de Productos", "is_hero": False, "edge_label": "Checkout"},
        {"step_num": "02", "label": "Datos de Envío\nDirección y Flete", "is_hero": False, "edge_label": "Pagar"},
        {"step_num": "03", "label": "Pasarela de Pago\nStripe / Tarjeta", "is_hero": True, "edge_label": "Aprobado 200"},
        {"step_num": "04", "label": "Confirmación\nOrden y Factura", "is_hero": False, "edge_label": "Almacén"},
        {"step_num": "05", "label": "Despacho y Tracking\nEnvío por Courier", "is_hero": False}
    ]
    engine_flujo(scene, title, steps, palette=DEFAULT_PALETTE, wave=False, w=1450, h=380)
    sem_diagram = SemanticDiagram(
        title=title, semantic_type="flowchart", detail_level=DetailLevel.BALANCED,
        output_preset=OutputPreset.DOCS, engine="flujo",
        steps=[SemanticFlowStep(step_num=s["step_num"], label=s["label"], is_hero=s.get("is_hero", False)) for s in steps]
    )
    scene_data, report = validate_scene(scene.to_dict(), diagram=sem_diagram, auto_repair=True)
    out_path = os.path.join(OUT_DIR, "proceso_compra_tienda.excalidraw")
    scene.save(out_path)
    print(f"✅ {title} -> {report.sketion_overall_score}/100 | Guardado en PRUEBAS_V2/")


def gen_saas_lifecycle():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color="#ffffff")
    title = "Ciclo de Vida de un Producto SaaS"
    steps = [
        {"step_num": "01", "label": "Ideación y Discovery\nValidación de Problema", "is_hero": False, "edge_label": "Validar PMF"},
        {"step_num": "02", "label": "MVP y Beta Privada\nCore Features & Feedback", "is_hero": False, "edge_label": "Lanzamiento"},
        {"step_num": "03", "label": "Product-Market Fit\nTracción y Retención", "is_hero": True, "edge_label": "Escalar PLG"},
        {"step_num": "04", "label": "Crecimiento y Escala\nAdquisición & Expansión", "is_hero": False, "edge_label": "Madurez"},
        {"step_num": "05", "label": "Madurez y Evolución\nLTV Máximo & Enterprise", "is_hero": False}
    ]
    engine_flujo(scene, title, steps, palette=DEFAULT_PALETTE, wave=False, w=1450, h=380)
    sem_diagram = SemanticDiagram(
        title=title, semantic_type="flowchart", detail_level=DetailLevel.BALANCED,
        output_preset=OutputPreset.DOCS, engine="flujo",
        steps=[SemanticFlowStep(step_num=s["step_num"], label=s["label"], is_hero=s.get("is_hero", False)) for s in steps]
    )
    scene_data, report = validate_scene(scene.to_dict(), diagram=sem_diagram, auto_repair=True)
    out_path = os.path.join(OUT_DIR, "ciclo_vida_producto_saas.excalidraw")
    scene.save(out_path)
    print(f"✅ {title} -> {report.sketion_overall_score}/100 | Guardado en PRUEBAS_V2/")


def gen_rest_api():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color="#ffffff")
    title = "Funcionamiento de una API REST"
    scopes = [
        {"id": "s_client", "label": "1. CLIENT LAYER (CONSUMIDOR)", "rel_x": 30, "rel_y": 80, "w": 340, "h": 500},
        {"id": "s_core", "label": "2. REST API SERVER (CORE)", "rel_x": 410, "rel_y": 80, "w": 420, "h": 500},
        {"id": "s_data", "label": "3. PERSISTENCE & EXTERNAL", "rel_x": 870, "rel_y": 80, "w": 360, "h": 500}
    ]
    nodes = [
        {"id": "c_web", "label": "Cliente Web Frontend", "sublabel": "Browser / React 18", "metadata": "HTTP Client", "rel_x": 50, "rel_y": 140},
        {"id": "c_mob", "label": "App Móvil", "sublabel": "Flutter / Axios", "metadata": "Bearer Auth", "rel_x": 50, "rel_y": 320},
        {"id": "r_api", "label": "API Router & Endpoints", "sublabel": "/api/v1/users · /orders", "metadata": ":8000", "is_hero": True, "rel_x": 440, "rel_y": 140},
        {"id": "r_mid", "label": "Middleware & Lógica", "sublabel": "Auth JWT + Validación JSON", "metadata": "Controller", "rel_x": 440, "rel_y": 320},
        {"id": "d_db", "label": "Base de Datos", "sublabel": "PostgreSQL / Prisma", "metadata": ":5432", "rel_x": 900, "rel_y": 140},
        {"id": "d_ext", "label": "Servicio Externo", "sublabel": "Pasarela / Notificaciones", "metadata": "OAuth2", "rel_x": 900, "rel_y": 320}
    ]
    edges = [
        {"from": "c_web", "to": "r_api", "label": "GET/POST HTTP"},
        {"from": "c_mob", "to": "r_api", "label": "PUT/DELETE"},
        {"from": "r_api", "to": "r_mid", "label": "Dispatch & Auth"},
        {"from": "r_mid", "to": "d_db", "label": "SQL CRUD"},
        {"from": "r_mid", "to": "d_ext", "label": "Webhook"},
        {"from": "r_api", "to": "c_web", "label": "200 OK JSON"}
    ]
    engine_red(scene, title, nodes, edges, scopes=scopes, palette=DEFAULT_PALETTE, w=1300, h=660)
    out_path = os.path.join(OUT_DIR, "api_rest_explicacion.excalidraw")
    scene.save(out_path)
    print(f"✅ {title} -> Guardado en PRUEBAS_V2/")


def gen_saas_b2b():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color="#ffffff")
    title = "Arquitectura SaaS B2B Moderna"
    scopes = [
        {"id": "s1", "label": "1. EDGE & INGRESS", "rel_x": 30, "rel_y": 80, "w": 340, "h": 620},
        {"id": "s2", "label": "2. GATEWAY & CORE", "rel_x": 410, "rel_y": 80, "w": 420, "h": 620},
        {"id": "s3", "label": "3. ASYNC & DATA", "rel_x": 870, "rel_y": 80, "w": 420, "h": 620},
        {"id": "s4", "label": "4. THIRD-PARTY", "rel_x": 1330, "rel_y": 80, "w": 300, "h": 620}
    ]
    nodes = [
        {"id": "w_app", "label": "Web Dashboard Next.js", "sublabel": "B2B Admin Panel", "metadata": ":3000", "rel_x": 50, "rel_y": 140},
        {"id": "w_cdn", "label": "Cloudflare Edge", "sublabel": "WAF & DDoS Shield", "metadata": ":443", "rel_x": 50, "rel_y": 320},
        {"id": "a_gate", "label": "API Gateway FastAPI", "sublabel": "Rate Limit & Routing", "metadata": ":8000", "is_hero": True, "rel_x": 440, "rel_y": 140},
        {"id": "a_auth", "label": "Auth & RBAC Service", "sublabel": "SAML / OIDC / JWT", "metadata": ":8081", "rel_x": 440, "rel_y": 320},
        {"id": "a_ten", "label": "Tenant Service", "sublabel": "Multi-Tenant Context", "metadata": ":8082", "rel_x": 440, "rel_y": 480},
        {"id": "d_bus", "label": "Event Bus (Kafka)", "sublabel": "Event Streaming", "metadata": ":9092", "rel_x": 900, "rel_y": 140},
        {"id": "d_work", "label": "Async Workers", "sublabel": "Reportes & Webhooks", "metadata": "Celery", "rel_x": 900, "rel_y": 320},
        {"id": "d_sql", "label": "PostgreSQL Multi-Tenant", "sublabel": "Esquemas por cliente", "metadata": ":5432", "rel_x": 900, "rel_y": 480},
        {"id": "x_str", "label": "Stripe Billing", "sublabel": "Suscripciones B2B", "metadata": "API v1", "rel_x": 1360, "rel_y": 140},
        {"id": "x_s3", "label": "AWS S3 / R2", "sublabel": "Facturas & Docs", "metadata": "Blob Store", "rel_x": 1360, "rel_y": 320},
        {"id": "x_mail", "label": "Resend / SendGrid", "sublabel": "Emails Transaccionales", "metadata": "SMTP", "rel_x": 1360, "rel_y": 480}
    ]
    edges = [
        {"from": "w_app", "to": "w_cdn", "label": "HTTPS"},
        {"from": "w_cdn", "to": "a_gate", "label": "Route"},
        {"from": "a_gate", "to": "a_auth", "label": "SAML Auth"},
        {"from": "a_gate", "to": "a_ten", "label": "Tenant"},
        {"from": "a_ten", "to": "d_bus", "label": "Emit Event"},
        {"from": "d_bus", "to": "d_work", "label": "Consume"},
        {"from": "a_ten", "to": "d_sql", "label": "SQL CRUD"},
        {"from": "d_work", "to": "x_s3", "label": "Save PDF"},
        {"from": "d_work", "to": "x_mail", "label": "Send Email"},
        {"from": "a_ten", "to": "x_str", "label": "Billing"}
    ]
    engine_red(scene, title, nodes, edges, scopes=scopes, palette=DEFAULT_PALETTE, w=1680, h=750)
    out_path = os.path.join(OUT_DIR, "arquitectura_saas_b2b.excalidraw")
    scene.save(out_path)
    print(f"✅ {title} -> Guardado en PRUEBAS_V2/")


def gen_ecommerce_platform():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color="#ffffff")
    title = "Arquitectura de Plataforma E-Commerce Global"
    scopes = [
        {"id": "sc1", "label": "1. USUARIOS & FRONTEND", "rel_x": 30, "rel_y": 80, "w": 340, "h": 640},
        {"id": "sc2", "label": "2. INFRAESTRUCTURA DE APP", "rel_x": 410, "rel_y": 80, "w": 400, "h": 640},
        {"id": "sc3", "label": "3. SERVICIOS CORE", "rel_x": 850, "rel_y": 80, "w": 400, "h": 640},
        {"id": "sc4", "label": "4. BASE DE DATOS & EVENTOS", "rel_x": 1290, "rel_y": 80, "w": 380, "h": 640},
        {"id": "sc5", "label": "5. PROVEEDORES EXTERNOS", "rel_x": 1710, "rel_y": 80, "w": 340, "h": 640}
    ]
    nodes = [
        {"id": "ec_web", "label": "Web Storefront (Next.js)", "sublabel": "Catálogo & Carrito SSR", "metadata": ":3000", "rel_x": 50, "rel_y": 140},
        {"id": "ec_mob", "label": "App Móvil (Flutter)", "sublabel": "Compradores iOS/Android", "metadata": "Mobile", "rel_x": 50, "rel_y": 320},
        {"id": "ec_cdn", "label": "Cloudflare CDN / WAF", "sublabel": "Imágenes & Cache Edge", "metadata": "Edge", "rel_x": 50, "rel_y": 480},
        
        {"id": "ec_gate", "label": "API Gateway & Router", "sublabel": "Rate Limit & Load Balancer", "metadata": ":8000", "is_hero": True, "rel_x": 440, "rel_y": 140},
        {"id": "ec_auth", "label": "Auth & Sesiones", "sublabel": "JWT / OAuth2 / Perfiles", "metadata": ":8081", "rel_x": 440, "rel_y": 380},
        
        {"id": "ec_cat", "label": "Servicio de Catálogo", "sublabel": "Búsqueda Elasticsearch", "metadata": "Search", "rel_x": 880, "rel_y": 140},
        {"id": "ec_ord", "label": "Servicio de Pedidos", "sublabel": "Checkout & Saga Pattern", "metadata": ":8082", "rel_x": 880, "rel_y": 320},
        {"id": "ec_inv", "label": "Servicio de Inventario", "sublabel": "Bloqueo de Stock en Vivo", "metadata": ":8083", "rel_x": 880, "rel_y": 480},
        
        {"id": "ec_sql", "label": "PostgreSQL Primary/Replica", "sublabel": "Órdenes, Clientes & Stock", "metadata": ":5432", "rel_x": 1320, "rel_y": 140},
        {"id": "ec_red", "label": "Redis Cache Cluster", "sublabel": "Carritos Activos & Locks", "metadata": ":6379", "rel_x": 1320, "rel_y": 320},
        {"id": "ec_kaf", "label": "Kafka Event Streaming", "sublabel": "OrderPlaced, PaidEvents", "metadata": ":9092", "rel_x": 1320, "rel_y": 480},
        
        {"id": "ec_pay", "label": "Pasarelas de Pago", "sublabel": "Stripe / PayPal / Apple Pay", "metadata": "PCI-DSS", "rel_x": 1740, "rel_y": 140},
        {"id": "ec_cou", "label": "Logística & Courier", "sublabel": "FedEx / DHL / ShipStation", "metadata": "Tracking", "rel_x": 1740, "rel_y": 320},
        {"id": "ec_com", "label": "Comunicaciones", "sublabel": "Twilio SMS & Resend Email", "metadata": "SMTP", "rel_x": 1740, "rel_y": 480}
    ]
    edges = [
        {"from": "ec_web", "to": "ec_cdn", "label": "HTTPS"},
        {"from": "ec_mob", "to": "ec_gate", "label": "API Calls"},
        {"from": "ec_cdn", "to": "ec_gate", "label": "Origin Route"},
        {"from": "ec_gate", "to": "ec_auth", "label": "Verify Token"},
        {"from": "ec_gate", "to": "ec_cat", "label": "GET /products"},
        {"from": "ec_gate", "to": "ec_ord", "label": "POST /checkout"},
        {"from": "ec_ord", "to": "ec_inv", "label": "Lock Stock"},
        {"from": "ec_cat", "to": "ec_sql", "label": "Read Replica"},
        {"from": "ec_ord", "to": "ec_sql", "label": "Write Primary"},
        {"from": "ec_ord", "to": "ec_red", "label": "Cart State"},
        {"from": "ec_ord", "to": "ec_kaf", "label": "Emit OrderCreated"},
        {"from": "ec_ord", "to": "ec_pay", "label": "Charge Payment"},
        {"from": "ec_kaf", "to": "ec_cou", "label": "Fulfillment Job"},
        {"from": "ec_kaf", "to": "ec_com", "label": "Send Confirmation"}
    ]
    engine_red(scene, title, nodes, edges, scopes=scopes, palette=DEFAULT_PALETTE, w=2100, h=780)
    out_path = os.path.join(OUT_DIR, "arquitectura_plataforma_ecommerce.excalidraw")
    scene.save(out_path)
    print(f"✅ {title} -> Guardado en PRUEBAS_V2/")


if __name__ == "__main__":
    print("==================================================")
    print("EJECUTANDO BENCHMARK SKETION CORE EN PRUEBAS_V2/")
    print("==================================================\n")
    gen_ecommerce_flow()
    gen_saas_lifecycle()
    gen_rest_api()
    gen_saas_b2b()
    gen_ecommerce_platform()
    print("\n🎉 GENERACIONES EN PRUEBAS_V2/ COMPLETADAS CON ÉXITO!")
