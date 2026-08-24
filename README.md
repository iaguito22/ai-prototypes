# prototipos

Cuatro prototipos visuales de una misma página que **de verdad no se parecen entre sí**.

El problema que resuelve: si le pides a un modelo "tres opciones de diseño", te
devuelve tres veces la mediana de su entrenamiento (una clara y minimalista, una
oscura de lujo, una de papel). Aquí la dirección estética **no la elige el modelo**:
la tira un dado, `dado.py`, con un catálogo de 12 familias (caelestia, nothing,
liquid-glass, neumorphism, glassmorphism, industrial, claymorphism, producto, suizo,
editorial, lujo, orgánico) cruzadas con 10 arquetipos de tarjeta.

El dado recuerda las últimas tiradas y no las repite, así que no te sale siempre lo
mismo. La skill obliga después a montar una página que compare los cuatro a la vez
y a mirarla antes de entregar.

## Instalar

**Antigravity CLI**

    git clone https://github.com/iaguito22/prototipos ~/.gemini/config/skills/prototipos

**Claude Code**

    git clone https://github.com/iaguito22/prototipos ~/.claude/skills/prototipos

Necesita `python3` para el dado. Nada más.

## Usar

    /prototipos necesito una web para un bufet de sushi donde se pida por mesa

Se activa también sola cuando pides "varias versiones", "opciones de diseño" o
arrancas un diseño sin dirección estética decidida.

Banderas del dado (las usa el modelo, pero puedes lanzarlo a mano):

    python3 dado.py --semilla <texto>   repite exactamente la misma tirada
    python3 dado.py --evitar lujo       descarta una familia entera
    python3 dado.py --solo suizo        fuerza una y sortea las otras tres
    python3 dado.py --repetir           ignora la memoria de tiradas recientes

## Ver el resultado

El último paso pide **mirar** la comparativa antes de entregarla. Si tienes
[`agy-ver`](https://github.com/iaguito22/porton-verificacion) vale `agy-ver abrir
comparar.html`; si no, sirve cualquier forma de ver la página de verdad.

## Licencia

MIT.
