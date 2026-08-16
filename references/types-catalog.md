# Catálogo de Tipos de Diagramas Sketion (27 Tipos $\rightarrow$ 9 Motores)

Este catálogo mapea los **27 tipos de diagramas más utilizados en ingeniería, producto y diseño editorial** directamente a los **9 motores visuales base** de Sketion para Excalidraw.

---

## Mapeo Completo: 27 Tipos Visuales

| # | Tipo de Diagrama | Motor Sketion | Descripción y Reglas de Maquetación |
| :-: | :--- | :---: | :--- |
| **1** | **Architecture** | `red` | Componentes de backend, frontend, bases de datos y colas con flechas etiquetadas (HTTP, gRPC, SQL). |
| **2** | **Flowchart** | `flujo` | Flujo de decisiones con nodos de proceso y bifurcaciones con flechas condicionales (Sí/No). |
| **3** | **Sequence Diagram** | `flujo` | Actores en columnas o secuencia horizontal con mensajes numerados en orden cronológico. |
| **4** | **State Machine** | `red` | Estados (cajas con esquinas redondeadas) y transiciones con eventos/guards en flechas. |
| **5** | **ER / Data Model** | `matriz` / `red` | Entidades con campos tipados (PK, FK, string, int) y conectores de relación 1:N o N:M. |
| **6** | **Timeline** | `timeline` | Eje horizontal con marcadores circulares y tarjetas de hitos alternadas arriba/abajo. |
| **7** | **Swimlane** | `board` | Carriles verticales u horizontales por rol/departamento con pasos conectados a través de carriles. |
| **8** | **Quadrant / 2x2** | `matriz` | Cuadrícula de 4 celdas sobre dos ejes (Impacto vs Esfuerzo, Urgencia vs Importancia). |
| **9** | **Nested Hierarchy** | `arbol` / `red` | Cajas contenedoras que engloban subsistemas (Scope containment). |
| **10** | **Tree / Sitemap** | `arbol` | Jerarquía estricta Padre $\rightarrow$ Hijos $\rightarrow$ Nietos (máximo 3 niveles). |
| **11** | **Org Chart** | `arbol` | Estructura organizacional con roles, reportes directos y escalaciones. |
| **12** | **Venn Diagram** | `cerebro` | Conjuntos superpuestos con etiquetas en intersecciones o nodos satélites. |
| **13** | **Layer Stack** | `matriz` / `board` | Capas apiladas horizontalmente (Infraestructura $\rightarrow$ Datos $\rightarrow$ Lógica $\rightarrow$ Presentación). |
| **14** | **Pyramid / Funnel** | `flujo` / `board` | Fases de conversión con anchos decrecientes y métricas de drop-off. |
| **15** | **Consultant 2x2** | `matriz` | Escenarios con nombres de cuadrante (ej. Líderes, Retadores, Nicho) y tarjetas de contexto. |
| **16** | **Radar / Spider** | `dashboard` / `matriz` | Tabla o matriz de evaluación de entidades frente a 3-5 criterios cuantitativos. |
| **17** | **Loop / Flywheel** | `cerebro` | Ciclo continuo donde la última etapa alimenta la primera, con un hub central de estado acumulado. |
| **18** | **IT Current-State** | `board` | Mapa del estado legado clasificado por sistemas/departamentos para proyectos de modernización. |
| **19** | **High-Level System Map** | `red` | Vista de extremo a extremo de un cluster o plataforma con nodos agrupados en contenedores. |
| **20** | **Bar / Category Chart** | `matriz` | Comparación de magnitudes categóricas con barras proporcionales en Excalidraw. |
| **21** | **Line Trend Chart** | `timeline` | Línea de tendencia con puntos de inflexión y etiquetas de valor. |
| **22** | **Gantt Chart** | `timeline` | Eje temporal con barras de duración por fase y dependencias de inicio/fin. |
| **23** | **Scatter Distribution** | `matriz` | Dispersión de conceptos sobre un plano cartesiano. |
| **24** | **Multi-Actor Process** | `flujo` / `board` | Proceso secuencial que pasa por múltiples actores con traspasos de datos claros. |
| **25** | **Medallion Data Architecture** | `flujo` / `board` | 3 niveles de almacenamiento de datos: Bronze (Raw) $\rightarrow$ Silver (Clean) $\rightarrow$ Gold (Business). |
| **26** | **Data Flow Pipeline** | `flujo` | Pipeline de transformación de datos con origen, enriquecimiento, filtrado y destino. |
| **27** | **Security Matrix** | `matriz` | Matriz de permisos (Roles vs Acciones) con celdas coloreadas semánticamente (Lectura/Escritura/Denegado). |

---

## Resumen de los 9 Motores Visuales Base

```text
┌─────────────────────────────────────────────────────────────┐
│                   LOS 9 MOTORES BASE                        │
├──────────────┬──────────────────────────────────────────────┤
│ 1. CEREBRO   │ Hub central elíptico + ramas conectadas      │
│ 2. FLUJO     │ Pasos horizontales con flechas ortogonales   │
│ 3. RED       │ Nodos interconectados y clusterizados        │
│ 4. MATRIZ    │ Celdas con encabezados de fila y columna     │
│ 5. ÁRBOL     │ Jerarquía vertical descendente               │
│ 6. TIMELINE  │ Eje horizontal con hitos alternados          │
│ 7. BOARD     │ Carriles verticales con tarjetas apiladas    │
│ 8. DASHBOARD │ Grilla de chips numéricos gigantes (KPIs)    │
│ 9. STORYBOARD│ Diapositivas 1600x900 en secuencia          │
└──────────────┴──────────────────────────────────────────────┘
```
