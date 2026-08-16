# Reglas de Validación y Calidad Visual de Sketion

Este documento establece las reglas automáticas que el validador de Sketion (`validation/validator.py`) ejecuta para garantizar que un diagrama no solo sea técnicamente válido, sino visualmente impecable.

---

## 1. Validación Estructural (Técnica)

- **JSON Válido v2:** El archivo debe tener `type: "excalidraw"`, `version: 2`, `elements` como array plano y `appState`.
- **Reciprocidad de Vínculos:**
  - Todo elemento de texto con `containerId: X` debe existir dentro del array `boundElements` del contenedor `X`.
  - Todo contenedor con `boundElements` debe apuntar a elementos de texto válidos que existen en la escena.
- **IDs Únicos:** Ningún elemento puede compartir `id` o `seed`.
- **Dimensiones Positivas:** `width > 0` y `height > 0` para todos los elementos geométricos.

---

## 2. Validación Geométrica (Espacial)

- **Sin Solapamientos No Intencionales (`Overlaps`):** Dos tarjetas del mismo nivel jerárquico no pueden compartir coordenadas superpuestas.
- **Límites del Frame:** Todos los elementos hijos con `frameId` deben estar posicionados dentro del área rectangular del frame.
- **Longitud de Texto:** Los textos no deben desbordar el ancho de su tarjeta contenedora.

---

## 3. Validación Visual y Editorial

- **Regla del Acento Único:** Máximo **2 nodos con color de acento (`ACCENT`)** por frame. Si hay 3 o más, el validador emite una advertencia de sobrecarga de señal.
- **Límite de Densidad:** Densidad objetivo $\le 6/10$. Si hay más de 9 nodos en un frame simple sin división en sub-clusters, se recomienda partir el diagrama.
- **Consistencia Tipográfica:** Máximo 2 familias tipográficas en el mismo diagrama (`fontFamily: 2` Normal y `fontFamily: 3` Mono).
- **Prohibición de Emojis Decorativos:** Reemplazar glifos de emojis por texto corto (`SI/NO/PARCIAL`, `OK/ERROR`).

---

## 4. Validación Semántica

- **Sin Nodos Huérfanos:** En diagramas de flujo y arquitectura, todo nodo debe tener al menos una arista de entrada o salida.
- **Integridad de Conexiones:** Toda arista debe conectar nodos existentes (`from` y `to` válidos).
