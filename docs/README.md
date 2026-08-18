# 📚 Centro de Documentación Sketion (v11.0 GA)

Bienvenido a la documentación oficial del motor **Sketion Visual Composition Engine (v11.0 GA)**.

---

## 🏛️ Blueprints Arquitectónicos del Motor

Disponemos de dos vistas completas del sistema diseñadas con el propio motor Sketion:

### 1. [Diagrama de Arquitectura Técnica Integral](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/docs/sketion_engine_architecture.svg)
* **Público Objetivo:** Desarrolladores, Arquitectos de Software, DevOps e Ingenieros de Datos.
* **Contenido:**
  * **Pipeline End-to-End de 6 Etapas:** Inferencia semántica, selección topológica inteligente, layout solver multi-algoritmo, ruteo ortogonal Manhattan A*, motor de temas y serializador dual.
  * **Subsistemas Internos:** `ContentModel`, `PortManager`, `ManhattanRouter`, `VisualTypes27Engine`, `ClosedLoopRepairEngine`.
  * **Guía de Código en Python:** Ejemplos para API Unificada (`sketion.render`), Layout Solver (`LayoutSolver`) y Builder de bajo nivel (`ExcalidrawScene`).
  * **Estructura Interna `.excalidraw`:** Especificación del JSON nativo.
* **Archivos:**
  * Vectorial SVG: [`docs/sketion_engine_architecture.svg`](sketion_engine_architecture.svg)
  * Editable Excalidraw: [`docs/sketion_engine_architecture.excalidraw`](sketion_engine_architecture.excalidraw)
  * Script Generador: [`docs/generate_architecture_diagram.py`](generate_architecture_diagram.py)

---

### 2. [Guía Visual Intuitiva para Todo Público](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/docs/sketion_guia_no_tecnica.svg)
* **Público Objetivo:** Directores de Empresa, Gerentes de Producto, Equipos de Negocio y Clientes.
* **Contenido:**
  * **El Viaje de tu Idea en 4 Pasos:** *El Lector Inteligente* ➔ *El Arquitecto de Ideas* ➔ *El Urbanista del Lienzo* ➔ *El Diseñador Ejecutivo*.
  * **Duelo Visual Antes vs Después:** El problema de los diagramas manuales desordenados vs la claridad de Sketion.
  * **Los 4 Superpoderes:** Cero monotonía (20+ formas visuales), flechas sin enredos, diseño ejecutivo y 100% editable.
  * **Casos de Uso Reales:** Ventas, Operaciones Industriales, Estrategia de Equipos y Asistentes de IA.
* **Archivos:**
  * Vectorial SVG: [`docs/sketion_guia_no_tecnica.svg`](sketion_guia_no_tecnica.svg)
  * Editable Excalidraw: [`docs/sketion_guia_no_tecnica.excalidraw`](sketion_guia_no_tecnica.excalidraw)
  * Script Generador: [`docs/generate_non_technical_architecture_diagram.py`](generate_non_technical_architecture_diagram.py)

---

## 🎨 Galerías y Plantillas Disponibles

* [**Galería de los 27 Tipos Visuales Nativos (`docs/gallery/README.md`)**](gallery/README.md)
* [**Biblioteca Central de 62 Plantillas (`templates/README.md`)**](../templates/README.md)
* [**Biblioteca de Expansión de 150 Plantillas Especializadas (`templates_2/README.md`)**](../templates_2/README.md)
* [**Guía de Uso Universal Paso a Paso (`GUIA_DE_USO_UNIVERSAL.md`)**](../GUIA_DE_USO_UNIVERSAL.md)
* [**Informe de Diagnóstico y Diversidad (`INFORME_DIAGNOSTICO_Y_DIVERSIDAD_212_PLANTILLAS.md`)**](../INFORME_DIAGNOSTICO_Y_DIVERSIDAD_212_PLANTILLAS.md)
