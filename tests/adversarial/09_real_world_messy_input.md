# 🧪 Test Adversarial 09: Transcripción Oral Caótica y Desordenada (Loom / Zoom Dump)

## 🎯 Objetivo de la Prueba
Evaluar la capacidad de Sketion para **extraer orden y estructura a partir del caos verbal**: transcripciones sin filtrar de llamadas de Zoom o notas de voz donde el speaker divaga, cambia de idea, repite conceptos, usa muletillas y salta de un tema a otro sin orden cronológico.

---

## 📥 Prompt de Entrada (Raw Input)

```text
transcripción de la reunión con el fundador:
"a ver mira te cuento... o sea básicamente el cliente entra a la web y ve los productos no? pero bueno antes de eso el tipo tuvo que loguearse, ah no espera, puede navegar como invitado también, sí, que pueda ver el catálogo sin login. Pero cuando va a pagar ahí sí, le pedimos el mail. Bueno la cosa es que cuando le da al botón de comprar, eso tiene que hablar con Stripe, pero ojo porque si es en México usamos Conekta o SPEI. Ah y me olvidaba, el stock! Si dos personas compran la última remera al mismo tiempo una tiene que rebotar, no podemos vender cosas que no tenemos en el depósito. El depósito nos pasa un excel todos los días pero queremos que sea en tiempo real con una API. Si el pago pasa, le mandamos un WhatsApp con el tracking de Andreani o DHL, y a los del almacén les tiene que sonar una tablet para que armen el paquete. Si el tipo no está en la casa cuando llega el correo, bueno, ahí hay que reintentar dos veces y si no vuelve al depósito y se le reembolsa el 80% porque le cobramos el flete. Ah y el contador quiere ver todo en un dashboard a fin de mes con los impuestos separados por provincia. Armame un diagrama de cómo tiene que funcionar todo esto para mostrárselo a los inversores mañana."
```

---

## 🔍 Criterios de Evaluación y Juicio de Sketion

| Criterio | Decisión Correcta (PASS) | Decisión Incorrecta (FAIL) |
| :--- | :--- | :--- |
| **Limpieza y Extracción Estructurada** | Filtrar el ruido coloquial e identificar las 5 capas de arquitectura: (1. Catálogo/Invitado vs Checkout, 2. Enrutamiento de Pasarelas Stripe/Conekta, 3. Lock Atómico de Stock WMS, 4. Cadena Logística con reintentos y retorno, 5. Dashboard Contable/Fiscal). | Copiar frases textuales desordenadas del usuario dentro de las cajas del diagrama. |
| **Modelado de Reglas de Negocio Ocultas** | Mapear la regla de devolución del $80\%$ con deducción de flete ante entrega fallida en la máquina de estados. | Olvidar las reglas logísticas y hacer un simple checkout genérico. |
| **Tono para Inversores** | Formatear el diagrama con el **Arquetipo Duelo / Cadena de Valor** de alta estética editorial con titulares claros y métricas de retención, listo para pitch. | Presentar un boceto informal lleno de texto crudo sin jerarquía. |
