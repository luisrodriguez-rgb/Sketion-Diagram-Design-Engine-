# Sketion Semantic Patterns (Intención y Comportamiento)

Los **patrones semánticos** describen **qué está ocurriendo en el sistema / información** antes de decidir cómo dibujarlo. La forma visual debe ser consecuencia de la estructura de los datos, nunca una elección aleatoria de cajas.

---

## 1. Tabla de Enrutamiento Semántico

| Lo que el usuario intenta explicar… | Patrón Semántico | Motor Visual Sketion | Slug Motor |
| :--- | :--- | :--- | :--- |
| Muchos productores compitiendo por capacidad finita o cuello de botella | **Fan-in Queue / Bottleneck** | `flujo` o `red` | `flujo` / `red` |
| Preguntas, entradas, controles y salidas repetidas en fases secuenciales | **Stage Framework con Slots** | `board` o `flujo` | `board` / `flujo` |
| Diálogo suelto / ideas desordenadas transformándose en un artefacto estructurado | **Unstructured Input $\rightarrow$ Artifact** | `flujo` | `flujo` |
| Comparativa de dos caminos/políticas y dónde divergen (Pass/Fail) | **Paired Policy Traces** | `matriz` o `flujo` | `matriz` / `flujo` |
| Componentes con límites de seguridad y rutas permitidas vs bloqueadas | **Secure Paved Road** | `red` o `arbol` | `red` / `arbol` |
| Controles agrupados por capa de abstracción / responsabilidad | **Governance & Layer Stack** | `matriz` o `board` | `matriz` / `board` |
| Concepto central con atributos satelitales / Persona / Propósito | **Hub Central & Radiación** | `cerebro` | `cerebro` |
| Evolución temporal, hitos, roadmaps con dependencias secuenciales | **Timeline & Milestones** | `timeline` | `timeline` |
| Métricas cuantitativas clave / KPIs de estado | **Dashboard de Impacto** | `dashboard` | `dashboard` |
| Presentación ejecutiva paso a paso / Diapositivas en lienzo | **Storyboard** | `storyboard` | `storyboard` |

---

## 2. Presupuesto de Complejidad (Complexity Budget)

Para evitar el "ruido visual" y mantener la densidad editorial **4/10**:

- **Límite de Nodos Primarios:** Máximo **7 a 9 nodos principales** por frame. Si hay más de 9 elementos, se divide en 2 frames (Visión General + Detalle).
- **Límite de Conexiones:** Cada flecha debe comunicar una transferencia real de datos, control o dependencia. Eliminar flechas obvias.
- **Jerarquía de Color:**
  - 1 nodo con `ACCENT` (el héroe / núcleo).
  - 1 nodo con `PAIN` (si hay un cuello de botella o problema a resaltar).
  - Todos los demás nodos en neutro (`PAPER_CARD` + `INK` + `MUTED`).

---

## 3. Guía de Selección Rápida en 3 Pasos

```text
1. ¿El contenido tiene eje temporal o de etapas?
   ├── SÍ: ¿Son fechas/meses? ──> TIMELINE
   │       ¿Son etapas/pasos de un proceso? ──> FLUJO
   │       ¿Son diapositivas de pitch? ──> STORYBOARD
   └── NO: Continuar a paso 2.

2. ¿El contenido es comparativo o tabular?
   ├── SÍ: ¿Tiene filas y columnas (SWOT, 2x2, Features)? ──> MATRIZ
   │       ¿Son columnas/carriles de estado (Kanban, Roles)? ──> BOARD
   └── NO: Continuar a paso 3.

3. ¿El contenido es estructural o relacional?
   ├── SÍ: ¿Tiene un concepto central dominante? ──> CEREBRO
   │       ¿Tiene jerarquía descendente (Nivel 1 -> 2)? ──> ÁRBOL
   │       ¿Son métricas/KPIs numéricos? ──> DASHBOARD
   └── Por descarte: Sistema distribuido o arquitectura ──> RED
```
