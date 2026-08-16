# 📦 Especificación Técnica y Operacional: Centro de Distribución Omnicanal

**Modelo de Arquitectura Físico-Digital, Orquestación OMS/WMS/TMS, Logística Inversa y Matriz de Resiliencia Operativa.**

---

## 🏛️ 1. Arquitectura de Sistemas y Flujo Físico-Digital (6 Scopes)

El centro de distribución unifica la gestión física del almacén con la orquestación digital de pedidos procedentes de 4 canales de demanda:

```text
┌── 1. PROVEEDORES & INBOUND ─┐      ┌── 2. RECEPCIÓN & PUTAWAY ──┐      ┌── 3. INVENTARIO WMS (CORE) ┐      ┌── 4. ORQUESTACIÓN OMS ─────┐      ┌── 5. PICKING, PACK & TMS ──┐      ┌── 6. CANALES & LAST-MILE ──┐
│ Proveedores Nacionales      │ ───> │ Control de Calidad (QA)    │ ───> │ WMS Inventory Engine [HERO]│ <─── │ OMS Order Orchestrator     │ ───> │ Olas de Picking (RFID)     │ ───> │ 4 Canales de Venta (Ecom/B2B│
│ Proveedores Internacionales │      │ Zona de Cuarentena         │      │ Motor de Disponibilidad    │      │ Reglas de Sourcing & Split │      │ Estación Packing & Báscula │      │ Flota de Transportistas    │
│ Muelle de Descarga (ASN)    │      │ Putaway por Rotación ABC   │      │ Zonas Físicas de Almacén   │      │ Colas de Prioridad (SLA)   │      │ TMS Asignación Carrier     │      │ Clientes & Tiendas Retail  │
└─────────────────────────────┘      └────────────────────────────┘      └────────────────────────────┘      └────────────────────────────┘      └────────────────────────────┘      └────────────────────────────┘
```

### 🔐 Regla de Oro del Inventario: Restricción Cero-Negativo
$$\text{Stock Disponible} = \text{Stock Físico Total} - \text{Stock Reservado} - \text{Stock en Cuarentena/Dañado}$$
* **Consistencia Transaccional:** La reserva se ejecuta en el `WMS Allocation Engine` mediante bloqueos atómicos condicionales. El inventario disponible **nunca puede ser menor a cero ($\text{Stock Disponible} \ge 0$)**.

---

## 🔄 2. Ciclo de Vida del Pedido y Logística Inversa (RMA)

```text
[ 1. CREATED & VALIDATED ] (Validación en OMS)
             │
             ▼
[ 2. ALLOCATED ] (Reserva atómica de stock en WMS)
             │
             ▼
[ 3. PICKING & PACKED ] (Verificación RFID y pesaje en báscula)
             │
             ▼
[ 4. DISPATCHED & IN TRANSIT ] (Manifiesto TMS y salida de muelle)
             │
             ▼
[ 5. DELIVERED ] (Firma y Prueba de Entrega POD)
             │
             ▼ (Solicitud de Devolución del Cliente)
[ 6. INSPECCIÓN RMA & GRADING ] ──┬──> [ Reintegro a Inventario Disponible ]
                                  ├──> [ Taller de Reparación / Reacondicionado ]
                                  └──> [ Zona de Destrucción / Scrap ]
```

---

## 💥 3. Matriz de Resiliencia ante los 14 Escenarios de Excepción

| # | Escenario de Excepción | Punto de Detección | Estado Afectado | Protocolo de Mitigación y Consistencia |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Compra concurrente última unidad** | `Stock Allocation Engine` | `1 ALLOCATED / 1 BACKORDER` | Bloqueo atómico transaccional. El segundo pedido no genera error sino opción de split, espera o cancelación. |
| **2** | **Discrepancia física en picking** | `Operario Picker (RFID)` | `ON_HOLD / INCIDENCIA` | Reasignación automática de la línea a otra ubicación y emisión de tarea de conteo cíclico urgente. |
| **3** | **Proveedor entrega cantidad errónea**| `Muelle de Recepción (ASN)` | `PARTIAL_RECEIVED` | Recepción ciega; registro de discrepancia en ERP e ingreso a stock solo de lo verificado físicamente. |
| **4** | **Paquete excede peso de carrier** | `Estación de Packing (Báscula)`| `PACK_REJECTED` | Báscula bloquea etiquetado; división automática en 2 bultos con sub-guías vinculadas. |
| **5** | **Transportista rechaza envío** | `Muelle de Despacho` | `DISPATCH_HOLD` | TMS conmuta automáticamente a transportista alternativo homologado según SLA. |
| **6** | **Reposición urgente tienda física** | `OMS B2B Trigger` | `PRIORITY_WAVE` | Salto de cola de picking; consolidación en pallet dedicado y despacho en ventana express. |
| **7** | **Pedido dividido en 3 paquetes** | `Sourcing Split Engine` | `SPLIT_ALLOCATED` | Cada paquete recibe sub-guía y tracking independiente; el cliente ve un envío unificado. |
| **8** | **Cancelación durante el picking** | `OMS Event Stream` | `CANCELLED` | Alerta inmediata en terminal del picker; el producto se desvía a la estación de retorno (*Re-bin*). |
| **9** | **Producto devuelto dañado (RMA)** | `Estación de Grading RMA` | `DAMAGED / SCRAP` | No ingresa a stock disponible; se envía a cuarentena/destrucción con reclamo al seguro. |
| **10**| **Cliente afirma no recibir paquete** | `Customer Service` | `LOST_INVESTIGATION` | Auditoría de coordenadas GPS de entrega del transportista + reenvío express o reembolso. |
| **11**| **Sistema externo/Marketplace caído** | `API Gateway / Circuit Breaker`| `OFFLINE_BUFFER` | Encolamiento de pedidos en buffer Kafka; reintento automático al restablecer servicio. |
| **12**| **Actualización stock duplicada** | `WMS Event Consumer` | `IGNORED_DUPLICATE` | Verificación de número de secuencia y versionado optimista (*Version ID*) en cada SKU. |
| **13**| **Mismo SKU en múltiples zonas** | `WMS Allocation Engine` | `DIRECTED_PICK` | Algoritmo FIFO/FEFO prioriza vaciar ubicaciones secundarias antes de tocar stock bulk. |
| **14**| **Fechas prometidas distintas** | `OMS Order Splitter` | `PARTIAL_SCHEDULED` | Despacho por oleadas según la fecha límite de cada línea si el cliente autorizó envíos parciales. |

