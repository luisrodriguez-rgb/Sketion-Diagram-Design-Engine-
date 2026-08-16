# Sketion Style Guide & Design Tokens

Esta guía define el sistema visual editorial para la generación de archivos `.excalidraw`. Todas las decisiones visuales se basan en tokens semánticos rigurosos y una jerarquía tipográfica proporcional que garantiza **legibilidad inmediata sin forzar zoom**.

---

## 1. Principios Editoriales de Diseño

1. **La regla de oro:** *El movimiento de mayor calidad es la eliminación*. Cada nodo, línea y etiqueta debe ganarse su lugar.
2. **Densidad objetivo: 4/10:** Espacio en blanco amplio y respirable. `gap` generoso entre bloques. No saturar tarjetas de texto largo.
3. **Regla del acento único (1 Accent Rule):** El color de acento (`ACCENT` / `HERO`) se reserva exclusivamente para **1 o 2 nodos focales** por frame.
4. **Tipografía Proporcional Anti-Espacio Vacío:** El tamaño del texto debe llenar armónicamente el contenedor (60-70% del área vertical útil). Prohibido usar texto diminuto (11-14px) en tarjetas amplias de 300px+.
5. **Sin sombras ni degradados:** Excalidraw no requiere sombras. Las separaciones se hacen con bordes limpios (`hairlines`), fondos contrastados o franjas sutiles.
6. **Conectores ortogonales:** Conectores con codos en ángulo recto (90º) en lugar de líneas diagonales cruzando cajas.
7. **Esquinas controladas:** `roundness: {"type": 3}` para tarjetas estándar, `roundness: None` para tablas y contenedores técnicos.

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
| `ACCENT` | Color focal de marca (1-2 nodos por diagrama) | `#D93829` (Coral) / `#059669` (Verde) |
| `ACCENT_BG` | Tinte suave de fondo para el nodo focal | `#FFF5F2` / `#F0FDF4` |
| `PAIN` | Alertas, riesgos, cuellos de botella, deuda | `#E03A2F` |
| `PAIN_BG` | Tinte suave de fondo para alertas | `#FEF2F2` |
| `SUCCESS` | Estados completados, confirmaciones | `#059669` |
| `SUCCESS_BG` | Fondo para estados de éxito | `#F0FDF4` |
| `STICKY` | Fondo de etiquetas post-it / headers flotantes | `#FFE95C` |

---

## 4. Catálogo de Paletas Predefinidas

### A. Jet Editorial & Diagram Design (Arquitectura Cloud & Datos)
```python
JET_EDITORIAL = {
    "PAPER": "#F8FAFC",
    "PAPER_CARD": "#FFFFFF",
    "PAPER_CONTAINER": "#FFFFFF",
    "INK": "#0F172A",
    "MUTED": "#64748B",
    "RULE": "#CBD5E1",
    "ACCENT": "#D93829",       # Coral editorial Diagram Design
    "ACCENT_BG": "#FFF5F2",
    "PAIN": "#E03A2F",
    "PAIN_BG": "#FEF2F2",
    "STICKY": "#FFE95C"
}
```

### B. Miro Nico (Discovery, Brainstorming, Workshops)
```python
MIRO_NICO = {
    "PAPER": "#F4F4F4",
    "PAPER_CARD": "#FFFFFF",
    "PAPER_CONTAINER": "#EBEBEB",
    "INK": "#0C0C0C",
    "MUTED": "#9A9A9A",
    "RULE": "#D1D1D1",
    "ACCENT": "#F5BEC0",       # Rosa editorial
    "ACCENT_BG": "#FDF2F4",
    "PAIN": "#E03A2F",
    "PAIN_BG": "#FCE8E6",
    "STICKY": "#FFE95C"        # Amarillo canario post-it
}
```

### C. El Sabio / Hospitality OS (Plataformas de Restaurantes & Operaciones)
```python
EL_SABIO = {
    "PAPER": "#F8FAFC",
    "PAPER_CARD": "#FFFFFF",
    "PAPER_CONTAINER": "#F1F5F9",
    "INK": "#0F172A",
    "MUTED": "#64748B",
    "RULE": "#CBD5E1",
    "ACCENT": "#059669",       # Verde esmeralda de control
    "ACCENT_BG": "#F0FDF4",
    "PAIN": "#D93829",         # Coral de fricción
    "PAIN_BG": "#FEF2F2",
    "STICKY": "#FFE95C"
}
```
