# Sketion Diagram Design Engine — Hoja de Ruta Estratégica (Roadmap v3.4 -> v4.0)

Este documento define la secuencia técnica y estratégica para consolidar a **Sketion** como el estándar de comunicación visual y diseño automatizado de diagramas editoriales.

---

## Estado Actual (Versión 3.4)

* **Capas Core:** Modelo Semántico -> Layout Geométrico -> Render Excalidraw Nativo -> Quality Validator.
* **Infraestructura Geométrica:** 9 Motores de Layout Base (Flow, Timeline, Tree, Radial, Grid, Board, Dashboard, Network, Routing).
* **Catálogo de Negocio:** 20 Arquetipos Visuales (El Duelo, Las Fases, El Cerebro, La Serpiente, La Cebolla, etc.).
* **Novedad v3.4:** Motor de Inferencia por Audiencia (`engines/audience.py`), Simetría 1:1 en User Journeys y Enrutamiento de Flujo Físico Inter-Zonas.
* **Pruebas de Validación:** Pruebas V3 (Miro Toolkit), Pruebas V4 (Onboarding, Universidad, Pagos) y Pruebas V5 (Benchmark de 3 Audiencias).

---

## Fases del Roadmap

```text
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 ROADMAP SKETION (v3.4 ───> v4.0)                                       │
├────────────────────────────┬────────────────────────────┬────────────────────────────┬─────────────────┤
│ FASE 1: BENCHMARK RUNNER   │ FASE 2: AUDIENCE PIPELINE  │ FASE 3: AUTO-SPLIT ELÁSTICO│ FASE 4: SKILL   │
│ • Ejecución de 9 Tests     │ • Inferencia automática    │ • Descomposición autónoma  │   DISTRIBUCIÓN  │
│   Adversariales            │   de audiencia en prompt   │   cuando densidad > 5.5/10 │ • CLI de Sketion│
│ • Scoring de Decisión      │ • Enrutador de arquetipos  │ • Enlace visual entre      │ • Comando Slash │
│ • Detección de Hard Fails  │ • Filtro semántico por rol │   frames coordinados       │ • Marketplace   │
└────────────────────────────┴────────────────────────────┴────────────────────────────┴─────────────────┘
```

---

### Fase 1: Automatización del Banco de Pruebas Adversariales (Tests 01 a 09)
**Objetivo:** Crear un ejecutor automatizado (`tests/adversarial_runner.py`) que procese los 9 casos de prueba adversariales y emita un reporte cuantitativo de decisión y fidelidad.

* **Entregables:**
  1. `tests/adversarial_runner.py`: Script que lee cada `tests/adversarial/0X_*.md`, genera la escena `.excalidraw` y valida las rúbricas PASS/FAIL.
  2. Evaluación de **Semantic Hard Constraints**: Validación automática de que ningún nodo crítico (ej. Ledger, CISO approval) sea eliminado por estética.
  3. Matriz de regresión de toma de decisiones autónoma.

---

### Fase 2: Integración Nativa del Motor de Audiencia en el Pipeline End-to-End
**Objetivo:** Permitir que el pipeline reconozca automáticamente la audiencia implícita o explícita en el prompt y aplique el perfil correspondiente.

* **Entregables:**
  1. Integración en `semantic/` para detectar frases como *"para el director general"*, *"diagrama para developers"*, *"plano de planta para operaciones"*.
  2. Activación automática del arquetipo óptimo (Duelo/Fases para CEO, Planta/Takt para Ops, Cloud/Journey para Tech).
  3. Supresión inteligente de ruido según el perfil de audiencia (ocultar microservicios al CEO, ocultar finanzas macro al equipo de desarrollo).

---

### Fase 3: Auto-Split Elástico y Detección Automática de Sobresaturación
**Objetivo:** Evitar que prompts complejos y masivos colapsen en un solo frame saturado mediante particionado automático.

* **Entregables:**
  1. Algoritmo de particionado cuando $\text{Nodos} > 15$ o $\text{Densidad Proyectada} > 5.5/10$.
  2. Creación automática de Frames especializados:
     * Frame 1: Topología / Arquitectura Macro.
     * Frame 2: Flujo Secuencial / Journey.
     * Frame 3: Matriz de Gobernanza / Datos.
     * Frame 4: Dashboard de Rendimiento / Métricas.
  3. Trazado de líneas de conexión y referencias visuales entre marcos.

---

### Fase 4: Empaquetado, CLI y Distribución como Skill Global
**Objetivo:** Hacer de Sketion una herramienta de línea de comandos y un plugin portable para cualquier entorno de desarrollo y agente de IA.

* **Entregables:**
  1. **CLI Unificado:**
     ```bash
     sketion generate "prompt.txt" --audience ceo --output decision_board.excalidraw
     ```
  2. **Integración con Antigravity IDE:** Slash command `/sketion` para generar y visualizar tableros directamente en el workspace.
  3. **Visualizador Rápido:** Script de exportación automática a SVG/PNG de alta fidelidad para vista previa instantánea.

---

## Resumen de Prioridades Inmediatas

| Prioridad | Tarea | Impacto |
| :-: | :--- | :--- |
| **P1** | Implementar `tests/adversarial_runner.py` para correr los 9 casos adversariales. | Evalúa el cerebro de Sketion de forma 100% automatizada. |
| **P2** | Conectar `engines/audience.py` con el parser del modelo semántico. | Permite inferir audiencias automáticamente sin código manual. |
| **P3** | Afinar el Auto-Split elástico para lienzos con más de 20 componentes. | Garantiza densidad 4/10 en cualquier escenario extremo. |