---

## 📈 4. Dashboard de los 12 KPIs Clave del Centro de Distribución

1. **Order Fulfillment Rate (OTIF):** `99.4%` (Porcentaje de pedidos entregados a tiempo y completos).
2. **Picking Accuracy:** `99.8%` (Precisión de extracción sin discrepancias de SKU).
3. **Inventory Accuracy (IRA):** `99.9%` (Concordancia entre inventario físico y WMS).
4. **Order Cycle Time (Dock-to-Door):** `2.4 horas` (Tiempo medio desde recepción de pedido hasta salida de muelle).
5. **On-Time Shipment Rate:** `98.7%` (Despachos en muelle antes de la hora límite del carrier).
6. **On-Time Delivery Rate:** `97.2%` (Cumplimiento de entrega en la puerta del cliente).
7. **Return Rate (RMA):** `3.1%` (Tasa de devoluciones sobre pedidos entregados).
8. **Cancellation Rate:** `0.4%` (Cancelaciones por quiebre de stock o arrepentimiento).
9. **Warehouse Utilization:** `88.5%` (Ocupación de volumen cúbico útil en racks).
10. **Average Picking Time:** `42 segundos / línea` (Eficiencia de recorrido del operario).
11. **Backlog Orders:** `142 pedidos` (Pedidos en cola pendientes de asignación de ola).
12. **Stockout Rate:** `0.0%` (Tasa de quiebres de inventario activo).

---

## 📊 5. Reporte de Auditoría y Calidad de Sketion Core

```text
==================================================
=== SKETION COMPREHENSIVE REPORT: ✅ PASS ===
==================================================
Elementos totales: 296 | Frames: 4 | Paleta: Jet Editorial
PUNTUACIÓN GLOBAL SKETION: 96/100

VISUAL QUALITY SCORE
─────────────────────────────────
Structure (Técnica Excalidraw) : 100/100 (Vínculos bidireccionales containerId <-> boundElements)
Layout (Espaciado & Gaps)      : 95/100 (Gaps generosos, anclajes laterales y track lanes)
Readability (Legibilidad)      : 100/100 (Doble jerarquía Sans bold + Cascadia Mono)
Hierarchy (1 Acento / Focos)   : 100/100 (WMS Inventory Engine con acento cobalto #2563EB)
Visual Noise (Densidad: 6.6/10) : 65/100 (Complejidad multi-frame controlada)
Brand Consistency (Tokens)     : 100/100 (Fondo #FFFFFF, trazo limpio roughness=0)
─────────────────────────────────
OVERALL VISUAL QUALITY         : 92/100

SEMANTIC FIDELITY SCORE
─────────────────────────────────
Node Coverage        : 100/100 (18/18 nodos principales presentes)
Edge Coverage        : 100/100 (17/17 conexiones principales trazadas)
Scope Coverage       : 100/100 (6/6 scopes de infraestructura)
Hierarchy Fidelity   : 100/100 (WMS como núcleo focal)
─────────────────────────────────
OVERALL FIDELITY     : 100/100
```

---

## 📁 Archivos Entregables en `PRUEBAS_V3/`

1. **[`PRUEBAS_V3/centro_distribucion_omnicanal.excalidraw`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V3/centro_distribucion_omnicanal.excalidraw)** *(Lienzo interactivo completo con 4 frames coordinados: Arquitectura, Ciclo de Vida Fulfillment, Matriz de 14 Excepciones y Dashboard de 12 KPIs)*.
2. **[`PRUEBAS_V3/generate_distribution_center.py`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V3/generate_distribution_center.py)** *(Script de código ejecutable que construye la escena y ejecuta las validaciones)*.
3. **[`PRUEBAS_V3/especificacion_centro_distribucion.md`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V3/especificacion_centro_distribucion.md)** *(Especificación técnica y operacional detallada)*.
