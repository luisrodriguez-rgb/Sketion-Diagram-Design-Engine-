# Sketion Diagram Design Engine (v8.0)

**Motor editorial de diseño y generación de diagramas inteligentes, libres de amontonamientos y 100% editables en formato nativo `.excalidraw`.**

> **Official Core Certification (Sketion 8.0 — Tri-Intelligence System FROZEN):**  
> *Sketion 8.0 has successfully passed the Grand Holdout End-to-End Benchmark across 160 blind runs (40 novel scenarios x 4 audience-goal matrices), achieving **Quality Score: 96.0/100**, **Render Fidelity: 89.0/100**, **ATS: 96.0/100**, **PFR: 81.4%**, **RDS: 0.00**, and **0.0% Crashes**.*

---

> [!IMPORTANT]
> ### 📖 ¿Cómo usar Sketion según tu caso o plataforma?
> Para saber exactamente cómo configurar, integrar y usar Sketion en tu entorno particular (**Antigravity IDE, ChatGPT Gratuito vs Plus, Claude Pro vs Free, Cursor, Windsurf, Terminal CLI local, VS Code o Excalidraw Web**), lee nuestra guía maestra paso a paso:
> 👉 [**GUIA_DE_USO_UNIVERSAL.md**](GUIA_DE_USO_UNIVERSAL.md) (o en [`docs/GUIA_DE_USO_UNIVERSAL.md`](docs/GUIA_DE_USO_UNIVERSAL.md))
> *Incluye: Matriz de Costos (Planes Gratuitos vs Pago), Comparativa de Calidad (Tier 1 Python vs Tier 3 Web LLM), Métodos 100% Gratis sin suscripción y Plantillas de Prompts.*

---

## 🏛️ Arquitectura del Sistema

Inspirado en los principios de diseño de **Diagram Design** (densidad visual 4/10, regla del acento único, conectores ortogonales a 90 grados) y construido sobre una **arquitectura desacoplada de 3 Inteligencias Integradas**:
1. **Composition Intelligence** (Modelado Narrativo & Oracle Composition Judge FROZEN 1.0).
2. **Rendering Intelligence** (AnchorGeometry, Routing Ortogonal 90°, Confinamiento de Frames & Cero Colisiones).
3. **Information Architecture Intelligence** (Ranking de Importancia de 5 Tiers & Progressive Disclosure).

---

## ⚡ Instalación Rápida y Formas de Uso

### Opción 1: Instalación en 1 Comando para Agentes y Terminal (Antigravity / Cursor / Windsurf / Claude Code)
Ejecuta en tu terminal para instalar Sketion como Skill Global y habilitar el comando `sketion`:
```bash
curl -fsSL https://raw.githubusercontent.com/luisrodriguez-rgb/Sketion-Diagram-Design-Engine-.git/main/install.sh | bash
```

### Opción 2: Instalación como Paquete Python (CLI Global)
```bash
pip install git+https://github.com/luisrodriguez-rgb/Sketion-Diagram-Design-Engine-.git
```
Luego puedes usarlo en cualquier carpeta de tu equipo:
```bash
# Listar los 20 arquetipos visuales disponibles:
sketion types

# Generar un diagrama de Lakehouse Medallion con acabado editorial:
sketion generate "Arquitectura Lakehouse E-Commerce" --type medallion --output lakehouse.excalidraw --validate

# Validar calidad visual y reparar automáticamente cualquier archivo existente:
sketion validate mi_diagrama.excalidraw

# Ejecutar el benchmark integral de pruebas:
sketion benchmark
```

---

## 🏛️ Catálogo de los 20 Arquetipos Visuales de Negocio (A - T)

Sketion implementa un catálogo exhaustivo de 20 arquetipos de diseño para resolver cualquier problema de comunicación técnica, estratégica y operativa:

