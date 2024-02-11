"""
Escribir una función que reciba una muestra de números en una lista y devuelva 
otra lista con sus cuadrados
"""


def numeros(*grupo):
    lista=[]
    for i in grupo:
        lista.append(i**2)
    return lista

print(numeros(4,6,4,2,8))
print(numeros(6,4,8,54))