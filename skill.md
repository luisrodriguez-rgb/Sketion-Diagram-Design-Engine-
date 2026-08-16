---
name: sketion-diagram-design
description: Generador editorial de diagramas y tableros nativos para Excalidraw (.excalidraw). Arquitectura desacoplada en 4 capas (Semantica -> Layout -> Render -> Calidad Visual) con soporte de Smart Defaults, niveles de detalle, Catalogo de 20 Arquetipos Visuales respaldados por 9 Motores Geometricos Base y evaluador de Semantic Hard Constraints sin colisiones.
license: MIT
metadata:
  version: "3.3"
---

# Sketion Diagram Design Skill (Motor Editorial para Excalidraw)

Crea tableros y diagramas profesionales con calidad editorial, diseno limpio, cero amontonamientos y editabilidad nativa total en formato `.excalidraw`.

Combina los principios de **Diagram Design** (densidad 4/10, regla del acento unico, eliminacion de ruido visual) con los **20 Arquetipos de Negocio** y la precision geometrica de sus **9 Motores de Layout Base**.

---

## 0. Smart Defaults y Progressive Disclosure (Sin Friccion)

**No interrumpir al usuario con formularios de preguntas.** El motor resuelve automaticamente la intencion semantica y genera el tablero terminado en el primer turno:

- **Si el usuario especifica:** Respetar sus elecciones (paleta, roughness, detalle, modo, arquetipo).
- **Si no se especifica nada (Smart Defaults automaticos):**
  - **Modo:** Claro (`viewBackgroundColor: "#F4F4F4"` lienzo editorial o `"#FFFFFF"`).
  - **Trazo (`roughness`):** `0` (Limpio, tecnico, vectorial profesional).
  - **Paleta:** `MIRO_EDITORIAL` (`#F4F4F4` base, `#0C0C0C` tinta, `#E03A2F` acento de dolor, `#FFE95C` sticky notes).
  - **Nivel de Detalle:** `balanced` con descomposiciones multi-frame si el problema excede 9 nodos.
  - **Metricas Faltantes:** Estimar cifras creibles de industria y documentarlas al pie en lugar de dejar huecos vacios.

---

## 1. Arquitectura de Dos Niveles: Motores Geometricos y Arquetipos

