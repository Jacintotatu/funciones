"""
Resuelva de nuevo el ejercicio "if ... elif ... else ... 6" de manera que el 
cálculo lo realice una función que reciba un parámetro (el año) y devuelva True
 o False según que el año sea o no bisiesto.

El enunciado del ejercicio era:
Escriba un programa que pida un año y que escriba si es bisiesto o no.

Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100
 no lo son, aunque los múltiplos de 400 sí.

Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es 
bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
"""

print("COMPROBADOR DE AÑOS BISIESTOS")

def año_bisiesto(año):
    return año % 400 == 0 or (año % 100 != 0 and año % 4 == 0)
fecha = int(input("Escriba un año y le diré si es bisiesto: "))

if año_bisiesto(fecha):
    print(f"El año {fecha} es un año bisiesto.")
else:
    print(f"El año {fecha} no es un año bisiesto.")

año_bisiesto(fecha)
