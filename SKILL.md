---
name: prototypes
description: >-
  Seis prototipos visuales de verdad distintos de una misma página, app o panel, en estilo
  Dribbble clean, para comparar y elegir. Úsala cuando el usuario diga "/prototypes",
  "prototipos", "hazme varias versiones", "dame opciones de diseño", "no sé cómo quiero que
  se vea", "varias propuestas", o cuando arranque un diseño desde cero sin dirección decidida.
  Vale para landings, apps móviles y dashboards.
---

# Seis prototipos clean que no se parecen

El listón es Dribbble 2025-26 (búsquedas "web", "landing page", "mobile"): pocas piezas,
una sola tinta, un objeto o una foto protagonista, radios generosos y movimiento con el
scroll. El fallo de siempre es sacar **seis pieles del mismo esqueleto**: mismo titular,
mismas secciones en el mismo orden, mismo botón, y solo cambia color, fuente y foto. El
usuario lo nota enseguida ("me gustan, pero no son diferentes, falta creatividad"). Cada
prototipo tiene que ser **una idea distinta**, con su propia estructura y su propio texto,
dentro de un gusto clean. Y en todas sus referencias **la imagen es la página**: Kumo es
un vaso enorme sobre un montículo con el titular encima, Golfair una foto a sangre con
widgets de vidrio, Nuvé una cara con recuadros de UI. Una maqueta de texto con una foto de
adorno al lado no es eso. Por eso **la dirección no la eliges tú: la pone el dado.**

## Paso 1. Tira el dado. Obligatorio, y sin leerlo

```
python3 ~/.gemini/config/skills/prototypes/dado.py "<encargo tal cual>"   # Antigravity CLI
python3 ~/.claude/skills/prototypes/dado.py "<encargo tal cual>"          # Claude Code
```
No uses `find` (hay otro `dado.py` en `web-frontend`). Detecta solo si es `landing`,
`movil` o `panel`; si se equivoca, `--tipo movil`. Otras opciones: `--evitar nothing,estudio`
si el usuario descartó un estilo, `--solo liquid-glass` para forzar uno, `--repetir` para
ignorar el historial.

Devuelve seis fichas. Por orden de importancia:
1. **HERO** + **FOTO**: la primera pantalla ES esa imagen, grande, con su encuadre. Los seis
   heros son distintos en cada tirada y uno siempre es `fondo-completo` (foto que llena la
   ventana entera, sin margen ni tarjeta). El comparador enseña sobre todo esa primera
   pantalla: si los seis abren con titular + subtítulo + botón, parecen el mismo.
   **CONCEPTO** y **AL ABRIR**: la idea rectora y lo que pone ENCIMA de la imagen (etiquetas
   sobre las piezas, una tarjeta flotante con controles, una ficha de papel apoyada…).
2. **ESTRUCTURA**: cómo se recorre la página (capítulos, horizontal, una pantalla, índice
   lateral, tarjetas apiladas, artículo, tablero). No siempre hero + secciones.
3. **VOZ**: cómo habla, y la forma de su H1 (seco = 1-3 palabras; preguntas = H1 con
   interrogación; instrucciones = imperativo…). Seis H1 del mismo tono técnico-poético
   ("Ajuste milimétrico para…", "Calibración sin holguras…") es no haber leído la voz.
4. La piel: **estética, hero, nav, movimiento, paleta, tipos, foto y trampa**.
   La FIRMA es opcional: solo si sirve al concepto.

Todo lo demás es obligatorio salvo que choque de verdad con el encargo. Si un concepto no
encaja (un "plano" para una app sin lugar físico), adáptalo al encargo (el plano del
sistema, del flujo) antes de cambiarlo. La TRAMPA es lo que sale mal si no piensas, léela.

Estilos posibles (el usuario los eligió): `suave` (sale siempre), `minimal`,
`liquid-glass`, `nothing`, `lienzo`, `estudio`, `editorial`, `suizo`. (`color-plano` lo
descartó el usuario: "horrible".)
Caelestia NO: tiene su propia skill y aquí sobra al lado de `suave`.

## Paso 2. Datos comunes, textos propios

Escribe primero una **ficha de datos** del encargo (qué ofrece, precios orientativos,
horario, cómo llegar o cómo funciona) y úsala en los seis: los datos no cambian. **El texto
sí**: cada prototipo escribe su titular, su CTA y sus textos con su VOZ, y elige qué datos
enseña y en qué orden según su CONCEPTO. **Ningún titular ni CTA repetido entre los seis**
(el revisor lo detecta).
- Es el contenido de ESTE encargo: un taller tiene servicios, tarifas orientativas,
  horario y cómo llegar; una app tiene sus pantallas; un SaaS, lo que hace. Sin catálogo ni
  carrito si no es una tienda.
