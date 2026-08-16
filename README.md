# Sketion Diagram Design Engine 🎨📐

**Motor editorial de diseño y generación de diagramas inteligentes y 100% editables en formato nativo `.excalidraw`.**

Inspirado en los principios de diseño de **Diagram Design** (densidad 4/10, regla del acento único, conectores ortogonales a 90º) y construido sobre una **arquitectura desacoplada en 4 capas** con auditoría de **Fidelidad Semántica**, **Calidad Visual** y **Bucle de Auto-Corrección**.

---

## 🌟 ¿Por qué Sketion?

La mayoría de herramientas de IA generan diagramas como imágenes estáticas (SVG/PNG) o producen "sopas de cajas redondeadas" sin criterio visual ni jerarquía.

**Sketion resuelve ambos problemas:**
1. **Calidad Editorial Estricta:** Aplica un sistema de tokens de diseño (`PAPER`, `INK`, `ACCENT`), evita decoraciones innecesarias ("AI slop") y enruta flechas con codos ortogonales limpios.
2. **Editabilidad Nativa Total:** Genera archivos `.excalidraw` válidos v2, con texto estrictamente vinculado a contenedores (`containerId` $\leftrightarrow$ `boundElements`) y serialización JSON minificada.
3. **Evaluación de Fidelidad y Auto-Corrección:** El motor evalúa tanto la estética visual como la fidelidad con respecto a la intención del usuario, auto-reparando desviaciones antes de entregar el archivo.

---

## 🏛️ Arquitectura Desacoplada en 4 Capas

```text
                  PROMPT / IDEA DEL USUARIO
                             ↓
       ┌───────────────────────────────────────────┐
       │ 1. MODELO SEMÁNTICO (semantic/)           │
       │    • Representación intermedia tipada     │
       │    • Scopes / Zonas de infraestructura    │
       │    • 3 Niveles de Detalle (Simple/Bal/Det)│
       └─────────────────────┬─────────────────────┘
                             ↓
       ┌───────────────────────────────────────────┐
       │ 2. MOTOR DE LAYOUT (layout/)              │
       │    • flow.py / hierarchy.py / grid.py      │
       │    • routing.py (Codos ortogonales a 90º) │
       └─────────────────────┬─────────────────────┘
                             ↓
       ┌───────────────────────────────────────────┐
       │ 3. RENDER EXCALIDRAW (render/)            │
       │    • Primitivas nativas (cajas, textos)   │
       │    • Vinculación bidireccional estricta   │
       │    • JSON minificado sin indentación      │
       └─────────────────────┬─────────────────────┘
                             ↓
       ┌───────────────────────────────────────────┐
       │ 4. QUALITY VALIDATOR & REPAIR (validation)│
       │    • Visual Quality Score (Densidad 4/10) │
       │    • Semantic Fidelity Score (Coverage)   │
       │    • Self-Correction Loop (Repair Engine) │
       └─────────────────────┬─────────────────────┘
                             ↓
                ARCHIVO .excalidraw 100% EDITABLE
```

---

## 📊 Los 9 Motores Visuales Base (27 Tipos Semánticos)

| Motor | Estructura Visual | Tipos de Diagrama Soportados |
| :--- | :--- | :--- |
| **Cerebro** | Hub elíptico central + ramas radiales | Concept Hub, Persona Ideal, Sitemap central, Loop / Flywheel, Venn |
| **Flujo** | Secuencia horizontal con flechas | Flowcharts, Pipelines de Datos, User Journey, Funnels, Sequence |
| **Red** | Nodos distribuidos en zonas / scopes | Arquitectura Cloud, Microservicios, State Machines, High-Level |
| **Matriz** | Grilla con cabeceras de fila y columna | Comparativas, SWOT, Cuadrante 2x2, Matriz de Permisos / Seguridad |
| **Árbol** | Jerarquía descendente (Nivel 1 $\rightarrow$ 2) | Org Charts, Taxonomías, Sitemaps multinivel, Árboles de Decisión |
| **Timeline** | Eje horizontal continuo con hitos | Roadmaps de Producto, Cronogramas de Release, Gantt |
| **Board** | Carriles verticales con Post-It headers | Kanban, Swimlanes, IT Current-State, Categorización |
| **Dashboard** | Chips oscuros con números gigantes | KPIs de Negocio, Métricas de Rendimiento, Conteos |
| **Storyboard**| Frames 1600×900 secuenciales | Pitch Decks, Presentaciones ejecutivas, Diapositivas |

---

## 🎨 Sistema de Diseño y Tokens Semánticos

Todas las decisiones visuales se rigen por [references/style-guide.md](references/style-guide.md):

