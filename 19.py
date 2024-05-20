lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
aux = []

for i in lista:
    if i % 2 == 0:
        aux.append(i)
        
for i in lista:
    if not(i in aux):
        aux.append(i)

lista = aux

print(lista)