# 📖 Guía Universal de Uso de Sketion Engine (v8.0)
## Manual Maestro Paso a Paso para Integrar y Usar Sketion en Antigravity, Claude, ChatGPT, Cursor, Windsurf, Terminal y Editores Excalidraw

---

## 📑 Tabla de Contenidos
1. [¿Qué es Sketion y cómo funciona internamente?](#1-qué-es-sketion-y-cómo-funciona-internamente)
2. [Cómo funciona y cómo lo usa el Agente de IA aquí (Antigravity IDE)](#2-cómo-funciona-y-cómo-lo-usa-el-agente-de-ia-aquí-antigravity-ide)
3. [Uso en Claude (Claude Projects, Claude Desktop y Claude Code)](#3-uso-en-claude-claude-projects-claude-desktop-y-claude-code)
4. [Uso en ChatGPT / OpenAI (Custom GPTs y Prompts Web)](#4-uso-en-chatgpt--openai-custom-gpts-y-prompts-web)
5. [Uso en Editores de Código (Cursor, Windsurf y VS Code)](#5-uso-en-editores-de-código-cursor-windsurf-y-vs-code)
6. [Uso desde la Terminal y como Librería Python (CLI / SDK)](#6-uso-desde-la-terminal-y-como-librería-python-cli--sdk)
7. [Visualización y Edición en Excalidraw, VS Code y Obsidian](#7-visualización-y-edición-en-excalidraw-vs-code-y-obsidian)
8. [Catálogo Rápido de Comandos y Ejemplos Prácticos](#8-catálogo-rápido-de-comandos-y-ejemplos-prácticos)

---

## 1. ¿Qué es Sketion y cómo funciona internamente?

**Sketion** es un motor de diseño visual y arquitectura de información que transforma cualquier descripción en texto o especificación en lenguaje natural en un diagrama nativo, profesional, con calidad editorial y **100% editable** en formato `.excalidraw`.

A diferencia de generadores tradicionales que crean diagramas genéricos o "amontonan cajas", Sketion opera mediante un pipeline de **3 Inteligencias Desacopladas y 5 Capas**:

```text
                  PROMPT / ESPECIFICACIÓN DEL USUARIO
                                  │
                                  ▼
 ┌─────────────────────────────────────────────────────────────────┐
 │ 1. SEMANTIC MODEL                                               │
 │ • Extrae entidades, roles, acciones, restricciones y audiencias.│
 │ • Descompone textos largos en títulos, subtítulos y badges.     │
 └────────────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼
 ┌─────────────────────────────────────────────────────────────────┐
 │ 2. NARRATIVE CORE & ORACLE COMPOSITION JUDGE                    │
 │ • Determina la intención (explicativa, comparativa, proceso).   │
 │ • Selecciona el Arquetipo Visual Óptimo entre los 20 modelos    │
 │   disponibles (Hub Radial, Flow con bucle, Swimlanes, Stack).   │
 └────────────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼
 ┌─────────────────────────────────────────────────────────────────┐
 │ 3. INFORMATION ARCHITECTURE (IA) & PROGRESSIVE DISCLOSURE       │
 │ • Clasifica las entidades en 5 Tiers: HERO (foco), PRIMARY,     │
 │   SECONDARY, METADATA (pills) y APPENDIX (callouts laterales).  │
 │ • Evita la sobrecarga cognitiva en diagramas de 10 a 50+ nodos. │
 └────────────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼
 ┌─────────────────────────────────────────────────────────────────┐
 │ 4. ADAPTIVE RENDERING ENGINE                                    │
 │ • AnchorGeometry: Corte de flechas en el perímetro exacto.      │
 │ • Routing Ortogonal: Conectores a 90° sin cruzar sobre cajas.   │
 │ • Confinamiento de Frames: Coordenadas relativas -> absolutas.  │
 │ • ExcalidrawScene: Vinculación containerId <-> boundElements.   │
 └────────────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼
 ┌─────────────────────────────────────────────────────────────────┐
 │ 5. QUALITY AUDIT & AUTO-REPAIR (5 SUBSISTEMAS)                  │
 │ • Text Repair: Atributos tipográficos completos (100% visible). │
 │ • Spatial Collision Repair: Cero superposición de tarjetas.     │
 │ • Accent Repair: Regla del acento único (1-2 por marco).        │
 └────────────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼
                    ARCHIVO NATIVO .excalidraw
```

---

## 2. Cómo funciona y cómo lo usa el Agente de IA aquí (Antigravity IDE)

En este entorno (**Antigravity IDE**), Sketion funciona como una **Skill Nativa**. El agente cuenta con acceso a la terminal, al sistema de archivos y a los scripts del motor en Python.

### ¿Cómo interactúa el agente paso a paso cuando le pides un diagrama?

```text
  USUARIO: "Organízame esta arquitectura en un .excalidraw"
                            │
                            ▼
 1. LECTURA DE SKILL.md     El agente consulta las reglas maestras de diseño.
                            │
                            ▼
 2. ANÁLISIS SEMÁNTICO     Clasifica el problema (ej. "Sistema Legal B2B" -> 4 Marcos).
                            │
                            ▼
 3. ESCRITURA DEL SCRIPT   Crea un generador Python utilizando ExcalidrawScene:
                            • add_frame()
                            • add_stack_layer() (capas arquitectónicas)
                            • add_feature_card() (tarjetas con viñetas estructuradas)
                            • add_quad_card() (tarjetas de 4 esquinas con iconos)
                            • add_arrow() (conectores con enrutamiento ortogonal)
                            │
                            ▼
 4. RENDERIZADO Y GUARDADO  Ejecuta el script para generar el archivo .excalidraw físico.
                            │
                            ▼
 5. AUDITORÍA AUTOMÁTICA   Ejecuta validate_scene(auto_repair=True) para verificar:
                            • Cero textos invisibles
                            • Cero colisiones de tarjetas
                            • Puntuación de calidad >= 95/100
                            │
                            ▼
 6. ENTREGA AL USUARIO     Sincroniza en Git y entrega el enlace clickable directo.
```

---

## 3. Uso en Claude (Claude Projects, Claude Desktop y Claude Code)

### A. En Claude Web (Proyectos / Custom Instructions)
1. Abre tu proyecto en [Claude.ai](https://claude.ai) o ve a **Settings** $\rightarrow$ **Custom Instructions**.
2. Abre el archivo [`CLAUDE_PROJECT_INSTRUCTIONS.md`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/CLAUDE_PROJECT_INSTRUCTIONS.md) incluido en este repositorio.
3. Copia todo su contenido y pégalo en la sección de **Instrucciones del Proyecto**.
4. **Cómo pedirle diagramas a Claude:**
   > *"Diseña un diagrama en formato Excalidraw para una arquitectura de microservicios con Kafka, PostgreSQL y Redis, enfocada en alta concurrencia."*
5. Claude te responderá directamente con el bloque JSON de Excalidraw. 
6. Copia ese JSON, guárdalo con extensión `.excalidraw` (ej. `arquitectura.excalidraw`) o pégalo directamente en [excalidraw.com](https://excalidraw.com) usando `Ctrl + V` / `Cmd + V`.

### B. En Claude Code (CLI)
Si usas Claude Code en tu terminal local:
```bash
# Agregar la skill de Sketion a Claude Code:
claude-code --add-skill /ruta/a/Sketion-Diagram-Design-Engine-/skill.md
```

---

## 4. Uso en ChatGPT / OpenAI (Custom GPTs y Prompts Web)

### A. Crear un Custom GPT de Sketion
1. Ve a [ChatGPT](https://chatgpt.com) $\rightarrow$ **Explore GPTs** $\rightarrow$ **Create a GPT**.
2. En la pestaña **Configure**:
   * **Name:** `Sketion Visual Architect`
   * **Description:** `Diseñador editorial de diagramas y arquitecturas en formato nativo Excalidraw.`
   * **Instructions:** Pega el contenido completo del archivo [`skill.md`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/skill.md).
   * **Capabilities:** Activa *Code Interpreter / Advanced Data Analysis*.
3. En **Knowledge**, sube los archivos de la carpeta `references/`:
   * `types-catalog.md`
   * `style-guide.md`
   * `layout-rules.md`
4. **Listo.** Ahora tu Custom GPT generará diagramas respetando la regla del acento único, la densidad 4/10 y los 20 arquetipos de diseño.

---

## 5. Uso en Editores de Código (Cursor, Windsurf y VS Code)

### A. En Cursor (`.cursorrules` o `.cursor/rules/`)
Crea o edita el archivo `.cursorrules` en la raíz de tu proyecto y agrega:
```markdown
# Sketion Diagram Engine Rules
Cuando se te pida diseñar, estructurar o exportar diagramas, flujos o arquitecturas:
1. Utiliza siempre el motor Sketion ubicado en la carpeta del workspace.
2. Construye escenas mediante `render.excalidraw_builder.ExcalidrawScene`.
3. Sigue las reglas de diseño editorial de `skill.md` (diversidad de arquetipos, acento único, 0 colisiones).
4. Ejecuta `validate_scene()` para asegurar una puntuación >= 95/100 antes de entregar el archivo .excalidraw.
```

### B. En Windsurf (`.windsurfrules`)
Agrega la misma instrucción en tu archivo `.windsurfrules` para que Cascade utilice el constructor oficial `ExcalidrawScene` y las primitivas de capas y tarjetas.

---

## 6. Uso desde la Terminal y como Librería Python (CLI / SDK)

### A. Instalación Global del CLI
```bash
# Instalación rápida en 1 comando:
curl -fsSL https://raw.githubusercontent.com/luisrodriguez-rgb/Sketion-Diagram-Design-Engine-.git/main/install.sh | bash
```

### B. Comandos de Terminal (`sketion`)
```bash
# 1. Ver catálogo de los 20 arquetipos disponibles:
sketion types

# 2. Generar un diagrama automáticamente a partir de un tipo:
sketion generate "Pipeline de Conciliación Bancaria" --type pipeline --output conciliacion.excalidraw --validate

# 3. Validar y auto-reparar cualquier archivo .excalidraw existente:
sketion validate mi_diagrama.excalidraw

# 4. Ejecutar la suite integral de benchmarks:
sketion benchmark
```

### C. Uso Programático como SDK en tus propios scripts de Python
```python
from render.excalidraw_builder import ExcalidrawScene, place, place_reset
from validation.validator import validate_scene

# 1. Inicializar escena
scene = ExcalidrawScene(roughness=0, bg_color="#F8FAFC")

# 2. Crear marco
fw, fh = 1400.0, 600.0
frame_id = scene.add_frame("01. Arquitectura de Autenticación OAuth2", 40.0, 40.0, fw, fh)

# 3. Añadir tarjeta estructurada
scene.add_quad_card(
    80.0, 120.0, 280.0, 120.0,
    title="API Gateway",
    sublabel="Valida y firma tokens JWT.\nRate limiting activo.",
    badge="GATEWAY",
    icon="lock",
    is_hero=True,
    frame_id=frame_id
)

# 4. Guardar archivo
scene.save("oauth2_architecture.excalidraw")

# 5. Validar calidad editorial
_, report = validate_scene("oauth2_architecture.excalidraw")
print(f"Puntuación Sketion: {report.sketion_overall_score}/100 [PASS]")
```

---

## 7. Visualización y Edición en Excalidraw, VS Code y Obsidian

Los archivos `.excalidraw` generados por Sketion son **100% estándar y nativos**, compatibles con cualquier visor de Excalidraw:

| Plataforma | Cómo abrir y editar |
| :--- | :--- |
| **Navegador Web** | Entra a [excalidraw.com](https://excalidraw.com) $\rightarrow$ Clic en el icono de carpeta superior izquierda $\rightarrow$ **Open / Abrir** $\rightarrow$ Selecciona tu archivo `.excalidraw`. |
| **VS Code / Cursor** | Instala la extensión oficial **Excalidraw** (`pomdtr.excalidraw-editor`). Al hacer clic en cualquier archivo `.excalidraw`, se abrirá el lienzo interactivo directamente dentro del editor. |
| **Obsidian** | Instala el plugin **Obsidian-Excalidraw** de Zsolt Viczian. Puedes arrastrar el archivo a tu vault y visualizarlo/editarlo de inmediato. |

---

## 8. Catálogo Rápido de Comandos y Ejemplos Prácticos

### Plantilla de Prompt Universal para cualquier IA:
> *"Usa la Skill de Sketion v8.0 para crear un diagrama en formato `.excalidraw` sobre [TU TEMA]. Requisitos: Aplica el arquetipo visual adecuado entre los 20 disponibles, utiliza la regla del acento único (un solo componente en color coral/rojo), asegúrate de que todos los textos estén centrados y vinculados al contenedor con `containerId`, y valida que no haya colisiones ni solapamientos."*
