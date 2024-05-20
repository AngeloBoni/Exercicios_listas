lista = [1, 2, 3, 4, 5]
lista2 = []

for i in range(len(lista) - 1, -1, -1):
    lista2.append(lista[i])

print(f"Lista original: {lista}")
print(f"Lista invertida: {lista2}")