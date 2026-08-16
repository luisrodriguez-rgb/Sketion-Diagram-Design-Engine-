# 🎨 Catálogo Maestro: Los 20 Arquetipos Visuales de Sketion

**Sistema de Organización de Información y Composición Visual Editorial para Excalidraw Nativo.**

Inspirado en el **Kit Miro Nico**, diseño editorial de alta gama (Stripe, Apple, McKinsey) y arquitectura de sistemas complejos.

---

## 🧭 Índice de los 20 Arquetipos

| Código | Nombre del Arquetipo | Estructura Geométrica | Caso de Uso Principal |
| :-: | :--- | :--- | :--- |
| **A** | **EL CEREBRO** | Hub circular central con 4 ramas radiales | "Todo mi producto/sistema dentro de una herramienta" |
| **B** | **LAS FASES** | 6 cuadrantes con numerales gigantes (120px) | Roadmaps de 90 días, progresiones con gates |
| **C** | **LA SERPIENTE** | Curva S continua en vaivén (Boustrophedon) | Procesos lineales de 8 a 16 pasos sin desbordar |
| **D** | **EL DUELO (VS)** | 2 mitades enfrentadas con espina de stickies | Antes vs Después / Legacy vs Moderno / Pitches |
| **E** | **LA CADENA** | Swimlanes paralelos por actor con handoffs | Procesos multi-actor (Cliente, Máquina, Operario) |
| **F** | **EL EMBUDO (FUNNEL)** | Bloques trapezoidales descendentes con drop-off | Conversión de ventas, pipelines de contratación |
| **G** | **LA PIRÁMIDE** | 4-5 capas horizontales apiladas de base a cúspide | Modelos de madurez, niveles de seguridad |
| **H** | **EL RADAR 2x2** | Eje cartesiano ortogonal en 4 cuadrantes pastel | Priorización Impacto vs Esfuerzo, riesgos |
| **I** | **EL FLYWHEEL** | Círculo de 4-6 nodos con flechas perimetrales | Bucles de crecimiento (Growth Loops), retención |
| **J** | **LA CEBOLLA (ONION)** | Anillos concéntricos anidados hacia el núcleo | Clean Architecture, Hexagonal, Data Governance |
| **K** | **EL KANBAN WIP** | Columnas de estado con límites WIP en cabecera | Pipelines ágiles, releases, colas de trabajo |
| **L** | **EL ICEBERG** | Línea de agua: 15% visible vs 85% oculto | Deuda técnica, complejidad backend vs UI simple |
| **M** | **LA ESPINA (ISHIKAWA)**| Eje central horizontal con costillas diagonales | Análisis de causa raíz, post-mortems |
| **N** | **LA GALERÍA 3x3** | Grilla modular simétrica con chips de status | Catálogo de microfrontends, suite de productos |
| **O** | **EL ÁRBOL DE DECISIÓN**| Dilema inicial que bifurca en ramas SÍ/NO | Protocolos de escalado, triaje, reglas de negocio|
| **P** | **LA CADENA DE VALOR** | Franjas de soporte superiores y chevron final | Mapeo estratégico de operaciones y márgenes |
| **Q** | **LOS PILARES BENCHMARK**| Podio de 3 a 5 columnas con barras de llenado | Comparativa de rendimiento, latencia y costes |
| **R** | **ROADMAP CON GATES** | Timeline horizontal con diamantes de validación | Lanzamientos v3.0, auditorías SOC2 / ISO |
| **S** | **LA MATRIZ CRUD** | Grilla de Servicios (Y) vs Entidades (X) | Mapeo de propiedad de datos (Data Ownership) |
| **T** | **LA CAJA EXPLOTADA** | Caja macro conectada con líneas guía a zoom | Explicar el funcionamiento interno de un motor |

---

## 📐 Detalle de los 15 Nuevos Arquetipos (F a T)

---

### F · EL EMBUDO DE CONVERSIÓN (`engine_embudo`)
```text
┌──────────────────────────────────────────────────────────┐  10,000 Visitas (100%)
│ 1. VISITAS & DESCUBRIMIENTO                              │  Drop: -60%
└──────────────────────────────────────────────────────────┘
      ┌──────────────────────────────────────────────┐        4,000 Registro Free (40%)
      │ 2. ACTIVACIÓN & ONBOARDING                   │        Drop: -50%
      └──────────────────────────────────────────────┘
            ┌──────────────────────────────────┐              2,000 Usuarios Activos (20%)
            │ 3. USO RECURRENTE & ENGAGEMENT   │              Drop: -75%
            └──────────────────────────────────┘
                  ┌──────────────────────┐                    500 Clientes Pro (5%)
                  │ 4. MONETIZACIÓN PAID │
                  └──────────────────────┘
```
* **Elementos en Excalidraw:** Cajas decrecientes centradas, pastillas rojas laterales con el % de fuga (*Drop-off Rate*), números grandes en bold.

