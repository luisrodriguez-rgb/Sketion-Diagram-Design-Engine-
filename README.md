# Sketion Diagram Design Engine (v7.0)

**Motor editorial de diseño y generación de diagramas inteligentes, libres de amontonamientos y 100% editables en formato nativo `.excalidraw`.**

> **Official Core Certification (Sketion Composition Engine 1.0 — FROZEN):**  
> *Sketion Composition Engine 1.0 has demonstrated robust composition selection across a 20-case blind benchmark, achieving 90% exact primary archetype accuracy, 100% acceptable composition accuracy, 100% top-2 recall, and successful adaptation to paraphrased prompts and mutated narrative intent.*

Inspirado en los principios de diseño de **Diagram Design** (densidad visual 4/10, regla del acento único, conectores ortogonales a 90 grados) y construido sobre una **arquitectura desacoplada de Inteligencia de Composición y Renderizado**: `Semantic Model` $\rightarrow$ `Narrative Model Engine` $\rightarrow$ `Oracle Composition Judge` $\rightarrow$ `Adaptive Rendering Engine` $\rightarrow$ `Validation & Repair System`.

---

## ⚡ Instalacion Rapida y Formas de Uso

### Opcion 1: Instalacion en 1 Comando para Agentes y Terminal (Antigravity / Cursor / Windsurf / Claude Code)
Ejecuta en tu terminal para instalar Sketion como Skill Global y habilitar el comando `sketion`:
```bash
curl -fsSL https://raw.githubusercontent.com/luisrodriguez-rgb/Sketion-Diagram-Design-Engine-.git/main/install.sh | bash
```

### Opcion 2: Instalacion como Paquete Python (CLI Global)
```bash
pip install git+https://github.com/luisrodriguez-rgb/Sketion-Diagram-Design-Engine-.git
```
Luego puedes usarlo en cualquier carpeta de tu equipo:
```bash
# Listar los 27 tipos visuales disponibles:
sketion types

# Generar un diagrama de Lakehouse Medallion con acabado Diagram Design:
sketion generate "Arquitectura Lakehouse E-Commerce" --type medallion --output lakehouse.excalidraw --validate

# Validar calidad visual de un archivo existente
sketion validate mi_diagrama.excalidraw

# Ejecutar el benchmark de pruebas adversariales
sketion benchmark
```

