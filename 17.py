lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
aux = []
print("Lista inicial: " + str(lista))

for i in range(0, len(lista), 1):
    if not(lista[i] % 2 != 0):
        aux.append(lista[i])

lista = aux

print("Lista final: " + str(lista))