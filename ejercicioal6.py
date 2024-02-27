"""
Escribir una función que reciba una muestra de números en una lista y devuelva 
su media.
"""


def suma(*media):
    return sum(media) / len(media)

print(suma(1, 90, 87 ,23, 98))

def compra(*alimentos):
    return sum(alimentos)

print(round(compra(5.95, 4.30, 9.99, 2.50),2))

def animales(*mamiferos):
    return sum(mamiferos)

print(animales(23, 45, 32, 56, 67))