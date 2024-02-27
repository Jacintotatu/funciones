"""
Escribir una función que calcule el área de un círculo y otra que calcule el 
volumen de un cilindro usando la primera función.
"""
def circulo(radio):
    pi = 3.14
    return pi * radio**2

def volumen(radio, altura):
    return circulo(radio) * altura


print(volumen(25, 10))

def rectangulo(base, altura):
    return base * altura

print(rectangulo(4, 5))