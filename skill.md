---
name: sketion-diagram-design
description: Motor editorial de diseño y generación de diagramas inteligentes, libres de amontonamientos y 100% editables en formato nativo .excalidraw (v8.0). Arquitectura desacoplada en 5 capas: Semantic Model -> Narrative Model Engine -> Oracle Composition Judge (FROZEN 1.0) -> Information Architecture Engine (Importance Ranking & Progressive Disclosure) -> Adaptive Rendering Engine (AnchorGeometry, Orthogonal 90 Router, Adaptive Multi-Frame, Frame Containment, Spatial Collision Avoidance, Render Fidelity >=90/100, Layout Stability Var 0.0) -> Validation & Multi-Layer Repair System (Bindings, Text, Frames, Spatial, Accents).
license: MIT
metadata:
  version: "8.0"
---

# Sketion Diagram Design Skill (Motor Editorial para Excalidraw v8.0)

Crea tableros y diagramas profesionales con calidad editorial, diseño limpio, cero amontonamientos, tipografía proporcional legible a primera vista, **estricta diversidad de arquetipos visuales**, gestión de cargas masivas (50+ entidades) con **Progressive Disclosure**, **confinamiento espacial automático en marcos**, **cero colisiones entre tarjetas** y editabilidad nativa total en formato `.excalidraw`.

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
                  │ 4. RENDERING CORE │  Adaptive Multi-Frame Reflow & Frame Containment Safety
                  └─────────┬─────────┘  Polymorphic AnchorGeometry & 90° Orthogonal Router
                            ▼
                  ┌───────────────────┐
                  │ 5. QUALITY & REPAIR│ Render Fidelity (>=90/100) · Preservation (97/100)
                  └───────────────────┘  Spatial Collision Repair · Text Spec Completeness · RDS = 0.0
```

---

## 🚫 Reglas Inviolables de Calidad Editorial & Anti-Monocultivo

### 1. Diversidad Estructural Obligatoria entre Marcos
> [!CAUTION]
> **PROHIBICIÓN ESTRICTA DE CLONAR PLANTILLAS:** En tableros de múltiples marcos (multi-frame), **ningún frame puede repetir la misma disposición columnar ni el mismo patrón geométrico que su marco adyacente** (ej. prohibido encadenar frames con chevrons y 5 columnas de tarjetas).
> Cada marco **DEBE** derivar su estructura del dominio semántico que representa:

```text
┌───────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ DOMINIO SEMÁNTICO                     │ ARQUETIPO GEOMÉTRICO OBLIGATORIO                       │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Ecosistema / Visión Central / Hub     │ Arquetipo A: El Cerebro (Hub Radial con Satélites)     │
│ Arquitectura Software / Capas Legales │ Arquetipo Layer Stack: Pila Arquitectónica de Capas    │
│ Pipelines / Algoritmos / Onboarding   │ Arquetipo C: Flow con Bucle de Feedback Visible        │
│ Roadmaps / Madurez / Horizontes       │ Arquetipo G: Escalera de Niveles + Timeline Roadmap    │
│ Comparativa / Antes vs Después        │ Arquetipo D: El Duelo (Contraste Fricción vs Control)  │
│ Matriz de Capacidades / RBAC / SLA    │ Arquetipo S: Matriz Tabular Proporcional               │
│ Triaje Condicional / Incidentes       │ Arquetipo O: Árbol de Decisión / Matriz 2x4            │
│ Causa-Raíz / Diagnóstico de Fallos    │ Arquetipo M: La Espina (Ishikawa)                      │
│ Cadena de Suministro / Proveedores    │ Arquetipo P: Cadena de Valor & Supply Chain            │
│ Auditoría Forense / Trazabilidad      │ Arquetipo Audit: Terminal de Evidencia Inmutable       │
└───────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

### 2. Llenado Espacial Proporcional (Cero Cajas Vacías)
* Ninguna tarjeta o capa debe tener más del 30% de espacio blanco muerto desaprovechado.
* Utilizar las primitivas enriquecidas:
  * **`add_stack_layer()`**: Para pilas arquitectónicas con barra de cabecera, badge de capa y chips horizontales organizados.
  * **`add_feature_card()`**: Para tarjetas con título destacado (15px bold), icono de esquina y viñetas estructuradas (12px regular).
  * **`add_quad_card()`**: Para tarjetas de 4 esquinas con badge, título, subtítulo e icono.

### 3. Confinamiento Espacial Estricto & Cero Superposiciones
* Todos los elementos asignados a un frame deben tener coordenadas absolutas dentro de los límites del frame. El motor auto-convierte cualquier coordenada relativa mediante `_base_element()` y `repair/frame_repair.py`.
* Prohibición absoluta de tarjetas superpuestas. El subsistema `repair/spatial_repair.py` separa automáticamente elementos colisionantes.

