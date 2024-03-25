def hacer_album(artista, album, canciones=None):
    disco = {'artista' : artista, 'album' : album}

while True:
    art = input('Artista: ')
    disco['artista']=art
    alb = input('Album: ')
    disco['album']=alb
    can = input('Canciones: ')
    if canciones!=None:
        disco['Tracks']=canciones
    elif art == 'q' or alb == 'q' or can == 'q':
        break

    print(hacer_album(art, alb, can))

    
    
    
    
    

