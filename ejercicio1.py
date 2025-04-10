lista_de_numeros = [2, 345, 908, 1, 234, 6754, 7262, 990, 6534, 3, 21]

def pares(numero):
    return numero % 2 == 0

pares_de_lista = list(filter(pares, lista_de_numeros))
print(pares_de_lista)
