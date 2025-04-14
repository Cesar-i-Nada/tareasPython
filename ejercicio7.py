palabras = ["carro", "casa", "sol", "trapo", "bicicleta", "electrocardiograma"]

def menos_de_cinco(palabra):
    return len(palabra) < 5

menos_de_cinco = True
if menos_de_cinco:
    palabra = list(filter(menos_de_cinco, palabras))
else:
    palabras = list(map(menos_de_cinco,palabras))
    
    print(palabras)
    

    

        

    