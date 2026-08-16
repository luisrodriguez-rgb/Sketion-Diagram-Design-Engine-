"""
Sketion Master Generator — Centro de Distribución Omnicanal y Cadena de Suministro
Genera una escena de alta densidad editorial con 3 Frames coordinados:
- Frame 1: Arquitectura de Sistemas y Flujo Físico-Digital Omnicanal (6 Scopes)
- Frame 2: Máquina de Estados de Fulfillment y Logística Inversa (RMA)
- Frame 3: Matriz Operacional de 14 Excepciones y Dashboard de 12 KPIs Clave
"""

import os
import sys

workspace_dir = "/Users/leonfeliperodriguez/Desktop/Trabajos/Sketion SKILL"
sys.path.insert(0, workspace_dir)

from render.excalidraw_builder import ExcalidrawScene, place_reset, place, compute_card_dimensions
from engines.recipes import engine_red, engine_flujo, engine_matriz, engine_dashboard, DEFAULT_PALETTE
from semantic.models import SemanticDiagram, SemanticNode, SemanticEdge, Scope, DetailLevel, OutputPreset, SemanticFlowStep, SemanticMetric
from validation.validator import validate_scene

OUT_DIR = os.path.join(workspace_dir, "PRUEBAS_V3")
os.makedirs(OUT_DIR, exist_ok=True)


