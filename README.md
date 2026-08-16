# Sketion Diagram Design Engine

**Motor editorial de diseno y generacion de diagramas inteligentes y 100% editables en formato nativo .excalidraw.**

Inspirado en los principios de diseno de **Diagram Design** (densidad visual 4/10, regla del acento unico, conectores ortogonales a 90 grados) y construido sobre una **arquitectura desacoplada en 4 capas** con auditoria de **Fidelidad Semantica**, **Calidad Visual**, **Semantic Hard Constraints** y **Bucle de Auto-Correccion**.

---

## 1. Arquitectura de Dos Niveles: Motores Geometricos y Arquetipos de Negocio

Sketion 3.3 opera mediante una separacion estricta entre la **geometria matematica** y la **composicion editorial de negocio**:

```text
                  PROMPT / REQUISITOS DEL USUARIO
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
| **Timeline** | `layout/flow.py` | Eje cronologico alternado | Distribuye hitos temporales arriba y abajo de un eje central sin colision de texto. |
| **Tree** | `layout/hierarchy.py`| Arbol jerarquico balanceado | Posiciona nodos padres e hijos en multiples niveles calculando anchos de sub-arbol. |
| **Radial** | `layout/hierarchy.py`| Distribucion perimetral angular | Calcula radios y angulos equidistantes alrededor de un nodo o hub central. |
| **Grid / Matrix** | `layout/grid.py` | Grilla tabular bidimensional proporcional | Calcula anchos de columna dinamicos segun longitud de texto (hasta 560px) y alturas de fila por lineas reales. |
| **Board / Lanes** | `layout/grid.py` | Carriles verticales paralelos (Kanban) | Gestiona columnas de ancho uniforme y apilamiento vertical de tarjetas. |
| **Dashboard** | `layout/grid.py` | Matriz de chips numericos | Distribuye tarjetas de KPI en grillas de 2, 3 o 4 columnas con proporciones fijas. |
| **Network / Red** | `engines/recipes.py` | Grafo distribuido con Scopes | Agrupa nodos por columnas de infraestructura aplicando gutter de 65px entre contenedores. |
| **Routing** | `layout/routing.py` | Enrutamiento ortogonal y Track Lanes | Genera codos a 90 grados, anclajes de salida en saltos de columna y carriles de retorno superiores. |

---

## 3. El Catalogo Maestro de los 20 Arquetipos de Composicion Visual

Los arquetipos representan las recetas de diseno de alto nivel que resuelven problemas de negocio reales combinando los motores base:

| Codigo | Nombre del Arquetipo | Motores Base Utilizados | Estructura y Descripcion Visual |
| :--- | :--- | :--- | :--- |
| **A** | **El Cerebro** | `Radial` + `Grid` + `Routing` | Hub circular central conectado por lineas radiales a 4 columnas tematicas, con chips numericos al pie, banner de remate inferior y slots de captura. |
| **B** | **Las Fases** | `Grid` + `Routing` + `Banners` | Grilla de 6 cuadrantes con numerales gigantes (72px a 120px) en el lateral, cajas con borde discontinuo, badges pastel y barras de entregable obligatorio en rojo. |
| **C** | **La Serpiente** | `Flow` (Wave) + `Routing` | Flujo en curva continua en vaiven (Boustrophedon) con badges circulares numerados, ideal para procesos de 8 a 16 pasos sin desbordar el ancho del canvas. |
| **D** | **El Duelo (VS)** | `Grid` + `Sticky` + `Routing` | Pantalla dividida en dos mitades enfrentadas con espina central de post-its amarillos rotados (-1.5 a +1.5 grados), tarjetas de dolor (gris) vs solucion (coral) y metricas comparativas. |
| **E** | **La Cadena** | `Board` + `Grid` + `Routing` | Swimlanes paralelos horizontales organizados por actor con columnas de tiempo y flechas ortogonales que representan handoffs y llamadas API. |
| **F** | **El Embudo (Funnel)** | `Flow` + `Banners` | Bloques trapezoidales descendentes de ancho decreciente con pastillas laterales que indican el porcentaje de caida (drop-off rate) entre etapas. |
| **G** | **La Piramide** | `Hierarchy` + `Banners` | Capas horizontales apiladas de base a cuspide para modelos de madurez DevOps/IA y capas de seguridad defensiva (Defense-in-Depth). |
| **H** | **El Radar 2x2** | `Grid` + `Routing` | Eje cartesiano ortogonal que divide el espacio en 4 cuadrantes con fondos pastel suaves para clasificar iniciativas por Impacto vs Esfuerzo o matrices de riesgo. |
| **I** | **El Flywheel** | `Radial` + `Routing` | Nodos en orbita circular continua con flechas en arco perimetral en sentido horario y un nodo central que sintetiza el efecto compuesto del bucle. |
| **J** | **La Cebolla (Onion)** | `Hierarchy` (Nested) | Cajas concentricas anidadas desde el nucleo (dominio) hacia las capas exteriores (aplicacion, adaptadores, UI) con flechas de dependencia hacia adentro. |
| **K** | **El Kanban WIP** | `Board` + `Sticky` | Columnas verticales de estado con limites de trabajo en curso (WIP Limits) en las cabeceras y tarjetas apiladas con tags de prioridad. |
| **L** | **El Iceberg** | `Grid` + `Banners` | Division por linea de agua: 15% superior visible (UI simple) vs 85% inferior sumergido (infraestructura oculta, bases de datos y conciliacion). |
| **M** | **La Espina (Ishikawa)** | `Hierarchy` + `Routing` | Eje horizontal continuo que apunta al problema final a la derecha, con costillas diagonales superiores e inferiores para analisis de causa raiz y post-mortems. |
| **N** | **Galeria 3x3** | `Dashboard` + `Grid` | Cuadricula modular simetrica de tarjetas uniformes con micro-iconos, descripcion de dos lineas y status badges ([GA], [BETA], [DEPRECATED]). |
| **O** | **Arbol de Decision** | `Tree` + `Routing` | Nodo dilema inicial que bifurca mediante pastillas condicionales ([SI] / [NO]) hacia nodos secundarios y cajas terminales de accion. |
| **P** | **Cadena de Valor** | `Flow` + `Grid` | Franjas horizontales superiores de soporte y secuencia inferior de 5 actividades primarias, rematando con un chevron triangular de margen comercial. |
| **Q** | **Pilares Benchmark** | `Board` + `Dashboard` | Podio de 3 a 5 columnas verticales con barras de nivel proporcional, valores numericos gigantes y lista de ventajas competitivas. |
| **R** | **Roadmap con Gates** | `Timeline` + `Banners` | Eje cronologico continuo con diamantes de control (Quality Gates) que contienen listas de verificacion indispensables para avanzar de fase. |
| **S** | **Matriz CRUD** | `Grid` (Proportional) | Tabla bidireccional donde las filas representan servicios y las columnas entidades de datos, con celdas que contienen micro-pills [C][R][U][D]. |
| **T** | **Caja Explotada** | `Network` + `Routing` | Caja macro a la izquierda conectada mediante lineas de proyeccion conicas hacia un marco detallado a la derecha que desglosa su funcionamiento interno. |

---

## 4. Reglas de Micro-Diseno y Cero Colisiones (Core 3.3)

Sketion aplica formulas matematicas para garantizar que ningun elemento colisione o quede desalineado:

1. **Centrado Geometrico Bidimensional:**
   El texto no se coloca en el borde superior de la tarjeta. Se calcula la altura real del bloque de texto:
   $$\text{text\_h} = \text{line\_count} \times \text{font\_size} \times 1.35$$
   $$\text{text\_y} = y + \frac{\text{card\_h} - \text{text\_h}}{2}$$
   Se activa `autoResize: True` y `verticalAlign: "middle"` para centrado exacto.

2. **Gutter Seguro de 65px entre Scopes:**
   Las columnas de infraestructura se disponen secuencialmente asegurando un margen lateral de 65px entre bordes adyacentes. Cero solapamiento de contenedores.

3. **Anclaje de Salida en Saltos de Columna (Cross-Scope Bypass):**
   Si una conexion cruza mas de una columna ($dx > 350\text{px}$), su pastilla protectora se ancla en el origen ($x_1 + 55\text{px}, y_1 - 14\text{px}$), dejando los scopes intermedios 100% limpios y sin acumulacion de etiquetas.

4. **Espaciado de Flujo de 95px con Pastilla Centrada:**
   Las tarjetas secuenciales se separan exactamente 95px para que las pastillas de transicion queden suspendidas en el centro exacto de la flecha sin tocar las cajas.

5. **Grillas Tabulares Proporcionales:**
   El ancho de cada columna de la matriz se calcula segun la longitud maxima de su contenido (hasta 560px para explicaciones) y la altura de fila segun el numero real de lineas.

---

## 5. Sistema de Tokens y Paleta Editorial

Todas las decisiones visuales se rigen por `references/style-guide.md`:

```python
MIRO_PALETTE = {
    "CANVAS": "#F4F4F4",          # Fondo suave de pizarra
    "CARD": "#FFFFFF",            # Tarjetas blancas nitidas
    "CARD_BORDER": "#BDBDBD",     # Borde suave de 1.5px
    "INK": "#0C0C0C",             # Tinta negra solida para titulares y chips
    "MUTED": "#8B8B8B",           # Texto secundario y conectores auxiliares
    "STICKY": "#FFE95C",          # Post-it amarillo con micro-rotacion (-1.5 a +1.5 grados)
    "PAIN_RED": "#E03A2F",        # Alertas, cuellos de botella y numeros criticos
    "PAIN_BG": "#FDEFEF",         # Fondo de tarjetas de dolor o advertencia
    "PAIN_BORDER": "#F05A5A",     # Borde discontinuo de slots de captura
    "BANNER_PINK": "#F5BEC0",     # Frase de remate inferior
    "PASTEL_BLUE": "#9BC7E4",     # Cabeceras de fases y zonas de red
    "PASTEL_GREEN": "#C2E5D3"     # Confirmaciones y estados exitosos
}
```

---

## 6. Principio de Semantic Hard Constraints

Cuando la **Calidad Visual** y la **Fidelidad Semantica** entran en conflicto, Sketion aplica una jerarquia estricta:

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

## 7. Ejecucion de Pruebas y Benchmarks

```bash
# Validacion de regresion visual
python3 tests/test_visual_regression.py

# Stress testing de alta densidad
python3 tests/test_stress.py

# Benchmark de fidelidad integral
python3 tests/benchmark_dogfooding.py

# Generador de casos maestros V4
python3 PRUEBAS_V4/generate_onboarding_transformation.py
python3 PRUEBAS_V4/generate_university_space_reservation.py
python3 PRUEBAS_V4/generate_payment_platform.py
```
