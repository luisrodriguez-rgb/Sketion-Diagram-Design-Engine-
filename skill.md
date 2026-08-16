---
name: sketion-diagram-design
description: Generador editorial de diagramas y tableros nativos para Excalidraw (.excalidraw). Arquitectura desacoplada en 4 capas (Semántica -> Layout -> Render -> Calidad Visual) con soporte de Smart Defaults, niveles de detalle (Simple/Balanced/Detailed) y 27 tipos visuales.
license: MIT
metadata:
  version: "2.7"
---

# Sketion Diagram Design Skill (Motor Editorial para Excalidraw)

Crea tableros y diagramas profesionales con calidad editorial, diseño limpio y editabilidad nativa total en formato `.excalidraw`.

Inspirado en los principios editoriales de **Diagram Design** (densidad visual 4/10, regla del acento único, eliminación de ruido visual) combinado con la potencia geométrica y modular del motor de **Sketion**.

---

## 0. Smart Defaults & Progressive Disclosure (Sin Fricción)

**No interrumpir al usuario con preguntas si no son necesarias.** El motor resuelve automáticamente:

- **Si el usuario especifica:** Respetar sus elecciones (paleta, roughness, detalle, modo).
- **Si existe configuración de marca / branding:** Aplicar los tokens correspondientes.
- **Si no se especifica nada (Smart Defaults automáticos):**
  - **Modo:** Claro (`viewBackgroundColor: "#FFFFFF"` con supervivencia a inversión).
  - **Trazo (`roughness`):** `0` (Limpio, técnico, vectorial).
  - **Paleta:** `JET_EDITORIAL` (`#FFFFFF` base, `#0F172A` tinta, `#2563EB` acento cobalto).
  - **Nivel de Detalle:** `balanced`.
- **¿Cuándo preguntar?** Únicamente ante una ambigüedad semántica crítica sobre el contenido o flujo de negocio.

---

## 1. Filosofía Editorial

> **"El movimiento de mayor calidad es la eliminación."**
> Un diagrama no está terminado cuando no hay nada más que añadir, sino cuando no queda nada que se pueda suprimir.

- **Densidad objetivo: 4/10:** Espacio en blanco respirable (`gap` generoso). Si un frame tiene más de 9 nodos principales, **dividirlo en Visión General + Detalle**.
- **Regla del Acento Único (1 Accent Rule):** El color de acento (`ACCENT`) se reserva exclusivamente para **1 o 2 nodos focales** (el servicio crítico, el estado actual o el héroe).
- **Cero "AI Slop":** Sin degradados morados/cian, sin sombras difusas, sin emojis decorativos (usar texto corto coloreado `SI/NO/PARCIAL`), sin cajas idénticas repetidas sin jerarquía.
- **Conectores Ortogonales:** Flechas y líneas con codos a 90º o alineación recta. Nunca diagonales arbitrarias que crucen cajas.
- **Jerarquía Tipográfica:**
  - `fontFamily: 2` (Normal/Helvetica): 95% del contenido (tarjetas, títulos, descripciones).
  - `fontFamily: 3` (Cascadia/Code): Exclusivo para puertos, parámetros, endpoints, SQL types.
  - `fontFamily: 1` (Virgil): Solo para boceto informal o títulos de marca cuando se pide `roughness: 1`.

---

## 2. Pipeline en 4 Capas Desacopladas

```text
                  PROMPT / IDEA DEL USUARIO
                             ↓
       ┌───────────────────────────────────────────┐
       │ 1. MODELO SEMÁNTICO (semantic/models.py)   │
       │    - Intención: Fan-in, Paved Road, etc.   │
       │    - Nivel de Detalle: Simple/Balanced/Full│
       │    - JSON intermedio desacoplado           │
       └─────────────────────┬─────────────────────┘
                             ↓
       ┌───────────────────────────────────────────┐
       │ 2. MOTOR DE LAYOUT (layout/)              │
       │    - flow.py / hierarchy.py / grid.py      │
       │    - routing.py (Conectores ortogonales)   │
       └─────────────────────┬─────────────────────┘
                             ↓
       ┌───────────────────────────────────────────┐
       │ 3. RENDER EXCALIDRAW (render/)            │
       │    - Vinculación containerId <-> bound    │
       │    - Aplicación de Tokens de style-guide   │
       │    - Serialización JSON minificada         │
       └─────────────────────┬─────────────────────┘
                             ↓
       ┌───────────────────────────────────────────┐
       │ 4. QUALITY VALIDATOR & REPAIR (validation)│
       │    - Visual Quality Score (Densidad 4/10) │
       │    - Semantic Fidelity Score (Coverage)   │
       │    - Self-Correction Loop (Repair Engine) │
       └─────────────────────┬─────────────────────┘
                             ↓
                ARCHIVO .excalidraw EDITABLE
```

