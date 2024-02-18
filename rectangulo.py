def rectangulo(anchura, altura):
    for i in range(altura):
        for j in range(anchura):
            print(caracter, end=" ")
        print()
    
anchura=int(input('Anchura del rectángulo: '))
altura=int(input('Altura del rectángulo: '))
caracter=input('Que simbolo?: ')
rectangulo(anchura, altura)