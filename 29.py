matriz = []

x = int(input("Quantas linhas tem a matriz?: "))
y = int(input("Quantas colunas tem a matriz?: "))

for i in range(y):
    linha = []
    for j in range(x):
        linha.append(int(input(f"Digite o valor da posição [{i}][{j}]:")))
    matriz.append(linha)



for i in range(len(matriz)):
    print(matriz[i])

soma = 0
somacoluna = []

for i in range(x):
    soma = 0
    for j in range(y):
        soma += matriz[j][i]
    print(f"Soma da {i + 1}ª coluna : {soma}")
    somacoluna.append(soma)

for i in range(len(matriz[0])):
    print(f"Média da {i + 1}ª coluna: {round(somacoluna[i] / x, 2)} ")