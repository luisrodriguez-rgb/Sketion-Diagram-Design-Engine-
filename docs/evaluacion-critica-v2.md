# 🔬 Auditoría Crítica de Renderizado y Diseño Visual (Sketion v2.8)

**Evaluación exhaustiva de las entregas visuales reales sobre el canvas web de Sketion.**

---

## 🎯 Resumen Ejecutivo

Al inspeccionar los diagramas generados en el visor interactivo de Sketion, se observa una mejora drástica en comparación con la versión anterior:
- ✅ **El desbordamiento de texto (*Text Bleeding*) ha desaparecido.**
- ✅ **Los títulos de los frames ya no se truncan.**
- ✅ **Las etiquetas de las flechas tienen pastillas protectoras blancas.**

Sin embargo, al someter el motor a una evaluación de **diseño editorial profesional (nivel Stripe / Apple / Diagram Design)**, surgen **5 problemas visuales de segundo nivel** que impiden que el resultado se sienta como el trabajo de un diseñador senior:

---

## 🔍 Los 5 Problemas Visuales Críticos Identificados

---

### 1. Colisión de Pastillas de Flecha con Nodos Hermanos (*Label-Node Occlusion*)
* **Evidencia en la Captura (E-Commerce):**
  - La flecha vertical entre *Web Storefront* y *Cloudflare CDN* calcula su punto medio `(mid_x, mid_y)`, y coloca la pastilla de texto `[HTTPS]` **justo encima de la tarjeta intermedia (*App Móvil*)**, tapando su texto (`"Comprad [HTTPS] droid Mobile"`).
* **Causa Raíz:** El cálculo del punto medio de la flecha es estrictamente geométrico entre $(x_1, y_1)$ y $(x_2, y_2)$ sin verificar si la caja de la pastilla colisiona con el *bounding box* de otros nodos que se encuentren en medio.
* **Solución Técnica:**
  - Si una flecha conecta un nodo superior con uno inferior pasando por encima de un nodo intermedio, la ruta debe enrutarse por fuera del carril de nodos (desvío lateral) o la pastilla debe colocarse en el segmento inicial libre (`start_y + 25px`).

---

### 2. Anchos Irregulares en la Misma Columna (*Inconsistent Column Widths*)
* **Evidencia en la Captura (API REST):**
  - En la zona `REST API SERVER`, la tarjeta superior (*API Router*) mide **280px de ancho**, mientras que la tarjeta inferior (*Middleware & Lógica*) mide **380px**.
  - Esto produce un efecto visual de "escalera desigual" que rompe la cuadrícula y la armonía editorial.
* **Causa Raíz:** Cada tarjeta calcula su ancho de forma aislada e independiente en lugar de **homogeneizar el ancho a nivel de columna / Scope**.
* **Solución Técnica:**
  ```python
  # Calcular el ancho máximo requerido por todos los nodos de un mismo Scope/Columna
  column_w = max(compute_card_dimensions(n)[0] for n in nodes_in_scope)
  for node in nodes_in_scope:
      node.width = max(260.0, column_w)
  ```

---

### 3. Cruces de Flechas Tipo "Spaghetti" y Rutas Diagonalizadas
* **Evidencia en la Captura (E-Commerce & API REST):**
  - En la API REST, la flecha de respuesta `[200 OK JSON]` retrocede desde el Router hacia el Frontend con un codo invertido que invade el encabezado del Scope.
  - En el E-Commerce, la flecha de *Servicio de Pedidos* hacia *Stripe* atraviesa transversalmente las líneas de *Redis* y *PostgreSQL*.
* **Causa Raíz:** El motor de routing actual es ortogonal simple de 1 codo (`mid_dx, mid_dy`). No implementa **Canales de Enrutamiento Dedicados (Track Lanes)** para separar flujos de ida (Forward) de flujos de retorno (Feedback / Response).
* **Solución Técnica:**
  - **Carril Superior de Retorno:** Las respuestas (`200 OK`, `Webhooks`) viajan por un carril horizontal superior reservado, mientras que las peticiones viajan por el carril central/inferior.

