# 🧪 Test Adversarial 03: Conflicto entre Calidad Visual y Fidelidad Semántica

## 🎯 Objetivo de la Prueba
Evaluar el comportamiento de Sketion cuando la exhaustividad de relaciones de un sistema financiero distribuido amenaza con saturar el canvas. Comprobar que el motor aplica **Semantic Hard Constraints** y **NUNCA elimina componentes críticos ni simplifica reglas de negocio complejas solo para que el diagrama se vea más limpio**.

---

## 📥 Prompt de Entrada (Raw Input)

```text
Representa el siguiente sistema manteniendo toda la información importante.

Una plataforma de pagos recibe solicitudes de pago desde comercios.

Cada solicitud contiene:
merchant_id
customer_id
amount
currency
payment_method
order_id

La solicitud pasa por:
API Gateway
Authentication
Fraud Detection
Payment Orchestrator
Payment Provider
Ledger
Notification Service
Analytics

Fraud Detection puede devolver:
APPROVED
REVIEW
REJECTED

Payment Provider puede devolver:
AUTHORIZED
DECLINED
TIMEOUT
UNKNOWN

Si el resultado es UNKNOWN, el sistema no puede asumir que el pago falló porque el proveedor podría haberlo procesado.
El sistema debe realizar reconciliation posteriormente.

Un pago autorizado puede posteriormente:
- capturarse
- cancelarse
- reembolsarse parcialmente
- reembolsarse totalmente

El Ledger debe ser la fuente de verdad financiera.
Las notificaciones no deben modificar el estado financiero.
Analytics debe ser eventual y nunca bloquear el procesamiento.
Los eventos pueden entregarse más de una vez.
Todos los consumidores deben ser idempotentes.

El sistema debe soportar:
- timeout del proveedor
- doble envío de una solicitud
- respuesta duplicada
- webhook duplicado
- webhook fuera de orden
- caída temporal de Analytics
- caída temporal de Notifications

Representa toda la información necesaria para que un ingeniero pueda entender las responsabilidades y estados del sistema.
No elimines relaciones importantes para mejorar visualmente el resultado.
Si no es posible representar toda la información claramente en un solo canvas, determina cómo dividirla.
```

---

## 🔍 Criterios de Evaluación y Juicio de Sketion

| Criterio de Dominio | Decisión Correcta (PASS) | Decisión Incorrecta (FAIL) |
| :--- | :--- | :--- |
| **Manejo de `UNKNOWN`** | `UNKNOWN` transiciona a `PENDING_RECONCILIATION` y activa el worker de conciliación. | Asumir que `UNKNOWN` o `TIMEOUT` es un fallo directo (`FAILED/DECLINED`). |
| **Ledger Inmutable** | Modelar el Ledger como única fuente de verdad con partida doble ($\sum \text{Debe} = \sum \text{Haber}$). | Tratar el Ledger como un simple log secundario que se puede actualizar (`UPDATE balance`). |
| **Aislamiento de Dominio** | Notificaciones y Analytics son estrictamente *read-only* y desacoplados asíncronamente en Kafka. | Conectar Notificaciones en el flujo síncrono bloqueando la confirmación del pago. |
| **Tolerancia a Concurrencia** | Matriz formal de resiliencia que cubre los 7 escenarios distribuidos (idempotencia en Redis, versionado de webhooks, DLQ). | Omitir los escenarios de concurrencia o resolverlos con textos vagos tipo *"el sistema reintenta"*. |
| **Resolución del Conflicto** | Dividir la arquitectura en **Frames Especializados** (Pipeline, Estados, Matriz de Idempotencia, Modelo Ledger) para preservar el 100% de los datos con densidad 4/10. | Borrar el Ledger o los webhooks para que todo quepa en 1 solo frame y "se vea bonito". |
