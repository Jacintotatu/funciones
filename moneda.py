import random
from collections import deque
j1 = 100
j2 = 100
j1_apuesta = random.randint(0, 101)
j2_apuesta = random.randint(0, 101)
tablero = deque([[], [], [], [0], [], [], []])
while j1 > 0 and j2 > 0:
    j1-=j1_apuesta
    j2-=j2_apuesta

    j1_apuesta = random.randint(j1, 100)
    j2_apuesta = random.randint(j2, 100)



    if j1_apuesta > j2_apuesta:
        tablero.rotate(-1)
    elif j1_apuesta < j2_apuesta:
        tablero.rotate(1)
    elif j1==0:
        print('J1: YOU LOSE!!')
    elif j2==0:
        print('J2: YOU LOSE!!')
        

print(f'J1: {j1_apuesta} - J2: {j2_apuesta}')
print(j1, j2)    
for i in tablero:   
    print(i, end=" ")

