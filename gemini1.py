"""

Ejercicio de funciones con argumentos y condicionales anidados
Descripción:

Escribe una función en Python que recibe dos números como argumentos y devuelve una calificación según el siguiente criterio:

Si la suma de los dos números es mayor o igual a 100, la función debe devolver "Excelente".
Si la suma de los dos números es mayor o igual a 80, la función debe devolver "Muy bien".
Si la suma de los dos números es mayor o igual a 60, la función debe devolver "Bien".
Si la suma de los dos números es menor que 60, la función debe devolver "Insuficiente".
Requisitos:

La función debe llamarse calificacion.
La función debe recibir dos argumentos: nota_1 y nota_2.
La función debe devolver una cadena con la calificación.
"""

def calificacion(nota_1, nota_2):
    if nota_1 + nota_2 >= 100:
        return 'Excelente'
    elif nota_1 + nota_2 >= 80:
        return 'Muy Bien'
    elif nota_1 + nota_2 >= 60:
        return 'Bien'
    else:
        return 'Insuficiente'
    
calificacion = calificacion(20, 50)
print(calificacion)


