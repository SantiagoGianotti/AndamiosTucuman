"""Genera el catálogo PDF de Tucumán Andamios y Equipos."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white, Color
from reportlab.pdfgen import canvas
from PIL import Image
import os

BASE = '/home/santiagog/Proyectos/AndamiosTucuman/catalogo-fotos'
LOGO = os.path.join(BASE, 'logo-circular.png')
OUT = '/home/santiagog/Proyectos/AndamiosTucuman/Catalogo-Tucuman-Andamios.pdf'

# Links
WHATSAPP_URL = 'https://wa.me/5493816938388'
WEBSITE_URL = 'https://tucumanandamios.com.ar'
INSTAGRAM_URL = 'https://www.instagram.com/tucuman.andamios/'
TEL_URL = 'tel:+5493816938388'
MAPS_URL = 'https://maps.google.com/?q=Guyanas+401,+Yerba+Buena,+Tucumán'

# Brand palette
NAVY = HexColor('#0f172a')
GOLD = HexColor('#eab308')
BLUE = HexColor('#1a5fb4')
LIGHT = HexColor('#f1f5f9')
HAIRLINE = HexColor('#cbd5e1')
NAVY_70 = Color(15 / 255, 23 / 255, 42 / 255, alpha=0.7)
WHITE_80 = Color(1, 1, 1, alpha=0.8)
GOLD_40 = Color(234 / 255, 179 / 255, 8 / 255, alpha=0.4)

TITULO = 'Catálogo de Equipos'
SUBTITULO = 'Tucumán Andamios y Equipos — Alquiler profesional en todo Tucumán'
TAGLINE = 'Equipos que rinden. Obras que avanzan.'
CTA_BACK = '¿Necesitás un presupuesto? Hablemos hoy.'

categorias = [
    {
        'name': 'Compactación de Bases',
        'intro': 'Compactación firme y pareja para bases de veredas, contrapisos, cimientos y terraplenes.',
        'equipos': [
            {'nombre': 'Placa Vibratoria Chancha', 'foto': 'equipo-14.jpeg',
             'desc': 'Compactadora a nafta de alta frecuencia para compactar bases de suelos y gravilla. Dejá tu base lista para contrapisos, veredas o adoquinado con acabado parejo y firme.'},
            {'nombre': 'Canguro Pisonador', 'foto': 'equipo-03.jpeg',
             'desc': 'Pisón percutor para compactar bases en zanjas angostas y espacios reducidos. Perfecto para rellenos alrededor de cañerías, cimientos y trabajos donde la placa no entra.'},
        ]
    },
    {
        'name': 'Demolición y Corte',
        'intro': 'Potencia controlada para intervenir hormigón, mampostería y pavimentos.',
        'equipos': [
            {'nombre': 'Martillo Demoledor', 'foto': 'equipo-04.jpeg',
             'desc': 'Martillo eléctrico de alto impacto para romper hormigón, mampostería y pavimento. Apurás demoliciones y aperturas de canaletas sin depender de un compresor.'},
            {'nombre': 'Cortadora de Hormigón', 'foto': 'equipo-17.jpeg',
             'desc': 'Cortadora a nafta con disco diamantado y refrigeración por agua. Hacés cortes limpios en losas, pavimentos y veredas para juntas de dilatación o reparaciones.'},
            {'nombre': 'Amoladora', 'foto': 'equipo-11.jpeg',
             'desc': 'Amoladora profesional para cortar y desbastar metal, hormigón y cerámicos. Una herramienta versátil que no puede faltar en ninguna obra.'},
        ]
    },
    {
        'name': 'Hormigón',
        'intro': 'Todo lo que necesitás para preparar, colocar y terminar hormigón en obra.',
        'equipos': [
            {'nombre': 'Vibrador de Hormigón', 'foto': 'equipo-02.jpeg',
             'desc': 'Vibrador de inmersión con chicote flexible que elimina burbujas de aire del hormigón fresco. Lográs columnas, vigas y losas más densas, resistentes y sin nidos de abeja.'},
            {'nombre': 'Allanadora Helicóptero', 'foto': 'equipo-10.jpeg',
             'desc': 'Allanadora mecánica con aspas rotativas para terminación de pisos de hormigón. Conseguís superficies lisas, compactas y listas para uso industrial o comercial.'},
            {'nombre': 'Hormigonera', 'foto': 'equipo-15.jpeg',
             'desc': 'Hormigonera con tambor rotativo para preparar mezclas en obra. Ganás autonomía y mezclás la cantidad justa cuando la necesitás, sin depender del camión mixer.'},
            {'nombre': 'Revocadora', 'foto': 'equipo-16.jpeg',
             'desc': 'Máquina revocadora que proyecta mortero directo sobre el muro. Multiplicás el rendimiento de tu cuadrilla y terminás paredes en menos tiempo, con espesor parejo.'},
        ]
    },
    {
        'name': 'Trabajo en Altura',
        'intro': 'Soluciones seguras para llegar alto sin complicarte la logística.',
        'equipos': [
            {'nombre': 'Tijera Elevadora', 'foto': 'equipo-13.jpeg',
             'desc': 'Elevador tipo tijera autopropulsado para trabajos seguros en altura. Ideal para montajes, mantenimiento, pintura y tareas donde el andamio no es práctico.'},
            {'nombre': 'Andamios', 'foto': 'equipo-07.jpeg',
             'desc': 'Andamios tubulares y de aluminio en distintas alturas, armado rápido y seguro. Contamos con stock suficiente para obras chicas, grandes y frentes múltiples en simultáneo.'},
            {'nombre': 'Escaleras Extensibles', 'foto': 'equipo-06.jpeg',
             'desc': 'Escaleras de gran alcance para tareas puntuales en altura. Resolvés trabajos de fachada, instalación o mantenimiento sin necesidad de montar andamio completo.'},
        ]
    },
    {
        'name': 'Maquinaria Pesada',
        'intro': 'Movimiento de materiales y trabajos pesados con rendimiento garantizado.',
        'equipos': [
            {'nombre': 'Minicargadora', 'foto': 'equipo-01.jpeg',
             'desc': 'Bobcat con pala frontal para mover tierra, escombros y materiales en espacios reducidos. Aumentás la productividad del obrador y reducís tiempos de carga y traslado interno.'},
            {'nombre': 'Autoelevador', 'foto': 'equipo-12.jpeg',
             'desc': 'Autoelevador de 2.5 toneladas para mover pallets, bolsones y cargas pesadas. Ágil en playa de obra, depósito o pañol, con operación cómoda y segura.'},
        ]
    },
    {
        'name': 'Limpieza',
        'intro': 'Potencia industrial para dejar obras, pisos y maquinaria impecables.',
        'equipos': [
            {'nombre': 'Hidrolavadora Industrial', 'foto': 'equipo-18.jpeg',
             'desc': 'Hidrolavadora de alta presión con motor eléctrico y bomba profesional. Ideal para limpieza de obras, pisos, maquinaria y fachadas donde se necesita potencia real.'},
        ]
    },
]

W, H = A4


# ---------- Helpers ----------

def tracked_string(c, x, y, text, font, size, color, tracking=0, align='left'):
    """Draw text with letter-spacing (tracking in thousandths of em)."""
    c.setFont(font, size)
    c.setFillColor(color)
    space = size * tracking / 1000.0
    total_width = sum(c.stringWidth(ch, font, size) for ch in text) + space * (len(text) - 1)
    if align == 'center':
        x = x - total_width / 2
    elif align == 'right':
        x = x - total_width
    cur = x
    for ch in text:
        c.drawString(cur, y, ch)
        cur += c.stringWidth(ch, font, size) + space


def wrap_text(c, text, font, size, max_width):
    """Simple word wrap."""
    words = text.split()
    lines, current = [], []
    for word in words:
        test = ' '.join(current + [word])
        if c.stringWidth(test, font, size) < max_width:
            current.append(word)
        else:
            if current:
                lines.append(' '.join(current))
            current = [word]
    if current:
        lines.append(' '.join(current))
    return lines


def draw_image_contained(c, path, x, y, max_w, max_h):
    """Draw image preserving aspect ratio, centered in box."""
    if not os.path.exists(path):
        return
    img = Image.open(path)
    iw, ih = img.size
    aspect = iw / ih
    if aspect > max_w / max_h:
        draw_w = max_w
        draw_h = max_w / aspect
    else:
        draw_h = max_h
        draw_w = max_h * aspect
    draw_x = x + (max_w - draw_w) / 2
    draw_y = y + (max_h - draw_h) / 2
    c.drawImage(path, draw_x, draw_y, width=draw_w, height=draw_h,
                preserveAspectRatio=True, mask='auto')


def diagonal_band(c, anchor='bottom-left'):
    """Draw the signature diagonal gold band."""
    c.saveState()
    if anchor == 'bottom-left':
        c.translate(0, 0)
        c.rotate(15)
        c.setFillColor(GOLD)
        c.rect(-5 * cm, -2 * cm, W + 10 * cm, 6 * cm, fill=1, stroke=0)
    else:  # top-right
        c.translate(W, H)
        c.rotate(15)
        c.setFillColor(GOLD)
        c.rect(-W - 5 * cm, -4 * cm, W + 10 * cm, 6 * cm, fill=1, stroke=0)
    c.restoreState()


# ---------- Pages ----------

def draw_cover(c):
    # Background
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Diagonal gold band (bottom-left)
    c.saveState()
    c.translate(-3 * cm, 5 * cm)
    c.rotate(-15)
    c.setFillColor(GOLD)
    c.rect(0, 0, W + 6 * cm, 4 * cm, fill=1, stroke=0)
    c.restoreState()

    # Logo (circular with transparency)
    if os.path.exists(LOGO):
        logo_diam = 7 * cm
        cx = W / 2
        cy = H - 4.5 * cm - logo_diam / 2
        c.drawImage(LOGO, cx - logo_diam / 2, cy - logo_diam / 2,
                    width=logo_diam, height=logo_diam,
                    preserveAspectRatio=True, mask='auto')

    # Eyebrow
    tracked_string(c, W / 2, H - 13.5 * cm, 'CATÁLOGO DE EQUIPOS',
                   'Helvetica-Bold', 11, GOLD, tracking=200, align='center')

    # Main title
    c.setFont('Helvetica-Bold', 44)
    c.setFillColor(white)
    c.drawCentredString(W / 2, H - 15.5 * cm, 'TUCUMÁN')

    # Subtitle
    c.setFont('Helvetica-Bold', 22)
    c.drawCentredString(W / 2, H - 17.8 * cm, 'ANDAMIOS Y EQUIPOS')

    # Gold divider
    c.setFillColor(GOLD)
    c.rect(W / 2 - 2 * cm, H - 19.5 * cm, 4 * cm, 0.07 * cm, fill=1, stroke=0)

    # Tagline
    c.setFillColor(WHITE_80)
    c.setFont('Helvetica', 13)
    c.drawCentredString(W / 2, H - 20.5 * cm, TAGLINE)

    # Footer strip (gold band)
    c.setFillColor(GOLD)
    c.rect(0, 0, W, 1.2 * cm, fill=1, stroke=0)
    tracked_string(c, W / 2, 0.45 * cm, 'YERBA BUENA · TUCUMÁN · 2026',
                   'Helvetica-Bold', 10, NAVY, tracking=150, align='center')

    c.showPage()


def draw_toc(c, toc_entries):
    """Draw table of contents page.

    toc_entries: list of dicts with 'type' ('category' or 'equipo'),
    'name', and 'page'.
    """
    # Header band
    c.setFillColor(NAVY)
    c.rect(0, H - 2.2 * cm, W, 2.2 * cm, fill=1, stroke=0)

    if os.path.exists(LOGO):
        lh = 1.4 * cm
        c.drawImage(LOGO, 1.8 * cm, H - 2.2 * cm + 0.4 * cm,
                    width=lh, height=lh, preserveAspectRatio=True, mask='auto')

    tracked_string(c, W - 1.8 * cm, H - 1.35 * cm, 'ÍNDICE',
                   'Helvetica-Bold', 9, GOLD, tracking=200, align='right')

    # Gold accent under header
    c.setFillColor(GOLD)
    c.rect(0, H - 2.3 * cm, W, 0.1 * cm, fill=1, stroke=0)

    # Title
    tracked_string(c, 1.8 * cm, H - 4 * cm, 'CONTENIDO',
                   'Helvetica-Bold', 9, GOLD, tracking=200, align='left')
    c.setFillColor(NAVY)
    c.setFont('Helvetica-Bold', 32)
    c.drawString(1.8 * cm, H - 5.5 * cm, 'Índice')
    c.setFillColor(GOLD)
    c.rect(1.8 * cm, H - 6 * cm, 3 * cm, 0.07 * cm, fill=1, stroke=0)

    # Entries
    y = H - 7.5 * cm
    for entry in toc_entries:
        if entry['type'] == 'category':
            if y < H - 7.8 * cm:
                y -= 0.3 * cm  # extra space before category
            tracked_string(c, 1.8 * cm, y, entry['name'].upper(),
                           'Helvetica-Bold', 11, NAVY, tracking=150,
                           align='left')
            # Gold small rule
            c.setFillColor(GOLD)
            c.rect(1.8 * cm, y - 0.25 * cm, 1.5 * cm, 0.04 * cm,
                   fill=1, stroke=0)
            # Page number
            c.setFillColor(NAVY_70)
            c.setFont('Helvetica', 10)
            c.drawRightString(W - 1.8 * cm, y,
                              f"pág. {entry['page']}")
            # Clickable link to the category divider
            if entry.get('bookmark'):
                c.linkAbsolute('', entry['bookmark'],
                               (1.8 * cm, y - 0.3 * cm,
                                W - 1.8 * cm, y + 0.4 * cm),
                               thickness=0)
            y -= 0.85 * cm
        else:
            c.setFillColor(NAVY_70)
            c.setFont('Helvetica', 10.5)
            c.drawString(2.6 * cm, y, entry['name'])
            # dotted leader
            text_w = c.stringWidth(entry['name'], 'Helvetica', 10.5)
            dot_start = 2.6 * cm + text_w + 0.3 * cm
            dot_end = W - 2.5 * cm
            c.setFillColor(HAIRLINE)
            c.setFont('Helvetica', 10.5)
            x = dot_start
            while x < dot_end:
                c.drawString(x, y, '.')
                x += 0.2 * cm
            c.setFillColor(NAVY)
            c.setFont('Helvetica-Bold', 10.5)
            c.drawRightString(W - 1.8 * cm, y, str(entry['page']))
            # Clickable link to the equipment page
            if entry.get('bookmark'):
                c.linkAbsolute('', entry['bookmark'],
                               (2.6 * cm, y - 0.2 * cm,
                                W - 1.8 * cm, y + 0.3 * cm),
                               thickness=0)
            y -= 0.7 * cm

    # Footer
    c.setFillColor(GOLD)
    c.rect(0, 2.2 * cm, W, 0.1 * cm, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(0, 0, W, 2.2 * cm, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont('Helvetica', 9)
    c.drawString(1.8 * cm, 0.8 * cm, 'tucumanandamios.com.ar')
    c.setFont('Helvetica-Bold', 10)
    c.drawCentredString(W / 2, 0.8 * cm, '2')
    c.setFont('Helvetica', 9)
    c.drawRightString(W - 1.8 * cm, 0.8 * cm, '+54 9 3816 93-8388')

    c.linkURL(WEBSITE_URL,
              (1.8 * cm, 0.4 * cm, 7 * cm, 1.4 * cm),
              relative=0, thickness=0)
    c.linkURL(WHATSAPP_URL,
              (W - 7 * cm, 0.4 * cm, W - 1.8 * cm, 1.4 * cm),
              relative=0, thickness=0)

    c.showPage()


def draw_category_divider(c, cat, number, bookmark_key=None):
    if bookmark_key:
        c.bookmarkPage(bookmark_key)

    # Top half: Navy
    c.setFillColor(NAVY)
    c.rect(0, H / 2, W, H / 2, fill=1, stroke=0)

    # Category number (oversized gold)
    c.setFillColor(GOLD)
    c.setFont('Helvetica-Bold', 120)
    c.drawString(2 * cm, H / 2 + 2 * cm, f'{number:02d}')

    # Eyebrow above numeral
    tracked_string(c, 2 * cm, H / 2 + 120 * 0.8 + 2 * cm + 0.5 * cm,
                   'CATEGORÍA', 'Helvetica-Bold', 9, white,
                   tracking=300, align='left')

    # Category name (bottom half) — dynamic size to avoid overflow
    c.setFillColor(NAVY)
    name_max_width = W - 4 * cm
    size = 32
    while c.stringWidth(cat['name'], 'Helvetica-Bold', size) > name_max_width and size > 22:
        size -= 1
    c.setFont('Helvetica-Bold', size)
    c.drawString(2 * cm, H / 2 - 2.5 * cm, cat['name'])

    # Gold rule
    c.setFillColor(GOLD)
    c.rect(2 * cm, H / 2 - 3 * cm, 5 * cm, 0.07 * cm, fill=1, stroke=0)

    # Intro
    c.setFillColor(NAVY_70)
    c.setFont('Helvetica', 11)
    lines = wrap_text(c, cat['intro'], 'Helvetica', 11, W - 4 * cm)
    y = H / 2 - 4 * cm
    for line in lines:
        c.drawString(2 * cm, y, line)
        y -= 0.5 * cm

    # Items list (below intro, two columns if needed)
    y -= 0.5 * cm
    tracked_string(c, 2 * cm, y, 'EN ESTA SECCIÓN',
                   'Helvetica-Bold', 9, GOLD, tracking=200, align='left')
    y -= 0.8 * cm
    c.setFillColor(NAVY)
    c.setFont('Helvetica', 11)
    for i, eq in enumerate(cat['equipos'], 1):
        # Gold dot
        c.setFillColor(GOLD)
        c.circle(2.15 * cm, y + 0.15 * cm, 0.1 * cm, fill=1, stroke=0)
        # Name
        c.setFillColor(NAVY)
        c.setFont('Helvetica', 11)
        c.drawString(2.5 * cm, y, eq['nombre'])
        y -= 0.6 * cm

    c.showPage()


def draw_equipment_page(c, eq, cat_name, item_num, cat_num, page_num, total_pages,
                        bookmark_key=None):
    if bookmark_key:
        c.bookmarkPage(bookmark_key)
    # Header band
    c.setFillColor(NAVY)
    c.rect(0, H - 2.2 * cm, W, 2.2 * cm, fill=1, stroke=0)

    # Logo in header (small)
    if os.path.exists(LOGO):
        lh = 1.4 * cm
        c.drawImage(LOGO, 1.8 * cm, H - 2.2 * cm + 0.4 * cm,
                    width=lh, height=lh, preserveAspectRatio=True, mask='auto')

    # Category name in header (right)
    tracked_string(c, W - 1.8 * cm, H - 1.35 * cm, cat_name.upper(),
                   'Helvetica-Bold', 9, GOLD, tracking=200, align='right')

    # Photo zone background
    c.setFillColor(LIGHT)
    c.rect(0, H - 2.2 * cm - 12.3 * cm, W, 12.3 * cm, fill=1, stroke=0)

    # Photo
    img_path = os.path.join(BASE, eq['foto'])
    draw_image_contained(c, img_path, 3.5 * cm, H - 2.2 * cm - 11.3 * cm,
                         14 * cm, 10.5 * cm)

    # Gold signature hairline below photo
    c.setFillColor(GOLD)
    c.rect(1.8 * cm, H - 2.2 * cm - 12.3 * cm - 0.4 * cm,
           4 * cm, 0.05 * cm, fill=1, stroke=0)

    # Item tag (number + category)
    item_tag = f'{item_num:02d} · {cat_name.upper()}'
    tracked_string(c, 1.8 * cm, H - 2.2 * cm - 12.3 * cm - 1.5 * cm,
                   item_tag, 'Helvetica-Bold', 9, GOLD, tracking=200,
                   align='left')

    # Equipment name
    c.setFillColor(NAVY)
    c.setFont('Helvetica-Bold', 26)
    c.drawString(1.8 * cm, H - 2.2 * cm - 12.3 * cm - 2.7 * cm, eq['nombre'])

    # Gold rule
    c.setFillColor(GOLD)
    c.rect(1.8 * cm, H - 2.2 * cm - 12.3 * cm - 3.2 * cm,
           2.5 * cm, 0.07 * cm, fill=1, stroke=0)

    # Description body
    c.setFillColor(NAVY)
    c.setFont('Helvetica', 11)
    lines = wrap_text(c, eq['desc'], 'Helvetica', 11, 17 * cm)
    y = H - 2.2 * cm - 12.3 * cm - 4 * cm
    for line in lines:
        c.drawString(1.8 * cm, y, line)
        y -= 0.55 * cm

    # Consulta callout (clickable WhatsApp)
    callout_y = 3 * cm
    c.setFillColor(LIGHT)
    c.roundRect(1.8 * cm, callout_y, W - 3.6 * cm, 2.4 * cm,
                0.3 * cm, fill=1, stroke=0)

    tracked_string(c, 2.3 * cm, callout_y + 1.7 * cm, 'CONSULTÁ DISPONIBILIDAD',
                   'Helvetica-Bold', 9, GOLD, tracking=200, align='left')
    c.setFillColor(NAVY)
    c.setFont('Helvetica-Bold', 13)
    c.drawString(2.3 * cm, callout_y + 0.9 * cm,
                 'WhatsApp: +54 9 3816 93-8388')
    c.setFillColor(NAVY_70)
    c.setFont('Helvetica', 9)
    c.drawString(2.3 * cm, callout_y + 0.35 * cm,
                 'Respondemos en minutos · Entrega en obra')

    # Make the whole callout clickable (WhatsApp)
    c.linkURL(WHATSAPP_URL,
              (1.8 * cm, callout_y, W - 1.8 * cm, callout_y + 2.4 * cm),
              relative=0, thickness=0)

    # Footer bands
    c.setFillColor(GOLD)
    c.rect(0, 2.2 * cm, W, 0.1 * cm, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(0, 0, W, 2.2 * cm, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont('Helvetica', 9)
    c.drawString(1.8 * cm, 0.8 * cm, 'tucumanandamios.com.ar')
    c.setFont('Helvetica-Bold', 10)
    c.drawCentredString(W / 2, 0.8 * cm, f'{page_num} / {total_pages}')
    c.setFont('Helvetica', 9)
    c.drawRightString(W - 1.8 * cm, 0.8 * cm, '+54 9 3816 93-8388')

    # Footer links (clickable)
    c.linkURL(WEBSITE_URL,
              (1.8 * cm, 0.4 * cm, 7 * cm, 1.4 * cm),
              relative=0, thickness=0)
    c.linkURL(WHATSAPP_URL,
              (W - 7 * cm, 0.4 * cm, W - 1.8 * cm, 1.4 * cm),
              relative=0, thickness=0)

    c.showPage()


def draw_back_cover(c):
    # Background
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Diagonal gold band (top-right, mirrored)
    c.saveState()
    c.translate(W + 3 * cm, H - 5 * cm)
    c.rotate(-15)
    c.setFillColor(GOLD)
    c.rect(-W - 6 * cm, 0, W + 6 * cm, 4 * cm, fill=1, stroke=0)
    c.restoreState()

    # Logo
    if os.path.exists(LOGO):
        ld = 5 * cm
        cx = W / 2
        cy = H - 4 * cm - ld / 2
        c.drawImage(LOGO, cx - ld / 2, cy - ld / 2,
                    width=ld, height=ld, preserveAspectRatio=True, mask='auto')

    # Headline
    tracked_string(c, W / 2, H - 11 * cm, 'CONTACTO',
                   'Helvetica-Bold', 28, GOLD, tracking=150, align='center')

    # Gold rule
    c.setFillColor(GOLD)
    c.rect(W / 2 - 1.5 * cm, H - 12 * cm, 3 * cm, 0.07 * cm, fill=1, stroke=0)

    # CTA
    c.setFillColor(white)
    c.setFont('Helvetica', 13)
    c.drawCentredString(W / 2, H - 13 * cm, CTA_BACK)

    # Contact block (with clickable links)
    contact_items = [
        ('WhatsApp', '+54 9 3816 93-8388', WHATSAPP_URL),
        ('Web', 'tucumanandamios.com.ar', WEBSITE_URL),
        ('Instagram', '@tucuman.andamios', INSTAGRAM_URL),
        ('Dirección', 'Guyanas 401, Yerba Buena, Tucumán', MAPS_URL),
        ('Horarios', 'Lun-Dom 8 a 21 hs', None),
    ]
    y = H - 15 * cm
    for label, value, url in contact_items:
        tracked_string(c, W / 2, y, label.upper(),
                       'Helvetica-Bold', 10, GOLD, tracking=150,
                       align='center')
        c.setFillColor(white)
        c.setFont('Helvetica', 13)
        c.drawCentredString(W / 2, y - 0.55 * cm, value)
        # Clickable area over label + value
        if url:
            text_w = c.stringWidth(value, 'Helvetica', 13)
            c.linkURL(url,
                      (W / 2 - text_w / 2 - 0.5 * cm, y - 0.9 * cm,
                       W / 2 + text_w / 2 + 0.5 * cm, y + 0.4 * cm),
                      relative=0, thickness=0)
        y -= 1.6 * cm

    # Bottom gold band
    c.setFillColor(GOLD)
    c.rect(0, 0, W, 1.2 * cm, fill=1, stroke=0)
    tracked_string(c, W / 2, 0.45 * cm,
                   'TUCUMÁN ANDAMIOS Y EQUIPOS · 2026',
                   'Helvetica-Bold', 10, NAVY, tracking=150, align='center')

    c.showPage()


# ---------- Build ----------

def main():
    c = canvas.Canvas(OUT, pagesize=A4)

    # Page plan:
    # 1: cover, 2: toc, then per category: divider + N equipment, then back cover
    total_equipos = sum(len(cat['equipos']) for cat in categorias)
    total_pages = 1 + 1 + len(categorias) + total_equipos + 1

    # Compute TOC entries with correct page numbers and bookmark keys
    toc = []
    page = 3  # cover=1, toc=2, first divider=3
    for cat_idx, cat in enumerate(categorias):
        cat_bookmark = f'cat_{cat_idx}'
        toc.append({'type': 'category', 'name': cat['name'],
                    'page': page, 'bookmark': cat_bookmark})
        cat['_bookmark'] = cat_bookmark
        page += 1  # divider
        for eq_idx, eq in enumerate(cat['equipos']):
            eq_bookmark = f'eq_{cat_idx}_{eq_idx}'
            toc.append({'type': 'equipo', 'name': eq['nombre'],
                        'page': page, 'bookmark': eq_bookmark})
            eq['_bookmark'] = eq_bookmark
            page += 1

    # Set PDF metadata
    c.setTitle('Catálogo de Equipos - Tucumán Andamios y Equipos')
    c.setAuthor('Tucumán Andamios y Equipos')
    c.setSubject('Alquiler de andamios, maquinaria y servicios para obras')

    # Cover (page 1)
    draw_cover(c)

    # TOC (page 2)
    draw_toc(c, toc)

    # Categories
    page = 3
    for cat_idx, cat in enumerate(categorias, 1):
        draw_category_divider(c, cat, cat_idx,
                              bookmark_key=cat.get('_bookmark'))
        page += 1
        for item_idx, eq in enumerate(cat['equipos'], 1):
            draw_equipment_page(c, eq, cat['name'], item_idx, cat_idx,
                                page, total_pages,
                                bookmark_key=eq.get('_bookmark'))
            page += 1

    # Back cover
    draw_back_cover(c)

    c.save()
    print(f'✓ PDF generado: {OUT}')
    print(f'  Páginas totales: {total_pages}')


if __name__ == '__main__':
    main()
