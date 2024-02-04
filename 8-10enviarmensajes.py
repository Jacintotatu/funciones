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