---

### G · LA PIRÁMIDE DE MADUREZ (`engine_piramide`)
```text
                       /  NIVEL 4: AUTONOMOUS AI  \
                      /────────────────────────────\
                     /  NIVEL 3: PREDICTIVE ANALYT  \
                    /────────────────────────────────\
                   /   NIVEL 2: AUTOMATED WORKFLOWS   \
                  /────────────────────────────────────\
                 /    NIVEL 1: MANUAL & REACTIVE OPS    \
                /────────────────────────────────────────\
```
* **Elementos en Excalidraw:** Capas horizontales apiladas con número de nivel en pastilla oscura, requisitos del nivel y salto de valor.

---

### H · EL RADAR DE 4 CUADRANTES 2x2 (`engine_cuadrantes_2x2`)
```text
                ALTO IMPACTO / VALOR
                        ▲
   [ QUICK WINS ]       │    [ APUESTAS ESTRATÉGICAS ]
   • Auth Magic Links   │    • Motor IA Recomendaciones
   • Exportar CSV       │    • Soporte Multi-Región
  ──────────────────────┼──────────────────────► ALTO ESFUERZO
   [ TAREAS DE LLENADO ]│    [ DESPERDICIO / NO HACER ]
   • Rediseño de iconos │    • Migración a Blockchain
   • Ajuste de footer   │    • Sistema de foros propio
                        ▼
```
* **Elementos en Excalidraw:** Eje cartesiano con flechas, 4 fondos tenues independientes (`#F8FAFC`, `#EFF6FF`, `#FEF2F2`, `#FEFCE8`), tarjetas con micro-chips.

---

### I · EL FLYWHEEL / RUEDA DE CRECIMIENTO (`engine_flywheel`)
```text
                     [ 1. MÁS CONTENIDO DE CALIDAD ]
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
       [ 4. MÁS RECOMENDACIONES ]            [ 2. MÁS TRÁFICO ORGÁNICO ]
                    ▲                             │
                    └──────────────┬──────────────┘
                                   │
                                   ▼
                       [ 3. MÁS VENTAS & FONDOS ]
```
* **Elementos en Excalidraw:** 4 a 6 nodos en órbita circular, flechas en arco perimetral con pastillas de impulso y un nodo central que resume el efecto compuesto.

---

### J · LA CEBOLLA / CAPAS CONCÉNTRICAS (`engine_cebolla`)
```text
┌─── CAPA 4: FRAMEWORKS & UI (Next.js, Flutter, CLI) ────────────────────────────────┐
│ ┌─── CAPA 3: ADAPTERS & GATEWAYS (PostgreSQL, Stripe, Kafka, Twilio) ────────────┐ │
│ │ ┌─── CAPA 2: CASOS DE USO / APLICACIÓN (CreateReservation, ValidateStock) ───┐ │ │
│ │ │ ┌─── CAPA 1: ENTIDADES DE DOMINIO & REGLAS CORE (Mesa, Reserva, Horario)─┐ │ │ │
│ │ │ └────────────────────────────────────────────────────────────────────────┘ │ │ │
│ │ └────────────────────────────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────────────────┘
```
* **Elementos en Excalidraw:** Cajas anidadas concéntricas con colores pastel decrecientes y flechas ortogonales que apuntan hacia el interior.

---

### K · EL TABLERO KANBAN (`engine_kanban`)
* **Estructura:** 4 columnas verticales (`BACKLOG [WIP: ∞]`, `EN PROGRESO [WIP: 3]`, `EN REVISIÓN [WIP: 2]`, `DONE [✓]`).
* **Elementos:** Post-it en la cabecera con ángulo orgánico, tarjetas blancas con chips de prioridad (`[P0 CRÍTICO]`, `[P1 ALTO]`).

---

### L · EL ICEBERG: VISIBLE VS. OCULTO (`engine_iceberg`)
* **Estructura:**
  - **Superficie (15%):** Fondo blanco `#FFFFFF` $\rightarrow$ "Botón 'Reservar Mesa' en 1 clic".
  - **Línea de Agua:** Trazo azul `#2563EB` con etiqueta `~~~ LÍNEA DE FLOTACIÓN (LO QUE NO SE VE) ~~~`.
  - **Fondo Marino (85%):** Fondo gris azulado `#F1F5F9` $\rightarrow$ 12 microservicios, locks distribuidos en Redis, conciliación de pagos y replicación de BD.

