# pip install requests
import requests

# Torrente, el brazo tonto de la ley
r = requests.get('https://www.filmaffinity.com/es/film334167.html')

t = r.text

# print(t)   # Esto es para imprimirme el HTML de la peli

espacio = '&nbsp;'
dd = '<dd>'
dd_c = '</dd>'
span = '<span>'
span_c = '</span>'
div_c = '</div>'
dt = '<dt>'
dt_c = '</dt>'
a = '<a>'
a_c = '</a>'
style = '<style>'
style_c = '</style>'


def extraer_titulo_original(t):
    label = t[t.find('<dt>Título original</dt>'):t.find(dd_c)]

    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()

    find_aka = titulo_original.find('<span')

    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]

    return titulo_original


def extraer_año(t):
    longitud_etiqueta_año = len('<dd itemprop="datePublished">')

    año = t[t.find('<dd itemprop="datePublished">') +
            longitud_etiqueta_año:t.find('<dd itemprop="datePublished">')+longitud_etiqueta_año+4]

    return año


def extraer_duracion(t):
    longitud_etiqueta_duracion = len('<dd itemprop="duration">')

    duracion = t[t.find('<dd itemprop="duration">') +
                 longitud_etiqueta_duracion:t.find('<dd itemprop="duration">')+longitud_etiqueta_duracion+7]

    return duracion


def extraer_pais(t):
    longitud_espacio = len(espacio)

    label = t[t.find('<span id="country-img">'):]

    pais = label[label.find(espacio)+longitud_espacio:label.find(dd_c)]

    return pais


def extraer_direccion(t):
    longitud_etiqueta_direccion = len('<span itemprop="name">')

    label = t[t.find('<dd class="directors">'):]

    direccion = label[label.find(
        '<span itemprop="name">')+longitud_etiqueta_direccion:label.find(span_c)]

    return direccion


def extraer_guion(t):
    longitud_etiqueta_span = len('<span>')

    label = t[t.find('<dt>Guion</dt>'):]

    guion = label[label.find('<span>')+longitud_etiqueta_span:label.find(span_c)]

    return guion


def extraer_musica(t):
    longitud_etiqueta_span = len('<span>')

    label = t[t.find('<dt>Música</dt>'):]

    musica = label[label.find('<span>')+longitud_etiqueta_span:label.find(span_c)]

    return musica


def extraer_fotografia(t):
    longitud_etiqueta_span = len('<span>')

    label = t[t.find('<dt>Fotografía</dt>'):]

    fotografia = label[label.find('<span>')+longitud_etiqueta_span:label.find(span_c)]

    return fotografia


def extraer_reparto(t):
    label = t[t.find('<dt>Reparto</dt>'):]

    label = label[label.find('<span itemprop="name">'):label.find(style_c)]

    array = label.split("name")
    array.pop(0)

    reparto = ""

    for i in array:
        reparto += i[2:i.find(span_c)]+", "

    return reparto


def extraer_productora(t):
    longitud_etiqueta_span = len('<span>')

    label = t[t.find('<dt>Compañías</dt>'):]

    productora = label[label.find('<span>')+longitud_etiqueta_span:label.find(span_c)]

    return productora


def extraer_genero(t):
    cadena = '<a href="https://www.filmaffinity.com/es/moviegenre.php?genre=CO&attr=rat_count&nodoc">'

    longitud = len(cadena)

    label = t[t.find('<dt>Género</dt>'):]

    label = label[label.find(
        '<a href="https://www.filmaffinity.com/es/moviegenre.php?genre=CO&attr=rat_count&nodoc">')+longitud:label.find(dd_c)]

    array = label.split("<a")

    generos = ""

    generos += label[:label.find(a_c)]+", "

    array.pop(0)

    for i in array:
        cadena = 'count&nodoc">'
        longitud = len(cadena)
        generos += i[i.find('count&nodoc">')+longitud:i.find(a_c)]+", "

    return generos


def extraer_sinopsis(t):
    longitud_etiqueta_sinopsis = len('<dd class="" itemprop="description">')

    label = t[t.find('<dt>Sinopsis</dt>'):]

    sinopsis = label[label.find(
        '<dd class="" itemprop="description">')+longitud_etiqueta_sinopsis:label.find(dd_c)]

    return sinopsis


diccionario = {
    "titulo_original": extraer_titulo_original(t),
    "año": extraer_año(t),
    "duracion": extraer_duracion(t),
    "pais": extraer_pais(t),
    "direccion": extraer_direccion(t),
    "guion": extraer_guion(t),
    "musica": extraer_musica(t),
    "fotografia": extraer_fotografia(t),
    "reparto": extraer_reparto(t),
    "productora": extraer_productora(t),
    "genero": extraer_genero(t),
    "sinopsis": extraer_sinopsis(t)
}

print(diccionario)
