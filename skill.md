---
name: sketion-diagram-design
description: Generador editorial de diagramas y tableros nativos para Excalidraw (.excalidraw). Arquitectura desacoplada en 4 capas (Semantica -> Layout -> Render -> Calidad Visual) con soporte de Smart Defaults, niveles de detalle, Catalogo de 20 Arquetipos Visuales y motor de renderizado editorial de alta precision sin colisiones.
license: MIT
metadata:
  version: "3.3"
---

# Sketion Diagram Design Skill (Motor Editorial para Excalidraw)

Crea tableros y diagramas profesionales con calidad editorial, diseno limpio, cero amontonamientos y editabilidad nativa total en formato `.excalidraw`.

Combina los principios de **Diagram Design** (densidad 4/10, regla del acento unico, eliminacion de ruido visual) con los **Arquetipos Editoriales de Alto Impacto** (Post-it rotados, chips de metrica gigantes, slots de captura y banners de remate) y la precision geometrica del motor de **Sketion 3.3**.

---

## 0. Smart Defaults y Progressive Disclosure (Sin Friccion)

**No interrumpir al usuario con formularios de preguntas.** El motor resuelve automaticamente la intencion semantica y genera el tablero terminado en el primer turno:

- **Si el usuario especifica:** Respetar sus elecciones (paleta, roughness, detalle, modo, arquetipo).
- **Si no se especifica nada (Smart Defaults automaticos):**
  - **Modo:** Claro (`viewBackgroundColor: "#F4F4F4"` lienzo editorial o `"#FFFFFF"`).
  - **Trazo (`roughness`):** `0` (Limpio, tecnico, vectorial profesional).
  - **Paleta:** `MIRO_EDITORIAL` (`#F4F4F4` base, `#0C0C0C` tinta, `#E03A2F` acento de dolor, `#FFE95C` sticky notes).
  - **Nivel de Detalle:** `balanced` con descomposiciones multi-frame si el problema excede 9 nodos.
  - **Metricas Faltantes:** Estimar cifras creibles de industria y documentarlas al pie en lugar de dejar huecos vacios.

---

## 1. Reglas de Micro-Diseno y Cero Colisiones (Core 3.3)

1. **Centrado Geometrico del Texto:**
   - La coordenada Y del elemento de texto se calcula exactamente segun la altura real de las lineas:
     text_h = line_count * font_size * 1.35
     text_y = y + (card_h - text_h) / 2
   - Se activa `autoResize: True` y `verticalAlign: "middle"` para centrado bidimensional exacto.

2. **Separacion de Scopes (Gutter Seguro de 65px):**
   - Las columnas de infraestructura/scopes se disponen consecutivamente garantizando un canal libre de 65px entre sus bordes. Cero solapamiento de lineas divisorias.

3. **Anclaje de Salida en Saltos de Columna (Cross-Scope Bypass):**
   - Cuando una flecha cruza multiples columnas (dx > 350px), su pastilla protectora se ancla en el origen (x1 + 55px, y1 - 14px), dejando los scopes intermedios 100% limpios y sin colisiones de etiquetas.

4. **Conectores de Flujo con Separacion de 95px:**
   - En flujos secuenciales, las tarjetas se separan exactamente 95px para que las pastillas de transicion queden suspendidas en el centro exacto de la flecha sin pisar las cajas.

5. **Grillas Tabulares Proporcionales y Dinamicas:**
   - El ancho de cada columna de la matriz se calcula segun la longitud maxima de su texto (hasta 560px para explicaciones) y la altura de fila se adapta a las lineas reales.

---

## 2. Paleta Editorial Miro Nico en Excalidraw

```python
MIRO_PALETTE = {
    "CANVAS": "#F4F4F4",          # Fondo suave de pizarra
    "CARD": "#FFFFFF",            # Tarjetas blancas nitidas
    "CARD_BORDER": "#BDBDBD",     # Borde suave 1.5px
    "INK": "#0C0C0C",             # Tinta negra solida para titulares y chips
    "MUTED": "#8B8B8B",           # Texto secundario y conectores de contexto
    "STICKY": "#FFE95C",          # Post-it amarillo con micro-rotacion (-1.5 a +1.5 grados)
    "PAIN_RED": "#E03A2F",        # Alertas, cuellos de botella y numeros criticos
    "PAIN_BG": "#FDEFEF",         # Fondo de tarjetas de dolor o antes/legacy
    "PAIN_BORDER": "#F05A5A",     # Borde discontinuo de slots de captura
    "BANNER_PINK": "#F5BEC0",     # Frase de remate / punchline inferior
    "PASTEL_BLUE": "#9BC7E4",     # Cabeceras de fases y zonas
    "PASTEL_GREEN": "#C2E5D3"     # Confirmaciones y estados exitosos
}
```

