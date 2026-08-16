---
name: sketion-diagram-design
description: Generador editorial de diagramas y tableros nativos para Excalidraw (.excalidraw). Arquitectura desacoplada en 4 capas (Semantica -> Layout -> Render -> Calidad Visual) con motor de inferencia por audiencia (Audience-Aware Engine), Catalogo Completo de 20 Arquetipos de Negocio (A - T), Suite de 27 Tipos Visuales Específicos, Gramatica Editorial de Diagram Design (Tarjetas Quad-Corner, Cintas Chevron, Rieles Verticales, Ejes de Pasos, Leyendas Estructuradas), Escalado Tipografico Proporcional Anti-Espacio Vacio (18-20px en tarjetas, 14px en tablas), Regla Anti-Monocultivo de Layout (Prohibición estricta de clonar estructuras columnares en múltiples frames), simetria 1:1 en journeys, enrutamiento inter-zonas y evaluador de Semantic Hard Constraints & Archetype Fitness sin colisiones.
license: MIT
metadata:
  version: "4.0"
---

# Sketion Diagram Design Skill (Motor Editorial para Excalidraw v4.0)

Crea tableros y diagramas profesionales con calidad editorial, diseno limpio, cero amontonamientos, tipografía proporcional legible a primera vista, **estricta diversidad de arquetipos visuales** y editabilidad nativa total en formato `.excalidraw`.

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
│ Workshops / Sesión de Discovery       │ Arquetipo Workshop: Post-its, Checklist & Preguntas    │
└───────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

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

- [ ] El archivo tiene extension `.excalidraw` y es JSON valido minificado.
- [ ] **Diversidad de Arquetipos:** Cada frame usa un arquetipo diferente (Hub Radial, Stack Horizontal, Flow con Bucle, Escalera, etc.). Cero clones de 5 columnas.
- [ ] La tipografía de las tarjetas utiliza **18-20px Bold** para el título y **13-14px** para el subtítulo, llenando armónicamente el espacio interior.
- [ ] Las tablas y matrices usan **14-15px** en cabeceras y **13-14px** en celdas para lectura inmediata.
- [ ] La estructura del diagrama responde a la audiencia objetivo (CEO, Ops, Tech, Devs, Data).
- [ ] Se utilizo la paleta editorial con exactamente 1 acento focal principal por frame.
- [ ] El validador `validate_scene()` devuelve `PASS` con puntuacion global >= 90/100 y `Archetype Fitness` >= 90/100.
