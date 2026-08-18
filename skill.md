---
name: sketion-diagram-design
description: Motor empresarial autónomo de composición visual para diagramas de arquitectura de software, infraestructura, sistemas complejos, negocios y estrategia (v11.0 GA). Arquitectura desacoplada: Semantic Model -> Content Model -> Visual Composition Engine (20 Patrones) -> Diversity Judge (VDS Multidimensional) -> Declarative Layout Solver (Multi-Algoritmo) -> Manhattan A* Connector Router con Puertos Magnéticos -> Theme & Style Engine (8 Estilos + Style Lock) -> Iconografía Vectorial Pura (155+ iconos, 0 emojis) -> Narrative & Presentation Composer -> Exportación Multiformato (.excalidraw & .svg).
license: MIT
metadata:
  version: "11.0"
---

# Sketion Visual Composition Engine (v11.0 GA)

Sketion es el motor de composición visual autónomo para diseñar diagramas de arquitectura de software, sistemas complejos, procesos de ingeniería y estrategias corporativas en formato `.excalidraw` y `.svg` vectorial puro, con **0 emojis**, enrutamiento Manhattan A* sin colisiones, 20 patrones de composición estructurales y 8 temas semánticos con *Style Lock*.

---

## 🏛️ Pipeline de Generación Sketion 11.0

```text
USER PROMPT
    ↓
SEMANTIC ENGINE (Interpreta entidades y roles)
    ↓
CONTENT MODEL (Estructura de datos tipada intermedia)
    ↓
COMPOSITION ENGINE (20 Patrones: Layered, Radial, Tree, Matrix, Timeline, etc.)
    ↓
DIVERSITY JUDGE (Score VDS contextual: fit semántico, jerarquía, balance)
    ↓
LAYOUT SOLVER (Multi-algoritmo: Sugiyama, Radial, Matrix, Swimlane, Tree)
    ↓
CONNECTOR ROUTER (Manhattan A* con minimización de cruces y puertos magnéticos)
    ↓
THEME & STYLE ENGINE (8 Estilos semánticos + Style Lock multi-board)
    ↓
VALIDATOR & REPAIR (Auditoría de geometría, 0 emojis y VCS >= 99)
    ↓
EXCALIDRAW & SVG VECTORIAL BUILDER
```

---

## 🚀 Uso Rápido en Python

### 1. Generación Declarativa con `LayoutSolver` (Sin Coordenadas Fijas)

```python
import sketion
from sketion import LayoutSolver, LayoutAlgorithm, ExcalidrawScene, ThemeEngine, VisualStyleType

# 1. Crear el solver con el algoritmo deseado
solver = LayoutSolver(algorithm=LayoutAlgorithm.HIERARCHICAL, direction="LR")

# 2. Declarar nodos
n_client = solver.add_node("client", "Web Client Portal", role="actor", shape="actor", layer_index=0)
n_waf = solver.add_node("waf", "Cloudflare WAF", role="security", shape="security", layer_index=1)
n_core = solver.add_node("core", "Payment Orchestrator", role="service", shape="card", layer_index=2, is_hero=True)
n_db = solver.add_node("db", "Aurora PostgreSQL", role="database", shape="database", layer_index=3)

# 3. Declarar conexiones
solver.connect("client", "waf", label="HTTPS / TLS 1.3")
solver.connect("waf", "core", label="mTLS Ingress")
solver.connect("core", "db", label="SQL / Port 5432", relation_type="critical")

# 4. Renderizar a escena
scene = ExcalidrawScene()
fid = scene.add_frame("Fintech Settlement Core", 0, 0, 1440, 900)
solver.render_to_scene(scene, frame_id=fid)

# 5. Exportar
scene.export_svg("architecture.svg")
scene.export_excalidraw("architecture.excalidraw")
```

### 2. Composición Narrativa de Presentación con `NarrativeComposer`

```python
from sketion import NarrativeComposer, ExcalidrawScene, VisualStyleType

# Crear historia técnica de 6 fases
board = NarrativeComposer.create_standard_story("Modernización de Arquitectura Cloud", domain="software")

scene = ExcalidrawScene()
# Vista Tablero Deep-Dive (un solo lienzo conectado)
NarrativeComposer.render_deep_dive_board(board, scene, style=VisualStyleType.EDITORIAL)

# O Vista Presentación (Slides coordinadas con StyleLock)
# NarrativeComposer.render_presentation_slides(board, scene, style=VisualStyleType.EXECUTIVE)

scene.export_svg("narrative_board.svg")
```

---

## 🎨 8 Estilos Visuales Desacoplados

