# ⚙️ ANATOMÍA INTERNA DE SKETION 4.0: CÓMO FUNCIONA EL MOTOR

> **La tesis de Sketion:**  
> *"La IA no debe diseñar desde cero ni dibujar píxeles al azar. La IA debe comprender la semántica del problema y compilarla en un sistema visual estructurado, determinista, proporcional y 100% editable en Excalidraw."*

---

## 🏛️ La Arquitectura de 4 Capas Desacopladas

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        PIPELINE DE COMPILACIÓN VISUAL DE SKETION 4.0                   │
│                                                                                        │
│   [PROMPT O DOCUMENTO]                                                                 │
│            │                                                                           │
│            ▼                                                                           │
│   ┌──────────────────────────────────────────────────────────────────────────────┐     │
│   │ CAPA 1: MOTOR SEMÁNTICO & INFERENCIA DE AUDIENCIA                            │     │
│   │ • Extrae entidades, jerarquías, relaciones y restricciones duras             │     │
│   │ • Identifica la audiencia (CEO, Operaciones, Tech, Data, Inversionistas)     │     │
│   │ • Genera la Representación Intermedia (IR Schema en JSON)                    │     │
│   └──────────────────────────────────────┬───────────────────────────────────────┘     │
│                                          │                                             │
│                                          ▼                                             │
│   ┌──────────────────────────────────────────────────────────────────────────────┐     │
│   │ CAPA 2: MOTOR DE ARQUETIPOS & ENRUTADOR VISUAL                               │     │
│   │ • Mapea al arquetipo óptimo entre los 20 de Negocio (A - T) o 27 Tipos       │     │
│   │ • Aplica la Regla Anti-Monocultivo (prohíbe repetir layouts en multi-frame)  │     │
│   └──────────────────────────────────────┬───────────────────────────────────────┘     │
│                                          │                                             │
│                                          ▼                                             │
│   ┌──────────────────────────────────────────────────────────────────────────────┐     │
│   │ CAPA 3: MOTOR GEOMÉTRICO, TOKENS & ESCALADO TIPOGRÁFICO                      │     │
│   │ • Calcula coordenadas absolutas (x, y, w, h), gaps (95px) y gutters (65px)   │     │
│   │ • Aplica Tipografía Proporcional (18-20px en tarjetas, 14px en tablas)       │     │
│   │ • Ruteo ortogonal de conectores a 90° con pastillas protectoras de texto     │     │
│   │ • Aplica la Regla del Acento Único (1 héroe focal por frame)                 │     │
│   └──────────────────────────────────────┬───────────────────────────────────────┘     │
│                                          │                                             │
│                                          ▼                                             │
│   ┌──────────────────────────────────────────────────────────────────────────────┐     │
│   │ CAPA 4: RENDER NATIVO, VALIDADOR 6D & BUCLE DE AUTO-REPAIR                   │     │
│   │ • Genera JSON nativo Excalidraw (boundElements bidireccionales, fontFamily=2)│     │
│   │ • Inspecciona 6 dimensiones de calidad (Structure, Layout, Noise, etc.)      │     │
│   │ • Bucle de Auto-Repair: Si Score < 90, autocorrige y re-inyecta (máx 3 veces)│     │
│   └──────────────────────────────────────┬───────────────────────────────────────┘     │
│                                          │                                             │
│                                          ▼                                             │
│                     [ARTEFACTO NATIVO .EXCALIDRAW (100% EDITABLE)]                     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔬 Las 4 Capas en Detalle Forense

### Capa 1: El Analizador Cognitivo (Semántica & Audiencia)
1. **Extracción de Nodos:** Descompone el texto libre en sustantivos operativos (*servicios, bases de datos, actores, fases*).
2. **Restricciones Duras (Hard Constraints):** Identifica dependencias que jamás deben romperse (ej. *Supabase debe alimentar al ExamBuilder, no al revés*).
3. **Audience-Aware Engine:**
   * Si detecta **CEO/Directivo:** Prioriza ROI, elimina puertos y endpoints técnicos, selecciona Arquetipos D (Duelo) o B (Fases).
   * Si detecta **Ingeniería/Tech:** Detalla VPCs, bases de datos, colas, selecciona Arquetipo Layer Stack o A (El Cerebro).

---

### Capa 2: El Enrutador Estructural (20 Arquetipos & 27 Tipos Visuales)
* En lugar de dibujar rectángulos aleatorios, Sketion tiene una biblioteca geométrica especializada:
  * **Ecosistemas:** Arquetipo A (*Hub Radial / El Cerebro*).
  * **Infraestructura:** Arquetipo *Layer Stack* (Pila horizontal de 4 capas).
  * **Algoritmos / Procesos:** Arquetipo C (*Flow Pipeline con feedback*).
  * **Roadmaps:** Arquetipo G (*Escalera de Madurez de 5 Niveles*) + Matriz de Horizontes.
  * **Comparativas:** Arquetipo D (*El Duelo VS*) o Arquetipo S (*Matriz Tabular*).
  * **Workshops:** Arquetipo *Workshop Canvas* (Post-its libres + Checklists).
* **Regla Anti-Monocultivo:** Valida que en diagramas con varios marcos, ningún marco use la misma plantilla que el anterior.

---

### Capa 3: El Calculador Espacial (Geometría, Tokens & Tipografía)
* **Gaps Editoriales Calibrados:** Mantiene márgenes de `95px` entre bloques mayores y `65px` entre tarjetas.
* **Escalado Tipográfico Proporcional:**
  * Tarjetas amplias ($w \ge 380\text{px}$): Título a **`20px Bold`**.
  * Tarjetas estándar: Título a **`18px Semi-bold`**.
  * Subtítulos técnicos: **`13-14px Regular`**.
  * Celdas de tablas: **`13-14px`**.
  * Badges de rol: **`11-12px Mono`**.
* **Conectores Ortogonales con Track Lanes:** Flechas con codos a 90° que no atraviesan cajas y llevan una pastilla protectora blanca (`pill label`) para evitar colisiones.
* **1 Accent Rule:** Reserva el color focal (Coral `#D93829`, Verde `#059669` o Cobalto `#2563EB`) exclusivamente para 1 o 2 componentes héroe.

---

### Capa 4: El Compilador, Validador 6D & Auto-Repair
* **Enlace Bidireccional de Texto:**
  * Rectángulo: `"boundElements": [{"id": "txt_1", "type": "text"}]`
  * Texto: `"containerId": "rect_1"`, `"textAlign": "center"`, `"verticalAlign": "middle"`, `"autoResize": true`.
* **Validador de 6 Dimensiones:**
  1. *Structure (100 pts):* Integridad de IDs y texto vinculado.
  2. *Layout (100 pts):* Ausencia de solapamientos y márgenes seguros.
  3. *Readability (100 pts):* Contraste y tamaño de fuente proporcional.
  4. *Hierarchy (100 pts):* Respeto estricto del presupuesto de acentos (1-3 por frame).
  5. *Visual Noise / Densidad (100 pts):* Curva calibrada en `4.0/10`.
  6. *Brand Consistency (100 pts):* Uso exclusivo de tokens semánticos aprobados.
* **Bucle Autónomo de Auto-Repair:** Si el Validador detecta sobrecarga de acentos o solapamiento, el motor ejecuta hasta 3 iteraciones autónomas de corrección antes de entregar el archivo.
