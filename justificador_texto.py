def format_text(text: str, maxWidth: int) -> list[str]:
    """Asigna al archivo recibido un formato justificado de ancho máximo maxWidth y devuelve una lista
    de cada fila del texto resultante."""
    lista_palabras =  text.split()
    return lista_palabras