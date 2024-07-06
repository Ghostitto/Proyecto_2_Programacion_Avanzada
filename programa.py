from justificador_texto import *


texto = open(str(input("Ingresa el nombre del archivo:")))
largo = input("Ingresa el largo máximo de cada fila.")

respuesta = format_text(texto, largo)

print(respuesta)