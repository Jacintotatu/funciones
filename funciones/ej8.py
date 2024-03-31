"""
disco = {}

def hacer_album(artista, album, canciones=None):
    disco = {'artista' : artista, 'album' : album}

    if canciones:
        disco['Cancion']=can
    return disco

while True:
    print('Pon q para quitar esto.')
    disco['artista']=art
    art = input('Artista: ')
    if art == 'q':
        print('Adios')
        break
    alb = input('Album: ')
    disco['album']=alb
    if alb == 'q':
        print('Adios')
        break
    can = input('Canción: ')
    if can == 'q':
        print('Adios')
        break

    
lp = hacer_album(art, alb, can)

print(lp)
"""

def hacer_album(artista, album, canciones=None):
    disco = {'artista': artista, 'cd': album}
    if canciones:
        disco['canciones'] = canciones
    return disco

while True:
    artista = input("Introduce el nombre del artista (o escribe 'salir'): ")
    if artista.lower() == "salir":
        break
    album = input("Introduce el título del álbum: ")
    canciones = input("Introduce las canciones del álbum (separadas por comas): ")
    if canciones:
        canciones = canciones.split(",")
    album_creado = hacer_album(artista, album, canciones)
    print(f"\nÁlbum creado: {album_creado}")

print("¡Gracias por usar el creador de álbumes!")



    
    
    
    
    

