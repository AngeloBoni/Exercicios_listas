matriz = []

for i in range (5):
    linha = []
    for j in range(5):
        linha = [0] * 5
    matriz.append(linha)

for i in range(5):
    for j in  range(5):
        if(i == j):
            matriz[i][j] = 1
        elif(5 - 1 - i == j):
            matriz[i][j] = 1

        if(j == 2 and i == 2):
            matriz[i][j] = 3

    print(matriz[i])