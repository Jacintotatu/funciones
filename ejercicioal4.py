"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y 
devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje
de IVA, deberá aplicar un 21%.
"""
def factura(bruto, iva = 21):
    """Función de aplica el IVA a una factura.
    Parametros
    bruto: Es la cantidad sin IVA
    iva: Es el porcentaje de IVA
    Devuelve el total de la factura una vez aplicado el IVA. 
    """
    return bruto + bruto * iva / 100

print(factura(1000, 10))

def horas(am):
    return am + 12
hora = int(input('Pon una hora: '))
print(f'Las {hora}:00 AM son las {horas(hora)}:00 PM')

