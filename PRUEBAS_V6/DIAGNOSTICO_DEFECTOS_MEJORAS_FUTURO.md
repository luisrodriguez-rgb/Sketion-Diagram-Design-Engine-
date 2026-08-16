# 📋 DIAGNÓSTICO FORENSE CORREGIDO, REESTRUCTURACIÓN DEL ROADMAP Y COMPOSITION INTELLIGENCE — SKETION 4.x / 5.0

> **Documento:** Auditoría Crítica de Inteligencia de Composición, Métricas de Dependencia y Reestructuración de Prioridades  
> **Ámbito:** Sketion Engine Core & Evaluación de Generalización Autónoma  
> **Fecha:** 16 de Agosto, 2026  
> **Estado:** Aprobado para Ejecución

---

## 1. 🎯 El Cambio de Paradigma: De "Motor que Pasa sus Propias Pruebas" a "Inteligencia de Diseño"

### La Crítica Fundamental
Tener un `Quality Score >= 90/100` en fixtures controlados no demuestra que el motor sea un buen diseñador; solo demuestra que los casos seleccionados satisfacen las reglas del validador. 

Para evitar el sesgo de auto-validación (*crear feature $\rightarrow$ crear fixture $\rightarrow$ modificar validador $\rightarrow$ fixture pasa $\rightarrow$ declarar éxito*), el sistema debe desacoplar tres niveles de evaluación:

```text
                     SKETION ENGINE
                           │
              ┌────────────┼────────────┐
              ↓            ↓            ↓
          Semántica     Geometría    Editorial
              │            │            │
              └────────────┼────────────┘
                           ↓
                      .excalidraw
                           │
                 ┌─────────┴─────────┐
                 ↓                   ↓
           Machine Audit        Human Review
                 │                   │
                 └─────────┬─────────┘
                           ↓
                    CALIDAD FINAL
```

---

## 2. 🔬 Corrección Forense de los Defectos Detectados

### A. Defecto #1: Hierarchical Accent Model (No solo aislamiento por frame)
* **Error del enfoque simple:** Aislar acentos por `frame_id` permite que si hay 4 frames, cada uno tenga 2 héroes (8 héroes en total). La máquina da `100/100`, pero visualmente el lienzo es un árbol de navidad sin clímax narrativo.
* **Solución (Hierarchical Accent Model):**
  * **Intra-frame:** Máximo 1 Héroe Focal + 0–1 Secundario.
  * **Cross-frame:** Jerarquía narrativa global (*Frame 1 Contexto $\rightarrow$ Frame 2 Núcleo / Clímax Heroico $\rightarrow$ Frame 3 Conclusión/Outcome*). No todos los frames compiten con la misma intensidad visual.

### B. Defecto #2: Target de Densidad Inferido Dinámicamente
* **Error del enfoque simple:** Poner flags manuales como `density_mode="executive"`.
* **Solución (Inferred Density Target):** La densidad óptima es una variable derivada autónomamente de:
  $$\text{Target Density} = f(\text{Audiencia}, \text{Intención del Diagrama}, \text{Complejidad Semántica}, \text{Arquetipo}, \text{Nº de Marcos})$$
  * *Ejemplo 1:* CEO + Estrategia + Hub Radial (6 nodos) $\rightarrow$ $\text{Target Density} \approx 2.0/10$.
  * *Ejemplo 2:* Arquitecto Cloud + Infraestructura + 25 microservicios $\rightarrow$ $\text{Target Density} \approx 5.5/10$.

### C. Defecto #3: Semantic Text Decomposer (Antes del Layout)
* **Error del enfoque simple:** Forzar textos largos a más líneas o tarjetas gigantescas.
* **Solución:** Clasificar la naturaleza del texto antes de pasarlo al motor geométrico:
  ```text
  Raw Input Text ──► [Classifier] ──► { Title, Subtitle, Metadata Pill, Bullet List, Metric, Callout/Warning } ──► Layout
  ```

### D. Defecto #4: AnchorGeometry (Abstracción Polimórfica de Fronteras)
* **Solución:** Abstraer el cálculo de intersección perimetral más allá de simples rectángulos:
  ```python
  class AnchorGeometry:
      def get_boundary_intersection(self, shape_type: str, source_point: Tuple[float, float], target_point: Tuple[float, float]) -> Tuple[float, float]:
          # Ray-shape clipping para Rectangles, RoundedRects, Diamonds, StickyNotes, Scopes y Circles
          ...
  ```

