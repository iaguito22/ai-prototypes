#!/usr/bin/env python3
"""
dado.py — Selector de cuatro direcciones completas para prototipos.
Garantiza 4 prototipos visualmente distintos con:
- 12 Familias de Diseño
- 10 Arquetipos de Card de Producto (nombres directos de 1 palabra)
- Soporte dual: MODO CLARO (por defecto) y MODO OSCURO
"""

import random
import sys
import os
import json
import argparse

# El historial vive junto a este script, sea cual sea la ruta de instalacion.
HISTORIAL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".historial.json")

FAMILIAS = [
    {
        "id": "caelestia",
        "nombre": "Caelestia Desktop M3",
        "ref": "https://caelestia.sh",
        "paleta_osc": "#0f0d13 fondo noche · #1d192b superficie · #d0bcff acento lavanda",
        "paleta_cla": "#f6f2f7 fondo claro · #eae4eb superficie · #6750a4 acento morado",
        "tipografia": "Google Sans / Roboto Flex",
        "material": "Vidrio tonal oscuro/claro con tinte lavanda y bordes sutiles",
    },
    {
        "id": "nothing",
        "nombre": "Nothing Glyph & Matrix",
        "ref": "https://nothing.tech",
        "paleta_osc": "#000000 negro puro · #ffffff serigrafía · #d71920 rojo LED",
        "paleta_cla": "#f4f4f4 gris chasis · #111111 tinta negra · #d71920 rojo LED",
        "tipografia": "Space Mono / Archivo",
        "material": "Policarbonato transparente, divisores dashed y matriz de puntos",
    },
    {
        "id": "liquid-glass",
        "nombre": "Apple Liquid Glass",
        "ref": "https://apple.com",
        "paleta_osc": "#000000 negro plano · #ffffff texto · #2997ff azul Apple",
        "paleta_cla": "#f5f5f7 gris Apple · #1d1d1f texto · #0071e3 azul Apple",
        "tipografia": "SF Pro / Inter",
        "material": "Óptica neutra transparente con bisel superior iluminado",
    },
    {
        "id": "neumorphism",
        "nombre": "Neumorphism Táctil Soft UI",
        "ref": "https://dribbble.com/tags/neumorphism",
        "paleta_osc": "#1e2127 arcilla grafito · #4f70ff acento índigo",
        "paleta_cla": "#e0e5ec gris cemento suave · #3d5af1 acento índigo",
        "tipografia": "Be Vietnam Pro / Plus Jakarta Sans",
        "material": "Relieves extruidos y cavidades continuas con sombras gemelas",
    },
    {
        "id": "glassmorphism",
        "nombre": "Glassmorphism Puro (Frosted Glass)",
        "ref": "https://ui.aceternity.com",
        "paleta_osc": "#0f1422 fondo plano noche · rgba(255,255,255,0.06) cristal · #818cf8 acento",
        "paleta_cla": "#e0e7ff fondo índigo plano · rgba(255,255,255,0.55) cristal · #4338ca acento",
        "tipografia": "Space Grotesk / Montserrat",
        "material": "Cristal escarchado blur(24px) sobre fondo plano contrastado",
    },
    {
        "id": "industrial",
        "nombre": "Hardware Teenage Engineering",
        "ref": "https://teenage.engineering",
        "paleta_osc": "#1a1a1a aluminio negro · #e6e4df texto · #ff5500 pulsador naranja",
        "paleta_cla": "#e6e4df aluminio anodizado · #1c1c1c serigrafía · #ff5500 pulsador naranja",
        "tipografia": "Space Mono · DM Sans",
        "material": "Aluminio mate mecanizado, cotas técnicas y tornillería de 1px",
    },
    {
        "id": "claymorphism",
        "nombre": "Claymorphism 3D Inflado",
        "ref": "https://dribbble.com/tags/claymorphism",
        "paleta_osc": "#15161e base noche · #202330 arcilla · #a78bfa acento",
        "paleta_cla": "#eef2f9 base nube · #ffffff masa · #6c5ce7 lila inflado",
        "tipografia": "Outfit / Poppins",
        "material": "Cojines inflados 3D con radio 28px y botones bombilla convexos",
    },
    {
        "id": "producto",
        "nombre": "Bento Sólido (Linear / Raycast)",
        "ref": "https://linear.app",
        "paleta_osc": "#000000 negro plano · #141414 tarjeta · #5e6ad2 acento",
        "paleta_cla": "#ffffff blanco plano · #f7f7f8 tarjeta · #5e6ad2 acento",
        "tipografia": "Plus Jakarta Sans / Geist",
        "material": "Superficies sólidas mate sin transparencias, bordes milimétricos al 8%",
    },
    {
        "id": "suizo",
        "nombre": "Estilo Tipográfico Internacional (Suizo)",
        "ref": "https://www.swissted.com",
        "paleta_osc": "#121212 asfalto · #f4f4f0 blanco · #ff3b30 rojo suizo",
        "paleta_cla": "#f4f4f0 papel blanco · #121212 tinta negra · #ff3b30 rojo suizo",
        "tipografia": "Helvetica Neue / Neue Haas Grotesk",
        "material": "Retícula matemática estricta, titulares a escala masiva y líneas gruesas",
    },
    {
        "id": "editorial",
        "nombre": "Revista Domus / El Croquis",
        "ref": "https://readsomethingwonderful.com",
        "paleta_osc": "#1a1918 papel oscuro · #f4f4f2 texto · #c2452d rojo óxido",
        "paleta_cla": "#f4f4f2 base papel marfil · #111111 tinta · #c2452d rojo óxido",
        "tipografia": "Newsreader (serif editorial) + Space Grotesk",
        "material": "Filetes tipográficos de 1px, pies de figura numerados (FIG. 01)",
    },
    {
        "id": "lujo",
        "nombre": "Casa de Subastas (Haute Horlogerie)",
        "ref": "https://www.phillips.com",
        "paleta_osc": "#0a0a0a fondo obsidiana · #f0ede6 texto · #8c7853 latón dorado",
        "paleta_cla": "#faf9f6 fondo marfil · #101010 texto · #8c7853 latón dorado",
        "tipografia": "Bodoni Moda (didona alto contraste) + Montserrat fina",
        "material": "Filetes de latón dorado de 1px, numeración romana y amplios márgenes",
    },
    {
        "id": "organico",
        "nombre": "Wabi-Sabi Orgánico Japandi",
        "ref": "https://kinfolk.com",
        "paleta_osc": "#1a1815 piedra oscura · #e6dfd5 arcilla · #8a9a86 matcha",
        "paleta_cla": "#f7f4ee papel arroz · #2b2621 tinta carbón · #5a6e56 matcha",
        "tipografia": "Cormorant Garamond + Satoshi",
        "material": "Bordes asimétricos suaves, tonos tierra cálidos y texturas cerámicas",
    }
]

