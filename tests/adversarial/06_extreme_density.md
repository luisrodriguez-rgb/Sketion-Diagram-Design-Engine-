# 🧪 Test Adversarial 06: Sobresaturación de Densidad y Auto-Split Elástico

## 🎯 Objetivo de la Prueba
Introducir **más de 25 entidades y 40 relaciones complejas** en un solo prompt. Verificar si el motor detecta la sobresaturación crítica ($\text{Densidad} > 7.0/10$) y activa automáticamente la **descomposición elástica multi-frame**, manteniendo la densidad en la zona dorada editorial ($3.5\text{--}4.5/10$).

---

## 📥 Prompt de Entrada (Raw Input)

```text
Diseña el mapa completo de infraestructura y flujos de un marketplace de comercio electrónico global que procesa 50,000 pedidos por minuto.

Incluye:
1. Red de Ingress: Cloudflare CDN, WAF, DNS Anycast, Load Balancer Envoy.
2. Capa de Aplicación: Auth Service, Catalog Service, Search Engine (Elasticsearch), Cart Service, Checkout Service, Pricing & Discounts Engine, Inventory Allocation, Recommendation ML, User Profile Service.
3. Capa de Mensajería y Eventos: Kafka Cluster (10 topics con particionado por customer_id), RabbitMQ (colas de prioridad para transacciones urgentes), Redis Pub/Sub (notificaciones en tiempo real a la UI).
4. Capa de Datos: PostgreSQL Primary-Replica (Sharding por región), DynamoDB (Sesiones y Carritos), ClickHouse (Event Store OLAP), Redis Cluster (Cache distribuida L1/L2), S3 Bucket (Imágenes y Facturas PDF).
5. Servicios de Terceros: Stripe, PayPal, MercadoPago, Twilio, SendGrid, Fedex API, DHL API, Datadog APM, PagerDuty.

Muestra cómo un usuario busca un producto, lo añade al carrito, aplica un cupón, paga con tarjeta, se reserva el stock en el almacén más cercano, se emite la factura y se genera la etiqueta de envío, con monitorización completa en caso de fallo.
```

---

## 🔍 Criterios de Evaluación y Juicio de Sketion

| Criterio | Decisión Correcta (PASS) | Decisión Incorrecta (FAIL) |
| :--- | :--- | :--- |
| **Detección de Sobresaturación** | El motor reconoce que 25 servicios + 5 capas en un solo frame colapsarían la legibilidad visual ($\text{Densidad} > 8.0/10$). | Dibujar una maraña de 25 cajas interconectadas con 40 líneas cruzadas (espagueti visual inmanejable). |
| **Descomposición Elástica** | Divide automáticamente el sistema en **3 frames coordinados**: (1. Topología Global de 5 Capas, 2. Flujo Secuencial E-Commerce de 8 Pasos, 3. Matriz de Resiliencia y Terceros). | Recortar o eliminar la mitad de las bases de datos para que quepa en un solo frame. |
| **Puntuación de Calidad** | Cada frame individual mantiene una densidad entre **3.5 y 4.5/10** con 0 colisiones de texto o flechas. | Frame saturado con penalización de densidad crítica en el validador. |
