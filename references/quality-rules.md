# Reglas de Validación y Calidad Visual de Sketion (v8.0)

Este documento establece las reglas automáticas que el validador de Sketion (`validation/validator.py`) y el motor de auto-reparación (`repair/engine.py`) ejecutan para garantizar que un diagrama sea técnicamente válido, visualmente equilibrado y libre de defectos geométricos.

---

## 1. Validación Estructural (Técnica & Tipográfica)

- **JSON Válido v2:** El archivo debe tener `type: "excalidraw"`, `version: 2`, `elements` como array plano y `appState`.
- **Completitud de Atributos de Texto (Visibilidad 100%):**
  - Todo elemento de texto debe contener: `width > 0`, `height > 0`, `fontSize`, `fontFamily: 2` (o 1/3), `lineHeight: 1.25`, `baseline: fontSize`, `originalText` sincronizado y `autoResize: true`.
  - Prohibido dejar elementos `type: "text"` sin `width` o `height` calculados (esto provoca que Excalidraw no dibuje los glifos).
- **Reciprocidad de Vínculos (Bidireccional):**
  - Todo elemento de texto con `containerId: X` debe existir dentro del array `boundElements` del contenedor `X`.
  - Todo contenedor con `boundElements` debe apuntar a elementos de texto válidos que existen en la escena.
- **IDs Únicos:** Ningún elemento puede compartir `id` o `seed`.

---

## 2. Validación Geométrica y Confinamiento Espacial

- **Confinamiento Estricto en Frames:** Todos los elementos con `frameId` deben estar situados matemáticamente dentro de los límites del marco $[F_x, F_x + F_w] \times [F_y, F_y + F_h]$.
- **Mapeo Automático de Coordenadas:** Si se ingresan coordenadas relativas locales al marco, `_base_element()` y `repair/frame_repair.py` las convierten automáticamente a coordenadas absolutas.
- **Cero Colisiones Espaciales (`Overlaps`):** Dos tarjetas del mismo nivel jerárquico no pueden superponerse. El subsistema `repair/spatial_repair.py` resuelve automáticamente colisiones desplazando verticalmente los elementos en conflicto.
- **Llenado Espacial Proporcional:** Las tarjetas y capas deben llenar armónicamente el espacio interior (máximo 30% de espacio blanco muerto).

---

## 3. Validación Visual y Editorial

- **Regla del Acento Único por Marco:** Máximo **1–2 nodos con color de acento (`ACCENT`)** por marco narrativo independiente.
- **Curva de Densidad Calibrada:** Densidad objetivo $\approx 3.0\text{--}4.5/10$ (Target Editorial: 4.0/10). En diagramas multi-frame, la densidad baja ($1.5\text{--}2.5$) es reconocida como espacio de respiración intencional (*Executive Breathing Room*).
- **Consistencia Tipográfica:**
  - Títulos de tarjeta: $14\text{--}16\text{px}$ Bold.
  - Viñetas y cuerpo explicativo: $12\text{--}13\text{px}$ Regular.
  - Badges y metadatos: $10\text{--}11\text{px}$ Mono/Sans.
- **Prohibición de Emojis Decorativos Sueltos:** Reemplazar por badges vectoriales o texto corto con contraste.

---

## 4. Pipeline de Auto-Reparación en 5 Capas (`RepairEngine`)

Cuando se invoca `validate_scene(..., auto_repair=True)`, se ejecutan en orden:
1. `text_repair.py`: Repara dimensiones, originalText y baseline en textos.
2. `binding_repair.py`: Restaura referencias bidireccionales `containerId <-> boundElements`.
3. `spatial_repair.py`: Detecta y separa colisiones entre tarjetas.
4. `frame_repair.py`: Re-ancla elementos fuera de sus marcos o auto-expande el marco.
5. `accent_repair.py`: Degrada acentos excedentes evaluando cada marco de forma independiente.
