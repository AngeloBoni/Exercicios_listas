tupla = (1, 2, 3, 4, 5)
aux = []

for i in range(len(tupla) - 1, -1, -1):
    aux.append(tupla[i])

tupla = tuple(aux)

print(f"Tupla invertida:\n{tupla}")