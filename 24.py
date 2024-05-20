matriz = []
somalinha = []
somacoluna = []

base = int(input("Quantas linhas tem a matriz?: "))
altura = int (input("Quantas colunas tem a matriz?: "))


for i in range(altura):
    lista = []
    soma = 0
    for j in range(base):
        lista.append(int(input(f"Digite o valor na posição[{i}][{j}]: " )))
        soma += lista[j]
    matriz.append(lista)
    somalinha.append(soma)

for i in range(altura):
    soma = 0
    for j in range(base):
        soma += matriz[j][i]
    somacoluna.append(soma)

print("Matriz criada:")

for linha in matriz:
    print(linha)

for i in range(len(somalinha)):
    print(f"Soma da {i + 1}ª linha: {somalinha[i]}")

for i in range(len(somacoluna)):
    print(f"Soma da {i + 1}ª Coluna: {somacoluna[i]}")