def build_distribution_center_scene():
    place_reset(max_row_w=5800, gap=180)
    scene = ExcalidrawScene(roughness=0, bg_color="#ffffff")

    # =========================================================================
    # FRAME 1: ARQUITECTURA DE SISTEMAS Y FLUJO FÍSICO-DIGITAL (6 SCOPES)
    # =========================================================================
    title_f1 = "Operación y Sistemas de Centro de Distribución Omnicanal"

    scopes_f1 = [
        {"id": "sc_supply", "label": "1. PROVEEDORES & INBOUND", "rel_x": 30, "rel_y": 90, "w": 340, "h": 720},
        {"id": "sc_qa_putaway", "label": "2. RECEPCIÓN, QA & PUTAWAY", "rel_x": 420, "rel_y": 90, "w": 380, "h": 720},
        {"id": "sc_storage_wms", "label": "3. INVENTARIO & WMS (CORE)", "rel_x": 850, "rel_y": 90, "w": 420, "h": 720},
        {"id": "sc_oms_routing", "label": "4. ORQUESTACIÓN OMS & ROUTING", "rel_x": 1320, "rel_y": 90, "w": 420, "h": 720},
        {"id": "sc_picking_pack", "label": "5. PICKING, PACKING & TMS", "rel_x": 1790, "rel_y": 90, "w": 400, "h": 720},
        {"id": "sc_channels_lastmile", "label": "6. CANALES & LAST-MILE", "rel_x": 2240, "rel_y": 90, "w": 340, "h": 720}
    ]

    nodes_f1 = [
        # Sc 1: Supply
        {"id": "supp_national", "label": "Proveedores Nacionales", "sublabel": "Entregas Locales / Cross-Dock", "metadata": "Inbound Trucks", "scope_id": "sc_supply", "rel_x": 55, "rel_y": 150},
        {"id": "supp_intl", "label": "Proveedores Internacionales", "sublabel": "Contenedores / Aduanas", "metadata": "Customs Port", "scope_id": "sc_supply", "rel_x": 55, "rel_y": 330},
        {"id": "inbound_dock", "label": "Muelle de Descarga", "sublabel": "Conteo de Pallets & ASN", "metadata": "Dock Staging", "scope_id": "sc_supply", "rel_x": 55, "rel_y": 510},

        # Sc 2: QA & Putaway
        {"id": "qa_inspection", "label": "Control de Calidad (QA)", "sublabel": "Muestreo, Lote & Fecha", "metadata": "Punto de Control", "scope_id": "sc_qa_putaway", "rel_x": 450, "rel_y": 150},
        {"id": "quarantine_zone", "label": "Zona de Cuarentena", "sublabel": "Productos Dañados / Rechazo", "metadata": "Aislamiento", "scope_id": "sc_qa_putaway", "rel_x": 450, "rel_y": 330},
        {"id": "putaway_forklift", "label": "Operación de Putaway", "sublabel": "Ubicación por Rotación ABC", "metadata": "WMS Directed", "scope_id": "sc_qa_putaway", "rel_x": 450, "rel_y": 510},

        # Sc 3: Inventory WMS (HERO)
        {"id": "wms_engine", "label": "WMS Core Inventory Engine", "sublabel": "Stock Físico / Lotes / Pasillos", "metadata": "Core Hero", "is_hero": True, "scope_id": "sc_storage_wms", "rel_x": 885, "rel_y": 150},
        {"id": "stock_allocation", "label": "Motor de Disponibilidad", "sublabel": "Stock Disponible = Total - Reservado", "metadata": "Zero-Negative Lock", "scope_id": "sc_storage_wms", "rel_x": 885, "rel_y": 330},
        {"id": "warehouse_zones", "label": "Zonas de Almacén", "sublabel": "Temperatura, Alta Rotación, Bulk", "metadata": "Locations Map", "scope_id": "sc_storage_wms", "rel_x": 885, "rel_y": 510},

        # Sc 4: OMS Routing
        {"id": "oms_core", "label": "OMS (Order Management)", "sublabel": "Consolidación de 4 Canales", "metadata": "Focal Engine", "scope_id": "sc_oms_routing", "rel_x": 1355, "rel_y": 150},
        {"id": "sourcing_rules", "label": "Reglas de Sourcing & Split", "sublabel": "Distancia, SLA & Prioridad", "metadata": "Decision Engine", "scope_id": "sc_oms_routing", "rel_x": 1355, "rel_y": 330},
        {"id": "order_priorities", "label": "Colas de Priorización", "sublabel": "Same-Day > Express > Tiendas", "metadata": "Priority Queue", "scope_id": "sc_oms_routing", "rel_x": 1355, "rel_y": 510},

        # Sc 5: Picking & Packing
        {"id": "picking_waves", "label": "Ola de Picking (Pickers)", "sublabel": "Ruta Óptima & Lector RFID", "metadata": "Pick-to-Light", "scope_id": "sc_picking_pack", "rel_x": 1825, "rel_y": 150},
        {"id": "packing_audit", "label": "Estación de Packing & Peso", "sublabel": "Verificación SKU & Caja", "metadata": "Scale Check", "scope_id": "sc_picking_pack", "rel_x": 1825, "rel_y": 330},
        {"id": "tms_dispatch", "label": "TMS & Asignación de Carrier", "sublabel": "Etiquetado de Envío & Manifiesto", "metadata": "Carrier API", "scope_id": "sc_picking_pack", "rel_x": 1825, "rel_y": 510},

        # Sc 6: Channels & Delivery
        {"id": "omnichannel_sales", "label": "4 Canales de Venta", "sublabel": "E-com, App, Marketplaces, Retail", "metadata": "Order Source", "scope_id": "sc_channels_lastmile", "rel_x": 2275, "rel_y": 150},
        {"id": "lastmile_carriers", "label": "Transportistas & Flota", "sublabel": "Rutas Urbanas & Reposición B2B", "metadata": "Tracking 24/7", "scope_id": "sc_channels_lastmile", "rel_x": 2275, "rel_y": 330},
        {"id": "customer_retail", "label": "Clientes & Tiendas Físicas", "sublabel": "Entrega Final & Firma", "metadata": "Proof of Delivery", "scope_id": "sc_channels_lastmile", "rel_x": 2275, "rel_y": 510}
    ]

    edges_f1 = [
        {"from": "supp_national", "to": "inbound_dock", "label": "Descarga"},
        {"from": "supp_intl", "to": "inbound_dock", "label": "Contenedor"},
        {"from": "inbound_dock", "to": "qa_inspection", "label": "Muestreo"},
        {"from": "qa_inspection", "to": "quarantine_zone", "label": "Rechazado"},
        {"from": "qa_inspection", "to": "putaway_forklift", "label": "Aprobado"},
        {"from": "putaway_forklift", "to": "warehouse_zones", "label": "Ubicación"},
        {"from": "warehouse_zones", "to": "wms_engine", "label": "Alta Stock"},
        {"from": "omnichannel_sales", "to": "oms_core", "label": "Nuevo Pedido"},
        {"from": "oms_core", "to": "sourcing_rules", "label": "Calcular SLA"},
        {"from": "sourcing_rules", "to": "stock_allocation", "label": "Reserva Stock"},
        {"from": "stock_allocation", "to": "wms_engine", "label": "Hold Atómico"},
        {"from": "sourcing_rules", "to": "order_priorities", "label": "Encolar"},
        {"from": "order_priorities", "to": "picking_waves", "label": "Lanzar Ola"},
        {"from": "picking_waves", "to": "packing_audit", "label": "Validar SKU"},
        {"from": "packing_audit", "to": "tms_dispatch", "label": "Etiquetar"},
        {"from": "tms_dispatch", "to": "lastmile_carriers", "label": "Despacho"},
        {"from": "lastmile_carriers", "to": "customer_retail", "label": "Entrega POD"}
    ]

    engine_red(scene, title_f1, nodes_f1, edges_f1, scopes=scopes_f1, palette=DEFAULT_PALETTE, w=2700, h=880)

    # =========================================================================
    # FRAME 2: CICLO DE VIDA DE FULFILLMENT Y LOGÍSTICA INVERSA (RMA)
    # =========================================================================
    title_f2 = "Ciclo de Vida del Pedido y Proceso de Devolución (RMA)"
    steps_f2 = [
        {"step_num": "01", "label": "Created & Validated\nRecepción en OMS", "is_hero": False, "edge_label": "Validar"},
        {"step_num": "02", "label": "Allocated\nReserva en WMS", "is_hero": False, "edge_label": "Ola"},
        {"step_num": "03", "label": "Picking & Packed\nVerificación de Peso", "is_hero": True, "edge_label": "Etiquetar"},
        {"step_num": "04", "label": "Dispatched & In Transit\nTransporte Carrier", "is_hero": False, "edge_label": "Entregar"},
        {"step_num": "05", "label": "Delivered\nPrueba de Entrega POD", "is_hero": False, "edge_label": "Devolución RMA"},
        {"step_num": "06", "label": "Inspección RMA & Grading\nReintegro / Scrap", "is_hero": False}
    ]
    engine_flujo(scene, title_f2, steps_f2, palette=DEFAULT_PALETTE, wave=False, w=1800, h=400)

    # =========================================================================
    # FRAME 3: MATRIZ OPERACIONAL DE 14 EXCEPCIONES Y RESILIENCIA
    # =========================================================================
    title_f3 = "Matriz de Manejo de Excepciones y Resiliencia Operativa"
    headers_f3 = ["Escenario de Excepción", "Punto de Detección", "Estado Afectado", "Protocolo de Mitigación y Consistencia"]
    rows_f3 = [
        {"Escenario de Excepción": "1. Compra concurrente última unidad", "Punto de Detección": "Motor Stock Allocation", "Estado Afectado": "1 ALLOCATED / 1 BACKORDER", "Protocolo de Mitigación y Consistencia": "Reserva atómica con lock transaccional. Nunca stock negativo; segundo pedido ofrece split/backorder."},
        {"Escenario de Excepción": "2. Discrepancia física en picking", "Punto de Detección": "Operario Picker (RFID)", "Estado Afectado": "ON_HOLD / INCIDENCIA", "Protocolo de Mitigación y Consistencia": "El sistema reasigna la línea a otra ubicación/pasillo y genera tarea de conteo cíclico urgente."},
        {"Escenario de Excepción": "3. Proveedor entrega cantidad errónea", "Punto de Detección": "Muelle de Recepción (ASN)", "Estado Afectado": "PARTIAL_RECEIVED", "Protocolo de Mitigación y Consistencia": "Recepción ciega; registro de discrepancia en ERP y entrada a inventario solo de lo verificado físicamente."},
        {"Escenario de Excepción": "4. Paquete excede peso de carrier", "Punto de Detección": "Estación de Packing (Báscula)", "Estado Afectado": "PACK_REJECTED", "Protocolo de Mitigación y Consistencia": "Báscula bloquea etiquetado; división automática en 2 bultos con sub-guías vinculadas."},
        {"Escenario de Excepción": "5. Transportista rechaza envío", "Punto de Detección": "Muelle de Despacho", "Estado Afectado": "DISPATCH_HOLD", "Protocolo de Mitigación y Consistencia": "TMS conmuta automáticamente a transportista alternativo homologado según SLA."},
        {"Escenario de Excepción": "6. Reposición urgente tienda física", "Punto de Detección": "OMS B2B Trigger", "Estado Afectado": "PRIORITY_WAVE", "Protocolo de Mitigación y Consistencia": "Salto de cola de picking; consolidación en pallet dedicado y despacho en ventana express."},
        {"Escenario de Excepción": "7. Pedido dividido en 3 paquetes", "Punto de Detección": "Sourcing Split Engine", "Estado Afectado": "SPLIT_ALLOCATED", "Protocolo de Mitigación y Consistencia": "Cada paquete recibe sub-guía y tracking independiente; el cliente ve envío consolidado."},
        {"Escenario de Excepción": "8. Cancelación durante el picking", "Punto de Detección": "OMS Event Stream", "Estado Afectado": "CANCELLED", "Protocolo de Mitigación y Consistencia": "Alerta inmediata en terminal del picker; el producto se desvía a la estación de retorno (*Re-bin*)."},
        {"Escenario de Excepción": "9. Producto devuelto dañado (RMA)", "Punto de Detección": "Estación de Grading RMA", "Estado Afectado": "DAMAGED / SCRAP", "Protocolo de Mitigación y Consistencia": "No ingresa a stock disponible; se envía a cuarentena/destrucción con reclamo al seguro."},
        {"Escenario de Excepción": "10. Cliente afirma no recibir paquete", "Punto de Detección": "Customer Service", "Estado Afectado": "LOST_INVESTIGATION", "Protocolo de Mitigación y Consistencia": "Auditoría de coordenadas GPS de entrega del transportista + reenvío express o reembolso."},
        {"Escenario de Excepción": "11. Sistema externo/Marketplace caído", "Punto de Detección": "API Gateway / Circuit Breaker", "Estado Afectado": "OFFLINE_BUFFER", "Protocolo de Mitigación y Consistencia": "Encolamiento de pedidos en buffer Kafka; reintento automático al restablecer servicio."},
        {"Escenario de Excepción": "12. Actualización stock duplicada", "Punto de Detección": "WMS Event Consumer", "Estado Afectado": "IGNORED_DUPLICATE", "Protocolo de Mitigación y Consistencia": "Verificación de número de secuencia y versionado optimista (*Version ID*) en cada SKU."},
        {"Escenario de Excepción": "13. Mismo SKU en múltiples zonas", "Punto de Detección": "WMS Allocation Engine", "Estado Afectado": "DIRECTED_PICK", "Protocolo de Mitigación y Consistencia": "Algoritmo FIFO/FEFO prioriza vaciar ubicaciones secundarias antes de tocar stock bulk."},
        {"Escenario de Excepción": "14. Fechas prometidas distintas", "Punto de Detección": "OMS Order Splitter", "Estado Afectado": "PARTIAL_SCHEDULED", "Protocolo de Mitigación y Consistencia": "Despacho por oleadas según la fecha límite de cada línea si el cliente autorizó envíos parciales."}
    ]
    engine_matriz(scene, title_f3, headers_f3, rows_f3, palette=DEFAULT_PALETTE, w=2200, h=920)

    # =========================================================================
    # FRAME 4: DASHBOARD DE 12 KPIS CLAVE DEL CENTRO DE DISTRIBUCIÓN
    # =========================================================================
    title_f4 = "Dashboard de 12 Métricas y KPIs de Operación Logística"
    metrics_f4 = [
        {"number": "99.4%", "label": "Order Fulfillment Rate"},
        {"number": "99.8%", "label": "Picking Accuracy"},
        {"number": "99.9%", "label": "Inventory Accuracy"},
        {"number": "2.4h", "label": "Order Cycle Time"},
        {"number": "98.7%", "label": "On-Time Shipment Rate"},
        {"number": "97.2%", "label": "On-Time Delivery Rate"},
        {"number": "3.1%", "label": "Return Rate (RMA)"},
        {"number": "0.4%", "label": "Cancellation Rate"},
        {"number": "88.5%", "label": "Warehouse Utilization"},
        {"number": "42s", "label": "Average Picking Time"},
        {"number": "142", "label": "Backlog Orders"},
        {"number": "0.0%", "label": "Stockout Rate"}
    ]
    engine_dashboard(scene, title_f4, metrics_f4, palette=DEFAULT_PALETTE, w=2200, h=480)

    # =========================================================================
    # VALIDACIÓN COMPLETA
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
    
    out_file = os.path.join(OUT_DIR, "centro_distribucion_omnicanal.excalidraw")
    scene.save(out_file)
    
    return report, out_file


if __name__ == "__main__":
    report, filepath = build_distribution_center_scene()
    print("==================================================")
    print("REPORTE DE AUDITORÍA Y CALIDAD DE SKETION")
    print("==================================================")
    print(report.summary())
    print(f"\nArchivo .excalidraw exportado en: {filepath}")
