#!/usr/bin/env python3
"""
dado.py — Selector inteligente de 6 direcciones ortogonales para prototipos.
Optimizado con matriz de arquetipos de negocio (Intents) y selección en 3 franjas:
1. Comercial (2 prototipos de alta conversión)
2. Técnico (2 prototipos de rigor funcional/datos)
3. Vanguardia (2 prototipos de impacto visual/emoción)
"""

import random
import sys
import os
import json
import argparse
import unicodedata

HISTORIAL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".historial.json")

# ==============================================================================
# 1. CATÁLOGO COMPLETO DE ELEMENTOS (GLOSARIO DE 1 PALABRA)
# ==============================================================================

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

# Mapas de acceso rápido por ID
FAMILIAS_MAP = {f["id"]: f for f in FAMILIAS}
CARDS_MAP = {c["id"]: c for c in CARDS}
NAVS_MAP = {n["id"]: n for n in NAVS}
HEROS_MAP = {h["id"]: h for h in HEROS}

# ==============================================================================
# 2. CATÁLOGO EXTENSO DE ARQUETIPOS DE ENCARGO / INTENTS
# ==============================================================================

OBJETIVOS = {
    "hardware_tech": {
        "nombre": "Hardware & Electrónica de Consumo",
        "desc": "Móviles, auriculares, relojes, ordenadores, audio Hi-Fi, periféricos, robótica, gadgets, IoT",
        "keywords": [
            "movil", "moviles", "smartphone", "telefono", "telefonos", "auricular", "auriculares",
            "reloj", "relojes", "smartwatch", "hardware", "gadget", "gadgets", "tech", "tecnologia",
            "audio", "hifi", "altavoz", "altavoces", "sonido", "pc", "ordenador", "teclado", "mouse",
            "chip", "procesador", "componentes", "robot", "robotica", "drone", "camara", "pantalla"
        ],
        "comercial": {
            "estilos": ["liquid-glass", "producto", "glassmorphism"],
            "heros": ["foto-split", "foto-hero", "m3"],
            "cards": ["bento", "dock", "dual"],
            "navs": ["anonima", "minimal", "burbuja", "split"]
        },
        "tecnico": {
            "estilos": ["nothing", "industrial", "suizo"],
            "heros": ["medidor", "optica", "masivo"],
            "cards": ["specs", "tabla", "fila"],
            "navs": ["chasis", "mono", "split"]
        },
        "vanguardia": {
            "estilos": ["caelestia", "claymorphism", "neumorphism"],
            "heros": ["vitrina", "burbuja", "split"],
            "cards": ["split", "showcase", "acordeon"],
            "navs": ["isla", "centrada", "burbuja"]
        }
    },

    "lujo_artesania": {
        "nombre": "Lujo, Alta Artesanía & Haute Horlogerie",
        "desc": "Joyería fina, relojería artesanal, luthería, marroquinería, perfumería nicho, alta costura, objetos de colección",
        "keywords": [
            "lujo", "joya", "joyas", "joyeria", "oro", "diamante", "relojeria", "artesania", "artesanal",
            "luthier", "lutheria", "madera noble", "cuero", "perfume", "perfumeria", "atelier",
            "haute", "reloj mecanico", "subasta", "alta costura", "sastre", "orfebreria", "cristal",
            "porcelana", "vino de autor", "reliquia", "coleccionista"
        ],
        "comercial": {
            "estilos": ["lujo", "organico", "editorial"],
            "heros": ["manifiesto", "foto-hero", "centrado"],
            "cards": ["showcase", "bento", "split"],
            "navs": ["subastas", "apilada", "centrada"]
        },
        "tecnico": {
            "estilos": ["suizo", "editorial", "industrial"],
            "heros": ["editorial", "foto-split", "masivo"],
            "cards": ["documental", "tabla", "specs"],
            "navs": ["mono", "split", "apilada"]
        },
        "vanguardia": {
            "estilos": ["liquid-glass", "caelestia", "organico"],
            "heros": ["vitrina", "optica", "centrado"],
            "cards": ["bento", "showcase", "dual"],
            "navs": ["isla", "anonima", "subastas"]
        }
    },

    "saas_b2b": {
        "nombre": "SaaS, Developer Tools & Plataformas B2B",
        "desc": "Software cloud, APIs, herramientas de programación, analítica, dashboards, ciberseguridad, productividad",
        "keywords": [
            "saas", "software", "app", "b2b", "developer", "dev", "api", "dashboard", "analytics",
            "cloud", "seguridad", "ciberseguridad", "productividad", "crm", "erp", "gestion", "workflow",
            "plataforma", "infraestructura", "servidores", "database", "devops", "ia", "ai", "agente"
        ],
        "comercial": {
            "estilos": ["producto", "liquid-glass", "glassmorphism"],
            "heros": ["m3", "editorial", "split"],
            "cards": ["dock", "bento", "dual"],
            "navs": ["minimal", "split", "anonima"]
        },
        "tecnico": {
            "estilos": ["nothing", "suizo", "industrial"],
            "heros": ["medidor", "masivo", "optica"],
            "cards": ["specs", "tabla", "fila"],
            "navs": ["mono", "chasis", "split"]
        },
        "vanguardia": {
            "estilos": ["caelestia", "claymorphism", "neumorphism"],
            "heros": ["burbuja", "vitrina", "foto-split"],
            "cards": ["split", "acordeon", "documental"],
            "navs": ["isla", "burbuja", "centrada"]
        }
    },

    "gastro_restauracion": {
        "nombre": "Gastronomía, Restauración & Bebidas de Autor",
        "desc": "Restaurantes de autor, cafeterías de especialidad, bistrós, bodegas, pastelería artesanal, coctelerías",
        "keywords": [
            "restaurante", "carta", "menu", "plato", "platos", "comida", "gastro", "gastronomia", "chef",
            "cocina", "cafe", "cafeteria", "bistro", "vino", "bodega", "cerveza", "coctel", "cocteleria",
            "panaderia", "pasteleria", "dulce", "tapa", "tapas", "maridaje", "degustacion", "brunch"
        ],
        "comercial": {
            "estilos": ["organico", "editorial", "lujo"],
            "heros": ["foto-hero", "centrado", "manifiesto"],
            "cards": ["fila", "bento", "showcase"],
            "navs": ["centrada", "subastas", "split"]
        },
        "tecnico": {
            "estilos": ["suizo", "editorial", "producto"],
            "heros": ["editorial", "foto-split", "masivo"],
            "cards": ["documental", "tabla", "dual"],
            "navs": ["apilada", "split", "minimal"]
        },
        "vanguardia": {
            "estilos": ["claymorphism", "caelestia", "liquid-glass"],
            "heros": ["burbuja", "vitrina", "optica"],
            "cards": ["dock", "acordeon", "split"],
            "navs": ["burbuja", "isla", "anonima"]
        }
    },

    "portfolio_creativo": {
        "nombre": "Estudios Creativos, Arquitectura & Fotografía",
        "desc": "Portfolios de arquitectura, estudios de diseño gráfico/industrial, fotografía de autor, directores de arte, cine",
        "keywords": [
            "portfolio", "estudio", "arquitectura", "arquitecto", "fotografia", "fotografo", "diseño",
            "diseñador", "arte", "artista", "galeria", "exposicion", "cine", "audiovisual", "editorial",
            "director de arte", "motion", "branding", "interiorismo", "render", "3d", "escultura"
        ],
        "comercial": {
            "estilos": ["editorial", "suizo", "organico"],
            "heros": ["foto-hero", "editorial", "centrado"],
            "cards": ["documental", "showcase", "bento"],
            "navs": ["split", "centrada", "minimal"]
        },
        "tecnico": {
            "estilos": ["nothing", "industrial", "suizo"],
            "heros": ["masivo", "foto-split", "medidor"],
            "cards": ["specs", "documental", "tabla"],
            "navs": ["mono", "chasis", "split"]
        },
        "vanguardia": {
            "estilos": ["caelestia", "liquid-glass", "lujo"],
            "heros": ["manifiesto", "vitrina", "optica"],
            "cards": ["split", "dock", "dual"],
            "navs": ["isla", "anonima", "apilada"]
        }
    },

    "salud_wellness": {
        "nombre": "Salud, Bienestar & Clínicas Especializadas",
        "desc": "Clínicas dentales/médicas, cosmética clínica, spas, suplementación avanzada, biotecnología médica, fitness",
        "keywords": [
            "salud", "clinica", "medico", "medica", "dental", "dentista", "wellness", "spa", "bienestar",
            "cosmetica", "dermatologia", "skincare", "suplemento", "suplementos", "nutricion", "fitness",
            "psicologia", "terapia", "fisioterapia", "hospital", "biomedicina", "longevidad"
        ],
        "comercial": {
            "estilos": ["liquid-glass", "producto", "organico"],
            "heros": ["foto-split", "centrado", "foto-hero"],
            "cards": ["bento", "dual", "dock"],
            "navs": ["minimal", "anonima", "split"]
        },
        "tecnico": {
            "estilos": ["suizo", "nothing", "industrial"],
            "heros": ["optica", "medidor", "editorial"],
            "cards": ["specs", "tabla", "acordeon"],
            "navs": ["mono", "split", "chasis"]
        },
        "vanguardia": {
            "estilos": ["caelestia", "glassmorphism", "claymorphism"],
            "heros": ["vitrina", "burbuja", "m3"],
            "cards": ["showcase", "split", "fila"],
            "navs": ["isla", "burbuja", "centrada"]
        }
    },

    "fintech_crypto": {
        "nombre": "Fintech, Inversión & Finanzas Digitales",
        "desc": "Neobancos, plataformas de inversión, pasarelas de pago, cripto/DeFi, gestión patrimonial, auditoría",
        "keywords": [
            "fintech", "finanzas", "banco", "neobanco", "inversion", "trading", "crypto", "cripto", "bitcoin",
            "ethereum", "defi", "patrimonio", "fondos", "pago", "pagos", "tarjeta", "broker", "bolsa",
            "auditoria", "fiscal", "prestamo", "wallet"
        ],
        "comercial": {
            "estilos": ["producto", "liquid-glass", "glassmorphism"],
            "heros": ["m3", "editorial", "split"],
            "cards": ["dock", "bento", "dual"],
            "navs": ["minimal", "split", "anonima"]
        },
        "tecnico": {
            "estilos": ["nothing", "suizo", "industrial"],
            "heros": ["medidor", "masivo", "optica"],
            "cards": ["tabla", "specs", "fila"],
            "navs": ["mono", "chasis", "split"]
        },
        "vanguardia": {
            "estilos": ["caelestia", "lujo", "neumorphism"],
            "heros": ["vitrina", "manifiesto", "foto-split"],
            "cards": ["split", "documental", "showcase"],
            "navs": ["isla", "subastas", "centrada"]
        }
    },

    "moda_streetwear": {
        "nombre": "Moda, Streetwear & Apparel Técnico",
        "desc": "Marcas de ropa, streetwear, calzado técnico, sastrería contemporánea, colecciones cápsula, accesorios",
        "keywords": [
            "moda", "ropa", "streetwear", "sneakers", "zapatillas", "calzado", "apparel", "sastrería",
            "textil", "abrigo", "chaqueta", "camiseta", "hoodie", "tienda ropa", "coleccion capsula",
            "prendas", "outdoor", "goretex", "tendencia"
        ],
        "comercial": {
            "estilos": ["editorial", "suizo", "producto"],
            "heros": ["foto-hero", "foto-split", "masivo"],
            "cards": ["bento", "fila", "showcase"],
            "navs": ["split", "minimal", "centrada"]
        },
        "tecnico": {
            "estilos": ["nothing", "industrial", "suizo"],
            "heros": ["medidor", "masivo", "editorial"],
            "cards": ["specs", "documental", "tabla"],
            "navs": ["chasis", "mono", "split"]
        },
        "vanguardia": {
            "estilos": ["claymorphism", "lujo", "caelestia"],
            "heros": ["manifiesto", "burbuja", "vitrina"],
            "cards": ["dock", "split", "dual"],
            "navs": ["burbuja", "subastas", "isla"]
        }
    },

    "inmobiliaria_espacios": {
        "nombre": "Inmobiliaria de Lujo & Espacios Exclusivos",
        "desc": "Promociones residenciales de lujo, villas, espacios de coworking premium, hoteles boutique, interiorismo",
        "keywords": [
            "inmobiliaria", "vivienda", "viviendas", "casa", "casas", "piso", "pisos", "villa", "villas",
            "mansion", "atico", "edificio", "promocion", "coworking", "hotel", "hotel boutique",
            "residencia", "inmueble", "finca", "terreno", "propiedad"
        ],
        "comercial": {
            "estilos": ["lujo", "organico", "editorial"],
            "heros": ["foto-hero", "manifiesto", "centrado"],
            "cards": ["showcase", "bento", "split"],
            "navs": ["subastas", "apilada", "centrada"]
        },
        "tecnico": {
            "estilos": ["suizo", "editorial", "producto"],
            "heros": ["editorial", "foto-split", "masivo"],
            "cards": ["documental", "tabla", "specs"],
            "navs": ["mono", "split", "minimal"]
        },
        "vanguardia": {
            "estilos": ["caelestia", "liquid-glass", "organico"],
            "heros": ["vitrina", "optica", "burbuja"],
            "cards": ["dock", "dual", "acordeon"],
            "navs": ["isla", "anonima", "burbuja"]
        }
    },

    "automocion_movilidad": {
        "nombre": "Automoción, Movilidad Eléctrica & Motorsport",
        "desc": "Coches eléctricos, hiperdeportivos, motocicletas de autor, bicicletas técnicas, náutica, aviación privada",
        "keywords": [
            "coche", "coches", "auto", "autos", "automocion", "motor", "electrico", "ev", "moto", "motos",
            "motocicleta", "bici", "bicicleta", "movilidad", "nautica", "barco", "yate", "avion", "aero",
            "hiperdeportivo", "supercar", "vehiculo"
        ],
        "comercial": {
            "estilos": ["liquid-glass", "producto", "lujo"],
            "heros": ["foto-hero", "foto-split", "m3"],
            "cards": ["bento", "showcase", "dual"],
            "navs": ["split", "minimal", "subastas"]
        },
        "tecnico": {
            "estilos": ["industrial", "nothing", "suizo"],
            "heros": ["medidor", "masivo", "optica"],
            "cards": ["specs", "tabla", "fila"],
            "navs": ["chasis", "mono", "split"]
        },
        "vanguardia": {
            "estilos": ["caelestia", "glassmorphism", "claymorphism"],
            "heros": ["vitrina", "burbuja", "split"],
            "cards": ["dock", "split", "documental"],
            "navs": ["isla", "anonima", "burbuja"]
        }
    },

    "educacion_cultura": {
        "nombre": "Educación, Cultura & Editoriales",
        "desc": "Academias de programación, escuelas de negocios, museos, fundaciones culturales, editoriales, congresos",
        "keywords": [
            "educacion", "curso", "cursos", "academia", "escuela", "universidad", "master", "bootcamp",
            "cultura", "museo", "fundacion", "libro", "libros", "editorial", "conferencia", "evento",
            "investigacion", "ciencia", "historia", "divulgacion"
        ],
        "comercial": {
            "estilos": ["editorial", "suizo", "producto"],
            "heros": ["editorial", "centrado", "foto-split"],
            "cards": ["bento", "documental", "fila"],
            "navs": ["split", "centrada", "minimal"]
        },
        "tecnico": {
            "estilos": ["suizo", "nothing", "editorial"],
            "heros": ["masivo", "medidor", "foto-hero"],
            "cards": ["tabla", "specs", "acordeon"],
            "navs": ["mono", "apilada", "chasis"]
        },
        "vanguardia": {
            "estilos": ["caelestia", "organico", "lujo"],
            "heros": ["manifiesto", "vitrina", "burbuja"],
            "cards": ["dock", "split", "showcase"],
            "navs": ["isla", "subastas", "anonima"]
        }
    },

    "general_ecommerce": {
        "nombre": "E-Commerce & Retail Directo al Consumidor",
        "desc": "Tiendas online multimarca, retail directo D2C, productos de consumo, hogar, regalos, belleza general",
        "keywords": [
            "tienda", "tiendas", "ecommerce", "e-commerce", "comprar", "venta", "retail", "shop",
            "carrito", "producto", "productos", "catalogo", "ofertas", "descuentos", "hogar", "regalo", "regalos"
        ],
        "comercial": {
            "estilos": ["producto", "liquid-glass", "editorial"],
            "heros": ["foto-hero", "foto-split", "centrado"],
            "cards": ["bento", "fila", "dock"],
            "navs": ["split", "minimal", "anonima"]
        },
        "tecnico": {
            "estilos": ["suizo", "nothing", "industrial"],
            "heros": ["optica", "medidor", "masivo"],
            "cards": ["tabla", "specs", "dual"],
            "navs": ["mono", "chasis", "split"]
        },
        "vanguardia": {
            "estilos": ["organico", "claymorphism", "caelestia"],
            "heros": ["burbuja", "vitrina", "manifiesto"],
            "cards": ["showcase", "split", "acordeon"],
            "navs": ["burbuja", "isla", "subastas"]
        }
    }
}

