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