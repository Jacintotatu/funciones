def hacer_album(artista, album, canciones=None):
    disco = {'artista' : artista, 'album' : album}
    if canciones!=None:
        disco['Tracks']=canciones
    return disco

musica1 = hacer_album('El último de la fila', 'Astronomia razonable', 8)
musica2 = hacer_album('Metallica', 'Master of puppets')
musica3 = hacer_album('Toni el gitano', 'La cabra', 14)
print(musica1, musica2, musica3)