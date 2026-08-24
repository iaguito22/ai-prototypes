---
name: prototypes
description: >-
  Seis prototipos visuales de verdad distintos de una misma pagina, adaptados al
  encargo para comparar y elegir. Usala cuando el usuario diga "/prototypes",
  "hazme varias versiones", "dame opciones de diseño", "no se como quiero que se vea",
  o cuando arranque un diseño desde cero sin direccion estetica decidida.
---

# Seis prototipos que no se parecen

El fallo de siempre: te piden varias opciones y salen versiones de la misma cosa
(una clara y minimalista, una oscura de lujo, una de papel). Es la mediana del
entrenamiento. Aqui **la direccion no la eliges tu**.

## Paso 1. Tira el dado. Obligatorio.

```
python3 ~/.gemini/config/skills/prototypes/dado.py   # Antigravity CLI
python3 ~/.claude/skills/prototypes/dado.py          # Claude Code
```

`dado.py` vive junto a este `SKILL.md`: si la skill esta en otra ruta, la del
dado es esa misma. No lo tires "de memoria": sin ejecutarlo no hay tirada.

Te devuelve **seis direcciones completas** que rotan ortogonalmente entre las 12 familias de diseño del catálogo, sus 10 arquetipos de tarjeta (`Card`) y sus 10 distribuciones de navegación (`Nav`), con soporte para **MODO CLARO** (por defecto) y **MODO OSCURO**.

- El dado **recuerda las ultimas direcciones y no las repite**, para garantizar frescura. `--repetir` desactiva esa memoria si te da igual.
- `--semilla <texto>` si quieres poder repetir la misma tirada.
- `--evitar <familia>` si el usuario ya ha descartado un mundo entero.
- `--solo <familia>` para forzar una (ej. `--solo liquid-glass`, `--solo caelestia`, `--solo suizo`).

## Glosario de Nombres de Una Sola Palabra (Mix & Match)

Usa siempre estos identificadores directos en la ficha y en la entrega:

### Familias Estéticas (`Estilo`)
- `caelestia`, `nothing`, `liquid-glass`, `neumorphism`, `glassmorphism`, `industrial`, `claymorphism`, `producto`, `suizo`, `editorial`, `lujo`, `organico`.

### Los 10 Arquetipos de Tarjeta (`Card`)
- `bento` — tarjeta vertical limpia con chip de categoría/ración arriba y botón directo.
- `fila` — fila horizontal continua con render a la izquierda y selector `[- 1 +]` a la derecha.
- `dual` — tarjeta con pestañas internas `[Estándar | Trufa]` para conmutar variantes en vivo.
- `specs` — ficha de hardware con tabla mono de datos/cotas técnicas y pulsador mecánico `[PUSH]`.
- `split` — división 50/50 con render enmarcado a la izquierda y bloque de texto y botón a la derecha.
- `showcase` — vitrina centrada en el objeto con badge flotante arriba y botón ancho completo.
- `tabla` — fila ultradensa de inventario con miniatura reducida, código SKU y chip de stock.
- `dock` — cápsula redondeada flotante tipo píldora de interacción rápida.
- `acordeon` — tarjeta compacta con desplegable de detalles técnicos/alérgenos al pulsar.
- `documental` — estructura editorial con numeración `FIG. 01`, marco técnico y pie documental.

### Los 10 Arquetipos de Navegación (`Nav`)
- `centrada` — enlaces 100% centrados en la página sin nombre de marca.
- `anonima` — cápsula píldora suspendida con selectores de categoría/filtro, sin logotipo ni texto de marca.
- `split` — logotipo a la izquierda y enlaces/CTA a la derecha en los extremos del contenedor.
- `mono` — cabecera técnica en monospace continuo con marca, versión y enlaces en línea.
- `isla` — píldora flotante compacta de vidrio suspendida con logo minimalista y enlaces.
- `apilada` — logotipo centrado en la fila superior y barra de enlaces centrada en la fila inferior.
- `chasis` — panel de ingeniería con tornillería en esquinas y selector de canal `[01] [02]`.
- `minimal` — solo logotipo tipográfico a la izquierda y un botón de acción directo a la derecha.
- `subastas` — logotipo monumental al centro dividido por dos enlaces a cada lado entre filetes de 1px.
- `burbuja` — cápsula inflada redondeada con volumen suave 3D y dot de estado activo.

