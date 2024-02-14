def TablaDeMultiplicar(n1, n2):
    return f'{str(n1)}x{str(n2)}={str(n1 * n2)}'
n = int(input('Ingrese un numero entero: '))
for i in range(0, 11):
    print(TablaDeMultiplicar(n, i))