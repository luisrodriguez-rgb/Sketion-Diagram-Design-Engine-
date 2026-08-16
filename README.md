# Sketion Diagram Design Engine

**Motor editorial de diseno y generacion de diagramas inteligentes y 100% editables en formato nativo .excalidraw.**

Inspirado en los principios de diseno de **Diagram Design** (densidad 4/10, regla del acento unico, conectores ortogonales a 90 grados) y construido sobre una **arquitectura desacoplada en 4 capas** con auditoria de **Fidelidad Semantica**, **Calidad Visual** y **Bucle de Auto-Correccion**.

---

## Por que Sketion?

La mayoria de herramientas de IA generan diagramas como imagenes estaticas (SVG/PNG) o producen diagramas sin criterio visual ni jerarquia estructurada.

**Sketion resuelve ambos problemas:**
1. **Calidad Editorial Estricta:** Aplica un sistema de tokens de diseno (`PAPER`, `INK`, `ACCENT`), evita decoraciones innecesarias y enruta flechas con codos ortogonales limpios y carriles de retorno (*Track Lanes*).
2. **Editabilidad Nativa Total:** Genera archivos `.excalidraw` validos v2, con texto estrictamente vinculado a contenedores (`containerId` <-> `boundElements`) y serializacion JSON minificada.
3. **Evaluacion de Fidelidad y Auto-Correccion:** El motor evalua tanto la estetica visual como la fidelidad con respecto a la intencion del usuario, auto-reparando desviaciones antes de entregar el archivo.
4. **Catálogo de 20 Arquetipos:** Soporta composiciones de alto impacto (El Duelo Before/After, Las Fases con numerales gigantes, El Cerebro Radial, Swimlanes, Embudo, Piramide, etc.).

---

## Arquitectura Desacoplada en 4 Capas

```text
                  PROMPT / IDEA DEL USUARIO
                             |
        +-------------------------------------------+
        | 1. MODELO SEMANTICO (semantic/)           |
        |    - Representacion intermedia tipada     |
        |    - Scopes / Zonas de infraestructura    |
        |    - 3 Niveles de Detalle (Simple/Bal/Det)|
        +--------------------+----------------------+
                             |
        +-------------------------------------------+
        | 2. MOTOR DE LAYOUT (layout/)              |
        |    - flow.py / hierarchy.py / grid.py     |
        |    - routing.py (Codos ortogonales 90 deg)|
        +--------------------+----------------------+
                             |
        +-------------------------------------------+
        | 3. RENDER EXCALIDRAW (render/)            |
        |    - Primitivas nativas (cajas, textos)   |
        |    - Vinculacion bidireccional estricta   |
        |    - Centrado geometrico Y de texto       |
        |    - JSON minificado sin indentacion      |
        +--------------------+----------------------+
                             |
        +-------------------------------------------+
        | 4. QUALITY VALIDATOR & REPAIR (validation)|
        |    - Visual Quality Score (Densidad 4/10) |
        |    - Semantic Fidelity Score (Coverage)   |
        |    - Semantic Hard Constraints Engine     |
        |    - Self-Correction Loop (Repair Engine) |
        +--------------------+----------------------+
                             |
                 ARCHIVO .excalidraw 100% EDITABLE
```

---

## Los 20 Arquetipos de Composicion Visual

