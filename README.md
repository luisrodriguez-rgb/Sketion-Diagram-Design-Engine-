# Sketion Diagram Design Engine (v3.4)

**Motor editorial de diseno y generacion de diagramas inteligentes, libres de amontonamientos y 100% editables en formato nativo .excalidraw.**

Inspirado en los principios de diseno de **Diagram Design** (densidad visual 4/10, regla del acento unico, conectores ortogonales a 90 grados) y construido sobre una **arquitectura desacoplada en 4 capas** con **Motor de Inferencia de Audiencia**, **20 Arquetipos de Negocio**, **Simetria 1:1 en Journeys**, **Enrutamiento Inter-Zonas** y **Validador de Semantic Hard Constraints**.

---

## ⚡ Instalacion Rapida y Formas de Uso

### Opcion 1: Instalacion en 1 Comando para Agentes y Terminal (Antigravity / Cursor / Windsurf / Claude Code)
Ejecuta en tu terminal para instalar Sketion como Skill Global y habilitar el comando `sketion`:
```bash
curl -fsSL https://raw.githubusercontent.com/luisrodriguez-rgb/Sketion-Diagram-Design-Engine-/main/install.sh | bash
```

### Opcion 2: Instalacion como Paquete Python (CLI Global)
```bash
pip install git+https://github.com/luisrodriguez-rgb/Sketion-Diagram-Design-Engine-.git
```
Luego puedes usarlo en cualquier carpeta de tu equipo:
```bash
# Generar diagrama para el Directorio / CEO
sketion generate "Estrategia de expansion internacional y ROI" --audience ceo --output decision.excalidraw --validate

# Validar calidad visual de un archivo existente
sketion validate mi_diagrama.excalidraw

# Ejecutar el benchmark de 9 pruebas adversariales
sketion benchmark
```

