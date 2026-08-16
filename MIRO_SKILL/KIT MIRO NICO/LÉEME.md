# LÉEME PRIMERO · Kit MIRO NICO

Descomprime este .zip. Dentro tienes 8 archivos. Sigue estos 4 pasos y en 10 minutos
puedes hacer boards con este estilo.

```
KIT MIRO NICO/
├── LÉEME.md                      ← esto
├── CLAUDE.md                     ← las instrucciones del proyecto (impide las preguntas)
├── base.md                       ← las reglas del estilo
├── Miro A - El Cerebro.dc.html   ← los 5 ejemplos que se forkean
├── Miro B - Las Fases.dc.html
├── Miro C - La Serpiente.dc.html
├── Miro D - El Duelo.dc.html
├── Miro E - La Cadena.dc.html
├── image-slot.js                 ← los huecos de captura arrastrables
└── support.js                    ← motor de los .dc.html (no lo toques)
```

**Míralos antes de nada:** abre cualquiera de los cinco `.dc.html` con doble clic. Se
abren en el navegador sin instalar nada. Así ves qué es cada letra.

---

## PASO 1 · Crea el proyecto del estilo

En Claude Design → **Nuevo proyecto** → nómbralo `MIRO NICO — Design System`.
En sus ajustes, márcalo como **Design System**.

Ese interruptor es lo importante: convierte el proyecto en algo que tus otros proyectos
pueden mirar para copiar el estilo.

## PASO 2 · Sube los 8 archivos ahí dentro

Arrástralos todos de golpe a ese proyecto. Los ocho, tal cual, sin renombrar.

**No sustituyas los `.dc.html` por capturas de pantalla.** Un estilo no se transmite
describiéndolo: se transmite dándole un board de verdad para copiar. Esa es toda la
diferencia entre "parecido" e "idéntico".

## PASO 3 · Crea tu proyecto de trabajo

Otro proyecto aparte, normal, llamado `Boards`. En sus ajustes, **enlaza el Design
System** del paso 1. Aquí es donde vivirán todos tus boards.

**Sube el `CLAUDE.md` a ESTE proyecto** (no al Design System). Ese archivo son las
instrucciones permanentes: le prohíbe abrir formularios de preguntas y le obliga a
forkear una de las cinco letras. Sin él, si escribes algo vago te preguntará.

## PASO 4 · Pruébalo

Chat nuevo en `Boards`. **El primer mensaje ya tiene que llevar el contenido** — no
empieces con "vamos a crear un board", eso no es un encargo, es un saludo. Pega esto:

```
No me hagas preguntas: tienes todo lo que necesitas abajo.
Board del estilo MIRO NICO. Forkea la composición D (EL DUELO) del design system
y cámbiale el contenido.

TÍTULO: ANTES IMPROVISABA / ahora tengo un sistema
TESIS: publicar sin sistema es trabajar el doble para la mitad de alcance
A QUIÉN: alguien que publica cuando le apetece y luego desaparece dos semanas
EL SISTEMA: decides el mes entero un día / grabas en bloque / publicas en automático
EL CONFLICTO: todo el mundo cree que el problema es la creatividad, y es la agenda
CIFRAS: piezas al mes 9 → 30 · horas semana 31 → 13 · días en blanco 5 → 0
PRUEBA: 3 capturas — el calendario lleno, un vídeo funcionando, el mes cerrado
CIERRE: comenta SISTEMA y te lo mando
```

Si sale un board con el estilo correcto, ya está montado.

---

## Si algo falla

**Sale un formulario de preguntas** → el prompt llegó cortado. Comprueba que la primera
línea es "No me hagas preguntas" y que la última que se pegó es el CIERRE.

**El board no se parece a los ejemplos** → el proyecto no tiene el Design System
enlazado, o dentro solo está el `base.md` sin los cinco `.dc.html`.

**Todos mis boards salen iguales** → está repitiendo composición. Dile la letra tú.
