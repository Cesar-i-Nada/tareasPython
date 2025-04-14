lugares = [("NY", 25), ("LA", 20), ("FL", 30)]

nuevos_lugares = list(map(lambda c: (c[0], (9/5) * c[1] + 32), lugares))
print(nuevos_lugares)
