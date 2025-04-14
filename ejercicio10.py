perfiles = [("Juan", 25), ("Ana", 20), ("Luis", 30)]

edades_ordenadas = sorted(perfiles, key=lambda edad: edad[0])
print(edades_ordenadas)
