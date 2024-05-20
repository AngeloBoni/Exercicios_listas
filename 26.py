matriz = []
cont = 0;

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite o valor na posição [{i}][{j}]: ")))
    matriz.append(linha)

print("Matriz: ")

for i in matriz:
    print(str(i))
tamanhomatriz = len(matriz) * len(matriz[0])
print("Tamanho da matriz: "+str(tamanhomatriz))

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] == 0:
            cont += 1
print(f"Número de zeros: {cont}")

if cont > tamanhomatriz/2:
    print("A matriz é esparsa")
else:
    print("A matriz não é esparsa")