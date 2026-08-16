---
name: sketion-diagram-design
description: Generador editorial de diagramas y tableros nativos para Excalidraw (.excalidraw). Arquitectura desacoplada en 4 capas (Semantica -> Layout -> Render -> Calidad Visual) con motor de inferencia por audiencia (Audience-Aware Engine), Catalogo Completo de 20 Arquetipos de Negocio (A - T), Suite de 27 Tipos Visuales Específicos, Gramatica Editorial de Diagram Design (Tarjetas Quad-Corner, Cintas Chevron, Rieles Verticales, Ejes de Pasos, Leyendas Estructuradas), simetria 1:1 en journeys, enrutamiento inter-zonas y evaluador de Semantic Hard Constraints & Archetype Fitness sin colisiones.
license: MIT
metadata:
  version: "4.0"
---

# Sketion Diagram Design Skill (Motor Editorial para Excalidraw v4.0)

Crea tableros y diagramas profesionales con calidad editorial, diseno limpio, cero amontonamientos y editabilidad nativa total en formato `.excalidraw`.

Combina los principios de **Diagram Design** (densidad 4/10, regla del acento unico, eliminacion de ruido visual) con el **Motor de Inferencia de Audiencia**, los **20 Arquetipos Visuales de Negocio (A - T)**, los **27 Tipos Visuales de Diagramacion**, la **Gramática Editorial de 5 Primitivas (Quad-Cards, Chevrons, Rails, Step Axes, Legends)** y la métrica de **Archetype Fitness**.

---

## 0. Motor de Decision de Audiencia (Audience-Aware Engine)

Sketion adapta autonomamente la seleccion de arquetipos y tipos visuales, la densidad de informacion y el vocabulario segun el perfil del receptor:

| Perfil de Audiencia | Arquetipos Principales | Tipos Visuales Principales | Foco Semantico Obligatorio | Elementos a Suprimir (Evitar Ruido) | Tono Editorial |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CEO / Directivo** | `D (Duelo)`, `B (Fases)`, `P (Cadena Valor)`, `H (Radar 2x2)` | `consultant_2x2`, `it_current_state`, `timeline`, `pyramid_funnel` | ROI, Margen, Coste Fijo $0, Retencion, Fases de Aprobacion | APIs, Microservicios, Codigo, Cronometros de segundos | Estrategico / Financiero |
| **Gerente Operaciones** | `E (Planta/Swimlanes)`, `M (Ishikawa)`, `S (Matriz Takt)`, `K (Kanban)` | `swimlane`, `process`, `gantt`, `dp_security_matrix` | Layout de Planta, Segregacion Fisica, Takt Time, Batching, Roles | Modelos Financieros Macro, Arquitectura Cloud, Nube | Industrial / Planta |
| **Equipo Producto / Tech**| `A (Cerebro)`, `C (Journey 1:1)`, `T (Caja Explotada)`, `N (Galeria)` | `architecture`, `sequence`, `state_machine`, `layer_stack` | Arquitectura Cloud, Microservicios, User Journey, Slots UI, KDS | Negociaciones Laborales, Nomina, Tramites Administrativos | Tecnico / Software |
| **Ingenieria de Datos**| `S (Matriz CRUD)`, `O (Arbol Decision)`, `T (Caja Explotada)` | `medallion`, `data_flow`, `dp_integration`, `er_model` | Multi-tier Storage, Pipelines ETL por Rol, Permisos RBAC | Discursos Comerciales, Planos Fisicos de Edificio | Data Lakehouse / RBAC |
| **Inversionistas / Pitch**| `D (Duelo VS)`, `F (Embudo)`, `I (Flywheel)`, `Q (Pilares)` | `consultant_2x2`, `pyramid_funnel`, `loop_flywheel`, `bar_chart` | Tamano de Mercado, Metricas Heroicas, Traccion, Dolor vs Solucion | Tablas Complejas, Diagramas de Red Detallados | Impacto / Traccion |

---

## 1. Catalogo de los 20 Arquetipos Visuales de Negocio (A - T)

