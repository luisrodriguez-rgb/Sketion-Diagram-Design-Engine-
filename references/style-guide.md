# Sketion Style Guide & Design Tokens

Esta guía define el sistema visual editorial para la generación de archivos `.excalidraw`. Todas las decisiones visuales se basan en tokens semánticos rigurosos, una jerarquía tipográfica proporcional y una **estricta diversidad de arquetipos visuales**.

---

## 1. Principios Editoriales de Diseño

1. **La regla de oro:** *El movimiento de mayor calidad es la eliminación*. Cada nodo, línea y etiqueta debe ganarse su lugar.
2. **Densidad objetivo: 4/10:** Espacio en blanco amplio y respirable. `gap` generoso entre bloques. No saturar tarjetas de texto largo.
3. **Regla del acento único (1 Accent Rule):** El color de acento (`ACCENT` / `HERO`) se reserva exclusivamente para **1 o 2 nodos focales** por frame.
4. **Tipografía Proporcional Anti-Espacio Vacío:** El tamaño del texto debe llenar armónicamente el contenedor (60-70% del área vertical útil: **18-20px Bold** en títulos de tarjetas, **13-14px** en subtítulos, **14-15px** en tablas).
5. **🚫 Regla Anti-Monocultivo de Layout (Diversidad de Arquetipos):** En tableros multi-frame, **queda terminantemente prohibido repetir la misma estructura geométrica** (ej. 5 columnas verticales idénticas con chevrons). Cada frame debe usar el arquetipo geométrico nativo que corresponde a su semántica:
   - *Ecosistema / Visión Central:* **Arquetipo A (El Cerebro / Hub Radial)**.
   - *Arquitectura de Software:* **Arquetipo Layer Stack (Pila Horizontal de Capas)**.
   - *Pipelines / Algoritmos:* **Arquetipo C (Flow Pipeline) con bucle visible de Auto-Repair**.
   - *Roadmaps / Madurez:* **Arquetipo G (Escalera de Madurez de 5 Niveles) + Horizontes**.
   - *Comparativa de Mercado:* **Arquetipo D (El Duelo VS)** o **Arquetipo S (Matriz Tabular)**.
   - *Workshops / Discovery:* **Arquetipo Workshop Canvas (Post-its libres, slots y preguntas)**.

---

## 2. Jerarquía Tipográfica Proporcional Universal

| Elemento Visual | Rango de Dimensión | Tamaño de Fuente (`fontSize`) | Peso / Familia |
| :--- | :--- | :---: | :--- |
| **Título de Frame / Tablero** | Ancho total ($w \ge 2000\text{px}$) | **28px – 34px** | Bold (`fontFamily: 2`) |
| **Subtítulo / Breadcrumb** | Cabecera superior | **13px – 15px** | Mono (`fontFamily: 2`, `color: MUTED`) |
| **Tarjeta Amplia / Hero** | $w \ge 380\text{px}$ o $h \ge 115\text{px}$ | **20px** | Bold (`fontFamily: 2`) |
| **Tarjeta Estándar** | $w \in [250\text{px}, 380\text{px}]$ | **18px** | Semi-bold (`fontFamily: 2`) |
| **Tarjeta Compacta / Nodo** | $w < 250\text{px}$ | **16px** | Medium (`fontFamily: 2`) |
| **Subtítulo / Metadata Técnica**| Dentro de tarjeta | **13px – 14px** | Regular / Mono (`color: MUTED`) |
| **Cabecera de Tabla / Matriz** | Columnas de matriz | **14px – 15px** | Bold Uppercase (`fontFamily: 2`) |
| **Celdas de Datos en Tablas** | Celdas de matriz | **13px – 14px** | Regular / Medium |
| **Badges de Rol (Top-Left)** | Pastillas $h=22\text{px}$ | **11px – 12px** | Mono Uppercase (`fontFamily: 2`) |
| **Pills de Datos (Bottom)** | Pastillas $h=16\text{px}$ | **10px – 11px** | Mono |
| **Icono Vectorial** | Tarjetas estándar / amplias | **28px – 32px** | Vectorial monocromático |

---

## 3. Tokens Semánticos Fundamentales

| Token | Propósito en el Canvas | Hex por Defecto (Jet Editorial) |
| :--- | :--- | :--- |
| `PAPER` | Fondo general del lienzo / App State | `#F8FAFC` |
| `PAPER_CARD` | Fondo de tarjetas estándar | `#FFFFFF` |
| `PAPER_CONTAINER` | Fondo de grupos o subsecciones | `#F1F5F9` |
| `INK` | Tinta principal (títulos, bordes, texto primario) | `#0F172A` |
| `MUTED` | Texto secundario, subtítulos, flechas neutras | `#64748B` |
| `RULE` | Líneas divisorias, separadores de carril, ejes | `#CBD5E1` |
| `ACCENT` | Color focal de marca (1-2 nodos por diagrama) | `#2563EB` (Cobalto) / `#059669` (Verde) / `#D93829` (Coral) |
| `ACCENT_BG` | Tinte suave de fondo para el nodo focal | `#EFF6FF` / `#F0FDF4` / `#FFF5F2` |
| `PAIN` | Alertas, riesgos, cuellos de botella, deuda | `#E03A2F` |
| `PAIN_BG` | Tinte suave de fondo para alertas | `#FEF2F2` |
| `SUCCESS` | Estados completados, confirmaciones | `#059669` |
| `SUCCESS_BG` | Fondo para estados de éxito | `#F0FDF4` |
| `STICKY` | Fondo de etiquetas post-it / headers flotantes | `#FFE95C` |

---

## 4. Mapeo Obligatorio: Dominio Semántico ──► Arquetipo Visual

```text
┌───────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ DOMINIO SEMÁNTICO                     │ ARQUETIPO GEOMÉTRICO OBLIGATORIO                       │
├───────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Ecosistema / Visión Central / Hub     │ Arquetipo A: El Cerebro (Hub Radial con Satélites)     │
│ Arquitectura Software / Cloud / Infra │ Arquetipo Layer Stack: Pila Horizontal de 4 Capas      │
│ Pipelines / Algoritmos / Lifecycles   │ Arquetipo C: Flow con Bucle de Feedback Visible        │
│ Roadmaps / Madurez / Horizontes       │ Arquetipo G: Escalera de 5 Niveles + Matriz Horizontes │
│ Comparativa / Antes vs Después        │ Arquetipo D: El Duelo (Contraste Fricción vs Control)  │
│ Matriz de Capacidades / Competencia   │ Arquetipo S: Matriz Tabular Proporcional               │
│ Workshops / Sesión de Discovery       │ Arquetipo Workshop: Post-its, Checklist & Preguntas    │
└───────────────────────────────────────┴────────────────────────────────────────────────────────┘
```
