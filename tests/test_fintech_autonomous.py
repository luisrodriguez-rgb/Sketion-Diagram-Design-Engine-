"""
Sketion 4.0 — Test Adversarial: Arquitectura de Pagos Fintech (Audiencia Mixta)
Ejecuta la síntesis semántica, layout por scopes, resolución de iconos por jerarquía,
enrutamiento ortogonal y validación de calidad.
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place
from validation.validator import validate_scene
from semantic.icon_resolver import resolve_node_icon

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


def build_fintech_autonomous_architecture():
    place_reset()
    scene = ExcalidrawScene(roughness=0, bg_color=PALETTE["CANVAS"])
    
    w, h = 3400.0, 1150.0
    fx, fy = place(w, h)
    fid = scene.add_frame("ARQUITECTURA PLATAFORMA DE PAGOS FINTECH (AUDIENCIA MIXTA)", fx, fy, w, h)
    
    # 1. Cabecera Editorial Estratégica (CEO / Dirección)
    scene.add_text(fx + 60, fy + 35, "PLATAFORMA TRANSACCIONAL DE PAGOS & CONCILIACIÓN FINTECH", font_size=32, font_family=2, color=PALETTE["INK"], frame_id=fid)
    scene.add_text(fx + 60, fy + 78, "arquitectura distribuida de alta disponibilidad: flujo transaccional en tiempo real, persistencia inmutable y conciliacion asincrona", font_size=15, font_family=2, color=PALETTE["PAIN_RED"], frame_id=fid)

    # Mini KPIs para Dirección & Producto
    scene.add_metric_pill(fx + w - 780, fy + 40, "DISPONIBILIDAD", "99.99% Multi-AZ", bg=PALETTE["INK"], frame_id=fid)
    scene.add_metric_pill(fx + w - 500, fy + 40, "LATENCIA P99", "< 180 ms", bg=PALETTE["INK"], frame_id=fid)
    scene.add_metric_pill(fx + w - 260, fy + 40, "IDEMPOTENCIA", "100% Garantizada", bg=PALETTE["INK"], frame_id=fid)

    # 2. Definición de Scopes Funcionales
    scopes_def = [
        {
            "id": "edge",
            "title": "1. INGRESS & EDGE GATEWAY",
            "w": 520.0,
            "nodes": [
                {"id": "web_mobile", "title": "Web & Mobile Clients", "sub": "Next.js & Flutter SDK", "role": "mobile", "tier": "component"},
                {"id": "edge_waf", "title": "Cloudflare Edge / WAF", "sub": "DDoS Shield & TLS 1.3", "role": "waf", "tier": "component"},
                {"id": "api_gw", "title": "Kong API Gateway", "sub": "Rate Limiting & Routing", "role": "gateway", "tier": "component"}
            ]
        },
        {
            "id": "security",
            "title": "2. SEGURIDAD & CONTROL",
            "w": 500.0,
            "nodes": [
                {"id": "auth_svc", "title": "Auth & Token Service", "sub": "OAuth2 / JWT & mTLS", "role": "auth", "tier": "component"},
                {"id": "idempotency_guard", "title": "Idempotency Guard", "sub": "X-Idempotency-Key Lock (TTL 24h)", "role": "key", "tier": "component"},
                {"id": "audit_log", "title": "Compliance & Audit Trail", "sub": "PCI-DSS v4.0 Signatures", "role": "security", "tier": "metadata"} # tier metadata: sin icono
            ]
        },
        {
            "id": "core",
            "title": "3. CORE TRANSACCIONAL",
            "w": 620.0,
            "is_hero_scope": True,
            "nodes": [
                {"id": "payment_core", "title": "Payment Orchestrator Core", "sub": "State Machine & Transaction Manager", "role": "orchestrator", "tier": "hero", "is_hero": True},
                {"id": "multi_acquirer", "title": "Smart Routing Engine", "sub": "Lowest Fee & Provider Health Check", "role": "service", "tier": "component"},
                {"id": "circuit_breaker", "title": "Circuit Breaker & Retries", "sub": "Exponential Backoff Policy", "role": "service", "tier": "metadata"} # metadata: sin icono
            ]
        },
        {
            "id": "async_events",
            "title": "4. ASINCRONÍA & EVENTOS",
            "w": 560.0,
            "nodes": [
                {"id": "event_queue", "title": "Kafka Event Pipeline", "sub": "Outbox Pattern & Event Sourcing", "role": "queue", "tier": "component"},
                {"id": "reconciler", "title": "Reconciliation Engine", "sub": "Automated Settlement vs Bank Ledger", "role": "reconciliation", "tier": "component"},
                {"id": "analytics_worker", "title": "Real-Time Analytics & ML", "sub": "Fraud Detection & Risk Scoring", "role": "analytics", "tier": "component"}
            ]
        },
        {
            "id": "persistence",
            "title": "5. PERSISTENCIA & ESTADO",
            "w": 520.0,
            "nodes": [
                {"id": "pg_ledger", "title": "PostgreSQL Immutable Ledger", "sub": "ACID Transactions (Multi-AZ)", "role": "postgres", "tier": "component"},
                {"id": "redis_cache", "title": "Redis Cluster (Cache & Lock)", "sub": "Distributed State & Session Cache", "role": "redis", "tier": "component"},
                {"id": "obj_storage", "title": "S3 Receipt & Invoice Store", "sub": "WORM Inmutable Storage", "role": "bucket", "tier": "component"}
            ]
        },
        {
            "id": "external",
            "title": "6. PROVEEDORES EXTERNOS",
            "w": 460.0,
            "nodes": [
                {"id": "acquirers", "title": "Payment Acquirers & Gateways", "sub": "Visa / Mastercard / Stripe / Pix", "role": "provider", "tier": "component"},
                {"id": "bank_networks", "title": "Banking Core & Webhooks", "sub": "ISO 20022 Direct Clearing", "role": "bank", "tier": "component"}
            ]
        }
    ]

    # 3. Renderizado de Contenedores de Scope y Tarjetas
    current_x = fx + 60.0
    start_y = fy + 140.0
    scope_h = 740.0
    node_coords = {}

    for s_idx, sc in enumerate(scopes_def):
        sw = sc["w"]
        stitle = sc["title"]
        snodes = sc["nodes"]
        is_hero_scope = sc.get("is_hero_scope", False)
        
        # Scope Container
        bg_scope = PALETTE["PASTEL_GREEN"] if is_hero_scope else "#FFFFFF"
        stroke_scope = PALETTE["INK"] if is_hero_scope else PALETTE["CARD_BORDER"]
        scene.add_scope_container(current_x, start_y, sw, scope_h, label=stitle,
                                  stroke=stroke_scope, bg=bg_scope, frame_id=fid)

        # Nodos dentro del scope
        card_w = sw - 50.0
        for n_idx, nd in enumerate(snodes):
            nid = nd["id"]
            ntitle = nd["title"]
            nsub = nd["sub"]
            nrole = nd.get("role", "service")
            ntier = nd.get("tier", "component")
            is_hero_node = nd.get("is_hero", False)
            
            ny = start_y + 70.0 + n_idx * 160.0
            card_h = 115.0
            
            # Resolver Icono Semántico
            icon_name = resolve_node_icon(ntitle, role=nrole, sublabel=nsub, tier=ntier)
            
            # Estilos según Jerarquía
            if is_hero_node:
                card_bg = PALETTE["INK"]
                card_stroke = PALETTE["INK"]
                text_col = "#FFFFFF"
            else:
                card_bg = "#FFFFFF"
                card_stroke = PALETTE["INK"]
                text_col = PALETTE["INK"]
                
            if icon_name:
                container, _ = scene.add_card_with_icon(
                    current_x + 25.0, ny, card_w, card_h,
                    ntitle, sublabel=nsub, icon=icon_name,
                    bg=card_bg, stroke=card_stroke, text_color=text_col,
                    frame_id=fid
                )
            else:
                # Nodo sin icono (Metadata o política secundaria)
                container, _ = scene.add_dual_card(
                    current_x + 25.0, ny, card_w, card_h,
                    ntitle, sublabel=nsub,
                    bg=card_bg, stroke=card_stroke, text_color=text_col,
                    frame_id=fid
                )
                
            node_coords[nid] = (container["x"], container["y"], container["width"], container["height"])

        current_x += sw + 50.0

    # 4. Conexiones Semánticas y Enrutamiento Ortogonal
    connections = [
        ("web_mobile", "edge_waf", "HTTPS / TLS", False),
        ("edge_waf", "api_gw", "WAF Filtered", False),
        ("api_gw", "auth_svc", "Validate JWT", False),
        ("auth_svc", "idempotency_guard", "Check Key", False),
        ("idempotency_guard", "payment_core", "Lock Acquired", False),
        ("payment_core", "multi_acquirer", "Smart Route", False),
        ("multi_acquirer", "acquirers", "Authorize Charge", False),
        ("payment_core", "pg_ledger", "ACID Write", False),
        ("payment_core", "event_queue", "Publish Event", False),
        ("event_queue", "reconciler", "Settlement Batch", False),
        ("event_queue", "analytics_worker", "Fraud Telemetry", False),
        ("reconciler", "bank_networks", "Daily Audit Polling", True),
        ("payment_core", "redis_cache", "Read Cache", True)
    ]

    for from_id, to_id, label_txt, is_dashed in connections:
        if from_id in node_coords and to_id in node_coords:
            fx_n, fy_n, fw_n, fh_n = node_coords[from_id]
            tx_n, ty_n, tw_n, th_n = node_coords[to_id]
            
            if tx_n >= fx_n + fw_n:
                scene.add_arrow(
                    fx_n + fw_n, fy_n + fh_n * 0.5,
                    tx_n, ty_n + th_n * 0.5,
                    stroke=PALETTE["INK"], stroke_w=1.5,
                    dashed=is_dashed, label=label_txt,
                    orthogonal=True, frame_id=fid
                )
            elif tx_n < fx_n:
                scene.add_arrow(
                    fx_n, fy_n + 25.0,
                    tx_n + tw_n, ty_n + 25.0,
                    stroke=PALETTE["MUTED"], stroke_w=1.2,
                    dashed=is_dashed, label=label_txt,
                    orthogonal=True, frame_id=fid
                )

    # 5. Banner Inferior Editorial de Gobernanza y Conciliación
    scene.add_banner(
        fx + 60, fy + 920, w - 120, 60,
        "garantias de arquitectura: idempotencia distribuida (redis ttl), libro contable inmutable de doble partida (postgresql) y conciliacion automatica diaria de liquidaciones bancarias.",
        bg=PALETTE["BANNER_PINK"], text_color=PALETTE["INK"], font_size=13, frame_id=fid
    )

    scene.auto_fit_frame(fid, padding=50.0)
    
    out_path = os.path.join(OUT_DIR, "plataforma_pagos_fintech_mixta.excalidraw")
    scene.save(out_path)
    print(f"[+] Archivo Excalidraw Fintech guardado en: {out_path}")
    
    _, report = validate_scene(out_path)
    print("\n" + report.summary())
    return out_path, report


if __name__ == "__main__":
    build_fintech_autonomous_architecture()
