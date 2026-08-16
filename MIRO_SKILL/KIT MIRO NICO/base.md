# MIRO NICO · sistema visual de boards

Lienzo de 3600px de ancho, fondo #F4F4F4, padding 70px. Pensado para grabarse detrás
de un reel: nada por debajo de 13px, los titulares se leen desde 3 metros.

## COLOR
```
#F4F4F4  lienzo                    #0C0C0C  tinta y chips de métrica
#bdbdbd  borde de caja             #FFE95C  sticky de etiqueta de sección
#F5BEC0  paralelogramo de frase de remate
#E03A2F  lo que duele y las cifras potentes
#F05A5A  marco de captura y de sub-board     #FDEFEF  fondo de caja roja
#9A9A9A  conector discontinuo (contexto)     #0C0C0C  conector sólido (columna vertebral)
```

## TIPOGRAFÍA
Archivo Black para titulares · Archivo para cuerpo · máximo 3 tamaños por board.

```html
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

## REGLAS INNEGOCIABLES
- Cajas blancas, borde 1.5px #bdbdbd, texto 14-15px. Sin sombras difusas.
- Chips de métrica: fondo negro, número enorme, etiqueta pequeña. El número manda.
- Sticky amarillo para las etiquetas de sección, con rotación de -2° a 2°.
- Etiquetas cortas solo en 2-3 flechas, nunca en todas.
- 3-4 huecos de captura con marco rojo 1.5px (`<image-slot>`).
- Denso y hecho a mano: sin huecos muertos, columnas equilibradas.
- Prohibido: emojis, degradados, gráficas de tarta, iconos de stock, texto de relleno.

## LAS 5 COMPOSICIONES
Se elige por la forma del contenido. **Nunca dos boards seguidos con la misma letra.**

| | Forma | Cuándo |
|---|---|---|
| **A · EL CEREBRO** | nodo central y ramas alrededor | "todo mi X dentro de Y" |
| **B · LAS FASES** | cuadrantes con números gigantes | roadmaps y progresiones |
| **C · LA SERPIENTE** | pasos en arcos que suben y bajan | procesos paso a paso |
| **D · EL DUELO** | board partido en dos mitades enfrentadas | antes / después |
| **E · LA CADENA** | carriles paralelos, uno por actor | sistemas con ramas simultáneas |

Cada letra tiene su archivo de ejemplo en este mismo Design System. **Para montar un board
nuevo se forkea el archivo de la letra elegida y se le cambia el contenido** — no se
construye desde cero.
