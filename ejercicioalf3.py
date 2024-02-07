#Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(numero):
    tmp = 1
    for i in range(numero):
        tmp *= i + 1
    return tmp

print(factorial(5))
print(factorial(10))
