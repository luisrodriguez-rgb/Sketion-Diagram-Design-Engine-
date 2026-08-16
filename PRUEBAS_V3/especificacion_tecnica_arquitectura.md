# 📑 Especificación Técnica: Plataforma SaaS B2B de Reservas para Restaurantes

**Diseño de Arquitectura de Sistemas, Ciclo de Vida, Concurrencia y Resiliencia ante Fallos Parciales.**

---

## 🏛️ 1. Arquitectura del Sistema (Distribución en 6 Capas / Scopes)

El sistema está organizado en una arquitectura de microservicios desacoplada y orientada a eventos (*Event-Driven Architecture*), garantizando aislamiento multi-tenant y disponibilidad en tiempo real:

```text
┌── 1. CANALES Y USUARIOS ──┐      ┌── 2. EDGE & SEGURIDAD ───┐      ┌── 3. SERVICIOS CORE ─────┐      ┌── 4. ASYNC STREAMING ────┐      ┌── 5. PERSISTENCIA & DATA ┐      ┌── 6. PROVEEDORES EXT. ───┐
│ Cliente Final (Web/App)   │ ───> │ Cloudflare WAF & Shield  │ ───> │ Reservation Service [HERO│ ───> │ Kafka Event Streaming    │ ───> │ PostgreSQL Multi-Tenant  │ ───> │ Stripe Payments (PCI)    │
│ Dashboard del Restaurante │      │ API Gateway & Router     │      │ Availability Service     │      │ Notification Worker      │      │ Redis Locks (Hold 120s)  │      │ WhatsApp / SMS (Twilio)  │
│ SuperAdmin Console        │      │ Auth & RBAC Service      │      │ Table & Floor Plan Serv. │      │ Analytics & Audit Worker │      │ AWS S3 / R2 Object Store │      │ Resend / SendGrid Email  │
└───────────────────────────┘      └──────────────────────────┘      └──────────────────────────┘      └──────────────────────────┘      └──────────────────────────┘      └──────────────────────────┘
```

### Límites de Responsabilidad Clave:
* **`Availability Service`:** Motor de lectura optimizado. No es dueño de los datos maestros de mesas ni de reservas; consulta horarios, aforos y bloqueos temporales en Redis y PostgreSQL para calcular slots libres en milisegundos.
* **`Reservation Service` (Nodo Héroe Focal):** Responsable único de la máquina de estados y de la consistencia transaccional. Coordina bloqueos con Redis y confirma mediante transacciones ACID en PostgreSQL.
* **Aislamiento Multi-Tenant:** Cada petición entrante inyecta el `tenant_id` (restaurante / sucursal) en el contexto de ejecución. Las consultas en PostgreSQL aplican *Row-Level Security (RLS)* estricto para evitar accesos cruzados.

---

## 🔄 2. Máquina de Estados de la Reserva y Control de Concurrencia

```text
[ REQUESTED ]
      │ (Verificar disponibilidad + Reglas)
      ▼
[ PENDING (Hold 120s) ] ──── (Tiempo expirado) ────> [ EXPIRED ]
      │ (Confirmar / Depósito Stripe)
      ▼
[ CONFIRMED ] ────────── (Cancelación cliente/staff) ───> [ CANCELLED ]
      │ (Llegada al local)
      ▼
[ SEATED ] ───────────── (No se presentó) ──────────────> [ NO_SHOW ]
      │ (Fin del servicio)
      ▼
[ COMPLETED ]
```

### 🛡️ Protección contra Doble Reserva Concurrente:
1. **Fase 1 (Bloqueo Temporal Rápido en Redis):**
   ```bash
   # Lock distribuido con tiempo de vida (TTL) de 120 segundos
   SET lock:mesa:14:2026-08-16T20:00 "cliente_A" NX EX 120
   ```
   - Si el comando retorna `OK`, el cliente A pasa al estado `PENDING` para rellenar datos o pagar depósito.
   - Si el cliente B intenta el mismo slot simultáneamente, Redis retorna `nil` y la UI le informa inmediatamente que la mesa está siendo retenida por otro usuario.
2. **Fase 2 (Confirmación Atómica en PostgreSQL):**
   ```sql
   UPDATE tables_schedule 
   SET status = 'CONFIRMED', reservation_id = $1 
   WHERE table_id = 14 AND time_slot = '2026-08-16 20:00:00' AND status = 'PENDING';
   ```

---

## 💥 3. Matriz de Resiliencia ante los 10 Escenarios de Fallo Parcial