- 4-5 bloques como mucho en landing. Ninguno de relleno (testimonios inventados,
  "por qué elegirnos", logos de clientes).
- Datos que no te dieron: `000 000 000`, `Calle, nº`, `hola@ejemplo.com`, y al final
  **Datos que faltan**. Nunca un teléfono, una dirección o un logo de marca real
  inventados.

## Paso 3. Construye cada uno

Un fichero por prototipo, `p1.html` … `p6.html`, autónomo, en **su modo** (estudio y nothing arrancan en NEGRO; el resto en claro) y con una
función `toggleTheme()` que conmuta al otro tema (`body.dark-mode`, o `body.light-mode` en
los que arrancan en negro; sin botón propio: lo pone el comparador). Por debajo de 30 KB cada uno.

### Prohibido: lo que el usuario llama "muy IA"
- **Hero mitad texto, mitad imagen.** Ningún hero de dos columnas, tampoco disfrazado de
  bento (tarjeta de texto de 8 columnas + tarjeta de foto al lado). El dado ya no los da;
  no te los inventes.
- **Palabra clave del titular en otro color**, en cursiva de color o con degradado.
  El titular va en una sola tinta (se permite un gris más claro en una línea entera).
- **Fila horizontal de estadísticas** ("10x · 65 % · 24/7"), y tampoco en **carrusel o
  cinta en movimiento**. Si hay cifras, van dentro de una tarjeta del bento, con su
  gráfica, de una en una.
- **Brillos que no sirven**: `box-shadow` o `text-shadow` de color, blobs difuminados,
  degradados morados, estrellitas, bordes de neón. La luz la pone la imagen, no el CSS.