### Opcion 3: Uso en el Navegador con Claude.ai o ChatGPT
Si usas Claude en la web (Claude Projects / Custom Instructions) o ChatGPT:
1. Abre el archivo [`CLAUDE_PROJECT_INSTRUCTIONS.md`](CLAUDE_PROJECT_INSTRUCTIONS.md).
2. Copia todo su contenido y pegalo en las **Instrucciones del Proyecto** de Claude o en las **Custom Instructions**.
3. Pidele a Claude: *"Disena un diagrama en formato Excalidraw para [tu problema]"* y te generara el JSON listo para importar en [excalidraw.com](https://excalidraw.com).

---

## 1. Arquitectura de Dos Niveles: Motores Geometricos y Arquetipos de Negocio

Sketion 3.4 opera mediante una separacion estricta entre la **geometria matematica** y la **composicion editorial de negocio**:

```text
                  PROMPT / REQUISITOS DEL USUARIO
                                |
                                v
+---------------------------------------------------------------+
| MOTOR DE AUDIENCIA: INFERENCIA DE ROL (engines/audience.py)   |
| (CEO_BOARD, OPERATIONS, PRODUCT_TECH, DEV_DOCS, INVESTOR_PITCH)|
+-------------------------------+-------------------------------+
                                |
                                v
+---------------------------------------------------------------+
| CAPA EDITORIAL: 20 ARQUETIPOS DE COMPOSICION VISUAL (A - T)   |
| (El Duelo, Las Fases, El Cerebro, La Serpiente, La Cebolla...) |
+-------------------------------+-------------------------------+
                                |
                                v
+---------------------------------------------------------------+
| CAPA GEOMETRICA: 9 MOTORES DE LAYOUT BASE (layout/ & engines/)|
| (flow.py, hierarchy.py, grid.py, routing.py, network, etc.)   |
+-------------------------------+-------------------------------+
                                |
                                v
+---------------------------------------------------------------+
| CAPA DE RENDER: PRIMITIVAS NATIVAS Y TOKENS (render/)         |
| (containerId <-> boundElements, stickies rotados, banners)    |
+-------------------------------+-------------------------------+
                                |
                                v
+---------------------------------------------------------------+
| CAPA DE AUDITORIA: SEMANTIC HARD CONSTRAINTS (validation/)    |
| (Fidelidad semantica inmutable, densidad 4/10, auto-repair)   |
+-------------------------------+-------------------------------+
                                |
                    ARCHIVO .excalidraw NATIVO
```

---

## 2. Los 9 Motores Geometricos Base (Algoritmos de Layout)

Ubicados en `layout/` y `engines/recipes.py`, constituyen la infraestructura computacional de posicionamiento:

| Motor Base | Archivo / Modulo | Algoritmo Geometrico | Responsabilidad Matematica |
| :--- | :--- | :--- | :--- |
| **Flow** | `layout/flow.py` | Distribucion secuencial horizontal y sinusoidal | Calcula coordenadas continuas con espaciado elastico (95px) para conectores y pastillas. |
| **Journey 1:1** | `layout/flow.py` | Simetria vertical estricta | Empareja exactamente N pasos superiores con N slots de captura inferiores. |
| **Timeline** | `layout/flow.py` | Eje cronologico alternado | Distribuye hitos temporales arriba y abajo de un eje central sin colision de texto. |
| **Tree** | `layout/hierarchy.py`| Arbol jerarquico balanceado | Posiciona nodos padres e hijos en multiples niveles calculando anchos de sub-arbol. |
| **Radial** | `layout/hierarchy.py`| Distribucion perimetral angular | Calcula radios y angulos equidistantes alrededor de un nodo o hub central. |
| **Grid / Matrix** | `layout/grid.py` | Grilla tabular bidimensional proporcional | Calcula anchos de columna dinamicos segun longitud de texto (hasta 560px) y alturas de fila por lineas reales. |
| **Board / Lanes** | `layout/grid.py` | Carriles verticales paralelos (Kanban) | Gestiona columnas de ancho uniforme y apilamiento vertical de tarjetas. |
| **Dashboard** | `layout/grid.py` | Matriz de chips numericos | Distribuye tarjetas de KPI en grillas de 2, 3 o 4 columnas con proporciones fijas. |
| **Network / Red** | `engines/recipes.py` | Grafo distribuido con Scopes | Agrupa nodos por columnas de infraestructura aplicando gutter de 65px entre contenedores. |
| **Routing** | `layout/routing.py` | Enrutamiento ortogonal y Flujo Inter-Zonas | Genera codos a 90 grados, anclajes de salida en saltos de columna y conectores de transito fisico. |

---

## 3. Catalogo Maestro de los 20 Arquetipos Visuales (A a T)

| Codigo | Nombre del Arquetipo | Motores Base Utilizados | Caso de Uso Principal |
| :--- | :--- | :--- | :--- |
| **A** | **El Cerebro** | `Radial` + `Grid` + `Routing` | Plataforma completa en un solo hub central |
| **B** | **Las Fases** | `Grid` + `Routing` + `Banners` | Roadmaps de 90 dias, progresiones con gates |
| **C** | **La Serpiente** | `Flow` (Wave) + `Routing` | Procesos lineales de 8 a 16 pasos |
| **D** | **El Duelo (VS)** | `Grid` + `Sticky` + `Routing` | Antes vs Despues / Legacy vs Moderno |
| **E** | **La Cadena / Planta**| `Board` + `Grid` + `Routing` | Swimlanes y Layout de planta con flujos direccionales |
| **F** | **El Embudo (Funnel)** | `Flow` + `Banners` | Conversion de ventas, pipelines de seleccion |
| **G** | **La Piramide** | `Hierarchy` + `Banners` | Modelos de madurez, capas de seguridad |
| **H** | **El Radar 2x2** | `Grid` + `Routing` | Priorizacion Impacto vs Esfuerzo, riesgos |
| **I** | **El Flywheel** | `Radial` + `Routing` | Bucles de crecimiento y retencion |
| **J** | **La Cebolla (Onion)** | `Hierarchy` (Nested) | Clean Architecture, Hexagonal, Gobernanza |
| **K** | **El Kanban WIP** | `Board` + `Sticky` | Pipelines agiles, colas de trabajo, releases |
| **L** | **El Iceberg** | `Grid` + `Banners` | Deuda tecnica, complejidad backend vs UI |
| **M** | **La Espina (Ishikawa)** | `Hierarchy` + `Routing` | Analisis de causa raiz (Ishikawa), post-mortems |
| **N** | **Galeria 3x3** | `Dashboard` + `Grid` | Catalogo de microfrontends, suite de APIs |
| **O** | **Arbol de Decision** | `Tree` + `Routing` | Protocolos de escalado, triaje, reglas |
| **P** | **Cadena de Valor** | `Flow` + `Grid` | Mapeo estrategico de operaciones y margen |
| **Q** | **Pilares Benchmark** | `Board` + `Dashboard` | Comparativa de latencia, throughput y costes |
| **R** | **Roadmap con Gates** | `Timeline` + `Banners` | Lanzamientos v3.0, auditorias SOC2 / ISO |
| **S** | **Matriz CRUD / Takt**| `Grid` (Proportional) | Mapeo de propiedad de datos o tiempos de ciclo industrial |
| **T** | **Caja Explotada** | `Network` + `Routing` | Explicar el funcionamiento interno de un motor |

---

## 4. Evaluacion de Calidad y Benchmarks

Sketion incluye un sistema de autoevaluacion de 6 dimensiones que garantiza calidad editorial minima de **95/100**:

```bash
# Correr la suite de 9 casos adversariales automatizados
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