---

## 3. Catalogo Maestro de los 20 Arquetipos Visuales

| Codigo | Arquetipo | Estructura Geometrica | Caso de Uso Principal |
| :--- | :--- | :--- | :--- |
| **A** | **El Cerebro** | Hub circular central con 4 ramas radiales | Plataforma completa en un solo hub central |
| **B** | **Las Fases** | 6 cuadrantes con numerales gigantes | Roadmaps de 90 dias, progresiones con gates |
| **C** | **La Serpiente** | Curva S continua en vaiven (Boustrophedon) | Procesos lineales de 8 a 16 pasos |
| **D** | **El Duelo (VS)** | 2 mitades enfrentadas con espina de stickies | Antes vs Despues / Legacy vs Moderno |
| **E** | **La Cadena** | Swimlanes paralelos por actor con handoffs | Procesos multi-actor con llamadas API |
| **F** | **El Embudo** | Bloques trapezoidales descendentes | Conversion de ventas, pipelines de seleccion |
| **G** | **La Piramide** | Capas horizontales apiladas de base a cuspide | Modelos de madurez, capas de seguridad |
| **H** | **El Radar 2x2** | Eje cartesiano en 4 cuadrantes pastel | Priorizacion Impacto vs Esfuerzo, riesgos |
| **I** | **El Flywheel** | Circulo de 4-6 nodos con flechas perimetrales | Bucles de crecimiento y retencion |
| **J** | **La Cebolla** | Anillos concentricos anidados hacia el nucleo | Clean Architecture, Hexagonal, Gobernanza |
| **K** | **El Kanban WIP** | Columnas de estado con limites WIP | Pipelines agiles, colas de trabajo, releases |
| **L** | **El Iceberg** | Linea de agua: 15% visible vs 85% oculto | Deuda tecnica, complejidad backend vs UI |
| **M** | **La Espina** | Eje horizontal con costillas diagonales | Analisis de causa raiz (Ishikawa), post-mortems |
| **N** | **Galeria 3x3** | Grilla modular simetrica con status badges | Catalogo de microfrontends, suite de APIs |
| **O** | **Arbol Decision** | Dilema inicial con ramas SI/NO | Protocolos de escalado, triaje, reglas |
| **P** | **Cadena de Valor**| Franjas superiores y cajas con chevron | Mapeo estrategico de operaciones y margen |
| **Q** | **Benchmark** | Podio de columnas con barras de llenado | Comparativa de latencia, throughput y costes |
| **R** | **Roadmap Gates** | Timeline horizontal con diamantes de control | Lanzamientos v3.0, auditorias SOC2 / ISO |
| **S** | **Matriz CRUD** | Grilla de Servicios (Y) vs Entidades (X) | Mapeo de propiedad de datos (Data Ownership) |
| **T** | **Caja Explotada**| Caja macro con lineas guia a zoom | Explicar el funcionamiento interno de un motor |

---

## 4. Checklist de Calidad antes de Entregar

- [ ] El archivo tiene extension `.excalidraw` y es JSON valido minificado.
- [ ] El texto dentro de todas las tarjetas esta centrado vertical y horizontalmente.
- [ ] Los scopes tienen separacion limpia (minimo 65px de gutter) sin solapamiento.
- [ ] Las flechas largas no amontonan pastillas de texto en columnas intermedias.
- [ ] Las tablas/matrices muestran todo el texto completo sin truncamientos.
- [ ] Se utilizo la paleta editorial con maximo 1-2 acentos focales.
- [ ] El validador `validate_scene()` devuelve `PASS` con puntuacion global >= 95/100.

---

## 5. Referencias y Archivos de Prueba

- Catalogo Completo de Arquetipos: `docs/catalogo-20-arquetipos-visuales.md`
- Propuesta de Mejoras Estrategicas: `docs/propuesta-mejoras-miro-sketion.md`
- Walkthrough Completo de Pruebas: `docs/walkthrough-pruebas-v3.md`
- Suite de Pruebas Adversariales: `tests/adversarial/`
- Demos Excalidraw Nativo: `PRUEBAS_V3/` y `PRUEBAS_V4/`