---

### M · LA ESPINA DE PESCADO (ISHIKAWA) (`engine_ishikawa`)
* **Estructura:** Eje central horizontal apuntando a la caja de problema a la derecha (`CAÍDA DEL SISTEMA EN BLACK FRIDAY`).
* **Ramas diagonales:** Personas (Falta de guardias), Código (Memory Leak), Infraestructura (Pool de BD agotado), Proveedores (Timeout de Pasarela).

---

### N · LA GALERÍA MODULAR 3x3 (`engine_galeria`)
* **Estructura:** Cuadrícula de 6 a 9 tarjetas idénticas con espaciado regular de 30px.
* **Elementos:** Icono en círculo, título en bold, descripción de 2 líneas y pastilla de estado (`[GA]`, `[BETA]`, `[PROXIMAMENTE]`).

---

### O · EL ÁRBOL DE DECISIÓN RAMIFICADO (`engine_arbol_decision`)
* **Estructura:** Nodo raíz con pregunta $\rightarrow$ bifurcación con pastillas verdes `[SÍ]` y rojas `[NO]` hacia nodos secundarios y cajas terminales de acción.

---

### P · LA CADENA DE VALOR DE PORTER (`engine_cadena_valor`)
* **Estructura:** Franja superior de infraestructura de soporte (RRHH, Tecnología, Compras) y 5 cajas inferiores secuenciales (Inbound $\rightarrow$ Operaciones $\rightarrow$ Outbound $\rightarrow$ Marketing $\rightarrow$ Servicio), cerrando con un chevron triangular de "Margen".

---

### Q · LOS PILARES DE BENCHMARK (`engine_pilares_benchmark`)
* **Estructura:** 3 a 5 columnas verticales altas tipo podio. Cada columna tiene una barra de nivel (ej. 85% de llenado en cobalto), una cifra gigante y 3 bullets de fortalezas.

---

### R · ROADMAP CON GATES DE CALIDAD (`engine_roadmap_gates`)
* **Estructura:** Eje horizontal cronológico donde cada fase concluye con un **diamante de Gate** con checklist (`[✓] 100% Tests unitarios`, `[✓] Auditoría de seguridad`, `[✓] Aprobación CTO`).

---

### S · LA MATRIZ CRUD DE ENTIDADES (`engine_matriz_crud`)
* **Estructura:** Tabla con microservicios en el eje vertical y entidades en el horizontal, con celdas que contienen pastillas coloreadas:
  - 🟢 `[C]` Crear
  - 🔵 `[R]` Leer
  - 🟡 `[U]` Actualizar
  - 🔴 `[D]` Borrar

---

### T · LA CAJA EXPLOTADA (DEEP DIVE ZOOM) (`engine_exploded_box`)
* **Estructura:** Una tarjeta macro a la izquierda ("Availability Service") conectada mediante líneas de proyección discontinuas hacia un frame detallado a la derecha que desglosa su algoritmo interno de locks y consultas.

---

## 🎨 Paleta y Tokens de Renderizado Editorial

```python
MIRO_NICO_TOKENS = {
    "CANVAS_BG": "#F4F4F4",       # Fondo de pizarra
    "CARD_BG": "#FFFFFF",         # Tarjetas blancas nítidas
    "CARD_BORDER": "#BDBDBD",     # Borde suave 1.5px
    "INK": "#0C0C0C",             # Tinta negra sólida
    "MUTED": "#9A9A9A",           # Texto secundario y flechas auxiliares
    "STICKY_YELLOW": "#FFE95C",   # Post-it de sección con tilt (-2° a +2°)
    "PAIN_RED": "#E03A2F",        # Alertas, cuellos de botella y números críticos
    "PAIN_BG": "#FDEFEF",         # Fondo de tarjetas de dolor
    "PAIN_BORDER": "#F05A5A",     # Borde discontinuo de slots
    "BANNER_PINK": "#F5BEC0",     # Frase de remate / punchline
    "PASTEL_BLUE": "#9BC7E4",     # Cabeceras de fases y zonas
    "PASTEL_GREEN": "#C2E5D3",    # Estados confirmados y éxitos
    "ROUGHNESS": 0                # Trazo vectorial editorial profesional
}
```