# ==============================================================================
# 3. FUNCIONES DE NORMALIZACIÓN Y DETECCIÓN SEMÁNTICA
# ==============================================================================

def normalizar_texto(texto):
    if not texto:
        return ""
    texto = texto.lower()
    # Eliminar tildes y diacríticos
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def detectar_objetivo(prompt):
    if not prompt:
        return "general_ecommerce", 0
    
    prompt_norm = normalizar_texto(prompt)
    palabras = set(prompt_norm.replace("/", " ").replace(",", " ").replace(".", " ").replace("-", " ").split())
    
    puntuaciones = {}
    for obj_id, obj_data in OBJETIVOS.items():
        score = 0
        for kw in obj_data["keywords"]:
            kw_norm = normalizar_texto(kw)
            if " " in kw_norm:
                if kw_norm in prompt_norm:
                    score += 3
            elif kw_norm in palabras:
                score += 2
            elif len(kw_norm) > 4 and kw_norm in prompt_norm:
                score += 1
        puntuaciones[obj_id] = score
    
    mejor_obj = max(puntuaciones, key=puntuaciones.get)
    mejor_score = puntuaciones[mejor_obj]
    
    if mejor_score > 0:
        return mejor_obj, mejor_score
    return "general_ecommerce", 0

# ==============================================================================
# 4. GESTIÓN DE HISTORIAL
# ==============================================================================

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