CARDS = [
    {"id": "bento", "nombre": "Bento Card", "desc": "Tarjeta vertical limpia con chip de categoría/ración arriba y botón directo"},
    {"id": "fila", "nombre": "Fila con Stepper", "desc": "Fila horizontal continua con miniatura a la izquierda y selector [- 1 +] a la derecha"},
    {"id": "dual", "nombre": "Pestañas Dual-Tier", "desc": "Tarjeta con conmutador interno [Estándar | Trufa] que cambia variantes en vivo"},
    {"id": "specs", "nombre": "Telemetría Industrial", "desc": "Ficha de hardware con tabla mono de datos/cotas y pulsador mecánico [PUSH]"},
    {"id": "split", "nombre": "Split-View Editorial", "desc": "División 50/50 con render enmarcado a la izquierda y bloque de texto y botón a la derecha"},
    {"id": "showcase", "nombre": "Showcase Vitrina", "desc": "Vitrina centrada en el objeto con badge flotante arriba y botón de ancho completo"},
    {"id": "tabla", "nombre": "Matriz Tabular B2B", "desc": "Fila ultradensa de inventario con miniatura reducida, código SKU y chip de stock"},
    {"id": "dock", "nombre": "Pill Flotante Dock", "desc": "Cápsula redondeada flotante tipo píldora de interacción rápida"},
    {"id": "acordeon", "nombre": "Ficha Acordeón", "desc": "Tarjeta compacta con desplegable de detalles técnicos/alérgenos al pulsar"},
    {"id": "documental", "nombre": "Ficha Documental", "desc": "Estructura editorial con numeración FIG. 01, marco técnico y pie documental"}
]

NAVS = [
    {"id": "centrada", "nombre": "Navegación Centrada", "desc": "Enlaces 100% centrados en la página sin nombre de marca"},
    {"id": "anonima", "nombre": "Cápsula Anónima", "desc": "Píldora suspendida con selectores de categoría/filtro, sin logotipo ni texto de marca"},
    {"id": "split", "nombre": "Split Extremos", "desc": "Logotipo a la izquierda y enlaces/CTA a la derecha en los extremos del contenedor"},
    {"id": "mono", "nombre": "Telemetría Mono", "desc": "Cabecera técnica en monospace continuo con marca, versión y enlaces en línea"},
    {"id": "isla", "nombre": "Isla Flotante", "desc": "Píldora flotante compacta de vidrio suspendida con logo minimalista y enlaces"},
    {"id": "apilada", "nombre": "Doble Fila Apilada", "desc": "Logotipo centrado en la fila superior y barra de enlaces centrada en la fila inferior"},
    {"id": "chasis", "nombre": "Chasis Mecanizado", "desc": "Panel de ingeniería con tornillería en esquinas y selector de canal [01] [02]"},
    {"id": "minimal", "nombre": "Minimal Directa", "desc": "Solo logotipo tipográfico a la izquierda y un botón de acción directo a la derecha"},
    {"id": "subastas", "nombre": "Simétrica de Subastas", "desc": "Logotipo monumental al centro dividido por dos enlaces a cada lado entre filetes"},
    {"id": "burbuja", "nombre": "Burbuja Táctil 3D", "desc": "Cápsula inflada redondeada con volumen suave y dot de estado activo"}
]

