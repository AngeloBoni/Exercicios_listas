lista = [1, 3, 5, 7, 9, 2, 4, 6, 8]
lista.sort()

print("Lista inicial: " + str(lista))

alternada = []

for i in range(1, len(lista)):
    vatual = lista[i]
    j = i - 1
    while j >= 0 and vatual < lista[j]:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = vatual

while lista:
    if lista:
        alternada.append(lista.pop())
    if lista:
        alternada.append(lista.pop(0))

lista = alternada
print("Lista modificada: " + str(lista))