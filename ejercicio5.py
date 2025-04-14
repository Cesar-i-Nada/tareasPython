diccionario_decimales = {}

diccionario_decimales = dict()

diccionario_decimales = {
    "primero": 4.9,
    "segundo": 2.1,
    "tercero": 3.87,
    "cuarto": 1.5,
    "quinto": 5.2,
    "sexto": 9.96,
    "sétimo": 8.11
}

diccionario_decimales_redondeados = dict(map(round, diccionario_decimales))

print(diccionario_decimales_redondeados)
