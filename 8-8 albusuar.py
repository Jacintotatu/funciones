"""
def hacer_album(artista, album, canciones = None):
    
    disco = {'artista': artista, 'cd': album}
    if canciones:
        disco['canciones'] = canciones
    return disco

while True:
    print('\nDime artistas y discos que te molen: ')
    print("(Pon 'q' para quitar esto.)")
    art = input('Artista: ')
    if art == 'q':
        break
    alb = input('Album: ')
    if alb == 'q':
        break
    num = int(input('numero de canciones: '))


    
    h_album = hacer_album(art, alb, num)
    print(h_album)
"""
def poderosos(heroe, grupo, editorial = None): #predefinimos el argumento editorial como None por si no lo keremos rellenar
    superheroe = {'nombre': heroe, 'equipo': grupo}
    if editorial:   #si se rellena....
        superheroe['editorial'] = editorial  #se añade a la lista
    return superheroe  #no tengo claro lo ke hace el return


while True:
    print('\nDime un superheroe y una editorial que te molen: ')
    print('(Pon "q" para quitar esto.)')
    her = input('Heroe: ')
    if her == 'q':
        break
    team = input('Equipo: ')
    if team == 'q':
        break
    edit = input('editorial: ')
    if edit == 'q':
        break


    power = poderosos(her, team, edit) #se crea una lista con los datos introducidos por el usuario
    print(power)




