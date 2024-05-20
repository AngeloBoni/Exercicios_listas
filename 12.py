lista = [1, 2, 2, 2, 3, 3, 3, 4, 5, 5]
aux = []

print("Lista original: " + str(lista))

for i in range(len(lista)):
    if(not(lista[i] in aux) ):
        aux.append(lista[i])

lista = aux

print("Lista Nova: " + str(lista))