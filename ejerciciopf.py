"""
Añade cualquier color con un input al principio de la lista mediante una función.
Debes comprobar fuera de la función, con un print(), que el color se ha añadido
correctamente.
"""

"""
colores = ["rojo", "verde", "amarillo"]

def meter_colores(colores):
    while True:
        color = input('Dime un color: ')
        if color == 'q':
            break
        else:
            colores.append(color)
        print(color)

meter_colores(colores)

print('Los colores de la lista son: ')
for color in colores:
    print(f'· {color}.')

"""
#############################################################################

# Encuentra un posible error en esta función:

def saludar():  #los dos puntos
    nombre = input("Introduzca su nombre, por favor\n")
    print(f"¡Muy buenas, {nombre}!")

saludar()  # y la llamada