---

## 0. Motor de Arquitectura de Información (IA & Progressive Disclosure)

Ante cargas de información complejas o masivas (15 a 50+ entidades), el motor aplica **Tiers de Importancia**:
* **`HERO` (1 por marco):** Protagonista exclusivo con color de acento dominante.
* **`PRIMARY` (3 - 6 por marco):** Componentes del flujo central en tarjetas estructuradas con fuentes 15-18px.
* **`SECONDARY` (Soporte):** Componentes auxiliares y conectores de paso.
* **`METADATA` (Pills):** SLAs, latencias y métricas numéricas convertidas en badges superiores compactos.
* **`APPENDIX` (Callouts):** Circuit breakers, warnings y fallbacks aislados en notas laterales para no sobrecargar el flujo.

---

## 1. Catálogo de los 20 Arquetipos Visuales de Negocio (A - T)

| Código | Arquetipo | Motores Geométricos | Caso de Uso Principal |
| :--- | :--- | :--- | :--- |
| **A** | **El Cerebro** | `Radial` + `Grid` + `Routing` | Plataforma completa en un solo hub central y subsistemas |
| **B** | **Las Fases** | `Grid` + `Routing` + `Banners` | Roadmaps de 90 días, progresiones con gates de aprobación |
| **C** | **La Serpiente** | `Flow` (Wave) + `Routing` | Procesos lineales extendidos y pipelines con bucles |
| **D** | **El Duelo (VS)** | `Grid` + `Sticky` + `Routing` | Antes vs Después / Legacy caótico vs Arquitectura moderna |
| **E** | **La Cadena / Swimlanes**| `Board` + `Grid` + `Routing` | Swimlanes de roles y flujos coordinados entre actores |
| **F** | **El Embudo (Funnel)** | `Flow` + `Banners` | Conversión de ventas, retención y pipelines de selección |
| **G** | **La Pirámide** | `Hierarchy` + `Banners` | Modelos de madurez, capas de seguridad y abstracción |
| **H** | **El Radar 2x2** | `Grid` + `Routing` | Priorización Impacto vs Esfuerzo, clasificación de riesgos |
| **I** | **El Flywheel** | `Radial` + `Routing` | Bucles virtuosos de crecimiento, retención y recomendación |
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
| **Título de Frame / Tablero** | Ancho total ($w \ge 2000\text{px}$) | **26px – 32px Bold** |
| **Subtítulo / Breadcrumb** | Cabecera superior | **13px – 14px Mono** |
| **Tarjeta Amplia / Hero** | $w \ge 380\text{px}$ o $h \ge 115\text{px}$ | **16px – 18px Bold** |
| **Título de Tarjeta Estándar** | $w \in [220\text{px}, 380\text{px}]$ | **14px – 15px Bold** |
| **Viñetas / Cuerpo Explicativo**| Dentro de tarjeta | **12px – 13px Regular** |
| **Cabecera de Capa / Tabla** | Stack Layer / Columnas | **13px – 14px Bold** |
| **Badges de Rol / Paso** | Pastillas $h=20\text{--}22\text{px}$ | **10px – 11px Mono/Sans** |

---

## 3. Checklist de Calidad Editorial antes de Entregar

- [ ] El archivo tiene extensión `.excalidraw` y es JSON válido.
- [ ] **Diversidad de Arquetipos:** Cada frame usa un arquetipo visual diferente adaptado a su semántica.
- [ ] **Visibilidad Tipográfica:** Todos los textos tienen `width`, `height`, `lineHeight: 1.25`, `baseline` y vinculación `containerId <-> boundElements`.
- [ ] **Llenado Espacial:** No hay tarjetas con grandes vacíos en blanco; el contenido llena armónicamente la caja.
- [ ] **Cero Colisiones:** Ninguna tarjeta ni texto se solapa sobre otro elemento.
- [ ] **Confinamiento en Frames:** Todos los elementos hijos están físicamente dentro de las coordenadas de su frame.
- [ ] **AnchorGeometry Activo:** Las flechas tocan con precisión milimétrica los bordes perimetrales sin traspasos.
- [ ] **Progressive Disclosure:** Máximo 6 tarjetas primarias por marco; métricas en pills y excepciones en callouts.
- [ ] Se utilizó la paleta editorial con exactamente 1 acento focal principal por marco.
- [ ] El validador `validate_scene()` devuelve `PASS` con puntuación global >= 95/100 y `RDS <= 40`.
