def enviar_mensajes(frases):
    for frase in frases:
        print(frase)
        mensajes_enviados.append(frase)
        mensajes.pop()


mensajes_enviados = []
mensajes = ['Hola amigo', 'Veste al peo', 'Camina ya', '6000 pesetas de wisky']
enviar_mensajes(mensajes)
print(mensajes_enviados)
print(mensajes)