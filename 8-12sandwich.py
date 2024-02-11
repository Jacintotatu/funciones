def sandwich(*ingredientes):
    print('El sandwich que has elegido lleva: ')
    for i in ingredientes:
        print(f'********************{i}')
    return ingredientes

sandwich('atun', 'lechuga', 'mayonesa')
sandwich('queso', 'tomate', 'alcaparras', 'anchoas')
sandwich('queso','salami','picante','chorizo','piña','carne')