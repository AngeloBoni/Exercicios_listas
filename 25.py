matriz = [[2, 3, 4], [5, 6, 7], [8, 9 , 10]]

x = input("Que valor você quer substituir nos elementos da matriz? ")

print("Matriz original: ")

for i in matriz:
    print(i)

print(" ")

for i in range(len(matriz)):
    for j in range(len(matriz)):
        matriz[i][j] = x

for i in matriz:
    print(i)