HEROS = [
    {"id": "foto-split", "nombre": "Split con Fotografía", "desc": "Pantalla dividida con fotografía de alta resolución de producto/taller a un lado y texto al otro"},
    {"id": "foto-hero", "nombre": "Fotografía Monumental", "desc": "Fotografía inmersiva a sangre con tratamiento de luz y titular tipográfico integrado"},
    {"id": "centrado", "nombre": "Centrado Minimal", "desc": "Titular masivo y lead 100% centrados en columna única sin cajas laterales"},
    {"id": "split", "nombre": "Split Gráfico 50/50", "desc": "Pantalla dividida con render técnico a la izquierda y texto a la derecha"},
    {"id": "medidor", "nombre": "Telemetría & Medidor", "desc": "Consola técnica con barras de nivel, osciloscopio o cotas acústicas"},
    {"id": "vitrina", "nombre": "Vitrina Pedestal", "desc": "Composición vertical centrada con el objeto sobre pedestal e insignia flotante"},
    {"id": "editorial", "nombre": "Revista Doble Columna", "desc": "Titular con filete vertical y dos columnas de texto tipo publicación de diseño"},
    {"id": "masivo", "nombre": "Tipografía Monumental", "desc": "Titular tipográfico a escala gigante que ocupa el ancho completo"},
    {"id": "manifiesto", "nombre": "Manifiesto de Autor", "desc": "Cita textual del luthier/artesano en tipografía cursiva destacada con firma"},
    {"id": "burbuja", "nombre": "Cojín Inflado 3D", "desc": "Volumen táctil suave con cápsula de relieve y badge convexo"},
    {"id": "optica", "nombre": "Óptica Translúcida", "desc": "Panel de cristal con bisel iluminado y diagrama de ondas de fase"},
    {"id": "m3", "nombre": "Capas Tonales M3", "desc": "Composición asimétrica por niveles tonales superpuestos"}
]

def cargar_historial():
    if os.path.exists(HISTORIAL_PATH):
        try:
            with open(HISTORIAL_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def guardar_historial(ids):
    os.makedirs(os.path.dirname(HISTORIAL_PATH), exist_ok=True)
    historial = cargar_historial()
    historial.extend(ids)
    historial = historial[-16:]
    with open(HISTORIAL_PATH, "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Tira el dado para 6 prototipos de diseño.")
    parser.add_argument("--semilla", type=str, help="Semilla para reproducir una tirada")
    parser.add_argument("--evitar", type=str, help="Familias a evitar separadas por coma")
    parser.add_argument("--solo", type=str, help="Forzar una familia específica")
    parser.add_argument("--repetir", action="store_true", help="Ignorar el historial de tiradas recientes")
    args = parser.parse_args()

    if args.semilla:
        random.seed(args.semilla)

    evitar = [x.strip() for x in args.evitar.split(",")] if args.evitar else []
    historial = [] if args.repetir else cargar_historial()

    candidatas = [f for f in FAMILIAS if f["id"] not in evitar and f["id"] not in historial]
    if len(candidatas) < 6:
        candidatas = [f for f in FAMILIAS if f["id"] not in evitar]

    if args.solo:
        elegidas = [f for f in FAMILIAS if f["id"] == args.solo]
        resto = [f for f in candidatas if f["id"] != args.solo]
        elegidas.extend(random.sample(resto, 5))
    else:
        elegidas = random.sample(candidatas, 6)

    cards_elegidas = random.sample(CARDS, 6)
    navs_elegidas = random.sample(NAVS, 6)
    heros_elegidos = random.sample(HEROS, 6)

    guardar_historial([f["id"] for f in elegidas])

    print("Seis direcciones con familias de diseño, arquetipos de Card, Nav y Hero distintos.")
    print("Cada una arranca en MODO CLARO por defecto e incluye botón para alternar a MODO OSCURO.\n")

    for i, (f, c, n, h) in enumerate(zip(elegidas, cards_elegidas, navs_elegidas, heros_elegidos), 1):
        print("=" * 74)
        print(f"PROTOTIPO {i} — {f['nombre']}   [estilo: {f['id']}]")
        print(f"NAV:         {n['id']} — {n['desc']}")
        print(f"HERO:        {h['id']} — {h['desc']}")
        print(f"CARD:        {c['id']} — {c['desc']}")
        print(f"PALETA CLA:  {f['paleta_cla']}")
        print(f"PALETA OSC:  {f['paleta_osc']}")
        print(f"MATERIAL:    {f['material']}")
        print()

if __name__ == "__main__":
    main()
