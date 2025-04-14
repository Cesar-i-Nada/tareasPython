palabras = ["carro", "casa", "sol", "trapo", "bicicleta", "electrocardiograma"]

def mayusculas(palabra):
    return palabra.upper()

palabras_mayusculas = list(map(mayusculas, palabras))
print(palabras_mayusculas)

