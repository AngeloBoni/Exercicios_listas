import random

x = int(input("Quantas colunas terá a matriz? "))
y = int(input("Quantas linhas terá a matriz? "))

matriz = []
soma = 0

print("A matriz aleatória gerada foi: ")
for i in range(x):
    linha = []
    for j in range(y):
        linha.append(random.randint(1, 9))
    matriz.append(linha)
    print(matriz[i])

for i in range(x):
    for j in range(y):
       soma = soma + matriz[i][j]

media = soma / (x * y)

print("A soma os números dessa matriz é: " + str(soma))
print("A média dos números dessa matriz é: " + str(round(media, 2)))