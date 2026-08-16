---
name: sketion-diagram-design
description: Motor editorial de diseño y generación de diagramas inteligentes, libres de amontonamientos y 100% editables en formato nativo .excalidraw (v8.0). Arquitectura desacoplada en 5 capas: Semantic Model -> Narrative Model Engine -> Oracle Composition Judge (FROZEN 1.0) -> Information Architecture Engine (Importance Ranking & Progressive Disclosure) -> Adaptive Rendering Engine (AnchorGeometry, Orthogonal 90 Router, Adaptive Multi-Frame, Render Fidelity >=95/100, Layout Stability Var 0.0) -> Validation & Repair System.
license: MIT
metadata:
  version: "8.0"
---

# Sketion Diagram Design Skill (Motor Editorial para Excalidraw v8.0)

Crea tableros y diagramas profesionales con calidad editorial, diseño limpio, cero amontonamientos, tipografía proporcional legible a primera vista, **estricta diversidad de arquetipos visuales**, gestión de cargas masivas (50+ entidades) con **Progressive Disclosure** y editabilidad nativa total en formato `.excalidraw`.

---

## 🏛️ Arquitectura del Sistema Sketion (5 Capas Certificadas)

```text
                 USER PROMPT / RAW SPEC
                           │
                           ▼
                 ┌───────────────────┐
                 │ 1. SEMANTIC MODEL │  Audience Inference & Semantic Text Decomposer
                 └─────────┬─────────┘
                           ▼
                 ┌───────────────────┐
                 │ 2. NARRATIVE CORE │  Narrative Model (Intent & Primary Question)
                 └─────────┬─────────┘  Oracle Composition Judge (Top-2 Recall 100%, Regret 0.00)
                           ▼
                 ┌───────────────────┐
                 │ 3. INFO ARCH (IA) │  Importance Ranking (Hero, Primary, Secondary, Metadata, Appendix)
                 └─────────┬─────────┘  Progressive Disclosure & Cognitive Load Management
                           ▼
                 ┌───────────────────┐
                 │ 4. RENDERING CORE │  Adaptive Multi-Frame Reflow (Single, Dual, Triple Narrative)
                 └─────────┬─────────┘  Polymorphic AnchorGeometry & 90° Orthogonal Router
                           ▼
                 ┌───────────────────┐
                 │ 5. QUALITY & AUDIT│  Render Fidelity (>=95/100) · Preservation (97/100)
                 └───────────────────┘  Layout Stability (Var 0.0) · Effective Density Calibrated
```

---

## 🚫 Regla Inviolable Anti-Monocultivo de Layout (Diversidad Estructural Obligatoria)

> [!CAUTION]
> **PROHIBICIÓN ESTRICTA DE CLONAR PLANTILLAS:** En tableros de múltiples marcos (multi-frame), **ningún frame puede repetir la misma disposición columnar ni el mismo patrón geométrico que su marco adyacente** (ej. prohibido encadenar frames con chevrons y 5 columnas de tarjetas).
> Cada marco **DEBE** derivar su estructura del dominio semántico que representa:

