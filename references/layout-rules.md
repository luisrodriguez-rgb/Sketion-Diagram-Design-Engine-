# Reglas de Layout y Distribución Espacial de Sketion

Este documento define la gramática geométrica y las reglas de enrutamiento espacial para los diagramas de Sketion en Excalidraw.

---

## 1. Reglas de Enrutamiento de Conectores (Routing Ortogonal)

1. **Codos a 90º (Ortogonales):** Todos los conectores entre nodos que no estén perfectamente alineados en el mismo eje deben doblar con ángulos rectos (90º) en lugar de cruzar diagonalmente.
2. **Separación de Puntos de Anclaje (Fan-out):** Cuando 2 o más flechas salen o entran al mismo lado de una caja, sus puntos de contacto deben distribuirse uniformemente con un espacio $\ge 16\text{ px}$ entre sí. Nunca encimar dos flechas en el mismo punto.
3. **Despeje de Etiquetas de Flecha:** Las etiquetas en conectores deben colocarse a $10\text{ px}$ por encima de la línea o en el punto medio exacto con una máscara de fondo que no tape el trazo.
4. **Prohibición de Traspaso de Nodos:** Ningún conector puede cruzar por detrás o por encima de una caja que no sea su destino u origen. El enrutador debe rodear la caja por su margen exterior.

---

## 2. Márgenes, Gaps y Padding

| Elemento | Padding / Gap Mínimo | Propósito |
| :--- | :---: | :--- |
| **Padding interno de Frame** | $40\text{ px}$ | Separación del borde del frame respecto al contenido |
| **Gap horizontal entre nodos (Flow)** | $50\text{ px} - 80\text{ px}$ | Espacio para flechas y etiquetas de conexión |
| **Gap vertical entre niveles (Tree)** | $100\text{ px} - 140\text{ px}$ | Separación clara entre nivel padre e hijos |
| **Gap entre carriles (Board)** | $40\text{ px}$ | Espacio para líneas divisorias punteadas |
| **Separación entre Frames (Cursor)** | $150\text{ px}$ | Evitar que tableros vecinos se toquen |

---

## 3. Presupuestos Espaciales por Nivel de Detalle

- **Simple:** 3 a 5 nodos principales. Ancho máximo de frame: $\approx 1000\text{ px}$.
- **Balanced (Default):** 6 a 8 nodos principales. Ancho máximo de frame: $\approx 1400\text{ px}$.
- **Detailed:** 9 a 12 nodos estructurados en 2 niveles o clusters. Ancho máximo de frame: $\approx 1800\text{ px}$.
