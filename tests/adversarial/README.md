# 🥋 Suite de Pruebas Adversariales de Sketion (Fase V4)

**Evaluación de Criterio Semántico, Juicio Visual y Decision-Making Autónomo.**

---

## 🎯 Objetivo de la Suite

A partir de Sketion 3.3, el desafío no es *"qué más puede renderizar el motor"*, sino **"qué tan bien decide el motor qué debe hacer ante problemas complejos, ambiguos y contradictorios"**.

Esta suite somete a Sketion a **9 escenarios adversariales extremos** donde no se le indican arquetipos, layouts ni instrucciones de maquetación previas.

---

## ⚖️ El Principio de "Semantic Hard Constraints"

Cuando la **Calidad Visual** y la **Fidelidad Semántica** entran en conflicto, Sketion aplica una jerarquía estricta:

```text
                 ┌────────────────────────────────┐
                 │    SEMANTIC HARD CONSTRAINTS   │
                 │ (Inviolables por Estética)     │
                 └───────────────┬────────────────┘
                                 │
         ┌───────────────────────┴───────────────────────┐
         ▼                                               ▼
[FATAL HARD FAILURES]                           [REPARACIONES PERMITIDAS]
• Nodo Crítico Faltante (ej. Ledger)             • Auto-Split en Multi-Frame
• Relación/Arista Crítica Omitida               • Degradación de Acento (>2)
• Transición de Estado Inválida                 • Espaciado elástico de Gaps
• Violación de Inmutabilidad                    • Enrutamiento por Track Lanes
```

> **Regla de Oro:** Un diagrama visualmente impecable (100/100) pero con omisión de un componente de dominio crítico es un **HARD FAILURE INMEDIATO**. La fidelidad semántica manda sobre la estética.

---

## 📋 Los 9 Escenarios Adversariales

1. [`01_ambiguous_process.md`](01_ambiguous_process.md) — Información sin estructura visual explícita (*AS-IS $\rightarrow$ Pain Points $\rightarrow$ TO-BE $\rightarrow$ Metrics*).
2. [`02_multi_perspective.md`](02_multi_perspective.md) — Información que exige múltiples perspectivas y separación obligatoria en frames.
3. [`03_semantic_vs_visual.md`](03_semantic_vs_visual.md) — Conflicto directo entre densidad visual y preservación exhaustiva de relaciones.
4. [`04_same_information_different_audience.md`](04_same_information_different_audience.md) — El mismo problema para 5 audiencias (CTO, Diseñador, Gerente, Devs, Pitch 5 min).
5. [`05_extreme_hierarchy.md`](05_extreme_hierarchy.md) — Jerarquías profundas multinivel y sistemas anidados.
6. [`06_extreme_density.md`](06_extreme_density.md) — Sobresaturación masiva y detección automática de descomposición elástica.
7. [`07_missing_information.md`](07_missing_information.md) — Información incompleta, estimación transparente y supresión de placeholders vacíos.
8. [`08_conflicting_requirements.md`](08_conflicting_requirements.md) — Requisitos contradictorios de negocio vs técnicos (Latencia vs Consistencia ACID).
9. [`09_real_world_messy_input.md`](09_real_world_messy_input.md) — Transcripciones orales caóticas de reuniones de Zoom / Loom.
