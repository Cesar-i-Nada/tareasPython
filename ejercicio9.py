lista_de_numeros = [2, -345, 908, -1, 234, -6754, 7262, -990, 6534, -3, 21]

positivos = filter(lambda x: x > 0, lista_de_numeros)

print("Los números positivos son: ", list(positivos))
