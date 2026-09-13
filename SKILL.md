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
entrenamiento. Aquí **la dirección no la eliges tú**.

## Paso 1. Tira el dado. Obligatorio.

Debes ejecutar el script de Python `dado.py` que se encuentra en la carpeta de esta skill para obtener las semillas creativas:

```sh
# Busca y ejecuta el dado
SCRIPT_PATH=$(find ~/.gemini/config/skills/ -name "dado.py" -type f | head -n 1)
python3 "$SCRIPT_PATH" "<prompt o palabras clave del encargo>"
```

Te devuelve **seis direcciones completas** estructuradas en **3 franjas ortogonales**:
1. **Comercial / Alta Conversión (2 prototipos)**: estándares de alta conversión y claridad directa para el sector.
2. **Técnico / Rigor Funcional (2 prototipos)**: enfoque en datos, tablas, telemetría y especificaciones de ingeniería.
3. **Vanguardia / Emoción Visual (2 prototipos)**: exploraciones audaces de impacto visual y diferenciación estética.

- **Autodetección inteligente**: pasa la descripción del encargo entre comillas y el dado clasificará automáticamente entre los 12 arquetipos de negocio.
- `--objetivo <id>` para forzar un arquetipo específico.
- `--aleatorio` para desactivar la ponderación sectorial y usar azar uniforme puro.
