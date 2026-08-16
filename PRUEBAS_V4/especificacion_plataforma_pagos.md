# 💳 Especificación de Arquitectura e Ingeniería: Plataforma Distribuida de Procesamiento de Pagos

**Sistema de Alta Concurrencia con Ledger Inmutable en Doble Partida, Idempotencia Exact-Once y Tolerancia a Fallos Distribuidos.**

---

## 🎯 1. Principios de Diseño & Aislamiento de Dominio

La plataforma se rige por **4 reglas arquitectónicas inviolables**:

1. **El Ledger es la Única Fuente de Verdad Financiera:** Ningún servicio externo ni base de datos secundaria determina el balance. Los balances se calculan mediante agregación inmutable de asientos en partida doble ($\sum \text{Debe} = \sum \text{Haber}$).
2. **Las Notificaciones Jamás Mutan Estado Financiero:** El `Notification Service` es un consumidor downstream de solo lectura. Un fallo, duplicación o retraso en un webhook jamás afecta la liquidación del dinero.
3. **Analytics es Eventual y No-Bloqueante:** El motor OLAP (ClickHouse/BigQuery) se alimenta de forma asíncrona mediante Kafka. Si Analytics cae o sufre retraso, la pasarela sigue autorizando pagos con latencia $< 50\text{ms}$.
4. **Idempotencia y Semántica At-Least-Once:** Todos los consumidores asumen que los eventos pueden recibirse múltiples veces o fuera de orden. El estado se protege mediante monotonicidad de versiones y claves de deduplicación en Redis.

---

## 🏛️ 2. Descomposición de la Arquitectura en 4 Frames

```text
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    PLATAFORMA DISTRIBUIDA DE PAGOS (PRUEBAS V4 - INGENIERÍA)                      │
├──────────────────────────┬──────────────────────────┬───────────────────────┬─────────────────────┤
│ FRAME 1: PIPELINE CORE   │ FRAME 2: MÁQUINA ESTADOS │ FRAME 3: RESILIENCIA  │ FRAME 4: MODELO BD  │
│ • 7 Scopes End-to-End    │ • Fraude & UNKNOWN       │ • Matriz 7 Fallos     │ • Payload JSON      │
│ • Síncrono vs Asíncrono  │ • Ciclo Post-Autorización│ • Deduplicación Redis │ • Ledger Doble Part.│
│ • Outbox Pattern & Kafka │ • Worker Reconciliación  │ • Versioning Webhooks │ • Reglas Aislamiento│
└──────────────────────────┴──────────────────────────┴───────────────────────┴─────────────────────┘
```

---

## 🔍 3. Detalle de los 4 Frames en `plataforma_pagos_distribuida.excalidraw`

### [Frame 1] Arquitectura Distribuida y Pipeline de Procesamiento
Estructurado en 7 columnas de infraestructura con 65px de gutter:
1. **Comercio (Merchant):** Envía `POST /v1/charges` con `merchant_id`, `customer_id`, `amount`, `currency`, `payment_method`, `order_id` y cabecera `Idempotency-Key: uuid`.
2. **Ingress & Auth:** API Gateway con rate limiting y Auth Service que valida la firma HMAC y API Key del comercio.
3. **Fraud Detection Engine:** Modelo ML que evalúa riesgo en $< 40\text{ms}$ y devuelve `APPROVED`, `REVIEW` o `REJECTED`.
4. **Payment Orchestrator:** Máquina de estados transaccional con *Transactional Outbox Pattern* y `Reconciliation Worker` en segundo plano.
5. **Payment Provider / Acquirer:** Procesador externo que responde `AUTHORIZED`, `DECLINED`, `TIMEOUT` o `UNKNOWN`.
6. **Financial Ledger:** Libro mayor inmutable en PostgreSQL donde se asienta la partida doble.
7. **Proyecciones Asíncronas:** Kafka Event Broker alimentando al `Notification Service` (webhooks al comercio) y `Analytics Engine` (ClickHouse).

---

### [Frame 2] Máquina de Estados Financiera & Ciclo Post-Autorización
* **Tratamiento de Fraude:**
  - `APPROVED` $\rightarrow$ Continúa a llamada de pasarela.
  - `REVIEW` $\rightarrow$ Cola manual para analistas de riesgo.
  - `REJECTED` $\rightarrow$ Rechazo inmediato sin consultar proveedor.
