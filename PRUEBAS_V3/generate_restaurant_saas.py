"""
Sketion Master Generator — SaaS B2B de Reservas y Gestión para Restaurantes
Genera la arquitectura completa en PRUEBAS_V3/ estructurada en:
- Frame 1: Arquitectura Global del Sistema (7 Scopes / Zonas)
- Frame 2: Máquina de Estados y Prevención de Doble Reserva (Concurrencia)
- Frame 3: Matriz de Resiliencia y Manejo de Fallos (10 Escenarios Críticos)
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place, compute_card_dimensions
from engines.recipes import engine_red, engine_flujo, engine_matriz, DEFAULT_PALETTE
from semantic.models import SemanticDiagram, SemanticNode, SemanticEdge, Scope, DetailLevel, OutputPreset, SemanticFlowStep
from validation.validator import validate_scene

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V3")
os.makedirs(OUT_DIR, exist_ok=True)


def build_restaurant_saas_scene():
    place_reset(max_row_w=5500, gap=180)
    scene = ExcalidrawScene(roughness=0, bg_color="#ffffff")

    # =========================================================================
    # FRAME 1: ARQUITECTURA GLOBAL DEL SISTEMA (7 SCOPES)
    # =========================================================================
    title_f1 = "Arquitectura de Plataforma SaaS de Restaurantes"

    scopes_f1 = [
        {"id": "sc_clients", "label": "1. CANALES Y USUARIOS", "rel_x": 30, "rel_y": 90, "w": 340, "h": 720},
        {"id": "sc_edge", "label": "2. EDGE & SEGURIDAD", "rel_x": 420, "rel_y": 90, "w": 380, "h": 720},
        {"id": "sc_core", "label": "3. SERVICIOS CORE & NEGOCIO", "rel_x": 850, "rel_y": 90, "w": 420, "h": 720},
        {"id": "sc_async", "label": "4. STREAMING ASÍNCRONO & WORKERS", "rel_x": 1320, "rel_y": 90, "w": 400, "h": 720},
        {"id": "sc_data", "label": "5. PERSISTENCIA & DATA PLATFORM", "rel_x": 1770, "rel_y": 90, "w": 380, "h": 720},
        {"id": "sc_ext", "label": "6. PROVEEDORES EXTERNOS", "rel_x": 2200, "rel_y": 90, "w": 340, "h": 720}
    ]

    nodes_f1 = [
        # Sc 1: Clients
        {"id": "client_web", "label": "Cliente Final (Web/App)", "sublabel": "Búsqueda & Reserva Online", "metadata": "Next.js / Flutter", "scope_id": "sc_clients", "rel_x": 55, "rel_y": 150},
        {"id": "staff_dashboard", "label": "Dashboard del Restaurante", "sublabel": "Zonas, Mesas & Turnos", "metadata": "Staff Panel", "scope_id": "sc_clients", "rel_x": 55, "rel_y": 330},
        {"id": "admin_console", "label": "SuperAdmin Console", "sublabel": "Métricas, Planes & Auditoría", "metadata": "Platform Admin", "scope_id": "sc_clients", "rel_x": 55, "rel_y": 510},

        # Sc 2: Edge
        {"id": "cloudflare_edge", "label": "Cloudflare WAF & Edge", "sublabel": "Rate Limit & Shield DDoS", "metadata": ":443", "scope_id": "sc_edge", "rel_x": 450, "rel_y": 150},
        {"id": "api_gateway", "label": "API Gateway & Router", "sublabel": "Tenant Context & Load Balance", "metadata": ":8000", "scope_id": "sc_edge", "rel_x": 450, "rel_y": 330},
        {"id": "auth_service", "label": "Auth & RBAC Service", "sublabel": "OAuth2 / Magic Links / JWT", "metadata": ":8081", "scope_id": "sc_edge", "rel_x": 450, "rel_y": 510},

        # Sc 3: Core
        {"id": "reservation_service", "label": "Reservation Service", "sublabel": "Ciclo de Vida & Consistencia", "metadata": "Core Hero", "is_hero": True, "scope_id": "sc_core", "rel_x": 885, "rel_y": 150},
        {"id": "availability_service", "label": "Availability Service", "sublabel": "Cálculo de Mesas en Tiempo Real", "metadata": "Focal Engine", "scope_id": "sc_core", "rel_x": 885, "rel_y": 330},
        {"id": "table_service", "label": "Table & Floor Plan Service", "sublabel": "Aforo, Zonas & Combinaciones", "metadata": ":8082", "scope_id": "sc_core", "rel_x": 885, "rel_y": 480},
        {"id": "payment_service", "label": "Payment & Billing Service", "sublabel": "Depósitos & Facturación B2B", "metadata": ":8083", "scope_id": "sc_core", "rel_x": 885, "rel_y": 630},

        # Sc 4: Async
        {"id": "kafka_bus", "label": "Kafka Event Streaming", "sublabel": "ReservationCreated, Confirmed", "metadata": ":9092", "scope_id": "sc_async", "rel_x": 1355, "rel_y": 150},
        {"id": "notification_worker", "label": "Notification Worker", "sublabel": "Confirmaciones & Recordatorios", "metadata": "Async Worker", "scope_id": "sc_async", "rel_x": 1355, "rel_y": 330},
        {"id": "analytics_worker", "label": "Analytics & Audit Worker", "sublabel": "Ocupación, Conversión & Logs", "metadata": "OLAP Sync", "scope_id": "sc_async", "rel_x": 1355, "rel_y": 510},

        # Sc 5: Data
        {"id": "postgres_db", "label": "PostgreSQL Multi-Tenant", "sublabel": "ACID / Row-Level Security", "metadata": ":5432", "scope_id": "sc_data", "rel_x": 1805, "rel_y": 150},
        {"id": "redis_cluster", "label": "Redis Lock & Cache", "sublabel": "Locks Distribuidos & Hold 120s", "metadata": ":6379", "scope_id": "sc_data", "rel_x": 1805, "rel_y": 330},
        {"id": "s3_storage", "label": "AWS S3 / R2 Storage", "sublabel": "Cartas, Menús & Fotos", "metadata": "Blob Store", "scope_id": "sc_data", "rel_x": 1805, "rel_y": 510},

        # Sc 6: External
        {"id": "stripe_gateway", "label": "Stripe Payments", "sublabel": "Tokenized Cards & Holds", "metadata": "PCI-DSS", "scope_id": "sc_ext", "rel_x": 2235, "rel_y": 150},
        {"id": "whatsapp_twilio", "label": "WhatsApp / SMS / Twilio", "sublabel": "Mensajería Transaccional", "metadata": "Messaging", "scope_id": "sc_ext", "rel_x": 2235, "rel_y": 330},
        {"id": "resend_email", "label": "Resend / SendGrid", "sublabel": "Emails & Recordatorios", "metadata": "SMTP/API", "scope_id": "sc_ext", "rel_x": 2235, "rel_y": 510}
    ]

    edges_f1 = [
        {"from": "client_web", "to": "cloudflare_edge", "label": "HTTPS"},
        {"from": "staff_dashboard", "to": "cloudflare_edge", "label": "HTTPS Auth"},
        {"from": "admin_console", "to": "cloudflare_edge", "label": "Admin Token"},
        {"from": "cloudflare_edge", "to": "api_gateway", "label": "Origin Route"},
        {"from": "api_gateway", "to": "auth_service", "label": "Verify JWT"},
        {"from": "api_gateway", "to": "reservation_service", "label": "POST /reservations"},
        {"from": "api_gateway", "to": "availability_service", "label": "GET /availability"},
        {"from": "api_gateway", "to": "table_service", "label": "Floor Layout"},
        {"from": "reservation_service", "to": "redis_cluster", "label": "Lock Mesa 120s"},
        {"from": "reservation_service", "to": "postgres_db", "label": "Commit Reserva"},
        {"from": "reservation_service", "to": "kafka_bus", "label": "Emit Confirmed"},
        {"from": "reservation_service", "to": "payment_service", "label": "Hold Depósito"},
        {"from": "availability_service", "to": "redis_cluster", "label": "Check Hold"},
        {"from": "availability_service", "to": "postgres_db", "label": "Read Schedule"},
        {"from": "kafka_bus", "to": "notification_worker", "label": "Consume Event"},
        {"from": "kafka_bus", "to": "analytics_worker", "label": "Stream Event"},
        {"from": "notification_worker", "to": "whatsapp_twilio", "label": "Send WhatsApp"},
        {"from": "notification_worker", "to": "resend_email", "label": "Send Email"},
        {"from": "payment_service", "to": "stripe_gateway", "label": "Charge Hold"}
    ]

    engine_red(scene, title_f1, nodes_f1, edges_f1, scopes=scopes_f1, palette=DEFAULT_PALETTE, w=2650, h=880)

    # =========================================================================
    # FRAME 2: MÁQUINA DE ESTADOS Y CONTROL DE CONCURRENCIA
    # =========================================================================
    title_f2 = "Ciclo de Vida de Reserva y Bloqueo Concurrente"
    steps_f2 = [
        {"step_num": "01", "label": "Requested\nIntento de Reserva", "is_hero": False, "edge_label": "Verificar"},
        {"step_num": "02", "label": "Pending (Hold 120s)\nLock Temporal en Redis", "is_hero": False, "edge_label": "Pagar/Confirmar"},
        {"step_num": "03", "label": "Confirmed\nTransacción ACID & Notif", "is_hero": True, "edge_label": "Llegada Cliente"},
        {"step_num": "04", "label": "Seated\nMesa Ocupada en Vivo", "is_hero": False, "edge_label": "Servicio Finalizado"},
        {"step_num": "05", "label": "Completed\nFacturado & Historial", "is_hero": False}
    ]
    engine_flujo(scene, title_f2, steps_f2, palette=DEFAULT_PALETTE, wave=False, w=1550, h=400)

    # =========================================================================
    # FRAME 3: MATRIZ DE RESILIENCIA Y MANEJO DE 10 FALLOS PARCIALES
    # =========================================================================
    title_f3 = "Matriz de Resiliencia y Manejo de Fallos Parciales"
    headers_f3 = ["Escenario de Fallo", "Componente Detector", "Estado de Reserva", "Mecanismo de Consistencia y Recuperación"]
    rows_f3 = [
        {"Escenario de Fallo": "1. WhatsApp Provider Caído", "Componente Detector": "Notification Worker", "Estado de Reserva": "CONFIRMED (Sin Rollback)", "Mecanismo de Consistencia y Recuperación": "Reintentos exponenciales con Dead Letter Queue (DLQ) y fallback a Email."},
        {"Escenario de Fallo": "2. Pasarela Pagos Lenta", "Componente Detector": "Payment Service", "Estado de Reserva": "PENDING (Con Lease)", "Mecanismo de Consistencia y Recuperación": "Idempotency Keys + Reconciliación Asíncrona vía Stripe Webhooks."},
        {"Escenario de Fallo": "3. Concurrencia Misma Mesa", "Componente Detector": "Reservation Service", "Estado de Reserva": "1 CONFIRMED / 1 REJECTED", "Mecanismo de Consistencia y Recuperación": "Redis Lock atómico (SETNX TTL 120s) + PostgreSQL Conditional WHERE status='free'."},
        {"Escenario de Fallo": "4. Caída Total de Redis", "Componente Detector": "Availability Service", "Estado de Reserva": "DEGRADADO A DB LOCK", "Mecanismo de Consistencia y Recuperación": "Fallback a PostgreSQL Advisory Locks transaccionales directos."},
        {"Escenario de Fallo": "5. Consumer Caído en Evento", "Componente Detector": "Kafka Consumer Group", "Estado de Reserva": "CONFIRMED (Preservado)", "Mecanismo de Consistencia y Recuperación": "Rebalanceo automático; commit de offset solo tras procesamiento exitoso."},
        {"Escenario de Fallo": "6. Evento Duplicado (At-least-once)", "Componente Detector": "Analytics & Notif Worker", "Estado de Reserva": "SIN DUPLICACIÓN", "Mecanismo de Consistencia y Recuperación": "Consumidores idempotentes con tabla 'processed_events' (Deduplicación)."},
        {"Escenario de Fallo": "7. Alta Latencia en DB Principal", "Componente Detector": "API Gateway / Healthcheck", "Estado de Reserva": "QUEUE BUFFERING", "Mecanismo de Consistencia y Recuperación": "Circuit Breaker en Gateway + derivación de lecturas de catálogo a Read Replicas."},
        {"Escenario de Fallo": "8. Cambio Horario con Reservas", "Componente Detector": "Restaurant Service", "Estado de Reserva": "CONFIRMED (Grandfathered)", "Mecanismo de Consistencia y Recuperación": "Reservas existentes protegidas; alerta al gerente para reubicación asistida."},
        {"Escenario de Fallo": "9. Expiración durante Checkout", "Componente Detector": "Redis Key Expiry Event", "Estado de Reserva": "EXPIRED", "Mecanismo de Consistencia y Recuperación": "Liberación atómica de mesa; aviso claro en UI con recálculo de disponibilidad."},
        {"Escenario de Fallo": "10. Cancelación Manual en Pending", "Componente Detector": "Staff Dashboard", "Estado de Reserva": "CANCELLED", "Mecanismo de Consistencia y Recuperación": "Cancelación atómica de PaymentIntent en Stripe + liberación inmediata de mesa."}
    ]
    engine_matriz(scene, title_f3, headers_f3, rows_f3, palette=DEFAULT_PALETTE, w=2100, h=780)

    # =========================================================================
    # VALIDACIÓN COMPLETA CON QUALITY & FIDELITY ENGINE
    # =========================================================================
    sem_diagram = SemanticDiagram(
        title=title_f1,
        semantic_type="architecture",
        detail_level=DetailLevel.DETAILED,
        output_preset=OutputPreset.DEEP_DIVE,
        engine="red",
        scopes=[Scope(id=s["id"], label=s["label"]) for s in scopes_f1],
        nodes=[SemanticNode(id=n["id"], label=n["label"], sublabel=n.get("sublabel"), is_hero=n.get("is_hero", False)) for n in nodes_f1],
        edges=[SemanticEdge(from_node=e["from"], to_node=e["to"], label=e.get("label")) for e in edges_f1]
    )

    scene_data, report = validate_scene(scene.to_dict(), diagram=sem_diagram, auto_repair=True)
    
    out_file = os.path.join(OUT_DIR, "arquitectura_restaurantes_saas.excalidraw")
    scene.save(out_file)
    
    return report, out_file


if __name__ == "__main__":
    report, filepath = build_restaurant_saas_scene()
    print("==================================================")
    print("REPORTE DE AUDITORÍA Y CALIDAD DE SKETION")
    print("==================================================")
    print(report.summary())
    print(f"\nArchivo .excalidraw exportado en: {filepath}")
