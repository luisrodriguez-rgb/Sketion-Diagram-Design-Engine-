---
name: sketion-diagram-design
description: Generador editorial de diagramas y tableros nativos para Excalidraw (.excalidraw). Arquitectura desacoplada en 4 capas (Semantica -> Layout -> Render -> Calidad Visual) con motor de inferencia por audiencia (Audience-Aware Engine), Catalogo Completo de 27 Tipos Visuales (Lakehouse, Estrategia 2x2, Software, Operaciones, DataViz), simetria 1:1 en journeys, enrutamiento inter-zonas y evaluador de Semantic Hard Constraints sin colisiones.
license: MIT
metadata:
  version: "4.0"
---

# Sketion Diagram Design Skill (Motor Editorial para Excalidraw v4.0)

Crea tableros y diagramas profesionales con calidad editorial, diseno limpio, cero amontonamientos y editabilidad nativa total en formato `.excalidraw`.

Combina los principios de **Diagram Design** (densidad 4/10, regla del acento unico, eliminacion de ruido visual) con el **Motor de Inferencia de Audiencia**, los **27 Tipos Visuales de Diagramacion**, y los **9 Motores de Layout Geometrico Base**.

---

## 0. Motor de Decision de Audiencia (Audience-Aware Engine)

Sketion adapta autonomamente la seleccion de tipos visuales, la densidad de informacion y el vocabulario segun el perfil del receptor:

| Perfil de Audiencia | Tipos Visuales Principales | Foco Semantico Obligatorio | Elementos a Suprimir (Evitar Ruido) | Tono Editorial |
| :--- | :--- | :--- | :--- | :--- |
| **CEO / Directivo** | `consultant_2x2`, `it_current_state`, `timeline`, `pyramid_funnel` | ROI, Margen, Coste Fijo $0, Retencion, Fases de Aprobacion | APIs, Microservicios, Codigo, Cronometros de segundos | Estrategico / Financiero |
| **Gerente Operaciones** | `swimlane`, `process`, `gantt`, `dp_security_matrix` | Layout de Planta, Segregacion Fisica, Takt Time, Batching, Roles | Modelos Financieros Macro, Arquitectura Cloud, Nube | Industrial / Planta |
| **Equipo Producto / Tech**| `architecture`, `sequence`, `state_machine`, `layer_stack` | Arquitectura Cloud, Microservicios, User Journey, Slots UI, KDS | Negociaciones Laborales, Nomina, Tramites Administrativos | Tecnico / Software |
| **Ingenieria de Datos**| `medallion`, `data_flow`, `dp_integration`, `er_model` | Multi-tier Storage, Pipelines ETL por Rol, Permisos RBAC | Discursos Comerciales, Planos Fisicos de Edificio | Data Lakehouse / RBAC |
| **Inversionistas / Pitch**| `consultant_2x2`, `pyramid_funnel`, `loop_flywheel`, `bar_chart` | Tamano de Mercado, Metricas Heroicas, Traccion, Dolor vs Solucion | Tablas Complejas, Diagramas de Red Detallados | Impacto / Traccion |

---

## 1. Catalogo Maestro de los 27 Tipos Visuales de Sketion 4.0

### 1. Data Platforms & Lakehouse
* **`medallion`:** Almacenamiento Lakehouse multi-tier (`Raw` $\rightarrow$ `Bronze` $\rightarrow$ `Silver` $\rightarrow$ `Gold` $\rightarrow$ `Archive`).
* **`data_flow`:** Pipeline analitico segregado por roles funcionales (`Data Engineer`, `Data Scientist`, `BI Analyst`).
* **`dp_integration`:** Topologia de fuentes heterogeneas $\rightarrow$ Data Platform Core $\rightarrow$ Consumidores de BI.
* **`dp_security_matrix`:** Matriz de control de acceso RBAC granular con estados Admin, Write, Read, None.
* **`er_model`:** Diagrama entidad-relacion con tipos de datos, claves primarias (PK) y foraneas (FK).

### 2. Estrategia & Consultoria Ejecutiva
* **`consultant_2x2`:** Matriz de escenarios cartesianos con nombres de cuadrantes (Quick Wins, Major Projects, etc.).
* **`quadrant`:** Posicionamiento bidimensional de impacto vs esfuerzo en plano cartesiano.
* **`loop_flywheel`:** Bucle virtuoso continuo con estaciones perimetrales alrededor de un hub central.
* **`it_current_state`:** Diagnostico de silos legados caoticos vs arquitectura destino unificada.
* **`venn`:** Superposicion conceptual y conjuntos intersecados (Deseable x Factible x Viable).
* **`pyramid_funnel`:** Jerarquia piramidal de capas y embudo de conversion con tasas de retencion.

### 3. Software & Arquitectura Cloud
* **`architecture`:** Microservicios distribuidos con boundaries de red, VPCs y gateways.
* **`high_level`:** Stack completo de infraestructura sobre cluster con orquestador superior.
* **`sequence`:** Secuencia temporal de mensajes con lifelines, cajas de activacion y retornos discontinuos.
* **`state_machine`:** Maquina de estados finitos con transiciones y guardas de ciclo de vida.
* **`layer_stack`:** Pila de capas de abstraccion tecnologica estructuradas verticalmente.
* **`nested`:** Jerarquia de contencion fisica y scopes anidados con margenes de seguridad.
* **`flowchart`:** Flujograma de decision logica con nodos de evaluacion y bifurcacion de caminos.

### 4. Procesos & Operaciones
* **`swimlane`:** Flujo de trabajo interdepartamental segregado por carriles funcionales.
* **`process`:** Flujo secuencial continuo de proceso de negocio con traspasos (handoffs) entre actores.
* **`gantt`:** Cronograma de fases, duraciones, dependencias y puertas de aprobacion (gates).
* **`timeline`:** Eje cronologico con hitos estrategicos alternados arriba y abajo sin colisiones.
* **`org_chart`:** Organigrama jerarquico de propiedad y enrutamiento de equipos.
* **`tree`:** Taxonomia y arbol balanceado de clasificacion jerarquica.

### 5. DataViz Cuantitativo Nativo en Canvas
* **`bar_chart`:** Grafico comparativo de barras cuantitativas con acento focal unico.
* **`line_chart`:** Grafico de lineas continuas y evolucion de tendencias temporales multiserie.
* **`scatter_plot`:** Diagrama de dispersion y correlacion en plano cartesiano.
* **`radar_spider`:** Comparativa multieje poligonal sobre coordenadas radiales concentricas.

---

## 2. Uso via CLI

```bash
# Listar los 27 tipos visuales disponibles:
python3 sketion_cli.py types

# Generar un tipo especifico:
python3 sketion_cli.py generate "Pipeline Lakehouse E-Commerce" --type medallion --output lakehouse.excalidraw --validate
```

---

## 3. Checklist de Calidad antes de Entregar

- [ ] El archivo tiene extension `.excalidraw` y es JSON valido minificado.
- [ ] La estructura del diagrama responde a la audiencia objetivo (CEO, Ops, Tech, Devs, Data).
- [ ] Si es un User Journey, existe correspondencia 1:1 entre pasos y slots de captura.
- [ ] Si es una planta operativa, existen flechas de transito fisico entre zonas.
- [ ] El texto dentro de todas las tarjetas esta centrado vertical y horizontalmente.
- [ ] Los scopes tienen separacion limpia (minimo 65px de gutter) sin solapamiento.
- [ ] Se utilizo la paleta editorial con maximo 1 acento focal principal.
- [ ] El validador `validate_scene()` devuelve `PASS` con puntuacion global >= 90/100.
