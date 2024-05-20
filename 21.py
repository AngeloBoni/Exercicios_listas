entrada = input("Digite os números da5 tupla separados por vírgula: ")
elementos = entrada.split(",")
tupla = tuple(int(elemento.strip()) for elemento in elementos)

aux = []
aux1 = []

for i in tupla:
    if i % 2 == 0:
        aux.append(i)
    else:
        aux1.append(i)

pares = tuple(aux)
impares = tuple(aux1)

print(f"Os números pares são: {pares}")
print(f"Os números ímpares são: {impares}")