| # | Escenario de Fallo | Componente Detector | Estado de la Reserva | Mecanismo de Resiliencia y Consistencia |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Proveedor de WhatsApp caído** | `Notification Worker` | `CONFIRMED` *(Preservada)* | No se hace rollback. El evento pasa a *Dead Letter Queue (DLQ)* con reintentos exponenciales y fallback automático a Email. |
| **2** | **Pasarela de pagos lenta** | `Payment Service` | `PENDING` *(Con Lease)* | Uso de *Idempotency Keys* en Stripe + conciliación asíncrona mediante webhooks entrantes (`payment_intent.succeeded`). |
| **3** | **Concurrencia en la misma mesa** | `Reservation Service` | `1 CONFIRMED / 1 REJECTED` | *Distributed Lock* en Redis (`SETNX` TTL 120s) + validación condicional atómica en base de datos (`WHERE status='free'`). |
| **4** | **Caída total de Redis** | `Availability Service` | `DEGRADADO A DB` | *Circuit Breaker* conmuta automáticamente a *PostgreSQL Advisory Locks* transaccionales directos. |
| **5** | **Consumer caído durante evento** | `Kafka Consumer Group` | `CONFIRMED` *(Preservada)* | El offset de Kafka solo se commitea tras procesar el mensaje con éxito. Rebalanceo automático a otro worker. |
| **6** | **Evento duplicado (*At-least-once*)** | `Analytics & Notif Worker` | `SIN DUPLICADOS` | Consumidores idempotentes con verificación previa en tabla `processed_events(event_id)`. |
| **7** | **Alta latencia en BD Principal** | `API Gateway / Healthcheck`| `BUFFERED` | *Circuit Breaker* en Gateway; las consultas de disponibilidad y catálogo se desvían a *Read Replicas* de solo lectura. |
| **8** | **Cambio de horario con reservas futuras** | `Restaurant Service` | `CONFIRMED` *(Grandfathered)*| Las reservas ya confirmadas quedan protegidas; se alerta al gerente en el dashboard para reubicación asistida. |
| **9** | **Expiración durante el checkout** | `Redis Key Expiry Event` | `EXPIRED` | El lock expira a los 120s; la mesa se libera atómicamente y la UI notifica al usuario para seleccionar otro turno. |
| **10**| **Cancelación manual en estado pending** | `Staff Dashboard` | `CANCELLED` | Se cancela el `PaymentIntent` en Stripe y se borra inmediatamente el lock en Redis para liberar la mesa. |

---

## 📊 4. Reporte de Auditoría y Métricas del Sketion Quality Engine

La escena interactiva generada en `PRUEBAS_V3/arquitectura_restaurantes_saas.excalidraw` fue auditada con el siguiente resultado:

```text
==================================================
=== SKETION COMPREHENSIVE REPORT: ✅ PASS ===
==================================================
Elementos totales: 228 | Frames: 3
PUNTUACIÓN GLOBAL SKETION: 99/100

VISUAL QUALITY SCORE
─────────────────────────────────
Structure (Técnica Excalidraw) : 100/100
Layout (Espaciado & Gaps)      : 95/100
Readability (Legibilidad)      : 100/100
Hierarchy (1 Acento / Focos)   : 100/100
Visual Noise (Densidad: 4.9/10) : 94/100
Brand Consistency (Tokens)     : 100/100
─────────────────────────────────
OVERALL VISUAL QUALITY         : 98/100

SEMANTIC FIDELITY SCORE
─────────────────────────────────
Node Coverage        : 100/100 (19/19 nodos requeridos presentes)
Edge Coverage        : 100/100 (19/19 relaciones trazadas)
Scope Coverage       : 100/100 (6/6 scopes de infraestructura)
Hierarchy Fidelity   : 100/100 (Reservation Service con acento cobalto)
─────────────────────────────────
OVERALL FIDELITY     : 100/100
```

---

## 📁 Archivos Entregables en `PRUEBAS_V3/`

1. **[`PRUEBAS_V3/arquitectura_restaurantes_saas.excalidraw`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V3/arquitectura_restaurantes_saas.excalidraw)** *(Lienzo interactivo completo con 3 frames: Arquitectura, Concurrencia y Matriz de Resiliencia)*.
2. **[`PRUEBAS_V3/generate_restaurant_saas.py`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V3/generate_restaurant_saas.py)** *(Script de código ejecutable que construye la escena y ejecuta las validaciones)*.
3. **[`PRUEBAS_V3/especificacion_tecnica_arquitectura.md`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V3/especificacion_tecnica_arquitectura.md)** *(Documento técnico formal de ingeniería)*.
