# Sketion Style Guide & Design Tokens

Esta guía define el sistema visual editorial para la generación de archivos `.excalidraw`. Todas las decisiones visuales se basan en tokens semánticos rigurosos, evitando colores genéricos o decoraciones innecesarias ("AI slop").

---

## 1. Principios Editoriales de Diseño

1. **La regla de oro:** *El movimiento de mayor calidad es la eliminación*. Cada nodo, línea y etiqueta debe ganarse su lugar.
2. **Densidad objetivo: 4/10:** Espacio en blanco amplio y respirable. `gap` generoso entre bloques. No saturar tarjetas de texto largo.
3. **Regla del acento único (1 Accent Rule):** El color de acento (`ACCENT`) se reserva exclusivamente para **1 o 2 nodos focales** o el camino crítico. Usarlo en 5 nodos destruye la jerarquía visual.
4. **Sin sombras ni degradados:** Excalidraw no requiere sombras. Las separaciones se hacen con bordes limpios (`hairlines`), fondos contrastados o franjas sutiles.
5. **Conectores ortogonales:** Conectores con codos en ángulo recto (90º) en lugar de líneas diagonales cruzando cajas.
6. **Esquinas controladas:** `roundness: {"type": 3}` para tarjetas estándar, `roundness: None` para tablas y contenedores técnicos.

---

## 2. Tokens Semánticos Fundamentales

| Token | Propósito en el Canvas | Hex por Defecto (Jet Editorial) |
| :--- | :--- | :--- |
| `PAPER` | Fondo general del lienzo / App State | `#F9FAFB` |
| `PAPER_CARD` | Fondo de tarjetas estándar | `#FFFFFF` |
| `PAPER_CONTAINER` | Fondo de grupos o subsecciones | `#F3F4F6` |
| `INK` | Tinta principal (títulos, bordes, texto primario) | `#111827` |
| `MUTED` | Texto secundario, subtítulos, flechas neutras | `#6B7280` |
| `RULE` | Líneas divisorias, separadores de carril, ejes | `#E5E7EB` |
| `ACCENT` | Color focal de marca (1-2 nodos por diagrama) | `#2563EB` |
| `ACCENT_BG` | Tinte suave de fondo para el nodo focal | `#EFF6FF` |
| `PAIN` | Alertas, riesgos, cuellos de botella, deuda | `#DC2626` |
| `PAIN_BG` | Tinte suave de fondo para alertas | `#FEF2F2` |
| `SUCCESS` | Estados completados, confirmaciones | `#16A34A` |
| `SUCCESS_BG` | Fondo para estados de éxito | `#F0FDF4` |
| `STICKY` | Fondo de etiquetas post-it / headers flotantes | `#FEF08A` |

---

## 3. Manejo Crítico de Modo Claro / Modo Oscuro en Excalidraw

> [!WARNING]
> **El filtro de inversión de Excalidraw:** Si el usuario abre el archivo en Excalidraw con modo oscuro activo, la aplicación invierte automáticamente los colores del canvas (blanco $\rightarrow$ casi negro, pasteles claros $\rightarrow$ tonos opacos/marrones).

### Reglas de Supervivencia Dark Mode:
- **No depender de grandes fondos de color sólido pastel:** Diseñar con fondo blanco o transparente y usar bordes finos (`strokeWidth: 1.5` o `2`).
- **Acentos en franjas o bordes:** Para destacar una tarjeta, utiliza un borde con `strokeColor: ACCENT` o una pequeña franja superior de acento, manteniendo el `backgroundColor: "transparent"` o `"#FFFFFF"`.
- **Contraste de Tinta:** El token `INK` (`#111827`) se invierte limpiamente a blanco en modo oscuro.

---

## 4. Tipografía en Excalidraw

Excalidraw soporta 3 familias tipográficas nativas:

| `fontFamily` ID | Nombre | Uso Obligatorio en Sketion |
| :---: | :--- | :--- |
| **2** | **Normal (Helvetica / Sans)** | **El 95% del contenido:** Tarjetas, nodos, títulos de sección, descripciones, tablas. Limpio y técnico. |
| **3** | **Cascadia (Code / Mono)** | **Contenido técnico:** Endpoints, puertos (`:8080`), variables, tipos SQL, parámetros JSON, IDs. |
| **1** | **Virgil (Hand-drawn / Boceto)** | **Opcional:** Solo para títulos gigantes de tablero si se pide explícitamente look artesanal o `roughness: 1`. |

### Tamaños Tipográficos Estándar:
- **Título de Tablero / Frame:** 24px - 32px (Bold)
- **Encabezado de Tarjeta / Nodo:** 16px - 18px (Semi-bold / Bold)
- **Cuerpo / Descripción:** 13px - 14px (Regular)
- **Etiqueta Técnica / Sublabel:** 11px - 12px (Mono)
- **Número Gigante (Dashboard KPI):** 48px - 64px (Bold)

---

## 5. Catálogo de Paletas Predefinidas

### A. Jet Editorial (Por defecto para Sistemas y Arquitectura)
```python
JET_EDITORIAL = {
    "PAPER": "#FFFFFF",
    "PAPER_CARD": "#FFFFFF",
    "PAPER_CONTAINER": "#F8FAFC",
    "INK": "#0F172A",
    "MUTED": "#64748B",
    "RULE": "#CBD5E1",
    "ACCENT": "#2563EB",       # Azul cobalto focal
    "ACCENT_BG": "#EFF6FF",
    "PAIN": "#EF4444",
    "PAIN_BG": "#FEF2F2",
    "STICKY": "#FEF08A"
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

### C. El Sabio (Comparativas de Marca, Estrategia, Negocio)
```python
EL_SABIO = {
    "PAPER": "#FAF9F6",
    "PAPER_CARD": "#FFFFFF",
    "PAPER_CONTAINER": "#F2EFE9",
    "INK": "#1C1B1A",
    "MUTED": "#8C887B",
    "RULE": "#DCD7CC",
    "ACCENT": "#B58E3F",       # Dorado cálido
    "ACCENT_BG": "#FBF6EB",
    "PAIN": "#A8433C",         # Rojo terracota
    "PAIN_BG": "#F9ECEB",
    "STICKY": "#EADBB6"
}
```

---

## 6. Onboarding de Marca (Extracción desde URL)

Cuando el usuario proporcione una URL de su marca (ej. `https://empresa.com`), se extraen y mapean los valores a estos tokens:

1. Fondo de la home $\rightarrow$ `PAPER`
2. Color principal de texto $\rightarrow$ `INK`
3. Color de botones/CTA dominante $\rightarrow$ `ACCENT`
4. Color de bordes/separadores $\rightarrow$ `RULE`
5. Validación WCAG AA: Ratio de contraste de `INK` sobre `PAPER` $\ge 4.5:1$.
