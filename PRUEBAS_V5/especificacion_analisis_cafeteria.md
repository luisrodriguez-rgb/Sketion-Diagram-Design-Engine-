# ☕ Especificación y Diagnóstico Operativo: Análisis de Cuellos de Botella en Cafetería Universitaria

**Diagnóstico As-Is, Modelo Causal de Ishikawa, Evaluación de 10 Alternativas (A - J) y Plan de Acción 2x2 para Equipo Directivo.**

---

## 🎯 1. Resumen Ejecutivo del Problema

* **Capacidad Nominal:** 180 pedidos / hora en periodos normales.
* **Demanda en Receso Principal:** 430 pedidos / hora.
* **Capacidad Teórica de Cocina:** 300 pedidos / hora.
* **Déficit Estructural:** **$-130\text{ pedidos/hora}$** durante la hora pico de receso.
* **Punto de Quiebre:** Cuando la fila supera las 25 personas, el tiempo de espera se incrementa de forma no lineal y los clientes abandonan la fila sin comprar (pérdida directa de facturación).

---

## 🏛️ 2. Estructura de la Composición Multi-Frame (4 Marcos Coordinados)

```text
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                 ANÁLISIS OPERATIVO DE CAFETERÍA UNIVERSITARIA (PRUEBAS V4)                        │
├──────────────────────────┬──────────────────────────┬───────────────────────┬─────────────────────┤
│ FRAME 1: FLUJO AS-IS     │ FRAME 2: MODELO CAUSAL   │ FRAME 3: MATRIZ A - J │ FRAME 4: PLAN 2X2   │
│ • Canales 71/19/10       │ • Espina de Ishikawa     │ • 10 Alternativas vs  │ • Radar Impacto/Esf.│
│ • Cajero 5-en-1          │ • 4 Ramas: Personas,     │   5 Restricciones     │ • Quick Wins        │
│ • Mezcla 62/23/15        │   Procesos, Capacidad,   │ • Trade-offs y Riesgo │ • 6 KPIs de Éxito   │
│ • Déficit -130 ped/h     │   Espacio y Visibilidad  │ • Dictamen Directivo  │ • Capacidad 410 p/h │
└──────────────────────────┴──────────────────────────┴───────────────────────┴─────────────────────┘
```

---

## 🔍 3. Detalle de los 4 Frames en `analisis_operaciones_cafeteria.excalidraw`

### [Frame 1] Diagnóstico As-Is: Flujo Operativo y Déficit de Capacidad
* **Arquetipo:** `Arquetipo E (Swimlanes)` + `Embudo de Capacidad`.
* **Canales de Entrada:**
  * Fila física: $71\%$ (llegan directo sin pedido previo).
  * App Digital: $19\%$ (horas de recogida variables, se acumulan en cocina).
  * Interno / Staff: $10\%$ (eventos y profesores).
* **Cuello de Botella 1 (Caja Multifunción):** 1 sola persona debe tomar pedidos, cobrar, resolver preguntas, entregar café y solucionar fallos de datáfono.
* **Cuello de Botella 2 (Cocina):** Demanda pico de 430 ped/h vs capacidad de 300 ped/h. El $15\%$ de productos tardan $>8\text{ min}$, bloqueando la línea de salida.
* **Zona de Congestión:** Clientes pidiendo, esperando entrega y retirándose colisionan en el mismo espacio físico de 3 metros sin señalización.

---

### [Frame 2] Modelo Causal: Espina de Ishikawa (Causa Raíz)
* **Arquetipo:** `Arquetipo M (La Espina de Ishikawa)`.
* **Efecto Terminal (Cabeza):** *"Colapso en Receso, Fila > 25 personas y Abandono de Clientes"*.
* **4 Costillas de Causa Raíz:**
  1. **Personas & Roles:** Cajero desbordado con 5 funciones incompatibles; sin apoyo de entrega en pico.
  2. **Procesos & Canales:** $71\%$ sin pedido previo; pedidos digitales entran sin aviso a cocina.
  3. **Producto & Capacidad:** Déficit de $-130\text{ ped/h}$; productos de alto margen requieren cocción prolongada.
  4. **Espacio & Visibilidad:** Sin separación entre "Pedir" y "Recoger"; clientes sin visibilidad del tiempo estimado.

