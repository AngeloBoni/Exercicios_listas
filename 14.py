lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 5, 6, 8, 1]
lista3 = []
##Esperado = 3, 4, 6, 8

for i in range(len(lista1)):
    if not (lista1[i] in lista2):
        lista3.append(lista1[i])
for i in range(len(lista2)):
    if not (lista2[i] in lista1):
        lista3.append(lista2[i])

print(lista3)