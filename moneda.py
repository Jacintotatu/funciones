"""
Dado un saldo inicial, por ejemplo 100 puntos para ti y para la CPU, tienes que 
hacer apuestas contra la CPU hasta que uno de los dos se quede sin puntos o gane
el juego. 

En cada ronda apuestas una cantidad de puntos a ciegas y la CPU también. Luego 
se revela cuanto ha apostado cada uno y el que ha apostado más gana la ronda y 
la moneda se mueve hacia su lado en un tablero de 7 posiciones. 

Si la moneda llega a una esquina (casilla J1 o J2 ) ese jugador gana la partida.
También puede perder la partida el jugador que antes se quede sin puntos para 
apostar.

Una forma de visualizar el juego es mediante el dibujo de un tablero ascii que 
muestra como queda en cada ronda:
[  ][  ][  ][ O ][  ][  ][  ]  # la moneda empieza en el centro

"""
import random
from collections import deque
#empezamos con 100 puntos cada uno
j1 = 100
j2 = 100

tablero = deque([[ ], [ ], [ ], ['💰'], [ ], [ ], [ ]]) #tablero con el modulo deque para poder usar rotate()

while j1 > 0 and j2 > 0:  #mientras que los puntos que tenemos no sean menores que 0
    #apuestas generadas automaticamente
    j1_apuesta = random.randint(0, j1)
    j2_apuesta = random.randint(0, j2)
    #la apuesta automatica se resta a los puntos que teniamos al principio
    j1-=j1_apuesta
    j2-=j2_apuesta

    if j1_apuesta > j2_apuesta:  #si la apuesta j1 es mayor que la de j2 la moneda se corre un lugar hacia la izquierda
        tablero.rotate(-1)
    elif j1_apuesta < j2_apuesta:   #si la apuesta j2 es mayor que la de j1 la moneda se corre un lugar hacia la derecha
        tablero.rotate(1)
    if j1<=0:  #si j1 se queda sin puntos
        print('\nJ1 PIERDE, GANA J2')
        break
    elif j2<=0: #si j2 se queda sin puntos
        print('\nJ2 PIERDE, GANA J1')
        break
    if tablero == deque([['💰'], [ ], [ ], [ ], [ ], [ ], [ ]]): #si la moneda llega a la izquierda
        print('\n¡¡¡El jugador 1 gana!!!')
        break
    elif tablero == deque([[ ], [ ], [ ], [ ], [ ], [ ], ['💰']]): #si la moneda llega a la derecha
        print('\n¡¡¡El jugador 2 gana!!!')
        break

    print(f'\nApuestas: J1: {j1_apuesta} <-> J2: {j2_apuesta}')
    print(f'Puntos restantes J1: {j1} <-> J2: {j2}')  
    for i in tablero:   #dibujar tablero
        print(i, end=" ")

print(f'J1: {j1_apuesta} <-> J2: {j2_apuesta}')
for i in tablero:   
    print(i, end=" ")



