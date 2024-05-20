lista = [1, 3, 2, 2, 6, 3, 2, 4, 5, 5]

x = input("Deseja a lista em ordem crescente ou decrescente?: (C/D) ")
x = x.lower()

print("Lista original:", lista)

for i in range(1, len(lista)):
    vatual = lista[i]
    j = i - 1
    if x == "c":
        while j >= 0 and vatual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
    elif x == "d":
        while j >= 0 and vatual > lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
    lista[j + 1] = vatual

print("Lista ordenada:", lista)