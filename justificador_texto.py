import numpy as np
from LCSubStr import *
from WordBreak import *

def format_text(text: str, maxWidth: int) -> list[str]:
    """Asigna al archivo recibido un formato justificado de ancho máximo maxWidth y devuelve una lista
    de cada fila del texto resultante."""

    lista_palabras =  text.split() # Lista de todas las palabras del texto.
    respuesta = [] # Respuesta final


    # Valores iniciales
    valor_temp_anterior = 0 # Posición de la primera letra de cada palabra.
    posicion_text = 0 # Posición de la primera letra de la primera palabra de cada fila.
    j = 0 # posición en la lista de palabras.
    h = 0 # Posición en la lista de palabras de la primera palabra de cada fila.


    while j + 1 < len(lista_palabras):

        text_temp = text[posicion_text: maxWidth + posicion_text] # Frase de largo maxWidth (mal escrito)
        str_temp = lista_palabras[j] # Frase (bien escrito)
        valor_temp_anterior = 0
        valor_temp = len(lista_palabras[j])
        
        # Si la palabra en text_temp está bien escrita, se agrega a la frase final de la fila.
        while wordBreak(lista_palabras[j: j + 1] + [" "], text_temp[valor_temp_anterior: valor_temp]):
            if j + 1 == len(lista_palabras):
                j += 1
                break

            str_temp += " " + lista_palabras[j + 1]
            valor_temp_anterior = valor_temp

            valor_temp = int(LCSubStr(text_temp, str_temp) + 1)
            j += 1

            if valor_temp == valor_temp_anterior: 
                break
            

        posicion_text += valor_temp_anterior

        respuesta += [lista_palabras[h: j]]
        h = j

    if respuesta[-1][-1] != lista_palabras[-1]:
        respuesta += [[lista_palabras[-1]]]


    return respuesta




#Ejemplo con cual funciona
print(format_text("buenas tardes, como está, yo estoy super bien", 15))





#WordBreak para eliminar los datos ya utilizados de la lista
# SolveWord para optimizar posiciones