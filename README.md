# Sketion Diagram Design Engine (v4.0)

**Motor editorial de diseno y generacion de diagramas inteligentes, libres de amontonamientos y 100% editables en formato nativo .excalidraw.**

Inspirado en los principios de diseno de **Diagram Design** (densidad visual 4/10, regla del acento unico, conectores ortogonales a 90 grados) y construido sobre una **arquitectura desacoplada en 4 capas** con **Motor de Inferencia de Audiencia**, **Catálogo Completo de los 27 Tipos Visuales**, **Gramática Editorial de 5 Primitivas (Quad-Cards, Cintas Chevron, Rieles Verticales, Ejes de Pasos, Leyendas Estructuradas)**, **Simetria 1:1 en Journeys**, **Enrutamiento Inter-Zonas** y **Validador de Semantic Hard Constraints & Archetype Fitness**.

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

## 🎨 Los 5 Patrones Editoriales de Diagram Design

1. **Tarjetas de 4 Esquinas (`Quad-Corner Cards`):**
   * Badge de rol superior izquierdo (`EXT`, `STORE`, `ORCH`, `FLOW`, `BI`).
   * Icono vectorial monocromático superior derecho (`postgres`, `minio`, `redis`, `server`).
   * Título central en Sans Bold 14-16px + Metadata técnica inferior.
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

## 🏛️ Catalogo de los 27 Tipos Visuales Soportados

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

## 4. Evaluacion de Calidad y Benchmarks

Sketion incluye un sistema dual de autoevaluacion que garantiza calidad visual mínima de **90/100** y ajuste estructural (*Archetype Fitness*) de **100/100**:

```bash
# Correr la suite de los 27 tipos visuales
python3 tests/test_all_27_types.py

# Correr el benchmark editorial de Diagram Design (Open Data Lake)
python3 tests/render_open_data_lake_benchmark.py
```

---

## Licencia

MIT License © 2026 Luis Rodriguez.
