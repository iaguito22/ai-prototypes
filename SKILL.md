---
name: prototipos
description: >-
  Cuatro prototipos visuales de verdad distintos de una misma pagina, adaptados al
  encargo para comparar y elegir. Usala cuando el usuario diga "/prototipos",
  "hazme varias versiones", "dame opciones de diseño", "no se como quiero que se vea",
  o cuando arranque un diseño desde cero sin direccion estetica decidida.
---

# Cuatro prototipos que no se parecen

El fallo de siempre: te piden varias opciones y salen versiones de la misma cosa
(una clara y minimalista, una oscura de lujo, una de papel). Es la mediana del
entrenamiento. Aqui **la direccion no la eliges tu**.

## Paso 1. Tira el dado. Obligatorio.

```
python3 ~/.gemini/config/skills/prototipos/dado.py   # Antigravity CLI
python3 ~/.claude/skills/prototipos/dado.py          # Claude Code
```

`dado.py` vive junto a este `SKILL.md`: si la skill esta en otra ruta, la del
dado es esa misma. No lo tires "de memoria": sin ejecutarlo no hay tirada.

Te devuelve **cuatro direcciones completas** que rotan ortogonalmente entre las 12 familias de diseño del catálogo y sus arquetipos de tarjeta (`Card`), con soporte para **MODO CLARO** (por defecto) y **MODO OSCURO**.

- El dado **recuerda las ultimas 8 direcciones y no las repite**, para garantizar frescura. `--repetir` desactiva esa memoria si te da igual.
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

## Paso 2. Fija lo que NO cambia

**Los cuatro prototipos llevan exactamente el mismo contenido (mismos productos/platos) y la misma estructura limpia simétrica.**

## Paso 3. Construye los cuatro en Modo Claro por defecto

Un archivo por prototipo: `p1.html`, `p2.html`, `p3.html`, `p4.html`, cada uno autónomo.

**Requisitos obligatorios**:
- Todos arrancan en **Modo Claro por defecto**.
- Deben incluir la función `toggleTheme()` en JavaScript que conmuta la clase `dark-mode` en el `body`.
- **Cero degradados "AI slop"**: fondos sólidos limpios y contrastados (en glassmorphism, el vidrio se apoya sobre el color de fondo plano).
- Escala tipográfica real (3-4 tamaños distintivos) e interlineado 1.5.
- Gráficos vectoriales SVG propios y proporcionados al contenedor.
- Precios o datos numéricos con `font-variant-numeric: tabular-nums`.

## Paso 4. Página para comparar con desglose Mix & Match

Los cuatro en `<iframe>` organizados en cuadrícula de 2x2. **En la cabecera de cada tarjeta (`.col-header`), incluye un botón redondo con el emoji `🌙` para conmutar el tema**.

Debajo de cada iframe, incluye la ficha con nombres de una palabra:
- **Estilo:** `lujo`, `industrial`, `glassmorphism`, etc.
- **Card:** `split`, `specs`, `fila`, `dual`, `bento`, etc.
- **Paleta:** color base · color acento (`#hex` · `#hex`).

```html
<div class="ingredientes">
  <div class="ing-row"><span class="ing-key">Estilo:</span><span class="ing-val">producto</span></div>
  <div class="ing-row"><span class="ing-key">Card:</span><span class="ing-val">bento</span></div>
  <div class="ing-row"><span class="ing-key">Paleta:</span><span class="ing-val">blanco · morado (<code>#ffffff</code> · <code>#5e6ad2</code>)</span></div>
</div>
```

## Paso 5. Miralos antes de enseñarlos

Abre `comparar.html` y **mira la captura antes de entregar**. Con `agy-ver`
instalado:

```
agy-ver abrir comparar.html
agy-ver foto los-cuatro
```

Sin el, vale cualquier via que te deje **ver** la pagina: la herramienta de
navegador de tu CLI, o pedirle al usuario que la abra y te diga que ve. Lo que
no vale es entregar cuatro prototipos que nadie ha mirado.

Abre la captura y comprueba: (1) que todos se ven en Modo Claro, (2) que **no se parecen**, (3) que el botón redondo conmuta a oscuro correctamente, (4) que la ficha usa nombres de una palabra fáciles de combinar.

## Paso 6. Entrega

Una línea por prototipo con sus nombres simples, y una recomendación con motivo.
