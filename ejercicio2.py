lista_de_numeros = [2, 345, 908, 1, 234, 6754, 7262, 990, 6534, 3, 21]

def triplicar(numero):
    return numero * 3

triplicar_numeros = list(map(triplicar, lista_de_numeros))
print(triplicar_numeros)