import random

from random import randint
j1 = 100
j2 = 100

j1_apuesta = random.randint(0, 101)
j2_apuesta = random.randint(0, 101)

j1 -= j1_apuesta
j2 -= j2_apuesta

tablero = [[], [], [], [0], [], [], []]

if j1_apuesta > j2_apuesta:
    del tablero [3]
    tablero.insert(2, 0)
else:
    del tablero [3]
    tablero.insert(4, 0)

print(j1_apuesta, j2_apuesta)
print(tablero)