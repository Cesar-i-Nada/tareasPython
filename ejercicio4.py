lista_de_numeros = [2, 345, 908, 1, 234, 6754, 7262, 990, 6534, 3, 21]

def ordenar(numero):
    return sorted(numero)

lista_de_numeros_ordenada = list(sorted(lista_de_numeros))
reverse = True
if reverse:
    lista_de_numeros_ordenada.reverse() 
print(lista_de_numeros_ordenada)