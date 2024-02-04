mensajes = ['vaya mierda', 'me cago en to', 'joputa marrano', 'veste al peo',]
enviados = []
#esta funcion envia los mensajes ke hay en la lista 'mensajes'
def enviar_mensajes(mensajes, enviados):
    while mensajes:
        enviado = mensajes.pop() 
        enviados.append(enviado)   #mete en la lista 'enviados', los mensajes que va borrando de la lista 'mensajes'

#esta funcion imprime los mensajes enviados.
def mensajes_enviados(enviados):
    print('\nEstos mensajes han sido enviados: ')
    for enviado in enviados:
        print(enviado)


enviar_mensajes(mensajes[:], enviados) #copiamos los enviados otra vez en mensajes para tenerlos archivados.
mensajes_enviados(enviados)

print(mensajes)
print(enviados)