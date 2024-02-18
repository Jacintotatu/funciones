
def triangulo_1(anchura):
    for i in range(1, anchura + 1):
        for j in range(i):
            print("* ", end="")
        print()

def triangulo_2(anchura):
    for i in range(1, anchura):
        for j in range(anchura - i):
            print("* ", end="")
        print()

anchura = int(input("Anchura del triángulo: "))
for i in range(anchura, 0, -1):
    triangulo_1(i)
    triangulo_2(i)