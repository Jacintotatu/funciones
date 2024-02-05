"""
def hacer_camiseta(texto = 'Me encanta Python', talla = 'XXXL'):
    print(f'Camiseta encargada de la talla {talla} con la palabra {texto}.')

hacer_camiseta('Calimero', 'XL')
hacer_camiseta(talla = 'XS')
hacer_camiseta()
"""

def hacer_cartel(tamaño = 'A4', texto = 'Pk lo digo yo'):  #argumentos predefinidos
    print(f'Cartel de tamaño {tamaño} y con el texto {texto}.')

hacer_cartel(texto ='"Viva yo"')  #tamaño predefinido
hacer_cartel('A3', '"La maté por que era mia"')
hacer_cartel()  #argumentos predefinidos
hacer_cartel('A5', 'A quien no le va a gustar?')
hacer_cartel(texto = 'Vale ya') #tamaño predefinido
hacer_cartel(tamaño = 'A2')  #texto predefinido