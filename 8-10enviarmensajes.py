"""
mensajes = ['vaya mierda', 'me cago en to', 'joputa marrano', 'veste al peo',]
enviados = []

def enviar_mensajes(mensajes, enviados):
    while mensajes:
        enviado = mensajes.pop()
        enviados.append(enviado)
    
def mensajes_enviados(enviados):
    print('\nEstos mensajes han sido enviados: ')
    for enviado in enviados:
        print(enviado)


enviar_mensajes(mensajes, enviados)
mensajes_enviados(enviados)

print(mensajes)
print(enviados)
"""

tintas = ['roja', 'azul', 'negra', 'verde',]
gastadas = []

def colores(tintas, gastadas):
    while tintas:
        gastada = tintas.pop()
        gastadas.append(gastada)

def tintas_gastadas(gastadas):
    print('Estas tintas estan gastadas: ')
    for gastada in gastadas:
        print(f'· {gastada.title()}')

colores(tintas[:], gastadas)
tintas_gastadas(gastadas)


print(tintas)
print(gastadas)
