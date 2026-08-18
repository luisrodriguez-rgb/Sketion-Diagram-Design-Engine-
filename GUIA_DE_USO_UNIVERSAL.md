# Guía Universal de Uso de Sketion Engine (v11.0 GA)
## Manual Maestro Paso a Paso para Integrar y Usar Sketion en Python SDK, CLI, Antigravity, Claude, ChatGPT, Cursor, Windsurf, Terminal y Editores Excalidraw / SVG

> [!TIP]
> **Blueprints Visuales de Arquitectura Disponibles:**
> * 💻 **[Diagrama de Arquitectura Técnica Integral (`docs/sketion_engine_architecture.svg`)](docs/sketion_engine_architecture.svg)** (Pipeline, ContentModel, Manhattan A*, 20 Patrones, SDK).
> * 👥 **[Guía Visual Intuitiva para Todo Público (`docs/sketion_guia_no_tecnica.svg`)](docs/sketion_guia_no_tecnica.svg)** (El Viaje en 4 Pasos, Comparativa Antes/Después, 4 Superpoderes).

---

## Matriz de Costos y Modalidades (Planes Gratuitos vs. Planes de Pago)

Sketion fue diseñado para ser **100% utilizable sin gastar dinero**, pero también ofrece integraciones avanzadas si cuentas con suscripciones de pago:

