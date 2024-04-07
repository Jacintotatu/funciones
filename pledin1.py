"""Crea un función EscribirCentrado, que reciba como parámetro un texto y lo 
escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista: 
deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el 
mensaje utilizando el carácter =.
"""

def escribirCentrado(texto):
    return texto.center(40)

print(escribirCentrado('\033[4mMe cago en to los fruitis\033[0m'))