1. **`editorial`:** Mucho espacio negativo, blanco/negro/terracota (`#D93829`), tipografía Inter fuerte.
2. **`technical`:** Azul/cyan/slate/verde, cuadrícula marcada y conectores en azul cobalto (`#2563EB`).
3. **`executive`:** Minimalista, slate oscuro, acento único terracota, alto contraste corporativo.
4. **`blueprint`:** Fondo azul marino (`#0B2545`), líneas blancas técnicas y acentos cian/verde flúor.
5. **`academic`:** Jerárquico, escala de grises sobria y pasteles discretos para papers y tesis.
6. **`workshop`:** Notas adhesivas amarillas/rosas, agrupaciones orgánicas de ideación ágil.
7. **`data_dense`:** Gauges, métricas KPI, tablas y distribuciones de alta densidad.
8. **`minimal`:** Líneas finas, máximo espacio libre y cero elementos decorativos.

---

## 📐 20 Patrones de Composición Estructural & Catálogo Visual

`layered_architecture`, `radial_hub`, `hierarchical_tree`, `pipeline_flow`, `matrix_2x2`, `swimlane_process`, `dual_split`, `timeline_roadmap`, `cornell_notes`, `a3_report`, `kanban_board`, `radar_spider`, `hexagonal_ports`, `k8s_topology`, `uml_class_model`, `service_blueprint`, `funnel_conversion`, `data_lakehouse`, `security_barrier`, `narrative_board`.

---

## 🧠 Guía de Selección Topológica Inteligente (Anti-Monotonía & Alta Fidelidad)

El motor Sketion NO debe recaer por defecto en el patrón genérico de capas horizontales ("sandwich"). Debe analizar la naturaleza semántica del problema y seleccionar la morfología visual que mejor comunica el modelo mental del dominio:

1. **Plataformas Distribuidas & Omnicanal (e.g., Banca, Fintech, Telecom):**
   - **Topología:** *Multi-Zone Decoupled Fabric (3 Columnas Funcionales)*.
   - **Columna 1:** Perímetro Transaccional Síncrono (Canales -> Edge WAF -> Gateway -> Core ACID DB).
   - **Columna 2:** Event Mesh & Prevención en Tiempo Real (Kafka -> ML Inferencia <50ms -> Workers).
   - **Columna 3:** Adaptación Legacy & Analítica (ACL -> Mainframe Host AS/400 + Lakehouse S3 -> Snowflake BI).
   - **Regla:** Ruteo ortogonal claro; nunca cruzar flechas diagonales sobre tarjetas intermedias.

2. **Diagnósticos Operacionales, Manufactura & TOC (e.g., Lean, VSM, Cuellos de Botella):**
   - **Topología:** *A3 Problem-Solving Dashboard*.
   - **Zona Superior:** Value Stream Map (VSM) completo con **todas las estaciones de proceso secuenciales** (e.g., Corte -> Mecanizado -> Ensamblaje -> Inspección -> Empaque) y buffers WIP intermedios destacados + canal inferior para bucles de retrabajo.
   - **Zona Inferior Izquierda:** Tabla Cuantitativa de Balance de Línea (Capacidad Teórica vs Real, Gaps y Ley de Little).
   - **Zona Inferior Derecha:** Matriz de Decisión Priorizada (SMED, Poka-Yoke, Heijunka, Asignación de Operadores).

3. **Ecosistemas de IA Empresarial, GenAI & Agentes Autónomos:**
   - **Topología:** *Split Runtime Loop + Continuous Quality Flywheel*.
   - **Lienzo Izquierdo (60%):** Pipeline de Ejecución en Vivo (Canales -> SSO -> DLP Guardrail -> SLM Router -> Orquestador -> 3 Rutas Especializadas [RAG / Text-to-SQL / Action HITL] -> Model Gateway -> LLMs -> Trazabilidad Inmutable).
   - **Lienzo Derecho (40%):** Ciclo de Evaluación Continua & Gobernanza (Golden Dataset -> Automated Evals -> CI/CD Quality Gatekeeper con bloqueo automático -> Observabilidad Langfuse -> Matriz de 4 Equipos).

4. **Reglas Geométricas Inmutables:**
   - **Cilindros de Base de Datos:** Mantener anchos estándar (180px–280px) con tapa elíptica proporcional (`cap_h = min(20.0, max(12.0, h * 0.14))`) para evitar el efecto de platillo aplastado.
   - **Textos y Etiquetas:** Las etiquetas de conectores deben tener su propio espacio de canal libre; NUNCA estampar texto flotante sobre títulos o bordes de cajas.
   - **Completitud de Nodos:** Nunca truncar o colapsar estaciones del proceso por restricciones de ancho; adaptar los anchos (`w=150..170px`) para dar cabida a todo el flujo.