| Entorno / Plataforma | Modalidad Gratuita (Free Tier) | Modalidad de Pago (Plus / Pro / Team) |
| :--- | :--- | :--- |
| **Python SDK (`import sketion`)** | **100% GRATIS** (ejecución autónoma local con Explainability y exportación SVG/Excalidraw). | No aplica (siempre es libre y abierto). |
| **Terminal / CLI (`sketion_cli.py`)** | **100% GRATIS** (corre localmente en tu máquina, cero costo de API o tokens). | No aplica (cero costo de ejecución). |
| **VS Code / Cursor / Windsurf** | **100% GRATIS** (ejecuta el motor local en tu workspace sin créditos de IA). | Opcional (usa modelos premium como Claude 3.5 Sonnet o GPT-4o). |
| **Claude (Anthropic)** | **100% GRATIS** (copiando el System Prompt al inicio del chat libre). | **Claude Pro ($20/mes):** Permite crear *Claude Projects* permanentes. |
| **ChatGPT (OpenAI)** | **100% GRATIS** (usando *Instrucciones Personalizadas* en tu cuenta). | **ChatGPT Plus ($20/mes):** Permite crear *Custom GPTs* con Code Interpreter. |
| **Excalidraw & Visores Web SVG** | **100% GRATIS** (en [excalidraw.com](https://excalidraw.com), navegadores web o extensión de VS Code). | **Excalidraw+:** Solo para colaboración corporativa en la nube. |

---

## Comparativa de Resultados: ¿Se obtiene el mismo resultado en todos los entornos?

**Respuesta directa y honesta:** **No, no son exactamente iguales.** 

Existe una diferencia técnica fundamental entre **ejecutar el motor matemático de Sketion en Python** (lo que hacemos en entornos como este o en la terminal) y **pedirle a un LLM en un chat web que "adivine" y escriba el JSON token a token**:

```text
 ┌─────────────────────────────────────────────────────────────────────────┐
 │ TIER 1: CALIDAD MÁXIMA (10/10) · EJECUCIÓN CON MOTOR PYTHON             │
 │ • Entornos: Antigravity IDE, Cursor, Windsurf, CLI Local, ChatGPT Plus  │
 │   (con Code Interpreter).                                               │
 │ • Por qué es superior: Las coordenadas (x, y), márgenes, enrutamiento  │
 │   a 90° y tamaños de fuente son calculados por algoritmos matemáticos   │
 │   exactos en Python.                                                    │
 │ • Auto-Reparación Activa: Si hay una colisión o un texto sin atributos, │
 │   validate_scene() lo detecta y corrige en 0.01s antes de guardar.      │
 │ • Capacidad: Soporta diagramas masivos de 400+ elementos y 4 marcos.    │
 └─────────────────────────────────────────────────────────────────────────┘
                                    ▲
                                    │
 ┌─────────────────────────────────────────────────────────────────────────┐
 │ TIER 2: CALIDAD ALTA (8.5 - 9.0/10) · LLMS FUERTES EN MODO TEXTO        │
 │ • Entornos: Claude 3.5 Sonnet (Claude.ai) o GPT-4o (ChatGPT Plus).      │
 │ • Cómo funciona: El LLM escribe el JSON directamente en el chat.        │
 │ • Resultado: Excelente para diagramas simples y medianos (5 a 15 nodos).│
 │ • Limitación: En diagramas de más de 20 cajas, como el LLM no "calcula" │
 │   píxeles sino que predice texto, pueden ocurrir pequeños desajustes de │
 │   10-20px en flechas o textos largos.                                   │
 └─────────────────────────────────────────────────────────────────────────┘
                                    ▲
                                    │
 ┌─────────────────────────────────────────────────────────────────────────┐
 │ TIER 3: CALIDAD CONCEPTUAL (7.0 - 7.5/10) · CHATGPT FREE (GPT-4o mini)  │
 │ • Entorno: Un estudiante en ChatGPT Gratuito con Custom Instructions.   │
 │ • Cómo funciona: El modelo pequeño genera el JSON en el chat.           │
 │ • Qué hace bien: Entiende la lógica del negocio o la economía           │
 │   (ej. "Flujo circular de la renta", "Oferta y Demanda", "Cadena B2B"). │
 │ • Limitación real: No puede generar un tablero de 450 elementos como el │
 │   de SEAMOSGENIOS; generará un diagrama útil de 5 a 8 cajas, pero       │
 │   visualmente más básico y sin validación matemática en bucle.          │
 └─────────────────────────────────────────────────────────────────────────┘
```

### 🎓 El Ejemplo del Estudiante de Economía en ChatGPT Free
Si un estudiante de economía le pide a ChatGPT Free:
> *"Hazme un diagrama del flujo circular del ingreso con Familias, Empresas, Mercado de Bienes, Mercado de Factores y Gobierno"*

* **En ChatGPT Free (Web):** Obtendrá un diagrama conceptualmente claro y ordenado de 5 cajas con colores sobrios (7.5/10). Es excelente para estudiar o hacer tareas rápidas, pero no tendrá sub-capas complejas, matrices de roles o cálculos de colisiones.
* **En el Motor Sketion (Python/CLI):** Obtendrá un tablero de grado corporativo con arquetipo formal, pastillas de datos numéricos, iconos incrustados y 0 colisiones (10/10).

> [!TIP]
> **¿Cómo puede un estudiante obtener la calidad 10/10 totalmente GRATIS?**  
> Simplemente usando la **Terminal / CLI de Sketion** en su propia computadora (`sketion generate ...`). No requiere pagar suscripciones ni APIs externas, ya que el motor de Python local corre 100% gratis en su máquina.

---

## 📑 Tabla de Contenidos
1. [¿Qué es Sketion y cómo funciona internamente?](#1-qué-es-sketion-y-cómo-funciona-internamente)
2. [Cómo funciona y cómo lo usa el Agente de IA aquí (Antigravity IDE)](#2-cómo-funciona-y-cómo-lo-usa-el-agente-de-ia-aquí-antigravity-ide)
3. [Uso en ChatGPT / OpenAI (Guía para Plan Gratuito y Plan Plus)](#3-uso-en-chatgpt--openai-guía-para-plan-gratuito-y-plan-plus)
4. [Uso en Claude (Guía para Plan Gratuito y Plan Pro)](#4-uso-en-claude-guía-para-plan-gratuito-y-plan-pro)
5. [Uso en Editores de Código (Cursor, Windsurf y VS Code)](#5-uso-en-editores-de-código-cursor-windsurf-y-vs-code)
6. [Uso desde la Terminal y como Librería Python (100% Local y Gratuito)](#6-uso-desde-la-terminal-y-como-librería-python-100-local-y-gratuito)
7. [Visualización y Edición en Excalidraw, VS Code y Obsidian](#7-visualización-y-edición-en-excalidraw-vs-code-y-obsidian)
8. [Plantillas de Prompts Listas para Usar](#8-plantillas-de-prompts-listas-para-usar)

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

## 3. Uso en ChatGPT / OpenAI (Guía para Plan Gratuito y Plan Plus)

> [!IMPORTANT]
> **Aclaración de Pagos:** La creación de *Custom GPTs* propios y la subida de archivos persistentes de conocimiento (*Knowledge*) requieren una suscripción de pago a **ChatGPT Plus ($20/mes)**. Sin embargo, si estás en el **plan gratuito de ChatGPT (Free Tier)**, puedes usar Sketion al 100% siguiendo el **Método A** sin pagar un solo centavo.

### 🆓 Método A: En ChatGPT GRATIS (Free Tier — GPT-4o / GPT-4o mini)
Hay dos formas de usarlo gratis:

#### Opción 1: Mediante "Instrucciones Personalizadas" (Configuración Permanente)
1. En [ChatGPT](https://chatgpt.com), haz clic en tu foto de perfil (abajo a la izquierda) $\rightarrow$ **Configuración / Settings** $\rightarrow$ **Personalización / Custom Instructions**.
2. En la casilla *"¿Cómo te gustaría que responda ChatGPT?"*, pega el siguiente prompt del motor Sketion:
   ```text
   Actúa como Sketion Visual Architect (v8.0). Cuando te pida diagramas, flujos o arquitecturas, genera un archivo JSON nativo válido para Excalidraw (versión 2) aplicando:
   1. Regla del Acento Único: Máximo 1-2 nodos con color coral/rojo (#D93829); el resto en blanco (#FFFFFF) con bordes slate (#CBD5E1).
   2. Tipografía legible: 15px bold para títulos, 12px para viñetas explicativas.
   3. Vinculación estricta: Todo elemento de texto dentro de una tarjeta debe tener containerId apuntando al rectángulo, y el rectángulo debe incluirlo en boundElements.
   4. Cero cajas vacías: Llena armónicamente el espacio interior con viñetas o capas.
   Entrega el resultado exclusivamente en un bloque de código ```json listo para copiar.
   ```
3. Guarda los cambios. A partir de ese momento, **todos tus chats gratuitos de ChatGPT generarán diagramas compatibles con Sketion**.

#### Opción 2: Pegando el Prompt en el Chat
Si no quieres modificar tus instrucciones generales, simplemente copia el contenido de [`CLAUDE_PROJECT_INSTRUCTIONS.md`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/CLAUDE_PROJECT_INSTRUCTIONS.md) y pégalo como primer mensaje en tu chat gratuito.

---

### 💎 Método B: En ChatGPT PLUS / TEAM ($20/mes — Custom GPT Dedicado)
Si tienes ChatGPT Plus, puedes crear un asistente permanente con procesamiento de código:
1. Ve a **Explore GPTs** $\rightarrow$ **Create a GPT** $\rightarrow$ Pestaña **Configure**.
2. **Name:** `Sketion Visual Architect`
3. **Instructions:** Pega el contenido completo de [`skill.md`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/skill.md).
4. **Capabilities:** Activa *Code Interpreter / Advanced Data Analysis*.
5. **Knowledge:** Sube los archivos de la carpeta `references/` (`style-guide.md`, `layout-rules.md`, `types-catalog.md`).

---

## 4. Uso en Claude (Guía para Plan Gratuito y Plan Pro)

> [!IMPORTANT]
> **Aclaración de Pagos:** La función de *Claude Projects* (proyectos con memoria compartida de archivos) es exclusiva de **Claude Pro / Team ($20/mes)**. Si usas **Claude Free**, puedes usar Sketion de forma 100% gratuita siguiendo el **Método A**.

### 🆓 Método A: En Claude GRATIS (Free Tier en Claude.ai)
1. Inicia una conversación nueva en [Claude.ai](https://claude.ai).
2. Adjunta el archivo [`skill.md`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/skill.md) o pega el contenido de [`CLAUDE_PROJECT_INSTRUCTIONS.md`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/CLAUDE_PROJECT_INSTRUCTIONS.md).
3. Pídele lo que deseas diseñar:
   > *"Diseña un diagrama en formato Excalidraw para un sistema de comercio electrónico con pagos Bold, facturación DIAN y módulo de PQRS."*
4. Claude te devolverá el bloque JSON de Excalidraw. Cópialo y pégalo en [excalidraw.com](https://excalidraw.com) con `Cmd + V` / `Ctrl + V`.

---

### 💎 Método B: En Claude PRO / TEAM (Claude Projects)
1. Ve a **Projects** $\rightarrow$ **Create Project** $\rightarrow$ Nómbralo `Sketion Architecture`.
2. En **Project Knowledge**, sube:
   * `skill.md`
   * `references/style-guide.md`
   * `references/layout-rules.md`
3. En **Set Custom Instructions**, pega el contenido de [`CLAUDE_PROJECT_INSTRUCTIONS.md`](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/CLAUDE_PROJECT_INSTRUCTIONS.md).
4. Tendrás un entorno dedicado de diseño gráfico ilimitado.

---

## 5. Uso en Editores de Código (Cursor, Windsurf y VS Code)

> **Costo:** 100% Gratuito en la ejecución local del motor.

### A. En Cursor (`.cursorrules` o `.cursor/rules/`)
Crea el archivo `.cursorrules` en tu proyecto:
```markdown
# Sketion Diagram Engine Rules
Cuando se te pida diseñar o exportar diagramas, flujos o arquitecturas:
1. Utiliza siempre el motor Sketion ubicado en el workspace.
2. Construye escenas mediante `render.excalidraw_builder.ExcalidrawScene`.
3. Aplica las primitivas `add_stack_layer()`, `add_feature_card()`, `add_quad_card()`.
4. Ejecuta `validate_scene(auto_repair=True)` para certificar calidad >= 95/100 antes de entregar el archivo .excalidraw.
```

### B. En Windsurf (`.windsurfrules`)
Agrega la misma directiva en `.windsurfrules`. Cascade ejecutará automáticamente los scripts de Python para generar los `.excalidraw`.

---

## 6. Uso desde la Terminal y como Librería Python (100% Local y Gratuito)

Sketion incluye un CLI completo que funciona sin internet y sin gastar créditos de ninguna API:

```bash
# 1. Instalación en tu terminal:
curl -fsSL https://raw.githubusercontent.com/luisrodriguez-rgb/Sketion-Diagram-Design-Engine-.git/main/install.sh | bash

# 2. Listar arquetipos disponibles:
sketion types

# 3. Generar un diagrama automáticamente:
sketion generate "Pipeline de Conciliación Bancaria" --type pipeline --output conciliacion.excalidraw --validate

# 4. Validar y auto-reparar cualquier archivo existente:
sketion validate mi_diagrama.excalidraw
```

---

## 7. Visualización y Edición en Excalidraw, VS Code y Obsidian

Todos los archivos generados con `.excalidraw` se pueden abrir y editar en:

* **[Excalidraw Web (Gratis)](https://excalidraw.com):** Clic en la carpeta superior izquierda $\rightarrow$ **Open / Abrir** $\rightarrow$ Selecciona tu archivo.
* **VS Code / Cursor (Gratis):** Instala la extensión **Excalidraw** (`pomdtr.excalidraw-editor`). Al abrir cualquier archivo `.excalidraw`, se abrirá como un lienzo visual interactivo.
* **Obsidian (Gratis):** Instala el plugin comunitario **Obsidian-Excalidraw**.

---

## 8. Plantillas de Prompts Listas para Usar

### Prompt para Arquitectura de Software
```text
Actúa como Sketion Visual Architect. Diseña un diagrama en formato Excalidraw nativo para una arquitectura de microservicios con: API Gateway (Hero en coral), Servicio de Autenticación con Redis, Base de Datos PostgreSQL particionada y Cola Kafka. Aplica el arquetipo Layer Stack, vincula todos los textos con containerId y usa conectores a 90°.
```

### Prompt para Procesos y Flujos de Negocio (Swimlanes)
```text
Actúa como Sketion Visual Architect. Diseña un diagrama de flujo en Excalidraw para un proceso de onboarding de clientes en 4 carriles (Cliente, Pasarela de Pago, Sistema de Facturación, Operaciones). Aplica el arquetipo Swimlanes, utiliza la regla del acento único y asegúrate de que no haya colisiones ni solapamientos entre tarjetas.
```