* **Manejo Crítico de `UNKNOWN` / `TIMEOUT`:**
  - Si el proveedor devuelve `TIMEOUT` o error 5xx, el sistema **NO asume que el pago falló**.
  - Pasa a estado `PENDING_RECONCILIATION`.
  - El `Reconciliation Worker` realiza polling exponencial ($30\text{s}, 2\text{m}, 10\text{m}$) y conciliación nocturna por extracto de liquidación.
* **Ciclo de Vida Post-Autorización:**
  $$\text{AUTHORIZED} \longrightarrow \text{CAPTURED} \longrightarrow \begin{cases} \text{PARTIALLY REFUNDED} \\ \text{FULLY REFUNDED} \end{cases}$$
  $$\text{AUTHORIZED} \longrightarrow \text{VOIDED / CANCELLED (Anulación previa a captura)}$$

---

### [Frame 3] Matriz de Resiliencia, Idempotencia y Manejo de Fallos (7 Escenarios)

| Escenario de Fallo | Causa Distribuida | Mecanismo de Idempotencia | Impacto en Ledger | Garantía de Consistencia |
| :--- | :--- | :--- | :--- | :--- |
| **1. Doble Envío de Solicitud** | Doble clic o reintento de red del cliente. | Redis Lock `idempotency:{mch}:{key}` con TTL 24h. Si existe, retorna respuesta en cache. | Cero duplicación de asientos. Un solo cargo. | **Exact-Once Effect** |
| **2. Timeout del Proveedor** | Pasarela no responde en 5000ms tras procesar. | Estado `PENDING_RECONCILIATION` y delegación en `Reconciliation Worker`. | No se crea asiento hasta confirmación de cobro. | **Consistencia Eventual** |
| **3. Respuesta Duplicada** | Confirmación doble síncrona del proveedor. | Filtro de State Machine: si ya es `AUTHORIZED`, ignora el segundo payload. | Ninguno. El Ledger ignora eventos ya aplicados. | **Idempotent State Check** |
| **4. Webhook Duplicado** | Proveedor reintenta webhook HTTP 5 veces. | Tabla de deduplicación con Unique Constraint sobre `webhook_event_id`. | Primer webhook asienta; los siguientes retornan 200 OK sin procesar. | **Deduplicación Atómica** |
| **5. Webhook Fuera de Orden** | Llega `CAPTURED` antes que `AUTHORIZED`. | Verificación de monotonicidad de versiones (`version_seq`). Aplica ambos secuencialmente. | Genera asientos de autorización y captura en orden lógico. | **Sequencing & Versioning** |
| **6. Caída de Notifications** | Servicio de webhooks / email temporalmente caído. | Outbox pattern en Kafka. Los eventos quedan encolados en el broker. | Cero impacto. El Ledger ya está cerrado y consistente. | **Aislamiento de Dominio** |
| **7. Caída de Analytics** | ClickHouse / BigQuery en mantenimiento. | Consumo asíncrono con Dead Letter Queue (DLQ) y replay al restablecer. | Cero impacto financiero. Analytics es 100% read-only. | **Eventual Consistency** |

---

### [Frame 4] Modelo de Datos, Doble Partida del Ledger y Aislamiento

#### 1. Payload Schema de la Solicitud
```json
{
  "merchant_id": "mch_994812",
  "customer_id": "usr_440192",
  "amount": 14950,
  "currency": "USD",
  "payment_method": {
    "type": "credit_card",
    "token": "tok_visa_4242"
  },
  "order_id": "ord_88192301",
  "idempotency_key": "idem_a8f9-41bc-9901"
}
```

#### 2. Estructura de Asiento de Doble Partida en Ledger (Captura $149.50)
* **Cuenta Debitada (DEBE):**
  * `Activo / Fondos por Cobrar Pasarela`: $+\$149.50$
* **Cuentas Acreditadas (HABER):**
  * `Pasivo / Saldo Comercio (Merchant)`: $+\$145.01$
  * `Ingreso / Comisión Plataforma (Fee)`: $+\$4.49$
* **Balance:** $\sum \text{Debe} (\$149.50) = \sum \text{Haber} (\$149.50)$.
* *Regla Inmutable:* Prohibido `UPDATE` o `DELETE` sobre asientos. Cualquier corrección se emite como un nuevo asiento de contrapartida.