---

### 4. Espacios Verticales Muertos en los Scopes (*Dead Height Padding*)
* **Evidencia en la Captura (API REST & E-Commerce):**
  - En la API REST, los 3 Scopes tienen una altura fija de `h: 500px`. Como solo contienen 2 tarjetas cada uno, queda un **40% de espacio vacío en la parte inferior de cada contenedor**.
* **Causa Raíz:** Los Scopes se definían con dimensiones `w` y `h` estáticas en lugar de calcularse como la envolvente real de sus nodos hijos.
* **Solución Técnica:**
  $$\text{Scope.Height} = \max(y_{\text{nodos}}) + \text{Card.Height} + 40\text{px} - \text{Scope.Y}$$

---

### 5. Falta de Micro-Identidad y Jerarquía de Acabado (*Visual Richness*)
* **Diagnóstico de Estilo:**
  - Todas las cajas secundarias lucen como rectángulos monocromáticos idénticos con bordes finos.
  - Falta un micro-sistema de **chips/tags de categoría** (`[FRONTEND]`, `[STORAGE]`, `[GATEWAY]`, `[ASYNC]`) que aporte ritmo visual y jerarquía sin añadir ruido (*AI Slop*).

---

## 📐 Roadmap de Soluciones Técnicas para Sketion Core 3.0

```text
                               SKETION CORE 3.0
                                      │
    ┌───────────────────┬─────────────┴─────────────┬───────────────────┐
    ↓                   ↓                           ↓                   ↓
1. COLUMN GRID ALIGN 2. DYNAMIC SCOPE BOUNDS 3. TRACK-LANE ROUTING 4. PILL SAFETY CHECK
Ancho uniforme por   Altura y ancho exacto   Carriles separados    Nunca tapar nodos
columna/zona         según sus nodos hijos   para ida y retorno    intermedios
```

---

### 🛠️ 1. Homogeneización de Ancho por Columna (`align_column_widths`)
Al renderizar una zona o columna de arquitectura:
```python
def compute_uniform_scope_layout(scopes, nodes):
    for scope in scopes:
        scope_nodes = [n for n in nodes if n.get("scope_id") == scope["id"]]
        if scope_nodes:
            # 1. Ancho uniforme para todas las tarjetas de la zona
            max_w = max(compute_card_dimensions(n["label"], n.get("sublabel"), n.get("metadata"))[0] for n in scope_nodes)
            uniform_w = max(260.0, max_w)
            for n in scope_nodes:
                n["w"] = uniform_w
            
            # 2. Ajuste exacto del contenedor de la zona
            scope["w"] = uniform_w + 60.0
            max_y = max(n["rel_y"] + n.get("h", 90) for n in scope_nodes)
            scope["h"] = max_y + 40.0
```

---

### 🛠️ 2. Enrutamiento de Retorno por Carril Superior (*Feedback Channel*)
Para evitar flechas spaghetti que crucen en diagonal:
- Si `target_x < source_x` (petición de retorno como `200 OK` o `Webhook`):
  - La flecha sube al carril superior del frame (`y = frame_y + 70px`), viaja horizontalmente por encima de las tarjetas y baja limpiamente al destino.

---

### 🛠️ 3. Validación de Colisión Geométrica (*AABB Collision in Validator*)
Incorporar en `validation/structural.py` la detección de superposición de cajas:
```python
def check_label_node_overlap(pill_boxes, node_boxes):
    for pill in pill_boxes:
        for node in node_boxes:
            if boxes_intersect(pill, node):
                return f"Error: La etiqueta '{pill.text}' colisiona físicamente con el nodo '{node.title}'."
```

---

## 🏆 Veredicto

El motor ya resolvió la estabilidad estructural y los desbordamientos. Con la implementación de **Ancho Uniforme por Columna**, **Dynamic Scope Heights** y **Enrutamiento por Carriles de Retorno**, Sketion alcanzará la **excelencia editorial definitiva**.
