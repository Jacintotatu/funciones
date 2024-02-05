"""
def ciudad_pais (ciudad, pais):

    mundo = f'{ciudad}, {pais}' 
    return mundo.title()

ciudades = ciudad_pais('roma', 'italia')
print(ciudades)
ciudades = ciudad_pais('londres', 'inglaterra')
print(ciudades)
ciudades = ciudad_pais('atenas', 'grecia')
print(ciudades)
"""

def heroe(nombre, universo):
    superheroe = f'{nombre}, {universo}.'
    return superheroe.title()

heroes = heroe('ironman', 'marvel')
print(heroes)
heroes = heroe('blackwidow', 'marvel')
print(heroes)
heroes = heroe('flash', 'dc')
print(heroes)