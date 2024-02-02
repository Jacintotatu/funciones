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