| Codigo | Arquetipo | Estructura Geometrica | Caso de Uso Principal |
| :--- | :--- | :--- | :--- |
| **A** | **El Cerebro** | Hub circular central con 4 ramas radiales | Plataforma completa en un solo hub central |
| **B** | **Las Fases** | 6 cuadrantes con numerales gigantes | Roadmaps de 90 dias, progresiones con gates |
| **C** | **La Serpiente** | Curva S continua en vaiven (Boustrophedon) | Procesos lineales de 8 a 16 pasos |
| **D** | **El Duelo (VS)** | 2 mitades enfrentadas con espina de stickies | Antes vs Despues / Legacy vs Moderno |
| **E** | **La Cadena** | Swimlanes paralelos por actor con handoffs | Procesos multi-actor con llamadas API |
| **F** | **El Embudo** | Bloques trapezoidales descendentes | Conversion de ventas, pipelines de seleccion |
| **G** | **La Piramide** | Capas horizontales apiladas de base a cuspide | Modelos de madurez, capas de seguridad |
| **H** | **El Radar 2x2** | Eje cartesiano en 4 cuadrantes pastel | Priorizacion Impacto vs Esfuerzo, riesgos |
| **I** | **El Flywheel** | Circulo de 4-6 nodos con flechas perimetrales | Bucles de crecimiento y retencion |
| **J** | **La Cebolla** | Anillos concentricos anidados hacia el nucleo | Clean Architecture, Hexagonal, Gobernanza |
| **K** | **El Kanban WIP** | Columnas de estado con limites WIP | Pipelines agiles, colas de trabajo, releases |
| **L** | **El Iceberg** | Linea de agua: 15% visible vs 85% oculto | Deuda tecnica, complejidad backend vs UI |
| **M** | **La Espina** | Eje horizontal con costillas diagonales | Analisis de causa raiz (Ishikawa), post-mortems |
| **N** | **Galeria 3x3** | Grilla modular simetrica con status badges | Catalogo de microfrontends, suite de APIs |
| **O** | **Arbol Decision** | Dilema inicial con ramas SI/NO | Protocolos de escalado, triaje, reglas |
| **P** | **Cadena de Valor**| Franjas superiores y cajas con chevron | Mapeo estrategico de operaciones y margen |
| **Q** | **Benchmark** | Podio de columnas con barras de llenado | Comparativa de latencia, throughput y costes |
| **R** | **Roadmap Gates** | Timeline horizontal con diamantes de control | Lanzamientos v3.0, auditorias SOC2 / ISO |
| **S** | **Matriz CRUD** | Grilla de Servicios (Y) vs Entidades (X) | Mapeo de propiedad de datos (Data Ownership) |
| **T** | **Caja Explotada**| Caja macro con lineas guia a zoom | Explicar el funcionamiento interno de un motor |

---

## Sistema de Diseno y Tokens Semanticos

Todas las decisiones visuales se rigen por `references/style-guide.md`:

* **`CANVAS` (`#F4F4F4` o `#FFFFFF`):** Fondo del canvas.
* **`CARD` (`#FFFFFF`):** Fondo de tarjetas de componentes.
* **`CARD_BORDER` (`#BDBDBD`):** Borde suave de 1.5px.
* **`INK` (`#0C0C0C`):** Tinta principal para titulos, bordes y texto.
* **`MUTED` (`#8B8B8B`):** Conectores secundarios y subetiquetas mono.
* **`STICKY` (`#FFE95C`):** Notas post-it con micro-rotacion (-1.5 a +1.5 grados).
* **`PAIN_RED` (`#E03A2F`):** Alertas, cuellos de botella y numeros criticos.
* **`PAIN_BG` (`#FDEFEF`):** Fondo de tarjetas de dolor o advertencia.
* **`PAIN_BORDER` (`#F05A5A`):** Borde discontinuo de slots de captura.
* **`BANNER_PINK` (`#F5BEC0`):** Frase de remate inferior.
* **`PASTEL_BLUE` (`#9BC7E4`):** Cabeceras de fases y zonas de red.
* **`PASTEL_GREEN` (`#C2E5D3`):** Confirmaciones y estados exitosos.

---

## Suite de Pruebas y Validacion

Ejecucion de pruebas automatizadas:

```bash
# Validacion de regresion visual
python3 tests/test_visual_regression.py

# Stress testing de alta densidad
python3 tests/test_stress.py

# Benchmark de fidelidad integral
python3 tests/benchmark_dogfooding.py
```
