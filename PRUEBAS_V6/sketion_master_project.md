# 🧠 SKETION — MASTER PROJECT DESIGN DOCUMENT

> **Tagline:** *Think. Structure. Build.*  
> **Concepto:** *Visual Knowledge Workspace*  
> **Filosofía Central:** *Knowledge shouldn't have to live in ten disconnected apps. Everything connected. Everything visual. AI should organize your thinking, not replace it.*

---

## 🏛️ 1. Identidad, Posicionamiento & Propuesta de Valor

### De Dónde Venimos y Hacia Dónde Vamos
* **Nombre:** Sketion (anteriormente explorado como My-Excalidraw).
* **Repositorio:** [github.com/luisrodriguez-rgb/Sketion](https://github.com/luisrodriguez-rgb/Sketion)
* **Web App:** [sketion.vercel.app](https://sketion.vercel.app)
* **Documentación Oficial:** [docs-sketion.vercel.app](https://docs-sketion.vercel.app)
* **Publicación Fundacional:** [DEV.to Article (11 de Agosto, 2026)](https://dev.to/luisrodriguezrgb/what-if-your-notes-pdfs-code-math-and-diagrams-lived-in-the-same-workspace-46ia)

---

### Cuadro de Posicionamiento de Mercado

| Herramienta | Enfoque Principal | Límite / Fricción | Cómo Sketion lo Transforma |
| :--- | :--- | :--- | :--- |
| **Excalidraw** | Dibujo libre / Bocetos | Solo dibujo, sin capas de documentos ni datos | **Canvas extendido con PDFs, LaTeX y datos** |
| **Miro / Mural** | Pizarra colaborativa | Rígido para código/fórmulas, no es local-first | **Local-First, LaTeX y soporte técnico real** |
| **Notion** | Documentos / Tablas | Estructura vertical lineal, sin espacialidad | **Conexiones espaciales y visuales libres** |
| **Obsidian** | Knowledge Graph / Markdown | Gráficos automáticos pero no manipulables | **Nodos visuales editables directamente** |
| **Anki** | Memorización espaciada | Aislado del material de estudio original | **Flashcards que nacen del mismo canvas** |
| **Canva** | Diseño gráfico | No estructurado para ingeniería o ciencia | **Diagramación técnica y semántica precisa** |
| **SKETION** | **Visual Knowledge Workspace** | **Unifica el ciclo completo de pensamiento** | **Source $\rightarrow$ Understanding $\rightarrow$ Structure $\rightarrow$ Knowledge** |

---

## ⚠️ 2. El Problema: El Ciclo de Fragmentación del Conocimiento

```text
EL FLUJO TRADICIONAL FRAGMENTADO:
PDF en Adobe ──► Notas en Notion ──► LaTeX en Overleaf ──► Diagrama en Excalidraw ──► Datos en Excel ──► Flashcards en Anki ──► GitHub
   └────────────── Fricción constante: Open -> Switch -> Copy -> Paste -> Reorganize -> Switch Again ──────────────┘

EL FLUJO UNIFICADO SKETION:
┌── Notes (Conocimiento conectado)
│   ├── PDFs (Texto interactivo y anotación)
└───┼── LaTeX / Math (Fórmulas matemáticas nativas)
    ├── Mermaid / Diagrams (Flujos de arquitectura)
    ├── Datasets & Charts (CSV / Google Sheets)
    └── Flashcards & Active Recall (Estudio integrado)
```

---

## ⚙️ 3. Arquitectura del Sistema & Stack Tecnológico

### Principio Local-First
> *"Your workspace should remain useful even when the network doesn't."*

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 SKETION APPLICATION STACK                               │
│                                                                                        │
│  [FRONTEND CORE]                                                                       │
│  React 18 · TypeScript · Vite · Tailwind CSS · Outfit & Inter Typography               │
│                                                                                        │
│  [CANVAS & RENDERING ENGINES]                                                          │
│  Excalidraw Engine · PDF.js Overlays · KaTeX (LaTeX) · Mermaid.js (Diagrams)           │
│                                                                                        │
│  [LOCAL PERSISTENCE (LOCAL-FIRST)]                                                     │
│  IndexedDB (Dexie.js / Local Workspace State) ──► Latencia Cero Offline                │
│                                                                                        │
│  [CLOUD & SYNCHRONIZATION BACKEND]                                                     │
│  Supabase Auth · PostgreSQL Database · Supabase Storage (Blobs) · Socket.IO Realtime   │
│                                                                                        │
│  [DEPLOYMENT & CI/CD]                                                                  │
│  Vercel Edge Network · VitePress Documentation Portal                                  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🤖 4. Sketion Intelligence: El Motor de IA Estructurado

> **Filosofía de IA:**  
> *"AI should organize your thinking, not replace it. AI doesn't design from scratch; AI completes structured visual systems."*

### El Pipeline Semántico de 4 Capas:
```text
PROMPT DEL USUARIO
   │
   ▼
[CAPA 1: ANÁLISIS SEMÁNTICO & INFERENCIA DE AUDIENCIA]
Determina intención, arquetipo óptimo, jerarquía de entidades y restricciones semánticas
   │
   ▼
[CAPA 2: MOTOR VISUAL & SELECCIÓN DE ARQUETIPO]
Mapeo a 1 de los 20 Arquetipos (A-T) o 27 Tipos Visuales (Lakehouse, 2x2, Software, Ops)
   │
   ▼
[CAPA 3: MOTOR DE LAYOUT GEOMÉTRICO & TOKENS]
Cálculo de gaps (95px), gutters (65px), centrado bidimensional y escalado tipográfico (18-20px)
   │
   ▼
[CAPA 4: RENDER NATIVO, VALIDACIÓN & AUTO-REPAIR]
Generación de JSON .excalidraw nativo 100% editable ──► Validador 6D ──► Auto-Repair
```

---

## 🗺️ 5. Estado Actual del Producto & Roadmap Oficial

```text
┌───────────────────────────────────┬───────────────────────────────────┬───────────────────────────────────┐
│ 🟢 DISPONIBLE HOY (Live)          │ 🟡 EN CONSTRUCCIÓN (Q3-Q4)        │ 🔵 EN INVESTIGACIÓN (R&D)         │
├───────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────┤
│ • Infinite Canvas Interactivo     │ • Biblioteca Premium de Templates │ • AI Skill Engine (Sketion 4.0)   │
│ • Motor Local-First (IndexedDB)   │ • Flujos Interactivos Mermaid     │ • Workflows IA para PDFs          │
│ • Espacio de Trabajo para PDFs    │ • Integraciones con Google Colab  │ • Knowledge Graph Automatizado    │
│ • Importación de Google Sheets    │ • Workflows Avanzados de LaTeX    │ • Ecosistema de Plugins           │
│ • Study Mode & Flashcards         │ • Sistema de Comentarios Espacial │ • Colaboración P2P en Tiempo Real │
│ • Renderizado Nativo de LaTeX     │ • Presenter Mode con Export PPTX  │ • Generación Visual Determinista  │
│ • Gestión de Proyectos / Boards   │ • Control de Versiones en Canvas  │ • API para Agentes Externos       │
└───────────────────────────────────┴───────────────────────────────────┴───────────────────────────────────┘
```

---

## 🚀 6. Los 5 Niveles de Evolución a Largo Plazo

1. **Nivel 1 — Canvas:** Dibujo y bocetado libre (*Draw*).
2. **Nivel 2 — Workspace:** Dibujo + Documentos + Notas + Fórmulas + Datos (*Workspace*).
3. **Nivel 3 — Knowledge Workspace:** Todo interconectado espacialmente (*Connected Knowledge*).
4. **Nivel 4 — AI Workspace:** La IA comprende el contexto y estructura las notas (*AI Assist*).
5. **Nivel 5 — Visual Intelligence Platform:** *Prompt $\rightarrow$ Estructura $\rightarrow$ Sistema Visual $\rightarrow$ Artefacto Nativo Editable*.
