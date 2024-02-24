"""
print('mostrar el numero mayor')

num1 = int(input('Dame un numero: '))
num2 = int(input('Dame otro numero: '))

def DevuelveMax(num1, num2):
    if num1 < num2:
        print(num2)
    elif num2 < num1:
        print(num1)
    else:
        print('Son iguales')
    

print('El numero mas alto es: ')
DevuelveMax(num1, num2)

#mi version############################################################
from numpy import append


print('Datos')

datos = []
Nombre = input('Nombre: ')
Direccion = input('Direccion: ')
telefono = int(input('Tlfn.: '))

datos.append(Nombre)
datos.append(Direccion)
datos.append(telefono)

print('Los datos personales son: ')
for i in datos:
    print(i, end=' ')

#version pro#############################################################

Nombre = input('Nombre: ')

Direccion = input('Direccion: ')

telefono = int(input('Tlfn.: '))

datos = [Nombre, Direccion, telefono]

print(f'Los datos personales son:  {datos[0]} {datos[1]} {datos[2]}')
#########################################################################
"""
##media aritmetica########################################################

n1 = int(input('numero uno: '))
n2 = int(input('numero dos: '))
n3 = int(input('numero tres: '))

media = (n1 + n2 + n3) / 3

print(f'La media aritmetica es: \n{media}')