- Muchos colores. Fondo, tinta y como mucho un acento; el resto, grises del mismo tono.
- Maximalismo: si una sección tiene más de dos ideas, sobra una.
- Lo de siempre: emoji sobre el titular, tres tarjetas con icono, frases hechas, fuentes
  por defecto (§3 de [`web-frontend`](https://github.com/iaguito22/antigravity-skills) si la tienes).

### Lo que sí hacen las buenas
- **Titular** de peso 500 (no 700), grande, `letter-spacing: -0.03em`, `line-height: 1`,
  `text-wrap: balance`. Texto de apoyo a 15-17 px en gris, máximo dos líneas.
- **Una sola escala de radios** (p. ej. 12 · 20 · 28 · pill) y botones en píldora.
- **Micro-UI de verdad**: tarjetitas flotantes con un dato del encargo (próxima cita,
  estado de una reparación, un paso de un proceso), no cajas vacías.
- **Sombras** amplias y tenues teñidas del tono (`0 24px 48px -16px rgb(20 30 60 / .12)`),
  nunca grises al 30 %.
- **Nav** pequeña (13-14 px) y tranquila; CTA negra en píldora.
- Imágenes con `object-fit: cover`, `alt` real, `width` y `height`.

### Movimiento de scroll (la ficha dice cuál)
Siempre dentro de `@supports (animation-timeline: view())` y
`@media (prefers-reduced-motion: no-preference)`, animando solo `transform` y `opacity`:
```css
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .revela { animation: sube linear both; animation-timeline: view();
              animation-range: entry 0% cover 30%; }
    @keyframes sube { from { opacity: 0; transform: translateY(24px); } }
  }
}
```
`zoom-lienzo`: el contenedor del hero con `animation-timeline: scroll()` y un keyframe de
`scale(.92)` a `scale(1)` y de `border-radius: 32px` a `0`.

### Recetas de estilo (solo si te ha tocado)
- **liquid-glass**: `backdrop-filter: blur(24px) saturate(180%)`, fondo
  `rgba(255,255,255,.18)`, `border: 1px solid rgba(255,255,255,.5)`,
  `box-shadow: inset 0 1px 0 rgba(255,255,255,.7), 0 8px 32px rgb(0 0 0 / .12)`, y SIEMPRE
  una foto detrás.
- **nothing** (sacado de las capturas de Nothing X en la App Store, 2025): negro puro,
  tarjetas `#1b1b1b` de radio 20 en rejilla de 2 columnas; titulares de pantalla en
  **serifa fina** (peso 300, 28-34 px), la UI en sans pequeña y gris. Piezas propias:
  grupos de 3 botones redondos (activo blanco con icono negro, resto `#2a2a2a`); cifras finas
  con barra (`7/40`); filas con icono · nombre · valor · chevron; segmentado en píldora con
  el activo blanco; gráfica de columnas de puntos (SVG, `r=3`, el punto de arriba rojo);
  anillo de progreso tipo pista; dial circular. **Sin fuente de puntos**; el rojo
  `#d71921` solo en el anillo, el punto activo o UN botón.
  Movimiento (su app): la selección salta de un botón redondo a otro con un anillo que se
  desplaza; el cambio de tema funde toda la pantalla en 300 ms; al entrar en vista, las
  columnas de puntos se encienden de abajo arriba (`transition-delay` escalonado) y el
  anillo se dibuja con `stroke-dashoffset`; al pulsar, `scale(.96)`. Curvas suaves
  `cubic-bezier(.2,0,0,1)`, nada de rebotes.
- **suizo**: texto alineado a la izquierda sobre una rejilla de 12 columnas, filetes de
  `1px`, números de sección en mono, titular enorme a `clamp(3.5rem, 10vw, 9rem)`; radios
  pequeños (0-8 px) y el acento en un solo sitio.
- **lienzo**: `body` con el color exterior y `padding: 16px`; un `.lienzo` con
  `border-radius: 36px; overflow: hidden` que lo contiene todo.
- **estudio**: fondo plano `#0a0a0b` sin degradado; el render lo hace todo.
- **editorial**: productos recortados (PNG sin fondo, o JPEG sobre blanco puro que se
  funde con la tarjeta), titular Didone a `clamp(3rem, 8vw, 7rem)` peso 400.

### Imágenes
El dado reparte las fotos (línea FOTO HERO): `foto 1` … `foto 6`, **una para cada
prototipo, sin excepción**, con su encuadre según el hero. Genera exactamente esas
con `generate_image`, ni una más, **de una en una y dejando ~15 s entre ellas** (`sleep 15`):
seguidas disparan el límite por minuto. Si aun así da `429 Too Many Requests`, espera 60 s y
reinténtala una vez; si vuelve a fallar, descarga fotos libres de `images.unsplash.com` que
encajen con esa línea FOTO HERO, comprímelas igual y dilo en la entrega. **La foto tiene que ser del encargo.** Si no hay un objeto físico (una app, un SaaS, un
servicio), la foto es la escena de uso real: manos con el móvil, la cocina de una pareja, la
mesa de trabajo; o el móvil con la UI de la app. Nunca un cuadro, flores o un paisaje
genérico porque la ficha decía "el objeto protagonista". Prompt de director de arte: objeto, encuadre y luz concretos,
"soft 3D render, studio light" o "35mm film, natural light"; sin gente mirando a cámara ni
retratos de personas reales. Cópialas comprimidas:
`python3 ~/.gemini/config/skills/web-frontend/foto.py <origen> img1.jpg` (de ~850 a ~150 KB; solo si tienes
[`web-frontend`](https://github.com/iaguito22/antigravity-skills), si no, cualquier compresor).
**Nunca la misma foto en el hero de dos prototipos.** La foto va grande (más de media
pantalla o a sangre), no en una miniatura. Más abajo, en otras secciones, sí se pueden
reutilizar recortadas.

### Que se distingan de verdad
Antes de escribir código, describe cada prototipo en una frase **sin mencionar color,
fuente ni foto** ("una ficha de taller que vas rellenando", "una bici que se desmonta
mientras bajas"). Si dos frases se parecen, uno de los dos no ha cogido su CONCEPTO.
- El concepto manda sobre las secciones: un `configurador` tiene su herramienta viva, un
  `documento` parece un documento al bajar. Pero en la primera pantalla va encima de la
  imagen, nunca en su lugar.
- La estructura se tiene que notar al bajar: una `horizontal` avanza de lado, una
  `una-pantalla` casi no hace scroll, unas `apiladas` se tapan unas a otras.
- La interacción protagonista funciona de verdad (JS mínimo), no es un dibujo.
- Como mucho **dos** primeras pantallas con el titular dentro de una tarjeta blanca
  centrada; es el esqueleto al que converge todo si no piensas.
- Respeta la posición del titular que da el dado. Tres heros con el titular centrado
  sobre una foto son un solo prototipo repetido tres veces.
- Creativo no es recargado: una idea fuerte por prototipo, ejecutada limpia. Si metes
  concepto + firma + tres animaciones, sobra algo (§ maximalismo).

### Si es `movil` o `panel`
- **movil**: cada `p*.html` es un lienzo de 1280x1000 con la composición de la ficha
  (pantallas de 390x844 con `border-radius: 48px`, isla dinámica, barra de estado 9:41) y
  UI real de la app: listas con chevron, tarjetas, barra inferior de 4-5 iconos.
- **panel**: 1440 de ancho, rejilla de widgets de radio 24 con datos coherentes entre sí;
  una gráfica en SVG propio, no una imagen.

## Paso 4. El comparador: `comparar.html`

Seis `<iframe>` en rejilla (`repeat(3, minmax(0,1fr))` por encima de 1350 px, dos
columnas por debajo, una en móvil), fondo `#f4f4f2`, y en la cabecera de cada tarjeta el
nombre del estilo y un botón redondo `🌙` que llama a `toggleTheme()` de su iframe. Un
botón arriba que conmuta los seis.

**Escala con `zoom` y viewport fijo, nunca con `transform: scale()`**, o el iframe se
maqueta a 700 px y enseña la versión móvil:
```html
<style>
  .iframe-container { width: 100%; overflow: hidden; background: #fff; }
  .iframe-container iframe { display: block; width: 1280px; height: 1000px; border: 0;
                             zoom: var(--z, 1); pointer-events: none; }
</style>
<script>
  const VP_W = 1280, VP_H = 1000;          // panel: 1440 x 900
  function ajustarEscala() {
    document.querySelectorAll('.iframe-container').forEach(c => {
      const z = c.clientWidth / VP_W;
      c.style.setProperty('--z', z);
      c.style.height = Math.round(VP_H * z) + 'px';
    });
  }
  ajustarEscala(); addEventListener('load', ajustarEscala); addEventListener('resize', ajustarEscala);
  new ResizeObserver(ajustarEscala).observe(document.documentElement);
</script>
```
`pointer-events: none` para que la rueda haga scroll en el comparador, y un enlace
"Abrir ↗" por tarjeta para verlo entero (ahí se ve el movimiento de scroll).

Debajo de cada iframe, la ficha con nombres de una palabra para combinar:
```html
<div class="ingredientes">
  <div class="ing-row"><span class="ing-key">Concepto</span><span class="ing-val">configurador</span></div>
  <div class="ing-row"><span class="ing-key">Estructura</span><span class="ing-val">una-pantalla</span></div>
  <div class="ing-row"><span class="ing-key">Voz</span><span class="ing-val">cercano</span></div>
  <div class="ing-row"><span class="ing-key">Estilo</span><span class="ing-val">liquid-glass</span></div>
  <div class="ing-row"><span class="ing-key">Hero</span><span class="ing-val">widget</span></div>
  <div class="ing-row"><span class="ing-key">Nav</span><span class="ing-val">isla-vidrio</span></div>
  <div class="ing-row"><span class="ing-key">Movimiento</span><span class="ing-val">zoom-lienzo</span></div>
  <div class="ing-row"><span class="ing-key">Paleta</span><span class="ing-val"><code>#e9ecf1</code> · <code>#0b0b0c</code></span></div>
</div>
```

## Paso 5. Míralos antes de enseñarlos

En UNA llamada:
```
python3 ~/.gemini/config/skills/web-frontend/revisa.py p?.html; agy-ver abrir comparar.html && agy-ver foto los-seis && agy-ver logs && agy-ver cerrar
```
Luego abre dos prototipos sueltos y baja por ellos (`agy-ver abrir p2.html && agy-ver ve
'#<2ª sección>'`) para ver que el movimiento funciona y nada se rompe.

El revisor solo si tienes [`web-frontend`](https://github.com/iaguito22/antigravity-skills). Cada línea del revisor se corrige con una edición puntual. Después mira las capturas y
contesta, una por una:
1. ¿Algún hero es mitad texto, mitad imagen? ¿Algún titular tiene una palabra de otro color?
2. ¿Hay una fila de cifras, o un brillo de color que no aporta nada?
3. Mirando solo la primera pantalla de cada uno, ¿se sabe cuál es su concepto? ¿Cada H1
   tiene la forma de su voz? Tapando los nombres, ¿son seis IDEAS o seis colores? Si dos tienen las mismas
   secciones en el mismo orden, o comparten titular centrado y foto, rehaz uno siguiendo
   su CONCEPTO y su ESTRUCTURA; no lo des por bueno.
4. ¿El `suave` está hecho con mimo? Es el estilo que más le gusta al usuario.

## Paso 6. Entrega

Una línea por prototipo con su idea en una frase y sus ingredientes, una recomendación con motivo, y
**Datos que faltan** si los hay.
