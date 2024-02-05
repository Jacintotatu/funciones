"""
def hacer_album(artista, album, canciones = None):
    disco = {'artist': artista, 'cd': album}
    if canciones:
        disco['canciones'] = canciones
    return disco

musica = hacer_album('metallica', 'and justice for all')
print(musica)
musica = hacer_album('julio iglesias', 'bamboleo')
print(musica)
musica = hacer_album('manolo escobar', 'mi carro', 12)
print(musica)
"""

def poderosos(heroe, grupo, editorial = None): #predefinimos el argumento editorial como None por si no lo keremos rellenar
    superheroe = {'nombre': heroe, 'equipo': grupo}
    if editorial:   #si se rellena....
        superheroe['editorial'] = editorial  #se añade a la lista
    return superheroe

comics = poderosos('spiderman', 'vengadores', 'marvel')
print(comics)
comics = poderosos('lobezno', 'patrulla x')  #Aqui no lo he rellenado
print(comics)
comics = poderosos('Capi', 'vengadores', 'marvel')
print(comics)
comics = ('Batman', 'Justice League', 'DC')
print(comics)