* **`PAPER` (`#FFFFFF`):** Fondo del canvas.
* **`PAPER_CARD` (`#FFFFFF`):** Fondo de tarjetas de componentes.
* **`PAPER_CONTAINER` (`#F8FAFC`):** Fondo tenue de Scopes / Zonas.
* **`INK` (`#0F172A`):** Tinta principal para títulos, bordes y texto.
* **`MUTED` (`#64748B`):** Conectores secundarios y subetiquetas mono.
* **`RULE` (`#CBD5E1`):** Líneas divisorias y bordes de zonas.
* **`ACCENT` (`#2563EB`):** Color focal reservado para **1 o 2 nodos héroe**.
* **`PAIN` (`#EF4444`):** Alertas, riesgos y cuellos de botella.

### Paletas Predefinidas
1. **Jet Editorial (Default):** Cobalto focal + tinta oscura (Arquitectura, Sistemas, APIs).
2. **Miro Nico:** Amarillo post-it + rosa suave (Discovery, Workshops, Brainstorming).
3. **El Sabio:** Dorado cálido + terracota (Estrategia de Negocio, Comparativas de Marca).

---

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/sketion-diagram-design.git
cd sketion-diagram-design
```

### 2. Estructura de Carpetas
```text
.
├── SKILL.md                  # Orquestador del skill para agentes (Claude, Gemini, Pi)
├── references/               # Guías normativas de estilo, semántica y layout
│   ├── style-guide.md
│   ├── semantic-patterns.md
│   ├── types-catalog.md
│   ├── layout-rules.md
│   └── quality-rules.md
├── semantic/                 # Modelos de datos tipados (JSON intermedio)
├── layout/                   # Cálculo espacial puro y enrutamiento ortogonal
├── render/                   # Constructor de primitivas Excalidraw y JSON minificado
├── repair/                   # Motor de auto-corrección desacoplado
├── validation/               # Calidad visual, fidelidad semántica y validator
└── tests/                    # Fixtures y suites de pruebas automatizadas
```

---

## 💻 Ejemplo de Uso en Python

### Generar una Arquitectura con Scopes y Doble Jerarquía
```python
from render.excalidraw_builder import ExcalidrawScene
from engines.recipes import engine_red, DEFAULT_PALETTE
from validation.validator import validate_scene

# 1. Crear escena
scene = ExcalidrawScene(roughness=0, bg_color="#ffffff")

# 2. Definir Zonas / Scopes
scopes = [
    {"id": "edge", "label": "EDGE LAYER", "rel_x": 30, "rel_y": 80, "w": 280, "h": 450},
    {"id": "core", "label": "CORE SERVICES", "rel_x": 340, "rel_y": 80, "w": 380, "h": 450}
]

# 3. Definir Nodos con Doble Jerarquía (Title + Sublabel Mono)
nodes = [
    {"id": "web", "label": "Web App", "sublabel": "Next.js 14", "metadata": ":3000", "rel_x": 50, "rel_y": 140},
    {"id": "api", "label": "API Gateway", "sublabel": "FastAPI Core", "metadata": ":8000", "is_hero": True, "rel_x": 380, "rel_y": 200}
]

edges = [
    {"from": "web", "to": "api", "label": "HTTPS / JSON"}
]

# 4. Renderizar con el motor RED
engine_red(scene, "Arquitectura SaaS", nodes, edges, scopes=scopes, palette=DEFAULT_PALETTE)

# 5. Validar y Auto-Corregir
scene_data, report = validate_scene(scene.to_dict(), auto_repair=True)
print(report.summary())

# 6. Guardar archivo .excalidraw minificado
scene.save("arquitectura_saas.excalidraw")
```

---

## 🧪 Pruebas de Regresión y Stress Testing

El repositorio incluye suites completas de pruebas automatizadas:

```bash
# Ejecutar suite de regresión con fixtures canónicos
python3 tests/test_visual_regression.py

# Ejecutar suite de stress testing (alta densidad, sobrecarga de acentos)
python3 tests/test_stress.py
```

### Reporte de Salida Típico
```text
==================================================
=== SKETION COMPREHENSIVE REPORT: ✅ PASS ===
==================================================
Elementos totales: 30 | Frames: 1
PUNTUACIÓN GLOBAL SKETION: 99/100

VISUAL QUALITY SCORE
─────────────────────────────────
Structure (Técnica Excalidraw) : 100/100
Layout (Espaciado & Gaps)      : 95/100
Readability (Legibilidad)      : 100/100
Hierarchy (1 Acento / Focos)   : 100/100
Visual Noise (Densidad: 3.6/10) : 100/100
Brand Consistency (Tokens)     : 100/100
─────────────────────────────────
OVERALL VISUAL QUALITY         : 99/100

SEMANTIC FIDELITY SCORE
─────────────────────────────────
Node Coverage        : 100/100
Edge Coverage        : 100/100
Scope Coverage       : 100/100
Hierarchy Fidelity   : 100/100
─────────────────────────────────
OVERALL FIDELITY     : 100/100
```

---

## 📜 Licencia

MIT License — Creado como base para el ecosistema visual de **Sketion** e inspirado en la filosofía editorial de **Diagram Design**.