| Código | Arquetipo | Motores Geométricos | Caso de Uso Principal |
| :--- | :--- | :--- | :--- |
| **A** | **El Cerebro** | `Radial` + `Grid` + `Routing` | Plataforma completa en un solo hub central y subsistemas |
| **B** | **Las Fases** | `Grid` + `Routing` + `Banners` | Roadmaps de 90 dias, progresiones con gates de aprobacion |
| **C** | **La Serpiente** | `Flow` (Wave) + `Routing` | Procesos lineales extendidos de 8 a 16 pasos secuenciales |
| **D** | **El Duelo (VS)** | `Grid` + `Sticky` + `Routing` | Antes vs Despues / Legacy caotico vs Arquitectura moderna |
| **E** | **La Cadena / Planta**| `Board` + `Grid` + `Routing` | Swimlanes y Layout de planta fisica con flujos direccionales |
| **F** | **El Embudo (Funnel)** | `Flow` + `Banners` | Conversion de ventas, retencion y pipelines de seleccion |
| **G** | **La Piramide** | `Hierarchy` + `Banners` | Modelos de madurez, capas de seguridad y abstraccion |
| **H** | **El Radar 2x2** | `Grid` + `Routing` | Priorizacion Impacto vs Esfuerzo, clasificacion de riesgos |
| **I** | **El Flywheel** | `Radial` + `Routing` | Bucles virtuosos de crecimiento, retencion y recomendacion |
| **J** | **La Cebolla (Onion)** | `Hierarchy` (Nested) | Clean Architecture, Hexagonal, Gobernanza por contencion |
| **K** | **El Kanban WIP** | `Board` + `Sticky` | Pipelines agiles, colas de trabajo, releases continuos |
| **L** | **El Iceberg** | `Grid` + `Banners` | Deuda tecnica, complejidad backend oculta vs UI superficial |
| **M** | **La Espina (Ishikawa)** | `Hierarchy` + `Routing` | Analisis de causa raiz (Ishikawa), diagnostico y post-mortems |
| **N** | **Galeria 3x3** | `Dashboard` + `Grid` | Catalogo de microfrontends, suite de APIs y componentes |
| **O** | **Arbol de Decision** | `Tree` + `Routing` | Protocolos de escalado, triaje, reglas condicionales |
| **P** | **Cadena de Valor** | `Flow` + `Grid` | Mapeo estrategico de operaciones, proveedores y margen |
| **Q** | **Pilares Benchmark** | `Board` + `Dashboard` | Comparativa cuantitativa de latencia, throughput y costes |
| **R** | **Roadmap con Gates** | `Timeline` + `Banners` | Lanzamientos v4.0, auditorias de seguridad SOC2 / ISO |
| **S** | **Matriz CRUD / Takt**| `Grid` (Proportional) | Mapeo de propiedad de datos o tiempos de ciclo industrial |
| **T** | **Caja Explotada** | `Network` + `Routing` | Desglose del funcionamiento interno de un motor complejo |

---

## 2. Los 5 Patrones Editoriales de Diagram Design (render/excalidraw_builder.py)

1. **Tarjetas de 4 Esquinas (`add_quad_card`):**
   - **Top-Left:** Mini-badge de rol (`EXT`, `STORE`, `ORCH`, `FLOW`, `QUERY`, `BI`, `CUS`, `WHS`).
   - **Top-Right:** Icono vectorial monocromático nítido (`postgres`, `minio`, `airflow`, `redis`, `server`).
   - **Centro:** Título en Sans Bold 14-16px + Subtítulo con metadata técnica (`CDC · SQL · API`).
   - **Bottom:** Mini-pills de tipo de dato o estado (`DB`, `LS`, `FL`, `TB`).
   - **Dimensiones Compactas Anti-Stretch:** Ancho máximo $w \le 340\text{px}$, altura proporcional $h \in [110, 135]\text{px}$.
2. **Cinta Chevron Superior (`add_chevron_ribbon`):**
   - Cinta de etapas concatenadas (`DATA SOURCES` $\rightarrow$ `INGESTION` $\rightarrow$ `STORAGE` $\rightarrow$ `TRANSFORM` $\rightarrow$ `VISUALIZATION`).
3. **Rieles Verticales Laterales (`add_vertical_rails`):**
   - Columnas para aspectos transversales (`ORCHESTRATION`, `SECURITY`, `OBSERVABILITY`).
4. **Eje de Pasos Circulares (`add_step_badge_axis`):**
   - Círculos numerados para workflows y swimlanes (`1 ORDER`, `2 VERIFY`, `3 ALLOCATE`).
5. **Bloque de Leyenda y Filosofía (`add_legend_footer`):**
   - Swatches de color, tipos de flechas y notas editoriales en cursiva (*"One coral. Position is the signal — color reserved for the recommended option."*).

---