---

## 3. 📊 Nuevas Métricas Obligatorias del Sistema

### 1. Repair Dependency Score (RDS)
Evalúa si el generador inicial produjo un buen diseño o si el `Auto-Repair` tuvo que parchar el diagrama para salvarlo:
$$\text{RDS} = \sum (\text{Severidad de Reparación} \times \text{Nº de Correcciones}) \times \text{Iteraciones}$$

| Rango RDS | Diagnóstico del Generador |
| :---: | :--- |
| **0 – 10** | **Excelente:** El generador colocó la geometría casi perfecta al primer intento. |
| **11 – 25** | **Saludable:** Ajustes menores de espaciado o degradación de 1 acento. |
| **26 – 50** | **Frágil:** Alta dependencia del bucle de auto-corrección. |
| **> 50** | **Fallo de Generador:** El motor inicial colocó mal los elementos y el repair tuvo que rehacerlo. |

### 2. Composition Fitness Score (CFS)
Mide la idoneidad de la estructura geométrica elegida frente a la intención semántica del prompt:
* ¿Un problema de causa-raíz eligió Ishikawa en vez de un Flow genérico?
* ¿Una comparativa de mercado eligió El Duelo (VS) o Matriz Tabular en vez de un Grid?

### 3. Human Editorial Benchmark (Rúbrica Humana 1 - 10)
1. ¿Entiendo qué estoy viendo en los primeros 5 segundos?
2. ¿Sé dónde mirar primero (foco visual inequívoco)?
3. ¿La jerarquía narrativa tiene sentido de izquierda a derecha?
4. ¿Las relaciones y flechas son fáciles de seguir sin esfuerzo cognitivo?
5. ¿Parece diseñado por un consultor senior o generado por un bot rígido?

---

## 🧭 4. Roadmap Corregido y Repriorizado (Enfoque en Inteligencia)

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        ROADMAP CORREGIDO: SKETION ENGINE CORE                          │
└────────────────────────────────────────────────────────────────────────────────────────┘

 🔴 P0 — COMPOSITION INTELLIGENCE (Prioridad Máxima Absoluta)
   1. Archetype Fitness & Composition Decision Engine (Selección inteligente de arquetipo).
   2. Semantic Text Decomposer (Clasificación de texto en título/subtítulo/lista/callout antes de layout).
   3. Hierarchical Accent Model (Jerarquía intra-frame y narrativa cross-frame).
   4. Automatic Inferred Density Targets (Densidad derivada de audiencia y complejidad).

 🟡 P1 — GEOMETRY & EVALUATION
   5. AnchorGeometry (Ray-Shape intersection para rectángulos, círculos, rombos, post-its).
   6. Collision-Aware Orthogonal Routing (Evitación de obstáculos y carriles dedicados).
   7. Repair Dependency Score (RDS) integrado en el reporte de validación.
   8. Human Editorial Benchmark Suite.
   9. Adaptive Canvas Reflow (Dividir o reajustar si el contenido satura el marco).

 🔵 P2 — ADVANCED RENDERING
   10. UI Skeletons & Wireframe Component System (Esquemas de interfaz semánticos).
   11. Dark Mode Token Engine (Conmutación automática de paleta).
   12. Rich Icon Resolver Expansion.

 ⚪ P3 — INFRASTRUCTURE & ECOSYSTEM (Congelado hasta madurar P0 y P1)
   13. Headless PNG / SVG Export.
   14. Sketion CLI Tool.
   15. .excalidrawlib Library.
   16. VS Code / Cursor Extension.
   17. Reverse Engineering (Canvas a Código).
```

---

## 🧪 5. El Benchmark de Generalización Autónoma ("The Zero-Hint Test")

A partir de ahora, la prueba definitiva de Sketion consiste en alimentarlo con **prompts no estructurados del mundo real**, sin darle ninguna directiva de diseño (sin decirle qué arquetipo usar, cuántos frames crear ni qué fuentes o colores poner), y auditar qué decisiones toma el motor de forma 100% autónoma.