---

## 3. Niveles de Detalle (Detail Levels)

1. **Simple:** Resumen de alto nivel ($3 - 5$ nodos). Ideal para resúmenes ejecutivos o pitch decks (`User -> App -> DB`).
2. **Balanced (Default):** Flujo completo de producción ($6 - 8$ nodos). Muestra servicios clave, autenticación, storage y dependencias.
3. **Detailed:** Arquitectura exhaustiva ($9 - 12+$ nodos). Incluye colas, caches, workers, réplicas y tags de red.

---

## 4. Los 9 Motores Visuales Base

| Motor | Estructura Visual | Casos de Uso Semánticos | Slug |
| :--- | :--- | :--- | :--- |
| **Cerebro** | Hub elíptico central + ramas radiales | Visión, persona ideal, hub de conceptos, flywheel / loop | `cerebro` |
| **Flujo** | Secuencia horizontal con flechas | Procesos, data pipelines, sequence, user journey, funnels | `flujo` |
| **Red** | Nodos distribuidos y agrupados | Arquitectura cloud, microservicios, state machines, high-level | `red` |
| **Matriz** | Grilla con cabeceras de fila y columna | Comparativas, SWOT, cuadrante 2x2, matriz de seguridad | `matriz` |
| **Árbol** | Jerarquía descendente (Nivel 1 $\rightarrow$ 2) | Org charts, sitemaps, árboles de decisión, taxonomías | `arbol` |
| **Timeline** | Eje horizontal continuo con hitos | Roadmaps, cronogramas, historial de releases, Gantt | `timeline` |
| **Board** | Carriles verticales con cabecera Post-It | Kanban, swimlanes, IT current-state, categorización | `board` |
| **Dashboard** | Chips oscuros con número gigante | KPIs, métricas clave, resúmenes cuantitativos, conteos | `dashboard` |
| **Storyboard** | Frames 1600×900 secuenciales | Pitch decks, resúmenes ejecutivos, diapositivas de canvas | `storyboard` |

---

## 5. Checklist de Calidad antes de Entregar

- [ ] ¿El archivo tiene extensión `.excalidraw` y es JSON válido minificado?
- [ ] ¿`roughness` es coherente con lo solicitado (`0` técnico o `1` boceto)?
- [ ] ¿Todos los rectángulos con texto tienen su `containerId` y `boundElements` sincronizados?
- [ ] ¿Se respetó la **regla del acento único** (máximo 1-2 nodos con color de acento)?
- [ ] ¿La densidad visual es baja y respirable (aprox 4/10, sin amontonar tarjetas)?
- [ ] ¿Los conectores son ortogonales y no atraviesan cajas innecesariamente?
- [ ] ¿No se usaron emojis decorativos ni degradados?
- [ ] ¿El validador `validate_scene()` devuelve `PASS` con puntuación global $\ge 90/100$?

---

## 6. Referencias Modulares del Skill

- Tokens de Diseño y Paletas: [references/style-guide.md](references/style-guide.md)
- Patrones Semánticos y Comportamiento: [references/semantic-patterns.md](references/semantic-patterns.md)
- Catálogo de los 27 Tipos Visuales: [references/types-catalog.md](references/types-catalog.md)
- Reglas de Layout y Enrutamiento: [references/layout-rules.md](references/layout-rules.md)
- Reglas de Calidad y Validación: [references/quality-rules.md](references/quality-rules.md)
- Hoja de Ruta Estratégica: [docs/10-architectural-improvements.md](docs/10-architectural-improvements.md)