## 3. Catalogo Maestro de los 27 Tipos Visuales de Sketion 4.0

### 1. Data Platforms & Lakehouse
* **`medallion`:** Almacenamiento Lakehouse multi-tier (`Raw` $\rightarrow$ `Bronze` $\rightarrow$ `Silver` $\rightarrow$ `Gold` $\rightarrow$ `Archive`).
* **`data_flow`:** Pipeline analitico segregado por roles funcionales (`Data Engineer`, `Data Scientist`, `BI Analyst`).
* **`dp_integration`:** Topologia de fuentes heterogeneas $\rightarrow$ Data Platform Core $\rightarrow$ Consumidores de BI.
* **`dp_security_matrix`:** Matriz de control de acceso RBAC granular con estados Admin, Write, Read, None.
* **`er_model`:** Diagrama entidad-relacion con tipos de datos, claves primarias (PK) y foraneas (FK).

### 2. Estrategia & Consultoria Ejecutiva
* **`consultant_2x2`:** Matriz de escenarios cartesianos con nombres de cuadrantes (Quick Wins, Major Projects, etc.).
* **`quadrant`:** Posicionamiento bidimensional de impacto vs esfuerzo en plano cartesiano.
* **`loop_flywheel`:** Bucle virtuoso continuo con estaciones perimetrales alrededor de un hub central.
* **`it_current_state`:** Diagnostico de silos legados caoticos vs arquitectura destino unificada.
* **`venn`:** Superposicion conceptual y conjuntos intersecados (Deseable x Factible x Viable).
* **`pyramid_funnel`:** Jerarquia piramidal de capas y embudo de conversion con tasas de retencion.

### 3. Software & Arquitectura Cloud
* **`architecture`:** Microservicios distribuidos con boundaries de red, VPCs y gateways.
* **`high_level`:** Stack completo de infraestructura sobre cluster con orquestador superior.
* **`sequence`:** Secuencia temporal de mensajes con lifelines, cajas de activacion y retornos discontinuos.
* **`state_machine`:** Maquina de estados finitos con transiciones y guardas de ciclo de vida.
* **`layer_stack`:** Pila de capas de abstraccion tecnologica estructuradas verticalmente.
* **`nested`:** Jerarquia de contencion fisica y scopes anidados con margenes de seguridad.
* **`flowchart`:** Flujograma de decision logica con nodos de evaluacion y bifurcacion de caminos.

### 4. Procesos & Operaciones
* **`swimlane`:** Flujo de trabajo interdepartamental segregado por carriles funcionales con eje de pasos.
* **`process`:** Flujo secuencial continuo de proceso de negocio con traspasos (handoffs) entre actores.
* **`gantt`:** Cronograma de fases, duraciones, dependencias y puertas de aprobacion (gates).
* **`timeline`:** Eje cronologico con hitos estrategicos alternados arriba y abajo sin colisiones.
* **`org_chart`:** Organigrama jerarquico de propiedad y enrutamiento de equipos.
* **`tree`:** Taxonomia y arbol balanceado de clasificacion jerarquica.

### 5. DataViz Cuantitativo Nativo en Canvas
* **`bar_chart`:** Grafico comparativo de barras cuantitativas con acento focal unico.
* **`line_chart`:** Grafico de lineas continuas y evolucion de tendencias temporales multiserie.
* **`scatter_plot`:** Diagrama de dispersion y correlacion en plano cartesiano.
* **`radar_spider`:** Comparativa multieje poligonal sobre coordenadas radiales concentricas.

---

## 4. Checklist de Calidad Editorial antes de Entregar

- [ ] El archivo tiene extension `.excalidraw` y es JSON valido minificado.
- [ ] Las tarjetas utilizan el patrón Quad-Corner con ancho compacto ($w \le 340\text{px}$).
- [ ] La estructura del diagrama responde a la audiencia objetivo (CEO, Ops, Tech, Devs, Data).
- [ ] Los scopes anchos usan cuadrículas internas en lugar de tarjetas estiradas.
- [ ] Se utilizo la paleta editorial con exactamente 1 acento focal principal (Coral / Pastel Green).
- [ ] Si es un pipeline de datos, incluye la cinta Chevron superior y rieles laterales de seguridad.
- [ ] Si es un proceso/swimlane, incluye el eje superior de pasos circulares numerados.
- [ ] El validador `validate_scene()` devuelve `PASS` con puntuacion global >= 90/100 y `Archetype Fitness` >= 90/100.
