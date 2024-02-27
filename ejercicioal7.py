"""
Escribir una función que reciba una muestra de números en una lista y devuelva 
otra lista con sus cuadrados
"""


def numeros(*grupo):
    return [i**2 for i in grupo]

print(numeros(4,6,4,2,8))
print(numeros(6,4,8,54))


def vehiculos(*con_ruedas):  # sourcery skip: identity-comprehension
    return [i for i in con_ruedas]

print(vehiculos('moto', 'coche', 'avion', 'patinete'))