### Opcion 3: Uso en el Navegador con Claude.ai o ChatGPT
Si usas Claude en la web (Claude Projects / Custom Instructions) o ChatGPT:
1. Abre el archivo [`CLAUDE_PROJECT_INSTRUCTIONS.md`](CLAUDE_PROJECT_INSTRUCTIONS.md).
2. Copia todo su contenido y pegalo en las **Instrucciones del Proyecto** de Claude o en las **Custom Instructions**.
3. Pidele a Claude: *"Disena un diagrama en formato Excalidraw para [tu problema]"* y te generara el JSON listo para importar en [excalidraw.com](https://excalidraw.com).

---

## 🏛️ Catalogo de los 20 Arquetipos Visuales de Negocio (A - T)

Sketion implementa un catálogo exhaustivo de 20 arquetipos de diseño para resolver cualquier problema de comunicación técnica, estratégica y operativa:

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

## 🎨 Los 5 Patrones Editoriales de Diagram Design

1. **Tarjetas de 4 Esquinas (`Quad-Corner Cards`):**
   * Badge de rol superior izquierdo (`EXT`, `STORE`, `ORCH`, `FLOW`, `BI`).
   * Icono vectorial monocromático superior derecho (`postgres`, `minio`, `redis`, `server`).
   * Título central en Sans Bold 14-16px + Metadata técnica inferior (`CDC · SQL · API`).
   * Límite de ancho compacto ($w \le 340\text{px}$) anti-stretch.
2. **Cinta Chevron Superior (`Pipeline Ribbon`):**
   * Cabecera macro de etapas concatenadas (`DATA SOURCES` $\rightarrow$ `INGESTION` $\rightarrow$ `STORAGE` $\rightarrow$ `TRANSFORM` $\rightarrow$ `VISUALIZATION`).
3. **Rieles Verticales Laterales (`Cross-Cutting Rails`):**
   * Columnas laterales para aspectos transversales (`ORCHESTRATION`, `SECURITY`, `OBSERVABILITY`).
4. **Eje de Pasos Circulares Numerados (`Step Badge Axis`):**
   * Círculos numerados para workflows y swimlanes (`1 ORDER`, `2 VERIFY`, `3 ALLOCATE`).
5. **Bloque de Leyenda y Filosofía (`Legend Footer`):**
   * Fila inferior con swatches de color y notas editoriales en cursiva (*"One coral. Position is the signal — color reserved for the recommended option."*).

---

## 🚫 Regla Inviolable Anti-Monocultivo de Layout (Diversidad Estructural Obligatoria)

En tableros de múltiples marcos (multi-frame), **ningún frame puede repetir la misma disposición columnar ni el mismo patrón geométrico que su marco adyacente** (ej. prohibido encadenar frames con chevrons y 5 columnas de tarjetas). Cada marco **DEBE** derivar su estructura del dominio semántico que representa:

* **Ecosistema / Visión Central / Hub:** **Arquetipo A (El Cerebro / Hub Radial)** con núcleo central y satélites orbitando.
* **Arquitectura Software / Cloud / Infra:** **Arquetipo Layer Stack (Pila Horizontal de Capas)** con VPCs, Gateways y bases de datos.
* **Pipelines / Algoritmos / Lifecycles:** **Arquetipo C (Flow Pipeline)** con bifurcaciones de decisión y bucles de feedback visibles (*Auto-Repair*).
* **Roadmaps / Madurez / Horizontes:** **Arquetipo G (Escalera de Madurez de 5 Niveles)** + Matriz de Horizontes.
* **Comparativa / Antes vs Después:** **Arquetipo D (El Duelo VS)** o **Arquetipo S (Matriz Tabular Proporcional)**.
* **Workshops / Sesión de Discovery:** **Arquetipo Workshop/Miro** con notas adhesivas, mapas de preguntas y cuadrículas interactivas.

---

## 📏 Jerarquia Tipografica Proporcional Universal (Regla Anti-Espacio Vacio)

Para garantizar legibilidad instantánea sin forzar zoom ni dejar tarjetas desiertas:

| Elemento Visual | Rango de Dimensión | Tamaño de Fuente (`fontSize`) |
| :--- | :--- | :---: |
| **Título de Frame / Tablero** | Ancho total ($w \ge 2000\text{px}$) | **28px – 34px Bold** |
| **Subtítulo / Breadcrumb** | Cabecera superior | **13px – 15px Mono** |
| **Tarjeta Amplia / Hero** | $w \ge 380\text{px}$ o $h \ge 115\text{px}$ | **20px Bold** |
| **Tarjeta Estándar** | $w \in [250\text{px}, 380\text{px}]$ | **18px Semi-bold** |
| **Tarjeta Compacta / Nodo** | $w < 250\text{px}$ | **16px Medium** |
| **Subtítulo / Metadata Técnica**| Dentro de tarjeta | **13px – 14px Regular** |
| **Cabecera de Tabla / Matriz** | Columnas de matriz | **14px – 15px Bold** |
| **Celdas de Datos en Tablas** | Celdas de matriz | **13px – 14px Regular** |
| **Badges de Rol (Top-Left)** | Pastillas $h=22\text{px}$ | **11px – 12px Mono** |

---

## 📊 Suite de los 27 Tipos Visuales Específicos

| # | Clave (`--type`) | Nombre Visual | Familia Semantica | Descripcion |
|---|---|---|---|---|
| 01 | `medallion` | Medallion Lakehouse | Data & Storage | Storage multi-tier (`Raw` $\rightarrow$ `Bronze` $\rightarrow$ `Silver` $\rightarrow$ `Gold`) |
| 02 | `data_flow` | Role-Scoped Data Flow | Data & Storage | Pipeline analitico con carriles por rol (`Data Eng`, `Data Sci`, `BI`) |
| 03 | `dp_integration` | Data Platform Integration | Data & Storage | Fuentes heterogeneas $\rightarrow$ Core Platform $\rightarrow$ Consumidores |
| 04 | `dp_security_matrix` | Security Matrix RBAC | Data & Storage | Matriz de control de acceso RBAC granular con permisos |
| 05 | `er_model` | ER / Data Model | Data & Storage | Modelo entidad-relacion tipado con claves PK y FK |
| 06 | `consultant_2x2` | Consultant 2x2 Matrix | Estrategia & Negocio | Matriz de 4 cuadrantes con nombres de celdas y foco hero |
| 07 | `quadrant` | Quadrant Cartesian | Estrategia & Negocio | Posicionamiento de impacto vs esfuerzo en plano cartesiano |
| 08 | `loop_flywheel` | Flywheel Growth Loop | Estrategia & Negocio | Bucle virtuoso continuo con estaciones alrededor de un hub |
| 09 | `it_current_state` | IT Current-State | Estrategia & Negocio | Diagnostico de silos legados caoticos vs plataforma destino |
| 10 | `venn` | Venn Overlap | Estrategia & Negocio | Superposicion conceptual y conjuntos intersecados |
| 11 | `pyramid_funnel` | Pyramid & Funnel | Estrategia & Negocio | Jerarquia piramidal de capas y embudo de conversion |
| 12 | `architecture` | Distributed Architecture | Software & Nube | Microservicios, boundaries de red, VPCs y gateways |
| 13 | `high_level` | High-Level Cluster Stack | Software & Nube | Stack completo de infraestructura con orquestador |
| 14 | `sequence` | Sequence Diagram | Software & Nube | Mensajes cronologicos con lifelines y cajas de activacion |
| 15 | `state_machine` | State Machine | Software & Nube | Maquina de estados finitos y transiciones de ciclo de vida |
| 16 | `layer_stack` | Layer Stack | Software & Nube | Pila de capas de abstraccion tecnologica vertical |
| 17 | `nested` | Nested Scope Hierarchy | Software & Nube | Jerarquia de contencion fisica y scopes anidados |
| 18 | `flowchart` | Logic Decision Flowchart | Software & Nube | Flujograma de decision logica y bifurcacion de caminos |
| 19 | `swimlane` | Cross-Functional Swimlane | Procesos & Operaciones | Carriles horizontales/verticales por departamento |
| 20 | `process` | Sequential Process | Procesos & Operaciones | Proceso secuencial continuo con handoffs entre actores |
| 21 | `gantt` | Gantt Schedule | Procesos & Operaciones | Cronograma de tareas, duraciones y gates de aprobacion |
| 22 | `timeline` | Milestone Timeline | Procesos & Operaciones | Eje cronologico con hitos alternados arriba y abajo |
| 23 | `org_chart` | Org Chart | Procesos & Operaciones | Organigrama jerarquico de propiedad y enrutamiento |
| 24 | `tree` | Hierarchical Tree | Procesos & Operaciones | Taxonomia y arbol balanceado de clasificacion |
| 25 | `bar_chart` | Categorical Bar Chart | DataViz Cuantitativo | Grafico de barras cuantitativas con acento focal |
| 26 | `line_chart` | Time Series Line Chart | DataViz Cuantitativo | Tendencias temporales continuas con series multiples |
| 27 | `scatter_plot` | Distribution Scatter Plot | DataViz Cuantitativo | Dispersion y correlacion en plano cartesiano |

---

## 5. Evaluacion de Calidad y Benchmarks

Sketion incluye un sistema dual de autoevaluacion que garantiza calidad visual mínima de **90/100** y ajuste estructural (*Archetype Fitness*) de **100/100**:

```bash
# Correr la suite de los 27 tipos visuales
python3 tests/test_all_27_types.py

# Correr el benchmark editorial de Diagram Design (Open Data Lake)
python3 tests/render_open_data_lake_benchmark.py

# Correr la suite de los 9 casos adversariales de negocio
python3 sketion_cli.py benchmark
```

* **Structure (100/100):** Vinculacion bidireccional estricta `containerId <-> boundElements`.
* **Layout (100/100):** Espaciado elastico de 95px y gutter de 65px entre scopes.
* **Readability (100/100):** Centrado bidimensional exacto y alturas proporcionales.
* **Hierarchy (100/100):** Regla del acento unico (maximo 1 nodo de color focal).
* **Noise Balance (Densidad ~4.0/10):** Espacio blanco calibrado sin amontonamiento.
* **Tokens (100/100):** Paleta editorial Miro y fuentes Sans/Mono sin colores aleatorios.

---

## Licencia

MIT License © 2026 Luis Rodriguez.