# ==============================================================================
# 5. MOTOR DE SELECCIÓN EN 3 FRANJAS ORTOGONALES
# ==============================================================================

def seleccionar_seis_direcciones(objetivo_id, evitar=None, solo=None, usar_historial=True):
    evitar = evitar or []
    historial = cargar_historial() if usar_historial else []
    
    obj = OBJETIVOS.get(objetivo_id, OBJETIVOS["general_ecommerce"])
    
    # 3 Franjas: 2 Comercial, 2 Técnico, 2 Vanguardia
    franjas = [
        ("comercial", obj["comercial"], "Comercial / Alta Conversión"),
        ("comercial", obj["comercial"], "Comercial / Alta Conversión"),
        ("tecnico", obj["tecnico"], "Técnico / Rigor Funcional"),
        ("tecnico", obj["tecnico"], "Técnico / Rigor Funcional"),
        ("vanguardia", obj["vanguardia"], "Vanguardia / Emoción Visual"),
        ("vanguardia", obj["vanguardia"], "Vanguardia / Emoción Visual")
    ]
    
    # Si se pide forzar una familia con --solo
    estilos_usados = []
    navs_usadas = []
    heros_usados = []
    cards_usadas = []
    
    resultado = []
    
    # Si hay un --solo, colocarlo en la primera posición
    if solo and solo in FAMILIAS_MAP:
        f_solo = FAMILIAS_MAP[solo]
        estilos_usados.append(f_solo["id"])
    
    for idx, (franja_nombre, franja_data, franja_label) in enumerate(franjas):
        # 1. Elegir Estilo
        if idx == 0 and solo and solo in FAMILIAS_MAP:
            f = FAMILIAS_MAP[solo]
        else:
            candidatos_estilo = [
                f_id for f_id in franja_data["estilos"]
                if f_id not in estilos_usados and f_id not in evitar and f_id not in historial
            ]
            if not candidatos_estilo:
                candidatos_estilo = [
                    f_id for f_id in franja_data["estilos"]
                    if f_id not in estilos_usados and f_id not in evitar
                ]
            if not candidatos_estilo:
                # Fallback a todas las familias no usadas
                candidatos_estilo = [f["id"] for f in FAMILIAS if f["id"] not in estilos_usados and f["id"] not in evitar]
            
            f_id = random.choice(candidatos_estilo)
            estilos_usados.append(f_id)
            f = FAMILIAS_MAP[f_id]
        
        # 2. Elegir Hero
        candidatos_hero = [h_id for h_id in franja_data["heros"] if h_id not in heros_usados]
        if not candidatos_hero:
            candidatos_hero = [h["id"] for h in HEROS if h["id"] not in heros_usados]
        h_id = random.choice(candidatos_hero)
        heros_usados.append(h_id)
        h = HEROS_MAP[h_id]
        
        # 3. Elegir Card (Regla de anti-colisión: si hero es foto-split o split, card no debe ser split si es posible)
        candidatos_card = [
            c_id for c_id in franja_data["cards"]
            if c_id not in cards_usadas and not (("split" in h_id) and c_id == "split")
        ]
        if not candidatos_card:
            candidatos_card = [c_id for c_id in franja_data["cards"] if c_id not in cards_usadas]
        if not candidatos_card:
            candidatos_card = [c["id"] for c in CARDS if c["id"] not in cards_usadas]
        c_id = random.choice(candidatos_card)
        cards_usadas.append(c_id)
        c = CARDS_MAP[c_id]
        
        # 4. Elegir Nav
        candidatos_nav = [n_id for n_id in franja_data["navs"] if n_id not in navs_usadas]
        if not candidatos_nav:
            candidatos_nav = [n["id"] for n in NAVS if n["id"] not in navs_usadas]
        n_id = random.choice(candidatos_nav)
        navs_usadas.append(n_id)
        n = NAVS_MAP[n_id]
        
        resultado.append({
            "franja": franja_label,
            "estilo": f,
            "card": c,
            "nav": n,
            "hero": h
        })
    
    guardar_historial(estilos_usados)
    return resultado

