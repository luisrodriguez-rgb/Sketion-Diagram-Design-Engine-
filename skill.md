---
name: sketion-diagram-design
description: Generador editorial de diagramas y tableros nativos para Excalidraw (.excalidraw). Arquitectura desacoplada en 4 capas (Semantica -> Layout -> Render -> Calidad Visual) con motor de inferencia por audiencia (Audience-Aware Engine), Catalogo de 20 Arquetipos Visuales respaldados por 9 Motores Geometricos, simetria 1:1 en journeys, enrutamiento inter-zonas y evaluador de Semantic Hard Constraints sin colisiones.
license: MIT
metadata:
  version: "3.4"
---

# Sketion Diagram Design Skill (Motor Editorial para Excalidraw)

Crea tableros y diagramas profesionales con calidad editorial, diseno limpio, cero amontonamientos y editabilidad nativa total en formato `.excalidraw`.

Combina los principios de **Diagram Design** (densidad 4/10, regla del acento unico, eliminacion de ruido visual) con el **Motor de Inferencia de Audiencia**, los **20 Arquetipos de Negocio**, y los **9 Motores de Layout Geometrico Base**.

---

## 0. Motor de Decision de Audiencia (Audience-Aware Engine)

Sketion adapta autonomamente la seleccion de arquetipos, la densidad de informacion y el vocabulario segun el perfil del receptor:

| Perfil de Audiencia | Arquetipos Principales | Foco Semantico Obligatorio | Elementos a Suprimir (Evitar Ruido) | Tono Editorial |
| :--- | :--- | :--- | :--- | :--- |
| **CEO / Directivo** | `D (Duelo)`, `B (Fases)`, `P (Cadena Valor)`, `H (Radar 2x2)` | ROI, Margen, Coste Fijo $0, Retencion, Fases de Aprobacion | APIs, Microservicios, Codigo, Cronometros de segundos | Estrategico / Financiero |
| **Gerente Operaciones** | `E (Planta/Swimlanes)`, `M (Ishikawa)`, `S (Matriz Takt)`, `K (Kanban)` | Layout de Planta, Segregacion Fisica, Takt Time, Batching, Roles | Modelos Financieros Macro, Arquitectura Cloud, Nube | Industrial / Planta |
| **Equipo Producto / Tech**| `A (Cerebro)`, `C (Journey 1:1)`, `T (Caja Explotada)`, `N (Galeria)` | Arquitectura Cloud, Microservicios, User Journey, Slots UI, KDS | Negociaciones Laborales, Nomina, Tramites Administrativos | Tecnico / Software |
| **Documentacion Devs** | `S (Matriz CRUD)`, `O (Arbol Decision)`, `T (Caja Explotada)` | Endpoints HTTP, JSON Schema, Idempotency Keys, Codigos Error | Discursos Comerciales, Planos Fisicos de Edificio | Contrato API / gRPC |
| **Inversionistas / Pitch**| `D (Duelo VS)`, `F (Embudo)`, `I (Flywheel)` | Tamano de Mercado, Metricas Heroicas, Traccion, Dolor vs Solucion | Tablas Complejas, Diagramas de Red Detallados | Impacto / Traccion |

---

## 1. Arquitectura de Dos Niveles: Motores Geometricos y Arquetipos

```text
PROMPT / REQUISITOS DEL USUARIO
        |
        v
[MOTOR DE AUDIENCIA]        -> Filtra informacion segun el perfil (CEO / Ops / Tech / Devs)
        |
        v
[CAPA EDITORIAL / NEGOCIO] -> 20 Arquetipos Visuales (A - T)
        |                     (El Duelo, Las Fases, El Cerebro, La Serpiente, etc.)
        v
[CAPA GEOMETRICA / LAYOUT]  -> 9 Motores de Layout Base (layout/ & engines/)
        |                     (flow.py, hierarchy.py, grid.py, routing.py, network)
        v
[CAPA DE RENDER NATIVO]     -> Primitivas Excalidraw (.excalidraw)
        |                     (containerId <-> boundElements, stickies rotados)
        v
[CAPA DE AUDITORIA]         -> Semantic Hard Constraints & Auto-Repair Engine
```

---

## 2. Los 9 Motores Geometricos Base (layout/ & engines/)

