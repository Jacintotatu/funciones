def make_car(marca, modelo, **extras):
    extras['marca'] = marca
    extras['modelo'] = modelo
    return extras

coche = make_car('Seat', 'Ibiza',color='Blanco', faros='Bombillas', comb='gasoil')

for c, v, in coche.items():
    print(c, ':', v)

print(coche)