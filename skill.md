---
name: sketion-diagram-design
description: Generador editorial de diagramas y tableros nativos para Excalidraw (.excalidraw). Arquitectura desacoplada en 4 capas (Semántica -> Layout -> Render -> Calidad Visual) con soporte de Smart Defaults, niveles de detalle, Catálogo de 20 Arquetipos Visuales y motor de renderizado editorial de alta precisión sin colisiones.
license: MIT
metadata:
  version: "3.3"
---

# Sketion Diagram Design Skill (Motor Editorial para Excalidraw)

Crea tableros y diagramas profesionales con calidad editorial, diseño limpio, cero amontonamientos y editabilidad nativa total en formato `.excalidraw`.

Combina los principios de **Diagram Design** (densidad 4/10, regla del acento único, eliminación de ruido visual) con los **Arquetipos Editoriales de Alto Impacto** (estilo Miro Nico: Post-it rotados, chips de métrica gigantes, slots de captura y banners de remate) y la precisión geométrica del motor de **Sketion 3.3**.

---

## 0. Smart Defaults & Progressive Disclosure (Sin Fricción)

**No interrumpir al usuario con formularios de preguntas.** El motor resuelve automáticamente la intención semántica y genera el tablero terminado en el primer turno:

- **Si el usuario especifica:** Respetar sus elecciones (paleta, roughness, detalle, modo, arquetipo).
- **Si no se especifica nada (Smart Defaults automáticos):**
  - **Modo:** Claro (`viewBackgroundColor: "#F4F4F4"` lienzo editorial o `"#FFFFFF"`).
  - **Trazo (`roughness`):** `0` (Limpio, técnico, vectorial profesional).
  - **Paleta:** `MIRO_EDITORIAL` (`#F4F4F4` base, `#0C0C0C` tinta, `#E03A2F` acento de dolor, `#FFE95C` sticky notes).
  - **Nivel de Detalle:** `balanced` con descomposiciones multi-frame si el problema excede 9 nodos.
  - **Métricas Faltantes:** Estimar cifras creíbles de industria y documentarlas al pie en lugar de dejar huecos con `[TU CIFRA]`.

---

## 1. Reglas de Micro-Diseño y Cero Colisiones (Core 3.3)

1. **Centrado Geométrico del Texto:**
   - La coordenada $Y$ del elemento de texto se calcula exactamente según la altura real de las líneas:
     $$\text{text\_h} = \text{line\_count} \times \text{font\_size} \times 1.35$$
     $$\text{text\_y} = y + \frac{\text{card\_h} - \text{text\_h}}{2}$$
   - Se activa `autoResize: True` y `verticalAlign: "middle"` para centrado bidimensional perfecto.

2. **Separación de Scopes (*Gutter Seguro de 65px*):**
   - Las columnas de infraestructura/scopes se disponen consecutivamente garantizando un canal libre de $65\text{px}$ entre sus bordes. Cero solapamiento de líneas divisorias.

3. **Anclaje de Salida en Saltos de Columna (*Cross-Scope Bypass*):**
   - Cuando una flecha cruza múltiples columnas ($dx > 350\text{px}$), su pastilla protectora se ancla en el origen ($x_1 + 55\text{px}, y_1 - 14\text{px}$), **dejando los scopes intermedios 100% limpios y sin colisiones de etiquetas**.

4. **Conectores de Flujo con Separación de 95px:**
   - En flujos secuenciales, las tarjetas se separan exactamente $95\text{px}$ para que las pastillas de transición (`[Verificar]`, `[Pagar]`) queden suspendidas en el centro exacto de la flecha sin pisar las cajas.

5. **Grillas Tabulares Proporcionales y Dinámicas:**
   - El ancho de cada columna de la matriz se calcula según la longitud máxima de su texto (hasta 560px para explicaciones) y la altura de fila se adapta a las líneas reales.

---

## 2. Paleta Editorial Miro Nico en Excalidraw

```python
MIRO_PALETTE = {
    "CANVAS": "#F4F4F4",          # Fondo suave de pizarra
    "CARD": "#FFFFFF",            # Tarjetas blancas nítidas
    "CARD_BORDER": "#BDBDBD",     # Borde suave 1.5px
    "INK": "#0C0C0C",             # Tinta negra sólida para titulares y chips
    "MUTED": "#9A9A9A",           # Texto secundario y conectores de contexto
    "STICKY": "#FFE95C",          # Post-it amarillo con micro-rotación (-1.5° a +1.5°)
    "PAIN_RED": "#E03A2F",        # Alertas, cuellos de botella y números críticos
    "PAIN_BG": "#FDEFEF",         # Fondo de tarjetas de dolor o antes/legacy
    "PAIN_BORDER": "#F05A5A",     # Borde discontinuo de slots de captura
    "BANNER_PINK": "#F5BEC0",     # Frase de remate / punchline inferior
    "PASTEL_BLUE": "#9BC7E4",     # Cabeceras de fases y zonas
    "PASTEL_GREEN": "#C2E5D3"     # Confirmaciones y estados exitosos
}
```