# ==============================================================================
# 6. INTERFAZ CLI
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="Tira el dado para 6 prototipos de diseño orientados a objetivo.")
    parser.add_argument("prompt", nargs="*", help="Texto del encargo o palabras clave para autodetección")
    parser.add_argument("--objetivo", "-o", type=str, choices=list(OBJETIVOS.keys()), help="Forzar un arquetipo de encargo específico")
    parser.add_argument("--listar-objetivos", action="store_true", help="Listar todos los arquetipos de negocio disponibles")
    parser.add_argument("--semilla", "-s", type=str, help="Semilla para reproducir una tirada exacta")
    parser.add_argument("--evitar", "-e", type=str, help="Familias a evitar separadas por coma")
    parser.add_argument("--solo", type=str, help="Forzar una familia específica")
    parser.add_argument("--repetir", "-r", action="store_true", help="Ignorar el historial de tiradas recientes")
    parser.add_argument("--aleatorio", "-a", action="store_true", help="Desactivar ponderación por objetivo y usar azar puro")
    args = parser.parse_args()

    if args.listar_objetivos:
        print("ARQUETIPOS DE NEGOCIO DISPONIBLES EN EL DADO:")
        print("=" * 74)
        for obj_id, data in OBJETIVOS.items():
            print(f"• {obj_id:<22} — {data['nombre']}")
            print(f"  {data['desc']}")
        sys.exit(0)

    if args.semilla:
        random.seed(args.semilla)

    evitar = [x.strip() for x in args.evitar.split(",")] if args.evitar else []

    # Determinar objetivo
    prompt_completo = " ".join(args.prompt) if args.prompt else ""
    
    if args.aleatorio:
        objetivo_usado = None
        origen_obj = "Azar puro (--aleatorio)"
    elif args.objetivo:
        objetivo_usado = args.objetivo
        origen_obj = f"Fijado explícitamente ({OBJETIVOS[objetivo_usado]['nombre']})"
    elif prompt_completo:
        detectado, score = detectar_objetivo(prompt_completo)
        objetivo_usado = detectado
        origen_obj = f"Autodetectado ({OBJETIVOS[objetivo_usado]['nombre']} · score {score})"
    else:
        objetivo_usado = "general_ecommerce"
        origen_obj = "Por defecto (General E-Commerce)"

    if args.aleatorio:
        # Modo clásico aleatorio puro
        candidatas = [f for f in FAMILIAS if f["id"] not in evitar]
        elegidas = random.sample(candidatas, 6)
        cards_elegidas = random.sample(CARDS, 6)
        navs_elegidas = random.sample(NAVS, 6)
        heros_elegidos = random.sample(HEROS, 6)
        
        direcciones = []
        for i, (f, c, n, h) in enumerate(zip(elegidas, cards_elegidas, navs_elegidas, heros_elegidos), 1):
            direcciones.append({
                "franja": "Azar Puro",
                "estilo": f,
                "card": c,
                "nav": n,
                "hero": h
            })
    else:
        direcciones = seleccionar_seis_direcciones(
            objetivo_id=objetivo_usado,
            evitar=evitar,
            solo=args.solo,
            usar_historial=(not args.repetir)
        )

    print("Seis direcciones con familias de diseño, arquetipos de Card, Nav y Hero distintos.")
    print(f"Enfoque de selección: {origen_obj}")
    print("Cada una arranca en MODO CLARO por defecto e incluye botón para alternar a MODO OSCURO.\n")

    for i, item in enumerate(direcciones, 1):
        f = item["estilo"]
        c = item["card"]
        n = item["nav"]
        h = item["hero"]
        franja = item["franja"]
        print("=" * 74)
        print(f"PROTOTIPO {i} [{franja}] — {f['nombre']}   [estilo: {f['id']}]")
        print(f"NAV:         {n['id']} — {n['desc']}")
        print(f"HERO:        {h['id']} — {h['desc']}")
        print(f"CARD:        {c['id']} — {c['desc']}")
        print(f"PALETA CLA:  {f['paleta_cla']}")
        print(f"PALETA OSC:  {f['paleta_osc']}")
        print(f"MATERIAL:    {f['material']}")
        print()

if __name__ == "__main__":
    main()
