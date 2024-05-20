matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [6, 5, 6, 7]]

somaprincipal = 0
somasecundaria = 0

for i in matriz:
    print(i)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            somaprincipal += matriz[i][j]
        elif len(matriz[0]) - 1 - i == j:
            somasecundaria += matriz[i][j]

print(f"Soma da diagonal principal: {somaprincipal}")
print(f"Soma da diagonal secundária: {somasecundaria}")