---

### [Frame 3] Matriz de Evaluación de 10 Alternativas (A - J) frente a 5 Restricciones

| ID | Alternativa | Impacto en Capacidad | Cumplimiento de Restricciones | Trade-Off / Riesgo | Dictamen |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **A** | **Pedidos Anticipados** | Alto ($+25\%$ throughput) | $100\%$ (Cero obras) | Requiere adopción de app | **PRIORIDAD 1** |
| **B** | **Separar Order y Pickup** | Muy Alto ($-40\%$ congestión) | $100\%$ (Reorganiza barra actual) | Mínimo costo de señalética | **PRIORIDAD 1 (Quick Win)** |
| **C** | **Menú Especial Pico** | Alto ($+30\%$ velocidad cocina) | Cumple (Solo 2 horas pico) | Menos variedad temporal | **PRIORIDAD 2** |
| **D** | **Batching Anticipado** | Muy Alto ($+35\%$ despacho) | $100\%$ (Usa horas valle previas) | Riesgo leve de merma | **PRIORIDAD 1** |
| **E** | **Pronóstico Histórico** | Medio ($+15\%$ previsión) | $100\%$ (Solo software) | Requiere registro de datos | **PRIORIDAD 2** |
| **F** | **Estación Digital Dedicada**| Alto (Descongestiona barra $19\%$) | Cumple (Ocupa 1.5m barra) | Ninguno relevante | **PRIORIDAD 1** |
| **G** | **Reasignación de Personal** | Muy Alto (Elimina cuello de caja) | $100\%$ (Cero contrataciones) | Exige capacitación cruzada | **PRIORIDAD 1 (Quick Win)** |
| **H** | **Pantallas de Espera** | Medio (Reduce abandono) | $100\%$ (Bajo coste) | No acelera cocción | **PRIORIDAD 2** |
| **I** | **Eliminar Baja Rotación** | Bajo en pico / Alto riesgo | **INCUMPLE (Prohibido bajar menú)** | Daña satisfacción de fijos | **DESCARTADA** |
| **J** | **Combos Rápidos** | Alto ($+20\%$ velocidad) | $100\%$ (Mejora ticket) | Requiere stock en barra | **PRIORIDAD 2** |

---

### [Frame 4] Plan de Implementación 2x2 & Dashboard de Métricas de Éxito
* **Arquetipo:** `Arquetipo H (Radar 2x2)` + `Dashboard de KPIs`.
* **Quick Wins Inmediatos (Costo Cero / Alto Impacto):**
  1. `B. Separar físicamente Order y Pickup` mediante carril A y B.
  2. `G. Reasignar personal durante el receso` (1 caja pura, 1 runner de entrega, 2 cocina).
  3. `D. Batching previo` de los 5 productos más vendidos antes de las 10:00 AM.
* **Proyectos Estratégicos:** Implementación de app de pre-order (`A`) y mesa de retiro dedicada (`F`).
* **Métricas Meta de Validación:**
  1. **Capacidad Efectiva:** $410\text{ ped/hora}$ ($+36\%$ sin nuevas contrataciones).
  2. **Tasa de Abandono de Fila:** $< 1.5\%$ (antes: $14\%$).
  3. **Tiempo Promedio de Espera P90:** $3.2\text{ minutos}$ (máximo 8 personas en fila).
  4. **Margen Promedio:** $+4.8\%$ protegido con combos.
  5. **Penetración Digital:** $42\%$ migrado a pre-order.
  6. **Costo Fijo Adicional:** $\$0$ en nuevos contratos a tiempo completo.
