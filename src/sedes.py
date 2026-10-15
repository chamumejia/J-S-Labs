import csv
import json
import unicodedata
from pathlib import Path


SEDES_VALIDAS = {
    "itagui": "Itagüí",
    "envigado": "Envigado",
    "env": "Envigado",
    "sabaneta": "Sabaneta",
}


def normalizar_sede(valor):
    """Devuelve la sede con nombre estándar o None si no la reconoce."""
    if valor is None:
        return None

    texto = str(valor).strip().casefold()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caracter
        for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )
    texto = texto.rstrip(".").strip()

    return SEDES_VALIDAS.get(texto)


def _leer_txt(ruta):
    with ruta.open(encoding="utf-8") as archivo:
        for linea in archivo:
            clave, separador, valor = linea.partition(":")
            if separador and clave.strip().casefold() == "sede":
                return normalizar_sede(valor)
    return None


def _leer_csv(ruta):
    with ruta.open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        fila = next(lector, None)

        if fila is None:
            return None

        for campo, valor in fila.items():
            if campo is not None and campo.strip().casefold() == "sede":
                return normalizar_sede(valor)
    return None


def _leer_json(ruta):
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)

    if not isinstance(datos, dict):
        return None

    for campo, valor in datos.items():
        if str(campo).strip().casefold() == "sede":
            return normalizar_sede(valor)
    return None


def obtener_sede(ruta):
    """Lee un pedido y devuelve su sede normalizada, o None si no la reconoce."""
    ruta = Path(ruta)

    try:
        extension = ruta.suffix.casefold()
        if extension == ".txt":
            return _leer_txt(ruta)
        if extension == ".csv":
            return _leer_csv(ruta)
        if extension == ".json":
            return _leer_json(ruta)
    except (OSError, UnicodeError, json.JSONDecodeError, csv.Error):
        return None

    return None
