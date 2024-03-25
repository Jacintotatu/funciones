def capullo(num1, num2):

    return f'{num1} + {num2} = {num1+num2}'

n = int(input('Pon un numero: '))

for i in range(1, 11):

    print(capullo(n, i))