```text
┌───────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ DOMINIO SEMÁNTICO                     │ ARQUETIPO GEOMÉTRICO OBLIGATORIO                       │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Ecosistema / Visión Central / Hub     │ Arquetipo A: El Cerebro (Hub Radial con Satélites)     │
│ Arquitectura Software / Cloud / Infra │ Arquetipo Layer Stack: Pila Horizontal de 4 Capas      │
│ Pipelines / Algoritmos / Lifecycles   │ Arquetipo C: Flow con Bucle de Feedback Visible        │
│ Roadmaps / Madurez / Horizontes       │ Arquetipo G: Escalera de 5 Niveles + Matriz Horizontes │
│ Comparativa / Antes vs Después        │ Arquetipo D: El Duelo (Contraste Fricción vs Control)  │
│ Matriz de Capacidades / Competencia   │ Arquetipo S: Matriz Tabular Proporcional               │
│ Triaje Condicional / Reglas           │ Arquetipo O: Árbol de Decisión                         │
│ Causa-Raíz / Diagnóstico de Fallos    │ Arquetipo M: La Espina (Ishikawa)                      │
│ Cadena de Suministro / Logística      │ Arquetipo P: Cadena de Valor & Supply Chain            │
│ Workshops / Sesión de Discovery       │ Arquetipo Workshop: Post-its, Checklist & Preguntas    │
└───────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 0. Motor de Arquitectura de Información (IA & Progressive Disclosure)

Ante cargas de información complejas o masivas (15 a 50+ entidades), el motor aplica **Tiers de Importancia**:
* **`HERO` (1 por marco):** Protagonista exclusivo con color de acento dominante.
* **`PRIMARY` (3 - 6 por marco):** Componentes del flujo central en tarjetas estructuradas con fuentes 18-20px.
* **`SECONDARY` (Soporte):** Componentes auxiliares y conectores de paso.
* **`METADATA` (Pills):** SLAs, latencias y métricas numéricas convertidas en badges superiores compactos.
* **`APPENDIX` (Callouts):** Circuit breakers, warnings y fallbacks aislados en notas laterales para no sobrecargar el flujo.

---

## 1. Catálogo de los 20 Arquetipos Visuales de Negocio (A - T)

| Código | Arquetipo | Motores Geométricos | Caso de Uso Principal |
| :--- | :--- | :--- | :--- |
| **A** | **El Cerebro** | `Radial` + `Grid` + `Routing` | Plataforma completa en un solo hub central y subsistemas |
| **B** | **Las Fases** | `Grid` + `Routing` + `Banners` | Roadmaps de 90 dias, progresiones con gates de aprobacion |
| **C** | **La Serpiente** | `Flow` (Wave) + `Routing` | Procesos lineales extendidos y pipelines con bucles |
| **D** | **El Duelo (VS)** | `Grid` + `Sticky` + `Routing` | Antes vs Después / Legacy caótico vs Arquitectura moderna |
| **E** | **La Cadena / Swimlanes**| `Board` + `Grid` + `Routing` | Swimlanes de roles y flujos coordinados entre actores |
| **F** | **El Embudo (Funnel)** | `Flow` + `Banners` | Conversión de ventas, retención y pipelines de selección |
| **G** | **La Pirámide** | `Hierarchy` + `Banners` | Modelos de madurez, capas de seguridad y abstracción |
| **H** | **El Radar 2x2** | `Grid` + `Routing` | Priorización Impacto vs Esfuerzo, clasificación de riesgos |
| **I** | **El Flywheel** | `Radial` + `Routing` | Bucles virtuosos de crecimiento, retención y recomendacion |
| **J** | **La Cebolla (Onion)** | `Hierarchy` (Nested) | Clean Architecture, Hexagonal, Gobernanza por contención |
| **K** | **El Kanban WIP** | `Board` + `Sticky` | Pipelines ágiles, colas de trabajo, releases continuos |
| **L** | **El Iceberg** | `Grid` + `Banners` | Deuda técnica, complejidad backend oculta vs UI superficial |
| **M** | **La Espina (Ishikawa)** | `Hierarchy` + `Routing` | Análisis de causa raíz (Ishikawa), diagnóstico y post-mortems |
| **N** | **Galería 3x3** | `Dashboard` + `Grid` | Catálogo de microfrontends, suite de APIs y componentes |
| **O** | **Árbol de Decisión** | `Tree` + `Routing` | Protocolos de escalado, triaje, reglas condicionales |
| **P** | **Cadena de Valor** | `Flow` + `Grid` | Mapeo estratégico de operaciones, proveedores y margen |
| **Q** | **Pilares Benchmark** | `Board` + `Dashboard` | Comparativa cuantitativa de latencia, throughput y costes |
| **R** | **Roadmap con Gates** | `Timeline` + `Banners` | Lanzamientos v4.0, auditorías de seguridad SOC2 / ISO |
| **S** | **Matriz CRUD / Takt**| `Grid` (Proportional) | Mapeo de propiedad de datos o tiempos de ciclo industrial |
| **T** | **Caja Explotada** | `Network` + `Routing` | Desglose del funcionamiento interno de un motor complejo |

---

## 2. Jerarquía Tipográfica Proporcional Universal

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

## 3. Checklist de Calidad Editorial antes de Entregar

- [ ] El archivo tiene extensión `.excalidraw` y es JSON válido.
- [ ] **Diversidad de Arquetipos:** Cada frame usa un arquetipo diferente (Hub Radial, Stack Horizontal, Flow con Bucle, Escalera, etc.). Cero clones de 5 columnas.
- [ ] La tipografía de las tarjetas utiliza **18-20px Bold** para el título y **13-14px** para el subtítulo, llenando armónicamente el espacio interior.
- [ ] **AnchorGeometry Activo:** Las flechas tocan con precisión milimétrica los bordes perimetrales de rectángulos, diamantes y círculos.
- [ ] **Enrutamiento Ortogonal:** Conectores con quiebres limpios a 90° sin colisiones sobre cajas intermedias.
- [ ] **Progressive Disclosure:** Máximo 6 tarjetas primarias por marco; métricas aisladas en pills y excepciones en callouts.
- [ ] Se utilizó la paleta editorial con exactamente 1 acento focal principal por marco.
- [ ] El validador `validate_scene()` devuelve `PASS` con puntuación global >= 90/100, `Render Fidelity` >= 90/100 y `RDS = 0`.