### Los Arquetipos de Cabecera Hero (`Hero`)
- `foto-split` — pantalla dividida con fotografía real de alta resolución enmarcada a un lado y texto con CTA al otro.
- `foto-hero` — fotografía inmersiva de producto/taller a sangre con tratamiento de luz y titular tipográfico integrado.
- `centrado` — titular masivo y lead 100% centrados en columna única limpia sin cajas laterales.
- `split` — pantalla dividida 50/50 con render técnico a la izquierda y texto a la derecha.
- `medidor` — consola técnica con barras de nivel, osciloscopio o cotas acústicas.
- `vitrina` — composición vertical centrada con el objeto sobre pedestal e insignia flotante.
- `editorial` — titular con filete vertical y dos columnas de texto tipo publicación de diseño.
- `masivo` — titular tipográfico monumental a escala gigante que ocupa el ancho completo.
- `manifiesto` — bloque editorial de declaración con cita textual del artesano en cursiva y firma.
- `burbuja` — volumen táctil suave con cápsula de relieve y badge convexo 3D.
- `optica` — panel translúcido con bisel iluminado y diagrama de ondas de fase.
- `m3` — composición tonal asimétrica por niveles tonales superpuestos.

## Paso 2. Fija lo que NO cambia

**Los seis prototipos llevan exactamente el mismo contenido (mismos productos/platos) y la misma estructura limpia simétrica.**

## Paso 3. Construye los seis en Modo Claro por defecto

Un archivo por prototipo: `p1.html`, `p2.html`, `p3.html`, `p4.html`, `p5.html`, `p6.html`, cada uno autónomo como **landing desktop completa y real** (Nav, Hero estructurado, Catálogo con el arquetipo de Card asignado, y Footer).

**Requisitos obligatorios**:
- Todos arrancan en **Modo Claro por defecto**.
- Deben incluir la función `toggleTheme()` en JavaScript que conmuta la clase `dark-mode` en el `body` (las páginas individuales no llevan botón visible de tema en su cabecera; el botón de conmutar va en el marco exterior del comparador).
- **Cero patrones de relleno IA (good-design obligatorio)**: prohibidos los degradados difuminados, los bloques de 3 tarjetas de beneficios/características y las tríadas de números flotantes (vanity stats). La información va en su contexto natural (catálogo, tabla técnica o texto).
- Escala tipográfica real (3-4 tamaños distintivos) e interlineado 1.5.
- Gráficos vectoriales SVG propios y proporcionados al contenedor.
- Precios o datos numéricos con `font-variant-numeric: tabular-nums`.

## Paso 4. Página para comparar reactiva y fluida

`comparar.html` organiza los seis en `<iframe>` mediante un layout **reactivo fluido con mayor ancho por tarjeta** (`repeat(3, minmax(0, 1fr))` para **3x2 en pantalla completa >1350px**, `@media (max-width: 1350px)` con `repeat(2, minmax(0, 1fr))` para **2x3 a mitad de pantalla**, y 1 columna en móvil), con **fondo cálido** (`#f5f2eb` / `#fbf9f4`) y escala de viewport desktop para visualizar las composiciones completas.

**En la cabecera de cada tarjeta (`.col-header`), incluye un botón redondo con el emoji `🌙` para conmutar el tema del iframe respectivo**.

Debajo de cada iframe, incluye la ficha con nombres de una palabra para facilitar el Mix & Match:
- **Estilo:** `lujo`, `industrial`, `glassmorphism`, etc.
- **Nav:** `mono`, `flotante`, `chasis`, `burbuja`, etc.
- **Hero:** `editorial`, `split`, `medidor`, `vitrina`, etc.
- **Card:** `split`, `specs`, `fila`, `dual`, `bento`, `tabla`, `dock`, etc.
- **Paleta:** color base · color acento (`#hex` · `#hex`).

```html
<div class="ingredientes">
  <div class="ing-row"><span class="ing-key">Estilo:</span><span class="ing-val">producto</span></div>
  <div class="ing-row"><span class="ing-key">Nav:</span><span class="ing-val">flotante</span></div>
  <div class="ing-row"><span class="ing-key">Hero:</span><span class="ing-val">split</span></div>
  <div class="ing-row"><span class="ing-key">Card:</span><span class="ing-val">bento</span></div>
  <div class="ing-row"><span class="ing-key">Paleta:</span><span class="ing-val"><code>#ffffff</code> · <code>#5e6ad2</code></span></div>
</div>
```

## Paso 5. Miralos antes de enseñarlos

Abre `comparar.html` y **mira la captura antes de entregar**. Con `agy-ver`
instalado:

```
agy-ver abrir comparar.html
agy-ver foto los-seis
```

Sin el, vale cualquier via que te deje **ver** la pagina: la herramienta de
navegador de tu CLI, o pedirle al usuario que la abra y te diga que ve. Lo que
no vale es entregar seis prototipos que nadie ha mirado.

Abre la captura y comprueba: (1) que todos se ven en Modo Claro, (2) que **no se parecen**, (3) que el botón redondo conmuta a oscuro correctamente, (4) que la ficha usa nombres de una palabra fáciles de combinar.

## Paso 6. Entrega

Una línea por prototipo con sus nombres simples, y una recomendación con motivo.