| Código | Arquetipo | Motores Geométricos | Caso de Uso Principal |
| :--- | :--- | :--- | :--- |
| **A** | **El Cerebro** | `Radial` + `Grid` + `Routing` | Plataforma completa en un solo hub central y subsistemas |
| **B** | **Las Fases** | `Grid` + `Routing` + `Banners` | Roadmaps de 90 días, progresiones con gates de aprobación |
| **C** | **La Serpiente** | `Flow` (Wave) + `Routing` | Procesos lineales extendidos de 8 a 16 pasos secuenciales |
| **D** | **El Duelo (VS)** | `Grid` + `Sticky` + `Routing` | Antes vs Después / Legacy caótico vs Arquitectura moderna |
| **E** | **La Cadena / Swimlanes**| `Board` + `Grid` + `Routing` | Swimlanes de roles y flujos coordinados entre actores |
| **F** | **El Embudo (Funnel)** | `Flow` + `Banners` | Conversión de ventas, retención y pipelines de selección |
| **G** | **La Pirámide** | `Hierarchy` + `Banners` | Modelos de madurez, capas de seguridad y abstracción |
| **H** | **El Radar 2x2** | `Grid` + `Routing` | Priorización Impacto vs Esfuerzo, clasificación de riesgos |
| **I** | **El Flywheel** | `Radial` + `Routing` | Bucles virtuosos de crecimiento, retención y recomendación |
| **J** | **La Cebolla (Onion)** | `Hierarchy` (Nested) | Clean Architecture, Hexagonal, Gobernanza por contención |
| **K** | **El Kanban WIP** | `Board` + `Sticky` | Pipelines ágiles, colas de trabajo, releases continuos |
| **L** | **El Iceberg** | `Grid` + `Banners` | Deuda técnica, complejidad backend oculta vs UI superficial |
| **M** | **La Espina (Ishikawa)** | `Hierarchy` + `Routing` | Análisis de causa raíz (Ishikawa), diagnóstico y post-mortems |
| **N** | **Galería 3x3** | `Dashboard` + `Grid` | Catálogo de microfrontends, suite de APIs y componentes |
| **O** | **Árbol de Decisión** | `Tree` + `Routing` | Protocolos de escalado, triaje, reglas condicionales |
| **P** | **Cadena de Valor** | `Flow` + `Grid` | Mapeo estratégico de operaciones, proveedores y margen |
| **Q** | **Pilares Benchmark** | `Board` + `Dashboard` | Comparativa cuantitativa de latencia, throughput y costes |
| **R** | **Roadmap con Gates** | `Timeline` + `Banners` | Lanzamientos v4.0, auditorías de seguridad SOC2 / ISO |
| **S** | **Matriz CRUD / Takt**| `Grid` (Proportional) | Mapeo de propiedad de datos o tiempos de ciclo industrial |
| **T** | **Caja Explotada** | `Network` + `Routing` | Desglose del funcionamiento interno de un motor complejo |

---

## 🛡️ Sistema Integral de Validación & Auto-Reparación

Sketion 8.0 incluye un pipeline automatizado de auto-reparación en 5 etapas antes de la serialización final:

1. **`text_repair.py`**: Asegura atributos tipográficos completos (`width`, `height`, `lineHeight: 1.25`, `baseline`, `originalText`, `autoResize`) y vinculación `containerId <-> boundElements` para 100% visibilidad en el canvas.
2. **`frame_repair.py`**: Detecta coordenadas relativas accidentales y las convierte a absolutas, garantizando que todos los elementos queden dentro de su marco contenedor.
3. **`spatial_repair.py`**: Detecta y resuelve colisiones espaciales entre tarjetas hermanas mediante separación vertical automática.
4. **`accent_repair.py`**: Aplica la regla del acento único (1–2 heroes) de forma independiente por cada marco en lienzos multi-frame.
5. **`binding_repair.py`**: Restaura enlaces bidireccionales en contenedores rectangulares.

---

## 📊 Grand Holdout End-to-End Benchmark (160 Renders a Ciegas)

```text
=============================================================================================
🏆 SKETION 8.0 — GRAND HOLDOUT END-TO-END BENCHMARK (160 EJECUCIONES A CIEGAS)
=============================================================================================
40 Casos Inéditos x 2 Audiencias x 2 Objetivos = 160 Renders Físicos con Core 100% Congelado

 • Dominio: NEGOCIO        | Renders: 40  | Quality Score Promedio: 96.0 / 100 [✅ PASS]
 • Dominio: TECH           | Renders: 40  | Quality Score Promedio: 96.0 / 100 [✅ PASS]
 • Dominio: OPERACIONES    | Renders: 40  | Quality Score Promedio: 96.0 / 100 [✅ PASS]
 • Dominio: RESEARCH       | Renders: 40  | Quality Score Promedio: 96.0 / 100 [✅ PASS]
=============================================================================================
 1. Total Ejecuciones Evaluadas       : 160 Renders End-to-End en 0.1s
 2. Global Sketion Quality Score      : 96.0 / 100 [✅ 100% PASS across all 160 runs] ⭐
 3. Global Render Fidelity Score      : 89.0 / 100 ⭐ EXCELLENT
 4. Audience Transformation (ATS)     : 96.0 / 100 ⭐ EXCELLENT
 5. Primary Flow Reduction (PFR)      : 81.4% (Alivio promedio del flujo central)
 6. Average Repair Dependency (RDS)   : 0.0 (Generador autónomo robusto, cero parches)
 7. Semantic Retention Rate           : 100.0% (Invariante en las 160 pruebas)
 8. Hard Failures / Crash             : 0 / 160 (0.0% de fallos)
=============================================================================================
```

---

## 📄 Licencia
Distribuido bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.
