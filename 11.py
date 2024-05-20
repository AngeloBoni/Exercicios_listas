lista = [1, 2, 2, 2, 3, 3, 3, 4, 5, 5]

print("Lista: " + str(lista))

x = int(input("Qual elemento você gostaria de tirar da lista?: "))

for i in range(len(lista)):
    if lista[i] == x:
        lista[i] = "*"

print("Lista nova: " + str(lista))