---

## 3. Catálogo Maestro de los 20 Arquetipos Visuales

| Código | Arquetipo | Estructura Geométrica | Caso de Uso Principal |
| :-: | :--- | :--- | :--- |
| **A** | **EL CEREBRO** | Hub circular central con 4 ramas radiales | "Todo mi producto/sistema dentro de una herramienta" |
| **B** | **LAS FASES** | 6 cuadrantes con numerales gigantes (120px) | Roadmaps de 90 días, progresiones con gates |
| **C** | **LA SERPIENTE** | Curva S continua en vaivén (Boustrophedon) | Procesos lineales de 8 a 16 pasos sin desbordar |
| **D** | **EL DUELO (VS)** | 2 mitades enfrentadas con espina de stickies | Antes vs Después / Legacy vs Moderno / Pitches |
| **E** | **LA CADENA** | Swimlanes paralelos por actor con handoffs | Procesos multi-actor (Cliente, Máquina, Operario) |
| **F** | **EL EMBUDO** | Bloques trapezoidales descendentes con drop-off | Conversión de ventas, pipelines de contratación |
| **G** | **LA PIRÁMIDE** | 4-5 capas horizontales apiladas de base a cúspide | Modelos de madurez, niveles de seguridad |
| **H** | **EL RADAR 2x2** | Eje cartesiano ortogonal en 4 cuadrantes pastel | Priorización Impacto vs Esfuerzo, riesgos |
| **I** | **EL FLYWHEEL** | Círculo de 4-6 nodos con flechas perimetrales | Bucles de crecimiento (Growth Loops), retención |
| **J** | **LA CEBOLLA** | Anillos concéntricos anidados hacia el núcleo | Clean Architecture, Hexagonal, Data Governance |
| **K** | **EL KANBAN WIP** | Columnas de estado con límites WIP en cabecera | Pipelines ágiles, releases, colas de trabajo |
| **L** | **EL ICEBERG** | Línea de agua: 15% visible vs 85% oculto | Deuda técnica, complejidad backend vs UI simple |
| **M** | **LA ESPINA** | Eje horizontal con costillas temáticas diagonales | Análisis de causa raíz (Ishikawa), post-mortems |
| **N** | **LA GALERÍA 3x3** | Grilla modular simétrica con chips de status | Catálogo de microfrontends, suite de productos |
| **O** | **ÁRBOL DECISIÓN** | Dilema inicial que bifurca en ramas SÍ/NO | Protocolos de escalado, triaje, reglas de negocio |
| **P** | **CADENA DE VALOR** | Franjas superiores y 5 cajas con chevron final | Mapeo estratégico de operaciones y márgenes |
| **Q** | **PILARES BENCHMARK**| Podio de 3 a 5 columnas con barras de llenado | Comparativa de rendimiento, latencia y costes |
| **R** | **ROADMAP GATES** | Timeline horizontal con diamantes de validación | Lanzamientos v3.0, auditorías SOC2 / ISO |
| **S** | **MATRIZ CRUD** | Grilla de Servicios (Y) vs Entidades (X) | Mapeo de propiedad de datos (Data Ownership) |
| **T** | **CAJA EXPLOTADA** | Caja macro conectada con guías a zoom detallado | Explicar el funcionamiento interno de un motor |

---

## 4. Checklist de Calidad antes de Entregar

- [ ] ¿El archivo tiene extensión `.excalidraw` y es JSON válido minificado?
- [ ] ¿El texto dentro de todas las tarjetas está centrado vertical y horizontalmente?
- [ ] ¿Los scopes tienen separación limpia (mínimo 65px de gutter) sin solapamiento?
- [ ] ¿Las flechas largas no amontonan pastillas de texto en columnas intermedias?
- [ ] ¿Las tablas/matrices muestran todo el texto completo sin truncamientos?
- [ ] ¿Se utilizó la paleta editorial con máximo 1-2 acentos focales?
- [ ] ¿El validador `validate_scene()` devuelve `PASS` con puntuación global $\ge 95/100$?

---

## 5. Referencias y Archivos de Prueba

- Catálogo Completo de Arquetipos: [docs/catalogo-20-arquetipos-visuales.md](docs/catalogo-20-arquetipos-visuales.md)
- Propuesta de Mejoras Estratégicas: [docs/propuesta-mejoras-miro-sketion.md](docs/propuesta-mejoras-miro-sketion.md)
- Walkthrough Completo de Pruebas V3: [docs/walkthrough-pruebas-v3.md](docs/walkthrough-pruebas-v3.md)
- Demos Excalidraw Nativo: [PRUEBAS_V3/](PRUEBAS_V3/)
