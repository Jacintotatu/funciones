"""
Escribir una función que reciba una muestra de números en una lista y devuelva 
su media.
"""


def suma(*media):
    return sum(media) / len(media)

print(suma(1, 45, 65 ,23, 67))