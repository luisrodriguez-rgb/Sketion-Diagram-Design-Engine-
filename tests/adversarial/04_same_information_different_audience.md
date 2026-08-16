# 🧪 Test Adversarial 04: Misma Información para 5 Audiencias Distintas

## 🎯 Objetivo de la Prueba
Evaluar si Sketion comprende el concepto de **Audience-Aware Information Hierarchy**. El mismo sistema subyacente (ej. la plataforma de pagos distribuida) debe producir **5 representaciones visuales completamente diferentes** según la audiencia destinataria.

---

## 📥 El Caso Base y las 5 Variantes de Audiencia

### Problema Base:
Plataforma de Pagos que procesa transacciones de comercio electrónico, valida fraude con ML, enruta hacia pasarelas bancarias, asienta en Ledger inmutable y notifica a comercios con SLA de 50ms y tolerancia a fallos.

---

### 👤 Variante A: Para un CTO / Chief Architect
* **Intención:** *"Explícaselo al CTO para una revisión de arquitectura y gobernanza."*
* **Foco Esperado:**
  - Topology de infraestructura (Kafka, Redis Cluster, PostgreSQL Multi-AZ, Circuit Breakers).
  - Protocolos de replicación, latencias P99 ($<45\text{ms}$), SLA de pasarela y recuperación ante desastres (RPO=0, RTO < 60s).
  - Outbox Pattern, políticas de particionado de Kafka y consistencia ACID vs Eventual.
* **Arquetipo Óptimo:** `ARQUITECTURA DE RED DISTRIBUIDA (SCOPES 1-7) + MATRIZ DE RESILIENCIA`.

---

### 👤 Variante B: Para un Diseñador de Producto / UX Lead
* **Intención:** *"Explícaselo al Diseñador de Producto que lidera la experiencia de checkout."*
* **Foco Esperado:**
  - Journey del usuario final: Formulario de tarjeta $\rightarrow$ Spinner de procesamiento $\rightarrow$ Pantalla de éxito / 3D Secure / Pantalla de error amigable.
  - Micro-estados de la interfaz: feedback visual durante el tiempo de espera, mensajes de rechazo comprensibles ("Tarjeta vencida", "Fondos insuficientes").
  - Flujo de reintento en 1-clic y notificaciones push en el móvil del cliente.
* **Arquetipo Óptimo:** `ARQUETIPO C · LA SERPIENTE (USER JOURNEY) + CAPTURAS DE INTERFAZ`.

---

### 👤 Variante C: Para un Gerente No Técnico / CFO
* **Intención:** *"Explícaselo al CFO / Director Financiero de la empresa."*
* **Foco Esperado:**
  - Flujo del dinero y comisiones: Tarifa por transacción ($2.9\% + \$0.30$), retención de fondos, liquidación $T+2$ al comercio y conciliación de extractos bancarios.
  - Mitigación de pérdidas por fraude (Chargebacks, contracargos $<0.5\%$) y métricas de volumen transaccional diario.
  - Cumplimiento normativo PCI-DSS y auditoría fiscal.
* **Arquetipo Óptimo:** `ARQUETIPO P · CADENA DE VALOR / FLUJO FINANCIERO + DASHBOARD DE KPIS`.

---

### 👤 Variante D: Documentación de Integración para Desarrolladores (Dev Docs)
* **Intención:** *"Úsalo como diagrama central en la documentación técnica para desarrolladores que integran nuestra API."*
* **Foco Esperado:**
  - Contratos de API: `POST /v1/charges`, headers HTTP (`Idempotency-Key`, `Authorization: Bearer`), payloads JSON con tipos de datos.
  - Diagrama de secuencia síncrono: Request $\rightarrow$ Response $200\text{ OK} / 400 / 422$ y Webhook payload events (`charge.succeeded`, `charge.failed`).
  - Snippets de código y códigos de error normalizados (`ERR_CARD_DECLINED`, `ERR_INSUFFICIENT_FUNDS`).
* **Arquetipo Óptimo:** `DIAGRAMA DE SECUENCIA API + CONTRATO DE CARGA ÚTIL (JSON SCHEMA)`.

---

### 👤 Variante E: Pitch Deck para Inversionistas (Presentación de 5 Minutos)
* **Intención:** *"Úsalo en una presentación ejecutiva de 5 minutos ante inversores."*
* **Foco Esperado:**
  - El dolor del mercado: El 15% de las ventas online se pierden por pasarelas lentas, caídas y fraude no detectado.
  - Nuestra solución única: Motor de enrutamiento inteligente que recupera el 99.4% de los pagos con zero-downtime.
  - Cifras de tracción y escala: \$120M procesados, 1,400 comercios, crecimiento $3.2\times$ interanual.
* **Arquetipo Óptimo:** `ARQUETIPO D · EL DUELO (ANTES CAÓTICO VS NUESTRA PLATAFORMA) + CHIPS HEROICOS`.
