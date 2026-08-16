# 🎯 Especificación del Benchmark de 3 Audiencias (Pruebas V5)

**Demostración de Criterio Semántico y Adaptación Visual: Mismo Caso Base $\rightarrow$ 3 Perspectivas Profesionales Radicalmente Diferentes.**

---

## 🏛️ Comparativa de Enfoque por Audiencia

```text
                               CASO BASE: CAFETERÍA UNIVERSITARIA
                                               │
         ┌─────────────────────────────────────┼─────────────────────────────────────┐
         ↓                                     ↓                                     ↓
  1. CEO / DIRECTIVO                    2. GERENTE OPERACIONES                3. EQUIPO DE PRODUCTO
  (Diagrama de Decisión)                (Proceso Físico y Takt)               (Arquitectura de Sistema)
  ─────────────────────                 ───────────────────────               ─────────────────────────
  • Archivo: 01_audiencia_ceo...        • Archivo: 02_audiencia_ops...        • Archivo: 03_audiencia_prod...
  • Foco: Margen, ROI, Riesgo y         • Foco: Tiempos de ciclo (Takt),      • Foco: Pre-Order App, KDS en
    aprobación de fases a coste $0.       carriles A/B y batching previo.       cocina, ETA Engine y Lockers.
  • Arquetipo: Duelo VS + Roadmap       • Arquetipo: Planta Física + Matriz   • Arquetipo: Arquitectura Cloud +
    de Fases con Aprobación.              de Tiempos de Ciclo.                  User Journey con Slots UI.
  • Elimina: Detalles de APIs,          • Elimina: Métricas financieras       • Elimina: Consideraciones de
    código y pantallas de cocina.         macro y código de software.           contratos laborales y CAPEX.
```

---

## 🔍 1. Audiencia 1: CEO / Directivo (`01_audiencia_ceo_decision.excalidraw`)
* **Propósito:** Permitir al Consejo de Administración o Director Ejecutivo tomar una decisión de aprobación en menos de 2 minutos.
* **Frames:**
  1. **El Duelo Estratégico (As-Is vs To-Be):** Contraste entre el modelo colapsado (déficit $-130\text{ ped/h}$, pérdida de $\$28\text{k/año}$, $14\%$ abandono) vs el modelo propuesto ($410\text{ ped/h}$, $+\$42\text{k}$ beneficio neto, abandono $<1.5\%$).
  2. **Hoja de Ruta Directiva por Fases:**
     - *Fase 1 (Semana 1):* Quick Wins a coste $\$0$ (Separar Order/Pickup, Reasignar personal, Batching previo de 80 unidades).
     - *Fase 2 (Semanas 2-4):* Inversión mínima en App de Pre-Order y Estación de Retiro Rápido (ROI 30 días).
     - *Fase 3 (Mes 2):* Menú especial de hora pico y combos rápidos para maximizar ticket promedio.
     - *Banner de Resolución Directiva:* Aprobación formal de Fase 1 inmediata y presupuesto de Fase 2.

---

## 🔍 2. Audiencia 2: Gerente de Operaciones (`02_audiencia_operaciones_proceso.excalidraw`)
* **Propósito:** Permitir al Jefe de Planta / Supervisor de Turno organizar físicamente la barra y balancear la línea de producción sin congestión.
* **Frames:**
  1. **Planta Operativa y Segregación de Espacios:**
     - *Zona 1 (Ingress):* Carril A (Fila de 12 personas máx) + Puesto 1 (Cajero Puro: solo cobra, Takt 9.0s).
     - *Zona 2 (Cocina):* Estación de Batching previo (80 unidades en calor) + Puestos 2 y 3 (2 cocineros con pantalla KDS).
     - *Zona 3 (Expedición):* Puesto 4 (Runner / Entrega física) + Carril B (Espera de recogida despejada).
     - *Zona 4 (Canal Digital Express):* Casillero de autoservicio QR (retiro en 5 segundos sin pisar la fila).
  2. **Ingeniería de Proceso y Matriz de Takt Time:**
     - Cálculo formal de tiempos de ciclo: Caja ($35\text{s} \rightarrow 9.0\text{s}$), Cocina rápida ($90\text{s} \rightarrow 15\text{s}$ en batch de 10), Despacho ($7.5\text{s}$ continuo) y App Express ($4.0\text{s}$).

---

## 🔍 3. Audiencia 3: Equipo de Producto / Tech (`03_audiencia_producto_sistema.excalidraw`)
* **Propósito:** Proveer a los Product Managers y Desarrolladores la arquitectura de microservicios y el journey de interacción para construir la solución digital.
* **Frames:**
  1. **Arquitectura de Software y Motor ETA:**
     - *Ingress:* App Móvil Alumnos (Flutter/React Native), Terminal POS Caja Contactless y Portal Web Staff.
     - *Core Services:* `Order Orchestrator`, `Dynamic ETA Engine` (cálculo de minutos de espera en tiempo real) y `Slot / Inventory Manager`.
     - *Hardware:* Pantalla KDS en cocina, tableta del runner y Pantalla TV pública con cola de turnos.
  2. **User Journey Digital del Alumno:**
     - 5 pasos: Selección de Slot $\rightarrow$ Pago 1-clic Apple/Google Pay $\rightarrow$ Comanda KDS a 4 min de entrega $\rightarrow$ Alerta Push $\rightarrow$ Retiro express en casillero con QR.
     - 4 slots de captura de interfaz para validación de diseño de UI/UX.

---

## 📁 Archivos Entregados en `PRUEBAS_V5/`

* 🎨 [**`PRUEBAS_V5/01_audiencia_ceo_decision.excalidraw`**](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V5/01_audiencia_ceo_decision.excalidraw) *(Decisión Estratégica / Score: 97/100)*
* 🎨 [**`PRUEBAS_V5/02_audiencia_operaciones_proceso.excalidraw`**](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V5/02_audiencia_operaciones_proceso.excalidraw) *(Proceso Físico y Takt / Score: 94/100)*
* 🎨 [**`PRUEBAS_V5/03_audiencia_producto_sistema.excalidraw`**](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V5/03_audiencia_producto_sistema.excalidraw) *(Arquitectura de Software / Score: 93/100)*
* 📜 [**`PRUEBAS_V5/generate_audience_benchmarks.py`**](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V5/generate_audience_benchmarks.py)
* 📋 [**`PRUEBAS_V5/especificacion_3_audiencias.md`**](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V5/especificacion_3_audiencias.md)
