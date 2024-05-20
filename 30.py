lista1 = [int(input(f"Digite o {i+1}º valor da 1ª lista: ")) for i in range(3)]
lista2 = [int(input(f"Digite o {i+1}º valor da 2ª lista: ")) for i in range(3)]
aux = []

print("Valor da primeira lista: " + str(lista1))
print("Valor da segunda lista: " + str(lista2))

for numero in lista1:
    if not(numero in lista2) and  not(numero in aux):
        aux.append(numero)

for numero in lista2:
    if not(numero in lista1) and  not(numero in aux):
        aux.append(numero)

print(aux)