| Motor Base | Archivo / Modulo | Algoritmo Geometrico | Responsabilidad Matematica |
| :--- | :--- | :--- | :--- |
| **Flow** | `layout/flow.py` | Secuencia horizontal y sinusoidal | Calcula coordenadas continuas con espaciado elastico de 95px. |
| **Journey 1:1** | `layout/flow.py` | Simetria vertical estricta | Empareja exactamente N pasos superiores con N slots de captura inferiores. |
| **Timeline** | `layout/flow.py` | Eje cronologico alternado | Distribuye hitos temporales arriba y abajo del eje central. |
| **Tree** | `layout/hierarchy.py`| Arbol jerarquico balanceado | Posiciona nodos padres e hijos calculando anchos de sub-arbol. |
| **Radial** | `layout/hierarchy.py`| Distribucion angular perimetral | Calcula radios y angulos equidistantes alrededor de un hub. |
| **Grid / Matrix** | `layout/grid.py` | Grilla tabular proporcional | Calcula anchos dinamicos (hasta 560px) y alturas por lineas reales. |
| **Board / Lanes** | `layout/grid.py` | Carriles verticales paralelos | Gestiona columnas de ancho uniforme y apilamiento vertical. |
| **Dashboard** | `layout/grid.py` | Matriz de chips numericos | Distribuye tarjetas de KPI en grillas de 2, 3 o 4 columnas. |
| **Network / Red** | `engines/recipes.py` | Grafo distribuido con Scopes | Agrupa nodos en columnas de infraestructura con gutter de 65px. |
| **Routing** | `layout/routing.py` | Enrutamiento ortogonal y Flujo Inter-Zonas | Genera codos a 90 grados, anclajes de salida y conectores de transito fisico. |

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

## 4. Reglas de Micro-Diseno y Cero Colisiones (Core 3.4)

1. **Centrado Geometrico del Texto:**
   - La coordenada Y del texto se calcula segun la altura real de las lineas:
     text_h = line_count * font_size * 1.35
     text_y = y + (card_h - text_h) / 2
   - Se activa `autoResize: True` y `verticalAlign: "middle"` para centrado bidimensional exacto.

2. **Simetria 1:1 en User Journeys:**
   - En flujos de experiencia de usuario con capturas, cada paso superior debe coincidir exactamente en posicion X y ancho con su slot de captura inferior correspondiente.

3. **Flujo Fisico Direccional Inter-Zonas:**
   - En diagramas de planta operativa o swimlanes, las zonas no deben quedar aisladas. Deben incluir flechas ortogonales que indiquen el transito de personas, productos y eventos.

4. **Separacion de Scopes (Gutter Seguro de 65px):**
   - Las columnas de infraestructura/scopes se disponen consecutivamente garantizando un canal libre de 65px entre sus bordes. Cero solapamiento de lineas divisorias.

5. **Anclaje de Salida en Saltos de Columna (Cross-Scope Bypass):**
   - Cuando una flecha cruza multiples columnas (dx > 350px), su pastilla protectora se ancla en el origen (x1 + 55px, y1 - 14px), dejando los scopes intermedios 100% limpios y sin colisiones.

---

## 5. Principio de Semantic Hard Constraints

```text
                 +--------------------------------+
                 |    SEMANTIC HARD CONSTRAINTS   |
                 |   (Inviolables por Estetica)   |
                 +---------------+----------------+
                                 |
         +-----------------------+-----------------------+
         |                                               |
         v                                               v
[FATAL HARD FAILURES]                           [REPARACIONES PERMITIDAS]
- Nodo de Dominio Omitido (ej. Ledger)           - Auto-Split en Multi-Frame
- Arista Crítica Borrada                         - Reduccion de Acentos (>2)
- Transicion de Estado Invalida                  - Espaciado elastico de Gaps
- Violacion de Inmutabilidad                     - Enrutamiento por Track Lanes
```

---

## 6. Checklist de Calidad antes de Entregar

- [ ] El archivo tiene extension `.excalidraw` y es JSON valido minificado.
- [ ] La estructura del diagrama responde a la audiencia objetivo (CEO, Ops, Tech, Devs).
- [ ] Si es un User Journey, existe correspondencia 1:1 entre pasos y slots de captura.
- [ ] Si es una planta operativa, existen flechas de transito fisico entre zonas.
- [ ] El texto dentro de todas las tarjetas esta centrado vertical y horizontalmente.
- [ ] Los scopes tienen separacion limpia (minimo 65px de gutter) sin solapamiento.
- [ ] Se utilizo la paleta editorial con maximo 1 acento focal principal.
- [ ] El validador `validate_scene()` devuelve `PASS` con puntuacion global >= 95/100.