```text
PROMPT / REQUISITOS DEL USUARIO
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
| **Timeline** | `layout/flow.py` | Eje cronologico alternado | Distribuye hitos temporales arriba y abajo del eje central. |
| **Tree** | `layout/hierarchy.py`| Arbol jerarquico balanceado | Posiciona nodos padres e hijos calculando anchos de sub-arbol. |
| **Radial** | `layout/hierarchy.py`| Distribucion angular perimetral | Calcula radios y angulos equidistantes alrededor de un hub. |
| **Grid / Matrix** | `layout/grid.py` | Grilla tabular proporcional | Calcula anchos dinamicos (hasta 560px) y alturas por lineas reales. |
| **Board / Lanes** | `layout/grid.py` | Carriles verticales paralelos | Gestiona columnas de ancho uniforme y apilamiento vertical. |
| **Dashboard** | `layout/grid.py` | Matriz de chips numericos | Distribuye tarjetas de KPI en grillas de 2, 3 o 4 columnas. |
| **Network / Red** | `engines/recipes.py` | Grafo distribuido con Scopes | Agrupa nodos en columnas de infraestructura con gutter de 65px. |
| **Routing** | `layout/routing.py` | Enrutamiento ortogonal y Track Lanes | Genera codos a 90 grados, anclajes de salida y carriles de retorno. |

---

## 3. Catalogo Maestro de los 20 Arquetipos Visuales (A a T)

| Codigo | Nombre del Arquetipo | Motores Base Utilizados | Caso de Uso Principal |
| :--- | :--- | :--- | :--- |
| **A** | **El Cerebro** | `Radial` + `Grid` + `Routing` | Plataforma completa en un solo hub central |
| **B** | **Las Fases** | `Grid` + `Routing` + `Banners` | Roadmaps de 90 dias, progresiones con gates |
| **C** | **La Serpiente** | `Flow` (Wave) + `Routing` | Procesos lineales de 8 a 16 pasos |
| **D** | **El Duelo (VS)** | `Grid` + `Sticky` + `Routing` | Antes vs Despues / Legacy vs Moderno |
| **E** | **La Cadena** | `Board` + `Grid` + `Routing` | Swimlanes paralelos por actor con handoffs |
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
| **S** | **Matriz CRUD** | `Grid` (Proportional) | Mapeo de propiedad de datos (Data Ownership) |
| **T** | **Caja Explotada** | `Network` + `Routing` | Explicar el funcionamiento interno de un motor |

---

## 4. Reglas de Micro-Diseno y Cero Colisiones (Core 3.3)

1. **Centrado Geometrico del Texto:**
   - La coordenada Y del elemento de texto se calcula exactamente segun la altura real de las lineas:
     text_h = line_count * font_size * 1.35
     text_y = y + (card_h - text_h) / 2
   - Se activa `autoResize: True` y `verticalAlign: "middle"` para centrado bidimensional exacto.

2. **Separacion de Scopes (Gutter Seguro de 65px):**
   - Las columnas de infraestructura/scopes se disponen consecutivamente garantizando un canal libre de 65px entre sus bordes. Cero solapamiento de lineas divisorias.

3. **Anclaje de Salida en Saltos de Columna (Cross-Scope Bypass):**
   - Cuando una flecha cruza multiples columnas (dx > 350px), su pastilla protectora se ancla en el origen (x1 + 55px, y1 - 14px), dejando los scopes intermedios 100% limpios y sin colisiones de etiquetas.

4. **Conectores de Flujo con Separacion de 95px:**
   - En flujos secuenciales, las tarjetas se separan exactamente 95px para que las pastillas de transicion queden suspendidas en el centro exacto de la flecha sin pisar las cajas.

5. **Grillas Tabulares Proporcionales y Dinamicas:**
   - El ancho de cada columna de la matriz se calcula segun la longitud maxima de su texto (hasta 560px para explicaciones) y la altura de fila se adapta a las lineas reales.

---

## 5. Paleta Editorial Miro Nico en Excalidraw

```python
MIRO_PALETTE = {
    "CANVAS": "#F4F4F4",          # Fondo suave de pizarra
    "CARD": "#FFFFFF",            # Tarjetas blancas nitidas
    "CARD_BORDER": "#BDBDBD",     # Borde suave 1.5px
    "INK": "#0C0C0C",             # Tinta negra solida para titulares y chips
    "MUTED": "#8B8B8B",           # Texto secundario y conectores de contexto
    "STICKY": "#FFE95C",          # Post-it amarillo con micro-rotacion (-1.5 a +1.5 grados)
    "PAIN_RED": "#E03A2F",        # Alertas, cuellos de botella y numeros criticos
    "PAIN_BG": "#FDEFEF",         # Fondo de tarjetas de dolor o antes/legacy
    "PAIN_BORDER": "#F05A5A",     # Borde discontinuo de slots de captura
    "BANNER_PINK": "#F5BEC0",     # Frase de remate / punchline inferior
    "PASTEL_BLUE": "#9BC7E4",     # Cabeceras de fases y zonas
    "PASTEL_GREEN": "#C2E5D3"     # Confirmaciones y estados exitosos
}
```

---

## 6. Principio de Semantic Hard Constraints

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

> **Regla de Oro:** Un diagrama visualmente impecable (100/100) pero que omite un componente critico es un **HARD FAILURE INMEDIATO**. La fidelidad semantica manda sobre la estetica; ante exceso de informacion, la unica respuesta valida es la **descomposicion elastica en multiples marcos coordinados**.

---

## 7. Checklist de Calidad antes de Entregar

- [ ] El archivo tiene extension `.excalidraw` y es JSON valido minificado.
- [ ] El texto dentro de todas las tarjetas esta centrado vertical y horizontalmente.
- [ ] Los scopes tienen separacion limpia (minimo 65px de gutter) sin solapamiento.
- [ ] Las flechas largas no amontonan pastillas de texto en columnas intermedias.
- [ ] Las tablas/matrices muestran todo el texto completo sin truncamientos.
- [ ] Se utilizo la paleta editorial con maximo 1-2 acentos focales.
- [ ] El validador `validate_scene()` devuelve `PASS` con puntuacion global >= 95/100.

---

## 8. Referencias y Archivos de Prueba

- Catalogo Completo de Arquetipos: `docs/catalogo-20-arquetipos-visuales.md`
- Propuesta de Mejoras Estrategicas: `docs/propuesta-mejoras-miro-sketion.md`
- Walkthrough Completo de Pruebas: `docs/walkthrough-pruebas-v3.md`
- Suite de Pruebas Adversariales: `tests/adversarial/`
- Demos Excalidraw Nativo: `PRUEBAS_V3/` y `PRUEBAS_V4/`
