def mensajes(frases, mensajes_enviados):
    while frases:
        current_frase = frases.pop()
        print(f'Enviando:  {current_frase}')
        mensajes_enviados.append(current_frase)

def mostrar_mensajes_enviados(mensajes_enviados):
    print('\nEstos mensajes han sido enviados: ')
    for mensaje_enviado in mensajes_enviados:
        print(mensaje_enviado)

frases = ['Hola amigo', 'Veste al peo', 'Camina ya', '6000 pesetas de wisky']
mensajes_enviados = []

print(mensajes(frases, mensajes_enviados))
print(mostrar_mensajes_enviados(mensajes_enviados))
print(frases)
print(mensajes_enviados)