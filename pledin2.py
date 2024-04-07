"""Crea un programa que pida dos número enteros al usuario y diga si alguno de 
ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos 
números, y devuelve si el primero es múltiplo del segundo."""

def EsMultiplo(num1, num2):
    if num1%num2 == 0:
        return num1
    else:
        return 'no es multiplo'
    
num1=int(input('Numero 1: '))
num2=int(input('Numero 2: '))

print(EsMultiplo(num1, num2))