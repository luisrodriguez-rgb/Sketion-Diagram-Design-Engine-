"""
Script para generar el diagrama de arquitectura para Inversionistas usando Sketion Engine (16:9 Presentation Preset)
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

    title = "SaaS Platform: Arquitectura y Ventajas Competitivas"

    # 1. Definición de 3 Pilares Estratégicos para Inversionistas
    scopes = [
        {
            "id": "scope_enterprise",
            "label": "1. CAPA EMPRESARIAL (ENTERPRISE READINESS)",
            "rel_x": 40,
            "rel_y": 90,
            "w": 380,
            "h": 580
        },
        {
            "id": "scope_scale",
            "label": "2. NÚCLEO ESCALABLE (MARGINS & HIGH SLA)",
            "rel_x": 450,
            "rel_y": 90,
            "w": 400,
            "h": 580
        },
        {
            "id": "scope_monetization",
            "label": "3. MOTOR DE MONETIZACIÓN Y DATOS",
            "rel_x": 880,
            "rel_y": 90,
            "w": 380,
            "h": 580
        }
    ]

    # 2. Nodos enfocados en Métricas de Negocio, Seguridad y Retención
    nodes = [
        # Pilar 1: Enterprise
        {
            "id": "node_sso",
            "label": "Seguridad Corporativa & SSO",
            "sublabel": "SAML 2.0 / Okta / Azure AD",
            "metadata": "Venta Enterprise",
            "rel_x": 65,
            "rel_y": 160
        },
        {
            "id": "node_isolation",
            "label": "Aislamiento Multi-Tenant",
            "sublabel": "Compliance SOC2 y GDPR Nativo",
            "metadata": "Data Privacy",
            "rel_x": 65,
            "rel_y": 360
        },
        # Pilar 2: Core
        {
            "id": "node_platform",
            "label": "Motor de Plataforma Cloud",
            "sublabel": "99.99% Uptime · Coste Marginal ~0",
            "metadata": "Infraestructura",
            "is_hero": True,  # Nodo focal de acento
            "rel_x": 475,
            "rel_y": 160
        },
        {
            "id": "node_automation",
            "label": "Procesamiento Asíncrono",
            "sublabel": "Alta Concurrencia sin Latencia",
            "metadata": "Event-Driven",
            "rel_x": 475,
            "rel_y": 360
        },
        # Pilar 3: Monetization
        {
            "id": "node_billing",
            "label": "Facturación y Expansión MRR",
            "sublabel": "Per-Seat + Cobro por Consumo",
            "metadata": "Stripe B2B",
            "rel_x": 905,
            "rel_y": 160
        },
        {
            "id": "node_data_moat",
            "label": "Base de Datos & Data Moat",
            "sublabel": "Alta Retención (NRR > 115%)",
            "metadata": "Defensibilidad",
            "rel_x": 905,
            "rel_y": 360
        }
    ]

    # 3. Conexiones estratégicas
    edges = [
        { "from": "node_sso", "to": "node_platform", "label": "Acceso Corporativo" },
        { "from": "node_isolation", "to": "node_platform", "label": "Garantía SOC2" },
        { "from": "node_platform", "to": "node_automation", "label": "Eficiencia Operativa" },
        { "from": "node_platform", "to": "node_billing", "label": "Upselling Automático" },
        { "from": "node_automation", "to": "node_data_moat", "label": "Activos y Métricas" },
        { "from": "node_billing", "to": "node_data_moat", "label": "Retención LTV" }
    ]

    # 4. Render en formato Presentación
    engine_red(scene, title, nodes, edges, scopes=scopes, palette=DEFAULT_PALETTE, w=1300, h=720)

    # 5. Validación y Quality Score
    sem_diagram = SemanticDiagram(
        title=title,
        semantic_type="architecture",
        detail_level=DetailLevel.BALANCED,
        output_preset=OutputPreset.PRESENTATION,
        engine="red",
        scopes=[Scope(id=s["id"], label=s["label"]) for s in scopes],
        nodes=[SemanticNode(id=n["id"], label=n["label"], sublabel=n.get("sublabel"), is_hero=n.get("is_hero", False)) for n in nodes],
        edges=[SemanticEdge(from_node=e["from"], to_node=e["to"], label=e.get("label")) for e in edges]
    )

    scene_data, report = validate_scene(scene.to_dict(), diagram=sem_diagram, auto_repair=True)
    print(report.summary())

    output_path = os.path.join(workspace_dir, "arquitectura_saas_pitch_inversionistas.excalidraw")
    scene.save(output_path)
    print(f"\nArchivo guardado con éxito en: {output_path}")

if __name__ == "__main__":
    generate()
