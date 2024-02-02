def ciudad_pais (ciudad, pais):

    mundo = f'{ciudad}, {pais}' 
    return mundo.title()

ciudades = ciudad_pais('roma', 'italia')
print(ciudades)
ciudades = ciudad_pais('londres', 'inglaterra')
print(ciudades)
ciudades = ciudad_pais('atenas', 'grecia')
print(ciudades)