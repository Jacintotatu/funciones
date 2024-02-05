"""
def describir_ciudad(nombre, pais = 'Alemania'):
    print(f'{nombre.title()} está en {pais.title()}.')

describir_ciudad('berlin')
describir_ciudad('frankfurt')
describir_ciudad('madrid', 'españa')
"""
def superheroe(nombre, editorial = 'Marvel'):
    print(f'{nombre} sale en los comics de {editorial}.')

superheroe('spiderman')  #ponemos el argumento nombre y dejamos la ditorial predefinida
superheroe('Batman', 'DC')  #cambiamos los dos argumentos
superheroe('Thor')  #ponemos el argumento nombre
superheroe(editorial = 'DC', nombre = 'Superman') #ponemos los argumentos cambiados pero como ponemos la variable no pasa nada.



